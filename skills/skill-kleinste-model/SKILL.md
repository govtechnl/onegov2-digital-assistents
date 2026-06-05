---
name: kleinste-model-per-taak
description: "Use this skill whenever a digital assistant will make LLM calls and a model has to be chosen or configured — at architecture time, when wiring up an inference call, or any time the default is to reach for the biggest/frontier model for everything. It enforces 'choose the smallest model that can handle the task': decompose the assistant into discrete tasks, judge each task's difficulty, and make the developer pick — and write down — which model each task uses, starting from the smallest plausible model and escalating to a larger one only when evals on a golden dataset show the small one falls short. Small models for easy tasks, large models for hard tasks. Triggers include 'which model', 'model selection', 'kies een model', 'kleinste model', 'model routing', 'router', 'select-then-route', 'SLM', 'frontier model', 'too expensive', 'latency', 'token cost', 'inference cost', 'energy of inference', or building/configuring any LLM-backed feature. Also raise it when an assistant uses one large model uniformly across every task. It does NOT pin specific model names — it gives a method and a config the team fills with their own models, provider-agnostic."
---

# Choose the smallest model that can handle the task

Not every task needs a frontier model. Reaching for one big general-purpose model for everything is the easy default, and it is wasteful: it costs more, runs slower, and burns more energy than the work requires. At the volume a citizen-facing assistant handles, that waste compounds — a mature assistant spends most of its footprint on inference, so the model you pick per task is one of the highest-leverage decisions you make. The rule is simple: **per task, pick the smallest model that reliably does the job, and use a big model only where the task genuinely needs it.**

Your role here is to make that choice **explicit and per-task** — not implicit and uniform. Make the developer decide, and record, which model each task uses.

## Step 0 — does this task even need an LLM?

Before choosing a model, ask whether the task needs an LLM at all. For deterministic work — a lookup in a table, a fixed set of answers, a query that maps to one source — a classic database or search function is typically orders of magnitude cheaper and greener than any LLM call. **AI is not a default; it is a choice with a cost.** Strip the tasks that don't need a model before sizing the ones that do.

## Make the developer define the per-task mapping

This is the heart of the skill. Don't let model choice stay implicit (a single `model=` constant threaded everywhere) or uniform (the biggest model for all). Instead:

1. **Decompose** the assistant into the discrete tasks it performs — e.g. intent classification, routing, entity extraction, FAQ answering, summarisation, drafting, multi-step reasoning, tool/agent use.
2. For each task, have the developer choose a model and **write it down** in a routing map (start from `templates/model-routing-map.yaml`). The map is the single source of truth and lives in config, so models can be swapped without touching code.
3. If the developer hasn't decided, **ask** them per task — or propose a draft mapping based on task difficulty for them to confirm. The choice is theirs to own; your job is to force the decision into the open and capture it.

A task→model map that someone deliberately filled in beats a buried default every time — it can be reviewed, measured, and changed.

## Right-size each task: smallest first, escalate on evidence

For each task, start at the **smallest plausible model** and move up only when you have to:

- **Start small, then measure.** Run the candidate model against your **golden dataset** (see your evaluation / offline-validation practice) and measure both **quality** and **cost** (tokens, latency, energy). Upgrade to a larger class **only when the quality demonstrably falls short** for that task — not because a bigger model "feels smarter".
- **"Smallest that can handle the task" = smallest model that passes your eval bar** for that task. Define the bar per task before choosing.
- **Compare per task, not per leaderboard.** A FAQ assistant and a document-searching agent have different needs; a general ranking doesn't know your use case. Where useful, consult per-task energy/efficiency sources rather than headline rankings.
- Small, fine-tuned models (SLMs) are often a structurally cheaper, greener fit for narrow, domain-specific tasks — consider them, but still verify on your data.

See `references/right-sizing-method.md` for difficulty signals, how to define tiers, and routing patterns.

## Route instead of defaulting

Once tasks are sized, wire the dispatch so simple prompts go to a small model and only complex ones reach a large model — a **router** (select-then-route) or a **cascade** (try small first, fall back to large on low confidence). Small/large routing is the technique with the highest demonstrated efficiency at preserved quality. Keep every route's model, endpoint, timeout, and token limit in **configuration**, not hard-coded, so the mapping stays swappable. (Routing detail is in `references/right-sizing-method.md`; this composes with a dedicated select-then-route practice if you have one.)

## Re-audit periodically

Model choice is not set-and-forget. New models appear, tasks change, and usage grows — all of which shift the optimum. Re-run the comparison at least yearly (and whenever a task or its volume changes materially), and update the routing map with the date. A choice that was efficient one year can be outdated the next.

## Pitfalls

- **Defaulting to the biggest model "to be safe."** At scale this quietly multiplies cost, latency, and energy; the safety is illusory if you never measured whether a smaller model passes.
- **Choosing by vibes, not evals.** "Seems smarter" is not a basis — measure quality and cost on the golden dataset.
- **One model for every task.** This couples easy and hard tasks to the same expensive tier; the win comes from separating them.
- **Hard-coding model IDs throughout the code.** It makes right-sizing and swapping impossible — put the mapping in config.
- **Escalating by default instead of as evidence.** Start small and move up on proof, not the reverse.
- **Over-optimising no-volume tasks.** Don't spend a week shaving cents off a once-a-day call; match the effort to the task's volume too.

## How this fits the rest of the framework

Right-sizing is one lever among several for efficient, sustainable inference — it pairs with making each call itself leaner (output limits, streaming, caching, RAG tuning) and with the evaluation discipline that tells you whether a smaller model is good enough. It is also a sustainability decision, not only a technical one: weigh social and economic criteria alongside pure energy efficiency.

## Sources

- AI Energy Score (Hugging Face) — per-task energy efficiency: https://huggingface.github.io/AIEnergyScore/
- ML.Energy Leaderboard: https://ml.energy/leaderboard
- UNESCO — Greening AI (smaller, greener): https://courier.unesco.org/en/articles/greening-ai-smarter-smaller-stronger
- Model routing, selection & cascades (Brenndoerfer): https://mbrenndoerfer.com/writing/model-routing-selection-ab-testing-cascades-strategies
- Multi-LLM routing strategies on AWS: https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/
- AI Sustainability Check (AlgorithmWatch / SustAIn): https://sustain.algorithmwatch.org/en/how-sustainable-is-my-ai/
