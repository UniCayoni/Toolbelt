---
title: "Theme 8 — Verify gates normal scope (pass 2 expand + analysis)"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-8-verify/scope-normal-pass1.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
supersedes: null
---

# Theme 8 — Verify gates: pass 2 expand + analysis

**Using `research-protocol`**; depth: **normal** (expansion of pass-1 gaps — still not deep fleets).

**Lean:** quality + code readability; faithfulness to plan/design; Toolbelt standalone method spirit.

## 1. Scope

Close pass-1 gaps enough to write a Theme 8 **deep campaign brief**. Decide whether a **third** normal pass is needed.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Alexandria `rag_query` (SE); WebFetch Claude best-practices; `gh api` Spec Kit `converge.md`; Read pass-1 + Plan/Execute |
| What was *not* searched | Full HCI lit on code review; live E0 Toolbelt verify trials; Debug pocket |
| Depth | normal |
| stop_reason | Expansion gaps closed at discovery level; **no third normal pass** — remaining work is deep-track grade |

## 3. Expansion findings

### 3.1 Plan-validate atom candidates (beyond V1–V8)

From Theme 6 validating-plans inventory + Spec Kit/BMAD gates (prior) + pass-1:

| Candidate atom | Lane | Source grade |
|----------------|------|--------------|
| Reality-check paths/APIs/commands exist | Plan pre-exec (strengthen V4) | E1 Theme 6 |
| Drift vs tree/deps when plan reused | Plan (V5 deepen) | E1 Theme 6 |
| Spec/plan **coverage** (FR/section → task; no orphan tasks) | Plan validate | E1 BMAD/Spec Kit prior |
| Verify steps are **falsifiable** (not “looks good”) | Plan authoring + validate | E1 Claude + verification-before-completion |
| Ambiguity / inventable gaps → NEEDS CLARIFICATION / blocked | Plan | E1 Spec Kit / BMAD HALT |
| No TBD / placeholder scan | Plan (already anti-pattern) | E0 Plan skill |
| TDD Compliance Auditor / gh-issue packaging | **Park** | E3 Theme 6 — not Plan law |

- `INFERENCE` [E4] Plan-side Theme 8 work = **strengthen validate gates** (fold and/or thin `implementation-plan-validate` companion), not a mega Quality pocket. Premises: T7D; packs stub; user Theme 8 ask.

### 3.2 Execute: evidence + quality/readability

- `FACT` [E1] Superpowers verification-before-completion gate (IDENTIFY→RUN→READ→VERIFY→claim) already partially folded into Execute Done-when run. [E1: pass-1]
- `FACT` [E1] Claude: fresh-context **adversarial review** against named criteria (diff + plan); evidence over assertion. [E1: https://code.claude.com/docs/en/best-practices — 2026-07-30]
- `FACT` [E1] Spec Kit **converge**: assess codebase vs spec/plan/tasks; classify gaps (`missing`/`partial`/`contradicts`/`unrequested`); **append-only** remediation tasks; no silent rewrite of plan/spec; no app code edits in converge itself. [E1: github/spec-kit `templates/commands/converge.md` via API 2026-07-30]
- `FACT` [E2] Osmani code-review checks include correctness **and** readability/maintainability, style, unused code, comments/intent — human diligence on AI output. [E2: Alexandria chunk_ids `d0369fad9ec1c3e4c6d4b750`, `b08ba03768f720bb46605057`, `ae5ea30721760ce3b23ed7af`]
- `INFERENCE` [E4] Execute Theme 8 should add a **second evidence layer** after command green: optional/required fresh review against (a) plan Done-when/constraints, (b) **readability/maintainability** rubric (clear boundaries, naming, no clever opacity, no drive-by), (c) faithfulness (no unrequested scope — Spec Kit `unrequested`). Premises: user lean; Osmani; Claude; converge gap types.
- `INFERENCE` [E4] Command-green alone is **necessary but not sufficient** for Toolbelt quality lean. Premises: §3.2 FACTs; Theme 7 deferred “optional light end check”.

### 3.3 Surface-shape options (for deep brief)

| Option | Shape | Pros | Cons |
|--------|-------|------|------|
| **A. Touchups only** | Strengthen Plan V1–V8 + Execute evidence/review steps in existing skills | Thinnest; matches “may be touchups” | Skills grow; weak discoverability of verify discipline |
| **B. Thin shared companion** | e.g. `implementation-verify` invoked from Plan (pre) and Execute (post/task) | One SoT for evidence gate + rubrics; broad-use | Extra skill to maintain |
| **C. Two companions** | `…-plan-validate` + `…-execute-verify` | Clear lane split | More surfaces; may overfit pocket sprawl |
| **D. Fat Quality pocket** | New pack with many review skills | Room for PR/TDD later | Conflicts with thin Toolbelt spirit **now** |

- `INFERENCE` [E4] Deep research should **compare A vs B** (C as fallback; **D deferred**). Lean entering deep: **B** (shared thin companion) *or* **A+light B** if companion stays &lt;1 skill and Plan/Execute stay orchestrators. Premises: packs stub; user quality lean; standalone spirit.
- `FACT` [E0] **Human lock 2026-07-30:** surface **C** — companions `implementation-plan-verify` + `implementation-execute-verify`; other D2–D30 leans accepted. See [`campaign-brief.md`](./campaign-brief.md) §0. Supersedes “prefer B” lean above for campaign constraints.

### 3.4 Analysis — third normal pass?

| Question | Verdict |
|----------|---------|
| Need more discovery before briefing deep? | **No** — pass 1+2 name tracks, surface options, and atom candidates |
| Remaining unknowns | Exact rubrics, when review is required vs opt-in, companion name, converge home — **deep-track** work |
| Third normal pass | **Skip** |

## 4. What deep research must cover (input to brief)

1. **T8A** — Plan validation gates (strengthen V1–V8 + coverage/falsifiable-verify/ambiguity)  
2. **T8B** — Execute verification gates (evidence iron law + post-green quality/readability/faithfulness review)  
3. **T8C** — Community deepen (verification-before-completion, validating-plans atoms, Spec Kit converge, BMAD review triage, Claude adversarial) → transferable vs park  
4. **T8D** — Surface decision (A/B/C) + elevation candidates + portable notes for later Debug/PR  

## 5. Implications

- `INFERENCE` [E4] Combine pass 1+2 into Theme 8 deep **campaign brief**; do not elevate from these drafts. Premises: `draft-is-not-sot`; user workflow.
