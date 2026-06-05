---
name: privacy-anonimisering
description: Gebruik deze skill wanneer je een digitale assistent bouwt die persoonsgegevens van burgers verwerkt én geaggregeerde inzichten moet leveren. De skill dwingt een harde scheiding af tussen de pseudonieme verwerkingslaag (individuele afhandeling) en de volledig anonieme inzichtenlaag (rapportages en dashboards), en begeleidt je door de bijbehorende AVG- en EU AI Act-verplichtingen.
---

# Privacy & Anonimisering

## Wanneer gebruik je deze skill

Gebruik deze skill als de assistent:

- Signalen, meldingen, klachten of verzoeken van burgers verzamelt via één of meerdere kanalen
- Individuele meldingen classificeert, routeert of doorzet naar medewerkers of externe partijen
- Geaggregeerde rapportages, dashboards of trendanalyses produceert op basis van die meldingen
- Gegevens combineert met externe databronnen (open data, weerdata, geodata, etc.)

De skill is in het bijzonder van toepassing wanneer het systeem twee verschillende doelgroepen bedient: medewerkers die individuele meldingen afhandelen (en daarvoor persoonsgegevens nodig hebben), en beleidsmakers of bestuurders die uitsluitend geaggregeerde inzichten mogen zien.

## Wat te doen

### Stap 1 — Stel de AVG-grondslag vast vóór de verwerking

Documenteer voor elk type verwerking de wettelijke grondslag onder de AVG:

- **Individuele afhandeling** (pseudonieme laag): voor gemeenten vaak de uitvoering van een publieke taak (AVG art. 6 lid 1 sub e). Leg de grondslag per meldingstype vast.
- **Geaggregeerde analyse** (anonieme laag): zodra gegevens aantoonbaar anoniem zijn, valt de verwerking buiten de AVG. Motiveer expliciet waarom de gegevens als anoniem worden beschouwd — anonimiteit is geen gevolg van aggregatie alleen.
- **Sociale media en openbare bronnen**: ook openbare berichten zijn persoonsgegevens onder de AVG. Bepaal een afzonderlijke grondslag en voer een proportionaliteitstoets uit voordat je deze bronnen activeert. Haal juridisch advies in.

### Stap 2 — Schei de dataarchitectuur in twee strikte lagen

Ontwerp en implementeer een harde scheiding tussen:

| Laag | Bevat | Toegang | Bewaartermijn |
|---|---|---|---|
| **Persoonlijke laag** | Naam, contactgegevens, adres, volledige meldingstekst | Uitsluitend behandelende medewerkers | Doelgebonden; verwijder na afsluiting + wettelijke bewaartermijn |
| **Inzichtenlaag** | Meldingstype, tijdstip, wijkcode, uitkomst | Analisten, managers, dashboards | Langere retentie toegestaan; geen persoonsgegevens |

De splitsing vindt plaats **bij inname**, niet op het moment van rapportage. Persoonsgegevens mogen nooit — ook niet tijdelijk — de inzichtenlaag bereiken.

### Stap 3 — Pseudonimiseer de persoonlijke laag, anonimiseer de inzichtenlaag

- **Persoonlijke laag**: vervang directe identificatoren (naam, e-mail, telefoonnummer) direct bij binnenkomst door een zaak-ID. Sla de koppeling op in een afzonderlijke, toegangsbeheerde sleuteltabel. Medewerkers werken met het zaak-ID; alleen de sleuteltabel legt de koppeling met de persoon.
- **Inzichtenlaag**: verwijder alle directe én indirecte identificatoren voor inname. Pas k-anonimiteit toe (zie stap 4) voordat gegevens deze laag bereiken.

### Stap 4 — Pas k-anonimiteitsdrempels toe op alle geaggregeerde uitvoer

Publiceer of toon nooit een getal als de onderliggende groep te klein is om herleiding te voorkomen:

- **Standaarddrempel: k = 5** — onderdruk elke cel waarbij minder dan 5 meldingen de grondslag vormen.
- **Gevoelige combinaties** (bijv. meldingstype + wijk + week): verhoog de drempel naar k = 10 of pas celonderdrukking toe.
- Onderdruk bij celonderdrukking ook de complementaire cel als die terugrekening mogelijk maakt.
- Leg de gekozen drempel vast in het systeemontwerp en maak hem zichtbaar in dashboards (bijv. "Niet weergegeven: minder dan 5 meldingen in deze periode").

### Stap 5 — Voer een DPIA uit als dat verplicht is

Een gegevensbeschermingseffectbeoordeling (DPIA) is **verplicht** als twee of meer van de volgende criteria van toepassing zijn:

- Systematische monitoring van burgers op grote schaal
- Combinatie van gegevens uit meerdere bronnen
- Profilering van personen of gebieden
- Kwetsbare groepen behoren mogelijk tot de betrokkenen

Betrek de Functionaris Gegevensbescherming (FG/DPO) vóór de pilotfase. Ga niet live zonder afgeronde DPIA.

### Stap 6 — Registreer in het Algoritmeregister

Als de assistent routeringsbeslissingen beïnvloedt of analyses produceert die beleidsvorming ondersteunen:

- Registreer het systeem in het [Algoritmeregister](https://algoritmeregister.overheid.nl) vóór de livegang.
- Beschrijf: doel, gebruikte gegevens, menselijk toezichtmechanisme, contactpersoon.
- Werk de registratie bij bij elke materiële wijziging van het systeem.

### Stap 7 — Informeer burgers over het gebruik van AI

Op grond van EU AI Act art. 50 en AVG art. 13-14 moeten burgers geïnformeerd worden:

- Dat hun melding verwerkt kan worden door een AI-assistent.
- Welke gegevens worden verzameld, voor welk doel en hoe lang ze worden bewaard.
- Bij wie ze terecht kunnen voor inzage, correctie of verwijdering.

Voeg deze informatie toe aan elk inname-kanaal (webformulier, e-mail auto-reply, telefoonscript).

## Te volgen conventies

- Gebruik de term **pseudoniem** (niet anoniem) voor de persoonlijke laag — ook na vervanging door een zaak-ID is herleiding nog mogelijk via de sleuteltabel.
- Gebruik de term **anoniem** uitsluitend wanneer herleiding aantoonbaar onmogelijk is, ook als de sleuteltabel wordt vernietigd.
- Leg de k-anonimiteitsdrempel vast in codekommentaar en dashboarddocumentatie zodat toekomstige ontwikkelaars hem niet per ongeluk verlagen.
- Voeg een verwijzing naar de DPIA toe vanuit het architectuurbesluitdocument (ADR) van het systeem.
- Grondslag in het raamwerk: [`content/domains/ethiek-mensenrechten.md`](../../content/domains/ethiek-mensenrechten.md), [`content/practices/data-logbescherming.md`](../../content/practices/data-logbescherming.md)

## Wat te vermijden

- **Niet** één gecombineerde dataopslag bouwen voor persoonlijke en analytische gegevens, met query-filtering als enige scheidingsmechanisme — dit is foutgevoelig en niet auditeerbaar.
- **Niet** aggregatie gelijkstellen aan anonimisering. Vijf rijen gegroepeerd op wijk zijn niet anoniem.
- **Niet** vrije tekst van meldingen opnemen in de inzichtenlaag — vrije tekst bevat vrijwel altijd namen, adressen of andere identificatoren.
- **Niet** een DPIA overslaan omdat het systeem "alleen routeert" — routeringsbeslissingen kunnen toegang tot diensten beïnvloeden en kwalificeren als hoog-risicoverwerking.
- **Niet** sociale media activeren zonder afzonderlijke grondslag en proportionaliteitstoets.
- **Niet** de k-anonimiteitsdrempel verlagen onder tijdsdruk om rijkere dashboarddata te tonen.

## Aanvullende bronnen

- [`content/domains/ethiek-mensenrechten.md`](../../content/domains/ethiek-mensenrechten.md) — Domein Ethiek & Mensenrechten: bias, transparantie en menselijke controle.
- [`content/practices/data-logbescherming.md`](../../content/practices/data-logbescherming.md) — Privacy-by-design patronen, PII-filtering en logbescherming.
- [`skills-IAMA/iama-wettelijke-toetsing.md`](../../skills-IAMA/iama-wettelijke-toetsing.md) — Wettelijke toetsingstabel voor AVG, EU AI Act en IAMA.
- [Algoritmeregister](https://algoritmeregister.overheid.nl) — Registratieportaal voor overheids-AI-systemen.
- [Autoriteit Persoonsgegevens — DPIA-handleiding](https://www.autoriteitpersoonsgegevens.nl/themas/beveiliging/data-protection-impact-assessment-dpia) — Officiële DPIA-richtlijnen.
