---
title: "Theme 20 — guide-* pocket rename (integrated report)"
status: accepted
theme: theme-20-guide-rename
created: 2026-08-04
updated: 2026-08-04
accepted: 2026-08-04
acceptance_scope: method_and_elevate_t20_guide_rename
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: scrub_complete_smokes_pass
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-20-guide-rename/campaign-brief.md
  - docs/research/notes/theme-20-guide-rename/t20a-reference-inventory.md
  - docs/research/notes/theme-20-guide-rename/t20b-thickness-contract.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-17-debug-router.md
  - docs/research/reports/theme-19-standards-apply.md
supersedes: null
amends:
  - docs/research/reports/theme-14-pocket-routers.md  # vocabulary: guide-* skill ids; router remains role term
---

# Theme 20 — guide-* pocket rename

**Status:** **accepted** (method + elevate) — 2026-08-04.  
**Depth:** normal.  
**Using `author-cursor-surfaces`** for surface edits.  
**Smokes:** Theme 20 claim-card **5/5 PASS**.

## 1. Executive summary

Rename the five pocket entry / classify→wire skills to a symmetric **`guide-*`** prefix (verb-family naming). Hard cutover — no dual-id aliases. Thickness preserved per T20B: `guide-research` / `guide-design` stay thick; Implementation / Debug / Standards guides stay thin compose-only.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-20-guide-rename`** |
| D2 | Prefix map (all five): see §3 |
| D3 | Hard cutover — no alias stubs |
| D4 | Preserve T20B thickness contracts |
| D5 | Historical notes / run filenames may keep old skill ids; live tiers + reports scrubbed |
| D6 | Report path `theme-17-debug-router.md` unchanged (theme folder id ≠ skill id) |

## 3. Rename map

| Former id | New id | Thickness |
|-----------|--------|-----------|
| `research-scope` | `guide-research` | thick companion |
| `design-process` | `guide-design` | thick spine |
| `implementation-router` | `guide-implementation` | thin |
| `debug-router` | `guide-debug` | thin |
| `standards-router` | `guide-standards` | thin |

Templates / checklists / refresh mappings follow the new ids. Rule **`standards-resolve-gate`** announces **`guide-standards`**.

## 4. What changed (elevate)

- Skill dirs under `skills/guide-*`
- Templates: `guide-implementation.md`, `guide-debug.md`, `guide-standards.md`
- Packs Routers row + README / CONTRIBUTING / CHANGELOG / plugin keywords
- Smoke matrix + claim-card **content** (filenames kept for history where useful)
- Descriptions retain former ids as discovery keywords

## 5. Explicit non-goals / parks

- Dual-id aliases
- Global meta-guide
- T19J fan-out of resolve into other pocket guides (still later)
- Renaming Theme 14/17 **report files** or theme folder paths

## 6. Verify before accept

- [x] Live tiers: no current-skill use of old ids except “formerly …” discovery text
- [x] `python scripts/refresh-skill-references.py` OK
- [x] `python scripts/sync-toolbelt-local-plugin.py` + Reload Window
- [x] Theme 20 claim-card smokes **5/5 PASS** (R7, D1, I1, R8, S2) — [CONTROLLER-SUMMARY-theme20-20260804.md](../notes/theme-11-validation/runs/CONTROLLER-SUMMARY-theme20-20260804.md)
- [x] Human review → accept → commit/push when asked
