# Human-oversight plan — <assistant / solution name>

> Fill this in for the solution. It defines how a human stays in control, and whether
> that control is optional (low-risk) or mandatory (high-risk). It is the detailed
> version of section 5 ("Human-oversight plan") of the toetsingsdossier in the
> `skill-iama` skill — link the two.

## 0. Risk and obligation
- **Risk classification** (from the `ai-act-high-risk` skill): ☐ Minimal ☐ Limited ☐ High-risk ☐ Prohibited
- **Is human oversight MANDATORY here?** ☐ Yes (high-risk / AVG art. 22 decision) ☐ No (optional but provided)
- **Legal basis if mandatory:** ☐ AI Act art. 14 ☐ AVG art. 22 ☐ FRIA (art. 27)
- If mandatory, oversight is **non-bypassable** and occurs **before the decision takes effect**.

## 1. Oversight model
- **Model chosen:** ☐ Human in the loop ☐ Human on the loop ☐ Human above the loop ☐ Human before the loop (may combine)
- **Why this model** (risk, system type, volume, lifecycle phase):

## 2. The boundary — what the system may never decide alone
- Decisions always made by a human, even when the assistant advises:
- How this boundary is enforced in practice (not just on paper):

## 3. Intervention thresholds (when a human MUST step in)
| Condition (e.g. confidence < X, case type, flagged risk) | Action | Who |
|---|---|---|
| … | | |

## 4. The overseer
- **Who reviews / can intervene** (role):
- **RACI/VERI** — responsible per phase / accountable for deviant behaviour / contact for operational signals:
- **Can they actually act?** Technical ability to halt / set aside / reverse: ☐  | Organisationally free to go against the system (not penalised): ☐

## 5. Mechanisms built into the solution
- **Escalation / handoff to a human** (how it is triggered and reached):
- **Override / stop control** (where in the UI; accessible per `wcag-accessibility`):
- **Routing** of low-confidence / high-stakes cases to a person:
- **Logging** of human decisions (who, what changed, when):

## 6. Guarding against sham oversight
- **Deviation monitoring** — how you track whether reviewers actually deviate (near-zero = red flag):
- **Anti-automation-bias measures** (e.g. surface uncertainty, withhold suggestion until human forms a view):
- **AP four-dimension check** — strong on all four? ☐ Human ☐ Technology & design ☐ Process ☐ Governance

## 7. Review
- Last reviewed (date / by):
- Re-review on material change (new purpose, model version, volume, monitoring signals).
