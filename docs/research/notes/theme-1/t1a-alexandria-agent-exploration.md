# Theme 1 / Slice A — Agent exploration & codebase comprehension (notes)

Status: notes only (not integrated report)  
Agent id: `t1a-alexandria-agent-exploration`  
Date: 2026-07-27  
Corpora: `ai_llm_agents` (primary), `software_engineering` (secondary)

---

## 1. Scope

How multi-agent / coding-agent systems should **explore, research, and comprehend** codebases/workspaces **before** documenting or implementing. Focus: literature patterns from Alexandria RAG (`ai_llm_agents`, plus `software_engineering` where useful). Out of scope: GreyMatter product design locks, plugin scaffolding, library choice.

---

## 2. Method

**Tools:** MCP `user-alexandria-rag` — `list_corpora`, `rag_probe`, `rag_query` (k≥12 where noted), `rag_fetch_chunk` (+ neighbors for high-value chunks). Schemas fetched via `GetMcpTools` first.

**Corpora observed (E0):** `ai_llm_agents` (71 docs / 22720 chunks); `software_engineering` (21 docs / 7712 chunks). [E0: MCP `list_corpora` observed 2026-07-27]

### Exact questions queried

**Probes (`rag_probe`):**

1. How should multi-agent or coding agents explore and comprehend a codebase or workspace before documenting or implementing changes? (`ai_llm_agents` → weak; `software_engineering` → partial)
2. agent exploration codebase research understanding before coding (`ai_llm_agents` → partial)
3. multi-agent systems gather context observe environment before acting (`ai_llm_agents` → partial)
4. coding agent tools search files grep navigate repository comprehension (`ai_llm_agents` → partial)
5. AI coding agent explore codebase understand architecture before implementing (`software_engineering` → partial)
6. ReAct plan observe reason tool use research phase (`ai_llm_agents` → partial)
7. grep search before editing find patterns explore project structure list directory (`ai_llm_agents` → weak)

**Queries (`rag_query`):**

1. How should agents explore research and comprehend a codebase or workspace before documenting or implementing? (`ai_llm_agents`, k=14)
2. How should AI coding agents explore and understand a codebase architecture before implementing changes? (`software_engineering`, k=14)
3. multi-agent systems gather context observe environment research before acting (`ai_llm_agents`, k=12)
4. coding agent tools search files navigate repository comprehension patterns (`ai_llm_agents`, k=12)
5. software engineering agent workflow understand requirements read existing code before changes test debug (`ai_llm_agents`, k=12)
6. before coding explore repository read docs architecture map context for AI assistants (`software_engineering`, k=12)
7. SWE-agent agent-computer interface navigate search view files ACI design (`ai_llm_agents`, k=12)
8. prompt phases memory check planning execution verification before coding agent workflow (`ai_llm_agents`, k=12)
9. provide context to AI coding tools README architecture docs file paths examples not vibe coding (`software_engineering`, k=12)
10. context engineering multi-agent gather relevant context research observation before generation (`ai_llm_agents`, k=10)
11. Windsurf full codebase indexing query architecture understand entire repository before changes (`software_engineering`, k=12)
12. deep research agentic workflow planning reflection gather information before content generation (`ai_llm_agents`, k=10)
13. AI Usage Tips README coding standards feed guidelines into AI tools familiarize with team conventions (`software_engineering`, k=8)

**High-value `rag_fetch_chunk`:** `a3ca188700ea420507cf33e2`, `b6ad313a03312c92aa6ef1e0`, `fbcd698ea2a16bfdbaab917c`, `5e8d0ad3dbccf383dd55bec5`, `1f3b75066fd980f6659a9735`, `bbfb07815b4e97c83e176f8d`, `bf477243b9632b8ee90296ed`, `6daf3081f797c0c94712cce0`, `77f56a9e6fbd2d613306674d`, `2fde38a7b98f218aafac233a`.

---

## 3. Findings

### 3.1 Understand-before-write as explicit SWE-agent workflow

- `FACT` [E2] Mentoring analogy for tool design: workflow is “First, understand the requirements. If modifying existing code, read and understand the current implementation. Make your changes incrementally. Test each change. Debug failures. Document your work.” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems Principles, Patterns, and Implementation for AI Agents (Victor Dibia) (z-library.sk, 1lib.sk, z-lib.sk).epub` chunk_id=`b6ad313a03312c92aa6ef1e0` query=`"software engineering agent workflow understand requirements..."`]

- `FACT` [E2] “Before an agent can write code, it needs to understand the existing codebase and make targeted changes.” File ops: `read_file` (understand existing code), `list_directory` (explore structure / discover files), `grep_search` (locate patterns), then write/edit. [E2: same source chunk_id=`b6ad313a03312c92aa6ef1e0` / `fbcd698ea2a16bfdbaab917c`]

- `FACT` [E2] Design principle: “Search capability: grep_search enables finding patterns before editing.” [E2: chunk_id=`fbcd698ea2a16bfdbaab917c` query=`"coding agent tools search files..."`]

### 3.2 Exploration tool surface (environment ↔ actions)

- `FACT` [E2] SWE-agent (Yang et al., 2024) cited: environment = computer (terminal + filesystem); actions include navigate repo, search files, view files, edit lines. Agent brain plans action sequences from task + environment feedback. [E2: Alexandria corpus=`ai_llm_agents` source=`AI Engineering Building Applications with Foundation Models (Chip Huyen) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`d33dcb7ee82677e9ef859d7f` / `708e254278366124e6ecbe02` query=`"SWE-agent agent-computer interface..."`]

- `FACT` [E2] Production coding-tool inventory (Dibia): Research tools (web/search/fetch) + Coding tools (`ReadFile`/`WriteFile`, `ListDirectory`, `GrepSearch`, `BashExecute`, Python REPL). Principle: reliability over breadth — too many tools confuse agents / fill context. [E2: Dibia epub chunk_id=`359cad50d4d5409ac4d7531c` query=`"coding agent tools search files..."`]

- `INFERENCE` [E4] Premises: (1) understand-before-write requires read/list/grep; (2) SWE-agent ACI centers navigate/search/view before edit. ⇒ Coding-agent “research phase” is primarily filesystem navigation + search + selective read, not free-form generation. Grades: E2+E2→E4.

### 3.3 Phased prompts: memory → plan → execute → verify (before jumping to code)

- `FACT` [E2] Meta-cognitive tools (`ThinkTool`, `TodoWrite`/`TodoRead`) “give the agent space to plan before acting.” [E2: Dibia chunk_id=`a3ca188700ea420507cf33e2`]

- `FACT` [E2] Effective prompts use numbered phases: **memory check, planning, execution, verification, completion** — “preventing the agent from jumping randomly between actions.” “The planning and memory-check phases ensure the agent starts with context.” Memory-first: check prior patterns before starting fresh. [E2: Dibia chunk_id=`a3ca188700ea420507cf33e2` query=`"prompt phases memory check planning..."`]

- `FACT` [E2] Completion criteria must be explicit (all planned steps done, tests passing, code documented); vague “done” → premature stop. [E2: same chunk]

- `FACT` [E2] Long multi-file exploration suffers **early stopping** (e.g., reads 6 of 30 files then confident summary) and **context rot**. Mitigations ladder: prompt-only criteria → todo + CompletionCheckHook → LLM judge on tool-call evidence. Code-review example: explore every directory, read every file; setup uses PlanningHook before start + LLMCompletionCheckHook; read-only tools for review. [E2: Dibia chunk_id=`5e8d0ad3dbccf383dd55bec5`]

### 3.4 Context engineering as the “comprehension” mechanism

- `FACT` [E2] Context engineering = selecting, structuring, delivering the right info to the LLM at the right time (instructions, constraints, facts, prior steps, goals). Without disciplined selection, multi-agent systems “repeat work, overlook constraints, or act inconsistently.” Answers: what / how / when (seed → incremental update → consolidate). Techniques: RAG, rerank, compression/summaries, slotting “must include” items; planners attach goals/subgoals. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh The GenAI-Powered Autonomous Agent Ecosystem (Eric Broda, Davis Broda) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`6daf3081f797c0c94712cce0` query=`"context engineering multi-agent..."`]

- `FACT` [E2] Albada: context bridges planning and execution; prioritize relevance; structure/schemas (e.g. MCP); summarize long histories; assemble dynamically per step. “While orchestration decides what steps to take… context engineering ensures that each step has the right information.” [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents Designing and Implementing Multiagent Systems (Michael Albada) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`4b9a08fc084f85631bcc5c68`]

- `FACT` [E2] Rothman Context Engine: Planner→Executor loop; Researcher = retrieve → (sanitize) → synthesize from sources before Writer generates; dual RAG separates factual retrieval from procedural/style blueprints (Librarian vs Researcher). Plan–execute–reflect mirrors human complex work. [E2: `Context Engineering for Multi_Agent Systems...pdf` chunks `65d17c93df7a3495756a46af`, `cb3e48fb001322b701a94e93`, `07fcd3699bc730f7b2bf0b28`, `6795c07e629d218260bae1f0`]

- `FACT` [E2] Dibia: capability = tools × prompts × context engineering (compaction/hooks/isolation) for long tasks; without compaction, 50-iteration multi-file review thrash/early-stop/token blowup. [E2: Dibia chunk_id=`650b095c96ba8e2b577b1371`]

### 3.5 Human-side / IDE patterns for grounding AI in a codebase (Osmani)

- `FACT` [E2] Contextual prompting: models lack persistent memory of entire project unless provided (or IDE context). To fit existing codebase, supply relevant defs/API docs/examples; for large context, **summarize key elements** rather than dump everything. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani) (z-library.sk, 1lib.sk, z-lib.sk).epub` chunk_id=`1f3b75066fd980f6659a9735` query=`"provide context to AI coding tools..."`]

- `FACT` [E2] Windsurf: indexes entire codebase + RAG to feed relevant pieces; query in natural language (“Where… is auth handled?”) then implement with that context; described as assistant that “truly ‘reads the docs/code’ before writing,” reducing hallucinated APIs. Cursor: project-wide context vs older file-by-file assistants. [E2: Osmani chunks `bbfb07815b4e97c83e176f8d`, `bf477243b9632b8ee90296ed` query=`"Windsurf full codebase indexing..."`]

- `FACT` [E2] Team practice: encode conventions (lint/style) into AI tools; README section “AI Usage Tips” (e.g. functional components only; prefer Fetch over Axios). Golden rule: never merge AI code without thoroughly comprehending it; document rationale/context; share proven prompts. [E2: Osmani chunks `0964169c46f442821c732a94`, `ae5ea30721760ce3b23ed7af`]

- `CLAIM` [E3] Osmani cites Codacy blog on familiarizing AI with team standards → more uniform code (secondary/community-flavored citation inside book). [E3/E2 contested: same `0964169c46f442821c732a94`]

### 3.6 Research-before-generation (general multi-agent, transferable method)

- `FACT` [E2] Deep research agents (Albada): (1) plan agenda, (2) decompose to queries, (3) invoke tools + reflect on relevance/reliability, (4) synthesize evolving report with critique — **before** final deliverable. Strengths: adaptive, auditable plans; weaknesses: cost/latency/fragility. [E2: Albada chunk_id=`2fde38a7b98f218aafac233a` query=`"deep research agentic workflow..."`]

- `FACT` [E2] Ozdemir: deep research = multi-step explore/aggregate/cited reports; prefer **plan upfront** (larger model) then execute steps (smaller model) vs pure on-the-fly ReAct; add **re-plan/reflect** because plans go stale; workflow: plan → step executor → re-planner → summarize. [E2: `Building Agentic AI Workflows...` (Sinan Ozdemir) chunks `77f56a9e6fbd2d613306674d`, `6981c54ec1b33ae1a3bdb314`, `916911402d6016c657049c04`]

- `FACT` [E2] Huyen agent loop: plan generation (decomposition) → reflection/error correction → execution → again reflect; humans may supply/validate plans for risky ops. ReAct: Thought/Act/Observation until Finish; Reflexion separates evaluator + self-reflection. [E2: Huyen chunks `b6593fb02989cd5782e58dcb`, `9fdf742f7d5bf7ca40c5f96f`]

- `FACT` [E2] Pai: ReAct Thought→Action→Observation loop popular but “shown to be brittle.” [E2: `Designing Large Language Model Applications...` (Suhas Pai) chunk_id=`38e9160cc046590caba106ab`]

- `FACT` [E2] Ozdemir: presenting tools is insufficient if model is overconfident and skips tool use — still need guidance on **when** to use tools (calibration / instructional alignment). [E2: Ozdemir neighbor chunk `586d5ffda25bc2686d2220f7`]

### 3.7 Memory as persistent exploration residue

- `FACT` [E2] Dibia MemoryTool: store patterns/decisions/plans across conversations (`view`/`create`/`search`/`append`/`str_replace`); “Without memory, each task starts from zero.” [E2: chunks `fbcd698ea2a16bfdbaab917c`, `f96738c68892f77a606b5f00`]

- `INFERENCE` [E4] Premises: memory-first prompt phase + MemoryTool for institutional knowledge. ⇒ Pre-implementation “research” should write durable notes (patterns, open questions, file maps) into agent memory / artifacts, not only chat scratch. E2+E2→E4.

### 3.8 Evaluation / completeness of exploration

- `FACT` [E2] Evaluation-driven development: define success metrics before writing agent code; evaluate full **trajectory** (planning, tool sequences), not only final artifact. [E2: Dibia chunk_id=`abff3072fadd340ec8424e5e`]

- `FACT` [E2] Expert checklist for software agent outcomes includes functional correctness, tests, quality, docs — implies exploration quality is partly judged by whether intermediate process was thorough. [E2: Dibia chunk_id=`260f0282888c780315cf2c69`]

---

## 4. Contradictions / conflicts found

1. **Autonomous ReAct vs plan-first workflows:** Ozdemir/Albada/Rothman push upfront planning + re-plan; Dibia SWE agent is autonomous (model-driven control) but still encodes plan phases in prompts. Not a hard contradiction — continuum of rigidity — but literature disagrees on default. Prefer E2 sources that state trade-offs explicitly (Ozdemir: plan stale risk; Pai: ReAct brittle).

2. **Exhaustive explore-all-files vs selective RAG context:** Dibia code-review task demands explore every directory/file (with compaction + completion hooks); Osmani/Windsurf emphasize retrieve-relevant-only indexing. Conflict on strategy for large repos: exhaustive review vs query-driven retrieval. Both E2; applicability depends on task (audit vs feature).

3. **“Tools alone suffice” vs “must prompt when to use tools”:** Dibia emphasizes tools as operational capability; Ozdemir shows overconfident models skip retrieval. Complementary: tools necessary, not sufficient.

---

## 5. Gaps

- `GAP` Direct literature prescribing a GreyMatter-style “research then document then implement” pipeline for coding agents was **weak/absent** on the most literal probe (`ai_llm_agents` weak hit_count=2). Patterns reconstructed from adjacent SWE-agent / context-engine / deep-research chapters.

- `GAP` Little primary detail in retrieved chunks on **SWE-agent Agent-Computer Interface (ACI) design paper internals** beyond Huyen’s summary citation (Yang et al. 2024). OPEN: fetch arXiv primary if needed.

- `GAP` Sparse coverage of **multi-agent role split specifically for codebase exploration** (e.g. Explorer vs Implementer vs Documenter). Rothman has Librarian/Researcher/Writer for content, not clearly for source trees. OPEN.

- `GAP` No strong retrieved protocol for **dependency-graph / call-graph / architecture-diagram extraction** as a mandatory pre-step (only list/grep/read and IDE indexing).

- `GAP` `software_engineering` hits heavily concentrated in a single book (Osmani); limited diversity of SE sources on this slice.

- `OPEN` How to measure “enough comprehension” before allowing write tools (beyond todo/LLM-judge completion hooks in Dibia).

- `OPEN` Whether research steps should be a **hard workflow gate** vs **prompt-encoded soft phase** for coding tasks (literature supports both).

---

## 6. Candidate patterns for templates (cited only)

Reusable “research steps” **only where evidenced**:

| Step | Pattern (evidence-backed) | Sources |
|------|---------------------------|---------|
| R0 | Seed task context: requirements + constraints + team conventions (README / style tips) | Osmani `1f3b75066fd980f6659a9735`, `0964169c46f442821c732a94` |
| R1 | Memory / prior-knowledge check before fresh exploration | Dibia `a3ca188700ea420507cf33e2` |
| R2 | Plan exploration agenda (dirs/files/queries); optionally PlanningHook / larger planner model | Dibia `5e8d0ad3dbccf383dd55bec5`; Ozdemir `77f56a9e6fbd2d613306674d`; Albada `2fde38a7b98f218aafac233a` |
| R3 | Structure discovery: `list_directory` / repo navigate | Dibia `b6ad313a03312c92aa6ef1e0`; Huyen SWE-agent |
| R4 | Locate symbols/patterns: `grep_search` / NL codebase query / RAG over index **before edit** | Dibia `fbcd698ea2a16bfdbaab917c`; Osmani Windsurf |
| R5 | Selective `read_file` / view; for huge context summarize keys | Dibia file ops; Osmani contextual prompting tip |
| R6 | Retrieve–sanitize–synthesize factual notes (research agent) with citations/sources | Rothman Researcher; Albada deep research step 3–4 |
| R7 | Persist findings (memory create/append; todo checklist) | Dibia MemoryTool + Todo |
| R8 | Reflect / re-plan if evidence insufficient or plan stale | Ozdemir re-planner; Huyen/Albada reflection |
| R9 | Completion gate on exploration thoroughness (prompt criteria / todo hook / LLM judge) **before** enabling write tools | Dibia `5e8d0ad3dbccf383dd55bec5` |
| R10 | Then incremental edit + execute/test feedback loop | Dibia write→test→fix; junior-dev workflow |

`INFERENCE` [E4]: Ordering R1→R9 before implementation is a synthesis of the cited phases; no single chunk lists this exact numbered checklist for GreyMatter.

---

## 7. Source list (deduped)

**ai_llm_agents**

- Designing Multi-Agent Systems… (Victor Dibia) — epub
- AI Engineering… (Chip Huyen) — pdf
- Building Applications with AI Agents… (Michael Albada) — pdf
- Context Engineering for Multi_Agent Systems… (Denis Rothman) — pdf
- Agentic Mesh… (Eric Broda, Davis Broda) — pdf
- Building Agentic AI Workflows… (Sinan Ozdemir) — epub
- Designing Large Language Model Applications… (Suhas Pai) — pdf
- Mastering AI Agents… (Pratik Bhavsar) — pdf (lower relevance / case-study noise)
- AI Agents in Action (Micheal Lanham) — pdf (agent profile / planning components)
- Building Natural Language and LLM Pipelines… (Laura Funderburk) — pdf (SWE-agent arXiv cite in further reading)

**software_engineering**

- Beyond Vibe Coding… (Addy Osmani) — epub

**External primary referenced inside corpus (not fetched this pass)**

- Yang et al., 2024. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. arXiv:2405.15793 — OPEN/E1 candidate
- Yao et al., 2022. ReAct — cited via Huyen
- Shinn et al., 2023. Reflexion — cited via Huyen/Albada

---

## Method completeness note

Literal “explore codebase before documenting/implementing” coverage was **partial–weak** on first probe; densest support came from Dibia Ch.15 (SWE agent), Osmani (contextual prompting + codebase indexing IDEs), Rothman/Albada/Ozdemir (plan–research–synthesize), and Huyen (SWE-agent ACI + ReAct/Reflexion). Claims above stay within retrieved chunks; gaps marked explicitly.
