---
name: guide-design
description: >-
  Run Toolbelt’s design-before-implement loop (formerly design-process): explore
  context, clarify (one question at a time), criteria, 2–3 options/tradeoffs,
  sectional design approval, optional design note + self-review, human decide,
  ADR when needed, then implement. Use when guide-design, design-process,
  designing features, architecture, creative systems, planning before code,
  alternatives matrices, HITL design gates, or when the user asks to design
  (not just build). Prefer this over jumping straight to implementation.
---

# Guide design

Announce once: **Using `guide-design`**.

Authority: Theme 5 accepted (T5A method guidance). **Draft/proposed designs and ADRs ≠ accepted law.**  
Theme 14/20: Design pocket **guide** entry (`guide-design`; was `design-process`).

## When to use

- Non-trivial design: features, architecture, creative systems, process locks
- Before writing implementation code for a new capability
- When options or tradeoffs exist

Simple work can still use a **short** design (a few sentences) + approval — skip heavy docs/ADRs unless significance triggers fire.

**Out of scope:** Product UX/UI methods (T5C deferred). Domain depth → `design-technical` / `design-systems` / `design-narrative` / `design-world-character` after the spine. Do not import third-party git/worktree/plan-execution workflows.

## Spine (do in order)

1. **Explore context** — relevant files, docs, recent patterns in the host project (lightweight recon; use `research-codebase-recon` when the area is unfamiliar or large)
2. **Scope check** — if the ask spans multiple independent subsystems, help decompose into sub-designs first; do not deep-design a platform in one pass
3. **Clarify** — purpose, constraints, success criteria; **one question per message** when possible; prefer multiple-choice when it fits
4. **Criteria before solutions** — what “good” means; do not lock stack/story yet
5. **Options** — **2–3** real approaches with tradeoffs; **lead with your recommendation and why** (human still decides). When recommending, **lean toward**: (a) **quality** (sound structure, maintainability, honest tradeoffs), (b) **code readability** (clear boundaries, understandable units — not clever opacity), (c) **faithfulness to intent** (what this design is actually for — purpose/success criteria — over trendy stacks, drive-by scope, or unrelated refactors)
6. **Present design in sections** — scale length to complexity; get approval after each section (or revise)
7. **Critique** — pressure-test; amend; call out vibes-only / premature lock / drive-by unrelated refactors
8. **Human decide** — you propose; **human is accountable**
9. **Record**
   - Significant / multi-option locks → **`research-draft-adr`** → `docs/adr/NNNN-slug.md`
   - Broader feature shape (when useful) → short design note under host `docs/design/YYYY-MM-DD-<topic>-design.md` (user path overrides OK)
10. **Self-review** (written artifacts): placeholders/TODOs, internal contradictions, scope too large, ambiguous requirements — fix before asking for final review
11. **Gate** — only after approval proceed via **`guide-implementation`** (or leaves: **`implementation-plan`** → **`implementation-plan-verify`** → **`implementation-execute`** / `-subagents` → **`implementation-execute-verify`**). Trivial one-file work may skip durable plan/execute (intelligent exception)

## Lanes (keep separate)

| Lane | Meaning |
|------|---------|
| A | Human judgment & criteria |
| B | Agent orchestration (plan → gate → execute) |
| C | Decision capture (ADR / design note memory) |

## Existing codebases

- Follow existing patterns unless the design explicitly changes them
- Include targeted boundary fixes only when they serve the current goal
- Do not propose unrelated refactors

## Anti-patterns

- Vibes-only / implement with no options or approval
- Treating chat plans as a substitute for ADR when significance triggers fire
- Locking libraries/stacks from draft research alone
- One mega-design for multiple independent subsystems

## Domain handoff

| Domain | After spine, use |
|--------|------------------|
| Code architecture / stack / services | `design-technical` then `research-draft-adr` as needed |
| Game/creative systems | `design-systems` |
| Story / quests / interactive narrative | `design-narrative` |
| World bible / characters | `design-world-character` |
| UX / UI product design | **Defer** — no Toolbelt skill yet (T5C) |

## Handoffs (after gate)

| Need | Use |
|------|-----|
| Full Toolbelt ladder (cold start / controller) | **`implementation-happy-path`** |
| Implementation pocket wire (prefer) | **`guide-implementation`** |
| Implementation plan (leaf) | `implementation-plan` |
| Validate plan before ready | `implementation-plan-verify` |
| Execute | `implementation-execute` / `-subagents` + `implementation-execute-verify` |
| Lock Decision | `research-draft-adr` |

## References

- Read `references/guide-design-checklist.md` **when** running a full design session or recovering a skipped step
- Transfer rationale: `docs/research/notes/theme-5-design/brainstorm-vs-design-process.md` (draft note; Theme 5 remains SoT)
- Theme 5: Toolbelt `docs/research/reports/theme-5-design-pocket.md` (accepted)
