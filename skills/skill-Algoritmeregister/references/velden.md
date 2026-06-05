# Veldcatalogus — Algoritmeregister Publicatiestandaard v1.0.0

Bron: MinBZK Publicatiestandaard, consultatieversie 29-11-2024
(https://regels.overheid.nl/standaarden/algoritmeregister-publicatiestandaard).

Legenda "Altijd tonen":
- **Verplicht** = wordt niet gepubliceerd als het leeg is; altijd invullen.
- **Ja** = wordt altijd getoond; bij leeg toont de site "Veld niet ingevuld".
- **Nee** = alleen getoond als ingevuld.
- **Nooit tonen, wel verplicht** = niet zichtbaar op de site, maar moet wel aangeleverd worden.

## Inhoud
1. Algemene informatie (2.1.1 – 2.1.11)
2. Verantwoord gebruik (2.2.1 – 2.2.11)
3. Werking (2.3.1 – 2.3.6)
4. Metadata (2.4.1 – 2.4.4)

---

## 1. Algemene informatie

### Naam — JSON: `naam`
- Type: Tekst (<100 tekens). Altijd tonen: **Verplicht**.
- Een naam, bij voorkeur met een werkwoord, die aangeeft wat het algoritme doet. Begrijpelijk voor externen.
- Voorbeeld: *Automatische Verkeersregeling Ringweg*.

### Korte omschrijving — JSON: `korte_omschrijving`
- Type: Tekst (<350 tekens). Altijd tonen: **Verplicht**. **B1-taalniveau.**
- Korte, duidelijke beschrijving van het algoritme en het proces. Twee à drie zinnen. Verschijnt in het zoekoverzicht.
- Voorbeeld: *Dit algoritme zorgt met sensoren in het wegdek ervoor dat het verkeer zo makkelijk mogelijk doorstroomt.*

### Organisatie — JSON: `organisatie`
- Type: Tekst (<100 tekens). Altijd tonen: **Verplicht**.
- Volledige naam van de organisatie waar het algoritme wordt ingezet, gebaseerd op de TOOI-waardelijsten (https://standaarden.overheid.nl/tooi/waardelijsten/). Eén organisatie per registratie.
- Voorbeeld: *Gemeente Noorderhaaks*.

### Thema — JSON: `thema`
- Type: Lijst. Altijd tonen: **Ja**.
- Beleidsterrein(en) uit de Thema-indeling voor Officiële Publicaties (https://standaarden.overheid.nl/owms/4.0/doc/waardelijsten/thema-indeling-voor-officiele-publicaties).
- Voorbeeld: *Verkeer*.

### Status — JSON: `status`
- Type: Keuze. Altijd tonen: **Verplicht**.
- Exact één van: `In ontwikkeling`, `In gebruik`, `Buiten gebruik`. Bij zowel ontwikkeling als gebruik: kies `In gebruik`. Geen andere tekst in dit veld.
- Voorbeeld: *In gebruik*.

### Begindatum — JSON: `begindatum`
- Type: `yyyy-mm`. Altijd tonen: **Ja**.
- Maand en jaar van ingebruikname.
- Voorbeeld: *2023-01*.

### Einddatum — JSON: `einddatum`
- Type: `yyyy-mm`. Altijd tonen: **Ja**.
- Maand en jaar van buitengebruikstelling. Leeg laten als nog in gebruik.
- Voorbeeld: *2023-01*.

### Contactgegevens — JSON: `contactgegevens`
- Type: Geldige URL of e-mail. Altijd tonen: **Verplicht**.
- E-mailadres of website waar betrokkenen vragen kunnen stellen. URL begint met `https://`.
- Voorbeeld: *algoritmes@gemeentenoorderhaaks.nl*.

### Link naar publiekspagina — JSON: `link_publiekspagina`
- Type: Geldige URL. Altijd tonen: **Nee**.
- URL naar een eigen publiekspagina over het proces waarin het algoritme wordt ingezet (niet het decentrale register). Begint met `https://`.

### Publicatiecategorie — JSON: `publicatiecategorie`
- Type: Keuze. Altijd tonen: **Verplicht**.
- Exact één van: `Hoog-risico AI-systemen` (categorie A), `Impactvolle algoritmes` (categorie B), `Overige algoritmes` (categorie C).
- Voorbeeld: *Impactvolle algoritmes*.

### Link naar bronregistratie — JSON: `link_bronregistratie`
- Type: Geldige URL. Altijd tonen: **Nee**.
- Verwijzing naar het eigen (decentrale) register, machineleesbaar. Begint met `https://`.

---

## 2. Verantwoord gebruik

### Doel en impact — JSON: `doel_en_impact`
- Type: Tekst (<2500 tekens). Altijd tonen: **Ja**. **B1-taalniveau.**
- Het doel waarvoor het algoritme is ontwikkeld én hoe burgers/bedrijven ermee in aanraking komen wanneer het naar behoren werkt. Risico's komen in een apart veld.

### Afwegingen — JSON: `afwegingen`
- Type: Tekst (<2500 tekens). Altijd tonen: **Ja**. **B1-taalniveau.**
- Voor- en nadelen van de inzet en waarom die redelijk gerechtvaardigd is; benoem overwogen alternatieven en ethische afwegingen. Kan putten uit IAMA en DPIA.

### Menselijke tussenkomst — JSON: `menselijke_tussenkomst`
- Type: Tekst (<2500 tekens). Altijd tonen: **Ja**. **B1-taalniveau.**
- Hoe een mens de uitkomsten gebruikt, controleert en kan bijstellen. Geef ook aan als er géén menselijke tussenkomst is.

### Risicobeheer — JSON: `risicobeheer`
- Type: Tekst (<2500 tekens). Altijd tonen: **Ja**.
- Geïdentificeerde risico's (technisch, juridisch, financieel, ethisch — bijv. discriminatie, uitlegbaarheid) en hoe daarmee wordt omgegaan (bijv. periodieke monitoring).

### Wettelijke basis — JSON: `wettelijke_basis`
- Type: Tekst (<2500 tekens). Altijd tonen: **Nee**.
- Omschrijving van de wettelijke basis voor het proces; geef kort het doel van de wet aan, ook voor niet-juristen.

### Link naar wettelijke basis — JSON: `link_wettelijke_basis`
- Type: Geldige URL. Altijd tonen: **Ja**.
- Link naar de wettelijke grondslag (wet, verordening, formeel besluit). Bijv. wetten.overheid.nl-link.

### Titel van wettelijke basis — JSON: `titel_wettelijke_basis`
- Type: Tekst (<100 tekens). Altijd tonen: **Nee**.
- Titel van de gelinkte grondslag. Voorbeeld: *Wegenverkeerswet 1994*.

### Verwerkingsregister — JSON: `verwerkingsregister`
- Type: Geldige URL. Altijd tonen: **Nee**.
- Link naar het openbare deel van een verwerkingsregister dat betrekking heeft op dit algoritme.

### Impacttoets(en) — JSON: `impacttoetsen`
- Type: Tekst. Altijd tonen: **Ja**.
- Naam/namen van uitgevoerde impacttoetsen (bijv. DPIA, IAMA). Andere toetsen: noem de naam.

### Link naar impacttoets — JSON: `link_impacttoets`
- Type: Geldige URL. Altijd tonen: **Nee**.
- Link naar publiek beschikbare resultaten van een uitgevoerde impacttoets. Begint met `https://`.

### Toelichting op impacttoetsen — JSON: `toelichting_impacttoetsen`
- Type: Tekst (<2500 tekens). Altijd tonen: **Nee**.
- Toelichting waarom een bepaalde toets niet is gedaan (bijv. geen persoonsgegevens, dus geen DPIA).

---

## 3. Werking

### Gegevens — JSON: `gegevens`
- Type: Tekst (<2500 tekens). Altijd tonen: **Ja**.
- Overzicht van de gebruikte gegevens (en data gebruikt bij het bouwen). Wees specifiek bij persoonsgegevens (type, bijv. adres, leeftijd) en benoem de bron (BRP, BKR, eigen klantgegevens).

### Link naar gegevensbron — JSON: `link_gegevensbron`
- Type: Geldige URL. Altijd tonen: **Nee**.
- Link naar beschrijving van de gebruikte gegevensbron (bijv. datacatalogus).

### Titel van gegevensbron — JSON: `titel_gegevensbron`
- Type: Tekst (<500 tekens). Altijd tonen: **Nee**.
- Titel van de gelinkte gegevensbron.

### Technische werking — JSON: `technische_werking`
- Type: Tekst (<5000 tekens). Altijd tonen: **Ja**.
- Uitleg van input → werking → output. Minimaal aangeven of het zelflerend is. Links naar stroomdiagram of wetenschappelijke documentatie zijn welkom. Mag technischer/specialistischer taalgebruik bevatten.

### Leverancier — JSON: `leverancier`
- Type: Tekst (<200 tekens). Altijd tonen: **Ja**.
- Naam van de externe leverancier, of `Intern ontwikkeld`. Open-source packages binnen een groter algoritme tellen hier niet als leverancier.

### Link naar broncode — JSON: `link_broncode`
- Type: Geldige URL. Altijd tonen: **Nee**.
- URL naar de codepagina. Leeg laten als er geen publieke codebase is. Begint met `https://`.

---

## 4. Metadata

### Taal — JSON: `taal`
- Type: ISO 639-3 code. Altijd tonen: **Nooit tonen, wel verplicht**.
- Op dit moment alleen `nld`.

### Schema — JSON: `schema`
- Type: Keuze. Altijd tonen: **Nooit tonen, wel verplicht**.
- De versie van de publicatiestandaard. Op dit moment `1.0.0`. Geen andere tekst.

### Bron-ID — JSON: `bron_id`
- Type: Tekst (<100 tekens). Altijd tonen: **Nooit tonen**.
- Unieke identificatie zoals gebruikt in het interne register/database van de organisatie.

### Zoektermen — JSON: `zoektermen`
- Type: Tekst (<2500 tekens), komma-gescheiden. Altijd tonen: **Nooit tonen**.
- Trefwoorden om de vindbaarheid te vergroten (bijv. relevante organisatie, domein).
- Voorbeeld: *Verkeer, Mobiliteit, VRI, Infrastructuur*.

---

## Velden waar B1-taalniveau verplicht is
Korte omschrijving, Doel en impact, Afwegingen, Menselijke tussenkomst.

## Verplichte velden (publicatie geweigerd indien leeg)
Naam, Korte omschrijving, Organisatie, Status, Contactgegevens, Publicatiecategorie, Taal, Schema.

## Opmaakregel
Geen regeleinden (enters) en geen opsommingen/bullets binnen veldwaarden — alleen doorlopende platte tekst.
