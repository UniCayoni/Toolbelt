---
title: "Theme 8 — Verify gates normal scope (pass 1)"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
  - skills/implementation-plan/SKILL.md
  - skills/implementation-execute/SKILL.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 8 — Verify gates: normal research pass 1

**Using `research-protocol`**; depth: **normal** (scoping — what to deep-research).

**Status:** `draft`. Not Verify SoT. Lean: **quality + code readability** first; ease is a side effect. Toolbelt = standalone method utility.

## 1. Scope

- Question: What evidence-based **verification/validation gates** should Toolbelt add for **Plan** and **Execute**, and what surface shape (fold vs companion skill vs shared verify skill) fits the project spirit?
- In: Inventory what Plan/Execute already own; community/vendor patterns; gaps for deep brief.
- Out: Elevating skills; Debug pocket design; mandatory TDD/git as law; re-litigating Plan density / Execute N=2.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (Plan/Execute skills, checklists, plan-minimal, T7D); Alexandria `rag_probe`; WebSearch; `gh` Superpowers verification-before-completion |
| Queries | evidence-based verification validation gates AI coding agents; verification-before-completion SKILL |
| What was *not* searched | Full validating-plans deep refs (known 404 Theme 6); Spec Kit converge body; quality-rubric literature beyond Osmani probe |
| Depth | normal |
| stop_reason | Pass-1 inventory complete; expansion needed on plan-QA depth, quality-beyond-command, surface shape |

## 3. E0 — What Plan & Execute already do

### Plan (`implementation-plan`)

| Gate | Present? | Notes |
|------|----------|-------|
| Done-when + Verify **grammar** in each task | yes | command + expected signal |
| V1–V8 **light pre-exec** checklist | yes | intent, files, verify runnable, reality-check, drift, design Qs, constraints, hybrid density |
| Faithfulness to approved Design/ADR | partial | consume Decision; no invent — not a graded “plan vs design” audit skill |
| Standalone plan-validate skill | **no** | Theme 6 deferred full validating-plans |

### Execute (`implementation-execute` / `-subagents`)

| Gate | Present? | Notes |
|------|----------|-------|
| Critical review before code | yes | batch concerns |
| Evidence-before-completion (run Verify) | yes | N=2 then verify-fail |
| Major-deviation / escalate | yes | HITL on blocked/major deviation |
| Fresh task reviewer (spec + quality/readability) | **optional mention only** | subagents skill; not a rubric |
| End-of-plan / converge vs design+plan | **optional light** / deferred | Theme 7 → later review |
| Shared cross-cutting verify skill | **no** | folded lightly into execute |

- `FACT` [E0] Packs: Quality/Verify stub — “may be pocket **or** touchups on Plan/Execute”. [E0: `docs/packs/README.md`]
- `FACT` [E0] T7D: Plan owns V1–V8; Execute owns Done-when **run** + light verify; fuller review portable later. [E0: `t7d-w1-boundaries-elevation.md`]

## 4. Community / vendor signal (pass 1)

- `FACT` [E1] Superpowers `verification-before-completion`: Iron Law — no completion claims without fresh evidence; gate IDENTIFY→RUN→READ→VERIFY→claim; rejects “should/probably/looks”. [E1: obra/superpowers SKILL.md via GitHub API 2026-07-30]
- `CLAIM` [E3] Same pattern widely mirrored (Charpup, registries). Stars≠SoT. [E3: WebSearch]
- `FACT` [E1] Claude: runnable verify; adversarial fresh-subagent review against criteria; “if you can’t verify it, don’t ship it”. [E1: Theme 6/7 prior; Claude best practices]
- `FACT` [E2] Osmani: trust-but-verify; AI as validator; review for quality/readability/security; human owns final code. [E2: Alexandria Beyond Vibe Coding — probe pass 1]
- `FACT` [E0] Theme 6 inventoried validating-plans (reality-check / drift / TDD auditor) — deep refs 404; pocket home was OPEN. [E0: Theme 6 notes]

## 5. Gaps that need expansion (or deep)

| Gap | Why it matters for Toolbelt |
|-----|----------------------------|
| Plan-side **validate** beyond V1–V8 | Quality of *plans* (coverage, inventable ambiguity, weak Verify steps) before execute burns context |
| Execute-side **quality/readability** evidence | Command pass ≠ readable/maintainable/faithful code — user lean |
| Surface shape | Fold vs companions — **later locked C:** `implementation-plan-verify` + `implementation-execute-verify` (see campaign-brief §0) |
| Converge / gap-append patterns | Spec Kit converge (append remaining work) — not deep-read pass 1 |
| When HITL review is required vs optional | Quality lean vs thin method |

## 6. Implications (pass 1)

- `INFERENCE` [E4] Theme 8 is **not** starting from zero — strengthen **gates** on existing Plan/Execute, possibly plus a thin shared verify companion. Premises: §3–§4.
- `INFERENCE` [E4] **Pass 2 expansion warranted** before deep brief: (1) plan-validate atom candidates; (2) quality/readability review criteria for execute; (3) Spec Kit converge + Claude adversarial review as E1; (4) surface-shape options matrix. Premises: §5 gaps block a sharp deep brief.
