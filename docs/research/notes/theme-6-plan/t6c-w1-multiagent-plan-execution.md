---
title: "T6C W1 — Plans under 1..N agent execution (handoffs, isolation, gates)"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [grok-t6c-w1]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/PROTOCOL.md
---

# T6C W1 — Plans under 1..N agent execution

**Using `research-protocol`** · depth: **deep** · wave: **1** · slice: **T6C**.

## 1. Scope

- Question / goal: How should **plans** be composed when execution is by **one agent** or **multiple subagents** (often with fresh contexts)?
- In scope:
  1. Handoff / task-packet patterns; what each subagent needs in-context vs by reference
  2. Isolation vs shared state; review gates between tasks
  3. Failure/retry and “blocked → escalate to human/design” patterns **when sourced**
  4. Web E1/E2 on multi-agent SE / orchestrator-worker; Alexandria `ai_llm_agents` on multi-agent task plans/handoffs/subagents
  5. Local Superpowers `subagent-driven-development` as **E0/E3 inventory only** (no git/PR/TDD policy locks)
- Out of scope:
  - Inventing Cursor Task API / runtime spawn contracts
  - Re-opening Theme 4 plugin-agents wireup GAPs as product law (Theme 4 remains SoT for surfaces; residual GAPs stay non-locks)
  - Locking Superpowers execution skills as Toolbelt Plan SoT
  - Domain Build recipes; UX planning (T5C)
- Comprehension / research goal type: adaptive (shape Plan artifacts for 1..N execution)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol, Superpowers SKILL + implementer-prompt); WebSearch; WebFetch; Alexandria MCP `rag_probe` / `rag_query` |
| Corpora / URLs searched | Alexandria `ai_llm_agents`; Anthropic engineering (building-effective-agents, multi-agent-research-system); OpenAI Agents SDK multi_agent docs; false-friend probe on trading/finance agents |
| Queries (exact) | Web: `multi-agent software engineering orchestrator-worker pattern LLM agents handoff 2024 2025`; `Anthropic multi-agent research system orchestrator worker architecture`; `Anthropic building effective agents orchestrator-workers pattern site:anthropic.com`. Alexandria probe: `multi-agent task plans handoffs subagents orchestrator worker isolation review gates`; `agent handoff task packet context isolation shared state failure retry blocked escalate`; `multi-agent trading stock portfolio financial agents`. Alexandria query: `orchestrator worker multi-agent handoff task decomposition fresh context isolation subagent review`; `task packet agent handoff shared state failure retry blocked escalate human review gate software engineering plan` |
| What was *not* searched | Cursor product Task/subagent API as SoT; Theme 4 residual E0 harnesses; AutoGen/CrewAI primary docs beyond RAG hits; GitHub issues/forums as design locks; runtime experiments spawning parallel implementers |
| Depth | deep |
| Waves / stop_reason | Wave 1 primary SoT + RAG corroboration for T6C only. `stop_reason`: **wave1_slice_coverage** — Method + findings cover the three MUST axes with E1/E2/E0 citations; remaining items are W2 deepeners or named GAPs (no invent Cursor Task API). Campaign-level W2/W3/integrate owned by coordinator. |
| Provenance (optional PROV) | Entity←Anthropic/OpenAI docs + Alexandria chunks + Superpowers cache files; Activity=T6C W1 gather; Agent=cursor-grok-4.5-high-fast |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Plan composition question spans external multi-agent literature (systematic web+RAG) plus local Superpowers inventory (as-needed path read) |
| Scope boundary | Included: plan/task-packet shape, isolation, gates, failure/escalation patterns. Excluded: inventing Task tool behavior; Theme 4 plugin-agent load-path reopen |

## 4. Findings

### 4.1 Architectural primitives (1 agent vs N)

- `FACT` [E1] Anthropic distinguishes **workflows** (predefined code paths) from **agents** (LLM directs process/tools); recommends simplest solution first and adding multi-step/multi-agent complexity only when it improves outcomes. [E1: Building effective agents — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-29]
- `FACT` [E1] **Orchestrator-workers**: a central LLM dynamically breaks down tasks, delegates to worker LLMs, and synthesizes results; suited when subtasks cannot be predicted in advance (e.g. coding multi-file changes, multi-source search). Distinct from fixed parallelization because decomposition is input-dependent. [E1: Building effective agents §Orchestrator-workers — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-29]
- `FACT` [E1] Anthropic Research uses orchestrator-worker: lead agent plans, persists plan to Memory (context truncation risk), spawns specialized subagents with separate context windows in parallel, synthesizes, optionally iterates, then CitationAgent for attribution. [E1: How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-29]
- `CLAIM` [E1] Anthropic reports multi-agent Research (Opus lead + Sonnet subagents) outperformed single-agent Opus by **90.2%** on an internal research eval for breadth-first queries; also reports ~**15×** tokens vs chat for multi-agent (vs ~**4×** for single agents). [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Anthropic states some domains needing **shared context** or **many inter-agent dependencies** (e.g. most coding today) are a weaker fit for multi-agent than high-parallel research; “LLM agents are not yet great at coordinating and delegating to other agents in real time.” [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents SDK: two LLM-orchestration patterns — **agents as tools** (manager keeps control, specialists via `Agent.as_tool()`) vs **handoffs** (specialist becomes active agent). Code orchestration: chaining, evaluator loops, parallel `asyncio.gather` for independent tasks. [E1: Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-29]
- `CLAIM` [E2] Plan-based orchestration: orchestrator maintains explicit task plans/assignments/dependencies; **orchestrator sees all context**; other agents receive **only relevant information**; state centralized in orchestrator. Software-dev example: research → coding with selective context from prior step. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)` chunk_id=`3468fcf7fbcea4d9fc928c5b` query=`orchestrator worker multi-agent handoff…`]
- `CLAIM` [E2] Handoff pattern: peer-to-peer transfer; each agent has limited visibility; **state explicitly passed** during handoff; risks cycles without careful design. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)` chunk_id=`3468fcf7fbcea4d9fc928c5b` / `042a4d786a445aac926afc13` query=`orchestrator worker…` / `task packet…`]

### 4.2 Handoff / task-packet patterns (in-context vs by reference)

- `FACT` [E1] Lead→subagent delegation should include: **objective**, **output format**, **guidance on tools/sources**, and **clear task boundaries**. Vague instructions (“research the semiconductor shortage”) caused duplicated/misaligned work. [E1: multi-agent-research-system §Teach the orchestrator how to delegate — accessed 2026-07-29]
- `FACT` [E1] Scale effort to complexity via explicit guidelines (e.g. simple fact-finding: 1 agent / 3–10 tool calls; comparisons: 2–4 subagents; complex: >10 with divided responsibilities). [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Appendix pattern: store large subagent outputs on a **filesystem / artifact store** and pass **lightweight references** to the coordinator (“minimize the game of telephone”); works well for structured outputs (code, reports). [E1: multi-agent-research-system Appendix — accessed 2026-07-29]
- `FACT` [E1] Long-horizon: summarize completed phases into external memory; spawn **fresh subagents with clean contexts** while retrieving stored plan/context for continuity. [E1: multi-agent-research-system Appendix — accessed 2026-07-29]
- `CLAIM` [E2] Structured handoffs should feel like **internal APIs**, not free-form chat. A good handoff includes: user goal (one sentence); brief prior actions/results; key facts (+ provenance); open question for the receiver; constraints (e.g. no writes). Benefits: diagnosable routing vs tool vs reasoning failures. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex… (Andrei Gheorghiu)` chunk_id=`618afba9e60090c0249026d4` query=`orchestrator worker multi-agent handoff…`]
- `CLAIM` [E2] Common orchestration shapes: router+specialists; **planner and workers** (concrete sub-tasks, narrow instructions/tool menus); **producer and reviewer**. Theme: clear identity + limited surface area. [E2: Alexandria corpus=`ai_llm_agents` source=`LlamaIndex… (Gheorghiu)` chunk_id=`618afba9e60090c0249026d4` query=`orchestrator worker…`]
- `FACT` [E0] Superpowers SDD (local skill text): fresh subagent per task; controller **constructs** context — subagents “should never inherit your session’s context or history.” Dispatch should carry: (1) one-line fit in project; (2) **task brief path** as requirements SoT; (3) interfaces/decisions from earlier tasks the brief cannot know; (4) ambiguity resolutions; (5) report-file path/contract. Exact values live in the brief, not pasted history. [E0: path=`…/superpowers/…/skills/subagent-driven-development/SKILL.md` §§Why subagents, File Handoffs — observed 2026-07-29]
- `FACT` [E0] Superpowers red flag: do **not** make a subagent read the whole plan file — hand a **task brief** (`scripts/task-brief`). Do not paste accumulated prior-task summaries into later dispatches. [E0: same SKILL.md §§File Handoffs, Red Flags — observed 2026-07-29]
- `FACT` [E0] Implementer prompt template: read brief first; scene-setting context; ask clarifying questions before work; escalate with `BLOCKED` / `NEEDS_CONTEXT`; write full report to report file. [E0: path=`…/subagent-driven-development/implementer-prompt.md` — observed 2026-07-29]
- `INFERENCE` [E4] For Toolbelt **Plan** artifacts under multi-agent execution, each executable unit should be composable as a **task packet**: self-contained objective + acceptance/output contract + boundaries + constraints + pointers (paths) to design/specs/artifacts by reference — not a dump of controller chat history. Premises: (1) Anthropic delegation fields [E1]; (2) LlamaIndex handoff fields [E2]; (3) Superpowers brief+paths pattern [E0/E3].
- `GAP` Cursor-specific Task-tool prompt schema / max sizes / inheritance rules for plugin agents. Searched: not in this slice by design (out: invent Task API; Theme 4 residual GAPs not reopened as law). Result: **no product lock from this note**.

### 4.3 Isolation vs shared state; review gates

- `FACT` [E1] Subagents facilitate compression via **parallel separate context windows**; separation of concerns (distinct tools, prompts, trajectories) reduces path dependency. [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Lead agent currently runs subagents **synchronously** (waits for batches); simplifies coordination but blocks steering/cross-subagent coordination; async noted as future tradeoff (state consistency, error propagation). [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Evaluator-optimizer workflow: one LLM generates, another evaluates/feedbacks in a loop when criteria are clear and iteration helps. [E1: Building effective agents §Evaluator-optimizer — accessed 2026-07-29]
- `FACT` [E1] Agents may pause for human feedback at checkpoints or blockers; stopping conditions (e.g. max iterations) recommended. [E1: Building effective agents §Agents — accessed 2026-07-29]
- `CLAIM` [E2] Orchestrator selective visibility vs conversation-driven **broadcast** shared history (group chat) — different state models; pick by predictability vs flexibility needs. [E2: Alexandria corpus=`ai_llm_agents` source=`Dibia` chunk_id=`3468fcf7fbcea4d9fc928c5b` / `042a4d786a445aac926afc13` / `0a74058837b1785916371c87`]
- `CLAIM` [E2] Shared memory / durable conversation state enables pause/resume and handoff after crashes; naive env-var state loses recovery. Concurrency needs versioning/rollback when multiple agents update shared state. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh… (Broda)` chunk_id=`77ee369ab3c127110d065034` query=`task packet…`]
- `CLAIM` [E2] Guardrails for orchestration: per-agent tool permissions; structured output schemas; iteration limits; restricted handoff routes; explicit stop when retrieval empty; traceable execution. [E2: Alexandria corpus=`ai_llm_agents` source=`LlamaIndex… (Gheorghiu)` chunk_id=`f1a1778b3dcd57d0448bb822` query=`orchestrator worker…`]
- `FACT` [E0] Superpowers SDD process: implementer → **task reviewer** (spec compliance + code quality) → fix loop → mark complete; **final whole-branch review** after all tasks. Continuous execution between tasks unless BLOCKED / ambiguity / complete. [E0: SKILL.md §§The Process, Continuous execution — observed 2026-07-29]
- `FACT` [E0] Superpowers: durable **progress ledger** file (not only todos/chat) because compaction can cause expensive re-dispatch of completed tasks. [E0: SKILL.md §Durable Progress — observed 2026-07-29]
- `FACT` [E0] Superpowers red flag: do **not** dispatch multiple **implementation** subagents in parallel (conflicts). Reviewers/fixers are separate roles in the loop. [E0: SKILL.md §Red Flags — observed 2026-07-29]
- `INFERENCE` [E4] Plans for N-agent execution should separate **shared durable state** (plan file, progress ledger, artifact paths, global constraints) from **private worker context** (task packet + only needed interfaces). Review gates belong in the plan as checkable exits between tasks (or producer→reviewer roles), not as optional vibes. Premises: Anthropic Memory/artifacts [E1]; Dibia selective context [E2]; Superpowers ledger+review [E0/E3].
- `OPEN` When Toolbelt plans should prefer **serial implementers + review** (SDD-like) vs **parallel research-style workers** for coding — Anthropic hedges coding parallelism [E1]; Superpowers forbids parallel implementers [E0/E3]. Follow-up: T6B/T6A + W2, not a W1 lock.

### 4.4 Failure, retry, blocked → escalate

- `FACT` [E1] Production agents: durable execution, resume from failure (not full restart), combine model adaptability with retries/checkpoints; compound errors make minor failures catastrophic without mitigations. [E1: multi-agent-research-system §Production reliability — accessed 2026-07-29]
- `CLAIM` [E2] Plan-based orchestrator: evaluate each step before proceeding; on failure, **retry with enhanced instructions** from failure analysis (targeted feedback, not blind retry). [E2: Alexandria corpus=`ai_llm_agents` source=`Dibia` chunk_id=`3468fcf7fbcea4d9fc928c5b` / `5d7b25d4e53679e4b569efd0` query=`orchestrator worker…` / `task packet…`]
- `CLAIM` [E2] Human-in-the-loop gates: approval for high-stakes actions; clarification when underspecified (don’t guess); **escalation when confidence/grounding is low** (“could not find policy text…”). Production: durable pause, timeouts, resume. [E2: Alexandria corpus=`ai_llm_agents` source=`LlamaIndex… (Gheorghiu)` chunk_id=`f6db83cbefcb3eb041e52205` query=`task packet…`]
- `CLAIM` [E2] HITL escalation criteria examples: persistent unexplained errors; regulatory/ethical anomalies; high-value/mission-critical failures; conflicting automated recommendations; prioritize low certainty × high consequence. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents… (Michael Albada)` chunk_id=`9a4a77548eeb379fd593d576` query=`task packet…`]
- `CLAIM` [E2] Agents must escalate errors/ambiguous states/critical decisions to humans; transparent reporting vs silent ignore. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`748eb643c5a65c6363f7cc16` query=`task packet…`]
- `FACT` [E0] Superpowers implementer statuses: `DONE` | `DONE_WITH_CONCERNS` | `NEEDS_CONTEXT` | `BLOCKED`. For BLOCKED: (1) more context + re-dispatch; (2) stronger model; (3) break into smaller pieces; (4) **if plan itself is wrong → escalate to human**. Never force same model retry unchanged. [E0: SKILL.md §Handling Implementer Status — observed 2026-07-29]
- `FACT` [E0] Plan-mandated findings that conflict with review: present finding + plan text to **human**; do not auto-dismiss or auto-fix against plan. Pre-flight plan conflict scan before Task 1. [E0: SKILL.md §§Pre-Flight Plan Review, Constructing Reviewer Prompts — observed 2026-07-29]
- `INFERENCE` [E4] Plan text should name **failure exits**: retry-with-feedback vs re-slice task vs escalate-to-human (and when to reopen Design). Premises: Dibia retry [E2]; Superpowers BLOCKED ladder [E0/E3]; LlamaIndex/Albada escalation [E2].
- `GAP` Toolbelt-owned vocabulary for plan-level status enums (`BLOCKED` etc.) — only observed in Superpowers community skill [E0/E3], not adopted as Toolbelt law in this note.

### 4.5 False friends / rejected retrieval

- `FACT` [E0] Alexandria probe `multi-agent trading stock portfolio financial agents` returned **strong** coverage led by finance/agentic-mesh titles (e.g. *Agent AI for Finance*). **Not used** for Plan composition claims (domain false friend). [E0: rag_probe corpus=`ai_llm_agents` 2026-07-29]
- `CLAIM` [E2] RAG cookbook “orchestrator-workers” chunk describes SQL/wiki/LLM workers for document Q&A — pattern name matches, but content is **agentic RAG infra**, not software task-plan authoring. Used only as weak pattern corroboration, not Plan SoT. [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook… (Dominik Polzer)` chunk_id=`2e3a61e3945d02c7b5d35de7` query=`orchestrator worker…`]
- `GAP` CrewAI/LangGraph/AutoGPT framework comparison chunks discuss role sequencing/shared memory but are secondary product guides; not elevated to Plan locks. [E2 weak: Alexandria chunk_id=`5ed70c111a48d85aeeb66348` — discovery only]

### 4.6 Local Superpowers inventory (E0/E3 — structure only)

- `FACT` [E0] Skill present at `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\subagent-driven-development\SKILL.md` with companion `implementer-prompt.md`, `task-reviewer-prompt.md`, `scripts/task-brief`, `scripts/review-package`. [E0: path listing/read 2026-07-29]
- `CLAIM` [E3] SDD encodes a **controller + per-task implementer + per-task reviewer + final branch reviewer** workflow with file-based briefs/reports/ledger. Community skill; **not** Toolbelt Plan SoT; **no** git/worktree/TDD policy merge from this note (per campaign brief). [E3: same SKILL.md — inventory only]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Multi-agent plans need per-task packets (objective, format, boundaries, constraints) plus path references for bulky artifacts | confirmed (literature) | Anthropic [E1]; LlamaIndex [E2]; Superpowers [E0] |
| H2 | Shared chat history across all workers is a poor default for plan execution | confirmed (selective context preference) | Dibia visibility [E2]; Anthropic fresh contexts [E1]; Superpowers no session inherit [E0] |
| H3 | Coding plans should default to parallel implementers | rejected / open conflict | Anthropic coding fit caveat [E1]; Superpowers forbids parallel implementers [E0] — leave OPEN for Toolbelt |
| H4 | Review gates between tasks improve fidelity vs fire-and-forget task lists | confirmed (pattern) | Evaluator-optimizer [E1]; producer-reviewer [E2]; SDD task review [E0] |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Parallel implementers for coding | Anthropic: multi-agent weaker when many dependencies / coding often less parallelizable [E1] | Superpowers: never parallel implementation subagents [E0/E3] | Prefer higher-grade Anthropic caution for *when* multi-agent helps; treat Superpowers parallel ban as community process inventory. Toolbelt: **OPEN** — no lock. |
| Orchestrator keeps all context vs file-reference handoffs | Dibia: orchestrator sees all [E2] | Anthropic appendix: filesystem artifacts + refs to avoid telephone [E1] | Not contradictory if “sees all” = coordinator role while workers get packets/refs. Prefer E1 artifact pattern for bulky outputs. |
| Plan wrong vs implementer stuck | Superpowers: escalate plan defects to human [E0] | LlamaIndex: escalate when grounding insufficient [E2] | Compatible: distinguish **missing context** (re-dispatch) vs **wrong/underspecified plan/design** (human/design). |

## 7. Gaps & OPEN

- `GAP` Official Cursor Task / subagent dispatch contract as Plan authoring SoT — out of scope; do not invent.
- `GAP` Theme 4 plugin-agents ↔ runtime Subagents wireup — **remain Theme 4 residual GAPs**; not reopened here as Plan law.
- `OPEN` Default serial vs parallel execution policy for Toolbelt coding plans (see Conflicts).
- `OPEN` Whether Plan template should adopt Superpowers-like status vocabulary (`DONE` / `BLOCKED` / …) or a Toolbelt-native set after acceptance.
- `OPEN` W2: deepen with AutoGen/LangGraph primary docs only if needed to close a named P0; prefer not to expand false-friend RAG.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design/Plan lock without separate acceptance.

- `INFERENCE` [E4] **Compose plans as a controller-readable spine + per-task packets.** The spine holds ordering, dependencies, global constraints, and progress hooks; each packet is executable by a fresh context with objective, I/O contract, boundaries, verify steps, and path references to design/research/artifacts. Premises: §4.2.
- `INFERENCE` [E4] **Default isolation: private worker context; shared durable artifacts.** Prefer file/ledger/memory for shared state over pasting session history into every dispatch. Premises: §4.3.
- `INFERENCE` [E4] **Put review gates in the plan** when N>1 or quality risk is high (task-level producer→reviewer and/or end-of-plan broad review). Single-agent execution can collapse packet sequence into one context but should still keep verify exits. Premises: §4.3; Anthropic start-simple [E1].
- `INFERENCE` [E4] **Name escalation exits in the plan:** retry-with-feedback → re-slice → escalate to human (and reopen Design when the plan/design is wrong). Premises: §4.4.
- `INFERENCE` [E4] Multi-agent is a **Plan composition concern** (packetization, isolation, gates) separate from **orchestration runtime** product APIs — do not wait on Theme 4 GAP closure to draft Plan methods, and do not invent Cursor Task API to fill the gap. Premises: campaign brief cautions; §4.2 GAP; Theme 4 out.

## 9. Source list (deduped)

1. Anthropic — Building effective agents — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-29 [E1]
2. Anthropic — How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-29 [E1]
3. OpenAI Agents SDK — Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-29 [E1]
4. Alexandria `ai_llm_agents` — Dibia, *Designing Multi-Agent Systems* — chunk_ids=`3468fcf7fbcea4d9fc928c5b`, `042a4d786a445aac926afc13`, `0a74058837b1785916371c87`, `5d7b25d4e53679e4b569efd0` [E2]
5. Alexandria `ai_llm_agents` — Gheorghiu, *Building Data-Driven Applications with LlamaIndex* — chunk_ids=`618afba9e60090c0249026d4`, `1b65ee4b38cae2e581a07c60`, `f1a1778b3dcd57d0448bb822`, `f6db83cbefcb3eb041e52205` [E2]
6. Alexandria `ai_llm_agents` — Broda, *Agentic Mesh* — chunk_id=`77ee369ab3c127110d065034` [E2]
7. Alexandria `ai_llm_agents` — Albada, *Building Applications with AI Agents* — chunk_ids=`9a4a77548eeb379fd593d576`, `748eb643c5a65c6363f7cc16` [E2]
8. Alexandria `ai_llm_agents` — Polzer, *RAG with Python Cookbook* — chunk_id=`2e3a61e3945d02c7b5d35de7` (false-friend watch / weak pattern only) [E2]
9. Superpowers cache — `skills/subagent-driven-development/SKILL.md` + `implementer-prompt.md` — observed 2026-07-29 [E0 inventory / E3 community process]
10. Theme 6 campaign brief / T6 coordinator pin — path=`docs/research/notes/theme-6-plan/` — scope only [E0]
