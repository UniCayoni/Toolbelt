---
title: "T23B-RAG — playbook / operator-doc patterns (Alexandria)"
status: draft
theme: theme-23-host-playbook
track: T23B
created: 2026-08-04
updated: 2026-08-04
authors: [t23b-rag-gatherer]
depth: deep
wave: 1
supersedes: null
aligned_with:
  - docs/research/notes/theme-23-host-playbook/campaign-brief.md
  - docs/PROTOCOL.md
---

# T23B-RAG — Playbook / operator-doc patterns

**Using `research-protocol`**. Depth: **deep**. Cite-or-omit. Draft ≠ SoT.

## 1. Scope

- **Question / goal:** What do Alexandria corpora say about writing **playbooks**, **operator guides**, **runbooks**, **onboarding docs**, and **progressive disclosure** for tools/agents — transferable to a **Toolbelt host adoption playbook** (Cursor agent-skills plugin consumer)?
- **In scope:** Patterns from `software_engineering` and `ai_llm_agents` (optional PAS if SE/agents thin); structure, onboarding, sync/drift, tool/skill documentation for users/operators.
- **Out of scope:** Writing the final `docs/host-playbook.md`; Theme 24 learn-back; contributor CI; inventing Diataxis/law from parametric memory; finance/game shelves unless clearly about documentation playbooks.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools used | Alexandria MCP `user-alexandria-rag`: `list_corpora`, `rag_probe`, `rag_query`, `rag_fetch_chunk` |
| Corpora / URLs searched | Prefer: `software_engineering` (21 docs / 7712 chunks), `ai_llm_agents` (71 / 22720). Optional probe: `programming_algorithms_systems`. Skipped: `finance_trading`, `game_design`, `games_engine_graphics`, `data_sql`. |
| Queries (exact) | See §2.1 |
| What was *not* searched | Web/GitHub primary docs; Diataxis site; Toolbelt E0 skill inventory (T23A); finance/game shelves; hierarchical RAG mode |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer. **stop_reason:** diminishing returns — after ~12 `rag_query` + probes, new hits restated runbook / docstring / README-TOC atoms; **progressive disclosure** as a documentation term was **absent** (architecture/index noise); PAS probe weak/off-topic; no new P0 atoms for host playbook craft. |
| Provenance (optional PROV) | Entity←Alexandria chunks; Activity=T23B-RAG deep gather 2026-08-04; Agent=t23b-rag-gatherer + user-alexandria-rag |

### 2.1 Exact queries

**Probes (`rag_probe`):**

1. `playbook vs runbook vs guide documentation structure` → `software_engineering` (partial)
2. `operator onboarding documentation getting started guide` → `software_engineering` (partial)
3. `progressive disclosure documentation documentation architecture` → `software_engineering` (partial; mostly architecture layers)
4. `keeping documentation in sync with changing tools APIs` → `software_engineering` (partial)
5. `agent skills tool use documentation for users getting started` → `ai_llm_agents` (partial)
6. `playbook runbook operator guide for AI agents tools` → `ai_llm_agents` (partial)
7. `progressive disclosure documentation getting started guide operator handbook` → `programming_algorithms_systems` (partial; off-topic tops)

**Queries (`rag_query`, k=4–8):**

1. `playbook vs runbook vs guide documentation structure for operators` → `software_engineering`
2. `progressive disclosure documentation architecture layered docs for users` → `software_engineering`
3. `keeping documentation in sync with changing APIs and tools documentation drift` → `software_engineering`
4. `getting started guides for developer tools onboarding documentation best practices` → `software_engineering`
5. `how to document agent tools and skills for operators and end users` → `ai_llm_agents`
6. `playbook runbook operator guide structure for AI agents and tool use` → `ai_llm_agents`
7. `README documentation structure table of contents setup development environment for software component` → `software_engineering`
8. `documentation as modularization principle separation of concerns for maintainability` → `software_engineering`
9. `tool contracts docstrings descriptions when and how to use tools for LLM agents` → `ai_llm_agents`
10. `operator workbench playbook for running and governing AI agents in production` → `ai_llm_agents`
11. `model cards documentation intended use cases limitations when not to use` → `software_engineering`
12. `Documentation principle of modularization what documentation should include for modules` → `software_engineering`
13. `guide tool usage clearly order of operations when and how to use each tool instructions for agents` → `ai_llm_agents`
14. `runbooks for each metric alert so everyone knows what to do operational documentation` → `software_engineering`

**Fetches:** `rag_fetch_chunk` `chunk_id=e90b23a2a0acaf64ae846e3b` neighbors=1 (neighbor `35a29bce0149220c70a53f48`).

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed (RAG-only gatherer) |
| Why this mode | T23B Wave 1 RAG leg; no E0 inventory in this note |
| Scope boundary | Alexandria secondary literature only |

## 4. Findings

### 4.1 Runbooks (ops response docs) vs “playbooks”

- `CLAIM` [E2] After deployment of AI-touched systems, authors recommend **operational runbooks** for the ops team that document non-obvious behaviors (model quirks, caching, temp-file deps) so responders know what to check. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani)` chunk_id=`9f9966bbcd04f4f531da73cf` query=`playbook vs runbook vs guide documentation structure for operators`] Quote: “Provide runbooks for the ops team that describe any special aspects…”
- `CLAIM` [E2] In an architecture-metrics case study, for each monitored metric the team **built runbooks** so everyone knew the response; each runbook **referenced the metrics** to diagnose and cut false positives, plus diagnostic APIs/tools. [E2: Alexandria corpus=`software_engineering` source=`Software Architecture Metrics…` chunk_id=`403e33e231c9d33f127e1939` query=`runbooks for each metric alert so everyone knows what to do operational documentation`]
- `FACT` [E2] Index entry in same Osmani book points to “operational runbooks” under ongoing best practices. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`34162bc8eb119388c0b24550` query=`playbook vs runbook vs guide documentation structure for operators`]
- `GAP` Searched: playbook vs runbook vs guide (SE + agents). Result: **no** clear comparative taxonomy of “playbook vs runbook vs guide” as documentation genres; “playbook” hits were mostly **Ansible IaC** or agent **ACE strategy** playbooks (see § False friends).

### 4.2 Onboarding / getting-started structure

- `CLAIM` [E2] **Software Component Documentation Principle:** each component needs docs whose **main idea is quickly onboarding new people**; critical that **dev-environment setup** is well-documented and easy; also document problem domain and OOD. [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)` chunk_id=`35a29bce0149220c70a53f48` query=`README documentation…` / fetch neighbor of `e90b23a2a0acaf64ae846e3b`]
- `CLAIM` [E2] Recommended layout: root `README.MD` + split files under `docs/` (reduce merge conflicts); example TOC: short purpose → feature list (link Gherkin rather than duplicate) → architecture / data-flow / per-subdomain OOD → **auto-generated API docs** for libraries → implementation notes → **setup / build / unit-test** instructions (dev containers preferred for setup). [E2: Alexandria corpus=`software_engineering` source=`Clean Code… (Silen)` chunk_id=`e90b23a2a0acaf64ae846e3b` query=`README documentation structure table of contents…`]
- `CLAIM` [E2] Research-software packaging checklist expects README to state **motivation / audience**, **install**, **example usage**, plus deeper API docs elsewhere (e.g. Read the Docs); CONTRIBUTING for community paths. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python…` chunk_id=`19b65d1fd83a0a318bd1c898` query=`README documentation structure…`]
- `CLAIM` [E2] Silen intro restates documenting components so **onboarding new developers is quick and easy**. [E2: Alexandria corpus=`software_engineering` source=`Clean Code… (Silen)` chunk_id=`c9be4f5ec3dab516840608ef` query=`runbooks for each metric alert…` (secondary hit)]

### 4.3 Sync / drift / single source of truth

- `CLAIM` [E2] For **library public APIs**, comments should feed **auto-generated API documentation** “to avoid situations where API comments and docs are out of sync.” [E2: Alexandria corpus=`software_engineering` source=`Clean Code… (Silen)` chunk_id=`b594c791e9f5df63210b2a27` query=`keeping documentation in sync with changing APIs and tools documentation drift`]
- `CLAIM` [E2] Feature lists can **link** Gherkin feature files so the same information is **not stored in two places**. [E2: Alexandria corpus=`software_engineering` source=`Clean Code… (Silen)` chunk_id=`e90b23a2a0acaf64ae846e3b` query=`README documentation structure…`]
- `CLAIM` [E2] Ops guidance: watch for **drift** (e.g. AI-generated SQL vs migrations) and keep code/migrations/deploy in sync; humans monitor automations. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`69b47b61979e5a6d0b4f4f00` query=`keeping documentation in sync…`]
- `CLAIM` [E2] Agents need strategies for **tool updates and versioning**, deprecated features, and adapting to new tool interfaces. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems` chunk_id=`c4b3a514f592b5583f106a0d` query=`playbook runbook operator guide structure for AI agents and tool use`]
- `CLAIM` [E2] Custom tools that call external services “need testing, debugging, and **updates as APIs change**.” [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook (Dominik Polzer)` chunk_id=`48662232d1fb4fbe046c7308` query=`tool contracts docstrings…`]

### 4.4 Progressive disclosure / layered entry

- `CLAIM` [E2] Modularization requires **clear documentation of module interfaces, dependencies, and usage guidelines** so developers understand interaction and integration. [E2: Alexandria corpus=`software_engineering` source=`Clean Architecture with .NET (Dino Esposito)` chunk_id=`b60d8cff13de880cb7adba88` query=`Documentation principle of modularization…`]
- `CLAIM` [E2] Modularization principles include Documentation alongside SoC, loose coupling, dependency management, testability; SoC = each module a **clearly defined and focused purpose**. [E2: Alexandria corpus=`software_engineering` source=`Clean Architecture with .NET` chunk_id=`c5273b4d72576b8d4cf8a3a4` query=`documentation as modularization principle…`]
- `CLAIM` [E2] Enterprise agent UX: a **home view orients** users to the right surface (marketplace / consumer / creator / trust / **operator** workbench); each surface is **opinionated about its job** while sharing identity/policy/traceability patterns — progressive *entry by role*, not one encyclopedia page. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh… (Eric Broda, Davis Broda)` chunk_id=`d3337c395696e47f8a118c48` query=`operator workbench playbook…`]
- `GAP` Searched: “progressive disclosure documentation…” (SE + PAS). Result: **no** usable chunks teaching progressive disclosure as a **doc-writing** technique; hits were layered **software** architecture, indexes, or off-topic PAS. Treat progressive disclosure for Toolbelt playbook as **OPEN** pending web/docs/E0 Theme 2 layers — not locked from this RAG pass.

### 4.5 Documenting tools / skills for agents and operators

- `CLAIM` [E2] Tools are defined with clear descriptions (docstrings or JSON schema) communicating **purpose, required inputs, expected outputs**; LLM needs at minimum description + expected input. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems` chunk_id=`05b44354ee921a9ccba99711` query=`tool contracts docstrings…`]
- `CLAIM` [E2] Docstrings provide purpose, parameters, return values, helping the LLM understand **when and how** to use each tool; that documentation is the context guiding decisions. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems` chunk_id=`d70776b1b7cbd9b120af5c4c` query=`playbook runbook operator guide structure…`]
- `CLAIM` [E2] Well-designed tools define purpose/inputs/outputs through docstrings; the LLM reads them to choose tools and chain workflows; keep each tool **single responsibility**. [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook` chunk_id=`48662232d1fb4fbe046c7308` query=`tool contracts docstrings…`]
- `CLAIM` [E2] **Default tool description isn’t enough** — give precise instructions on **when and how**, including **order of operations** and required inputs (e.g. get list ID before create card). [E2: Alexandria corpus=`ai_llm_agents` source=`n8n BOOK FOR BEGINNERS…` chunk_id=`d926f29ed6b623ff81496772` query=`guide tool usage clearly…`]
- `CLAIM` [E2] Agents can access **tool documentation** to invoke tools correctly (alongside prompts/history). [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Large Language Model Applications (Suhas Pai)` chunk_id=`38e9160cc046590caba106ab` query=`how to document agent tools…`]
- `CLAIM` [E2] Agent capability = interplay of **tools** (what’s possible), **prompts/instructions** (how to use), and context engineering. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems (Victor Dibia)` chunk_id=`b6ad313a03312c92aa6ef1e0` query=`guide tool usage clearly…`]
- `CLAIM` [E2] LlamaIndex: descriptive docstrings are extracted so agents understand **when and how** to use a FunctionTool. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex…` chunk_id=`f9c6d8a81b810af793d2248a` query=`tool contracts docstrings…`]
- `CLAIM` [E2] Operator workbench focuses on **performance/reliability** (observability, diagnostics/logs/audit, start/stop/pause) — distinct from developer/consumer task content. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh…` chunk_id=`33721951ff8df33465c28d3c` query=`operator workbench playbook…`]

### 4.6 “When not” / inventory-card shape / start-small

- `CLAIM` [E2] **Model cards** as standardized transparency docs (“nutrition labels”): identity/version, **intended use cases**, **scenarios where the model should not be used**, performance/fairness notes, dataset limits, risks. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`8fb25e011a77d79c0de11fe8` query=`model cards documentation intended use cases limitations when not to use`]
- `CLAIM` [E2] Document **AI usage decisions** internally (why a suggestion was/wasn’t used) to onboard new members and support audits. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`f41473323803bb4fae2c6399` query=`model cards…`]
- `CLAIM` [E2] Guidance: **always start small**, test thoroughly, gradually expand agent capabilities; attend to clear task definition. [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering AI Agents… (Pratik Bhavsar)` chunk_id=`30404208ef719d3c2fb95362` query=`playbook runbook operator guide structure…`]
- `CLAIM` [E2] Test each component separately before wiring a full multi-agent system. [E2: Alexandria corpus=`ai_llm_agents` source=`n8n BOOK FOR BEGINNERS…` chunk_id=`d926f29ed6b623ff81496772` query=`guide tool usage clearly…`]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | SE corpus would yield Diataxis / progressive-disclosure doc craft | rejected / GAP | Probes returned architecture layers / indexes, not doc progressive disclosure |
| H2 | “Playbook” in corpora often means Ansible or agent ACE, not host adoption | confirmed | Ansible chunks + ACE evolving playbooks |
| H3 | Strongest transferable atoms = onboarding TOC + runbooks + tool/skill cards + sync-from-source | confirmed | Silen, Osmani, Architecture Metrics, agent tool-doc cluster |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Meaning of “playbook” | Ansible IaC YAML (Percival TDD book) | ACE “evolving playbooks” for agent self-strategy (Funderburk) | Neither is Toolbelt **host adoption** playbook; treat both as false friends; prefer “runbook” / “operator guide” / “component docs” atoms for transfer |
| Who docs serve | Silen: **developer onboarding** | Agentic Mesh: **ops** vs consumers vs creators | Complementary audiences — host playbook may need a thin start-here + pointers, not one role’s encyclopedia |

## 7. Gaps & OPEN

- `GAP` Progressive disclosure / Diataxis-style doc taxonomy **not found** in preferred corpora under that wording.
- `GAP` No corpus chunk defining host-plugin “adoption playbook” structure for Cursor skills specifically.
- `OPEN` Corroborate progressive-disclosure / start-here-vs-catalog with Theme 2 doc-layers / web Diataxis / GitHub host-plugin READMEs (other T23B legs).
- `OPEN` Map Silen TOC + model-card fields onto T23A inventory columns (intent / good-for / limits / next).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] A Toolbelt host playbook should prioritize **fast onboarding** (setup + purpose + first successful use) over dumping the full skill encyclopedia. Premises: Silen onboarding principle (`35a29bce0149220c70a53f48`); role-oriented home/surfaces (`d3337c395696e47f8a118c48`).
- `INFERENCE` [E4] Per-surface “cards” should include **intended use** and **when not to use**, analogous to model cards. Premises: `8fb25e011a77d79c0de11fe8`; campaign vocabulary intent/good-for/limits.
- `INFERENCE` [E4] Catalog depth should **link to SoT** (SKILL.md / guides) rather than duplicate; maintenance = update gate when surfaces change. Premises: Silen link-don’t-duplicate + API auto-gen (`e90b23a2a0acaf64ae846e3b`, `b594c791e9f5df63210b2a27`); tool versioning (`c4b3a514f592b5583f106a0d`).
- `INFERENCE` [E4] Host playbook should state **when/how/order** to invoke skills (not only names), mirroring agent tool-instruction practice. Premises: `d926f29ed6b623ff81496772`, `d70776b1b7cbd9b120af5c4c`, `b6ad313a03312c92aa6ef1e0`.
- Do **not** promote these to design lock without T23 integrate + human accept (`draft-is-not-sot`).

## 9. Patterns transferable to Toolbelt host playbook

1. **Onboarding-first layered TOC** — Purpose → features (link, don’t clone) → architecture/map → deep refs → setup/first-run; README + `docs/` split. (Silen)
2. **Per-surface “nutrition label”** — Identity, intended use, **when not**, limits/risks (model-card shape adapted to skills/rules). (Osmani)
3. **Runbook-grade “when things go wrong”** — Non-obvious failure modes + what to check; optionally tie to smoke/alerts. (Osmani; Architecture Metrics)
4. **Skill/tool cards state when / how / order** — Default blurb insufficient; include handoffs and prerequisites. (n8n; Building Agentic AI Systems; Dibia)
5. **Single-source + update contract** — Point to SKILL.md / packs; regenerate or gate docs when surfaces/APIs change. (Silen; tool versioning cluster)
6. **Role-separated entry** — Home/start-here routes host to adopt vs operate vs contribute paths; each surface one job. (Agentic Mesh UX)
7. **Start small, expand** — Document smallest successful adoption path before full toolbox. (Mastering AI Agents; n8n component testing)

## 10. False friends / do not import

| Pattern | Why not for Toolbelt host playbook |
|---------|-----------------------------------|
| **Ansible playbooks** | Declarative IaC automation YAML (Percival TDD book chunks `bd036cb85d37b29435403c12`, `f4c3d8772fa42df0b8ff2fa6`) — not human adoption guides. |
| **ACE “evolving playbooks”** | Agent self-reflection/strategy loops (Funderburk `9740ff6f59f82785d95400d3`) — not host-facing plugin docs. |
| **Game QA doc types** (GDD, Game Bible, etc.) | Domain-specific production docs; not operator adoption for agent skills. |
| **Microservice/Kubernetes ops encyclopedia** | Silen DevSecOps depth exceeds host plugin adopt scope; steal onboarding TOC, not cluster runbooks. |
| **“Progressive disclosure” via layered app architecture** | Clean Architecture layering ≠ documentation progressive disclosure; do not relabel SoC layers as playbook craft. |
| **Poisoned tool-description / AgentSecOps attacks** | Security threat model for agent metadata (Funderburk) — awareness only; not a playbook TOC pattern. |

## 11. Source list (deduped)

1. Alexandria `software_engineering` — Silen, *Clean Code Principles And Patterns Python Edition* (`e90b23a2a0acaf64ae846e3b`, `35a29bce0149220c70a53f48`, `b594c791e9f5df63210b2a27`, `c9be4f5ec3dab516840608ef`)
2. Alexandria `software_engineering` — Osmani, *Beyond Vibe Coding* (`9f9966bbcd04f4f531da73cf`, `8fb25e011a77d79c0de11fe8`, `f41473323803bb4fae2c6399`, `69b47b61979e5a6d0b4f4f00`, `34162bc8eb119388c0b24550`)
3. Alexandria `software_engineering` — *Software Architecture Metrics* (`403e33e231c9d33f127e1939`)
4. Alexandria `software_engineering` — Esposito, *Clean Architecture with .NET* (`b60d8cff13de880cb7adba88`, `c5273b4d72576b8d4cf8a3a4`)
5. Alexandria `software_engineering` — Irving et al., *Research Software Engineering with Python* (`19b65d1fd83a0a318bd1c898`)
6. Alexandria `software_engineering` — Percival, *TDD with Python* (Ansible false friend: `bd036cb85d37b29435403c12`)
7. Alexandria `ai_llm_agents` — *Building Agentic AI Systems* (`05b44354ee921a9ccba99711`, `d70776b1b7cbd9b120af5c4c`, `c4b3a514f592b5583f106a0d`)
8. Alexandria `ai_llm_agents` — Polzer, *RAG with Python Cookbook* (`48662232d1fb4fbe046c7308`)
9. Alexandria `ai_llm_agents` — n8n beginners handbook (`d926f29ed6b623ff81496772`)
10. Alexandria `ai_llm_agents` — Pai, *Designing LLM Applications* (`38e9160cc046590caba106ab`)
11. Alexandria `ai_llm_agents` — Dibia, *Designing Multi-Agent Systems* (`b6ad313a03312c92aa6ef1e0`)
12. Alexandria `ai_llm_agents` — Gheorghiu, *LlamaIndex* (`f9c6d8a81b810af793d2248a`)
13. Alexandria `ai_llm_agents` — Broda, *Agentic Mesh* (`33721951ff8df33465c28d3c`, `d3337c395696e47f8a118c48`)
14. Alexandria `ai_llm_agents` — Bhavsar, *Mastering AI Agents* (`30404208ef719d3c2fb95362`)
15. Alexandria `ai_llm_agents` — Funderburk (ACE playbooks false friend: `9740ff6f59f82785d95400d3`)

### Citation count

**Unique cited `chunk_id`s:** 27  
(FACT/CLAIM support + explicit false-friend locators; no invented IDs.)
