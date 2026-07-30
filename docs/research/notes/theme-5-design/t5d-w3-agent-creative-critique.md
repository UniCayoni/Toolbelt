---
title: "T5D Wave 3 — Agent creative critique / HITL residual (+1)"
status: draft
theme: theme-5-design
track: T5D
wave: 3
slice: T5D-W3
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5d-w3-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5d-coordinator-pin.md
  - docs/research/notes/theme-5-design/t5d-w2-corroboration.md
  - docs/research/notes/theme-5-design/t5a-track-synthesis.md
  - docs/research/notes/theme-5-design/t5a-w1-s2-agent-design-process.md
  - docs/PROTOCOL.md
---

# T5D-W3 — Agent creative critique / HITL residual (+1)

**Using `research-protocol`; depth: deep; wave: 3; slice: T5D-W3; +1 after low_return.**

**Status:** `draft`. Not Design SoT. Residual **P0** only (named in T5D-W2 coordinator signal). Does **not** invent a creative AgDR / creative decision-record standard. Does **not** elevate Design skills. Creative process remains **plural**. **TTRPG/GM ≠ video-game systems law.**

## 1. Scope

- Question / goal: How should **humans + agents** critique creative design (systems / narrative / world / character) — **options**, **consistency checks**, and **HITL gates** — without locking a single craft school or inventing a creative AgDR?
- In scope: Transferable HITL / producer–critic patterns; human creative critique baselines (iteration, lenses, bible/consistency, GUR as evaluation arm); light web + Alexandria `ai_llm_agents` / `game_design`; E3 community skill/workflow inventory only; reuse T5A HITL/critique vocabulary as **labels**.
- Out of scope: Re-deriving MDA/narrative topologies/world-bible law (W1–W2); studio GDD pipelines; inventing machine-readable beat↔state schemas; elevating Superpowers/AgDR; T5C UX; GreyMatter stack locks; further residual stages after this +1.
- Comprehension / research goal type: other (residual process GAP close)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria MCP `list_corpora`, `rag_query`; WebSearch; WebFetch; `gh api` (repo metadata); Read of `t5d-w2-corroboration.md`, `t5a-track-synthesis.md`, `t5a-w1-s2-agent-design-process.md`, campaign brief T5D W3 row, research-note template; research-protocol skill |
| Corpora / URLs searched | Alexandria `ai_llm_agents`, `game_design`; https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems ; https://arxiv.org/html/2605.29625v1 ; GitHub community creative-agent repos (see §4.4); discovery hits for mixed-initiative / writer–editor |
| Queries (exact) | Alexandria: `human in the loop critique review approve agent design process options alternatives creative critique`; `producer critic reviewer agent pair feedback critique refine creative writing narrative generation quality`; `design critique playtest iteration consistency check narrative worldbuilding character review feedback loop designer critique`; `lenses critique design questions consistency theme elemental tetrad feedback playtest`. Web: `AI agent creative writing critique human-in-the-loop game narrative design review`; `LLM agent writer editor critic loop narrative consistency check worldbuilding`; `Cursor skill creative critique game design agent HITL github` |
| What was *not* searched | Full Schell lens catalog extraction; studio creative-pipeline ethnographies; Articy/Yarn deep; Gygax method mine; Adams *Fundamentals* body; biometric GUR deep; inventing Toolbelt creative-ADR schema; exhaustive skills.sh catalog; live Cursor IDE E0 experiments |
| Depth | deep |
| Waves / stop_reason | wave: **3** (slice T5D-W3). stop_reason: **low_return_plus_one** — named P0 residual addressed with transferable HITL + creative critique patterns + E3 inventory; further same-shelf RAG / more community repos would restate producer–critic + consistency-gate shapes. **Recommend track synthesis.** No further +1. |
| Provenance (optional PROV) | Entity←ai_llm_agents + game_design books + HAI essay + arXiv HTML + GitHub READMEs; Activity=T5D-W3 residual; Agent=gatherer-t5d-w3-grok + Alexandria/Web/`gh` |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Residual close against fixed W2 P0; not workspace recon |
| Scope boundary | Critique/HITL/consistency only; cite retrieved locators; prefer GAP over invented creative AgDR |

## 4. Findings

Lane labels: **A** human creative critique baselines · **B** transferable agent HITL / producer–critic · **C** creative-domain agent patterns (narrative/world) · **D** E3 community inventory · **E** bind to T5A vocabulary (labels only).

### 4.1 Lane A — Human creative critique baselines (systems / story / world / character)

These are **critique surfaces** agents may assist; humans still own taste, theme, and accept/reject.

**Systems / iteration (critique → revise)**

- `FACT` [E2] Sharp & Macklin: iterative game design = **conceptualize → prototype → playtest → evaluate**; evaluate includes review strengths/weaknesses against design values, incubate, brainstorm options, **decide**, document, schedule next prototype. [E2: Alexandria corpus=`game_design` source=`Games, Design and Play…Sharp…Macklin…` chunk_ids=`8b41b883183ab2603fad7955`, `3864932d5f58d8c9776eeabc`, `5f0c980ebcff11191eb3df46` query=`design critique playtest…`]
- `FACT` [E2] Sharp & Macklin distinguish **input** (player suggestions that may rewrite intent) vs **feedback** (problems noted; creator decides whether/how to act) — peer workshops / table reads / critiques as analogues across creative media. [E2: same source chunk_ids=`363be94ef6e1d6c913ba2eaa`, `e786a0fdc22c56a9213d9858`]
- `FACT` [E2] Schell: playtests answer specific **why** questions (not bare “is it fun?”); lenses are a source of good playtest questions; elemental tetrad lens asks whether mechanics/story/aesthetics/technology are used, improvable, and **in harmony toward a theme**. [E2: Alexandria corpus=`game_design` source=`Schell…Art of Game Design…` chunk_ids=`5b4e3b5072a4bcfa9c74fcdf`, `7918cc5e718c4682220e9375`, `8b8e78a08f3e72c429d3385a` query=`lenses critique…`]
- `INFERENCE` [E4] For systems critique with agents: treat Schell/Sharp loops as **human-owned evaluate/decide**; agents may draft option lists and lens-checklists. Premises: above FACTs; T5A “human decides” spine (labels only).

**Narrative ↔ fiction consistency (W2 bind, reused)**

- `FACT` [E2] Zubek: when fiction is present, **gameplay and fiction must match**; violations include fantasy-contradicting action limits and ludonarrative dissonance (Hocking). [E2: pinned from W2; Alexandria corpus=`game_design` Zubek chunk_ids=`65b960bf5a4566c70d4fb97f`, `7b18eb988e69f2c900e1e354`, `bbc9d97b9a00874b18fd9900` — W2 §4.1]
- `INFERENCE` [E4] Narrative critique checklist for agents (draft, not lock): causality / meaningful choice / beat↔state wiring / fiction–gameplay match — human owns “is this choice meaningful?” Premises: W1 S2 Lane D INFERENCE; Zubek FACT; T5A critique step.

**World / character consistency**

- `FACT` [E2] Collas: lore coherence needs documentation + coherence + **human intelligence**; bible for other developers’ constraints; role-targeted notes. [E2: W2 §4.2 — Alexandria chunk_id=`0bf880a9bf44084feadc87bb`]
- `FACT` [E2] Hungerford/Baur (Kobold): living dated world bible; focus / anti kitchen-sink. [E2: W2 §4.2]
- `INFERENCE` [E4] World/character **consistency checks** = diff draft vs bible/cast rules (agent-strong); **promotion of canon** and taste judgments = human gate. Premises: Collas/Hungerford FACTs; Stanford HAI agency principle (§4.2).

**Empirical evaluation arm (not agent-replaceable taste)**

- `FACT` [E2] GUR handbook supplies plural methods (observation, think-aloud, RITE, heuristics, surveys, etc.); QA ≠ GUR. [E2: W2 §4.3]
- `INFERENCE` [E4] Agent critique ≠ playtest substitute; agents may prepare protocols / summarize notes; humans/players supply behavioral/attitude evidence. Premises: GUR FACTs; Sharp input vs feedback.

### 4.2 Lane B — Transferable agent HITL / producer–critic (not creative-specific law)

Reuse T5A vocabulary: **propose → critique/amend → human decide → gate before durable commit**.

- `FACT` [E2] Gheorghiu (*LlamaIndex* workflows): HITL as intentional step boundary — **approval gates** before side effects (payload easy to evaluate: tool, args, rationale, impact); **review gates** for high-stakes content (compact draft + supporting context + claims to verify); **clarification gates** when underspecified; separate producer vs reviewer roles improve consistency even if both are LLMs. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex…Gheorghiu…` chunk_ids=`eb26af7b81ef9539f023e63c`, `5b3dad545d2a2b403672a7a2` query=`human in the loop critique…`]
- `FACT` [E2] Albada: HITL review workflow = agent generates output candidates → human evaluator feedback/approve → human-approved outputs; needed for ambiguous intent, ethics, conflicting goals, novel edges. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents…Albada…` chunk_ids=`98e29b82cc8c92a02ec884e6`, `1e9af7e8523d281b08fce63e`]
- `FACT` [E2] Dibia: tool **approval_mode** stops execution for human approve/reject/resume; agents may request clarification; human input treated like tool results in context. [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems…Dibia…` chunk_ids=`8d4a9f67867e78f2348daa7d`, `366f0de1a9d1e2d9ab43a749`]
- `FACT` [E2] Raieli & Iuculano (Virtual Lab summary): human sets agenda; **critic agent** provides critiques; individual meetings may loop agent↔critic; PI/human retains decision weight; human-in-the-loop collaboration framing. [E2: Alexandria corpus=`ai_llm_agents` source=`Building AI Agents with LLMs…Raieli…` chunk_ids=`998eb925da420d18d202cc01`, `d65164e090a7e884342a9299`]
- `FACT` [E2] Devlin (secondary guide): multi-agent division of labor includes **critic** evaluating quality/coherence; peer review among agents (generate → critique → revise) framed as hallucination mitigation pattern. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG…Devlin…` chunk_ids=`50f741919e432e2ab05fed10`, `e552f5faad69b7c15171f4a4`]
- `FACT` [E1] Ge Wang (Stanford HAI): HITL reframes automation as HCI — incorporate useful human interaction; principles include **value human agency** (preference, taste, judgment), **granularity** (break tasks vs Big Red Button), **tools not oracles**; creative meaning ≠ style transfer. [E1: https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems — accessed 2026-07-29]
- `INFERENCE` [E4] For Toolbelt creative work: map gates as (1) **clarification** when brief/theme underspecified; (2) **review** of high-stakes creative claims (tone, theme, IP, player-harm); (3) **approval** before promoting draft→canon / shipping narrative assets. Premises: Gheorghiu FACTs; Wang E1; T5A Lane A/B separation.
- `OPEN` Design-time HITL encoding vs per-decision gates — remains **OPEN** per T5A W3; do not re-litigate here. Creative track inherits coexistence framing.

### 4.3 Lane C — Creative-domain agent patterns (narrative / world / co-creation)

- `FACT` [E1] Valdivia & Burelli (arXiv HTML): iterative **Writer–Editor** multi-agent process — one LLM generates story, another evaluates/scores and provides feedback for refinement; simulation study reports perceived quality improves across loops; focus dimension **Relevance** / faithfulness to player-selected constraints (anti faithfulness-hallucination). Child board-game co-creation setting (YOLI) — not studio VG pipeline law. [E1: https://arxiv.org/html/2605.29625v1 — accessed 2026-07-29]
- `CLAIM` [E2] *Building Agentic AI Systems* (secondary): writing/narrative agents framed as maintaining character consistency, plot coherence, narrative flow while preserving author voice; artistic agents as iterative collaborators with feedback — discovery-grade for creative roles, not a Toolbelt schema. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems.pdf` chunk_id=`3fdff7bc6805a64efd2cb1cd` query=`producer critic…`]
- `CLAIM` [E2] Raieli & Iuculano: agents can propose/evaluate/refine/prioritize ideas and provide critique in brainstorming-style multi-agent setups (research framing). [E2: Alexandria corpus=`ai_llm_agents` same Raieli source chunk_id=`e0b3f81ecaba7065f4116aa2`]
- `CLAIM` [E1/E2 discovery] Mixed-initiative co-creative storytelling games (e.g. Snake Story / “Designing Mixed-Initiative Video Games”) study player–AI co-creation roles — relevant to **playtime** co-creation, not identical to designer-side critique gates. [E1/E2 discovery: https://doi.org/10.1145/3649921.3649996 ; https://doi.org/10.48550/arxiv.2307.03877 — accessed via WebSearch/WebFetch 2026-07-29; not promoted to studio method law]
- `GAP` No retrieved E1/E2 source defines a **shared industry “creative AgDR”** (agent decision record for narrative/world/character/systems locks). Searched: web creative-agent + Alexandria critic/HITL. Result: Writer–Editor / critic / consistency-checker **patterns** exist; no canonical creative ADR/AgDR standard. Prefer **GAP** over invention.
- `INFERENCE` [E4] Strongest transferable creative-agent pattern this residual: **separate generator from critic/editor**, score against explicit constraints (bible, cast rules, player tiles, theme), loop a few times, then **human gate** before canon. Premises: Valdivia E1; Gheorghiu review gates; Collas human intelligence; Wang agency.

### 4.4 Lane D — Community workflows / skills (E3 inventory only)

**Hard grade rule:** stars and community plugins = **discovery inventory**, not Design SoT. Same discipline as T5A Superpowers/AgDR and T5D-W2 GDD templates.

- `CLAIM` [E3] `IShalkin/manoe` — multi-agent fiction orchestration README claims Writer→Critic score threshold + revision; Archivist for key constraints/world state; Worldbuilder/Profiler roles; vector memory for consistency. [E3: https://github.com/IShalkin/manoe — stars=`0` via `gh api` 2026-07-29]
- `CLAIM` [E3] `aayushakumar/StorySmith` — Plotter / Stylist / Critic / Continuity Checker / Summarizer roles; continuity agent tracks characters/settings/timelines. [E3: https://github.com/aayushakumar/StorySmith — stars=`1` via `gh api` 2026-07-29]
- `CLAIM` [E3] `queelius/claude-anvil` **worldsmith** plugin — `/check consistency`, multi-agent review, draft/revise/iterate with end-of-loop user checkpoint claimed in README. [E3: https://github.com/queelius/claude-anvil — stars=`1` via `gh api` 2026-07-29; path `worldsmith`]
- `CLAIM` [E3] `DTSFO/novel-agent-workflow` — fixed roles (planner/writer/reviewer/plot keeper/entity keeper); review gate `REVISE` / pass; file-backed knowledge. [E3: https://github.com/DTSFO/novel-agent-workflow — stars=`0` via `gh api` 2026-07-29]
- `CLAIM` [E3] Community skill directories also surface UI-oriented `/critique` (e.g. impeccable) and browser-game UI `game-designer` skills — **false friends** for T5D creative systems/narrative/world critique (closer to T5C / frontend). [E3: WebSearch discovery 2026-07-29 — e.g. explainx.ai skill pages; not fetched as primary SKILL.md]
- `INFERENCE` [E4] E3 inventory **converges** on: role-split (writer/critic/continuity), constraint memory (bible/vault/RAG), score/threshold loops, optional HITL checkpoints — corroborates Lane C pattern shape without authorizing any repo as Toolbelt law. Premises: E3 CLAIMS; draft-is-not-sot; campaign weak-E3 caveat.
- `GAP` Corroborated E0/E1 evaluation that any of these community stacks produce better GreyMatter/Toolbelt creative outcomes. Searched: repo metadata + READMEs only.

### 4.5 Lane E — Bind to T5A vocabulary (labels only; no creative AgDR invent)

From T5A track synthesis (draft labels, not locks):

| T5A label | Creative (T5D) use this residual |
|-----------|-----------------------------------|
| Options | Enumerate structure family / loop variants / world tenets / character trait packs (plural) |
| Critique | Lens checklist + fiction–gameplay match + bible/cast continuity + (optional) Writer–Editor or critic agent pass |
| Decide | **Human** owns theme, canon promotion, which critique to accept (Sharp feedback ≠ input) |
| Record | Living bible / quest-state notes / design doc — **not** a newly invented creative AgDR |
| HITL gate | Clarification / review / approval before canon or ship (Gheorghiu shapes) |

- `INFERENCE` [E4] Do **not** mint “creative AgDR” as Toolbelt standard from E3 fiction workflows or AgDR lineage (me2resh) — keep AgDR as T5A E3 inventory only. Premises: GAP §4.3; T5A synthesis OPEN on AgDR; cite-or-omit.
- `INFERENCE` [E4] Candidate (draft) envelope for later integrator — **not a lock**: frame constraints → options (2–3) → agent-assisted critique/consistency → human decide → record in existing creative docs → HITL before implement/canon. Premises: T5A spine; Lanes A–C; W2 evaluation envelope.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Transferable HITL/producer–critic patterns exist in `ai_llm_agents` | confirmed | §4.2 |
| H2 | Writer–Editor / critic loops appear in creative narrative research | confirmed (narrow E1) | Valdivia §4.3 |
| H3 | Community fiction-agent stacks share consistency + critic gates | confirmed as E3 shape only | §4.4 |
| H4 | A creative AgDR / industry creative decision-record SoT can be locked from this +1 | rejected | GAP §4.3; prefer GAP |
| H5 | Agent critique replaces GUR/playtest | rejected | §4.1 GUR/Sharp |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Who owns critique outcomes | Sharp: creator may reject player **input**; keep **feedback** | E3 repos: autonomous iterate-to-threshold | Prefer human decide (Wang E1; T5A); agent loops = assist only |
| Agent–agent critique vs human gate | Devlin/Raieli peer critic loops | Gheorghiu/Albada human review gates | Compatible layers: agent critic **before** human review for high-stakes creative claims |
| Playtime co-creation vs design-time critique | Snake Story mixed-initiative | Designer bible/consistency + GUR | Keep lanes; do not equate player co-write with design SoT process |
| Creative AgDR vs ADR/AgDR | T5A AgDR E3 | Fiction workflow “review records” E3 | **No merge** — GAP for creative AgDR standard |

## 7. Gaps & OPEN

### Closed or softened this residual

- Softened: W2 P0 “agent creative critique / HITL patterns” — now has graded transferable patterns (HITL gate types; producer–critic; Writer–Editor E1; human creative baselines; E3 inventory).
- Softened: Cross-walk to T5A options/critique/decide/HITL **labels**.

### Still GAP / OPEN (prefer GAP)

- `GAP` **Creative AgDR / shared creative decision-record standard** — do not invent.
- `GAP` Studio-primary creative critique pipelines (BioWare/CDPR/etc.) as law.
- `GAP` Machine-required HITL field mapping for narrative/world assets.
- `GAP` E0 evaluation of community fiction-agent stacks in Toolbelt context.
- `OPEN` Whether later Design pack encodes a thin “creative critique” skill that **only** wraps T5A spine + consistency checklists + HITL gates (integrator/human accept) — not decided here.
- `OPEN` T5A HITL design-time vs per-decision (inherited).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T5D can **reuse T5A process labels** and add creative-specific **consistency surfaces** (bible/cast/fiction–gameplay/lens questions) without a new decision-record dialect. Premises: §4.5; GAP on creative AgDR.
- `INFERENCE` [E4] Default agent role split for creative assist: **generator ≠ critic/continuity**; human owns theme/canon. Premises: §§4.2–4.3; Wang E1.
- `INFERENCE` [E4] E3 fiction-agent repos are optional structure cousins (like Superpowers for T5A) — inventory, do not import git/runtime policies or star-chase locks. Premises: §4.4; campaign caveat.
- **Non-lock reminder:** This note is `draft`. Hard stop after this +1.

## 9. Source list (deduped)

1. Andrei Gheorghiu — *Building Data-Driven Applications with LlamaIndex…* — Alexandria `ai_llm_agents` chunks `eb26af7b81ef9539f023e63c`, `5b3dad545d2a2b403672a7a2` — **E2**
2. Michael Albada — *Building Applications with AI Agents…* — chunks `98e29b82cc8c92a02ec884e6`, `1e9af7e8523d281b08fce63e` — **E2**
3. Victor Dibia — *Designing Multi-Agent Systems…* — chunks `8d4a9f67867e78f2348daa7d`, `366f0de1a9d1e2d9ab43a749` — **E2**
4. Salvatore Raieli & Gabriele Iuculano — *Building AI Agents with LLMs…* — chunks `998eb925da420d18d202cc01`, `d65164e090a7e884342a9299`, `e0b3f81ecaba7065f4116aa2` — **E2**
5. Mira S. Devlin — *Building LLM Agents with RAG…* — chunks `50f741919e432e2ab05fed10`, `e552f5faad69b7c15171f4a4` — **E2**
6. *Building Agentic AI Systems* — chunk `3fdff7bc6805a64efd2cb1cd` — **E2** CLAIM
7. John Sharp & Colleen Macklin — *Games, Design and Play…* — chunks `8b41b883183ab2603fad7955`, `3864932d5f58d8c9776eeabc`, `5f0c980ebcff11191eb3df46`, `363be94ef6e1d6c913ba2eaa`, `e786a0fdc22c56a9213d9858` — **E2**
8. Jesse Schell — *The Art of Game Design* — chunks `5b4e3b5072a4bcfa9c74fcdf`, `7918cc5e718c4682220e9375`, `8b8e78a08f3e72c429d3385a` — **E2**
9. Ge Wang — Stanford HAI “Humans in the Loop…” — https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems — **E1**
10. Arturo Valdivia & Paolo Burelli — Writer–Editor storytelling — https://arxiv.org/html/2605.29625v1 — **E1**
11. Mixed-initiative discovery — https://doi.org/10.1145/3649921.3649996 ; https://doi.org/10.48550/arxiv.2307.03877 — **E1/E2 discovery**
12. E3 community — https://github.com/IShalkin/manoe ; https://github.com/aayushakumar/StorySmith ; https://github.com/queelius/claude-anvil ; https://github.com/DTSFO/novel-agent-workflow — **E3**
13. W2 priors (local pin): `t5d-w2-corroboration.md` (Zubek consistency; Collas/Hungerford; GUR) — **E0** context / prior grades retained
14. T5A vocabulary pins: `t5a-track-synthesis.md`, `t5a-w1-s2-agent-design-process.md` — **E0** process labels only
15. Campaign / coordinator — `campaign-brief.md`, `t5d-coordinator-pin.md` — **E0**

---

## Coordinator signal

| Field | Value |
|-------|-------|
| `stop_reason` | **low_return_plus_one** |
| `low_return_detected` | **yes** (pre-declared from W2; confirmed after this +1) |
| Rationale | Named P0 residual now has graded coverage: HITL gate types + producer–critic; human creative critique baselines; Writer–Editor E1; E3 fiction-agent inventory; explicit **GAP** (no creative AgDR invent). Further community repo mining or same-book RAG would restate the same shapes. |
| Residual after +1 | Confirmed GAP/OPEN only (creative AgDR standard; studio pipelines; machine HITL field maps; E0 stack eval) — **not** another gatherer wave |
| Recommendation | **Track synthesis** for T5D (merge pin + W1 S1–S3 + W2 + this W3); then campaign integrator as brief directs |

---

## Parent return summary

**FACTS:** HITL approval/review/clarification gates (Gheorghiu); candidate→human approve loops (Albada/Dibia); critic-agent / Virtual Lab patterns; Sharp/Schell human critique & playtest question craft; Wang HAI agency/granularity/tools-not-oracles; Valdivia Writer–Editor E1.

**CLAIMS (E3 only):** Community fiction multi-agent stacks (MANOE, StorySmith, worldsmith, novel-agent-workflow) share writer/critic/continuity shapes — inventory, not SoT.

**GAPs retained:** Creative AgDR standard (**prefer GAP — do not invent**); studio critique pipelines; machine HITL schemas.

**Signal:** `stop_reason=low_return_plus_one`; **recommend T5D track synthesis**. Hard stop.
