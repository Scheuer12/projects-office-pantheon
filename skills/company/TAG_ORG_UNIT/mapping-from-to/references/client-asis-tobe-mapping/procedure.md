# [COMPANY_PRODUCT]-asis-tobe-mapping

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# [COMPANY_PRODUCT] AS IS ↔ TO BE Mapping (From-To)

Referenciador norteador para IAs de levantamento, AS IS e TO BE. **Não** fecha escopo comercial sozinho; **é determinante** em conceitos de produto quando a KB [CODE_REFERENCE] tem evidência de path.

## Autoridade

Ordem e conflitos: [shared/authority.yaml](shared/authority.yaml)

1. [REDACTED_KB_NAME] [CODE_REFERENCE] (código) — prevalece  
2. POP / metodologia [COMPANY_PRODUCT]  
3. Exemplos AS IS/TO BE assinados (prática)  
4. Levantamento/evidências do cliente (fatos)  
5. [CODE_REFERENCE] genérico — só lacunas; nunca sobrescreve [COMPANY_PRODUCT]  

Snapshot local: [../../references/[CODE_REFERENCE]-kb/][REDACTED_INSTRUCTION]  
Origem Desktop/[REDACTED_INSTRUCTION]: `[REDACTED_INSTRUCTION]`

## Pipeline

```mermaid
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

1. Ler `[REDACTED_INSTRUCTION]` e [CODE_REFERENCE] [REDACTED_INSTRUCTION].
2. Extrair termos/processos das fontes do cliente (sem alterar [REDACTED_INSTRUCTION]).
3. Normalizar com [shared/glossary-logistics-[COMPANY_PRODUCT].md][REDACTED_INSTRUCTION].
4. Resolver From-To com [shared/mapping-from-to.md][REDACTED_INSTRUCTION].
5. Emitir **MappingPack** (template abaixo).
6. Separar: factual AS IS × hipóteses TO BE × [REDACTED_INSTRUCTION] futura × gaps.

## Regras duras

- **Board gate:** mutação de arquivos de referência só após permissão do board +
  aprovação do `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION].
  Sem autorização → só propor MappingPack + diff; não gravar.
- Não inventar telas, módulos, enums ou parâmetros sem path [CODE_REFERENCE]/código.
- Não transformar capacidade [COMPANY_PRODUCT] em estado atual do cliente.
- Não colocar TO BE no corpo AS IS.
- Conflito genérico × [COMPANY_PRODUCT] → vence [COMPANY_PRODUCT]; registrar conflito.
- MV ≠ modelo de movimentação; [REDACTED_INSTRUCTION]; Consolidado [REDACTED_INSTRUCTION] ≠ estoque consolidado.
- [SYSTEM_LINK]: hub `[REDACTED_INSTRUCTION]`; parceiro só com evidência.
- Config: citar **área** [REDACTED_INSTRUCTION]; nunca inventar valor.
- Visita presencial não é requisito deste mapeamento.

## MappingPack — saída

Ver [template-mapping-pack.md](template-mapping-pack.md).

Campos mínimos por item: `[REDACTED_INSTRUCTION]`, `to`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`.

Status finais do pacote:

- `[INTERNAL_API_METHOD]` — mapa útil com gaps explícitos  
- `[INTERNAL_API_METHOD]` — termos críticos sem resolução e sem pergunta  
- `[INTERNAL_API_METHOD]` — [REDACTED_INSTRUCTION]

## [SYSTEM_LINK] com Papiro / Perseu / futuro Atlas

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|---|---|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## Exemplos

Ver [examples.md](examples.md).
