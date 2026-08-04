---
title: "Toolbelt guide-implementation checklist"
status: active
aligned_with:
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-21-standards-fanout.md
created: 2026-07-31
updated: 2026-08-04
---

# Guide-implementation checklist

Authority: Theme 14 accepted; Theme 21 fan-out. Used by skill `guide-implementation`.  
**Compose only** — invoke leaves via **Using `<skill>`**; do not paste Plan/Execute/Verify law here.

## Classifier

```text
Impl ask: full-ladder | plan-only | plan+verify | execute | execute-subagents | execute-verify | resume-blocked | trivial-skip
Design/ADR accepted paths (or skip reason):
Trivial skip documented?: yes | no | n/a
```

## Standards resolve (if-present) — Theme 21

```text
Resolve: done (pointers) | no-op (no accepted catalog) | already-pinned (skip) | n/a
standards_catalog:
standards_modules: (id / path / reason) or none
Pocket lean: technical / impl modules matching paths — not design-only principles unless catalog matches
```

## Structured handoff (fill before first leaf)

```text
Goal (one sentence):
Prior actions / results:
Key facts + where from:
Open question for next leaf:
Constraints (e.g. no writes / files in scope):
standards_catalog / standards_modules: (from resolve, or none)
```

## Wire plan (check what you will run)

```text
- [ ] implementation-plan — or N/A / trivial skip
- [ ] implementation-plan-verify → Meta ready — or N/A
- [ ] implementation-execute OR implementation-execute-subagents — or N/A
- [ ] implementation-execute-verify (non-trivial / EOP) — or N/A
- [ ] On verify-fail / unclear Critical → hand off **guide-debug** (not owned here)
```

## Stop

```text
Exit: ready for human | blocked (reason) | continue to happy-path next stage | debug handoff
```
