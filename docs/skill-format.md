# The SKILL.md format

A Skill is a directory containing a `SKILL.md` file with YAML frontmatter and Markdown body, optionally bundled with supporting files. Skills follow the **open Agent Skills standard** ([agentskills.io](https://agentskills.io/)), which is implemented by Claude Code, Cursor, Windsurf, OpenAI Codex, and 40+ other agentic coding tools.

This document describes the **portable subset** every team should target, plus the tool-specific extensions you may want to know about.

## Minimum portable structure

```
my-skill/
├── SKILL.md          # required
├── reference.md      # optional supporting docs
└── scripts/          # optional bundled scripts the agent can execute
    └── helper.py
```

`SKILL.md`:

```markdown
---
name: my-skill
description: What this Skill does and when an agent should use it. Put the key trigger phrase first.
---

# My Skill

## When to use this Skill
...

## What to do
1. ...
2. ...
```

## Required frontmatter fields

| Field         | Required        | Rules |
|---------------|-----------------|-------|
| `name`        | Recommended     | Lowercase letters, numbers, hyphens. Max 64 characters. No reserved words (`anthropic`, `claude`). Should match the directory name. If omitted, the agent uses the directory name. |
| `description` | **Required**    | Non-empty. Max 1024 characters. Must describe **both** what the Skill does **and** when it should be used. Put the trigger phrase first, descriptions are loaded into the agent's context at startup, and clarity here determines whether the agent picks the right Skill. |

Other frontmatter fields beyond these two are **tool-specific** and should be used sparingly (see below).

## Body conventions

- **Be concrete.** State what to do, not why or how the framework was designed.
- **Be concise.** Aim for under 5,000 tokens. Once a Skill is loaded, every token stays in context.
- **Reference supporting files** instead of inlining huge reference dumps. Link `reference.md`, example outputs, or large data files; the agent only loads them on demand.
- **Use standing instructions**, not one-time steps. The Skill content loads once and stays for the rest of the session.

A typical body has:

1. **When to use this Skill**, the trigger conditions.
2. **What to do**, numbered steps.
3. **Output format** (if applicable), exact shape the agent should produce.
4. **Conventions to follow**, naming, terminology, framework references.
5. **What to avoid**, anti-patterns, scope boundaries.
6. **Additional resources**, links to supporting files.

## Three levels of loading

The standard supports **progressive disclosure**:

| Level | Loaded                        | Typical size       | What it contains                                     |
|-------|-------------------------------|--------------------|------------------------------------------------------|
| 1     | Always (at startup)           | ~100 tokens / Skill | `name` and `description` from frontmatter            |
| 2     | When the Skill is triggered   | Under ~5k tokens   | The body of `SKILL.md`                               |
| 3     | As referenced                 | Effectively unlimited | Linked supporting files, scripts executed via shell |

Your `SKILL.md` is Level 2. Anything that doesn't have to be there every time the Skill fires belongs in Level 3 files.

## Tool-specific extensions

Several frontmatter fields are **Claude Code extensions** and not part of the portable standard:

`allowed-tools`, `disable-model-invocation`, `user-invocable`, `argument-hint`, `arguments`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`, `when_to_use`

You may use them, but the brief requires Skills to work in **at least two tools**. If you use a tool-specific field, add an explicit **"Tool-specific extensions"** section in the body that explains the fallback for tools that don't support it.

Example:

```markdown
## Tool-specific extensions

This Skill declares `allowed-tools: Bash(git *)` for Claude Code so git commands don't require per-use approval. In Cursor or Windsurf, the user must approve git tool use manually; the Skill still works.
```

## What works across tools

These features are part of the portable standard and work everywhere:

- Frontmatter `name` + `description`.
- Markdown body with sections.
- Relative links to bundled files (`reference.md`, `examples/foo.md`).
- Bundled scripts the agent can run via the host shell.

These features are **not** portable; use only with a fallback:

- Dynamic context injection (Claude Code's `` !`<command>` `` and `` ```! `` blocks).
- String substitution placeholders (`$ARGUMENTS`, `$0`, `${CLAUDE_SKILL_DIR}`).
- Tool-specific frontmatter (listed above).
- Pre-approval of tools.

## Naming and storage

Where the Skill lives depends on the tool, but for this hackathon all Skills live in the repo under:

```
skills/<your-skill-name>/SKILL.md
```

Most tools also support a per-user (`~/.claude/skills/`, `~/.cursor/skills/`, …) or per-project (`.claude/skills/`, `.cursor/skills/`, …) location. For grading and reproducibility we keep everything in `skills/` at the repo root.

## References

- [Open Agent Skills standard](https://agentskills.io/)
- [Anthropic, Skills in Claude Code](https://code.claude.com/docs/en/skills)
- [Anthropic, Agent Skills overview (Claude API + claude.ai)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Anthropic, Skills authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
