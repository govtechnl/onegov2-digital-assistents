---
name: rag-pijplijn
description: "Use this skill whenever a developer is building, designing, or improving a Retrieval-Augmented Generation (RAG) solution — any assistant that answers from a knowledge base, document store, or retrieved sources rather than from the model's own weights. It covers the full pipeline: source and data quality, chunking and indexing, embeddings, hybrid retrieval and reranking, tiered retrieval, and grounded, source-cited generation — tuned for (Dutch) government use. Triggers include 'RAG', 'retrieval augmented generation', 'retrieval-augmented', 'kennisbank', 'knowledge base', 'document search', 'vector database', 'vectordatabase', 'embeddings', 'chunking', 'semantic search', 'hybrid search', 'BM25', 'reranking', 'grounding', 'bronvermelding', 'ground answers in documents', or building an assistant that answers from a corpus of documents, FAQs, or legislation. It does NOT trigger for assistants that do not retrieve from a knowledge source. For measuring whether the RAG actually works, pair it with the rag-evaluatie skill."
---

# Building a quality RAG pipeline

Retrieval-Augmented Generation is the standard architecture for an assistant that must answer from current, trustworthy sources rather than from a model's frozen weights. The single most important thing to internalise: **a RAG system's quality depends far more on the data and the retrieval than on the language model.** RAG systems fail more often from poor data engineering and weak retrieval than from a weak model. Spend your effort accordingly.

## The pipeline at a glance

`sources → ingest & chunk → embed & index → retrieve (hybrid + rerank) → ground & cite → answer`, with **evaluation wrapped around the whole thing**. This skill covers building it; measuring it is the `rag-evaluatie` skill, and you cannot claim quality without it.

- How to retrieve well (chunking, embeddings, vector store, hybrid search, reranking, tiered retrieval, efficiency): `references/building-the-pipeline.md`.
- How to keep it trustworthy (source quality, lineage, grounding, citations, and the security of retrieved content): `references/sources-grounding-and-safety.md`.

## Start with the sources, not the model

The assistant is only as good as its sources. Before tuning retrieval:

- **Curate an authoritative source whitelist.** Index only approved, authoritative sources — not "whatever we can crawl". (The overheid.nl team, for instance, works from a small set of governed sources rather than the open web.)
- **Be wary of websites as a source.** Municipal and government websites *look* authoritative, but ungoverned content and poor content management often make their quality and reliability insufficient in practice. Prefer governed, structured sources.
- **Get domain experts involved — this is the real bottleneck.** Insufficient domain expertise is the most common thing that wrecks a RAG project (and its evaluation). Plan expert validation sessions as a fixed part of the process, not an afterthought.
- **Record data lineage and a time model.** Log which documents were retrieved for each answer (use a metadata standard such as DCAT-AP-NL), and decide explicitly whether the assistant reflects the *current* state only or can answer historical questions too.

Detail in `references/sources-grounding-and-safety.md`.

## Retrieve well

- **Hybrid search by default.** Combine lexical (BM25) with semantic (vector) retrieval — neither alone is as robust as the two together.
- **Structure-aware chunking.** Page-level chunking is a strong, consistent default across mixed datasets, but the optimum is corpus-dependent — so measure it (see `rag-evaluatie`), don't assume.
- **Use a good Dutch embedding model** for Dutch corpora (the E5-NL models are a solid open option) rather than defaulting to an English-centric model.
- **Pick a self-hostable vector store** — Qdrant, Milvus, Weaviate, or Elasticsearch if you already run it — and avoid lock-in to a proprietary cloud vector database.
- **Rerank** the top candidates, and consider **tiered (layered) retrieval**: search a narrow layer first (e.g. FAQs), and fall back to a broader layer (e.g. legislation) only if needed.

Detail in `references/building-the-pipeline.md`.

## Ground every answer and cite the source

- **Always attach source attribution.** Every answer must be traceable to the underlying source — this is good practice *and* a transparency obligation under the EU AI Act (see the `ai-act-high-risk` skill).
- **Ground strictly in retrieved context.** The answer must not exceed the evidence retrieved. When retrieval is weak or empty, the assistant should **say it doesn't know** (and point the user to where to look) rather than fill the gap from the model's parametric memory — that is where hallucinations come from.
- This pairs with human control: a low-confidence or no-evidence case is a good place to escalate to a person (see the `menselijke-controle` skill).

## Treat retrieved content as untrusted

Retrieved passages are an attack surface. A document, email, or web page in your corpus can contain hidden instructions ("ignore previous instructions and…") that hijack the model through the retrieval path. **Treat retrieved text as data, not as instructions**: validate and sanitise passages, mark them clearly as untrusted context, and screen for suspicious patterns before they reach the model. (See your prompt-injection / RAG-hardening practice for the full treatment.)

## Tune for quality and cost together

Chunk size, retrieval thresholds, and the number of passages retrieved each affect **both** answer quality **and** energy/token cost — and over-aggressive chunking can save energy while measurably hurting quality. Measure both before optimising. For high-frequency questions, semantic caching (supported by Qdrant, Milvus, pgvector) avoids re-running the full retrieval+generation path. (See your zuinige-inferentie / efficient-inference practice.)

## Capture the pipeline in config

Record the pipeline's choices — embedding model, vector store, chunking strategy, hybrid weights, top-k, score thresholds, reranker, citation format, and the source whitelist reference — in configuration (start from `templates/rag-pipeline-config.yaml`), so the pipeline is reviewable, swappable, and reproducible rather than scattered through code.

## How this fits the rest of the library

- **`rag-evaluatie`** — measure retrieval and grounding quality; you can't tune what you don't measure.
- **`menselijke-controle`** — abstain and escalate to a human when retrieval is weak or stakes are high.
- **`kleinste-model-per-taak`** — the generation model can often be right-sized; good retrieval lets a smaller model answer well.
- Security (prompt-injection / RAG-hardening) and efficiency (zuinige-inferentie) practices, cross-referenced above.

## Sources

- Dense vs. sparse retrieval (BM25, vector, hybrid): https://dev.to/qvfagundes/dense-vs-sparse-retrieval-mastering-faiss-bm25-and-hybrid-search-4kb1
- NVIDIA — finding the best chunking strategy: https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/
- E5-NL embedding models (Hugging Face): https://huggingface.co/models?search=e5-nl
- Qdrant: https://qdrant.tech/ · Milvus: https://milvus.io/ · Weaviate: https://weaviate.io/
- DCAT-AP-NL 3.0 (metadata/lineage): https://www.forumstandaardisatie.nl/intakeadvies-dcat-ap-nl-30
- Overheidsbrede handreiking Generatieve AI (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai
- WetWijzer (tiered RAG over legislation, KOOP/Logius): https://gitlab.com/koop/innovatielab/wetwijzer-bedrijven-prototype
