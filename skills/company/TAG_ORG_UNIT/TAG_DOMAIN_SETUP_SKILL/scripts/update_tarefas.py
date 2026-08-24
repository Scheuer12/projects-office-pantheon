#!/usr/bin/env python3
"""Atualiza o JSON "vivo" de tarefas com o resultado de uma call de acompanhamento de
setup. Trabalha no nivel de SUBITEM (ex. "[TASK_CODE].01"), nao no nivel da tarefa inteira --
cada subitem tem seu proprio status, porque e nesse nivel que o setup de fato acontece
(um [DOMAIN_ENTITY] pode estar cadastrado enquanto outro ainda nao).

Uso:
    python3 update_tarefas.py tarefas_<cliente>.json update_<data>.json tarefas_<cliente>.json

(passar o mesmo caminho de entrada e saida sobrescreve o arquivo no lugar -- e assim que
o "documento" vive; se preferir manter historico de versoes, salve com sufixo de data)

Formato do update_<data>.json:
{
  "resultados": [
    {"codigo": "[TASK_CODE].01", "status": "CONCLUIDA", "data_execucao": "10/07/2026",
     "observacoes": "[DOMAIN_ENTITY] [CLIENT_NAME_1_UNIT_1] cadastrado e validado."}
  ],
  "novos_pontos_atencao": [
    {"texto": "...", "impacto_pct": 60, "plano_de_acao": "..."}
  ],
  "conclusao_consultor": null
}

status esperado: "CONCLUIDA", "EM ANDAMENTO", "BLOQUEADA" ou "PENDENTE".
novos_pontos_atencao ganham codigo RISCOnn automaticamente, continuando a numeracao
dos pontos de atencao ja existentes no JSON (nunca reordena ou renumera os antigos).
conclusao_consultor so deve vir preenchido no dia de encerramento (todos os subitens
concluidos ou explicitamente descartados com o cliente) -- nos demais dias, null.
"""
import sys, json


def flatten_subitens(tarefas):
    by_codigo = {}
    for t in tarefas:
        for s in t["subitens"]:
            by_codigo[s["codigo"]] = s
    return by_codigo


def main():
    tarefas_in, update_path, tarefas_out = sys.argv[1:4]

    with open(tarefas_in, encoding="utf-8") as f:
        state = json.load(f)
    with open(update_path, encoding="utf-8") as f:
        update = json.load(f)

    by_codigo = flatten_subitens(state["tarefas"])
    nao_encontrados = []
    for r in update.get("resultados", []):
        s = by_codigo.get(r["codigo"])
        if s is None:
            nao_encontrados.append(r["codigo"])
            continue
        s["status"] = r.get("status", s["status"])
        s["data_execucao"] = r.get("data_execucao", s["data_execucao"])
        s["observacoes_execucao"] = r.get("observacoes", s["observacoes_execucao"])

    pontos = state.setdefault("pontos_atencao", [])
    proximo_idx = len(pontos) + 1
    for item in update.get("novos_pontos_atencao", []):
        pontos.append({
            "codigo": f"RISCO{proximo_idx:02d}",
            "texto": item["texto"],
            "impacto_pct": item.get("impacto_pct", 60),
            "plano_de_acao": item.get("plano_de_acao", "A combinar com o cliente."),
        })
        proximo_idx += 1

    conclusao = update.get("conclusao_consultor")
    if conclusao:
        state["conclusao_consultor"] = conclusao

    with open(tarefas_out, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    todos = list(by_codigo.values())
    total = len(todos)
    concluidas = sum(1 for s in todos if s["status"].upper().startswith("CONCLU"))
    bloqueadas = sum(1 for s in todos if s["status"].upper().startswith("BLOQ"))
    print(f"OK: {tarefas_out} | subitens concluidos={concluidas}/{total} | bloqueados={bloqueadas} | "
          f"novos_pontos={len(update.get('novos_pontos_atencao', []))} | "
          f"nao_encontrados={nao_encontrados or 'nenhum'}")


if __name__ == "__main__":
    main()
