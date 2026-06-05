# EU AI Act — obligations and timeline

Read this for what high-risk and limited-risk systems must satisfy, and when. Orientation only — verify against the current EUR-Lex text, because the Act was amended in 2026 (Digital Omnibus) and dates may shift again.

## High-risk requirements (the system) — articles 9–15

- **Art. 9 — Risk-management system.** A continuous process to identify, evaluate and mitigate risks across the lifecycle.
- **Art. 10 — Data & data governance.** Training/validation/test data that is relevant, representative, and as error-free as possible; bias examined and addressed.
- **Art. 11 — Technical documentation.** Drawn up before deployment and kept current (Annex IV content).
- **Art. 12 & 19 — Record-keeping / automatic logs.** The system logs events enabling traceability; logs are retained.
- **Art. 13 — Transparency to deployers.** Instructions for use that let deployers understand and operate the system correctly.
- **Art. 14 — Human oversight.** Designed so people can effectively oversee it — understand its limits, intervene, and override. Oversight must be real, not nominal.
- **Art. 15 — Accuracy, robustness & cybersecurity.** Appropriate levels declared and maintained.

## Obligations on actors — articles 16–27 (selected)

- **Art. 16–18 — Providers.** Ensure the art. 9–15 requirements; maintain a **quality-management system** (art. 17) and **technical documentation** (art. 18); undergo **conformity assessment** and affix **CE marking**.
- **Art. 26 — Deployers.** Use per instructions; ensure human oversight in practice; monitor operation; keep logs; suspend and report where risks or serious incidents arise; cooperate with authorities.
- **Art. 27 — Fundamental-rights impact assessment (FRIA).** **Public-body deployers** (and private entities providing public services, plus certain credit/insurance deployers) must perform a FRIA **before first use** and **notify the market-surveillance authority** of the result. → handled by the `skill-iama` skill.
- **Art. 49 — Registration.** Providers register high-risk systems in the **EU database**; public-authority deployers register their use as well.

## Limited-risk transparency — article 50

- Users must be **informed they are interacting with an AI system** (unless obvious).
- **AI-generated or manipulated content** (text published to inform the public, images, audio, video / deepfakes) must be **disclosed/labelled**.
- Providers of generative systems must mark synthetic output in a **machine-readable** way.

For a user-facing assistant, the art. 50 disclosure is also a UI concern — coordinate with the `wcag-accessibility` and `organisatie-huisstijl` work so the disclosure is present, legible, and on-brand.

## Always in force — article 4 (AI literacy)

Providers and deployers must ensure staff dealing with the system have **sufficient AI literacy**. Enforceable since **2 February 2025**, independent of risk category. Treat it as a standing obligation, not a launch task.

## Application timeline (moving — verify before relying on a date)

| Provision | Original date | Status as of mid-2026 |
|---|---|---|
| Prohibited practices (art. 5) | 2 Feb 2025 | In force |
| AI literacy (art. 4) | 2 Feb 2025 | In force |
| GPAI / general-purpose model obligations | 2 Aug 2025 | In force |
| Most art. 50 transparency duties | 2 Aug 2026 | Applies (short deferral for marking pre-existing generative output, ~2 Dec 2026) |
| **Standalone Annex III high-risk (incl. art. 27 FRIA)** | **2 Aug 2026** | **Provisionally deferred to 2 Dec 2027 (Digital Omnibus) — not yet formally adopted; original date stands until it is** |
| Product-embedded (Annex I) high-risk | 2 Aug 2027 | Provisionally deferred to 2 Aug 2028 |

The **Digital Omnibus on AI** reached a provisional political agreement in May 2026 to defer the high-risk deadlines as shown, prompted by delays in finalising harmonised standards and designating national authorities. Until it is published in the Official Journal, the original timeline applies. **Always confirm the current state** — and remember the deferral is intended as preparation time, with the expectation that compliance work is already under way.

## Sources

- EU AI Act — full text (EUR-Lex): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Implementation timeline: https://artificialintelligenceact.eu/implementation-timeline/
- Art. 50 (transparency): https://artificialintelligenceact.eu/article/50/
- Art. 4 (AI literacy): https://artificialintelligenceact.eu/article/4/
- Digital Omnibus on AI — Council press release (7 May 2026): https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/
