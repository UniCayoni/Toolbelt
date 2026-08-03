---
title: "Theme 19 — Standards application router (research campaign brief)"
status: accepted
theme: theme-19-standards-apply
created: 2026-08-03
updated: 2026-08-03
accepted: 2026-08-03
accepted_by: human (Jonathan)
authors: [scope-agent]
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-16-host-standards.md
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-18-recon-history.md
supersedes: null
amends:
  - docs/research/reports/theme-16-host-standards.md  # D10 bind + D12 always-on fence may be revisited after accept
---

# Research campaign brief — Theme 19 Standards application

**Using `research-scope`**. Companion only — does not replace `research-protocol`.  
**Draft ≠ law** until human accepts scope / later report / elevate.

## Header

```text
Title / idea: Standards *application process* for Toolbelt — thin ambient gate +
  small standards-router that points agents/chats/subagents at relevant host
  standard *modules* by action / wording / skill / perceived intent — so full
  standards corpora are NOT dumped into every context. Reuse Theme 16 feedstock
  (profiles, types, draft≠SoT, derive). Not writing host standards content.
  Later: same apply pattern may expand to other routers; this theme = standards only.
Complexity: theme/campaign (deep expected after normal baseline + lean)
Host note path: docs/research/notes/theme-19-standards-apply/
Date: 2026-08-03
Scoped by: agent (session)
Enough-to-start (agent propose): yes — after human accepts this brief
Human accept scope: accepted 2026-08-03
O1 lean: accepted 2026-08-03
Depth stop lean: diminishing_returns_plus_2 (authorized with lean)
```

## Working vocabulary (session lean — lock with scope accept)

| Term | Means | Not |
|------|--------|-----|
| **Apply / resolve** | Select which accepted host standard modules to load for this turn/task | Authoring rule text; merge ceremony |
| **Standards-router** | Small classify → **pointers** to modules (compose-only) | Pocket meta-router; method SoT for coding style |
| **Module** | Scoped host standards artifact (paths/pocket/type) | One mega-file required; Toolbelt-universal law |
| **Catalog / index** | Map action/skill/path → modules | Full rule dump in always-on rule |
| **Ambient gate** | Thin always-on (or intelligent) rule: if present+accepted → resolve; else no-op | Embedding full standards in alwaysApply body |
| **Selective load** | Agent loads only pointed modules into working context | Stuffing entire standards set every message |
| **Feedstock** | Theme 16 profiles / types / conflict lean / derive+S12b | This theme’s deliverable |

## Expand (short)

```text
- Fence: application process + surfaces; do NOT author Toolbelt-universal standards content
- Reuse Theme 16: host-owned profiles, accepted-only, AGENTS thin pointer, Plan/Execute/Closeout bind as baseline
- Candidate model (session): ambient if-present gate → standards-router → module pointers → selective load
- Compare external systems: how plugins/repos route or progressively disclose coding standards / AGENTS / rules / packs
- Channels: Alexandria RAG + GitHub (skills/rules/AGENTS/STANDARDS patterns) + primary docs (Cursor rules/skills, peers)
- Decide later (after research): amend D12? new skill vs author-standards mode? catalog schema? wire to pocket routers (P1)
- Parks this theme: writing actual Toolbelt host standards; global meta-router; expanding apply pattern to debug/impl routers beyond design hooks
- Smoke later: router classifies without pasting full modules; empty/absent = no-op
```

## Explicit non-goals

- Shipping a Toolbelt coding style guide as law  
- Writing the host’s concrete S1…Sn rules in this theme (except tiny smoke fixtures if needed)  
- Global meta-router across all pockets  
- Auto-promote draft/proposed standards  
- Phase 2 CI/Bugbot as standards apply  
- Dual-era profile schema v2 as primary deliverable (may note hooks only)

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T19A | Local baseline | What does Theme 16 bind + Toolbelt routers/rules actually do today for standards apply? Gaps vs selective-load intent? | skills/rules/templates/packs; Theme 14/16/17/18 reports | Elevating yet | P0 | normal | recon + protocol |
| T19B | Problem / success | What failure modes does mega-context / soft-only bind cause; what does “good apply” look like for agents/subagents? | Agent context budgets; draft≠SoT; compose-only | Host style aesthetics | P0 | normal | protocol |
| T19C | Router contract | What must a standards-router classify on (action, wording, skill id, path, intent)? Handoff fields? Intelligent skip? | Mirror impl/debug-router family | Global meta-router | P0 | normal→deep | protocol + docs |
| T19D | Catalog / modules | How should host standards be split + indexed so routers point without dumping all rules? | Index schema; module frontmatter; path/pocket/type | Mandating Google-style encyclopedia | P0 | normal→deep | protocol + gh |
| T19E | Ambient gate | How do always-on / intelligent rules load progressive disclosure elsewhere? Empty/absent no-op patterns? Cursor rule limits? | Cursor rules/skills docs; Toolbelt always-on culture; D12 amend options | Fat always-on rule bodies | P0 | deep | docs + protocol |
| T19F | External apply patterns (RAG) | How do SE / agent / standards guides describe progressive disclosure, context routing, or “load relevant conventions”? | Alexandria `software_engineering`, `ai_llm_agents` | Inventing Toolbelt law from E2 alone | P0 | deep | protocol (RAG) |
| T19G | External apply patterns (GitHub) | How do repos/plugins structure STANDARDS / AGENTS / `.cursor/rules` / skill packs so agents load *slices*? Routing or index patterns? | Public repos + Cursor plugin packs; sampling not one SoT | Copying one org guide as Toolbelt law | P0 | deep | gh + docs |
| T19H | Subagent / Task load | How should parent vs subagent receive module pointers (handoff fields vs re-resolve)? | Task/subagent patterns; Theme 14 handoffs | Plugin `agents/` Task types (Theme 4 GAP) | P1 | normal→deep | protocol + docs |
| T19I | Shape options / lean | Skill `standards-router` vs `author-standards` mode `resolve`? Rule id? Catalog template? Amend D10/D12? | Options matrix + recommendation | Immediate elevate without accept | P0 | normal | integrator |
| T19J | Wire / expand later | Where would pocket routers grow `if present` standards resolve *after* this theme? | Design hooks only; happy-path note | Implementing debug/impl apply expansion this theme | P1 | normal | integrator |
| T19K | Smoke plan | Claim card: classify→pointers; no full dump; absent no-op; refuse Toolbelt-universal law | Theme 11 pattern | Phase D harness | P0 | normal | Theme 11 |

## Comparator discovery (after accept)

| Channel | Use for |
|---------|---------|
| Alexandria RAG | Progressive disclosure, coding standards for agents, context/routing, AGENTS/convention load patterns |
| GitHub | Multi-file STANDARDS/AGENTS; `.cursor/rules` globs; skill-pack “when to read”; index/README routers |
| Web / primary | Cursor rules/skills docs; Claude memory/AGENTS; Codex AGENTS; peer plugin manifests |
| Local E0 | Toolbelt Theme 16 surfaces + pocket routers as baseline |

## Recommended gather order (after accept)

1. **Normal:** T19A–B–C–D (light) + T19I lean draft  
2. **Human lean** on shape (router skill vs mode; ambient gate yes/no)  
3. **Deep:** T19E–G (+ F RAG, G gh) then residual T19H; stop under agreed rule  
4. Draft Theme 19 report → accept → elevate apply surfaces (not standards content)  
5. **Later theme:** expand same apply pattern to other routers (T19J)

Do **not** auto-launch deep fleets from this brief alone.

## Enough? / stop

```text
Agent enough-to-start?: yes — after human accepts scope (+ optional depth stop_rule)
Open GAPs before gather:
  - Exact skill id (standards-router vs author-standards resolve) — OPEN until T19I
  - Whether D12 amend is in-scope for elevate — OPEN until lean
  - Catalog path convention — OPEN until T19D/I
Human gate: accept | revise | defer this brief before gather
```

## After accept

Normal wave notes → shape lean → human accept lean → deep T19E–G (RAG+GitHub+primary) under stop rule → integrate report → human accept → elevate via `/author-cursor-surfaces` (apply process only) → smoke → **stop for review before commit/push**.
