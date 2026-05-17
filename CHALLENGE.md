# Challenge Brief | Digital Assistants for Government

> **OneGov #2** · ICTU · 4–5 June 2026 · The Hague Tech
>
> *From framework to reusable skills: a shared library every government assistant can build on.*
>
> **Challenge owners:** Monique Neijman (ICTU), Laurent Smeets & Jochem Huijps (ADC Consulting)
> **Contact:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)

This is an English working translation of the original Dutch challenge brief.
The authoritative source is [Challenge_Brief_Digitale_Assistenten.pdf](Challenge_Brief_Digitale_Assistenten.pdf)
and the version on Junction.

---

## Background

Government organisations that want to build or further develop a digital
assistant start over every single time. There is no shortage of good
practices: the *Raamwerk van de Digitale Assistent* (Digital Assistant
framework) bundles concrete guidelines, architectural principles, and
implementation patterns for the responsible use of AI in public services.
But that knowledge has not yet been translated into reusable, ready-to-use
instructions for the **agentic coding tools** developers work with every day.

The consequence: every organisation starts at zero, makes its own choices,
and arrives at inconsistent implementations. Knowledge built up inside one
*uitvoeringsorganisatie* does not spread. Teams that want to build an
assistant tomorrow figure out themselves what other teams already worked out
three months ago. This is the space ICTU, ADC Consulting, and DigiCampus
offer your team during OneGov #2: **build the infrastructure that breaks
this cycle.**

## Problem statement

Government organisations that want to build a digital assistant run into the
same walls:

- There is **no shared standard** for how to set up an assistant in line with
  the framework. Every organisation reinvents the wheel.
- Good practices exist, but are **not translated into the format that
  agentic coding tools understand**: concrete, structured instruction files.
- Implementations are **tool-specific** and therefore not transferable. What
  works at Logius does not help DUO move forward.
- There is **no shared repository** that government organisations can learn
  from, build on, and contribute to.
- The *Raamwerk van de Digitale Assistent* exists. The translation into
  working, reusable code instructions is still missing.

## The challenge

> *How do we build a shared, open library of **tool-independent Skills** on
> top of the Digital Assistant framework, so that every government
> organisation can build a responsible digital assistant faster and more
> consistently, and so that knowledge built up in one organisation
> spreads instead of getting lost?*

## What Skills are, and why this format

A **Skill** is a folder with a `SKILL.md` file plus optional scripts and
references. The `SKILL.md` file contains a name, a description, and concrete
instructions that tell an agentic coding tool exactly *how* to implement a
particular domain or pattern.

The format was originally developed by Anthropic and is now an **open
standard**, supported by **40+ AI tools** including Claude Code, OpenAI
Codex, Cursor, and Windsurf. A Skill you build therefore works across all
these environments.

See [docs/skill-format.md](docs/skill-format.md) for the full spec and the
portable subset.

## Two design approaches

Teams pick **A**, **B**, combine both, or design their own structure.

### Approach A, One Skill per domain

Build a separate, narrowly-scoped Skill for each domain or good practice
from the framework. Each Skill represents one responsibility.

Examples:

- Authentication & identity verification
- Accessibility (WCAG) for answers
- Memory architecture & session management
- Logging & audit trail

See [docs/example-skills/answer-quality-checks/](docs/example-skills/answer-quality-checks/)
for a fully worked Approach A Skill.

### Approach B, Layered composition

Build Skills that build on each other: a base Skill for response format, a
domain layer for specific rules, and a composition Skill that ties them
together.

Examples:

- **Base Skill:** tone and style guide for government communication.
- **Domain Skill:** legal restraint on sensitive questions.
- **Composition Skill:** complete assistant for a single organisation.

## Guiding research questions

The challenge owners formulated four questions teams can use as a compass:

1. Which **domains or good practices** from the framework lend themselves
   best to translation into a Skill, and why?
2. How do you write a Skill so that it is **tool-independent** and remains
   usable as the framework evolves?
3. How do you ensure **consistency between Skills** so that an assistant
   combining several Skills does not receive conflicting instructions?
4. How do you make Skills **usable for organisations that do not (yet)
   know** the framework?

**Optional extension:** design a **validation Skill** that judges whether
other Skills are built correctly according to the framework's structural
conventions. See [docs/example-skills/framework-validator/](docs/example-skills/framework-validator/)
for a starter.

## Starting point: the Git repository

Every team starts from the same open Git repository:
[github.com/govtechnl/onegov2-digital-assistents](https://github.com/govtechnl/onegov2-digital-assistents).
It contains all the building blocks you need to get going immediately.
**Fork the repo, build your Skills, open a Pull Request.**

### 01 · The framework as `.md` files, the raw material

The framework consists of **13 domains** and **6 practices**, each as a
separate `.md` file under [content/](content/).

- **Domains:** answer quality, security, compliance, culture & adoption,
  digital sovereignty, sustainability, ethics & human rights,
  functionality, user experience, governance, infrastructure & data,
  knowledge & capacity, technical performance.
- **Practices:** data quality governance, infrastructure choice,
  LLMOps monitoring, model deployment, RAG pipeline, scalability &
  production.

Each file follows the same structure: `id`, `ring`, `title`, `short`, and a
descriptive body. Practices also carry domain tags, **phases** (PoC / Pilot
/ Production) and **levels** (Operational / Tactical / Strategic).

> *"The .md files are your starting point. Every best practice is already
> structured and available."*

### 02 · Skill structure template, the format

The repository follows the standard folder layout: [content/domains/](content/domains/)
for the 13 domain files, [content/practices/](content/practices/) for the 6
practices, and a separate [skills/](skills/) folder for the Skills teams add
during the hackathon.

Minimum requirements: a `SKILL.md` with `name`, `description`, and concrete
instructions. Optional: scripts, reference files, tests. Keep the structure
simple and lightweight. Copy [skills/_template/](skills/_template/) to start.

> *"Small format, big impact: a good Skill fits in a single file."*

### 03 · Context and background documentation, the framing

The repo also contains the challenge brief, a README explaining the
framework, and links to additional sources. So you understand *why* certain
choices were made.

Includes: challenge brief, architectural overview of the framework, links to
the Digital Assistant documentation and relevant government standards
([NL API Strategie](docs/integrations/nl-api-strategie.md),
[Common Ground](docs/integrations/common-ground.md)).

> *"The context is already in there: you don't need to look up the framework
> yourself."*

### 04 · Contributing via Pull Request, the workflow

Fork the repo, build your Skills on your own branch, open a Pull Request at
the end of the hackathon. After the hackathon, high-quality contributions
are merged into the central library.

**Ground rules:** **one PR per team.** Skills must follow the `SKILL.md`
structure and be demonstrably based on a good practice from the framework.
The repo stays publicly available after the hackathon.

> *"Your hackathon PR could become the standard the next government
> assistant uses."*

## Resources available in the repository

Repository contents (available via GitHub & Junction):

1. **Framework as `.md` files**, every good practice from the framework as
   a separate, editable `.md` file. This is your primary raw material.
2. **Example Skills**, fully worked reference Skills demonstrating the
   `SKILL.md` structure. Use these as a template for your own Skills. See
   [docs/example-skills/](docs/example-skills/).
3. **README and challenge brief**, explanation of the repository's purpose,
   the structural conventions for Skills, and links to the full framework.
4. **Folder structure for teams**, a proposed folder layout for your
   submission so all PRs are consistent and easy to review. See
   [folder-structure.md](folder-structure.md).
5. **Validation checklist (optional)**, a list of quality criteria a Skill
   must meet. Use this for self-evaluation before the pitch. See
   [docs/skill-checklist.md](docs/skill-checklist.md).
6. **Additional sources**, links to the full framework documentation,
   relevant government standards (NL API Strategie, Common Ground), and
   reference implementations of digital assistants.

> ℹ️ The repository is available at
> [github.com/govtechnl/onegov2-digital-assistents](https://github.com/govtechnl/onegov2-digital-assistents)
> and is also surfaced through the Junction platform. **Monique Neijman
> (ICTU)** and the technical partners from **ADC Consulting** are available
> on the day itself for questions about the framework, the repository, and
> Skill structure.

## Judging criteria

Teams are judged by an expert jury with expertise in digital government
services, AI, and open-source development. Four levels:

### ✅ Must: minimum requirements for a valid submission

- The submission contains **at least two** worked Skills, each based on a
  demonstrable good practice from the framework.
- Each Skill follows the `SKILL.md` structure: `name`, `description`, and
  concrete instructions.
- Skills are demonstrably **tool-independent**: they work in at least two
  agentic coding tools (e.g. Claude Code and Cursor).

### ⭐ Should: distinguishing qualities

- Skills are written so that a developer **without prior framework
  knowledge** can pick them up and start working immediately.
- Attention to **consistency**: Skills used together do not contradict each
  other.
- Skills are **modular**: they can be deployed in isolation or combined into
  a full assistant.

### ⚠️ Should not: pitfalls to avoid

- Building Skills so specific to one organisation that they are not
  reusable by others.
- Skills that depend on tool-specific syntax instead of generic
  instructions.

### ✨ Could: bonus for outstanding submissions

- Skills that build on or reference existing government standards
  ([NL API Strategie](docs/integrations/nl-api-strategie.md),
  [Common Ground](docs/integrations/common-ground.md)).
- A **composition Skill** showing how multiple library Skills come together
  in one working assistant.
- A **validation Skill** that automatically judges whether other Skills are
  built correctly.

## Deliverables

At the end of the hackathon, every team delivers via a Pull Request on the
central repository and presents:

- **At least two worked Skills** in the correct folder structure, submitted
  as a Pull Request.
- A short **demo (max. 3 minutes)** showing how a Skill works in an agentic
  coding tool of your choice.
- A **pitch deck (max. 10 slides)**: which domains did you choose, why, and
  what makes your Skills reusable?
- A **PR link** to `github.com/govtechnl/onegov2-digital-assistents` with
  your Skill submission.
- A short PR description: which good practices were translated, and which
  choices were made when writing the instructions.
- Submit the PR link, the demo (recording or live-demo slot), and the deck
  through the **Junction submission form** for this challenge.

See [.github/pull_request_template.md](.github/pull_request_template.md) and
[docs/skill-checklist.md](docs/skill-checklist.md).

## Technical framework: what you need to know

When building Skills you'll encounter a number of technical and substantive
choices. The most important ones:

- **The Skill format.** A Skill is a folder with a `SKILL.md` file. That
  file contains at least a `name` and `description` field, then the
  instruction text. Optional: scripts, reference files, test cases. Keep it
  as light and specific as possible. See [docs/skill-format.md](docs/skill-format.md).
- **Tool independence.** Write instructions in plain language, not in the
  syntax of a specific tool. A Skill you write for Claude Code must also
  work in Cursor, Windsurf, or OpenAI Codex. **Test this during the
  hackathon.**
- **Alignment with the framework.** Every Skill must be demonstrably based
  on a good practice from the *Raamwerk van de Digitale Assistent*. Link
  from your `SKILL.md` to the relevant `.md` source in the repository.
- **Licence.** The repository and all contributions are under an open
  licence (**EUPL-1.2** or **CC-BY 4.0**). Your Skill becomes publicly
  available after the hackathon as part of the library.

## Resources and inspiration

The following material is available as a starting point:

- **Raamwerk Digitale Assistent** (website, forthcoming): all good practices
  per domain, structured.
- **GitHub repository** with `.md` files, example Skills, and folder
  structure: [github.com/govtechnl/onegov2-digital-assistents](https://github.com/govtechnl/onegov2-digital-assistents).
- **`SKILL.md` specification and background:** [agentskills.io](https://agentskills.io/),
  [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills),
  [cursor.sh](https://cursor.sh), [windsurf.com](https://windsurf.com).
- **NL API Strategie and Common Ground architecture principles:**
  [developer.overheid.nl](https://developer.overheid.nl) ·
  [commonground.nl](https://commonground.nl).
- **GreenPT API documentation** for teams integrating LLM calls into Skills:
  [greenpt.nl](https://greenpt.nl).
- **Overview of supported agentic coding tools:**
  [claude.ai/code](https://claude.ai/code) ·
  [cursor.sh](https://cursor.sh) ·
  [windsurf.com](https://windsurf.com) ·
  [openai.com/codex](https://openai.com/codex).
- **Challenge brief and context:** available as an attachment on Junction.
- **Framework background documentation:** made available via Junction at
  the latest **two weeks before the hackathon**.

**Monique Neijman (ICTU)** and the technical partners from **ADC
Consulting (Laurent Smeets and Jochem Huijps)** are present all day as
challenge owners. They bring deep knowledge of the framework and can guide
your team on substantive and technical questions. Alongside them, a wider
group of domain experts is available as mentors.

## Out of scope

- Building or hosting an assistant model.
- Building the public framework website (ADC owns that; see
  [docs/adc-reference/](docs/adc-reference/)).
- Processing real personal data of any kind.

## Disclaimer

The Skills and contributions that emerge from this hackathon are published
as open source under **EUPL-1.2** or **CC-BY 4.0**. Contributions to the
repository are reviewed by the challenge owners after the hackathon.
Inclusion in the definitive library depends on quality assessment. The
challenge is intended as an innovation exercise; Skills require further
review before use in production environments.

---

**Challenge owners:**
Monique Neijman · `Monique.Neijman@ictu.nl`
Laurent Smeets · `laurent.s@adc-consulting.com`
Jochem Huijps · `jochem.h@adc-consulting.com`

**Hackathon questions:** [hack@govtechnl.nl](mailto:hack@govtechnl.nl)
