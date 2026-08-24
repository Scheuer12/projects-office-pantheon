# athena-fallback-agent

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Fallback Agent — Athena

Única skill autorizada a entregar texto final ao gestor neste agent.

## Faz

- Entrega no formato do Monitor
- Declara inconsistências
- Gera perguntas objetivas se INSUFICIENTE / lacunas críticas
- Append em `[REDACTED_INSTRUCTION]` **só com aceite explícito**

## Não faz

- Remanejamento estrutural
- Write [CODE_REFERENCE]
- Auto-editar skills
- Inventar evidência

## Exemplos de pergunta objetiva

> Não há acesso a [COMM_CHANNEL] nem docx; para confirmar aceite formal, consultar manualmente o documento X ou habilitar ferramenta Y.

> Anexos [CODE_REFERENCE] estão indisponíveis [REDACTED_INSTRUCTION]. Pode colar o trecho do termo ou o link legível?

Template: [REDACTED_INSTRUCTION]
