# Pantheon: structuring AI support for project operations

## Context

Project delivery depends on more than a schedule. Meeting notes, scope definitions, process knowledge, and implementation decisions all affect what a team should do next. When those sources are scattered, even a well-written status report can miss the reason a project is stuck.

Pantheon brings specialist agent roles into that work. The goal is to support analysis and preparation while keeping evidence and decision authority visible.

This public version is a redacted architecture case study. The source files preserve parts of the design, but they cannot be imported as a working production system.

## My contribution

I structured the operating model: responsibilities, agent instructions, reusable skill packages, handoff contracts, and rules for handling evidence and escalating decisions.

The contribution described here is that project-specific design. Platform-related utility packages are also included under `skills/paperclipai/`; the repository should not be read as a claim that I built the underlying agent platform.

## How the work is divided

Two groups handle different questions:

| Workstream | Question | Roles |
|---|---|---|
| Project analysis | What is happening, what is at risk, and what needs attention? | Zeus coordinates Cronos and Athena |
| Process discovery and blueprinting | Do we understand the current operation well enough to propose the next one? | Gaia coordinates Papiro, Perseu, Atlas, and approved mapping work |

Cronos covers the structural side of project analysis, including schedules and workload. Athena examines evidence, scope, and qualitative risks. Zeus consolidates their findings.

For process work, Papiro checks whether the input is sufficient. Perseu structures the current process, or AS-IS. Atlas develops the proposed process, or TO-BE. MappingFromTo handles changes to the relationship between operational concepts and the target vocabulary, with a human approval boundary.

The [blueprint pipeline](skills/company/TAG_ORG_UNIT/gaia/references/shared/blueprint-pipeline.yaml) shows the coordination structure. The [agent definitions](agents/) provide the individual responsibilities.

## Decisions worth inspecting

### 1. Split the work by responsibility

Schedule analysis, evidence review, and process mapping need different inputs and checks. Separate roles make those boundaries easier to describe and inspect.

The cost is coordination: every additional role creates another handoff to maintain. The design therefore needs explicit contracts rather than relying on an agent name to imply what it can do.

### 2. Carry evidence through the workflow

A statement can be confirmed, a claim, an indication, or a conflict. Treating all of them as established facts would make the final report misleading.

The [evidence taxonomy](skills/company/TAG_ORG_UNIT/papiro/references/shared/evidence-taxonomy.yaml) retains fields for source references, locators, assertions, classification, and confidence. A [handoff schema](skills/company/TAG_ORG_UNIT/papiro/references/shared/handoff-asis.schema.yaml) provides the structure for passing discovery work forward.

These files show the intended contracts. They do not, by themselves, prove that every runtime response follows them.

### 3. Keep calculations explicit

Some steps are easier to inspect as ordinary code. The [transcript scanner](skills/company/TAG_ORG_UNIT/TAG_DOMAIN_SETUP_SKILL/scripts/scan_transcricao.py) finds candidate passages and preserves their surrounding text and time reference. It does not decide whether a passage is actually relevant to the issue being analyzed.

The [segment calculation script](skills/company/TAG_ORG_UNIT/TAG_DOMAIN_SETUP_SKILL/scripts/compute_indice.py) takes already-confirmed segments and calculates a total and percentage. The separation matters: classification needs context; adding durations should remain reproducible.

### 4. Separate analysis from authority to act

Finding a risk does not automatically authorize a scope change, a system update, or an external message. The operating model includes escalation and approval boundaries for those actions.

The [communication action matrix](skills/company/TAG_ORG_UNIT/pmo-zeus/references/shared/communication-action-matrix.yaml) and [mapping approval gate](skills/company/TAG_ORG_UNIT/mapping-from-to/references/shared/board-gate.yaml) show parts of this design. Technical enforcement still depends on the runtime and its access controls.

## What the public case establishes

The export makes the role design, workflow structure, evidence contracts, and selected processing scripts available for inspection. It shows how I approached turning ambiguous operational work into components with clearer responsibilities.

It does not establish measured time savings, accuracy, production reliability, or financial return. A reviewer cannot reproduce the full system from this version, and the repository does not include a public benchmark or automated evaluation suite.

A useful next step for public demonstration is a small, independent workflow with synthetic inputs, expected outputs, and tests. That would let someone inspect execution without depending on the original operational environment.

## Publication boundaries

Client information, internal procedures, endpoints, and credentials are outside the scope of this case. Redactions in the source files should not be filled in from guesses.

See [export notes](README-PORTFOLIO.md) and [publication boundaries](LEGAL_AND_PRIVACY_NOTE.md).

[Back to Pantheon](README.md)
