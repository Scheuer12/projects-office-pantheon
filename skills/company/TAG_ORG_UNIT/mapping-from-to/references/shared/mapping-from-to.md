# Mapping From-To - Sanitized Portfolio Stub

## Purpose

Demonstrate the mapping discipline used by the agent organization without exposing product vocabulary or operational doctrine.

## Contract

| Field | Meaning |
|------|---------|
| source_concept | `[DOMAIN_CONCEPT_N]` from AS IS or client language |
| target_anchor | `[CODE_REFERENCE]` or `[MODULE_AREA_N]` |
| evidence | `[SOURCE_ANCHOR]` |
| confidence | high / medium / low / not_confirmed |
| caveat | `[REDACTED_REASONING_NOTE]` |

## Rules

1. Do not map a concept without evidence.
2. Preserve false-friend warnings as placeholders.
3. Emit `proposed_reference_diff` before any write.
4. Wait for explicit board approval before changing references.

## Redacted

Concrete product concepts, domain terms, flow names, partner names, system labels, and implementation details were removed.