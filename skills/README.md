# Skill library

This submission uses a hybrid Approach A/B for responsible public-service digital assistants:

- domain Skills for answer quality, RAG/source governance, behavior testing, compliance intake, evidence packs, and developer release gates;
- a router Skill that selects and composes the smallest useful Skill set for the user task;
- a validator Skill for challenge readiness, portability, consistency, framework grounding, and demo evidence.

The Skills are portable `SKILL.md` files. They do not require kagent, Kubernetes, GitHub, or a specific coding assistant for their core behavior.

## Skill catalogue

| Skill | Purpose |
|---|---|
| `citizen-service-answer-quality` | Reviews or drafts citizen-facing answers for source grounding, plain Dutch/B1, uncertainty, refusal behavior, human handoff, and launch blockers. |
| `rag-source-readiness-governance` | Checks RAG sources for ownership, authority, freshness, metadata, citation precision, no-answer behavior, Common Ground provenance, and NL API Strategie/API contracts. |
| `public-service-assistant-test-design` | Produces release, regression, adversarial, accessibility, handoff, and source-failure tests with observable pass criteria. |
| `compliance-intake-assessment` | Routes a digital-assistant use case across AI Act, AVG/GDPR, DPIA, IAMA, Algoritmeregister, governance, and required evidence. |
| `compliance-evidence-pack-generator` | Turns intake findings into an auditable evidence pack with controls, gaps, owners, and next actions. |
| `developer-compliance-gate` | Converts evidence gaps into implementation tasks, acceptance criteria, release gates, logging, monitoring, rollback, and security work. |
| `responsible-assistant-skill-router` | Entry point for selecting and composing Skills, maintaining handoff state, normalizing statuses, and producing readiness decisions. |
| `skill-library-validator` | Reviews the Skill library itself for mechanical format, modularity, government standards, framework grounding, consistency, safety, and submission readiness. |

## Recommended entry point

Use `responsible-assistant-skill-router` when the request spans more than one domain or when the right Skill is unclear. It runs the full readiness flow only for explicit pilot, launch, end-to-end, or demo requests; otherwise it routes to the smallest useful Skill set.

## Naming

Each Skill directory name matches the frontmatter `name` field. The `_template/` folder remains only as the starter template from the challenge repository.
