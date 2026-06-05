# The RAG golden dataset

Read this to build the dataset everything else depends on. A golden dataset is a curated collection of questions with their "ideal answers" — and for RAG, the **expected sources** per question — against which you test every change to prompts, models, or the pipeline. It either grows with reality or goes stale within months.

## What makes it a *RAG* golden dataset

A general golden set has questions and ideal answers. A RAG golden set adds, **per question, the documents/chunks that should be retrieved**. That extra column is what lets you evaluate retrieval on its own — "did the system find the right sources?" — separately from "was the final answer good?". Without expected sources you can only judge the end answer, and you can't tell whether a failure is in retrieval or in generation.

## Building it

- **Seed from what exists.** If the assistant replaces a manual process, use existing Q&A pairs, curated cases, or historical email answers as the starting set. Don't start from zero.
- **Cover the obvious *and* the edge cases.** Have domain experts write both. A set of only average questions measures only the easy part; exceptions, sensitive situations, and legal edges are where the assistant breaks and where the dataset earns its value.
- **Expand with AI under human review.** An LLM can generate variants — paraphrases, minor language variation, malformed phrasings — but every generated sample must be validated by a human before it enters the set. An unreviewed generated set tests the model that produced it, not reality.
- **Build with diverse stakeholders.** Engineers can't do it alone; domain experts, product managers, and users must be involved early for label curation and ground truth. A dataset with no user perspective misses exactly the signals that matter.

## Maintaining it

- **Treat it as a living document.** Feed real-world edge cases and discovered bugs back to domain experts for validation, and add them to the set.
- **Version it like code.** Keep it in a repository with PR review on new samples and version labels on runs — otherwise you can't tell what a "better" result is being compared against.
- **Keep it out of training data.** If you fine-tune, the evaluation set must not be in the training set, or you are testing on data the model has already seen — a common and dangerous mistake.
- **Document ownership in a RACI matrix.** Who defines "good", who builds the set, who curates it, who runs evaluations? Without an explicit split the work falls through the cracks and the dataset goes quiet.

## Record shape

See `templates/rag-golden-dataset.example.yaml`. Each entry should carry at least: an id, the question, the ideal answer, the expected source(s)/chunk(s), tags (e.g. edge_case, sensitive, legal), and a last-validated date. Tags let you report quality per slice (e.g. faithfulness on sensitive cases specifically).

## Sources

- Overheidsbrede handreiking Generatieve AI (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai
- RAGAS (uses question / answer / contexts / ground-truth structure): https://docs.ragas.io/
