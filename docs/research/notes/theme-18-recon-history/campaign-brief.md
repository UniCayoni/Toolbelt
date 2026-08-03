---
title: "Theme 18 — Recon git/history wire (research campaign brief)"
status: accepted
theme: theme-18-recon-history
created: 2026-08-03
updated: 2026-08-03
accepted: 2026-08-03
accepted_by: human (Jonathan)
authors: [scope-agent]
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-16-host-standards.md
  - docs/research/notes/theme-16-host-standards/deep-t16h-i-brownfield-git.md
  - docs/research/notes/theme-16-host-standards/deep-t16i-git-era-primary.md
supersedes: null
amends:
  - docs/research/reports/theme-16-host-standards.md  # §4 “no Toolbelt numeric law” → Toolbelt default 12m + host override
---

# Research campaign brief — Theme 18 Recon git/history wire

**Using `research-scope`**. Companion only — does not replace `research-protocol`.  
**Draft ≠ law** until human accepts scope / lean / later elevate.

## Header

```text
Title / idea: Wire git/history + conflict-tiebreak into research-codebase-recon
  (and tighten author-standards derive glue) so brownfield D9 has recon feedstock.
Complexity: thin product follow-up (Theme 16 method already accepted; no deep gather)
Host note path: docs/research/notes/theme-18-recon-history/
Date: 2026-08-03
Scoped by: agent (session)
Enough-to-start (agent propose): yes — Theme 16 D9 + deep T16H/I recipe + session lean
Human accept scope: accepted 2026-08-03
Lean locks (window + conflict tiebreak): accepted 2026-08-03
```

## Working vocabulary (session lean)

| Term | Means | Not |
|------|--------|-----|
| **Recency window** | Default **12 months**; host may override with absolute date, months, or years | Industry SoT; mandatory whole-repo scan limit |
| **Conflict tiebreak** | When patterns conflict → prefer **most recent non-one-off** as default *candidate* | Silent SoT; auto-promote |
| **One-off** | Singleton / isolated / contradicts config SoT / outside hot paths — demote | Hard statistical majority law |
| **Hot-path support** | Light churn map to support one-off + quarantine | Primary selector for “which style wins” |
| **History step** | Conditional recon collection of window + conflict log + evidence | Always-on fat recon; CI ceremony |

## Proposed lean locks (accept to proceed)

| # | Lean |
|---|------|
| L1 | **Window:** default **12 months**; host override (date / months / years) — Toolbelt method default, not claimed industry law |
| L2 | **Conflict primary:** on conflicting approaches → most recent **non-one-off** is the default propose candidate |
| L3 | **One-off heuristics:** singleton path/commit; contradicts lint/format config; not repeated in hot paths — label exception, do not auto-win |
| L4 | **Hot-path:** light optional churn support only (quarantine / one-off aid), not the main selector |
| L5 | **When:** history step **conditional** — `author-standards` derive / brownfield / era conflict / user asks |
| L6 | **Fence:** cite-or-omit; emit **proposed** only; no auto-promote; CLI churn one-liners = examples not mandatory procedure |
| L7 | **ignore-revs:** if `.git-blame-ignore-revs` present, use when blaming (formatter noise ≠ culture) |
| L8 | **Surfaces:** extend recon template + skill checklist; tighten `author-standards` derive to expect those fields; smoke 2/2 |
| L9 | **Parks:** closeout rename; dual-era full profile schema; hard N-exemplar thresholds; Phase 2 CI; always-on standards rule |

## Expand (short)

```text
- Amend Theme 16 §4 GAP row: “no Toolbelt numeric law” → default 12m + host override (method)
- No new deep gather unless baseline finds blocking ambiguity
- Prefer configs first; git/history for conflict/era, not inventing style from fossils
- Elevate via author-cursor-surfaces (or thin direct edit if recon-only — prefer author skill)
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T18A | Local baseline | Exact recon S-step placement + derive checklist gaps | recon skill/template/checklist; author-standards derive | Closeout rename | P0 | normal | recon + protocol |
| T18B | Shape | Conditional history section fields (window, conflict log, evidence) | template + skill refs | Dual-era profile schema v2 | P0 | normal | integrator |
| T18C | Wire | author-standards derive points at history fields | derive mode + checklist | New skill | P0 | normal | author-cursor-surfaces |
| T18D | Smoke | Claim card: conditional history + conflict tiebreak language | in-session + fresh | Phase D harness | P0 | normal | Theme 11 pattern |

## Enough? / stop

```text
Agent enough-to-start?: yes — after human accepts scope + L1–L9
Open GAPs before wire: none blocking (L1–L9 close session OPENs)
Human gate: accept this brief (scope + leans) before elevate
```

## After accept

Short T18A baseline note (optional if E0 inline) → shape/wire via `/author-cursor-surfaces` → smoke → amend Theme 16 report GAP row → sync + push.
