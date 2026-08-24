#!/usr/bin/env python3
"""Gera o Plano de Setup e Preparação Inicial em HTML de uma única página, no mesmo
estilo visual do DPO_auxiliar (painel do homologacao-doc41) -- mas aqui o HTML É o
documento principal da skill apoio-setup, não um painel interno secundário.

Regenera o arquivo inteiro a partir do JSON "vivo" de tarefas (ver parse_tarefas.py /
update_tarefas.py) toda vez que for chamado -- não edita HTML existente. Isso é seguro
porque todo o estado (status de cada subitem, pontos de atenção, conclusão do consultor)
mora no JSON, nunca no HTML.

A tabela principal é organizada por tarefa (Txx), com uma linha de cabeçalho de grupo
(nome da tarefa, responsável, recurso de apoio) seguida de uma linha por SUBITEM
(Txx.NN) -- é no subitem que o status realmente vive.

Uso:
    python3 build_setup_html.py tarefas_<cliente>.json "<Nome do Cliente>" \
        Plano_Setup_<Cliente>.html [progress.json]

progress.json (opcional, julgamento do consultor sobre a call do dia -- ver SKILL.md):
{
  "fase_texto": "Execução — Semana 2 de Setup",
  "status_texto": "Iniciado",
  "risco_atraso_texto": "...",
  "pendencias_cliente_texto": "..."
}
"""
import sys, json, html
from datetime import date

def esc(t):
    return html.escape(t or "")

def truncate(t, n):
    t = t or ""
    return t if len(t) <= n else t[:n-1].rsplit(" ", 1)[0] + "…"

def impact_color(pct):
    if pct >= 80: return "#dc2626"
    if pct >= 40: return "#ca8a04"
    if pct >= 20: return "#2563eb"
    return "#16a34a"

STATUS_BADGE = {
    "CONCLUIDA": ("#4ade80", "#1e293b"),
    "EM ANDAMENTO": ("#dbeafe", "#1e3a8a"),
    "BLOQUEADA": ("#fecaca", "#7f1d1d"),
    "PENDENTE": ("#f1f5f9", "#475569"),
}
STATUS_BADGE_FALLBACK = ("#e2e8f0", "#1e293b")

RESP_BADGE = {
    "CLIENTE": ("#fef9c3", "#854d0e"),
    "CONSULTOR": ("#dbeafe", "#1e3a8a"),
}

HEADER_STATUS_BADGE = {
    "AGUARDANDO INÍCIO": ("#ffffff", "#1e293b"),
    "INICIADO": ("#ffffff", "#1e293b"),
    "BLOQUEADO POR PENDÊNCIA DO CLIENTE": ("#fecaca", "#1e293b"),
    "BLOQUEADO POR AGENDA": ("#fecaca", "#1e293b"),
    "ATRASO CRÍTICO": ("#7f1d1d", "#ffffff"),
    "CONCLUÍDO PARCIALMENTE": ("#bbf7d0", "#7f1d1d"),
    "CONCLUÍDO": ("#4ade80", "#1e293b"),
}
HEADER_STATUS_BADGE_FALLBACK = ("#e2e8f0", "#1e293b")


def norm(s):
    return (s or "").strip().upper().replace("Ã", "A").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ç","C")


def status_badge_colors(status):
    key = norm(status)
    for k, v in STATUS_BADGE.items():
        if norm(k) == key:
            return v
    return STATUS_BADGE_FALLBACK


def header_status_colors(status_txt):
    return HEADER_STATUS_BADGE.get((status_txt or "").strip().upper(), HEADER_STATUS_BADGE_FALLBACK)


def build_html(cliente, tarefas, pontos_atencao, data_geracao, conclusao_consultor=None, progress=None):
    all_subitens = [s for t in tarefas for s in t["subitens"]]
    total = len(all_subitens)
    concluidas = [s for s in all_subitens if norm(s["status"]).startswith("CONCLU")]
    bloqueadas = [s for s in all_subitens if norm(s["status"]).startswith("BLOQ")]
    em_andamento = [s for s in all_subitens if norm(s["status"]).startswith("EM AND")]
    pendentes = [s for s in all_subitens if s not in concluidas and s not in bloqueadas and s not in em_andamento]
    andamento_pct = round(len(concluidas) / total * 100) if total else 0

    rows_tarefas = ""
    for t in tarefas:
        rbg, rfg = RESP_BADGE.get(norm(t["responsavel"]), ("#f1f5f9", "#475569"))
        rows_tarefas += (
            "<tr class='group-row'><td colspan='2'>"
            f"<strong>{esc(t['codigo'])}</strong> — {esc(t['nome'])}"
            "</td><td>"
            f"<span class='badge' style='background:{rbg};color:{rfg}'>{esc(t['responsavel'])}</span>"
            "</td><td colspan='3' style='color:#64748b;font-size:10.5px'>"
            f"{esc(truncate(t.get('recurso',''), 100))}"
            "</td></tr>\n"
        )
        for s in t["subitens"]:
            bg, fg = status_badge_colors(s["status"])
            obs = s.get("observacoes_execucao") or ""
            rows_tarefas += (
                "<tr><td style='white-space:nowrap;padding-left:18px'>{codigo}</td>"
                "<td>{texto}</td>"
                "<td></td>"
                "<td><span class='badge' style='background:{bg};color:{fg}'>{status}</span></td>"
                "<td style='white-space:nowrap'>{data}</td>"
                "<td>{obs}</td></tr>\n"
            ).format(
                codigo=esc(s["codigo"]), texto=esc(s["texto"]),
                bg=bg, fg=fg, status=esc(s["status"]),
                data=esc(s.get("data_execucao", "")),
                obs=esc(truncate(obs, 90)),
            )

    top_pontos = sorted(pontos_atencao, key=lambda x: -x["impacto_pct"])
    rows_pontos = ""
    for p in top_pontos:
        pct = p["impacto_pct"]
        color = impact_color(pct)
        rows_pontos += (
            "<tr><td>"
            f"<div style='font-weight:600;margin-bottom:1px'><span style='color:#1e293b;background:#f1f5f9;"
            f"border-radius:3px;padding:0 4px;font-size:10px;margin-right:5px'>{esc(p['codigo'])}</span>"
            f"{esc(p['texto'])}</div>"
            f"<div style='font-size:10px;color:#64748b'>{esc(p['plano_de_acao'])}</div>"
            "</td><td style='width:100px'>"
            f"<div style='display:flex;align-items:center;gap:5px'>"
            f"<div style='flex:1;background:#f1f5f9;border-radius:10px;height:8px;overflow:hidden'>"
            f"<div style='width:{pct}%;height:100%;background:{color};border-radius:10px'></div></div>"
            f"<span style='font-size:10px;font-weight:800;color:{color}'>{pct}%</span>"
            "</div></td></tr>\n"
        )
    if not rows_pontos:
        rows_pontos = "<tr><td colspan='2' style='color:#94a3b8;font-style:italic'>Nenhum ponto de atenção registrado até o momento.</td></tr>"

    progress = progress or {}
    fase_txt = progress.get("fase_texto", "Kickoff — Plano Inicial")
    status_txt = progress.get("status_texto", "Aguardando Início")
    status_bg, status_fg = header_status_colors(status_txt)
    risco_atraso_txt = progress.get("risco_atraso_texto",
        "N/A nesta versão — cronograma de execução ainda não iniciado. Este indicador passa a ser "
        "calculado a partir da 1ª atualização (ritmo de subitens concluídos/semana vs. prazo do setup).")
    pendencias_txt = progress.get("pendencias_cliente_texto",
        "N/A nesta versão — documento gerado a partir do To-Be, antes da 1ª call de acompanhamento.")

    conclusao_html = ""
    if conclusao_consultor:
        conclusao_html = (
            "<div class='card'><div class='card-header'>Conclusão do Consultor</div>"
            f"<div class='na-note' style='font-style:normal'>{esc(conclusao_consultor)}</div></div>"
        )

    html_out = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Plano de Setup — {esc(cliente)}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  :root {{
    --bg-row-alt:#f8fafc; --border:#e2e8f0; --text-primary:#1e293b; --text-secondary:#64748b;
    --header-bg:#1e293b; --section-title-bg:#f1f5f9;
  }}
  body {{ font-family:'Inter',system-ui,-apple-system,sans-serif; font-size:12.5px; color:var(--text-primary);
          background:#fff; width:210mm; margin:0 auto; padding:10px 14px; }}
  .header {{ background:var(--header-bg); color:#fff; border-radius:6px; padding:8px 14px; display:flex;
             align-items:center; justify-content:space-between; margin-bottom:8px; }}
  .header-title {{ font-size:15px; font-weight:700; letter-spacing:-0.3px; }}
  .header-sub {{ font-size:10.5px; color:#94a3b8; margin-top:1px; }}
  .header-meta {{ display:flex; gap:14px; align-items:center; flex-wrap:wrap; justify-content:flex-end; }}
  .header-meta span {{ font-size:10.5px; color:#cbd5e1; line-height:1.5; flex:0 0 auto; }}
  .header-meta strong {{ color:#fff; display:block; }}
  .status-badge {{ display:inline-block; padding:2px 7px; border-radius:4px; font-size:8.5px; line-height:1.25;
                   font-weight:700; border:1px solid rgba(0,0,0,0.12); white-space:normal; text-align:center;
                   max-width:210px; }}
  .card {{ border:1px solid var(--border); border-left:3px solid #1e293b; border-radius:6px; overflow:hidden; margin-bottom:8px; }}
  .card-header {{ background:var(--section-title-bg); padding:5px 11px; font-size:10.5px; font-weight:700;
                  color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.5px;
                  border-bottom:1px solid var(--border); }}
  .card.warn {{ border-left-color:#ca8a04; }}
  .card.na {{ border-left-color:#94a3b8; }}
  table {{ width:100%; border-collapse:collapse; }}
  th {{ background:#f8fafc; font-size:10px; font-weight:600; color:var(--text-secondary);
        text-transform:uppercase; letter-spacing:0.4px; padding:3px 10px; text-align:left; border-bottom:1px solid var(--border); }}
  td {{ padding:4px 10px; font-size:11.5px; color:var(--text-primary); border-bottom:1px solid var(--border);
        vertical-align:middle; line-height:1.3; }}
  tr:last-child td {{ border-bottom:none; }}
  tr:nth-child(even):not(.group-row) td {{ background:var(--bg-row-alt); }}
  tr.group-row td {{ background:#eef2f7 !important; font-size:11px; border-top:1px solid #cbd5e1; padding:5px 10px; }}
  .badge {{ display:inline-block; padding:2px 7px; border-radius:4px; font-size:10px; font-weight:700; white-space:nowrap; }}
  .grid-2col {{ display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:8px; }}
  .metric-box {{ text-align:center; padding:8px 6px; }}
  .metric-value {{ font-size:22px; font-weight:800; color:#1e293b; }}
  .metric-label {{ font-size:9.5px; color:#64748b; text-transform:uppercase; letter-spacing:0.4px; margin-top:1px; }}
  .na-note {{ padding:9px 12px; font-size:10.5px; color:#64748b; font-style:italic; }}
  .footer {{ text-align:center; font-size:9.5px; color:var(--text-secondary); padding-top:5px; border-top:1px solid var(--border); }}
  @media print {{ body {{ width:100%; padding:8px 10px; }} @page {{ size:A4; margin:8mm; }} }}
</style>
</head>
<body>

<div class="header">
  <div>
    <div class="header-title">Plano de Setup e Preparação Inicial</div>
    <div class="header-sub">Documento vivo &middot; Setup Inicial [DOMAIN_PRODUCT] [COMPANY_PRODUCT]</div>
  </div>
  <div class="header-meta">
    <span><strong>CLIENTE</strong>{esc(cliente)}</span>
    <span><strong>DATA</strong>{esc(data_geracao)}</span>
    <span><strong>FASE</strong>{esc(fase_txt)}</span>
    <span><strong>STATUS</strong><span class="status-badge" style="background:{status_bg};color:{status_fg}">{esc(status_txt)}</span></span>
  </div>
</div>

<div class="grid-2col">
  <div class="card">
    <div class="card-header">Andamento do Setup</div>
    <div style="display:flex">
      <div class="metric-box" style="flex:1"><div class="metric-value">{andamento_pct}%</div><div class="metric-label">Andamento</div></div>
      <div class="metric-box" style="flex:1"><div class="metric-value">{len(concluidas)}/{total}</div><div class="metric-label">Concluídos</div></div>
      <div class="metric-box" style="flex:1"><div class="metric-value">{len(bloqueadas)}</div><div class="metric-label">Bloqueados</div></div>
      <div class="metric-box" style="flex:1"><div class="metric-value">{len(pendentes)}</div><div class="metric-label">Pendentes</div></div>
    </div>
    <div class="na-note">{len(tarefas)} tarefas do Guia padrão, detalhadas em {total} subitens específicos deste cliente.</div>
  </div>
  <div class="card warn">
    <div class="card-header">Pontos de Atenção — Impacto no Setup (0–100%)</div>
    <table>
      <thead><tr><th>Ponto identificado</th><th>Impacto</th></tr></thead>
      <tbody>
        {rows_pontos}
      </tbody>
    </table>
  </div>
</div>

<div class="card">
  <div class="card-header">Plano de Setup — Tarefas ({len(tarefas)}) e Subitens ({total})</div>
  <table>
    <thead><tr><th>Código</th><th>Subitem</th><th>Responsável</th><th>Status</th><th>Data</th><th>Observações</th></tr></thead>
    <tbody>
      {rows_tarefas}
    </tbody>
  </table>
</div>

<div class="grid-2col">
  <div class="card na">
    <div class="card-header">Risco de Atraso vs. Cronograma</div>
    <div class="na-note">{esc(risco_atraso_txt)}</div>
  </div>
  <div class="card na">
    <div class="card-header">Pendências de Responsabilidade do Cliente</div>
    <div class="na-note">{esc(pendencias_txt)}</div>
  </div>
</div>

{conclusao_html}

<div class="footer">
  Gerado por Consultoria [DOMAIN_PRODUCT] [COMPANY_PRODUCT] &nbsp;&middot;&nbsp; Plano de Setup e Preparação Inicial &nbsp;&middot;&nbsp; {esc(data_geracao)}
</div>

</body>
</html>
"""
    return html_out


if __name__ == "__main__":
    tarefas_json_path, cliente, out_html_path = sys.argv[1:4]
    progress = None
    if len(sys.argv) > 4:
        with open(sys.argv[4], encoding="utf-8") as f:
            progress = json.load(f)
    with open(tarefas_json_path, encoding="utf-8") as f:
        data = json.load(f)
    out = build_html(
        cliente, data["tarefas"], data.get("pontos_atencao", []),
        date.today().strftime("%d/%m/%Y"),
        data.get("conclusao_consultor"), progress,
    )
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"OK: {out_html_path}")
