---
title: "Theme 6 — Plan pocket deep research campaign brief"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
campaign_phase: accepted_elevated
aligned_with:
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
  - docs/research/reports/theme-5-design-pocket.md
  - docs/research/notes/theme-5-design/brainstorm-vs-design-process.md
supersedes: null
---

# Theme 6 — Plan campaign brief

**Using `research-protocol`** · depth: **deep**.

**Status:** `draft` brief. Not Plan SoT. No Plan skills elevated until accept + `author-cursor-surfaces`.

**Human kickoff (2026-07-29):** Deep research authorized; Wave 1 launched without separate approval gate (intent given in session).

---

## 1. Purpose

| Field | Value |
|-------|-------|
| Pocket | **Plan** (everything Toolbelt owns about planning) |
| Goal | Evidence-backed methods to **write plans agents (incl. fresh subagents) can follow** — faithful to prior research + design, low hallucination/assumption, good decomposition |
| Depth | deep: Wave 1→2→3 per track; Theme 5 stop: low-return → **+1 residual** → `low_return_plus_one` |
| Ladder | Research → Design (accepted) → **Plan (this)** → Implement (mostly agent) → Verify/Debug later |

**Non-goals now:** Elevating Plan skills mid-research; importing Superpowers git/worktree/TDD as Toolbelt law; Build-domain recipe sprawl; UX planning (T5C still deferred).

---

## 2. Campaign cautions

| Risk | Mitigation |
|------|------------|
| Stars = SoT | E3 discovery only until E0/E1/E2 corroborate |
| Plan vs Design blur | Design owns *what/why*; Plan owns *how to sequence checkable work* |
| Plan vs Implement blur | Plan does not teach language/framework craft |
| Multi-agent hype | Separate orchestration patterns from plan *document* quality |
| RAG false friends | “Planning” in ML/robotics/path-planning ≠ software task plans |
| Context waste | +1 after low-return; no chained +1s |

---

## 3. Tracks

### T6A — Plan artifacts for fresh / subagent readers

How to write a plan so a **new context** can execute without inventing requirements: self-contained facts, explicit constraints, interfaces, verify steps, “do not assume” rules; link to design/ADR/research without requiring the reader to re-derive them.

### T6B — Decompose design → plan

How to break approved design (and supporting research) into ordered tasks, file maps, boundaries, acceptance checks; scale simple vs complex (atomize).

### T6C — Plans under 1..N agent execution

How plans should be shaped when one agent or multiple subagents execute (task isolation, handoff packets, shared vs private context, review gates). **Not** locking Superpowers execution skills.

### T6D — High-signal community plan-writing skills (discovery)

Inventory highly starred/discussed GitHub skills/rules for plan writing; structure only until corroborated.

**Optional gap fleet (coordinator):** After W1/W2, spawn extra gatherers only for named P0/P1 (e.g. context engineering for specs, anti-assumption checklists, BMAD story packets).

---

## 4. Shared protocol

- Cite-or-omit; FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U  
- Subagents: `cursor-grok-4.5-high-fast`  
- Notes: `docs/research/notes/theme-6-plan/`  
- Report: `docs/research/reports/theme-6-plan-pocket.md` (draft until accept)  
- Reuse Theme 5 Design spine as **input** to plans; do not re-litigate Design  
- Stop: `low_return_plus_one` per track / campaign  

### Parallelism

| Phase | Shape |
|-------|-------|
| W1 | Parallel T6A–T6D gatherers |
| W2 | Corroboration (RAG+web+GitHub deepen) |
| Gap fleet | Only if named high-value GAPs |
| W3 / +1 | Residual closers |
| Integrate | Serial |

---

## 5. Candidate elevation (post-accept only — not commitments)

| Candidate | Notes |
|-----------|-------|
| `implementation-plan` / `write-plan` skill | Core pocket skill |
| Plan checklist / template in `references/` | Self-contained task shape |
| Thin rule: no implement without plan when non-trivial | Optional; intelligent |
| Compose later | Entry-flow skill after pieces proven |

---

## 6. Approval / kickoff

- [x] Human authorized deep Plan research (2026-07-29 session)  
- [x] Stop rule: Theme 5 +1 residual  
- [x] Superpowers = E3 structure inventory; no git/PR merge  
