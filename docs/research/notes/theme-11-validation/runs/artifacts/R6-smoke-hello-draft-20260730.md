---
title: "R6 smoke — draft skill smoke-hello (frontmatter + outline)"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
authors: [theme-11-pocket-smoke]
supersedes: null
---

# Draft proposal — skill `smoke-hello` (not written to `skills/`)

**Status:** `draft` / proposed only. Not SoT. Do not elevate. Do not write under Toolbelt `skills/` or `rules/` until human accepts.

## Surface choice (Theme 4 §1)

| Field | Value |
|-------|-------|
| Primary surface | **Skill** (`skills/smoke-hello/SKILL.md`) |
| Why not rule | Checklist / multi-step judgment → skill; always-on rules stay short (Theme 4 reinforce) |
| Mode | author |
| Scaffold | `no` (draft outline only; `/create-skill` optional if later accepted) |
| Until human accepts | `draft` |

## Proposed frontmatter

```yaml
---
name: smoke-hello
description: >-
  Print a short hello checklist for Theme 11 pocket-smoke drills. Use when
  validating skill discovery, author-cursor-surfaces drafts, or checklist-only
  smoke-hello runs. Explicit invoke. Not a workflow orchestrator or always-on rule.
---
```

## Theme 4 reinforce checklist (applied to this draft)

- [x] `name` == parent folder: `smoke-hello` ↔ `skills/smoke-hello/`
- [x] Pushy `description` (what + when + keywords: pocket-smoke, checklist, discovery)
- [x] `disable-model-invocation` omitted (not slash-only; allow discovery) — flip to `true` only if human wants `/smoke-hello` exclusive
- [x] Body lean; no `references/` needed for a one-page checklist
- [x] Announce **Using `smoke-hello`** once for auditability
- [x] Not an always-on fat rule for a multi-step workflow

## Proposed body outline

```markdown
# Smoke hello

Announce once: **Using `smoke-hello`**.

## Checklist

- [ ] Skill discovered (name + description)
- [ ] Folder path matches `name` (`skills/smoke-hello/`)
- [ ] Checklist printed; no repo writes unless human asked
- [ ] Remains draft until human accepts

## Stop

Do not elevate. Do not treat this surface as SoT until accepted.
```

## Verify (deferred)

Reload / Customize / `/` smoke — n/a until human accepts and files are written outside this draft artifact.
