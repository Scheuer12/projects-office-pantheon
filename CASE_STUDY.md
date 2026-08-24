# Sanitized Multi-Agent Operations Portfolio

## Overview

This repository is a sanitized portfolio export of a specialist multi-agent organization for project operations, process discovery, implementation planning, and governance.

The artifact demonstrates how I structured agents as an operating system: clear reporting lines, lane ownership, explicit handoff contracts, safety boundaries, source hierarchy, and reusable skill packs.

## Problem

Operational teams often lose clarity when project data, process knowledge, implementation plans, and client-facing decisions live across many tools and informal conversations.

This project explores a governed agent organization that separates:

- structural project analysis from qualitative risk review
- implementation blueprint work from portfolio management
- evidence gathering from decision-making
- code or system reading from mutation authority
- internal synthesis from outbound communication

## Architecture

The organization uses a CEO and PMO layer for prioritization and synthesis, with specialist agents underneath:

- `Cronos`: schedule, workload, and structural project analysis
- `Athena`: evidence, governance, client risk, and quality gates
- `Gaia`: blueprint orchestration for process and implementation work
- `Papiro`: intake quality, process discovery checks, and client-question packs
- `Perseu`: AS IS package construction and validation handoff
- `Atlas`: TO BE storytelling and read-only codebase refinement
- `MappingFromTo`: board-gated mapping between operational concepts and product vocabulary
- `CTO`: agent architecture, standards, portability, and safety review

## Technical Highlights

- Skill-pack pattern using `SKILL.md`, `references/`, and `scripts/`
- Agent anatomy pattern using `AGENTS.md`, `SOUL.md`, `TOOLS.md`, and `HEARTBEAT.md`
- Explicit source hierarchy for facts, rules, procedures, and memory
- Read-only default posture for sensitive systems
- Human approval gates for mutations, scope decisions, [RELEASE_DECISION] decisions, and external communication
- Reusable scripts for setup-plan generation, transcript scanning, topic reconciliation, naming, and progress updates
- Sanitized placeholders for employer, client, person, system, [REDACTED_ENDPOINT], and credential references

## Safety Model

The design assumes agents should fail honestly when evidence is missing, source access is blocked, or a decision exceeds their authority.

The core safety principles are:

- no hardcoded live client rosters or mutable operational facts
- no secrets in repo files, comments, or generated artifacts
- no unauthorized writes to business systems
- no client-facing claims without evidence and communication proof
- no silent reconciliation when sources conflict
- no use of human-local paths as production knowledge sources

## Portfolio Scope

This repository is not a runnable production import. It is intentionally redacted so reviewers can inspect the architecture and reasoning style without reconstructing employer processes, customer environments, or confidential operational details.

## What This Demonstrates

- Systems thinking applied to AI agent organizations
- Agent governance and delegation architecture
- Operational workflow design for real business constraints
- Practical safety boundaries for enterprise AI usage
- Ability to translate ambiguous process work into modular, auditable automation components
