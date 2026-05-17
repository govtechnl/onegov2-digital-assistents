# Contributing

Thank you for contributing to the OneGov #2 Digital Assistants Skills challenge. This document explains how to add a Skill, how to open a pull request, and the ground rules that keep the library trustworthy.

## Ground rules

- **No real personal data.** Use synthetic examples only.
- **Tool independence is non-negotiable.** Every Skill must work in at least two agentic coding tools. Test before you submit.
- **The `SKILL.md` format is the open standard.** Stick to the portable subset (`name`, `description`, body). Tool-specific features (e.g. `allowed-tools`, `disable-model-invocation`) live in a clearly labelled optional section or in a separate tool-specific overlay.
- **Plain language.** English is the primary language. Dutch domain terms are allowed when translation loses meaning; add them to [docs/glossary.md](docs/glossary.md).
- **One team, one PR, from a fork.** Fork the repo, work on a branch in your fork, open the PR back into this repo's `main`.

## How to add a Skill

1. Fork this repository under your team's account and clone the fork.
2. Copy `skills/_template/` to `skills/<your-skill-name>/`.
   - Directory name must be lowercase letters, numbers, and hyphens only (max 64 chars).
3. Fill in `SKILL.md`:
   - `name` (lowercase + hyphens, ≤64 chars), usually matches the directory name.
   - `description` (≤1024 chars), both *what the Skill does* and *when to use it*. Put the key trigger phrase first.
   - The body: clear, concrete instructions. Aim for under 5,000 tokens. Reference supporting files instead of inlining huge reference dumps.
3. Add supporting files as needed (`reference.md`, `examples/`, `scripts/`). Reference them from `SKILL.md` so the agent knows when to load them.
4. Run validation:

   ```powershell
   python scripts/validate.py
   ```

5. **Test in at least two tools.** Document which tools and what you tried in the PR description.
6. Walk through [docs/skill-checklist.md](docs/skill-checklist.md) and confirm each item.
7. See [docs/example-skills/](docs/example-skills/) for two fully-worked Skills you can imitate.

## Pull request expectations

A reviewable pull request:

- Comes from a team fork into this repo's `main`.
- Lands at least **two Skills** (the challenge minimum).
- Touches `skills/` primarily. Changes to `content/`, `scripts/`, or `docs/` are welcome but should be in the same PR with clear rationale.
- Has a PR description that covers: approach (A / B / hybrid), what each Skill does, which tools you tested, and a link to your demo and deck.
- Passes CI (`python scripts/validate.py`).
- Is also submitted through the Junction submission form for this challenge.

## Changing shared conventions

If you need to change the `SKILL.md` validation rules, the framework schema, or repo-wide conventions, raise an issue first. Hackathon teams should not block on this.

## Code of conduct

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md). Be kind, be specific, assume good intent.

## Maintainers

The repository is maintained by the OneGov #2 challenge owners and ADC Consulting.
