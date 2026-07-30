---
title: "Theme 8 — Verify gates deep research campaign brief"
status: draft
theme: theme-8-verify
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: deep
campaign_phase: accepted_elevated
aligned_with:
  - docs/research/notes/theme-8-verify/scope-normal-pass1.md
  - docs/research/notes/theme-8-verify/scope-normal-pass2-expand.md
  - docs/research/notes/theme-8-verify/scope-normal-pass3-github-web.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 8 — Verify gates campaign brief

**Using `research-protocol`** · depth: **deep** · Wave 1 launched 2026-07-30.

**Status:** `draft` brief. Not Verify SoT.  
**Identity:** Theme 8 is **not** the Debug/PR pocket. It is the **missing verification extension** of the already-shipped **Plan** and **Execute** pockets — thin companions that close plan-validate and execute-verify gaps. Debug/PR remains a later stub pack.

**Scoping:** [`pass1`](./scope-normal-pass1.md) + [`pass2`](./scope-normal-pass2-expand.md) + [`pass3 GitHub/web`](./scope-normal-pass3-github-web.md).  
**Determinations:** §0 locked; Wave 1 approved to launch.

---

## 0. Human determinations (locked for deep)

Source: pass 1–3 leans; human chose **D1 = C** with companion names below. Overrides earlier “prefer B” lean. Still `draft` until report accept / elevate.

**Framing lock:** Not Debug pocket. Extensions of Plan + Execute only.

### Surface & packaging

| ID | Determination |
|----|----------------|
| **D1** | **C — two companions:** `implementation-plan-verify` + `implementation-execute-verify` |
| **D2** | **Hybrid orchestration:** Plan/Execute remain orchestrators; companions hold validate/verify gates + rubrics |
| **D3** | **Skill-only** (no always-on verify rule) |
| **D4** | Theme/report naming: **Verify gates** (not a fat Quality pocket) |

### Plan-validate (`implementation-plan-verify` / T8A)

| ID | Determination |
|----|----------------|
| **D5** | **Explicit phase** between write-plan and Meta `ready` / execute |
| **D6** | **Parallel** Reality + Drift + coverage/actionability; **park TDD auditor** |
| **D7** | Severity + verdicts: **PASS / PASS WITH NOTES / NEEDS REVISION** |
| **D8** | On NEEDS REVISION: **fix the plan, not code**; re-validate before execute |
| **D9** | Ambiguity / inventable gaps → **hard gate** (`blocked(intent-gap)` / NEEDS REVISION) |
| **D10** | **Light** task taxonomy (composite / ambiguous / coverage gap / misordered); park heavy D1–D13 |
| **D11** | **Light** FR→task coverage + acyclic deps |
| **D12** | Codebase verification table **required for non-trivial** plans; skip trivial |
| **D13** | Spec Kit analyze/checklist: **steal grammar only** (no dependency) |

### Execute-verify (`implementation-execute-verify` / T8B)

| ID | Determination |
|----|----------------|
| **D14** | Explicit evidence iron law: IDENTIFY→RUN→READ→VERIFY; ban “should/looks” completion claims |
| **D15** | Post-green quality/readability review: **required** for non-trivial tasks + end-of-plan; optional on trivial |
| **D16** | When D15 required: **fresh** reviewer context (subagent or fresh chat) |
| **D17** | Dimensions: **evidence + faithfulness + readability/coherence** (OpenSpec Completeness/Correctness/Coherence as labels only) |
| **D18** | End-of-plan: **required light converge** — gap types incl. **unrequested**; append tasks; no silent plan rewrite; no code edits in converge pass |
| **D19** | Keep split: signal verify (“builds?”) vs intent coverage (“promised?”) |
| **D20** | HITL: **Theme 7** (blocked / major deviation); WARNING/NIT agent-fixable unless escalate |
| **D21** | N=2 verify retries: **frozen** (Theme 7 law) |

### Park / defer

| ID | Determination |
|----|----------------|
| **D22** | TDD auditor as Plan law → **park** |
| **D23** | OpenSpec / Spec Kit / Superpowers as runtime deps → **park** (atoms only) |
| **D24** | Copilot PR-skills / Debug-PR pack → **defer** |
| **D25** | Git SHA ceremony as SoT → **park** |
| **D26** | Multi-consultant “council” ceremony → **park**; keep verification-table atom |
| **D27** | Fat Quality pocket (option D) → **defer** |

### Campaign protocol

| ID | Determination |
|----|----------------|
| **D28** | Subagents: `cursor-grok-4.5-high-fast` |
| **D29** | Stop: `low_return_plus_one` |
| **D30** | Waves: W1 parallel T8A–T8C + T8D light → W2 corroboration → +1 residual → integrate |

### Deep-only gaps (do not treat as SoT yet)

G1 rubric wording · G2 non-trivial threshold · G3 skill description triggers · G4 wiring into Plan/Execute/-subagents · G5 OpenSpec rubrics deep-read · G6 Spec Kit analyze/checklist grammar · G7 rube-de table · G8 kanbanzai subset · G9 validating-plans refs 404 · G10 Debug/PR leftovers · G11 optional live E0 trials · G12 converge home = **`implementation-execute-verify`** (follows D1=C; deep may refine steps)

---

## 1. Purpose

| Field | Value |
|-------|-------|
| Theme | **Verify gates** — Plan/Execute verification extensions (not a new Debug pocket) |
| Goal | Evidence-backed validation of plans and implementations (not vibes); **quality + code readability** first-class |
| Form | **Two thin companions** + strengthen Plan/Execute orchestration (not fat Quality pack; not Debug/PR) |
| Ladder | Research → Design → Plan → **plan-verify** → Execute → **execute-verify** → (later) Debug/PR |

**Non-goals:** Designing the **Debug / PR / workflow** pack; re-litigating Plan density / Execute N=2 / status vocab; Build cookbooks; Superpowers/OpenSpec/BMAD as runtime dependency; mandatory TDD/git/PR as Toolbelt law; fat Review/Debug pocket (deferred to later theme).

**Essence filter:** Standalone Toolbelt method. Extract atoms from verification-before-completion, validating-plans, Spec Kit converge/analyze/checklist, OpenSpec verify-change, Claude adversarial review — **cut coupling**.

**Quality lean:**

1. Faithfulness to approved design + plan (no invent, no unrequested scope)  
2. Evidence before completion claims (run → read → claim)  
3. Code **readability / maintainability**  
4. Thin surfaces — companions only for discoverable plan-validate vs execute-verify lanes  

---

## 2. Why Theme 8 (from normal passes)

| Already shipped | Still thin / missing |
|-----------------|----------------------|
| Plan: Done-when grammar + V1–V8 light pre-exec | Graded plan-validate companion (coverage, falsifiable verifies, ambiguity, reality/drift) |
| Execute: critical review + Done-when run + N=2 + major-deviation | Post-green quality/readability/faithfulness; converge-style intent coverage; discoverable execute-verify |
| T7D deferred fuller review | Theme 8 = light-to-medium layer; PR/Debug later |

---

## 3. Tracks (constrained by §0)

### T8A — Plan validation (`implementation-plan-verify`)

Design the **explicit** pre-exec validate phase: parallel Reality + Drift + coverage/actionability; severity + PASS / PASS WITH NOTES / NEEDS REVISION; fix-plan-not-code; hard ambiguity gate; light task taxonomy; light coverage + acyclic deps; codebase verification table for non-trivial; steal Spec Kit analyze/checklist grammar.  
Output: atoms + skill shape for `implementation-plan-verify`; wiring from `implementation-plan` (orchestrator).

### T8B — Execute verification (`implementation-execute-verify`)

Evidence iron law; required fresh post-green review (non-trivial + EOP) on evidence + faithfulness + readability/coherence; required light converge (incl. unrequested; append tasks); keep signal-verify vs intent-coverage split; Theme 7 HITL + frozen N=2.  
Output: atoms + skill shape for `implementation-execute-verify`; wiring from `implementation-execute` / `-subagents`.

### T8C — Community / vendor deepen

Deep-read Tier A (pass 3): verification-before-completion + requesting-code-review; validating-plans SKILL.md (confirm refs 404); Spec Kit converge/analyze/checklist; OpenSpec verify-change rubrics (park CLI); rube-de review-plan table; spot-check plan-review / validate-plan subsets.  
Park: Copilot PR packaging; Superpowers mirrors; TDD auditor; council ceremony.  
Output: transferable vs park table with grades — **must respect §0 parks**.

### T8D — Surface shape & elevation

**Surface locked: C** with names `implementation-plan-verify` + `implementation-execute-verify`.  
Deep work: description triggers (G3), wiring (G4), non-trivial thresholds (G2), rubrics (G1), checklist/skill file layout. **G10 = leftover list only** (what belongs in later Debug/PR — do not design that pocket here). Confirm hybrid orchestration. Elevation only after report accept.

**Optional gap fleet:** Only if W2 names P0.

---

## 4. Shared protocol

- Cite-or-omit; FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U  
- Subagents: `cursor-grok-4.5-high-fast` (D28)  
- Notes: `docs/research/notes/theme-8-verify/`  
- Report: `docs/research/reports/theme-8-verify-gates.md` (preferred) or `theme-8-verify-pocket.md` if integrator keeps pocket label  
- Theme 6+7 = **input law**; §0 determinations = **brief constraints** (not elevated SoT)  
- Stop: `low_return_plus_one` (D29)

| Phase | Shape |
|-------|-------|
| Approve brief | Human (determinations already in §0) |
| W1 | Parallel T8A–T8C + T8D light |
| W2 | Corroboration |
| W3 / +1 | Residual |
| Integrate | Draft report → accept → elevate companions |

---

## 5. Candidate elevation (post-accept only)

| Candidate | Notes |
|-----------|-------|
| `implementation-plan-verify` | **Primary** (D1=C) |
| `implementation-execute-verify` | **Primary** (D1=C) |
| Strengthen Plan checklist / V1–V8+ + wire to plan-verify | Almost certain |
| Strengthen Execute evidence/review steps + wire to execute-verify | Almost certain |
| Thin always-on rule | **No** (D3) |
| Fat Quality pack | **Deferred** (D27) |
| Shared single `implementation-verify` | **Rejected** (D1=C) |

---

## 6. Approval gate

- [x] Human determinations §0 (leans + D1=C + companion names + framing ≠ Debug)  
- [x] Human approves launching Wave 1 on this brief  
- [x] Subagent model `cursor-grok-4.5-high-fast`  
- [x] Stop `low_return_plus_one`  
- [x] Wave 1 launched
