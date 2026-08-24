#!/usr/bin/env python3
"""
compute_indice.py — última etapa MECÂNICA: soma os minutos de desconexão já CONFIRMADOS
(depois do julgamento do passo 2 do SKILL.md) e calcula a entrada final
{"data", "pct", "minutos"} que alimenta desconexao_<cliente>.json (o mesmo arquivo lido
por scripts/build_auxiliar.py da skill homologacao-doc41-auxiliar para o gráfico de
colunas).

Este script não decide o que é ou não desconexão — só faz a conta a partir do que já foi
classificado como confirmado, exatamente pelo mesmo motivo que build_auxiliar.py calcula
andamento_pct/pizza de risco a partir de resultados_<cliente>.json em vez de aceitar um
número digitado à mão: elimina divergência entre o índice e a soma real dos trechos
confirmados.

Entrada esperada (confirmados.json) — lista de trechos de desconexão CONFIRMADOS depois
da leitura do contexto e do cruzamento com o To-Be, cada um com a duração estimada em
minutos (direto, ou como início/fim):

    [
      {"motivo": "Discussão sobre módulo do [EXTERNAL_SYSTEM] sem relação com o cenário testado",
       "inicio_min": 12.0, "fim_min": 16.5},
      {"motivo": "Call encerrada 20 min antes do previsto por indisponibilidade do cliente",
       "minutos": 20}
    ]

Uso:
    python3 compute_indice.py confirmados.json --duracao-total-min 60 --data 13/08/2026 \\
        [--append desconexao_<cliente>.json]
"""
import sys
import json
import argparse


def segment_minutes(seg):
    if "minutos" in seg:
        return max(0.0, float(seg["minutos"]))
    inicio = seg.get("inicio_min")
    fim = seg.get("fim_min")
    if inicio is not None and fim is not None:
        return max(0.0, float(fim) - float(inicio))
    raise ValueError(f"Segmento sem 'minutos' nem 'inicio_min'/'fim_min': {seg}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("confirmados", help="JSON com a lista de trechos de desconexão já confirmados (ver formato acima)")
    ap.add_argument("--duracao-total-min", type=float, required=True, help="Duração total da call, em minutos")
    ap.add_argument("--data", required=True, help="Data da call no formato dd/mm/aaaa")
    ap.add_argument("--append", default=None, help="Caminho de desconexao_<cliente>.json para ACRESCENTAR a entrada do dia (nunca sobrescreve entradas anteriores)")
    args = ap.parse_args()

    with open(args.confirmados, encoding="utf-8") as f:
        confirmados = json.load(f)

    total_min = round(sum(segment_minutes(s) for s in confirmados), 1)
    pct = round(100 * total_min / args.duracao_total_min) if args.duracao_total_min else 0
    pct = max(0, min(100, pct))

    entrada = {"data": args.data, "pct": pct, "minutos": total_min}

    print(json.dumps(entrada, ensure_ascii=False, indent=2))
    print(
        f"\n{len(confirmados)} trecho(s) confirmado(s) somam {total_min} min de "
        f"{args.duracao_total_min} min totais da call ({pct}%).",
        file=sys.stderr,
    )

    if args.append:
        try:
            with open(args.append, encoding="utf-8") as f:
                historico = json.load(f)
        except FileNotFoundError:
            historico = []
        if any(h.get("data") == entrada["data"] for h in historico):
            print(
                f"AVISO: já existe uma entrada para {entrada['data']} em {args.append} — "
                f"nada foi escrito. Edite o arquivo manualmente se for uma correção "
                f"intencional do mesmo dia.",
                file=sys.stderr,
            )
        else:
            historico.append(entrada)
            with open(args.append, "w", encoding="utf-8") as f:
                json.dump(historico, f, ensure_ascii=False, indent=2)
            print(f"OK: entrada de {entrada['data']} acrescentada a {args.append}", file=sys.stderr)


if __name__ == "__main__":
    main()
