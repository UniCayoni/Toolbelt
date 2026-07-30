---
title: "T8B W1 — Execute verification companion (`implementation-execute-verify`)"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [t8b-w1-gatherer]
depth: deep
stop_reason: wave1_slice_coverage
aligned_with:
  - docs/research/notes/theme-8-verify/campaign-brief.md
  - docs/research/notes/theme-8-verify/t8-coordinator-pin.md
  - docs/research/reports/theme-7-execute-pocket.md
  - skills/implementation-execute/SKILL.md
  - skills/implementation-execute-subagents/SKILL.md
supersedes: null
---

# T8B W1 — What `implementation-execute-verify` should contain

**Using `research-protocol`**.

**Status:** `draft`. Not Verify SoT. Design atoms only — do not elevate skills from this note.  
**Identity:** Theme 8 = missing verification **extension** of shipped Execute (companion `implementation-execute-verify`). Execute skills remain orchestrators (D2). **Not** the Debug/PR pocket (D24, packs stub).

---

## 1. Scope

| Field | Value |
|-------|-------|
| Question / goal | What should `implementation-execute-verify` contain for **post-task** and **end-of-plan** verification? |
| In scope | Evidence iron law; post-green quality/faithfulness/readability review; review dimensions; light converge; signal-vs-intent split; Theme 7 HITL + frozen N=2; wiring from Execute/-subagents; non-trivial threshold candidates; proposed skill layout (design); transferable vs park |
| Out of scope | Designing Debug/PR pack; re-litigating N=2; elevating skills; T8A plan-validate; OpenSpec/Spec Kit/Superpowers as runtime deps; inventing Cursor Task APIs |
| Track | T8B only (Wave 1) |

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign-brief, coordinator pin, pass 1–3, Theme 7 report, Execute skills + checklist, packs README); WebFetch (Superpowers verification-before-completion + requesting-code-review + code-reviewer.md; Spec Kit converge.md; OpenSpec openspec-verify-change; Claude Code best-practices); `gh api` for raw download URLs |
| Corpora / URLs searched | See §9 Source list |
| Queries (exact) | `gh api repos/obra/superpowers/contents/skills/verification-before-completion/SKILL.md`; same for `requesting-code-review`; `github/spec-kit/.../converge.md`; `Fission-AI/OpenSpec/.../openspec-verify-change/SKILL.md`; WebFetch `https://code.claude.com/docs/en/best-practices` |
| What was *not* searched | Live E0 Toolbelt execute-verify trials (G11); full HCI code-review literature; Debug/PR packaging deep-design; validating-plans deep refs (T8A/T8C); exhaustive Superpowers fork tree |
| Depth | deep |
| Waves / stop_reason | Wave 1 slice T8B; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←Theme 7 accepted law + Tier A vendor skills; Activity=T8B W1 gather; Agent=t8b-w1-gatherer |

---

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Theme 7 + shipped skills = E0 law inventory; Tier A vendor docs = E1 atom extraction; brief §0 = campaign constraints (not elevated SoT) |
| Scope boundary | Execute pocket + companion design; park Debug/PR, CLI deps, fat Quality, TDD/git SHA ceremony |

---

## 4. Findings

### 4.0 Baseline — what Execute already owns (E0)

- `FACT` [E0] Execute spine: load → critical review → statused task loop → Done-when verify with evidence → escalate on blocked/major deviation → continuous when green. [E0: `docs/research/reports/theme-7-execute-pocket.md` §3 — accessed 2026-07-30]
- `FACT` [E0] Task verify: run listed command → expected signal; keep evidence; no bare “done” claims (**evidence-before-completion**). On mismatch: enhanced local fix up to **N=2**, then `blocked`+`verify-fail`. [E0: `skills/implementation-execute/SKILL.md` Spine step 3 — accessed 2026-07-30]
- `FACT` [E0] N=2 verify retries are **accepted Theme 7 law** (O-N). [E0: Theme 7 report Elevation O-N — accessed 2026-07-30]
- `FACT` [E0] HITL escalate reasons: `intent-gap` \| `verify-fail` \| `needs-human` \| **major deviation** (File map / Interfaces / deps / Never·Do-not / Goal·Done-when rewrite / irreversible / drive-by). Continue when green — no per-task HITL. [E0: `implementation-execute/SKILL.md` Spine steps 3–4]
- `FACT` [E0] End-of-plan today: **optional** light coherence check; fuller review deferred. Checklist: “Optional light coherence note; fuller review deferred.” [E0: `implementation-execute/SKILL.md` step 5; `references/implementation-execute-checklist.md` End]
- `FACT` [E0] Subagents mode: optional fresh **task reviewer** “for spec+quality when stakes are high”; after all tasks optional light end review (fresh context); fuller review later. [E0: `implementation-execute-subagents/SKILL.md` Controller steps 3–5]
- `FACT` [E0] Packs: Verify gates = Theme 8 Plan/Execute extensions; Debug/PR = **separate later pack**. [E0: `docs/packs/README.md` — accessed 2026-07-30]
- `FACT` [E0] Brief locks for T8B: D14–D21, D24–D27; G12 converge home = `implementation-execute-verify`. [E0: `campaign-brief.md` §0]

### 4.1 Evidence iron law (IDENTIFY→RUN→READ→VERIFY) + Done-when + frozen N=2

- `FACT` [E1] Superpowers **Iron Law**: no completion claims without fresh verification evidence. Gate: **IDENTIFY** (what command proves claim) → **RUN** (full fresh command) → **READ** (full output, exit code, failures) → **VERIFY** (output confirms claim) → only then claim. Skip any step = not verifying. [E1: obra/superpowers `skills/verification-before-completion/SKILL.md` — https://raw.githubusercontent.com/obra/superpowers/main/skills/verification-before-completion/SKILL.md — accessed 2026-07-30]
- `FACT` [E1] Same skill bans “should / probably / seems to / looks” and satisfaction language before verification; requirements met needs checklist ≠ tests-only. [E1: verification-before-completion — Red Flags + Common Failures table]
- `FACT` [E1] Claude Code: give a runnable check producing pass/fail; agent runs check, reads result, iterates; show evidence (command + output), not bare assertion; “If you can’t verify it, don’t ship it.” [E1: https://code.claude.com/docs/en/best-practices — “Give Claude a way to verify its work” — accessed 2026-07-30]
- `FACT` [E0] Toolbelt already folds a **light** form: Done-when Verify command + expected signal + evidence kept; ban bare done. [E0: `implementation-execute/SKILL.md`]
- `INFERENCE` [E4] Companion should **make the iron law explicit** (IDENTIFY→RUN→READ→VERIFY wording + ban should/looks) as a discoverable gate invoked from the orchestrator — not replace Done-when grammar. Premises: (1) D14; (2) Superpowers gate [E1]; (3) Execute already runs command+signal [E0]; (4) D2 hybrid orchestration.
- `INFERENCE` [E4] Relation to N=2: iron law governs **how** a verify attempt is evidenced; N=2 governs **how many** enhanced local fix cycles before `verify-fail`. Companion **must not** change N. Premises: Theme 7 O-N [E0]; brief D21 frozen; campaign non-goal “re-litigate N=2”.
- `CLAIM` [E0 constraint] **N=2 is FROZEN** for Theme 8 — cite Theme 7; do not propose alternate N. [E0: campaign-brief D21; Theme 7 O-N]

### 4.2 Post-green quality / readability / faithfulness review

- `FACT` [E1] Claude: before treating work done, **adversarial review** in fresh subagent context — reviewer sees only diff + criteria (not implementer reasoning); can check against plan; flag only gaps that affect correctness or stated requirements (avoid over-engineering chase). [E1: Claude best-practices — “Add an adversarial review step” — accessed 2026-07-30]
- `FACT` [E1] Claude also: Writer/Reviewer pattern — fresh context improves review (reviewer not biased toward code it wrote). [E1: Claude best-practices — multi-session quality workflows]
- `FACT` [E1] Superpowers `requesting-code-review`: dispatch reviewer with plan/requirements + precise context (**never** session history); mandatory after each task in subagent-driven development / major feature / before merge; fix Critical immediately, Important before proceed; severity Critical / Important / Minor. [E1: obra/superpowers `skills/requesting-code-review/SKILL.md` — accessed 2026-07-30]
- `FACT` [E1] Reviewer template checks: plan alignment, code quality (SoC, errors, types, DRY, edges), architecture, testing, production readiness; read-only review; clear verdict. [E1: obra/superpowers `skills/requesting-code-review/code-reviewer.md` — accessed 2026-07-30]
- `FACT` [E0] Brief D15–D16: post-green quality/readability review **required** for non-trivial tasks + end-of-plan; **optional** on trivial; when required → **fresh** reviewer context (subagent or fresh chat). [E0: campaign-brief §0]
- `INFERENCE` [E4] Companion owns the **post-green** layer: after signal verify green, run (or require) review against faithfulness + readability/coherence; orchestrator decides *when* to call companion per threshold. Premises: D15–D16; Execute’s “optional” end check [E0]; Claude + Superpowers fresh review [E1].
- `INFERENCE` [E4] Post-green review is **not** a second N=2 command-retry loop. Findings map: Critical/Important faithfulness or correctness → agent-fix inside Files/Interfaces (or escalate if major-deviation); WARNING/NIT agent-fixable unless escalate (D20). Premises: D20; Theme 7 major-deviation checklist [E0]; Superpowers severity triage [E1].
- `OPEN` Exact severity vocabulary for execute-verify (Superpowers Critical/Important/Minor vs OpenSpec CRITICAL/WARNING/SUGGESTION vs Plan-side PASS WITH NOTES). Follow-up: G1 + T8C/T8D. See §7.

### 4.3 Review dimensions (evidence + faithfulness + readability/coherence)

- `FACT` [E1] OpenSpec `openspec-verify-change` structures post-implement verify as three dimensions: **Completeness** (tasks/spec coverage), **Correctness** (requirement/scenario mapping), **Coherence** (design adherence + pattern consistency); issues CRITICAL / WARNING / SUGGESTION. [E1: Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md` — https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/skills/openspec-verify-change/SKILL.md — accessed 2026-07-30]
- `FACT` [E1] OpenSpec heuristics: Completeness = objective checklist; Correctness = keyword/path inference (not perfect certainty); Coherence = glaring inconsistencies, don’t nitpick style; prefer lower severity when uncertain. [E1: openspec-verify-change — Verification Heuristics]
- `FACT` [E0] Brief D17: Toolbelt dimensions = **evidence + faithfulness + readability/coherence**; OpenSpec Completeness/Correctness/Coherence as **labels only** (no CLI dep — D23). [E0: campaign-brief §0]
- `INFERENCE` [E4] Proposed Toolbelt mapping (labels only, not OpenSpec dependency):

  | Toolbelt dimension (D17) | OpenSpec label (alias only) | What to check |
  |--------------------------|----------------------------|---------------|
  | **Evidence** | (no OpenSpec twin; Superpowers/Claude gate) | IDENTIFY→RUN→READ→VERIFY; Done-when signal matched with kept output |
  | **Faithfulness** | Completeness + Correctness (labels) | Plan/task Done-when + Files/Interfaces/Do-not + design/ADR decisions; no invent; no Goal rewrite |
  | **Readability / coherence** | Coherence (label) | Clear boundaries, naming, no clever opacity, pattern fit, no drive-by; design adherence |

  Premises: D17; OpenSpec three dims [E1]; Superpowers evidence gate [E1]; Theme 7 major-deviation / do-not-invent [E0].
- `GAP` Full readability rubric wording (G1) — Osmani chunks cited in pass 2 not re-probed this gather; use pass-2 CLAIM as discovery only until T8C corroborates. Searched: OpenSpec Coherence section + Superpowers quality bullets. Result: transferable bullets exist; Toolbelt house prose OPEN.

### 4.4 Required light converge at plan end

- `FACT` [E1] Spec Kit `converge`: assess codebase vs spec/plan/tasks; classify gaps **`missing` / `partial` / `contradicts` / `unrequested`**; append remediation tasks only; **MUST NOT** modify spec/plan, rewrite/renumber/delete existing tasks, or edit application code; if clean → leave tasks file byte-for-byte unchanged. [E1: github/spec-kit `templates/commands/converge.md` — https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md — accessed 2026-07-30]
- `FACT` [E1] Converge: `unrequested` = code not called for by artifacts — surfaced for awareness; does not delete code; appends task to review/justify or remove. [E1: converge.md §4 gap types]
- `FACT` [E0] Brief D18: end-of-plan **required light converge** — gap types incl. unrequested; append tasks; no silent plan rewrite; no code edits in converge pass. G12: converge home = `implementation-execute-verify`. [E0: campaign-brief §0]
- `FACT` [E3/E2 discovery] Pass 3 notes rune-kit split: “verification asks does it build; converge asks is everything promised in the code?” [E3: `scope-normal-pass3-github-web.md` Tier B — discovery; deepen optional in T8C]
- `INFERENCE` [E4] Companion end-of-plan phase (light Toolbelt converge):
  1. Load intent: approved plan (Goal, tasks, Done-when, File map, Always/Block/Never, Out of scope) + accepted design/ADR pointers — **not** Spec Kit path ceremony.
  2. Assess code in plan-named scope; emit findings with gap type ∈ {missing, partial, contradicts, unrequested}.
  3. Present severity-graded summary **before** any append.
  4. If actionable findings → **append** new tasks to plan ledger (or clearly labeled Convergence section); never silent rewrite of Goal/existing tasks/design.
  5. **No application code edits** in the converge pass — implementer/orchestrator runs appended tasks via Execute spine afterward.
  6. If no findings → report converged; leave plan file unchanged (no empty Convergence header).
  Premises: D18; Spec Kit converge [E1]; Theme 7 do-not invent / no silent plan rewrite [E0].
- `OPEN` Append format for Toolbelt `docs/plans/` (checkbox section vs Status rows; ID scheme). Follow-up: T8D + plan-minimal touch after accept.
- `OPEN` Whether post-task converge is ever required vs EOP-only. Brief requires EOP; Superpowers reviews every subagent task — conflict logged §6.

### 4.5 Keep split: signal verify vs intent coverage

- `FACT` [E0] Pass 3 insight: two verify problems — evidence-before-claim **and** intent coverage (converge) **and** quality/coherence review. [E0: `scope-normal-pass3-github-web.md` §4]
- `FACT` [E0] Brief D19: keep split signal verify (“builds?”) vs intent coverage (“promised?”). [E0: campaign-brief D19]
- `INFERENCE` [E4] Companion should **name two lanes** (and not collapse them):

  | Lane | Question | Primary mechanism | When |
  |------|----------|-------------------|------|
  | **Signal verify** | Does the Done-when command produce the expected signal? | Iron law + Theme 7 Done-when run + N=2 | Every task (already orchestrator; companion strengthens wording/checklist) |
  | **Intent coverage** | Does code satisfy plan/design promises without unrequested scope? | Light converge + faithfulness dimension | Required at EOP; optional/required post-task per non-trivial threshold |

  Quality/readability sits as a **third check** after signal green (D15), not as a substitute for either lane. Premises: D19; Spec Kit converge [E1]; OpenSpec Completeness/Correctness [E1]; Execute Done-when [E0].

### 4.6 HITL — Theme 7 only

- `FACT` [E0] Brief D20: HITL = Theme 7 (blocked / major deviation); WARNING/NIT agent-fixable unless escalate. [E0: campaign-brief D20]
- `FACT` [E0] Theme 7 escalate set is the SoT for stop/ask — companion must not invent a parallel HITL ceremony (e.g. mandatory merge gate, PR approval, council). [E0: Theme 7 report Boundaries §4; D24 park Copilot PR]
- `INFERENCE` [E4] Execute-verify findings routing:
  - Signal mismatch after N=2 → orchestrator `blocked`+`verify-fail` (Theme 7) — companion does not redefine N.
  - Review finds work outside Files/Interfaces / unrequested that would require scope expand → **major deviation** HITL.
  - Review finds agent-fixable quality/faithfulness gaps inside task bounds → fix + re-evidence; no human pause.
  - Converge appends tasks → continue Execute loop (continuous when green); human only if append reveals intent-gap / needs-human.
  Premises: D20; Theme 7 spine [E0]; Spec Kit append-then-implement [E1].

### 4.7 Wiring from `implementation-execute` and `-subagents`

- `FACT` [E0] Hybrid orchestration (D2): Plan/Execute remain orchestrators; companions hold validate/verify gates + rubrics. Skill-only, no always-on verify rule (D3). [E0: campaign-brief D2–D3]
- `FACT` [E0] Current Handoffs tables do **not** list an execute-verify companion (gap G4). [E0: both Execute SKILL.md Handoffs — accessed 2026-07-30]
- `INFERENCE` [E4] Proposed wiring (design only — strengthen orchestrators post-accept):

  | Orchestrator hook | Call companion for | Notes |
  |-------------------|--------------------|-------|
  | After task Verify green (non-trivial) | Post-green review (evidence confirm + faithfulness + readability/coherence) | Fresh reviewer when D15/D16 required; subagents already mention optional task reviewer — promote to companion invocation |
  | After task Verify green (trivial) | Skip or optional light self-check | Threshold G2 |
  | Before claiming task `done` | Iron-law checklist (IDENTIFY→RUN→READ→VERIFY) | May be inline reference in companion; orchestrator must not mark done without it |
  | After all required tasks done (EOP) | Required: post-green plan-level review **and** light converge | G12 home |
  | On review Critical inside bounds | Fix → re-run signal verify (consumes same N=2 budget if signal breaks) | Do not invent new retry counter |
  | On blocked / major deviation | Escalate per Theme 7 — companion reports; does not redesign HITL | D20 |

  Premises: D2, D14–D18, G4, G12; subagents optional reviewer [E0].
- `INFERENCE` [E4] Description triggers (G3, for T8D): discoverable phrases like “execute-verify”, “post-green review”, “converge plan”, “verify before done”, “end-of-plan verification” — companion loaded when those apply; Execute skills point to it in Handoffs + spine steps 3/5. Premises: D3 skill-only; G3 OPEN.
- `OPEN` Exact prose patches to Execute SKILL.md / checklist / subagents (wording). Follow-up: elevation after report accept.

### 4.8 Non-trivial threshold candidates (OPEN ok)

- `FACT` [E0] G2 = non-trivial threshold still deep-only gap; D12 uses non-trivial for plan verification table (Plan lane); D15 uses non-trivial for execute post-green. [E0: campaign-brief G2, D12, D15]
- `FACT` [E1] Superpowers: review mandatory after each task in subagent-driven development; optional when “simple” is called out as rationalization to never skip. [E1: requesting-code-review — When + Red Flags]
- `FACT` [E1] Claude: skip heavy planning for typo/log/rename; planning useful when multi-file / uncertain / unfamiliar. [E1: Claude best-practices — plan-mode overhead note]
- `OPEN` **Non-trivial threshold candidates** for requiring post-green review (pick at accept / T8D — not locked here):

  | ID | Candidate | Signal |
  |----|-----------|--------|
  | NT1 | Multi-file task (`Files` length ≥ 2) | E0 plan grammar |
  | NT2 | Touches Interfaces / public shape | Theme 7 major-deviation adjacency |
  | NT3 | New dependency or toolchain mentioned | Theme 7 major-deviation list |
  | NT4 | Plan marks task non-trivial / review-required | Explicit plan flag (needs template touch) |
  | NT5 | Subagent-driven execute mode | Superpowers “after each task” [E1] — may be stricter |
  | NT6 | End-of-plan always non-trivial for review+converge | D15 + D18 — EOP always required regardless of per-task triviality |

  Premises: D15–D16; Claude small-task skip [E1]; Superpowers always-review tension [E1] — see Conflicts.
- `INFERENCE` [E4] Safe interim lean (not SoT): **EOP always** runs review+converge; per-task review required if NT1∨NT2∨NT4∨NT5; else optional. Premises: D15; D18; reduce over-ceremony on one-line fixes.

### 4.9 Proposed skill layout (design only — do NOT create)

- `INFERENCE` [E4] Proposed layout for future elevation (mirrors Execute packaging; **not** created this wave):

  ```text
  skills/implementation-execute-verify/
    SKILL.md                          # announce; when; phases; handoffs; anti-patterns
    references/
      execute-verify-checklist.md     # iron law + post-green + EOP converge checklist
      review-dimensions.md            # evidence / faithfulness / readability-coherence rubrics (G1)
      converge-light.md               # gap types; append contract; no-code / no-silent-rewrite
  ```

  **SKILL.md phases (candidate spine):**
  1. **Signal evidence gate** — IDENTIFY→RUN→READ→VERIFY; ban should/looks; consume task Verify from plan.
  2. **Post-green review** (when required) — fresh context; dimensions evidence confirm + faithfulness + readability/coherence; severity triage; agent-fix vs Theme 7 escalate.
  3. **End-of-plan light converge** — gap taxonomy; append tasks; no silent rewrite; no code edits in this pass.
  4. **Handoff back** — orchestrator continues Execute loop or reports converged / blocked.

  Premises: D1=C companion name; D2 hybrid; D14–D19; Theme 7 checklist pattern [E0].
- `CLAIM` [E0 constraint] Do **not** create these files until report accept + elevate. [E0: coordinator pin hard constraints; draft-is-not-sot]

### 4.10 Transferable vs park (execute-verify lens)

| Atom / surface | Stance | Grade | Notes |
|----------------|--------|-------|-------|
| IDENTIFY→RUN→READ→VERIFY + ban should/looks | **Transfer** | E1 | Into companion evidence gate; strengthen Execute wording |
| Done-when command + expected signal | **Keep (Execute)** | E0 | Orchestrator owns run; companion owns explicit iron-law checklist |
| N=2 verify retries | **Frozen keep** | E0 | Do not re-litigate (D21) |
| Fresh adversarial / reviewer subagent | **Transfer** | E1 | D16; Claude + Superpowers |
| Review severity Critical/Important/Minor | **Transfer light** | E1 | Map to agent-fix vs Theme 7 HITL; exact vocab OPEN (G1) |
| OpenSpec Completeness/Correctness/Coherence | **Labels only** | E1 | D17; park CLI (D23) |
| Spec Kit gap types + append-only converge | **Transfer** | E1 | D18; park Spec Kit paths/hooks/CLI |
| Git SHA base/head ceremony as SoT | **Park** | E1→park | D25; optional aid for reviewers, not law |
| “Before merge to main” / PR mandatories | **Park → Debug/PR** | E1→D24 | requesting-code-review merge gate |
| Copilot PR-skills packaging | **Defer** | E0 | D24 |
| TDD red-green as verify law | **Park** | E1 | verification-before-completion TDD section; D22 |
| Multi-consultant council | **Park** | E0 | D26 |
| Fat Quality pocket | **Defer** | E0 | D27 |
| Debug/PR pack design | **Park / leftover list only** | E0 | D24; G10 for T8D — T8B does not design |
| OpenSpec/Spec Kit/Superpowers runtime dep | **Park** | E0 | D23 |
| Always-on verify rule | **No** | E0 | D3 |

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Companion should explicit-ize iron law without replacing Done-when | confirmed (design lean) | D14; Superpowers [E1]; Execute [E0] |
| H2 | Post-green review + EOP converge close Theme 7 deferred “optional light / fuller later” | confirmed (design lean) | D15–D18; Theme 7 step 5 [E0] |
| H3 | Signal verify and intent coverage must stay split | confirmed (design lean) | D19; Spec Kit + pass 3 [E1/E0] |
| H4 | Per-task review always-on (Superpowers SDD) fits Toolbelt | revised → OPEN | Conflicts with trivial skip (D15) and Claude small-task skip [E1] |
| H5 | Converge append format can reuse plan Status rows unchanged | open | Needs plan-minimal design (T8D) |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Review frequency | Superpowers: mandatory after each SDD task [E1] | Brief D15: required non-trivial + EOP; optional trivial [E0] | Prefer **brief D15** as campaign constraint; treat Superpowers “every task” as stricter mode when using `-subagents` (NT5 candidate) — OPEN exact rule |
| Reviewer context packaging | Superpowers: git SHA range as primary diff handle [E1] | Spec Kit converge: no git/history; present-state vs artifacts [E1] | Transfer **fresh context + plan/criteria**; SHA optional aid; D25 parks SHA ceremony as SoT; converge stays present-state |
| HITL surface | Superpowers “before merge” [E1] | Theme 7 blocked/major deviation only [E0]; D20/D24 | Prefer Theme 7; park merge/PR |
| Dimension naming | OpenSpec Completeness/Correctness/Coherence [E1] | Brief D17 evidence + faithfulness + readability/coherence [E0] | Prefer D17 names; OpenSpec as aliases only |
| Verify retry N | (none in Theme 8) | Theme 7 O-N = 2 [E0] | **No conflict — frozen**; do not open |

---

## 7. Gaps & OPEN

| ID | Item | Follow-up |
|----|------|-----------|
| G1 | Rubric wording for faithfulness + readability/coherence | T8C/T8D; house prose |
| G2 | Non-trivial threshold lock (NT1–NT6 candidates above) | Accept gate / T8D |
| G3 | Skill description triggers | T8D |
| G4 | Exact Execute / -subagents wiring prose | Post-accept elevation |
| G12 | Converge home confirmed companion — append **format** still OPEN | T8D + plan-minimal |
| OPEN-T8B-1 | Severity vocab unify across Plan-verify vs Execute-verify | Integrator |
| OPEN-T8B-2 | Post-task converge ever required? (lean: EOP-only) | W2 / accept |
| OPEN-T8B-3 | Live E0 trial of companion checklist on a sample plan | G11 optional |
| GAP | Osmani readability bullets not re-fetched this gather | T8C may corroborate pass-2 chunk_ids |

---

## 8. Implications (INFERENCE only — not design law)

- `INFERENCE` [E4] Elevate path: accept Theme 8 report → create `implementation-execute-verify` → patch Execute + `-subagents` Handoffs/spine to **require** companion at EOP and at non-trivial post-green; keep N=2 and HITL unchanged. Premises: §4.1–4.7; D1–D3.
- `INFERENCE` [E4] Until elevation, agents should not treat this draft as mandatory procedure (`draft-is-not-sot`). Premises: coordinator pin; PROTOCOL.
- `INFERENCE` [E4] Debug/PR leftovers for T8D G10 list (not designed here): merge gates, Copilot PR skills, SHA ceremony as SoT, finish-branch packaging, production-readiness checklist depth from Superpowers reviewer template. Premises: §4.10 park rows; D24–D25.

---

## 9. Source list (deduped)

1. [E0] `docs/research/notes/theme-8-verify/campaign-brief.md` — D14–D21, D24–D27, G1–G12 — accessed 2026-07-30  
2. [E0] `docs/research/notes/theme-8-verify/t8-coordinator-pin.md` — accessed 2026-07-30  
3. [E0] `docs/research/notes/theme-8-verify/scope-normal-pass1.md` / `pass2-expand.md` / `pass3-github-web.md` — accessed 2026-07-30  
4. [E0] `docs/research/reports/theme-7-execute-pocket.md` (accepted) — accessed 2026-07-30  
5. [E0] `skills/implementation-execute/SKILL.md` + `references/implementation-execute-checklist.md` — accessed 2026-07-30  
6. [E0] `skills/implementation-execute-subagents/SKILL.md` — accessed 2026-07-30  
7. [E0] `docs/packs/README.md` — accessed 2026-07-30  
8. [E1] obra/superpowers `verification-before-completion/SKILL.md` — https://raw.githubusercontent.com/obra/superpowers/main/skills/verification-before-completion/SKILL.md — accessed 2026-07-30  
9. [E1] obra/superpowers `requesting-code-review/SKILL.md` + `code-reviewer.md` — accessed 2026-07-30  
10. [E1] github/spec-kit `templates/commands/converge.md` — https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md — accessed 2026-07-30  
11. [E1] Fission-AI/OpenSpec `skills/openspec-verify-change/SKILL.md` — accessed 2026-07-30  
12. [E1] Claude Code best practices — https://code.claude.com/docs/en/best-practices — accessed 2026-07-30  

---

## 10. Coordinator return — key atoms + OPENs

### Key atoms (transfer into companion)

1. **Evidence iron law** — IDENTIFY→RUN→READ→VERIFY; ban should/looks; sits **on top of** Done-when (does not replace); **N=2 frozen**.  
2. **Post-green review** — required non-trivial + EOP; optional trivial; **fresh** reviewer context when required.  
3. **Dimensions** — evidence + faithfulness + readability/coherence (OpenSpec Completeness/Correctness/Coherence = labels only).  
4. **Light EOP converge** — gap types missing/partial/contradicts/**unrequested**; append tasks; no silent plan rewrite; **no code edits** in converge pass (G12 home).  
5. **Split lanes** — signal verify (“builds?”) vs intent coverage (“promised?”); quality is third check after green.  
6. **HITL** — Theme 7 blocked/major deviation only; WARNING/NIT agent-fixable.  
7. **Wiring** — Execute/-subagents orchestrate; call companion at post-green (threshold) + required EOP; strengthen Handoffs post-accept.  
8. **Layout (design)** — `implementation-execute-verify/SKILL.md` + checklist + review-dimensions + converge-light refs.  
9. **Park** — Debug/PR packaging, SHA-as-SoT, CLI deps, TDD auditor, council, fat Quality, always-on rule.

### OPENs for integrator / later waves

- G1 rubric wording · G2 non-trivial lock (NT1–NT6) · G3 description triggers · G4 exact Execute prose · converge append format · severity vocab unify · post-task converge? (lean EOP-only) · optional E0 trial (G11)
