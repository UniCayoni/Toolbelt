---
title: "Toolbelt standards catalog (host-owned index)"
status: active
aligned_with: docs/research/reports/theme-19-standards-apply.md
created: 2026-08-03
---

# Standards catalog (index)

Authority: Theme 19 accepted. Used by skill **`standards-router`** and rule **standards-resolve-gate**.  
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
| | | | | | | |

**One-file hosts:** list a single row pointing at `docs/standards/standards-profile.md` (Theme 16 template) with broad globs.

## Resolve contract

```text
Only modules with Status = accepted are loadable as law.
draft / proposed → ignore for apply (draft≠SoT).
Absent catalog or zero accepted modules → standards-resolve-gate no-op.
```
