# [COMPANY_PRODUCT]-pm-schedule-controller

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Schedule Controller — Cronos v0

## Pré-requisito

1. **[COMPANY_PRODUCT]-pm-tar-reader** → `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION]
2. **[COMPANY_PRODUCT]-pm-response-monitor** → validar antes de entregar

Glossário: [shared/glossary.md](shared/glossary.md)  
Taxonomia: [REDACTED_INSTRUCTION]
Blocos de campo: [shared/field-blocks.yaml](shared/field-blocks.yaml)  
Funções: [shared/resource-types.yaml][REDACTED_INSTRUCTION]  
Eixos projeto: [shared/project-context.yaml][REDACTED_INSTRUCTION]

## Eixos de projeto (obrigatório na análise)

Consumir `[REDACTED_INSTRUCTION]` — **complexidade** e **sensibilidade** [REDACTED_INSTRUCTION].

| Uso | [REDACTED_INSTRUCTION] |
|-----|-------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Premissas formais: [../[COMPANY_PRODUCT]-pm-project-doctrine/SKILL.md][REDACTED_INSTRUCTION] (quando preenchida).

## Intenções suportadas

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|----------|-----------|
| [REDACTED_INSTRUCTION] | CONFIRMADO |
| [REDACTED_INSTRUCTION] | DERIVADO |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## Blocos de campo (cronograma e simultaneidade)

Para **quantas implantações na mesma semana**, **picos até fim do ano** ou **conflito de agenda**, usar blocos — não contagem de tarefas.

Ver [shared/field-blocks.yaml](shared/field-blocks.yaml). Pontos críticos:

- **Unidade** = tarefa pai (ex. #[TASK_ID_1]); filhas `[REDACTED_INSTRUCTION]` = **um** período.
- **Excluir** roteiro, registro, entregáveis, termos, envio/[REDACTED_INSTRUCTION] da contagem de semanas de campo.
- **Período do bloco** = intervalo das filhas diárias; fases longas sem filhas → semana do prazo apenas.
- **[PERSON_NAME_21] / assistente:** bloco impl/hom/setup → sem recurso; não conta como consultor ocupado.
- **Métrica:** `[REDACTED_INSTRUCTION]` = blocos distintos [REDACTED_INSTRUCTION].
- **N** = `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION]. **Proibido** usar literal fixo de equipe.
- **Risco (capacidade):** `[REDACTED_INSTRUCTION]`
- **Crítico / inviável:** `[REDACTED_INSTRUCTION]` sem remanejo
- Datas de sprint/tarefa (limites, status) = [REDACTED_INSTRUCTION] atual — [REDACTED_INSTRUCTION]

Reportar pico **por semana útil**, não por quinzena calendário.

## Resolução de entidades

```
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Hierarquia obrigatória: Sprint → Tipo → **Nome** → Status → Substatus.

## Critério de atraso (CONFIRMADO)

Fonte autoritativa: [shared/glossary.md](shared/glossary.md) — [REDACTED_INSTRUCTION].

```
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|------|----------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Responder atraso com `[REDACTED_INSTRUCTION]`; citar `[REDACTED_INSTRUCTION]` só como contexto/drift.

## Score de ameaça (DERIVADO) — sprint ativo

Peso sugerido por sprint [REDACTED_INSTRUCTION]:

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------|--------|
| [REDACTED_INSTRUCTION] | +30 |
| [REDACTED_INSTRUCTION] | +20 |
| [REDACTED_INSTRUCTION] | +15 |
| [REDACTED_INSTRUCTION] | +10 |
| [REDACTED_INSTRUCTION] | +10 |

Top 3 sprints por score decrescente. **Sempre** listar fatores por projeto.

Não apresentar score como verdade [CODE_REFERENCE] — é modelo Controller.

## Cronograma por sprint

Campos:
- `[REDACTED_INSTRUCTION]` — deadline projeto
- Tarefas abertas ordenadas por `[REDACTED_INSTRUCTION]` (deadline / conclusão)
- Drift: dias entre `[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION]

## Tendência a atraso (INFERÊNCIA)

Sinais [REDACTED_INSTRUCTION]:
- Tarefas abertas com limite ∈ P e flag `[REDACTED_INSTRUCTION]`
- WIP alto sem checkpoint recente
- Ratio previsto vs registrado (se previsto disponível)

**Frase obrigatória:** *"Indicadores de risco, não confirmação de atraso."*

## Filtros WS úteis

```json
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

Cruzar sempre com sprint ∈ [INTERNAL_IDENTIFIER].

## Flags com `completo: 1`

Usar quando presentes: `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `tpa`, `tac`.

## Saída recomendada

```markdown
[REDACTED_CODE_OR_CONFIG]

[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]

[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]

[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

## Proibido

- Afirmar data de conclusão futura como certeza
- Classificar **atraso** por `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION]
- Ignorar ambiguidade de tarefa/projeto
- Omitir Monitor
- Contar cada subtarefa diária como [IMPLEMENTATION_EVENT]/[VALIDATION_STAGE] distinta
- Apresentar totais por quinzena como "implantações simultâneas" sem definir semana útil

Exemplos: [REDACTED_INSTRUCTION]
