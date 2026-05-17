---
id: llmops-monitoring
title: LLMOps and Monitoring
summary: Continuously monitor model behaviour, drift, and incidents in production.
domains: [technical-performance, answer-quality, governance]
phases: [Pilot, Production]
levels: [Operational, Tactical]
sources: [onegov-principles, ai-act]
---

Set up monitoring for latency, error rates, source coverage, refusal rates, and user feedback. Alert on regressions versus a known-good baseline.

Capture redacted traces of representative interactions for offline evaluation. Combine automated metrics with periodic human review of samples.

Tie every alert to a runbook with an owner and an explicit rollback path. Without that link, the alert is noise.
