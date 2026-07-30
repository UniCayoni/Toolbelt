---
title: "T7-W3-PLUS1 — Residual house-policy freeze (+1 after low return)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7-w3-plus1-grok]
depth: deep
wave: 3
slice: T7-PLUS1
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/t7-coordinator-pin.md
  - docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md
  - docs/research/notes/theme-7-execute/t7-w2-spine-corroboration.md
  - docs/research/notes/theme-7-execute/t7-w2-community-gaps.md
  - docs/templates/plan-minimal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7-W3-PLUS1 — Residual house-policy freeze (+1 after low return)

**Using `research-protocol`**; depth: **deep**; wave: **3**; slice: **T7-PLUS1**.

**Status:** `draft`. Not Execution SoT. No skills elevated. Freezes **E4 candidates only** (labeled `INFERENCE`) for house-policy residuals that vendor E1 cannot close. Then **stop**.

## 1. Scope

- Question / goal: After W2 diminishing returns on vendor E1 / community primary deep-reads, freeze residual **house-policy candidates** (verify-retry; major-deviation checklist; Meta↔task sync; ledger default; BMAD triage → Plan blocked-reason map) so the integrator can synthesize without another gatherer fleet.
- In scope: Candidate freeze from prior notes + `plan-minimal` / Theme 6 accepted law; BMAD→Plan mapping candidates; campaign stop `low_return_plus_one`.
- Out of scope: Elevating skills; inventing new vendor facts; live E0 execute trial; writing the integrate report (`theme-7-execute-pocket.md` — coordinator owns); closing numeric `N` as SoT.
- Comprehension / research goal type: other (policy-candidate freeze / residual close)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (all Theme 7 notes under `docs/research/notes/theme-7-execute/`; `plan-minimal.md` Meta/Status fields; Theme 6 elevation #2/#9 via prior note cites) |
| Corpora / URLs searched | Local notes only this slice — no new web/RAG (W2 already marked vendor E1 diminishing returns on spine) |
| Queries (exact) | N/A (synthesis freeze from prior graded notes) |
| What was *not* searched | New Claude/Cursor/Codex pages; live E0 trial; BMAD interactive `bmad-build` step-04; Spec Kit lean converge |
| Depth | deep |
| Waves / stop_reason | Wave 3 / +1 residual. **`stop_reason: low_return_plus_one`** — candidates frozen as INFERENCE; remaining items need human accept-gate or E0 trial, not more search. |
| Provenance (optional PROV) | Entity←T7A/W2-SPINE/W2-COMMUNITY + plan-minimal + Theme 6 + campaign §7.1; Activity=T7-PLUS1 freeze; Agent=cursor-grok-4.5-high-fast |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Named residual list from W2 stop signals; no discovery fleet |
| Scope boundary | Freeze candidates only; do not elevate; stop even if GAP remains |

## 4. Findings

### 4.0 Premise (why +1, not another W2)

- `FACT` [E0] Campaign stop rule: low-return → **+1 residual** → record `low_return_plus_one`. [E0: `campaign-brief.md` §4; `t7-coordinator-pin.md`]
- `FACT` [E0] W2-SPINE: vendor E1 on cold-execute spine at diminishing returns; residuals are house policy (N, major-deviation text, Meta sync) and/or E0 trial. [E0: `t7-w2-spine-corroboration.md` §4.1.2, §7]
- `FACT` [E0] W2-COMMUNITY: Spec Kit / BMAD review / verification-before-completion primary GAPs closed; residual includes BMAD triage ↔ Plan blocked-reason mapping detail. [E0: `t7-w2-community-gaps.md` §7]
- `INFERENCE` [E4] Further vendor/community search would restate atoms without closing accept-gate choices → this +1 freezes candidates and stops. Premises: depth-modes diminishing-returns rule; W2 stop signals.

### 4.1 Freeze — verify-retry policy (INFERENCE candidates)

Premises: T7A W1 conflict (Claude iterate-until-pass vs Superpowers “repeatedly”) [E0]; Codex repair stop quartet + example `max_iterations=3` [E1 via W2-SPINE]; Dibia enhanced retry [E2 via W2]; Theme 6 `verify-fail` token [E0].

- `INFERENCE` [E4] **Verify-retry policy candidate (not elevated):**

  | Step | Rule |
  |------|------|
  | On Verify mismatch | Enter a **small local fix loop** grounded in the failing signal (enhanced fix — not blind identical retry) |
  | Stay in loop only if | Fix stays inside task Files / Interfaces / Do-not and does not expand Goal / Done-when |
  | Exit → `blocked` + `verify-fail` when **any** | (1) house max attempts `N` reached; (2) expected signal still unmatched with **no new information** (delta not changing); (3) environment cannot produce the signal; (4) fix would require inventing intent or major deviation |
  | Candidate `N` (house policy, not vendor SoT) | **N=2** (Codex “same mistake twice” rhyme) **or** **N=3** (Codex cookbook harness example) — pick at accept gate |
  | Override | Optional per-plan note later; default global until accept |

- `GAP` Exact default `N` as Toolbelt law. Searched: Theme 6, plan-minimal, W2 vendor. Result: **durable** — needs human accept. **Stop; do not search further.**

### 4.2 Freeze — major-deviation checklist from plan-minimal fields

Premises: campaign §7.1 HITL on major deviation [E0]; plan-minimal binding surfaces [E0]; Cursor revert+refine [E1 via W2]; Codex constraints/Done-when [E1 via W2]; T7A/W2-SPINE candidate list [E0 draft].

- `INFERENCE` [E4] **Major-deviation checklist candidate** — stop/ask (do **not** “improve” by inventing) if implement would need to:

  1. Edit/create paths **outside** File/Code Map or task **Files** without a plan update;
  2. Change **Interfaces** (consumes/produces) or public API shape beyond the task;
  3. Add a **new dependency / toolchain** not listed in plan constraints;
  4. Violate **Never / Do-not / Out of scope / Block if**;
  5. Redefine **Goal** or **Done-when** success criteria to make verify pass;
  6. Perform **irreversible / credentialed / prod** ops not authorized in plan → also maps to `needs-human`.

- `INFERENCE` [E4] **Non-major (local fix / verify-retry):** verify fails but remediation stays inside Files + Interfaces + Do-not and does not expand Goal — use §4.1 loop, not automatic major-deviation HITL. Premises: §7.1 continuous-when-green; W2-SPINE §4.3.
- `GAP` Elevated skill wording + edge cases (drive-by refactors inside allowed files). Result: candidates sufficient for integrate; wording = accept-gate craft. **Stop.**

### 4.3 Freeze — Meta ↔ task status sync rule

Premises: `plan-minimal` dual Status fields same enum; Blocked reason at Meta; Theme 6 #9 vocab only [E0]; Codex living Progress [E1 via W2]; T7A GAP on sync [E0].

- `INFERENCE` [E4] **Sync rule candidates** (pick one at accept; not elevated):

  | ID | Rule | Lean |
  |----|------|------|
  | **S1** | Meta = aggregate of tasks: `done` iff all tasks `done`; `blocked` if any task `blocked`; else `in_progress` if any `in_progress` or any `done` with remaining `ready`; `ready` only if all `ready` | **Preferred lean** for cold agents reading Meta alone |
  | **S2** | Meta = execution-session flag: `in_progress` at first task start; Meta `done` only after end-of-plan acceptance/end review; task ledger SoT mid-run | Acceptable if end review is required |
  | **S3** | Task-ledger primary; Meta only at halt (`blocked`) and final `done` | Cheapest; risk of stale Meta mid-run — **dispreferred** for cold resume |

- `INFERENCE` [E4] **Default lean for faithfulness:** prefer **S1** (else S2) over S3. Premises: cold agents load durable plan [E0 T7A]; living Progress [E1 W2].
- `GAP` Accepted sync text in template/skill. **Durable house policy — stop.**

### 4.4 Freeze — ledger = plan file checkboxes / Status default

Premises: W2-COMMUNITY ledger candidates A/B/C [E0 draft]; OpenSpec/Spec Kit checkbox pattern [E1]; Theme 6 house `docs/plans/` [E0]; park `.superpowers/sdd/` [E0].

- `INFERENCE` [E4] **Ledger default candidate (not elevated):**

  | Priority | Ledger | Stance |
  |----------|--------|--------|
  | **Default** | **Plan file** under `docs/plans/…`: per-task Status fields + checkbox markers as progress ledger | Aligns Theme 6 vocab; cold/fresh resume without foreign paths |
  | Optional | Toolbelt-native **sidecar** progress file only when subagent controller needs compaction-proof resume beyond plan checkboxes | Name/path OPEN at elevate; **never** `.superpowers/sdd/progress.md` |
  | Park | Superpowers / OpenSpec CLI / BMAD artifact paths as Execute SoT | Inspiration only |

- `OPEN` Exact sidecar filename **if** optional C is adopted — product choice at elevate, not more research.

### 4.5 BMAD triage → Plan blocked-reason mapping candidates

Premises: BMAD step-04 triage enum `intent_gap` \| `bad_spec` \| `patch` \| `defer` \| `reject` [E1 via W2-COMMUNITY]; Theme 6 blocked reasons `intent-gap` \| `verify-fail` \| `needs-human` [E0]; T7D later-review lane for defer/reject inventory [E0]; campaign do-not-invent [E0].

- `INFERENCE` [E4] **Mapping candidates** (Execute / later-review; **not** elevating BMAD enum as Toolbelt SoT):

  | BMAD triage | Toolbelt Execute / Plan action (candidate) | Lane |
  |-------------|--------------------------------------------|------|
  | `intent_gap` | `blocked` + `intent-gap` → human; do not invent; do not continue green-path | Execute escalate |
  | `bad_spec` | Prefer `blocked` + `intent-gap` **or** `needs-human` (plan/spec amend required) — do **not** silently rewrite plan as implementer | Execute escalate; plan amend is human/Plan lane |
  | `patch` | Local fix + re-verify inside Files/Interfaces; consume verify-retry budget (§4.1); on exhaust → `verify-fail` | Execute fix loop |
  | `defer` | Do **not** block Execute green-path solely for deferred findings; record deferred list for **later review** portable queue; continue if Done-when verify still green | Later review (touchups/pocket OPEN) |
  | `reject` (OOS / drop) | If work already landed → stop as major deviation / `needs-human` to revert or replan; if finding only → drop from Execute scope, optionally note in deferred | Execute escalate **or** later review |

- `INFERENCE` [E4] Repair-loop **cap idea** (BMAD `review_loop_iteration` max 5) is portable as a **later-review** / optional companion numeric — **not** required as Execute spine SoT; spine uses §4.1 verify-retry `N` instead. Premises: W2-COMMUNITY §4.2; T7D boundary.
- `OPEN` Whether `bad_spec` collapses always to `intent-gap` vs distinct `needs-human` wording — accept-gate craft. **Stop; no more BMAD body search required for Execute spine.**

### 4.6 What this +1 deliberately does **not** close

| Item | Why left | Next owner |
|------|----------|------------|
| Exact verify-retry `N` | House accept | Human post-report |
| Elevated major-deviation prose | Skill authoring | Accept + elevate |
| Chosen Meta sync ID (S1/S2/S3) | House accept | Human + template touch |
| Skill name `execute-plan` vs `implement-plan` | T7D O1 | Human accept |
| Live E0 cold-execute trial | Not run | Optional follow-up |
| Require vs recommend fresh session | T7A OPEN | Human accept |
| Converge ship-with-Execute vs later-only | Stance hardened W2 | Product choice |
| Review home pocket vs touchups | T7D O5 | Later effort |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Residual P0 items are house-policy freezes, not missing vendor docs | confirmed | §4.0; W2-SPINE stop |
| H2 | Freezing INFERENCE candidates unblocks integrate without elevation | confirmed (directional) | §§4.1–4.5 |
| H3 | Another vendor/community gatherer pass would close N / Meta sync | rejected | diminishing returns |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| BMAD `bad_spec` vs Plan tokens | BMAD amend+loopback [E1 W2] | Theme 6 do-not-invent / no silent plan rewrite [E0] | Map to escalate (`intent-gap` or `needs-human`); Plan amend = human/Plan lane |
| BMAD review cap=5 vs verify-retry N | BMAD step-04 [E1] | Codex 2/3 examples [E1 W2] | Cap=5 = later-review portable; spine uses house N candidates |
| Ledger sidecar vs plan-only | SDD durable ledger [E0/E3] | Theme 6 `docs/plans/` [E0] | **Default = plan file**; sidecar optional |

## 7. Gaps & OPEN

- `GAP` Exact `N`, elevated wording, accepted S1/S2/S3 — durable until human accept (**not** more search).
- `OPEN` See §4.6 table (P0 for human after report listed in synthesis note).
- **No further gatherer spawn from this slice.**

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Integrator may cite §§4.1–4.5 as **frozen candidate set** for draft report Method spine — still `draft`, not elevation authority. Premises: `draft-is-not-sot`; campaign post-accept elevation only.
- `INFERENCE` [E4] Campaign deep gatherer phase for Theme 7 Execute research is at **`stop_reason: low_return_plus_one`**. Premises: §2 Method; campaign brief §4; W2 diminishing returns + this freeze.

## 9. Source list (deduped)

1. `docs/research/notes/theme-7-execute/campaign-brief.md` §4, §7.1 [E0]
2. `docs/research/notes/theme-7-execute/t7-coordinator-pin.md` [E0]
3. `docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md` [E0 draft]
4. `docs/research/notes/theme-7-execute/t7-w2-spine-corroboration.md` [E0 draft]
5. `docs/research/notes/theme-7-execute/t7-w2-community-gaps.md` [E0 draft]
6. `docs/templates/plan-minimal.md` [E0]
7. `docs/research/reports/theme-6-plan-pocket.md` elevation #2, #9 [E0 accepted]
8. BMAD / Codex / Superpowers facts only as cited in W2 notes (no new primary fetch this slice)

---

## Return summary (to parent)

| Field | Value |
|-------|-------|
| **stop_reason** | **`low_return_plus_one`** |
| **Frozen (INFERENCE)** | Verify-retry policy + N∈{2,3} candidates; major-deviation checklist from plan-minimal fields; Meta sync S1/S2/S3 (lean S1); ledger default = plan file Status/checkboxes; BMAD triage→Plan blocked map |
| **Not closed** | Exact N; elevated prose; accept-gate skill name / fresh-session / review home |
| **Elevate?** | No |
