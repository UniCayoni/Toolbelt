---
title: "T7B W1 — Subagent controller execution (broad-use)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [grok-t7b-w1]
depth: deep
wave: 1
slice: T7B
supersedes: null
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/templates/plan-minimal.md
  - docs/PROTOCOL.md
---

# T7B W1 — Subagent controller execution (broad-use)

**Using `research-protocol`** · depth: **deep** · wave: **1** · slice: **T7B**.

**Status:** `draft`. Not Execution SoT. No skills elevated from this note.

## 1. Scope

- Question / goal: How should a **controller agent** execute Theme 6–style plans via **fresh subagents** (implementer packets + reviews) for **broad use** across implementations?
- In scope:
  1. Per-task handoff packet contents (align Theme 6 Plan packets / `plan-minimal`)
  2. Serial default; parallel-safe only when plan marks independence + exclusive writes / worktrees (Plan accepted #2)
  3. Task-level review vs end-of-plan review; continuous execution when green (HITL on blocked / major deviation — campaign §7.1)
  4. Sources: Anthropic / Claude Code / Cursor / OpenAI E1; Alexandria `ai_llm_agents`; local Superpowers SDD as E0/E3 inventory only — Toolbelt stays standalone
  5. What makes a pattern **broad-use** vs niche
- Out of scope:
  - Inventing Cursor Task API / spawn schemas beyond published product docs
  - Elevating Superpowers “never parallel implementers” as Toolbelt law (use Plan #2 scoped rules)
  - Elevating Execution skills mid-research
  - Domain Build recipes; Superpowers git/worktree/TDD/finishing packaging as SoT
  - Cold same-session execute loop without subagents (T7A)
- Comprehension / research goal type: adaptive (shape controller execute method)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (research-protocol, campaign-brief §7.1, Theme 6 report + T6C/T6-W2-EXEC notes, `plan-minimal.md`, Superpowers SDD `SKILL.md` + `implementer-prompt.md`); WebFetch (Anthropic building-effective-agents + multi-agent-research-system; Claude Code best-practices + sub-agents; Cursor subagents + multi-agent help + agent-best-practices blog; OpenAI Agents SDK multi_agent); Alexandria MCP `rag_probe` / `rag_query` on `ai_llm_agents`; Shell fetch attempt for OpenAI Codex pages (failed) |
| Corpora / URLs searched | Anthropic engineering; code.claude.com best-practices / sub-agents; cursor.com docs/subagents + help/multi-agent + blog/agent-best-practices; openai.github.io/openai-agents-python/multi_agent; Alexandria `ai_llm_agents`; local Superpowers cache SDD |
| Queries (exact) | Alexandria probe: `controller orchestrator fresh subagents implementer reviewer per-task handoff packets serial parallel coding plans review gates continuous execution HITL`; Alexandria query: `orchestrator worker controller fresh context implementer reviewer handoff task packet serial parallel coding review gate continuous execution escalate human`; Web: `OpenAI Codex best practices agents subagents implementation plans 2025 2026` |
| What was *not* searched | Cursor Task tool internal/private API schemas; live E0 Toolbelt controller trials; Spec Kit / OpenSpec / BMAD deep-read (T7C); AutoGen/LangGraph primary docs; elevating skill draft text |
| Depth | deep |
| Waves / stop_reason | Wave 1 primary SoT for T7B only. `stop_reason`: **wave1_slice_coverage** — Method + findings cover all five MUST axes with cite-or-omit; Codex best-practices live page left as GAP (308/timeout); no invent Task API; residual deepeners → W2. Campaign integrate owned by coordinator. |
| Provenance (optional PROV) | Entity←vendor docs + Alexandria chunks + Theme 6 accepted Plan law + Superpowers cache inventory; Activity=T7B W1 gather; Agent=cursor-grok-4.5-high-fast |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Controller pattern needs vendor E1 + RAG corroboration (systematic) plus Theme 6 Plan packet alignment and Superpowers inventory (as-needed local reads) |
| Scope boundary | Included: packet contents, serial/parallel-safe rules, review cadence, continuous-vs-HITL, broad-use filter. Excluded: inventing Task API; skill elevation; Build cookbooks |

## 4. Findings

### 4.1 Controller role (orchestrator + durable spine)

- `FACT` [E1] Anthropic **orchestrator-workers**: a central LLM breaks down work, delegates to workers, synthesizes results; suited to complex multi-file coding where subtasks are input-dependent (distinct from fixed parallelization). [E1: Building effective agents §Orchestrator-workers — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-30]
- `FACT` [E1] Anthropic Research: lead agent plans, spawns specialized subagents with **separate context windows**, synthesizes; subagents facilitate compression/separation of concerns. [E1: How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-30]
- `FACT` [E1] Cursor **orchestrator pattern**: parent coordinates specialists in sequence — Planner → Implementer → Verifier — with structured handoffs. [E1: Subagents §Common patterns — https://cursor.com/docs/subagents — accessed 2026-07-30]
- `FACT` [E1] OpenAI Agents SDK: manager keeps control via **agents-as-tools**, or **handoffs** when a specialist becomes active; code orchestration includes chaining and evaluator-in-a-loop. [E1: Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-30]
- `CLAIM` [E2] Plan-based orchestration: orchestrator maintains explicit task plans/assignments/dependencies; **orchestrator sees all context**; workers receive **only relevant information**; state centralized (plan, progress, evaluation). [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)` chunk_id=`3468fcf7fbcea4d9fc928c5b` query=`orchestrator worker controller…`]
- `FACT` [E0] Theme 6 accepted Plan spine: controller-readable plan + per-task handoff packets; execution default `serial_implement_review`. [E0: `docs/research/reports/theme-6-plan-pocket.md` §§Accepted decisions #2, Plan method spine #6–7; `docs/templates/plan-minimal.md` — observed 2026-07-30]
- `FACT` [E0] Superpowers SDD (inventory): controller dispatches fresh implementer per task, then task reviewer, then final whole-branch review; constructs exact context — workers must not inherit session history. [E0: path=`C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\subagent-driven-development\SKILL.md` §§Why subagents, The Process — observed 2026-07-30]
- `INFERENCE` [E4] For Toolbelt Execute, the controller owns: load/review plan spine, build per-task packets, dispatch fresh implementers, adjudicate statuses, gate reviews, update progress/status vocab, escalate on blocked/major deviation — **not** implement every task in-controller context. Premises: Anthropic/Cursor orchestrator [E1]; Dibia selective visibility [E2]; Theme 6 packets [E0]; SDD inventory [E0/E3].

### 4.2 Per-task handoff packet contents (align Theme 6)

#### 4.2.1 Vendor / literature fields

- `FACT` [E1] Anthropic delegation fields for each subagent: **objective**, **output format**, **guidance on tools/sources**, **clear task boundaries**. Vague instructions caused duplicated/misaligned work. [E1: multi-agent-research-system §Teach the orchestrator how to delegate — accessed 2026-07-30]
- `FACT` [E1] Anthropic appendix: store large outputs on **filesystem / artifact store**; pass **lightweight references** to the coordinator (“minimize the game of telephone”); spawn **fresh subagents with clean contexts** while retrieving stored plan/context. [E1: multi-agent-research-system Appendix — accessed 2026-07-30]
- `FACT` [E1] Cursor: subagents start with **clean context**; parent must include needed info in the prompt (no prior conversation history). Keep prompts specific; avoid overly long prompts. [E1: Subagents §§How subagents work, Best practices — https://cursor.com/docs/subagents — accessed 2026-07-30]
- `FACT` [E1] Claude Code: after a complete spec, **start a fresh session to execute**; most useful specs are self-contained — files/interfaces, out-of-scope, e2e verification. [E1: Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-30]
- `CLAIM` [E2] Structured handoffs should feel like internal APIs: user goal (one sentence); brief prior actions/results; key facts (+ provenance); open question for receiver; constraints. Orchestration works best when each agent has clear identity + limited surface area (producer/reviewer). [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex… (Andrei Gheorghiu)` chunk_id=`eb26af7b81ef9539f023e63c` / related handoff chunks from T6C `618afba9e60090c0249026d4` query=`orchestrator worker controller…`]
- `FACT` [E0] Superpowers File Handoffs (inventory): dispatch carries (1) one-line fit in project; (2) **task brief path** as requirements SoT; (3) interfaces/decisions from earlier tasks the brief cannot know; (4) ambiguity resolutions; (5) report-file path/contract. Exact values live in the brief — do not paste accumulated prior-task history; do not make worker read the whole plan file. [E0: SDD SKILL.md §§File Handoffs, Red Flags — observed 2026-07-30]

#### 4.2.2 Theme 6 packet field freeze (alignment target)

- `FACT` [E0] Theme 6 / `plan-minimal` task unit fields: Objective; Files; Interfaces (consumes/produces); Deps; Done-when; Verify (`command` → expected signal); optional GWT; Parallel-safe; task-local Do-not; plus plan-level Goal, Always·Block If·Never, Out of scope, File/Code Map. Paste tiers T0–T3; **T3: do not dump chat history into worker briefs**. [E0: `docs/templates/plan-minimal.md`; Theme 6 report spine #5–8 — observed 2026-07-30]
- `INFERENCE` [E4] **Controller implementer packet (broad-use candidate)** — compose from Theme 6 task block + Anthropic/Cursor fields, as paths/refs not chat dumps:

  | Packet field | Source alignment |
  |--------------|------------------|
  | Scene-setting (1 line: where task fits) | Anthropic boundaries [E1]; SDD inventory [E0] |
  | Task brief / requirements SoT (path or T0 extract of Objective + Done-when + Verify + Files + Interfaces + Do-not) | Theme 6 task unit [E0]; Anthropic objective/boundaries [E1] |
  | Global constraints binding this task (Always·Block If·Never subset / path+§) | Theme 6 header [E0] |
  | Cross-task interfaces/decisions not in brief | Anthropic refs [E1]; SDD [E0] |
  | Out-of-scope / do-not | Theme 6 [E0]; Claude self-contained specs [E1] |
  | Report / status contract (what to return) | Anthropic output format [E1]; Theme 6 status vocab [E0] |
  | Artifact paths (diff/report/ledger) by reference | Anthropic filesystem refs [E1] |

  Premises: §4.2.1–4.2.2. **Not** a skill elevation.

- `GAP` Official Cursor Task-tool prompt schema / max sizes / inheritance rules as Execute SoT. Searched: Cursor public subagents docs only (2026-07-30). Result: published behavior (clean context; parent supplies prompt; parallel = multiple Task calls in one message) — **no invented API beyond that**. [E1: Subagents §Parallel execution — accessed 2026-07-30]

### 4.3 Serial default vs parallel-safe (Plan #2 — not Superpowers absolute ban)

- `FACT` [E0] Theme 6 **accepted #2**: `serial_implement_review` default for shared-checkout coding; parallel only when independence + exclusive file ownership (or worktrees) are stated in the plan. Template: Parallel-safe only `yes` if independence + exclusive writes or worktree stated. [E0: Theme 6 report; `plan-minimal.md` Execution notes — observed 2026-07-30]
- `FACT` [E1] Anthropic: domains needing **shared context** or **many inter-agent dependencies** (e.g. **most coding today**) are a weaker fit for multi-agent than high-parallel research; agents not yet great at real-time coordination. [E1: multi-agent-research-system — accessed 2026-07-30]
- `FACT` [E1] Anthropic parallelization: **sectioning** requires independent subtasks; use when parallelizable for speed or multiple perspectives. [E1: Building effective agents §Parallelization — accessed 2026-07-30]
- `FACT` [E1] Cursor: from a plan, **Build in Parallel** runs **independent** steps at once while keeping **dependent** steps ordered. [E1: What is multi-agent coding? — https://cursor.com/help/ai-features/multi-agent — accessed 2026-07-30]
- `FACT` [E1] Cursor: parallel agents commonly use **git worktrees** so edits don’t collide; subagent parallel capability documented as multiple Task tool calls in one message (capability statement only). [E1: Cursor blog agent-best-practices §Running agents in parallel — https://cursor.com/blog/agent-best-practices — accessed 2026-07-30; Subagents §Parallel execution — accessed 2026-07-30]
- `FACT` [E1] OpenAI Agents SDK: run multiple agents in parallel (e.g. `asyncio.gather`) when tasks **don’t depend on each other**. [E1: Agent orchestration — accessed 2026-07-30]
- `FACT` [E0] Superpowers SDD red flag (inventory): “Never … Dispatch multiple implementation subagents in parallel (conflicts).” [E0: SDD SKILL.md §Red Flags — observed 2026-07-30]
- `CLAIM` [E3] Superpowers never-parallel-implementers is **community process inventory**, not Toolbelt Execution law. [E3: same SKILL.md — inventory only]
- `INFERENCE` [E4] **Controller rule (Toolbelt-aligned):** default **serial** implement → review/verify on shared checkout. Fan-out writers **only** when the plan marks parallel-safe / independence **and** exclusive-write ownership or worktree isolation (Plan #2). Do **not** import Superpowers absolute ban as SoT — Plan #2 already scopes the exception. Premises: Theme 6 #2 [E0]; Anthropic coding caveat [E1]; Cursor independent steps + worktrees [E1]; OpenAI independence [E1]; SDD as E3 inventory only.

### 4.4 Task-level review vs end review; continuous exec when green

#### 4.4.1 Two review layers

- `FACT` [E1] Anthropic **evaluator-optimizer**: generate → evaluate/feedback loop when criteria are clear; agents may **pause for human feedback** at checkpoints or blockers. Coding agents: automated tests help; **human review remains crucial** for broader alignment. [E1: Building effective agents §§Evaluator-optimizer, Agents, Appendix coding agents — accessed 2026-07-30]
- `FACT` [E1] Claude Code: verification by **second opinion** — fresh subagent / Writer–Reviewer across sessions; **adversarial review** of the diff in a fresh context before treating work done; reviewer sees criteria/diff, not the writer’s reasoning. [E1: Best practices §§Give Claude a way to verify, Add an adversarial review step — accessed 2026-07-30]
- `FACT` [E1] Cursor: **verifier** subagent pattern after claimed completion; Planner → Implementer → Verifier; independent verification called out as a subagent use case. [E1: Subagents §§When to use, Common patterns — accessed 2026-07-30]
- `FACT` [E0] Superpowers SDD (inventory): **per-task** review (spec compliance + code quality) after each implementer; **final whole-branch** review after all tasks; fix Critical/Important before next task. [E0: SDD SKILL.md §§The Process, Constructing Reviewer Prompts — observed 2026-07-30]
- `CLAIM` [E2] Producer + reviewer separation yields more consistent outcomes; HITL as intentional step boundary (approval / clarification / escalation when grounding low — don’t guess). [E2: Alexandria corpus=`ai_llm_agents` source=`LlamaIndex… (Gheorghiu)` chunk_id=`eb26af7b81ef9539f023e63c`, `f6db83cbefcb3eb041e52205` query=`orchestrator worker controller…`]
- `CLAIM` [E2] Plan-based orchestrator evaluates each step before proceeding; on failure, **retry with enhanced instructions** from failure analysis (not blind retry). [E2: Alexandria corpus=`ai_llm_agents` source=`Dibia` chunk_id=`3468fcf7fbcea4d9fc928c5b`, `5d7b25d4e53679e4b569efd0` query=`orchestrator worker controller…`]
- `INFERENCE` [E4] **Broad-use review cadence for controller execute:**
  1. **Task-level gate** after each coding task (or parallel tranche): Done-when/verify evidence + optional fresh reviewer (spec vs plan packet + quality) — catches over/under-build early.
  2. **End review** once after all tasks: whole-change / branch-level coherence (cross-task gaps Claude/Cursor verifier patterns address).
  Premises: Claude adversarial + Writer/Reviewer [E1]; Cursor verifier [E1]; SDD two-layer inventory [E0/E3]; evaluator-optimizer [E1].

#### 4.4.2 Continuous execution vs HITL (campaign §7.1)

- `FACT` [E0] Campaign §7.1 human decision: **HITL between tasks** = escalate/ask on **major deviation or blocked** — not pause for every task when green. [E0: `docs/research/notes/theme-7-execute/campaign-brief.md` §7.1 — observed 2026-07-30]
- `FACT` [E0] Superpowers SDD continuous execution (inventory): do not pause between tasks; stop only for BLOCKED / ambiguity / all complete. [E0: SDD SKILL.md §Continuous execution — observed 2026-07-30]
- `FACT` [E1] Anthropic agents: pause for human at checkpoints **or blockers**; recommend stopping conditions. [E1: Building effective agents §Agents — accessed 2026-07-30]
- `CLAIM` [E2] Escalation when confidence/grounding low; clarification when underspecified — do not guess. Termination/human-delegation patterns prevent runaway execution. [E2: Alexandria corpus=`ai_llm_agents` chunk_id=`f6db83cbefcb3eb041e52205`, `aac1118a15bb5420d2dbd59a` query=`orchestrator worker controller…`]
- `INFERENCE` [E4] **Controller default:** when task verify + (if used) task review are green → mark task complete, update ledger/status, **continue to next task without human check-in**. Stop/ask when: blocked (intent-gap / verify-fail / needs-human per Plan vocab), major plan deviation, plan-vs-review conflict requiring human choice, or all tasks done (then end review). Premises: campaign §7.1 [E0]; Claude/Anthropic blockers [E1]; SDD continuous [E0/E3]; LlamaIndex don’t-guess [E2].

### 4.5 Broad-use vs niche (priority filter)

Campaign §7.1 / T7B priority: patterns usable across almost all implementations (SDD-like controller), not niche Build recipes.

| Dimension | Broad-use (prefer) | Niche (park / exclude from Execute SoT) |
|-----------|--------------------|----------------------------------------|
| Domain | Language-/stack-agnostic controller loop | React/Unity/… Build cookbooks |
| Coupling | Consumes Theme 6 plan fields + status vocab | Requires Superpowers/OpenSpec/BMAD runtime or their git/TDD packaging |
| Parallelism | Serial default + Plan #2 parallel-safe markers | Absolute never-parallel law **or** unconstrained parallel writers |
| Review | Task gate + end review + runnable Verify | Product-specific review scripts as mandatory SoT |
| HITL | Blocked / major deviation | Approve every task when green |
| Handoff | Packet = objective/I/O/boundaries/verify/path refs | Dump whole plan + chat history into every worker |
| Runtime | Method describes roles + packets; uses host subagents as available | Invent Task API / harness-specific spawn contracts |

- `INFERENCE` [E4] A pattern is **broad-use** iff it applies to nearly any Theme 6 plan on a shared coding agent host **without** importing a third-party skill runtime or domain Build ceremony. SDD-like **controller + fresh implementer + review layers + continuous-when-green** qualifies as broad-use **structure**; Superpowers scripts/worktrees/TDD/commit-every-task do not. Premises: campaign essence filter [E0]; Theme 6 non-imports [E0]; vendor orchestrator/verifier patterns [E1].

### 4.6 Local Superpowers inventory only (standalone Toolbelt)

- `FACT` [E0] Local SDD skill present with `implementer-prompt.md`, `task-reviewer-prompt.md`, `scripts/task-brief`, `scripts/review-package`; statuses `DONE` / `DONE_WITH_CONCERNS` / `NEEDS_CONTEXT` / `BLOCKED`; durable progress ledger. [E0: SDD directory under Superpowers cache — observed 2026-07-30]
- `CLAIM` [E3] Transferable **atoms** for later Execute design (not SoT): fresh implementer per task; file brief + report paths; task review then end review; continuous until blocked; progress ledger against compaction re-dispatch. Park: mandatory worktrees, TDD-in-every-task, commit-every-task, finishing-branch, absolute never-parallel. [E3: SDD SKILL.md — inventory only]
- `INFERENCE` [E4] Toolbelt should **inspire-from / extract atoms**, remain **standalone** — no Superpowers dependency (campaign §7.1). Premises: campaign brief [E0]; coexistence stance.

### 4.7 OpenAI Codex surface (fetch GAP)

- `GAP` Live OpenAI Codex best-practices and Codex concepts/subagents pages could not be retrieved this pass (WebFetch timeout; PowerShell `308 Permanent Redirect`). Searched: `https://developers.openai.com/codex/learn/best-practices`, `https://developers.openai.com/codex/concepts/subagents` — 2026-07-30. Result: **not fetched**. OpenAI **Agents SDK** orchestration doc used as E1 instead. W2 may re-fetch Codex if P0.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Broad-use controller = spine + per-task packets + fresh implementers + review layers | confirmed (literature + Plan alignment) | §4.1–4.2 |
| H2 | Serial default for shared-checkout coding; parallel only Plan #2 criteria | confirmed (Theme 6 accepted + vendor) | §4.3 |
| H3 | Continuous exec when green; HITL on blocked/major deviation | confirmed (campaign §7.1 + vendor/RAG) | §4.4.2 |
| H4 | Superpowers never-parallel must become Toolbelt law | rejected | Plan #2 supersedes; SDD = E3 inventory §4.3 |
| H5 | Task-level + end review both belong in broad-use controller | confirmed (pattern) | §4.4.1 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Parallel implementers | Superpowers: never parallel implementers [E0/E3] | Theme 6 #2 + Cursor/OpenAI: parallel when independent + isolation [E0/E1] | **Prefer Theme 6 accepted #2** as Toolbelt law. SDD ban = inventory corroborating conflict risk, not absolute ban. |
| HITL every step vs continuous | Some Osmani/HITL “approve steps” (Theme 7 normal scope E2/E3) | Campaign §7.1 + SDD continuous [E0]; Anthropic pause at blockers [E1] | **Campaign §7.1 wins for Theme 7:** continuous when green; escalate on blocked/major deviation. |
| Orchestrator sees all vs file refs | Dibia: orchestrator sees all [E2] | Anthropic: filesystem artifacts + refs [E1] | Compatible: controller holds spine/ledger; workers get packets/refs. Prefer E1 for bulky artifacts. |

## 7. Gaps & OPEN

- `GAP` OpenAI Codex best-practices / subagents primary page bodies (fetch failed 2026-07-30) — use Agents SDK E1 interim; W2 re-fetch if needed.
- `GAP` Cursor Task-tool internal prompt contract — out of scope; do not invent.
- `GAP` Live E0 Toolbelt controller trial measuring packet size / review latency — not run this wave.
- `OPEN` Whether task-level fresh reviewer is **required** every task vs **optional** when verify is strong (quality lean vs cost) — design/accept later; this note records both layers as pattern.
- `OPEN` Toolbelt-native implementer status enum vs adopt/adapt Superpowers statuses — defer to T7A/T7D + accept gate.
- `OPEN` Supplementary skill vs fold into main `execute-plan` spine — campaign §7.1 allows both; elevation post-accept only.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to Execution skill SoT without separate acceptance.

- `INFERENCE` [E4] **Answer (controller execute, broad-use):** Controller loads Theme 6 plan → optional pre-flight conflict scan → for each ready task (serial by default): build implementer packet (§4.2) → dispatch **fresh** implementer → collect report/verify evidence → task-level review gate → on green update status/ledger and **continue**; on fail fix-loop or escalate; after all tasks → end review. Parallel writers only if plan marks parallel-safe with independence + exclusive writes/worktrees (Plan #2). Premises: §§4.1–4.5.
- `INFERENCE` [E4] **Do not elevate skills from this draft.** Premises: `draft-is-not-sot`; campaign non-goals.
- `INFERENCE` [E4] **Supplementary broad-use skill candidate** (post-accept only): thin “subagent-driven execute” companion that teaches packet + review cadence — **without** Superpowers packaging. Premises: campaign §5/§7.1; §4.5 filter.

## 9. Source list (deduped)

1. Anthropic — Building effective agents — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-30 [E1]
2. Anthropic — How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-30 [E1]
3. Claude Code — Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-30 [E1]
4. Claude Code — Sub-agents — https://code.claude.com/docs/en/sub-agents — accessed 2026-07-30 [E1]
5. Cursor — Subagents — https://cursor.com/docs/subagents — accessed 2026-07-30 [E1]
6. Cursor — What is multi-agent coding? — https://cursor.com/help/ai-features/multi-agent — accessed 2026-07-30 [E1]
7. Cursor — Agent best practices (blog) — https://cursor.com/blog/agent-best-practices — accessed 2026-07-30 [E1]
8. OpenAI Agents SDK — Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-30 [E1]
9. Alexandria `ai_llm_agents` — Dibia chunks `3468fcf7fbcea4d9fc928c5b`, `5d7b25d4e53679e4b569efd0`, `aac1118a15bb5420d2dbd59a`, `a8f7795ae960fe72bed28eab`, `0a74058837b1785916371c87` [E2]
10. Alexandria `ai_llm_agents` — Gheorghiu chunks `eb26af7b81ef9539f023e63c`, `f6db83cbefcb3eb041e52205` (+ T6C `618afba9e60090c0249026d4`) [E2]
11. Theme 6 accepted report + `docs/templates/plan-minimal.md` [E0]
12. Theme 7 campaign-brief §7.1 [E0]
13. Superpowers cache — `subagent-driven-development/SKILL.md` + `implementer-prompt.md` — inventory only [E0/E3]
14. Theme 6 notes `t6c-w1-multiagent-plan-execution.md`, `t6-w2-exec-shape-serial-parallel.md` — prior gatherer corroboration [E0 draft path; facts re-checked against primary URLs this pass where cited as E1]

---

## Return summary (to parent)

**T7B W1 draft:** Controller = Theme 6 spine + **per-task packets** (objective/files/interfaces/Done-when/Verify/constraints/path refs — not chat dumps) → fresh implementer → **task review** → continue when green → **end review**. Serial default; parallel writers only Plan #2. HITL on blocked/major deviation (§7.1). SDD = transferable atoms / E3 inventory — **not** never-parallel Toolbelt law. Codex pages GAP; no Task API invented; no skills elevated.
