---
title: "Theme 14 — Pocket routers (integrated report)"
status: accepted
theme: theme-14-pocket-routers
created: 2026-07-31
updated: 2026-07-31
accepted: 2026-07-31
acceptance_scope: method_guidance_t14_pocket_routers
accepted_by: human (Jonathan)
authors: [integrator]
depth: normal
stop_reason: human_accepted_o1_bundle
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
  - docs/research/notes/theme-14-pocket-routers/t14a-local-baseline.md
  - docs/research/notes/theme-14-pocket-routers/t14b-skill-pack-comparators.md
  - docs/research/notes/theme-14-pocket-routers/t14c-github-workflow-analogy.md
  - docs/research/notes/theme-14-pocket-routers/t14d-agentic-dynamic-stages.md
  - docs/research/notes/theme-14-pocket-routers/t14e-shape-options-lean.md
  - docs/research/reports/theme-10-happy-path.md
supersedes: null
amends:
  - docs/research/reports/theme-10-happy-path.md  # composition: happy-path chains pocket routers
---

# Theme 14 — Pocket routers

**Status:** **accepted** (method guidance) — 2026-07-31.  
**Elevated:** `implementation-router` + `docs/templates/implementation-router.md`; happy-path thinned to chain pocket entries; packs **Routers / pocket entry** row.  
**Depth:** normal gather (T14A–E); no deep fleet.

**Using `research-protocol`** · integrator.

### Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-14-pocket-routers`**; vocabulary **router** (not guide) |
| D2 | Shape **O1** — new `implementation-router`; keep `research-scope` + `design-process` as de-facto pocket routers (document; no rename this theme) |
| D3 | Packs: first-class row **Routers / pocket entry**; Happy-path = chains routers |
| D4 | Defer **`debug-router`** *(superseded by Theme 17 — shipped)* |
| D5 | Implementation router = **pure select/wire** among fixed leaves (not a planner/decomposer) |
| D6 | **Park** global always-on / meta `skill-router` |
| D7 | Happy-path remains compose-only (Theme 10 D8); workers = one pocket; no always-on rule |
| D8 | Structured handoff fields on routers (goal, prior, facts+source, open question, constraints) — checklist, not always-apply rule |

---

## 1. Executive summary

Theme 10 shipped a thin end-to-end ladder. Pocket-local wiring stayed in Handoffs, which under-served Implementation’s multi-leaf fan-out. Theme 14 adds a **router layer**: pocket-level classify + wire; happy-path becomes an optional **caller** of those routers. Aligns with Toolbelt modularity, Anthropic-style routing workflows, and GitHub reusable-workflow nesting (analogy only).

---

## 2. Sources

Campaign brief + T14A–E notes under `docs/research/notes/theme-14-pocket-routers/`; Theme 10 accepted report; Alexandria `ai_llm_agents`; GitHub Docs reusable workflows; Superpowers / community skill-router samples (E3 where noted in track notes).

---

## 3. Layer model (accepted)

```text
Leaf skills     → own pocket method law
Pocket router   → classify + wire leaves (compose-only); selection ≠ solving
Happy-path      → optional chain of pocket routers / de-facto entries
Loose use       → leaf or pocket router directly
```

| Pocket | Router / entry (this elevate) |
|--------|-------------------------------|
| Research | `research-scope` (de facto; Theme 12) |
| Design | `design-process` (de facto; Theme 5) |
| Implementation | **`implementation-router`** (new) |
| Debug | **`debug-router`** (Theme 17) |
| Cross-pocket | `implementation-happy-path` |

---

## 4. Elevation status

| Surface | Status |
|---------|--------|
| `implementation-router` | **Shipped** |
| `docs/templates/implementation-router.md` | **Shipped** |
| Happy-path thin rewire | **Shipped** |
| Packs Routers row | **Shipped** |
| `debug-router` | **Shipped** (Theme 17) |
| Global skill-router | **Parked** |
| Rename scope/process → `*-router` | **Parked** (optional later) |

---

## 5. Acceptance checklist

- [x] Human accepted scope + O1 quality bundle — 2026-07-31  
- [x] Integrated report accepted  
- [x] Elevate `implementation-router` + thin happy-path + packs/README/CHANGELOG  
- [x] In-session E0 smokes I1 + H1 — **2/2 PASS**  
- [x] Fresh-chat smokes I1 + H1 — **2/2 PASS** (`I1-fresh-20260731.md`, `H1-fresh-20260731.md`; delta note)  
- [x] Operator: Reload + skills loaded (reported 2026-07-31)  


---
