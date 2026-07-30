---
title: "Theme 7 — Execution pocket deep research campaign brief"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: deep
campaign_phase: accepted_elevated
aligned_with:
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
supersedes: null
---

# Theme 7 — Execution campaign brief

**Using `research-protocol`** · depth: **deep**.

**Status:** `draft` brief. Not Execution SoT. Scoping: [`scope-normal.md`](./scope-normal.md).

**Human approved (2026-07-30):** tracks T7A–D; subagents `cursor-grok-4.5-high-fast`; stop `low_return_plus_one`; directional OPENs per §7.1.

---

## 1. Purpose

| Field | Value |
|-------|-------|
| Pocket | **Execution / Implementation** (drive approved plans to code with cold agents) |
| Goal | Evidence-backed methods so agents **execute** Theme 6 plans (and equivalents) without inventing requirements — verify, escalate, preserve quality/readability |
| Depth | deep: Wave 1→2→3 + `low_return_plus_one` |
| Ladder | Research → Design → Plan (shipped) → **Execute (this)** → Verify/Debug (later; may be touchups not a full pocket) |

**Non-goals:** Language/framework Build cookbooks; importing Superpowers (or other plugins) as runtime dependency; re-opening Plan density decisions; elevating skills mid-research; Brain/RAG product work.

**Essence filter:** Toolbelt remains a **standalone method utility**. Take inspiration from Superpowers / OpenSpec / BMAD / Spec Kit — extract what works, **do not depend on them**. Prefer transferable loops over product-specific harnesses.

---

## 2. Why this pocket (from normal scope)

| Gap today | Normal-scope finding |
|-----------|----------------------|
| Plan writes; nothing executes | Theme 6 elevated `implementation-plan`; no execute skill |
| Community already has execute skills | Superpowers `executing-plans` + SDD; OpenSpec apply; BMAD build |
| Vendor E1 agrees on cold exec | Fresh session, runnable verify, don’t guess, review gates |
| RAG = principles | plan→execute→verify→report; reflection; HITL — not a skill grammar |

Highest-value target: thin Toolbelt-native **`execute-plan`** (or `implement-plan`) that consumes `docs/plans/…` + Plan status vocab.

---

## 3. Tracks

### T7A — Cold-agent execute loop (spine)

Load plan → critical review → task loop → Done-when/verify → update status → stop/escalate (`intent-gap` / `verify-fail` / `needs-human` / major deviation).

### T7B — Subagent controller execution (broad-use)

Per-task packets to fresh implementers; serial vs parallel-safe (Plan #2); task-level vs end review. **Priority:** patterns usable across almost all implementations (SDD-like controller), not niche Build recipes.

### T7C — Community execute-skill deepen

Deep-read Superpowers execute/SDD/verification-before-completion; OpenSpec apply; Spec Kit implement/converge; BMAD build-auto implement. Stars=E3; transferable atoms only; park git/TDD packaging; **no runtime dependency** on those projects.

### T7D — Pocket boundaries & elevation candidates

Execute vs later review/debug touchups; **main spine skill + supplementary skills** as needed; house paths; coexistence (inspiration ≠ dependency); draft≠SoT for in-progress plan status.  
**Note (human):** T7D feeds a future **review** effort that may cover plan+execute review and multi-use tooling — may be a pocket or **touchups** on Plan/Execute (+ Debug). Keep T7D findings portable for that later work.

**Optional gap fleet:** Only if W2 names P0.

---

## 4. Shared protocol

- Cite-or-omit; FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U  
- Subagents: **`cursor-grok-4.5-high-fast`**  
- Notes: `docs/research/notes/theme-7-execute/`  
- Report: `docs/research/reports/theme-7-execute-pocket.md` (draft until accept)  
- Theme 6 Plan = **input law** (do not re-litigate)  
- Stop: low-return → **+1 residual** → `low_return_plus_one`

| Phase | Shape |
|-------|-------|
| Approve brief | **done** 2026-07-30 |
| W1 | Parallel T7A–T7C + T7D light |
| W2 | Corroboration + named GAPs |
| W3 / +1 | Residual |
| Integrate | Serial → draft report |

---

## 5. Candidate elevation (post-accept only)

| Candidate | Notes |
|-----------|-------|
| Main spine: `execute-plan` / `implement-plan` | Core pocket |
| Supplementary broad-use skills | e.g. subagent-driven execute pattern — when evidence supports |
| Light companions (verify-before-done atoms) | Fold or thin companion; fuller review deferred |
| Thin always-on rule | Unlikely (skill-only) |
| Entry-flow compose | Later |

---

## 6. Value / quality lean (integrator)

1. **Faithfulness to plan** — no invent; blocked on gaps / major deviation → human  
2. **Quality & readability** — verify gates; optional fresh reviewer; no drive-by refactors  
3. **Thin method + standalone** — no Build sprawl; inspire-from, don’t depend-on Superpowers/others  
4. **Plan compatibility** — `plan-minimal` / status vocab / serial default  

---

## 7. Approval gate

- [x] Human approves brief + tracks T7A–D (2026-07-30)  
- [x] Subagents: `cursor-grok-4.5-high-fast`  
- [x] Stop: `low_return_plus_one`  

### 7.1 Directional OPEN decisions (human 2026-07-30)

| OPEN | Decision |
|------|----------|
| Skill naming | **Toolbelt-native** (`execute-plan` / `implement-plan` style). Inspiration from other projects OK; **standalone** — no Superpowers (or other) dependency; extract what works and cut coupling over time. Same stance for OpenSpec/BMAD/Spec Kit/etc. |
| One skill vs two | **Main spine skill** + **supplementary skills** as needed by plan/implementation shape. Prefer researching **broad-use** supplements (esp. subagent-driven patterns usable across nearly all implementations). |
| HITL between tasks | **Escalate / ask user** on major deviation or blocked implementation — not pause for every task when green. |
| Companion / review | Light companion atoms OK in Execute. Fuller “what exists / keep / change” for plan+execute review → later **review** work (may be pocket **or** touchups on Plan/Execute + Debug consideration) — T7D should leave portable notes for that. |
