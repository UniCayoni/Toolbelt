---
title: "Theme 15 — author-cursor-surfaces reinforce (implementation-closeout)"
status: accepted
theme: theme-15-closeout-readiness
created: 2026-08-02
updated: 2026-08-02
authors: [coordinator]
aligned_with:
  - docs/templates/author-cursor-surfaces.md
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/notes/parked/author-surfaces-reinforce-t14-t15.md
supersedes: null
---

# Theme 15 — author-cursor-surfaces reinforce

**Using `author-cursor-surfaces`**.

## 0 — Outcome & mode

| Field | Value |
|-------|-------|
| Outcome | Retroactive Theme 4 reinforce for `implementation-closeout` (elevated without this skill) |
| Mode | **author** (reinforce; no method redesign) |
| Target | Toolbelt `skills/implementation-closeout/` |
| Scaffold | no |

## 1 — Surface

| Choice | Value |
|--------|-------|
| Primary | Skill (readiness define/check) |
| Always-on rule | Rejected (Theme 15) |
| `disable-model-invocation` | **No** — discoverable like closeout companion |

## 3 — Toolbelt reinforce checklist

### `implementation-closeout`

- [x] `name` == folder
- [x] Pushy description — reinforced to include skill id `implementation-closeout` for cold-start keywords
- [x] No `disable-model-invocation`
- [x] Body lean (~81 lines); profile + checklist refs with read-when
- [x] Announce **Using `implementation-closeout`**
- [x] Compose: handoffs to happy-path / router / author-standards; ceremony out of scope
- [x] Templates mapped in `refresh-skill-references.py`

## Packaging delta this pass

| Change | Why |
|--------|-----|
| Description adds `implementation-closeout` keyword | Theme 4 pushy discovery parity with `implementation-router` |

## 5 — Verify

- [x] Paths relative
- [x] Sync after this note
- [ ] Operator Reload if needed

## Process debt

First elevation skipped `/author-cursor-surfaces`. This note closes packaging reinforce only — readiness method unchanged (Theme 15 accepted).
