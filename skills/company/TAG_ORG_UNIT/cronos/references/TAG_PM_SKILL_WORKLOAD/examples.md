# Exemplos — Workload Controller

## Livre de [IMPLEMENTATION_EVENT] — [REDACTED_INSTRUCTION]

**Pergunta:** Que consultores internos estão livres de [IMPLEMENTATION_EVENT] na semana de 15 a 19 de maio?

**Pipeline:**
1. Reader: sprints ativos + tarefas com prazo ∈ P + `[REDACTED_INSTRUCTION]` + `[REDACTED_INSTRUCTION]`
2. `[REDACTED_INSTRUCTION]` = `[REDACTED_INSTRUCTION]` do Reader [REDACTED_INSTRUCTION]
3. Montar **blocos** de [IMPLEMENTATION_EVENT] (`[REDACTED_INSTRUCTION]`) — não contar subtarefas `[REDACTED_INSTRUCTION]`
4. Livres = consultores **ativos** sem **bloco impl** intersectando a semana W (teto 1/semana)

**Resposta (trecho):**
- Universo: **N consultores ativos** da allowlist [REDACTED_INSTRUCTION]
- Confiança: **CONFIRMADO** para critério atribuição+prazo+nome+função+ativo
- Nota: [PERSON_NAME_21], [PERSON_NAME_3] etc. são consultoras cadastradas mas **inativas** — fora do escopo

## Bloco pai vs subtarefas diárias — [PROJECT_CLIENT_2]

**Referência [CODE_REFERENCE]:** #[TASK_ID_1] `[REDACTED_INSTRUCTION]` (pai) → filhas #[TASK_ID_2]–[TASK_ID_10] `[REDACTED_INSTRUCTION]`.

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|----------|-------|
| [REDACTED_INSTRUCTION] | 10+ |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

**Erro comum:** tratar cada `[REDACTED_INSTRUCTION]` como [VALIDATION_STAGE] separada → pico falso.

## Assistência de projetos ([PERSON_NAME_21])

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|------|----------------------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## Consultor inativo vs ativo

| [REDACTED_INSTRUCTION] | id | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|---------|-----|--------|-------|
| [PERSON_NAME] | 354 | [REDACTED_INSTRUCTION] | Sim |
| [PERSON_NAME] | 644 | [REDACTED_INSTRUCTION] | Sim |
| [REDACTED_INSTRUCTION] | 696 | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Pergunta "consultor livre" → só [PERSON_NAME], [PERSON_NAME], [PERSON_NAME] entram no cálculo (N=3).

## [PERSON_NAME_5] vs [PERSON_NAME] — funções diferentes

**Pergunta:** Quem está livre de [IMPLEMENTATION_EVENT] na semana que vem?

- **[PERSON_NAME_5]** ([RESOURCE_ID_5], Analista) → fora do universo "consultores ativos"
- **[PERSON_NAME]** (644, Consultor ativo) → dentro do universo

## [PERSON_NAME] — envolvido hoje

**Separar:**
- **Atribuído hoje:** WIP com prazo [DATE], recurso 354, Consultor **ativo**
- **Envolvido hoje:** checkpoints + mensagerias em [DATE]

Se mensageria não rodou: INSUFICIENTE para envolvimento; reportar atribuído separadamente.

## Ranking de carga (visão ativa)

Ordenar **consultores ativos** (`[REDACTED_INSTRUCTION]`) por:
1. Total WIP (desc)
2. Desempate: soma previsto (se disponível)

Colunas **Função** e **Ativo** obrigatórias se universo misto.
