# Theme 1 — Codebase research for agents (integrated report)

**Date:** 2026-07-27  
**Status:** integrated report  
**Protocol:** `docs/research/PROTOCOL.md`  
**Integrator scope:** Theme 1 only — merge listed notes; no new facts; no plugin stub; no MVP locks.

### Sources merged

| ID | Path |
|----|------|
| T1A | `docs/research/notes/theme-1/t1a-alexandria-agent-exploration.md` |
| T1B | `docs/research/notes/theme-1/t1b-web-agent-workspace-patterns.md` |
| T1C | `docs/research/notes/theme-1/t1c-program-comprehension-methods.md` |
| COORD-T1 | `docs/research/sources/coordinator-t1-program-comprehension.md` |

---

## 1. Executive summary

Verified synthesis from the inputs (≤12 bullets):

1. Coding-agent “research before write” is filesystem navigation + search + selective read, then edit/test — not free-form generation. [E2 T1A Dibia/Huyen; E4 T1A]
2. Effective agent prompts encode phases (memory check → plan → execute → verify) so exploration starts with context and does not skip ahead. [E2 T1A Dibia]
3. Vendor docs converge on **explore / plan / then implement**, often with exploration isolated in a subagent so search noise does not fill the main thread. [E1 T1B Claude/Codex/Cursor]
4. Durable repo guidance belongs in agent instruction files (`AGENTS.md`, `CLAUDE.md`, Cursor rules, etc.): layout, exact commands, conventions, do-nots, definition of done. [E1 T1B]
5. Instruction **filename and merge semantics differ by product** (closest-wins vs concatenate-override vs agent-decides); there is no single universal schema. [E1 T1B]
6. Structural context injection varies: Aider/Continue symbol repo-maps; Cursor embeddings + Instant Grep + Explore; Continue deprecating `@Codebase` toward tools/MCP. [E1 T1B]
7. Classical program comprehension builds a **mental model** via hypotheses resolved by evidence; strategies include top-down (beacons/plans), bottom-up (chunking), and opportunistic switching (integrated metamodel). [E1 T1C; E1/E2 COORD-T1]
8. **Systematic** reading yields stronger causal mental models; **as-needed** is common on large systems but risks missed interactions — agents that retrieve snippets without flow tracing inherit that risk. [E1 T1C via Storey←Littman; E4 T1C]
9. Architecture is often not explicit in code; SAR processes (bottom-up extract–abstract–present, top-down style matching, hybrid) and dependency/cycle awareness transfer to agent recon. [E1 T1C Ducasse/Pollet; E2 T1C Clean Architecture / Architecture Metrics]
10. Context engineering (select/structure/deliver the right facts per step) and memory of prior patterns are the multi-agent mechanisms that make comprehension stick across turns. [E2 T1A Broda/Albada/Rothman/Dibia]
11. Exhaustive “read every file” and query-driven RAG/index retrieval are both evidenced strategies; choice depends on task (audit vs feature), not a universal default. [E2 T1A conflict]
12. No single retrieved source prescribed a GreyMatter-specific “research → document → implement” pipeline; the unified protocol below is an **E4 synthesis** of adjacent patterns. [GAP T1A; E4 T1A R0–R10]

---

## 2. Unified reconnaissance protocol for agents

Ordered steps for pre-implementation / pre-documentation codebase research. Each step cites evidence from the notes. Ordering of the full checklist is itself `INFERENCE` [E4] (T1A §6): no single chunk lists this exact sequence for GreyMatter.

| Step | Agent action | Evidence |
|------|--------------|----------|
| **S0 — Seed task context** | Load requirements, constraints, and team conventions (README / AI usage tips / instruction files). Prefer short accurate instruction files; nest per package when monorepo. | `FACT` [E2 T1A Osmani `1f3b75066fd980f6659a9735`, `0964169c46f442821c732a94`]; `FACT` [E1 T1B agents.md; Codex AGENTS.md; Claude memory] |
| **S1 — Declare comprehension goal** | State task type (e.g. corrective / perfective / adaptive / reuse / “understand for X”) before exploring. | `INFERENCE` [E4 T1C PC-GOAL] premises: [E1 von Mayrhauser & Vans 1995] |
| **S2 — Choose strategy mode** | Label session: **systematic** (broader control/data-flow), **as-needed** (task slice), or **hybrid**; for large repos prefer scoped systematic regions, not whole-repo systematic. | `INFERENCE` [E4 T1C PC-STRAT] premises: [E1 Storey←Littman]; `FACT` [E1 T1C systematic of entire large programs often unrealistic] |
| **S3 — Memory / prior-knowledge check** | Check prior patterns, memory artifacts, and previous research notes before fresh exploration. | `FACT` [E2 T1A Dibia `a3ca188700ea420507cf33e2`]; `INFERENCE` [E4 T1A] durable notes into memory, not chat-only |
| **S4 — Plan exploration agenda** | Plan dirs/files/queries; optionally use plan mode / larger planner; decompose into tool-backed inquiries. Warn against unbounded exploration. | `FACT` [E2 T1A Dibia PlanningHook; Ozdemir plan-first; Albada deep research]; `FACT` [E1 T1B Claude explore→plan→code; Codex Plan mode; Cursor Explore] |
| **S5 — Bootstrap instruction / ignore surface** | Read root (+ nested) agent instructions; configure ignore/deny for secrets, vendored, generated noise so search stays relevant. | `FACT` [E1 T1B Codex “reads AGENTS.md before any work”; Cursor ignore files; Claude large-codebases deny Reads] |
| **S6 — Structure discovery** | List directories / navigate repo / obtain structural outline (repo map or tree) before bulk dumps. | `FACT` [E2 T1A Dibia list_directory; Huyen SWE-agent navigate]; `FACT` [E1 T1B Aider repomap; Continue `@Tree` / `@Repository Map`] |
| **S7 — Form top-down hypotheses** | When domain/architecture is somewhat familiar, state expected layers/modules and beacon cues to verify. | `FACT` [E1 T1C Brooks/Soloway via Storey & von Mayrhauser]; `INFERENCE` [E4 COORD-T1] opportunistic switching, not only linear dumps |
| **S8 — Locate symbols / patterns before edit** | Grep / Instant Grep / NL codebase query / index RAG / LSP — **search before write**. | `FACT` [E2 T1A Dibia grep_search principle; Osmani Windsurf indexing]; `FACT` [E1 T1B Cursor Search; Claude LSP plugins optional] |
| **S9 — Isolate recon context** | Delegate broad search/read to Explore / investigation subagent; return **summaries** to the main implementation thread. | `FACT` [E1 T1B Cursor Explore; Claude “subagents for investigation”; Codex subagents] |
| **S10 — Selective read + bottom-up chunking** | Read target files; chunk into control-flow (program model) then data/functional (situation model); summarize keys when context is huge. | `FACT` [E2 T1A Dibia read_file; Osmani summarize vs dump]; `FACT` [E1 T1C Pennington/Shneiderman bottom-up] |
| **S11 — Inquiry episodes for delocalized plans** | For scattered related logic: question → conjecture → search → result; do not trust local clues alone. | `INFERENCE` [E4 T1C PC-INQUIRY] premises: [E1 Storey←Letovsky; von Mayrhauser] |
| **S12 — Architecture / dependency pass (when goal warrants)** | Extract deps → abstract modules/layers → present view → note expected vs implemented; flag cycles as hazards. | `INFERENCE` [E4 T1C SAR-EXTRACT / SAR-CYCLES] premises: [E1 Ducasse/Pollet]; [E2 Architecture Metrics; Clean Architecture]. Note: T1A recorded `GAP` that agent-literature chunks rarely mandate this as a hard pre-step. |
| **S13 — Synthesize cited research notes** | Retrieve → (sanitize) → synthesize factual notes with sources; keep parallel domain / program / situation model notes; log hypotheses accept/reject/revise. | `FACT` [E2 T1A Rothman Researcher; Albada deep research]; `INFERENCE` [E4 T1C PC-HYPO / PC-MODEL] |
| **S14 — Persist findings** | Write durable memory/artifacts/artifacts (patterns, open questions, file maps); update instruction files after repeated mistakes. | `FACT` [E2 T1A MemoryTool + Todo]; `FACT` [E1 T1B Cursor/Codex/Claude “update instructions when agent repeats mistakes”] |
| **S15 — Reflect / re-plan** | If evidence insufficient or plan stale, re-plan before editing; calibrate tool use (models may skip tools if overconfident). | `FACT` [E2 T1A Ozdemir re-planner; Huyen reflect; Ozdemir when-to-use-tools; Pai ReAct brittle] |
| **S16 — Completion gate on exploration** | Explicit thoroughness criteria (todo / hooks / LLM judge on tool-call evidence) before enabling write tools — soft (prompt) or hard (hooks) per product. | `FACT` [E2 T1A Dibia `5e8d0ad3dbccf383dd55bec5`]; `FACT` [E1 T1B Claude: instructions ≠ enforcement; PreToolUse hooks for hard blocks]; `OPEN` T1A hard gate vs soft phase |
| **S17 — Then incremental edit + verify** | Incremental changes; run verification/test commands from instruction files; treat AI summaries as conjectures verified against code. | `FACT` [E2 T1A Dibia junior-dev workflow]; `FACT` [E1 T1B agents.md FAQ / Codex Done when]; `INFERENCE` [E4 T1C AI-VERIFY] |
| **S18 — Make investigation reproducible (research artifacts)** | Version-control notes; separate raw inputs vs derived results; record env/steps; prefer inspectable automation. | `INFERENCE` [E4 T1C RSE-LAYOUT / RSE-PROV] premises: [E2 RSE with Python] |

---

## 3. Program comprehension mapping

| PC concept | Meaning (evidence) | Mapped agent actions |
|------------|--------------------|----------------------|
| **Top-down** | Domain/hypotheses refined via **beacons** and **programming plans** when code is familiar. [E1 T1C; E1/E2 COORD-T1] | Read `AGENTS.md`/architecture docs; state expected modules; search for beacon names/idioms; verify or revise hypotheses (S0, S7, S8, S13). |
| **Bottom-up** | Statements → chunks → higher abstractions; program model (control-flow) then situation model (data/function). [E1 T1C] | `list_directory` → selective `read_file` → summarize chunks; build control then data notes (S6, S10, S13). |
| **Opportunistic / integrated metamodel** | Switch among domain, program, and situation models; assimilation top-down or bottom-up by cue. [E1 T1C; E4 COORD-T1] | Alternate map/hypothesis steps with targeted reads; do not lock a single linear order (S7↔S10↔S11). |
| **Beacons / plans / rules of discourse** | Cues and conventions that index knowledge and set expectations. [E1 T1C] | Grep for idioms/API names; encode conventions in instruction files; record which beacons supported which hypothesis (S0, S8, S13). |
| **Delocalized plans** | Related logic non-contiguous; local clues mislead. [E1 T1C] | Cross-file grep + inquiry episodes; prefer subagent recon for scatter (S9, S11). |
| **Systematic** | Methodical control- and data-flow tracing → stronger static + causal knowledge. [E1 T1C Storey←Littman] | Scoped systematic pass over a subsystem; completion criteria on dirs/files covered (S2, S12, S16). |
| **As-needed** | Only task-relevant code → weaker causal model, more interaction errors. [E1 T1C] | Feature-slice search/RAG; **explicitly** note missed-interaction risk; expand scope when causal links appear (S2, S8, S15). |
| **SAR bottom-up / top-down / hybrid** | Extract–abstract–present vs style/hypothesis matching vs both. [E1 T1C Ducasse/Pollet] | Dependency extract + view presentation; compare expected architecture to code; flag cycles (S12). |
| **AI-era as-needed risk** | Snippet retrieval without flow tracing mirrors Littman as-needed failure mode. [E4 T1C] | Require verification against code/deps; prefer rich project context over isolated snippets (S17, AI-VERIFY). |

**Documented model nuance (not an error):** Pennington stages situation model after a fuller program model; von Mayrhauser & Vans allow situation model after **partial** program model with concurrent switching. Prefer integrated metamodel for agent protocols that must adapt mid-task. [E1 T1C Storey]

---

## 4. Tooling patterns across vendors

| Pattern | Evidence-backed practice | Products / notes |
|---------|--------------------------|------------------|
| **Agent instruction files** | Markdown guidance: overview, build/test, style, security, definition of done; no required schema on agents.md. [E1 T1B] | `AGENTS.md` (agents.md, Codex, Cursor, Copilot coding agent, VS Code); `CLAUDE.md` (Claude Code, import/symlink); `.cursor/rules`; `.continue/rules`; `.github/copilot-instructions.md` |
| **Explore / plan before edit** | Plan mode; Explore/investigation subagents; “Agent finds files if you don’t `@` them”. [E1 T1B] | Claude Code; Codex; Cursor |
| **Repo maps** | Files + key symbols under token budget; helps decide next files to open. [E1 T1B] | Aider `--map-tokens` (~1k default); Continue `@Repository Map` (Aider-inspired) |
| **Indexing / search** | Embeddings + exact grep; ignore lists; privacy claims for Cursor embeddings. [E1 T1B] | Cursor active; Continue **deprecating** `@Codebase` embeddings UX toward tools/MCP; Aider symbolic (tree-sitter), not embeddings-centric in primary docs |
| **Context isolation** | Subagents return summaries so recon does not pollute implementation context. [E1 T1B] | Cursor Explore/Bash/Browser; Claude investigation subagents; Codex exploration subagents |
| **Hooks / hard gates** | Lifecycle hooks can observe/block/modify; instructions alone are soft. [E1 T1B] | Cursor `hooks.json`; Claude PreToolUse; literature also has CompletionCheckHook (E2 T1A Dibia) |
| **llms.txt** | Curated **website/docs** link map for LLMs — not a git-repo agent protocol. [E1 T1B; E4 T1B] | llmstxt.org; do not conflate with `AGENTS.md` |
| **IDE indexing (literature)** | Windsurf/Cursor described as project-wide context / RAG before write (secondary book). [E2 T1A Osmani] | Complements E1 vendor docs; not a substitute for them |

### Contradictions within tooling (see also §5)

- Native filename: `AGENTS.md` vs `CLAUDE.md` vs `.github/copilot-instructions.md` vs `.continue/rules`.
- Nested merge: closest-wins (agents.md FAQ) vs root→leaf concatenate-override (Codex) vs combine with specific precedence (Cursor) vs agent-decides (VS Code nested AGENTS.md) vs Claude ancestor concat + on-demand subdir.
- Indexing direction: Cursor embeddings+grep vs Continue deprecating embedding `@Codebase` vs Aider symbol map.
- Size budgets: Codex ~32 KiB combined AGENTS.md; Claude soft ~200 lines / ~25KB auto-memory; Cursor rules soft &lt;500 lines; Aider map ~1k tokens — no shared numeric standard.

---

## 5. Conflicts table

| # | Topic | Position A | Position B | Resolution (higher grade / applicability) | Remaining conflict |
|---|-------|------------|------------|---------------------------------------------|--------------------|
| 1 | Control style | Plan-first + re-plan (Ozdemir/Albada/Rothman) [E2 T1A] | Autonomous ReAct-style loops; Dibia still encodes plan phases in prompts [E2 T1A]; Pai: ReAct brittle [E2 T1A] | Prefer sources that state trade-offs (plan staleness; ReAct brittleness). Treat as continuum of rigidity. | Default rigidity for coding tasks still `OPEN` (T1A). |
| 2 | Exploration breadth | Exhaustive explore-every-file (Dibia code-review + completion hooks) [E2 T1A] | Retrieve-relevant-only indexing (Osmani/Windsurf; vendor RAG) [E2 T1A; E1 T1B] | Task-dependent: audit/review → systematic/exhaustive tooling; feature work → as-needed + map/grep. Both E2/E1. | No universal default. |
| 3 | Tools sufficiency | Tools as operational capability (Dibia) [E2 T1A] | Overconfident models skip tools without “when to use” guidance (Ozdemir) [E2 T1A] | Complementary: tools necessary, not sufficient. | — |
| 4 | Instruction filename | `AGENTS.md` portable baseline [E1 T1B] | Claude `CLAUDE.md` only natively; Copilot Chat matrix omits AGENTS.md; Continue uses `.continue/rules` [E1 T1B] | Prefer documenting **interop** (import/symlink/adapters), not a single-file lock. | Template preference `OPEN` (T1B). |
| 5 | Nested merge semantics | “Closest wins” [E1 agents.md] | Codex concat root→leaf override; Cursor combine+specific; VS Code agent-decides; Claude different load rules [E1 T1B] | Same filename, different implementations — record all; do not assume one merge model. | Unresolved product fragmentation. |
| 6 | Indexing strategy | Cursor embeddings + Instant Grep [E1 T1B] | Continue deprecating `@Codebase`; Aider symbolic map [E1 T1B] | Multiple valid strategies; template should allow map **or** semantic search **or** tool-driven explore. | Direction diverging across vendors. |
| 7 | Size budgets | Soft line guidance (Claude ~200; Cursor &lt;500) [E1 T1B] | Hard Codex 32 KiB; Aider ~1k map tokens [E1 T1B] | Prefer progressive disclosure over one magic number. | No shared standard. |
| 8 | PC staging | Pennington: situation after fuller program model [E1 T1C] | von Mayrhauser & Vans: concurrent / after partial program model [E1 T1C] | Prefer integrated metamodel for adaptive agent protocols (Storey notes difference). | Theoretical difference remains documented. |
| 9 | “Top-down” wording | Clean Code Stepdown Rule = **authoring** guideline [E2 T1C] | Brooks/Soloway top-down = **comprehension** empirics [E1 T1C] | Do not equate without caveat. | Naming collision only. |
| 10 | von Mayrhauser full text | T1C fetched open PDF as E1 [T1C] | COORD-T1 marked full text `GAP`, relied on secondary [COORD-T1] | Prefer **T1C E1 primary PDF** for Theme 1 claims; coordinator gap is session-local. | COORD pass incomplete relative to T1C. |
| 11 | Dependency graph as mandatory pre-step | T1A `GAP`: agent literature rarely mandates call/dependency graphs [T1A] | T1C SAR pattern as candidate when architecture goal warrants [E1/E4 T1C] | Include as **conditional** S12, not universal gate. | Whether templates should require SAR always remains `OPEN`. |

---

## 6. Gaps & OPEN items (deduped)

### Gaps

- `GAP` Literal “research then document then implement” pipeline for coding agents was weak/absent in Alexandria `ai_llm_agents` probes; protocol reconstructed from adjacent SWE-agent / context-engine / deep-research / vendor docs. [T1A]
- `GAP` ~~SWE-agent ACI paper (Yang et al. 2024, arXiv:2405.15793) not fetched as primary; Huyen summary only.~~ **Closed secondary 2026-07-28** — see `notes/secondary/sec-p0-aci-codex-wtd.md`. [T1A]
- `GAP` Sparse multi-agent role split specifically for codebase exploration (Explorer vs Implementer vs Documenter); Rothman Librarian/Researcher/Writer is content-oriented. [T1A]
- `GAP` `software_engineering` Alexandria corpus lacks primary PC papers as documents; classical theory required web PDFs. [T1C E0]
- `GAP` Littman et al. 1986, Letovsky 1987 JSS, Soloway et al. CACM 1988, Storey 2006 SQJ — primary full texts not all obtained this pass (claims via Storey/von Mayrhauser where noted). [T1C]
- `GAP` No empirical study retrieved that directly measures LLM/agent strategies against Littman systematic/as-needed outcomes. [T1C]
- `GAP` Feature location / concept assignment literature not deeply surveyed. [T1C]
- `GAP` No single formal RFC/schema for `AGENTS.md` content beyond “standard Markdown.” [T1B]
- `GAP` Cursor does not publish a public indexing algorithm comparable to Aider’s tree-sitter + ranking write-up. [T1B]
- `GAP` Hooks can enforce gates but vendors do **not** mandate explore-before-edit by default. [T1B]
- `GAP` First-class major-LLM crawl support for llms.txt not evidenced as E1. [T1B]
- `GAP` Windsurf/Devin/Amp/Jules proprietary recon docs not deeply fetched. [T1B]
- `GAP` Copilot CLI full discovery order for concurrent instruction files only partially covered. [T1B]
- `GAP` “Theory of Code Space” / modern agent benchmarks from search snippets — not verified. [COORD-T1]

### OPEN

- `OPEN` How to measure “enough comprehension” before allowing write tools (beyond Dibia todo/LLM-judge hooks). [T1A]
- `OPEN` Hard workflow gate vs prompt-encoded soft research phase for coding tasks. [T1A]
- `OPEN` Whether templates prefer one filename (`AGENTS.md`) + adapters vs generating multiple vendor files. [T1B]
- `OPEN` Whether research protocol should require Cursor Explore / Claude investigation-subagent as a mandatory step. [T1B]
- `OPEN` How to operationalize “beacon” detection for agents (heuristics vs embeddings vs name/API patterns) without inventing psychology claims. [T1C]
- `OPEN` Map PC strategies onto specific Cursor tool sequences with E0 validation (empirical pass not done). [COORD-T1]
- `OPEN` Whether SAR/dependency extraction should be a required template step or conditional on architecture goals. [from conflict #11]

---

## 7. Implications for GreyMatter research templates

All items below are **`INFERENCE` [E4]** candidate recommendations — **not** design locks, library choices, or MVP scope.

1. **Template a phased recon checklist** (S0–S18 condensed) that agents must fill: goal, strategy mode, hypotheses, files/tools used, open questions, verification commands — premises: T1A R0–R10 + T1C PC-\* + T1B explore→plan→edit. [E4]
2. **Treat instruction files as the durable “how to research this repo” layer**; draft portable `AGENTS.md` content areas from agents.md/Codex, with optional `CLAUDE.md` `@AGENTS.md` and Cursor rules adapters — premises: T1B E1 interop facts. [E4] (`OPEN` on single vs multi-file generation.)
3. **Separate soft guidance from hard gates:** put explore-before-edit in rules/skills; reserve hooks for enforcement when needed — premises: Claude best practices + Cursor hooks [E1 T1B]; Dibia completion hooks [E2 T1A]. [E4]
4. **Default recon to context-isolated exploration** (subagent or equivalent) returning summaries — premises: shared vendor pattern [E1 T1B]. [E4] (Mandatory vs recommended still `OPEN`.)
5. **Support both systematic and as-needed modes** with explicit labeling and scoped systematic regions for large repos — premises: Littman via Storey [E1 T1C]. [E4]
6. **Support opportunistic top-down ↔ bottom-up switching** with a written mental-model artifact (domain / program / situation + hypothesis log) — premises: integrated metamodel [E1 T1C]; COORD-T1 E4. [E4]
7. **Make architecture/dependency recovery a conditional module** (when goal is architectural or risk of cycles/delocalized plans is high), not a universal mandatory gate — premises: conflict #11; T1A GAP vs T1C SAR. [E4]
8. **Prefer progressive disclosure** (short root instructions, nested package files, linked deeper docs, token-budgeted maps) over dumping whole repos — premises: T1B size/nesting E1; Osmani summarize [E2 T1A]; Aider map budget [E1 T1B]. [E4]
9. **Require cited research notes before implementation deliverables** in research workflows (retrieve → synthesize → persist) — premises: Rothman/Albada [E2 T1A]; RSE inspectability [E2 T1C]. [E4]
10. **Do not conflate `llms.txt` with repo agent config** in templates — premises: T1B E4. [E4]
11. **Evaluation of agent research quality should include trajectory** (tool sequences, hypothesis updates), not only final code — premises: Dibia evaluation-driven development [E2 T1A]. [E4]

---

## 8. Source index

### Note / coordinator paths

- `d:\GreyMatter\docs\research\notes\theme-1\t1a-alexandria-agent-exploration.md`
- `d:\GreyMatter\docs\research\notes\theme-1\t1b-web-agent-workspace-patterns.md`
- `d:\GreyMatter\docs\research\notes\theme-1\t1c-program-comprehension-methods.md`
- `d:\GreyMatter\docs\research\sources\coordinator-t1-program-comprehension.md`
- `d:\GreyMatter\docs\research\PROTOCOL.md`

### Key E1 URLs (from notes)

**Program comprehension / SAR**

- https://www.cs.kent.edu/~jmaletic/cs63902/Papers/ProgramComprehension/von_mayrhauser-1995.pdf — von Mayrhauser & Vans 1995 (DOI https://doi.org/10.1109/2.402076)
- https://plg.uwaterloo.ca/~migod/846/papers/storey-jss.pdf — Storey, Fracchia & Müller (cognitive design elements)
- http://staff.cs.upt.ro/~ioana/arhitrec/SARtaxonomy.pdf — Pollet/Ducasse SAR taxonomy (journal DOI https://doi.org/10.1109/tse.2009.19)

**Agent instruction / vendor docs**

- https://agents.md/
- https://llmstxt.org/
- https://cursor.com/docs/rules.md
- https://cursor.com/docs/skills.md
- https://cursor.com/docs/hooks.md
- https://cursor.com/docs/agent/tools/search.md
- https://cursor.com/docs/subagents.md
- https://cursor.com/docs/agent/prompting.md
- https://cursor.com/docs/reference/ignore-file.md
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/large-codebases
- https://code.claude.com/docs/en/best-practices
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/learn/best-practices
- https://github.com/openai/codex/blob/main/codex-rs/core/hierarchical_agents_message.md
- https://aider.chat/docs/repomap.html
- https://aider.chat/2023/10/22/repomap.html
- https://docs.continue.dev/guides/codebase-documentation-awareness
- https://docs.continue.dev/customize/deep-dives/custom-providers
- https://docs.continue.dev/reference/deprecated-codebase
- https://docs.github.com/en/copilot/reference/custom-instructions-support
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://agentskills.io (referenced by Cursor; not fully re-fetched in T1B)

### Key E2 corpora / books (Alexandria — see T1A/T1C source lists)

- Dibia — *Designing Multi-Agent Systems…* (`ai_llm_agents`)
- Huyen — *AI Engineering…* (`ai_llm_agents`)
- Albada, Rothman, Broda, Ozdemir, Pai — multi-agent / context engineering (`ai_llm_agents`)
- Osmani — *Beyond Vibe Coding…* (`software_engineering`)
- Irving et al. — *Research Software Engineering with Python*; Martin *Clean Architecture*; Architecture Metrics; Architecture Patterns with Python (`software_engineering`)

### Notable E1 candidate not fetched this track

- Yang et al., 2024 — SWE-agent ACI — arXiv:2405.15793 (`OPEN` / E1 candidate) [T1A]
