# Dutch legal context for digital accessibility

Read this when the assistant is being built for a Dutch government body (rijk, provincie, gemeente, waterschap, or a publiekrechtelijke instelling), or whenever the developer asks what accessibility is legally required. It explains the floor you must meet and the obligations beyond the code itself.

## What the law requires

- Accessibility is **mandatory** for all websites, intranets, extranets, cloud applications, mobile apps, and the content on them, for Dutch government bodies. The obligation lives in the **Besluit digitale toegankelijkheid overheid**, which since July 2023 is part of the **Wet digitale overheid (Wdo)**. (The word "Tijdelijk" has been dropped; the decree itself stays in force.)
- The decree requires conformance by applying the European standard **EN 301 549**, which incorporates **WCAG 2.1 level A and AA**. That is the binding floor.
- A valid **accessibility statement (toegankelijkheidsverklaring)** must be published for every website and app — this is a separate legal obligation from the code conforming.

## WCAG 2.1 vs 2.2 — what to build to

- **Legal floor:** WCAG **2.1 AA** (via EN 301 549). You must never fall below this.
- **Build target:** WCAG **2.2 AA**. WCAG 2.2 was published by W3C in October 2023 but is **not yet legally mandatory** for government bodies, because it has not been incorporated into EN 301 549 yet, and there is no fixed date for that. However, 2.2 is recommended for new builds, central government already reports against 2.2, and because 2.2 is a superset of 2.1, building to 2.2 satisfies the legal floor automatically. So: ship 2.2 AA, treat 2.1 AA as the non-negotiable minimum.

## The accessibility statement (toegankelijkheidsverklaring)

This is the part teams most often forget, and it is legally required.

- Publish a statement for each website/app, conventionally linked from `www.<domein>.nl/toegankelijkheid`.
- Create it with the official *invulassistent* at https://www.toegankelijkheidsverklaring.nl/ — it walks through a fixed model.
- The statement declares a conformance status: **fully** compliant, **partially** compliant (with the known issues and a remediation plan), or **not** compliant. Partial conformance is explicitly allowed — so a known, documented gap with a plan is acceptable, while an undeclared gap is not.
- Compliance must be evidenced by a valid accessibility audit, and websites are expected to be re-tested periodically (the common cadence is at least every three years / 36 months).
- Practically: even if you cannot fix everything before launch, the statement must still exist and tell the truth about what works and what does not.

## Procurement angle (relevant to vendors)

Government bodies must procure accessible products and services. If the assistant is built or supplied by an external vendor, that vendor must be able to demonstrate how accessible the product is. Accessibility is therefore a contractual and tender requirement, not only a build-time concern.

## Beyond government: the EAA

The **European Accessibility Act (EAA)**, as implemented in Dutch law, applies from **28 June 2025** and extends accessibility requirements to many **private-sector** digital services (for example banking, e-commerce, transport, telecoms). If the assistant is for a private organisation rather than a government body, accessibility may still be legally required under the EAA — confirm scope with the developer rather than assuming it is exempt.

## Who is responsible

Accessibility is not something the web team can deliver alone. It involves management (mandate and budget), procurement (accessible tenders), legal/privacy, designers (house style and contrast), content editors (alt text, plain language, document accessibility), developers, and testers. When you flag accessibility work, flag it as an organisation-wide responsibility, not just a front-end ticket.

## Sources

- DigiToegankelijk — wetgeving en richtlijnen: https://www.digitoegankelijk.nl/wetgeving/wat-is-verplicht
- Digitale Overheid — beleid digitale toegankelijkheid: https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/digitale-inclusie/digitaal-toegankelijk/beleid/
- Toegankelijkheidsverklaring (invulassistent): https://www.toegankelijkheidsverklaring.nl/
- CommunicatieRijk — verplichte richtlijnen digitale toegankelijkheid: https://www.communicatierijk.nl/vakkennis/rijkswebsites/verplichte-richtlijnen/digitale-toegankelijkheid
- WCAG 2.2 — W3C: https://www.w3.org/TR/WCAG22/
