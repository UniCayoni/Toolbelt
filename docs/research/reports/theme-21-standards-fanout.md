---
title: "Theme 21 — Standards resolve fan-out / T19J (integrated report)"
status: accepted
theme: theme-21-standards-fanout
created: 2026-08-04
updated: 2026-08-04
accepted: 2026-08-04
acceptance_scope: method_and_elevate_t21_standards_fanout
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: theme_19_apply_law_sufficient_wire_only
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-21-standards-fanout/campaign-brief.md
  - docs/research/reports/theme-19-standards-apply.md
  - docs/research/reports/theme-20-guide-rename.md
supersedes: null
amends:
  - docs/research/reports/theme-19-standards-apply.md  # D11 T19J parked → shipped
---

# Theme 21 — Standards resolve fan-out (T19J)

**Status:** **accepted** (method + elevate) — 2026-08-04.  
**Using `author-cursor-surfaces`**.  
**Cutover:** single sync after coherent wire (no accepted Toolbelt host catalog during elevate).

## 1. Executive summary

Closes Theme 19 **T19J**: pocket **`guide-*`** entries run Theme 19 **if-present** resolve (`guide-standards`) so `standards_modules` attach at pocket entry. No new apply classifier law. Empty catalog → no-op (Design/Research stay flexible by default). Host-tagged principles / design-inclination modules enable philosophical bounds when accepted; Impl technical modules stay pocket-scoped.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-21-standards-fanout`** (ships T19J) |
| D2 | Wire **all five** pocket guides: `guide-research`, `guide-design`, `guide-implementation`, `guide-debug` (+ happy-path already-pinned note). `guide-standards` remains the resolve skill |
| D3 | Step: already-pinned skip → else if accepted catalog → **Using `guide-standards`** → pointers on handoff → else no-op |
| D4 | Pocket lean: research/design → principles / method-inclination tags; impl/debug → technical tags; no auto cross-apply |
| D5 | Happy-path: guides own resolve; **do not** force four full reloads — carry pinned modules |
| D6 | Ambient `standards-resolve-gate` unchanged (coexists) |
| D7 | Parks: dual-era schema v2; Toolbelt-universal style; host corpora as host action. **Global meta-guide** → **shipped Theme 22** |
| D8 | Smoke **S3** (or extend S2): pocket entry no-op + fixture pointers + already-pinned skip + pocket lean |

## 3. Surfaces

| Surface | Change |
|---------|--------|
| `guide-research` / `guide-design` / `guide-implementation` / `guide-debug` | If-present resolve step |
| `guide-standards` | Caller pocket + pocket-lean classifier hints |
| `implementation-happy-path` + templates | Theme 21 notes; pinned modules line |
| `docs/templates/standards-catalog.md` | Example pocket tag rows |
| Theme 19 report | D11 T19J → shipped |

## 4. Acceptance checklist

- [x] Scope lean accepted (all pocket guides) — 2026-08-04  
- [x] Elevate via `author-cursor-surfaces`  
- [x] Smoke S3 **PASS** (`S3-theme21-20260804.md`)  
- [x] Sync once (Reload Window on your side)  
- [ ] Human review → commit/push when asked  
