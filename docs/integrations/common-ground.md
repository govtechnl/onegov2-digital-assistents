# Integration, Common Ground

[Common Ground](https://commonground.nl/) is the Dutch municipal information-architecture vision: decouple data from process and applications, expose data via APIs, and prefer reuse over rebuild. It directly shapes how a government digital assistant should retrieve and use data.

## Why it matters here

- A Common Ground-aligned assistant **retrieves data at the moment of use** from authoritative APIs, instead of duplicating it into its own store.
- This keeps answers fresh, auditable, and consistent with the rest of the municipal stack.
- It also forces a clean separation between *retrieval / source-of-truth* and *generation*, which is exactly the boundary an LLM assistant needs.

## Layered model recap (very brief)

- **Layer 1, Data.** Authoritative registers (BRP, BAG, BRK, Kadaster, RDW, ...).
- **Layer 2, Services.** API gateways and standardised endpoints over Layer 1.
- **Layer 3, Integration / orchestration.** Composition of services, including agents.
- **Layer 4, Interaction.** User-facing applications, including the assistant.
- **Layer 5, Process.** End-to-end business processes.

A digital assistant typically lives at Layer 4 and consumes Layers 2/3.

## What to do in your assistant

- **Retrieve from APIs, do not cache silently.** If you must cache for performance, log the TTL and the data owner.
- **Pin to versioned API contracts.** Treat a breaking API change as a release-blocking event.
- **Carry provenance through.** Every retrieved fact must keep its source identifier (e.g. BAG object id, BRP record reference) so the assistant can cite it.
- **Honour authorisation at the API.** Do not let the assistant elevate privileges; pass the user's session through.
- **Prefer Haal Centraal endpoints** (or municipal equivalents) over scraping web pages.

## Common Ground-aligned APIs to know

- **Haal Centraal BRP**, Basisregistratie Personen (personal records).
- **Haal Centraal BAG**, Basisregistratie Adressen en Gebouwen (addresses and buildings).
- **Haal Centraal BRK**, Basisregistratie Kadaster (cadastral data).
- **Open Zaak / ZGW APIs**, case-management (Zaken, Documenten, Catalogi, Besluiten).
- **NLX / FSC**, inter-organisational API broker for the Dutch public sector.

## Pitfalls to avoid

- Letting the assistant invent identifiers that look like real BSNs / case numbers, strict output filtering.
- Logging full API responses in clear text, redact PII before storage.
- Storing retrieved personal data in a vector index, keep it ephemeral or, if persisted, treat the index as a personal-data store with full GDPR controls.

## References

- Common Ground portal: <https://commonground.nl/>
- VNG API standaarden: <https://vng-realisatie.github.io/api-standaarden/>
- NLX: <https://nlx.io/>
- Haal Centraal: <https://github.com/VNG-Realisatie/Haal-Centraal>
