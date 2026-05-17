# Repository layout

```
onegov2-digital-assistents/
├── Challenge_Brief_Digitale_Assistenten.pdf  # the official brief, leading
├── README.md
├── CHALLENGE.md                              # brief summary + design approaches
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── requirements.txt
├── folder-structure.md                       # this file
│
├── skills/                                   # ← teams add their Skills here
│   ├── README.md
│   └── _template/                            # copy this to start a new skill
│       └── SKILL.md
│
├── content/                                  # the Raamwerk as raw material
│   ├── context.yaml
│   ├── filters.yaml                          # phases + levels vocabulary
│   ├── glossary.yaml
│   ├── home.yaml
│   ├── sources.yaml                          # canonical source registry
│   ├── domains/                              # 13 domain markdown files
│   │   ├── answer-quality.md
│   │   ├── compliance.md
│   │   ├── culture-adoption.md
│   │   ├── digital-sovereignty.md
│   │   ├── ethics-human-rights.md
│   │   ├── functionality.md
│   │   ├── governance.md
│   │   ├── infrastructure-data.md
│   │   ├── knowledge-capacity.md
│   │   ├── security.md
│   │   ├── sustainability.md
│   │   ├── technical-performance.md
│   │   └── user-experience.md
│   └── practices/                            # 6 practice markdown files
│       ├── data-quality-governance.md
│       ├── infrastructure-choice.md
│       ├── llmops-monitoring.md
│       ├── model-deployment.md
│       ├── production-scalability.md
│       └── rag-pipeline.md
│
├── scripts/
│   ├── validate.py                            # lints content/ and skills/
│   └── lint_skill.py                          # invoked by validate.py; can be run standalone
│
├── docs/
│   ├── skill-format.md                        # the SKILL.md spec, portable subset
│   ├── skill-checklist.md                     # quality checklist for your Skill
│   ├── glossary.md
│   ├── personas.md
│   ├── scenarios.md
│   ├── example-skills/                        # worked examples; not part of your deliverable
│   │   ├── answer-quality-checks/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   └── framework-validator/
│   │       └── SKILL.md
│   ├── integrations/
│   │   ├── nl-api-strategie.md
│   │   └── common-ground.md
│   └── adc-reference/                         # ADC's own templates, for reference
│       ├── folder-structure.md                # ADC's site repo structure
│       ├── domains.md                         # ADC's domain template
│       └── practice.md                        # ADC's practice template
│
└── .github/
    ├── pull_request_template.md
    ├── ISSUE_TEMPLATE/
    └── workflows/
        └── validate.yml
```

## What is where

- **`skills/`**, the deliverable. Your team's Skills live here.
- **`content/`**, the *Raamwerk Digitale Assistenten* in Markdown + YAML. Treat it as raw material: read it, link to it from your Skills, but you do not have to edit it (and most teams shouldn't).
- **`scripts/validate.py`**, the linter. Runs on every PR via [.github/workflows/validate.yml](.github/workflows/validate.yml).
- **`docs/`**, supporting docs: the SKILL.md spec, the submission checklist, two worked example Skills in `docs/example-skills/`, integrations, and ADC's reference templates.
- **`docs/example-skills/`**, fully-worked Skills you can study without them being part of your own `skills/` deliverable.
- **`docs/adc-reference/`**, ADC sent these as reference for how *their* site repo organises content. You do **not** need to replicate this structure; it is here so teams know what the framework's downstream consumer expects.
