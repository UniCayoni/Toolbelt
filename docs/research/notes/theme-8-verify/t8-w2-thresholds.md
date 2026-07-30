---
title: "T8 W2-THRESHOLDS — G2 unify, OPEN-T8B-2, append format, G3 triggers"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8-w2-thresholds-gatherer]
depth: deep
campaign_phase: deep_wave2
aligned_with:
  - docs/research/notes/theme-8-verify/t8-w1-track-board.md
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8a-w1-plan-verify.md
  - docs/research/notes/theme-8-verify/t8b-w1-execute-verify.md
  - docs/research/notes/theme-8-verify/t8d-w1-surface-elevation.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/templates/plan-minimal.md
supersedes: null
---

# T8 W2-THRESHOLDS — house-policy freeze candidates

**Using `research-protocol`** · depth: **deep**.  
**Identity:** Theme 8 = Plan/Execute verification extensions — **not** Debug/PR. Do **not** elevate. Cite-or-omit.  
**Status:** `draft` — freeze candidates only; not design law until human accept / PLUS1.

---

## 1. Scope

| Field | Value |
|-------|-------|
| Question / goal | Propose unified **G2** non-trivial threshold; corroborate **OPEN-T8B-2** (post-task converge?); propose **converge append format** for Theme 6 `docs/plans/`; polish **G3** description triggers; list PLUS1-ready vs human-gate OPEN |
| In scope | G2 unify (Plan table ↔ Execute post-green); OPEN-T8B-2; append grammar; G3 trigger polish; freeze readiness table |
| Out of scope | G1 rubric prose; Debug/PR design; skill creation; G9 re-search; elevating companions |
| Track | W2-THRESHOLDS only |

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (W1 notes, campaign-brief §0, Theme 6 report, plan-minimal, research-note template); `gh api` + WebFetch Spec Kit `converge.md`; Grep W1 sections |
| Corpora / URLs searched | Local Theme 8 W1 notes; Theme 6 accepted report; `docs/templates/plan-minimal.md`; https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md |
| Queries (exact) | `gh api repos/github/spec-kit/contents/templates/commands/converge.md`; Grep G2/NT1–NT6/OPEN-T8B-2/T-D/G3/append in theme-8-verify notes |
| What was *not* searched | Live E0 companion trials (G11); Cursor skill-matching length experiments; G1 rubric bodies (W2-RUBRICS); validating-plans refs (G9 closed); Debug/PR packaging |
| Depth | deep |
| Waves / stop_reason | Wave 2 gatherer W2-THRESHOLDS; `stop_reason: diminishing_returns_on_thresholds` — all five assigned axes have freeze candidates with graded premises; residual items need human accept, not more search |
| Provenance (optional PROV) | Entity←W1 T8A/T8B/T8D + Theme 6 #7 + Spec Kit converge E1 + brief D12/D15/D18; Activity=W2 threshold unify; Agent=t8-w2-thresholds-gatherer |

---

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Reconcile existing W1 candidate tables (no new community hunt); corroborate Spec Kit append grammar once for Toolbelt mapping |
| Scope boundary | Threshold / converge-timing / append / description triggers only |

---

## 4. Findings

### 4.1 Locked campaign constraints (premise FACT)

- `FACT` [E0] **D12:** Codebase verification table **required for non-trivial** plans; skip trivial. [E0: `campaign-brief.md` §0]
- `FACT` [E0] **D15:** Post-green quality/readability review **required** for non-trivial tasks + end-of-plan; optional on trivial. [E0: `campaign-brief.md` §0]
- `FACT` [E0] **D18:** End-of-plan **required light converge** — gap types incl. unrequested; append tasks; no silent plan rewrite; no code edits in converge pass. [E0: `campaign-brief.md` §0]
- `FACT` [E0] Theme 6 elevation **#7:** Durable plans under `docs/plans/` for non-trivial work; trivial one-file tweaks may stay chat-ephemeral. **#10:** skill-only “plan before implement when non-trivial” — intelligent exceptions for trivial diffs. [E0: `theme-6-plan-pocket.md` elevation decisions]
- `FACT` [E0] Track board assigns G2 / OPEN-T8B-2 / append format / G3 → **W2-THRESHOLDS**. [E0: `t8-w1-track-board.md`]

### 4.2 W1 candidate inputs (not re-litigated as new discovery)

- `FACT` [E0] T8A G2 candidates lean **align with durable `docs/plans/`**; rube-de “single file, under 5 lines” noted as possibly too tight. [E0: `t8a-w1-plan-verify.md` §4.6]
- `FACT` [E0] T8B NT1–NT6: multi-file; Interfaces; new dep/toolchain; plan flag; subagent mode; **EOP always** for review+converge. Interim lean: EOP always; per-task review if NT1∨NT2∨NT4∨NT5. [E0: `t8b-w1-execute-verify.md` §4.8]
- `FACT` [E0] T8D G2 options T-A…T-D; Wave-1 lean **T-D** (durable-plan default + risk escalate); EOP converge always on durable plans. [E0: `t8d-w1-surface-elevation.md` §4.4]
- `FACT` [E0] OPEN-T8B-2: post-task converge ever required? lean **EOP-only**. [E0: `t8b-w1-execute-verify.md` §7]
- `FACT` [E0] T8D G3 draft descriptions + trigger phrases for both companions (not elevated). [E0: `t8d-w1-surface-elevation.md` §4.2]
- `FACT` [E0] plan-minimal has Goal, Tasks (`### Task <id>`), Pre-exec, Execution notes; no Convergence section today. [E0: `docs/templates/plan-minimal.md`]

### 4.3 Spec Kit converge append grammar (E1 corroboration)

- `FACT` [E1] Spec Kit `converge.md`: **append-only, never rewrite** — only write is appending a new `## Phase N: Convergence` section; MUST NOT modify spec/plan, rewrite/renumber/delete existing tasks, or edit application code; if clean → leave tasks file **byte-for-byte unchanged** (no empty Convergence header). [E1: github/spec-kit `templates/commands/converge.md` — accessed 2026-07-30]
- `FACT` [E1] Gap types: `missing` / `partial` / `contradicts` / `unrequested`. Present severity-graded findings **before** any append. Task line shape: `- [ ] T{nnn} <imperative> per <source-ref> (<gap-type>)`. Never reuse IDs; prior Convergence phases left untouched. [E1: same — Steps 4–7]
- `FACT` [E1] Converge is framed as post-implement assessment of present code vs artifacts — **not** a per-task mid-loop ceremony in Spec Kit. [E1: converge.md Goal + “MUST run only after implement has run”]

### 4.4 G2 — Unified non-trivial threshold (freeze candidate)

- `INFERENCE` [E4] **Adopt T-D as the shared spine**, with NT1–NT6 as concrete signals inside that spine — one coherent rule set for Plan-verify table (D12) and Execute-verify post-green (D15). Premises: T8D T-D lean [E0]; T8A durable-plan preferred lean [E0]; Theme 6 #7 [E0]; T8B NT table [E0]; avoid inventing a new numeric paste-style SoT (Theme 6 parked numeric budgets).

#### FC-G2 — House-policy freeze candidate (INFERENCE)

**Shared predicate `non_trivial` (true if any):**

| Signal ID | Condition | Maps from |
|-----------|-----------|-----------|
| **DUR** | Work is written/updated as (or ought to be) a durable plan under `docs/plans/YYYY-MM-DD-<slug>-plan.md` | T-A / Theme 6 #7 / T8A preferred |
| **MF** | Task `Files` length ≥ 2 **or** plan File Map has ≥2 paths **or** plan has ≥2 tasks | NT1 / T-B |
| **IF** | Task touches Interfaces / public shape | NT2 |
| **DEP** | New dependency, toolchain, migration, auth/secrets, or multi-package change | NT3 / T-C risk |
| **FLAG** | Plan marks task `review-required` (or equivalent non-trivial flag) | NT4 |
| **SUB** | Execute mode is `implementation-execute-subagents` | NT5 (stricter mode) |

**Trivial skip path (all must hold):**

- Chat-ephemeral **or** single-file one-task tweak **and**
- Not DUR / MF / IF / DEP / FLAG / SUB **and**
- Skip is documented in Pre-exec / task note (“trivial skip”)

**Lane application:**

| Lane | When required | When skip |
|------|---------------|-----------|
| **Plan-verify · verification table (D12)** | `non_trivial` **or** DUR (durable plan being validated) | Trivial skip path; also skip table body if plan has **no** concrete file refs (rube-de atom — still run light Reality elsewhere) |
| **Execute-verify · post-green review (D15)** | Task `non_trivial` (incl. SUB) | Trivial skip → optional light self-check |
| **Execute-verify · EOP review + light converge (D15/D18 / NT6)** | **Always** when a durable plan ledger exists (`docs/plans/…`) and execute claims plan-level completion | No durable plan (pure chat-ephemeral one-file) → EOP converge **N/A** (no ledger to append); optional light self-check only |

**Coherence notes (INFERENCE):**

1. Plan and Execute share the same `non_trivial` predicate — agents do not invent separate bars.
2. DUR is the default “yes” without counting lines (reject rube-de “under 5 lines” as Toolbelt law; keep as community discovery only).
3. Risk escalate (IF/DEP) forces required gates even when humans call the change “small.”
4. NT5 does **not** force post-task **converge** (see §4.5); it forces post-green **review** frequency under `-subagents`.
5. EOP review+converge is **never** skipped for durable plans — satisfies D15+D18 / NT6 regardless of per-task triviality.

- `OPEN` Exact optional YAML/field name for NT4 (`review-required` vs prose in Do-not) — template touch at elevation; not blocking FC-G2 logic.
- `OPEN` Whether Execute precondition should **bounce** to plan-verify if DUR and companion not yet run — owned by G4 (out of this gatherer’s prose patches).

### 4.5 OPEN-T8B-2 — Post-task converge? (freeze candidate: EOP-only)

- `FACT` [E0] Brief D18 requires light converge at **end-of-plan** only; does not require per-task converge. [E0: campaign-brief D18]
- `FACT` [E1] Spec Kit converge is an end-of-implement / post-tasks assessment against full artifacts, append-only; not specified as after every task. [E1: converge.md Goal + Operating Constraints]
- `FACT` [E0] T8B conflict log: Superpowers mandates review after each SDD task vs D15 non-trivial+EOP — resolved toward brief for **review**, with NT5 as stricter **review** mode; that conflict is about **code review**, not Spec Kit–style converge. [E0: `t8b-w1-execute-verify.md` §6]
- `FACT` [E0] Mid-plan intent coverage is already partially served by post-green **faithfulness** dimension (D17) without full converge ceremony. [E0: campaign-brief D17; t8b §4.3–4.5]

- `INFERENCE` [E4] **Freeze candidate FC-T8B-2: EOP-only converge.** Post-task converge is **not** required under Toolbelt constraints. Optional ad-hoc converge mid-plan only if human asks or orchestrator hits major-deviation / unrequested scope that needs ledger remediation before continuing — not a default gate. Premises: D18; Spec Kit timing [E1]; Superpowers “every task” maps to **review** (NT5), not converge; ceremony overload risk in T8D §4.9.
- `GAP` No E1 primary under Toolbelt constraints found that **requires** post-task converge for hybrid plan/execute companions. Searched: Spec Kit converge.md; W1 notes conflict log. Result: none contradict EOP-only for **converge**.

### 4.6 Converge append format (freeze candidate grammar)

- `INFERENCE` [E4] Steal Spec Kit **append contract + gap tags + present-before-write**, map onto Theme 6 `plan-minimal` Task blocks — **not** Spec Kit `tasks.md` Phase paths or CLI hooks. Premises: D13/D18 grammar-only; D23 park CLI; plan-minimal [E0]; converge.md [E1].

#### FC-APPEND — Candidate grammar

**Hard rules (must):**

1. **Append-only.** Allowed write surfaces: (a) new section at end of plan file; (b) new `### Task …` blocks inside that section; (c) Meta `Status` / blocked-reason sync per Theme 6 S1 when unfinished work exists.  
2. **Forbidden silent rewrites:** Goal; Global constraints; Out of scope; Coverage map rows; File / Code Map rows; existing Task bodies/IDs/Status; Pre-exec historical checks.  
3. **No application code edits** in the converge pass (D18).  
4. **Present findings first** (session table), then append only if actionable.  
5. **Clean converge:** leave plan file **byte-for-byte unchanged** (no empty Convergence header).

**Recommended section shape:**

```markdown
## Convergence

<!-- Appended by implementation-execute-verify. Do not edit prior sections.
     Re-runs append ## Convergence 2, ## Convergence 3, … — never rewrite prior Convergence. -->

### Task `C001` — <imperative title>

- [ ] Status: `ready`
- **Objective:** <remaining work>
- **Files:**
- **Interfaces (consumes / produces):**
- **Deps:** (none | prior task ids)
- **Done when:**
- **Verify:** `command` → expected signal
- **Gap type:** missing | partial | contradicts | unrequested
- **Source-ref:** <Goal | Coverage:<FR/section> | Task:<id> | design:<path§> | Always/Never>
- **Do-not (task-local):**
```

**ID scheme candidate:** `C001`, `C002`, … per Convergence section (zero-padded). Never reuse. If a second EOP converge runs, open `## Convergence 2` with `C101+` **or** continue max(`C*`)+1 — pick one at elevation; lean **continue global max `C*`**.

**Findings table (session, before write) — candidate:**

| ID | Gap Type | Severity | Source-ref | Evidence | Remaining Work |
|----|----------|----------|------------|----------|----------------|
| F1 | missing | … | … | path/area | … |

**Meta sync (allowed, not Goal rewrite):** If Meta was `done` and tasks appended → set Meta `in_progress` (S1 aggregate). Do not invent new Goal text.

- `OPEN` Whether plan-minimal template gains a stub `## Convergence` comment block at elevation, or companions create the heading only when appending (lean: **create only when appending** — matches Spec Kit “no empty header”).
- `OPEN` Severity vocab for findings table (CRITICAL/HIGH vs Plan-verify BLOCKER…) — **G1 / OPEN-T8B-1**; do not freeze here.

### 4.7 G3 — Description triggers (polished freeze candidates)

- `INFERENCE` [E4] Polish T8D/T8B phrases into final **discoverability candidates** for companion SKILL.md `description:` — still **not elevate**. Premises: T8D §4.2 [E0]; T8B §4.7 G3 lean [E0]; D3 skill-only.

#### FC-G3-PLAN — `implementation-plan-verify`

**Candidate description:**

> Validate a Toolbelt implementation plan before execute: Reality + Drift + coverage/actionability; verdicts PASS / PASS WITH NOTES / NEEDS REVISION; hard ambiguity → intent-gap; light FR→task coverage and acyclic deps; codebase verification table when non-trivial (durable `docs/plans/` or risk escalate). Use when plan-validate, validate-plan, review-plan before implement, pre-exec validate, after implementation-plan write, or before Meta ready / implementation-execute. Prefer over jumping from draft plan to code. Not for execute verify, converge, or Debug/PR.

**Trigger phrases (freeze candidate set):**  
`plan-validate` · `validate-plan` · `validate plan` · `review plan before implement` · `pre-exec validate` · `NEEDS REVISION` (plan) · after `implementation-plan` · before `implementation-execute` / Meta `ready`

#### FC-G3-EXEC — `implementation-execute-verify`

**Candidate description:**

> Verify Toolbelt plan execution: evidence iron law (IDENTIFY→RUN→READ→VERIFY); post-green faithfulness + readability/coherence review (fresh context when non-trivial); required end-of-plan light converge (gap types missing/partial/contradicts/unrequested; append tasks only; no silent Goal rewrite; no code edits in converge). Use when execute-verify, verification-before-completion, post-green review, converge against plan, intent coverage, after task Done-when green, or end-of-plan quality check. Prefer with implementation-execute / implementation-execute-subagents. Not for plan writing or PR/Debug packaging.

**Trigger phrases (freeze candidate set):**  
`execute-verify` · `verify before claiming done` · `verification-before-completion` · `post-green review` · `converge` · `converge plan` · `intent coverage` · `unrequested` · after task green · end-of-plan · with `implementation-execute` / `-subagents`

- `OPEN` Cursor matching length/keyword density — no E0 this slice (optional G11 after elevate).

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | T-D + NT signals unify D12/D15 without new numeric SoT | confirmed (freeze lean) | §4.4; Theme 6 #7 |
| H2 | EOP-only converge fits Toolbelt; Superpowers every-task ≠ converge | confirmed (freeze lean) | §4.5; Spec Kit timing [E1] |
| H3 | plan-minimal Task blocks + `## Convergence` + `C###` IDs preserve no-silent-Goal-rewrite | confirmed (grammar lean) | §4.6; Spec Kit append [E1] |
| H4 | NT5 forces post-green review, not post-task converge | confirmed (for FC-T8B-2) | §4.4–4.5 |
| H5 | Chat-ephemeral one-file has no EOP converge obligation | confirmed (lean) | NT6 + Theme 6 #7 skip |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Threshold spine | T8D T-D durable+risk [E0] | T8B NT1∨NT2∨NT4∨NT5 interim [E0] | **Merge:** T-D spine; NT1–NT5 as signals; NT6 EOP always for durable |
| Review every task | Superpowers SDD [E1] | D15 optional trivial [E0] | Prefer D15; NT5 = stricter **review** under `-subagents` only |
| Post-task converge | (none required in brief) | Optional mid-plan intent check via faithfulness | **EOP-only converge** (FC-T8B-2); faithfulness ≠ full converge |
| Skip bar | rube-de under-5-lines [E1] | Theme 6 durable bar [E0] | Prefer Theme 6 DUR; park line-count as law |
| Append shape | Spec Kit `## Phase N: Convergence` + `Tnnn` [E1] | plan-minimal `### Task` [E0] | Transfer contract; house IDs `C###` + Task block fields |

---

## 7. Gaps & OPEN

| ID | Item | PLUS1? |
|----|------|--------|
| OPEN-W2-TH-1 | NT4 exact field name in plan-minimal | Human / elevation |
| OPEN-W2-TH-2 | Global `C*` vs per-section restart ID policy (lean: global max) | Human accept (minor) |
| OPEN-W2-TH-3 | Findings severity vocab unify with Plan-verify | **G1 / OPEN-T8B-1** (other gatherer) |
| OPEN-W2-TH-4 | G4 bounce-to-plan-verify prose | Defer post-accept |
| OPEN-W2-TH-5 | Cursor description match smoke | Optional G11 |
| G9 | validating-plans refs 404 | **Closed** — no re-search |

---

## 8. Implications (INFERENCE only — not design law)

- `INFERENCE` [E4] Integrator may treat FC-G2, FC-T8B-2, FC-APPEND, FC-G3-* as **PLUS1 freeze candidates** pending human accept gate — still `draft`. Premises: §4.4–4.7; `draft-is-not-sot`.
- `INFERENCE` [E4] Elevation must not create skills from this note alone; accept Theme 8 report first (T8D elevation order). Premises: T8D §4.8; coordinator pin.
- `INFERENCE` [E4] No further threshold research waves needed unless human rejects T-D spine or demands numeric task/file SoT. Premises: stop_reason.

---

## 9. Source list (deduped)

1. [E0] `docs/research/notes/theme-8-verify/campaign-brief.md` — D12, D15, D18, G2/G3/G12 — accessed 2026-07-30  
2. [E0] `docs/research/notes/theme-8-verify/t8-w1-track-board.md` — accessed 2026-07-30  
3. [E0] `docs/research/notes/theme-8-verify/t8a-w1-plan-verify.md` §4.6 — accessed 2026-07-30  
4. [E0] `docs/research/notes/theme-8-verify/t8b-w1-execute-verify.md` §4.4–4.8, §6–7 — accessed 2026-07-30  
5. [E0] `docs/research/notes/theme-8-verify/t8d-w1-surface-elevation.md` §4.2, §4.4, §4.7 — accessed 2026-07-30  
6. [E0] `docs/research/reports/theme-6-plan-pocket.md` elevation #7, #10 — accessed 2026-07-30  
7. [E0] `docs/templates/plan-minimal.md` — accessed 2026-07-30  
8. [E1] github/spec-kit `templates/commands/converge.md` — https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md — accessed 2026-07-30  

---

## 10. Coordinator return — freeze-candidate table

| ID | Topic | Freeze candidate (INFERENCE) | PLUS1 ready? | Still OPEN for human accept |
|----|-------|------------------------------|--------------|-----------------------------|
| **FC-G2** | Non-trivial unify | **T-D spine** + signals DUR/MF/IF/DEP/FLAG/SUB; trivial skip documented; **EOP review+converge always** on durable plans (NT6) | **Yes** (logic) | NT4 field name; G4 bounce wiring |
| **FC-T8B-2** | Post-task converge | **EOP-only**; mid-plan uses faithfulness/post-green, not full converge; NT5 = review stricter, not converge | **Yes** | Optional human-requested mid-plan converge only |
| **FC-APPEND** | Converge → `docs/plans/` | Append `## Convergence` + `### Task C###` blocks; gap-type + source-ref; present-before-write; byte-unchanged if clean; Meta S1 sync OK; **no Goal/existing-task rewrite** | **Yes** (grammar) | `C*` ID continue vs restart; severity vocab → G1 |
| **FC-G3-PLAN** | Plan-verify triggers | Polished description + phrase set in §4.7 | **Yes** (copy) | Cursor match length (G11) |
| **FC-G3-EXEC** | Execute-verify triggers | Polished description + phrase set in §4.7 (incl. EOP-only converge wording) | **Yes** (copy) | Cursor match length (G11) |

**Not this gatherer:** G1 rubric prose · G4 exact orchestrator patches · skill creation · Debug/PR · G9.

**stop_reason:** `diminishing_returns_on_thresholds`
