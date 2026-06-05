# Oversight models, meaningfulness, and the legal mapping

Read this to choose an oversight model and to judge whether the control you've designed is actually meaningful. Orientation, not legal advice — the obligation and its sufficiency are for compliance/legal and the FG/DPO to confirm.

## The four oversight models

Pick deliberately per use case; the right choice depends on the type of system, the risk, and the lifecycle phase. They are not mutually exclusive — a system often combines several.

- **Human in the loop (HITL).** A person reviews each relevant output *before* a decision is made or an action is taken. Highest assurance; the default for high-risk systems and for any decision with significant effect on an individual.
- **Human on the loop (HOTL).** A person monitors operation and can intervene, but the system acts without per-case approval. Only acceptable with **concrete intervention thresholds** and a real ability to stop the system — otherwise it degrades into sham oversight.
- **Human above the loop.** A person governs at the strategic and ethical level — setting goals, norms, and boundaries, and reviewing aggregate behaviour rather than individual outputs.
- **Human before the loop.** Ethical and legal considerations are designed into the system up front (constraints, refusals, guardrails) so that some bad outcomes are prevented by construction.

### When is human-in-the-loop mandatory (not just optional)?

- The system is **high-risk** under the EU AI Act (Annex III) → **art. 14** requires effective human oversight; for public-body deployers this is part of the **art. 27 FRIA**. Use the `ai-act-high-risk` and `skill-iama` skills.
- The system produces a **solely automated decision with legal or similarly significant effect** on a person → **AVG art. 22**: there must be meaningful human intervention, or a recognised exception that is justified.
- When unsure, treat oversight as mandatory until the classification says otherwise.

Optional-but-recommended HITL still applies everywhere else: even a low-risk assistant needs a reachable fallback to a human.

## Volume changes where oversight sits

Reviewing every output one-by-one does not scale. At high volume, the locus of control shifts from the **individual decision** to the **decision-making system as a whole**: its goals, norms, data quality, defined exceptions, error rates, escalation routes, audits, and stop buttons. Design oversight at that level — with sampling, thresholds, and monitoring — rather than pretending a human reads everything.

## Meaningful vs. sham oversight

A control point can exist on paper and mean nothing. Test it against these:

- **Right moment** — intervention happens before the decision takes effect, not as a post-hoc audit.
- **Concrete thresholds** — specific, written conditions trigger mandatory human action (low confidence, case type, flagged risk).
- **Real power to act** — the reviewer can technically and organisationally halt the system, set aside output, or reverse a decision, and is not penalised for doing so.
- **Independent judgement** — reviewers actually deviate from the system sometimes. A near-zero deviation rate is a red flag for rubber-stamping; monitor it and revise the process. Design against automation bias (e.g. surface uncertainty, or have the human form a view before seeing the suggestion).
- **The boundary holds** — the decisions you said a human must always make are, in practice, made by a human.

### The Autoriteit Persoonsgegevens' four dimensions

The AP frames meaningful human intervention across four dimensions. Strength on one cannot compensate for a gap in another:

1. **Human** — competence, authority, time, and willingness to intervene.
2. **Technology & design** — the system surfaces what the human needs and provides working override/stop controls.
3. **Process** — clear intervention moments, thresholds, and escalation procedures.
4. **Governance** — roles, accountability, and monitoring that keep the oversight honest over time.

## Responsibilities — never one person

Capture in a RACI or VERI matrix who is responsible for human control **per lifecycle phase**, who is ultimately accountable when the system behaves unexpectedly, and who is the contact point for signals from operations. Do not offload responsibility for the whole control process onto the individual reviewer — that is both unfair and ineffective.

## What to build (design checklist)

- Reachable escalation / handoff to a human (proactive, not only on user demand).
- A working override / stop control, surfaced accessibly in the UI.
- Routing thresholds that send low-confidence or high-stakes cases to a person.
- Logging of human decisions (who, what changed, when) for auditability.
- Monitoring of the deviation rate and of whether the never-decide-alone boundary holds.

## Sources

- Algoritmekader — Menselijke controle: https://minbzk.github.io/Algoritmekader/onderwerpen/menselijke-controle/
- Algoritmekader — Betekenisvolle menselijke tussenkomst: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-03-menselijke-tussenkomst/index.html
- Algoritmekader — Rollen en verantwoordelijkheden: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-01-rollen-en-verantwoordelijkheden/
- Autoriteit Persoonsgegevens — Betekenisvolle menselijke tussenkomst: https://www.autoriteitpersoonsgegevens.nl/actueel/betekenisvolle-menselijke-tussenkomst-bij-algoritmische-besluitvorming
- EU AI Act art. 14: https://artificialintelligenceact.eu/article/14/
