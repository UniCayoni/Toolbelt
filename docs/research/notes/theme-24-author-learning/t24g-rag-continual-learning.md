---
title: "T24G-RAG — continual-learning / harvest patterns (Alexandria)"
status: draft
theme: theme-24-author-learning
track: T24G
created: 2026-08-05
updated: 2026-08-05
authors: [t24g-rag-gatherer]
depth: deep
wave: 1
supersedes: null
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
  - docs/PROTOCOL.md
---

# T24G-RAG — Continual-learning comparators (Alexandria)

**Using `research-protocol`**. Depth: **deep**. Cite-or-omit. **Draft ≠ SoT.**

**Hard fence:** Patterns inform **host/workspace** harvest candidates (skills, standards, AGENTS) via proposed deltas + human accept — **not** Toolbelt plugin `skills/*` rewrite; **never** silent auto-promotion.

## 1. Scope

- **Question / goal:** What patterns exist for harvesting learnings into **durable workspace knowledge** without **silent auto-promotion**?
- **In scope:** Continual / nonparametric learning for agents; agent memory tiers; retrospective / Reflexion-style loops; learning from failures; exemplar / experience-store patterns; feedback pipelines; HITL review and gated validation; documentation as organizational memory.
- **Out of scope:** Web/GitHub primary sources (T24G-web / T24G-gh); elevating `author-learning` skill; rewriting Toolbelt plugin skills; CI ceremony; personal (non-workspace) memory as primary SoT; locking design from this note alone.
- **Comprehension / research goal type:** other (comparator literature for Theme 24 method).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | Alexandria MCP `user-alexandria-rag` / `rag_query` (schema via `GetMcpTools` first) |
| Corpora / URLs searched | Primary: `ai_llm_agents` (all + corpus-scoped). No other shelves. |
| Queries (exact) | See §2.1 |
| What was *not* searched | Web; GitHub; Cursor docs; Toolbelt E0 surfaces; hierarchical RAG; `query_transform`; finance/game/SE shelves; experience-replay papers by name beyond RAG hits |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer. **stop_reason:** diminishing returns after 3 `rag_query` passes — new hits restated Albada improvement-loop / Reflexion / memory-tier atoms; no corpus hit on “workspace AGENTS.md / host standards promotion gate” as a named pattern. |
| Provenance (optional PROV) | Entity←Alexandria `ai_llm_agents` chunks; Activity=T24G-RAG deep gather 2026-08-05; Agent=t24g-rag-gatherer + user-alexandria-rag |

### 2.1 Exact queries

1. `continual learning for agents; agent memory; retrospective feedback loops; learning from failures; experience replay for LLM agents; workspace memory; human-in-the-loop promotion of learnings. What patterns exist for harvesting learnings into durable workspace knowledge WITHOUT silent auto-promotion?` → corpus=`all`, k=12
2. `human-in-the-loop review promote improvements feedback pipelines documentation organizational memory validate before deployment no automatic promotion agent learnings` → corpus=`ai_llm_agents`, k=10
3. `experience replay buffer learn from failures retrospective reflection memory buffer exemplar store successful examples agent learning without fine-tuning` → corpus=`ai_llm_agents`, k=8

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | as-needed (RAG-only gatherer) |
| Why this mode | T24G Wave 1 RAG leg; web/gh parallel elsewhere |
| Scope boundary | Alexandria secondary books in `ai_llm_agents` only |

## 4. Findings

**Grade note:** Retrieved sources are **published secondary books** → labeled **[E2]** (secondary). **[E3]** reserved for community forums/blogs/issue threads — **none used as locks here**. Do not promote E2 book patterns to Toolbelt design law without acceptance.

### 4.1 Improvement loop: observe → propose → validate → embed (gates, not silent promote)

- `CLAIM` [E2] Continuous improvement is an interconnected cycle: (1) feedback pipelines observe/categorize failures and surface insights via **automation + HITL review**; (2) **proposed** improvements are **validated** in controlled environments (shadow deployments, A/B testing, Bayesian Bandits) before broader rollout; (3) only then are improvements **embedded** via in-context learning or offline retraining. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents… (Michael Albada)` chunk_id=`6d14bb768510009b99b076b7` query=`…WITHOUT silent auto-promotion` / HITL query] Quote: “proposed improvements must be validated… before… Finally, improvements must be embedded…”
- `CLAIM` [E2] Feedback pipelines are the diagnostic engine; experimentation validates before full deployment; continuous learning embeds adaptations; **human oversight** keeps changes aligned with strategic goals; **documentation** preserves organizational memory across the cycle. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`bbe9e02c915899e1f6c3f4cb` query=`human-in-the-loop review promote…`] Quote: “human oversight ensures that changes are aligned… Documentation serves as the connective tissue…”
- `CLAIM` [E2] Table of methodologies: feedback pipelines blend automation and human oversight and build **improvement backlogs**; experimentation reduces risk **predeployment**; continuous learning has overfitting/regression risks and needs monitoring. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`fc2367198e347abd88cd93ca` query=`human-in-the-loop review promote…`]
- `INFERENCE` [E4] This staged loop is a comparator for “harvest → **proposed** candidate → human/experiment gate → durable embed,” opposing silent auto-promotion into SoT. Premises: (1) CLAIMs on propose/validate/embed above; (2) Theme 24 hard fence (accepted brief). Does **not** lock Toolbelt surfaces.

### 4.2 HITL review: humans approve / override automated recommendations

- `CLAIM` [E2] HITL review complements automated detection/RCA for ambiguous intent, ethics, conflicting goals, or novel edge cases; humans review agent **output candidates** and provide feedback culminating in **human-approved** outputs; system feedback loops back. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`98e29b82cc8c92a02ec884e6` query=`human-in-the-loop review promote…`] Quote: “human-approved outputs… System feedback from the review process loops back…”
- `CLAIM` [E2] Automated pipelines can **propose** prompt/tool/reasoning refinements from failure data, but engineers must **review, validate, and override** recommendations; automation amplifies humans, does not replace judgment. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`980437391eeefeb6d64d7a78` query=`human-in-the-loop review promote…`] Quote: “engineers must review, validate, and, when necessary, override the recommendations…”
- `CLAIM` [E2] Index maps HITL review to feedback pipelines (and separately HITL validation / escalation criteria). [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`64d93a22dca17db98ae93ca9` / `b5e7417118a3c639fc0c1dcd` query=`human-in-the-loop review promote…`]
- `CLAIM` [E2] Production HITL workflows route high-value / sensitive / uncertain cases to humans **before executing actions**; approved and rejected cases can become training data to refine thresholds — logging decisions, not silent policy write. [E2: Alexandria corpus=`ai_llm_agents` source=`AI Agents and Applications… (Roberto Infante)` chunk_id=`e787ec9011337cc21b505474` query=`human-in-the-loop review promote…`]
- `GAP` Searched: “human-in-the-loop **promotion of learnings**” into workspace skills/standards/AGENTS. Result: HITL is described for **output approval**, **feedback pipelines**, and **escalation** — not for promoting reflections into host Cursor surfaces. Treat workspace-surface promotion gate as Theme 24 design work (OPEN for T24E / author path), not found as named pattern here.

### 4.3 Organizational / documented memory vs runtime memory

- `CLAIM` [E2] Improvement loops need systems for **documenting insights**, prioritizing improvements, and safeguarding against unintended consequences — organizational, not only model-weight, learning. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`6d14bb768510009b99b076b7` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] Agents externalize memory into logs, databases, knowledge graphs, or vector embeddings; reflection turns memory from passive store into improvement driver; fleets may share stores. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh… (Eric Broda, Davis Broda)` chunk_id=`a8535eb03e5bf44a0d6c386f` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] Memory hierarchy: native (weights) → short-term/contextual (volatile) → long-term/external (RAG and similar); short-term dissipates unless summarized/stored. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh…` chunk_id=`3882173e32b14e57682ec8a2` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] Short-term vs long-term memory; distinction between **application-managed** (automatic store/retrieve by code) and **agent-managed** (agent decides what to store/retrieve) memory. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems… (Victor Dibia)` chunk_id=`3408937256594a6e23b4cf10` query=`…WITHOUT silent auto-promotion`]
- `INFERENCE` [E4] Durable **workspace** knowledge (host skills/standards/AGENTS) is closer to documented organizational memory + curated external store than to silent agent-managed writebacks. Premises: documentation/HITL CLAIMs (§4.2–4.3); Theme 24 target = host surfaces. Still proposed-only.

### 4.4 Nonparametric harvest stores: exemplars, Reflexion buffers, experience banks

- `CLAIM` [E2] Nonparametric exemplar learning: quality-labeled examples become few-shot context; richer form builds a **memory bank** of context/actions/outcomes/feedback and retrieves similar cases (case-based style). [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`038c563d49a057f9bfb23691` query=`experience replay buffer…`]
- `CLAIM` [E2] Saving successful examples in **persistent storage** and retrieving them into the prompt improves performance; scale suggests relevance-based retrieval. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`11114b4ac438084dfb750eca` query=`experience replay buffer…`] Quote: “successful examples are saved in persistent storage, then retrieved…”
- `CLAIM` [E2] **Reflexion:** after failure, agent writes a short reflection; reflections live in a **memory buffer** with actions/observations; next attempt prepends recent reflections — no weight update; trials logged to persistent storage. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`11114b4ac438084dfb750eca` query=`experience replay buffer…`]
- `CLAIM` [E2] Plan→Act→Reflect→Revise: if performance is good, **store reflection in long-term memory**; retrieval injects prior lessons into new plans; selective forgetting / compression of many logs into meta-reflections. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG… (Mira S. Devlin)` chunk_id=`32f5bb52d47fcd5a316fc2db` / `8c261f41dbebd340dd43faa4` query=`experience replay buffer…`]
- `CLAIM` [E2] RAG can store past experience for later retrieval; fine-tuning internalizes experiences at higher cost; sophisticated RAG may mimic STM/LTM consolidation. [E2: Alexandria corpus=`ai_llm_agents` source=`Building AI Agents with LLMs, RAG, and Knowledge Graphs… (Raieli, Iuculano)` chunk_id=`efd4b7c5d3d214bd9192aa62` query=`experience replay buffer…`]
- `GAP` Searched: “experience replay for LLM agents.” Result: corpus emphasizes **exemplar banks**, **Reflexion buffers**, and **RAG experience stores** — not classic RL experience-replay buffers as a first-class named pattern in top hits. Do not invent ER-specific APIs.
- `INFERENCE` [E4] Exemplar/reflection stores are useful **candidate feedstock** patterns (structured logs + distilled lessons) but, without an explicit human gate, auto-injecting them into prompts is **runtime adaptation**, not safe promotion into workspace SoT. Premises: Reflexion/exemplar CLAIMs; HITL override CLAIM (§4.2).

### 4.5 Continuous learning scopes: session ICL vs durable policy

- `CLAIM` [E2] Continuous learning blends automated adaptation with **carefully managed oversight** to prevent unintended consequences (e.g. overfitting, regressions); mechanisms include in-context learning and online learning. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`e8433f87e9ba9d6515c2a56d` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] In-context learning adapts within a session (examples/feedback in prompt) without broader retraining — immediate but typically **session-scoped**. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`e8433f87e9ba9d6515c2a56d` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] Principle: equip agents with mechanisms to learn from experience (e.g. in-context learning) and **integrate user feedback**; ignoring feedback loops repeats mistakes. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`ccb9b700ad0104b92e689238` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] RAG feedback loops: collect → analyze → retrain/fine-tune; **manual** retraining (curate + periodic deploy) is more controlled but slower; **automated** retraining can deploy without human intervention — trade-off called out explicitly. [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering Retrieval-Augmented Generation…` chunk_id=`2aa5c2f7528250af0da038eb` query=`human-in-the-loop review promote…`]
- `INFERENCE` [E4] For host/workspace durable knowledge, the **manual / curated** side of the manual-vs-automated trade-off aligns better with proposed-only promotion than automated writeback. Premises: Mastering RAG CLAIM; Theme 24 never-auto-promote fence. Not a stack lock.

### 4.6 Continual learning as open problem (caution)

- `CLAIM` [E2] Continual learning (adapt to new tasks/environments without forgetting) and catastrophic forgetting remain **open problems** in deep learning — parametric continual learning is not a free lunch. [E2: Alexandria corpus=`ai_llm_agents` source=`Building AI Agents with LLMs… (Raieli, Iuculano)` chunk_id=`84dfefaf217c5caf8b629095` query=`…WITHOUT silent auto-promotion`]
- `CLAIM` [E2] Learning capability is useful but **optional** and costs design/eval/monitoring; nonparametric vs parametric learning are distinct paths. [E2: Alexandria corpus=`ai_llm_agents` source=`Albada` chunk_id=`6ff1698c9723c51cd9c44906` query=`…WITHOUT silent auto-promotion`]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Literature favors staged improve loops (propose → validate → embed) over silent SoT write | supported (comparator only) | Albada §4.1–4.2 chunks |
| H2 | Reflexion/exemplar stores are harvest **inputs**, not automatic host-law writers | supported (E4) | §4.4 + HITL override |
| H3 | Named “workspace memory → AGENTS/skills promote” pattern exists in Alexandria | rejected / GAP | no chunk; see §7 |
| H4 | Classic experience replay is a primary LLM-agent harvest pattern in this corpus | rejected / GAP | §4.4 GAP |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Auto vs manual embed of learnings | Albada: automate pipelines that **propose** refinements; humans override [E2:`980437391eeefeb6d64d7a78`] | Mastering RAG: automated retraining may deploy **without** human intervention [E2:`2aa5c2f7528250af0da038eb`] | Both valid product choices. For Theme 24 hard fence, prefer Albada-style propose+HITL / manual curation path; do **not** treat automated deploy as Toolbelt law. Conflict status: open for product choice, resolved for this theme’s fence. |
| Runtime memory write vs organizational docs | Reflexion/Devlin auto-store reflections to LTM [E2:`11114b4ac438084dfb750eca`, `32f5bb52d47fcd5a316fc2db`] | Albada: documentation + human oversight for strategic alignment [E2:`bbe9e02c915899e1f6c3f4cb`] | Different layers: runtime LTM ≠ workspace SoT. Theme 24 targets documented host surfaces with human accept. |

## 7. Gaps & OPEN

- `GAP` No Alexandria hit naming **Cursor workspace** promotion (skills / standards modules / `AGENTS.md`) with an explicit refuse-auto-accept contract.
- `GAP` “Experience replay” as RL buffer not substantively retrieved; use exemplar/Reflexion language instead unless web/gh finds primary papers.
- `OPEN` Map Albada feedback-pipeline stages onto Theme 24 candidate atoms (T24B) and elevate smoke (T24E) — integrator / later waves.
- `OPEN` Corroborate HITL-gate pattern via T24G-web / T24G-gh (primary/community) before any method lock; keep E3 community (if found) as discovery only.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Comparator pattern set for **no silent auto-promotion:** (1) log failures/successes; (2) distill candidates (RCA / reflection / exemplars); (3) HITL review + optional experiment; (4) embed into durable stores / docs only after approval; (5) keep session ICL separate from SoT. Premises: §4.1–4.5. **Proposed-only** for host/workspace author-learning — not Toolbelt plugin rewrite.
- `INFERENCE` [E4] Prefer treating agent memory buffers as **staging** for harvest candidates, with a human promotion step into host feedstock. Premises: H2; campaign O1.
- Do **not** lock skill shape, storage format, or always-on hooks from this note.

## 9. Source list (deduped)

1. Alexandria `ai_llm_agents` — Albada, *Building Applications with AI Agents…* — chunks `ccb9b700ad0104b92e689238`, `11114b4ac438084dfb750eca`, `038c563d49a057f9bfb23691`, `6ff1698c9723c51cd9c44906`, `6d14bb768510009b99b076b7`, `fc2367198e347abd88cd93ca`, `980437391eeefeb6d64d7a78`, `98e29b82cc8c92a02ec884e6`, `bbe9e02c915899e1f6c3f4cb`, `e8433f87e9ba9d6515c2a56d`, `64d93a22dca17db98ae93ca9`, `b5e7417118a3c639fc0c1dcd`, `6de7f53f6f3ecf9193953ad9`
2. Alexandria `ai_llm_agents` — Broda & Broda, *Agentic Mesh…* — `3882173e32b14e57682ec8a2`, `a8535eb03e5bf44a0d6c386f`, `e36c1cc356f59c7969e4b017`
3. Alexandria `ai_llm_agents` — Dibia, *Designing Multi-Agent Systems…* — `3408937256594a6e23b4cf10`
4. Alexandria `ai_llm_agents` — Devlin, *Building LLM Agents with RAG…* — `18b11a9ede89eeb93e6ae08e`, `32f5bb52d47fcd5a316fc2db`, `8c261f41dbebd340dd43faa4`
5. Alexandria `ai_llm_agents` — Raieli & Iuculano, *Building AI Agents with LLMs…* — `efd4b7c5d3d214bd9192aa62`, `84dfefaf217c5caf8b629095`
6. Alexandria `ai_llm_agents` — Infante, *AI Agents and Applications…* — `e787ec9011337cc21b505474`
7. Alexandria `ai_llm_agents` — *Mastering Retrieval-Augmented Generation…* — `2aa5c2f7528250af0da038eb`
8. Alexandria `ai_llm_agents` — *Building Agentic AI Systems* — `e0ee3955f154c2bf000be867` (reflection importance; secondary support only)

## Self-check

- [x] Depth recorded (deep); stop_reason recorded
- [x] Method block present
- [x] Every FACT/CLAIM has corpus+chunk_id support
- [x] INFERENCEs list premises
- [x] No invented citations; E3 not used as design lock
- [x] Conflicts logged (auto vs manual; runtime LTM vs docs)
- [x] Draft/proposed ≠ design law; host/workspace fence stated
