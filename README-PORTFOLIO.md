# Pantheon — Export Notes

This package is a redacted export of the Pantheon operating model. Start with the [project overview](README.md) or [case study](CASE_STUDY.md); this document explains how to read the exported source files.

## Purpose

Demonstrate architecture of a specialist agent org (roles, skills, handoffs, governance patterns) **without** disclosing employer-confidential process, credentials, or client identifiers.

## Placeholder legend

| Tag | Meaning |
|-----|---------|
| `[COMPANY_PRODUCT]` | Employer product / platform name |
| `[COMPANY_DOMAIN]` / `[CLIENT_HOST]` | Real domains / client hosts |
| `[CLIENT_NAME_N]` / `[PROJECT_CLIENT_N]` | Real client and project names |
| `[ORG_NAME]` / `[ORG_SLUG]` / `[ORG_UNIT]` | Internal team naming |
| `[DOMAIN_PRODUCT]` / `[PROJECT_SYSTEM]` / `[INTERNAL_KB_NAME]` | Internal systems |
| `[ORACULO_WEBHOOK_URL]` / `[ENV_VAR]` / `[SECRET_VALUE]` / `[AUTH_TOKEN]` | Secrets & [REDACTED_ENDPOINT]s |
| `[EMAIL]` / `[UUID]` / `[IP_ADDRESS]` / `[SERVER_PATH]` | Identifiers & infra |
| `[REDACTED_INSTRUCTION]` | Mid-sentence hole (may break grammar on purpose) |
| `[CODE_REFERENCE]` | Product/system/codebase vocabulary collapsed to opaque ref |
| `[REDACTED_CODE_OR_CONFIG]` | Code/config fences |
| `[REDACTED_IMAGE]` | Charts/images removed |
| `[PERSON_NAME]` / `[PERSON_NAME_N]` | Employee / consultant names |
| `[INTERNAL_API_METHOD]` | Internal webservice / API operation names |
| `[COMPANY_INTERNAL_ID]` | Internal authored_by / enum-like company ids |
| `[METRIC]` / `[DATE]` | SLA numbers and concrete dates |

## Redaction style (broken coherence)

Keep the **reasoning spine** (headings, AS IS / TO BE, list order, “do X then Y”).  
Punch holes so specifics become unintelligible — even if the sentence breaks:

> Contar a **história do [REDACTED_INSTRUCTION] do cliente** como se o [CODE_REFERENCE] fosse o único vocabulário — módulos, fluxos, [REDACTED_INSTRUCTION] aderir o sistema à operação.

A reviewer should see craft and structure, not be able to reconstruct employer process.

## What remains visible

- Agent tree and role separation (CEO, PMO, analysts, specialists)
- Skill packaging pattern (`SKILL.md` + `scripts/` + `references/`)
- Inter-agent contract style and heartbeat/soul/tools conventions
- That operational doctrine existed and was structured (headings retained)

## What was removed / obscured

- Employer branding and product names
- Client hosts, [COMM_CHANNEL]s, tokens, paths
- Detailed SOPs, SLA numbers, matrices, nomenclatures, and process checklists

## Execution limits

Secrets, endpoints, configuration values, and parts of the implementation were removed. This repository is not a runnable company import, and adding environment configuration alone will not restore it. The source files are included for architectural inspection.

