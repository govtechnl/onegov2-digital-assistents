---
name: public-sector-rag-source-governance
description: Prepare and govern source materials for public-sector RAG assistants before implementation, pilot, or release, including source ownership, freshness, versioning, retrieval readiness, citation requirements, and evidence gaps.
---

# Public Sector RAG Source Governance

Use this Skill to prepare the source base for a public-sector retrieval-augmented generation (RAG) assistant before implementation, pilot, release, or content refresh. The goal is to make source ownership, quality, freshness, versioning, citation behavior, and retrieval readiness explicit before the assistant answers citizens or civil servants. Keep the work focused on sources and retrieval readiness, not full assistant audit, model selection, or production infrastructure design.

## When to use this Skill

Use this Skill when the user asks to:

- Prepare official documents, web pages, FAQs, procedures, or policy sources for a RAG-based public-sector assistant.
- Create a source register, freshness plan, versioning rules, citation requirements, or retrieval-readiness checklist.
- Decide whether sources are ready for ingestion, pilot use, or release.
- Identify source gaps, stale documents, conflicting rules, unsupported topics, or missing owners.
- Define test questions for source coverage, retrieval precision, and citation quality.

## Repository resources

When these files exist in the repository, use them to ground the work:

- [RAG pipeline](../../content/practices/rag-pipeline.md): citable retrieval, source coverage, source precision, chunking, re-ranking, and no-answer behavior.
- [Data quality and governance](../../content/practices/data-quality-governance.md): ownership, freshness, completeness, accuracy, quarantine, and release pairing.
- [Infrastructure and data](../../content/domains/infrastructure-data.md): robust data flows, trustworthy sources, quality checks, and data lineage.
- [Answer quality](../../content/domains/answer-quality.md): factual correctness, relevance, completeness, plain language, and measurable evaluation.
- [Compliance](../../content/domains/compliance.md): applicable law, policy, standards, demonstrable compliance, and closure of findings.

Use the service owner's official documents as the authority. If a needed source, owner, or policy is missing, record the gap instead of inventing rules.

## Inputs to inspect

Ask for or inspect the minimum evidence needed:

- Assistant purpose, audience, jurisdiction, scope, and launch phase.
- Candidate source list: URLs, document paths, titles, owners, effective dates, review dates, and versions.
- Known high-impact topics: eligibility, deadlines, legal status, money, safety, identity, sanctions, rights, duties, and essential services.
- Source update process: owner, review cadence, publication workflow, archive rules, and emergency update path.
- Retrieval design facts if available: chunking, metadata, embeddings, re-ranking, filters, citation format, and no-answer fallback.
- Existing evaluation questions, failed answers, analytics, complaints, or content gaps.

## What to do

1. **Set scope.** State the assistant, service, audience, jurisdiction, source types, and launch phase.
2. **Create a source register.** For each source, record title, owner, authority level, URL or path, version/effective date, review cadence, topics covered, and known limits.
3. **Classify source risk.** Mark low, medium, high, or critical based on whether wrong or stale source use could affect rights, obligations, eligibility, legal status, health, safety, finances, personal data, or access to essential public services.
4. **Check readiness gates.** Identify blockers before ingestion or release, especially missing owner, stale source, conflicting sources, missing citation target, unclear jurisdiction, or unsupported high-impact topic.
5. **Define retrieval metadata.** Recommend metadata fields needed for filtering, citation, freshness, jurisdiction, topic, document type, language, version, and owner.
6. **Design coverage tests.** Create practical questions that prove the retriever can find the right source, avoid wrong sources, cite precisely, and say when it cannot verify an answer.
7. **Decide readiness.** Conclude whether the source base is ready, ready with monitoring, not ready, or insufficient evidence.

## Readiness gates

Mark the source base as **not ready** when any of these apply:

- A high-impact source has no named owner or review process.
- A source is stale, superseded, draft-only, unofficial, or conflicts with a more authoritative source.
- A high-impact topic has no approved source but the assistant is expected to answer it.
- Citations cannot point to stable source identifiers, sections, pages, URLs, versions, or effective dates.
- Source metadata cannot distinguish jurisdiction, date, audience, program, document type, language, or authority where those differences matter.
- The retrieval process has no no-answer behavior for missing, conflicting, or low-confidence sources.
- Personal data, secrets, internal-only content, or case-specific data would be ingested without an approved purpose and access control.

## Practical checklist

### Source authority and ownership

- Is each source official, approved, and appropriate for the assistant's scope?
- Is there a named source owner or steward?
- Is the source public, internal, confidential, or restricted?
- Does the source have a clear version, effective date, or publication date?
- Are draft, archived, or superseded materials excluded or clearly marked?

### Freshness and lifecycle

- How often must each source be reviewed?
- What event triggers an urgent update, such as a law change, form change, fee change, or contact-channel change?
- How are stale sources quarantined and re-enabled?
- Can a release be traced to the exact source set it was tested against?
- Are source changes connected to release notes or regression tests?

### Retrieval and citation readiness

- Can sources be chunked without losing legal conditions, exceptions, tables, dates, or definitions?
- Which metadata fields must be attached to each chunk?
- Does the citation format let reviewers verify the exact source used?
- Are there test questions for source coverage and source precision?
- Does the assistant know what to do when retrieval returns no relevant source?

### Coverage and gaps

- Which expected user topics are fully covered, partially covered, or unsupported?
- Are high-impact topics covered by primary sources rather than summaries?
- Are exceptions, eligibility limits, deadlines, fees, forms, and contact channels covered?
- Are multilingual, accessibility, or plain-language source needs identified?
- Are gaps recorded as "do not answer", "handoff", or "needs source owner decision"?

### Compliance and data protection

- Are legal, policy, and records-management constraints identified where relevant?
- Are personal data and sensitive data excluded unless there is an approved purpose and secure access path?
- Are internal-only sources separated from public-facing sources?
- Are retention, logging, and access expectations clear for source ingestion and retrieval traces?
- Is AI output clearly constrained to source-backed information for high-impact topics?

## Output format

Use this structure unless the user asks for another format:

```markdown
## Public-Sector RAG Source Governance

**Scope:** <assistant, service, audience, jurisdiction, launch phase>
**Readiness:** ready | ready with monitoring | not ready | insufficient evidence
**Highest source risk:** low | medium | high | critical

### Summary
- <main readiness conclusion>
- <main source blocker or gap>
- <most important next action>

### Source register
| Source and version | Owner and authority | Topics and limits | Risk and status | Notes |
| --- | --- | --- | --- | --- |
| <title, URL/path, date/version> | <owner or missing; official/internal/draft/etc.> | <topics covered and known limits> | <critical/high/medium/low; ready/gap/blocker> | <freshness, citation, or evidence notes> |

### Findings and required fixes
| Severity | Finding and evidence | Required fix and acceptance criterion |
| --- | --- | --- |
| critical/high/medium/low | <source issue with artifact or missing evidence> | <fix plus testable pass condition> |

### Retrieval metadata
- <metadata field>: <why it is needed>

### Coverage tests
1. <user question> -> <expected source, citation behavior, and answer/no-answer behavior>

### Evidence gaps
- <missing source, owner, effective date, policy, metadata, or test evidence>
```

## Quality bar

- Each source recommendation should be traceable to a reviewed artifact, owner statement, or documented gap.
- Use primary, official, current sources for high-impact topics.
- Apply stricter evidence and freshness requirements to topics that affect rights, obligations, eligibility, legal status, health, safety, finances, personal data, or access to essential public services.
- Treat missing evidence as a source-readiness issue, not as permission to guess.
- Keep the source register small enough that a service owner can maintain it.

## What to avoid

- Do not approve a source base because the assistant demo answer looks good.
- Do not invent source owners, effective dates, policy rules, or review cadences.
- Do not mix public and internal sources without access and citation rules.
- Do not ingest stale, draft, archived, or unofficial content for high-impact answers unless clearly restricted and labelled.
- Do not create tests that only check whether some source was retrieved; test whether the correct source was retrieved and cited.
