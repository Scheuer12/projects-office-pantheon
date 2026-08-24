#!/usr/bin/env python3
"""
cruzar_topicos.py — segunda passada MECÂNICA do índice de desconexão da call de SETUP.

Para cada candidato de scan_transcricao.py, procura a tarefa (Txx), o subitem (Txx.NN)
ou o ponto de atenção do Plano de Setup cujo texto mais se parece com o contexto da
frase-gatilho.

Isto é um SINAL, não o veredito. Score baixo aumenta a chance de o trecho ser desconexão
(assunto fora das 25 tarefas / To-Be de cadastro). Score alto não prova que está no foco
— duas palavras em comum podem ser coincidência. Leia o contexto sempre (ver
references/desconexao.md).

Uso:
    python3 cruzar_topicos.py candidatos.json tarefas_<cliente>.json -o candidatos_cruzados.json
"""
import sys
import re
import json
import argparse

STOPWORDS = set(
    "de da do das dos e a o as os para com sem que não nao uma um no na em ao se ou "
    "por como quando isso essa esse aqui ali hoje agora vamos seguir padrao guia "
    "sem detalhamento especifico cliente".split()
)


def keywords(text):
    words = re.findall(r"[a-zà-ú0-9]{4,}", (text or "").lower())
    return set(w for w in words if w not in STOPWORDS)


def best_match(context_kw, items, text_fn, code_fn, name_fn):
    best, best_score = None, 0
    for item in items:
        kw = keywords(text_fn(item))
        score = len(context_kw & kw)
        if score > best_score:
            best, best_score = item, score
    if best is None or best_score == 0:
        return None
    return {"codigo": code_fn(best), "nome": name_fn(best), "score_sobreposicao": best_score}


def tarefa_text(t):
    return " ".join([
        t.get("codigo", ""), t.get("nome", ""), t.get("recurso", ""),
        t.get("rastreabilidade", ""),
    ])


def subitem_text(s, tarefa_nome=""):
    return " ".join([
        s.get("codigo", ""), tarefa_nome, s.get("texto", ""),
        s.get("observacoes_execucao", ""),
    ])


def ponto_text(p):
    return " ".join([p.get("codigo", ""), p.get("texto", ""), p.get("plano_de_acao", "")])


def flatten_subitens(tarefas):
    out = []
    for t in tarefas:
        nome = t.get("nome", "")
        for s in t.get("subitens", []):
            item = dict(s)
            item["_tarefa_nome"] = nome
            out.append(item)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("candidatos", help="JSON gerado por scan_transcricao.py")
    ap.add_argument("tarefas", help="tarefas_<cliente>.json (formato parse_tarefas.py)")
    ap.add_argument("--threshold", type=int, default=2, help="Score mínimo para 'relacionado ao setup' (default: 2)")
    ap.add_argument("-o", "--out", default=None, help="Onde salvar o resultado (default: stdout)")
    args = ap.parse_args()

    with open(args.candidatos, encoding="utf-8") as f:
        cand_data = json.load(f)
    with open(args.tarefas, encoding="utf-8") as f:
        tarefas_data = json.load(f)

    tarefas = tarefas_data.get("tarefas", [])
    subitens = flatten_subitens(tarefas)
    pontos = tarefas_data.get("pontos_atencao", [])

    for cand in cand_data.get("candidatos", []):
        ctx_kw = keywords(cand.get("contexto", ""))
        tar_match = best_match(ctx_kw, tarefas, tarefa_text, lambda t: t["codigo"], lambda t: t["nome"])
        sub_match = best_match(
            ctx_kw, subitens,
            lambda s: subitem_text(s, s.get("_tarefa_nome", "")),
            lambda s: s["codigo"],
            lambda s: s.get("texto", "")[:80],
        )
        pt_match = best_match(ctx_kw, pontos, ponto_text, lambda p: p["codigo"], lambda p: p.get("texto", "")[:60])

        melhor_score = max(
            (tar_match or {}).get("score_sobreposicao", 0),
            (sub_match or {}).get("score_sobreposicao", 0),
            (pt_match or {}).get("score_sobreposicao", 0),
        )
        cand["tarefa_relacionada"] = tar_match
        cand["subitem_relacionado"] = sub_match
        cand["ponto_atencao_relacionado"] = pt_match
        if melhor_score == 0:
            sinal = "sem_correspondencia_lexical_com_o_setup"
        elif melhor_score < args.threshold:
            sinal = "correspondencia_fraca_leia_o_contexto"
        else:
            sinal = "correspondencia_moderada_ou_forte_ainda_assim_leia_o_contexto"
        cand["sinal_pertinencia"] = sinal

    out = json.dumps(cand_data, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"OK: candidatos cruzados salvos em {args.out}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
