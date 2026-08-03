---
title: "Deep T19F — RAG apply / selective context patterns"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
depth: deep
track: T19F
authors: [research-gatherer]
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
  - docs/research/notes/theme-19-standards-apply/t19i-shape-options-lean.md
---

# Deep T19F — RAG (selective standards / context apply)

**Using `research-protocol`.** Depth: **deep**. Wave: W1 RAG.

## 1. Scope

- **Question:** How do SE / agent guides describe progressive disclosure or loading *relevant* conventions without stuffing full style corpora into every prompt?
- **Out of scope:** Locking Toolbelt skill ids; writing host standards content.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-08-03 |
| Tools | Alexandria `rag_query` |
| Corpora | `ai_llm_agents`, `software_engineering` |
| Queries (exact) | (1) How should coding agents load project conventions, AGENTS.md, coding standards, or rules progressively without putting the entire style guide in context? Context routing, selective load, when to read standards. corpus=`ai_llm_agents` k=10 (2) progressive disclosure coding standards style guide modular documentation for developers agents load relevant conventions only corpus=`software_engineering` k=8 |
| Not searched | Full primary PDFs outside retrieved chunks; Feathers |
| Depth / waves | W1 RAG; SE hit quality weak (index-heavy) — label honestly |
| stop_reason (this note) | Named transferable atoms found in `ai_llm_agents`; SE pass mostly non-applicable index noise |

## 3. Findings

### 3.1 Context engineering / selective include (`ai_llm_agents`)

- `FACT` [E2] Broda *Agentic Mesh*: context engineering is selecting, structuring, and delivering the right information to an LLM at the right time; irrelevant text can dilute reasoning; multi-agent systems compound the problem — only a subset of messages/tool outputs is useful for the next decision. Practical layers include RAG, reranking, compression/summaries, and **slotting** reserved prompt sections for “must include” items (e.g. safety rules). [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh…` chunk_id=`6daf3081f797c0c94712cce0`]
- `FACT` [E2] Albada *Building Applications with AI Agents*: context engineering decides what to include, how to structure it, and how to fit token limits; prioritize relevance rather than indiscriminately appending large blocks; each added element can help only if included thoughtfully. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents…` chunk_id=`4b9a08fc084f85631bcc5c68`]
- `FACT` [E2] *Context Engineering for Multi-Agent Systems* (retrieved Q&A / narrative): a **Librarian** specialist finds the right **style guide** by searching descriptions (not the entire JSON/code block); Writer must follow the guide the Librarian finds; Orchestrator packages facts + style guide for the Writer; facts and style guides live in separate labeled sections of one store. [E2: Alexandria corpus=`ai_llm_agents` source=`Context Engineering for Multi_Agent Systems…` chunk_ids=`d51865d1ce28efb07216b934`, `07fcd3699bc730f7b2bf0b28`]
- `CLAIM` [E2] Same Context Engineering text: Planner uses an **agent registry / capabilities catalog** so it knows who does what — directory of specialists, not dumping every specialist’s full procedure into every step. [E2: chunk_id=`07fcd3699bc730f7b2bf0b28`]
- `CLAIM` [E2] n8n beginners handbook (agentic RAG): access controls — not all agents need access to everything; dynamic knowledge-base selection by question. [E2: Alexandria corpus=`ai_llm_agents` source=`n8n BOOK FOR BEGINNERS…` chunk_id=`e2d0cfa80cdb379cb5ce1789`]
- `INFERENCE` [E4] Transferable atoms for Theme 19 O1: (1) select relevant standards context per step; (2) separate “which guide” lookup from “full guide body”; (3) optional specialist/router role analogous to Librarian / standards-router; (4) slot thin must-include (safety) vs on-demand modules. Premises: FACT/CLAIM set above; O1 lean accepted.

### 3.2 `software_engineering` pass

- `GAP` Query on progressive disclosure / modular standards for agents returned mostly Clean Architecture **index** entries and generic style-convention mentions — not a primary method for agent selective-load of standards. [E2 weak / non-applicable: e.g. chunk_ids `dbf1a6e8aacce5316b1182b3`, `3e5673689e5a09e818f1f9da`]
- `FACT` [E2] FDG foreword (prior Theme 16 corpus familiarity; chunk also retrieved in SE sampling contexts): following existing project conventions helps converge old and new code — supports *having* standards, not *how* agents slice-load them. [E2: corpus=`software_engineering` source=`Framework Design Guidelines…` chunk_id=`95542d0ca16cd64a8670970c` — corroborative only]

## 4. Implications for O1

| O1 piece | RAG support |
|----------|-------------|
| Thin ambient gate | Slot “must include” / safety; not full corpus [E2 Broda] |
| standards-router | Librarian / registry / dynamic KB selection analogues [E2] |
| Module pointers then load | Search description → then fetch body [E2 Context Engineering] |
| No mega dump | Explicit anti-pattern in context engineering texts [E2 Albada/Broda] |

## 5. Source list (chunk_ids)

1. `6daf3081f797c0c94712cce0` — Agentic Mesh context engineering  
2. `4b9a08fc084f85631bcc5c68` — Albada context engineering  
3. `d51865d1ce28efb07216b934`, `07fcd3699bc730f7b2bf0b28` — Context Engineering multi-agent Librarian/registry  
4. `e2d0cfa80cdb379cb5ce1789` — n8n agentic RAG access/dynamic KB  
5. SE index chunks — GAP for method transfer  
