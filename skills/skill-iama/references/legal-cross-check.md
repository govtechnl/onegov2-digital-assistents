# Legal cross-check — IAMA outcomes against concrete legal duties

A completed IAMA is **necessary but not sufficient**. The IAMA is a deliberation about fundamental-rights and ethical impact; it does not by itself guarantee that every concrete legal obligation from the **EU AI Act**, the **AVG/GDPR**, and the **Awb** is met. Walk this checklist *with* the developer (and have the compliance officer / FG verify), marking for each row whether it was discussed in the IAMA **and** whether the legal duty is actually secured. Anything not secured becomes an open item with an owner and a deadline in the dossier.

This is a checklist to structure the conversation — not legal advice. Final judgement on each row belongs to compliance/legal.

## Cross-check table

| IAMA theme | Relevant law | Concrete obligation to confirm |
|---|---|---|
| Purpose limitation & necessity | AVG art. 5(1)(b) and (c) | Processing purpose described; no further processing outside that purpose |
| Lawful basis for processing | AVG art. 6 / art. 9 (special categories) | A valid basis established for each data type |
| Automated decision-making | AVG art. 22 | Meaningful human intervention arranged, or the exception justified |
| Transparency to the citizen | AI Act art. 50 / AVG art. 13–14 | Information about the use of AI is provided to users |
| Human oversight | AI Act art. 14 (high-risk) | An oversight mechanism is described and assigned to someone |
| Logging & auditability | AI Act art. 12 (high-risk) | Logging of relevant decisions is in place |
| Non-discrimination | Awb art. 2:4 / ECHR art. 14 | Bias check performed; results documented |
| Data-subject rights | AVG art. 15–22 | A procedure for access, correction and objection exists |
| Accountability | AVG art. 5(2) | Records of processing (verwerkingsregister) updated |
| Right to remedy / reasoning | Awb afd. 3.7 / art. 3:46–3:50 | Decisions sufficiently reasoned; objection possible |

## The dossier this feeds

The cross-check result is one component of the **toetsingsdossier** (see `templates/toetsingsdossier-outline.md`), which should contain:

1. **Classification decision** — the AI risk category with reasoning.
2. **Cross-check result** — which duties are covered, which remain open (with action owner and deadline).
3. **DPIA outcome** (if applicable) — summary and residual risks.
4. **IAMA report** — key findings and agreements.
5. **Human-oversight plan** — who approves which output, at which thresholds.
6. **Registration evidence** — extract from the verwerkingsregister and, where relevant, the EU AI database.

Retain the dossier at least as long as the system is in use plus five years; ten years for high-risk systems (AI Act art. 18).

## How to use this in practice

- Treat each row as a question, not a box to tick. "Is there a procedure for objection?" → if the answer is "we'll add one later", that is an *open* item, not a *covered* one.
- Where a row depends on the AI Act risk category (human oversight, logging), confirm the category first — use the `ai-act-high-risk` skill.
- Where a row concerns personal data, the FG/DPO owns the answer; route it there rather than concluding yourself.

## Sources

- AVG/GDPR — Autoriteit Persoonsgegevens: https://www.autoriteitpersoonsgegevens.nl/
- EU AI Act: https://artificialintelligenceact.eu/
- Algemene wet bestuursrecht (Awb): https://wetten.overheid.nl/BWBR0005537/
- IAMA (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2021/02/25/impact-assessment-mensenrechten-en-algoritmes
