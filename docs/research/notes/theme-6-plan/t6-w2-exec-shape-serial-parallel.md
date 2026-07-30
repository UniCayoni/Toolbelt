---
title: "T6-W2-EXEC-SHAPE — Serial implementers+review vs parallel workers; plan markers"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [grok-t6-w2-exec-shape]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6c-w1-multiagent-plan-execution.md
  - docs/PROTOCOL.md
---

# T6-W2-EXEC-SHAPE — Execution shape for plans (serial vs parallel)

**Using `research-protocol`** · depth: **deep** · wave: **2** · slice: **T6-W2-EXEC-SHAPE**.

## 1. Scope

- Question / goal: Deepen T6C `OPEN` — when plans should encode **serial implementers + review** vs **parallel workers** (research-style vs coding), and how the **plan document** should mark parallel-safety, review gates, single-writer ownership, and escalate-to-human triggers — **only with citations**.
- In scope:
  1. Decision criteria for serial coding/review vs parallel research/independent workers
  2. Plan-document markers / fields supported by E1/E0 evidence (or explicitly marked GAP if sources lack a prescribed token)
  3. Anthropic multi-agent / Claude Code + OpenAI Agents SDK + Cursor docs (fetchable); Superpowers SDD as E0/E3 inventory only
  4. Optional Alexandria short probe; reject trading/RAG-infra false friends
- Out of scope:
  - Inventing Cursor Task API / spawn contracts beyond published product docs
  - Elevating Superpowers or any Plan skills to Toolbelt SoT
  - Locking git/worktree/TDD policy from community skills
  - Domain Build recipes; UX planning (T5C)
- Comprehension / research goal type: adaptive (shape Plan artifact execution annotations)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol template, T6C W1 note, Superpowers `subagent-driven-development/SKILL.md`); WebSearch; WebFetch (Anthropic engineering, OpenAI Agents SDK, Claude Code docs, Cursor docs); Alexandria MCP `rag_probe` |
| Corpora / URLs searched | Anthropic building-effective-agents + multi-agent-research-system; OpenAI Agents SDK multi_agent; Claude Code sub-agents / agent-teams / worktrees / best-practices; Cursor subagents + multi-agent help + worktrees; Alexandria `ai_llm_agents` probe only |
| Queries (exact) | Web: `Cursor IDE parallel agents subagents Task tool documentation best practices`; `Claude Code parallel agents subagents best practices site:docs.anthropic.com OR site:code.claude.com`; `Cursor plan Build in Parallel independent steps worktrees file conflicts documentation`. Alexandria probe: `when to run parallel agents vs serial for coding implementation file conflicts worktree ownership review gates` |
| What was *not* searched | Cursor Task tool internal/private API schemas; AutoGen/LangGraph primary docs (W1 deferred unless P0); runtime experiments spawning parallel implementers; trading/finance agent corpora as Plan law |
| Depth | deep |
| Waves / stop_reason | Wave 2 deepen of T6C OPEN only. `stop_reason`: **diminishing_returns** — E1 sources converge on independence / shared-context / file-ownership criteria; Alexandria probe `partial` dominated by false friends (n8n workflows, RAG cookbook); no further primary SoT found for a prescribed `[P]` token or Toolbelt-native status enum. Residual GAPs listed; no invent Task API. |
| Provenance (optional PROV) | Entity←Anthropic/OpenAI/Claude Code/Cursor docs + Superpowers cache + T6C; Activity=T6-W2-EXEC-SHAPE gather; Agent=cursor-grok-4.5 |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Execution-shape question needs external product/engineering SoT (systematic fetch) plus local Superpowers red-flag verification (as-needed path read) |
| Scope boundary | Included: serial vs parallel criteria; plan markers with citations. Excluded: inventing Task API; elevating skills; Theme 4 residual wireup |

## 4. Findings

### 4.1 When parallel workers fit (research-style / independent fan-out)

- `FACT` [E1] Anthropic Research multi-agent systems excel especially for **breadth-first** queries with multiple **independent** directions; subagents operate in parallel with separate context windows as compression/separation of concerns. [E1: How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Anthropic: parallelization workflow has two forms — **sectioning** (independent subtasks in parallel) and **voting** (same task multiple times); use when subtasks are parallelizable for speed or multiple perspectives are needed. [E1: Building effective agents §Parallelization — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-29]
- `FACT` [E1] Anthropic Research: for speed, lead spins **3–5 subagents in parallel** (not serially) and subagents call **3+ tools in parallel**; cut research time up to ~90% on complex queries. [E1: multi-agent-research-system §Prompt engineering — accessed 2026-07-29]
- `FACT` [E1] OpenAI Agents SDK (code orchestration): run multiple agents in parallel (e.g. `asyncio.gather`) when tasks **don't depend on each other**. [E1: Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-29]
- `FACT` [E1] Claude Code: for independent investigations, spawn multiple subagents simultaneously; “works best when the research paths don't depend on each other.” [E1: Subagents — https://code.claude.com/docs/en/sub-agents — accessed 2026-07-29]
- `FACT` [E1] Claude Code agent teams: strongest when parallel exploration adds value; examples include research + analysis and debugging with competing hypotheses; “work best when teammates can operate independently.” [E1: Agent teams — https://code.claude.com/docs/en/agent-teams — accessed 2026-07-29]
- `FACT` [E1] Claude Code: if new to agent teams, start with clear-boundary tasks that **don't require writing code** (PR review, library research, bug investigation) to get parallel value without parallel-implementation coordination. [E1: Agent teams §Start with research and review — accessed 2026-07-29]
- `FACT` [E1] Cursor: use subagents for long research, **parallel workstreams**, or independent verification; built-in Explore uses a faster model enabling many parallel searches. [E1: Subagents — https://cursor.com/docs/subagents — accessed 2026-07-29]
- `FACT` [E1] Cursor help: from a plan, **Build in Parallel** runs **independent** steps at once while keeping **dependent** steps in order. [E1: What is multi-agent coding? — https://cursor.com/help/ai-features/multi-agent — accessed 2026-07-29]

### 4.2 When serial implementers + review fit (coding / high dependency)

- `FACT` [E1] Anthropic: domains needing **shared context** or **many inter-agent dependencies** (e.g. **most coding today**) are a weaker fit for multi-agent than high-parallel research; “LLM agents are not yet great at coordinating and delegating to other agents in real time.” [E1: multi-agent-research-system — accessed 2026-07-29]
- `FACT` [E1] Anthropic: orchestrator-workers is well-suited for coding products making complex multi-file changes where subtasks can't be predicted in advance — **distinct from fixed parallelization** because decomposition is input-dependent (does **not** claim unconstrained parallel implementers on one checkout). [E1: Building effective agents §Orchestrator-workers — accessed 2026-07-29]
- `FACT` [E1] Anthropic: evaluator-optimizer (generate → evaluate/feedback loop) when criteria are clear and iteration helps; agents may **pause for human feedback** at checkpoints or blockers. [E1: Building effective agents §§Evaluator-optimizer, Agents — accessed 2026-07-29]
- `FACT` [E1] Anthropic coding agents: automated tests help verify functionality, but **human review remains crucial** for alignment with broader system requirements. [E1: Building effective agents Appendix 1 §Coding agents — accessed 2026-07-29]
- `FACT` [E1] Claude Code agent teams: for **sequential tasks, same-file edits, or work with many dependencies**, a single session or subagents are more effective than teams. [E1: Agent teams — accessed 2026-07-29]
- `FACT` [E1] Claude Code best practices: adversarial review — before treating work as done, have a subagent review the diff in a **fresh context**; Writer/Reviewer across sessions so the reviewer is not biased by having written the code. [E1: Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29]
- `FACT` [E1] Cursor common pattern: orchestrator sequence **Planner → Implementer → Verifier** with structured handoffs; separate verifier subagent validates claimed completion. [E1: Subagents §§Common patterns — accessed 2026-07-29]
- `FACT` [E1] OpenAI: chaining + evaluator-in-a-loop patterns for sequential refine-until-criteria-pass flows. [E1: Agent orchestration — accessed 2026-07-29]
- `FACT` [E0] Superpowers SDD (local skill text): process is dispatch **one implementer** → **task reviewer** → fix loop → next task; final whole-branch review after all tasks. Red flag: **Never** “Dispatch multiple implementation subagents in parallel (conflicts).” [E0: path=`C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99\skills\subagent-driven-development\SKILL.md` §§The Process, Red Flags — observed 2026-07-29]
- `CLAIM` [E3] Superpowers parallel-implementer ban is community process inventory, not Toolbelt Plan SoT; corroborates conflict risk but does not alone lock Toolbelt policy. [E3: same SKILL.md — inventory only]
- `INFERENCE` [E4] **Default for coding plans with shared mutable checkout / many task dependencies: serial implementer + review gate per task (or per dependency tranche).** Prefer parallel workers when work is read-mostly research, independent verification lenses, or explicitly independent file/ownership slices (with isolation). Premises: Anthropic coding multi-agent caveat [E1]; Claude same-file/deps guidance [E1]; Cursor independent-vs-dependent plan steps [E1]; Superpowers parallel ban [E0/E3].

### 4.3 File isolation vs context isolation (parallel coding hazards)

- `FACT` [E1] Claude Code: “Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.” [E1: Agent teams §Avoid file conflicts — accessed 2026-07-29]
- `FACT` [E1] Claude Code worktrees: isolate parallel sessions/subagents in separate git worktrees so edits don't collide; `isolation: worktree` on custom subagents; worktrees isolate file edits while subagents/teams coordinate work. [E1: Worktrees — https://code.claude.com/docs/en/worktrees.md — accessed 2026-07-29]
- `FACT` [E1] Cursor worktrees: use when starting several agents on the same repo **without conflicts**; each task gets isolated checkout; `/worktree` and `/best-of-n` isolate runs. [E1: Worktrees — https://cursor.com/docs/configuration/worktrees — accessed 2026-07-29]
- `FACT` [E1] Cursor: parallel subagent launch = multiple Task tool calls in one message (product docs describe capability; this note does **not** invent Task API schemas beyond that published statement). [E1: Subagents §Parallel execution — https://cursor.com/docs/subagents — accessed 2026-07-29]
- `FACT` [E1] Cursor: subagents start with clean context; parent must include needed info in the prompt (context isolation ≠ automatic file isolation). [E1: Subagents §How subagents work — accessed 2026-07-29]
- `GAP` Official Cursor primary doc stating that `/multitask` alone provides filesystem isolation (vs context isolation only). Searched: Cursor multi-agent help + subagents + worktrees (2026-07-29). Result: worktrees docs cover file isolation; multi-agent help covers Build in Parallel / independent steps; **no** fetched E1 page equating multitask with file isolation. Secondary blogs claim context-only multitask — treat as **U/E3**, not Plan lock.
- `INFERENCE` [E4] Plans that authorize parallel **writers** should either (a) assign **non-overlapping file sets** (single-writer ownership) on one checkout, or (b) require **worktree/branch isolation** per worker, plus a later merge/apply gate. Parallel **readers/researchers/reviewers** do not need writer ownership. Premises: Claude file-ownership [E1]; Claude/Cursor worktrees [E1]; Anthropic shared-context coding caveat [E1].

### 4.4 How the plan document should mark execution shape

Sources describe **criteria and workflows**; they do **not** prescribe a universal Toolbelt token like `[P]`. Markers below are either directly sourced language or labeled `INFERENCE` candidates.

#### 4.4.1 Parallel-safe (`[P]` candidate)

- `FACT` [E1] Cursor plan UI language: run **independent** steps in parallel; keep **dependent** steps ordered. [E1: multi-agent help — accessed 2026-07-29]
- `FACT` [E1] OpenAI: parallel when tasks don't depend on each other. [E1: Agent orchestration — accessed 2026-07-29]
- `FACT` [E1] Anthropic parallelization: sectioning requires **independent** subtasks. [E1: Building effective agents — accessed 2026-07-29]
- `GAP` A prescribed literal marker `[P]` / `parallel-safe` in Anthropic, OpenAI, Claude Code, or Cursor plan authoring SoT. Searched: fetched primary docs above + Superpowers writing-plans (lists files per task; no `[P]` token observed). Result: **not found**.
- `INFERENCE` [E4] **Guidance candidate:** mark a task `[P]` (or `parallel-safe: true`) only when the plan asserts **all** of: no required outputs from incomplete peer tasks; non-overlapping writer ownership **or** worktree isolation; read/research/verify role if overlapping files. Absence of `[P]` means serial or dependency-ordered. Premises: Cursor independent/dependent [E1]; OpenAI independence [E1]; Claude ownership [E1]; GAP on token name.

#### 4.4.2 Review gates

- `FACT` [E1] Anthropic prompt-chaining: programmatic **gates** on intermediate steps; evaluator-optimizer loops; human checkpoints/blockers. [E1: Building effective agents — accessed 2026-07-29]
- `FACT` [E1] Claude Code: adversarial/fresh-context review before treating work done; `/code-review` skill reviews current diff in a fresh subagent. [E1: Best practices — accessed 2026-07-29]
- `FACT` [E1] Cursor: Verifier subagent pattern after claimed completion; Planner→Implementer→Verifier sequence. [E1: Subagents — accessed 2026-07-29]
- `FACT` [E0] Superpowers: per-task review (spec + quality) required; never skip; final whole-branch review. [E0: SDD SKILL.md — observed 2026-07-29]
- `INFERENCE` [E4] **Guidance candidate:** each coding task (or parallel tranche) should name a **review gate**: what is checked (spec/tests/diff), who/role (fresh reviewer vs same agent), and pass/fail exit before dependents start. Research-only parallel fan-out may gate at **synthesis** instead of per-worker code review. Premises: Anthropic gates/evaluator [E1]; Claude/Cursor verifier patterns [E1]; SDD [E0/E3].

#### 4.4.3 Single-writer file ownership

- `FACT` [E1] Claude Code: break work so each teammate **owns a different set of files**. [E1: Agent teams §Avoid file conflicts — accessed 2026-07-29]
- `FACT` [E0] Superpowers writing-plans: each task lists exact files to create/modify; “A task's implementer sees only their own task.” [E0: path=`…/superpowers/…/skills/writing-plans/SKILL.md` — observed 2026-07-29]
- `INFERENCE` [E4] **Guidance candidate:** for any `[P]` writing task, plan lists **Files (exclusive write):** paths; overlapping write paths ⇒ not parallel-safe unless worktree-isolated with an explicit merge gate. Premises: Claude ownership [E1]; Superpowers per-task Files [E0/E3]; Cursor/Claude worktrees [E1].

#### 4.4.4 Escalate-to-human triggers

- `FACT` [E1] Anthropic: agents pause for human feedback at checkpoints or blockers; stopping conditions (e.g. max iterations) recommended. [E1: Building effective agents §Agents — accessed 2026-07-29]
- `FACT` [E0] Superpowers: stop continuous execution for BLOCKED unresolved, genuine ambiguity, or completion; BLOCKED ladder ends with **escalate to human if the plan itself is wrong**; plan-vs-review conflicts presented to human. [E0: SDD SKILL.md §§Continuous execution, Handling Implementer Status, Constructing Reviewer Prompts — observed 2026-07-29]
- `CLAIM` [E2] (carried from T6C, not re-fetched) HITL escalation when underspecified / low grounding / high-stakes — LlamaIndex & Albada via Alexandria. [E2: see T6C §4.4 citations — not re-probed as SoT here]
- `INFERENCE` [E4] **Guidance candidate:** plan Global Constraints (or per-task exits) should name escalate-to-human when: plan/design contradiction; unresolved ambiguity blocking progress; repeated failure after feedback; high-stakes irreversible actions; confidence/grounding insufficient. Premises: Anthropic checkpoints [E1]; Superpowers BLOCKED/plan-wrong [E0/E3]; T6C E2 HITL [E2].

### 4.5 Alexandria probe (optional) — false friends rejected

- `FACT` [E0] `rag_probe` corpus=`ai_llm_agents` question=`when to run parallel agents vs serial for coding implementation file conflicts worktree ownership review gates` → coverage_verdict **partial**; top sources led by n8n beginner handbook, LlamaIndex, *AI Agents in Action*, **RAG with Python Cookbook**, agentic workflow titles. [E0: Alexandria rag_probe 2026-07-29]
- `FACT` [E0] Per campaign caution and T6C precedent: **RAG-infra / workflow-automation / trading** hits are false friends for software task-plan execution shape — **not used** as Plan SoT in this note. No `rag_query` follow-up (diminishing returns vs fresh E1 product docs). [E0: Method decision 2026-07-29]
- `GAP` Alexandria chunk that states a normative serial-vs-parallel coding policy comparable to Anthropic’s coding multi-agent caveat. Searched: probe above. Result: partial/noisy; not elevated.

### 4.6 Hypothesis resolution (vs T6C H3)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H3 (from T6C) | Coding plans should default to parallel implementers | **rejected as default** (still OPEN on exact Toolbelt template syntax) | Anthropic weaker fit for most coding [E1]; Claude same-file/deps → single session [E1]; Superpowers forbids parallel implementers [E0]; Cursor allows parallel only for **independent** plan steps [E1] |
| H5 (this slice) | Parallel is default-good for research/explore/review fan-out | confirmed (literature) | Anthropic Research [E1]; Claude parallel research [E1]; Cursor Explore/parallel workstreams [E1] |
| H6 | Plan docs need an explicit independence + ownership annotation for parallel writers | confirmed (need); token name OPEN | Criteria E1; `[P]` token GAP |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Research-style work is the primary green zone for parallel workers | confirmed | Anthropic Research [E1]; Claude [E1]; Cursor [E1] |
| H2 | Coding on shared checkout defaults to serial implementer + review | confirmed (as guidance candidate, not accepted SoT) | Anthropic [E1]; Claude [E1]; Superpowers [E0/E3] |
| H3 | Parallel coding writers require file ownership XOR worktree isolation | confirmed (pattern) | Claude ownership + worktrees [E1]; Cursor worktrees [E1] |
| H4 | Sources prescribe a literal `[P]` plan marker | rejected / GAP | No E1 token found |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Parallel for coding | Anthropic: most coding weaker multi-agent fit [E1]; Superpowers: never parallel implementers [E0/E3] | Cursor: parallel subagents / Build in Parallel for independent steps [E1]; Claude teams can refactor modules in parallel if independent [E1] | **Compatible if scoped:** parallel coding only when independence + non-overlapping writes or worktree isolation; else serial+review. No Toolbelt lock of Superpowers ban as absolute law. |
| Orchestrator-workers for coding | Anthropic lists coding multi-file as orchestrator-workers use case [E1] | Same Anthropic Research post: coding often less parallelizable [E1] | Orchestrator **decomposition** ≠ free parallel writers; prefer dynamic serial/batched workers with synthesis, not unchecked same-checkout parallelism. |
| Context isolation vs file isolation | Cursor/Claude: subagents isolate context [E1] | Worktrees isolate files [E1] | Plans must not treat “spawn parallel subagents” as file-safe; mark ownership or worktree requirement explicitly. |

## 7. Gaps & OPEN

- `GAP` Prescribed plan-authoring token `[P]` / schema field in Cursor/Anthropic/OpenAI SoT — not found; candidate only (§4.4.1).
- `GAP` Official Cursor E1 page clarifying multitask filesystem vs context isolation (secondary blogs only).
- `GAP` Toolbelt-owned status vocabulary for escalate exits (`BLOCKED` etc.) — still only Superpowers inventory [E0/E3] (T6C OPEN retained).
- `GAP` Invented Cursor Task API contracts — out of scope; only published “multiple Task tool calls in one message” fact used.
- `OPEN` Exact markdown/YAML shape for Toolbelt Plan template (marker names, required fields) — needs Design/acceptance; this note supplies **guidance candidates** only.
- `OPEN` Whether parallel **reviewers** on the same diff (Claude “parallel code review” lenses) should be default for high-risk tasks — sourced as pattern, not Toolbelt policy.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to Plan skill or design lock without separate acceptance.

**Guidance candidates (INFERENCE only):**

1. `INFERENCE` [E4] **Encode a default execution shape in the plan spine:** `exec_default: serial_implement_review` for coding plans that share a checkout; allow `parallel_ok` tranches only for tasks meeting independence criteria. Premises: §4.2–4.3.
2. `INFERENCE` [E4] **Mark parallel-safe tasks explicitly** (candidate tag `[P]` / `parallel-safe`) with: independence statement, exclusive write paths **or** `isolation: worktree`, and synthesis/merge gate. Unmarked = serial/dependency-ordered. Premises: §4.4.1; token GAP.
3. `INFERENCE` [E4] **Put review gates in the plan** after each coding task (or after each parallel writer tranche): fresh-context verify against acceptance criteria; research fan-out may gate at lead synthesis. Premises: §4.4.2.
4. `INFERENCE` [E4] **Single-writer ownership table** (task → exclusive files) for any parallel writers; overlapping writes without worktrees ⇒ reject `[P]`. Premises: §4.4.3.
5. `INFERENCE` [E4] **Name escalate-to-human triggers** in Global Constraints: plan/design wrong; ambiguity; repeated failure; high-stakes actions. Premises: §4.4.4.
6. `INFERENCE` [E4] **Do not elevate** Superpowers SDD or Cursor Task internals to Toolbelt Plan SoT from this draft; use as E0/E3 inventory + E1 product docs only. Premises: campaign brief; draft-is-not-sot.

**Stop signal:** `diminishing_returns` — primary E1 docs converge; Alexandria partial/false-friend; residual items are template-syntax OPENs for acceptance, not more web/RAG fan-out.

## 9. Source list (deduped)

1. Anthropic — Building effective agents — https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-29 [E1]
2. Anthropic — How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-29 [E1]
3. OpenAI Agents SDK — Agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/ — accessed 2026-07-29 [E1]
4. Claude Code — Subagents — https://code.claude.com/docs/en/sub-agents — accessed 2026-07-29 [E1]
5. Claude Code — Agent teams — https://code.claude.com/docs/en/agent-teams — accessed 2026-07-29 [E1]
6. Claude Code — Worktrees — https://code.claude.com/docs/en/worktrees.md — accessed 2026-07-29 [E1]
7. Claude Code — Best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-29 [E1]
8. Cursor — Subagents — https://cursor.com/docs/subagents — accessed 2026-07-29 [E1]
9. Cursor — What is multi-agent coding? — https://cursor.com/help/ai-features/multi-agent — accessed 2026-07-29 [E1]
10. Cursor — Worktrees — https://cursor.com/docs/configuration/worktrees — accessed 2026-07-29 [E1]
11. Superpowers cache — `skills/subagent-driven-development/SKILL.md` (+ writing-plans Files field) — observed 2026-07-29 [E0 inventory / E3 community]
12. T6C W1 — `docs/research/notes/theme-6-plan/t6c-w1-multiagent-plan-execution.md` — prior OPEN / E2 HITL carry [E0 path]
13. Alexandria `ai_llm_agents` — rag_probe only (false friends rejected; no chunk SoT) — 2026-07-29 [E0]
