# mapping-from-to-orchestrator

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Mapping Orchestrator

## Por que este agent existe

Mantém o **referenciador From-To** [REDACTED_INSTRUCTION] que Atlas e
Perseu usam. Não é etapa automática do blueprint: **altera arquivo de referência
de TO BE/mapping** quando aplica mudanças.

## Gate (obrigatório)

Ler [shared/board-gate.yaml](shared/board-gate.yaml).

Só executar se:

1. **Board solicitou** explicitamente, ou  
2. **Gaia propôs** e o **board autorizou** a corrida.

Sem isso → `[INTERNAL_API_METHOD]` e parar.

## Protocolo em 2 fases

### Fase A — Propor (sem mutar referência)

1. Carregar [shared/authority.yaml](shared/authority.yaml)
2. Executar [../[COMPANY_PRODUCT]-asis-tobe-mapping/SKILL.md][REDACTED_INSTRUCTION]
3. Emitir **MappingPack** + **`[REDACTED_INSTRUCTION]`**:
   - arquivos-alvo
   - trechos atuais × propostos [REDACTED_INSTRUCTION]
   - motivo / evidência [CODE_REFERENCE]
4. Entregar ao board (via [REDACTED_INSTRUCTION]. Status: `[INTERNAL_API_METHOD]`.

### Fase B — Aplicar (só após aprovação do diff)

1. Confirmar que o board aprovou o **mesmo** diff (ou revisão marcada).
2. Só então gravar os arquivos de referência listados no diff aprovado.
3. Emitir `[REDACTED_INSTRUCTION]` [REDACTED_INSTRUCTION].

**Proibido:** editar referência antes do OK do board; “aplicar e depois avisar”.

[CODE_REFERENCE] prevalece em conflito com [CODE_REFERENCE] genérico.
