---
title: "T7-W2-COMMUNITY — Gap fill: Spec Kit, BMAD review, verification-before-completion, OPENs"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7-w2-community-gatherer]
depth: deep
wave: 2
slice: T7-W2-COMMUNITY
aligned_with:
  - docs/research/notes/theme-7-execute/t7c-w1-community-execute-skills.md
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7-W2-COMMUNITY — Gap fill: Spec Kit, BMAD review, verification-before-completion, OPENs

**Using `research-protocol`**; depth: **deep**; wave: **2**; slice: **T7-W2-COMMUNITY**.

**Status:** `draft`. Not Execution SoT. Stars = E3 discovery only. **Standalone Toolbelt** — inspire/cut; no runtime dependency on Superpowers / OpenSpec / Spec Kit / BMAD. Do **not** elevate Toolbelt skills from this note. Park packaging (git / TDD / CLI / worktree / finish-branch / renderer).

## 1. Scope

- Question / goal: Close or harden named W1 residuals: Spec Kit `implement`/`converge` primary files; BMAD build-auto implement + `step-04-review` if present; Superpowers `verification-before-completion` full body; T7C OPENs (ledger path candidates; converge home; serial vs Plan parallel-safe — reaffirm Plan #2).
- In scope: Primary-file deep-reads; transferable atoms newly confirmed or hardened; OPEN candidates (not locks); residual GAPs.
- Out of scope: Elevating skills; locking ledger path or converge home as SoT; Spec Kit/BMAD packaging adoption; re-litigating Theme 6 #2; star re-counts; ECC/Karpathy.
- Comprehension / research goal type: reuse

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Local Read (Superpowers cache); GitHub MCP `get_file_contents` + `search_code`; Read Theme 6 accepted report + `plan-minimal.md` + T7C/T7D notes |
| Corpora / URLs searched | `github/spec-kit` (`templates/commands/implement.md`, `templates/commands/converge.md`, `presets/lean/commands/speckit.implement.md`); `bmad-code-org/BMAD-METHOD` (`bmad-build-auto/step-03-implement.md`, `step-04-review.md`, `workflow.md`); local Superpowers `verification-before-completion/SKILL.md` + SDD Durable Progress section; Theme 6 report elevation #2; `docs/templates/plan-minimal.md` |
| Queries (exact) | `repo:bmad-code-org/BMAD-METHOD step-04-review`; `repo:github/spec-kit filename:implement.md OR filename:converge.md`; paths listed above |
| What was *not* searched | Spec Kit lean `converge` (no lean converge file found in W1/W2 search set); BMAD interactive `bmad-build/step-04-review` body (auto path only — exists per search); live E0 Toolbelt execute trials; star re-measure; finishing/worktree/TDD full re-deep-read (park stance stands) |
| Depth | deep |
| Waves / stop_reason | Wave 2 slice T7-W2-COMMUNITY. Stop: named GAPs closed or hardened with primary E0/E1; ledger path left as **candidates** (no house lock without accept); diminishing returns on further Spec Kit hook/ignore-file detail |
| Provenance (optional PROV) | Entity←community primary skill/command texts + Theme 6 accepted Plan law; Activity=T7 W2 community GAP fill; Agent=t7-w2-community-gatherer (Grok) |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Named W1 GAP list; primary SoT files only; corroborate T7C without inventing conflict with Plan #2 |
| Scope boundary | Close listed residuals; park packaging; no elevation |

## 4. Findings

### 4.1 Spec Kit `implement` + `converge` — GAP **closed** (E1 primary)

#### Full `templates/commands/implement.md` [E1]

- `FACT` [E1] Command goal: execute the implementation plan by processing all tasks in `tasks.md`. Prerequisites via `{SCRIPT}` (`check-prerequisites` with `--require-tasks --include-tasks`). [E1: `github/spec-kit` `templates/commands/implement.md` — accessed 2026-07-30]
- `FACT` [E1] Preflight: optional checklist completeness gate — if any checklist incomplete, **STOP** and ask user yes/no before continuing (HITL before start, not per task). [E1: same]
- `FACT` [E1] Required load: `tasks.md` + `plan.md`; optional `data-model.md`, `contracts/`, `research.md`, `/memory/constitution.md`, `quickstart.md`. [E1: same]
- `FACT` [E1] Execute: phase-by-phase; respect sequential vs `[P]` parallel; “Follow TDD approach” (test tasks before corresponding impl); same-file tasks sequential; halt on non-parallel failure; mark completed `[X]`; completion validation vs spec/plan/tests; Done When checklist. [E1: same]
- `FACT` [E1] **Park packaging (not Toolbelt atoms):** ignore-file bootstrap by tech stack; `.specify/extensions.yml` before/after hooks with `EXECUTE_COMMAND`; prereq scripts. [E1: same]

#### Lean `presets/lean/commands/speckit.implement.md` [E1]

- `FACT` [E1] Lean loop: read `.specify/feature.json` → load constitution/spec/plan/tasks → execute in order → mark `- [x]` → halt on failure → validate matches spec. No checklist HITL, ignore bootstrap, or TDD mandate in lean body. [E1: `presets/lean/commands/speckit.implement.md` — accessed 2026-07-30]
- `INFERENCE` [E4] Lean form remains the closer Toolbelt-thin spine analogue; full form adds packaging + TDD + optional pre-start HITL. Premises: lean vs full bodies; T7C H3.

#### `templates/commands/converge.md` [E1]

- `FACT` [E1] Goal: close gap between spec/plan/tasks intent and **current codebase** (not git history); sole intent SoT = those artifacts + constitution; append remaining work as new tasks so implement can finish. Must run after implement (and after tasks produced). [E1: `templates/commands/converge.md` — accessed 2026-07-30]
- `FACT` [E1] Operating constraint: **append-only** `## Phase N: Convergence` on `tasks.md`; never rewrite existing tasks; never edit app code / spec / plan; if clean, leave `tasks.md` **byte-unchanged**. Gap types: `missing` / `partial` / `contradicts` / `unrequested`. Severity CRITICAL→LOW. Handoff: on append → re-run implement; on converged → recommend review/PR. [E1: same]
- `FACT` [E1] **Park packaging:** prereq scripts; before/after converge hooks. [E1: same]

**Transferable atoms hardened (Spec Kit):**

| Atom | Grade | Park |
|------|-------|------|
| Load plan+tasks (+ optional context) → ordered task loop → checkbox ledger → halt on fail → validate vs spec | E1 | FEATURE_DIR / `.specify` schema |
| Optional pre-start checklist HITL (full only) | E1 | Not per-task pause (§7.1) |
| `[P]` parallel marker + same-file serial rule | E1 | Align with Plan #2; don’t import TDD law |
| Converge: assess code vs intent; append-only gap tasks; re-implement | E1 | Hooks/scripts; not primary execute spine |

### 4.2 BMAD build-auto implement + `step-04-review` — GAP **closed** (E1; file exists)

- `FACT` [E1] Path exists: `src/bmm-skills/4-implementation/bmad-build-auto/step-04-review.md` (also referenced from `step-03-implement.md` NEXT and `step-01` resume routes). [E1: GitHub MCP `search_code` + `get_file_contents` 2026-07-30]

#### Implement (`step-03-implement.md`) — corroborate W1 [E1]

- `FACT` [E1] Precondition: missing `spec_file` → HALT `blocked` / `missing spec_file before implementation`. Capture `baseline_revision` (HEAD or `NO_VCS`) → status `in-progress` → synchronous implementer subagent with spec as sole SoT (handoff must not contradict spec) → run `## Verification` → optional matrix test audit → NEXT `step-04-review`. No human questions in implement step. [E1: `bmad-build-auto/step-03-implement.md` — accessed 2026-07-30]

#### Review (`step-04-review.md`) — new primary deep-read [E1]

- `FACT` [E1] Status → `in-review`; construct diff since `baseline_revision` (read-only; no `git add`); run review layers **in parallel** as several **blocking** same-turn awaits (never backgrounded — `workflow.md` Subagents). [E1: `step-04-review.md` + `workflow.md` — accessed 2026-07-30]
- `FACT` [E1] Triage categories (exactly one each): `intent_gap` \| `bad_spec` \| `patch` \| `defer` \| `reject`. Scope for defer/reject-as-OOS may come only from **intent**, not plan/diff shape alone. Cascading: intent_gap → HALT blocked + revert + save patch; bad_spec → amend outside intent-contract + KEEP notes + loopback to step-03 (max `review_loop_iteration` **5**, else HALT non-convergence); patch → auto-fix + re-verify; defer → frontmatter `deferred` list; reject → drop. [E1: `step-04-review.md`]
- `FACT` [E1] Finalize: write `## Auto Run Result`; optional followup-review score; VCS commit reviewed files + spec finalization → status `done` (or `NO_VCS` path). [E1: same]
- `FACT` [E1] **Park packaging:** mandatory subagents; local commit/finalization VCS ceremony; story/epic/`implementation_artifacts` paths; uv renderer (skill shell); review-layer template injection `{workflow.review_layers}`. [E1: `workflow.md`, `step-04-review.md`]

**Transferable atoms hardened (BMAD review):**

| Atom | Grade | Park |
|------|-------|------|
| Implement → verify commands → then review gate | E1 | — |
| Diff-scoped review with severity re-owned by controller | E1 | BMAD layer prompt files |
| Triage: intent_gap / bad_spec / patch / defer / reject | E1 | Enum as SoT; Toolbelt may map to Plan `intent-gap` / `verify-fail` / `needs-human` |
| Repair loop with iteration cap + non-convergence HALT | E1 | Cap=5 as BMAD-specific |
| Deferred findings list (portable later-review queue) | E1 | Frontmatter shape |

- `INFERENCE` [E4] BMAD step-04 is **post-implement review packaging** — high signal for later review/touchup + light Execute companion (triage vocabulary / repair-cap idea); **not** main execute spine. Premises: step order; T7D later-review lane; campaign §7.1 companion note.

### 4.3 Superpowers `verification-before-completion` — GAP **closed** (E0 full body)

Local cache path: `…/superpowers/…/skills/verification-before-completion/SKILL.md` (full body read 2026-07-30).

- `FACT` [E0] Iron law: **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**. If the verification command was not run in this message, cannot claim pass. [E0: SKILL.md]
- `FACT` [E0] Gate function: IDENTIFY command → RUN full fresh command → READ output/exit/failures → VERIFY claim vs output → ONLY THEN claim. Skip any step = “lying, not verifying.” [E0: same]
- `FACT` [E0] Common-failure table: tests/linter/build/bug-fix/regression/agent-done/requirements each require specific evidence; prior runs, “should pass,” agent reports, partial checks are insufficient. [E0: same]
- `FACT` [E0] Red flags: “should/probably/seems”; satisfaction before verify; commit/PR without verify; trust agent reports; partial verification; wording that implies success without having run verification. [E0: same]
- `FACT` [E0] When to apply: before any success/completion/satisfaction language; before commit/PR/task completion; before moving to next task; before delegating. Applies to paraphrases/implications, not only exact phrases. [E0: same]
- `FACT` [E0] Agent-delegation pattern: agent reports success → check VCS diff → verify changes → report actual state (do not trust report alone). Requirements pattern: re-read plan → checklist → verify each → report gaps or completion. [E0: same]
- `CLAIM` [E3] Skill cites “24 failure memories” narrative — community process lore; not Toolbelt SoT. [E3: SKILL.md “Why This Matters”]
- `INFERENCE` [E4] Highest-value Toolbelt companion/spine atom: evidence-before-`done` / before next task — map to Plan Done-when + status vocab; park TDD red-green-as-law and commit/PR packaging hooks. Premises: E0 body; Theme 6 #3–#4 verify required / TDD optional; campaign park git packaging.

### 4.4 T7C OPENs — hardened (not elevated)

#### OPEN — Ledger path candidates (not locked)

Community + house observations:

| Candidate | Source | Notes |
|-----------|--------|-------|
| **A. Plan artifact checkboxes / task Status fields** in Theme 6 house plan | OpenSpec/Spec Kit checkbox pattern [E1]; `docs/plans/YYYY-MM-DD-<slug>-plan.md` + `plan-minimal` task Status [E0] | Primary ledger for single-session / cold execute; aligns Plan status vocab |
| **B. Same plan file as resume map** (task `in_progress`/`done`/`blocked`) | Theme 6 status vocab [E0]; T7A/T7D framing | Prefer updating plan over chat-only todos |
| **C. Optional sidecar progress ledger** (Toolbelt-native name TBD) for multi-subagent / compaction resume | SDD durable ledger atom [E0/E3] | Inspire atom; **do not** adopt `.superpowers/sdd/progress.md` |
| **Park** `.superpowers/sdd/progress.md` + git-ignored scratch scripts | SDD Durable Progress [E0] | Product path |

- `INFERENCE` [E4] **Candidate ranking for later design (not SoT):** Prefer **A+B** (status in `docs/plans/…` plan) as default; add **C** only if subagent controller needs compaction-proof resume beyond plan checkboxes. Exact filename for C remains OPEN until elevate. Premises: Theme 6 house path #7; SDD ledger purpose; standalone (no `.superpowers`).

#### OPEN — Converge home (Execute vs later review) — hardened

- `FACT` [E1] Spec Kit converge is post-implement gap assessment + append-only tasks; handoff on clean = “proceed to review / opening a PR.” [E1: converge.md]
- `FACT` [E0] T7D pins fuller “what exists / keep / change” and deep review inventory to **later review/debug** (pocket or touchups); Execute owns light verify + optional fresh task reviewer only. [E0: `t7d-w1-boundaries-elevation.md` §4.2]
- `INFERENCE` [E4] **Hardened stance:** Converge-style pass is **not** main Execute spine. Prefer **later review/touchup** home; allow as **optional Execute supplement** only after a first implement pass when the plan/tasks ledger needs append-only gap tasks. Do not require converge every execution. Premises: converge goal; T7C H4; T7D later-review lane; campaign essence (drive approved plans).

#### OPEN — Serial vs Plan parallel-safe — **reaffirm Plan #2** (no invent conflict)

- `FACT` [E0] Theme 6 **accepted #2**: `serial_implement_review` default for shared-checkout coding; parallel only when independence + exclusive file ownership (or worktrees) are stated in the plan. [E0: `docs/research/reports/theme-6-plan-pocket.md` elevation #2]
- `FACT` [E0] `plan-minimal.md`: Parallel-safe only `yes` if independence + exclusive writes or worktree stated; Execution notes repeat serial default. [E0: `docs/templates/plan-minimal.md`]
- `FACT` [E0] Superpowers SDD: never dispatch multiple **implementation** subagents in parallel (community process). [E0: SDD SKILL.md — inventory]
- `FACT` [E1] Spec Kit full implement allows `[P]` parallel when marked; same-file tasks sequential. [E1: implement.md]
- `INFERENCE` [E4] **Reaffirm — no conflict invented:** Toolbelt Execute **enforces Plan #2** at runtime. Superpowers absolute ban and Spec Kit `[P]` are inventory/packaging variants; neither overrides accepted Plan law. Default serial writers; parallel writers only when the plan marks parallel-safe with independence + exclusive writes/worktrees. Premises: Theme 6 #2 [E0]; T7B §4.3; campaign T7B track; T7C conflict table.

### 4.5 Cross-slice synthesis (W2)

- `INFERENCE` [E4] W2 corroborates T7C cluster without new spine atoms beyond: (1) verification-before-completion detail for light companion; (2) BMAD review triage/repair-cap as later-review portable notes; (3) Spec Kit converge append contract details for optional supplement. Premises: §§4.1–4.4.
- `CLAIM` [E3] Stars unused this pass; method from E0/E1 bodies only. [E3: protocol]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Spec Kit implement/converge primary files close W1 GAP with lean=thin / converge=supplement | confirmed | §4.1 |
| H2 | BMAD `step-04-review.md` exists and is review packaging, not execute spine | confirmed | §4.2 |
| H3 | verification-before-completion full body is high-value evidence-before-done companion | confirmed | §4.3 |
| H4 | Ledger should be Toolbelt-native under/near `docs/plans/`, not `.superpowers` | confirmed as candidate ranking | §4.4 |
| H5 | Converge belongs in Execute core | rejected (spine); optional supplement / later review | §4.4 |
| H6 | Serial policy should invent conflict with Plan #2 | rejected | §4.4 reaffirm |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Parallel writers | SDD never-parallel [E0/E3]; Spec Kit `[P]` [E1] | Theme 6 Plan #2 scoped parallel-safe [E0] | **Prefer Plan #2** (accepted). No new Execute absolute ban or unconstrained parallel |
| Review home | BMAD step-04 rich repair loop [E1]; Spec Kit converge→PR [E1] | T7D light verify in Execute / fuller later [E0] | Light evidence-verify in Execute; BMAD triage + converge → later review or optional supplement |
| Ledger path | SDD `.superpowers/sdd/progress.md` [E0] | Theme 6 `docs/plans/` [E0] | Candidates A/B default; C optional sidecar; park SP path |
| HITL | Spec Kit checklist before implement [E1] | §7.1 escalate on blocked/major deviation only [E0] | Optional preflight ≠ per-task pause |

## 7. Gaps & OPEN

### Closed this pass

- Spec Kit `implement.md` + lean implement + `converge.md` primary deep-read
- BMAD `bmad-build-auto/step-04-review.md` exists + full body; step-03 corroboration
- Superpowers `verification-before-completion` full body (local E0)

### Remaining GAP / OPEN (integrator)

- `GAP` Spec Kit lean converge (if any) — not found in searched paths; full converge stands. Searched: lean `speckit.implement.md` + templates `converge.md`. Result: no lean converge in this pass.
- `GAP` BMAD interactive `bmad-build/step-04-review.md` body not deep-read (auto path closed; interactive may differ on HITL). Residual low priority unless integrator needs human-in-loop BMAD.
- `GAP` Park nuance: SP finishing/worktree/TDD full bodies still unlisted (W1 park stance stands; not P0 for Execute atoms).
- `OPEN` Exact Toolbelt sidecar ledger filename/path **if** C is adopted (candidates only in §4.4).
- `OPEN` Whether converge-style supplement ships with Execute elevate or waits for later review effort (stance hardened; product choice deferred).
- `OPEN` How much of BMAD triage enum maps 1:1 into Plan blocked reasons vs later-review vocabulary (portable note only).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] **Do not elevate** skills; **do not** lock community repos or ledger path from this draft. Premises: draft-is-not-sot; campaign non-goals.
- `INFERENCE` [E4] Integrator can treat Spec Kit / BMAD-review / verification-before-completion W1 GAPs as **closed** for T7C deepen; residual is packaging park + non-P0 interactive BMAD / lean-converge absence. Premises: §§4.1–4.3, §7.
- `INFERENCE` [E4] Serial/parallel wording for Execute skills should cite **Theme 6 accepted #2**, not Superpowers red-flag absolute. Premises: §4.4.

## 9. Source list (deduped)

1. `github/spec-kit` `templates/commands/implement.md` [E1]
2. `github/spec-kit` `presets/lean/commands/speckit.implement.md` [E1]
3. `github/spec-kit` `templates/commands/converge.md` [E1]
4. `bmad-code-org/BMAD-METHOD` `src/bmm-skills/4-implementation/bmad-build-auto/step-03-implement.md` [E1]
5. `bmad-code-org/BMAD-METHOD` `…/bmad-build-auto/step-04-review.md` [E1]
6. `bmad-code-org/BMAD-METHOD` `…/bmad-build-auto/workflow.md` [E1]
7. Local Superpowers `verification-before-completion/SKILL.md` [E0]
8. Local Superpowers `subagent-driven-development/SKILL.md` §Durable Progress [E0]
9. `docs/research/reports/theme-6-plan-pocket.md` elevation #2 [E0]
10. `docs/templates/plan-minimal.md` [E0]
11. `t7c-w1-community-execute-skills.md`; `t7d-w1-boundaries-elevation.md`; `campaign-brief.md` §7.1 [E0 framing]

---

## Return to parent

### Atoms added / hardened this pass

1. **Evidence-before-completion gate** (identify→run→read→verify→claim) — companion/spine light atom from full SP verification skill  
2. **Spec Kit lean execute loop** corroborated (load→serial tasks→checkbox→halt→validate)  
3. **Spec Kit converge contract** hardened (append-only Convergence phase; gap types; no code edits; re-implement handoff)  
4. **BMAD review triage** (`intent_gap` / `bad_spec` / `patch` / `defer` / `reject`) + repair-loop cap + deferred list — later-review portable  
5. **Ledger candidates** A/B (`docs/plans/…` status/checkboxes) > optional C sidecar; park `.superpowers/sdd/`  
6. **Converge home:** later review/touchup preferred; optional Execute supplement after first pass — not spine  
7. **Serial/parallel:** reaffirm Plan #2 only — no Superpowers absolute ban as Toolbelt law  

### Park (unchanged)

worktrees-required · finishing-branch · commit-every-task law · mandatory TDD · OpenSpec/BMAD/Spec Kit CLI-renderer-hooks-ignore bootstrap · `.superpowers` paths · stars-as-acceptance  

### Remaining GAPs

- Lean Spec Kit converge (absent in search)  
- Interactive BMAD `bmad-build` step-04 (optional)  
- Exact sidecar ledger filename if C adopted  
- Converge ship-with-Execute vs later-review product choice (stance only)  
- BMAD triage ↔ Plan blocked-reason mapping detail  

**Out:** elevation; locking community SoT; inventing conflict with Plan #2.
