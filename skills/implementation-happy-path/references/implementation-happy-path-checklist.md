---
title: "Toolbelt happy-path checklist"
status: active
aligned_with:
  - docs/research/reports/theme-10-happy-path.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/reports/theme-17-debug-router.md
  - docs/research/reports/theme-19-standards-apply.md
  - docs/research/reports/theme-21-standards-fanout.md
created: 2026-07-30
updated: 2026-08-04
---

# Happy-path checklist

Authority: Theme 10 accepted; composition Themes 14–15 / 17 / 19 / 21. Used by skill `implementation-happy-path`.  
Orchestration only — chain **pocket routers / entries** via **Using `<skill>`**; do not paste pocket law here.

## Classifier

```text
Ask type: feature | bug | research-only | authoring | standards-resolve | trivial | implementation-only | closeout
Entry skill / skip notes:
  (standards modules → guide-standards; author profiles → author-standards; ambient gate no-ops if no catalog)
  (Theme 21: each pocket guide runs if-present resolve; already-pinned → skip re-resolve)
```

## Progress

```text
Happy-path Progress:
- [ ] 0 Classified ask
- [ ] 1 Research as needed — guide-research (optional; if-present resolve) → research leaves — or N/A
- [ ] 2 guide-design (if-present resolve) → domain design → human accept — or skip documented
- [ ] 3 research-draft-adr if locks — or N/A
- [ ] 4 guide-implementation (if-present resolve; already-pinned OK) → plan → … — or N/A
- [ ] 5 Debug branch if needed — guide-debug (if-present resolve; already-pinned OK)
- [ ] 6 implementation-closeout (optional define/check) — or N/A / trivial skip
- [ ] 7 Stop / human handoff (host ceremony; CI/Bugbot automation Phase 2)
standards_modules pinned this ladder (ids) or none:
```

## Subagent reminder

Controller may hold this checklist. Workers = **one pocket leaf** (not the full ladder).
