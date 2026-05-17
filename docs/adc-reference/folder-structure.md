# Mapstructuur - raamwerk-digitale-assistent

```
raamwerk-digitale-assistent/
├── README.md
├── index.html
├── logo.png
├── .gitignore
├── css/
│   └── style.css
├── js/
│   ├── app.jsx
│   ├── bronnen.jsx
│   ├── chrome.jsx
│   ├── diagram.jsx
│   ├── glossary.jsx
│   ├── pages.jsx
│   └── tweaks-panel.jsx
├── scripts/
│   ├── build.py
│   └── watch.py
└── content/
    ├── bronnen.yaml
    ├── context_raamwerk.yaml
    ├── filters.yaml
    ├── glossery.yaml
    ├── home.yaml
    ├── domains/
    │   ├── antwoordkwaliteit.md
    │   ├── beveiliging.md
    │   ├── compliance.md
    │   ├── cultuur-adoptie.md
    │   ├── digitale-soevereiniteit.md
    │   ├── duurzaamheid.md
    │   ├── ethiek-mensenrechten.md
    │   ├── functionaliteit.md
    │   ├── gebruikerservaring.md
    │   ├── governance.md
    │   ├── infrastructuur-data.md
    │   ├── kennis-capaciteit.md
    │   └── technische-prestaties.md
    └── practices/
        ├── datakwaliteit-governance.md
        ├── infrastructuur-keuze.md
        ├── llmops-monitoring.md
        ├── model-deployment.md
        ├── rag-pijplijn.md
        └── schaalbaarheid-productie.md
```

## Korte uitleg per map

- **`css/`** - stylesheets voor de site.
- **`js/`** - React/JSX bronbestanden die de UI opbouwen (chrome, pagina's, diagram, glossarium, etc.).
- **`scripts/`** - Python build- en watch-scripts die de content omzetten naar `js/data.js`.
- **`content/`** - alle redactionele inhoud:
  - YAML-bestanden voor structuur (home, filters, bronnen, glossarium, context).
  - **`domains/`** - één markdown-bestand per domein (ring) van het raamwerk.
  - **`practices/`** - één markdown-bestand per praktijk/aanbeveling.
- **`local_output/`** - lokale, niet-gecommitte werkmap (in `.gitignore`).
