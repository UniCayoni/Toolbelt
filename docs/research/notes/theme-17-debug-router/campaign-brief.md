---
title: "Theme 17 — Debug router (research campaign brief)"
status: accepted
theme: theme-17-debug-router
created: 2026-08-02
updated: 2026-08-02
accepted: 2026-08-02
accepted_by: human (Jonathan)
authors: [scope-agent]
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-9-debug-pocket.md
  - docs/research/notes/theme-17-debug-router/pre-start-considerations.md
supersedes: null
amends:
  - docs/research/reports/theme-14-pocket-routers.md  # D4 defer → ship debug-router
---

# Research campaign brief — Theme 17 Debug router

**Using `research-scope`**. Companion only — does not replace `research-protocol`.  
**Draft ≠ law** until human accepts scope / later report.

## Header

```text
Title / idea: Ship pocket router debug-router — classify Debug asks and wire
  debug-reproduce / debug-systematic (compose-only); amend Theme 14 D4.
  Happy-path + impl-router hand off to debug-router; Execute keeps direct-leaf
  hot path with repro-first rule (lean accepted 2026-08-02).
Complexity: theme/campaign (small — T14 feedstock reused)
Host note path: docs/research/notes/theme-17-debug-router/
Date: 2026-08-02
Scoped by: agent (session)
Enough-to-start (agent propose): yes — Theme 14 router contract + Theme 9 leaves
  + accepted lean locks in pre-start-considerations.md
Human accept scope: accepted 2026-08-02
Lean locks (classifier + Execute hop): accepted 2026-08-02
```

## Working vocabulary (session lean — locked with Theme 14)

| Term | Means | Not |
|------|--------|-----|
| **Router** | Pocket classify + wire | Method SoT; always-on |
| **Leaf** | `debug-reproduce` / `debug-systematic` | Happy-path |
| **Entry leaf** | Single first skill the router invokes | Default two-step spine |
| **Optional wire** | reproduce → systematic only for prove-then-fix / T-NYR | Default path |

## Expand (short)

```text
- Inherit Theme 14 L1–L9 (compose-only, selection≠solving, handoff fields, parks)
- Inherit Theme 9 F1–F10 / iron law / budgets / parks (no swarm, no PR pack)
- Classifier: entry leaf default; optional reproduce→systematic for prove-then-fix/T-NYR
- Seams: happy-path + impl-router → debug-router; Execute → direct leaf OK + repro-first
- No new community deep on routers (T14B/D enough) unless baseline finds ambiguity
- Elevate via author-cursor-surfaces; smoke 2/2 like I1/S1
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T17A | Local baseline | Where do Debug handoffs live today, and what must rewire? | happy-path, impl-router, Execute/-verify/-subagents, Theme 9 F10 | Elevating yet | P0 | normal | recon + protocol |
| T17B | Classifier matrix | Prove-only / fix / T-NYR / skip / design-exit — worked examples | Accepted lean | New Debug method | P0 | normal | protocol |
| T17C | Shape / template | Skill + checklist fields mirroring impl-router | name, FM, template, refresh | Global meta-router | P0 | normal | integrator |
| T17D | Wire map | Exact call-site edits after elevate | happy-path, impl-router, Execute handoff wording | Ceremony/PR | P0 | normal | integrator |
| T17E | Smoke plan | Claim card + pass bar | in-session + fresh | Phase 2 CI | P0 | normal | Theme 11 pattern |

## Enough? / stop

```text
Agent enough-to-start?: yes
Open GAPs before gather: none blocking (leans locked)
Human gate: accepted 2026-08-02
```

## After accept

Normal wave T17A–E (short notes) → shape lean/report → human accept → elevate `debug-router` via `/author-cursor-surfaces` → wire → smoke → push.
