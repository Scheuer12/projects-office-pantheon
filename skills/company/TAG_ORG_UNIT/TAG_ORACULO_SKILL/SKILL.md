---
name: [REDACTED_INSTRUCTION]
description: [REDACTED_INSTRUCTION]
slug: [REDACTED_INSTRUCTION]
metadata:
  [AGENT_PLATFORM]:
    slug: [REDACTED_INSTRUCTION]
    skillKey: [REDACTED_INSTRUCTION]
  paperclipSkillKey: [REDACTED_INSTRUCTION]
  skillKey: [REDACTED_INSTRUCTION]
key: [REDACTED_INSTRUCTION]

# Skill: consultar [[ENV_VAR]] [COMPANY_PRODUCT]

Consulta o [[ENV_VAR]] via [REDACTED_INSTRUCTION]. Não use [WORKFLOW_PLATFORM].

## Arquivo a executar

Caminho relativo à raiz desta skill:

```text
[REDACTED_CODE_OR_CONFIG]
```

## Pré-requisitos

- Env `[ENV_VAR]` injetado pelo [AGENT_PLATFORM]
- Dependências: `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`
- Payload completo do acionador: `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`

## Comando

```bash
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Opcionais:

```bash
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

## Saída

O script imprime JSON no stdout. Campo útil:

- `[REDACTED_INSTRUCTION]` — [REDACTED_INSTRUCTION]
- `ok`, `[REDACTED_INSTRUCTION]` — diagnóstico

Em erro, JSON em stderr com `[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]`.

## Regras

1. Se faltar `[REDACTED_INSTRUCTION]` / `[REDACTED_INSTRUCTION]` / `[REDACTED_INSTRUCTION]` / `[REDACTED_INSTRUCTION]`, **não execute** o script; peça ao agente acionador.
2. Um cliente por execução.
3. Não imprima `[ENV_VAR]`.
4. Responda ao acionador com o conteúdo de `[REDACTED_INSTRUCTION]`.
