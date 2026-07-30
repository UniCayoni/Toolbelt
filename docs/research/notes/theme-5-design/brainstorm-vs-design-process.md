---
title: "Superpowers brainstorming vs Toolbelt design-process (transfer scan)"
status: draft
theme: theme-5-design
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/reports/theme-5-design-pocket.md
  - skills/design-process/SKILL.md
supersedes: null
---

# Brainstorming vs design-process — what to borrow

**Using `research-protocol`** · depth: **normal** (transfer scan only).

## 1. Scope

- Question: What does Superpowers `brainstorming` do, how it compares to Toolbelt Design skills, and what (if anything) to integrate **without contradicting** accepted Theme 5.
- In: Structure/process comparison; compatible transfers into `design-process` (and checklist).
- Out: Re-adopting Superpowers; importing git/worktree/PR/TDD plan machinery; elevating UX visual companion as SoT (T5C deferred).

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | normal |
| Tools | Read local Superpowers `brainstorming` + `writing-plans` SKILL.md; Toolbelt `design-process`; Theme 5 / T5A-S3 notes |
| Paths | `…/superpowers/…/skills/brainstorming/SKILL.md`; `…/writing-plans/SKILL.md`; `skills/design-process/SKILL.md` |
| What was *not* searched | visual-companion.md deep dive; marketplace popularity; runtime A/B of both skills |

## 3. What brainstorming does (E0)

Ordered loop with a **hard gate** (no code/scaffold/implement until design approved):

1. Explore project context  
2. Optional visual companion (JIT, not upfront)  
3. Clarifying questions **one at a time** (MC preferred)  
4. **2–3 approaches** + tradeoffs + recommendation  
5. Present design **in sections**; approve per section  
6. Write spec to `docs/superpowers/specs/…` (+ commit)  
7. Spec self-review (placeholders, consistency, scope, ambiguity)  
8. User reviews written spec  
9. Hand off **only** to `writing-plans`  

Also: decompose oversized multi-subsystem asks; YAGNI; existing-codebase pattern-following; scale section length to complexity.

`writing-plans` (adjacent): file map, Interfaces, tiny TDD-ish steps, Superpowers plan paths / execution skills — **out of Design pocket transfer** (git/exec policy).

## 4. Comparison to Toolbelt Design skills

| Aspect | Brainstorming (E0/E3) | Toolbelt Design (Theme 5 accept) |
|--------|----------------------|----------------------------------|
| Trigger | Before *any* creative/impl work (incl. “simple”) | Non-trivial design; domain handoffs |
| Options | 2–3 + recommend | 2–3 + critique + human decide |
| Record | Feature **spec** under `docs/superpowers/specs/` | **ADR** under `docs/adr/` when significance triggers; draft≠SoT |
| Gate | Dual: sectional chat + written spec | Human decide + gate before implement |
| Depth | Architecture/components/data/error/testing in one flow | Spine → `technical-design` / creative-* |
| Next step | Forced `writing-plans` | Implement/plan tasks; no Superpowers handoff |
| Authority | Community skill | Accepted Theme 5 method SoT |

**Overlap (already aligned):** options/tradeoffs, human approval before implement, criteria-ish clarifying (purpose/constraints/success).

**Toolbelt strengths brainstorm lacks:** ADR house + significance triggers; lane separation (A/B/C); domain skills; contested-standards / plural creative disclaimers; explicit draft≠accepted.

**Brainstorm strengths Toolbelt spine was thin on:** context explore first; 1Q/msg; sectional approval; written design/spec + self-review checklist; decompose-before-deep-design; scale-to-complexity; lead with recommendation.

## 5. Transfer decisions

### Adopt (compatible with Theme 5)

| Practice | Why OK |
|----------|--------|
| Explore context before deep questions | Matches recon/design intent; no Superpowers path |
| One clarifying question at a time; MC when useful | Improves HITL; doesn’t weaken human decide |
| Lead with recommended option among 2–3 | Still human decides; Toolbelt bias: quality, readability, faithfulness to intent |
| Present design in sections; approve as you go | Strengthens HITL gates |
| Written design note + self-review (placeholder/consistency/scope/ambiguity) | Complements ADR; use Toolbelt path `docs/design/` not Superpowers |
| Decompose multi-subsystem asks before one mega-design | Prevents scope explosion |
| Scale design length to complexity (short OK if approved) | Still a design gate; ADR only on significance triggers |
| Existing codebase: follow patterns; no drive-by refactors | Aligns technical-design |

### Do **not** adopt

| Practice | Why |
|----------|-----|
| Absolute hard gate on *every* trivial change | Toolbelt keeps “non-trivial” + ADR triggers; always-on absolute gate fights judgment |
| `docs/superpowers/…` paths / auto-commit | Wrong product; don’t merge git policy |
| Forced handoff to `writing-plans` / worktrees / commit-per-step | Explicit non-goal (user: ignore Superpowers in Toolbelt) |
| Visual companion as required Design surface | T5C deferred; optional later if UX track reopens |
| Replacing ADR with only a feature spec | Theme 5: significant decisions → `draft-adr` |

### OPEN (not now)

- Separate Toolbelt **implementation-plan** skill (file map / interfaces) inspired by writing-plans structure — Build pack later; keep out of Design elevation this pass.

## 6. Recommendation

Integrate the **Adopt** row into `design-process` + checklist. Keep Toolbelt naming, ADR house, and no Superpowers references. Leave writing-plans machinery out.

## 7. Sources

1. Local Superpowers brainstorming/writing-plans SKILL.md (E0)  
2. Toolbelt `skills/design-process/SKILL.md`  
3. Theme 5 accepted report + T5A-S3 inventory  
