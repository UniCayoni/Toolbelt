---
title: "T7A W1 — Cold/fresh agent execute loop for approved plans"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7a-gatherer-grok]
depth: deep
wave: 1
slice: T7A
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/templates/plan-minimal.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7A W1 — Cold/fresh agent execute loop for approved plans

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T7A**.

**Status:** `draft`. Not Execution SoT. No skills elevated from this note.

## 1. Scope

- Question / goal: How should a cold/fresh agent execute an **approved** Toolbelt implementation plan end-to-end (load → review → task loop → verify → stop/escalate), without inventing requirements?
- In scope: Cold-agent execute spine; Plan status vocab + Done-when/verify; stop/escalate reasons; fresh vs same-session; vendor E1 + optional Alexandria corroboration; Superpowers `executing-plans` as **E0 structure inventory only** (inspire, do not depend).
- Out of scope: Elevating skills; Superpowers git/worktree/TDD/finishing-branch as Toolbelt law; Design or Plan re-litigation; language/framework Build recipes; T7B subagent-controller deep design; full Verify/Debug pocket.
- Comprehension / research goal type: reuse (method inventory → transferable loop)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign brief §7.1, Theme 6 accepted report, `plan-minimal`, `implementation-plan` skill, local Superpowers `executing-plans`); WebFetch (Claude Code best practices, Cursor agent best practices, Cursor Plan Mode docs, Anthropic session-management blog); WebSearch; Alexandria `rag_query` (`ai_llm_agents`, `software_engineering`) |
| Corpora / URLs searched | `https://code.claude.com/docs/en/best-practices`; `https://claude.com/blog/using-claude-code-session-management-and-1m-context`; `https://cursor.com/blog/agent-best-practices`; `https://cursor.com/docs/agent/plan-mode`; Alexandria corpora above; local Superpowers cache skill |
| Queries (exact) | Web: `Claude Code best practices fresh session execute plan verification 2025 2026`; RAG `ai_llm_agents`: `How should coding agents execute an implementation plan task by task with verification, stop when blocked, escalate to human, reflection after each step?`; RAG `software_engineering`: `autonomous coding agents plan execute verify report human-in-the-loop approve steps clear success criteria` |
| What was *not* searched | Spec Kit implement/converge bodies (T7C); OpenSpec/BMAD execute deep-read (T7C); Superpowers SDD / verification-before-completion bodies (T7B/T7C); live E0 Toolbelt execute trial on a real plan; OpenAI Codex best-practices re-fetch |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer slice only. `stop_reason` for this note: **coverage_of_T7A_musts** — five required claim clusters addressed with cite-or-omit; residual GAPs listed for W2. Campaign-level stop remains coordinator `low_return_plus_one`. |
| Provenance (optional PROV) | Entity←Theme 6 Plan SoT + vendor docs + Superpowers structure + Alexandria books; Activity=T7A W1 cold-execute loop; Agent=cursor-grok-4.5-high-fast gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Theme 6 accepted elevation decisions are input law (systematic); vendor + community structure opportunistic for corroboration |
| Scope boundary | Execute **existing approved plans** under `docs/plans/` / house template grammar — not plan authoring, not Design |

## 4. Findings

### 4.0 Framing inputs (accepted Plan + campaign direction)

- `FACT` [E0] Theme 6 accepted elevation: status vocab `ready` · `in_progress` · `blocked` (`intent-gap` / `verify-fail` / `needs-human`) · `done`; HALT ≡ `blocked`+`intent-gap`. [E0: `docs/research/reports/theme-6-plan-pocket.md` § Elevation #9 — accessed 2026-07-30]
- `FACT` [E0] Theme 6 accepted: `serial_implement_review` default for shared-checkout coding; Done-when + runnable command + expected signal default; **verify required**; TDD ceremony optional. [E0: Theme 6 report elevation #2–#4]
- `FACT` [E0] House plan template requires per-task **Done when**, **Verify:** `command` → expected signal, and plan/task Status fields matching the vocab above. [E0: `docs/templates/plan-minimal.md`]
- `FACT` [E0] Plan skill handoff: implementers follow plan serially (or parallel-safe only); verify each Done-when; intent ambiguity → `blocked`+`intent-gap` (**do not invent**). Implement craft is explicitly not the Plan skill. [E0: plugin `implementation-plan/SKILL.md` Status vocabulary + Handoffs]
- `FACT` [E0] Campaign brief §7.1 (human 2026-07-30): Toolbelt-native naming / standalone (inspire, don’t depend); main spine + supplementary skills; **HITL = escalate/ask on major deviation or blocked — not pause every green task**; light companion atoms OK. [E0: `docs/research/notes/theme-7-execute/campaign-brief.md` §7.1]

### 4.1 Load + critical review before coding (raise concerns vs invent)

- `FACT` [E0] Superpowers `executing-plans` process (structure inventory): (1) read plan; (2) review critically — identify questions/concerns; (3) if concerns → raise with human **before** starting; (4) if no concerns → proceed with tasks. [E0: local Superpowers `…/skills/executing-plans/SKILL.md` Step 1 — structure only; not Toolbelt law]
- `FACT` [E0] Theme 6 / plan-minimal pre-exec V1: unresolved intent gaps → `blocked`+`intent-gap` — **do not invent**. [E0: `plan-minimal.md` Pre-exec V1; Theme 6 #9]
- `FACT` [E1] Claude Code: separate explore/plan from implementation; after a written spec exists, start a fresh session to execute against that document; useful specs name files/interfaces, state out-of-scope, and end with e2e verification. [E1: https://code.claude.com/docs/en/best-practices — “Explore first, then plan, then code” + interview→SPEC.md section — accessed 2026-07-30]
- `FACT` [E1] Cursor: Plan Mode produces a reviewable plan; user reviews/edits; build when ready; if build mismatches intent, revert + refine plan rather than endless patching. [E1: https://cursor.com/docs/agent/plan-mode — accessed 2026-07-30; https://cursor.com/blog/agent-best-practices — “Starting over from a plan”]
- `FACT` [E2] Osmani: planning phase is a primary quality gate — review plans for correctness/alignment before autonomous execution. [E2: Alexandria corpus=`software_engineering` chunk_id=`6ba1a4cb341d5260f63eeafd` source=`Beyond Vibe Coding` query=`autonomous coding agents plan execute verify…`]
- `INFERENCE` [E4] For Toolbelt cold execute: load the durable plan file first; run a **critical review** against Goal / Always·Block If·Never / out-of-scope / file map / task Done-when+Verify; **raise concerns to human** (or set `blocked`+`intent-gap` / `needs-human`) rather than inventing missing intent. Premises: (1) Superpowers Step 1 structure [E0]; (2) Theme 6 V1 + do-not-invent [E0]; (3) vendor plan-then-build gates [E1]; (4) campaign faithfulness lean [E0 brief §6].
- `GAP` Exact checklist fields a Toolbelt execute skill must require at review time (beyond Theme 6 V1–V8 already owned by Plan). Searched: Theme 6 + Superpowers Step 1. Result: Plan owns light pre-exec; Execute-specific review rubric not yet written.

### 4.2 Task loop: status ready→in_progress→done/blocked; Done-when verify

- `FACT` [E0] Status transitions implied by Theme 6 vocab: task starts `ready` → mark `in_progress` while executing → `done` only when verify signal passes; else `blocked` with reason. [E0: Theme 6 #9; `implementation-plan/SKILL.md` Status vocabulary — `done` = “Verify signal passed”]
- `FACT` [E0] Superpowers execute task loop (structure): for each task mark in_progress → follow steps → run verifications as specified → mark completed. [E0: `executing-plans/SKILL.md` Step 2]
- `FACT` [E1] Claude Code: give a runnable check (tests, build, linter, script, screenshot compare) producing pass/fail; agent works → runs check → iterates until pass; show evidence (command + output), not bare assertion. [E1: https://code.claude.com/docs/en/best-practices — “Give Claude a way to verify its work”]
- `FACT` [E1] Cursor practitioners guidance: provide verifiable goals (typed languages, linters, tests) so agents have clear correctness signals. [E1: https://cursor.com/blog/agent-best-practices — “They provide verifiable goals”]
- `FACT` [E2] Osmani autonomous-agent loop: **plan → execute → verify → report**; verification via tests/build; human reviews results (“trust but verify”). [E2: Alexandria corpus=`software_engineering` chunk_ids=`eb18ff3000ac18694b4d981d`, `373acdb75e7f59fe7c94a532`]
- `FACT` [E2] Huyen: reflection after each execution step and after the whole plan; evaluate outcomes and correct mistakes (or escalate when out of scope). [E2: Alexandria corpus=`ai_llm_agents` chunk_ids=`607ca6bdaea6eba8af862153`, `b6593fb02989cd5782e58dcb`]
- `INFERENCE` [E4] Toolbelt cold execute loop per task: (1) pick next `ready` task respecting deps + serial default; (2) set `in_progress`; (3) implement only within Files / Interfaces / Do-not; (4) run **Verify command**; (5) compare to **expected signal**; (6) on match → `done` and update plan ledger; on mismatch → treat as verify failure path (§4.3), not silent “looks done”. Premises: Theme 6 Done-when+verify [E0]; Claude pass/fail loop [E1]; Osmani verify step [E2].
- `GAP` Whether plan **file** status (header Meta Status) must flip to `in_progress`/`done` in lockstep with the last open task, vs task-only ledger updates. Searched: `plan-minimal` Meta + task Status. Result: both exist; sync rule not specified for Execute.
- `GAP` Retry budget before `blocked`+`verify-fail` (Superpowers: “fails repeatedly”; Theme 6: reason token only). Result: no numeric/policy SoT — prefer OPEN for W2.

### 4.3 Stop / escalate: intent-gap, verify-fail, needs-human, major deviation (HITL; do not guess)

- `FACT` [E0] Superpowers stop triggers (structure): blocker / missing dependency / test fails / instruction unclear / critical plan gaps / don’t understand instruction / verification fails repeatedly — **ask rather than guess**. [E0: `executing-plans/SKILL.md` “When to Stop and Ask for Help”]
- `FACT` [E0] Theme 6 blocked reasons: `intent-gap` · `verify-fail` · `needs-human`; do not invent across intent gaps. [E0: Theme 6 #9; plan-minimal Blocked reason]
- `FACT` [E0] Campaign §7.1 HITL: escalate/ask user on **major deviation** or blocked implementation — **not** pause for every task when green. [E0: campaign-brief.md §7.1]
- `FACT` [E2] Huyen: humans may validate plans or approve risky operations; agents should classify out-of-scope / IRRELEVANT rather than inventing impossible solutions; define automation level per action. [E2: Alexandria `ai_llm_agents` chunk_id=`b6593fb02989cd5782e58dcb`]
- `FACT` [E2] Dibia (via Alexandria): agents need when-to-delegate-to-humans / approval for high-consequence actions; HITL adds latency but prevents catastrophic failure. [E2: Alexandria `ai_llm_agents` chunk_id=`3c79f29c291e453c073f7b79`]
- `INFERENCE` [E4] Mapping for Toolbelt execute stop states (not elevated law):

  | Condition | Status / action |
  |-----------|-----------------|
  | Missing/ambiguous intent with multiple defensible outcomes | `blocked` + `intent-gap` → human; do not invent |
  | Verify command fails after reasonable fix attempts / environment can’t produce signal | `blocked` + `verify-fail` → human (or Debug handoff later) |
  | Needs credential, product choice, or irreversible ops outside plan | `blocked` + `needs-human` |
  | Implementation would materially deviate from Goal / Never / out-of-scope / interfaces | stop → human HITL (major deviation); do not “improve” by inventing scope |
  | Task green (verify signal matched) | continue to next task — no mandatory HITL pause |
  Premises: Theme 6 vocab [E0]; Superpowers ask-don’t-guess [E0 structure]; campaign §7.1 [E0]; Huyen/Dibia HITL [E2].

- `GAP` Formal definition of “major deviation” thresholds (e.g. file outside File Map, new dependency, API shape change). Searched: Theme 6 + brief. Result: directional only — OPEN for Execute skill text.
- `GAP` Whether `verify-fail` implies immediate halt vs one local fix loop then halt. Searched: Superpowers “repeatedly”; Claude iterate-until-pass. Result: **conflict** logged §6 — no Toolbelt numeric budget.

### 4.4 Fresh session vs same-session execution (Claude / Cursor E1)

- `FACT` [E1] Claude Code: once a complete spec is written, **start a fresh session to execute it** — clean context focused on implementation, with the written spec as reference; self-contained specs + e2e verification preferred. [E1: https://code.claude.com/docs/en/best-practices — accessed 2026-07-30]
- `FACT` [E1] Claude Code: `/clear` between unrelated tasks; if corrected more than twice on the same issue, clear and restart with a better prompt; subagents get fresh context for verification so the implementer isn’t grading itself. [E1: same page — “Manage your session” + verification subagent note; https://claude.com/blog/using-claude-code-session-management-and-1m-context — subagent fresh window]
- `FACT` [E1] Cursor: start a **new conversation** when moving to a different task/feature, when the agent is confused / repeats mistakes, or after finishing a logical unit; continue when iterating the same feature or debugging what it just built; long chats accumulate noise. [E1: https://cursor.com/blog/agent-best-practices — “When to start a new conversation”]
- `FACT` [E1] Cursor: save plans to workspace for resume / future agents; plans are durable context for later sessions. [E1: Cursor Plan Mode docs + blog “Save to workspace”]
- `FACT` [E0] Superpowers `executing-plans` description: use when executing a written plan **in a separate session** with review checkpoints; if subagents available, prefers SDD instead. [E0: skill frontmatter + Overview note — structure inventory]
- `INFERENCE` [E4] Toolbelt default lean for **cold execute**: prefer a **fresh session (or fresh subagent context)** whose primary brief is the durable plan path + current task packet — not the planning chat that authored the plan. Same-session continue is acceptable for tight iterate-on-green / debug-just-built loops **within** a task, but plan authorship context should not pollute execution. Premises: Claude fresh-after-spec [E1]; Cursor new-chat heuristics [E1]; Superpowers separate-session description [E0]; Theme 6 “subagents don’t inherit chat” [E0 Theme 6 exec summary #1].
- `GAP` Product-level “cold” definition for Cursor (new chat vs new subagent vs `/clear` equivalent). Searched: Cursor blog + Plan Mode docs. Result: conversation heuristics only — no Toolbelt harness SoT.
- `OPEN` Whether Theme 7 main spine skill should **require** fresh session, or **recommend** it with same-session allowed when plan already approved in-chat (campaign allows main + supplementary shapes).

### 4.5 Community structure inventory (Superpowers) + standalone stance

- `FACT` [E0] Transferable atoms from Superpowers `executing-plans` (inventory only): announce skill; load plan; critical review before code; task loop with listed verifications; stop/ask don’t guess; don’t skip verifications. [E0: local SKILL.md]
- `FACT` [E0] Non-transfer as Toolbelt Execute SoT (park — same as Theme 6 Plan stance): required git worktrees; required finishing-a-development-branch; coupling to writing-plans as runtime dependency; main/master consent rule as Execute grammar. [E0: same SKILL.md Integration + Remember sections; Theme 6 “Superpowers = structure inventory only”]
- `FACT` [E0] Campaign essence: Toolbelt remains standalone method utility — inspire from Superpowers/OpenSpec/BMAD/Spec Kit; extract what works; **do not depend**. [E0: campaign-brief.md §1 Essence filter + §7.1]
- `INFERENCE` [E4] A future Toolbelt `execute-plan` / `implement-plan` skill should restate the loop in Toolbelt vocabulary (status vocab, Done-when, blocked reasons, serial default) without importing Superpowers skill graph. Premises: §4.0–4.3 + standalone stance. **Not elevating here.**

### 4.6 Optional Alexandria corroboration (principles, not skill grammar)

- `FACT` [E2] Book-level corroboration: plan/execute/verify/report; reflection after steps; HITL for risky/out-of-scope; well-defined tasks with clear success criteria. [E2: chunks cited in §4.1–4.3]
- `INFERENCE` [E4] Alexandria does **not** supply a portable Toolbelt execute skill grammar (status tokens, Done-when field names, blocked reasons) — same pattern as Theme 6 paste-budget finding. Premises: partial book coverage; principles only.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Cold execute spine = load → critical review → statused task loop → Done-when verify → stop/escalate | confirmed (directional) | §§4.1–4.3 |
| H2 | Vendor E1 prefers fresh context after written plan/spec | confirmed | §4.4 Claude; Cursor new-chat heuristics |
| H3 | Theme 6 status vocab is sufficient Execute ledger without new tokens | confirmed (reuse) | §4.0; GAP only on header sync |
| H4 | HITL every task (Osmani/Cline approve-each-step style) is Toolbelt default | rejected for default | campaign §7.1 escalate-on-blocked/major-deviation |
| H5 | Superpowers packaging (worktree/finish/TDD) must ship inside Execute | rejected | Theme 6 + campaign standalone |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Verify fail → iterate vs halt | Claude: iterate until check passes [E1] | Superpowers: stop when verification fails repeatedly; ask [E0] | Prefer: **local iterate against the plan’s Verify command**; on repeated fail or unclear expected signal → `blocked`+`verify-fail`. Exact retry count = OPEN/GAP. |
| HITL density | Osmani/Cline approve-steps transparency [E2] | Campaign §7.1 + Superpowers SDD continuous-until-blocked (scope-normal) | Prefer campaign: no pause when green; HITL on blocked / major deviation. |
| Fresh vs same session | Claude: fresh session after spec [E1] | Cursor: continue when iterating same feature [E1] | Prefer fresh for **plan→execute handoff**; same-session OK for in-task iteration. OPEN on hard require. |

## 7. Gaps & OPEN

- `GAP` Toolbelt Execute skill body / name finalization (`execute-plan` vs `implement-plan`) — elevation deferred (T7D / accept gate).
- `GAP` Header Meta Status sync rule vs per-task ledger.
- `GAP` Retry policy before `verify-fail`.
- `GAP` “Major deviation” operational definition.
- `GAP` Live E0 trial: cold agent runs a Theme 6 `plan-minimal` plan end-to-end.
- `GAP` Codex / Spec Kit / OpenSpec apply corroboration deferred to T7C / W2.
- `OPEN` Require vs recommend fresh session for main spine skill.
- `OPEN` How much light “companion verify evidence” text lives in Execute vs later review touchups (campaign: light OK).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] Highest-value T7A spine for a future Toolbelt-native skill: **Load approved plan → critical review (raise, don’t invent) → serial task loop with status `ready`→`in_progress`→`done`/`blocked` → run Done-when Verify command to expected signal → escalate on `intent-gap` / `verify-fail` / `needs-human` / major deviation without guessing → prefer fresh session at plan→execute boundary.** Premises: §§4.0–4.5.
- `INFERENCE` [E4] Do **not** elevate Execution skills from this draft note. Premises: `draft-is-not-sot`; campaign elevation post-accept only.
- `INFERENCE` [E4] Superpowers remains **inspiration inventory**; Toolbelt Execute must speak Theme 6 plan grammar. Premises: §4.5; Theme 6 non-import stance.

## 9. Source list (deduped)

1. `docs/research/reports/theme-6-plan-pocket.md` (accepted) [E0]
2. `docs/templates/plan-minimal.md` [E0]
3. Toolbelt plugin `implementation-plan/SKILL.md` [E0]
4. `docs/research/notes/theme-7-execute/campaign-brief.md` §7.1 [E0]
5. Local Superpowers `executing-plans/SKILL.md` [E0 structure inventory]
6. Claude Code best practices — https://code.claude.com/docs/en/best-practices [E1]
7. Anthropic — Using Claude Code: session management — https://claude.com/blog/using-claude-code-session-management-and-1m-context [E1]
8. Cursor agent best practices — https://cursor.com/blog/agent-best-practices [E1]
9. Cursor Plan Mode docs — https://cursor.com/docs/agent/plan-mode [E1]
10. Alexandria Osmani / Huyen / Dibia chunks (ids in §§4.1–4.3) [E2]
11. `docs/research/notes/theme-7-execute/scope-normal.md` (scoping precursor) [E0 draft]

---

## Return summary (to parent)

| Label | Compression |
|-------|-------------|
| **FACT** | Theme 6 supplies execute ledger: `ready`→`in_progress`→`done`/`blocked`(+`intent-gap`/`verify-fail`/`needs-human`) + Done-when Verify command→expected signal; verify required; serial default. |
| **FACT** | Claude E1: fresh session after written spec; runnable pass/fail verify; self-contained files/interfaces/out-of-scope/e2e check. Cursor E1: save plan for future agents; new chat on task boundary / confusion; revert+refine plan beats endless patch. |
| **FACT** | Superpowers `executing-plans` E0 structure: load→critical review→task verify loop→stop/ask don’t guess (park worktree/finish/TDD coupling). |
| **FACT** | Campaign §7.1: HITL on blocked/major deviation, not every green task; standalone Toolbelt-native spine. |
| **GAP** | Execute skill body/name; Meta vs task status sync; verify retry budget; major-deviation definition; live E0 trial; Codex/Spec Kit/OpenSpec deepen (T7C/W2). |
