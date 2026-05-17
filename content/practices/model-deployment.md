---
id: model-deployment
title: Model Deployment
summary: Deploy and update models in a controlled, reproducible, and reversible way.
domains: [technical-performance, governance, security]
phases: [Pilot, Production]
levels: [Operational, Tactical]
sources: [onegov-principles, ai-act]
---

Treat a model version, its prompts, its retrieval configuration, and its guardrails as a single deployable unit. Pin versions; never let "latest" decide what production runs.

Use shadow or canary rollouts to compare a new version against the current one on a representative traffic slice before full promotion. Define rollback criteria in advance.

Sign-off for production includes evaluation results, an incident playbook, and an explicit decision-maker - not a thumbs-up in a chat.
