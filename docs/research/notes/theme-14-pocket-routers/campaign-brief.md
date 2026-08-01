---
title: "Theme 14 — Pocket routers (research campaign brief)"
status: accepted
theme: theme-14-pocket-routers
created: 2026-07-31
updated: 2026-07-31
authors: [scope-agent]
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-10-happy-path.md
supersedes: null
---

# Research campaign brief — Theme 14 Pocket routers

Authority: Theme 12 accepted. Used by skill **`research-scope`**.  
Companion only — does **not** replace `research-protocol` notes/grades.  
**Draft ≠ law** until human accepts scope / later report.

## Header

```text
Title / idea: Pocket routers — per-pocket compose-only entry skills that classify
  an ask and wire leaf skills; happy-path becomes a thin chain of routers
  (optional full ladder). Naming lean: "router" over "guide".
Complexity: theme/campaign
Host note path: docs/research/notes/theme-14-pocket-routers/
Date: 2026-07-31
Scoped by: agent (session ask: scope + comparator gather)
Enough-to-start (agent propose): yes — tracks clear; risks named; existing
  Toolbelt analogues (research-scope, design-process, happy-path) bound E0.
Human accept scope: accepted 2026-07-31 (O1 quality bundle)
Gather status: T14A–E notes + integrated report accepted; elevated
```

## Expand (short)

What must be true / looked up / decided before / during gather?

```text
- Pocket router ≠ leaf method SoT; compose-only (Theme 10 D8 analogue)
- Risks: duplication with research-scope/design-process; skill sprawl; order drift vs happy-path
- Look up: how agent skill packs / workflows express stage routing & dynamic stages
- Look up: GitHub Docs patterns for reusable/composable workflows (analog only — not import as Toolbelt law)
- Look up: RAG + web on agentic pipelines, routers, orchestrator vs specialist
- Decide later (design, not this scope): which pockets get new routers vs reuse entry skills; naming prefix
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T14A | Local baseline | What entry/router surfaces does Toolbelt already have, and what gap does Theme 10 leave? | Happy-path, research-scope, design-process, Handoffs; packs | Elevating routers | P0 | normal | `research-codebase-recon` + short protocol note |
| T14B | Skill-pack comparators | How do Cursor/agent skill repos structure orchestrator vs specialist vs stage routing? | Superpowers, agentskills.io patterns, Continue/Aider-ish if routing surfaces exist | Importing their git/PR packaging as law | P0 | normal | `research-protocol` (+ web/gh) |
| T14C | GitHub workflow analogies | What does GitHub document for reusable, composable, callable workflows / dynamic jobs that maps (loosely) to pocket routers + happy-path? | GitHub Docs Actions: reusable workflows, workflow_call, matrix, concurrency | Making Toolbelt depend on Actions | P1 | normal | `research-docs` / protocol |
| T14D | Agentic dynamic stages | What literature/practice exists for dynamic stage handling, routers, planner–executor, state machines in agent systems? | RAG `ai_llm_agents` + `software_engineering`; primary/secondary web | Locking a framework stack | P0 | normal→deep if thin | Alexandria + protocol |
| T14E | Shape options for Toolbelt | Given A–D, what router-pocket shapes fit Toolbelt ideals (compose-only, multi-entry, draft≠SoT)? | Options matrix + risks; parks | Authoring skills before accept | P0 | normal | integrator after A–D |

## Enough? / stop

```text
Agent enough-to-start?: yes
Open GAPs / OPENs before gather:
  - Exact theme id / skill naming (`*-router` vs pocket umbrella) — OPEN until design
  - Whether "router" is its own packs row vs implementation umbrella — OPEN
stop_reason (if stopping scope without gather): n/a — gather authorized this session
Human gate: accept | revise | defer  ← reply with one
```

## After accept

Hand off per track; do not auto-launch unbounded deep fleets.  
Integrator merges into draft Theme 14 report; elevation only after human accept.

## Working vocabulary (session lean — not locked)

| Term | Means | Not |
|------|--------|-----|
| **Router** | Pocket-level classify + wire leaf skills | Method SoT; always-on rule |
| **Leaf** | Skill that owns pocket law | Happy-path |
| **Happy-path** | Optional chain of routers (end-to-end) | Only entry mode |
| **Router pocket** | Product concept: routers as first-class compose surfaces | New always-apply rules |
