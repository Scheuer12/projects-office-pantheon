# [COMPANY_PRODUCT]-pm-response-monitor

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Response Monitor — Cronos v0

## Papel

Validar outputs do Reader, Schedule, Workload, **Management Advisor** e **Data Hunter** **antes** do Fallback.

**Monitor produz rascunho; Fallback entrega ao gestor.**

Glossário: [shared/glossary.md](shared/glossary.md)  
Blocos de campo: [shared/field-blocks.yaml](shared/field-blocks.yaml)  
Funções recurso: [shared/resource-types.yaml][REDACTED_INSTRUCTION]  
Mobilidade: [REDACTED_INSTRUCTION]
Data Hunter: [../[COMPANY_PRODUCT]-pm-data-hunter/SKILL.md][REDACTED_INSTRUCTION]  
Management Advisor: [../[COMPANY_PRODUCT]-pm-management-advisor/SKILL.md][REDACTED_INSTRUCTION]  
Fallback: [REDACTED_INSTRUCTION]

## Selos de confiança

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|------|----------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

**Veredicto geral:** `[INTERNAL_API_METHOD]` | `[INTERNAL_API_METHOD]` | `[INTERNAL_API_METHOD]`

Downgrade automático para **PARCIAL** se:
- `[REDACTED_INSTRUCTION]` zerado em >80% das tarefas WIP analisadas
- Mensageria não consultada numa pergunta de **envolvido**
- Nome de pessoa com >1 recurso interno sem desambiguação
- Cobertura sprint < 100% dos ativos
- Pergunta cita "consultor" mas universo = todos cadastrados ou internos [REDACTED_INSTRUCTION]
- Pergunta cita "consultor" mas universo ignora allowlist ativos
- Capacidade / simultaneidade usou contagem de tarefas em vez de **blocos** (`[REDACTED_INSTRUCTION]`)
- Subtarefas `[REDACTED_INSTRUCTION]` contadas como implantações separadas
- Pergunta exige contexto externo [REDACTED_INSTRUCTION] e **Data Hunter não foi acionado**
- Data Hunter retornou **NO_ACCESS** ou **PARTIAL** e contexto externo é **relevante** (não crítico)
- Evidência externa **FOUND** usada sem citar fonte, data e confiança separadas do [CODE_REFERENCE]
- **Management Advisor** acionado sem saídas Schedule **e** Workload
- Recomendação Advisor move **[IMPLEMENTATION_EVENT]** como primeira opção sem declarar último recurso + aprovação humana
- Advisor omitiu trade-off, risco residual ou decisão humana em recomendação **CRÍTICA**
- Contexto qualitativo relevante ausente e Advisor não declarou limitação (PARCIAL)
- Decisão Advisor depende de aceite/promessa externa e Data Hunter NO_ACCESS → INSUFICIENTE

## Política anti-alucinação

**Proibido:**
- Número sem filtro [CODE_REFERENCE] + timestamp
- Colapsar atribuído e envolvido
- Apresentar inferência como certeza
- Omitir tarefas excluídas por falta de prazo
- Transformar evidência externa ([COMM_CHANNEL], [EXTERNAL_CHANNEL]) em fato [CODE_REFERENCE] **CONFIRMADO**
- Afirmar comunicação ao cliente sem Data Hunter ou fonte externa consultável

**Obrigatório:**
- Lead with confidence level
- Separar **fato [CODE_REFERENCE]** vs **evidência externa** vs interpretação
- Listar o que faltou para CONFIRMADO
- Se Data Hunter **FOUND**: citar fonte, data, participantes e confiança em bloco separado de Evidência [CODE_REFERENCE]
- Se Data Hunter **NOT_FOUND**: declarar busca feita — não confundir com NO_ACCESS

## Bloco Monitor (sempre presente)

Copiar este template em **toda** resposta ao gestor:

```markdown
[REDACTED_CODE_OR_CONFIG]

[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

## Checklist de validação

- [ ] Snapshot cruzou apenas sprints ativos [REDACTED_INSTRUCTION]
- [ ] Período P aplicado a todos os critérios [REDACTED_INSTRUCTION]
- [ ] Hierarquia Sprint→Tipo→Nome→Status→Substatus respeitada
- [ ] Categorias X via [REDACTED_INSTRUCTION]
- [ ] Pergunta de tendência rotulada INFERÊNCIA
- [ ] Desambiguação documentada [REDACTED_INSTRUCTION]
- [ ] Função do recurso (`[REDACTED_INSTRUCTION]`) aplicada quando pergunta cita consultor/analista/dev
- [ ] Status **ativo** cruzado com `[REDACTED_INSTRUCTION]` em resource-types.yaml
- [ ] Universo declarado como `[REDACTED_INSTRUCTION]` + nomes [REDACTED_INSTRUCTION]
- [ ] Capacidade/risco usou N do snapshot [REDACTED_INSTRUCTION] — sem hardcode de equipe
- [ ] Implantações simultâneas / livre de [IMPLEMENTATION_EVENT] (semana) usaram **blocos**, não taxonomia bruta
- [ ] Assistência de projetos: campo → sem recurso; admin fora da capacidade
- [ ] Pico reportado por **semana útil**, não quinzena agregada
- [ ] Contexto externo exigido → Data Hunter acionado com `[REDACTED_INSTRUCTION]` válido
- [ ] Evidência externa citada em bloco separado — não misturada com selo [CODE_REFERENCE] CONFIRMADO
- [ ] NO_ACCESS declarado quando [REDACTED_INSTRUCTION] [REDACTED_INSTRUCTION] indisponível
- [ ] Rascunho encaminhado ao **[COMPANY_PRODUCT]-pm-fallback-agent** — Monitor não entrega ao gestor diretamente
- [ ] Management Advisor: base Schedule+Workload citada; mobilidade provisória declarada se mover agendas
- [ ] Recomendação crítica inclui trade-offs e decisões humanas

## Quando bloquear conclusão

Responder **INSUFICIENTE** como conclusão principal quando:
- Match de projeto/tarefa/pessoa não é único
- [REDACTED_ENDPOINT] crítico falhou e não há fallback
- Pergunta exige envolvimento completo e mensageria indisponível
- Data Hunter retornou **NO_ACCESS** e decisão **depende criticamente** da fonte externa (`[REDACTED_INSTRUCTION]`)
- Data Hunter retornou **AMBIGUOUS** e conclusão exige identificação única externa

Pode acrescentar: *"Embora os sinais parciais indiquem…"* **após** a recusa, nunca no lugar dela.

## Template de resposta completa

Ver [template.md](template.md).
