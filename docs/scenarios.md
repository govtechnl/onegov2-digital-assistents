# Demo Scenarios

Concrete, scoped scenarios that exercise one or more practices end-to-end. Use these as targets for prototypes, evaluation prompts, or demos. All scenarios are synthetic, never use real citizen data.

## 1. Benefits eligibility explainer

A citizen asks a municipal assistant whether they qualify for a specific allowance. The assistant explains the criteria, cites the underlying regulation, and routes the citizen to the official application form. It refuses to make a binding decision and offers a contact channel for edge cases.

Exercises: `answer-quality`, `rag-pipeline`, `user-experience`, `ethics-human-rights`.

## 2. Policy-draft research helper

A policy officer drafting a memo asks the assistant for relevant parliamentary documents and prior policy decisions. The assistant returns a ranked list with citations and a short synthesis, clearly separating retrieval from interpretation.

Exercises: `rag-pipeline`, `answer-quality`, `governance`.

## 3. Internal procedure Q&A

A civil servant asks an internal assistant how to handle a specific procedural step. The assistant answers from the latest internal procedure documents and shows the document version. If the procedure changed within the last 30 days, the assistant flags it.

Exercises: `data-quality-governance`, `rag-pipeline`, `culture-adoption`.

## 4. Low-digital-skill conversation

A citizen with limited digital skills asks an open question in informal Dutch. The assistant responds in B1-level plain language, offers to repeat in simpler terms, and provides a phone number for human help.

Exercises: `user-experience`, `ethics-human-rights`, `answer-quality`.

## 5. Multilingual citizen request

A citizen writes in a non-Dutch language. The assistant detects the language, answers in that language with a Dutch summary, and indicates that the Dutch version is authoritative.

Exercises: `user-experience`, `answer-quality`, `compliance`.

## 6. Suspicious-input handling

A user attempts prompt injection ("ignore previous instructions and ..."). The assistant refuses, logs the attempt, and continues serving normal requests without leaking system instructions.

Exercises: `security`, `governance`, `llmops-monitoring`.

## 7. Source-outage degradation

The retrieval back-end becomes unavailable. The assistant tells the user it cannot consult the source right now and offers the contact channel, instead of guessing.

Exercises: `production-scalability`, `infrastructure-data`, `user-experience`.

## 8. Model upgrade rollout

A new model version is rolled out via canary on 5% of traffic. Evaluation metrics are compared against the baseline. The release is promoted, paused, or rolled back based on pre-agreed criteria.

Exercises: `model-deployment`, `llmops-monitoring`, `technical-performance`.
