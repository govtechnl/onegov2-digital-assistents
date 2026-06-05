---
name: responsible-assistant-skill-router
description: Use when a public-service digital-assistant task needs routing across the Skill library, handoff state, or an end-to-end readiness flow. Select only the needed Skills by default; run the full flow only for pilot, launch, or complete responsible-assistant readiness requests.
---

# Responsible Assistant Skill Router

Use this Skill when a user asks for help designing, reviewing, testing, evidencing, or preparing a public-service digital assistant and it is not immediately obvious which individual Skill should be applied.

This Skill is the meta Skill for the library. It is a lightweight orchestration layer, not a runtime engine. It does not require persistent state, automatic function calls, Kubernetes, kagent, GitHub, or a specific agentic coding tool.

Its job is to help an agent:

1. classify the user's request;
2. select the smallest useful set of Skills;
3. run those Skills in a safe order;
4. pass outputs between phases;
5. maintain a temporary handoff table;
6. produce blockers, evidence gaps, developer actions, tests, and a readiness decision.

## Core principle

Do **not** run the full flow by default.

Select only the Skills needed to answer the user's request safely and usefully. Run the full responsible-assistant delivery flow only when the user asks for launch readiness, pilot readiness, end-to-end review, or when the request clearly spans answer behavior, sources, compliance, evidence, and implementation.

If the user explicitly asks for a demo or hackathon walkthrough, and gives a short prompt such as `Doorloop de volledige flow voor onze digitale assistent`, run the full readiness flow using the demo scenario.

**Demo scenario:** municipality pilot for a citizen chatbot covering waste, permits, appointments, and general service information; RAG over public web pages and approved internal FAQ; plain Dutch/B1 target; personal data possible in free-text; hosted LLM; human escalation for legal, case-specific, high-impact, or uncertain questions.

## Available Skill map

When repository access is available, scan `skills/*/SKILL.md` and build a temporary registry from each Skill's `name`, `description`, headings, inputs, and outputs.

When repository access is not available, use this library map:

| Skill | Use when |
|---|---|
| `citizen-service-answer-quality` | The task concerns citizen-facing answer behavior, plain language, citations, uncertainty, refusal behavior, human handoff, no binding decisions, credentials, prompt injection, or launch blockers in assistant responses. |
| `public-service-assistant-test-design` | The task requires test cases, regression tests, adversarial tests, prompt-injection tests, refusal tests, accessibility tests, source-failure tests, or pass/fail criteria. |
| `rag-source-readiness-governance` | The task concerns RAG, source ownership, freshness, citations, source-of-truth rules, public/internal sources, retrieval risk, Common Ground provenance, NL API Strategie/API contracts, or no-answer behavior. |
| `compliance-intake-assessment` | The task concerns legal/compliance routing, AI Act, AVG/GDPR, DPIA, IAMA, Algoritmeregister, launch phase, public-sector risk indicators, or required governance steps. |
| `compliance-evidence-pack-generator` | The task requires an evidence pack, owner table, control status, missing evidence, approval gates, decision log, audit trail, or traceability for compliance/readiness. |
| `developer-compliance-gate` | The task requires converting findings or evidence gaps into developer work, issues, acceptance criteria, logging, monitoring, rollback, release gates, or implementation tasks. |
| `skill-library-validator` | The task concerns validating the Skill library itself for portability, consistency, framework alignment, modularity, overlap, demo evidence, or readiness for submission. |

Do not recursively call this router as a sub-Skill.

## Task classification

Classify the user request into one or more categories:

- `answer_quality`
- `test_design`
- `rag_readiness`
- `compliance_intake`
- `evidence_pack`
- `developer_gate`
- `full_readiness_flow`
- `skill_library_validation`

If the request is ambiguous, make a best-effort classification from the information provided. Do not ask for clarification unless the missing detail prevents any useful output.

## Routing rules

Use these default routes:

| User intent | Selected Skills |
|---|---|
| Review or draft a chatbot answer | `citizen-service-answer-quality` |
| Create release, regression, or red-team tests | `public-service-assistant-test-design` |
| Review a RAG/source setup | `rag-source-readiness-governance` |
| Determine compliance obligations | `compliance-intake-assessment` |
| Create audit/evidence material | `compliance-evidence-pack-generator` |
| Turn gaps into build work | `developer-compliance-gate` |
| Validate the Skill library | `skill-library-validator` |
| Assess pilot or launch readiness | `citizen-service-answer-quality` -> `rag-source-readiness-governance` when sources/RAG are involved -> `compliance-intake-assessment` -> `compliance-evidence-pack-generator` -> `developer-compliance-gate` -> `public-service-assistant-test-design` |
| Run a complete responsible-assistant flow | `citizen-service-answer-quality` -> `rag-source-readiness-governance` -> `compliance-intake-assessment` -> `compliance-evidence-pack-generator` -> `developer-compliance-gate` -> `public-service-assistant-test-design` |

Skip `rag-source-readiness-governance` if the assistant does not use RAG, retrieval, document grounding, official sources, internal knowledge bases, or cited content.

Skip `developer-compliance-gate` if the user only asks for policy, assessment, or review and does not need implementation work.

Skip `public-service-assistant-test-design` unless the user asks for tests, readiness, acceptance criteria, or proof that behavior can be verified.

Include `skill-library-validator` only when the subject is the Skill library itself, not a government assistant implementation.

## Handoff state

Maintain a temporary handoff state during the response. Use this table whenever more than one Skill is selected:

| Phase | Skill | Input used | Output produced | Blockers | Next handoff |
|---|---|---|---|---|---|

Keep the state concise. Do not duplicate full outputs from sub-Skills in the handoff table.

## Standard handoff fields

Use these fields when passing output from one phase to the next:

| Field | Meaning |
|---|---|
| `use_case_summary` | Short description of the assistant, service domain, target users, and intended phase. |
| `target_users` | Citizen, civil servant, case worker, policy team, developer, or other user group. |
| `launch_phase` | Exploration, prototype, pilot, production, or unknown. |
| `risk_indicators` | Rights, benefits, permits, enforcement, sanctions, health, housing, legal deadlines, vulnerable users, personal data, or high-impact decisions. |
| `answer_quality_findings` | Findings about answer behavior, clarity, grounding, uncertainty, refusal, human handoff, unsafe claims, credentials, or launch blockers. |
| `required_tests` | Tests required to verify readiness, safety, refusal, source behavior, privacy, accessibility, handoff, or regression coverage. |
| `rag_source_gaps` | Missing source ownership, freshness, metadata, access rules, citation stability, source-of-truth rules, Common Ground/API provenance, or no-answer behavior. |
| `compliance_obligations` | Relevant AI Act, AVG/GDPR, DPIA, IAMA, Algoritmeregister, organizational governance, or other compliance steps. |
| `evidence_gaps` | Missing proof, owner, approval, test result, log, decision record, source register, or monitoring evidence. |
| `developer_issues` | Implementation tasks with acceptance criteria and release gates. |
| `readiness_status` | One of `ready`, `ready with conditions`, `not ready`, or `insufficient evidence`. |

## Readiness status

Use exactly these readiness statuses in router outputs:

- `ready`
- `ready with conditions`
- `not ready`
- `insufficient evidence`

Apply these rules:

| Condition | Status |
|---|---|
| No blockers and required evidence is present | `ready` |
| No blockers, but minor issues or monitoring actions remain | `ready with conditions` |
| Any launch blocker is present | `not ready` |
| Required information or evidence is missing | `insufficient evidence` |

Do not mark an assistant `ready` based only on a successful demo, attractive UI, or plausible sample answer.

When composing outputs from other Skills, normalize their local statuses into the router readiness status:

| Local status | Router status |
|---|---|
| `pass`, `satisfied`, `passes developer gate`, `ready for exploration`, `conditionally ready for production` | `ready` |
| `needs review`, `partially satisfied`, `passes with conditions`, `conditionally ready for pilot`, `ready with monitoring` | `ready with conditions` |
| `fail`, `missing`, `does not pass developer gate`, `not ready for pilot`, `not ready for production`, `not ready` | `not ready` |
| `unknown`, `missing required evidence`, `insufficient evidence` | `insufficient evidence` |

If a local status could map to more than one router status, choose the more conservative status and explain why.

## Human oversight rule

Human-in-the-loop only counts as a valid mitigation when all of the following are defined:

- escalation trigger
- responsible human role or owner
- authority of the human reviewer
- handoff channel
- expected response time or fallback
- context passed to the human
- audit evidence or log entry

If a high-impact, urgent, legal, case-specific, rights-affecting, financial, housing, health, enforcement, benefits, permits, or vulnerable-user scenario requires escalation and the handoff path is undefined, mark the relevant phase as blocked.

## Execution process

### Step 1 - Understand the request

Extract:

- assistant purpose
- target users
- service domain
- launch phase
- whether RAG/sources are used
- whether personal data may appear
- whether the assistant can affect rights, benefits, permits, enforcement, sanctions, housing, health, legal deadlines, or essential services
- what output the user asked for

If details are missing, state assumptions briefly and continue.

### Step 2 - Select Skills

List the selected Skills and one short reason for each.

Do not select Skills just because they exist. Select them because their output is needed for the user's task.

### Step 3 - Run phases

For each selected Skill:

1. apply the relevant instructions from that Skill;
2. produce only the output needed for the user's task;
3. record blockers and handoff fields;
4. pass useful outputs to the next phase.

Avoid repeating full checklists from sub-Skills unless the user explicitly asks for a detailed version.

### Step 4 - Resolve conflicts

If two Skills produce conflicting conclusions:

- prefer launch blockers over conditional readiness;
- prefer missing evidence over optimistic assumptions;
- prefer current official source readiness over unsupported answer quality;
- prefer human escalation when user-specific, high-impact, legal, or rights-affecting advice is involved;
- prefer concrete tests and acceptance criteria over broad assurance claims.

Explain the conflict briefly in the final output.

### Step 5 - Produce final output

For multi-Skill routes, return:

1. selected Skills;
2. handoff state table;
3. key findings;
4. blockers;
5. evidence gaps;
6. required developer actions, if applicable;
7. required tests, if applicable;
8. readiness decision;
9. next best action.

For single-Skill routes, keep the output focused and do not force the full state table unless useful.

## Output template for full readiness flow

Use this structure for full readiness, pilot readiness, launch readiness, or an explicit demo prompt:

```markdown
# Responsible assistant readiness flow

## Selected Skills
| Skill | Why selected |
|---|---|

## Handoff state
| Phase | Skill | Input used | Output produced | Blockers | Next handoff |
|---|---|---|---|---|---|

## Key findings
### Answer behavior
### Tests and acceptance criteria
### RAG/source readiness
### Compliance routing
### Evidence gaps
### Developer gates

## Launch blockers
| Blocker | Source phase | Required fix | Owner |
|---|---|---|---|

## Developer actions
| Issue | Why it matters | Acceptance criteria | Readiness impact |
|---|---|---|---|

## Required tests
| Test | Prompt or scenario | Expected behavior | Pass criteria |
|---|---|---|---|


## Readiness decision
Status: `ready | ready with conditions | not ready | insufficient evidence`

Reason:

## Next best action
```

Add the optional platform showcase section only when the user asks for a demo, platform showcase, kagent, GitHub, Kubernetes, or k3d:

```markdown
## Optional platform showcase
| Evidence | Value |
|---|---|
| Skill source | https://github.com/felice-navidad/onegov2-digital-assistents |
| Runtime loading | kagent Agent `spec.skills.gitRefs` clones SKILL.md files at startup when used in the demo platform |
| Portability claim | The same Skill files remain usable outside kagent |
```

## Output template for routing-only requests

Use this when the user asks which Skill to use:

```markdown
# Skill routing recommendation

## Recommended route
| Step | Skill | Why |
|---|---|---|

## Skip these Skills
| Skill | Why skipped |
|---|---|

## Suggested prompt
```

## Jury demo prompt pack

Use these prompts when the user asks for a live demo script:

1. `Doorloop de volledige flow voor onze digitale assistent.`
2. `Maak een burgerantwoord op B1-niveau voor een vraag over een vergunning, met bronnen en duidelijke grenzen.`
3. `Ontwerp een compacte regressietestset voor broncitatie, DigiD-veiligheid, eligibility guarantees, human handoff en prompt-injection vanuit opgehaalde content.`
4. `Beoordeel of onze RAG-bronnen klaar zijn voor pilotgebruik, inclusief eigenaarschap, actualiteit, metadata, citaties en Common Ground/NL API Strategie.`
5. `Welke compliance-bewijzen heb ik nodig voor een pilot?`
6. `Maak een compliance evidence pack op basis van deze intake.`
7. `Vertaal dit evidence pack naar concrete developer tasks met acceptance criteria.`
8. `Valideer deze skill library voor challenge readiness.`

## What to avoid

- Do not run every Skill just because it exists.
- Do not claim legal approval, production approval, AI Act approval, or AVG/GDPR approval.
- Do not hide unresolved gaps behind optimistic status wording.
- Do not include real personal data, credentials, private documents, or raw sensitive prompts.
- Do not require kagent, Kubernetes, GitHub, Codex, Cursor, Claude Code, or another specific platform for the core Skill behavior.
- Do not treat human-in-the-loop as a mitigation unless trigger, owner, authority, channel, timing, context, and audit evidence are defined.

## Framework grounding

- [onegov2 challenge repo](https://github.com/govtechnl/onegov2-digital-assistents)
- [onegov2 skill checklist](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/skill-checklist.md)
- [onegov2 - answer quality domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/answer-quality.md)
- [onegov2 - compliance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/compliance.md)
- [onegov2 - governance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/governance.md)
- [onegov2 - security domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/security.md)
- [onegov2 - RAG pipeline practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/rag-pipeline.md)
- [onegov2 - data quality governance practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/data-quality-governance.md)
- [onegov2 - LLMOps and monitoring practice](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/practices/llmops-monitoring.md)
- [Common Ground integration notes](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/integrations/common-ground.md)
- [NL API Strategie integration notes](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/integrations/nl-api-strategie.md)
