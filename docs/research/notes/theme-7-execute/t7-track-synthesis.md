---
title: "T7 track synthesis — Execution pocket (pre-report merge)"
status: draft
theme: theme-7-execute
created: 2026-07-30
updated: 2026-07-30
authors: [t7-synth-grok]
depth: deep
wave: 3
slice: T7-SYNTH
aligned_with:
  - docs/research/notes/theme-7-execute/campaign-brief.md
  - docs/research/notes/theme-7-execute/scope-normal.md
  - docs/research/notes/theme-7-execute/t7-coordinator-pin.md
  - docs/research/notes/theme-7-execute/t7a-w1-cold-execute-loop.md
  - docs/research/notes/theme-7-execute/t7b-w1-subagent-controller.md
  - docs/research/notes/theme-7-execute/t7c-w1-community-execute-skills.md
  - docs/research/notes/theme-7-execute/t7d-w1-boundaries-elevation.md
  - docs/research/notes/theme-7-execute/t7-w2-spine-corroboration.md
  - docs/research/notes/theme-7-execute/t7-w2-community-gaps.md
  - docs/research/notes/theme-7-execute/t7-w3-plus1-residual.md
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# T7 track synthesis — Execution pocket (pre-report merge)

**Using `research-protocol`**; depth: **deep**; wave: **3**; slice: **T7-SYNTH**.

**Status:** `draft`. Not Execution SoT. **No new facts** beyond prior Theme 7 notes + Theme 6 accepted law. Integrator merge for coordinator draft report — this note does **not** write `docs/research/reports/theme-7-execute-pocket.md`.

## 1. Scope

- Question / goal: Cross-track merge of Theme 7 Execute deep research into a single synthesis: FACT cluster, conflicts, candidate method spine, elevation candidates, portable review notes, P0 OPENs, source shortlist.
- In scope: Merge T7A–D W1 + W2 spine/community + W3 PLUS1; respect campaign §7.1 human decisions; cite-or-omit.
- Out of scope: Skill elevation; inventing APIs; writing the pocket report file; re-litigating Theme 6 Plan law.
- Comprehension / research goal type: other (integrator synthesis)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (all notes under `docs/research/notes/theme-7-execute/`; packs README for ladder framing) |
| Corpora / URLs searched | Local Theme 7 notes only (no new web/RAG) |
| Queries (exact) | N/A (merge) |
| What was *not* searched | New primary sources; live E0 execute trial |
| Depth | deep |
| Waves / stop_reason | Waves: pin → W1 T7A–D → W2 SPINE+COMMUNITY → W3 PLUS1 → this SYNTH. Campaign gatherer **`stop_reason: low_return_plus_one`** (from PLUS1). |
| Provenance (optional PROV) | Entity←prior gatherer notes; Activity=T7-SYNTH merge; Agent=cursor-grok-4.5-high-fast |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | Full-track merge for draft report handoff |
| Scope boundary | Theme 7 notes + Theme 6 accepted inputs; no elevation |

## 4. Findings

### 4.1 Cross-track FACT cluster (multi-source)

Each bullet is supported by **≥2 independent track/source families** (or Theme 6 accepted + ≥1 Execute track).

#### Plan law consumed by Execute (Theme 6 + templates + T7A/T7D)

- `FACT` [E0] Status vocab for implement-time ledger: `ready` · `in_progress` · `blocked` (`intent-gap` / `verify-fail` / `needs-human`) · `done`; HALT ≡ `blocked`+`intent-gap`. [E0: Theme 6 elevation #9; `plan-minimal.md`; T7A §4.0; T7D §4.1]
- `FACT` [E0] Default exec shape: `serial_implement_review`; parallel writers only when plan marks independence + exclusive writes/worktrees (Plan #2). [E0: Theme 6 #2; `plan-minimal.md`; T7B §4.3; W2-COMMUNITY §4.4 reaffirm]
- `FACT` [E0] Per-task Done-when + Verify `command` → expected signal; verify required; TDD ceremony optional. [E0: Theme 6 #3–#4; `plan-minimal.md`; T7A §4.0]
- `FACT` [E0] Plan owns authoring + V1–V8 light pre-exec; Implement craft is not Plan skill. [E0: Theme 6 pocket scope / #5; T7D §4.2; packs Plan shipped]

#### Cold-execute loop (T7A + vendor E1 + community E0/E1)

- `FACT` [E0/E1] Community + vendor cluster on: load plan → critical review before code → task loop with listed verify → stop/ask don’t guess. [E0: Superpowers `executing-plans` via T7A/T7C; E1: Claude best practices via T7A; OpenSpec apply / Spec Kit lean via T7C/W2]
- `FACT` [E1] Fresh / clean context after written plan/spec is a strong vendor lean (Claude fresh session; Cursor new-chat heuristics; Cursor save plan for future agents). [E1: T7A §4.4; Cursor plan-mode W2 re-fetch]
- `FACT` [E1] Runnable pass/fail verify with evidence (command + output), not bare “done” assertion. [E1: Claude best practices T7A; Codex Done-when/verify W2-SPINE; BMAD Verification section T7C/W2]
- `FACT` [E0] Campaign §7.1 human: HITL = escalate on **major deviation or blocked**, not pause every green task; Toolbelt-native standalone (inspire, don’t depend). [E0: `campaign-brief.md` §7.1; T7A/T7B/T7D]

#### Subagent controller (T7B + Anthropic/Cursor E1 + SDD inventory)

- `FACT` [E1] Orchestrator-workers / parent coordinates specialists with structured handoffs; subagents get clean context; parent must supply prompt. [E1: Anthropic building-effective-agents + multi-agent research; Cursor subagents — T7B §4.1–4.2]
- `FACT` [E0] Theme 6 plan-minimal task unit fields are the alignment target for implementer packets (Objective, Files, Interfaces, Deps, Done-when, Verify, Parallel-safe, Do-not + plan-level constraints). [E0: `plan-minimal.md`; T7B §4.2.2]
- `FACT` [E0/E3] Superpowers SDD inventory: fresh implementer per task → task review → continuous until blocked → end review; park worktree/TDD/finish/commit-every-task / absolute never-parallel as Toolbelt law. [E0: T7B/T7C; conflict resolved by Plan #2]

#### Community deepen (T7C + W2-COMMUNITY)

- `FACT` [E0] Superpowers `verification-before-completion`: no completion claims without fresh identify→run→read→verify evidence. [E0: W2-COMMUNITY §4.3 full body]
- `FACT` [E1] OpenSpec apply: status/instructions loop, checkbox ledger, `blocked`/`all_done`, contextFiles, pause don’t guess — park CLI packaging. [E1: T7C]
- `FACT` [E1] Spec Kit implement (lean thinner than full); converge = append-only gap tasks, no code edits — not primary spine. [E1: T7C + W2-COMMUNITY]
- `FACT` [E1] BMAD build-auto: implement→verify→review; triage `intent_gap`/`bad_spec`/`patch`/`defer`/`reject`; park uv/renderer/VCS ceremony. [E1: T7C + W2-COMMUNITY]

#### Boundaries (T7D + packs + brief)

- `FACT` [E0] Packs ladder: Execute after shipped Plan; Quality/Verify stub after Execute. [E0: `docs/packs/README.md`; campaign ladder; T7D §4.1]
- `FACT` [E0] Candidate elevation table (post-accept only): main spine + supplementary broad-use + light verify fold/companion; thin always-on unlikely. [E0: campaign §5; T7D §4.3]

#### Principles corroboration (Alexandria E2 — not skill grammar)

- `FACT` [E2] Osmani plan→execute→verify→report; Huyen reflection + out-of-scope IRRELEVANT; Dibia evaluate/retry-enhanced; Broda retry/escalate/abort — principles only, no Toolbelt status grammar. [E2: scope-normal / T7A / W2-SPINE]

#### W2/W3 closures (factual dispositions)

- `FACT` [E0] Codex best-practices GAP closed via 308→learn.chatgpt.com; Cursor plan-mode re-confirmed; Spec Kit/BMAD review/verification-before-completion W1 residuals closed at primary-file level. [E0: W2-SPINE; W2-COMMUNITY]
- `FACT` [E0] PLUS1 froze house-policy **candidates** (INFERENCE) and recorded campaign gatherer stop `low_return_plus_one`. [E0: `t7-w3-plus1-residual.md`]

### 4.2 CONFLICT table

Resolved by **campaign §7.1 human decisions** and/or **Theme 6 accepted law** where applicable. Unresolved remain OPEN.

| ID | Topic | Source A | Source B | Resolution |
|----|-------|----------|----------|------------|
| C1 | HITL density | Osmani/Cline/AutoGPT approve-steps [E2]; Spec Kit pre-start checklist HITL [E1] | Campaign §7.1 continuous when green; SDD/OpenSpec continuous [E0/E1] | **§7.1 wins:** escalate on blocked/major deviation only; optional preflight ≠ per-task pause |
| C2 | Parallel writers | Superpowers SDD never-parallel implementers [E0/E3] | Theme 6 #2 + Cursor/OpenAI independent parallel [E0/E1]; Spec Kit `[P]` [E1] | **Theme 6 #2 wins** as Toolbelt law; SDD ban = inventory of conflict risk only |
| C3 | Ambiguity / invent | Codex ExecPlans “resolve ambiguities autonomously” [E1 W2] | Theme 6 do-not-invent + `intent-gap` [E0] | **Toolbelt Plan + §7.1:** escalate intent gaps (false friend logged) |
| C4 | Verify iterate vs halt | Claude iterate-until-pass [E1]; Codex max-attempt loop [E1] | Superpowers stop when verify fails repeatedly [E0] | **Local enhanced retries up to house N, then `verify-fail`** (PLUS1 freeze); exact N = OPEN |
| C5 | Fresh vs same session | Claude fresh after spec [E1] | Cursor continue when iterating same feature [E1] | Prefer fresh at **plan→execute** handoff; same-session OK in-task; require vs recommend = OPEN |
| C6 | Verify / review home | Execute Done-when run + light companions | Packs Quality/Verify stub; BMAD step-04 / Spec Kit converge richness | **Light verify in Execute now**; fuller review/converge → later (pocket **or** touchups) — home OPEN |
| C7 | Git/worktree/finish/TDD | Superpowers/BMAD/Spec Kit packaging required in those products [E0/E1] | Toolbelt standalone + Theme 6 non-import [E0] | **Park** as Execute SoT; inspire atoms only |
| C8 | Ledger path | SDD `.superpowers/sdd/progress.md` [E0] | Theme 6 `docs/plans/` [E0] | **Default = plan file Status/checkboxes** (PLUS1); optional Toolbelt sidecar; park SP path |
| C9 | Orchestrator sees all vs refs | Dibia orchestrator sees all [E2] | Anthropic filesystem refs [E1] | Compatible: controller holds spine/ledger; workers get packets/refs |
| C10 | BMAD `bad_spec` amend loop | BMAD review amends + loopback [E1] | Do-not-invent / Plan owns plan text [E0] | Escalate (`intent-gap`/`needs-human`); no silent implementer rewrite (PLUS1 map) |

### 4.3 Candidate Execute method spine (INFERENCE — not elevated)

`INFERENCE` [E4] **Candidate Toolbelt-native Execute method spine** (draft synthesis; **not** skill SoT / not elevated):

```text
0. Preconditions
   - Plan status ready (or human waive) — draft/non-ready → escalate needs-human (OPEN gate wording)
   - Announce execute skill/mode
1. Load durable plan (docs/plans/… / plan-minimal grammar)
2. Critical review (batch concerns) before first code
   - Goal / Always·Block If·Never / Out of scope / File map / Done-when+Verify
   - Raise → human OR blocked+intent-gap — do not invent
3. Task loop (serial default; Plan #2 parallel-safe only when marked)
   a. Pick next ready task (respect deps)
   b. Set in_progress; update plan ledger (Status/checkboxes) — Meta sync per S1 lean candidate
   c. Implement within Files / Interfaces / Do-not
   d. Run Verify command → expected signal (evidence-before-done)
   e. On match → done; continue (no HITL pause when green)
   f. On mismatch → verify-retry policy (PLUS1); else blocked+verify-fail
4. Stop / escalate (don’t guess)
   - intent-gap | verify-fail | needs-human | major-deviation checklist (PLUS1)
5. Optional end-of-plan light coherence check / pointer to later review
6. Prefer fresh session (or fresh subagent context) at plan→execute boundary
```

**Controller / subagent mode (supplementary shape — same spine, different runtime):**

```text
Controller owns spine + packets + status adjudication
→ per-task fresh implementer (packet = Theme 6 fields + constraints + report contract; path refs not chat dumps)
→ task-level gate (Done-when evidence + optional fresh reviewer)
→ continue when green
→ end review after all tasks
Parallel writers only Plan #2
```

Premises: T7A return spine; T7B §8 answer; T7C ranked atoms; T7D boundary; W2 corroboration; PLUS1 freezes; §7.1.

**Top method atoms (ranked for elevation design):**

1. Load → critical review (raise, don’t invent) → then code  
2. Statused task loop + durable plan-file ledger (`ready`→`in_progress`→`done`/`blocked`)  
3. Done-when Verify + evidence-before-completion claims  
4. Stop/escalate don’t guess (`intent-gap` / `verify-fail` / `needs-human` / major deviation)  
5. Continuous green-path (HITL only when blocked/major deviation)  
*(Honorable: required context pack without foreign CLI; serial default / Plan #2)*

### 4.4 Elevation candidates (post-accept only — not elevating)

`INFERENCE` [E4] Elevation shape aligned with §7.1 + Theme 6 skill-only precedent. Premises: campaign §5; T7D §4.3; T7C rankings; T7B supplementary.

| Priority | Candidate | Type | Role |
|----------|-----------|------|------|
| **P0** | Toolbelt-native `execute-plan` **or** `implement-plan` (name OPEN) | **Main spine skill** | Cold/same-session consume `docs/plans/…` → §4.3 spine |
| **P0–P1** | Subagent-driven execute (name TBD) | **Supplementary broad-use skill** (preferred) or spine mode | Controller + fresh implementer packets + task/end review; Plan #2 |
| **P1** | Light verify-before-done atoms | **Fold into spine** (preferred lean) and/or thin companion | Identify→run→read→claim; maps to Done-when — not full review pack |
| P2 | Thin always-on Execute rule | rule | Unlikely (mirror Theme 6) |
| Later | Entry-flow compose; converge-style append; BMAD-like triage vocabulary | — | After accept / later review effort |
| — | Superpowers / OpenSpec / BMAD / Spec Kit as runtime dependency | — | **Rejected** |

**Park from elevation SoT:** required worktrees; finishing-branch; commit-every-task law; mandatory TDD; foreign CLI/renderer/hooks; `.superpowers` paths; stars-as-acceptance.

### 4.5 Portable review notes for later (from T7D + W2)

Retain for a future effort that may cover **plan + execute review** and **multi-use tooling**. Do **not** treat as Review pocket architecture / SoT.

1. **Split already decided at light layer:** Plan = V1–V8 **pre-exec**; Execute = **run** Done-when + light verify + optional fresh task reviewer. Inventory of “what review surfaces exist / keep / change” = **later**. [E0: T7D §4.4]
2. **Multi-use tooling:** Prefer designing shared fresh-context reviewer / evidence / faithfulness checklists **once later**; Execute ships **minimal** inline atoms only. [E0: T7D §4.4]
3. **Home undecided:** pocket **or** touchups on Plan/Execute (+ Debug). [E0: campaign §7.1; T7D O5]
4. **Portable queue from community:** Spec Kit converge append-only gap contract; BMAD triage+repair-cap+deferred list; Superpowers requesting-code-review pattern; finishing/PR packaging; systematic-debugging full method; deep validating-plans / TDD auditor (Theme 6 #5 deferrals). [E0/E1: T7D §4.4; W2-COMMUNITY]
5. **Inspiration ≠ dependency** applies to future review surfaces. [E0: §7.1]
6. **Do not** invent Review skill names, pack layout, or SoT from Theme 7 alone. [E0: T7D §4.4]

### 4.6 P0 OPEN for human after report

| ID | OPEN | Why P0 | Notes |
|----|------|--------|-------|
| **O-N** | Exact verify-retry default `N` (2 vs 3) + per-plan override? | Gates `verify-fail` behavior | PLUS1 candidates only |
| **O-MD** | Accept major-deviation checklist as skill text (incl. drive-by-refactor edge) | HITL faithfulness | PLUS1 §4.2 freeze |
| **O-SYNC** | Meta↔task sync: adopt **S1** (lean) vs S2 vs S3 | Cold resume honesty | PLUS1 §4.3 |
| **O-NAME** | Spine skill name: `execute-plan` vs `implement-plan` | Elevation packaging | T7D O1; §7.1 native |
| **O-FRESH** | Require vs recommend fresh session at plan→execute | Spine wording strength | T7A OPEN; C5 |
| **O-SUB** | Subagent-driven: separate supplementary skill vs spine mode | Elevation shape | T7D O2; §7.1 allows both |
| **O-VFOLD** | Light verify: fold-only vs fold + thin companion | Surface count | T7D O3/H4 |
| **O-DRAFT** | Draft / non-`ready` plan at execute: hard escalate vs human waive | Aligns `draft-is-not-sot` | T7D O4 |
| **O-REV** | Later review home: pocket vs touchups | Out of Theme 7 SoT but blocks pack ladder narrative | T7D O5 |
| **O-REVIEWER** | Optional fresh task reviewer: default on / opt-in / plan-gated | Quality vs thin | T7D O6; T7B OPEN |

*(Coordinator report should surface these; elevation waits on accept.)*

### 4.7 Boundary pin (compact — from T7D)

| Lane | Owns |
|------|------|
| **Execute** | Cold-agent load→task loop→Done-when **run**→status→escalate; enforce serial/parallel-safe; light verify + optional fresh reviewer; broad-use subagent controller |
| **Plan** | Write plans; V1–V8; Done-when **grammar**; status vocab; packets/shape; `implementation-plan` shipped |
| **Later review/debug** | Fuller plan+execute review; deep validate/TDD auditor; PR/finish; systematic debug; multi-use review tooling — home OPEN |
| **Out** | Build cookbooks; community plugins as dependency; re-litigate Plan; elevate mid-research; Review architecture as Theme 7 SoT |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Community + vendor converge on review→loop→verify→escalate | confirmed | §4.1 |
| H2 | Theme 6 status/serial/Done-when suffice as Execute ledger grammar | confirmed | §4.1; Meta sync still OPEN |
| H3 | Main spine + subagent supplement is the elevation shape | confirmed (directional §7.1) | §4.4 |
| H4 | Alexandria supplies skill grammar | rejected | §4.1 principles only |
| H5 | More vendor gatherers needed before draft report | rejected | PLUS1 `low_return_plus_one` |

## 6. Conflicts

See **§4.2 CONFLICT table** (authoritative merge of track conflict logs).

## 7. Gaps & OPEN

### Confirmed durable GAPs (not blocking draft report)

- Live E0 Toolbelt cold-execute trial on a real `plan-minimal` plan — not run  
- Spec Kit lean converge (absent in search) — low priority  
- BMAD interactive `bmad-build` step-04 — optional residual  
- Cursor Task-tool internal prompt contract — do not invent  

### P0 OPENs

See **§4.6**.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Coordinator may draft `docs/research/reports/theme-7-execute-pocket.md` from this synthesis + prior notes **without** another gatherer wave. Premises: §2 stop_reason; PLUS1 freeze; W2 diminishing returns.
- `INFERENCE` [E4] Do **not** elevate Execute skills from this draft synthesis. Premises: `draft-is-not-sot`; campaign elevation post-accept only.
- `INFERENCE` [E4] Highest-value post-accept delivery remains thin Toolbelt-native **main spine** + **broad-use subagent supplement** + **light verify fold**, consuming Theme 6 plans, standalone of Superpowers/OpenSpec/BMAD/Spec Kit. Premises: §§4.3–4.4; brief §6 lean.

## 9. Source shortlist (deduped high-signal)

### Local / house (E0)

1. `docs/research/reports/theme-6-plan-pocket.md` (accepted)  
2. `docs/templates/plan-minimal.md`  
3. Toolbelt `implementation-plan/SKILL.md`  
4. `docs/packs/README.md`  
5. Theme 7 notes: `campaign-brief.md`, `scope-normal.md`, `t7-coordinator-pin.md`, `t7a`–`t7d` W1, `t7-w2-spine-corroboration.md`, `t7-w2-community-gaps.md`, `t7-w3-plus1-residual.md`  
6. Local Superpowers (inventory only): `executing-plans`, `subagent-driven-development`, `verification-before-completion`, `requesting-code-review`

### Vendor primary (E1)

7. Claude Code best practices — https://code.claude.com/docs/en/best-practices  
8. Cursor Plan Mode — https://cursor.com/docs/agent/plan-mode  
9. Cursor agent best practices — https://cursor.com/blog/agent-best-practices  
10. Cursor Subagents — https://cursor.com/docs/subagents  
11. Anthropic — Building effective agents; multi-agent research system  
12. Codex best practices — https://learn.chatgpt.com/guides/best-practices  
13. Codex ExecPlans + iterative repair cookbooks (OpenAI developers cookbook)  
14. OpenAI Agents SDK multi_agent orchestration  
15. Fission-AI/OpenSpec `openspec-apply-change/SKILL.md`  
16. github/spec-kit `implement.md` / lean implement / `converge.md`  
17. bmad-code-org/BMAD-METHOD build-auto `step-03-implement.md` + `step-04-review.md` + `workflow.md`

### Secondary (E2) — principles only

18. Alexandria Osmani / Huyen / Dibia / Broda chunks (ids in T7A / W2-SPINE)

### Explicitly not SoT

Community stars; Superpowers/OpenSpec/BMAD/Spec Kit packaging; draft Theme 7 notes as design law.

---

## Return summary (to parent / coordinator)

| Field | Value |
|-------|--------|
| **stop_reason** | **`low_return_plus_one`** |
| **Top 5 method atoms** | (1) critical review before code (2) statused task loop + plan-file ledger (3) Done-when verify + evidence-before-done (4) stop/escalate don’t guess (5) continuous green-path / HITL on block·major-deviation |
| **Elevation candidates** | Main spine + supplementary broad-use subagent skill; light verify fold — **not elevated** |
| **P0 OPENs** | N; major-deviation wording; Meta sync S1/S2/S3; skill name; fresh require/recommend; subagent skill vs mode; verify fold; draft-plan gate; review home; reviewer default |
| **Report file** | **Not written** — coordinator owns `theme-7-execute-pocket.md` |
