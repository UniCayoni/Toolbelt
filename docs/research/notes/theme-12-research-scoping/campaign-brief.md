---
title: "Theme 12 — Research scoping compose brief"
status: accepted
theme: theme-12-research-scoping
created: 2026-07-31
updated: 2026-07-31
accepted: 2026-07-31
accepted_by: human (Jonathan)
authors: [coordinator]
depth: normal
campaign_phase: elevated
aligned_with:
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
  - docs/research/notes/theme-12-research-scoping/scope-normal-pass1.md
  - docs/research/reports/theme-10-happy-path.md
  - skills/research-protocol/SKILL.md
supersedes: null
---

# Theme 12 — Research scoping: compose brief

**Using `research-protocol`**; depth: **normal compose** (no deep gatherer fleet).

**Status:** **accepted** 2026-07-31 — elevated. SoT report: `docs/research/reports/theme-12-research-scoping.md`.  
**Authority for decisions:** [`scope-normal-pass1.md`](./scope-normal-pass1.md) §7.1 (O3 = B+C companion).

**Intent:** Companion skill **`research-scope`** — expand/atomize into tracks and gate enough-to-start without changing `research-protocol`’s job.

---

## 1. Locked product decisions (summary)

| # | Lock |
|---|------|
| D1 | Theme id **`theme-12-research-scoping`** |
| D2 | Scope = scoping / atomize / tracks / enough **only** |
| D3 | Surfaces = companion skill **`research-scope`** + template(s) (**B+C**). Protocol/recon/docs = **Handoffs only** |
| D4 | Use when **appropriate** (complex / theme/campaign / user asks expand-first) — not mandatory on every research call; composable in other orders |
| D5 | **Complexity ≠ depth** (two axes) |
| D6 | Enough = **agent proposes + human accepts** |
| D7 | Happy-path = **one Handoff** to `research-scope` when expand-first fits; keep Theme 10 D3 as-needed preface |
| D8 | **Normal compose** elevation; Theme 12 report as addendum SoT |
| D9 | Parks: no S0–S18/D0–D14 rewrite; no always-on rule; no mega-skill; **no** scoping spine inside `research-protocol` |

---

## 2. Glossary (G2)

| Term | Meaning | Not |
|------|---------|-----|
| **Concept atom** | A researchable piece of a fuzzy idea (becomes a **track** or sub-question) | T3 D11 greppable path/API |
| **Checkable doc atom** | Theme 3 D11 extract (symbol, CLI, route, …) for docs↔code verify | Campaign track |
| **Complexity** | Simple (one surface / clear question) vs Complex (multi-surface / tracks unclear) | Depth mode |
| **Depth** | `normal` vs `deep` (owned by `research-protocol` / depth-modes) | Complexity |
| **Track** | Named in/out research slice | Pack or Cursor skill |
| **Enough?** | Agent stop + residual GAP/OPEN list; **human** accepts before design locks | Silent “looks done” |

---

## 3. Skill identity — `research-scope`

| Field | Value |
|-------|-------|
| Name | **`research-scope`** |
| Role | Companion: expand concept → atomize → track board → propose depth per track → enough?/human gate |
| Not | Note writing, cite-or-omit enforcement, deep wave dispatch, recon checklist, docs D0–D14 |
| After scope | Hand off to `codebase-recon` / `docs-research` / `research-protocol` (and deep waves) as needed |
| Composability | Controllers/users may invoke before research, between waves, or from other pockets — order not owned solely by happy-path |

### 3.1 Candidate spine (skill body)

```text
0  Announce Using research-scope
1  Classify: simple | complex | theme/campaign | user-forced scope
2  If simple and user did not ask to scope → recommend skip; point to research-protocol / recon / docs
3  Expand — what must be true / looked up / decided? (short bullets)
4  Atomize — concept atoms → tracks (name, question, in/out, priority)
5  Suggest depth per track — normal | deep (default normal); do not auto-launch fleets
6  Write campaign brief / checklist from template
7  Enough-to-start? — agent proposes; human accepts before treating scope as ready for gather
8  Handoff — list next skills per track (protocol / recon / docs-research); stop
```

**Anti-patterns:** Becoming a second research-protocol; auto-deep fleets; mandatory on every lookup; pasting S0–S18/D0–D14; owning design; conflating concept atoms with D11 checkable atoms.

---

## 4. Artifacts to ship (elevate checklist)

| Artifact | Action |
|----------|--------|
| `skills/research-scope/SKILL.md` | **New** companion skill (spine §3.1) |
| `skills/research-scope/references/` | Optional thin checklist copy |
| `docs/templates/research-campaign-brief.md` | **New** — tracks, complexity, depth suggestion, enough?/human gate |
| `skills/research-protocol/SKILL.md` | **Handoff only** — complex/theme/unclear → consider `research-scope` first |
| `docs/templates/research-depth-modes.md` (+ sync references) | **Pointer** — track invent / expand-first → `research-scope` |
| `skills/implementation-happy-path/SKILL.md` | **Handoff** — when expand-first appropriate → `research-scope` then research skills |
| `docs/templates/happy-path.md` (+ checklist copy) | Matching one-liner |
| `docs/packs/README.md` | List `research-scope` under Research pack |
| `docs/research/reports/theme-12-research-scoping.md` | Accepted report after elevate |
| `codebase-recon` / `docs-research` | Optional Handoff only — **no** spine rewrite |

---

## 5. Out of scope (this compose)

- Deep literature on question decomposition  
- Folding scoping steps into `research-protocol` body (superseded A+C)  
- Rewriting S0–S18 / D0–D14  
- Always-on rule  
- Forcing scope before every happy-path research preface  

---

## 6. Acceptance gate (human)

- [x] Companion **`research-scope`** (B+C) accepted  
- [x] Spine §3.1 elevated  
- [x] Theme 12 report accepted  

**Operator follow-up:** sync local plugin → Reload → optional `/research-scope` smoke.

---

## 7. Sources

1. [`scope-normal-pass1.md`](./scope-normal-pass1.md) (proposed decisions + O3 pivot)  
2. Theme 5 [`campaign-brief.md`](../theme-5-design/campaign-brief.md) (E0 track pattern)  
3. `docs/templates/research-depth-modes.md`  
4. `docs/research/reports/theme-10-happy-path.md`  
5. `skills/research-protocol/SKILL.md`  
