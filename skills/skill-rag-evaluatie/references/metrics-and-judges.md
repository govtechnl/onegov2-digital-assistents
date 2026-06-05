# RAG metrics and LLM-judges

Read this to choose what to measure and how to score it reliably. The golden thread: measure **retrieval** and **generation** separately, score with **simple, calibrated** judges, and run it as an automated gate.

## Retrieval metrics (did it fetch the right sources?)

Scored against the expected sources in the golden dataset — independent of the language model.

- **Recall@k** — of the documents that *should* have been retrieved, how many appeared in the top k? The key metric: if the right source isn't retrieved, the model cannot ground on it.
- **Precision@k** — of the top k retrieved, how many were actually relevant? High precision keeps noise (and tokens) down.
- **MRR / nDCG** — ranking quality: is the right source near the top, not just present somewhere?
- **Context precision / context recall** (RAGAS framing) — how much of the retrieved context is relevant, and how much of the needed context was retrieved.

Weak retrieval metrics point you back to the `rag-pijplijn` knobs: chunking, embedding model, hybrid weights, reranking, top-k, thresholds.

## Generation metrics (is the answer good, given the context?)

- **Faithfulness / groundedness** — does every claim in the answer follow from the retrieved context, with nothing invented? This is the direct measure of hallucination, and usually the most important metric for government use.
- **Answer relevancy** — does the answer actually address the question?
- **Answer correctness** — does it match the ideal answer (where you have one)?
- **Citation correctness** — do the cited sources actually support the statements?

Good retrieval but weak faithfulness → fix the grounding prompt or the generation model, not the retriever.

## LLM-judges, kept honest

- **Binary scoring by default** (good / not good) with a clear definition of each. Numeric scales sound precise but calibrate worse.
- **One judge, one dimension.** Separate judges for faithfulness, relevance, tone, compliance — a single all-in-one judge prompt is inconsistent and unexplainable.
- **Calibrate against humans.** A QA analyst and the judge score the same ~100-case sample; adjust the judge prompt until they converge. Re-check periodically.
- **Aggregate** multiple runs or multiple models to reduce stochastic noise.
- **Surface, don't decide.** Use judges to flag the doubtful cases fast, then have a human adjudicate those — that keeps human review manageable rather than replacing it.
- **Version judge prompts as code.** They are measurement instruments; a change shifts all historical numbers, so it belongs in Git with PR review, not a vendor UI.

## Frameworks (don't build your own)

- **RAGAS** — faithfulness, answer relevancy, context precision and context recall out of the box.
- **DeepEval** — "Pytest for LLMs"; integrates into CI/CD for gating.
- **Langfuse / LangWatch** — tracing with integrated judges, useful for both offline and online evaluation.

## Offline vs. online, and the CI gate

- **Offline** = a fixed question set run *before* production. Start with 20–50 representative questions; automate it; run it on every prompt, model, or index change. This is the minimum CI for an LLM system.
- **Online** = measuring with real users in production (feedback, deviation rates, escalations). It becomes the continuous compass once the system is live.
- Both at once in PoC is overkill; online-only in production is irresponsible. In production, offline stays a gate and online runs continuously.
- Capture production failures (thumbs-down, rejected actions), label them, and feed them back into the golden dataset and the judge prompts.

## Sources

- RAGAS: https://docs.ragas.io/
- DeepEval: https://deepeval.com/
