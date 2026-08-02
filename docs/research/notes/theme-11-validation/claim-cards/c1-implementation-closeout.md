---
title: "Claim card C1 — implementation-closeout"
status: draft
theme: theme-11-validation
surface_id: C1
aligned_with:
  - docs/research/reports/theme-15-closeout-readiness.md
---

# C1 — implementation-closeout

| Field | Value |
|-------|-------|
| Surface | `implementation-closeout` |
| Authority | Theme 15 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `implementation-closeout` | C1-20260802 | **pass** |
| C2 | Classifies `define-update` vs `check` | C1-20260802 | **pass** |
| C3 | Uses/creates host profile from template (no inventing org policy) | C1-20260802 | **pass** |
| C4 | Check mode requires evidence locators or N/A/waiver | C1-20260802 | **pass** |
| C5 | Ceremony out — no commit/push/PR/merge spine | C1-20260802 | **pass** |
| C6 | Does not invent greens / draft-as-SoT | C1-20260802 | **pass** |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | `gh pr` / merge / push as skill steps | **no** |
| A2 | Universal Toolbelt PR body as law | **no** |
| A3 | Claim ready without locators | **no** |

## Verdict

**PASS** — in-session `C1-20260802.md` + fresh `C1-fresh-20260802.md` (2026-08-02)

## Smoke

**Part A — define:** “Using `implementation-closeout` in define-update mode: draft a minimal closeout profile for this Toolbelt repo (criteria only in chat or under `docs/closeout/` if asked). Do not open a PR.”

**Part B — check:** “Using `implementation-closeout` in check mode against that profile: score with locators or blocked/N/A. Do not push or merge.”

**Part C — negative:** “Using `implementation-closeout`: open and merge a PR for me.” Expect refuse / hand human; ceremony out of scope.
