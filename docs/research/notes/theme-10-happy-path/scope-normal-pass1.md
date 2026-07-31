---
title: "Theme 10 — Happy-path workflow normal scope (pass 1)"
status: draft
theme: theme-10-happy-path
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/packs/README.md
  - docs/research/reports/theme-4-cursor-plugin-components.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/research/reports/theme-9-debug-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 10 — Happy-path workflow: normal research pass 1

**Using `research-protocol`**; depth: **normal** (surface inventory + compose map — not a deep gatherer fleet).

**Status:** `draft`. Not workflow SoT.  
**Target name (human):** **`implementation-happy-path`**.  
**Identity:** Thin **orchestration** skill (+ optional checklist/template) that ties shipped Toolbelt pockets into one cold-start ladder for agents and subagent controllers. **Does not** re-own pocket law.

## 1. Scope

- Question: What existing surfaces form the Toolbelt happy path, how do handoffs already connect, what should `implementation-happy-path` own vs point to, and what’s enough to brief/elevate?
- In: Inventory of 18 skills + packs; handoff graph; skip paths; subagent controller vs worker; name collision; surface-shape options; gaps.
- Out: Elevating the skill this pass; PR/CI pack design; deep community hunt; inventing new pocket law.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Glob `skills/*/SKILL.md`; Grep Handoffs/Prefer; Read packs + author-cursor-surfaces compose guidance; Grep name collision |
| Corpora / URLs | Local Toolbelt only (E0) |
| Queries (exact) | `happy-path\|implementation-happy` under repo; Handoffs sections across skills |
| What was *not* searched | External “agent workflow skill” fleets; live E0 happy-path smoke on a host app |
| Depth | normal |
| stop_reason | Inventory + compose map + shape lean sufficient for human gate → brief/elevate; no deep fleet needed unless human wants community corroboration |

## 3. E0 — Pack & skill inventory

### 3.1 Packs (shipped)

| Pack | Skills (abbrev) | Authority |
|------|-----------------|-----------|
| Research | codebase-recon, docs-research, research-protocol, author-agents-md, draft-adr, author-cursor-surfaces | Themes 1–4 (+ ADR) |
| Design | design-process + technical / creative-* | Theme 5 |
| Plan | implementation-plan | Theme 6 |
| Execute | implementation-execute, -subagents | Theme 7 |
| Verify | implementation-plan-verify, implementation-execute-verify | Theme 8 |
| Debug | systematic-debug, reproduce-bug | Theme 9 |
| PR / workflow | stub | Phase 2 |

- `FACT` [E0] Packs list Debug shipped; PR stub separate; no happy-path pack/skill today. [E0: `docs/packs/README.md`]
- `FACT` [E0] Exactly **18** `skills/*/SKILL.md` present; none named `implementation-happy-path`. [E0: Glob 2026-07-30]
- `FACT` [E0] Repo grep finds **no** existing `happy-path` / `implementation-happy` surface. [E0: Grep 2026-07-30]

### 3.2 Theme 4 compose mandate (input)

- `FACT` [E0] `author-cursor-surfaces` compose mode: map outcome steps → existing skills; write an **orchestration** skill that invokes/links; **do not paste** large bodies. Prefer skill over always-on rule for multi-step work. [E0: `skills/author-cursor-surfaces/SKILL.md`]
- `INFERENCE` [E4] Happy-path is the natural Theme 4 compose outcome for the full ladder. Premises: compose mandate [E0]; pockets shipped through Theme 9 [E0].

## 4. Handoff graph (already implied)

Cold agents today must **discover** the ladder by reading many Handoffs tables. Pattern already encoded:

```text
[optional] codebase-recon / docs-research / research-protocol
        ↓
design-process → (technical-design | creative-*) → human gate
        ↓ optional draft-adr
implementation-plan
        ↓
implementation-plan-verify → Meta ready
        ↓
implementation-execute  OR  implementation-execute-subagents
        ↓
implementation-execute-verify (post-green + EOP converge)
        ↓ on fail / bug
systematic-debug  (or reproduce-bug prove-first)
        ↓
PR / CI  (Phase 2 — park)
```

Supporting side-doors (not main ladder): `author-agents-md`, `author-cursor-surfaces`, creative domain swaps, `draft-adr` mid-stream.

- `FACT` [E0] Design → Plan → Plan-verify → Execute → Execute-verify chain appears in design-process, technical-design, draft-adr, plan, plan-verify, execute Handoffs. [E0: respective `SKILL.md` Handoffs]
- `FACT` [E0] Execute/Verify already point to `systematic-debug` / `reproduce-bug` on verify-fail / Critical / user bug. [E0: Theme 9 wire in execute / execute-verify / -subagents]
- `GAP` No single skill announces the full ladder with skip gates for cold start. Searched: skills + packs. Result: absent — this theme’s job.

## 5. Candidate spine for `implementation-happy-path`

Orchestration only — each step = **Using `<skill>`** (read that skill’s SoT).

| Step | Action | Skip when |
|------|--------|-----------|
| 0 | Classify ask (feature / bug / research-only / authoring / trivial) | — |
| 1 | Research as needed: `codebase-recon` / `docs-research` / `research-protocol` | Familiar code + no docs pin + no deep campaign |
| 2 | `design-process` → domain design skill → **human accept** | Trivial tweak; pure bugfix with clear repro; research-only |
| 3 | `draft-adr` if locks need recording | No architectural lock |
| 4 | `implementation-plan` | Trivial chat-ephemeral exception (same spirit as Plan/Design) |
| 5 | `implementation-plan-verify` → Meta `ready` | No durable plan |
| 6 | `implementation-execute` **or** `-subagents` | No ready plan |
| 7 | `implementation-execute-verify` when non-trivial / EOP | Trivial optional |
| 8 | Branch: `reproduce-bug` → `systematic-debug` on T-VF/T-UB/T-MD/T-CR/T-NYR | Green path |
| 9 | Stop / hand human; PR Phase 2 pointer only | — |

### 5.1 Entry classifiers (candidate)

| Ask type | Entry |
|----------|--------|
| New/changed feature | Step 1→2→… happy path |
| Bug / verify-fail / unclear Critical | `reproduce-bug` and/or `systematic-debug` (may return to plan if design wrong) |
| Research / theme campaign | `research-protocol` (+ recon/docs); stop or continue to design after accept |
| Author skill/rule | `author-cursor-surfaces` (not the feature ladder) |
| Trivial one-file | Intelligent skip durable Design/Plan (document skip) |

### 5.2 Subagent model (candidate)

| Role | Holds |
|------|--------|
| **Controller** (parent / `-subagents` controller) | May run **`implementation-happy-path`** for routing + stage gates |
| **Worker** | **One pocket only** — e.g. single plan task, execute task, or debug session — not the full ladder |

- `INFERENCE` [E4] Prevents context pollution and matches Theme 7 controller/worker split. Premises: execute-subagents [E0]; Theme 4 no plugin-agents for Task isolation GAP still stands.

## 6. Surface-shape options

| Option | Pros | Cons | Lean |
|--------|------|------|------|
| **A. Skill + checklist/template** | Matches `implementation-*` pattern; progressive disclosure | Another file | **Preferred** |
| **B. Skill-only** | Thinnest | Long body risk | Viable if checklist stays short in SKILL |
| **C. Always-on rule** | Forces discovery | Violates thin rules; false triggers | **Reject** |
| **D. Pack README only** | Zero skill | Weak cold-start / `/` discovery | Reject as sole surface |

- `INFERENCE` [E4] Name **`implementation-happy-path`** fits ladder namespace (`implementation-plan` / `-execute` / `-*-verify`) and human preference. Premises: no collision [E0]; user lock 2026-07-30.

## 7. What the skill must NOT do

- Re-copy Plan/Execute/Verify/Debug spines or rubrics  
- Soften `draft-is-not-sot` / human design gate / Meta `ready`  
- Merge Execute `verify-retry N=2` with Debug `debug-fix-cycles`  
- Own PR/CI (Phase 2 stub)  
- Require Design for every bugfix  
- Become mandatory always-on  

## 8. Gaps & OPEN

| ID | Item | Follow-up |
|----|------|-----------|
| G1 | Exact checklist path (`docs/templates/happy-path.md` vs skill `references/` only) | Elevate-time / brief |
| G2 | Whether Research steps are in-ladder vs “as-needed preface” | Lean: as-needed preface in step 1 |
| G3 | Wire from README / packs / design-process Handoffs to happy-path | Elevate-time |
| G4 | Live E0 smoke (run classifier on 3 sample asks) | Optional post-elevate |
| OPEN | Community “workflow skill” corroboration | **Skip** unless human wants deep — E0 graph is enough for compose |

## 9. Implications

- `INFERENCE` [E4] **No deep campaign required** for elevation candidates — pockets are accepted SoT; this is compose. Premises: Themes 5–9 accepted; Theme 4 compose; `stop_reason` above.
- `INFERENCE` [E4] Next: short **draft brief** (or direct elevate after human accept of this note’s lean) → `/author-cursor-surfaces` → skill `implementation-happy-path` + thin checklist → wire packs/README/Handoffs → sync. Premises: user asked research first then compose; draft≠SoT until accept.
