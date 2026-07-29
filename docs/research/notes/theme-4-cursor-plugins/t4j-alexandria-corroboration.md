---
title: "T4J Alexandria corroboration — Cursor plugin Wave 1 vs RAG"
status: draft
theme: theme-4-cursor-plugins
wave: 2
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-T4J]
supersedes: null
related:
  - wave2-staging-alexandria-github.md
mcp_server: user-alexandria-rag
---

# T4J Alexandria corroboration (Cursor plugins)

Using `research-protocol`. MCP server: `user-alexandria-rag`.

## 1. Scope

- **Question / goal:** Reinforce (or mark `GAP`) Wave 1 Cursor plugin-component findings using Alexandria RAG; document transferable adjacent patterns (MCP packaging, progressive disclosure, agent instruction / tool design) clearly labeled as **not** Cursor packaging SoT.
- **In scope:** `list_corpora`; multiple `rag_query` on `ai_llm_agents` (k 8–12); opportunistic `software_engineering` probes; cite useful hits; honest GAP log mapped to Wave 1 components (skills / rules / hooks / mcp / agents / commands / manifest).
- **Out of scope:** Web / GitHub primary reinforcement (T4H–T4I); locking Cursor design on book chapters; inventing chunk_ids.
- **Comprehension / research goal type:** reuse (corroboration / negative evidence).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria MCP `user-alexandria-rag`: `list_corpora`, `rag_query` (leaf, default rerank); k=8–10 |
| Corpora / URLs searched | `ai_llm_agents` (primary); `software_engineering` (AGENTS.md / Cursor plugins probes) |
| Queries (exact) | See table below |
| What was *not* searched | Other shelves (`data_sql`, `finance_trading`, `game_design`, etc.); web; GitHub; official cursor.com docs (Wave 1 / E1 elsewhere); agentskills.io live site |
| Provenance (optional PROV) | Entity=Alexandria indices; Activity=T4J Wave 2 deep pass; Agent=gatherer-T4J + `user-alexandria-rag`; wasDerivedFrom=`wave2-staging-alexandria-github.md` |

### Exact queries run

| # | Corpus | `question` (exact) | k |
|---|--------|--------------------|---|
| Q1 | `ai_llm_agents` | `Cursor IDE plugins rules skills hooks SKILL.md .mdc` | 10 |
| Q2 | `ai_llm_agents` | `Agent Skills SKILL.md YAML frontmatter progressive disclosure` | 10 |
| Q3 | `ai_llm_agents` | `AGENTS.md coding agent instructions` | 10 |
| Q4 | `ai_llm_agents` | `Model Context Protocol MCP server host Cursor configuration` | 10 |
| Q5 | `ai_llm_agents` | `how to write effective tools/skills for LLM agents cold start context` | 10 |
| Q6 | `ai_llm_agents` | `Cursor plugin.json mcp.json hooks.json rules .mdc marketplace` | 10 |
| Q7 | `ai_llm_agents` | `agentskills.io Agent Skills Specification SKILL.md frontmatter name description` | 10 |
| Q8 | `ai_llm_agents` | `MCP mcpServers configuration JSON host client tools resources prompts packaging` | 10 |
| Q9 | `ai_llm_agents` | `describe tools for LLM agents tool descriptions cold start few tools domain-specific` | 8 |
| Q10 | `ai_llm_agents` | `fewer excellent domain-specific tools rather than many general-purpose` | 8 |
| Q11 | `software_engineering` | `AGENTS.md coding agent instructions Cursor llms.txt` | 8 |
| Q12 | `software_engineering` | `Cursor IDE plugins skills rules hooks` | 8 |

**Note:** An additional attempt for `~/.cursor/mcp.json Claude Desktop mcpServers configuration` was intended; useful path evidence already returned under Q4 (chunk `eaeac0599358517c03c5d041`). No further distinct Cursor-packaging hits expected.

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (suggested query set) + hybrid follow-ups on filenames / Spec / tool-quality |
| Why this mode | Staging already flagged weak Cursor-plugin coverage; T4J must stress-test with filename/Spec queries and still record GAP |
| Scope boundary | RAG only; map to Wave 1 components as `INFERENCE` with premises only |

## 4. Findings

### 4.1 Corpus inventory (E0)

- `FACT` [E0] `list_corpora` returned seven corpora; `ai_llm_agents` has 71 docs / 22720 chunks, active index `v1`, `last_ingest_at` 2026-07-10T00:34:34Z; `software_engineering` has 21 docs / 7712 chunks, `last_ingest_at` 2026-07-10T00:22:09Z. [E0: Alexandria `list_corpora` 2026-07-29]

### 4.2 What RAG actually supports (MCP / host — adjacent to plugin `mcp`)

These hits are **secondary literature (E2)** about MCP generally or Cursor-as-MCP-host anecdotes. They do **not** define Cursor plugin `mcp.json` packaging, marketplace manifests, or plugin-scoped MCP wiring. Treat as adjacent context only.

- `CLAIM` [E2] MCP hosts include Cursor as an AI-powered IDE example alongside Claude Desktop and autonomous agents. Quote: “Examples include Claude Desktop … Cursor, an AI-powered IDE … and AI agents…” [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape, Security Threats, and Future Research Directions.pdf` chunk_id=`f61f330a9235f4ecb173bed2` query=`MCP mcpServers configuration JSON host client tools resources prompts packaging`]

- `CLAIM` [E2] Survey case study describes Cursor using MCP to schedule external tools (e.g. Playwright) after natural-language tasks, with developers declaring tool addresses rather than per-tool adapters. Quote: “they only need to declare the tool addresses to access different types of services…” [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape…pdf` chunk_id=`84ae91a36873c50e83f864e3` query=`Model Context Protocol MCP server host Cursor configuration`]

- `CLAIM` [E2] Secondary figure/list of MCP host config paths includes `~/.cursor/mcp.json` among Claude Desktop / Cline / Windsurf paths, in a credential-theft risk illustration with `mcpServers` JSON. Quote path list includes: “`~/.cursor/mcp.json`”. [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape…pdf` chunk_id=`eaeac0599358517c03c5d041` query=`Model Context Protocol MCP server host Cursor configuration`]

- `CLAIM` [E2] MCP server creation packages **metadata**, **capability declaration** (tools / resources / prompts), **code**, and optional slash commands; deployment includes release, installer, environment setup, tool registration. Quote: “Capability declaration specifies the standardized functions the server provides, such as tools, resources, or prompts…” [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape…pdf` chunk_id=`1e25631bbd80de92d6410b9a` query=`MCP mcpServers configuration JSON host client tools resources prompts packaging`]

- `CLAIM` [E2] MCP servers expose tools, resources, and prompts; host/client/server workflow uses intent analysis → tool selection → invocation. [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape…pdf` chunk_id=`249e1d8f9a2d4accef1af699` query=`MCP mcpServers configuration JSON host client tools resources prompts packaging`]

- `CLAIM` [E2] Manning / Infante: MCP host process connects via MCP clients to local (STDIO) or remote (Streamable HTTP) servers that expose tools. Quote: “MCP servers can be either remote … or local (accessed via standard input/output [STDIO]…” [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents and Applications With LangChain, LangGraph, and MCP (Roberto Infante)….pdf` chunk_id=`4fb2ea8fa47b4a0d078e740b` query=`MCP mcpServers configuration JSON host client tools resources prompts packaging`]

- `CLAIM` [E2] Cursor Directory MCP listed among MCP server collections (table “As of Sept. 2025”, ~1800 servers URL cursor.directory/mcp) — marketplace/directory discovery signal for MCP tools, **not** Cursor plugin marketplace packaging SoT. [E2: Alexandria corpus=`ai_llm_agents` source=`Model Context Protocol (MCP)_Landscape…pdf` chunk_id=`055fd78cd0b9cc1eebe341dd` query=`Cursor plugin.json mcp.json hooks.json rules .mdc marketplace`]

- `CLAIM` [E2] Dibia: one MCP server can work across Claude Desktop, Cursor, VSCode, and custom apps (“Multi-platform tools”). Quote: “Write one MCP server that works across Claude Desktop, Cursor, VSCode, and custom applications.” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)….epub` chunk_id=`c7db6837716b06809061d371` query=`Cursor plugin.json mcp.json hooks.json rules .mdc marketplace`]

**Wave 1 map (`mcp` component):** `INFERENCE` [E4] Alexandria can corroborate *host-level* MCP config shape (`mcpServers`, tools/resources/prompts, STDIO vs remote) as **adjacent** evidence for how plugin-bundled MCP might *feel* to authors, but cannot corroborate Cursor plugin `mcp.json` / plugin-scoped MCP wiring. Premises: (1) strong E2 MCP packaging hits above; (2) zero hits defining Cursor plugin MCP embedding; (3) Wave 1 E1 must remain SoT for plugin paths.

### 4.3 Transferable adjacent patterns (NOT Cursor packaging SoT)

Label every item below as **adjacent only** — useful for Toolbelt skill/tool authoring culture, not as law for `SKILL.md` / `.mdc` / `hooks.json` / `plugin.json`.

#### Progressive disclosure (UX / response / framework API — not Agent Skills Spec)

- `CLAIM` [E2] Dibia multi-agent UX: “Progressive Disclosure: Start with basic capabilities and reveal advanced features as users become comfortable…” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)….epub` chunk_id=`436da0e040ce7fbabd2c6a60` query=`Agent Skills SKILL.md YAML frontmatter progressive disclosure`]

- `CLAIM` [E2] Albada: surface core capabilities first; progressive disclosure for advanced features. Quote: “Effective designs prioritize progressive disclosure, showing core capabilities initially and revealing advanced features…” [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents… (Michael Albada)….pdf` chunk_id=`c1f5765ced7b9715e08d38f4` query=`Agent Skills SKILL.md YAML frontmatter progressive disclosure`]

- `CLAIM` [E2] Framework-API progressive disclosure: “Progressive disclosure—you only see complexity when you need it.” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)….epub` chunk_id=`a3956681adc018eab4f952bb` query=`Agent Skills SKILL.md YAML frontmatter progressive disclosure`]

- `CLAIM` [E2] RAG cookbook “Progressive disclosure response generation” = step-by-step answer revelation in RAG UX — **homonym**, not skills frontmatter. Quote: “answers are revealed in a step-by-step manner rather than all at once.” [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook… (Deepak Dhyani)….pdf` chunk_id=`fcfa315e71b35e8edb0b7d41` query=`Agent Skills SKILL.md YAML frontmatter progressive disclosure`]

**Wave 1 map (`skills` / cold-start UX):** `INFERENCE` [E4] Progressive-disclosure *concept* is abundant in agent UX literature and may inform how Toolbelt documents capability layers; it is **not** evidence for Cursor Agent Skills Spec / `SKILL.md` YAML progressive loading. Premises: (1) Q2/Q7 returned UX/RAG/framework senses only; (2) no agentskills.io or Cursor skills docs in hits.

#### Agent instruction & tool-description design (adjacent to skills / agents / commands)

- `CLAIM` [E2] Dibia: “A common mistake is building many general-purpose tools rather than fewer excellent, domain-specific ones…” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)….epub` chunk_id=`ed618cc3a5501d5562776c37` query=`fewer excellent domain-specific tools rather than many general-purpose`]

- `CLAIM` [E2] Dibia: treat system instructions as **model-specific** assets; version with model choice; A/B when switching models. Quote: “System messages aren’t portable across versions of the same model…” [E2: same chunk_id=`ed618cc3a5501d5562776c37` query=`AGENTS.md coding agent instructions`]

- `CLAIM` [E2] Dibia SWE agent: capabilities emerge from tools + prompts + context engineering; “an agent is only as capable as the tools it has and the instructions that guide their use.” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)….epub` chunk_id=`b6ad313a03312c92aa6ef1e0` query=`how to write effective tools/skills for LLM agents cold start context`]

- `CLAIM` [E2] Polzer: well-designed tools define purpose/inputs/outputs in docstrings; LLM uses them for selection; keep tools single-responsibility / domain-specific. Quote: “Well-designed tools define their purpose, inputs, and outputs through docstrings.” [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook… (Dominik Polzer)….pdf` chunk_id=`48662232d1fb4fbe046c7308` query=`describe tools for LLM agents tool descriptions cold start few tools domain-specific`]

- `CLAIM` [E2] Infante: tool descriptions must specify parameters, expected outputs, and when to use; selection quality depends on description quality. Quote: “Tool descriptions must specify input parameters, expected outputs, and when to use the tool.” [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents and Applications… (Roberto Infante)….pdf` chunk_id=`00b366b003c62ffc871a0744` query=`describe tools for LLM agents tool descriptions cold start few tools domain-specific`]

- `CLAIM` [E2] Pai: with many tools, keep short name+description in the prompt and retrieve detailed docs on selection (cold-start / context budget pattern). Quote: “If you have a lot of tools, then the detailed descriptions of the tools can be represented in a data store and retrieved only if they are selected. The prompt then needs to contain only the name of the tool and a short description.” [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Large Language Model Applications… (Suhas Pai)….pdf` chunk_id=`6cbf6cf1524fed5ebc3ca975` query=`describe tools for LLM agents tool descriptions cold start few tools domain-specific`]

- `CLAIM` [E2] Context-engine registry: human-readable capability descriptions for the planner LLM determine plan quality (“plain-text manual that the Planner reads”). [E2: Alexandria corpus=`ai_llm_agents` source=`Context Engineering for Multi_Agent Systems….pdf` chunk_id=`0daa1658d7b9728287fa082d` query=`agentskills.io Agent Skills Specification SKILL.md frontmatter name description`]

- `CLAIM` [E2] Ozdemir coding-agent system prompt embeds available functions + file-system modules for cold start without native tool-calling. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Workflows… (Sinan Ozdemir)….epub` chunk_id=`94ad9f44629ffa45950c9672` query=`AGENTS.md coding agent instructions`]

**Wave 1 map (`skills` / `agents` / `commands`):** `INFERENCE` [E4] Literature supports “fewer excellent tools + crisp descriptions + model-specific instructions + short cold-start catalog” as *agent authoring* norms transferable to how Toolbelt writes skills/rules text — **not** as Cursor file-format SoT. Premises: Dibia/Polzer/Infante/Pai CLAIMs above; absence of Cursor SKILL.md / AGENTS.md format in retrieval.

#### False friends / do-not-map

- `CLAIM` [E2] Lanham “skills/plugin” = Semantic Kernel folders (`config.json`, `skprompt.txt`), not Cursor Skills. Quote: “open the skills/Recommender/Recommend_Movies folder…” [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents in Action (Micheal Lanham)….pdf` chunk_id=`54f20bb1288afb810ea8f848` query=`Cursor IDE plugins rules skills hooks SKILL.md .mdc`]

- `CLAIM` [E2] AutoGen Studio “Adding skills” = agent tool/actions in Studio UI, not Cursor `SKILL.md`. [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents in Action…` chunk_id=`06d3f4d9294f5b063eabc35f` query=`agentskills.io Agent Skills Specification SKILL.md frontmatter name description`]

- `CLAIM` [E2] Dibia “hooks” (CompletionCheckHook / PlanningHook) = PicoAgents runtime verification hooks — **homonym** with Cursor `hooks.json`. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems…` chunk_id=`5e8d0ad3dbccf383dd55bec5` query=`how to write effective tools/skills for LLM agents cold start context`]

- `CLAIM` [E2] Osmani *Beyond Vibe Coding* discusses Cursor as AI IDE / background agents product — not plugin components (`plugin.json`, rules, skills). [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani)….epub` chunk_id=`046ed224a64c0bb89d03b284` query=`Cursor IDE plugins skills rules hooks`]

### 4.4 Explicit GAP log (Cursor plugin components)

| Wave 1 component | Searched (queries) | Result | Label |
|------------------|--------------------|--------|-------|
| **Skills** (`SKILL.md`, Agent Skills Spec, YAML frontmatter, agentskills.io) | Q1, Q2, Q7 | Hits = Semantic Kernel / AutoGen “skills”, progressive disclosure UX/RAG, capability registries — **no** agentskills.io Spec, **no** Cursor Skills docs, **no** `SKILL.md` frontmatter schema | `GAP` |
| **Rules** (`.mdc`, project rules packaging) | Q1, Q6, Q12 | No `.mdc` / Cursor rules packaging chunks; Osmani “hooks in React” false friend in SE index | `GAP` |
| **Hooks** (`hooks.json`, Cursor lifecycle hooks) | Q1, Q6, Q12 | PicoAgents hooks / React hooks only; no Cursor hooks.json | `GAP` |
| **MCP in plugins** (plugin-scoped `mcp.json`, plugin.json MCP fields) | Q4, Q6, Q8 | Host-level MCP + `~/.cursor/mcp.json` path anecdote only; **no** plugin packaging of MCP | `GAP` (host MCP adjacent CLAIM exists; plugin packaging still GAP) |
| **Agents / AGENTS.md** | Q3, Q11 | Coding-agent prompts / CrewAI / AutoGen — **no** `AGENTS.md` format law; SE corpus no AGENTS.md / llms.txt SoT | `GAP` |
| **Commands** (Cursor slash/commands packaging) | Q1, Q6 | MCP “slash command definition” for MCP servers only — not Cursor plugin commands | `GAP` |
| **Manifest** (`plugin.json`, marketplace identity) | Q6, Q12 | MCP marketplace tables / Cursor Directory MCP; **no** Cursor `plugin.json` / plugin marketplace SoT | `GAP` |

Staging reinforcement: `FACT` [E0] This deep pass **confirms** staging assessment that Alexandria lacks first-class Cursor official plugin/skills/rules/hooks docs and agentskills.io Spec for this campaign. [E0: T4J query set Q1–Q12 2026-07-29; consistent with `wave2-staging-alexandria-github.md`]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Alexandria contains Cursor plugin packaging SoT (SKILL.md / plugin.json / hooks.json / .mdc) | **rejected** | GAP table; false-friend skills/hooks only |
| H2 | Alexandria useful for MCP host/client packaging patterns adjacent to plugin MCP | **confirmed** (adjacent only) | §4.2 CLAIMs |
| H3 | Progressive disclosure hits map to Agent Skills Spec progressive loading | **rejected** | UX / RAG / framework-API senses only |
| H4 | `software_engineering` closes AGENTS.md GAP | **rejected** | Q11–Q12 product Cursor mentions only |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| “Skills” meaning | Lanham / AutoGen Studio = framework skills | Cursor Wave 1 Skills = `SKILL.md` Spec | Prefer Wave 1 E1 for Cursor; treat Alexandria “skills” as non-SoT / false friend |
| “Hooks” meaning | Dibia PicoAgents hooks | Cursor `hooks.json` | Do not map; leave Cursor hooks as GAP in Alexandria |
| Progressive disclosure | Dibia UX / Chollet API / Dhyani RAG | agentskills.io progressive disclosure (if any, Wave 1/E1) | Homonyms; no Spec corroboration from RAG |

## 7. Gaps & OPEN

- `GAP` Cursor-specific: `SKILL.md`, `.mdc` rules, `hooks.json`, plugin `mcp.json`, `AGENTS.md`, plugin commands, `plugin.json` / marketplace — not found as first-class sources in `ai_llm_agents` or `software_engineering` this pass.
- `OPEN` Ingest candidates for a future Alexandria shelf refresh: cursor.com/docs (skills, rules, hooks, plugins), agentskills.io Spec, cursor/plugin-template README — then re-run T4J-class queries.
- `OPEN` Primary reinforcement remains web + GitHub (T4H, T4I) per staging.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] **Do not lock** Cursor plugin architecture, file formats, or MVP scope on Alexandria book/survey chapters. Premises: H1 rejected; draft≠SoT; PROTOCOL cite-or-omit.
- `INFERENCE` [E4] For Toolbelt authoring culture (skill text, tool catalogs, MCP server quality), Alexandria **does** supply transferable patterns: fewer/better tools, docstring-quality descriptions, short cold-start catalogs with on-demand detail, model-specific instructions, MCP tools/resources/prompts packaging hygiene + secret handling awareness. Premises: §4.2–4.3; map carefully away from Cursor packaging SoT.
- `INFERENCE` [E4] Wave 2 diminishing-returns: further Alexandria queries on this theme unlikely to close Cursor-component GAPs without corpus ingest. Premises: Q1–Q12 consistent weak relevance; staging stop-rule.

## 9. Source list (deduped)

1. Alexandria `list_corpora` — 2026-07-29 (E0)
2. Hou et al., *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions* — chunks cited in §4.2
3. Victor Dibia, *Designing Multi-Agent Systems…* — progressive disclosure, tools, instructions, MCP multi-platform
4. Michael Albada, *Building Applications with AI Agents…* — progressive disclosure of capabilities
5. Roberto Infante, *AI Agents and Applications With LangChain, LangGraph, and MCP* — MCP architecture; tool description quality
6. Dominik Polzer, *RAG with Python Cookbook…* — custom tool docstring design
7. Suhas Pai, *Designing Large Language Model Applications* — short tool catalog + retrieve detailed docs
8. Deepak Dhyani, *RAG with Python Cookbook…* — progressive disclosure *response* generation (homonym)
9. Micheal Lanham, *AI Agents in Action* — Semantic Kernel / AutoGen “skills” (false friends)
10. Sinan Ozdemir, *Building Agentic AI Workflows…* — coding agent system prompts
11. *Context Engineering for Multi_Agent Systems…* — AgentRegistry capability descriptions
12. Addy Osmani, *Beyond Vibe Coding…* (`software_engineering`) — Cursor product, not plugins
13. Staging note: `docs/research/notes/theme-4-cursor-plugins/wave2-staging-alexandria-github.md`

---

**Self-check:** Method with exact queries ✓ · FACT/CLAIM cited ✓ · INFERENCEs list premises ✓ · No invented chunk_ids ✓ · Conflicts (skills/hooks/PD homonyms) logged ✓ · draft ≠ accepted SoT ✓
