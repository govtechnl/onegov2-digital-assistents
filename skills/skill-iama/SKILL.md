---
name: iama
description: "Use this skill to decide whether a public-sector digital assistant needs a fundamental-rights and legal assessment, and to prompt the developer accordingly — before the assistant is built or deployed. Trigger it whenever an assistant could affect people or their rights (decisions or advice about benefits, permits, debt help, access to services, sanctions, risk scoring), processes personal or special-category data, or could disadvantage specific groups. It walks the developer through screening questions, flags which instruments apply (IAMA / Impact Assessment Mensenrechten en Algoritmes, DPIA under the AVG/GDPR, the EU AI Act Article 27 fundamental-rights impact assessment), cross-checks against concrete legal duties (AI Act, AVG, Awb), and routes the work to the compliance officer, privacy officer (FG/DPO) and IAMA facilitator. Triggers include 'IAMA', 'mensenrechten', 'grondrechten', 'fundamental rights', 'FRIA', 'DPIA', 'persoonsgegevens', 'personal data', 'geautomatiseerde besluitvorming', 'automated decision', 'AVG', 'GDPR', or building an assistant that decides or advises on entitlements for citizens. Do NOT treat this as something to certify in code — the skill prompts, flags and routes; it does not perform or sign off the assessment."
---

# IAMA — triggering a fundamental-rights and legal assessment

When a public-sector assistant can affect people — decisions about benefits, permits, debt support, access to services, or any processing of personal data — the team must run a fundamental-rights and legal assessment *before* building and deploying it. In the Netherlands the instrument for the fundamental-rights part is the **IAMA** (Impact Assessment Mensenrechten en Algoritmes); alongside it sit the **DPIA** (AVG), the EU AI Act's **Article 27 fundamental-rights impact assessment (FRIA)**, and obligations under the **Algemene wet bestuursrecht (Awb)**. This skill's job is to **notice when such an assessment is needed, prompt the developer with the right questions, flag the obligations, and route the work to the responsible people** — not to perform or sign off the assessment itself.

## You are the trigger, not the assessor

Be explicit with yourself and the developer: an IAMA is a **multidisciplinary human deliberation** (legal, policy, domain, and affected-group perspectives), and whether something is lawful is a judgement for the organisation's compliance officer, privacy officer (FG/DPO), and legal counsel — not something to certify in code. Your role is to:

- **Detect** that an assessment is likely needed;
- **Ask** the developer the screening questions below, rather than assuming the answers;
- **Flag** which assessments and legal duties apply;
- **Route** the work to the right humans, at the right moment (before build and deploy);
- **Help prepare** — gather inputs, structure the dossier, and turn the legal cross-check into a checklist the humans verify.

Drafting and organising materials is welcome; deciding "this is compliant" is not yours to do.

## When to raise this

Raise it proactively when the assistant (now, or plausibly in a later iteration):

- supports or makes **decisions about people** — eligibility, entitlements, prioritisation, risk scoring, sanctions; or
- processes **personal data**, and especially **special-category** data (health, ethnicity, and so on); or
- affects **access to public services or rights**, or could **disadvantage specific groups**; or
- operates in a **sensitive domain** — benefits, permits, debt help, enforcement, fraud, immigration.

If none of these hold — for example a purely internal developer tool with no personal data and no effect on people — an IAMA is likely not required; say so briefly and move on. When you are unsure, treat it as in scope and ask.

## Screening questions to put to the developer

Ask these in plain language before going further — don't infer them:

1. Who is affected, and can the assistant's output influence a **decision about a person**? Is it information-only, advisory, or decisional?
2. Does it process **personal data**? Any **special-category** data?
3. Could it **disadvantage specific groups** — and how would you detect that if it did?
4. Is there **meaningful human involvement** before any decision takes effect, or could it act automatically? (→ AVG art. 22)
5. What is the **domain and what is at stake** (benefits, permits, enforcement…)?
6. Has a **DPIA** been done or started? Is there an **AI Act risk classification**? (If it looks high-risk, use the `ai-act-high-risk` skill.)

## What the answers imply

- **Personal data involved** → a **DPIA** (AVG art. 35) is likely required; involve the FG/DPO.
- **Effect on fundamental rights or decisions about people** → an **IAMA** is warranted.
- **High-risk under the AI Act and you are a public body (deployer)** → an **Article 27 FRIA** is mandatory before first use and must be notified to the market-surveillance authority. The IAMA can do much of the FRIA's work, but confirm it covers the FRIA's required points (intended purpose, frequency, affected groups, risks, human-oversight and mitigation measures). Hand the classification to the `ai-act-high-risk` skill.
- **Automated decisions without meaningful human involvement** → an AVG art. 22 problem; either build in genuine human intervention or have the exception justified by legal.
- **In every case**: an IAMA on its own is **necessary but not sufficient** — its outcomes must be cross-checked against the concrete legal duties. Walk `references/legal-cross-check.md` with the developer.

## Help assemble the dossier (for the humans to own)

Offer to prepare a **toetsingsdossier** — the file that proves, at an audit or enforcement review, that the analysis was actually done. Structure it from `templates/toetsingsdossier-outline.md`. At minimum: the AI-risk classification with reasoning; the legal cross-check result (what is covered, what is open, with an owner and deadline per open item); the DPIA outcome; the IAMA findings; the human-oversight plan; and the registration evidence (verwerkingsregister, and the EU database where applicable). Keep it at least as long as the system is in use plus five years — ten years for high-risk systems (AI Act art. 18).

## Timing and re-triggering

This is not one-and-done. Raise it again, and reopen the dossier, on any **material change**: a new purpose or use beyond the original; new data sources or system coupling; a wider audience (internal → external, or a new group of citizens); a changed model or version with different outputs; or monitoring signals about bias, errors, or citizen complaints. Record each re-assessment with its date and outcome.

## Pitfalls to name out loud

- **Ticking off an IAMA without the legal cross-check.** The IAMA conversation is valuable but does not automatically cover AVG art. 22 or the AI Act high-risk duties — always do both.
- **Classifying the risk too low.** Doubt about the category points to the *higher* one; the burden of justifying a lower classification sits with the organisation.
- **A stale dossier.** An out-of-date dossier is worse than none — it feigns compliance while the reality has moved on.
- **Human oversight on paper only.** An oversight procedure that nobody actually follows does not count as a safeguard, legally or in practice.

## Sources

- IAMA — Impact Assessment Mensenrechten en Algoritmes (Rijksoverheid/BZK): https://www.rijksoverheid.nl/documenten/rapporten/2021/02/25/impact-assessment-mensenrechten-en-algoritmes
- Algoritmekader (BZK): https://minbzk.github.io/Algoritmekader/
- EU AI Act, Article 27 (FRIA): https://artificialintelligenceact.eu/article/27/
- AVG/GDPR (esp. art. 22, art. 35) — Autoriteit Persoonsgegevens: https://www.autoriteitpersoonsgegevens.nl/
- Algemene wet bestuursrecht (Awb): https://wetten.overheid.nl/BWBR0005537/
