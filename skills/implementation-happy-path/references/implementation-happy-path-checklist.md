---
title: "Toolbelt happy-path checklist"
status: active
aligned_with:
  - docs/research/reports/theme-10-happy-path.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/reports/theme-17-debug-router.md
  - docs/research/reports/theme-19-standards-apply.md
created: 2026-07-30
updated: 2026-08-03
---

# Happy-path checklist

Authority: Theme 10 accepted; composition Themes 14–15 / 17 / 19. Used by skill `implementation-happy-path`.  
Orchestration only — chain **pocket routers / entries** via **Using `<skill>`**; do not paste pocket law here.

## Classifier

```text
Ask type: feature | bug | research-only | authoring | standards-resolve | trivial | implementation-only | closeout
Entry skill / skip notes:
  (standards modules → guide-standards; author profiles → author-standards; ambient gate no-ops if no catalog)
```

## Progress

```text
Happy-path Progress:
- [ ] 0 Classified ask
- [ ] 1 Research as needed — guide-research (optional) → research leaves — or N/A
- [ ] 2 guide-design → domain design → human accept — or skip documented
- [ ] 3 research-draft-adr if locks — or N/A
- [ ] 4 guide-implementation (plan → plan-verify → execute|-subagents → execute-verify) — or N/A
- [ ] 5 Debug branch if needed — guide-debug (reproduce / systematic)
- [ ] 6 implementation-closeout (optional define/check) — or N/A / trivial skip
- [ ] 7 Stop / human handoff (host ceremony; CI/Bugbot automation Phase 2)
```

## Subagent reminder

Controller may hold this checklist. Workers = **one pocket leaf** (not the full ladder).
