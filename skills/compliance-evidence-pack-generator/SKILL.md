---
name: compliance-evidence-pack-generator
description: Use when an intake assessment exists and the agent must generate an auditable compliance evidence pack for a government digital assistant. Trigger phrases include "evidence pack", "bewijs", "audit", and "intake".
---

## When to use this Skill

Use after a compliance intake exists (pasted by the user or from the prior agent turn) when owners need a reviewable evidence pack for experiment, pilot, production gate, or pull request.

If the user pastes no intake, ask once for it. If they explicitly ask for a demo and say "op basis van deze intake" without content, use the **demo intake** from the intake skill (municipality waste/permit chatbot, pilot phase, RAG on public pages, personal data possible in prompts) and label it as demo assumptions.

## Inputs to collect

- Completed intake assessment or intake summary
- Intended phase and readiness status
- Owners for product, privacy, security, content, development, and human escalation
- RAG sources, classification, freshness rules, traceability design
- Available logs, monitoring, incident, rollback, and evaluation evidence
- Known gaps, deadlines, and review decisions

## What to do

1. Follow these steps in order after loading this skill.
2. Produce sections for: `compliance-evidence-pack.md`, `risk-register.md`, `decision-log.md`, `human-oversight-plan.md`, `data-and-source-register.md`, `audit-and-logging-plan.md`, and `approval-checklist.md` (as headings inside one response unless the user asks for separate files).
3. For **every** control listed below, emit one row with status, owner, and next action.
4. Use only these status values: `satisfied`, `partially satisfied`, `missing`, `not applicable`.
5. Assign owner and concrete next action to every `partially satisfied` or `missing` item.
6. Separate evidence that exists from evidence still to be created.
7. Use synthetic example data only.

**Controls to cover (minimum):** governance ownership; purpose and scope; user transparency; AI/system classification; privacy/data protection routing; human oversight; RAG source governance; source freshness; source traceability; security controls; logging and audit trail; monitoring and evaluation; incident response; rollback/degradation; approval gates.

## Consistency contract

Use the same control names in every evidence table so downstream agents can map gaps to developer tasks without interpretation drift. Preserve any intake `Readiness status` and explain whether this evidence pack confirms, worsens, or cannot verify it.

Preserve incoming `Handoff ID` values from the intake when present. For new gaps, add an `Evidence ID` using this pattern: `EVID-<control>-<number>`, for example `EVID-AUDIT-1`. Include either the original handoff ID or the new evidence ID in every missing or partially satisfied row.

For every `missing` or `partially satisfied` row, include:

- a named owner role, not just "team"
- a next action that can be completed or rejected
- a due date or gate (`before pilot`, `before production`)
- a source/reference or explicit `missing evidence`

Do not mark a control as `satisfied` unless the user provided evidence or an explicitly requested demo scenario states it.

## Output format

Start with an executive summary (5–8 bullets), then the evidence table. Each control in detailed sections must use:

```text
Control:
Why it matters:
Evidence:
Status:
Owner:
Next action:
Due date:
Source/reference:
```

Full response skeleton:

```markdown
# Compliance evidence pack

## Executive summary
- ...

## Use case scope
...

## Current readiness status
...

## Evidence table
| ID | Control | Evidence | Status | Owner | Next action | Source/reference |
|---|---|---|---|---|---|---|
| | Governance ownership | | | | | |
| | Purpose and scope | | | | | |
| | User transparency | | | | | |
| | AI/system classification | | | | | |
| | Privacy/data protection | | | | | |
| | Human oversight | | | | | |
| | RAG source governance | | | | | |
| | Source freshness | | | | | |
| | Source traceability | | | | | |
| | Security controls | | | | | |
| | Logging and audit trail | | | | | |
| | Monitoring and evaluation | | | | | |
| | Incident response | | | | | |
| | Rollback/degradation | | | | | |
| | Approval gates | | | | | |

## Missing evidence
- ...

## Owner table
| Role | Responsibility |
|---|---|

## Next actions
| ID | Owner | Action | Due date |
|---|---|---|---|

This evidence pack does not prove legal compliance. It records available evidence, gaps, owners, and next actions for review.
```

Prefer the **evidence table** for the demo; add 2–3 expanded control blocks only for the highest-risk gaps.

## What to avoid

- Do not use status values outside the four allowed values.
- Do not claim the pack is a compliance determination or legal sign-off.
- Do not include secrets, real citizen data, raw prompts with personal data, private keys, tokens, or production credentials.
- Do not mark unknown items as `satisfied`.

## Framework grounding

- [onegov2 — compliance](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/compliance.md)
- [onegov2 — governance](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/governance.md)
- [onegov2 — infrastructure and data](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/infrastructure-data.md)
- [onegov2 — security](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/security.md)
- [onegov2 — LLMOps and monitoring](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/llmops-monitoring.md)
- [onegov2 — RAG pipeline practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/rag-pipeline.md)
- [NL API Strategie integration notes](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/integrations/nl-api-strategie.md)
- [ADC raamwerk — compliance monitoring](https://github.com/ADC-Consulting/raamwerk-digitale-assistent)
