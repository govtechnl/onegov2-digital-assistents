# EU AI Act — risk classification

Read this to classify an assistant under the AI Act. It is orientation for prompting and routing, not legal advice — the final classification is the organisation's to make and document. Always verify against the current text on EUR-Lex (the Act was amended in 2026 via the Digital Omnibus).

## The four risk tiers

1. **Unacceptable risk — prohibited (art. 5).** May not be built or used. Includes (non-exhaustive): social scoring by or for public authorities; manipulative or deceptive techniques that distort behaviour and cause harm; exploiting vulnerabilities of specific groups (age, disability, socio-economic situation); untargeted scraping of facial images to build recognition databases; biometric categorisation inferring sensitive attributes; real-time remote biometric identification in public spaces for law enforcement (narrow exceptions); emotion recognition in the workplace and education (narrow exceptions); predictive policing based solely on profiling; and — added through the Digital Omnibus — AI-generated non-consensual intimate imagery and CSAM. If a use case resembles any of these: **stop and escalate to legal.**

2. **High risk (Annex III + art. 6).** Permitted but heavily regulated. Annex III lists eight areas; the ones most relevant to public-sector assistants:
   - **Access to essential public (and certain private) services and benefits** — eligibility for social security, assistance, and public services; emergency dispatch prioritisation; **creditworthiness/credit scoring**; risk assessment and pricing in **life and health insurance**.
   - **Employment & workers** — recruitment, selection, evaluation, task allocation, monitoring, promotion/termination.
   - **Education & vocational training** — admission, assessment, exam scoring, proctoring.
   - **Law enforcement** — individual risk assessments, evidence evaluation, profiling.
   - **Migration, asylum and border control.**
   - **Administration of justice and democratic processes.**
   - **Biometrics** (where not prohibited) and **safety components of critical infrastructure.**
   Note art. 6 also includes a limited "no significant risk" carve-out for some Annex III cases — but the deployer/provider must document and justify it, and profiling always counts as high-risk. Don't assume the carve-out; confirm it with compliance.

3. **Limited risk — transparency (art. 50).** Most chatbots and generative assistants. Core duties: tell users they are interacting with an AI system; label AI-generated or manipulated content (deepfakes); and make synthetic output machine-readable.

4. **Minimal risk.** Everything else — no specific obligations, but still record the classification.

## Doubt resolves upward

Where a use case sits between two tiers, treat it as the **higher** tier until compliance/legal decides otherwise. The burden of justifying a lower classification is on the organisation, and the cost of under-classifying (deploying a high-risk system as if it were limited-risk) is far higher than the cost of an unnecessary assessment.

## Provider vs deployer — fix the role

- **Provider** — develops or has developed an AI system and places it on the market / puts it into service under its own name. Carries the bulk of the high-risk *system* requirements (art. 9–15) plus quality management, conformity assessment, CE marking, and EU-database registration.
- **Deployer** — uses an AI system under its authority (a government body using a vendor's system is typically here). Carries the art. 26 deployer duties and, for public bodies, the **art. 27 FRIA**.

A public body can also become a *provider* — e.g. by building its own system, or by substantially modifying a third-party one or putting it on the market under its own name. Clarify this early, because it changes which obligations apply.

## Recording the classification

Capture a short, dated classification record with reasoning (see `templates/risicoclassificatie.md`): the category, the Annex III area (if any), the provider/deployer role, the art. 6 carve-out justification (if claimed), and the open follow-ups. This record is the first item in the toetsingsdossier (see the `skill-iama` skill).

## Sources

- EU AI Act — full text (EUR-Lex): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Annex III (high-risk use cases): https://artificialintelligenceact.eu/annex/3/
- Art. 5 (prohibited practices): https://artificialintelligenceact.eu/article/5/
- Art. 6 (classification rules): https://artificialintelligenceact.eu/article/6/
