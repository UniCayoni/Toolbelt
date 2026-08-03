---
title: "Smoke T16 — standards (draft)"
status: draft
smoke: S1
created: 2026-08-02
---

# Standards profile (smoke)

Authority: Theme 16 / `author-standards` mode `standards`. **Draft ≠ SoT.**

## Header

```text
Host / product: Toolbelt (smoke fixture)
Profile version / date: smoke-2026-08-02
Owner (human): smoke runner
Status: draft
Scope: docs/**/*.md, skills/**/SKILL.md (smoke only)
Principles profile path: smoke-t16-principles.md
Enforcement pointers: human review / existing refresh scripts (no new CI law)
```

## Types in scope (v1 lean)

| Type | In profile? | Notes |
|------|-------------|-------|
| Naming | yes | skill `name` == folder kebab-case |
| Layout / structure | yes | skill body lean; detail in references/ with read-when |
| Patterns | no | park for smoke |
| Tests / docs | no | park |
| Safety / secrets | no | park |

## Rules

| ID | Type | Rule | Example | Exceptions | How to check |
|----|------|------|---------|------------|--------------|
| S1 | Naming | Skill `name` frontmatter equals parent folder | `author-standards` / `skills/author-standards/` | Renames with dual path note | E0 list dir vs FM |
| S2 | Layout | Progressive disclosure: checklist/templates in `references/`, not megabody | closeout/author-standards pattern | Tiny skills &lt; ~80 lines OK inline | File size / refs present |

## Evolution

```text
Smoke only — delete or ignore after S1.
```
