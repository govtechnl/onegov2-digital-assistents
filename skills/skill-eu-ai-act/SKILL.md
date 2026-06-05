---
name: ai-act-high-risk
description: "Use this skill the moment a digital assistant looks like it could be HIGH-RISK under the EU AI Act, to make the developer classify it correctly and surface the obligations that follow. Trigger it whenever the assistant supports or automates decisions in an Annex III area: access to or eligibility for public benefits and services (uitkeringen, toeslagen, schuldhulp, voorzieningen), permits/vergunningen, employment (recruitment, evaluation, monitoring), education and exams, law-enforcement or criminal-justice context, fraud detection on individuals, migration/border control, biometrics, critical infrastructure, creditworthiness/credit scoring, or insurance pricing — and on explicit cues like 'high-risk', 'hoog risico', 'AI Act', 'AI-verordening', 'Annex III', 'bijlage III', 'conformiteitsbeoordeling', 'CE-markering', or 'prohibited AI'. It classifies the system (prohibited / high-risk / limited-risk transparency / minimal), fixes the provider-versus-deployer role, lists the high-risk obligations (risk management, data governance, logging, human oversight, transparency, registration, and the Article 27 FRIA for public bodies), and flags the moving application timeline. Classifying and certifying conformity is the organisation's responsibility — this skill flags, structures and routes; it does not declare a system compliant."
---

# EU AI Act — high-risk trigger and obligations

Some assistants fall into the EU AI Act's **high-risk** category, which carries heavy, specific obligations. This skill fires when what the developer is building **looks high-risk**, makes them classify it properly, surfaces the obligations that follow, and routes the compliance work to the right people. Classifying a system and certifying its conformity is the organisation's responsibility (compliance, legal); your role is to **flag, structure, and route** — not to declare a system compliant.

## When this triggers

Raise it whenever the assistant supports or automates something in a **high-risk use area (Annex III)** — for a public body, most often:

- access to or eligibility for **public benefits and services** (uitkeringen, toeslagen, schuldhulp, toegang tot voorzieningen);
- **permits / vergunningen** and similar entitlement decisions;
- **employment** — recruitment, evaluation, task allocation, monitoring;
- **education** — admission, exam scoring, proctoring;
- **law-enforcement or criminal-justice** context, and **fraud** detection on individuals;
- **migration, asylum and border** control;
- **biometrics**, **critical infrastructure**, **administration of justice**;
- **creditworthiness / credit scoring** and **life & health insurance** pricing.

Also trigger on explicit cues ("high-risk", "hoog risico", "AI Act", "Annex III", "conformiteitsbeoordeling"). When a use case sits *near* one of these, treat it as in scope and classify it rather than wave it through. Purely internal tooling with no effect on people and no Annex III use is usually out of scope.

## Step 1 — Classify (and when in doubt, go higher)

Determine the category and **write down the reasoning** (this record matters at audit):

- **Prohibited (art. 5)** — e.g. social scoring by authorities, manipulative or deceptive techniques, exploiting the vulnerabilities of specific groups, untargeted scraping of facial images, certain biometric categorisation and real-time remote biometric identification, and (added via the Digital Omnibus) AI-generated non-consensual intimate imagery / CSAM. If it looks prohibited: **stop and escalate to legal now — don't build it.**
- **High-risk (Annex III + art. 6)** — the areas listed above. Heavy obligations (Step 2).
- **Limited-risk / transparency (art. 50)** — most chatbots and generative assistants: users must be told they are interacting with AI; AI-generated or deepfake content must be labelled; synthetic output must be machine-readable.
- **Minimal risk** — no specific obligations, but record the classification anyway.

Rule of thumb from practice: **doubt between categories resolves upward** — the burden of justifying a *lower* classification sits with the organisation.

Also fix the **role**: a government body using a system built by a vendor is usually a **deployer**, not the provider. Providers and deployers carry different duties, so this decides which obligations are yours. See `references/ai-act-risk-classification.md`.

## Step 2 — Surface the obligations

If the system is **high-risk**, confirm with compliance which duties fall on the provider versus the deployer. In outline:

- **Requirements on the system (provider-led):** risk-management system (art. 9), data & data governance (art. 10), technical documentation (art. 11), record-keeping / automatic logging (art. 12 & 19), transparency and information to deployers (art. 13), **human oversight (art. 14)**, and accuracy/robustness/cybersecurity (art. 15); plus a quality-management system (art. 17), **conformity assessment and CE marking**, and **registration in the EU database** (art. 49).
- **Deployer duties (art. 26):** use the system per its instructions, ensure human oversight in practice, monitor, keep logs, and inform the provider/authority of risks or serious incidents.
- **Public-body deployers — the Article 27 FRIA:** a **fundamental-rights impact assessment before first use**, notified to the market-surveillance authority. → use the `skill-iama` skill; in the Netherlands the IAMA does much of this work. Public authorities also register their use in the EU database.
- **Already in force regardless of category:** **AI literacy (art. 4)** — staff need sufficient AI competence — and, for any user-facing assistant, the **art. 50 transparency** disclosure.

If the system is **limited-risk**, the core duty is the art. 50 transparency disclosure plus content labelling. See `references/ai-act-obligations-and-timeline.md`.

## Step 3 — Timeline (this is moving — verify the current state)

The categories and obligations above are stable; the **application dates are in flux.** As originally enacted, standalone Annex III high-risk obligations (and the art. 27 FRIA) applied from **2 August 2026**. The **Digital Omnibus on AI** (provisional political agreement, May 2026) would defer standalone Annex III high-risk obligations to **2 December 2027**, and product-embedded (Annex I) high-risk to **2 August 2028** — but it is **not yet formally adopted**, so until it is, the original 2 August 2026 date stands as written. **Prohibitions (art. 5)** and **AI literacy (art. 4)** have applied since **2 February 2025**, and most **art. 50 transparency** duties from **2 August 2026** (with a short deferral for marking pre-existing generative-AI output).

**Verify the current status on an authoritative source** (EUR-Lex, or the European Commission / EU AI Act site) before relying on any date — this area changed in 2026 and may change again. And note the framing in the EU's own communications: the delay, if adopted, is **time to prepare, not permission to wait**. High-risk requirements are large and lead times are long, so preparation should already be under way.

## Step 4 — Route to humans and record the decision

Classification and conformity are not yours to certify. Capture the classification in a short record (template: `templates/risicoclassificatie.md`) with its reasoning, then route it: the **compliance officer / legal** for sign-off, the **privacy officer (FG/DPO)** for the DPIA, and — if it is high-risk and you are a public body — trigger the **`skill-iama`** skill for the FRIA. Register the system where required, and (for user-facing surfaces) remember the art. 50 disclosure ties into the UI.

## Sources

- EU AI Act (Regulation (EU) 2024/1689) — full text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- EU AI Act explorer (articles & annexes): https://artificialintelligenceact.eu/
- Digital Omnibus on AI — Council press release (May 2026): https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/
- Overheidsbrede handreiking Generatieve AI (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai
