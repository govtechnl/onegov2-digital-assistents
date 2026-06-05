---
name: menselijke-controle
description: "Use this skill whenever you are designing or building the final solution of a digital assistant, to guarantee a human can stay in control of what it does. Every solution built with this skill must have a human-in-the-loop OPTION — a real way for a person to review, intervene, override, or take over — and any solution that is HIGH-RISK (the ai-act-high-risk skill decides) must have MANDATORY, non-bypassable human oversight before a decision takes effect. It helps choose the right oversight model per use case (human in / on / above / before the loop), makes that oversight meaningful rather than a rubber stamp, and builds the override and escalation path into the architecture and UI. Triggers include 'human in the loop', 'human-in-the-loop', 'HITL', 'menselijke controle', 'menselijk toezicht', 'human oversight', 'menselijke tussenkomst', 'escalation', 'override', 'stop button', 'approval step', 'automated decision', 'geautomatiseerde besluitvorming', 'AVG art. 22', 'AI Act article 14', or finalising any assistant that makes or supports decisions about people. Do not sign off a solution as done without a human-control path — optional by default, mandatory when high-risk."
---

# Human control over the assistant

A digital assistant may support the work, but it must never fully, autonomously make decisions that directly affect citizens. Two laws back this up: **AVG art. 22** (people have a right not to be subject to solely automated decisions with significant effects) and the **EU AI Act art. 14** (high-risk systems must allow effective human oversight). This skill makes sure a human can actually stay in control of the solution you build — and that the control is real, not a formality.

## The two rules this skill enforces

1. **Every solution gets a human-in-the-loop *option*.** Whatever you build with this skill must include a genuine way for a person to review, intervene, override, or take over — an escalation path to a human, an override/stop control, and the ability to set the assistant's output aside. This holds even for low-risk assistants: a fallback to a human must exist and be reachable.
2. **High-risk solutions get *mandatory*, non-bypassable human oversight.** If the solution is high-risk, a human must be in the loop **before any decision takes effect**, and that step cannot be silently disabled or skipped. Get the risk classification from the **`ai-act-high-risk`** skill; if it is high-risk (or it makes decisions about people in the sense of AVG art. 22), human-in-the-loop is required, not optional. Record it in the oversight plan and, for public bodies, in the FRIA (see the `skill-iama` skill).

If you cannot tell whether the solution is high-risk, treat the oversight as mandatory until the classification says otherwise.

## Choose the oversight model per use case

Don't apply one pattern blindly — pick deliberately, driven by risk, system type, and lifecycle phase (definitions in `references/oversight-models-and-meaningfulness.md`):

- **Human in the loop** — a person reviews each output *before* a decision is made. The default for high-risk and for decisions about individuals.
- **Human on the loop** — a person monitors and can intervene. Acceptable only with concrete intervention thresholds (see the sham-oversight warning below).
- **Human above the loop** — a person steers at the strategic/ethical level.
- **Human before the loop** — ethical considerations are built into the system up front.

At high volume, oversight shifts from the individual decision to the **decision system as a whole** — its goals, norms, data, exceptions, error rates, escalations, audits, and stop buttons. Design for that, not just for one reviewer clicking "approve".

## Make the oversight meaningful, not a rubber stamp

This is where human control usually fails. Hold these lines:

- **Intervene at the right moment.** Control *after* the system has already acted controls nothing. For high-risk, the human acts before the decision takes effect.
- **Set concrete intervention thresholds.** "A human is on the loop" is sham oversight if it means glancing at dashboards. Define the specific conditions (confidence below X, certain case types, flagged risks) at which a human *must* step in.
- **The reviewer must be able — and free — to intervene.** Oversight is only real if the person can halt the system, set output aside, or reverse a decision, both technically and organisationally. Build a working stop/override, and make sure reviewers are not penalised for going against the system.
- **Watch for rubber-stamping.** If reviewers almost never deviate from the assistant's output, that is a signal there is effectively no human intervention — monitor the deviation rate and revise the process if it is near zero. Design against automation bias (show uncertainty, withhold the suggestion until the human has formed a view, etc.).
- **Check all four dimensions.** The Autoriteit Persoonsgegevens frames meaningful intervention across **human, technology & design, process, and governance**. A control point strong on one but failing on another is not meaningful — verify all four.

## Define what the system may never decide alone

Per use case, write down which decisions are **always** made by a human, even when the assistant gives advice — and make that boundary hold in practice. Formal documentation is not enough if reviewers structurally adopt the output without independent judgement.

## Build it into the solution

The control path is part of the deliverable, not a policy footnote:

- a reachable **escalation / handoff to a human** (ties into your error-handling: hand off after difficulty, not only when the user demands it);
- an **override / stop** control the overseer can actually use, surfaced in the UI (coordinate with the `wcag-accessibility` and `organisatie-huisstijl` skills so it is accessible and on-brand);
- **routing thresholds** that send low-confidence or high-stakes cases to a person (this pairs with a select-then-route / model-routing setup);
- **logging of human decisions** (who reviewed, what they changed, when) for auditability;
- clear **responsibilities** — never one person for the whole of control. Capture in a RACI/VERI matrix who is responsible per phase, who is ultimately accountable for deviant behaviour, and who handles signals from operations. Don't offload process responsibility onto the individual reviewer.

Capture all of this in `templates/human-oversight-plan.md` (which also feeds section 5 of the `skill-iama` toetsingsdossier).

## Don't call it done without a control path

Before treating the solution as finished, confirm the human-control path exists and works: optional for low-risk, mandatory and non-bypassable for high-risk. If it is missing, build it; if it is high-risk and the oversight can be skipped, that is a blocker, not a nice-to-have.

## Sources

- Algoritmekader — Menselijke controle over algoritmes: https://minbzk.github.io/Algoritmekader/onderwerpen/menselijke-controle/
- Algoritmekader — Betekenisvolle menselijke tussenkomst (maatregel): https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-03-menselijke-tussenkomst/index.html
- Autoriteit Persoonsgegevens — Betekenisvolle menselijke tussenkomst: https://www.autoriteitpersoonsgegevens.nl/actueel/betekenisvolle-menselijke-tussenkomst-bij-algoritmische-besluitvorming
- EU AI Act art. 14 (human oversight): https://artificialintelligenceact.eu/article/14/
- AVG/GDPR art. 22 (automated individual decision-making): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
