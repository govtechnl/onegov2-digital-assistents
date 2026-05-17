"""Repo-wide validator.

Runs two checks:

1. Lint every Skill under `skills/` against the open Agent Skills standard
   (delegates to `skills/framework-validator/scripts/lint_skill.py`).
2. Lint the framework content under `content/` for front-matter, cross-refs,
   and required global YAML files.

Exits non-zero if either check fails.
"""
from __future__ import annotations

import re
import runpy
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Install dependencies with: pip install -r requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
SKILLS_DIR = ROOT / "skills"
LINT_SKILL = ROOT / "scripts" / "lint_skill.py"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def read_yaml(path: Path):
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def parse_markdown(path: Path):
    raw = path.read_text(encoding="utf-8").strip()
    match = FRONT_MATTER_RE.match(raw)
    if not match:
        return {}, raw
    front_matter, body = match.groups()
    meta = yaml.safe_load(front_matter) or {}
    return meta, body.strip()


def validate_domains(errors: list[str]) -> set[str]:
    required = ["id", "nr", "ring", "title", "short"]
    ids: set[str] = set()

    for path in sorted((CONTENT_DIR / "domains").glob("*.md")):
        meta, body = parse_markdown(path)
        for field in required:
            if field not in meta:
                errors.append(f"content/domains/{path.name}: missing field '{field}'")

        domain_id = meta.get("id")
        if domain_id:
            if not ID_RE.match(str(domain_id)):
                errors.append(
                    f"content/domains/{path.name}: id '{domain_id}' must be lowercase "
                    "alphanumeric with hyphens"
                )
            if domain_id in ids:
                errors.append(f"content/domains/{path.name}: duplicate id '{domain_id}'")
            ids.add(domain_id)

        if not body or len(body) < 80:
            errors.append(
                f"content/domains/{path.name}: body text is missing or shorter than 80 chars"
            )

    return ids


def validate_practices(errors: list[str], domain_ids: set[str]) -> None:
    required = ["id", "title", "summary", "domains", "phases", "levels", "sources"]
    ids: set[str] = set()

    sources = read_yaml(CONTENT_DIR / "sources.yaml") or []
    source_ids = {item.get("id") for item in sources if isinstance(item, dict)}

    filters = read_yaml(CONTENT_DIR / "filters.yaml") or {}
    allowed_phases = set(filters.get("phases", []) or [])
    allowed_levels = set(filters.get("levels", []) or [])

    for path in sorted((CONTENT_DIR / "practices").glob("*.md")):
        meta, body = parse_markdown(path)
        for field in required:
            if field not in meta:
                errors.append(f"content/practices/{path.name}: missing field '{field}'")

        practice_id = meta.get("id")
        if practice_id:
            if not ID_RE.match(str(practice_id)):
                errors.append(
                    f"content/practices/{path.name}: id '{practice_id}' must be lowercase "
                    "alphanumeric with hyphens"
                )
            if practice_id in ids:
                errors.append(f"content/practices/{path.name}: duplicate id '{practice_id}'")
            ids.add(practice_id)

        if not body or len(body) < 120:
            errors.append(
                f"content/practices/{path.name}: body text is missing or shorter than 120 chars"
            )

        for domain_ref in meta.get("domains", []) or []:
            if domain_ref not in domain_ids:
                errors.append(
                    f"content/practices/{path.name}: unknown domain reference '{domain_ref}' "
                    "(not in content/domains/)"
                )

        for phase in meta.get("phases", []) or []:
            if allowed_phases and phase not in allowed_phases:
                errors.append(
                    f"content/practices/{path.name}: unknown phase '{phase}' "
                    f"(allowed: {sorted(allowed_phases)})"
                )

        for level in meta.get("levels", []) or []:
            if allowed_levels and level not in allowed_levels:
                errors.append(
                    f"content/practices/{path.name}: unknown level '{level}' "
                    f"(allowed: {sorted(allowed_levels)})"
                )

        for source_id in meta.get("sources", []) or []:
            if source_id not in source_ids:
                errors.append(
                    f"content/practices/{path.name}: unknown source reference '{source_id}' "
                    "(not in content/sources.yaml)"
                )


def validate_globals(errors: list[str]) -> None:
    for required in [
        CONTENT_DIR / "context.yaml",
        CONTENT_DIR / "home.yaml",
        CONTENT_DIR / "filters.yaml",
        CONTENT_DIR / "glossary.yaml",
        CONTENT_DIR / "sources.yaml",
    ]:
        if not required.exists():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")


def run_skill_lint() -> int:
    """Run the skill linter and return its exit code (0 = pass)."""
    if not LINT_SKILL.exists():
        print(f"[skills] linter not found at {LINT_SKILL.relative_to(ROOT)}; skipping")
        return 0
    if not SKILLS_DIR.exists():
        print("[skills] skills/ directory not found; skipping")
        return 0
    argv_backup = sys.argv
    try:
        sys.argv = [str(LINT_SKILL), str(SKILLS_DIR)]
        try:
            runpy.run_path(str(LINT_SKILL), run_name="__main__")
        except SystemExit as exc:
            return int(exc.code or 0)
        return 0
    finally:
        sys.argv = argv_backup


def main() -> int:
    print("==> Validating skills/")
    skill_status = run_skill_lint()

    print("\n==> Validating content/")
    errors: list[str] = []
    validate_globals(errors)
    domain_ids = validate_domains(errors)
    validate_practices(errors, domain_ids)

    if errors:
        print("Content validation failed:")
        for err in errors:
            print(f"- {err}")
        content_status = 1
    else:
        print("Content validation passed")
        content_status = 0

    return skill_status or content_status


if __name__ == "__main__":
    raise SystemExit(main())
