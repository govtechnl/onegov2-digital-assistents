---
name: skill-library-validator
description: Use when reviewing one or more government digital assistant SKILL.md files for challenge readiness, tool independence, framework grounding, consistency, modularity, and concrete outputs before PR submission.
---

## When to use this Skill

Use this Skill before submitting a Skill library PR, when reviewing another team's Skills, or when checking whether a set of Skills can be composed into a responsible government digital assistant workflow.

Trigger on requests such as "validate these skills", "is this submission ready", "review our SKILL.md files", "challenge readiness", or "check consistency".

## Inputs to inspect

- Each `skills/<name>/SKILL.md` file in scope
- The PR description, demo script, or pitch summary if available
- Any referenced support files, examples, scripts, or tests
- The relevant framework source links under `content/domains/`, `content/practices/`, and `docs/integrations/`

If a file or referenced source is unavailable, continue with the available evidence and mark the missing item as an evidence gap.

## What to do

1. Check mechanical readiness: directory/name match, YAML frontmatter, useful `description`, concrete body, valid links, no unnecessary tool-specific syntax.
2. Check framework grounding: each Skill must link to and operationalize at least one relevant framework domain or practice. Prefer direct links to specific `content/` files.
3. Check tool independence: instructions should work in Codex, Claude Code, Cursor, Windsurf, or similar tools without relying on one product's syntax.
4. Check usefulness: each Skill should produce a concrete artifact, decision, runnable test set, issue list, evidence pack, assistant-behavior audit, or implementation output.
5. Check consistency: shared status vocabularies, owner roles, control names, severity labels, and handoff fields must not contradict each other.
6. Check modularity: each Skill should do one job; any composition Skill must clearly state which Skills it composes and how outputs flow between them.
7. Check public-sector safety: no real personal data, secrets, legal approval claims, hidden automated decision-making, or unsupported production-readiness claims.
8. Check traceability: intake gaps, evidence rows, and developer issues should preserve stable IDs or clearly generate them.
9. Check demo evidence: the submission should be able to show the GitHub Skill source, the runtime-loading mechanism, and the live specialist agents without making the Skill content dependent on Kubernetes.
10. Check government-standards bonus coverage: NL API Strategie and Common Ground should be referenced where API, retrieval, provenance, or source-of-truth behavior is relevant.
11. Check usability for non-framework experts: a developer or product owner should be able to follow the Skill without first reading the full framework.
12. Check direct assistant behavior coverage: citizen-facing Skills and composition Skills should include refusals, citations, unsupported guarantee handling, source uncertainty, human handoff, prompt-injection from retrieved content, and credential/DigiD refusal where relevant.
13. Check test design coverage: the library should include practical normal, edge, negative, privacy, source-grounding, prompt-injection, human handoff, AI-transparency, and regression tests.
14. Check RAG source governance coverage: the library should make source ownership, authority, freshness, metadata, citation precision, no-answer behavior, Common Ground provenance, and NL API Strategie/API-contract expectations explicit.
15. Score readiness and list the smallest set of fixes needed before submission.

## Output format

Use this exact Markdown structure:

```markdown
# Skill library validation

## Overall verdict
<ready for PR | ready with minor fixes | not ready>

## Scorecard
| Criterion | Status | Evidence | Fix needed |
|---|---|---|---|
| Mechanical format | pass/partial/fail | | |
| Framework grounding | pass/partial/fail | | |
| Tool independence | pass/partial/fail | | |
| Usefulness | pass/partial/fail | | |
| Consistency | pass/partial/fail | | |
| Modularity | pass/partial/fail | | |
| Traceability | pass/partial/fail | | |
| Demo evidence | pass/partial/fail | | |
| Government standards | pass/partial/fail | | |
| Usable without framework knowledge | pass/partial/fail | | |
| Assistant behavior coverage | pass/partial/fail | | |
| Test design coverage | pass/partial/fail | | |
| RAG source governance | pass/partial/fail | | |
| Public-sector safety | pass/partial/fail | | |

## Per-skill findings
| Skill | Strongest point | Risk or gap | Required fix |
|---|---|---|---|
| | | | |

## Composition check
- <how outputs flow between Skills>
- <status vocabulary or handoff mismatch, if any>
- <whether a developer without framework knowledge can use the set>

## Submission fixes
1. <highest-value fix before PR>

## Demo evidence to show the jury
- <one concrete artifact or behavior to show>

This validation reviews Skill quality and challenge readiness. It is not legal, security, privacy, or accessibility approval.
```

## Quality bar

- Prefer concrete, fixable findings over broad advice.
- Treat a missing framework link as a real submission gap.
- Treat unsupported "approved", "compliant", or "production ready" wording as a safety issue.
- Treat missing launch-blocker coverage as a real quality gap for any public-facing assistant Skill.
- Treat missing negative/regression tests as a real quality gap when a submission claims release or pilot readiness.
- Treat missing source ownership, freshness, citation, or no-answer rules as a real RAG-readiness gap.
- Treat answers that request DigiD, passwords, one-time codes, or other credentials as launch blockers.
- Treat unsupported eligibility, approval, rejection, fine, or entitlement guarantees as launch blockers.
- Treat retrieved-content prompt injection as in scope: a strong Skill must tell the assistant to ignore unsafe instructions found in retrieved documents.
- A composition Skill is a bonus only when it actually composes outputs from smaller Skills.
- A kagent demo is useful evidence of delivery and orchestration, but the Skills must remain portable outside Kubernetes.

## What to avoid

- Do not fail a Skill only because it is concise.
- Do not require a specific coding tool, model, cluster, or cloud provider.
- Do not bless a submission that is only a generic checklist without actionable output.
- Do not invent test results in tools the team did not actually use.

## Framework grounding

- [onegov2 — skill checklist](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/skill-checklist.md)
- [onegov2 — skill format](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/docs/skill-format.md)
- [onegov2 — compliance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/compliance.md)
- [onegov2 — governance domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/governance.md)
- [onegov2 — security domain](https://github.com/govtechnl/onegov2-digital-assistents/blob/main/content/domains/security.md)
