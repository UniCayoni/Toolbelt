---
title: "Smoke trials — elevated GreyMatter skills"
status: draft
created: 2026-07-28
theme: smoke
---

# Smoke trial summary

## Scope

Two read-only smoke trials after elevating skills to `.cursor/skills/`:

1. **`codebase-recon`** on https://github.com/obra/superpowers + local Cursor plugin install  
2. **`docs-research`** on Cursor Skills/Rules docs + live GreyMatter `.cursor` artifacts  

Plugin stub remains on hold. No Superpowers/Cursor product code modified.

## Verdict

Both skills are **usable as written**. Checklists filled, citations graded, E0 corroboration caught real skew/drift. Soft S16 gate respected (no implement).

| Trial | Skill | Result |
|-------|-------|--------|
| Superpowers | `codebase-recon` (+ Explore) | **Pass** — structure, version pin, docs↔tree conflict found |
| Cursor docs | `docs-research` | **Pass** — skill/rule atoms MATCH local elevation |

## Trial 1 — Superpowers (`recon-superpowers.md`)

| Item | Evidence |
|------|----------|
| Local install | `…/superpowers/d884ae04…` version **6.1.1** [E0] |
| GitHub tip | plugin.json **6.2.0** [E1] → **version skew** |
| Skills | 14 folders [E0]; manifest skills+hooks only |
| Docs drift | `docs/testing.md` documents `evals/` + `npm test`; `evals/` missing local+tip; no package `scripts` [E0/E1] |
| E3 sample | open bugs #1936, #1878, #1827, #1856 — discovery only |
| Explore | [Explore superpowers](6a5163e5-b6cb-4999-8018-a4bc79298f91) |

## Trial 2 — Cursor docs (`docs-cursor.md`)

| Atom | Docs (E1) | Local (E0) |
|------|-----------|------------|
| `.cursor/skills/*/SKILL.md` | required layout | 5 skills OK |
| `name` == folder | required | all match |
| `disable-model-invocation` | optional explicit invoke | author-agents-md, draft-adr |
| `.cursor/rules/*.mdc` | required extension | 3 rules |
| `/llms.txt` | index | fetched; one malformed changelog URL |

## Skill pack feedback (smoke → possible tweaks)

| Observation | Severity | Suggested tweak |
|-------------|----------|-----------------|
| Windows PowerShell one-liners unreliable for listing; Python E0 script worked | medium | Add optional `scripts/e0_path_check.py` pattern under `codebase-recon` / `docs-research` references |
| Version pin (install vs tip) is high-value and easy to miss | low | Already in D0/S0 — keep; maybe bold in skill body |
| `docs-research` D7 full issue scan heavy for smoke | low | Skill already allows waive — OK |
| Superpowers `using-superpowers` forces skill-before-any-response; conflicts with GreyMatter soft recon | OPEN | Product tension if both always-on — document coexistence later |
| Exact Cursor app build not captured | GAP | Optional E0 step: read About / CLI version |

## Artifacts

- Working notes: `archive/recon-superpowers.md`, `archive/docs-cursor.md`, `archive/_e0_check.py`
- This summary

## Next

- Optional: apply small skill tweaks from feedback table  
- Optional: deeper Cursor changelog / Superpowers update to 6.2.0  
- Resume plugin stub when ready
