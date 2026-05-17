---
id: rag-pipeline
title: RAG Pipeline
summary: Ground answers in retrieved, citable sources with measurable coverage.
domains: [answer-quality, infrastructure-data, compliance]
phases: [PoC, Pilot, Production]
levels: [Operational, Tactical]
sources: [gdpr, onegov-principles]
---

Design retrieval so every answer can cite the documents it relied on, with stable identifiers and versioning. Measure source-coverage and source-precision on a fixed evaluation set.

Document chunking, embedding model, and re-ranking choices. Re-run evaluation after each change; treat unexplained regressions as blocking.

When the retriever finds nothing relevant, the assistant should say so plainly rather than improvise an answer.
