---
title: "T7-W2-SPINE — Cold-execute spine corroboration (Wave 2)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7-w2-spine-grok]
depth: deep
wave: 2
slice: T7-W2-SPINE
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md
  - docs/research/notes/theme-7-execute/t7b-w1-subagent-controller.md
  - docs/templates/plan-minimal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7-W2-SPINE — Cold-execute spine corroboration (Wave 2)

**Using `research-protocol`**; depth: **deep**; wave: **2**; slice: **T7-W2-SPINE**.

**Status:** `draft`. Not Execution SoT. No skills elevated from this note.

## 1. Scope

- Question / goal: Corroborate T7A cold-execute spine; attack W1 GAPs (verify-retry budget, major-deviation definition candidates, Meta vs per-task status sync); close or confirm durable GAPs after re-fetch of Codex / Cursor plan-mode; short Alexandria corroboration of execute→verify→escalate (flag false friends); state diminishing-returns stop for vendor E1 on this spine.
- In scope: Spine loop only (load → review → task loop → verify → stop/escalate); W1 named GAPs above; vendor E1 re-fetch; Alexandria principles with false-friend watch.
- Out of scope: T7B controller packet deep redesign; T7C community skill deepen; skill elevation; live E0 execute trial; inventing Cursor Task API.
- Comprehension / research goal type: reuse (corroboration / GAP attack)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (research-protocol, research-note template, campaign-brief §7.1, t7a-w1, t7b-w1 §4.7 Codex GAP, plan-minimal, Theme 6 report status bits, t7-coordinator-pin); WebFetch (Cursor plan-mode; Codex cookbook ExecPlans + iterative repair loops; Codex best-practices via redirect target); Shell (resolve `developers.openai.com/codex/learn/best-practices` → 308 Location); Alexandria MCP `rag_query` (`ai_llm_agents`, `software_engineering`) |
| Corpora / URLs searched | `https://cursor.com/docs/agent/plan-mode`; `https://developers.openai.com/codex/learn/best-practices` (308 → `https://learn.chatgpt.com/guides/best-practices`); `https://developers.openai.com/cookbook/articles/codex_exec_plans`; `https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex`; Alexandria corpora above; W1 Claude/Cursor URLs cited by reference only (not re-fetched this pass except Cursor plan-mode) |
| Queries (exact) | Alexandria `ai_llm_agents`: `How should an autonomous coding agent execute a plan task by task, verify with tests or checks, retry on failure, and escalate to a human when blocked or out of scope without inventing requirements?`; Alexandria `software_engineering`: `autonomous coding agents plan execute verify report escalate human-in-the-loop success criteria stop when blocked retry budget`; Web (discovery): `OpenAI Codex best practices agent verification retry plan execution 2025 2026` |
| What was *not* searched | Spec Kit / OpenSpec / BMAD bodies (T7C); Superpowers skill bodies beyond W1 inventory; live E0 Toolbelt cold-execute trial; Cursor private Task schemas; further Claude Code re-fetch (W1 E1 retained) |
| Depth | deep |
| Waves / stop_reason | Wave 2 spine corroboration only. `stop_reason` (this slice): **diminishing_returns_vendor_E1_on_spine** — Claude (W1) + Cursor plan-mode (re-fetched) + Codex best-practices/ExecPlans/repair-loop (fetched this pass) restate the same load→verify→escalate shape; remaining spine items are house-policy OPENs / E0 trial, not more vendor E1. Campaign stop remains coordinator `low_return_plus_one`. |
| Provenance (optional PROV) | Entity←T7A W1 + Theme 6 Plan SoT + vendor Codex/Cursor + Alexandria books; Activity=T7-W2-SPINE corroboration; Agent=cursor-grok-4.5-high-fast |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Systematic attack of named W1 GAPs; opportunistic vendor re-fetch + short RAG |
| Scope boundary | Cold-execute **spine** GAPs only — not controller packet redesign |

## 4. Findings

### 4.0 W1 spine retained (input; not re-litigated)

- `FACT` [E0] T7A W1 directional spine: load approved plan → critical review (raise, don’t invent) → serial task loop `ready`→`in_progress`→`done`/`blocked` → Done-when Verify command→expected signal → escalate on `intent-gap` / `verify-fail` / `needs-human` / major deviation; prefer fresh session at plan→execute boundary; HITL not every green task. [E0: `docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md` §§4.1–4.4, Return summary — accessed 2026-07-30]
- `FACT` [E0] Campaign §7.1: escalate/ask on major deviation or blocked — not pause every green task; Toolbelt-native standalone spine. [E0: `docs/research/notes/theme-7-execute/campaign-brief.md` §7.1]
- `FACT` [E0] Theme 6 / `plan-minimal`: Meta Status + per-task Status share vocab `ready` \| `in_progress` \| `blocked` \| `done`; task Verify required; no Execute sync rule between Meta and tasks. [E0: `docs/templates/plan-minimal.md` Meta table + Tasks — observed 2026-07-30]

### 4.1 Vendor re-fetch (Codex + Cursor plan-mode)

#### 4.1.1 Codex best-practices (W1 timeout / 308 — closed this pass)

- `FACT` [E0] `https://developers.openai.com/codex/learn/best-practices` returns **308 Permanent Redirect** with `Location: https://learn.chatgpt.com/guides/best-practices` (PowerShell, no auto-follow). Explains W1 WebFetch timeout / 308 GAP. [E0: Shell observe 2026-07-30]
- `FACT` [E1] Codex best practices (redirect target): prompt defaults include **Goal**, **Context**, **Constraints**, **Done when** (tests passing / behavior / bug gone); plan before coding on complex tasks (`/plan`, interview, or `PLANS.md`); `AGENTS.md` should encode build/test/lint, constraints/do-not, and **what done means / how to verify**; “Don’t stop at asking Codex to make a change — create tests when needed, run checks, confirm result, review before accept”; when Codex makes the **same mistake twice**, ask for a retrospective and update `AGENTS.md`; one chat per coherent unit of work; common mistake: not giving build/test commands so the agent can see its work. [E1: https://learn.chatgpt.com/guides/best-practices — accessed 2026-07-30; formerly advertised at developers.openai.com/codex/learn/best-practices]
- `FACT` [E1] Codex ExecPlans cookbook: plans are **living documents**; Progress checklist must reflect actual current state; validation not optional — exact commands + expected outputs; acceptance as **observable behavior**; “If a step can fail halfway, include how to retry or adapt”; on implement: keep sections up to date; **false-friend risk:** template text also says “Resolve ambiguities autonomously” / “do not prompt the user for next steps” — conflicts with Toolbelt do-not-invent + campaign HITL (see §6). [E1: https://developers.openai.com/cookbook/articles/codex_exec_plans — accessed 2026-07-30]
- `FACT` [E1] Codex iterative repair cookbook: production loop stop conditions = (1) validation passes, (2) **maximum number of attempts**, (3) remaining delta **stops changing**, (4) next decision needs **human review**; example harness uses `max_iterations: int = 3`; failures become structured feedback for next repair, not silent success. [E1: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex — accessed 2026-07-30]
- `FACT` [E1] Cursor Plan Mode (re-fetch): research → reviewable plan → user review/edit → build when ready; save to workspace for future agents; if build mismatches intent, **revert + refine plan** rather than endless patching. [E1: https://cursor.com/docs/agent/plan-mode — accessed 2026-07-30]

#### 4.1.2 Diminishing returns — vendor E1 on cold-execute spine

- `INFERENCE` [E4] **Vendor E1 for the cold-execute spine is at diminishing returns.** Premises: (1) W1 Claude: fresh session after spec, runnable pass/fail verify, ask don’t invent [E0 T7A]; (2) Cursor plan-mode + agent BP (W1/W2): durable plan, verify goals, new-chat heuristics, revert+refine vs endless patch [E1 this pass + T7A]; (3) Codex BP + ExecPlans + repair-loop (this pass): Done-when/verify, living progress, max-attempt stop, human on non-converging decisions [E1]; (4) further vendor pages restate the same atoms without closing house-policy GAPs (exact N, Meta sync grammar, major-deviation skill text). **Stop signal for more vendor E1 on this spine:** yes — prefer house INFERENCE/OPEN + optional E0 trial over another vendor pass.

### 4.2 GAP attack — verify-retry budget

- `FACT` [E0] W1 conflict: Claude iterate-until-pass vs Superpowers “verification fails repeatedly” → ask; no Toolbelt numeric budget. [E0: t7a-w1 §6 Conflicts]
- `FACT` [E1] Codex repair-loop: explicit **max attempts** + non-convergence + human-review stops; example default `max_iterations=3` is cookbook harness, **not** a universal product constant. [E1: iterative repair cookbook — accessed 2026-07-30]
- `FACT` [E1] Codex best practices: “same mistake **twice** → retrospective + update AGENTS.md” is a **guidance-improvement** heuristic, not a named per-task `verify-fail` ledger rule. [E1: learn.chatgpt.com/guides/best-practices]
- `CLAIM` [E2] Dibia plan-based orchestrator: evaluate each step; on failure **retry with enhanced instructions** from failure analysis (not blind retry). [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)` chunk_id=`3468fcf7fbcea4d9fc928c5b` query=`How should an autonomous coding agent execute…`]
- `CLAIM` [E2] Broda: on error decide whether to **retry, escalate, or abort** — error handling is core to execution; no numeric budget. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh… (Eric Broda, Davis Broda)` chunk_id=`8487d75ab7f1f6a11ae51c1b` query=same]
- `INFERENCE` [E4] **Verify-retry policy candidate (not elevated):** For a single task’s Verify command: (a) allow a **small local fix loop** grounded in the failing signal (enhanced fix, not blind retry); (b) stop → `blocked`+`verify-fail` when **any** of: max attempts reached, expected signal still unmatched with **no new information** (delta not changing), environment cannot produce the signal, or fix would require inventing intent / major deviation. Premises: Codex stop quartet [E1]; Dibia enhanced retry [E2]; W1 Claude/Superpowers conflict [E0]; Theme 6 `verify-fail` token [E0].
- `INFERENCE` [E4] **Numeric N is house policy, not vendor SoT.** Candidate defaults for later accept-gate (labeled candidates only): **N=2** (Codex “twice” retrospective rhyme) or **N=3** (Codex cookbook example). Neither closes as Toolbelt law from E1 alone. Premises: §4.2 facts above.
- `GAP` Exact Toolbelt default `N` / whether N is global vs per-plan override. Searched: Theme 6, plan-minimal, Codex BP/repair, Alexandria. Result: pattern only — **durable GAP** until accept gate or E0 trial.

### 4.3 GAP attack — “major deviation” definition candidates

- `FACT` [E0] Campaign §7.1 names “major deviation” as HITL trigger without operational thresholds. [E0: campaign-brief.md §7.1]
- `FACT` [E0] Theme 6 / plan-minimal already supply binding surfaces: Goal; Always·Block If·Never; Out of scope; File/Code Map; task Files / Interfaces / Do-not; Verify expected signal. [E0: plan-minimal.md]
- `FACT` [E1] Cursor: build mismatch → revert + refine plan, not endless local patch — supports treating scope/intent mismatch as stop-and-replan, not silent expand. [E1: cursor.com/docs/agent/plan-mode]
- `FACT` [E1] Codex Done-when / constraints / do-not guidance + observable acceptance — deviation from stated Done-when/constraints is out-of-contract. [E1: learn.chatgpt.com/guides/best-practices; ExecPlans cookbook]
- `INFERENCE` [E4] **Major-deviation candidate checklist** (operationalize for future Execute skill text; **not elevated**): treat as major deviation → stop/ask (do not “improve” by inventing) if the agent would need to:
  1. Edit/create paths **outside** File/Code Map (or task Files) without plan update;
  2. Change **Interfaces** (consumes/produces) or public API shape beyond the task;
  3. Add **new dependency / toolchain** not listed in plan constraints;
  4. Violate **Never / Do-not / Out of scope / Block if**;
  5. Redefine **Goal** or Done-when success criteria to make verify pass;
  6. Perform **irreversible / credentialed / prod** ops not authorized in plan → also maps to `needs-human`.
  Premises: plan-minimal binding fields [E0]; campaign HITL [E0]; Cursor revert+refine [E1]; Codex constraints/Done-when [E1].
- `INFERENCE` [E4] **Non-major (continue / local fix):** verify signal fails but fix stays inside Files + Interfaces + Do-not and does not expand Goal — enter verify-retry loop (§4.2), not automatic major-deviation HITL. Premises: campaign continuous-when-green [E0]; Codex local repair [E1].
- `GAP` Formal elevated wording + edge cases (e.g. drive-by refactors inside allowed files). Searched: Theme 6 + brief + vendor. Result: candidates only — **durable GAP** for skill authoring / accept gate (policy, not missing vendor E1).

### 4.4 GAP attack — Meta plan status vs per-task status sync

- `FACT` [E0] `plan-minimal` defines **both** Meta Status and per-task Status with the same enum; Blocked reason lives at Meta; no rule stating when Meta flips relative to tasks. [E0: plan-minimal.md]
- `FACT` [E0] Theme 6 elevation #9 freezes vocab tokens, not Meta↔task sync mechanics. [E0: `docs/research/reports/theme-6-plan-pocket.md` elevation #9]
- `FACT` [E1] Codex ExecPlans: Progress section **must always reflect actual current state**; living document updated at every stopping point — supports a **controller-visible ledger** that stays honest, not task-only silent progress. [E1: ExecPlans cookbook]
- `INFERENCE` [E4] **Sync rule candidates** (pick one at accept gate; not elevated):

  | ID | Rule | Notes |
  |----|------|-------|
  | S1 | Meta = aggregate of tasks | `done` iff all tasks `done`; `blocked` if any task `blocked`; else `in_progress` if any `in_progress` or any `done` with remaining `ready`; `ready` only if all `ready` |
  | S2 | Meta = “execution session” flag | Set Meta `in_progress` at first task start; Meta `done` only after end-of-plan acceptance/end review; task ledger is source of truth mid-run |
  | S3 | Task-ledger primary; Meta optional | Cold agent updates tasks always; Meta updated only at halt (`blocked`) and final `done` — cheapest, risk of stale Meta mid-run |

  Premises: dual fields exist [E0]; ExecPlans living Progress [E1]; controller needs honest spine [E0 T7B pattern].
- `INFERENCE` [E4] **Lean for Toolbelt faithfulness:** prefer **S1** (aggregate) or **S2** over S3 so cold/fresh agents reading only Meta don’t misread a half-done plan as `ready`. Premises: cold agents load durable plan [E0 T7A]; Codex living Progress [E1].
- `GAP` Accepted sync rule text in template/skill. Searched: plan-minimal + Theme 6. Result: unspecified — **durable GAP** (house policy).

### 4.5 Alexandria short corroboration (execute→verify→escalate) + false friends

- `FACT` [E2] Osmani: autonomous agents follow **plan → execute → verify → report**; verify via tests/build; human reviews (“trust but verify”); agents excel at well-defined tasks with clear success criteria. [E2: Alexandria corpus=`software_engineering` chunk_ids=`eb18ff3000ac18694b4d981d`, `373acdb75e7f59fe7c94a532`, `6ba1a4cb341d5260f63eeafd` query=`autonomous coding agents plan execute verify…`]
- `FACT` [E2] Huyen: classify out-of-scope as IRRELEVANT rather than inventing; humans may validate plans / approve risky ops; automation level per action; reflect after execution outcomes. [E2: Alexandria corpus=`ai_llm_agents` chunk_id=`b6593fb02989cd5782e58dcb` query=`How should an autonomous coding agent execute…`]
- `FACT` [E2] Dibia: orchestrator evaluates steps; retries failed steps with **enhanced** instructions; centralized plan/progress/evaluation. [E2: chunk_id=`3468fcf7fbcea4d9fc928c5b`]
- `FACT` [E2] Broda: retry / escalate / abort as execution error-handling triad; supervised execution for deviations. [E2: chunk_ids=`8487d75ab7f1f6a11ae51c1b`, `9648b6bb2865d8e29f6ea5b7`]
- `INFERENCE` [E4] Alexandria **corroborates principles** (verify, reflect, escalate when out-of-scope/risky, don’t invent) but still **does not supply** Toolbelt status tokens, Done-when field names, or numeric retry SoT — same paste-budget pattern as Theme 6 / T7A. Premises: chunks above; T7A §4.6.
- **False friends (do not import as Toolbelt HITL default):**
  - `CLAIM` [E2] AutoGPT-style permission every task / every N tasks — conflicts campaign §7.1 continuous-when-green. [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents in Action (Micheal Lanham)` chunk_id=`97aa452add8b4b321347a368` — “ask for permission for every task or for every x number of tasks”]
  - `CLAIM` [E2] Cline approve-each-step transparency — HITL density higher than §7.1. [E2: Alexandria corpus=`software_engineering` chunk_id=`b8b7294e50700b5ab9f9216e` — opportunity to approve/modify each step]
  - `FACT` [E1] Codex ExecPlans “resolve ambiguities autonomously” — **false friend** vs Theme 6 do-not-invent / `intent-gap`. Prefer Toolbelt: escalate intent gaps. [E1: ExecPlans cookbook; Theme 6 #9]
  - Low-signal / skip as spine SoT: Agentic Mesh general “execution as life metaphor” chunks; n8n beginner prompting book (automation UX, not coding-plan grammar).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W1 cold-execute spine survives Codex + Cursor re-fetch | confirmed | §4.1 |
| H2 | Vendor E1 still diminishing for spine after Codex close | confirmed | §4.1.2 |
| H3 | Verify-retry has pattern (max + non-converge + human) but not numeric SoT | confirmed | §4.2 |
| H4 | Major deviation can be operationalized from plan-minimal fields | confirmed (candidates) | §4.3 |
| H5 | Meta↔task sync is house policy, not missing vendor doc | confirmed | §4.4 |
| H6 | Alexandria closes skill grammar GAPs | rejected | §4.5 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Ambiguity handling | Codex ExecPlans: resolve autonomously / don’t ask next steps [E1] | Theme 6 + campaign: do not invent; escalate intent-gap / major deviation [E0] | **Prefer Toolbelt Plan + §7.1.** Treat ExecPlans autonomy line as false friend for intent gaps. |
| HITL density | AutoGPT/Cline approve-each-step [E2] | Campaign §7.1 continuous when green [E0] | **Campaign wins.** |
| Verify iterate vs halt | Claude iterate-until-pass [E1 W1]; Codex max-attempt loop [E1] | Superpowers stop when fails repeatedly [E0 W1] | **Local enhanced retries up to house N, then `verify-fail`.** Exact N = durable OPEN. |
| Codex “twice” | AGENTS.md retrospective after same mistake twice [E1] | Per-task verify-fail budget | Related rhyme only — do not equate without accept-gate choice. |

## 7. Gaps & OPEN — closed vs durable

### Closed this wave (spine)

| Item | Disposition |
|------|-------------|
| Codex best-practices primary page unreadable (W1) | **Closed** — 308 → `learn.chatgpt.com/guides/best-practices` fetched [E1] |
| Cursor plan-mode unreachable / stale (W1 risk) | **Closed** — re-fetched; confirms W1 claims [E1] |
| Vendor silence on “have a retry budget at all” | **Closed as pattern** — Codex stop quartet [E1]; numeric N still open |
| Major deviation “no candidates” | **Closed as candidate list** (§4.3 INFERENCE) — not elevated |
| Meta sync “no candidates” | **Closed as S1/S2/S3 candidates** (§4.4 INFERENCE) — not elevated |

### Durable GAPs / OPENs (spine)

| Item | Why durable |
|------|-------------|
| Exact verify-retry `N` (+ per-plan override?) | House policy; vendor gives examples (2/3), not Toolbelt SoT |
| Elevated “major deviation” skill wording | Needs accept-gate craft; candidates exist |
| Meta↔task sync rule in `plan-minimal` / execute skill | Needs accept-gate; S1 lean is INFERENCE only |
| Live E0 cold-agent trial on a real `plan-minimal` plan | Not run |
| Require vs recommend fresh session | Remains OPEN from T7A |
| Skill name / elevation (`execute-plan` vs `implement-plan`) | T7D / post-accept — not spine evidence |

### Stop signal for spine

- **Vendor E1 on cold-execute spine: STOP** (`diminishing_returns_vendor_E1_on_spine`).
- Further W2/W3 value for this spine = **house-policy decisions** (N, major-deviation text, Meta sync) and/or **E0 trial** — not more Claude/Cursor/Codex best-practice pages.
- Campaign-level stop remains coordinator `low_return_plus_one` (other tracks T7B–D may still need residual work).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] T7A spine remains the highest-value Execute method shape; W2 vendor+RAG corroboration **does not change** the loop, only supplies retry/major-deviation/Meta **candidates**. Premises: §§4.0–4.5.
- `INFERENCE` [E4] Do **not** elevate Execution skills from this draft. Premises: `draft-is-not-sot`.
- `INFERENCE` [E4] Integrator may treat spine vendor surface as **sufficiently corroborated** for draft report synthesis; residual spine items should appear as **OPEN policy** / E0 follow-ups, not more gatherer vendor passes. Premises: §4.1.2; §7 stop signal.

## 9. Source list (deduped)

1. `docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md` [E0 draft]
2. `docs/research/notes/theme-7-execute/t7b-w1-subagent-controller.md` §4.7 [E0 draft]
3. `docs/research/notes/theme-7-execute/campaign-brief.md` §7.1 [E0]
4. `docs/templates/plan-minimal.md` [E0]
5. `docs/research/reports/theme-6-plan-pocket.md` (accepted) [E0]
6. Codex best practices — https://learn.chatgpt.com/guides/best-practices (redirect from https://developers.openai.com/codex/learn/best-practices) [E1]
7. Codex ExecPlans — https://developers.openai.com/cookbook/articles/codex_exec_plans [E1]
8. Codex iterative repair loops — https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex [E1]
9. Cursor Plan Mode — https://cursor.com/docs/agent/plan-mode [E1]
10. Alexandria `ai_llm_agents` — Huyen `b6593fb02989cd5782e58dcb`; Dibia `3468fcf7fbcea4d9fc928c5b`; Broda `8487d75ab7f1f6a11ae51c1b`; Lanham `97aa452add8b4b321347a368` [E2]
11. Alexandria `software_engineering` — Osmani `eb18ff3000ac18694b4d981d`, `373acdb75e7f59fe7c94a532`, `6ba1a4cb341d5260f63eeafd`; Cline false-friend `b8b7294e50700b5ab9f9216e` [E2]

---

## Return summary (to parent)

| Axis | Result |
|------|--------|
| **Closed** | Codex BP fetch (via 308→learn.chatgpt.com); Cursor plan-mode re-confirm; retry **pattern** (max/non-converge/human); major-deviation **candidates**; Meta sync **S1/S2/S3 candidates** |
| **Durable GAPs** | Exact retry `N`; elevated major-deviation text; accepted Meta sync rule; live E0 trial; require vs recommend fresh session; skill elevation/name |
| **Stop signal (spine)** | **Yes — diminishing returns on vendor E1** for cold-execute spine. Next value = house policy + optional E0, not more vendor pages. |
| **False friends** | ExecPlans “resolve ambiguities autonomously”; AutoGPT/Cline approve-every-step HITL |
| **Elevate?** | No — draft only |
