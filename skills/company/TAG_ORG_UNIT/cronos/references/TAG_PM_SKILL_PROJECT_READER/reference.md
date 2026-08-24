# Referência MCP — [CODE_REFERENCE] Reader ([ENVIRONMENT])

## Ferramentas (preferir **user-MCP-[CODE_REFERENCE]** com `[INTERNAL_API_METHOD]`)

| Finalidade | Tool |
|------------|------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Hub Analista: prefixo `[REDACTED_INSTRUCTION]` — **params devem ir em `[REDACTED_INSTRUCTION]`**.

Mensageria: [REDACTED_INSTRUCTION]

## Enums validados ([ENVIRONMENT] [DATE])

### Sprint
- `[REDACTED_INSTRUCTION]` → Projetos [PROJECT_SYSTEM]
- `[REDACTED_INSTRUCTION]` → Ativado [REDACTED_INSTRUCTION]
- `[REDACTED_INSTRUCTION]` → Congelado (excluir do escopo ativo)

### Tarefa statusTarefa
- `1` Lançada | `2` Andamento | `3` Pendente | `5` Finalizada
- Abertas WIP: 1, 2, 3

### Substatus
- `[REDACTED_INSTRUCTION]` → Aguardando cliente

### Recurso — nível (`[INTERNAL_API_METHOD]`)
- `1` → Interno [REDACTED_INSTRUCTION]
- `2` → Externo [REDACTED_INSTRUCTION]

### Recurso — [REDACTED_INSTRUCTION]

Campo **autoritativo** para Consultor vs Analista vs [ROLE_PLACEHOLDER_3].

| id | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|----|---------------------------|--------------|
| 1 | [REDACTED_INSTRUCTION] | 3 |
| 2 | [REDACTED_INSTRUCTION] | 9 |
| 3 | [REDACTED_INSTRUCTION] | 4 |
| 4 | [REDACTED_INSTRUCTION] | 12 |
| 5 | [REDACTED_INSTRUCTION] | 9 |
| 6 | [REDACTED_INSTRUCTION] | 3 |
| 8 | [REDACTED_INSTRUCTION] | 2 |
| 9 | [REDACTED_INSTRUCTION] | 5 |
| 11 | [REDACTED_INSTRUCTION] | 2 |
| 12 | [REDACTED_INSTRUCTION] | 1 |
| 13 | [REDACTED_INSTRUCTION] | 2 |
| 14 | [REDACTED_INSTRUCTION] | 4 |

Mapa completo e grupos: [shared/resource-types.yaml][REDACTED_INSTRUCTION].

**Bug [ENVIRONMENT]:** `[REDACTED_INSTRUCTION]` no WS falha [REDACTED_INSTRUCTION] — buscar `[REDACTED_INSTRUCTION]` e filtrar `[REDACTED_INSTRUCTION]` no cliente.

**Não confundir:** `[REDACTED_INSTRUCTION]` = tipo de usuário no cadastro; **não** é função do recurso.

**Ativo operacional:** allowlist `[REDACTED_INSTRUCTION]` em [shared/resource-types.yaml][REDACTED_INSTRUCTION] — cadastro [CODE_REFERENCE] ≠ ativo.

## Consultores ativos

[REDACTED_INSTRUCTION]


## [INTERNAL_API_METHOD] — exemplo

```json
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Resposta relevante: `id`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`.

## [INTERNAL_API_METHOD] — filtros úteis

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
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

## [INTERNAL_API_METHOD] — resposta real

```json
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Parâmetros: `[REDACTED_INSTRUCTION]`

## [INTERNAL_API_METHOD] — resposta

**Importante ([REDACTED_INSTRUCTION] hub):** `[REDACTED_INSTRUCTION]` deve ser **string**, não número.

```json
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Passar `[REDACTED_INSTRUCTION]` (integer) falha na validação do [REDACTED_INSTRUCTION] Analista.

```json
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Mapear remetente/destinatário: `[REDACTED_INSTRUCTION]` → campo `[REDACTED_INSTRUCTION]`.

Cenários de regressão: [../../tests/golden-questions.yaml][REDACTED_INSTRUCTION] (GOLD-010, GOLD-015).

## [API_DOCS]

- Índice: [EXTERNAL_URL]]/
- Schemas: `[REDACTED_INSTRUCTION]` — campo previsto `[REDACTED_INSTRUCTION]`

## Volume esperado (orientação — revalidar via MCP)

Não usar estes números como verdade operacional. Spot-check [DATE]: ~20 sprints [PROJECT_SYSTEM] ativos; ~57 recursos internos; allowlist consultores = `[REDACTED_INSTRUCTION]` em resource-types.yaml.

- Sprints ativos: `[REDACTED_INSTRUCTION]` → `[REDACTED_INSTRUCTION]`
- Recursos internos: `[REDACTED_INSTRUCTION]` → total paginação
- Consultores ativos: allowlist YAML + existência no [INTERNAL_API_METHOD]
- Tarefas: variam por sprint (paginar 250/página)
- Tempo detalhado: dezenas de linhas por sprint
