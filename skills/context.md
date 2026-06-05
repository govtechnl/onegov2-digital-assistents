## Team

- Team name: Data Assistent - Team 1 (Skilltron)
- Members: Jochem Huijps, Joris Feis, Bogdan Potemskyi, Thomas Bersee, Harm Erbe, Laurent Smeets Lisette van Lange

## Approach

- [ ] Approach A, one Skill per framework topic
- [ ] Approach B, layered (base / domain / composition)
- [x] Hybrid

Approach A &B . We created an orchestrated skill framework where each Skill addresses an independent compliance or quality concern (privacy, EU AI Act, human oversight, accessibility, etc.) that a public-sector development team can apply separately or in combination when building a digital assistant.

## Skills in this repository

- `master-skill` — entry point that analyses the use case and determines which skills are relevant, in which order. Run this first.
- `skill-EU-AI-act` — classifies the assistant under the EU AI Act (prohibited / high-risk / limited-risk / minimal), fixes the provider-versus-deployer role, and lists applicable obligations (risk management, logging, human oversight, transparency, registration).
- `skill-Algoritmeregister` — prepares a publication for the Dutch Algorithm Register (algoritmes.overheid.nl) according to the MinBZK Publication Standard v1.0.0, including publication category (A/B/C) and all required fields.
- `skill-privacy-anonymisation` — enforces a strict separation between the pseudonymous processing layer (individual case handling) and the fully anonymous insights layer (dashboards, chatbot context), and walks through the associated GDPR and EU AI Act obligations.
- `skill-human-in-the-loop` — designs a human oversight plan with escalation path, override control in the UI, decision log, and RACI matrix for AI-generated outputs before they reach citizens.
- `skill-IAMA` — runs the Impact Assessment on Human Rights and Algorithms (IAMA) screening questions, produces a dossier outline, and routes to the organisation's Data Protection Officer and legal advisor.
- `skill-rag-pijplijn` — guides the setup of a Retrieval-Augmented Generation pipeline: chunking strategy, embedding choice, vector store, retrieval configuration, and citation requirements.
- `skill-rag-evaluatie` — evaluates the quality of a RAG system: faithfulness, relevance, hallucination risk, and coverage across the source set.
- `skill-kleinste-model` — optimises model choice per task type; produces a configuration file that maps each task (e.g. simple statistics query vs. complex analysis) to the smallest model that meets quality requirements.
- `skill-ui-huisstijl` — applies the Dutch government house style (Rijkshuisstijl) and municipality brand tokens (colours, typography, logo) to the interface in a maintainable way.
- `skill-wcag` — audits the interface for WCAG 2.1 AA compliance: contrast, keyboard navigation, screen reader support, and accessibility statement requirements.

