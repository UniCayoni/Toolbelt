---
title: "T16H/I — Lifecycle & brownfield derive (normal)"
status: draft
theme: theme-16-host-standards
tracks: [T16H, T16I]
created: 2026-08-02
---

# T16H/I — Lifecycle & brownfield

## Findings

- `CLAIM` [E3] Extract conventions from existing code systematically; document what *is*; majority vs conflict boundaries (legacy vs rewrite); evidence file:line. [E3: rulesync / AI Tools Guidebook convention detection — discovery]
- `CLAIM` [E3] Prefer config files (eslint/prettier) as high-confidence; AST/stats for implicit patterns; confidence scores. [E3: code-standards-analyzer / detective skills — discovery]
- `CLAIM` [E2] Framework guidelines evolve (editions, obsolete appendix) — standards are living. [E2: Alexandria FDG foreword/obsolete appendix mentions]
- `INFERENCE` [E4] Toolbelt brownfield method lean: `research-codebase-recon` sample + **git history/recency** signals + conflict log → **proposed** standards/principles → human accept; never silent SoT. Premises: campaign intent; draft≠SoT; E3 extract literature.
- `INFERENCE` [E4] Greenfield: principles first (tone/core), then thin standards; mid-project: derive candidates then reconcile with principles/design.
- `GAP` Exact git-history recipe (churn windows, blame) not pinned — deep or design.
- `OPEN` Automation of extract vs human-led recon checklist.
