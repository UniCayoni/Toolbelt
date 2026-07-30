---
title: "T7D W1 — Execute boundaries & elevation shape (light pin)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7d-w1-boundaries]
depth: deep
wave: 1
slice: T7D
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/packs/README.md
supersedes: null
---

# T7D W1 — Execute boundaries & elevation shape (light pin)

**Using `research-protocol`** · depth: **deep** · wave: **1** · slice: **T7D** (light boundary pin).

**Status:** `draft`. Not Execution SoT. No skills elevated from this note. Integrator-style merge of campaign brief §7.1 + Theme 6 accepted elevation decisions + packs ladder; light web not required this pass.

## 1. Scope

- Question / goal: What belongs in **Execute** vs later **review/debug** (touchups may suffice, not necessarily a pocket), and what **elevation shape** fits human directional decisions for post-accept surfaces?
- In scope: Boundary table (Execute / Plan / Later review-debug / Out); elevation candidates (main spine + supplementary broad-use + light verify companions); portable notes for a future review effort; short OPENs for post-deep human accept.
- Out of scope: Elevating skills; inventing Review pocket architecture / SoT; deep community inventory (T7C); locking skill bodies or house paths beyond candidates.
- Comprehension / research goal type: other (pocket boundary + elevation shape pin)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (local); Grep (Theme 6 elevation sections) |
| Corpora / URLs searched | None (light web deferred — local brief + accepted Theme 6 + packs sufficient for boundary pin) |
| Queries (exact) | N/A (no web/RAG this pass) |
| What was *not* searched | Superpowers/OpenSpec/BMAD/Spec Kit skill bodies (T7C); Cursor/Claude re-fetch; Alexandria; live E0 execute trials; Review pocket design literature |
| Depth | deep |
| Waves / stop_reason | Wave 1 light pin for T7D. Stop this slice: `boundary_table_plus_elevation_candidates` — enough for integrator merge; residual naming/folding → post-deep accept OPENs. Campaign stop remains `low_return_plus_one` at report level. |
| Provenance (optional PROV) | Entity←Theme 6 accepted report + T7 brief §7.1 + packs README + T7 scope-normal framing; Activity=T7D W1 light pin; Agent=t7d-w1-boundaries (Grok) |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Boundary pin is decision-merge, not discovery inventory |
| Scope boundary | Theme 7 Execute pocket vs Plan (accepted) vs later Quality/Verify/Debug/review; no T7C deepen |

## 4. Findings

### 4.1 Ladder & ownership facts (local)

- `FACT` [E0] Packs ladder places **Execute** after shipped Plan; Quality / Verify / workflow marked stub “future (after Execute)”. [E0: `docs/packs/README.md`]
- `FACT` [E0] Campaign brief ladder: Research → Design → Plan (shipped) → **Execute (this)** → Verify/Debug (later; may be touchups not a full pocket). [E0: `docs/research/notes/theme-7-execute/campaign-brief.md` §1]
- `FACT` [E0] Theme 6 pocket scope is planning (write plans agents can follow; design→task decomposition; 1..N execution *shape* in the plan) — **not** Implement craft; Superpowers git/TDD/PR not Plan SoT. [E0: `docs/research/reports/theme-6-plan-pocket.md` pocket scope + elevation table]
- `FACT` [E0] Theme 6 elevated skill-only: `implementation-plan` + checklist + `docs/templates/plan-minimal.md` + house `docs/plans/`; thin always-plan rule **not** elevated. [E0: Theme 6 elevation #10–#12, §8]
- `FACT` [E0] Plan owns light pre-exec checks **V1–V8**; full validating-plans / TDD auditor / issue packaging deferred. [E0: Theme 6 elevation #5]
- `FACT` [E0] Status vocab (Plan law): `ready` · `in_progress` · `blocked` (`intent-gap` / `verify-fail` / `needs-human`) · `done`; HALT ≡ `blocked`+`intent-gap`. [E0: Theme 6 elevation #9]
- `FACT` [E0] Default exec shape in Plan: `serial_implement_review`; parallel only when independence + exclusive writes (or worktrees) stated in plan. [E0: Theme 6 elevation #2]
- `FACT` [E0] Human directional OPENs (2026-07-30): Toolbelt-native naming, standalone (no Superpowers/other dependency); **main spine + supplementary** (prefer broad-use, esp. subagent-driven); HITL = escalate on major deviation/blocked, not every green task; light companion atoms OK in Execute; fuller plan+execute review → later review work (pocket **or** touchups). [E0: campaign-brief §7.1]
- `FACT` [E0] Candidate elevation table in brief (post-accept only): main spine `execute-plan`/`implement-plan`; supplementary broad-use (e.g. subagent-driven); light verify companions; thin always-on rule unlikely; entry-flow compose later. [E0: campaign-brief §5]
- `FACT` [E0] T7D note in brief: findings should stay **portable** for future review covering plan+execute review and multi-use tooling. [E0: campaign-brief §3 T7D]

### 4.2 Boundary table (integrator pin)

`INFERENCE` [E4] The following ownership split is the T7D working pin for Wave 1. Premises: (1) Theme 6 accepted elevation #2–#5, #9–#12 [E0]; (2) campaign brief §1 non-goals + §5–§7.1 [E0]; (3) packs ladder Execute before Quality/Verify stub [E0]; (4) scope-normal P0/P1/P2/Out ranking [E0 draft — framing only, not SoT].

| Lane | Owns (method concern) | Does **not** own |
|------|----------------------|------------------|
| **Execute owns** | Drive **accepted / ready** plans (or equivalent) to code with cold/fresh agents: load plan → critical consume/concerns → task loop → run **Done-when / verify** → update status ledger → stop/escalate (`intent-gap` / `verify-fail` / `needs-human` / major deviation). Enforce Plan’s `serial_implement_review` (and stated parallel-safe) at runtime. Faithfulness (no invent requirements). Quality/readability via **light** verify gates + optional fresh task reviewer. Broad-use **subagent controller** pattern when multi-context. Light verify-before-done companion atoms. | Plan authoring; V1–V8 pre-exec plan QA; Design/ADR reopen; Build cookbooks; mandatory git/worktree/TDD/PR packaging; fuller “what exists / keep / change” review inventory |
| **Plan owns** | Write hybrid plans for fresh agents; `plan-minimal` / `docs/plans/`; density & nesting; Done-when **grammar** (command + expected signal); execution **shape** in-plan (`serial_implement_review`, optional `[P]`/parallel-safe); handoff packets as plan artifacts; status **vocab** definition; **V1–V8** light pre-exec checks; Design→plan gate + decompose. Skill `implementation-plan` (shipped). | Runtime implement loop; inventing code; deep review/debug product; Execute skill bodies |
| **Later review / debug** (may be **touchups**, not a pocket) | Fuller plan+execute **review** (“what exists / keep / change”); deep validating / TDD auditor / issue packaging deferred from Plan #5; adversarial or multi-pass review craft beyond light Execute gates; finishing/PR/workflow packaging; systematic debug loops when verify fails beyond thin escalate/handoff; multi-use review tooling shared across Plan+Execute. Home: **OPEN** — pocket **or** touchups on Plan/Execute (+ Debug). | Must not block Theme 7 spine research; T7D only leaves portable notes (§4.4) |
| **Out** | Language/framework Build recipes; importing Superpowers / OpenSpec / BMAD / Spec Kit as **runtime dependency**; re-litigating Plan density/#1–#12; elevating skills mid-research; Brain/RAG product work; mandatory worktrees / TDD ceremony / commit-every-task as Execute SoT; inventing Review pocket architecture in Theme 7 | — |

Compact matrix (same pin):

| Concern | Execute | Plan | Later review/debug | Out |
|---------|---------|------|--------------------|-----|
| Write / house plans | | ✓ | | |
| V1–V8 pre-exec plan checks | | ✓ | deepen | |
| Cold-agent task loop + status updates | ✓ | | | |
| Done-when **run** at implement time | ✓ | grammar only | | |
| Light verify / optional fresh task reviewer | ✓ | | deepen | |
| Subagent-driven controller (broad-use) | ✓ | packets/shape | | |
| Escalate / HITL on block or major deviation | ✓ | vocab | | |
| Fuller plan+execute review inventory | | | ✓ (pocket or touchups) | |
| Debug loop / PR finish packaging | thin handoff only | | ✓ | |
| Superpowers (etc.) as dependency | | | | ✓ |
| Build cookbooks / git-TDD law import | | | | ✓ |

### 4.3 Elevation shape candidates (post-accept only — not elevating now)

`INFERENCE` [E4] Elevation shape that fits human §7.1 + Theme 6 precedent (skill-only main surface; thin always-on unlikely). Premises: brief §5 + §7.1; Theme 6 #10–#12 skill-only pattern; packs “elevate after accepted research”.

| Priority | Candidate | Type | Role | Notes |
|----------|-----------|------|------|-------|
| P0 | `execute-plan` **or** `implement-plan` (Toolbelt-native name TBD) | **Main spine skill** | Cold/same-session: load `docs/plans/…` → critical consume → serial task loop → Done-when verify → status → escalate | Core pocket; standalone — inspire-from Superpowers/OpenSpec/etc., **no dependency** |
| P0–P1 | Subagent-driven execute pattern (name TBD, e.g. `execute-plan-subagents` / mode of spine) | **Supplementary broad-use skill** (preferred) **or** documented mode of spine | Controller + per-task fresh implementer packets; task-level vs end review; respect Plan #2 serial/parallel-safe | Prefer **broad-use** across nearly all implementations (brief §7.1); not niche Build recipes |
| P1 | Light verify-before-done atoms | **Fold into spine** and/or **thin companion skill** | Evidence before marking `done`; maps to Plan Done-when | Fuller review deferred (later); do not grow into validating-plans replacement |
| P2 | Thin always-on Execute rule | rule | Unlikely | Mirror Theme 6 #10 — skill-only default |
| Later | Entry-flow compose | skill | After pocket accept | Same deferral as Plan entry-flow |
| — | Superpowers / other plugins as required runtime | — | **Rejected as dependency** | Inspiration + extract atoms only; cut coupling over time [E0: §7.1] |

**Coexistence (pin):** Community skills = structure inventory (E0/E1/E3 as graded elsewhere). Toolbelt Execute surfaces must remain usable **without** those plugins installed. `draft` / `proposed` plan status ≠ implement law (`draft-is-not-sot`); Execute should treat non-`ready` / draft plans as escalate/`needs-human` unless human waives — exact gate wording `OPEN`.

**House paths (candidate, not locked):** Consume Theme 6 house `docs/plans/`; Execute skill under Toolbelt skills pack (path TBD at elevate time via `author-cursor-surfaces`). No new plan schema from T7D.

### 4.4 Portable notes for future review work (not Review SoT)

Retain for a later effort that may cover **plan + execute review** and **multi-use tooling**. Do **not** treat as Review pocket architecture.

1. **Split already decided at light layer:** Plan = V1–V8 **pre-exec** checks; Execute = **run** Done-when + light verify gates + optional fresh task reviewer. Anything that inventories “what review surfaces exist / keep / change” across Plan+Execute is **later**.
2. **Multi-use tooling:** Review-like atoms may be shared (fresh-context reviewer prompt, evidence checklist, faithfulness-to-plan checklist). Prefer designing those once later rather than forking incompatible checklists inside Execute now — Execute may ship **minimal** inline atoms only.
3. **Home undecided:** Campaign + packs allow Verify/Debug/review as stub or **touchups** on Plan/Execute (+ Debug). T7D does not choose pocket vs touchups.
4. **Parked from Execute core (portable queue):** deep validating-plans / TDD auditor; requesting/receiving code-review loops; finishing-branch / PR packaging; systematic-debugging full method; issue packaging — all deferred from Theme 6 #5 and T7 scope-normal P2/Out.
5. **Inspiration ≠ dependency** applies equally to future review surfaces.
6. **Do not** invent Review skill names, pack layout, or SoT in Theme 7 integrate from this note alone.

### 4.5 Value lean alignment (boundary filter)

- `INFERENCE` [E4] Boundary table in §4.2 satisfies brief §6 lean: faithfulness + light quality gates + thin standalone method + Plan compatibility (`plan-minimal`, status vocab, serial default). Premises: brief §6; Theme 6 #2/#9/#12.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Execute should not re-own Plan V1–V8 or plan authoring | confirmed (pin) | Theme 6 #5/#12; brief T7D |
| H2 | Main spine + subagent supplementary matches human §7.1 | confirmed (directional) | brief §5, §7.1 |
| H3 | Later review is a full pocket (not touchups) | open | brief §7.1 allows either |
| H4 | Light verify folds into spine without a companion skill | open | brief §5 “fold or thin companion” |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Verify home | Execute owns Done-when run (scope-normal; brief light companions) | Quality/Verify pack stub after Execute (packs README) | **Pin:** light verify in Execute now; deepen later (pocket or touchups). No conflict for Wave 1. |
| HITL frequency | Some community continuous-exec (scope-normal conflict log) | Human §7.1: escalate on major deviation/blocked, not every green task | Prefer **human §7.1** for Toolbelt default |
| Review home | Packs “Quality / Verify / workflow” stub | Brief: may be touchups not a pocket | Leave **OPEN**; portable notes only (§4.4) |

## 7. Gaps & OPEN

### OPEN — post-deep human accept (short)

| ID | OPEN | Notes |
|----|------|-------|
| O1 | Exact spine skill name: `execute-plan` vs `implement-plan` (or other Toolbelt-native) | Directional: native; pick at accept |
| O2 | Subagent-driven: **separate supplementary skill** vs **mode/section of spine** | Prefer researching as broad-use supplement; packaging TBD |
| O3 | Light verify: **fold-only** vs **fold + thin companion** | Do not grow into full review pack |
| O4 | Draft / non-`ready` plan at execute time: hard escalate vs human waive path | Align `draft-is-not-sot` + status vocab |
| O5 | Later review home: **pocket** vs **touchups** on Plan/Execute (+ Debug) | Out of Theme 7 SoT; portable §4.4 |
| O6 | Optional fresh reviewer: default on / opt-in / only when plan says | Quality lean vs thin method |

### GAP (not closed here)

- `GAP` T7C community deepen (bodies/atoms) — owned by T7C, not T7D.
- `GAP` Live E0 Toolbelt execute trials — not this slice.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Theme 7 integrate should treat §4.2–§4.3 as the working **boundary + elevation shape** pin pending human accept — still `draft`, not elevation authority. Premises: brief T7D charter; `draft-is-not-sot`.
- `INFERENCE` [E4] Do **not** elevate Execute skills from this note. Premises: brief non-goals; packs elevate-after-accept.
- `INFERENCE` [E4] Integrator report can cite this note for “Execute vs Plan vs later review/debug vs Out” without waiting on Review pocket design. Premises: §4.4 portable notes; brief §7.1 companion/review decision.

## 9. Source list (deduped)

1. `docs/research/notes/theme-7-execute/campaign-brief.md` (esp. §1, §3 T7D, §5, §7.1) [E0]
2. `docs/research/reports/theme-6-plan-pocket.md` (elevation decisions 1–12; §5 spine; §8 elevation status) [E0 accepted]
3. `docs/packs/README.md` [E0]
4. `docs/research/notes/theme-7-execute/scope-normal.md` (framing / P0–Out ranking; draft) [E0 draft]
5. Workspace rule `draft-is-not-sot` / packs draft≠law stance [E0]

---

## Return summary (for parent / integrator)

**Boundary table**

| Execute owns | Plan owns | Later review/debug (touchups OK) | Out |
|--------------|-----------|----------------------------------|-----|
| Cold-agent load→task loop→Done-when **run**→status→escalate; enforce serial/parallel-safe; light verify + optional fresh task reviewer; broad-use subagent controller | Write plans; V1–V8; Done-when **grammar**; status vocab; packets/shape in-plan; `implementation-plan` shipped | Fuller plan+execute review inventory; deep validate/TDD auditor; PR/finish; systematic debug; multi-use review tooling — home OPEN | Build cookbooks; Superpowers/etc. **dependency**; re-litigate Plan; elevate mid-research; Review architecture as Theme 7 SoT |

**Elevation candidates (post-accept only)**

1. **Main spine skill** — Toolbelt-native `execute-plan` / `implement-plan` (name OPEN)
2. **Supplementary broad-use** — subagent-driven execute (separate skill or spine mode — OPEN)
3. **Light verify companions** — fold and/or thin companion; not full review pack
4. **No** Superpowers (or other) runtime dependency; thin always-on rule unlikely; entry-flow later
