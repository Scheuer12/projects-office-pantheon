#!/usr/bin/env python3
"""
scan_transcricao.py — primeira passada MECÂNICA do índice de desconexão da call.

Lê a transcrição e devolve todas as ocorrências das frases-gatilho de desconexão
(`[INTERNAL_API_METHOD]` abaixo, ou um arquivo próprio via --keywords), cada uma com o
trecho de contexto ao redor e uma estimativa de timestamp/posição na call.

Isto é só o CANDIDATO — não decide sozinho se é desconexão de verdade. "Isso é com o
[EXTERNAL_SYSTEM]" pode ser setup ([TASK_CODE] — dados de acesso ao [EXTERNAL_SYSTEM]) ou fuga de foco. Só o cruzamento
com tarefas_<cliente>.json e a leitura do contexto decide — ver references/desconexao.md.
A lista de frases não é exaustiva: releia o restante da transcrição em busca de trechos
fora de foco que não bateram em nenhuma frase.

Uso:
    python3 scan_transcricao.py transcricao.txt [--keywords palavras.json] \\
        [--duracao-min 60] [--contexto 220] -o candidatos.json
"""
import sys
import re
import json
import argparse

DEFAULT_KEYWORDS = {
    "Encaminhamento para sistema/área fora do [DOMAIN_PRODUCT]": [
        "isso é com o [EXTERNAL_SYSTEM]", "isso é do [EXTERNAL_SYSTEM]", "isso é do financeiro", "isso é do fiscal",
        "isso é do comercial", "isso não é do [DOMAIN_PRODUCT]", "isso é do sistema de faturamento",
        "vamos aguardar resposta do [EXTERNAL_SYSTEM]", "vamos aguardar retorno do [EXTERNAL_SYSTEM]",
        "isso é com o time de ti", "isso é com o suporte do [EXTERNAL_SYSTEM]",
    ],
    "Sinalização explícita de fuga de foco": [
        "estamos perdendo o foco", "vamos focar no que interessa", "voltando ao assunto",
        "isso não é da [VALIDATION_STAGE]", "isso não é do setup", "isso foge do escopo",
        "saindo do assunto", "fugindo do ponto", "vamos manter o foco na [VALIDATION_STAGE]",
        "vamos manter o foco no setup", "isso é da [VALIDATION_STAGE]", "isso é uat",
        "vamos testar o cenário", "isso é project-client-8 não cadastro",
    ],
    "Encerramento/interrupção da call": [
        "vou cancelar aqui", "vamos remarcar", "vamos encerrar por aqui",
        "preciso sair mais cedo", "vamos parar por aqui", "vou ter que sair",
        "podemos retomar depois",
    ],
    "Fora do To-Be / requisito não previsto": [
        "não está no to-be", "não estava no to-be", "isso não estava previsto",
        "isso é um requisito novo", "isso não faz parte do que foi assinado",
        "isso não foi definido no to-be", "isso não estava no escopo do projeto",
    ],
    "Repetição / assunto já decidido": [
        "já discutimos isso", "isso já tinha ficado definido", "voltamos nesse assunto de novo",
        "já validamos isso antes", "isso já foi decidido", "já cadastramos isso",
    ],
    "Dependência externa travando o setup": [
        "depende do fornecedor", "depende do time de ti", "sem isso não conseguimos avançar",
        "vamos aguardar posição do fornecedor", "estamos travados nesse ponto",
        "ainda não recebemos as credenciais", "layout ainda não está definido",
    ],
    "Abertura/encerramento social (saudação sem conteúdo de setup)": [
        "bom dia a todos", "bom dia pessoal", "boa tarde a todos", "boa tarde pessoal",
        "boa noite a todos", "tudo bem com vocês", "tudo bem pessoal", "como vocês estão",
        "conseguem me ouvir", "estão me ouvindo", "consegue me ver", "vamos começar",
        "podemos começar", "então pessoal", "vamos iniciar a call", "muito obrigado a todos",
        "obrigado pela reunião", "obrigado pela call", "agradeço a presença", "então é isso",
        "por hoje é isso", "por hoje ficamos nisso", "vamos finalizar por aqui",
        "tenham uma boa tarde", "tenham um bom dia", "até a próxima",
        "até a próxima call", "nos falamos amanhã", "qualquer coisa me chama",
        "fico à disposição", "um abraço pessoal",
    ],
}

# Mapa de flexibilização: cada caractere-base pode aparecer acentuado na transcrição real
# (transcrições automáticas variam muito nisso). Constrói uma classe de caracteres para
# casar "e" com "e/é/ê", "to-be" com "to-be/tobe", etc., sem depender de normalizar unicode
# e perder o offset original do texto (importante para o trecho de contexto).
_FLEX = {
    "a": "[aàáâã]", "e": "[eèéê]", "i": "[iìíî]", "o": "[oòóôõ]", "u": "[uùúû]",
    "c": "[cç]",
}


def flex_pattern(phrase):
    """Escapa a frase e substitui letras por classes de caracteres tolerantes a acento,
    além de tratar hífen/espaço como equivalentes e permitir espaçamento duplo."""
    out = []
    for ch in phrase.lower():
        if ch in _FLEX:
            out.append(_FLEX[ch])
        elif ch in (" ", "-"):
            out.append(r"[\s-]+")
        else:
            out.append(re.escape(ch))
    return "".join(out)


# Timestamp no início da linha: "[00:12:34]", "00:12:34 -->", "00:12:34 Nome:", etc.
TS_RE = re.compile(r"^\s*\[?(\d{1,2}):(\d{2})(?::(\d{2}))?\]?")


def parse_ts_to_min(m):
    parts = [int(g) for g in m.groups() if g is not None]
    if len(parts) == 3:
        h, mi, s = parts
    elif len(parts) == 2:
        h, mi, s = 0, parts[0], parts[1]
    else:
        return None
    return h * 60 + mi + s / 60.0


def build_context(text, start, end, radius):
    lo = max(0, start - radius)
    hi = min(len(text), end + radius)
    prefix = "…" if lo > 0 else ""
    suffix = "…" if hi < len(text) else ""
    return prefix + text[lo:hi].replace("\n", " ").strip() + suffix


def scan(text, keywords, radius, duracao_min):
    # Mapa: offset de caractere -> minuto estimado, construído varrendo linha a linha e
    # carregando o último timestamp visto (cursor). Isso permite localizar cada match no
    # tempo real da call quando a transcrição tem marcação de horário.
    line_starts = []
    offset = 0
    ts_cursor = None
    any_ts_found = False
    for line in text.splitlines(keepends=True):
        m = TS_RE.match(line)
        if m:
            parsed = parse_ts_to_min(m)
            if parsed is not None:
                ts_cursor = parsed
                any_ts_found = True
        line_starts.append((offset, ts_cursor))
        offset += len(line)
    total_chars = max(len(text), 1)

    def estimate_minute(char_offset):
        # timestamp da última linha com marcação de horário que precede o offset
        ts = None
        for start_off, cursor in line_starts:
            if start_off <= char_offset:
                ts = cursor
            else:
                break
        if ts is not None:
            return round(ts, 2), "timestamp_transcricao"
        if duracao_min:
            rel = char_offset / total_chars
            return round(duracao_min * rel, 2), "posicao_relativa_no_texto"
        return None, "sem_referencia_de_tempo"

    candidatos = []
    for categoria, frases in keywords.items():
        for frase in frases:
            pattern = flex_pattern(frase)
            for m in re.finditer(pattern, text, flags=re.IGNORECASE):
                minuto, fonte_estimativa = estimate_minute(m.start())
                linha_num = text.count("\n", 0, m.start()) + 1
                candidatos.append({
                    "categoria": categoria,
                    "frase_gatilho": frase,
                    "trecho_encontrado": m.group(0),
                    "contexto": build_context(text, m.start(), m.end(), radius),
                    "linha": linha_num,
                    "minuto_estimado": minuto,
                    "fonte_estimativa_tempo": fonte_estimativa,
                })
    candidatos.sort(key=lambda c: (c["minuto_estimado"] is None, c["minuto_estimado"] or 0, c["linha"]))
    return candidatos, any_ts_found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("transcricao", help="Caminho do arquivo de transcrição (texto puro)")
    ap.add_argument("--keywords", help="JSON próprio de palavras-chave (mesmo formato de DEFAULT_KEYWORDS); default usa a lista bundled")
    ap.add_argument("--duracao-min", type=float, default=None, help="Duração total da call em minutos, usada como fallback quando não há timestamp na transcrição")
    ap.add_argument("--contexto", type=int, default=220, help="Tamanho (em caracteres) da janela de contexto ao redor de cada match")
    ap.add_argument("-o", "--out", default=None, help="Onde salvar o JSON de candidatos (default: stdout)")
    args = ap.parse_args()

    with open(args.transcricao, encoding="utf-8") as f:
        text = f.read()

    keywords = DEFAULT_KEYWORDS
    if args.keywords:
        with open(args.keywords, encoding="utf-8") as f:
            keywords = json.load(f)

    candidatos, any_ts_found = scan(text, keywords, args.contexto, args.duracao_min)

    resultado = {
        "total_candidatos": len(candidatos),
        "transcricao_tem_timestamps": any_ts_found,
        "candidatos": candidatos,
    }
    if not any_ts_found and not args.duracao_min:
        print(
            "AVISO: a transcrição não parece ter timestamps e --duracao-min não foi "
            "informado — 'minuto_estimado' virá nulo para todos os candidatos. Informe "
            "--duracao-min para pelo menos ter uma estimativa por posição relativa no "
            "texto.",
            file=sys.stderr,
        )

    out = json.dumps(resultado, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"OK: {len(candidatos)} candidato(s) salvos em {args.out}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
