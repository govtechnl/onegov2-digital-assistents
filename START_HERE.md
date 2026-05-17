# Start Here (Hackathon Teams)

Use this flow to get to your first valid Skill quickly.

## 1) Read challenge + output format (10 min)

- Read [CHALLENGE.md](CHALLENGE.md).
- Read [docs/skill-format.md](docs/skill-format.md).
- Read [docs/skill-checklist.md](docs/skill-checklist.md).

## 2) Set up local validation (10 min)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/validate.py
```

## 3) Pick your strategy (5 min)

- Approach A: one focused skill per topic.
- Approach B: layered skills (base + domain + composition).
- Hybrid: start with one focused skill, then add composition.

## 4) Create your first skill

- Copy [skills/_template/](skills/_template/)
  to `skills/<your-skill-name>/`.
- Fill frontmatter and instructions in `SKILL.md`.
- Re-run `python scripts/validate.py`.

## 5) Ground your skill in framework content

- Use domain docs in [content/domains/](content/domains/).
- Use practices in [content/practices/](content/practices/).
- Use supporting terms from [content/glossary.yaml](content/glossary.yaml).

## 6) Before submission

- Test in at least two agentic coding tools.
- Ensure instructions are tool-independent and deterministic.
- Open one PR per team with a short evidence summary.