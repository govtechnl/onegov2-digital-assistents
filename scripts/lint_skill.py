#!/usr/bin/env python3
"""Lint one or more Skill directories against the open Agent Skills standard
and the OneGov #2 conventions.

Usage:
    python lint_skill.py <path>            # lint a single skill directory
    python lint_skill.py skills/           # lint every skill under skills/

Exits non-zero when any skill has errors.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Install with: pip install -r requirements.txt"
    ) from exc

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
RESERVED_NAMES = {"anthropic", "claude"}
TOOL_SPECIFIC_FIELDS = {
    "allowed-tools",
    "disable-model-invocation",
    "user-invocable",
    "model",
    "effort",
    "context",
    "agent",
    "hooks",
    "paths",
    "shell",
    "argument-hint",
    "arguments",
    "when_to_use",
}
SKIP_DIRS = {"_template"}


def parse_skill(skill_md: Path) -> tuple[dict, str]:
    raw = skill_md.read_text(encoding="utf-8").lstrip()
    match = FRONT_MATTER_RE.match(raw)
    if not match:
        return {}, raw
    front, body = match.groups()
    return yaml.safe_load(front) or {}, body


def lint_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    rel = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        errors.append(f"{rel}: missing SKILL.md")
        return errors

    meta, body = parse_skill(skill_md)
    if not meta:
        errors.append(f"{rel}/SKILL.md: missing or malformed YAML frontmatter")
        return errors

    # Required: name (recommended) and description (required by spec).
    name = meta.get("name")
    if not name:
        errors.append(f"{rel}/SKILL.md: 'name' missing (recommended; should match directory name)")
    else:
        if not isinstance(name, str) or not NAME_RE.match(name):
            errors.append(
                f"{rel}/SKILL.md: 'name' must be lowercase letters, numbers, hyphens; max 64 chars"
            )
        if name in RESERVED_NAMES:
            errors.append(f"{rel}/SKILL.md: 'name' '{name}' is a reserved word")
        if name and name != rel:
            errors.append(
                f"{rel}/SKILL.md: 'name' ('{name}') does not match directory name ('{rel}')"
            )

    description = meta.get("description")
    if not description or not isinstance(description, str) or not description.strip():
        errors.append(f"{rel}/SKILL.md: 'description' is required and must be non-empty")
    elif len(description) > 1024:
        errors.append(
            f"{rel}/SKILL.md: 'description' is {len(description)} chars (max 1024)"
        )

    # Body must have actual instructions, not just a single heading.
    stripped_body = body.strip()
    if not stripped_body:
        errors.append(f"{rel}/SKILL.md: body is empty")
    elif len(stripped_body) < 200:
        errors.append(
            f"{rel}/SKILL.md: body is shorter than 200 chars; add concrete instructions"
        )

    # Tool-specific extensions: allowed, but require an explicit section.
    tool_specific_used = sorted(set(meta.keys()) & TOOL_SPECIFIC_FIELDS)
    if tool_specific_used and "tool-specific" not in body.lower():
        errors.append(
            f"{rel}/SKILL.md: tool-specific frontmatter field(s) {tool_specific_used} "
            "used without a 'Tool-specific extensions' section explaining fallback"
        )

    # Supporting files referenced from the body must exist.
    link_re = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
    for target in link_re.findall(body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Resolve relative to the SKILL.md file.
        ref_path = (skill_md.parent / target).resolve()
        if not ref_path.exists():
            errors.append(f"{rel}/SKILL.md: broken link '{target}'")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2

    target = Path(argv[1]).resolve()
    if not target.exists():
        print(f"Path not found: {target}")
        return 2

    if (target / "SKILL.md").exists():
        skill_dirs = [target]
    else:
        skill_dirs = [
            p
            for p in sorted(target.iterdir())
            if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith(".")
        ]

    if not skill_dirs:
        print(f"No skill directories found under {target}")
        return 0

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        errors = lint_skill(skill_dir)
        if errors:
            all_errors.extend(errors)

    if all_errors:
        print(f"Skill lint failed ({len(all_errors)} issue(s)):")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Skill lint passed ({len(skill_dirs)} skill(s) checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
