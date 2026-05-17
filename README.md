# OneGov #2 | Digital Assistants Skills

Starter repository for the OneGov #2 hackathon challenge **"Digital Assistants for Government"** (4–5 June 2026, The Hague Tech).

The challenge: build a **library of Agent Skills**, `SKILL.md` files following the [open Agent Skills standard](https://agentskills.io/), that turn the ICTU/ADC *Raamwerk Digitale Assistenten* into concrete, tool-independent instructions any agentic coding assistant (Claude Code, Cursor, Windsurf, OpenAI Codex, …) can apply when helping a government team build, evaluate, or operate a digital assistant.

> The full brief is in [Challenge_Brief_Digitale_Assistenten.pdf](Challenge_Brief_Digitale_Assistenten.pdf). Read it first, it overrides anything in this repo.

New teams can begin with [START_HERE.md](START_HERE.md).

## What is a Skill?

A Skill is a directory containing a `SKILL.md` file with YAML frontmatter (`name`, `description`) and Markdown instructions, plus optional supporting files (reference docs, scripts, examples).

```
my-skill/
├── SKILL.md          # required: name + description + instructions
├── reference.md      # optional: deeper reference loaded on demand
└── scripts/
    └── helper.py     # optional: deterministic helpers the agent can run
```

When a developer asks their coding agent a relevant question, the agent loads the matching `SKILL.md` and follows its instructions. The same file works across Claude Code, Cursor, Windsurf, OpenAI Codex, and any other tool that implements the standard.

See [docs/skill-format.md](docs/skill-format.md) for the full format reference.

## What this repo gives you

- **[content/](content/)**, the *Raamwerk Digitale Assistenten* as Markdown + YAML: 13 domains, 6 practices, glossary, sources. This is the **raw material** your skills wrap around.
- **[skills/](skills/)**, where teams put their Skills.
  - [skills/_template/](skills/_template/), copy this to start a new skill.
- **[docs/example-skills/](docs/example-skills/)**, two fully-worked example Skills (Approach A + a bonus validation Skill) you can study without them being part of your `skills/` deliverable.
- **[docs/skill-format.md](docs/skill-format.md)**, the SKILL.md format, what's portable across tools, what's tool-specific.
- **[docs/skill-checklist.md](docs/skill-checklist.md)**, the quality checklist your Skill must pass before submission.
- **[scripts/validate.py](scripts/validate.py)**, lints every `SKILL.md` in `skills/` and every file in `content/`.
- **[docs/integrations/](docs/integrations/)**, relevant standards: [NL API Strategie](docs/integrations/nl-api-strategie.md), [Common Ground](docs/integrations/common-ground.md).

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Lint all skills and framework content
python scripts/validate.py
```

To author a Skill:

1. **Fork this repo** under your team's account and clone the fork.
2. Copy `skills/_template/` to `skills/<your-skill-name>/`.
3. Fill in the frontmatter (`name`, `description`) and instructions.
4. Run `python scripts/validate.py`.
5. Test it in **at least two agentic coding tools** (e.g. Claude Code + Cursor), Skills must be tool-independent.
6. Open one pull request per team from your fork into this repo's `main`. See [CHALLENGE.md](CHALLENGE.md) for full deliverables.

## Approach: A, B, or hybrid

The brief offers two design approaches; pick one (or mix):

- **Approach A, One Skill per framework topic.** A skill per domain or practice (e.g. `answer-quality-checks`, `rag-pipeline`, `security-baseline`). Best for narrow, focused expertise.
- **Approach B, Layered Skills.** A `base` Skill with shared conventions, `domain` Skills that extend it, and a `composition` Skill that ties them together. Best when the agent needs to reason across topics.

See [CHALLENGE.md](CHALLENGE.md) for examples of each.

## Repository layout

See [folder-structure.md](folder-structure.md).

## Partners on the day

- **ICTU**, Monique Neijman, framework owner.
- **ADC Consulting**, technical support for the framework, repo, and Skill structure.

ADC also runs the public *Raamwerk Digitale Assistenten* site; their content templates are in [docs/adc-reference/](docs/adc-reference/) for reference.

## License

- Code: Apache License 2.0, see [LICENSE](LICENSE).
- Content under `content/`, `skills/`, and `docs/`: CC BY 4.0 unless stated otherwise.
