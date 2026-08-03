---
title: "Theme 18 — Recon git/history wire (integrated report)"
status: accepted
theme: theme-18-recon-history
created: 2026-08-03
updated: 2026-08-03
accepted: 2026-08-03
acceptance_scope: method_and_elevate_t18_recon_history
accepted_by: human (Jonathan) — campaign brief + L1–L9
authors: [integrator]
depth: normal
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-18-recon-history/campaign-brief.md
  - docs/research/reports/theme-16-host-standards.md
supersedes: null
amends:
  - docs/research/reports/theme-16-host-standards.md
---

# Theme 18 — Recon git/history wire

**Status:** **accepted** (method + elevate) — campaign brief / L1–L9 2026-08-03.  
**Using `author-cursor-surfaces`** for surface edits.

## 1. Executive summary

Wire conditional **S12b** (git history / recency) into `research-codebase-recon` and tighten `author-standards` **derive** so Theme 16 brownfield D9 has recon feedstock. Conflict primary = **most recent non-one-off**; default window **12 months** with host override; light hot-path support only.

## 2. Elevation decisions (accepted L1–L9)

| # | Decision |
|---|----------|
| L1 | Default window **12 months**; host override date/months/years (Toolbelt method) |
| L2 | Conflict → most recent **non-one-off** default propose candidate |
| L3 | One-off heuristics demote (singleton / contradicts config / not in hot paths) |
| L4 | Light hot-path/churn support only |
| L5 | History step **conditional** (derive / brownfield / era conflict / user ask) |
| L6 | Cite-or-omit; **proposed** only; CLI examples not law |
| L7 | Honor `.git-blame-ignore-revs` when present |
| L8 | Surfaces: recon template/skill + derive glue; smoke **R9** |
| L9 | Parks: closeout rename; dual-era profile schema v2; hard N-thresholds; Phase 2 CI |

## 3. Surfaces

| Surface | Change |
|---------|--------|
| `docs/templates/codebase-reconnaissance.md` | **S12b** |
| `skills/research-codebase-recon` | Instructions + handoff + description |
| `docs/templates/author-standards-checklist.md` | Derive expects S12b + L2 |
| `skills/author-standards` | Derive mode Theme 18 language |
| Theme 16 report | D9 + GAP rows amended |

## 4. Acceptance checklist

- [x] Campaign scope + L1–L9 accepted — 2026-08-03  
- [x] Elevate / wire via `author-cursor-surfaces`  
- [x] Smoke R9 **2/2 PASS** (2026-08-03)  
- [x] Sync + push (noreply)  
