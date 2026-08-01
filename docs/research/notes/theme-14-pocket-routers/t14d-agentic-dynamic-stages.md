---
title: "T14D — Agentic routing and dynamic stage handling"
status: draft
theme: theme-14-pocket-routers
track: T14D
created: 2026-07-31
updated: 2026-07-31
authors: [gatherer]
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
supersedes: null
---

# T14D — Agentic dynamic stages

## 1. Scope

- Question: What established patterns (RAG + primary web) help Toolbelt think about pocket routers vs happy-path vs leaf specialists?
- In scope: Router vs planner-executor vs pipeline; workflows vs agents; structured handoffs
- Out of scope: Locking LangGraph/CrewAI/etc. as Toolbelt runtime

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | Alexandria `rag_query` (`ai_llm_agents`); WebSearch; WebFetch (Anthropic partial via search/highlights) |
| Corpora / URLs | Alexandria `ai_llm_agents`; https://www.anthropic.com/engineering/building-effective-agents ; https://www.anthropic.com/engineering/multi-agent-research-system |
| Queries | RAG: “route between specialists, orchestrators, planners and executors…”; web: orchestrator router specialist dynamic stages |
| What was *not* searched | Full LangGraph docs pin; software_engineering corpus (weak relevance scores) |
| Depth | normal (enough signal; no deep fleet) |
| stop_reason | diminishing_returns — patterns converge across RAG + Anthropic |

## 3. Findings

### Primary / product engineering

- `CLAIM` [E1/E2] Anthropic distinguishes **workflows** (predefined orchestration paths) vs **agents** (model directs process); recommends **simplest solution first**; **routing** = classify input → specialized follow-up (separation of concerns). [E1/E2: https://www.anthropic.com/engineering/building-effective-agents — accessed 2026-07-31; page fetch timed out — claims from search highlights + known article structure; treat contested details as E2 until re-fetch]
- `CLAIM` [E1] Anthropic multi-agent research uses **orchestrator-worker**: lead coordinates; specialized subagents in parallel; structured plan/memory. [E1: https://www.anthropic.com/engineering/multi-agent-research-system — accessed 2026-07-31]

### Alexandria (secondary books)

- `CLAIM` [E2] Production multi-agent practice often settles on **Router + specialists** (router selects, does not solve), **Planner + workers**, **Producer + reviewer**; handoffs should be **structured like internal APIs** (goal, summary, facts+provenance, open question, constraints). [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex…` chunk_id=`618afba9e60090c0249026d4` query=`agent route specialists orchestrators`]
- `CLAIM` [E2] **Agentic workflow** vs **agent**: workflow = LLM chooses among **predefined** steps (router / controller-worker); agent = more dynamic tool/flow selection. [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents and Applications With LangChain, LangGraph, and MCP` chunk_id=`d5f0032cc4d3f623b2fcc345` query=same]
- `CLAIM` [E2] Planner→Executor with **agent registry** (capabilities list) is a common dynamic multi-stage engine: plan from registry, executor invokes specialists, tracer logs. [E2: Alexandria corpus=`ai_llm_agents` source=`Context Engineering for Multi_Agent Systems…` chunk_id=`3e7f820fec8a0ce6190ef432`]
- `CLAIM` [E3] Community blogs restate pipeline vs orchestrator-worker vs dynamic handoff / adaptive planning (secondary/community). [E3: e.g. beam.ai, gurusup.com — discovery only]

### Toolbelt-facing inferences

- `INFERENCE` [E4] Toolbelt pocket **router** matches Anthropic/LlamaIndex **routing workflow**: classify within a pocket → specialized leaf skills; router should **not** own leaf method law. Premises: (1) Anthropic routing CLAIM; (2) Theme 10 D8; (3) T14A gap.
- `INFERENCE` [E4] Happy-path matches a **sequential pipeline / caller workflow** of pocket routers more than a free swarm. Premises: (1) Theme 10 ladder E0; (2) Infante workflow vs agent CLAIM; (3) GitHub no-loops analogy T14C.
- `INFERENCE` [E4] Dynamic stage handling inside a pocket (skip plan-verify, choose execute vs -subagents, reproduce vs systematic) is **router responsibility**; end-to-end dynamism (re-order Research↔Design↔Execute arbitrarily) should stay **exceptional / human-directed**, not default happy-path. Premises: (1) Anthropic simplest-first; (2) Toolbelt draft≠SoT + human gates.
- `INFERENCE` [E4] Structured handoffs (goal, prior actions, facts+source, open question, constraints) should be a **router checklist item**, not a new always-on rule. Premises: LlamaIndex handoff CLAIM + Toolbelt announce-Using culture.
- `GAP` No Toolbelt-specific empirical eval of router skills yet (Theme 11 did not cover routers).
- `OPEN` How much **planner** (decompose) vs pure **router** (select among fixed leaves) belongs in Implementation router — design decision.

## 4. Conflicts

| Topic | Sources | Prefer for Toolbelt |
|-------|---------|---------------------|
| Fully dynamic agents vs fixed workflows | Anthropic: agents when flexibility needed; workflows when predictable | Default = **workflow + routing**; escalate to dynamic only with documented skip/human |
| Global skill-router always-on | craftwork (T14B) vs Anthropic simplest-first | **No** always-on global router |

## 5. Next

T14E shape options lean (draft).
