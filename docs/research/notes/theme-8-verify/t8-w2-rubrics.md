---
title: "T8 W2-RUBRICS — G1 checklist + severity unify + soft ambiguity"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8-w2-rubrics-gatherer]
depth: deep
campaign_phase: deep_wave2
aligned_with:
  - docs/research/notes/theme-8-verify/t8-w1-track-board.md
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8a-w1-plan-verify.md
  - docs/research/notes/theme-8-verify/t8b-w1-execute-verify.md
  - docs/research/notes/theme-8-verify/t8c-w1-community-verify.md
  - docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md
supersedes: null
---

# T8 W2-RUBRICS — House-policy candidates (not locks)

**Using `research-protocol`**.

**Status:** `draft`. Not Verify SoT. **INFERENCE** house-policy candidates only — do not elevate skills.  
**Identity:** Theme 8 = Plan/Execute **verification extensions**, not Debug/PR.

---

## 1. Scope

- **Question / goal:** Corroborate and propose thin house-policy candidates for (1) G1 readability/faithfulness/coherence rubric, (2) severity vocab unify OPEN-T8B-1, (3) plan-side soft ambiguity WARNING vs CRITICAL / intent-gap, (4) durable GAP vs PLUS1-freeze readiness.
- **In scope:** Re-probe OpenSpec verify-change Completeness/Correctness/Coherence; Superpowers requesting-code-review quality bullets; Alexandria Osmani chunks from pass2; map Plan-verify vs Execute-verify severity; corroborate T8A soft-ambiguity candidates.
- **Out of scope:** G2 thresholds (W2-THRESHOLDS); elevating skills; Debug/PR; inventing citations; live E0 trials; converge append format; orchestrator wiring prose (G4).

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (track board, campaign-brief §0, T8A/T8B/T8C W1, pass2 Osmani locators, research-note template, research-protocol); `gh api` raw OpenSpec `openspec-verify-change`, Superpowers `requesting-code-review` + `code-reviewer.md`, Spec Kit `analyze.md` severity/ambiguity, validating-plans severity; Alexandria MCP `rag_fetch_chunk` ×3 Osmani chunk_ids |
| Corpora / URLs searched | Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md`; obra/superpowers requesting-code-review; github/spec-kit `analyze.md`; majiayu000 validating-plans SKILL.md; Alexandria corpus `software_engineering` chunk_ids `d0369fad9ec1c3e4c6d4b750`, `b08ba03768f720bb46605057`, `ae5ea30721760ce3b23ed7af`; Theme 8 W1 notes |
| Queries (exact) | `gh api -H "Accept: application/vnd.github.raw" repos/Fission-AI/OpenSpec/contents/skills/openspec-verify-change/SKILL.md`; same pattern for obra/superpowers requesting-code-review + code-reviewer.md; github/spec-kit analyze.md; majiayu000 validating-plans SKILL.md; `rag_fetch_chunk` for three pass2 Osmani ids |
| What was *not* searched | G2 NT thresholds; kanbanzai full rubrics body; HCI code-review lit beyond Osmani chunks; live E0 trials; Debug/PR Copilot bodies; validating-plans refs (G9 closed 404) |
| Depth | deep |
| Waves / stop_reason | Wave 2 slice **W2-RUBRICS**. `stop_reason: wave2_slice_coverage` — G1 thin checklist, OPEN-T8B-1 dual-lane map, and plan soft-ambiguity triggers covered with E1/E2 corroboration; further Tier A re-fetch of the same bodies would be diminishing returns (not chosen as stop label because slice axes are complete, not stalled mid-search) |
| Provenance (optional PROV) | Entity←W1 T8A/T8B/T8C + Tier A primaries + Alexandria Osmani; Activity=W2-RUBRICS gather; Agent=t8-w2-rubrics-gatherer |

---

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | W1 candidates as E0 campaign inventory; re-probe Tier A + Alexandria for E1/E2 corroboration; propose dual-lane house map without inventing new vendor APIs |
| Scope boundary | Rubrics + severity + soft ambiguity only; park G2/thresholds/wiring |

---

## 4. Findings

### 4.1 Re-probed sources (corroboration)

- `FACT` [E1] OpenSpec verify-change report dimensions: **Completeness** (tasks + spec coverage), **Correctness** (requirement/scenario mapping), **Coherence** (design adherence + pattern consistency); issue tiers **CRITICAL / WARNING / SUGGESTION**; heuristics: Completeness = objective checklists; Correctness = keyword/path inference without perfect certainty; Coherence = glaring inconsistencies, don’t nitpick style; prefer lower severity when uncertain; every issue actionable. [E1: Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] Superpowers requesting-code-review: fresh reviewer with plan/requirements (never session history); act Critical immediately, Important before proceed, Minor later; severity **Critical / Important / Minor**. [E1: obra/superpowers `skills/requesting-code-review/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] Superpowers `code-reviewer.md` check bullets: **plan alignment** (match plan; deviations justified; planned functionality present); **code quality** (SoC, errors, types, DRY without premature abstraction, edges); **architecture** (design, scale/perf, security, integrate cleanly); **testing** (real behavior, edges, integration where matter); **production readiness** (migrations, compat, docs, obvious bugs). Critical = bugs/security/data loss/broken functionality; Important = architecture/missing features/poor errors/test gaps; Minor = style/optimization/docs polish. [E1: obra/superpowers `skills/requesting-code-review/code-reviewer.md` — accessed 2026-07-30]
- `FACT` [E1] validating-plans severities: BLOCKER (execution will fail / nonexistent refs) · CRITICAL (high rework risk) · WARNING (suboptimal / vague steps) · NIT (style); verdicts PASS / PASS WITH NOTES / NEEDS REVISION. [E1: majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` Step 4 — accessed 2026-07-30]
- `FACT` [E1] Spec Kit analyze Ambiguity: vague adjectives without measurable criteria; unresolved placeholders; severity CRITICAL = constitution MUST / missing core / zero-coverage blocking baseline; HIGH = ambiguous security/performance / untestable AC; MEDIUM = underspecified edge; LOW = style. CRITICAL → resolve before implement. [E1: github/spec-kit `templates/commands/analyze.md` Detection B + Severity — accessed 2026-07-30]
- `FACT` [E2] Osmani (Alexandria) code-review checks include: functionality/correctness (tests, edges, errors); **readability and maintainability** (style guides, clear naming); remove unused code; comments explain intent (esp. AI-generated); respectful specific feedback. [E2: Alexandria corpus=`software_engineering` chunk_id=`d0369fad9ec1c3e4c6d4b750` source=`Beyond Vibe Coding… (Addy Osmani)` heading=`Responsible AI Checklist` — fetched 2026-07-30]
- `FACT` [E2] Osmani: treat AI output like junior-developer code — human diligence on bugs/security/sloppy impl; assume nothing works until proven; don’t outsource QA entirely to AI. [E2: Alexandria chunk_id=`b08ba03768f720bb46605057` heading=`Focus on Code Review and Quality Assurance` — fetched 2026-07-30]
- `FACT` [E2] Osmani golden rule: AI-generated code checked against **original goal**; verify functionality, logic, relevance; never integrate without understanding. [E2: Alexandria chunk_id=`ae5ea30721760ce3b23ed7af` heading=`The Golden Rules of Vibe Coding` — fetched 2026-07-30]
- `FACT` [E0] Brief D17: Toolbelt dimensions = evidence + faithfulness + readability/coherence; OpenSpec Completeness/Correctness/Coherence as **labels only**. D7–D9: Plan verdicts + hard inventable gaps. D20: Execute WARNING/NIT agent-fixable unless Theme 7 escalate. [E0: `campaign-brief.md` §0]
- `FACT` [E0] T8A G1 OPEN: WARNING vs CRITICAL on soft ambiguity / undeclared deps. T8B OPEN-T8B-1: severity vocab unify Plan vs Execute. [E0: `t8a-w1-plan-verify.md` §7; `t8b-w1-execute-verify.md` §7]

### 4.2 G1 — Thin Toolbelt rubric (house-policy candidate)

`INFERENCE` [E4] Proposed **thin** post-green checklist for `implementation-execute-verify` (and shared dimension names for plan faithfulness where applicable). Keep OpenSpec names as **aliases only** (D17/D23). Premises: §4.1 FACTs; T8B §4.3 mapping; pass2 lean.

#### Dimension A — Evidence *(no OpenSpec twin)*

Thin bullets (signal lane already green before this pass):

1. Claim rests on IDENTIFY→RUN→READ→VERIFY (or Done-when command + kept output) — ban “should/looks/seems”.
2. Expected signal matched; failures/exit codes read, not assumed.
3. Requirements/Done-when checklist ≠ “tests green alone” when plan lists extra constraints.

#### Dimension B — Faithfulness *(alias Completeness + Correctness)*

1. Planned Done-when / Files / Interfaces / Do-not / Always·Block·Never present in outcome (or explicit out-of-scope).
2. No Goal / Done-when / Interfaces rewrite; deviations flagged for Theme 7 major-deviation if out of bounds.
3. No invent: missing intent → escalate, don’t invent design.
4. Unrequested scope surfaced (converge gap type) — not silently accepted as “bonus”.
5. Design/ADR decisions followed when cited (OpenSpec Coherence design-adherence atom as label).

#### Dimension C — Readability / coherence *(alias Coherence)*

1. Clear module/file boundaries; naming matches local conventions.
2. No clever opacity / unexplained magic; AI-generated logic has intent comments where non-obvious (Osmani).
3. Pattern fit with surrounding code; glaring inconsistency only — **don’t nitpick style** (OpenSpec Coherence heuristic).
4. No drive-by edits outside Files/Interfaces.
5. Unused leftovers removed; DRY without premature abstraction (Superpowers quality + Osmani unused).

**Anti-fat rule:** Do **not** import full Superpowers production-readiness / merge gate or Osmani bias/license checklist as Theme 8 law — park → Debug/PR or house later. Theme 8 stays thin.

### 4.3 OPEN-T8B-1 — Dual-lane severity (do not force identical strings)

`INFERENCE` [E4] Prefer **two native vocabularies** with an explicit **crosswalk**, rather than one forced string set. Plan verdicts stay validating-plans trio (D7); Execute issue tiers stay Superpowers-shaped for agent triage (fix-now vs later), with OpenSpec CRITICAL/WARNING/SUGGESTION as optional aliases on the report. Premises: D7; D17 labels-only; D20; T8C conflict log; §4.1 FACTs.

#### Lane P — Plan-verify (`implementation-plan-verify`)

| Plan severity | Meaning (Toolbelt) | Verdict impact |
|---------------|--------------------|----------------|
| **BLOCKER** | Plan cannot be executed as written (hallucinated path/API/package; inventable gap; cycle; in-scope baseline uncovered) | → **NEEDS REVISION**; Meta not `ready`; often `blocked`+`intent-gap` if invent required |
| **CRITICAL** | High rework / hard ambiguity / undeclared hard dep / orphan task on in-scope FR | → **NEEDS REVISION** unless human **risk-accept** recorded |
| **WARNING** | Soft ambiguity; undeclared soft dep; composite mash; orphan with out-of-scope justification weak; vague step still unique path | → **PASS WITH NOTES** allowed |
| **NIT** | Wording/style on plan prose | → PASS or PASS WITH NOTES |

Verdicts (unchanged D7): **PASS** · **PASS WITH NOTES** · **NEEDS REVISION**. Fix-plan-not-code (D8).

#### Lane E — Execute-verify (`implementation-execute-verify`)

| Execute severity (native) | OpenSpec alias (optional) | Meaning | Routing |
|---------------------------|---------------------------|---------|---------|
| **Critical** | CRITICAL | Broken functionality / security / data loss / faithfulness break inside claimed done | Fix immediately; re-evidence; if out of Files/Interfaces → Theme 7 major-deviation |
| **Important** | WARNING | Architecture / missing promised feature / weak errors / material faithfulness gap | Fix before proceed / before claim task done |
| **Minor** | SUGGESTION | Style, polish, non-blocking pattern drift | Note; agent-fixable if cheap; else later |

**No Plan verdict trio on Execute** — Execute already has Theme 7 task status (`done` / `blocked`+reasons). Post-green review emits Critical/Important/Minor findings; converge emits gap types + severity, not PASS WITH NOTES.

#### Crosswalk (mapping clarity > string identity)

| Plan severity | ≈ Execute | ≈ OpenSpec | Notes |
|---------------|-----------|------------|-------|
| BLOCKER | Critical (+ often HITL intent-gap) | CRITICAL | Different *object*: plan artifact vs code |
| CRITICAL | Critical or Important | CRITICAL or WARNING | Prefer Critical if invent/hard gate; Important if fixable faithfulness |
| WARNING | Important or Minor | WARNING or SUGGESTION | Soft ambiguity → WARNING/Important; pure style → Minor/SUGGESTION |
| NIT | Minor | SUGGESTION | Same spirit |

`CLAIM` [E0 constraint] Theme 7 HITL remains SoT for stop/ask; companion severities do not invent merge gates (D20/D24). [E0: campaign-brief]

### 4.4 Plan-side soft ambiguity — WARNING vs CRITICAL / intent-gap

`INFERENCE` [E4] Corroborate and tighten T8A §4.4 candidates with Spec Kit severity heuristics + validating-plans WARNING=“vague steps”. Premises: T8A §4.4; Spec Kit analyze [E1]; validating-plans [E1]; D9.

#### Hard gate → BLOCKER / CRITICAL + NEEDS REVISION (+ `intent-gap` when invent required)

1. Multiple defensible interpretations of Goal / Done-when / Interfaces with no Decision/ADR close.
2. TBD / placeholder / “similar to Task N” remaining (Spec Kit Ambiguity placeholders).
3. Verify step not falsifiable (“looks good”, no command/signal).
4. In-scope approved FR/section with **zero** tasks (baseline blocker).
5. Reality BLOCKER (nonexistent path/API treated as given) that cannot be fixed without inventing design.
6. Dependency **cycle** (DAG break).

#### Soft ambiguity → WARNING → PASS WITH NOTES (unique implementer path still exists)

1. Vague adjective (“robust”, “fast”) but Done-when command still unique and falsifiable.
2. Undeclared **soft** dependency (order preference) without cycle — ask/note, not invent.
3. Composite task that is serial-safe — recommend split; not hard gate unless parallel-unsafe mash → CRITICAL.
4. Orphan task with explicit out-of-scope / exploratory justification.
5. Line-number / drift MEDIUM risk with clear recover path (validating-plans CRITICAL for stale lines is **park weight** for Toolbelt unless Reality lane fails).

#### Intent-gap Meta vs NEEDS REVISION

| Situation | Meta / verdict |
|-----------|----------------|
| Fixable by editing the plan alone (add task, fix path cite, split composite) | **NEEDS REVISION**; stay off-`ready`; **no** invent |
| Cannot choose among defensible intents without human/design | **NEEDS REVISION** + Meta `blocked`+`intent-gap` |
| WARNING-only soft ambiguity | **PASS WITH NOTES**; `ready` allowed; notes recorded |

### 4.5 Durable GAP vs PLUS1-freeze readiness

| Item | Status | Ready for PLUS1 freeze? |
|------|--------|-------------------------|
| G1 thin dimension bullets (§4.2) | House candidate corroborated E1/E2 | **Yes** — freeze as checklist prose candidate |
| Dual-lane severity + crosswalk (§4.3) | Resolves OPEN-T8B-1 as mapping (not one string set) | **Yes** — freeze dual-lane scheme |
| Soft ambiguity triggers (§4.4) | Corroborates T8A; closes T8A G1 wording gap as candidate | **Yes** — freeze hard vs soft tables |
| Exact SKILL.md copy-paste polish | Not elevated | **PLUS1** editorial only |
| G2 non-trivial thresholds | Out of this slice | **No** — W2-THRESHOLDS |
| Live E0 trial of rubric | Not run | **Durable GAP** (G11 optional) |
| validating-plans deep refs | Still 404 | **Durable GAP** (G9 closed — write native) |
| Fat Osmani / Superpowers production checklists | Parked | **Durable park** — not Theme 8 law |

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Dual-lane severity beats forced identical strings | confirmed lean | Plan D7 trio + Execute Superpowers triage + OpenSpec aliases [E1/E0] |
| H2 | Thin 3-dimension checklist enough for G1 | confirmed lean | OpenSpec dims + Superpowers bullets + Osmani readability [E1/E2]; anti-fat |
| H3 | Soft ambiguity = WARNING when path unique | confirmed lean | T8A; validating-plans WARNING=vague; Spec Kit HIGH vs CRITICAL [E1] |
| H4 | Further vendor sources will change G1 atoms | rejected for this slice | Same Tier A bodies as T8B/T8C; Osmani re-fetched |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Execute severity strings | Superpowers Critical/Important/Minor [E1] | OpenSpec CRITICAL/WARNING/SUGGESTION [E1] | Native = Superpowers; OpenSpec = aliases in report (D17) |
| Plan vs Execute vocab | validating-plans BLOCKER…NIT [E1] | Execute Critical…Minor [E1] | Dual-lane + crosswalk — **do not unify strings** |
| Soft vague adjectives | Spec Kit HIGH for security/perf ambiguity [E1] | validating-plans WARNING for vague steps [E1] | Security/perf unmeasurable on in-scope baseline → CRITICAL; else WARNING if Done-when unique |
| Review depth | Superpowers full production-readiness [E1] | Theme 8 thin spirit / D27 park fat Quality [E0] | Thin §4.2 only; park production/merge depth |

---

## 7. Gaps & OPEN

- `OPEN` Editorial freeze of §4.2–4.4 into companion `references/review-dimensions.md` — post-accept elevation, not this note.
- `GAP` Live E0 trial applying checklist to a real Toolbelt plan/diff (G11) — not run.
- `GAP` G9 upstream deep checklists unavailable — native Toolbelt checklists required if elevated.
- Out of slice: G2 thresholds, OPEN-T8B-2 post-task converge, append format, G4 wiring.

---

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] PLUS1 / integrator can freeze: (1) thin Evidence / Faithfulness / Readability-coherence bullets; (2) dual-lane severity with crosswalk; (3) hard vs soft ambiguity tables — still `draft` until report accept. Premises: §4.2–4.5; `draft-is-not-sot`.
- `INFERENCE` [E4] Do not elevate skills from this note. Premises: campaign identity; coordinator board.

---

## 9. Source list (deduped)

1. [E0] `docs/research/notes/theme-8-verify/t8-w1-track-board.md` — accessed 2026-07-30
2. [E0] `docs/research/notes/theme-8-verify/campaign-brief.md` §0 — accessed 2026-07-30
3. [E0] `docs/research/notes/theme-8-verify/t8a-w1-plan-verify.md` — accessed 2026-07-30
4. [E0] `docs/research/notes/theme-8-verify/t8b-w1-execute-verify.md` — accessed 2026-07-30
5. [E0] `docs/research/notes/theme-8-verify/t8c-w1-community-verify.md` — accessed 2026-07-30
6. [E0] `docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md` — accessed 2026-07-30
7. [E1] Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md` — via `gh api` 2026-07-30
8. [E1] obra/superpowers `skills/requesting-code-review/SKILL.md` + `code-reviewer.md` — via `gh api` 2026-07-30
9. [E1] majiayu000/claude-skill-registry `skills/testing/validating-plans/SKILL.md` — via `gh api` 2026-07-30
10. [E1] github/spec-kit `templates/commands/analyze.md` — via `gh api` 2026-07-30
11. [E2] Alexandria `software_engineering` chunk_ids `d0369fad9ec1c3e4c6d4b750`, `b08ba03768f720bb46605057`, `ae5ea30721760ce3b23ed7af` — Osmani *Beyond Vibe Coding* — fetched 2026-07-30
12. [E0] `docs/PROTOCOL.md` / research-protocol — cite-or-omit — accessed 2026-07-30

---

## 10. Coordinator return (short)

### Proposed G1 thin rubric

| Dimension | Alias | Thin checks |
|-----------|-------|-------------|
| **Evidence** | — | Iron law; signal kept; ban should/looks |
| **Faithfulness** | Completeness+Correctness | Plan constraints met; no invent/rewrite; unrequested flagged; ADR followed |
| **Readability/coherence** | Coherence | Boundaries/naming; no opacity/drive-by; pattern fit; no style nitpick; unused gone |

### Severity map (dual-lane)

| Plan | Execute (native) | OpenSpec alias | Verdict / routing |
|------|------------------|----------------|-------------------|
| BLOCKER | Critical (+ intent-gap if invent) | CRITICAL | NEEDS REVISION / not ready |
| CRITICAL | Critical or Important | CRITICAL/WARNING | NEEDS REVISION unless risk-accept |
| WARNING | Important or Minor | WARNING/SUGGESTION | PASS WITH NOTES |
| NIT | Minor | SUGGESTION | PASS / notes |

Execute does **not** use PASS/PASS WITH NOTES/NEEDS REVISION — uses Theme 7 task status + Critical/Important/Minor findings.

### Soft ambiguity (plan)

- **Hard** (BLOCKER/CRITICAL): multi-intent, placeholders, non-falsifiable Verify, zero-coverage baseline, Reality invent, cycles → NEEDS REVISION / intent-gap.
- **Soft** (WARNING): vague but unique path, soft undeclared deps, serial-safe composite → PASS WITH NOTES.

### Freeze readiness

G1 + dual-lane + soft/hard tables → **ready for PLUS1 freeze as candidates**. Durable GAP: E0 trial, G9 native checklists. G2 → other gatherer.

**stop_reason:** `wave2_slice_coverage`
