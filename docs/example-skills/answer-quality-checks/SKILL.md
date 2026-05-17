---
name: answer-quality-checks
description: Review the output of a government digital assistant against the Raamwerk Digitale Assistenten "Answer Quality" domain. Use when the user asks the agent to evaluate, audit, or improve an assistant's responses, RAG output, or refusal behaviour. Produces a structured review with required fixes and source-coverage findings.
---

# Answer Quality Checks

A review Skill for digital assistants built by Dutch government organisations. It applies the Answer Quality domain of the *Raamwerk Digitale Assistenten* to a set of assistant responses and produces a concrete, actionable review.

## When to use this Skill

Trigger this Skill when:

- The user pastes one or more assistant responses (with the originating user query) and asks for a review.
- The user asks the agent to "check the quality" / "audit" / "improve" an assistant's output.
- The user is working on an evaluation set or QA harness for a digital assistant.

Do **not** use this Skill to write new prompts from scratch or to design the assistant's architecture, there are other Skills for that.

## What to do

For each `(user_query, assistant_response)` pair the user provides:

1. **Read the framework context** in [content/domains/answer-quality.md](../../../content/domains/answer-quality.md) so you apply the framework's own vocabulary.
2. **Score the response** against the four quality dimensions:
   - **Factual correctness**, is every factual claim verifiable? Mark unverified claims.
   - **Relevance**, does the response answer the question the user actually asked?
   - **Completeness**, are required caveats, eligibility conditions, deadlines, or contact paths missing?
   - **Plain language**, flag jargon, passive voice, sentences over 20 words, and assumed prior knowledge.
3. **Check source coverage**: every factual claim must cite a source. If the response cites nothing, that is a fail, not a warning.
4. **Check refusal behaviour**: if the retriever returned nothing relevant, the response must say so plainly instead of improvising. See [reference.md](reference.md).
5. **Produce the review** in the structured format below.

## Output format

For each response reviewed, output:

```
### Response N: <one-line summary>

**Verdict:** pass | needs-fix | fail

**Findings**
- Factual: <findings or "OK">
- Relevance: <findings or "OK">
- Completeness: <findings or "OK">
- Plain language: <findings or "OK">
- Source coverage: <findings or "OK">
- Refusal behaviour: <findings or "N/A">

**Required fixes (ordered by severity)**
1. ...
2. ...

**Suggested rewrite (optional)**
> <improved response>
```

End with a one-paragraph summary of patterns across the set (recurring failure modes, suggested upstream fixes in retrieval, prompting, or evaluation).

## Conventions to follow

- Use the framework's terminology (see [content/glossary.yaml](../../../content/glossary.yaml) and [docs/glossary.md](../../glossary.md)).
- Source identifiers must match entries in [content/sources.yaml](../../../content/sources.yaml). If a cited source isn't there, flag it.
- Phases and levels (when relevant) must match [content/filters.yaml](../../../content/filters.yaml).
- If the assistant is for citizens, write findings in B1-level Dutch or English. If it is for civil servants, normal professional register is fine.

## What to avoid

- Do not invent sources to fill missing citations.
- Do not rewrite responses without first listing the findings, the user needs to see the diagnosis, not just the cure.
- Do not score on style alone if the response is factually wrong; correctness dominates.
- Do not mark a refusal as a failure when no relevant source was retrievable.

## Additional resources

- [reference.md](reference.md), refusal patterns, source-coverage worked examples, and edge cases.
- [content/domains/answer-quality.md](../../../content/domains/answer-quality.md), the framework domain.
- [content/practices/rag-pipeline.md](../../../content/practices/rag-pipeline.md), related practice on retrieval and citation.
