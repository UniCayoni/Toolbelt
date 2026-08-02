---
title: "Toolbelt happy-path checklist"
status: active
aligned_with:
  - docs/research/reports/theme-10-happy-path.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-15-closeout-readiness.md
created: 2026-07-30
updated: 2026-08-02
---

# Happy-path checklist

Authority: Theme 10 accepted; composition Themes 14–15. Used by skill `implementation-happy-path`.  
Orchestration only — chain **pocket routers / entries** via **Using `<skill>`**; do not paste pocket law here.

## Classifier

```text
Ask type: feature | bug | research-only | authoring | trivial | implementation-only | closeout
Entry skill / skip notes:
```

## Progress

```text
Happy-path Progress:
- [ ] 0 Classified ask
- [ ] 1 Research as needed — research-scope (optional) → research leaves — or N/A
- [ ] 2 design-process → domain design → human accept — or skip documented
- [ ] 3 research-draft-adr if locks — or N/A
- [ ] 4 implementation-router (plan → plan-verify → execute|-subagents → execute-verify) — or N/A
- [ ] 5 Debug branch if needed (debug-reproduce / debug-systematic) — Debug router deferred
- [ ] 6 implementation-closeout (optional define/check) — or N/A / trivial skip
- [ ] 7 Stop / human handoff (host ceremony; CI/Bugbot automation Phase 2)
```

## Subagent reminder

Controller may hold this checklist. Workers = **one pocket leaf** (not the full ladder).
