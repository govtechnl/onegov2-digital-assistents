# NL API Strategie

The [Nederlandse API Strategie](https://docs.geostandaarden.nl/api/API-Strategie/) is the Dutch government's shared playbook for designing and operating APIs. The hackathon brief explicitly calls it out as a reference Skills may want to encode.

For digital assistants, the API Strategie matters in three places:

1. **The data layer your assistant reads from.** Most government source systems already expose API-Strategie-compliant REST endpoints (Haal Centraal, Open Zaak, Producten en Diensten, …). A Skill that helps a team build a retriever should encode the conventions: pagination, expansion, versioning headers, error formats.
2. **The interface your assistant exposes** (if any). When the assistant is wrapped in a backend service consumed by frontends or other systems, that service should itself follow the API Strategie.
3. **The provenance trail.** Every assistant response that derives from a government API call must be traceable to the specific endpoint, version, and timestamp. This is both an API-Strategie convention and an Answer Quality requirement (see [content/domains/answer-quality.md](../../content/domains/answer-quality.md)).

## Skill ideas

- A Skill that, given a piece of code calling a Dutch government API, checks compliance with the API Strategie's URI conventions, paging parameters, content negotiation, and error format.
- A Skill that generates an `openapi.yaml` skeleton for an assistant's own backend that already encodes the API Strategie's mandatory headers and error model.
- A Skill that, when a developer is wiring an assistant to Haal Centraal or Open Zaak, reminds them of the consent and authorisation patterns required by [Common Ground](common-ground.md).

## References

- [API Strategie, design rules](https://docs.geostandaarden.nl/api/API-Strategie-DR/)
- [API Strategie, modules](https://docs.geostandaarden.nl/api/API-Strategie-mod/)
- [API.overheid.nl, the registry of Dutch government APIs](https://api.overheid.nl/)
