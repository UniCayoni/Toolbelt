---
title: "Theme 22 — Global meta-guide (integrated report)"
status: accepted
theme: theme-22-meta-guide
created: 2026-08-04
updated: 2026-08-04
accepted: 2026-08-04
acceptance_scope: method_and_elevate_t22_meta_guide
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: theme_14_park_reopen_as_skill_only
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-22-meta-guide/campaign-brief.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-20-guide-rename.md
  - docs/research/reports/theme-21-standards-fanout.md
supersedes: null
amends:
  - docs/research/reports/theme-14-pocket-routers.md  # D6 global skill-router → skill guide-meta (not always-on)
---

# Theme 22 — Global meta-guide

**Status:** **accepted** (method + elevate) — 2026-08-04.  
**Using `author-cursor-surfaces`**.  
**Cutover:** single sync after coherent wire.

## 1. Executive summary

Ships **`guide-meta`**: thin diagnostic front door — classify fuzzy/cold asks → **one** next Toolbelt surface → handoff → stop. Reopens Theme 14’s parked global skill-router as an **opt-in skill**, not always-on. Does not replace pocket guides or `implementation-happy-path`.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-22-meta-guide`** |
| D2 | Skill id **`guide-meta`** + template `docs/templates/guide-meta.md` |
| D3 | Thickness: **thin diagnostic** (not PIPELINE composition planner) |
| D4 | **Not** `alwaysApply` — discovery via description + `/guide-meta` |
| D5 | Allowlist next: pocket `guide-*`, `implementation-happy-path`, `author-standards`, `author-cursor-surfaces`, `implementation-closeout`, or leaf-direct skip |
| D6 | Prefer smallest sufficient entry; happy-path only when full feature ladder is the ask |
| D7 | Standards resolve stays Theme 21 / ambient gate — meta does not own it |
| D8 | Parks: always-on meta rule; mega-wire inside meta |
| D9 | Smoke **M1** |

## 3. Surfaces

| Surface | Change |
|---------|--------|
| `skills/guide-meta/` | New |
| `docs/templates/guide-meta.md` | New + refresh mapping |
| Packs / README / CHANGELOG / plugin keywords | Meta row / skill count |
| Theme 14 report | D6 park → shipped as skill-only |

## 4. Acceptance checklist

- [x] Scope O1 accepted (skill-only; not always-on) — 2026-08-04  
- [x] Elevate via `author-cursor-surfaces`  
- [x] Smoke M1 **PASS** (`M1-theme22-20260804.md`)  
- [x] Sync once (Reload Window on your side)  
- [ ] Human review → commit/push when asked  
