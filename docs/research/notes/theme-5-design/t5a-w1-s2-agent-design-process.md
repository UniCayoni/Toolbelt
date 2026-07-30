---
title: "T5A W1 S2 — Agent-assisted design process (HITL, options, critique, decide)"
status: draft
theme: theme-5-design
track: T5A
slice: T5A-S2
wave: 1
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5a-s2]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5a-coordinator-pin.md
  - docs/PROTOCOL.md
---

# T5A W1 S2 — Agent-assisted design process

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T5A-S2**.

**Status:** `draft`. Not Design SoT. ADR template details owned by S1; community skill inventories owned by S3.

## 1. Scope

- **Question / goal:** How should humans + AI/coding agents run a **design process** — options, constraints, tradeoffs, critique, decision, HITL gates — **before implementation**?
- **In scope:** Human-led AI-assisted design loops; alternatives matrices / options analysis; critique & refinement checkpoints; propose vs decide ownership; HITL / design-time gates; anti-patterns (vibes-only, premature stack/architecture lock); clear separation of (A) human design methods, (B) agent orchestration patterns, (C) coding-agent decision capture.
- **Out of scope:** ADR/MADR template law (S1); Superpowers / AgDR / community skill file inventories (S3); T5B architecture styles content; T5C UX; Design skill elevation; inventing Cursor Plan Mode behavior; full Alexandria Wave 2 corroboration.
- **Comprehension / research goal type:** other (process methodology research)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebSearch; WebFetch; local read of campaign brief + T5A pin + research-note template |
| Corpora / URLs searched | See §9 Source list; Method queries below |
| Queries (exact) | `Salesforce architectural decisions human-led AI-powered`; `Glukhov decision records AI-driven development`; `human in the loop AI software design process alternatives critique decision`; `AI assisted software architecture decision making process tradeoffs`; `"vibe coding" anti-pattern design before implementation AI agents` |
| What was *not* searched | Alexandria corpora (`ai_llm_agents`, `software_engineering`) — deferred to Wave 2; Superpowers `brainstorming` / `writing-plans` file inventory — S3; AgDR inventories — S3; official Cursor Plan Mode docs — W3 residual if still OPEN; NIST AI RMF deep dive; ATAM/SEI primary manuals; peer-reviewed GenAI-for-architecture MLR full texts (SSRN/ECSA abstracts noted as discovery only); Theme 2 ADR report re-litigation |
| Depth | deep |
| Waves / stop_reason | wave: **1** (primary / high-signal E1–E2). Stop for this slice: **wave1_primary_complete** — diminishing returns for further W1 vendor blog chase; residual vendor Plan Mode + Alexandria corroboration reserved for W2/W3 |
| Provenance (optional PROV) | Entity←vendor blogs + practitioner blogs + Fowler bliki; Activity=T5A-S2 W1 gather; Agent=WebSearch/WebFetch + human coordinator brief |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Process literature slice; no codebase recon required for W1 |
| Scope boundary | External primary/secondary web sources only; no plugin skill inventory |

## 4. Findings

Findings are **lane-separated**. Do not collapse A/B/C into one “agent design” mega-claim.

### 4.1 Lane A — Human design methods (judgment, criteria, decide)

- `FACT` [E1] Salesforce advocates a **human-led, AI-powered** architectural decision practice: humans supply project-specific context and stakeholder empathy for assessment criteria; AI accelerates research, comparison drafting, and ADR formatting. Architect remains accountable for every key decision. [E1: Dave Norris, “Architectural Decisions: A Human-Led, AI-Powered Approach” — https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/ — accessed 2026-07-29]
- `FACT` [E1] Norris’s documented loop (prompt chaining with architect checkpoints): (1) generate **assessment criteria** from context (no solution yet); (2) human refine criteria; (3) AI produce **options analysis / tradeoff matrix** vs criteria; (4) human critique & amend analysis; (5) human states **final decision**, AI drafts ADR. Explicit constraint in early prompts: *do not propose a solution / do not decide*. [E1: Norris Salesforce blog — same URL — accessed 2026-07-29]
- `FACT` [E1] Norris defines HITL for generative architectural decisions as giving the architect opportunity to **course-correct AI-generated content**; LLMs characterized as “pattern recognition – not comprehension,” lacking professional judgment, business context, and empathy required for sound decisions. [E1: Norris Salesforce blog — same URL — accessed 2026-07-29]
- `FACT` [E1] Related Salesforce guidance: use AI as a **thinking partner** in analysis (challenge framing, surface assumptions, pressure-test before commit), not only as an answer/implementation engine; five-step daily pattern: expand problem → challenge assumptions → explore multiple design options → analyze system impact → (document/decide — article continues). [E1: David Nava, “5 Steps to Develop an Architect Mindset With AI” — https://www.salesforce.com/blog/5-steps-architect-mindset-ai/ — accessed 2026-07-29]
- `CLAIM` [E2] Practitioner framing of “Decision-Oriented Development”: frame problem → identify existing decisions → explore options/tradeoffs → **record selected decision** → then generate/modify code → review code vs decisions. Positions generate-test-commit alone as too thin for serious systems. [E2: Rost Glukhov, “Decision Records for AI-Driven Software Development” — https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/ — accessed 2026-07-29]
- `FACT` [E1] Martin Fowler defines **vibe coding** as prompting an LLM to build/change software **without looking at generated code**; distinguishes it from **agentic programming** where humans still review structure. States vibe-coded software often has maintainability/correctness/security problems and is best for disposable/limited-audience use. [E1: Martin Fowler, “Vibe Coding” — https://martinfowler.com/bliki/VibeCoding.html — accessed 2026-07-29]
- `INFERENCE` [E4] For Toolbelt’s “design before implement” spine, vibes-only (forget the artifact / skip structured options) is an anti-pattern for durable systems; human-owned criteria → options → critique → decide maps to Norris/Nava, while Fowler’s vibe coding is the negative control case. Premises: (1) Norris E1 loop; (2) Nava E1 “thinking partner before solve”; (3) Fowler E1 vibe coding definition & risk scope.
- `GAP` Classical human design methods outside AI-assist (e.g. full ATAM stakeholder workshops, double-diamond UX process, TRIZ) were **not** primary-fetched this slice. Searched: AI-assisted architecture decision queries. Result: ATAM/RAG thesis and ECSA abstracts appear in search snippets only — insufficient for FACT locks here. Follow-up: W2/W3 if needed for non-AI human method baseline.

### 4.2 Lane B — Agent orchestration patterns (how multi-step AI systems run)

- `FACT` [E1] Norris distinguishes **manual chat HITL prompt chaining** from a future **agentic** workflow that is asynchronous/event-driven, using RAG for trusted criteria and MCP for live org metadata, with the architect **overseeing a multi-stage process** rather than constant back-and-forth prompting. Presented as aspirational/future Salesforce Agentforce direction, not a completed product prescription in the article. [E1: Norris Salesforce blog — same URL — accessed 2026-07-29]
- `CLAIM` [E2] “Decision surfaces” pattern: agent gathers evidence, weighs options against constraints, surfaces **structured multi-path recommendations with tradeoffs**; human picks; agent executes the pick. Contrasted with autonomous executor that collapses framing/evidence/tradeoffs/commit into opaque action. [E2: Kumar Thangamuthu, “AI Agent Architecture: Decision Surfaces, Not Autonomous Executors” — https://kumart.me/writing/ai-agents-decision-surfaces — accessed 2026-07-29]
- `CLAIM` [E2] Three production-oriented patterns claimed: (1) plan-then-execute with checkpoints; (2) structured workflows with selective LLM calls at decision points; (3) decision surfaces. Unifying principle: AI for synthesis/recall/comparison; humans for judgment/accountability. [E2: Thangamuthu — same URL — accessed 2026-07-29]
- `CLAIM` [E2/E3] Thangamuthu cites Devin 2.0 “Interactive Planning” (plan → human approve/adjust → execute) and lists “Cursor’s agent mode, Claude Code’s plan mode” as examples of plan-then-execute. **Cursor Plan Mode behavior is not verified in this slice** — treat product-behavior claims as unverified for Toolbelt locks. [E2/E3: Thangamuthu — same URL — accessed 2026-07-29]
- `OPEN` Official **Cursor Plan Mode** (and related IDE plan/agent modes) docs and E0 behavior — deferred to **Wave 3** residual per campaign brief. Do not invent Plan Mode contracts from secondary blog mentions.
- `GAP` Peer-reviewed / standards-grade agent orchestration (e.g. NIST AI RMF human oversight controls; LangGraph interrupt patterns as primary docs) not fetched. Searched: HITL design-process queries. Result: community blogs (Hetland “HITL at design time”, Surber “Human on the Design”, Substack “HITL is not a control strategy”) appear in discovery — **not promoted** to design locks this wave (E3 risk; corroborate in W2 or leave).
- `INFERENCE` [E4] Lane B is about **where checkpoints sit in an agent workflow** (propose/plan → human gate → execute), which is related to but not identical to Lane A’s **how a human forms a design decision**. Premises: (1) Norris E1 separates chat HITL vs agent oversight; (2) Thangamuthu E2 decision-surface vs autonomous executor.

### 4.3 Lane C — Coding-agent decision capture (memory for future agents)

- `CLAIM` [E2] Decision records (ADR / PDR / DDR) act as **durable project memory** for humans and AI coding agents: context, alternatives, decision, consequences; store as Markdown in-repo; review like code; instruct agents to **read before proposing/implementing**. [E2: Glukhov — https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/ — accessed 2026-07-29]
- `CLAIM` [E2] Glukhov: AI may draft records but **must not own** them — human verifies no invented rationale, real alternatives, honest consequences; optional “AI guidance” section turns records into durable agent instructions (preserve/avoid/prefer/ask-for-review). [E2: Glukhov — same URL — accessed 2026-07-29]
- `CLAIM` [E2] Specs vs decision records: specs capture **what** to build/verify; decision records capture **why / instead-of**; both complement for agent context. Writing records **before implementation** preferred while alternatives are fresh. [E2: Glukhov — same URL — accessed 2026-07-29]
- `FACT` [E1] Norris: after human decision, AI drafts ADR including considered options, rationale, consequences; recommend AI-usage disclosure (role, tools, accuracy expectation, human accountability). [E1: Norris Salesforce blog — same URL — accessed 2026-07-29]
- `GAP` Template field-level ADR/MADR law — **out of scope** (S1 / Theme 2 reuse). This slice records *process role* of decision capture only.
- `OPEN` Superpowers brainstorming/writing-plans and AgDR community decision-audit skills — **structure inventory only in S3**; not SoT here.

### 4.4 Cross-lane process pattern (options → constraints → tradeoffs → critique → decide → gate)

- `INFERENCE` [E4] A Wave-1-supported **design-before-implement** spine (not a Toolbelt lock):
  1. **Frame / expand problem** and constraints (human-owned; AI may help surface) — Nava Steps 1–2.
  2. **Criteria** before options (human refine) — Norris Prompt 1–2.
  3. **Alternatives matrix** with explicit tradeoffs/risk ratings — Norris Prompt 3; Nava Step 3.
  4. **Critique loop** (human amends AI analysis; AI as counterpoint) — Norris Prompt 4; Nava.
  5. **Human decide** (accountability) — Norris Prompt 5 / conclusion.
  6. **Record** decision for humans + future agents — Norris ADR draft; Glukhov memory layer.
  7. **HITL gate before implementation** — plan/decision surface approval (Thangamuthu CLAIM); then implement under recorded constraints (Glukhov CLAIM).
  Premises: cited E1/E2 items in §§4.1–4.3.
- `CLAIM` [E3] Secondary/community anti-pattern labels such as “Blank Canvas” (delegate architecture to AI without constraints) appear in practitioner blogs; useful as discovery for W2, **not** locks. [E3 discovery: e.g. https://decyon.com/vibe-coding-ai-development/ — accessed 2026-07-29 — not used as SoT]
- `INFERENCE` [E4] Premature stack/architecture lock without criteria/options/critique conflicts with Norris’s explicit “do not decide” early-step constraints and Nava’s multi-option exploration. Premises: Norris E1; Nava E1.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Human-owned criteria + options matrix + critique + decide, with AI as draft/research partner, is the dominant W1 vendor pattern for AI-assisted architectural design | confirmed (for Salesforce primary) | Norris E1; Nava E1 |
| H2 | Agent orchestration should expose decision surfaces / plan checkpoints rather than opaque autonomous execution for consequential design+build | open | Thangamuthu E2 CLAIM; Norris future-agents section E1 (aspirational) |
| H3 | Coding-agent reliability improves when accepted decision records are in-repo memory and read before changes | open | Glukhov E2 CLAIM; needs W2 Alexandria / E0 corroboration |
| H4 | Cursor Plan Mode implements the plan-then-execute design gate | open | Not verified; W3 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| HITL as primary control | Norris E1: HITL course-correction essential for AI architectural content | Discovery blogs argue execution-time HITL fails at scale; prefer design-time constraints (“Human-on-the-Design”) | **OPEN** — not resolved this wave; both may apply at different layers (decision quality vs runtime agent governance). Prefer E1 for design-decision drafting; do not lock anti-HITL slogans from E3 |
| Autonomy vs checkpoints | Norris E1 explores future autonomous agents for ADR workflows under architect oversight | Thangamuthu E2 argues against autonomous executor default | No hard conflict if autonomy is **after** human decision/plan gate; leave OPEN for product-specific cases |
| “Vibe coding” meaning | Fowler E1: no looking at code | Community semantic diffusion uses term for any AI coding | Prefer Fowler E1 definition for Toolbelt labels |

## 7. Gaps & OPEN

- `GAP` Alexandria corroboration (`ai_llm_agents`, `software_engineering`) — Wave 2.
- `GAP` Non-AI classical design-method baselines (ATAM, etc.) not primary-fetched.
- `GAP` Community skill inventories (Superpowers, AgDR) — S3 only.
- `OPEN` Cursor / IDE Plan Mode official behavior — Wave 3.
- `OPEN` Whether design-time constraint encoding (rules, allowlists, memory promotion) should replace or only supplement per-decision HITL for Toolbelt Design pack — needs W2 + human accept.
- `OPEN` Ownership split propose/critique/decide across multiple agent roles (multi-agent debate) — discovery only; no E1 this slice.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] T5A spine should keep three artifact/process layers distinct: **(A)** human design judgment methods, **(B)** agent orchestration checkpoint patterns, **(C)** durable decision-record memory for coding agents. Collapsing them into “use agents to design” loses propose-vs-decide ownership. Premises: §§4.1–4.3.
- `INFERENCE` [E4] Minimum viable design gate before implementation (candidate, not lock): human-approved criteria + ≥2 options with tradeoffs + recorded decision (status accepted/proposed) + AI disclosure if AI drafted. Premises: Norris E1; Glukhov E2.
- `INFERENCE` [E4] Anti-patterns to flag in later Design pack drafting (still draft): vibes-only (Fowler E1); one-shot “decide everything” prompts without criteria (contradicts Norris E1); AI as decision owner (contradicts Norris E1 + Glukhov E2); treating community skills as SoT (campaign constraint → S3 E3 only).

## 9. Source list (deduped)

1. Dave Norris — Architectural Decisions: A Human-Led, AI-Powered Approach — https://www.salesforce.com/blog/architectural-decisions-human-led-ai-powered-approach/ — accessed 2026-07-29 — **E1**
2. David Nava — 5 Steps to Develop an Architect Mindset With AI — https://www.salesforce.com/blog/5-steps-architect-mindset-ai/ — accessed 2026-07-29 — **E1**
3. Martin Fowler — Vibe Coding — https://martinfowler.com/bliki/VibeCoding.html — accessed 2026-07-29 — **E1**
4. Rost Glukhov — Decision Records for AI-Driven Software Development — https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/ — accessed 2026-07-29 — **E2**
5. Kumar Thangamuthu — AI Agent Architecture: Decision Surfaces, Not Autonomous Executors — https://kumart.me/writing/ai-agents-decision-surfaces — accessed 2026-07-29 — **E2** (product claims about Cursor/Devin: treat carefully; Cursor Plan Mode → OPEN W3)
6. Discovery only (not SoT): https://decyon.com/vibe-coding-ai-development/ ; https://wiki.totto.org/blog/2026/03/16/the-human-in-the-loop--at-design-time/ ; https://gregsurber.com/2026/01/30/Human-on-the-Design.html — **E3**
7. Campaign context (local): `docs/research/notes/theme-5-design/campaign-brief.md`; `docs/research/notes/theme-5-design/t5a-coordinator-pin.md` — **E0** pin/brief only

---

## Parent return summary (FACTS / CLAIMS / GAPs)

**FACTS (E1):** Salesforce (Norris): human-led AI-assisted ADR loop via prompt chaining — criteria → human refine → options/tradeoff matrix → human critique → human decide → AI drafts ADR; HITL course-correct; architect accountable; LLMs ≠ comprehension. Salesforce (Nava): AI as thinking partner — expand problem, challenge assumptions, explore multiple options, system impact before build. Fowler: vibe coding = ship without reading code; best for disposable; distinct from agentic programming with review.

**CLAIMS (E2):** Glukhov: in-repo ADR/PDR/DDR as agent-readable memory; AI drafts ≠ owns; read-before-implement; specs (what) ≠ decision records (why). Thangamuthu: decision surfaces / plan-then-execute checkpoints vs autonomous executors.

**GAPs / OPEN:** Alexandria W2; classical non-AI design methods; S3 community skills; Cursor Plan Mode W3; unresolved tension execution-HITL vs design-time constraints (E3 discovery).
