---
name: framework-validator
description: Validate that one or more Skills in this repository follow the open Agent Skills standard and the OneGov #2 conventions. Use when the user asks to lint, validate, or check Skills before submission, or when adding a new Skill to skills/.
---

# Framework Validator

A meta-Skill: it validates other Skills against the open Agent Skills standard and the OneGov #2 submission conventions.

## When to use this Skill

Trigger this Skill when:

- The user asks "is my Skill ready?", "lint this Skill", "validate skills/", or similar.
- A new Skill directory was just added under `skills/` and the user wants a pre-submission check.
- CI fails on `python scripts/validate.py` and the user wants to understand why.

## What to do

1. **Determine the scope.** If the user names a specific Skill, validate just that one. Otherwise validate every directory under `skills/` (except `_template`).
2. **Run the bundled linter** for fast, deterministic checks:

   ```bash
   python scripts/lint_skill.py skills/
   ```

3. **Walk through [docs/skill-checklist.md](../../skill-checklist.md)** for each Skill. The linter catches mechanical issues; the checklist covers judgement calls (tool independence, clarity, modularity).
4. **Report findings** grouped per Skill:

   ```
   ### skills/<skill-name>/

   Linter: pass | fail (N issues)
   - <issue 1>
   - <issue 2>

   Checklist:
   - [x] Frontmatter has required fields
   - [ ] Tested in at least 2 tools  ← document which tools in the PR description
   - ...

   Verdict: ready | needs-fix
   ```

5. **End with a one-paragraph summary** of repo-wide issues (naming inconsistencies, duplicated descriptions, missing tool-independence evidence).

## Conventions to enforce

- Directory name matches frontmatter `name`.
- `name` is lowercase letters/numbers/hyphens, ≤64 chars, no reserved words (`anthropic`, `claude`).
- `description` is present, non-empty, ≤1024 chars, and answers both "what" and "when".
- Body has at least one section with concrete instructions (not just a heading).
- Supporting files referenced in the body actually exist.
- No tool-specific frontmatter (`allowed-tools`, `disable-model-invocation`, `user-invocable`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`, `argument-hint`, `arguments`) appears without an explicit "Tool-specific extensions" section explaining the fallback for tools that don't support it.

## What to avoid

- Do not rewrite Skills automatically. Report findings and let the author choose the fix.
- Do not flag the `_template/` directory, it is intentionally a skeleton.

## Additional resources

- [scripts/lint_skill.py](../../../scripts/lint_skill.py), the linter this Skill runs.
- [docs/skill-format.md](../../skill-format.md), the spec.
- [docs/skill-checklist.md](../../skill-checklist.md), the human checklist.
- [scripts/validate.py](../../../scripts/validate.py), the repo-wide validator (CI also runs this).
