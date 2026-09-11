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

## Worked example: conflicting delivery signals

This is a synthetic scenario written to explain the design. The source IDs below refer only to the invented inputs in this table. It is not a customer case or output from a running agent system.

| Source | Input |
|---|---|
| S1 — schedule snapshot, Monday 09:00 | Acceptance testing starts Thursday. Import validation is a prerequisite and is marked complete. |
| S2 — meeting note, Monday 10:00 | The implementation lead reports that two import errors remain unresolved. There is no repair estimate yet. |
| S3 — approved scope, revision 2 | Acceptance testing requires the import validation checklist to pass. |

The useful question is whether the team has enough evidence to keep Thursday's plan.

**Structural analysis.** Cronos would identify the dependency between import validation and testing. The inputs do not include a repair estimate or remaining validation effort, so they do not support calculating a new finish date.

**Evidence review.** Athena would retain the conflict between S1 and S2. The note establishes that someone reported errors; it does not independently establish their severity or whether they fail the checklist in S3. Neither silently trusting the schedule nor declaring a confirmed delay resolves that gap.

**Consolidated handoff.** Zeus would prepare a decision brief along these lines:

| Field | Proposed content |
|---|---|
| Finding | Readiness for Thursday's acceptance testing is unresolved. |
| Evidence | S1 marks the prerequisite complete; S2 reports open errors; S3 defines the acceptance condition. |
| Risk | Testing may need to move if the errors prevent the checklist from passing. |
| Missing information | Checklist results, error severity, repair estimate, and time needed for revalidation. |
| Next step | Ask the implementation lead to reconcile the status and provide the missing evidence. |
| Decision boundary | The responsible person reviews the evidence before approving any schedule change or external update. |

The output should preserve that uncertainty. It should not invent a delay estimate, treat a reported error as a verified blocker, or change the schedule automatically.

For a future executable demo, this scenario can become an evaluation fixture: check that the output cites all three sources, retains the conflict, asks for the missing evidence, and proposes no unsupported completion date. Those checks are proposed acceptance criteria, not tests already implemented here.

## What the public case establishes

The export makes the role design, workflow structure, evidence contracts, and selected processing scripts available for inspection. It shows how I approached turning ambiguous operational work into components with clearer responsibilities.

It does not establish measured time savings, accuracy, production reliability, or financial return. A reviewer cannot reproduce the full system from this version, and the repository does not include a public benchmark or automated evaluation suite.

A useful next step for public demonstration is a small, independent workflow with synthetic inputs, expected outputs, and tests. That would let someone inspect execution without depending on the original operational environment.

## Publication boundaries

Client information, internal procedures, endpoints, and credentials are outside the scope of this case. Redactions in the source files should not be filled in from guesses.

See [export notes](README-PORTFOLIO.md) and [publication boundaries](LEGAL_AND_PRIVACY_NOTE.md).

[Back to Pantheon](README.md)
