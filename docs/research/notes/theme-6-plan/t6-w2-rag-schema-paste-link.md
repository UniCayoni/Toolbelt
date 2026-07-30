---
title: "T6-W2 — RAG corroboration: paste-vs-link + portable task schema"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6-w2-rag-schema-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6-coordinator-pin.md
  - docs/research/notes/theme-6-plan/t6a-w1-plan-for-fresh-agents.md
  - docs/research/notes/theme-6-plan/t6b-w1-design-to-plan-decompose.md
  - docs/research/notes/theme-6-plan/t6c-w1-multiagent-plan-execution.md
  - docs/PROTOCOL.md
---

# T6-W2 — RAG corroboration: paste-vs-link + portable task schema

**Using `research-protocol`**; depth: **deep**; wave: **2**; slice: **T6-W2-RAG-SCHEMA**.

**Status:** `draft`. Not Plan SoT. No skill elevation. Does not reopen Theme 5 Design locks.

## 1. Scope

- Question / goal: Corroborate or weaken W1 FACTs on Goal/Constraints/Done-when, fresh context, and task packets via Alexandria RAG; attack GAPs on **paste-vs-link budget** and **portable agent task schema** fields; assess RAG diminishing returns.
- In scope:
  - Alexandria `ai_llm_agents` + `software_engineering` probes/queries on plans for coding agents, handoffs, acceptance criteria, context engineering, WBS/story slicing
  - False-friend watch (robotics path planning; trading/finance agents)
  - Optional WebFetch for Gherkin Given-When-Then / PMI WBS wording
  - CLAIM/INFERENCE synthesis of schema field candidates only when multi-source overlap
- Out of scope:
  - Elevating Toolbelt Plan skills/templates
  - Inventing Cursor Task API contracts
  - Importing Superpowers git/TDD/PR policy as Toolbelt law
  - Wave-3 fleet expansion beyond this slice’s named GAPs
- Comprehension / research goal type: other (method corroboration)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (research-protocol, research-note template, T6A/T6B/T6C W1 notes); Alexandria MCP `rag_probe` → `rag_query` → `rag_fetch_chunk`; WebFetch (Gherkin; PMI library page failed; Wikipedia WBS timed out) |
| Corpora / URLs searched | Alexandria `ai_llm_agents`, `software_engineering`; https://cucumber.io/docs/gherkin/reference/ ; attempted https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063 (error page); attempted https://en.wikipedia.org/wiki/Work_breakdown_structure (timeout) |
| Queries (exact) | **Probes:** `writing implementation plans for coding agents task handoffs acceptance criteria context engineering`; `WBS work breakdown story slicing implementation tasks acceptance criteria from design`; `context engineering what to put in prompt vs retrieve by reference file path identifiers just-in-time`; `agent task specification schema fields files dependencies acceptance criteria constraints do not`; `software task specification template files ownership dependencies acceptance criteria design reference`; false friends: `robotics path planning motion planning agents`; `multi-agent trading stock portfolio financial agents`. **Queries:** `How to write implementation plans and task specifications for coding agents including goal constraints done-when acceptance criteria and fresh context handoffs?`; `context engineering what content must be inlined in agent prompt versus file path references just-in-time retrieval lightweight identifiers for large documents`; `structured agent task handoff packet fields objective output format constraints files dependencies acceptance criteria do-not boundaries`; `decompose design into work packages tasks dependencies acceptance criteria definition of done for implementation planning WBS story slicing`; `software implementation task template specifying files ownership dependencies acceptance criteria design document references`; `AI coding agent implementation plan WBS subtasks dependencies acceptance criteria from feature or design`; `software engineering agent system prompt structure workflow understand requirements read code make changes test verify constraints`. **Fetch:** chunk_ids `629850574ac1748fb1093cf7`, `6daf3081f797c0c94712cce0`, `8b7602d0a9c3407c72c5673d`, `054c45ce9edf298e82ce235a`, `a3ca188700ea420507cf33e2` |
| What was *not* searched | Full PMI Practice Standard PDF (paywall; PMI library page errored this pass); MIL-STD-881F; live E0 Toolbelt plan trials; BMAD/story-packet vendor schemas; Cursor Task API; GitHub plan-skill inventories (T6D); AutoGen/LangGraph primary beyond RAG hits |
| Depth | deep |
| Waves / stop_reason | wave: **2**; slice: **T6-W2-RAG-SCHEMA**. `stop_reason`: **rag_diminishing_returns** — probes mostly `partial`; high-signal hits largely restate T6A/T6B/T6C W1 clusters (Dibia selective context/deps, Gheorghiu handoff fields, Dooley AC/SMART, Osmani WBS/deps) plus a few new secondary scaffolds (Broda slotting/tiers; Dibia completion-criteria wording; Funderburk Write/Select/Compress/Isolate). Named GAPs (numeric paste budget; portable JSON field schema as SoT) **not** closable by further secondary-book RAG. Prefer confirmed GAP over more weak E2/E3. |
| Provenance (optional PROV) | Entity←Alexandria chunks + Cucumber Gherkin + W1 notes; Activity=T6-W2 RAG corroboration; Agent=cursor-grok gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | Wave-2 mandate: probe then query both named corpora; fetch neighbors for contested locators; optional primary deepen for AC/WBS wording only |
| Scope boundary | Corroboration + GAP attack for paste/schema; no Plan skill elevation |

## 4. Findings

### 4.0 False friends (rejected)

- `FACT` [E0] Probe `robotics path planning motion planning agents` on `ai_llm_agents` returned **partial** coverage led by *Multi-Agent Coordination A Reinforcement Learning Approach* (robotics/RL coordination). **Not used** for Plan document claims. [E0: rag_probe corpus=`ai_llm_agents` 2026-07-29]
- `FACT` [E0] Probe `multi-agent trading stock portfolio financial agents` returned **strong** coverage (*Agent AI for Finance*, Agentic Mesh finance-adjacent). **Not used** for Plan composition claims (domain false friend; same watch as T6C W1). [E0: rag_probe corpus=`ai_llm_agents` 2026-07-29]
- `CLAIM` [E2] CrewAI/AutoGen *travel itinerary* Task examples (`description` + `expected_output`) illustrate product task objects, not coding-plan SoT — discovery only. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems.pdf` chunk_id=`8929e3c72616dcd94f05acef` query=`How to write implementation plans…`]

### 4.1 Corroboration — Goal / Constraints / Done-when

W1 anchors (T6A): Codex Goal/Context/Constraints/Done-when [E1]; Claude verify/e2e [E1]; Anthropic altitude/no false shared context [E1].

- `CLAIM` [E2] Osmani (*Beyond Vibe Coding*): **plan-first** AI-assisted engineering begins by outlining what to build and defining **constraints and acceptance criteria up front** (mini-PRD or checklist) before AI generation; example spec names responsibilities, API, error handling, design-system constraints. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani).epub` chunk_id=`054c45ce9edf298e82ce235a` query=`AI coding agent implementation plan WBS…`]
- `CLAIM` [E2] Osmani: AI may draft a plan/WBS from a feature/user story, suggest subtasks, and **highlight dependencies** so ordering is logical; humans still prioritize. [E2: same corpus/source chunk_id=`9605dd89df91f04c7f7bafda` — also cited T6B W1]
- `CLAIM` [E2] Broda (*Agentic Mesh*): context quality needs structure; typical scaffolding includes a **brief objective**, **constraints**, available **tools with signatures**, current **state**, and a clear **“next-action”** request; **slotting** reserves prompt sections for “must include” items such as safety rules, APIs, or constraints. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh… (Broda).pdf` chunk_id=`629850574ac1748fb1093cf7` / neighbor `6daf3081f797c0c94712cce0` query=`context engineering what content must be inlined…`]
- `CLAIM` [E2] Dibia (*Designing Multi-Agent Systems*): for SE agents, **completion criteria are critical** — if “done” is vague the agent stops prematurely; spell out what done means: **all planned steps complete, tests passing, code documented**; structured prompts use phases including **verification** and **completion**. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia).epub` chunk_id=`a3ca188700ea420507cf33e2` query=`software engineering agent system prompt structure…`]
- `FACT` [E2] Dooley & Kazakova: product owner writes **acceptance criteria** that become acceptance tests; this is typically the agile **definition of “done”**; unclear AC ⇒ restart story conversation. [E2: Alexandria corpus=`software_engineering` source=`Software Development, Design, and Coding… (Dooley & Kazakova).pdf` chunk_id=`354cdc82c80fb36bc1bc52b8` query=`decompose design into work packages…` — corroborates T6B W1]
- `CLAIM` [E2] Winteringham (*Software Testing with Generative AI*): vague LLM prompts yield vague outputs; valuable prompts include feature text plus explicit **Acceptance criteria** bullets (formats, limits, progress, access, audit). [E2: Alexandria corpus=`software_engineering` source=`Software Testing with Generative AI… (Mark Winteringham).pdf` chunk_id=`15b5921982321fd433f00230` query=`software implementation task template…`]
- `FACT` [E1] Cucumber Gherkin: examples follow **Given** (initial context) / **When** (event) / **Then** (expected outcome); Feature free-form text may document business rules as general acceptance criteria. [E1: Cucumber Docs — Gherkin Reference — https://cucumber.io/docs/gherkin/reference/ — accessed 2026-07-29]
- `INFERENCE` [E4] W1 Goal/Constraints/Done-when cluster is **corroborated** (not weakened) by secondary SE/agent literature: constraints+AC up front (Osmani), must-slot constraints (Broda), explicit completion/tests (Dibia), AC↔done (Dooley), optional Gherkin GWT as AC *syntax* (Cucumber E1). Premises: bullets above + T6A Codex/Claude E1. **No elevation** of a locked checklist.

### 4.2 Corroboration — fresh context / isolation

W1 anchors (T6A/T6C): Cursor/Claude clean subagent contexts [E1]; Anthropic fresh subagents + artifact refs [E1].

- `CLAIM` [E2] Funderburk: core context strategies Write / Select / Compress / **Isolate** — Isolate splits work into sub-agents with **clean, isolated context windows**; subagent returns a **distilled summary** to the supervisor (cites Anthropic 2025 among others). [E2: Alexandria corpus=`ai_llm_agents` source=`Building Natural Language and LLM Pipelines… (Laura Funderburk).pdf` chunk_id=`5e77dfb7df87ae61d3934d0c` query=`context engineering what content must be inlined…`]
- `CLAIM` [E2] Dibia: plan-based orchestration — orchestrator sees all context; **other agents receive only relevant information**; SE example passes selective research context into coding step to prevent overload. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Dibia).epub` chunk_id=`3468fcf7fbcea4d9fc928c5b` query=`structured agent task handoff…` — also T6C W1]
- `CLAIM` [E2] Albada: prioritize relevance; avoid indiscriminately appending large blocks; use summarization; assemble context dynamically per step. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents… (Michael Albada).pdf` chunk_id=`4b9a08fc084f85631bcc5c68` query=`context engineering what content must be inlined…`]
- `INFERENCE` [E4] Fresh-context / selective-packet FACTs from W1 are **corroborated** by RAG secondary sources (Isolate + selective visibility + anti-dump). Premises: Funderburk; Dibia; Albada; T6A/T6C E1 product docs. Broadcast group-chat shared history remains a **competing pattern** (Dibia conversation-driven) — same conflict logged in T6C; for Toolbelt plans aimed at Cursor/Claude-style fresh subagents, prefer clean-brief model.

### 4.3 Corroboration — task packets / handoffs

W1 anchors (T6C): Anthropic delegation fields [E1]; Gheorghiu structured handoff [E2]; Superpowers task brief [E0/E3].

- `CLAIM` [E2] Gheorghiu (*LlamaIndex*): good handoffs resemble **internal APIs**, including: user goal (one sentence); brief prior actions/results; key facts (+ provenance); open question for receiver; **constraints** (e.g. “do not execute write actions”). [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex… (Andrei Gheorghiu).epub` chunk_id=`618afba9e60090c0249026d4` query=`structured agent task handoff…` — also T6C W1]
- `CLAIM` [E2] Broda scaffolding (objective, constraints, tools, state, next-action) overlaps the same packet shape for *in-prompt* working sets. [E2: chunk_id=`629850574ac1748fb1093cf7` — §4.1]
- `CLAIM` [E2] Devlin: Executor inputs include **task instructions** from Planner and contextual data; outputs deliverables in the **requested format** plus status/artifacts; Evaluator compares output to Planner intent using measurable criteria. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG… (Mira S. Devlin).pdf` chunk_id=`1743f89b302e91fc2dd6c232` query=`How to write implementation plans…`]
- `CLAIM` [E2] Dibia SE agent: capabilities = tools + prompts + context engineering; mentoring analogy workflow: understand requirements → read existing code → incremental changes → **test** → debug → document; prompts must define completion and error handling. [E2: chunk_ids=`b6ad313a03312c92aa6ef1e0`, `0500925c70044c07eff46c04`, `a3ca188700ea420507cf33e2`]
- `INFERENCE` [E4] W1 “task packet” cluster is **corroborated**: objective + constraints/do-not + I/O or expected format + selective context + verify/done. Premises: Gheorghiu; Broda; Devlin; Dibia; T6C Anthropic E1.

### 4.4 GAP attack — paste-vs-link budget

**Target GAP (T6A W1):** No E1 universal “how many lines of ADR/design to paste vs link.”

- `CLAIM` [E2] Broda: memory **tiers** — prompt = hot/working; middle tier = compact summaries/open tasks; **long-term tier** = complete artifacts (documents, logs) accessed **selectively via retrieval**; slotting for must-include constraints/APIs/safety. Answers *what/how/when* for context, **not** a line-count paste budget for design docs. [E2: chunk_ids=`6daf3081f797c0c94712cce0`, `629850574ac1748fb1093cf7`]
- `CLAIM` [E2] Funderburk Write/Select/Compress/Isolate: externalize bulky info; JIT retrieve; compress/summarize; isolate subagent mess — again principles, not ADR paste quotas. [E2: chunk_id=`5e77dfb7df87ae61d3934d0c`]
- `CLAIM` [E2] Albada: include only useful retrieved snippets; compress histories; each extra element can help or distract/token-bloat. [E2: chunk_id=`4b9a08fc084f85631bcc5c68`]
- `INFERENCE` [E4] Secondary literature **supports hybrid** “inline binding decisions + path/retrieve for bulky rationale” (aligns with T6A W1 INFERENCE and Anthropic JIT identifiers [E1 from W1]) but **does not** supply a Toolbelt-grade citation budget (N lines / % of context / mandatory paste set). Premises: Broda tiers/slotting; Funderburk Select/Compress; Albada relevance; T6A GAP statement.
- `GAP` **Paste-vs-link numeric/policy budget still open.** Searched this wave: Alexandria probes/queries above on both corpora; WebFetch Gherkin (AC syntax only); PMI Practice Standard library page (error); Wikipedia WBS (timeout — W1 already holds E2 WBS summary). Result: **principles yes; universal paste budget no.** Closing would need E1 vendor plan-authoring SoT, accepted Toolbelt convention after trials, or E0 experiments — not more secondary RAG.

### 4.5 GAP attack — portable agent task schema fields

**Target GAP (T6B W1):** No E1 schema mandating `{design_section_id, files[], owner, deps[], acceptance[]}`.

Candidate fields from **multi-source overlap** only (CLAIM/INFERENCE — **not elevated**):

| Candidate field | Overlap sources (grade) | Notes |
|-----------------|-------------------------|-------|
| `goal` / objective | Broda scaffolding [E2]; Gheorghiu handoff [E2]; Osmani plan-first [E2]; Codex Goal [E1 W1] | Strong overlap |
| `constraints` + `do_not` / never | Broda must-slot constraints [E2]; Gheorghiu constraints example [E2]; Codex Constraints [E1 W1]; Albada task boundaries [E2] | Strong overlap; naming varies |
| `acceptance` / `verify` / done-when | Osmani AC [E2]; Dibia completion criteria [E2]; Dooley AC→done [E2]; Claude/Codex verify [E1 W1]; optional Gherkin GWT [E1] | Strong overlap; syntax not standardized |
| `deps` | Dibia plan assignments/dependencies [E2]; Osmani highlight dependencies [E2]; PMI sequencing [E2 W1] | Strong for ordering; not a coding-agent JSON schema |
| `files[]` / path touch list | Dibia file tools + SE workflow [E2]; Osmani identify utilities/API [E2]; Superpowers Files [E0 W1] | Medium—tools imply paths; few books mandate a `files[]` field |
| `design_ref` / path+extract | Broda cold-tier artifact retrieval [E2]; Anthropic lightweight identifiers [E1 W1]; T6A link+binding excerpts INFERENCE | Medium—path refs common; “extract instruction” rarely formalized |
| `consumes` / `produces` (interfaces) | Superpowers Interfaces [E0 W1]; Dibia structured output / handoff state [E2]; Gheorghiu I/O facts [E2] | Weaker naming overlap; treat as CLAIM candidate only |
| `output_format` / expected_output | Gheorghiu open question + format discipline [E2]; CrewAI `expected_output` [E2 product]; Devlin requested format [E2] | Medium |

- `INFERENCE` [E4] A **candidate** portable packet (non-lock) that survives multi-source overlap: `{ goal, constraints|do_not[], acceptance|verify[], deps[], files[]?, design_ref?, consumes/produces?, output_format? }` — with `?` = weaker overlap. Premises: table above. **Do not elevate** to Toolbelt schema without accept wave + trials (`draft-is-not-sot`).
- `GAP` Still no E1/E2 **standard portable schema** (named fields + required/optional) for coding-agent implementation tasks. Searched: Alexandria schema/template queries on both corpora; W1 vendor docs already negative for universal schema. Result: **principles + candidate field bag; no SoT schema.**
- `FACT` [E2] Dooley SMART tasks: story→tasks must be **specific, measurable, achievable, relevant, time-boxed**; tasks “maximally specific… including any relevant details.” Supports specificity of packets, not a field list. [E2: chunk_id=`8b7602d0a9c3407c72c5673d`]

### 4.6 WBS / AC wording deepen (optional)

- `FACT` [E2] Dooley INVEST/SMART/AC material re-retrieved — corroborates T6B W1 story→task→AC chain; no new WBS primary this wave. [E2: chunk_ids=`354cdc82c80fb36bc1bc52b8`, `8b7602d0a9c3407c72c5673d`, `9cd6adc27e6ed16132dea90c`, `ef8c7f22c527ab2c2fd82869`, `1c545ae73acd19c9d0a4730c`]
- `GAP` PMI Practice Standard primary PDF / live PMI library article not obtained this pass (error page). Rely on T6B W1 E2 Wikipedia/PMI secondary for 100% rule until a successful primary fetch.
- `FACT` [E1] Gherkin Given-When-Then is a primary **syntax** for executable examples/AC; vendors in T6A still prefer Done-when/verify/tests without mandating Gherkin. [E1: Cucumber Gherkin reference — accessed 2026-07-29]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W1 Goal/Constraints/Done-when is stable under RAG secondary corroboration | confirmed (this wave) | §4.1 |
| H2 | Fresh-context / selective packets are stable under RAG | confirmed (this wave) | §4.2–4.3 |
| H3 | RAG will yield a numeric paste-vs-link budget | rejected | §4.4 GAP |
| H4 | RAG will yield an E1 portable task JSON schema | rejected | §4.5 GAP |
| H5 | Further Alexandria queries on these topics will mainly restate W1 | confirmed | Method stop_reason; repeat chunk_ids from T6B/T6C |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Shared history vs clean packets | Dibia conversation-driven broadcast [E2] | Funderburk Isolate + Dibia selective orchestrator [E2]; Cursor/Claude clean context [E1 W1] | For Toolbelt *plan docs* for fresh coding subagents: prefer selective/clean packet; leave OPEN product-specific history handoffs (T6C) |
| AC syntax | Gherkin GWT [E1] | Codex Done-when / Claude verify [E1 W1]; Dooley AC bullets [E2] | Role of AC is corroborated; **syntax** OPEN (GWT optional, not mandatory) |
| Schema formality | Superpowers Files+Interfaces+Expected [E0/E3 W1] | Books: principles without fixed field names [E2] | Inventory + candidate fields only; no Toolbelt lock |

## 7. Gaps & OPEN

### Corroborated cluster (stable after W2 RAG)

- Goal + Constraints + Done-when/AC/verify
- Fresh / isolated worker context + selective task packets
- Structured handoff contents (goal, prior/results, facts, open question, constraints/do-not)
- Story→SMART tasks→AC for decomposition (SE textbook + W1 Wake/Cohn)

### Remaining GAPs

- `GAP` Paste-vs-link **budget** (what must be inlined vs path+extract) — principles only; no E1/E2 numeric or mandatory paste set. Searched: §2 queries + optional PMI/Gherkin.
- `GAP` Portable agent task **schema as SoT** — candidate field bag only (§4.5); no elevation.
- `GAP` PMI Practice Standard primary text this wave (fetch failed).
- `OPEN` Whether Toolbelt adopts Gherkin GWT, bullet AC, or verify-command+Expected as default AC form.
- `OPEN` E0 Toolbelt trials measuring hallucination rate for paste-heavy vs link+binding-excerpt plans.
- `OPEN` Integrator merge into Theme 6 draft report (coordinator).

### RAG diminishing returns

- **Yes — diminishing returns for this slice.** Probe verdicts mostly `partial`; strongest “strong” hit was a **false friend** (trading). New unique signal this wave: Broda tiers/slotting; Dibia completion-criteria wording; Funderburk Isolate/Write-Select-Compress; Osmani plan-first AC chunk; Cucumber GWT E1. Remaining P0 GAPs need vendor SoT, human convention, or E0 trials — not another book-RAG pass on the same questions.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to Plan lock without Theme 6 accept + elevation.

- `INFERENCE` [E4] Wave-2 RAG **reinforces** writing plans as self-contained packets (goal, constraints/do-not, acceptance/verify, deps, path refs) for fresh agents; it does **not** unlock a paste-character budget or a frozen JSON schema. Premises: §§4.1–4.5.
- `INFERENCE` [E4] For paste-vs-link drafting guidance (still non-SoT): **inline** objective, binding constraints/do-not, interfaces/decisions, and verify/done; **link** long design/ADR/research with an extract instruction (“read §X Decision/Interfaces”) — justified by Broda hot/cold tiers + W1 Anthropic JIT, not by a measured budget. Premises: §4.4; T6A §4.2 INFERENCE.
- `INFERENCE` [E4] Candidate schema fields in §4.5 are fit for a **future proposed** plan template checklist after accept — not for mid-research elevation. Premises: multi-source overlap table; `draft-is-not-sot`.

## 9. Source list (deduped)

1. Alexandria `ai_llm_agents` — Broda, *Agentic Mesh* — chunk_ids=`629850574ac1748fb1093cf7`, `6daf3081f797c0c94712cce0` [E2]
2. Alexandria `ai_llm_agents` — Dibia, *Designing Multi-Agent Systems* — chunk_ids=`3468fcf7fbcea4d9fc928c5b`, `042a4d786a445aac926afc13`, `b6ad313a03312c92aa6ef1e0`, `0500925c70044c07eff46c04`, `a3ca188700ea420507cf33e2` [E2]
3. Alexandria `ai_llm_agents` — Gheorghiu, *LlamaIndex…* — chunk_id=`618afba9e60090c0249026d4` [E2]
4. Alexandria `ai_llm_agents` — Funderburk, *Building Natural Language and LLM Pipelines…* — chunk_ids=`5e77dfb7df87ae61d3934d0c`, `5768caf2a6a0b9bd0b58c5d1` [E2]
5. Alexandria `ai_llm_agents` — Albada, *Building Applications with AI Agents…* — chunk_id=`4b9a08fc084f85631bcc5c68` [E2]
6. Alexandria `ai_llm_agents` — Devlin, *Building LLM Agents with RAG…* — chunk_id=`1743f89b302e91fc2dd6c232` [E2]
7. Alexandria `software_engineering` — Osmani, *Beyond Vibe Coding* — chunk_ids=`054c45ce9edf298e82ce235a`, `9605dd89df91f04c7f7bafda`, `eb18ff3000ac18694b4d981d`, `6ba1a4cb341d5260f63eeafd` [E2]
8. Alexandria `software_engineering` — Dooley & Kazakova — chunk_ids=`354cdc82c80fb36bc1bc52b8`, `8b7602d0a9c3407c72c5673d`, `9cd6adc27e6ed16132dea90c`, `ef8c7f22c527ab2c2fd82869`, `1c545ae73acd19c9d0a4730c` [E2]
9. Alexandria `software_engineering` — Winteringham, *Software Testing with Generative AI* — chunk_id=`15b5921982321fd433f00230` [E2]
10. Cucumber — Gherkin Reference — https://cucumber.io/docs/gherkin/reference/ — accessed 2026-07-29 [E1]
11. W1 notes (skimmed) — `t6a-w1-plan-for-fresh-agents.md`, `t6b-w1-design-to-plan-decompose.md`, `t6c-w1-multiagent-plan-execution.md` — E0 campaign continuity / prior citations
12. False-friend probes — robotics path planning; trading agents — rejected [E0]
