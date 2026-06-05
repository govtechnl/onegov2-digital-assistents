---
name: llmops-monitoring
description: >
  Gebruik deze skill wanneer een digitale assistent naar productie gaat of al in productie draait en je wilt weten of de kwaliteit, kosten en beschikbaarheid op orde zijn. LLMOps werkt wezenlijk anders dan traditioneel applicatiebeheer: naast latency en beschikbaarheid moeten ook antwoordkwaliteit, hallucinaties, tokengebruik en kosten worden bewaakt. Trigger bij: "monitoring", "observability", "LLMOps", "hallucinaties meten", "kwaliteit bewaken", "Langfuse", "RAGAS", "LLM-as-a-judge", "tokenkosten", "productie AI", "hoe weet ik of mijn assistent goed werkt", "logging en tracing", "evaluatie in productie", "MLflow", "DeepEval", "LangWatch".
---

# Monitoring, evaluatie en LLMOps

Een LLM-assistent die in productie draait zonder monitoring is een zwarte doos. Traditionele APM-tooling bewaakt latency en uptime — maar vertelt niets over of de antwoorden kloppen, of er gehallucineerd wordt, of de kosten ontsporen, of de kwaliteit na een promptwijziging is gedaald. LLMOps vult dit gat. Centrale stelling: **meten is weten, ook voor AI** — en meten begint vóór go-live, niet erna.

## Stap 1 — Zet een observability-hub op

Kies één centrale plek voor traces, logs en evaluatiescores. Koppel al je LLM-aanroepen hieraan vóór go-live.

- **Langfuse** is het aanbevolen startpunt: volledig self-hostable (AVG-vriendelijk), open-source, en integreert met alle grote frameworks (LangChain, LlamaIndex, OpenAI SDK, Anthropic SDK). Vergelijk met **LangWatch** als alternatief voor jouw organisatieprofiel.
- Leg per aanroep vast: prompt (versie), model, parameters (temperature, top_p), inputtokens, outputtokens, latency, en de uiteindelijke score.
- Gebruik **MLflow** als je naast tracing ook experiment-tracking en een modelregistry nodig hebt — met name bij fine-tuning of wanneer reproduceerbaarheid en auditability eisen zijn.
- Zorg dat de hub volledig losgekoppeld is van de productiedatabase met persoonsgegevens. Tracedata is zelf ook een gegevenstype — pas dataminimalisatie toe (zie ook `skill-privacy-anonymisation`).

## Stap 2 — Bewijk kwaliteit continu met RAGAS en LLM-as-a-judge

Antwoordkwaliteit degradeert stil: een promptwijziging, een modelupdate of een uitgebreide kennisbank kan de kwaliteit van honderd andere vragen raken zonder dat latency of uptime iets laat zien. Automatische evaluatie is de enige schaalbaarheidsoplossing.

**Vier kernmetrieken van RAGAS** (ook toepasbaar buiten RAG):

| Metriek | Wat het meet | Typische drempel |
|---|---|---|
| **Faithfulness** | Zijn alle claims in het antwoord aantoonbaar terug te vinden in de broncontext? | > 0,85 |
| **Answer relevancy** | Beantwoordt het antwoord daadwerkelijk de vraag? | > 0,80 |
| **Context precision** | Bevat de opgehaalde context relevante informatie (weinig ruis)? | > 0,75 |
| **Context recall** | Is alle benodigde informatie aanwezig in de opgehaalde context? | > 0,75 |

- Faithfulness is de directe maatstaf voor hallucinaties — een score onder 0,85 betekent dat antwoorden claims bevatten die niet door de bronnen worden gedekt.
- RAGAS integreert direct met Langfuse: scores worden automatisch als spans gelogd en zijn terug te vinden in de observability-hub.
- Vul RAGAS aan met een **LLM-as-a-judge** voor domein-specifieke oordelen (bijv. "Is dit antwoord juridisch verantwoord voor een gemeente?"). Kalibreer de judge op een sample van minimaal 100 cases tegen menselijk oordeel vóórdat je hem als gatekeeping inzet.
- Gebruik **DeepEval** voor het schrijven van LLM-unit-tests die draaien in CI/CD — vergelijkbaar met pytest, maar dan voor chatbotgedrag.

## Stap 3 — Monitor kosten actief

Tokenkosten zijn onzichtbaar totdat ze op de factuur staan. Implementeer proactief beheer:

- Stel **tokenbudgetten per team of toepassing** in — niet één globale limiet. Een chatbot voor burgers en een batchproces voor beleid verdienen aparte budgetten.
- Configureer alerts bij 70%, 90% en 100% van het maandbudget.
- Log inputtokens en outputtokens afzonderlijk per aanroep — outputtokens zijn doorgaans duurder en beter te optimaliseren (kortere systeemprompts, striktere max_tokens).
- Evalueer regelmatig of een kleinere of goedkopere modelvariant dezelfde kwaliteitsscores haalt (zie ook `skill-kleinste-model`).

## Stap 4 — Centraliseer logging en tracing

- Leg voor elke productieaanroep vast: welke promptversie actief was, welke modelparameters golden, welke context werd opgehaald (bij RAG), en wat de uitkomst was.
- Gebruik **promptversiebeheer**: een promptwijziging is een codewijziging — sla prompts op in Git, niet als vrije tekst in een database.
- Sluit aan op het domein **Beveiliging** van het raamwerk voor aanvullende eisen rondom logbescherming, toegangscontrole op tracedata en audittrails (verplicht bij hoog-risicogebruik onder de EU AI Act).
- Verwijder of maskeer persoonsgegevens uit traces vóór opslag — vrije tekst van gebruikersvragen bevat vrijwel altijd PII.

## Stap 5 — Sluit de feedbackloop vanuit productie

Offline evaluatie meet op bekende vragen; online monitoring vangt het onbekende:

- Verzamel negatieve gebruikerssignalen (duim omlaag, afgewezen antwoord, klacht via medewerker) en label ze.
- Voeg gelabelde mislukte cases toe aan de **golden dataset** van de RAG-evaluatieskill (`skill-rag-evaluatie`) — een evaluatieset die niet groeit met de werkelijkheid is binnen drie maanden verouderd.
- Plan een maandelijkse kwaliteitsreview: bekijk de laagst scorende traces, analyseer patronen, en vertaal bevindingen naar promptverbeteringen of kennisbankupdates.

## Wat te vermijden

- **Niet** alleen latency en uptime bewaken en dit "monitoring" noemen — dat zijn infrastructuurmetrieken, geen kwaliteitsmetrieken.
- **Niet** beginnen met bouwen van eigen evaluatieframeworks — RAGAS, DeepEval en Langfuse bestaan precies voor dit doel; begin daar.
- **Niet** een LLM-judge inzetten zonder kalibratie op menselijk oordeel — een ongekalibreerde judge is een willekeurige meter.
- **Niet** promptwijzigingen doorvoeren zonder eerst een baseline-evaluatie te draaien — je weet dan niet of de kwaliteit is gedaald.
- **Niet** één globaal kostenbudget instellen zonder opsplitsing per toepassing — kostenoverschrijdingen zijn dan niet terug te herleiden.
- **Niet** tracedata zonder dataminimalisatie opslaan als de gebruikersvragen persoonsgegevens kunnen bevatten.

## Raamwerk-bronnen

- [`content/practices/LLMOps-monitoring.md`](../../content/practices/LLMOps-monitoring.md) — Good practice LLMOps-monitoring uit het Raamwerk Digitale Assistenten (ring: Productie; niveaus: Developer/Engineer).
- [`content/domains/infrastructuur-data.md`](../../content/domains/infrastructuur-data.md) — Domein Infrastructuur & Data: observability, logging en kostenbeheersing.

## Relevante bronnen

- [Langfuse](https://langfuse.com) — Open-source LLM-observability platform, volledig self-hostable.
- [RAGAS](https://docs.ragas.io/) — Open-source evaluatieframework voor RAG-pijplijnen met faithfulness, answer relevancy, context precision en context recall.
- [DeepEval](https://deepeval.com/) — Framework voor unit-testen van chatbots: meet hoe relevant en feitelijk de antwoorden zijn.
- [LangWatch](https://langwatch.ai) — Alternatief observability-platform voor LLM-applicaties.
- [MLflow](https://mlflow.org) — Open-source modelregistry, experiment-tracking en tracing voor reproduceerbaarheid en auditability.
- [OWASP Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Referentielijst van de tien grootste security-risico's voor LLM-applicaties.
- [Overheidsbrede handreiking Generatieve AI (BZK)](https://www.rijksoverheid.nl/documenten/rapporten/2025/04/16/overheidsbrede-handreiking-generatieve-ai)

## Samenhang met andere skills

- **`skill-rag-evaluatie`** — deze skill richt zich op operationele monitoring in productie; skill-rag-evaluatie behandelt offline evaluatie en de opbouw van een golden dataset vóór go-live. Gebruik beide.
- **`skill-kleinste-model`** — kostenmonitoring (stap 3) levert de input om te beslissen of een kleiner model ingezet kan worden.
- **`skill-privacy-anonymisation`** — tracedata en logs mogen geen persoonsgegevens bevatten; de laagscheiding uit de privacy-skill geldt ook voor de observability-hub.
- **`skill-human-in-the-loop`** — LLM-judges markeren twijfelgevallen voor menselijke review; de escalatiestructuur uit de human-in-the-loop skill bepaalt wie die review doet.
