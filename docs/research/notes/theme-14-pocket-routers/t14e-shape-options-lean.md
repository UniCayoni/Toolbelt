---
title: "T14E — Shape options lean (pocket routers)"
status: accepted
theme: theme-14-pocket-routers
track: T14E
created: 2026-07-31
updated: 2026-07-31
authors: [integrator-draft]
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
  - docs/research/notes/theme-14-pocket-routers/t14a-local-baseline.md
  - docs/research/notes/theme-14-pocket-routers/t14b-skill-pack-comparators.md
  - docs/research/notes/theme-14-pocket-routers/t14c-github-workflow-analogy.md
  - docs/research/notes/theme-14-pocket-routers/t14d-agentic-dynamic-stages.md
supersedes: null
---

# T14E — Shape options lean

**Status:** draft lean for human — **not** design law. Premises from T14A–D only; no new facts.

## Working map (inference)

```text
Leaf skills     = own pocket law (SoT)
Pocket router   = classify + wire leaves (+ structured handoff); compose-only
Happy-path      = caller that chains pocket routers (optional full ladder)
Loose use       = invoke leaf or pocket router directly
```

Analogies (not imports): GitHub `workflow_call` callee ≈ pocket router; top-level caller ≈ happy-path [T14C]. Anthropic routing workflow ≈ pocket router [T14D].

## Options

| ID | Shape | Pros | Cons / risks |
|----|--------|------|----------------|
| **O1** | New `*-router` skills for Implementation + Debug only; keep `research-scope` + `design-process` as de-facto routers; thin happy-path to call routers | Smallest delta; fills T14A gap; avoids rename churn | Naming inconsistency (`scope`/`process` vs `router`) |
| **O2** | Rename/normalize all pocket entries to `research-router`, `design-router`, … | Clean domain-first vocabulary | High churn; Theme 5/12 surface renames; smoke cost |
| **O3** | One global `skill-router` (craftwork/Superpowers-like) + keep happy-path | Max discoverability | Conflicts with intelligent-skip culture; sprawl; always-on pressure — **park lean** |
| **O4** | No new skills — thicken Handoffs + happy-path only | Zero skill count growth | Does **not** fix pocket-local discoverability (user pain) |

## Agent lean (quality-over-ease)

Prefer **O1** first:

1. **Do not** ship global always-on router (O3 park).
2. Treat `research-scope` + `design-process` as existing routers (document in packs; optional later rename = O2 phase-2).
3. Elevate **`implementation-router`** (and optionally **`debug-router`**) as compose-only: classify ask → which of plan / plan-verify / execute / -subagents / execute-verify (or reproduce / systematic).
4. Rework **`implementation-happy-path`** to chain pocket routers (and existing entries), not re-list every leaf — still compose-only (Theme 10 D8 preserved).
5. Router contract (from T14B/D): **selection not solving**; structured handoff fields; **explicit skips**; never restate leaf law.
6. Watch risks: duplication, order drift (single checklist SoT), skill sprawl (cap new routers to pockets that lack an entry).

## Parks

- CLA / fat CI coupling
- Framework lock (LangGraph etc.)
- Global meta-router as always-apply rule
- Importing Actions nesting limits as hard Toolbelt constants

## Human gate (this track)

**Accepted O1 lean** — 2026-07-31 (human). Elevated via Theme 14 report.
