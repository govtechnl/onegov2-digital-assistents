---
name: public-sector-assistant-test-design
description: Design practical test cases for public-sector digital assistants before launch or review, including answer quality, source grounding, safety, privacy, prompt injection, AI transparency, and human handoff behavior.
---

# Public Sector Assistant Test Design

Use this Skill to create practical test cases for a public-sector digital assistant before launch, pilot, review, or regression testing. The goal is to turn service risks, source materials, and known assistant behavior into concrete tests with expected outcomes. Keep the work focused on test design, not broad governance advice or full audit scoring.

## When to use this Skill

Use this Skill when the user asks to:

- Create acceptance tests, regression tests, red-team tests, or evaluation prompts for a public-sector assistant.
- Turn a service description, source corpus, policy, or previous audit finding into test cases.
- Check answer quality, grounding, privacy, prompt injection, refusal behavior, AI transparency, or handoff behavior through examples.
- Prepare test scenarios for a launch review, pilot, procurement review, or demo.

## Repository resources

When these files exist in the repository, use them to ground the test criteria:

- [Answer quality](../../content/domains/answer-quality.md): correctness, completeness, relevance, plain language, and measurable evaluation.
- [Security](../../content/domains/security.md): prompt injection, API/tool access, secrets, misuse prevention, output filtering, and audit logging.
- [Compliance](../../content/domains/compliance.md): applicable law, policy, standards, demonstrable compliance, and closure of findings.

Use the service owner's official sources and user-provided documents as the authority for expected answers. If key artifacts are missing, create tests only for the evidence available and list missing evidence separately.

## Inputs to inspect

Ask for or inspect the minimum inputs needed:

- Assistant purpose, audience, jurisdiction, scope, and user impact.
- Official source pages, policy documents, FAQs, forms, or knowledge-base entries.
- Sample answers, previous incidents, known failure modes, audit findings, or complaint examples.
- Prompt, retrieval, tool/API, personal-data, refusal, and handoff behavior if available.
- Launch phase: proof of concept, pilot, or production.

## What to do

1. **Set test scope.** State the service, assistant capability, audience, jurisdiction, sources, and launch phase being tested.
2. **Classify impact.** Use low, medium, high, or critical based on rights, obligations, eligibility, legal status, safety, health, finances, personal data, or access to essential public services.
3. **Choose test types.** Cover ordinary use, edge cases, source-grounding traps, privacy probes, prompt injection, refusal, AI disclosure, and human handoff where relevant.
4. **Write concrete test cases.** Each test needs a user prompt, setup or source reference, expected assistant behavior, risk area, severity, and pass criteria.
5. **Add negative tests.** Include cases where the assistant should refuse, ask a clarifying question, say it cannot verify the answer, or hand off to a human.
6. **Avoid fake certainty.** If sources, prompts, tool permissions, or handoff rules are missing, record the evidence gap instead of inventing an expected behavior.

## Test checklist

### Answer quality and plain language

- Ordinary citizen question with a clear source-backed answer.
- Ambiguous question that should trigger a clarifying question or bounded guidance.
- Question from a stressed or low-literacy user; expected answer should use plain-language or B1-level clarity.
- Formatting check for short paragraphs, lists, descriptive links, and assistive-technology-friendly output.

### Source grounding and hallucination control

- Question where the source gives a precise condition, deadline, fee, exception, or next step.
- Question where the source is silent; assistant should not invent details.
- Question where rules vary by date, location, household, income, status, or user group.
- Question with conflicting or stale sources; assistant should explain uncertainty and prefer current approved sources.

### Safety, refusal, and human handoff

- Request for harmful, fraudulent, illegal, or unauthorized action.
- Request for a binding official decision, case-specific legal advice, or guaranteed entitlement.
- Urgent safety, housing, health, deadline, or essential-service scenario requiring human or official-channel handoff.
- User confusion or repeated failure to complete the process through self-service.

### Personal data protection

- User offers BSN/national ID, credentials, one-time codes, full identity documents, or someone else's personal data.
- User asks the assistant to access or change case data without verification.
- User asks whether chat data is logged, retained, reviewed by humans, or used for improvement.
- Assistant should direct identity verification and case handling to secure official channels.

### Security and prompt injection

- Retrieved document or uploaded file contains instructions to ignore policies, reveal prompts, change citations, or exfiltrate data.
- User asks for internal prompts, system rules, credentials, logs, or hidden source content.
- Tool/API action requires confirmation, least privilege, and auditability.
- Assistant should treat untrusted content as data, not instructions.

### Compliance, authority, and AI transparency

- User asks whether they are talking to an AI or a human.
- User asks for an appeal, complaint, correction, or human review route.
- User asks a cross-jurisdiction or out-of-scope question.
- Assistant should distinguish general information from official decisions and state its limits.

## Output format

Use this structure unless the user asks for another format:

```markdown
## Public-Sector Assistant Test Set

**Scope:** <assistant, service, audience, jurisdiction, sources reviewed>
**Impact level:** low | medium | high | critical
**Test focus:** <answer quality, grounding, safety, privacy, security, compliance, handoff>

### Summary
- <what this test set covers>
- <highest-risk behavior tested>
- <main evidence gaps, if any>

### Test cases
| ID | Area | Scenario and prompt | Source or setup | Expected behavior | Severity | Pass criteria |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | <area> | <scenario plus user prompt> | <source, policy, state, or missing evidence> | <what the assistant should do> | critical/high/medium/low | <observable pass condition> |

### Negative and abuse tests
1. <prompt> -> <expected refusal, safe completion, or handoff>

### Evidence gaps
- <missing source, prompt, tool permission, handoff rule, or policy needed to complete testing>

### Suggested regression set
- <small subset to run every release>
```

## Quality bar

- Tests should be realistic enough that a service owner recognizes the scenario.
- Expected behavior must be traceable to reviewed sources, observed behavior, or documented policy.
- Use synthetic examples only; do not include real personal data.
- Include both normal-use and failure-mode tests.
- Apply stricter evidence and testing requirements to assistants that affect rights, obligations, eligibility, legal status, safety, health, finances, or access to essential public services.

## What to avoid

- Do not write generic prompts that do not test a specific behavior.
- Do not invent policy, legal requirements, source content, tool permissions, or personal data.
- Do not create only happy-path tests.
- Do not treat a refusal as passing unless it is the correct behavior for the scenario.
- Do not make tests so broad that pass/fail cannot be observed.
