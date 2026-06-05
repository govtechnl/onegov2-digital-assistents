# Sources, grounding, citations and safety

Read this to make a RAG system *trustworthy*: good sources in, grounded and cited answers out, and safe against the retrieval path being abused. This is where government RAG most often succeeds or fails.

## Source quality — "the assistant is only as good as its sources"

- **Authoritative source whitelist.** Index only approved, authoritative sources. Define the whitelist explicitly and keep it small and governed rather than crawling broadly. (Example: the overheid.nl team works from a few pragmatic governed sources — Samenwerkende Catalogi incl. UPL, Wegwijzer.overheid.nl, and a curated set of Q&As — not the open web.)
- **Be wary of websites as sources.** Government and municipal sites look authoritative, but the structural lack of content governance and the state of content management often make their reliability insufficient for RAG. Prefer structured, governed sources; if you must use a website, treat its trustworthiness as a question to verify, not assume.
- **Domain-expert involvement is the biggest bottleneck and the biggest success factor.** Insufficient domain expertise severely hampers both building and evaluation. Schedule expert validation sessions as a fixed part of the development process.
- **Feedback loop.** Capture user feedback (including thumbs-down and corrections) structurally and route real-world failures back to experts and into the golden dataset (see `rag-evaluatie`).

## Lineage and the time model

- **Record data lineage.** Log which documents/chunks were retrieved for each prompt, with their source and version. Use a metadata standard such as DCAT-AP-NL 3.0. Lineage is needed for citations, audits, debugging, and accountability.
- **Decide the time model explicitly.** State whether the assistant always reflects the *current* situation or can also answer historical questions, and design indexing/versioning to match. Stale legislation answered as current is a serious failure in a government context.

## Grounding and citations

- **Cite the source on every answer.** Each answer must be traceable to the underlying source (chunk → document → authority). This is both a quality measure and an EU AI Act transparency obligation (see the `ai-act-high-risk` skill). Make citations precise enough to verify (document + section, not just "somewhere on the site").
- **Ground strictly in retrieved context.** Instruct the model to answer *only* from the retrieved passages, and design so the answer cannot exceed the evidence. If the passages don't support an answer, the assistant should **abstain** — say it doesn't know and point to where to look — rather than draw on parametric memory. This is the primary defence against confident hallucination.
- **Escalate weak cases.** No-evidence or low-confidence retrieval is a natural human-handoff point (see the `menselijke-controle` skill), especially for high-stakes questions.

## Retrieved content is untrusted (RAG injection)

The retrieval path is an attack surface, because the content you index is not necessarily content you control.

- **Treat retrieved text as data, never as instructions.** A document, email, PDF, or web page can contain "ignore previous instructions and…" style payloads that hijack the model when retrieved. Strictly separate the system instructions from retrieved content, and label retrieved passages as untrusted context.
- **Validate passages before they reach the model.** Check retrieved chunks for relevance, provenance, and suspicious instruction-like patterns; drop or quarantine anything anomalous.
- **Add a confirmation step for sensitive actions.** If the assistant can act (not just answer), don't let a retrieved passage trigger an action on its own — require explicit human confirmation for sensitive operations.
- For the full treatment, use your prompt-injection / RAG-hardening practice; this section is the RAG-specific summary.

## Sources

- Overheidsbrede handreiking Generatieve AI (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai
- DCAT-AP-NL 3.0: https://www.forumstandaardisatie.nl/intakeadvies-dcat-ap-nl-30
- Algoritmeregister: https://algoritmes.overheid.nl/
- WetWijzer (tiered RAG over legislation): https://gitlab.com/koop/innovatielab/wetwijzer-bedrijven-prototype
