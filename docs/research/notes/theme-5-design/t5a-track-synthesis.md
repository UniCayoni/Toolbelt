---
title: "T5A track synthesis — Agent / AI-assisted design process"
status: draft
theme: theme-5-design
track: T5A
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
waves: [pin, w1-s1, w1-s2, w1-s3, w2-rag, w2-web, w3]
stop_reason: low_return_plus_one
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5a-coordinator-pin.md
supersedes: null
---

# T5A track synthesis — Agent / AI-assisted design process

**Using `research-protocol`** · depth: **deep** · integrator merge only (no new facts).

**Status:** `draft`. Not Design SoT. Not permission to elevate Design skills.

## 1. Scope

- **Question:** How should humans + coding/creative agents run a design process (options, constraints, tradeoffs, decision, record)?
- **Merged from:** pin + W1 S1–S3 + W2 RAG/web + W3 residual
- **Out:** T5B/T5C/T5D content; Design skill elevation; inventing Plan Mode E0 UX

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep |
| Tools | Read gatherer notes only; no new primary search in this file |
| Waves | pin → W1 (S1 ADR, S2 process, S3 community) → W2 (Alexandria + web) → W3 residual |
| stop_reason | `low_return_plus_one` — W3 restated W2 Plan Mode pins; +1 residual complete; remaining = confirmed GAP/OPEN |
| Subagents | `cursor-grok-4.5-high-fast` |
| What was not searched | T5B/T5D; UX (T5C deferred); further community fleets after W3 |

### Note IDs

| ID | Path |
|----|------|
| PIN | `t5a-coordinator-pin.md` |
| W1-S1 | `t5a-w1-s1-adr-madr.md` |
| W1-S2 | `t5a-w1-s2-agent-design-process.md` |
| W1-S3 | `t5a-w1-s3-community-agent-workflows.md` |
| W2-RAG | `t5a-w2-alexandria-corroboration.md` |
| W2-WEB | `t5a-w2-web-corroboration.md` |
| W3 | `t5a-w3-residual-gaps.md` |

## 3. Spine (merged — draft, not lock)

Keep three **lanes** separate (W1-S2):

| Lane | Meaning |
|------|---------|
| A | Human design methods (criteria, judgment, decide) |
| B | Agent orchestration (plan/propose → gate → execute) |
| C | Coding-agent decision capture (in-repo rationale memory) |

**Design-before-implement loop** (INFERENCE [E4] from W1-S2, corroborated W2):

1. Frame problem / constraints (human-owned; AI may help)  
2. Criteria before solutions (human refine)  
3. Alternatives + tradeoffs (matrix / 2–3 approaches)  
4. Critique / amend  
5. **Human decides** (accountability)  
6. Record decision (ADR/MADR shape; AI may draft, human owns)  
7. HITL gate before implementation  

Anti-pattern: vibes-only / no review of durable artifacts (Fowler vibe coding [E1] W1-S2).

## 4. Findings (merged)

### 4.1 Decision records (Lane C + record step)

- `FACT` [E1] Nygard: one ADR per architecturally significant decision; Context / Decision / Status / Consequences; ~1–2 pages; Markdown in repo; proposed→accepted→deprecated|superseded; keep old records. [W1-S1]
- `FACT` [E1] Fowler: brevity; list serious alternatives + pros/cons; once accepted, do not edit — supersede. [W1-S1]
- `FACT` [E1] MADR 4.0: Considered Options → Decision Outcome → Consequences (+ optional Drivers/Pros-Cons/YAML). [W1-S1]
- `FACT` [E2] Theme 2 §2.5 already established ADR/MADR as decision-log layer; draft/proposed ≠ SoT. [W1-S1]
- `FACT` [E1] ADR create-when: significance / multi-option / undocumented architectural impact (AWS PG + Nygard + Google Cloud corroboration). [W2-WEB]
- `INFERENCE` [E4] Options+tradeoffs+decision+consequences is the agent-usable record shape (Fowler/MADR atoms on Nygard core). Premises: W1-S1. [W1-S1]
- `CLAIM` [E2] AI may draft ADRs; humans must verify (no invented rationale). [W1-S2 Glukhov; W1-S2 Norris]

### 4.2 Human + AI design process (Lane A)

- `FACT` [E1] Salesforce (Norris): criteria → human refine → options/tradeoff matrix → human critique → **human decide** → AI drafts ADR; HITL course-correct. [W1-S2]
- `FACT` [E1] Nava: AI as thinking partner (expand problem, challenge assumptions, multi-option) before build. [W1-S2]
- `FACT` [E1] Fowler Design-First + MIT CISR decision-rights corroborate human-led design-before-code beyond Salesforce alone. [W2-WEB]
- `FACT` [E2] Alexandria: Osmani *Beyond Vibe Coding* + Taulli *AI-Assisted Programming* corroborate plan-first / planning-before-coding; HITL review-approve patterns. [W2-RAG]

### 4.3 Agent orchestration (Lane B)

- `CLAIM` [E2] Decision surfaces / plan-then-execute checkpoints vs opaque autonomous executors. [W1-S2 Thangamuthu]
- `FACT` [E1] Cursor Plan Mode (official docs): clarify → plan → human review → build. [W2-WEB; W3 re-pin]
- `FACT` [E1/OPEN] Official docs do **not** establish Plan Mode as ADR/alternatives-matrix replacement — do not equate without evidence. [W3]
- `GAP` E0 Plan Mode UX unobserved this campaign. [W3]

### 4.4 Community structure inventory (E3 only — not Toolbelt law)

- `FACT` [E0/E3] Superpowers brainstorming: hard gate no code until design approved; 2–3 options+tradeoffs; sectional + written-spec HITL; then writing-plans. [W1-S3]
- `FACT` [E0/E3] writing-plans: file map, interfaces, TDD-ish task checkboxes — **do not import** Superpowers git/PR/worktree policies. [W1-S3]
- `FACT` [E3] AgDR: Y-statement + Options table (≥2) + Decision; agent/model/trigger metadata; single-author lineage (no second independent E1/E2). [W1-S3; W2-WEB]
- Homonym risk: other “AgDR” names exist — keep me2resh lineage explicit. [W2-WEB]

## 5. Conflicts (retained)

| Topic | Resolution for Toolbelt (draft) |
|-------|----------------------------------|
| ADR status vocab (Nygard vs Fowler vs MADR `rejected`) | OPEN — cite all; Theme 2 currently mirrors Nygard quartet |
| ADR folder path | GAP — project meta-decision |
| AgDR create-when (broad) vs ADR significance bar | Keep grades separate; prefer E1 ADR triggers for architecture-significant |
| HITL design-time encoding vs per-decision gates | OPEN — may apply at different layers [W1-S2; W2-WEB; W3] |

## 6. Confirmed GAP / OPEN (after stop)

- `GAP` Agent-native ADR schema / machine-required HITL field mapping  
- `GAP` Classical non-AI design baselines (ATAM etc.) not primary-fetched  
- `GAP` E0 Cursor Plan Mode UX  
- `OPEN` House ADR status enum + Confirmation/RACI YAML policy  
- `OPEN` HITL design-time vs per-decision acceptance  
- `OPEN` AgDR remains E3 — do not lock  
- `OPEN` T5C UX deferred (campaign-level)

## 7. Implications for later elevation (not commitments)

After Theme 5 accept + `author-cursor-surfaces` only:

- A **design-process** skill could encode Lane A loop + ADR/MADR record step + human decide gate  
- Coexist with Superpowers brainstorming as **process cousin** — do not merge git/PR policies  
- Reject mega-skill covering T5B/T5C/T5D content  
- Thin rule candidate: draft design / proposed ADR ≠ accepted architecture (mirror draft≠SoT)

## 8. Ready for next campaign step

T5A track synthesis **complete** (`stop_reason: low_return_plus_one`).

**Next per brief:** launch **T5B + T5D** deep in parallel (T5C still deferred).
