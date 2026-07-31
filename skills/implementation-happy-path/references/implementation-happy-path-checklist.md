---
title: "Toolbelt happy-path checklist"
status: active
aligned_with: docs/research/reports/theme-10-happy-path.md
created: 2026-07-30
---

# Happy-path checklist

Authority: Theme 10 accepted. Used by skill `implementation-happy-path`.  
Orchestration only — run each step via **Using `<skill>`**; do not paste pocket law here.

## Classifier

```text
Ask type: feature | bug | research-only | authoring | trivial
Entry skill / skip notes:
```

## Progress

```text
Happy-path Progress:
- [ ] 0 Classified ask
- [ ] 1 Research as needed (codebase-recon / docs-research / research-protocol) — or N/A
- [ ] 2 design-process → domain design → human accept — or skip documented
- [ ] 3 draft-adr if locks — or N/A
- [ ] 4 implementation-plan — or trivial skip documented
- [ ] 5 implementation-plan-verify → Meta ready
- [ ] 6 implementation-execute OR implementation-execute-subagents
- [ ] 7 implementation-execute-verify (non-trivial / EOP)
- [ ] 8 Debug branch if needed (reproduce-bug / systematic-debug)
- [ ] 9 Stop / human handoff (PR Phase 2 only if asked)
```

## Subagent reminder

Controller may hold this checklist. Workers = **one pocket** (not the full ladder).
