#!/usr/bin/env python3
"""Le um markdown de tarefas de setup customizadas (uma por bloco '### Txx | Nome',
mais uma tabela opcional de Pontos de Atencao Iniciais) e devolve um JSON "vivo" --
esse mesmo JSON e o que sera atualizado a cada call (ver update_tarefas.py) e
renderizado em HTML a cada vez (ver build_setup_html.py).

Cada tarefa padrao (Txx) e "explodida" em SUBITENS -- um subitem por elemento concreto
que o To-Be do cliente revela para aquela tarefa (ex.: um subitem por [DOMAIN_ENTITY], por
[DOMAIN_LOCATION], por [EXTERNAL_SYSTEM]...). Isso e a mesma logica de "um cenario = um passo" do
homologacao-doc41: a tarefa continua sendo a unidade de AUTORIA (responsavel e recurso
de apoio sao escritos uma vez por tarefa), mas o subitem e a unidade de execucao/status
no documento final -- e o que permite ao consultor marcar "cadastro do [DOMAIN_ENTITY] [CLIENT_NAME_1_UNIT_1]"
como concluido sem que isso esconda que "cadastro do [DOMAIN_ENTITY] [CLIENT_NAME_1_UNIT_2]" ainda esta
pendente atras de um status agregado da tarefa inteira.

Formato de entrada esperado (um bloco por tarefa, na ordem do Guia padrão):

### [TASK_CODE] | Cadastros de [DOMAIN_ENTITIES]
Responsável: Cliente
Recurso de apoio: Vídeo: Cadastros - [EXTERNAL_URL]]/...
Rastreabilidade: To-Be [CLIENT_NAME_1_UNIT_2], página 2
SUBITENS:
1. Cadastrar [DOMAIN_ENTITY] [CLIENT_NAME_1_UNIT_1] — [BUSINESS_IDENTIFIER] próprio, [SYSTEM_LINKED] ao [EXTERNAL_SYSTEM] [EXTERNAL_SYSTEM_3], sujeito a [BUSINESS_RULE_1] e [BUSINESS_RULE_2] mínimo de 6 meses.
2. Cadastrar [DOMAIN_ENTITY] [CLIENT_NAME_1_UNIT_2] — operador logístico do grupo, [SYSTEM_LINKED] ao [EXTERNAL_SYSTEM] [EXTERNAL_SYSTEM_1].

... um bloco desses por tarefa ([TASK_CODE]..[TASK_CODE] ou o que for aplicável a este cliente) ...

Se uma tarefa não tem nada específico no To-Be, ainda assim escreva um SUBITENS com um
único item genérico (ex. "1. Seguir padrão do Guia (sem detalhamento específico do
To-Be).") -- a tarefa nunca fica sem pelo menos um subitem, e nunca é omitida.

## PONTOS DE ATENÇÃO INICIAIS

| # | Ponto de atenção | Impacto (0-5) | Plano de ação |
|---|---|---|---|
| 1 | Cliente ainda não definiu layout final do [DOMAIN_LOCATION] | 4 | Agendar reunião com arquitetura de processos antes do [TASK_CODE] |

(a tabela de Pontos de Atenção Iniciais é opcional -- nem todo kickoff já tem
bloqueios conhecidos. Pode vir vazia ou ser omitida.)

Uso:
    python3 parse_tarefas.py tarefas_<cliente>.md > tarefas_<cliente>.json
"""
import sys, re, json


LABELS = ["Responsável", "Recurso de apoio", "Rastreabilidade", "SUBITENS"]

STEP_RE = re.compile(r"^\s*(\d+)\.\s*(.+)$")


def section(label, block, next_labels):
    pat = rf"{label}:\s*\n?(.*?)(?=\n(?:{'|'.join(next_labels)}):|\n##\s|\Z)"
    m = re.search(pat, block, re.S)
    return m.group(1).strip() if m else ""


def parse_subitens(codigo, raw):
    subitens = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        m = STEP_RE.match(line)
        if not m:
            continue
        num = int(m.group(1))
        texto = m.group(2).strip()
        subitens.append({
            "codigo": f"{codigo}.{num:02d}",
            "texto": texto,
            "status": "PENDENTE",
            "data_execucao": "",
            "observacoes_execucao": "",
        })
    if not subitens:
        # fallback: nunca deixar uma tarefa sem nenhum subitem
        subitens.append({
            "codigo": f"{codigo}.01",
            "texto": "Seguir padrão do Guia (sem detalhamento específico do To-Be).",
            "status": "PENDENTE",
            "data_execucao": "",
            "observacoes_execucao": "",
        })
    return subitens


def parse_tarefas(md_text):
    blocks = re.split(r"\n(?=### )", md_text)
    tarefas = []
    for b in blocks:
        if not b.strip().startswith("### "):
            continue
        m = re.match(r"### (\S+)\s*\|\s*(.+)", b)
        if not m:
            continue
        codigo = m.group(1).strip()
        nome = m.group(2).splitlines()[0].strip()

        responsavel = section("Responsável", b, LABELS) or "Cliente"
        recurso = section("Recurso de apoio", b, LABELS)
        rastreabilidade = section("Rastreabilidade", b, LABELS)
        subitens_raw = section("SUBITENS", b, LABELS)

        tarefas.append({
            "codigo": codigo,
            "nome": nome,
            "responsavel": responsavel,
            "recurso": recurso,
            "rastreabilidade": rastreabilidade,
            "subitens": parse_subitens(codigo, subitens_raw),
        })
    return tarefas


def parse_pontos_atencao(md_text):
    m = re.search(r"PONTOS DE ATENÇÃO INICIAIS\s*\n\n\|(.*?)\n\n", md_text + "\n\n", re.S)
    if not m:
        return []
    table_text = m.group(1)
    rows = [r for r in table_text.splitlines() if r.strip().startswith("|")]
    if len(rows) < 1:
        return []
    data_rows = rows[1:]
    pontos = []
    idx = 0
    for r in data_rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= set("-: "):
            continue
        idx += 1
        impacto = 3
        for c in cells:
            cc = c.strip().replace("*", "")
            if cc in [str(n) for n in range(6)]:
                impacto = int(cc)
        texto = re.sub(r"\*\*(.*?)\*\*", r"\1", cells[1] if len(cells) > 1 else "").strip()
        plano = re.sub(r"\*\*(.*?)\*\*", r"\1", cells[-1]).strip()
        pontos.append({
            "codigo": f"RISCO{idx:02d}",
            "texto": texto,
            "impacto_pct": impacto * 20,
            "plano_de_acao": plano,
        })
    return pontos


if __name__ == "__main__":
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        text = f.read()
    tarefas = parse_tarefas(text)
    pontos = parse_pontos_atencao(text)
    print(json.dumps({"tarefas": tarefas, "pontos_atencao": pontos}, ensure_ascii=False, indent=2))
