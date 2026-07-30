---
title: "T8D W1 — Surface shape & elevation (Verify gates companions)"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8d-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8-coordinator-pin.md
  - docs/packs/README.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
supersedes: null
---

# T8D W1 — Surface shape & elevation (Verify gates companions)

**Using `research-protocol`** · depth: **deep** · `stop_reason: wave1_slice_coverage`.

**Status:** `draft` candidates only. Do **not** elevate skills from this note. Do **not** invent Cursor/plugin APIs.

---

## 1. Scope

- Question / goal: Confirm locked surface **C** against Theme 6/7 elevation precedent; propose description triggers (G3), wiring touchpoints (G4), non-trivial thresholds (G2), skill/checklist layout, G10 leftovers, G12 converge home, elevation order, and sprawl/ceremony risks.
- In scope: Surface packaging + elevation *candidates* for `implementation-plan-verify` + `implementation-execute-verify`; hybrid orchestration; skill-only (D3); pack README alignment; checklist naming.
- Out of scope: Creating skills; designing Debug/PR pocket (G10 leftover list only); fat Quality pack (D27); shared `implementation-verify` (rejected); rubric wording body (G1 → T8A/T8B); inventing Task/subagent APIs; elevating anything.
- Comprehension / research goal type: perfective (extend Plan/Execute surfaces; no new pocket product).

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (local files); Grep (Theme 6/7 elevation + Theme 8 notes); Glob (plugin skills layout, plugin.json) |
| Corpora / URLs searched | None (local E0 only this slice) |
| Queries (exact) | Theme 6/7 reports: elevat\|companion\|wiring\|skill; Theme 8 notes: non-trivial\|converge\|G10\|option C; skill trees under `~/.cursor/plugins/local/toolbelt/skills/` |
| What was *not* searched | Live Cursor skill-discovery behavior; Alexandria; GitHub community skills (owned by T8C); rubric deep-reads (T8A/T8B/G1/G5/G6) |
| Depth | deep |
| Waves / stop_reason | W1 T8D slice; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←campaign-brief §0 + packs README + Theme 6/7 accepted reports + shipped Plan/Execute skills; Activity=T8D W1 surface elevation; Agent=t8d-w1-gatherer |

---

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Elevation patterns are documented in accepted reports (systematic); wiring candidates require reading shipped skill spines/checklists (as-needed) |
| Scope boundary | Included: `docs/research/{notes/theme-8-verify,reports/theme-6*,theme-7*}`, `docs/packs/README.md`, plugin skills `implementation-plan*`, `implementation-execute*`, `.cursor-plugin/plugin.json`. Excluded: inventing new skills on disk; Debug/PR design; T8A/T8B rubric bodies |

---

## 4. Findings

### 4.1 Locked surface C + names + hybrid (confirm vs Theme 6/7)

- `FACT` [E0] Campaign brief §0 locks **D1 = C**: companions named `implementation-plan-verify` + `implementation-execute-verify`; **D2** hybrid orchestration (Plan/Execute orchestrate; companions hold gates/rubrics); **D3** skill-only (no always-on verify rule); **D4** theme naming **Verify gates** (not fat Quality); shared single `implementation-verify` **rejected**; fat Quality **deferred** (D27). [E0: `docs/research/notes/theme-8-verify/campaign-brief.md` §0, §5]
- `FACT` [E0] Packs table already lists Verify gates Wave 1 with those two companion names; Debug/PR is a **separate later stub pack**. [E0: `docs/packs/README.md`]
- `FACT` [E0] Coordinator pin repeats companions + “Not Debug pocket” + do-not-elevate. [E0: `docs/research/notes/theme-8-verify/t8-coordinator-pin.md`]
- `FACT` [E0] Pass-2 earlier lean preferred B; human lock 2026-07-30 chose C and supersedes that lean for campaign constraints. [E0: `docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md` §3.3]
- `FACT` [E0] Theme 6 elevation: single spine skill `implementation-plan` + checklist/template; **skill-only** “plan before implement when non-trivial” — **not** hard always-on rule (#10); Plan owns **light** V1–V8; full validating-plans deferred (#5); thin always-plan rule **not elevated**. [E0: `docs/research/reports/theme-6-plan-pocket.md` elevation decisions + §8]
- `FACT` [E0] Theme 7 elevation: spine `implementation-execute` + **separate supplementary** skill `implementation-execute-subagents` (O-SUB); light evidence folded into spine (O-VFOLD); fuller review deferred; boundaries table puts fuller review/debug/PR later. [E0: `docs/research/reports/theme-7-execute-pocket.md` elevation decisions + §4–§5]
- `FACT` [E0] Shipped Plan handoff points to Execute / Execute-subagents; Execute out-of-scope includes writing the plan and “full Review/Debug packs”; Execute end step is “optional light end-of-plan coherence; fuller review → later”. [E0: `skills/implementation-plan/SKILL.md` Handoffs; `skills/implementation-execute/SKILL.md` Out of scope + spine §5]
- `INFERENCE` [E4] Surface **C** is consistent with Theme 7’s **spine + named supplement** pattern, applied twice for lane-split (plan-validate vs execute-verify), rather than Theme 6’s single-spine-only pocket. Premises: (1) Theme 7 O-SUB shipped a second skill for a distinct mode; (2) brief D1 rejects merging lanes into one `implementation-verify`; (3) D2 keeps Plan/Execute as orchestrators — same “spine owns loop, companion owns specialized gate” idea as Execute→subagents.
- `INFERENCE` [E4] **D3 skill-only** directly continues Theme 6 accepted #10 (no always-on plan rule) and packs README “intelligent / opt-in by default except thin always-on (draft≠SoT)”. Premises: Theme 6 #10; packs README; brief D3.
- `INFERENCE` [E4] Hybrid orchestration (D2) is the correct packaging for Theme 8: companions are **gate holders**, not replacement orchestrators — mirrors how `-subagents` does not replace Execute spine. Premises: brief D2; Execute-subagents “same spine” wording [E0: `skills/implementation-execute-subagents/SKILL.md`].
- `GAP` Plugin manifest does not enumerate skill paths (name/description/keywords only); elevation will not require inventing a skills registry API — layout is filesystem `skills/<name>/SKILL.md` as today. Searched: workspace + local plugin `.cursor-plugin/plugin.json`. Result: no skills array / path list. [E0: both `plugin.json` files]

### 4.2 G3 — Proposed description triggers (candidates)

Candidates for YAML `description:` frontmatter (discoverability). **Not elevated.** Wordsmithing may refine after T8A/T8B atoms stabilize.

#### `implementation-plan-verify`

- `INFERENCE` [E4] Trigger when agent is finishing or QA-ing a durable plan **before** Meta `ready` / execute handoff; when user asks to validate/review a plan; when Plan spine reaches pre-exec after V1–V8 light pass. Premises: brief D5 explicit phase between write-plan and Meta ready; Plan checklist Pre-exec V1–V8 [E0: `implementation-plan-checklist.md`].

**Candidate description (draft text):**

> Validate a Toolbelt implementation plan before execute: Reality + Drift + coverage/actionability, severity verdicts (PASS / PASS WITH NOTES / NEEDS REVISION), hard ambiguity gate, light FR→task coverage and acyclic deps, codebase verification table for non-trivial plans. Use when plan-validate, validate-plan, review-plan before implement, after implementation-plan write, or before Meta ready / implementation-execute. Prefer over jumping straight from draft plan to code.

**Trigger phrases (candidates):** `plan-validate`, `validate plan`, `review plan before implement`, `pre-exec validate`, `NEEDS REVISION` (plan), after `implementation-plan`, before `implementation-execute`.

#### `implementation-execute-verify`

- `INFERENCE` [E4] Trigger for post-green evidence discipline, required fresh quality/faithfulness/readability review (non-trivial + EOP), and end-of-plan light converge — not for writing plans or Debug/PR. Premises: brief D14–D19, G12; Execute deferred fuller review [E0: Theme 7 report §4].

**Candidate description (draft text):**

> Verify Toolbelt plan execution with evidence iron law (IDENTIFY→RUN→READ→VERIFY), post-green faithfulness + readability/coherence review (fresh context when required), and light end-of-plan converge (gap types incl. unrequested; append tasks only). Use when execute-verify, verification-before-completion, post-green review, converge against plan, after task Done-when green, or end-of-plan quality check. Prefer with implementation-execute / implementation-execute-subagents; not for plan writing or PR/Debug packaging.

**Trigger phrases (candidates):** `execute-verify`, `verify before claiming done`, `post-green review`, `converge`, `intent coverage`, `unrequested`, after task green / end-of-plan, with `implementation-execute` / `-subagents`.

- `OPEN` Exact description length / keyword density for Cursor skill matching — no E0 measured this slice. Follow-up: smoke after elevate (optional G11).

### 4.3 G4 — Wiring into Plan / Execute / -subagents (checklist touchpoints)

Hybrid rule (candidate): orchestrator skills **invoke / hand off** to companions at named steps; companions **do not** own Meta ledger or task loop.

#### Plan (`implementation-plan`) — candidate touchpoints

| # | Touchpoint | Today (E0) | Theme 8 candidate wire |
|---|------------|------------|------------------------|
| P1 | Spine step 9 “Pre-exec check (V1–V8)” | Light in-skill [E0: Plan SKILL spine §9] | Keep V1–V8 as **fast local** gate; for non-trivial durable plans → **require** `implementation-plan-verify` before Meta `ready` (D5) |
| P2 | Checklist “Pre-exec (V1–V8)” | Checklist items V1–V8 [E0: plan checklist] | Add checkbox: “Plan-verify companion run (or trivial skip documented)” |
| P3 | Handoffs table | Next = Execute [E0: Plan SKILL Handoffs] | Insert row: plan not yet validated → `implementation-plan-verify`; only then Execute |
| P4 | On NEEDS REVISION | N/A today | Stay in Plan pocket: fix **plan**, re-run companion (D8) — do not start Execute |
| P5 | Status | `ready` means cleared [E0: Plan status vocab] | Candidate: Meta `ready` implies plan-verify PASS or PASS WITH NOTES (or human waive) |

#### Execute (`implementation-execute`) — candidate touchpoints

| # | Touchpoint | Today (E0) | Theme 8 candidate wire |
|---|------------|------------|------------------------|
| E1 | Preconditions §2 “Run Plan V1–V8 lightly” | Light fold [E0: Execute SKILL] | If plan-verify not done and plan non-trivial → `blocked`+`needs-human` or bounce to plan-verify (OPEN which) |
| E2 | Task loop Verify | Command + signal + N=2 [E0: Execute SKILL + checklist] | **Signal verify stays in Execute** (D19/D21); companion not a substitute for N=2 |
| E3 | Post-green (per task) | Implicit continue-when-green | Non-trivial: hand to `implementation-execute-verify` for evidence+faithfulness+readability (D15–D17); trivial: optional |
| E4 | Spine §5 “Optional light end-of-plan” | Deferred fuller review [E0: Execute SKILL] | Promote to **required** light converge + EOP review via companion (D18, G12) |
| E5 | Checklist “End” | Optional light coherence [E0: execute checklist] | Replace/extend: “Execute-verify companion: EOP review + converge (or trivial skip)” |
| E6 | Handoffs | Debug pack later [E0: Execute SKILL] | Add: post-green / converge → `implementation-execute-verify`; leave Debug/PR row as later |

#### Execute-subagents (`implementation-execute-subagents`) — candidate touchpoints

| # | Touchpoint | Today (E0) | Theme 8 candidate wire |
|---|------------|------------|------------------------|
| S1 | Controller §3 “optional fresh task reviewer” | Optional when stakes high [E0: subagents SKILL] | Align with D15/D16: when review required, **fresh** reviewer context; companion owns rubric; controller still owns ledger |
| S2 | Controller §5 “optional light end review” | Deferred fuller [E0: subagents SKILL] | Wire same EOP companion path as Execute spine (G12) |
| S3 | Implementer contract | Verify evidence return [E0: subagents SKILL] | Keep signal verify with implementer/controller; companion reviews **after** green evidence present |
| S4 | Handoffs | Points at execute checklist [E0: subagents SKILL] | Add companion name; do not invent Task API fields |

- `INFERENCE` [E4] Wiring should be **checklist + Handoffs + one spine step each**, not a third orchestrator skill — matches D2 and Theme 7 supplement pattern. Premises: D2; Theme 7 O-SUB; current Handoffs tables.
- `OPEN` Whether plan-verify is mandatory before first Execute critical review, or may run as Execute precondition bounce — decide at integrate/accept.

### 4.4 G2 — Non-trivial threshold candidates (OPEN ok)

Brief: verification table required for non-trivial plans (D12); post-green review required for non-trivial tasks + EOP (D15); trivial skips. Theme 6 already uses “non-trivial → durable `docs/plans/`” vs “trivial one-file tweaks” [E0: Theme 6 #7; Plan SKILL intelligent exception].

**Candidate options (not locked):**

| ID | Option | Plan-verify / verify-table | Execute-verify review | Notes |
|----|--------|----------------------------|------------------------|-------|
| T-A | **Reuse Plan durable threshold** | Required iff writing/updating `docs/plans/…` durable plan | Required for tasks in durable plans; optional for chat-ephemeral one-file | Lowest new ceremony; aligns Theme 6 #7 |
| T-B | **Multi-file / multi-task** | Required if ≥2 files **or** ≥2 tasks | Same | Clear; may under-require single-file risky changes |
| T-C | **Risk flags** | Required if any: public API change, migrations, auth/secrets, multi-package | Same + EOP always for durable plans | Stronger quality; more agent judgment / drift |
| T-D | **Hybrid default** | Default T-A; escalate to required under T-C flags even for “small” plans | Default T-A; EOP converge always for durable plans (D18 already requires light converge) | Likely integrate lean |

- `OPEN` Exact threshold wording for SoT — follow-up at W2/integrate; T8A/T8B may propose rubric-tied defaults. Prefer cite Theme 6 durable-plan language over inventing numeric task counts as law.
- `INFERENCE` [E4] Safest Wave-1 recommendation lean: **T-D** (durable-plan default + risk escalate), with EOP converge always on durable plans per D18. Premises: D12/D15/D18; Theme 6 #7; avoid new numeric SoT (Theme 6 parked numeric paste budgets).

### 4.5 Skill directory layout + checklist naming (candidates)

Observed shipped layout [E0: Glob under `skills/`]:

```text
skills/<skill-name>/SKILL.md
skills/<skill-name>/references/<skill-name>-checklist.md   # Plan, Execute
skills/implementation-plan/references/plan-minimal.md      # extra Plan ref
```

**Proposed (do not create yet):**

```text
skills/implementation-plan-verify/
  SKILL.md
  references/
    implementation-plan-verify-checklist.md
    # optional later: verdict-rubric.md / verification-table.md (only if T8A needs progressive disclosure)

skills/implementation-execute-verify/
  SKILL.md
  references/
    implementation-execute-verify-checklist.md
    # optional later: evidence-iron-law.md / converge-checklist.md / review-dimensions.md (T8B)
```

Naming convention candidate: mirror Execute/Plan — checklist filename = `<skill-name>-checklist.md`.

Orchestrator touchups (post-accept, almost certain per brief §5):

- Edit `implementation-plan` SKILL + `implementation-plan-checklist.md` (wire P1–P5)
- Edit `implementation-execute` SKILL + `implementation-execute-checklist.md` (wire E1–E6)
- Edit `implementation-execute-subagents` SKILL (wire S1–S4)
- Update `docs/packs/README.md` Verify gates row → shipped when elevated
- Optionally refresh plugin `description`/`keywords` to mention verify companions (no skills path API today)

- `FACT` [E0] No `implementation-*-verify` directories exist yet under local toolbelt skills. [E0: Glob skills list]
- `INFERENCE` [E4] Keep companions **thin**: checklist + short SKILL; push long rubrics to `references/` progressive disclosure (Anthropic skill pattern already used by Plan/Execute). Premises: shipped layout; brief “thin companions”; Theme 6/7 checklist pattern.

### 4.6 G10 — Debug/PR leftover list only (Theme 8 does NOT own)

Leftovers for **later Debug / PR / workflow** stub pack — list only; **no pocket design** here. Sources: brief non-goals + D24/D27; Theme 7 boundaries; packs README; Execute out-of-scope.

| Leftover | Why not Theme 8 |
|----------|-----------------|
| PR create/finish / merge workflows | Brief non-goal; packs stub Debug/PR |
| Copilot PR-skills packaging | D24 defer |
| Git/worktree/commit ceremony as SoT | D25 park; Theme 6/7 non-imports |
| Systematic debugging / root-cause playbooks | Theme 8 = Plan/Execute verify extensions only |
| Fat Review/Debug pocket / multi-skill Quality pack | D27 defer; option D deferred |
| Multi-consultant “council” ceremony | D26 park (keep verification-table **atom** in plan-verify) |
| TDD auditor as law | D22 park |
| Foreign CLI deps (OpenSpec/Spec Kit/Superpowers runtime) | D23 park |
| Full requesting-code-review / ship workflows beyond fresh post-green rubric | Theme 7 deferred “fuller review”; Theme 8 takes light-to-medium layer only |
| Bugbot / CI babysit / merge-queue automation | Outside Verify gates framing |

- `FACT` [E0] Packs README: Debug/PR/workflow = stub, separate later pack, not Theme 8. [E0: `docs/packs/README.md`]
- `FACT` [E0] Theme 7 acceptance checklist still open: “Later: review home (pocket vs touchups) — deferred”. [E0: Theme 7 report §6]

### 4.7 G12 — Converge home = `implementation-execute-verify`

- `FACT` [E0] Brief deep gap G12: converge home = **`implementation-execute-verify`** (follows D1=C; deep may refine steps). D18: required light converge; gap types incl. **unrequested**; append tasks; no silent plan rewrite; no code edits in converge pass. D19: keep signal verify vs intent coverage split. [E0: campaign-brief §0]
- `FACT` [E0] Pass-2/3: Spec Kit converge atoms (append-only; unrequested) cited as E1 in scoping notes — transferable atom, not CLI dependency. [E0: pass2 §3.2; pass3 inventory]
- `INFERENCE` [E4] Confirm converge lives in **execute-verify** companion (not plan-verify, not Debug): it assesses **code vs plan/intent after implementation**, while plan-verify assesses **plan quality before code**. Premises: D18/D19/G12; Spec Kit analyze-vs-converge split in pass3.
- `INFERENCE` [E4] Refine steps (candidate only; T8B owns detail): (1) after all required tasks signal-green **or** at explicit EOP; (2) classify gaps missing/partial/contradicts/unrequested vs approved plan+design; (3) append remediation tasks to plan ledger; (4) no app code edits in converge pass; (5) re-enter Execute loop for appended tasks; (6) do not silently rewrite Goal/Done-when. Premises: D18; Theme 7 no silent plan rewrite [E0: execute checklist Escalate].

### 4.8 Elevation order candidates (post report accept only)

Brief §4: Integrate → draft report → accept → elevate companions. Brief §5 candidates.

**Recommended order candidate (post-accept):**

1. Accept Theme 8 report (method guidance + elevation decisions table) — **gate**
2. Elevate `implementation-plan-verify` (SKILL + checklist + optional refs)
3. Elevate `implementation-execute-verify` (SKILL + checklist + optional refs) — includes converge (G12)
4. Strengthen Plan orchestrator (SKILL + checklist wire P1–P5; keep V1–V8 light)
5. Strengthen Execute orchestrator (SKILL + checklist wire E2–E6; preserve N=2)
6. Strengthen Execute-subagents (S1–S4; fresh reviewer alignment)
7. Update `docs/packs/README.md` Verify gates → shipped; optional plugin description/keywords
8. Explicitly **do not** elevate: always-on verify rule (D3); fat Quality; shared `implementation-verify`; Debug/PR surfaces

Alternative order: 4–6 before 2–3 (wire-first) risks dangling handoffs — prefer companions-first then wires (like Theme 7 elevating both skills then checklist alignment).

- `INFERENCE` [E4] Prefer companions-first then orchestrator wires so Handoffs targets exist on disk. Premises: Theme 7 elevated both skills together; brief §5 “almost certain” strengthen Plan/Execute.

### 4.9 Risks

| Risk | Mechanism | Mitigation candidate |
|------|-----------|----------------------|
| **Ceremony overload** | V1–V8 + plan-verify + Execute critical review + signal verify + post-green + converge | Keep V1–V8 **light**; companions for graded/non-trivial; trivial skips (G2); D26 park council |
| **Skill sprawl** | Two new skills + existing Plan/Execute/subagents | Hard cap: **two** verify companions only (D1); no always-on rule (D3); no fat Quality (D27); progressive disclosure in `references/` |
| **Duplicate gates vs V1–V8** | Plan-verify redoes V1–V8 | Position plan-verify as **deepening** layer (coverage, taxonomy, verification table, verdicts); V1–V8 remain fast local preflight |
| **Duplicate gates vs Execute Done-when / N=2** | Companion re-runs commands as sole gate | D19/D21: signal verify + N=2 stay in Execute; companion adds evidence iron-law audit + faithfulness/readability + converge |
| **Lane confusion with Debug/PR** | Agents treat Theme 8 as PR pack | Packs README + skill Out of scope + G10 leftovers explicit |
| **Orchestrator vs companion ownership fight** | Companion mutates Meta/tasks incorrectly | D2: Plan/Execute/-subagents own ledger/loop; companions return verdicts / append-task proposals only |

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | C + hybrid + skill-only matches Theme 6/7 elevation precedent | confirmed (for campaign constraints) | §4.1 FACTs + INFERENCEs |
| H2 | Theme 7 `-subagents` is the closest packaging analog for “companion holds specialized mode” | confirmed | Theme 7 O-SUB; subagents SKILL |
| H3 | Non-trivial ≈ durable plan (+ risk escalate) avoids new numeric SoT | open | G2 options T-A/T-D; Theme 6 #7 |
| H4 | Converge-in-execute-verify is stable under D1=C | confirmed (brief lock; steps OPEN to T8B) | G12; D18 |
| H5 | Always-on verify rule would break Theme 6 #10 / packs opt-in norm | confirmed as reject | D3; Theme 6 #10 |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Surface A/B vs C | Pass-2 lean prefer B | Human lock D1=C 2026-07-30 | Prefer brief §0 (campaign constraint); C supersedes B lean |
| Fuller review home | Theme 7 “later review/debug” | Theme 8 execute-verify takes light-medium layer | Theme 8 owns post-green + converge companions; Debug/PR leftovers remain later (G10) |
| Plan-validate naming | Pass-2 `…-plan-validate` option text | Locked names `…-plan-verify` | Use locked names (D1) |

---

## 7. Gaps & OPEN

- G1 rubric wording — **T8A/T8B** (not designed here)
- G2 exact non-trivial threshold — **OPEN** with options T-A…T-D; lean T-D
- G3 description final copy — candidates above; optional G11 smoke after elevate
- G4 bounce behavior when Execute starts without plan-verify — **OPEN**
- G5–G9 — T8C / other tracks
- G10 — leftover **list** provided; pocket design parked
- G11 — optional live E0 trials after elevate
- G12 — home confirmed; step detail refine → T8B
- Plugin skill-discovery behavior unmeasured this slice

---

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] **Elevation recommendation for coordinator:** proceed on locked **C** — elevate two thin companions after report accept; hybrid wires into Plan/Execute/-subagents; skill-only; no always-on rule; no shared `implementation-verify`; no Debug/PR design in Theme 8.
- `INFERENCE` [E4] Closest precedent: Theme 7 spine + named supplement; Theme 6 skill-only + light in-spine checks that Theme 8 **deepens** via companions rather than deleting.
- `INFERENCE` [E4] Integrate should decide G2 (lean T-D) and G4 Execute-without-verify bounce before elevation checkboxes are ticked.

---

## 9. Source list (deduped)

1. `docs/research/notes/theme-8-verify/campaign-brief.md` [E0]
2. `docs/research/notes/theme-8-verify/t8-coordinator-pin.md` [E0]
3. `docs/packs/README.md` [E0]
4. `docs/research/reports/theme-6-plan-pocket.md` (accepted) [E0]
5. `docs/research/reports/theme-7-execute-pocket.md` (accepted) [E0]
6. `docs/research/notes/theme-8-verify/scope-normal-pass1.md` [E0]
7. `docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md` [E0]
8. `docs/research/notes/theme-8-verify/scope-normal-pass3-github-web.md` [E0]
9. `skills/implementation-plan/SKILL.md` + `references/implementation-plan-checklist.md` [E0]
10. `skills/implementation-execute/SKILL.md` + `references/implementation-execute-checklist.md` [E0]
11. `skills/implementation-execute-subagents/SKILL.md` [E0]
12. `.cursor-plugin/plugin.json` (workspace + local plugin) [E0]
13. `docs/templates/research-note.md` [E0]
