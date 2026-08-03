---
title: "T16A — Local baseline (host standards gap)"
status: draft
theme: theme-16-host-standards
track: T16A
created: 2026-08-02
---

# T16A — Local baseline

## Method

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools | Local skills/templates/reports |
| Depth | normal |

## Findings

- `FACT` [E0] `author-agents-md` authors portable `AGENTS.md` (skeleton includes “Code conventions”); layer docs distinguish AGENTS vs rules vs ADRs. [E0: `skills/author-agents-md/SKILL.md`, `docs/templates/agents-md-skeleton.md`]
- `FACT` [E0] Design/plan carry constraints and Done-when; closeout (`implementation-closeout`) is readiness profile + check; ceremony out. [E0: Themes 5–6/15]
- `FACT` [E0] No dedicated `author-standards` / principles-profile skill yet. [E0: skills list]
- `INFERENCE` [E4] Gap: feedstock for **principles + checkable standards** that Plan/Execute/Closeout bind to, without conflating with AGENTS.md dump or Theme 15 closeout gate. Premises: above.
- `OPEN` Whether principles live in AGENTS.md, separate PRINCIPLES.md, or standards profile set — T16K/E.
