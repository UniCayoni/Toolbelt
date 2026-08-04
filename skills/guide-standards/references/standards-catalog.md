---
title: "Toolbelt standards catalog (host-owned index)"
status: active
aligned_with:
  - docs/research/reports/theme-19-standards-apply.md
  - docs/research/reports/theme-21-standards-fanout.md
created: 2026-08-03
updated: 2026-08-04
---

# Standards catalog (index)

Authority: Theme 19 accepted. Used by skill **`guide-standards`** and rule **standards-resolve-gate**.  
**Host-owned** — copy to e.g. `docs/standards/index.md` (path override OK).  
**Purpose:** map work → **module paths**. Not the rules body.

```text
Host / product:
Catalog version / date:
Owner (human):
Status: draft | proposed | accepted
Principles profile path (optional):
Legacy single-file standards profile (optional module):
```

## Modules

| ID | Path | Status | Types (v1) | applies_to_paths | applies_to_skills / pockets | Notes |
|----|------|--------|------------|------------------|-----------------------------|-------|
| core-safety | docs/standards/modules/core-safety.md | | safety | **/* | * | thin must-include when any module loads (host choice) |
| | | | | | guide-research / research | research breadth / method inclinations (optional) |
| | | | | | guide-design / design | design inclinations (option count, prototype vs prod) (optional) |
| | | | | | guide-implementation / impl | technical naming/layout/tests (typical) |
| | | | | | guide-debug / debug | technical + safety as needed |

**One-file hosts:** list a single row pointing at `docs/standards/standards-profile.md` (Theme 16 template) with broad globs.  
**Theme 21:** pocket guides call resolve if-present; tag `applies_to_skills / pockets` so research/design do not pull Impl-only rows by default.

## Resolve contract

```text
Only modules with Status = accepted are loadable as law.
draft / proposed → ignore for apply (draft≠SoT).
Absent catalog or zero accepted modules → standards-resolve-gate no-op.
```
