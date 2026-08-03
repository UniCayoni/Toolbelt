---
title: "Smoke T16 — standards profile (S1 fresh)"
status: draft
theme: theme-11-validation
surface_id: S1
mode: standards
aligned_with: docs/research/reports/theme-16-host-standards.md
created: 2026-08-02
note: Theme 11 smoke artifact only — not accepted SoT. Naming + layout only.
---

# Standards profile

Authority: Theme 16 accepted. Skill **`author-standards`** mode `standards`.  
**Host-owned** smoke draft — docs/skills markdown conventions only.  
**Altitude:** explicit, **checkable** constraints — not vibes.

## Header

```text
Host / product: Toolbelt (smoke host)
Profile version / date: 0.1-smoke / 2026-08-02
Owner (human): Theme 11 validator (unaccepted)
Status: draft
Scope (langs / paths / packages): Markdown under skills/**/SKILL.md, skills/**/references/**, docs/templates/**
Principles profile path (optional): docs/research/notes/theme-11-validation/runs/artifacts/smoke-t16-principles-fresh.md
Enforcement pointers (linter/formatter/CI — host-owned): manual review / path glob (no CI ceremony claimed)
```

## Types in scope (v1 lean)

| Type | In profile? | Notes |
|------|-------------|-------|
| Naming | yes | skill folder + frontmatter `name` |
| Layout / structure | yes | SKILL.md + references/ |
| Patterns (prefer / avoid) | no | parked for smoke |
| Tests / docs expectations | no | parked |
| Safety / secrets | no | parked |
| API / errors (optional) | no | N/A |
| Parked (perf / i18n / a11y / process / architecture) | yes | point elsewhere or N/A |

## Rules

| ID | Type | Rule | Example | Exceptions | How to check |
|----|------|------|---------|------------|--------------|
| S1 | Naming | Each skill lives in `skills/<kebab-name>/` and YAML frontmatter `name` matches the folder name. | `skills/author-standards/` → `name: author-standards` | Historical renames under explicit host note | Glob `skills/*/SKILL.md`; compare folder basename to `name:` |
| S2 | Layout | Skill package root contains `SKILL.md`; optional long-form material under `references/` (not dumped into AGENTS.md). | `skills/author-standards/references/principles-profile.md` | One-file pocket skills with no references | Path exists check; AGENTS has pointer only if profiles exist |

## Anti-patterns

```text
- Dumping full standards profiles into root AGENTS.md
- Mixing philosophy (principles) into lint-style rows without a separate principles profile
- Claiming Toolbelt-universal coding law for all hosts
```

## Dual-era / brownfield (optional)

```text
Legacy paths quarantined: n/a for smoke
Format wave / .git-blame-ignore-revs note: not used this pass
New-code-only vs whole-repo: smoke scope = skills/** + docs/templates/**
```

## Evolution / deprecate

```text
Deprecated rules (id → replacement → remove-after): none
Changelog: 2026-08-02 S1 fresh smoke draft created.
```

## Bind

```text
Plan / Execute / Closeout should load this when present.
AGENTS.md: short pointer only.
Closeout: optional criterion row referencing this profile.
Status remains draft until human accepts — do not treat as SoT.
```
