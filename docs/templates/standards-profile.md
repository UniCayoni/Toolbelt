---
title: "Toolbelt standards profile (host-owned)"
status: active
aligned_with: docs/research/reports/theme-16-host-standards.md
created: 2026-08-02
---

# Standards profile

Authority: Theme 16 accepted. Used by skill **`author-standards`** (mode `standards` / `derive`).  
**Host-owned** — copy to e.g. `docs/standards/standards-profile.md` (path override OK).  
**Altitude:** explicit, **checkable** constraints — not vibes. Filename alone is overloaded; keep this purpose clear.

## Header

```text
Host / product:
Profile version / date:
Owner (human):
Status: draft | proposed | accepted
Scope (langs / paths / packages):
Principles profile path (optional):
Enforcement pointers (linter/formatter/CI — host-owned):
```

## Types in scope (v1 lean)

Mark which types this profile covers. Park the rest or point to ADR/CONTRIBUTING.

| Type | In profile? | Notes |
|------|-------------|-------|
| Naming | | |
| Layout / structure | | |
| Patterns (prefer / avoid) | | |
| Tests / docs expectations | | |
| Safety / secrets | | |
| API / errors (optional) | | |
| Parked (perf / i18n / a11y / process / architecture) | | point elsewhere or N/A |

## Rules

Each rule should be checkable or have a clear example + exception.

| ID | Type | Rule | Example | Exceptions | How to check |
|----|------|------|---------|------------|--------------|
| S1 | | | | | |
| S2 | | | | | |

## Anti-patterns

```text
-
```

## Dual-era / brownfield (optional)

```text
Legacy paths quarantined:
Format wave / .git-blame-ignore-revs note:
New-code-only vs whole-repo:
```

## Evolution / deprecate

```text
Deprecated rules (id → replacement → remove-after):
Changelog:
```

## Bind

```text
Plan / Execute / Closeout should load this when present.
AGENTS.md: short pointer only.
Closeout: optional criterion row referencing this profile.
```
