---
title: "T5A Wave 2 — Alexandria corroboration (HITL, ADR, plan-before-code)"
status: draft
theme: theme-5-design
track: T5A
wave: 2
slice: T5A-W2-RAG
created: 2026-07-29
updated: 2026-07-29
authors: [t5a-w2-alexandria-gatherer]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/t5a-w1-s1-adr-madr.md
  - docs/research/notes/theme-5-design/t5a-w1-s2-agent-design-process.md
  - docs/research/notes/theme-5-design/t5a-coordinator-pin.md
  - docs/research/notes/theme-5-design/campaign-brief.md
---

# T5A-W2-RAG — Alexandria corroboration for T5A process spine

**Using `research-protocol`; depth: deep; wave: 2; slice: T5A-W2-RAG.**

**Status:** `draft`. Not Design SoT. Does **not** restate W1 E1 FACTS as new FACTS — only corroborates, softens, or marks GAP. Does **not** elevate Design skills. Does **not** cover T5C/T5B domain content.

## 1. Scope

- Question / goal: Do Alexandria corpora `ai_llm_agents` and `software_engineering` corroborate (or contradict) Wave-1 T5A claims about human+agent design process (HITL, options/critique, plan/approve before coding) and ADR decision-record practices?
- In scope: Exact assigned queries; probe verdicts; graded E2 hits with corpus + chunk_id + source; false-friend watch; presence of brief-named books (*Beyond Vibe Coding*, *AI-Assisted Programming*).
- Out of scope: Re-fetching Nygard/Fowler/MADR primaries (W1 S1); Superpowers/AgDR inventory (S3); Cursor Plan Mode (W3); Design skill drafting; T5B architecture styles; T5C UX.
- Comprehension / research goal type: other (secondary-corpus corroboration)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | GetMcpTools + `rag_probe` / `rag_query` / `list_documents` on MCP `user-alexandria-rag`; Read of W1 S1/S2 notes + coordinator pin + research-note template; research-protocol skill |
| Corpora / URLs searched | Alexandria `ai_llm_agents`; Alexandria `software_engineering` |
| Queries (exact) | (1) `human in the loop agent design decisions planning critique alternatives` · (2) `architecture decision records ADR tradeoffs options consequences` · (3) `AI assisted programming design before coding plan approve` |
| Follow-up retrievals (recorded; not substitutes for exact queries) | path-scoped `rag_query` on Taulli / Osmani prefixes; targeted ADR string; Albada HITL/autonomy; `list_documents` name filters (`vibe`, `AI`, `human`, `decision`, `Framework`) |
| What was *not* searched | Web primaries; community skill files; vendor Plan Mode docs; other Alexandria corpora; T5B/T5C shelves |
| Depth | deep |
| Waves / stop_reason | wave: **2** (slice T5A-W2-RAG). stop_reason: **assigned_queries_probed_and_queried** — both corpora partial coverage; diminishing returns on further ADR keyword chasing (false-friend dominant); residual Plan Mode / community skills remain W3/S3 |
| Provenance (optional PROV) | Entity←Alexandria chunks from listed sources; Activity=T5A-W2 RAG corroboration; Agent=user-alexandria-rag MCP |

### 2.1 Probe coverage (exact queries)

| Query | Corpus | coverage_verdict | Notes |
|-------|--------|------------------|-------|
| Q1 HITL/planning/critique | `ai_llm_agents` | partial | Multi-agent planning / HITL framework features dominate |
| Q1 | `software_engineering` | partial | Top source: *Beyond Vibe Coding* |
| Q2 ADR tradeoffs/options/consequences | `ai_llm_agents` | partial | High false-friend risk (architecture/token “consequences,” not ADR artifacts) |
| Q2 | `software_engineering` | partial | Clean Code / unit-testing / metrics books in top_sources — **false friends** for ADR template law |
| Q3 AI-assisted plan/approve | `ai_llm_agents` | partial | Mixed coding-agent + MAS design |
| Q3 | `software_engineering` | partial | Top sources: *Beyond Vibe Coding*, *AI-Assisted Programming* |

### 2.2 Catalog presence (target books)

- `FACT` [E0] `list_documents` on `software_engineering` with `name_substring=vibe` returns *Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani)* (`source_id=34e9b0c879911f25`, 280 chunks). [E0: Alexandria list_documents — 2026-07-29]
- `FACT` [E0] `list_documents` on `software_engineering` with `name_substring=AI` returns *AI-Assisted Programming Better Planning, Coding, Testing, and Deployment (Tom Taulli)* (`source_id=d26c6134e46d77d4`, 271 chunks) among others. [E0: same]
- `FACT` [E0] `list_documents` on `ai_llm_agents` with `name_substring=human` returned **0** documents (title filter only; HITL content still appears via rag_query). [E0: same]
- `FACT` [E0] No document title containing `decision` in `software_engineering`; Framework Design Guidelines **is** present (false-friend risk for “design” queries). [E0: same]

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Corpus corroboration against fixed W1 claims; not workspace recon |
| Scope boundary | Two named corpora + assigned queries; cite only retrieved chunk_ids |

## 4. Findings

Lane labels reuse W1 S2: **A** human design judgment · **B** agent orchestration checkpoints · **C** coding-agent decision capture. W1 S1 owns ADR template atoms.

### 4.1 Corroboration — plan / approve / HITL before (or around) coding (Lane A/B; Q1 + Q3)

- `CLAIM` [E2] Osmani contrasts prompt-first **vibe coding** with **plan-first** AI-assisted engineering: begin with a plan (constraints + acceptance criteria); only then use AI to accelerate parts of that plan; grounding in intent before “letting the AI loose.” [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani) (z-library.sk, 1lib.sk, z-lib.sk).epub` chunk_id=`054c45ce9edf298e82ce235a` query=`AI assisted programming design before coding plan approve`]
- `CLAIM` [E2] Osmani responsible-AI golden rule: **always keep a human in the loop** — developer reviews every line and makes decisions; do not deploy raw AI output without human validation; take responsibility (do not blame Copilot). [E2: same corpus/source chunk_id=`53ae7dce5d6cd1df27bf95bf` query=`human in the loop agent design decisions planning critique alternatives`]
- `CLAIM` [E2] Osmani on autonomous agents: after candidate solution, **human reviews** (PR/diff approve or follow-up); “trust but verify”; generator-vs-reviewer asymmetry (write task description → review code). [E2: same source chunk_id=`373acdb75e7f59fe7c94a532` and chunk_id=`294db020275ca82481359be4` query=`human in the loop…` / path-scoped follow-up]
- `CLAIM` [E2] Osmani describes **intelligent checkpointing**: agent may pause at decision points (e.g. Library A vs B) and ask the human rather than guess. [E2: same source chunk_id=`4239391e2ef0cb2cf4f7be08` query=`human in the loop…`]
- `CLAIM` [E2] Osmani: AI may generate **two or three different design prototypes** for human/UX feedback — alternatives surface, but as coding/product prototypes, not an ADR options matrix. [E2: same source chunk_id=`3ce0debd7259dbf533516c58` query=`human in the loop…`]
- `CLAIM` [E2] Taulli book scope and TOC place **Ideas, Planning, and Requirements** (Ch. 7: brainstorming, PRD/SRS, project planning, TDD) **before** Coding (Ch. 8); cover copy lists requirements, planning, design, coding, debugging, testing. [E2: Alexandria corpus=`software_engineering` source=`AI-Assisted Programming Better Planning, Coding, Testing, and Deployment (Tom Taulli) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`055e90365ff17306461fb880` and chunk_id=`04a6b168f192369b6d5c016f` query=`AI assisted programming design before coding plan approve`]
- `CLAIM` [E2] Taulli: after requirements, plan the project approach; “one of the smartest things you can do **before you start coding** is to map out your test cases” (TDD / measure-twice). [E2: same source chunk_id=`a80abbf7735ab3c97a23802a` and chunk_id=`c3f290b4846439a4f6997c6b` query=path-scoped follow-up on Taulli]
- `CLAIM` [E2] Taulli (via Slack “levels of code AI”): Levels 0–2 are **human-led** (no AI → completion → longer creation with human oversight); Level 3+ shifts toward supervised/AI-led automation. [E2: same source chunk_id=`84bc7e3aa0e476d4a70e91aa` query=`AI assisted programming design before coding plan approve`]
- `CLAIM` [E2] Albada: **autonomy slider** Manual / Ask (assisted) / Agent — Ask mode drafts then human **reviews and approves** before apply/send; partial automation may require explicit approval before execution. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents Designing and Implementing Multiagent Systems (Michael Albada) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`b4fd598258782745232c8392` and chunk_id=`4d4c5e716ada93d0a6962c60` query=path-scoped HITL follow-up]
- `CLAIM` [E2] Albada: HITL review as structured escalation when automation is insufficient (ambiguity, ethics, high impact); human evaluates candidates → approved outputs. [E2: same source chunk_id=`98e29b82cc8c92a02ec884e6`]
- `CLAIM` [E2] Context-engineering text: think about AI systems **before writing code**; “The most advanced AI copilots can now boost code generation, but they cannot design a system without a human thinking about the design. We humans remain the architects.” [E2: Alexandria corpus=`ai_llm_agents` source=`Context Engineering for Multi_Agent Systems Move beyond prompting to build a Context Engine.pdf` chunk_id=`0c6aadea2cc86e199d2c721b` query=`AI assisted programming design before coding plan approve`]
- `CLAIM` [E2] Osmani on Cline (VS Code agent): shows each planned action and gives opportunity to **approve or modify each step** — human-in-the-loop between automation and control. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`b8b7294e50700b5ab9f9216e` query=`AI assisted programming design before coding plan approve`]
- `INFERENCE` [E4] W1 S2’s design-before-implement / human-owned decision / HITL course-correct spine is **directionally corroborated** by Osmani plan-first + HITL rules and Taulli planning-before-coding chapter order, plus Albada approve gates — but as **AI-coding / agent-UX practice**, not as Salesforce-style criteria→options-matrix→critique→ADR drafting. Premises: CLAIMs above; W1 S2 Norris/Nava E1 remain primary for that loop.
- `GAP` Exact W1 S2 Norris loop atoms (assessment criteria first; “do not decide”; tradeoff matrix; human final decision; AI drafts ADR) were **not** retrieved as named process from these corpora under assigned queries. Searched: Q1/Q3 on both corpora + path-scoped Osmani/Taulli/Albada. Result: plan/HITL/approve present; criteria-matrix-critique-ADR sequence absent.

### 4.2 Corroboration — critique / alternatives / multi-plan (Lane B; watch false friends)

- `CLAIM` [E2] Bhavsar (*Mastering AI Agents*): planning patterns include **task decomposition**, **multi-plan selection**, and **reflection/refinement**; human-in-the-loop called out for finetuning data / feedback; framework comparison notes LangGraph interruption, Autogen HITL modes, CrewAI `human_input`. [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering AI Agents A comprehensive guide for evaluating AI agents (Pratik Bhavsar) (z-library.sk, 1lib.sk, z-lib.sk).pdf` chunk_id=`43c95091f33f7278c1569ab2` and chunk_id=`63820fda248f381371228d79` query=`human in the loop agent design decisions planning critique alternatives`]
- `CLAIM` [E2] Devlin: Plan → Act → Reflect → Revise cognitive loop; Planner–Executor–Evaluator with evaluator **approve** verdict before returning result; Critic agent role in multi-agent setups. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG, Knowledge Graphs, and Reflection… (Mira S. Devlin)…pdf` chunk_id=`c4781fa5d76c93edf8e8553f` and chunk_id=`a9cde1fcdd51b40d5b193d55` query=`human in the loop…`]
- `CLAIM` [E2] Broda (*Agentic Mesh*): plan–act–evaluate–replan; plans with attached reasoning for human supervisor auditability; trade-offs in multiagent planning. [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh The GenAI-Powered Autonomous Agent Ecosystem (Eric Broda, Davis Broda)…pdf` chunk_id=`8aff89966056099505e0afd1` and chunk_id=`dfc64e502c87f39a67df6aa5` query=`human in the loop…`]
- `CLAIM` [E2] Raieli/Iuculano: Virtual Lab example keeps a **human in the loop** (PI) with optional critic agent — scientific multi-agent collaboration, not software ADR process. [E2: Alexandria corpus=`ai_llm_agents` source=`Building AI Agents with LLMs, RAG, and Knowledge Graphs by Salvatore Raieli, Gabriele Iuculano.pdf` chunk_id=`d65164e090a7e884342a9299` query=`human in the loop…`]
- `INFERENCE` [E4] These hits corroborate **Lane B** (orchestrated plan/critique/approve inside agent systems), not W1 Lane A’s human architectural decision method. Premises: CLAIMs in this subsection; W1 S2 lane separation; campaign brief false-friend warning on “agent design.”
- `GAP` Peer-reviewed / book-length treatment of **product/feature design critique workshops** (non-MAS) not found under Q1 in these corpora. Result: MAS critique roles only.

### 4.3 ADR / options / consequences (Lane C + W1 S1; Q2)

- `CLAIM` [E2] *Software Architecture Metrics* attributes the ADR term to **Michael Nygard** and describes weekly team discussion of upcoming spikes and ADRs alongside delivery metrics. [E2: Alexandria corpus=`software_engineering` source=`Software Architecture Metrics Case Studies to Improve the Quality of Your Architecture (Christian Ciceri, Dave Farley, Neal Ford etc.)…pdf` chunk_id=`a1b4ee7541275ccbc6a60390` query=`architecture decision records ADR tradeoffs options consequences`]
- `CLAIM` [E2] Same book: a team “captured an architecture decision record (ADR)” for a fail-fast jobs decision and later verified behavior “as described in the ADR.” [E2: same source chunk_id=`403e33e231c9d33f127e1939` query=`architecture decision records ADR tradeoffs options consequences` / targeted follow-up]
- `CLAIM` [E2] Index entry lists ADRs (architectural decision records) — presence confirmation only. [E2: same source chunk_id=`ad666e87782b1b97014d779c`]
- `GAP` Alexandria hits do **not** retrieve Nygard five-part sections, Fowler alternatives/pros-cons guidance, or MADR Considered Options / Decision Outcome / Consequences templates. Searched: exact Q2 on both corpora; targeted “ADR Nygard context decision consequences” on `software_engineering`. Result: mention/use of ADRs only; **no template law corroboration**. W1 S1 E1 primaries remain authoritative for section atoms.
- `GAP` Q2 on `ai_llm_agents` returned low-score false friends (hallucination “consequences,” deployment decision matrices, token-usage “architectural choice” economics) — **not** ADR artifacts. Do not cite as ADR corroboration. [probe partial; rag_query scores mostly ≪0.05 after rerank]
- `GAP` Q2 probe top_sources on `software_engineering` included Clean Code, Unit Testing, Clean Architecture, GoF — **false friends** for T5A ADR process. Framework Design Guidelines present in catalog (E0) but not used as process evidence here.
- `INFERENCE` [E4] No Alexandria contradiction of W1 S1 ADR section/status FACTS was found; absence is coverage GAP, not conflict. Premises: GAP bullets; W1 S1 E1 remains primary.

### 4.4 Anti-pattern / vibe coding (cross-check W1 S2)

- `CLAIM` [E2] Osmani treats vibe coding vs AI-assisted engineering as a spectrum; for complex algorithms, mission-critical systems, legacy integration, and performance work, **AI-assisted engineering should take precedence** (AI as assistant; human retains architecture control). [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding…` chunk_id=`9345993f3e432f7f2adc5e36` query=`AI assisted programming design before coding plan approve`]
- `INFERENCE` [E4] Aligns with W1 S2 use of Fowler vibe-coding risk as negative control for durable systems — Osmani adds operational “when to prefer plan-first.” Premises: this CLAIM; W1 S2 Fowler E1 (not re-fetched here).

### 4.5 Explicit non-corroborations / non-elevations

- Do **not** treat MAS Plan–Act–Reflect books as locks for Toolbelt Design skills.
- Do **not** treat Clean Architecture / Clean Code / Framework Design Guidelines retrievals as ADR or HITL process evidence.
- Do **not** invent Cursor Plan Mode contracts from Osmani/Cline product mentions (W3 OPEN remains).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 (from S2) | Human-owned criteria + options + critique + decide is dominant AI-arch design pattern | **revised** | W1 Salesforce E1 still primary; Alexandria corroborates plan-first/HITL/approve strongly, **not** the criteria-matrix-ADR chaining |
| H2 (from S2) | Agent orchestration should expose checkpoints / decision surfaces | **strengthened (E2)** | Albada autonomy slider + HITL review; Devlin approve loop; Bhavsar framework HITL; Osmani checkpointing |
| H3 (from S2) | In-repo decision records help coding agents | **weak RAG** | ADR *mentioned* in Architecture Metrics; no Glukhov-like agent-memory ADR chapter retrieved |
| H4 | Brief-named books appear and are usable for T5A W2 | **confirmed** | Osmani + Taulli present and on-query for Q1/Q3 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| What “critique” means | W1 S2: human amends AI options analysis (design decision) | Alexandria MAS: Critic/Evaluator agents in runtime loops | **No hard conflict** — different lanes (A vs B); keep separated |
| ADR richness | W1 S1 E1: full section/status law | Alexandria E2: ADR name + usage anecdote only | Prefer W1 E1 for template; Alexandria = weak existence corroboration |
| HITL sufficiency | Osmani E2: always HITL for responsible vibe coding | Albada E2: autonomy slider allows full Agent mode for routine tasks | Compatible: escalate HITL by stakes; leave Toolbelt policy **OPEN** |

## 7. Gaps & OPEN

- `GAP` No Alexandria retrieval of MADR/Nygard/Fowler **template atoms** (options, pros/cons, consequences sections, status lifecycle).
- `GAP` No Alexandria retrieval of Salesforce-style criteria-before-options architectural decision chaining.
- `GAP` No dedicated “agent HITL for product design decisions” book chapter that maps propose/critique/decide ownership for Toolbelt Design pack (MAS HITL ≠ design-method HITL).
- `GAP` Glukhov-style “AI drafts ADR but must not own” not found in these corpora under assigned queries.
- `OPEN` Whether Osmani plan-first + Taulli Ch.7 + Albada Ask/approve is enough E2 for a candidate “minimum design gate” — integrator/human accept only; draft ≠ SoT.
- `OPEN` Cursor / IDE Plan Mode official behavior — Wave 3 (unchanged).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] For T5A synthesis: treat Alexandria W2 as **strong secondary support for plan-before-code + human approve/HITL**, **weak support for ADR artifact practice**, and **non-support for ADR template law** (remain on W1 E1). Premises: §§4.1–4.3.
- `INFERENCE` [E4] When citing `ai_llm_agents`, default to Lane B labeling unless the chunk explicitly addresses human product/architecture decision ownership. Premises: false-friend pattern in Q1/Q2.
- `INFERENCE` [E4] This note does not authorize Design skills or close T5A — draft gatherer output only (`draft-is-not-sot`).

## 9. Source list (deduped)

1. Addy Osmani — Beyond Vibe Coding From Coder to AI-Era Developer — Alexandria `software_engineering` — chunks incl. `054c45ce9edf298e82ce235a`, `53ae7dce5d6cd1df27bf95bf`, `373acdb75e7f59fe7c94a532`, `294db020275ca82481359be4`, `4239391e2ef0cb2cf4f7be08`, `3ce0debd7259dbf533516c58`, `9345993f3e432f7f2adc5e36`, `b8b7294e50700b5ab9f9216e` — retrieved 2026-07-29
2. Tom Taulli — AI-Assisted Programming Better Planning, Coding, Testing, and Deployment — Alexandria `software_engineering` — chunks incl. `055e90365ff17306461fb880`, `04a6b168f192369b6d5c016f`, `a80abbf7735ab3c97a23802a`, `c3f290b4846439a4f6997c6b`, `84bc7e3aa0e476d4a70e91aa` — retrieved 2026-07-29
3. Michael Albada — Building Applications with AI Agents… — Alexandria `ai_llm_agents` — chunks `b4fd598258782745232c8392`, `4d4c5e716ada93d0a6962c60`, `98e29b82cc8c92a02ec884e6` — retrieved 2026-07-29
4. Pratik Bhavsar — Mastering AI Agents… — Alexandria `ai_llm_agents` — chunks `43c95091f33f7278c1569ab2`, `63820fda248f381371228d79` — retrieved 2026-07-29
5. Mira S. Devlin — Building LLM Agents with RAG, Knowledge Graphs, and Reflection… — Alexandria `ai_llm_agents` — chunks `c4781fa5d76c93edf8e8553f`, `a9cde1fcdd51b40d5b193d55` — retrieved 2026-07-29
6. Eric Broda, Davis Broda — Agentic Mesh… — Alexandria `ai_llm_agents` — chunks `8aff89966056099505e0afd1`, `dfc64e502c87f39a67df6aa5` — retrieved 2026-07-29
7. Salvatore Raieli, Gabriele Iuculano — Building AI Agents with LLMs, RAG, and Knowledge Graphs — Alexandria `ai_llm_agents` — chunk `d65164e090a7e884342a9299` — retrieved 2026-07-29
8. Context Engineering for Multi_Agent Systems… — Alexandria `ai_llm_agents` — chunk `0c6aadea2cc86e199d2c721b` — retrieved 2026-07-29
9. Ciceri / Farley / Ford et al. — Software Architecture Metrics… — Alexandria `software_engineering` — chunks `a1b4ee7541275ccbc6a60390`, `403e33e231c9d33f127e1939`, `ad666e87782b1b97014d779c` — retrieved 2026-07-29
10. Prior gatherers (not re-stated as new FACTS): `t5a-w1-s1-adr-madr.md`, `t5a-w1-s2-agent-design-process.md`, `t5a-coordinator-pin.md`

---

## Parent return summary

**Corroborated (E2):** Plan-first / planning-before-coding (Osmani, Taulli); human-in-the-loop review/approve and responsibility (Osmani, Albada, Cline approve-steps); agent checkpoint / multi-plan / critic loops as **Lane B** (Bhavsar, Devlin, Broda); ADR *term/usage* mention (Architecture Metrics + Nygard attribution).

**Contradicted:** None material vs W1 S1/S2. No source denied plan-before-code or human decision ownership.

**GAP:** ADR/MADR **template** atoms (options/tradeoffs/consequences/status law); Norris-style criteria→matrix→critique→ADR chain; agent-owned-vs-human ADR ethics (Glukhov); product-design critique literature beyond MAS false friends. Cursor Plan Mode still OPEN (W3).
