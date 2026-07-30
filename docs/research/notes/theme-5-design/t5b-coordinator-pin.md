---
title: "T5B coordinator pin — Technical design"
status: draft
theme: theme-5-design
track: T5B
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
waves: [pin]
campaign_phase: t5b_synthesis_done
stop_reason: low_return_plus_one
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5a-track-synthesis.md
supersedes: null
---

# T5B coordinator pin

**Using `research-protocol`** · depth: **deep** · after T5A spine synthesis.

## 1. Scope

| Field | Value |
|-------|-------|
| Question | How to design code architecture, features, stacks, services/apps, coding/clean standards (design-time), including with agents? |
| In | Architecture styles/tradeoffs, modular boundaries, stack *criteria*, services/desktop as design concerns, clean/standards as constraints |
| Out | Lint catalogs as product; grey-matter stack locks; Theme 1 recon-only; T5C UX; Design skill elevation |
| Reuse | T5A design-before-implement spine + ADR triggers; do not re-litigate ADR existence |

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep |
| Subagents | `cursor-grok-4.5-high-fast` |
| Corpora | `software_engineering` (primary); `programming_algorithms_systems` secondary only |
| Stop | low-return → +1 residual → `low_return_plus_one` |
| Note root | `docs/research/notes/theme-5-design/` |

## 3. Gatherer slices

| ID | Slice |
|----|-------|
| T5B-S1 | Architecture styles + modularity / dependency criteria |
| T5B-S2 | Stack/feature/service criteria + ADR when-to-decide |
| T5B-S3 | Contested clean/standards (both sides) + agent-assisted technical design |

## 4. Progress

| Wave | Status |
|------|--------|
| Pin | done |
| W1–W3 | done |
| Track synthesis | done — `t5b-track-synthesis.md` |
| stop_reason | `low_return_plus_one` |
