---
title: "T5B track synthesis — Technical design"
status: draft
theme: theme-5-design
track: T5B
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
waves: [pin, w1-s1, w1-s2, w1-s3, w2, w3]
stop_reason: low_return_plus_one
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5a-track-synthesis.md
supersedes: null
---

# T5B track synthesis — Technical design

**Using `research-protocol`** · depth: **deep** · merge only (no new facts).

**Status:** `draft`. Not Design SoT.

## 1. Scope

How to design architecture, features, stacks, services/apps, and coding/clean standards at design-time (with agents), without locking stacks or elevating lint packs.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep |
| stop_reason | `low_return_plus_one` |
| Subagents | `cursor-grok-4.5-high-fast` |
| Notes | `t5b-coordinator-pin.md`, `t5b-w1-s1/s2/s3-*.md`, `t5b-w2-corroboration.md`, `t5b-w3-residual.md` |

## 3. Findings (merged)

### 3.1 Architecture / modularity

- `FACT` [E1/E2] Clean Architecture Dependency Rule: source deps inward; UI/DB/frameworks outer. [W1-S1]
- `FACT` [E1/E2] Component principles ADP/SDP/SAP; W2 closed REP/CCP/CRP via Martin book. [W1-S1; W2]
- `FACT` [E2] GoF = named problem/solution/consequences vocabulary — not whole-app architecture. [W1-S1]
- `FACT` [E1] Hexagonal (Cockburn) + Onion (Palermo) primaries closed in W3. [W3]
- `FACT` [E2] Architecture Patterns with Python: DIP/ports; Metrics: cycles/MMI. [W2]

### 3.2 Stack / feature / ADR triggers

- `FACT` [E1] ADR when architecturally significant (structure, NFRs, deps, interfaces, construction) — Nygard/AWS; multi-option/undocumented — Google; single decision + alternatives — Fowler. [W1-S2; reuse T5A]
- `FACT`/`CLAIM` [E1/E2] Monolith-first / microservice premium vs outcome-first microservice benefits — **cite both sides**. [W1-S2; W2 Gorton/Esposito]
- `INFERENCE` [E4] Feature design uses T5A spine; escalate to ADR when significance triggers fire. Premises: T5A synth + W1-S2.

### 3.3 Clean / standards + agents

- `FACT`/`CLAIM` Contested: Martin Clean Code/Architecture as school vs critiques (qntm, Letsch, deep-module debates) — **no winner**. Treat as design-time **constraints**, not architecture SoT. [W1-S3]
- `FACT` [E2] Agent-assisted technical design: plan-first, human owns architecture decisions (Osmani/Taulli). [W1-S3; aligns T5A]

## 4. GAP / OPEN

- Windows service/desktop design — non-P0; not deep-researched  
- Newman/APOSD absent from Alexandria  
- House ADR-significance checklist OPEN  
- No grey-matter stack locks  

## 5. Elevation implications (not commitments)

- Technical-design skill: Dependency Rule + modularity criteria + ADR triggers + contested-standards awareness + T5A HITL  
- Point at `draft-adr`; not a lint pack  
- Reject mega-skill with T5D/T5C content  
