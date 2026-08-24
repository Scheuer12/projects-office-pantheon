# papiro-client-question-builder

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Client Question Builder — Papiro

Cada pergunta: id, priority, process_id, question, reason, [INTERNAL_IDENTIFIER],
[INTERNAL_IDENTIFIER], expected_evidence, recommended_role, source_id, locator, source_hash.

## IDs

Regras: [REDACTED_INSTRUCTION]

- Formato determinístico: `[REDACTED_INSTRUCTION]`
- Preservar `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`
- Mudança de hash da fonte → novo ID + versão; alias do ID anterior só com correspondência segura
- Não alterar o questionário original

## Regras

- Uma dúvida principal por pergunta.
- Não indutiva; não esconder origem.
- PT-BR.

## Perguntas de ecossistema (pós-[PROJECT_CLIENT_3])

Considerar ECO-01…ECO-09 quando tema ausente/ambíguo. Não inventar nomes de sistema como fato na pergunta.
