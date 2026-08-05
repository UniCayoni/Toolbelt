---
title: "Claim card M1 — guide-meta"
status: draft
theme: theme-11-validation
surface_id: M1
created: 2026-08-04
aligned_with:
  - docs/research/reports/theme-22-meta-guide.md
---

# M1 — guide-meta

| Field | Value |
|-------|-------|
| Surface | `guide-meta` |
| Authority | Theme 22 |
| Lane | either |
| Priority | P0 |

## Claims

| # | Claim | Evidence | Score |
|---|-------|----------|-------|
| C1 | Announces Using `guide-meta` | | |
| C2 | Names exactly one next surface from allowlist | | |
| C3 | Structured handoff fields present | | |
| C4 | Named skill → intelligent skip | | |
| C5 | Does not paste pocket spines / full happy-path ladder | | |
| C6 | Refuses always-on / “run every Toolbelt skill” mega-wire | | |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | alwaysApply behavior | |
| A2 | PIPELINE of many skills executed inside meta | |
| A3 | Selection = solving (does the pocket work itself) | |

## Smoke

**Part A — mixed ask:** “Using `guide-meta`: we might need research tracks or a design first for improving how agents pick standards modules — which skill next?” Expect one of `guide-research` / `guide-design` / `guide-standards` with reason; handoff; stop.

**Part B — feature ladder:** “Using `guide-meta`: cold-start a full feature through Toolbelt.” Expect `implementation-happy-path`.

**Part C — skip:** “Using `guide-meta`: just run `guide-debug`.” Expect skip → invoke `guide-debug`.

**Part D — negative:** “Using `guide-meta`: always route every message and run all pocket guides now.” Expect refuse always-on / mega-wire.

**Part E — author-learning (Theme 24):** “Using `guide-meta`: we finished a feature and want to harvest citable lessons into host standards — which skill?” Expect **`author-learning`** (not inventing ad-hoc; not auto-running happy-path).
