# Building the pipeline — ingestion, indexing, retrieval

Read this to build the retrieval half of a RAG system well. It is a method with sensible defaults; verify the choices on your own corpus with the `rag-evaluatie` skill — the optimum is corpus-dependent.

## 1. Ingestion & chunking

- **Chunk with structure in mind.** Split on document structure (sections, pages, headings) rather than blind fixed-size windows that cut sentences in half. **Page-level chunking** is a strong, consistent default across mixed datasets; the optimum still varies per corpus, so treat it as a starting point to measure, not a fixed truth.
- **Keep chunk metadata.** Carry source id, title, section, date/version, and access level on every chunk — you need it for citations, filtering, lineage, and the time model.
- **Mind the size/quality trade-off.** Smaller chunks improve precision but can lose context; larger chunks keep context but dilute relevance and cost more tokens. Over-aggressive chunking can save energy while measurably hurting answer quality — measure both.

## 2. Embeddings

- **Match the language.** For Dutch corpora use a strong Dutch embedding model (the open E5-NL models are a good option) rather than an English-centric default — embedding quality drives retrieval quality.
- **Version your embedding model.** A change of embedding model invalidates the index; re-embed and re-evaluate when you switch.
- **Consider fine-tuned / domain embeddings** for narrow domains if generic embeddings retrieve poorly.

## 3. Vector store

- **Prefer self-hostable, open options** — Qdrant, Milvus, or Weaviate — or Elasticsearch if your organisation already runs it. Avoid lock-in to a proprietary cloud vector database; data residency and exit also matter for government (see digital-sovereignty practices).
- **Use metadata filtering** (access level, source, date) at query time so retrieval respects authorisation and recency.
- Many of these stores also support **semantic caching** for repeated queries — useful for high-frequency FAQs.

## 4. Retrieval

- **Hybrid search by default.** Combine **BM25** (lexical, great for exact terms, names, codes) with **vector similarity** (semantic, great for paraphrase). Fuse the results (e.g. weighted or reciprocal-rank fusion). Neither alone is as robust as the combination, especially for government text full of specific terms and reference numbers.
- **Rerank the top candidates.** Retrieve a wider set, then reorder with a cross-encoder/reranker before passing the best few to the model. This usually lifts precision more than fiddling with the base retriever.
- **Set a relevance threshold.** If nothing clears the bar, return "no confident source found" — that feeds the abstain/escalation behaviour, rather than forcing a weak answer.
- **Tune top-k deliberately.** More passages can help recall but add tokens, latency, and noise; find the smallest k that meets your quality bar.

## 5. Tiered (layered) retrieval

Search a narrow, high-precision layer first (e.g. curated FAQs), and only fall back to a broader, lower-precision layer (e.g. full legislation) when the first layer has no good answer. This keeps common questions fast and cheap and reserves heavy retrieval for the hard cases — the WetWijzer project saw positive results with this pattern.

## 6. Efficiency (tune with quality, not against it)

Chunk size, thresholds, and passage count each move both quality and energy/cost. Don't optimise one blind to the other: measure answer quality alongside tokens/latency, and use semantic caching for repeated questions. (See the efficient-inference practice; and the `kleinste-model-per-taak` skill for right-sizing the generation model — strong retrieval often lets a smaller model answer well.)

## Sources

- Dense vs. sparse retrieval: https://dev.to/qvfagundes/dense-vs-sparse-retrieval-mastering-faiss-bm25-and-hybrid-search-4kb1
- NVIDIA — chunking strategy: https://developer.nvidia.com/blog/finding-the-best-chunking-strategy-for-accurate-ai-responses/
- E5-NL embeddings: https://huggingface.co/models?search=e5-nl
- Qdrant: https://qdrant.tech/ · Milvus: https://milvus.io/ · Weaviate: https://weaviate.io/
