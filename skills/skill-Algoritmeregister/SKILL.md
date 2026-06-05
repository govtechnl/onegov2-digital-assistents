---
name: algoritmeregister-publicatie
description: Bereidt een publicatie voor het Nederlandse Algoritmeregister (algoritmes.overheid.nl) voor volgens de MinBZK Publicatiestandaard v1.0.0. Gebruik deze skill zodra een gebruiker een algoritme of AI-systeem wil registreren, publiceren of transparant wil maken in het Algoritmeregister, een algoritmeregistratie wil opstellen of nakijken, de publicatiecategorie (A/B/C) wil bepalen, of de velden van de publicatiestandaard wil invullen. Trigger ook bij termen als "algoritmeregister", "algoritme register", "algoritmes.overheid.nl", "publicatiestandaard", "algoritme registreren", "transparantie algoritme overheid", "impactvol algoritme publiceren", zelfs als de gebruiker niet expliciet om de standaard vraagt.
---

# Algoritmeregister-publicatie voorbereiden

Deze skill helpt een overheidsorganisatie een algoritme of AI-systeem registratieklaar te maken voor het centrale Algoritmeregister van de Nederlandse overheid, volgens de **Publicatiestandaard v1.0.0** (MinBZK, consultatieversie 29-11-2024).

Het einddoel is een **complete, valide conceptregistratie**: alle velden ingevuld volgens de standaard, in toegankelijke taal, klaar om door de organisatie te laten controleren en te uploaden. Deze skill levert het concept; de daadwerkelijke publicatie doet de organisatie zelf via haar eigen registertooling.

## Belangrijk om vooraf te weten

- **Dit is een hulpmiddel, geen juridisch oordeel.** De inhoud (vooral wettelijke basis, risico's, afwegingen) moet de organisatie zelf laten valideren door de verantwoordelijke (proceseigenaar, FG, jurist).
- Publicatie in het register is voor veel algoritmes inmiddels het beleid; voor impactvolle algoritmes en hoog-risico AI-systemen wordt het wettelijk verplicht. Behandel een registratie dus serieus.
- **Eén registratie = één organisatie.** Wordt hetzelfde algoritme bij meerdere organisaties ingezet, dan zijn aparte registraties nodig.

## Werkwijze

Volg deze vier stappen op volgorde. Lees `references/velden.md` voor de exacte definitie, tekenlimiet en instructie van elk veld voordat je dat veld invult.

### Stap 1 — Bepaal de publicatiecategorie

Elke registratie krijgt één categorie. Dit bepaalt mede de toon en de verwachte diepgang. Vraag de gebruiker (of leid af uit de context):

- **Categorie A — Hoog-risico AI-systeem**: het systeem valt onder de hoog-risico-definitie van de AI-verordening (Verordening (EU) 2024/1689), bijv. Annex III-toepassing of veiligheidscomponent. Bij twijfel: doe of vraag eerst een AI Act-risicoclassificatie (Art. 5 verbodscheck → Art. 6 + Annex I/III → Art. 50).
- **Categorie B — Impactvol algoritme**: raakt burgers/bedrijven merkbaar (rechtsgevolgen, profilering, risico-indicatie, of anderszins betekenisvolle impact op betrokkenen), maar is geen hoog-risico AI-systeem.
- **Categorie C — Overig algoritme**: lage impact, geen profilering, geen rechtsgevolgen.

Leg de gekozen categorie en de redenering kort vast — die motivering is zelf waardevol voor de transparantiedoelen.

### Stap 2 — Verzamel de informatie via een gericht interview

Vraag de ontbrekende informatie op, gegroepeerd per blok. Stel niet alles in één keer; werk per blok en hergebruik wat al in het gesprek of in aangeleverde documenten (DPIA, IAMA, procesbeschrijving) staat. De vier blokken zijn:

1. **Algemene informatie** — naam, korte omschrijving, organisatie, thema, status, begin-/einddatum, contactgegevens, eventuele publiekspagina, publicatiecategorie, link naar eigen (decentraal) register.
2. **Verantwoord gebruik** — doel en impact, afwegingen (voor/nadelen + alternatieven + ethiek), menselijke tussenkomst, risicobeheer, wettelijke basis (+ link + titel), verwerkingsregister, uitgevoerde impacttoetsen (+ link + toelichting waarom evt. niet gedaan).
3. **Werking** — gebruikte gegevens (wees specifiek bij persoonsgegevens + bron zoals BRP/BKR), gegevensbron (+ titel), technische werking (input → verwerking → output; minimaal aangeven of het zelflerend is), leverancier (of "Intern ontwikkeld"), link naar broncode.
4. **Metadata** — taal (`nld`), schema (`1.0.0`), bron-ID (interne sleutel), zoektermen.

Voor de exacte vraagstelling, verplichtingen en voorbeelden per veld: zie `references/velden.md`.

### Stap 3 — Stel de veldteksten op

Houd je strikt aan deze regels van de standaard, anders wordt de registratie afgekeurd of slecht weergegeven:

- **Verplichte velden** (worden NIET gepubliceerd als ze leeg zijn): Naam, Korte omschrijving, Organisatie, Status, Contactgegevens, Publicatiecategorie, en (verborgen maar verplicht) Taal en Schema. Vul deze altijd.
- **Tekenlimieten** gelden hard. De belangrijkste: Naam <100, Korte omschrijving <350, vrije-tekstvelden bij "Verantwoord gebruik" en "Gegevens" <2500, Technische werking <5000. Volledige lijst in `references/velden.md`.
- **B1-taalniveau is het streven, en verplicht voor**: Korte omschrijving, Doel en impact, Afwegingen, en Menselijke tussenkomst. Schrijf korte zinnen, vermijd jargon, leg vaktermen uit. Technische werking en juridische velden mogen specialistischer.
- **Geen opmaak.** Het register ondersteunt op dit moment géén enters (regeleinden) en géén opsommingen/bullets. Schrijf elk veld als doorlopende platte tekst in hele zinnen. Gebruik nooit `\n`, opsommingstekens of nummering binnen een veldwaarde.
- **URLs** beginnen altijd met `https://`. **Datums** in `yyyy-mm`. **Status** is exact één van: `In ontwikkeling`, `In gebruik`, `Buiten gebruik`. **Publicatiecategorie** is exact één van: `Hoog-risico AI-systemen`, `Impactvolle algoritmes`, `Overige algoritmes`.
- **Thema** komt uit de Thema-indeling voor Officiële Publicaties; **Organisatie** uit de TOOI-waardelijsten. Verwijs de gebruiker naar die lijsten als de waarde onzeker is, en raad geen waarde die niet bestaat.

Vul `assets/registratie-template.md` (leesbaar concept voor review) én `assets/registratie-skeleton.json` (gestructureerd werkbestand) in. Kopieer beide eerst naar de werkmap voordat je ze bewerkt.

### Stap 4 — Valideer

Draai de validator op het ingevulde JSON-bestand:

```bash
python scripts/validate.py <pad-naar-ingevuld.json>
```

De validator controleert verplichte velden, tekenlimieten, datum- en URL-formaat, toegestane keuzewaarden en de afwezigheid van regeleinden. Los alle gemelde fouten op vóór je het concept teruggeeft. Waarschuwingen (bijv. een leeg "altijd tonen"-veld) meld je aan de gebruiker zodat die bewust kan kiezen.

## Oplevering

Lever aan de gebruiker:
1. Het ingevulde `registratie-template.md` (voor menselijke review en akkoord).
2. Het gevalideerde `registratie-skeleton.json` (om in de eigen registertooling te laden of als basis voor de officiële uploadstructuur).
3. Een korte lijst met **openstaande punten**: velden die de gebruiker zelf nog moet aanvullen of laten valideren (zoals definitieve wettelijke grondslag, links naar gepubliceerde impacttoetsen, of een akkoord van de FG).

Wijs er bij oplevering op dat de organisatie de inhoud zelf controleert en de daadwerkelijke publicatie verzorgt; deze skill maakt het concept, niet de definitieve registratie.

## Referenties in deze skill

- `references/velden.md` — volledige veldcatalogus van Publicatiestandaard v1.0.0 (definitie, type, verplicht/altijd-tonen, tekenlimiet, instructie en voorbeeld per veld). Lees dit voordat je velden invult.
- `assets/registratie-template.md` — leesbaar invulsjabloon per blok.
- `assets/registratie-skeleton.json` — gestructureerd werkbestand met alle veldsleutels.
- `scripts/validate.py` — controleert een ingevuld JSON-bestand tegen de standaard.
