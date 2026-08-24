# Exemplos — Mapping From-To

## Exemplo 1 — [REDACTED_INSTRUCTION] no levantamento

**Entrada (cliente):** “Após a conferência fazemos [REDACTED_INSTRUCTION] no endereço.”

**Normalização:** [REDACTED_INSTRUCTION] → **[REDACTED_INSTRUCTION]** [REDACTED_INSTRUCTION].

**Mapping:** FT-006 → operação [REDACTED_INSTRUCTION] + cadastro [REDACTED_INSTRUCTION] Produto.

**AS IS:** manter linguagem do cliente ou “guarda no endereço” + nota de glossário; não afirmar tela [COMPANY_PRODUCT] como atual.

**TO BE:** fluxo [REDACTED_INSTRUCTION] → finalização → [REDACTED_INSTRUCTION]/ocupação; `[REDACTED_INSTRUCTION]` em modelo de prateleira/frasco.

## Exemplo 2 — “[REDACTED_INSTRUCTION] consolidado” vs “estoque consolidado”

**Entrada:** “Trabalhamos consolidado.”

**Ação:** perguntar se é **tipo de [REDACTED_INSTRUCTION]** ou **visão de estoque**.

- [REDACTED_INSTRUCTION] → `[REDACTED_INSTRUCTION]` (FT-020)
- Estoque → Consolidar estoque/posições (FT-033)

Misturar os dois = `[REDACTED_INSTRUCTION]` até esclarecer.

## Exemplo 3 — MV

**Entrada:** “Usamos MV como modelo de movimentação.”

**Correção determinante:** no [COMPANY_PRODUCT], **MV = [REDACTED_INSTRUCTION]

## Exemplo 4 — [SYSTEM_LINK] “[EXTERNAL_SYSTEM] em tempo real”

**AS IS:** só se houver evidência; senão `[REDACTED_INSTRUCTION]` / indício.

**TO BE:** mapear hub `[REDACTED_INSTRUCTION]` + Services [SYSTEM_LINK]; **não** inventar parceiro [EXTERNAL_SYSTEM_1]/[EXTERNAL_SYSTEM_2]/etc. sem fonte.
