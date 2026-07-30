---
title: "Author Cursor surfaces — Theme 8 verify companions (reinforce)"
status: accepted
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
aligned_with:
  - docs/templates/author-cursor-surfaces.md
  - docs/research/reports/theme-4-cursor-plugin-components.md
  - docs/research/reports/theme-8-verify-gates.md
supersedes: null
---

# Author Cursor surfaces — T8 verify reinforce

**Using `author-cursor-surfaces`**.

## 0 — Outcome & mode

| Field | Value |
|-------|-------|
| Outcome | Theme 4–conformant skills for Plan/Execute verify companions (retroactive reinforce after elevate skipped this skill) |
| Mode | **author** (reinforce existing elevation) |
| Target | Toolbelt plugin `skills/` |
| Status | accepted with Theme 8 report (human lean quality/readability/Toolbelt focus) |

## 1 — Choose surface

| Surface | Choice |
|---------|--------|
| Primary | **Skills** (multi-step judgment + progressive refs) |
| Rule | **No** always-on verify rule (Theme 8 D3) |
| Command / slash-only | **No** `disable-model-invocation` — companions should auto-discover like Plan/Execute |
| Hook / agents | N/A |

## 2 — Scaffold

| Item | Value |
|------|-------|
| Scaffold used | **no** (authored from Theme 4 + Theme 8 method; `/create-skill` unused) |

## 3 — Toolbelt reinforce

### `implementation-plan-verify`

- [x] `name` == folder
- [x] Pushy description (what + when + keywords); not Debug/PR
- [x] No `disable-model-invocation` (discoverable companion)
- [x] Body lean; checklist in `references/` with read-when gate
- [x] &lt;500 lines
- [x] Announce Using …
- [x] Compose: handoffs to `implementation-plan` / execute / execute-verify

### `implementation-execute-verify`

- [x] `name` == folder
- [x] Pushy description
- [x] No `disable-model-invocation`
- [x] Body lean; checklist + review-dimensions + converge-light refs
- [x] &lt;500 lines
- [x] Announce Using …
- [x] Compose: orchestrated from Execute/-subagents; does not replace N=2

## 4 — Compose map

| Step | Skill | Action |
|------|-------|--------|
| Write plan | `implementation-plan` | invoke |
| Validate plan | `implementation-plan-verify` | invoke |
| Execute loop | `implementation-execute` / `-subagents` | invoke |
| Post-green / EOP | `implementation-execute-verify` | invoke |
| Design gate | `design-process` | link only |

## 5 — Verify

- [x] Paths relative under `skills/`
- [x] `sync-toolbelt-local-plugin.py` (re-run after reinforce)
- [ ] Operator: Reload Window + Customize shows both skills
- [x] Human accepted Theme 8 method before SoT treat

## Process debt (corrected)

First elevation wrote skills **without** invoking `author-cursor-surfaces`. Correct path for Toolbelt surface elevation: Theme accept → **`/author-cursor-surfaces`** (or explicit ask) → reinforce → sync. This note closes the reinforce gap.
