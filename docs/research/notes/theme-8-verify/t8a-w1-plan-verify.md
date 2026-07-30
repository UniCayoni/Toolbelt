---
title: "T8A W1 — Plan-verify gates for implementation-plan-verify"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8a-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8-coordinator-pin.md
  - docs/research/reports/theme-6-plan-pocket.md
  - skills/implementation-plan/SKILL.md
supersedes: null
---

# T8A W1 — Plan-verify gates (`implementation-plan-verify`)

**Using `research-protocol`**.

**Status:** `draft`. Not Verify SoT. Design candidates only — do not elevate skills.  
**Identity:** Theme 8 = missing verification **extension** of shipped Plan pocket. Target companion: `implementation-plan-verify`. Plan skill (`implementation-plan`) remains orchestrator. **Not** Debug/PR pocket.

---

## 1. Scope

- **Question / goal:** What should `implementation-plan-verify` contain as Toolbelt-native gates/atoms for validating a plan **before** Meta `ready` / execute?
- **In scope:**
  1. Explicit phase placement + Plan-skill wiring
  2. Parallel Reality + Drift + coverage/actionability (park TDD auditor)
  3. Severity + PASS / PASS WITH NOTES / NEEDS REVISION; fix-plan-not-code
  4. Hard ambiguity → `blocked(intent-gap)` / NEEDS REVISION
  5. Light task taxonomy; light FR→task coverage + acyclic deps
  6. Codebase verification table for non-trivial plans (thresholds → OPEN if unsure)
  7. Steal Spec Kit analyze/checklist grammar (no Spec Kit dependency)
  8. Relationship to existing V1–V8 (strengthen vs move vs duplicate)
  9. Proposed skill file layout (candidates only)
  10. Transferable vs park table
- **Out of scope:** Debug/PR pocket design; elevating skills; T8B execute-verify; T8C full community deepen; T8D surface elevation locks; inventing Cursor Task APIs; mandatory TDD/git/PR as Plan law; Spec Kit / OpenSpec / Superpowers as runtime deps.
- **Comprehension / research goal type:** perfective (extend Plan method with pre-exec validate companion).

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign-brief, coordinator-pin, scope pass1–3, Theme 6 report, `implementation-plan` SKILL + checklist, `plan-minimal`, research-note template); `gh api` (validating-plans SKILL.md, Spec Kit analyze.md + checklist.md, rube-de review-plan, kdcokenny plan-review, mab-go review-plan, kanbanzai validate-plan); `gh search code` (spot-check paths); Grep Theme 6 notes for V1–V8 / validating-plans GAP |
| Corpora / URLs searched | github.com/majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md`; github.com/github/spec-kit `templates/commands/analyze.md` + `checklist.md`; github.com/rube-de/cc-skills `plugins/council/skills/review-plan/SKILL.md`; github.com/kdcokenny/opencode-workspace `src/skills/plan-review/SKILL.md`; github.com/mab-go/trello-mcp `.agents/skills/review-plan/SKILL.md`; github.com/sambeau/kanbanzai `.kbz/skills/validate-plan/SKILL.md`; local Theme 6/8 notes |
| Queries (exact) | `gh api repos/…/contents/…`; `gh search code "review-plan" --repo rube-de/cc-skills`; `gh search code "plan-review" --repo kdcokenny/opencode-workspace`; `gh search code "validate-plan" --repo sambeau/kanbanzai`; tree listing `mab-go/trello-mcp` for review-plan path; Grep `validating-plans\|V1–V8` under `docs/research/notes/theme-6-plan` |
| What was *not* searched | validating-plans `references/*.md` deep bodies (confirmed 404 directory); OpenSpec verify-change full rubrics (T8B/T8C); Spec Kit converge.md re-fetch (execute-side; T8B); live E0 Toolbelt plan-verify trials (G11); Debug/PR Copilot packaging |
| Depth | deep |
| Waves / stop_reason | Wave 1 T8A; `stop_reason: wave1_slice_coverage` — all ten assigned axes covered with graded claims; residual OPEN → G1/G2/G3/G4/G9 for W2/T8D |
| Provenance (optional PROV) | Entity←Theme 6 accepted Plan law + Tier A plan-validate primaries; Activity=T8A W1 gather; Agent=t8a-w1-gatherer + gh api |

---

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | E0 on shipped Plan surfaces + E1 deep-read of Tier A plan-validate primaries; brief §0 D5–D13 / D22–D23 as campaign constraints (not elevated SoT) |
| Scope boundary | Plan pre-exec validate companion only; exclude execute-verify, Debug/PR |

---

## 4. Findings

### 4.0 Constraints from brief / Plan law (input, not locks from this note)

- `FACT` [E0] Campaign §0 locks companions `implementation-plan-verify` + hybrid orchestration (Plan remains orchestrator); Plan-validate determinations D5–D13; park TDD auditor (D22) and CLI framework deps (D23). [E0: `docs/research/notes/theme-8-verify/campaign-brief.md` §0 — observed 2026-07-30]
- `FACT` [E0] Theme 6 accepted: Plan owns **light** pre-exec V1–V8; full validating-plans / TDD auditor / issue packaging deferred. [E0: `docs/research/reports/theme-6-plan-pocket.md` elevation #5 — accepted 2026-07-29]
- `FACT` [E0] Shipped spine step 9 = “Pre-exec check (V1–V8)” then handoff to `implementation-execute`; Meta status includes `ready` · `blocked`(`intent-gap`…). [E0: `skills/implementation-plan/SKILL.md`; `docs/templates/plan-minimal.md`]

### 4.1 Explicit phase placement + Plan wiring

- `FACT` [E1] validating-plans places itself **between** write-plan and execute-plan; input = plan document; output = severity-graded validation report; do **not** use for validating code. [E1: majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — Workflow Position — accessed 2026-07-30]
- `FACT` [E1] Spec Kit `analyze` runs **after** tasks exist, **before** implement; strictly read-only report; CRITICAL issues → resolve before implement. [E1: github/spec-kit `templates/commands/analyze.md` — Goal / Operating Constraints / Next Actions — accessed 2026-07-30]
- `FACT` [E0] Toolbelt Plan spine today: write tasks → V1–V8 light → handoff execute; no graded companion phase. [E0: `skills/implementation-plan/SKILL.md` Spine 8–10]
- `INFERENCE` [E4] Toolbelt-native phase for `implementation-plan-verify`: **after** durable plan body written (and after or wrapping V1–V8 — see §4.8), **before** Meta Status `ready` and **before** invoking `implementation-execute` / `-subagents`. Premises: (1) D5; (2) validating-plans + Spec Kit analyze placement; (3) Theme 6 status vocab.
- `INFERENCE` [E4] Wiring candidates (design only; G4 OPEN for exact wording):
  | Pattern | Shape |
  |---------|-------|
  | **A. Orchestrator invoke** | `implementation-plan` spine ends with: run companion (or announce Using `implementation-plan-verify`) → only then set Meta `ready` |
  | **B. Gate on handoff** | Handoffs table: Execute only if plan-verify verdict PASS / PASS WITH NOTES (or human risk-accept) |
  | **C. Template meta** | `plan-minimal` Meta Status: remain non-`ready` until verify pass; optional “Plan-verify” section with verdict |
  Premises: D2 hybrid orchestration; D1=C companion; shipped handoffs table points only to execute today.

### 4.2 Parallel Reality + Drift + coverage/actionability (park TDD)

- `FACT` [E1] validating-plans launches **three parallel** validators: TDD Compliance Auditor, Reality Check Verifier, Drift Detector; aggregate into one report. [E1: validating-plans SKILL.md Step 3 — accessed 2026-07-30]
- `FACT` [E1] Reality Check (SKILL summary): file existence/line numbers; package registry existence; API signatures/exports; imports; command availability. Drift: file mods after plan; uncommitted changes; dependency updates; drift risk HIGH/MEDIUM/LOW/NONE. [E1: validating-plans SKILL.md Validation Checks Summary — accessed 2026-07-30]
- `FACT` [E0] Campaign D6: parallel Reality + Drift + coverage/actionability; **park TDD auditor**. D22 parks TDD auditor as Plan law. [E0: campaign-brief §0]
- `FACT` [E1] kdcokenny plan-review Actionability: tasks name files/components; avoid vague “investigate/figure out”; clear deps; implementer can start without clarification. Completeness: specific goal, logical phases, edge cases. [E1: kdcokenny/opencode-workspace `src/skills/plan-review/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] Spec Kit analyze Coverage Gaps: requirements with zero tasks; tasks with no mapped requirement/story; buildable Success Criteria not reflected in tasks. Ambiguity: vague adjectives; unresolved placeholders. [E1: spec-kit `analyze.md` Detection Passes B/E — accessed 2026-07-30]
- `GAP` validating-plans `references/` directory still **404** via GitHub API (deep checklist bodies unavailable). Use SKILL.md summaries only. [GAP: `gh api …/validating-plans/references` → HTTP 404 — 2026-07-30; corroborates Theme 6 G9 / D23 lean]
- `INFERENCE` [E4] Toolbelt parallel specialist set (candidate atoms):
  | Parallel lane | Checks (Toolbelt-native) | Source atoms |
  |---------------|--------------------------|--------------|
  | **Reality** | Cited paths exist (or marked create); packages/APIs/commands real; verify commands available | validating-plans Reality; V4 |
  | **Drift** | Plan still matches tree/deps if reused/stale; flag high drift → NEEDS REVISION or risk-accept | validating-plans Drift; V5 |
  | **Coverage / actionability** | FR/section→task map; orphan tasks; falsifiable Verify; light task taxonomy (§4.5) | Spec Kit analyze; kdcokenny; mab-go; V1–V3/V8 |
  | **TDD auditor** | **PARK** — not Plan-verify law | D6/D22; Theme 6 #4/#5 |
  Premises: D6; FACTs above; Theme 6 verify-required / TDD-optional.

### 4.3 Severity + verdicts; fix-plan-not-code

- `FACT` [E1] validating-plans severity: BLOCKER / CRITICAL / WARNING / NIT. Verdicts: PASS | PASS WITH NOTES | NEEDS REVISION. Sign-off: blockers resolved; criticals fixed or risk-accepted; ready YES/NO. [E1: validating-plans SKILL.md Step 4 — accessed 2026-07-30]
- `FACT` [E1] On blockers/criticals: TodoWrite tasks **fix the plan**, not code/install missing packages/create missing files the plan hallucinated. Re-run validate after plan fixes. [E1: validating-plans SKILL.md Step 5 — accessed 2026-07-30]
- `FACT` [E1] kanbanzai verdicts: `pass` / `pass_with_notes` / `fail` from blocking vs non-blocking D-checks. [E1: sambeau/kanbanzai `.kbz/skills/validate-plan/SKILL.md` Step 4 — accessed 2026-07-30]
- `FACT` [E1] rube-de review-plan: Critical → Needs revision; Note-only → Ready to execute; Critical codebase fails presented **before** consultants. [E1: rube-de/cc-skills `plugins/council/skills/review-plan/SKILL.md` Verdict Logic — accessed 2026-07-30]
- `FACT` [E0] Campaign D7–D8: severity + PASS / PASS WITH NOTES / NEEDS REVISION; on NEEDS REVISION fix plan not code; re-validate before execute. [E0: campaign-brief §0]
- `INFERENCE` [E4] Toolbelt-native verdict mapping (candidate):

  | Verdict | When | Next |
  |---------|------|------|
  | **PASS** | No BLOCKER/CRITICAL (or NIT-only) | Meta may become `ready`; handoff execute |
  | **PASS WITH NOTES** | WARNING/NIT only; no unresolved BLOCKER/CRITICAL | `ready` allowed; notes recorded; optional human risk-accept on WARNINGs |
  | **NEEDS REVISION** | Any BLOCKER or unaccepted CRITICAL | Meta **not** `ready`; todos/edits target **plan file**; re-run companion |

  Severity → Toolbelt status: BLOCKER / unresolved inventable ambiguity → Meta `blocked` + `intent-gap` when intent cannot be fixed by plan edit alone (else stay off-`ready` until plan revised). Premises: D7–D9; Theme 6 status vocab; validating-plans + rube-de.

### 4.4 Hard ambiguity → blocked(intent-gap) / NEEDS REVISION

- `FACT` [E0] Plan skill: if intent ambiguous with multiple defensible outcomes → `blocked` + `intent-gap` (**do not invent**). V1: no unresolved intent gaps. [E0: `skills/implementation-plan/SKILL.md` Preconditions; checklist Pre-exec V1]
- `FACT` [E1] Spec Kit analyze Ambiguity Detection: vague adjectives without measurable criteria; unresolved placeholders (TODO, TKTK, ???, `<placeholder>`). CRITICAL heuristic includes requirement with zero coverage that blocks baseline functionality. [E1: spec-kit `analyze.md` Detection B + Severity — accessed 2026-07-30]
- `FACT` [E1] Spec Kit checklist metaphor: “unit tests for English” — completeness/clarity/consistency/measurability/coverage of **requirements**, not implementation tests. [E1: github/spec-kit `templates/commands/checklist.md` Checklist Purpose — accessed 2026-07-30]
- `FACT` [E1] mab-go: for errors/vagueness/ambiguity, state issue + concrete fix; **do not edit the plan yet**; ask clarifying questions if required context missing. [E1: mab-go/trello-mcp `.agents/skills/review-plan/SKILL.md` Output — accessed 2026-07-30]
- `FACT` [E0] Campaign D9: ambiguity / inventable gaps → hard gate (`blocked(intent-gap)` / NEEDS REVISION). [E0: campaign-brief §0]
- `INFERENCE` [E4] Hard-gate triggers for plan-verify (candidate):
  1. Multiple defensible interpretations of Goal / Done-when / interfaces with no Decision/ADR close
  2. TBD / placeholder / “similar to Task N” remaining
  3. Verify step not falsifiable (“looks good”, no command/signal)
  4. Coverage hole on approved design section / FR that is in-scope (zero tasks)
  5. Reality BLOCKER (nonexistent path/API treated as given) that cannot be resolved without inventing design

  On hard gate: verdict **NEEDS REVISION** and/or Meta `blocked`+`intent-gap`; **do not invent**; escalate to design/human. Soft ambiguity (WARNING) may PASS WITH NOTES if implementer path still unique. Premises: D9; Plan V1; Spec Kit ambiguity; mab-go clarify-before-edit.

### 4.5 Light task taxonomy; light FR→task coverage + acyclic deps

- `FACT` [E1] mab-go task taxonomy: Incomplete · Composite · Ambiguous · Trivial · Misordered · Coverage gap — review each structured task item; do not edit until approve. [E1: mab-go review-plan SKILL.md Task item review — accessed 2026-07-30]
- `FACT` [E0] Campaign D10–D11: **light** task taxonomy (composite / ambiguous / coverage gap / misordered); park heavy D1–D13; **light** FR→task coverage + acyclic deps. [E0: campaign-brief §0]
- `FACT` [E1] kanbanzai blocking subset relevant to light coverage/deps: D3 task→REQ; D4 every REQ covered; D5 no scope drift; D6 dependency graph acyclic (topo sort); D13 actionable (heavy rubric: 50+ words — **park weight**). Full D1–D13 is product-specific heavy catalog. [E1: kanbanzai validate-plan SKILL.md checklist + D-table — accessed 2026-07-30]
- `FACT` [E1] Spec Kit analyze: task coverage mapping; inconsistency includes task ordering contradictions without dependency note. [E1: analyze.md Detection E/F — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt **light** taxonomy (adopt mab-go subset per D10; park Incomplete/Trivial as optional notes or fold into actionability):

  | Tag | Meaning (Toolbelt) | Severity lean |
  |-----|--------------------|---------------|
  | **composite** | Multiple independently failable changes in one task | WARNING → split (CRITICAL if parallel-unsafe mash) |
  | **ambiguous** | No clear Done-when / inventable outcome | BLOCKER / intent-gap |
  | **coverage_gap** | Approved FR/section with no task | BLOCKER if in-scope baseline |
  | **misordered** | Deps violate order / cycle / undeclared hard dep | BLOCKER if cycle; WARNING if undeclared |

  Light coverage: walk Coverage map (already in `plan-minimal`) — every approved design section/FR → ≥1 task; every task → ≥1 section/FR or explicit out-of-scope justification (orphan = WARNING/CRITICAL). Light deps: declared Deps form DAG (no cycles); flag obvious “uses Task B output” without Deps. **Park:** kanbanzai 50-word law, full D1–D13 ceremony, risk-assessment D10 as Plan-verify law. Premises: D10–D11; mab-go; kanbanzai D4/D6; plan-minimal Coverage map.

### 4.6 Codebase verification table (non-trivial); threshold OPEN

- `FACT` [E1] rube-de review-plan Step 2 **Codebase Verification** table before consultants:

  | Claim Type | Method | Failure |
  |------------|--------|---------|
  | File paths (modify/delete) | Glob existence | Critical |
  | File paths (create) | Parent dir exists | Note |
  | Line numbers | Read match | Warning |
  | API signatures | Grep params | Critical |
  | Import paths (relative) | Glob + export | Critical |
  | Duplicate work | Grep existing | Warning |
  | Test files | Glob area | Note |

  CRITICAL failures presented immediately; skip table if plan has no concrete file refs. Skip review for trivial plans (single file, under 5 lines). [E1: rube-de review-plan SKILL.md Step 2 + When NOT to Use — accessed 2026-07-30]
- `FACT` [E0] Campaign D12: codebase verification table **required for non-trivial** plans; skip trivial. D26: park multi-consultant council; **keep verification-table atom**. [E0: campaign-brief §0]
- `FACT` [E0] Theme 6: durable plans under `docs/plans/` for non-trivial; trivial one-file may be chat-ephemeral. [E0: theme-6-plan-pocket.md elevation #7]
- `OPEN` Exact **non-trivial threshold** for requiring the table (G2): candidates below — not locked this wave.

  | Candidate threshold | Basis | Status |
  |---------------------|-------|--------|
  | Multi-file **or** multi-task durable plan | Theme 6 durable-plan lean | OPEN |
  | 2+ tasks **or** File Map with more than one path | Lightweight heuristic | OPEN |
  | rube-de “single file, under 5 lines” skip | Community E1 | OPEN (may be too tight for Toolbelt) |
  | Align with Plan “non-trivial → docs/plans/” | Same bar as durable artifact | OPEN preferred lean |

- `INFERENCE` [E4] Adopt verification-table **atom** (columns: Claim · Method · Result · Severity) as required lane inside Reality (or pre-parallel gate) for non-trivial plans; **park** gemini/codex dual-consultant ceremony (D26). Premises: D12/D26; rube-de Step 2.

### 4.7 Steal Spec Kit analyze / checklist grammar (no dependency)

- `FACT` [E1] analyze grammar worth stealing: read-only; progressive disclosure load; requirements inventory + coverage table; detection passes (Duplication, Ambiguity, Underspecification, Coverage Gaps, Inconsistency); severity CRITICAL/HIGH/MEDIUM/LOW; compact findings table (ID, Category, Severity, Location, Summary, Recommendation); metrics (coverage %, ambiguity count); Next Actions; offer remediation **without** auto-apply. Constitution conflicts → CRITICAL (Toolbelt analogue: accepted Design/ADR / Always·Block If·Never). [E1: analyze.md — accessed 2026-07-30]
- `FACT` [E1] checklist grammar: requirements-quality questions (“Is X specified?”) not implementation verifies; dimensions Completeness / Clarity / Consistency / Measurability / Coverage / Edge cases; markers `[Gap]` `[Ambiguity]` `[Conflict]` `[Assumption]`; anti-pattern ban on “Verify/Test/Confirm” implementation items. [E1: checklist.md — accessed 2026-07-30]
- `FACT` [E0] D13: steal grammar only; no Spec Kit dependency (D23 parks CLI frameworks). [E0: campaign-brief §0]
- `INFERENCE` [E4] Map into companion without Spec Kit paths/hooks/scripts:

  | Steal | Toolbelt home |
  |-------|---------------|
  | Read-only analyze report shape | Companion output template |
  | Coverage summary table | Strengthen plan Coverage map audit |
  | Ambiguity + placeholder pass | Hard/soft gate (§4.4) |
  | “Unit tests for English” question form | Optional light requirements-quality pass when design sections thin / Open Questions linger (ties V6) |
  | No auto-edit during analyze | Aligns fix-plan-not-code + mab-go approve-before-edit |
  | Spec Kit hooks / FEATURE_DIR / constitution.md paths | **Park** |

  Premises: D13/D23; FACTs above.

### 4.8 Relationship to V1–V8 (strengthen vs move vs duplicate)

V1–V8 as shipped ([E0: `plan-minimal.md` Pre-exec; checklist]):

| ID | Shipped check |
|----|---------------|
| V1 | No unresolved intent gaps → else `blocked`+`intent-gap` |
| V2 | Files + interfaces + out-of-scope + verify present |
| V3 | Verify runnable + expected signal |
| V4 | Reality-check paths/packages/APIs/commands |
| V5 | Drift if plan reused |
| V6 | Design Open Questions that change build closed |
| V7 | Binding constraints / Always·Block If·Never explicit |
| V8 | Hybrid density (no mandatory impl-code dumps) |

- `INFERENCE` [E4] Recommended disposition (design candidate — not elevation):

  | ID | Disposition | Rationale |
  |----|-------------|-----------|
  | V1 | **Strengthen** in companion (hard gate + severity); keep light checkbox in Plan checklist as authoring self-check | D9; avoid silent drop |
  | V2–V3 | **Strengthen** via actionability/falsifiability lane; Plan keeps authoring checklist | kdcokenny + Claude verify grammar |
  | V4–V5 | **Move depth** into companion Reality/Drift specialists; Plan checklist retains one-line reminder (“run plan-verify”) | validating-plans parallel; avoid duplicating full audits in Plan SKILL |
  | V6–V7 | **Strengthen** lightly in companion (constitution/ADR alignment analogue); remain on Plan checklist | Spec Kit constitution CRITICAL → Design/ADR |
  | V8 | **Stay** Plan-authored density gate; companion spot-checks only if dump-shaped tasks appear | Theme 6 hybrid #1 |
  | New: coverage/taxonomy/table | **Add** in companion (not duplicate as V9–V16 laundry list on Plan) | D10–D12 |

  Anti-duplication rule: Plan skill stays orchestrator + thin V1–V8 authoring checklist; companion owns **graded report + parallel depth + verdict**. Premises: D2; Theme 6 #5; pass-1 gap “standalone plan-validate skill = no”.

### 4.9 Proposed skill file layout (candidates only — do not elevate)

- `FACT` [E0] Existing Plan skill layout: `skills/implementation-plan/SKILL.md` + `references/implementation-plan-checklist.md` + `references/plan-minimal.md`. [E0: repo tree]
- `INFERENCE` [E4] Candidate layouts for post-accept elevation (none created this wave):

  | Option | Files | Pros | Cons |
  |--------|-------|------|------|
  | **L1 Thin** | `skills/implementation-plan-verify/SKILL.md` only | Matches D3 skill-only; minimal | Long SKILL if all rubrics inline |
  | **L2 SKILL + checklist** (preferred lean) | `SKILL.md` + `references/plan-verify-checklist.md` (lanes, severity, verdict, table template) | Mirrors Plan pocket pattern; progressive disclosure | Extra file to maintain |
  | **L3 + report template** | L2 + `docs/templates/plan-verify-report-minimal.md` | Stable report shape for agents | More surfaces; may wait until E0 trials |

  SKILL.md spine candidate (content outline only):
  1. Announce Using `implementation-plan-verify`
  2. Load plan path + design/ADR refs
  3. Trivial? → skip or light V1–V3 only (threshold OPEN)
  4. Codebase verification table (non-trivial)
  5. Parallel: Reality ‖ Drift ‖ Coverage/Actionability (+ light taxonomy/deps)
  6. Aggregate severity → verdict
  7. On NEEDS REVISION: plan-fix todos only; re-validate
  8. On PASS / PASS WITH NOTES: return to Plan orchestrator for Meta `ready` / execute handoff
  9. Park: TDD auditor, gh-issue packaging, council consultants, Spec Kit CLI

  Premises: D1–D3; shipped Plan layout; D6–D8.

### 4.10 Transferable vs park table

| Atom / surface | Transfer? | Toolbelt home | Grade |
|----------------|-----------|---------------|-------|
| Phase between write-plan and execute | **Yes** | Companion + Plan wiring | E1 validating-plans / Spec Kit analyze |
| Parallel Reality + Drift | **Yes** | Companion lanes | E1 validating-plans |
| TDD Compliance Auditor | **Park** | — | E1 present; D6/D22 |
| Severity BLOCKER…NIT + PASS / PASS WITH NOTES / NEEDS REVISION | **Yes** | Companion verdict | E1 validating-plans; D7 |
| Fix-plan-not-code + re-validate | **Yes** | Companion Step | E1 validating-plans; D8 |
| GitHub issue packaging post-validate | **Park** | Later Debug/PR leftover | E1 validating-plans; D24 spirit |
| Superpowers path / executing-plans coupling | **Park** | — | E1 packaging |
| Codebase verification table | **Yes** | Reality / pre-parallel | E1 rube-de; D12 |
| Multi-consultant council (gemini+codex) | **Park** | — | E1 rube-de; D26 |
| Actionability / Completeness rubric | **Yes** (light) | Coverage/actionability lane | E1 kdcokenny |
| Citation-quality house rules (ref:delegation-id) | **Park** / house-specific | — | E1 kdcokenny product |
| Task taxonomy composite/ambiguous/coverage/misordered | **Yes** (light) | Taxonomy pass | E1 mab-go; D10 |
| Incomplete/Trivial tags | Optional note | Soft | E1 mab-go |
| FR→task coverage + acyclic deps | **Yes** (light) | Coverage + deps | E1 Spec Kit analyze + kanbanzai D4/D6; D11 |
| Heavy D1–D13 + 50-word actionability | **Park** | — | E1 kanbanzai; D10 |
| analyze read-only report + coverage metrics | **Yes** (grammar) | Report template | E1 Spec Kit; D13 |
| checklist “unit tests for English” | **Yes** (light/optional) | Ambiguity/V6 assist | E1 Spec Kit; D13 |
| Spec Kit CLI / hooks / FEATURE_DIR | **Park** | — | D23 |
| OpenSpec verify-change dimensions | **Park for T8A** | T8B labels | Pass-3; execute-side |
| V1–V8 light checklist | **Strengthen / split depth** | Plan + companion | E0 Theme 6 |

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Companion should sit after write-plan / before Meta `ready` | confirmed (for campaign) | D5; validating-plans; analyze placement |
| H2 | Three-lane parallel without TDD is sufficient Plan-verify core | confirmed lean | D6; SKILL.md; park D22 |
| H3 | V1–V8 should be deleted from Plan once companion exists | rejected | Theme 6 #5; anti-duplication = thin retain + deepen in companion |
| H4 | Non-trivial ≡ durable `docs/plans/` path | open | G2; Theme 6 #7 alignment candidate |
| H5 | L2 SKILL + checklist is enough for elevation later | open | G3/G4; no E0 trial yet |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Surface shape | Pass-2 lean shared companion B | Human lock C two companions | Prefer brief §0 D1=C for this campaign |
| TDD-in-validate | validating-plans Agent 1 required | Theme 6 #4 + D6/D22 park | **Park** TDD auditor; keep Reality/Drift |
| Verdict vocabulary | validating-plans PASS…; kanbanzai pass/fail; rube-de Ready/Needs revision/discussion; kdcokenny APPROVE/REQUEST_CHANGES | — | Prefer **validating-plans trio** per D7; map others as synonyms in transfer table |
| When to edit plan | validating-plans creates fix todos; mab-go no edit until approve | — | Companion: propose fixes / todos; apply plan edits per Plan orchestrator + human norms — **OPEN** exact HITL (G1/G4) |
| Skip trivial | rube-de under-5-lines single file | Theme 6 durable-plan bar | Leave **OPEN** G2; lean align with durable-plan |

---

## 7. Gaps & OPEN

- `OPEN` **G1** Rubric wording for WARNING vs CRITICAL on soft ambiguity / undeclared deps.
- `OPEN` **G2** Non-trivial threshold for mandatory verification table (+ skip path).
- `OPEN` **G3** Skill `description` triggers (when auto-suggest companion).
- `OPEN` **G4** Exact Plan SKILL / checklist / plan-minimal wiring text (orchestrator invoke vs handoff gate).
- `OPEN` **G9** validating-plans `references/*.md` remain 404 — cannot deepen Reality/Drift checklists from upstream; Toolbelt must write native checklists if elevated.
- `GAP` Live E0 trial of companion on a real Toolbelt plan (G11) — not run this wave.
- `GAP` mab-go Incomplete/Trivial severity mapping to BLOCKER/WARNING — not prescribed by D10; left optional.
- Out of T8A: T8B execute-verify; T8C full OpenSpec deepen; T8D elevation packaging.

---

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Elevate-later package is a **thin companion** holding: phase gate, parallel Reality‖Drift‖Coverage/Actionability, severity+verdict, fix-plan-not-code, hard intent-gap, light taxonomy+coverage+DAG, codebase verification table — **not** a fat Quality/Debug pocket. Premises: §4.1–4.10; D1–D13.
- `INFERENCE` [E4] Plan skill remains author of hybrid plans + thin V1–V8; companion supplies graded depth so V4–V5 do not bloat Plan SKILL. Premises: §4.8; D2.
- `INFERENCE` [E4] Do not treat this draft as design law; W2 should corroborate G1/G2/G4 and confirming refs 404 (G9). Premises: `draft-is-not-sot`; stop_reason wave1_slice_coverage.

---

## 9. Source list (deduped)

1. `docs/research/notes/theme-8-verify/campaign-brief.md` — accessed 2026-07-30 [E0]
2. `docs/research/notes/theme-8-verify/t8-coordinator-pin.md` — accessed 2026-07-30 [E0]
3. `docs/research/notes/theme-8-verify/scope-normal-pass1.md` … `pass3-github-web.md` — accessed 2026-07-30 [E0]
4. `docs/research/reports/theme-6-plan-pocket.md` (accepted) — accessed 2026-07-30 [E0]
5. `skills/implementation-plan/SKILL.md` + `references/implementation-plan-checklist.md` — accessed 2026-07-30 [E0]
6. `docs/templates/plan-minimal.md` — accessed 2026-07-30 [E0]
7. majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — via `gh api` 2026-07-30 [E1]
8. github/spec-kit `templates/commands/analyze.md` — via `gh api` 2026-07-30 [E1]
9. github/spec-kit `templates/commands/checklist.md` — via `gh api` 2026-07-30 [E1]
10. rube-de/cc-skills `plugins/council/skills/review-plan/SKILL.md` — via `gh api` 2026-07-30 [E1]
11. kdcokenny/opencode-workspace `src/skills/plan-review/SKILL.md` — via `gh api` 2026-07-30 [E1]
12. mab-go/trello-mcp `.agents/skills/review-plan/SKILL.md` — via `gh api` 2026-07-30 [E1]
13. sambeau/kanbanzai `.kbz/skills/validate-plan/SKILL.md` — via `gh api` 2026-07-30 [E1]
14. Theme 6 notes on validating-plans refs 404 (`t6-w3-plus1-residual.md`, `t6-gap-closure-lean.md`) — accessed 2026-07-30 [E0]
15. `docs/PROTOCOL.md` — cite-or-omit grades — accessed 2026-07-30 [E0]

---

## 10. Coordinator return summary

**Key atoms (candidate):** phase after write-plan / before Meta `ready`; Plan orchestrates companion; parallel Reality ‖ Drift ‖ Coverage/Actionability (**park TDD**); BLOCKER…NIT + PASS / PASS WITH NOTES / NEEDS REVISION; fix-plan-not-code + re-validate; hard ambiguity → `blocked(intent-gap)` / NEEDS REVISION; light taxonomy (composite / ambiguous / coverage_gap / misordered); light FR→task + DAG deps; codebase verification table for non-trivial; Spec Kit analyze/checklist **grammar only**; V1–V8 thin retain + deepen V4–V5 in companion; prefer skill layout **L2** SKILL + checklist.

**OPEN for W2/T8D:** G1 rubric wording · G2 non-trivial threshold · G3 description triggers · G4 Plan wiring text · G9 upstream refs still 404 · HITL before plan edits.

**stop_reason:** `wave1_slice_coverage`
