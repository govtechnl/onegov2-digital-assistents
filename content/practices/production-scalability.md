---
id: production-scalability
title: Production Scalability
summary: Make sure the assistant keeps performing under realistic and peak load.
domains: [technical-performance, infrastructure-data, sustainability]
phases: [Pilot, Production]
levels: [Operational, Tactical]
sources: [onegov-principles]
---

Test against realistic traffic patterns including peak windows (e.g. tax season, benefits deadlines). Identify scaling limits of the model endpoint, the retriever, and the data sources.

Define autoscaling, caching, and back-pressure strategies. Document graceful-degradation behaviour: what does the assistant tell the user when a component is unhealthy?

A scalability claim without a tested degradation path is a hope, not a plan.
