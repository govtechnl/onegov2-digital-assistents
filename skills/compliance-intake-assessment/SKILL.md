---
name: compliance-intake-assessment
description: Use when a business user, product owner, or compliance reviewer needs to classify a government digital assistant use case and identify required compliance evidence before pilot or production. Trigger phrases include "compliance-bewijzen", "intake", "pilot", and "digitale assistent".
---

## When to use this Skill

Use for early assessment of a government digital assistant idea before experiment, pilot, procurement, or production. Route the use case to the right evidence work and make gaps visible for owner review.

If the user explicitly asks for a demo and gives only a short prompt (for example "Welke compliance-bewijzen heb ik nodig voor een pilot?"), use this **demo scenario** unless they specify otherwise:

- **Organization:** Dutch municipality (gemeente)
- **Use case:** Citizen-facing chat assistant for waste collection, permits, and general service information
- **Users:** Citizens (burgers)
- **Purpose:** Informational Q&A with RAG on public website pages
- **Phase:** Pilot
- **Data:** Free-text questions may contain personal data; no special-category data expected; prompts stored for quality review
- **RAG:** Public web pages + internal FAQ (internal sources need extra governance)
- **Model:** Hosted LLM via approved cloud provider
- **Oversight:** Human escalation for legal, benefit, or case-specific questions

State assumptions explicitly when using the demo scenario.

## Inputs to collect

Collect from the user or infer from context:

- Organization type, use case, target users (citizens, civil servants, or both)
- Assistant purpose: informational, advisory, decision-supporting, or decision-making
- Whether output can influence rights, benefits, enforcement, services, or access to public services
- Data types; personal data in prompts; special-category data; prompt retention
- RAG usage, source types, public vs internal sources
- Model/provider and hosting category; phase (experiment, pilot, production)
- Human oversight, escalation path, owner roles, known gaps

Ask at most **two** clarifying questions if critical inputs are missing; otherwise proceed with stated assumptions.

## What to do

1. Call this skill loaded — follow these steps in order; do not skip sections.
2. Restate the use case in plain Dutch business language (3–5 sentences).
3. Classify assistant type, user group, and data sensitivity (`public only`, `personal data possible`, `special-category possible`, `internal/confidential`, or `unknown`).
4. Fill the routing indicators table for **AI Act**, **AVG/GDPR**, **DPIA**, **IAMA**, and **Algoritmeregister**. Route for review — never decide legal obligations.
5. Define minimum human oversight (escalation for uncertainty, sensitive, legal, and case-specific questions).
6. List required evidence documents with likely owners and status (`available`, `partial`, `missing`, `unknown`).
7. Separate blockers before **pilot** vs before **production**.
8. Choose exactly one readiness status from the allowed list.
9. End with open questions and next actions by owner (with suggested due dates).

**Allowed readiness statuses:** `ready for exploration`, `conditionally ready for pilot`, `not ready for pilot`, `conditionally ready for production`, `not ready for production`.

## Consistency contract

Use the same status vocabulary, owner labels, and control names as the other compliance Skills so the output can be passed directly into an evidence pack or developer gate. Treat this Skill as **routing and intake**, not proof of compliance.

Add a short `Handoff ID` for each important gap using this pattern: `INTAKE-<route>-<number>`, for example `INTAKE-DPIA-1` or `INTAKE-RAG-1`. Reuse these IDs in blockers and next actions so downstream Skills can trace the gap without guessing.

When another Skill consumes this output, the stable handoff fields are:

- `Use case`, `Fase`, `RAG`, `Model/hosting`
- `Assistant type`, `User group`, `Data sensitivity`, `Readiness status`
- `Routing indicators`
- `Required evidence`
- `Blockers before pilot`
- `Blockers before production`
- `Handoff IDs`

If a route is uncertain, mark it as `needs owner review`; do not silently downgrade it.

## Output format

Respond in **Markdown** using this structure exactly (fill every section):

```markdown
# Compliance intake assessment

## Intake summary
| Field | Assessment |
|---|---|
| Organisatie | |
| Use case | |
| Doelgroep | |
| Fase | |
| RAG | |
| Model/hosting | |

## Classification
- **Assistant type:**
- **User group:**
- **Data sensitivity:**
- **Readiness status:** <one allowed status>

## Routing indicators
| Route | Indicator | Why | Owner |
|---|---|---|---|
| AI Act | | | |
| AVG/GDPR | | | |
| DPIA | | | |
| IAMA | | | |
| Algoritmeregister | | | |

## Required evidence
| Document | Purpose | Owner | Status |
|---|---|---|---|
| | | | |

## Blockers before pilot
- ...

## Blockers before production
- ...

## Open questions
- ...

## Next actions by owner
| Handoff ID | Owner | Next action | Due date |
|---|---|---|---|
| | | | |

This is not legal approval. It is a structured compliance assessment aid that identifies evidence, risks, and gaps for owner review.
```

Keep the full output under ~800 words unless the user asks for detail.

## What to avoid

- Do not claim legal approval or that a legal owner has approved the assistant.
- Do not request or expose real personal data, credentials, API keys, private documents, or kubeconfigs.
- Do not treat public RAG sources as automatically correct or current.
- Do not allow decision-making claims to be hidden behind "informational" wording.
- Do not invent satisfied evidence — mark unknowns as gaps.

## Framework grounding

- [onegov2 — compliance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/compliance.md)
- [onegov2 — governance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/governance.md)
- [onegov2 — ethics and human rights domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/ethics-human-rights.md)
- [onegov2 — user experience domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/user-experience.md)
- [onegov2 — data quality governance practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/data-quality-governance.md)
- [onegov2 — RAG pipeline practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/rag-pipeline.md)
- [Common Ground integration notes](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/integrations/common-ground.md)
- [ADC raamwerk — risicobeoordeling AI](https://github.com/ADC-Consulting/raamwerk-digitale-assistent)
