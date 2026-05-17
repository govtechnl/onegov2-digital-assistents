# Answer Quality Checks, Reference

Loaded on demand by the agent when the main `SKILL.md` instructions need a deeper example.

## Refusal patterns

A correct refusal acknowledges the limit of the available sources and offers a next step. It does not invent content.

**Good**

> I couldn't find information about XYZ in the documents I have access to. You can check directly with <responsible organisation> or rephrase your question with more context.

**Bad**

> XYZ is generally handled by <made-up answer>. (No source cited, no acknowledgement of uncertainty.)

## Source coverage, worked example

User query: *"How long does a residency permit application take?"*

Assistant response: *"Residency permit applications typically take 6 to 8 weeks. The IND publishes processing times on their website."*

Source coverage findings:

- Claim "6 to 8 weeks" → must cite a specific source with a date. Without a citation, this is a fail.
- Claim "IND publishes processing times" → factual and verifiable; cite the IND processing-times page.
- Tone is plain and the response respects the limit of its knowledge (says "typically"). Pass on plain-language and refusal behaviour.

## Recurring failure modes

If you see these across the set, surface them in the summary paragraph:

- **Citation by URL only**, fine for transparency, but the agent should also reference the canonical `source_id` from `content/sources.yaml` so the framework can track usage.
- **Confident hallucinations on legal questions**, almost always a sign that retrieval is too permissive (returning loosely related documents and the model bridging the gap).
- **Over-refusal on questions about general process**, the assistant refuses safe, broadly-known information because retrieval missed. Tighten the threshold, don't tighten the prompt.
- **Mixed Dutch and English in a single response**, usually a prompt issue (system prompt language doesn't match the channel).

## Mapping to the framework

| Dimension          | Framework reference                                     |
|--------------------|---------------------------------------------------------|
| Factual / relevance / completeness / plain language | [content/domains/answer-quality.md](../../../content/domains/answer-quality.md) |
| Source coverage    | [content/practices/rag-pipeline.md](../../../content/practices/rag-pipeline.md) |
| Refusal behaviour  | [content/domains/answer-quality.md](../../../content/domains/answer-quality.md) + [content/domains/ethics-human-rights.md](../../../content/domains/ethics-human-rights.md) |
| Monitoring follow-up | [content/practices/llmops-monitoring.md](../../../content/practices/llmops-monitoring.md) |
