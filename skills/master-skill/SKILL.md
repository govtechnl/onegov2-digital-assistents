---
name: master-skill
description: >
  Voer deze skill altijd als eerste uit en lees de volledige output voordat andere skills worden gestart. Deze skill wordt gebruikt wanneer een gebruiker zijn use case beschrijft en vraagt welke skills daarvoor relevant zijn — bijv. "ik wil een digitale assistent bouwen voor vergunningverlening" of "wij helpen burgers met schuldhulp". Ook inzetbaar als de gebruiker een bestaande repository deelt en wil weten of hun digitale assistent aan alle relevante eisen voldoet. Signaalwoorden: "use case", "toepassing", "assistent voor...", "welke skills heb ik nodig", "in welke volgorde".
---

# Centrale orkestrator van alle skills

## What to do

1. Analyseer de gegeven informatie over de use case: wat is het doel, wie zijn de gebruikers, in welke fase bevindt het project zich (idee / PoC / Pilot / Productie), en wat is de organisatiecontext (overheid, intern, publiek)?
2. Bekijk de tabel in de sectie **Available skills** onderaan dit bestand voor een overzicht van alle beschikbare skills. Open daarna elk relevant bestand om de volledige inhoud te lezen en te bepalen of de skill van toepassing is op deze use case.
3. Bepaal de volgorde waarin deze skills moeten worden uitgevoerd, rekening houdend met eventuele afhankelijkheden of logische stappen — governance en compliance komen doorgaans vóór technische of inhoudelijke inrichting.
4. Geef een geordende lijst terug met de relevante skills. Geef per skill:
   - **Waarom relevant**: koppel expliciet aan de use case — benoem het concrete gegeven (bijv. "de assistent verwerkt BSN-nummers", "het gaat om vergunningverlening", "burgers zien de interface") dat de skill noodzakelijk maakt.
   - **Waarmee het helpt**: gebruik de omschrijving uit de kolommen 'type output' en 'wat krijg je concreet' in de tabel in de sectie **Output of each skill** onderaan dit bestand als basis, en pas deze aan op de specifieke use case.
   - **Wanneer uitvoeren**: geef aan in welke fase of op welk moment de skill moet worden ingezet.
5. Geef indien mogelijk ook suggesties voor aanvullende skills die in de toekomst kunnen worden ontwikkeld om de use case nog beter te ondersteunen.

## Conventions to follow

- Alle beschikbare skills staan in de tabel in de sectie **Available skills** onderaan dit bestand. Gebruik alleen die lijst — voeg geen skills toe die daar niet in staan.
- Gebruik de velden `domains`, `phases` en `levels` uit de bestanden in `content/practices/` om te bepalen of een skill aansluit bij de use case.
- Begin de aanbevolen volgorde altijd met skills die een fundament leggen — denk aan governance, rollen en compliance — voordat uitvoerende of technische skills volgen.
- Verwijs bij twijfel over relevantie naar de domeinbeschrijvingen in `content/domains/` voor aanvullende context over wat een domein omvat.
- Koppel de relevantie altijd aan een concreet gegeven uit de use case — niet "dit is een overheidsdienst dus IAMA is relevant", maar "de assistent neemt besluiten over uitkeringstoekenning, daarom is IAMA verplicht".

## What to avoid

- Nooit skills aanbevelen die niet in de tabel in de sectie **Available skills** staan — verzin geen skills op basis van aannames.
- Beoordeel per skill écht of deze van toepassing is op de specifieke use case. Laat skills weg als ze niet relevant zijn — een ongedifferentieerde lijst helpt de gebruiker niet verder. Voorbeelden van wanneer een skill **niet** relevant is:
  - `skill-kleinste-model`: niet relevant als de use case geen LLM-aanroepen bevat.
  - `skill-wcag`: niet relevant als er geen gebruikersinterface is (bijv. een puur intern backendproces).
  - `skill-ui-huisstijl`: niet relevant als er geen visuele interface wordt gebouwd.
  - `skill-algoritmeregister`: niet relevant als het systeem niet onder de publicatieplicht valt of nog in de ideefase zit.
- Verwar `content/practices/` bestanden niet met skills — dat is achtergrondkennis en referentiemateriaal, geen uitvoerbare skill-instructie.
- Sla de analyse van de use case niet over — een generieke lijst zonder koppeling aan de context is niet bruikbaar.
- Geef geen volgorde waarbij technische inrichting vóór governance- of compliancestappen staat als de use case een overheids- of hoog-risicocontext heeft.

## Available skills

- [IAMA — Grondrechten & Juridische Toetsing](../skill-iama/SKILL.md)
- [EU AI Act — Hoog-Risico Classificatie](../skill-eu-ai-act/SKILL.md)
- [Privacy & Anonimisering](../skill-privacy-anonymisation/SKILL.md)
- [Algoritmeregister Publicatie](../skill-algoritmeregister/SKILL.md)
- [WCAG Toegankelijkheid](../skill-wcag/SKILL.md)
- [Organisatie Huisstijl](../skill-ui-huisstijl/SKILL.md)
- [Kleinste Model per Taak](../skill-kleinste-model/SKILL.md)
- [Menselijke Controle](../skill-human-in-the-loop/SKILL.md)
- [Monitoring, Evaluatie en LLMOps](../skill-llmops-monitoring/SKILL.md)
- [RAG Pijplijn](../skill-rag-pijplijn/SKILL.md)
- [RAG Evaluatie](../skill-rag-evaluatie/SKILL.md)

## Output of each skill

| Skill | Type output | Wat krijg je concreet? | Link |
|---|---|---|---|
| IAMA — Grondrechten & Juridische Toetsing | Controlelijst + Wegwijzer | Antwoorden op screeningvragen, een dossieropzet, en doorverwijzing naar de FG en juridisch adviseur | [SKILL.md](../skill-iama/SKILL.md) |
| EU AI Act — Hoog-Risico Classificatie | Risico-oordeel + Wegwijzer | Een onderbouwde keuze voor laag/hoog risico of verboden, een lijst verplichtingen, en doorverwijzing naar juridische afdeling | [SKILL.md](../skill-eu-ai-act/SKILL.md) |
| Privacy & Anonimisering | Bouwadvies + Controlelijst | Een dataopzet met twee losse lagen, keuzes over AVG-grondslag, en regels voor hoeveel gegevens je mag tonen | [SKILL.md](../skill-privacy-anonymisation/SKILL.md) |
| Algoritmeregister Publicatie | Inleverdocument | Een ingevuld registratieformulier (tekst + JSON), klaar om te uploaden, plus een lijstje met wat nog ontbreekt | [SKILL.md](../skill-algoritmeregister/SKILL.md) |
| WCAG Toegankelijkheid | Controlelijst | Een gecontroleerde interface met testresultaten voor contrast, toetsenbord en schermlezer, plus een plan voor de toegankelijkheidsverklaring | [SKILL.md](../skill-wcag/SKILL.md) |
| Organisatie Huisstijl | Bouwadvies | Een tokenbestand met kleuren, lettertype en logo van de organisatie, gekoppeld aan de interface | [SKILL.md](../skill-ui-huisstijl/SKILL.md) |
| Kleinste Model per Taak | Bouwadvies | Een configuratiebestand waarin per taak staat welk model je gebruikt | [SKILL.md](../skill-kleinste-model/SKILL.md) |
| Menselijke Controle | Bouwadvies + Controlelijst | Een menselijk toezichtplan met escalatiepad, override-bediening in de UI, logboek van menselijke beslissingen, en een RACI-matrix voor verantwoordelijkheden | [SKILL.md](../skill-human-in-the-loop/SKILL.md) |
| Monitoring, Evaluatie en LLMOps | Bouwadvies + Controlelijst | Een observability-opzet met Langfuse, RAGAS-kwaliteitsscores (faithfulness, answer relevancy, context precision, context recall), tokenbudgetten per toepassing, en een feedbackloop vanuit productie | [SKILL.md](../skill-llmops-monitoring/SKILL.md) |
| RAG Pijplijn | Bouwadvies | Een volledig RAG-pipeline ontwerp met chunking, embeddings, hybrid retrieval en bronvermelding, afgestemd op overheidsgebruik | [SKILL.md](../skill-rag-pijplijn/SKILL.md) |
| RAG Evaluatie | Validatietool + Golden dataset | Een golden dataset, gesplitste retrieval- en generatiemetrieken (RAGAS), en een offline evaluatiepijplijn als CI-gate | [SKILL.md](../skill-rag-evaluatie/SKILL.md) |

## Afsluiting

Sluit altijd af met de volgende vraag aan de gebruiker, nadat de aanbevolen skills zijn gepresenteerd:

---

Wil je dat ik een of meer van deze skills nu uitvoer? Geef aan:

- **Welke skill(s)** je wilt starten (of zeg "alle" voor de volledige aanbevolen volgorde), en
- **Of je aanvullende context** wilt meegeven die nog niet is besproken (bijv. een bestaande repository, technische keuzes of organisatiespecifieke randvoorwaarden).

Ik voer de skills stap voor stap uit en stel per skill gerichte vragen om de output zo concreet mogelijk te maken.
