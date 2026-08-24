# gaia-mapping-delegate

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Mapping Delegate — Gaia

## Por que MappingFromTo existe

Referenciador conceitual [REDACTED_INSTRUCTION]. **Pode alterar o
arquivo de referência de TO BE/mapping** — por isso **não** é etapa default
automática do blueprint.

## Quando acionar

Só se:

1. O **board solicitou** explicitamente, ou  
2. Gaia julgou necessário **e** o board **autorizou** a corrida (após pedido claro).

Caso contrário: pular ST3 (`[REDACTED_INSTRUCTION]`) e seguir Atlas
com MappingPack já existente / bridge read-only, sem mutar referência.

## Como acionar

1. Se Gaia recomenda: pedir permissão ao board com motivo (lacunas [CODE_REFERENCE], termos
   novos, drift de referência). **Parar** até resposta.
2. Com OK: delegar `[REDACTED_INSTRUCTION]` em modo **propor** (MappingPack +
   `[REDACTED_INSTRUCTION]`).
3. Mostrar o diff ao board. **Não** permitir apply até aprovação do diff.
4. Só após aprovação: autorizar fase **aplicar** e exigir `[REDACTED_INSTRUCTION]`.

[CODE_REFERENCE] prevalece em conflito. Não inventar telas/webservices.
