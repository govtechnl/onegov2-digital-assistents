# IAMA, DPIA and the AI Act FRIA — how they relate

Read this to explain to the developer which assessment is which, where they overlap, and why doing one does not excuse the others. None of this is legal advice — it is orientation so the developer asks the right people the right questions.

## The three instruments

- **DPIA — Data Protection Impact Assessment (AVG art. 35).** Focuses on **data**: what personal data is processed, on what lawful basis, with what risks to privacy, and how those are mitigated. Required for processing likely to result in a high risk to data subjects — which is almost always the case for AI systems handling citizen data. Owned by the organisation with the FG/DPO.
- **IAMA — Impact Assessment Mensenrechten en Algoritmes (BZK).** A Dutch deliberation instrument focused on **people and fundamental rights**: which rights the system touches (dignity, equality, privacy, access to remedy), who is affected, what could go wrong, and what safeguards apply. It is a structured, multidisciplinary discussion, not a form one person fills in.
- **FRIA — Fundamental Rights Impact Assessment (EU AI Act art. 27).** A legal obligation on certain **deployers** of Annex III high-risk systems — notably **bodies governed by public law and private entities providing public services** (and specific private deployers in credit scoring and life/health insurance pricing). It must be done **before first use** and describe the intended purpose, the period and frequency of use, the categories of persons affected, the specific risks of harm, the human-oversight measures, and the mitigations. The deployer must **notify the market-surveillance authority** of the results (a template is provided by the European AI Office).

## How they fit together for a Dutch public body

- The **FRIA is the legal obligation**; the **IAMA is the instrument** that operationalises much of it. A well-run IAMA can supply most of what an Article 27 FRIA requires — but check it actually covers the FRIA's mandatory points before treating the obligation as met.
- The **DPIA and the FRIA overlap but are not identical.** Article 27(6) allows a deployer to rely on an existing DPIA only where it already covers the FRIA's elements; otherwise the FRIA must add the missing fundamental-rights analysis. A DPIA that "ticked every data box" can still miss systemic-discrimination and access-to-remedy risks the FRIA is designed to catch.
- Practical sequence for an Annex III, public-body assistant: confirm the **AI Act classification** (`ai-act-high-risk` skill) → run/refresh the **DPIA** with the FG → run the **IAMA**, scoped to also satisfy the **FRIA** points → **cross-check** outcomes against the concrete legal duties (`references/legal-cross-check.md`) → **notify** the market-surveillance authority of the FRIA result → assemble the **dossier**.

## When each is triggered

- **DPIA**: whenever personal data is processed with likely high risk (most citizen-facing AI).
- **IAMA**: whenever fundamental rights may be affected — recommended broadly for government algorithms, and effectively required to do the FRIA well.
- **FRIA**: when the system is **Annex III high-risk** *and* the deployer is a public body / public-service provider (or a covered private deployer). Tied to the high-risk obligations' application date — see the `ai-act-high-risk` skill for the (currently moving) timeline.

## Reuse and updates

Article 27 lets deployers rely, in similar cases, on a previously conducted FRIA or a provider's equivalent assessment — but it **must be updated** whenever its elements change or go out of date. The same discipline applies to the IAMA and DPIA: reopen them on any material change (new purpose, new data, new model version, monitoring signals).

## Sources

- IAMA (BZK): https://www.rijksoverheid.nl/documenten/rapporten/2021/02/25/impact-assessment-mensenrechten-en-algoritmes
- EU AI Act art. 27 (FRIA): https://artificialintelligenceact.eu/article/27/
- DPIA — Autoriteit Persoonsgegevens: https://www.autoriteitpersoonsgegevens.nl/themas/algemene-avg/verantwoordingsplicht/data-protection-impact-assessment-dpia
- Algoritmekader (BZK): https://minbzk.github.io/Algoritmekader/
