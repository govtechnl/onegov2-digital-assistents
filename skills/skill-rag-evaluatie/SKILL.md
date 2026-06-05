---
name: rag-evaluatie
description: "Use this skill whenever a developer is building, testing, tuning, or trying to trust a Retrieval-Augmented Generation (RAG) solution and needs to know whether it actually works — separating whether retrieval finds the right sources from whether the generated answer is correct and grounded. It covers building a RAG golden dataset (questions with ideal answers AND expected sources), retrieval metrics versus generation/faithfulness metrics, LLM-judges (kept simple and calibrated against humans), and offline validation as a CI gate before production. Triggers include 'evaluate RAG', 'RAG evaluation', 'RAGAS', 'faithfulness', 'groundedness', 'hallucination', 'retrieval recall', 'retrieval precision', 'is my RAG any good', 'golden dataset', 'LLM judge', 'offline evaluation', 'regression test for the assistant', 'context precision', 'context recall', or any work measuring or improving the quality of a retrieval-augmented assistant. It is RAG-scoped — pair it with the rag-pijplijn skill, which builds the pipeline this skill measures."
---

# Evaluating a RAG solution

You cannot claim a RAG system is good without measuring it, and a demo that works proves almost nothing — a single prompt change can silently break ten other questions. This skill makes RAG quality measurable. Its central principle: **evaluate retrieval and generation separately.** "Did the system fetch the right sources?" and "is the generated answer correct and grounded in them?" are different questions with different failure modes — a right answer drawn from the wrong sources, and a wrong answer despite the right sources, both need catching, and only a split evaluation finds them.

## The golden dataset is the foundation

Everything here rests on a curated **golden dataset**: questions with their ideal answers — and, for RAG specifically, the **expected sources/chunks per question**, so you can score retrieval on its own. Key practices (detail in `references/golden-dataset.md`):

- **Seed from what exists.** If the assistant replaces a manual process, start from historical Q&A pairs, curated cases, or past email answers — don't build from zero.
- **Experts author the edge cases.** A set of only average questions measures only the easy part; exceptions, sensitive situations, and legal edges reveal where the assistant breaks.
- **Expand with AI, but validate every sample with a human.** An LLM can generate paraphrases and variants, but an unreviewed generated set tests the model that made it, not reality.
- **Add the expected sources per question.** Map which documents/chunks *should* be retrieved for each input — this is what lets you evaluate retrieval independently of the final answer.
- **Treat it as a living document, versioned like code.** Feed production failures back in; version the set with PR review so you always know what you're comparing against. Document ownership in a RACI matrix and build it with diverse stakeholders (engineers can't do it alone).

Start from `templates/rag-golden-dataset.example.yaml`.

## Two layers of metrics

Score the two halves separately (definitions and tooling in `references/metrics-and-judges.md`):

- **Retrieval** — did it fetch the right chunks? Recall@k and precision@k against the expected sources, plus ranking measures (MRR, nDCG) and context precision/recall. This is independent of the language model.
- **Generation** — given the retrieved context, is the answer **faithful/grounded** (no claims beyond the evidence), **relevant**, and **correct**? Faithfulness/groundedness is the direct measure of hallucination.

Splitting them tells you *where* to fix: weak retrieval metrics → tune chunking/embeddings/hybrid/rerank (the `rag-pijplijn` skill); good retrieval but weak faithfulness → tune the grounding prompt or the generation model.

## LLM-judges for scale (calibrated, not blind)

Humans can't grade thousands of answers a day; LLM-judges can — if you keep them honest:

- **Keep scoring simple — prefer binary** (good / not good) with a clear definition. Five-point scales sound precise but measure unreliably.
- **One judge, one task.** A judge asked to assess correctness, tone, and compliance at once is inconsistent; one judge per dimension is better and explainable.
- **Calibrate against humans.** Have a QA analyst and the judge score the same sample (~100 cases) and adjust the judge prompt until they converge — an uncalibrated judge is a random meter.
- **Aggregate runs** (or multiple models) to cut stochastic noise.
- **Use judges to surface edge cases, not as the sole arbiter** — they flag the doubtful cases that a human then adjudicates, keeping human review manageable (ties to the `menselijke-controle` skill).
- **Version judge prompts as code** (Git, PR review) — a judge prompt is measurement instrumentation; changing it shifts all historical metrics.
- **Use existing frameworks**: RAGAS gives faithfulness, answer relevancy, context precision and context recall out of the box; DeepEval integrates into CI/CD; Langfuse/LangWatch add tracing with judges. Start there rather than building your own.

## Offline validation as a CI gate

- **Start small in PoC** — 20–50 representative questions with ideal answers already catch regressions. Waiting for a perfect dataset is an excuse not to start.
- **Automate it and gate on it.** Run the offline evals on every prompt, model, or index change *before* production — this is the minimum CI pipeline for an LLM system; manual runs get skipped on busy days.
- **Keep the eval set out of any training/fine-tuning data**, or you test the model on data it has already seen.
- **Offline vs. online**: offline dominates in PoC/pilot and stays a gate in production; online (real-user signals) becomes the continuous compass in production. Both at once in PoC is overkill; online-only in production is irresponsible.

## Close the loop from production

Capture negative signals (thumbs-down, rejected actions, complaints), label them, add them to the golden dataset, and use them to sharpen both the pipeline and the judges. An evaluation set that doesn't grow with reality is outdated within months.

## How this fits the rest of the library

- **`rag-pijplijn`** — the pipeline this skill measures; the metrics here point straight back to its knobs.
- **`menselijke-controle`** — judges surface candidates; humans (and domain experts) adjudicate; this is human oversight applied to evaluation.
- The golden dataset, offline-validation, and LLM-judge practices generalise beyond RAG, but here they are scoped to retrieval-augmented assistants.

## Sources

- RAGAS (faithfulness, answer relevancy, context precision/recall): https://docs.ragas.io/
- DeepEval ("Pytest for LLMs"): https://deepeval.com/
- E5-NL embeddings (Dutch retrieval): https://huggingface.co/models?search=e5-nl
- Overheidsbrede handreiking Generatieve AI (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai
