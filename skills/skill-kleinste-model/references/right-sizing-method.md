# Right-sizing method — difficulty, tiers, routing, verification

Read this to actually size each task and wire the routing. It is a method, not a model list — fill in your own models, provider-agnostic.

## 1. Judge each task's difficulty

For each task, rate the signals that drive how capable a model has to be:

- **Input complexity** — short and well-formed, or long, messy, multi-document?
- **Reasoning depth** — pattern-match / classify / extract (shallow), or multi-step inference and synthesis (deep)?
- **Output structure** — a label or short span (easy to get right and to check), or open-ended generation?
- **Stakes / risk** — does an error affect a person's rights, money, or access to a service? Higher stakes raise the quality bar (and may pull in the `skill-iama` / `ai-act-high-risk` skills).
- **Error tolerance** — can a wrong answer be cheaply caught and corrected, or does it go straight to a citizen?
- **Latency sensitivity** — is this in the interactive path where speed is UX, or a background job?
- **Volume / frequency** — high-volume tasks are where right-sizing pays off most; rare tasks rarely justify much tuning.

Shallow + structured + low-stakes + high-volume → strong candidate for the smallest tier. Deep + open-ended + high-stakes → where a large model earns its cost.

## 2. Define model tiers (abstractly, then fill in)

Define a small number of tiers and slot your actual models in (the routing map captures this):

- **Tier S — small / fast / cheap.** Classification, routing, extraction, short FAQ answers; often an SLM, possibly fine-tuned for your domain.
- **Tier M — mid-capability.** Summarisation, straightforward drafting, moderate reasoning.
- **Tier L — most capable.** Hard multi-step reasoning, ambiguous or high-stakes tasks, complex tool/agent use.
- **Non-model routes.** Don't forget: a deterministic **database/search** route (for lookups), and a **human** route (for high-risk or low-confidence cases). The cheapest, greenest call is the LLM call you avoid.

Keep tiers provider-agnostic: name them by role, not by vendor, so swapping a model is a config change.

## 3. Smallest first, escalate on evidence

The discipline that makes "smallest model" real:

1. For a task, set its **eval bar** first — the quality threshold on your golden dataset that the task must meet (and any latency budget).
2. Try **Tier S**. Run it against the golden dataset; measure **quality** and **cost** (tokens, latency, energy).
3. If it **passes the bar**, you're done — that's the smallest model that can handle the task.
4. If it **fails**, escalate one tier and repeat. Escalate on measured shortfall, never pre-emptively.
5. Record the chosen tier, the bar, and the measurement date in the routing map.

"Compare per task, not per leaderboard": a model that tops a general ranking may be overkill (or a poor fit) for your specific task. Per-task energy/efficiency sources (AI Energy Score, ML.Energy Leaderboard) are more relevant than headline rankings.

## 4. Routing patterns

Two complementary ways to dispatch by difficulty:

- **Select-then-route.** A lightweight front step classifies the incoming request — by rules or a small/cheap LLM call — and sends it down the matching route (search, Tier S, Tier M/L, or human) based on type, risk, latency, and cost. Build it as a small central router service; an orchestration framework (e.g. LangChain, Semantic Kernel) helps manage routes, prompts, and tools.
- **Cascade / fallback.** Try the small model first; if its confidence (or a cheap validator) is below threshold, fall back to a larger model. Good when classification is itself hard.

Per route, keep model, endpoint, timeout, token limit, and policy in **config** (YAML/JSON/env) so routes can be swapped and extended. Send route, model, latency, and error metrics to your observability stack so the routing strategy is measurable and tunable.

## 5. Re-audit

Re-run the per-task comparison at least yearly, and whenever a task changes, a model is added/retired, or volume grows materially. Update the routing map with the new decision and date. Treat the map as a living document, not a one-time setup.

## Sources

- AI Energy Score (Hugging Face): https://huggingface.github.io/AIEnergyScore/
- ML.Energy Leaderboard: https://ml.energy/leaderboard
- Model routing, selection & cascades (Brenndoerfer): https://mbrenndoerfer.com/writing/model-routing-selection-ab-testing-cascades-strategies
- Multi-LLM routing strategies on AWS: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- UNESCO — Greening AI: https://courier.unesco.org/en/articles/greening-ai-smarter-smaller-stronger
