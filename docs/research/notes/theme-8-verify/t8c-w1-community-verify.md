---
title: "Theme 8 Wave 1 T8C — Community / vendor verify deepen"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8c-w1-gatherer]
depth: deep
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/scope-normal-pass3-github-web.md
  - docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md
  - docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md
supersedes: null
---

# Theme 8 Wave 1 T8C — Community / vendor verify deepen

**Using `research-protocol`**. Identity: Theme 8 = Plan/Execute **verification extensions**, not Debug/PR pocket. Inventory transferable atoms; park CLI/product coupling.

**Status:** `draft`. Not Verify SoT. Respects campaign-brief §0 parks (D22–D27).

---

## 1. Scope

- Question / goal: Deep-read Tier A verify/validate surfaces; produce graded transferable-vs-park table for `implementation-plan-verify` (T8A) and `implementation-execute-verify` (T8B); confirm G9 (validating-plans refs 404).
- In scope: Primary SKILL/command bodies listed in pass-3 Tier A + spot-checks; Theme 6 notes that mention validating-plans.
- Out of scope: Designing Debug/PR pocket; elevating skills; locking OpenSpec/Spec Kit/Superpowers as runtime deps; writing T8A/T8B notes; live E0 Toolbelt trials.

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (research-protocol, note template, campaign-brief §0 + T8C, pass-3, Theme 6 validating-plans notes); `gh api` Accept `application/vnd.github.raw` for primary files; `gh api` contents listing + raw HEAD probes for G9; PowerShell `Invoke-WebRequest` HEAD for raw.githubusercontent refs |
| Corpora / URLs searched / accessed | See §9 Source list — all paths fetched 2026-07-30 unless noted |
| Queries (exact) | `gh api -H "Accept: application/vnd.github.raw" repos/obra/superpowers/contents/skills/verification-before-completion/SKILL.md`; same pattern for `requesting-code-review/SKILL.md` + `code-reviewer.md`; `repos/majiayu000/claude-skill-registry/contents/skills/testing/validating-plans/SKILL.md`; `repos/majiayu000/claude-skill-registry/contents/skills/testing/validating-plans` (dir list); `…/validating-plans/references` (expect 404); raw HEAD `https://raw.githubusercontent.com/majiayu000/claude-skill-registry/main/skills/testing/validating-plans/references/validating-plans-{tdd-compliance,reality-check,drift-detection}.md`; Spec Kit `templates/commands/{converge,analyze,checklist}.md`; OpenSpec `skills/openspec-verify-change/SKILL.md`; tree search `rube-de/cc-skills` → `plugins/council/skills/review-plan/SKILL.md`; `kdcokenny/opencode-workspace` → `src/skills/plan-review/SKILL.md`; `mab-go/trello-mcp` → `.agents/skills/review-plan/SKILL.md`; `sambeau/kanbanzai` → `.kbz/skills/validate-plan/SKILL.md` (+ `references/examples.md` subset) |
| What was *not* searched | Exhaustive Superpowers fork tree; Copilot PR-skills product docs body; rune-kit converge full file; OpenSpec CLI binary behavior E0; Spec Kit extension-hook runtime; kanbanzai plan-validator-rubrics.md full body; Discord heat |
| Depth | deep |
| Waves / stop_reason | Wave 1 T8C slice. `stop_reason`: **wave1_slice_coverage** — all MUST deep-reads + spot-checks completed; G9 re-confirmed; further mirrors are content-identical |
| Provenance (optional PROV) | Entity←Tier A GitHub primaries + Theme 6 E0 notes; Activity=T8C W1 gather; Agent=t8c-w1-gatherer / gh api |

---

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (Tier A MUST list) + as-needed spot-check |
| Why this mode | Campaign T8C requires full bodies for grammar/atoms; spot-checks only for actionability/taxonomy/D-check subset |
| Scope boundary | Plan-validate + execute-verify atoms; park Debug/PR, CLI deps, council ceremony, TDD auditor as law |

---

## 4. Findings

### 4.1 Transferable vs park (master table)

| Surface | Transferable atoms | Park | Grade |
|---------|-------------------|------|-------|
| **obra/superpowers `verification-before-completion`** | Iron law: no completion claim without fresh evidence; gate **IDENTIFY → RUN → READ → VERIFY**; reject “should/probably/seems”; requirements checklist ≠ tests-only; agent success → verify via VCS/diff independently | TDD red-green ceremony as mandatory pattern; commit/PR as always-apply triggers | `FACT` [E1] |
| **obra/superpowers `requesting-code-review` (+ `code-reviewer.md`)** | Fresh reviewer subagent with **plan/requirements + change range**; never coordinator session history; severity Critical / Important / Minor; fix Critical+Important before proceed; plan-alignment + code quality + readability dimensions in template | Git SHA ceremony as SoT (BASE/HEAD as *required* ritual); merge-to-main packaging; “after each task” as absolute law without Toolbelt non-trivial threshold | `FACT` [E1] |
| **majiayu000 `validating-plans`** | Phase between write-plan and execute; **parallel** Reality Check + Drift (+ park TDD); severity BLOCKER/CRITICAL/WARNING/NIT; verdicts PASS / PASS WITH NOTES / NEEDS REVISION; todos fix **the plan** not code; Reality checks: files/packages/APIs/imports/commands; Drift: tree/deps staleness | TDD Compliance Auditor as Plan law; Superpowers path coupling; gh issue labels packaging; organization-note edit ritual; deep `references/*.md` bodies (**unavailable** — G9) | `FACT` [E1] SKILL.md; `GAP` refs |
| **rube-de/cc-skills `review-plan`** | **Codebase verification table** before opinionated review: paths (modify vs create), line numbers, API signatures, relative imports/exports, duplicate work, existing tests; CRITICAL fail-fast present to user before proceeding; severity Critical/Warning/Note; verdict Ready / Needs revision / Needs discussion | Multi-consultant **council** (gemini+codex) ceremony; secret-scan→external model send; Superpowers/cdt path coupling | `FACT` [E1] |
| **github/spec-kit `converge.md`** | Post-implement intent coverage vs spec/plan/tasks; gap types **missing / partial / contradicts / unrequested**; append-only Convergence phase on tasks; **no** silent rewrite of spec/plan; **no** code edits in converge; constitution MUST → highest severity; present findings before write | Spec Kit CLI/scripts/hooks/FEATURE_DIR packaging; constitution path coupling | `FACT` [E1] |
| **github/spec-kit `analyze.md`** | Pre-implement **read-only** cross-artifact consistency; detection: duplication, ambiguity (vague adjectives, placeholders), underspecification, coverage gaps (req↔task), inconsistency/ordering; severity CRITICAL→LOW; coverage summary table; do not auto-edit | Spec Kit packaging/hooks; constitution as non-negotiable Toolbelt import | `FACT` [E1] |
| **github/spec-kit `checklist.md`** | “Unit tests for English” — validate **requirements quality** (completeness/clarity/consistency/measurability/coverage), **not** implementation behavior; question-form items; Gap/Ambiguity markers | Spec Kit checklist file generation ceremony; PR-audience defaults; full domain checklist factories | `FACT` [E1] |
| **Fission-AI/OpenSpec `openspec-verify-change`** | Three dimensions: **Completeness** (tasks + req coverage), **Correctness** (impl vs req/scenario), **Coherence** (design adherence + pattern consistency); issue tiers CRITICAL / WARNING / SUGGESTION; prefer lower severity when uncertain; every issue actionable; graceful degradation by available artifacts | OpenSpec CLI (`openspec status/instructions/store`) as runtime dependency | `FACT` [E1] |
| **kdcokenny `plan-review`** (spot) | Rubric: Completeness + **Actionability** (specific files; no vague “investigate/make it work”; clear deps); severity Critical→Nitpick; APPROVE / REQUEST_CHANGES / NEEDS_DISCUSSION | Citation-house rules (`ref:delegation-id`); `plan_save` structural pre-validation product coupling | `FACT` [E1] |
| **mab-go/trello-mcp `review-plan`** (spot) | Accuracy/correctness/clarity verification procedures; task taxonomy: **incomplete / composite / ambiguous / trivial / misordered / coverage gap**; do not edit until user approve | Product follow-ons (`/verify-changes`); AGENTS.md product conventions | `FACT` [E1] |
| **sambeau/kanbanzai `validate-plan`** (spot subset) | Light subset: **D3/D4** task↔REQ bi-coverage; **D5** scope drift; **D6** acyclic deps + topological sort; **D9** AC→producing task; **D13** actionability (deliverable + inputs + done criterion); verdicts pass / pass_with_notes / fail; anti-pattern “phantom traceability” / “hallucinated completeness” | Full **D1–D13** catalog as Toolbelt law; 50-word task minimum; kanbanzai doc-store/register ceremony; 5-tool-call budget; product rubrics path | `FACT` [E1] |

### 4.2 Claim bullets (cite-or-omit)

- `FACT` [E1] Superpowers verification-before-completion states: “NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE” and the five-step gate IDENTIFY/RUN/READ/VERIFY/ONLY THEN; “Requirements met” requires line-by-line checklist, not tests passing alone. [E1: obra/superpowers `skills/verification-before-completion/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] requesting-code-review mandates dispatching a reviewer subagent with crafted context (description, plan/requirements, BASE/HEAD SHAs), never session history; act on Critical immediately and Important before proceeding. [E1: obra/superpowers `skills/requesting-code-review/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] code-reviewer template checks plan alignment, code quality (incl. separation/error handling), architecture, testing, production readiness; issues Critical/Important/Minor; read-only on checkout. [E1: obra/superpowers `skills/requesting-code-review/code-reviewer.md` — accessed 2026-07-30]
- `FACT` [E1] validating-plans workflow position: Write-plan → **Validate-plan** → Execute-plan; launches 3 parallel agents (TDD / Reality / Drift); severity BLOCKER–NIT; verdicts PASS | PASS WITH NOTES | NEEDS REVISION; “TodoWrite creates todos to FIX THE PLAN, not to fix the problems the plan would create.” [E1: majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — accessed 2026-07-30]
- `FACT` [E0/E1] **G9 confirmed:** published skill dir contains only `SKILL.md` + `metadata.json`; `contents/…/references` → HTTP 404; raw HEAD for `validating-plans-tdd-compliance.md`, `…-reality-check.md`, `…-drift-detection.md` all 404. Theme 6 W2/W3 GAP retained and re-verified. [E0: gh api dir list + 404 responses 2026-07-30] [E1: SKILL.md cites those ref paths]
- `FACT` [E1] Spec Kit converge: sole write = append `## Phase N: Convergence` tasks; gap types missing/partial/contradicts/unrequested; must not modify spec/plan or application code; if clean, leave tasks.md byte-for-byte unchanged. [E1: github/spec-kit `templates/commands/converge.md` — accessed 2026-07-30]
- `FACT` [E1] Spec Kit analyze: STRICTLY READ-ONLY; detection passes include Ambiguity, Underspecification, Coverage Gaps, Inconsistency; CRITICAL if constitution MUST conflict or zero-coverage core req. [E1: github/spec-kit `templates/commands/analyze.md` — accessed 2026-07-30]
- `FACT` [E1] Spec Kit checklist purpose: “UNIT TESTS FOR REQUIREMENTS WRITING” — not implementation verification; items must ask whether requirements are complete/clear/consistent/measurable. [E1: github/spec-kit `templates/commands/checklist.md` — accessed 2026-07-30]
- `FACT` [E1] OpenSpec verify-change builds Completeness / Correctness / Coherence report with CRITICAL/WARNING/SUGGESTION; Completeness focuses objective checkboxes; Coherence looks for design adherence + pattern consistency (not nitpick style); CLI required (`compatibility: Requires openspec CLI`). [E1: Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] rube-de review-plan Step 2 verification table covers file paths, line numbers, API signatures, relative imports, duplicate work, test files; CRITICAL failures presented before launching consultants; verdict logic maps Critical→Needs revision. [E1: rube-de/cc-skills `plugins/council/skills/review-plan/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] kdcokenny plan-review Actionability: tasks must name file/component; avoid “investigate” without scope; Completeness wants specific measurable goals. [E1: kdcokenny/opencode-workspace `src/skills/plan-review/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] mab-go review-plan task taxonomy: Incomplete, Composite, Ambiguous, Trivial, Misordered, Coverage gap; “Do not edit the plan yet” until approval. [E1: mab-go/trello-mcp `.agents/skills/review-plan/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] kanbanzai validate-plan defines D1–D13; blocking include D3/D4/D5/D6/D9/D13; D6 is topological-sort cycle detection; verdicts pass | pass_with_notes | fail; anti-patterns include Phantom Traceability and Hallucinated Completeness. [E1: sambeau/kanbanzai `.kbz/skills/validate-plan/SKILL.md` — accessed 2026-07-30]
- `FACT` [E0] Theme 6 already extracted validating-plans atoms as V4/V5 reality/drift and logged refs 404; pocket home was OPEN — campaign-brief §0 now places plan-validate in Theme 8 companion (D1=C). [E0: `docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md`, `t6-w3-plus1-residual.md`, `campaign-brief.md` — accessed 2026-07-30]
- `INFERENCE` [E4] Community method atoms strongly corroborate §0 D5–D18 without requiring any vendor runtime. Premises: (1) §4.1 table E1 facts; (2) campaign-brief parks D22–D27.
- `INFERENCE` [E4] Two verify problems remain distinct: plan-validate (reality/drift/coverage/actionability) vs execute-verify (evidence + fresh quality review + converge intent). Premises: pass-3 cross-cuts; deep-reads above.

### 4.3 Cross-cutting insights for T8A / T8B (do not write their notes)

**For T8A (`implementation-plan-verify`):**

1. Parallel Reality + Drift + coverage/actionability matches D6; park TDD auditor (D22) — SKILL.md Phase-1 TDD checks are summary-only under G9.
2. Steal Spec Kit **analyze** grammar (ambiguity, coverage table, read-only report) and **checklist** “unit tests for English” lightly — not Spec Kit runtime (D13/D23).
3. Adopt rube-de **verification table** columns for non-trivial plans (D12); park consultant council (D26).
4. Light task taxonomy from trello-mcp + actionability from kdcokenny + light kanbanzai D3/D4/D6/D9/D13 — park heavy D1–D13 and 50-word rule (D10).
5. Verdict language PASS / PASS WITH NOTES / NEEDS REVISION + fix-plan-not-code is primary E1 from validating-plans (D7–D8).

**For T8B (`implementation-execute-verify`):**

1. Evidence iron law from verification-before-completion is the spine for D14 (IDENTIFY→RUN→READ→VERIFY).
2. Fresh-context review from requesting-code-review + OpenSpec Completeness/Correctness/Coherence labels (D15–D17) — park SHA ceremony as SoT (D25) and OpenSpec CLI (D23).
3. Converge gap taxonomy incl. **unrequested** + append-only tasks + no code edits (D18/G12) — park Spec Kit packaging.
4. Keep split: signal verify (“builds?”) vs intent coverage (“promised?”) — reinforced by converge operating constraints vs verification-before-completion.

**Shared parks (coordinator):** Copilot PR-skills / Debug-PR; Superpowers mirrors; TDD auditor as law; multi-consultant council ceremony; OpenSpec/Spec Kit/Superpowers runtime deps; git SHA ceremony as SoT.

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | validating-plans `references/*.md` still unpublished (G9) | **confirmed** | dir list + 3× raw 404 [E0/E1] |
| H2 | Codebase verification table is separable from council ceremony | **confirmed** | rube-de Step 2 before Step 3 [E1] |
| H3 | OpenSpec three dimensions usable as labels without CLI | **confirmed** as method atom | SKILL.md dimensions + explicit CLI park [E1] |
| H4 | Full kanbanzai D1–D13 is overfit for Toolbelt light taxonomy | **confirmed** lean | D10 parks heavy catalog; subset D3/D4/D5/D6/D9/D13 transferable [E1+E4] |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Fresh review timing | Superpowers: after each task + before merge [E1] | Campaign D15: required for non-trivial + EOP; optional trivial | Prefer campaign D15 threshold; steal fresh-context atom only |
| Plan QA severity labels | validating-plans BLOCKER/CRITICAL/WARNING/NIT [E1] | rube-de Critical/Warning/Note; OpenSpec CRITICAL/WARNING/SUGGESTION | Steal **verdicts** PASS/PASS WITH NOTES/NEEDS REVISION for plan; map execute issues to Theme 7 WARNING/NIT + OpenSpec labels — no lock this note |
| TDD-in-plan | validating-plans Agent 1 + Superpowers 5-step [E1] | Campaign D22 park; Spec Kit tests optional (Theme 6) | Park TDD auditor as law; keep falsifiable Done-when elsewhere |
| validating-plans pocket home | Theme 6 OPEN Plan vs Verify [E0] | Campaign D1=C companions | Brief constraint for deep: plan-validate → `implementation-plan-verify` |

---

## 7. Gaps & OPEN

- `GAP` G9 deep checklist bodies remain unpublished — use SKILL.md Phase 1–3 summaries only.
- `OPEN` Exact Toolbelt rubric wording (G1), non-trivial threshold (G2), skill description triggers (G3) — T8A/T8B/T8D.
- `OPEN` Whether checklist-style “unit tests for English” lives inside plan-verify or stays Plan V-checks — T8A/T8D.
- `GAP` kanbanzai `plan-validator-rubrics.md` not deep-read (spot subset only) — optional W2 if D13 wording contested.
- `GAP` Copilot PR-skills body not deep-read — correctly parked for Debug/PR.

---

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T8C deep-read **sufficient** for Wave 1 atom feed to T8A/T8B; no additional Tier A bodies required before W2 corroboration. Premises: MUST list complete; spot-checks add taxonomy without new spines.
- `INFERENCE` [E4] Do not elevate any vendor skill; extract atoms into Toolbelt companions only after report accept. Premises: `draft-is-not-sot`; D23.
- `INFERENCE` [E4] Ranked transferable atoms for coordinator merge — see return block below.

---

## 9. Source list (deduped)

1. https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md — accessed 2026-07-30 [E1]
2. https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md — accessed 2026-07-30 [E1]
3. https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/code-reviewer.md — accessed 2026-07-30 [E1]
4. https://github.com/majiayu000/claude-skill-registry/blob/main/skills/testing/validating-plans/SKILL.md — accessed 2026-07-30 [E1]
5. majiayu000 validating-plans dir list + `references/` 404 + raw refs 404 — accessed 2026-07-30 [E0]
6. https://github.com/github/spec-kit/blob/main/templates/commands/converge.md — accessed 2026-07-30 [E1]
7. https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md — accessed 2026-07-30 [E1]
8. https://github.com/github/spec-kit/blob/main/templates/commands/checklist.md — accessed 2026-07-30 [E1]
9. https://github.com/Fission-AI/OpenSpec/blob/main/skills/openspec-verify-change/SKILL.md — accessed 2026-07-30 [E1]
10. https://github.com/rube-de/cc-skills/blob/main/plugins/council/skills/review-plan/SKILL.md — accessed 2026-07-30 [E1]
11. https://github.com/kdcokenny/opencode-workspace/blob/main/src/skills/plan-review/SKILL.md — accessed 2026-07-30 [E1]
12. https://github.com/mab-go/trello-mcp/blob/main/.agents/skills/review-plan/SKILL.md — accessed 2026-07-30 [E1]
13. https://github.com/sambeau/kanbanzai/blob/main/.kbz/skills/validate-plan/SKILL.md — accessed 2026-07-30 [E1]
14. https://github.com/sambeau/kanbanzai/blob/main/.kbz/skills/validate-plan/references/examples.md — spot 2026-07-30 [E1]
15. `docs/research/notes/theme-6-plan/t6-w2-gap-community-templates.md` — accessed 2026-07-30 [E0]
16. `docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md` — accessed 2026-07-30 [E0]
17. `docs/research/notes/theme-8-verify/campaign-brief.md` + `scope-normal-pass3-github-web.md` — accessed 2026-07-30 [E0]

---

## 10. Return to coordinator (short)

### Ranked transferable atoms

1. Evidence iron law IDENTIFY→RUN→READ→VERIFY + ban “should/looks” (T8B / D14)
2. Parallel Reality + Drift + severity/verdicts + fix-plan-not-code (T8A / D5–D8)
3. Codebase verification table (paths/APIs/imports/dupes) for non-trivial plans (T8A / D12)
4. Converge gap taxonomy missing/partial/contradicts/**unrequested** + append-only tasks (T8B / D18)
5. Spec Kit analyze grammar: ambiguity + FR↔task coverage + read-only (T8A / D9–D11, D13)
6. OpenSpec Completeness / Correctness / Coherence labels (T8B / D17)
7. Fresh-context reviewer (plan + diff), Critical/Important/Minor triage (T8B / D15–D16)
8. Light task taxonomy: incomplete/composite/ambiguous/misordered/coverage-gap + actionability (T8A / D10)
9. Light structural: bi-coverage + acyclic deps + AC→task (kanbanzai D3/D4/D6/D9 subset) (T8A / D11)
10. Checklist “unit tests for English” (requirements quality, not impl tests) (T8A light)

### Parks (respect §0)

- TDD auditor as Plan law (D22)
- OpenSpec / Spec Kit / Superpowers **runtime** deps (D23)
- Copilot PR-skills / Debug-PR pack (D24)
- Git SHA ceremony as SoT (D25)
- Multi-consultant council ceremony (D26); keep table atom
- Fat Quality pocket (D27)
- Superpowers mirrors; gh-issue packaging; heavy D1–D13; 50-word task law; citation-house product rules

### G9

**Confirmed still 404** (E0 dir + E0/E1 raw HEAD 2026-07-30). Use SKILL.md summaries only.

### stop_reason

`wave1_slice_coverage`
