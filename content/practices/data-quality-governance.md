---
id: data-quality-governance
title: Data Quality and Governance
summary: Make data ownership, quality checks, and lifecycle explicit before an assistant uses any source.
domains: [infrastructure-data, governance, compliance]
phases: [PoC, Pilot, Production]
levels: [Tactical, Strategic]
sources: [gdpr, onegov-principles]
---

Name a data owner per source and document quality expectations (freshness, completeness, accuracy). Define how out-of-date or unreliable sources are quarantined and re-enabled.

Maintain a versioned record of which datasets the assistant may use, when they were last reviewed, and who signed off. Connect this record to the assistant's release notes so a release is always paired with the dataset state it was tested against.

Quality gates: failing freshness, completeness, or accuracy thresholds blocks promotion of a build to the next environment.
