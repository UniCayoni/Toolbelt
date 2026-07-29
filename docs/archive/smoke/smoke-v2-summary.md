---
title: "Smoke v2 — patched harness results"
status: draft
created: 2026-07-28
---

# Smoke v2 summary

## What changed before retest

Crosswalk: `harness-patch-crosswalk.md` (Themes 1–3 + Cursor/Superpowers smoke v1 → patches).

| Patch | Landed in |
|-------|-----------|
| S13 / persist either-OK | `codebase-recon`, `docs-research`, templates |
| Write gate = implementation only | `research-before-write.mdc`, S16 template |
| D0 `in_use` + build GAP | `docs-research`, `documentation-research.md` |
| Windows E0 tip | both research skills + templates |
| Announce Using skill | all 5 skills + grades rule |
| Coexistence soft rule | `research-skill-coexistence.mdc` |
| OpenAPI tools only if schema | `docs-research` + D12 template |

## Process (v2 vs v1)

| Discipline | v1 | v2 |
|------------|----|----|
| Announce skill | informal | **Using `…`** in notes + this run |
| Literal checklist copy | wrote filled notes directly | `Copy-Item` from skill `references/` then fill |
| S13 | grades in checklist (undeclared) | **declared** either-OK |
| Windows E0 | PS flaky → recovered via Python | Python first (`_e0_check_v2.py`) |
| Cursor D0 | awkward “session active” | **`in_use` + build GAP** |
| OpenAPI step | N/A ad hoc | **N/A by skill** |
| research-protocol full note | skipped | intentionally skipped (either-OK) |

## Research content (reconfirm)

Unchanged material findings:

- Superpowers local **6.1.1** vs tip **6.2.0**; `evals/` missing; no package `scripts`
- Cursor skill/rule layout MATCH; 4 rules now (added coexistence)

## Harness verdict

| Skill / rule | v2 result |
|--------------|-----------|
| `codebase-recon` | **Pass** under patched process |
| `docs-research` | **Pass** under patched process |
| `research-protocol` | Not fully re-run (allowed); grades still via checklist + always rule |
| Always grades / draft≠SoT | Hold |
| `research-before-write` | Wording fixed; research notes written without treating as gate violation |
| Coexistence rule | Present; soft — not conflict-exercised against Superpowers MUST |

**No invented APIs.** Patches did not worsen Superpowers/Cursor claims; they made process auditable and removed false OpenAPI/version pressure.

## Artifacts

- Working notes under `archive/` (`v2-*.md`, `_e0_check_v2.py`, `harness-patch-crosswalk.md`)
- This summary
