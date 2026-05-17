# Skill submission checklist

Walk through this list for **every Skill** in your PR before submitting. The first section is mechanical (also enforced by `scripts/validate.py`); the second is judgement.

## Mechanical (enforced by CI)

- [ ] Skill lives in `skills/<skill-name>/SKILL.md`.
- [ ] Directory name is lowercase letters, numbers, hyphens; max 64 chars; no reserved words (`anthropic`, `claude`).
- [ ] YAML frontmatter is valid and between `---` markers at the top of the file.
- [ ] Frontmatter `name` matches the directory name.
- [ ] Frontmatter `description` is present, non-empty, ≤1024 chars, and answers **both** "what does it do" and "when should the agent use it".
- [ ] Body has at least 200 chars of concrete instructions (not just headings).
- [ ] Every relative link in the body points to a file that exists.
- [ ] If any tool-specific frontmatter is used, the body contains a `Tool-specific extensions` section.

## Judgement (you check)

### Tool independence (Must)

- [ ] I tested this Skill in **at least two** agentic coding tools.
- [ ] I noted in the PR description which tools I tested and what I tried.
- [ ] No tool-specific syntax in the portable instructions, or a documented fallback is provided.

### Usefulness (Should)

- [ ] A developer with no prior framework knowledge can apply this Skill and produce something concrete.
- [ ] The Skill's output is actionable, not a generic essay.
- [ ] The Skill links to the relevant parts of `content/` so the agent can ground its work in the framework.

### Clarity

- [ ] `description` is sharp enough that the agent will choose this Skill, not another one, when it should fire.
- [ ] Steps in "What to do" are numbered and concrete.
- [ ] "What to avoid" lists real anti-patterns, not generic "do not be wrong".

### Modularity (Should)

- [ ] The Skill does one thing well. It does not try to be a full framework tour.
- [ ] If the Skill is part of a layered set (Approach B), the base / domain / composition relationship is obvious.

### Submission

- [ ] PR is opened from a team fork into this repo's `main`.
- [ ] One PR per team, containing **at least two** Skills.
- [ ] PR description covers: approach (A / B / hybrid), what each Skill does, tools tested, link to the 3-minute demo, link to the ≤10-slide pitch deck.
- [ ] PR link, demo, and deck submitted through the Junction submission form for this challenge.
- [ ] CI is green.
- [ ] No real personal data anywhere in the diff.
