# skills/

Your team's Skills go here. One subdirectory per Skill.

## How to start

```powershell
Copy-Item -Recurse skills/_template skills/<your-skill-name>
```

Then edit `skills/<your-skill-name>/SKILL.md`.

## What lives here already

- **[_template/](_template/)**, minimal SKILL.md skeleton. Copy this.

Worked examples live in [docs/example-skills/](../docs/example-skills/) so judges grade your `skills/` against an empty starting line:

- [docs/example-skills/answer-quality-checks/](../docs/example-skills/answer-quality-checks/), Approach A reference Skill end-to-end.
- [docs/example-skills/framework-validator/](../docs/example-skills/framework-validator/), bonus validation Skill that bundles a script the agent can run.

## Naming rules

- Directory name: lowercase letters, numbers, hyphens; max 64 characters; no leading hyphen; no reserved words (`anthropic`, `claude`).
- The frontmatter `name` field should match the directory name.

## What a good Skill looks like

See [docs/skill-format.md](../docs/skill-format.md) for the spec and [docs/skill-checklist.md](../docs/skill-checklist.md) for the submission checklist.
