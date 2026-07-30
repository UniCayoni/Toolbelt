---
title: "T6 W2 GAP — Community plan-template grammar depth"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [t6-gap-community-gatherer]
depth: deep
wave: 2
slice: T6-GAP-COMMUNITY
aligned_with:
  - docs/research/notes/theme-6-plan/campaign-brief.md
  - docs/research/notes/theme-6-plan/t6d-w1-github-plan-skills-inventory.md
supersedes: null
---

# T6 W2 GAP — Community plan-template grammar depth

**Using `research-protocol`** · depth: **deep** · wave: **2** · slice: **T6-GAP-COMMUNITY**.

**Stars = discovery (E3), not acceptance.** No repo locked as Toolbelt SoT. TDD/git packaging not imported as Plan law.

## 1. Scope

- Question / goal: Deepen W1 community inventory with **primary file fetches** of Spec Kit, BMAD, validating-plans, and OpenSpec templates — extract exact section grammar, markers, gates, and conflict axes for Plan-pocket design later.
- In scope: Exact checklist/section grammar; `[P]`/`[USn]` rules; tests-optional stance; Always/Block If/Never + Code Map + HALT-on-gap; validating-plans check axes; OpenSpec artifact order thin confirm; conflict table (code-in-plan vs thin tasks vs compact intent-contract).
- Out of scope: Locking any system as Toolbelt SoT; importing Superpowers TDD/git/worktree as Plan law; elevating Design skills; execution skills as Plan SoT.
- Comprehension / research goal type: reuse (grammar atoms for later Plan pocket design).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | GitHub MCP `user-github` `get_file_contents`, `search_code`; WebFetch (attempted for validating-plans references — 404); local Read of W1 inventory + campaign brief |
| Corpora / URLs searched | github.com/github/spec-kit; bmad-code-org/BMAD-METHOD; majiayu000/claude-skill-registry (+ mirrors); Fission-AI/OpenSpec; obra/superpowers `writing-plans` (conflict arm); jmagar/claude-box (404 — claimed upstream in metadata) |
| Queries (exact) | Paths from W1 shortlist; code search `validating-plans Reality Check Verifier filename:SKILL.md`; `validating-plans-tdd-compliance`; directory list `skills/testing/validating-plans` |
| What was *not* searched | Spec Kitty deep templates; Discord/forum heat; Alexandria RAG; full BMAD real-project `epics.md` examples; OpenSpec non-default schemas; exhaustive Superpowers fork diffs |
| Depth | deep |
| Waves / stop_reason | Wave 2 GAP slice. `stop_reason`: **diminishing returns** — primary templates for all five targets fetched; validating-plans `references/*.md` absent from published registry (GAP logged); further fork mirrors are content-identical SKILL.md copies |
| Provenance (optional PROV) | Entity←GitHub primary blobs 2026-07-29; Activity=T6-GAP-COMMUNITY deepen; Agent=cursor-grok gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | W1 named exact paths; W2 corroborates by full primary read + grammar extraction |
| Scope boundary | Plan-*writing* / plan-*QA* artifacts only; apply/implement steps noted only to demarcate |

## 4. Findings

### 4.1 Spec Kit — plan + tasks grammar

#### Plan template sections (exact order)

From `templates/plan-template.md`:

1. Title: `# Implementation Plan: [FEATURE]`
2. Meta line: Branch / Date / Spec link; **Input** from `spec.md`
3. `## Summary`
4. `## Technical Context` — Language/Version, Primary Dependencies, Storage, Testing, Target Platform, Project Type, Performance Goals, Constraints, Scale/Scope (each may be `NEEDS CLARIFICATION`)
5. `## Constitution Check` — *GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*
6. `## Project Structure` — Documentation tree (`plan.md`, `research.md`, `data-model.md`, `quickstart.md`, `contracts/`, `tasks.md` *not* created by plan command) + Source Code tree + **Structure Decision**
7. `## Complexity Tracking` — fill ONLY if Constitution Check violations need justification (Violation / Why Needed / Simpler Alternative Rejected)

- `FACT` [E1] Spec Kit plan command ends after Phase 1 design artifacts (`research.md`, `data-model.md`, `contracts/`, `quickstart.md`); tasks are a separate handoff. Key rules: ERROR on gate failures or unresolved clarifications; quickstart must not include full implementation code. [E1: github/spec-kit `templates/commands/plan.md`, `templates/plan-template.md` — accessed 2026-07-29]

#### Tasks checklist grammar + `[P]` / `[USn]`

**Format (template + command agree):**

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

| Atom | Rule |
|------|------|
| Checkbox | ALWAYS `- [ ]` |
| Task ID | Sequential `T001`, `T002`, … in execution order |
| `[P]` | ONLY if parallelizable (different files, no deps on incomplete tasks) |
| `[Story]` / `[USn]` | REQUIRED for user-story phase tasks only: `[US1]`, `[US2]`, …; **forbidden** on Setup, Foundational, Polish |
| Description | Clear action + **exact file path** |

**Phase order:** Setup → Foundational (BLOCKS all stories) → one phase per user story (P1→Pn) → Polish & Cross-Cutting.

**Per story phase atoms:** Goal; **Independent Test**; optional Tests subsection; Implementation tasks; Checkpoint.

- `FACT` [E1] **Tests are OPTIONAL** — only include/generate test tasks if explicitly requested in the feature specification or user requests TDD; sample test tasks in template are illustrative. When tests *are* included: write FIRST and ensure FAIL before implementation. [E1: `templates/tasks-template.md` line “Tests are OPTIONAL”; `templates/commands/tasks.md` “Tests are OPTIONAL” — accessed 2026-07-29]
- `FACT` [E1] Tasks must be “immediately executable” — specific enough that an LLM can complete without additional context; commit-after-task noted in Notes (git packaging, not Plan SoT candidate). [E1: `templates/commands/tasks.md` Completion Report; `templates/tasks-template.md` Notes — accessed 2026-07-29]
- `FACT` [E1] Within-story order when tests present: Tests → Models → Services → Endpoints → Integration. [E1: `templates/commands/tasks.md` Phase Structure — accessed 2026-07-29]

### 4.2 BMAD — epics/stories + build-auto intent-contract

#### Epics template + story AC shape

`epics-template.md` sections: Overview → Requirements Inventory (FR / NFR / Additional / UX Design) → **FR Coverage Map** → Epic List → per Epic → per Story:

```text
### Story {N}.{M}: {title}
As a {user_type},
I want {capability},
So that {value_benefit}.

**Acceptance Criteria:**
**Given** {precondition}
**When** {action}
**Then** {expected_outcome}
**And** {additional_criteria}
```

- `FACT` [E1] Story creation step mandates: single-dev-agent completable; clear AC; **MUST NOT depend on future stories within the same epic**; create entities only when the story needs them; facilitator role (collaborative, not silent bulk generation). [E1: BMAD-METHOD `…/steps/step-03-create-stories.md` — accessed 2026-07-29]
- `FACT` [E1] AC guidelines: Given/When/Then; independently testable; include edge/error cases; reference requirements when applicable. [E1: same step file — accessed 2026-07-29]

#### build-auto `spec-template` — Always / Block If / Never + Code Map

`<intent-contract>` block:

| Tier | Meaning |
|------|---------|
| **Always** | Invariant rules |
| **Block If** | Decisions that cannot be made unattended — agent HALTs with status `blocked` if triggered |
| **Never** | Non-goals + forbidden approaches |

Plus: Intent (Problem / Approach); optional I/O & Edge-Case Matrix; **Code Map** (`FILE -- ROLE_OR_RELEVANCE`); **Tasks & Acceptance** (`FILE -- ACTION -- RATIONALE`; AC as Given/when/then); optional Design Notes; **Verification** commands with expected success criteria.

Target size: **900–1600 tokens**; `oversized` warning if larger; never over-specify “how”.

- `FACT` [E1] Plan step: if intent gaps (multiple defensible readings → observably different outcomes with nothing in intent to select), **do not fantasize / do not leave open questions** — **HALT** with status `blocked`, blocking condition `intent gap`, include unanswered questions + evidence. Ready-for-dev gate: status → `ready-for-dev` or HALT on failed standard (one repair attempt). [E1: `…/bmad-build-auto/step-02-plan.md`, `spec-template.md` — accessed 2026-07-29]
- `FACT` [E1] Code Map is where investigation lands so implementer need not re-search; prefer one task per file. [E1: step-02-plan.md + spec-template.md — accessed 2026-07-29]

### 4.3 validating-plans — what it checks; pocket home OPEN

**Clear W1 path (primary):** `majiayu000/claude-skill-registry` → `skills/testing/validating-plans/SKILL.md` (identical SHA also under `skills/data/validating-plans/`, `skills/testing/validating-plans-jmagar-claude-box/`). Metadata claims upstream `jmagar/claude-box` — that repo **404** on fetch 2026-07-29.

**Workflow position (skill’s own):** Brainstorm → Write-plan → **Validate-plan** → Execute-plan → Finish-branch (between Superpowers `writing-plans` and `executing-plans`).

**Three parallel validators (from SKILL.md; referenced `references/*.md` files not present in registry):**

| Agent | Stated checks |
|-------|----------------|
| TDD Compliance Auditor | Red-green-refactor order; test quality/naming; expected errors; anti-patterns (batching, implementation-first); Superpowers 5-step pattern (failing test → run fail → code → run pass → **commit**) |
| Reality Check Verifier | File existence + line numbers; package registry existence; API signatures/exports; imports; command availability |
| Drift Detector | Files changed after plan; uncommitted tree; dependency file updates; drift risk |

**Severity:** BLOCKER / CRITICAL / WARNING / NIT. Verdicts: PASS | PASS WITH NOTES | NEEDS REVISION. Todos fix **the plan**, not the code. Optional post-pass GitHub issue with labels `implementation-plan` + `validated`.

- `FACT` [E1] Skill description and process above from primary SKILL.md. [E1: majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — accessed 2026-07-29]
- `GAP` Paths `references/validating-plans-tdd-compliance.md`, `…-reality-check.md`, `…-drift-detection.md` are cited in SKILL.md but **not found** via directory get or raw.githubusercontent fetch (404). Searched: registry skill dir listing (only SKILL.md + metadata.json); WebFetch raw refs; code search only hits SKILL.md mirrors. Result: deep checklist bodies unavailable — use SKILL.md summaries only.
- `GAP` Claimed source repo `jmagar/claude-box` returns 404; fork path clarity limited to registry mirrors with identical content SHA.
- `OPEN` Plan-pocket vs Quality/Verify pocket home: skill is **plan QA** (anti-hallucination, TDD-in-plan compliance, drift) tightly coupled to Superpowers writing-plans/executing-plans + git issue packaging. Transferable atoms (reality-check file/API existence; severity gates) may belong Plan-adjacent; **TDD compliance + commit steps + gh issue** lean Verify/execution packaging — **do not lock pocket home from E3**.

### 4.4 OpenSpec — thin confirmation

- `FACT` [E1] Default schema artifact order: **proposal → specs → design → tasks**; `apply.requires: [tasks]`, tracks `tasks.md`. Tasks instruction: numbered `##` groups; each task `- [ ] X.Y description`; small enough for one session; dependency-ordered; resolve design Open Questions that would change build before writing tasks; each task verifiable. [E1: Fission-AI/OpenSpec `schemas/spec-driven/schema.yaml` — accessed 2026-07-29]
- `FACT` [E1] Tasks template is minimal:

```markdown
## 1. <!-- Task Group Name -->
- [ ] 1.1 <!-- Task description -->
- [ ] 1.2 <!-- Task description -->
```

[E1: `schemas/spec-driven/templates/tasks.md` — accessed 2026-07-29]

- `FACT` [E1] Specs forbid implementation detail; design is conditional (architecture/how); proposal is why/what. Aligns with W1; no new grammar beyond checkbox + numbered groups. [E1: schema.yaml instructions — accessed 2026-07-29]

### 4.5 Superpowers writing-plans (conflict arm only)

- `FACT` [E1] Task steps embed **full code snippets** in the plan; mandatory TDD 5-step (including **Commit** with `git add`/`git commit`); No Placeholders; Interfaces Consumes/Produces; File Structure before tasks; 2–5 minute steps. [E1: obra/superpowers `skills/writing-plans/SKILL.md` — accessed 2026-07-29]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Spec Kit `[P]`/`[USn]` + phase grammar is stable and mechanically parseable | confirmed (W2 E1) | tasks-template + commands/tasks.md |
| H2 | BMAD build-auto Always/Block If/Never is the compact alternative to code-in-plan | confirmed as *community pattern* | spec-template.md; not Toolbelt lock |
| H3 | validating-plans reference files exist in published registry | rejected | dir listing + 404 fetches |
| H4 | OpenSpec needs deep re-extract beyond W1 | revised | thin confirm sufficient; template is intentionally minimal |
| H5 | Community converges on one plan density | rejected | three conflicting densities (§6) |

## 6. Conflicts

| Topic | Source A | Source B | Source C (if any) | Resolution |
|-------|----------|----------|-------------------|------------|
| **Plan body density** | Superpowers: **code snippets in plan** + exact Run/Expected | Spec Kit / OpenSpec: **thin checkbox tasks** (paths/actions; no embedded impl code in task list; Spec Kit quickstart also forbids full impl code) | BMAD build-auto: **compact intent-contract** (~900–1600 tokens) + Code Map + `file -- action -- rationale` (boundaries, not how) | **CONFLICT** — leave OPEN for Toolbelt; no lock |
| **Tests in plan** | Superpowers: TDD steps in every task | Spec Kit: tests **optional** unless requested | OpenSpec: “verifiable” without mandating test tasks; BMAD: optional Verification section (delete if N/A) | **CONFLICT** / OPEN — do not import TDD as Plan law |
| **Git in plan** | Superpowers + validating-plans: commit steps / issue packaging | Spec Kit Notes: “Commit after each task” (soft) | BMAD: no commit ceremony in spec-template | **OPEN** — treat as execution packaging; campaign non-goal |
| **Halt vs invent** | BMAD: HALT on intent gap | Spec Kit: ERROR on unresolved NEEDS CLARIFICATION / unjustified gates | Superpowers: No Placeholders (fix by writing content, not HALT status machine) | Shared *anti-assumption* spirit; different control syntax — OPEN for Toolbelt gate shape |
| **validating-plans pocket** | Lives in Superpowers Plan→Execute chain (Plan-adjacent QA) | Category tag `testing` in registry; TDD auditor is Verify-flavored | — | **OPEN** Plan vs Quality pocket |

## 7. Gaps & OPEN

- `GAP` validating-plans `references/*.md` not published in registry mirrors; claimed `jmagar/claude-box` 404.
- `GAP` No live BMAD project `epics.md` example fetched this wave (template + step only).
- `OPEN` Which density Toolbelt Plan adopts (code-in-plan / thin tasks / intent-contract) — design decision later, not research lock.
- `OPEN` Nesting: Spec Kit story phases vs BMAD session-sized stories vs Superpowers 2–5 min steps.
- `OPEN` Whether Independent Test (Spec Kit) vs AC Given/When/Then (BMAD) vs Verification commands (build-auto) unify into one verify atom.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Extractable **grammar atoms** (structure only, not SoT): (1) checkbox + stable ID; (2) optional parallelism marker `[P]`; (3) story/trace label `[USn]`; (4) exact file paths; (5) phase/blocking foundation; (6) Independent Test or AC per increment; (7) NEEDS CLARIFICATION / HALT / No Placeholders anti-assumption; (8) Code Map / file map upfront; (9) Always/Block If/Never boundary tiers; (10) FR↔story/task coverage map; (11) optional post-write reality-check (files/APIs exist). Premises: §§4.1–4.4.
- `INFERENCE` [E4] Explicitly **exclude from Plan elevation**: mandatory TDD ceremony, git commit steps, GitHub issue creation, apply/implement skills. Premises: campaign brief non-goals; §4.2–4.3 packaging.
- `INFERENCE` [E4] Do not treat star rank or any single community template as Toolbelt SoT. Premises: draft-is-not-sot; stars=E3.

## 9. Source list (deduped)

1. https://github.com/github/spec-kit/blob/main/templates/plan-template.md
2. https://github.com/github/spec-kit/blob/main/templates/tasks-template.md
3. https://github.com/github/spec-kit/blob/main/templates/commands/plan.md
4. https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md
5. https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/templates/epics-template.md
6. https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/3-solutioning/bmad-create-epics-and-stories/steps/step-03-create-stories.md
7. https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-build-auto/step-02-plan.md
8. https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-build-auto/spec-template.md
9. https://github.com/majiayu000/claude-skill-registry/blob/main/skills/testing/validating-plans/SKILL.md (+ metadata.json; mirrors under skills/data/)
10. https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml
11. https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/templates/tasks.md
12. https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md (conflict arm)
13. Local W1: `docs/research/notes/theme-6-plan/t6d-w1-github-plan-skills-inventory.md`

---

## Return to parent (conflict + grammar atoms)

**Conflict (no lock):** Superpowers **code-in-plan + mandatory TDD/git steps** vs Spec Kit/OpenSpec **thin checkbox tasks** (tests optional in Spec Kit) vs BMAD build-auto **compact intent-contract** (Always/Block If/Never + Code Map + file--action--rationale, HALT-on-gap). validating-plans pocket home **OPEN** (Plan QA vs Quality/Verify); its TDD/commit/issue packaging must not become Plan law.

**Extractable grammar atoms:** `- [ ]` + ID; optional `[P]`; story label `[USn]`; exact paths; Setup→Foundational(block)→story phases→Polish; Independent Test / AC GWT; Constitution/ERROR or intent HALT; Code Map; Always/Block If/Never; FR coverage map; optional reality-check (files/packages/APIs); OpenSpec order proposal→specs→design→tasks with `- [ ] X.Y`.

**Out:** no community system as Toolbelt SoT; no TDD/git import as Plan law.
