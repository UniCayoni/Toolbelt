---
title: "T9A W1 — Debug method spine (investigate → verify same repro)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9a-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-coordinator-pin.md
  - docs/research/notes/theme-9-debug/scope-normal-pass1.md
  - docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/PROTOCOL.md
supersedes: null
---

# T9A W1 — Debug method spine

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T9A**.

**Status:** `draft`. Not Debug SoT. No skills elevated. Superpowers/community surfaces are **inspiration only** — not Toolbelt dependencies.

## 1. Scope

- Question / goal: Formalize a Toolbelt-native **debug method spine**: investigate → reproduce (shrink) → hypothesize/falsify → root-cause (backward trace) → minimal fix → verify the **same** repro; plus red flags, N-fix stop → architecture, flaky light checklist, optional defense-in-depth, and Execute/`verify-fail` / user-bug seam language.
- In scope: Phase/step checklist candidates; reproduce iron law + `NOT-YET-REPRODUCED`; hypothesis-table discipline; root-cause atoms; fence material for **F3 / F4 / F7 / F10**; transferable vs park; residual GAPs/OPENs for W2.
- Out of scope: Elevating skills/rules; inventing Cursor private debug-server APIs; shipping collectors/MCP; PR/CI/Bugbot design; T9F swarm; re-owning Theme 7 verify-retry **N=2** or Theme 8 plan/execute-verify SoT; locking surface shape **A vs B** (fence **F1** → T9D; method implications only).
- Comprehension / research goal type: reuse (method inventory → transferable spine)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign brief, coordinator pin, scope pass1–3, Theme 7/8 reports, `PROTOCOL.md`, `implementation-execute` skill); `gh api` (obra/superpowers systematic-debugging + companions; silkyland/reproduce-my-bug; rbouschery/agent-skills bug-investigate-fix; millionco/debug-agent); Alexandria `rag_query` (`software_engineering`) |
| Corpora / URLs searched | GitHub API contents for repos above; Alexandria corpus=`software_engineering`; local Theme 7–9 draft/accepted docs |
| Queries (exact) | Alexandria: `systematic debugging reproduce before fix root cause hypothesis flaky intermittent`; `gh api` path fetches listed in Source list |
| What was *not* searched | Live E0 Toolbelt debug trials; silkyland `references/flaky-bugs.md` full body; VS Code DAP; Cursor Debug Mode deep compose (T9B); full T9C community tree beyond Tier-A method atoms; stas00 art-of-debugging primary re-fetch this wave |
| Depth | deep |
| Waves / stop_reason | Wave 1 gatherer slice only. `stop_reason`: **`wave1_slice_coverage`** — ten must-cover axes addressed with cite-or-omit; residual → W2. Campaign stop remains coordinator `low_return_plus_one`. |
| Provenance (optional PROV) | Entity←Theme 7/8 accepted boundaries + Superpowers/community E1 + Dooley/Osmani E2 + Theme 9 brief/scopes; Activity=T9A W1 method spine; Agent=t9a-w1-gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Theme 7/8 accepted reports + brief §0/§0b are systematic input law; community skill bodies opportunistic for method atoms |
| Scope boundary | Debug **investigation method** only — not Plan Done-when / Execute verify-retry / execute-verify post-green; not PR/CI |

## 4. Findings

### 4.0 Boundary inputs (do not re-own)

- `FACT` [E0] Theme 7 accepted: verify-retry **N=2** then `blocked`+`verify-fail`; escalate reasons include `verify-fail` \| `intent-gap` \| `needs-human` \| `major-deviation`. [E0: `docs/research/reports/theme-7-execute-pocket.md` O-N + §3 — accessed 2026-07-30]
- `FACT` [E0] Shipped Execute skill: on Done-when mismatch, up to **N=2** enhanced local fixes inside Files/Interfaces, then `blocked`+`verify-fail`; Debug pack later — not Execute SoT. [E0: `skills/implementation-execute/SKILL.md` task loop + Handoffs — observed 2026-07-30]
- `FACT` [E0] Theme 8 accepted: Plan/Execute verify companions; **Debug/PR pack out of scope**; Theme 7 **N=2 frozen** for Execute verify-retry. [E0: `docs/research/reports/theme-8-verify-gates.md` scope + D14–D21 + FC-PARKS — accessed 2026-07-30]
- `FACT` [E0] Campaign brief quality lean: reproduce before fix (or document why / `NOT-YET-REPRODUCED`); falsify hypotheses with runtime evidence; root cause over symptom patches; verify **same** repro; escalate don’t thrash. [E0: `docs/research/notes/theme-9-debug/campaign-brief.md` §1]
- `FACT` [E0] Fence items F3 (N-fix stop), F4 (flaky thickness), F7 (defense-in-depth), F10 (Execute→Debug seam wording) stay open until after deep report; working leans ≠ locks. [E0: campaign-brief §0b]
- `INFERENCE` [E4] Theme 7 **N=2** is a **verify-retry budget** on Done-when; Debug’s **N-failed-fix cycles** (fence F3) is a separate budget for root-cause thrashing — do not merge the numbers into one SoT. Premises: (1) Theme 7 O-N [E0]; (2) Superpowers “≥3 fixes → architecture” is about fix attempts after investigation [E1 §4.5]; (3) pass2 explicit “Do not replace Execute N=2 with Debug’s fix budget” [E0: scope-pass2 §3.6].

### 4.1 Axis 1 — Phase/step model (candidate checklist)

Community phase models (structure inventory; not Toolbelt law):

| Source | Phases / steps (compressed) | Citation |
|--------|----------------------------|----------|
| Superpowers `systematic-debugging` | (1) Root-cause investigation incl. reproduce (2) Pattern analysis (3) Hypothesis + minimal test (4) Implement + verify; ≥3 failed fixes → architecture | [E1: obra/superpowers `skills/systematic-debugging/SKILL.md` — fetched via `gh api` 2026-07-30] |
| silkyland `reproduce-my-bug` | Intake → Evidence → Path trace → Reproduce → Minimize → Flaky path → Dossier; **never patches** | [E1: silkyland/reproduce-my-bug `SKILL.md` — `gh api` 2026-07-30] |
| rbouschery `bug-investigate-fix` | Reproduce → Hypotheses (1–4) → Test → short fix plan → Implement → Verify same repro gone | [E1: rbouschery/agent-skills `bug-investigate-fix/SKILL.md` — `gh api` 2026-07-30] |
| millionco `debug-agent` | 3–5 hypotheses → instrument → reproduce → classify → fix with log proof → verify → cleanup | [E1: millionco/debug-agent `.agents/skills/debug-agent/SKILL.md` — `gh api` 2026-07-30] |
| Theme 9 pass2 candidate | Symptom intake → INVESTIGATE → REPRODUCE → HYPOTHESIZE → FALSIFY → ROOT CAUSE → FIX → VERIFY same → ESCALATE | [E0: `scope-normal-pass2-expand.md` §3.2] |

- `CLAIM` [E2] Classic SE: reproduce reliably → find source → fix that one → test the fix; shrink to simplest failing case. [E2: Alexandria corpus=`software_engineering` chunk_ids=`08490da27bbde1f95a445ac6`, `f2370255822d37ae59c3860e` source=`Dooley… Debugging` query=`systematic debugging reproduce before fix…` — 2026-07-30]
- `CLAIM` [E2] Don’t guess; don’t fix the symptom — find the root cause systematically. [E2: Alexandria `9e26a07559361b30390a1ffc` Dooley — same query]
- `INFERENCE` [E4] **Candidate Toolbelt spine checklist** (for fence/elevation later — not elevated):

```text
0. INTAKE — expected vs actual; artifacts (error/stack/steps/env); frequency
1. INVESTIGATE — read full error/stack; recent changes; locate suspect path (file:line)
2. REPRODUCE — same surface as report; shrink until load-bearing; if can't → NOT-YET-REPRODUCED (no guess-fix)
3. HYPOTHESIZE — 1–4 (or up to 3–5 when instrumenting in parallel) falsifiable rows in a table
4. FALSIFY — smallest experiment / instrumentation; record confirm | reject | inconclusive
5. ROOT CAUSE — backward trace to original trigger; document cause (not only symptom site)
6. MINIMAL FIX — one change addressing cause; no drive-by; failing repro/test preferred but TDD not law
7. VERIFY SAME REPRO — re-run the exact repro from step 2; evidence before “fixed”; clean temp instrumentation
8. STOP / ESCALATE — after N failed fix cycles or architecture smell → human (separate from Execute N=2)
```

  Premises: pass2 spine [E0]; Superpowers four phases [E1]; reproduce-my-bug / bug-investigate-fix [E1]; Dooley order [E2]; brief quality lean [E0].

- `OPEN` Exact numbering/labels in elevated skill(s) wait on F1 (A vs B) and F2 (names) — T9D owns surface packaging.

### 4.2 Axis 2 — Reproduce-before-fix iron law + `NOT-YET-REPRODUCED`

- `FACT` [E1] Superpowers iron law: no fixes without Phase 1 investigation first; if not reproducible → gather more data, don’t guess. [E1: systematic-debugging SKILL.md — Iron Law + Phase 1.2]
- `FACT` [E1] reproduce-my-bug prime directive: **no fix without a failing reproduction**; skill never patches; green ≠ repro. [E1: silkyland SKILL.md — Prime Directive + Hard rules]
- `FACT` [E1] Failure mode when unreproducible: tag **`NOT-YET-REPRODUCED`**; deliver evidence + eliminated hypotheses + monitoring; path not runnable locally → report blocker first (attempt #0). [E1: silkyland SKILL.md — “When things go wrong”]
- `FACT` [E1] bug-investigate-fix: observe bug in running environment; do **not** treat static code reading alone as reproduction; if blocked, state blockers — do not fabricate a fix plan. [E1: rbouschery SKILL.md §1]
- `FACT` [E1] debug-agent: never fix without runtime evidence; prefer existing failing test / ad hoc script / user repro. [E1: millionco SKILL.md — workflow + constraints]
- `INFERENCE` [E4] Toolbelt-native candidate iron law wording (draft, not lock):

  > **No product/code fix until a failing reproduction exists, or the case is explicitly tagged `NOT-YET-REPRODUCED` with evidence of attempts and blockers.**

  Premises: silkyland + Superpowers + rbouschery [E1]; brief §1 [E0].
- `INFERENCE` [E4] Method implication for working lean **B** (not F1 lock): a never-fix reproduce companion makes the iron law mechanically easier to enforce; lean **A** must encode the same gate inside one spine skill. Premises: pass3 surface lean [E0: scope-pass3 §11]; F1 owned by T9D.
- `GAP` Toolbelt house template for `NOT-YET-REPRODUCED` dossier fields (beyond silkyland REPRO.md shape). Searched: Theme 9 notes + silkyland SKILL. Result: atoms known; Toolbelt path/template not chosen (F5 → T9D).

### 4.3 Axis 3 — Hypothesis table discipline (1–4 / 3–5, falsifiable)

- `FACT` [E1] bug-investigate-fix: produce **1–4** ranked hypotheses; each specific, falsifiable, tied to symptoms; table columns Hypothesis / If true we'd see… / Quick test; record confirms/rejects/inconclusive; one small loop if all rejected — don’t spiral. [E1: rbouschery SKILL.md §2–3]
- `FACT` [E1] Superpowers Phase 3: form a **single** hypothesis, test minimally (one variable), don’t stack fixes; if failed → new hypothesis. [E1: systematic-debugging SKILL.md Phase 3]
- `FACT` [E1] debug-agent: generate **3–5** precise hypotheses; instrument to test in parallel; classify each CONFIRMED/REJECTED/INCONCLUSIVE with cited log evidence. [E1: millionco SKILL.md workflow steps 1, 4]
- `FACT` [E1] reproduce-my-bug: ranked hypothesis list by evidence; each names killer observation; append-only ledger (killed hypotheses demoted, not deleted). [E1: silkyland SKILL.md Step 2]
- `INFERENCE` [E4] Candidate Toolbelt discipline (compose, don’t fork Theme 8 evidence iron law):

  | Mode | Count | Use when |
  |------|-------|----------|
  | Serial falsify | **1–4** ranked; test in likelihood order | Default Agent+terminal/browser path |
  | Parallel instrument | **3–5** with `hypothesisId` atoms | When instrumentation batch is cheaper than serial (T9E compose) |

  Each row must be: specific mechanism · falsifiable observation · quick test · status (`open`/`confirmed`/`rejected`/`inconclusive`). Premises: rbouschery + Superpowers + debug-agent [E1]; T9E owns instrumentation packaging [E0 brief].
- `OPEN` Whether elevated spine mandates a markdown table vs freeform bullets — W2/elevation polish after F1.

### 4.4 Axis 4 — Root-cause backward trace atoms

- `FACT` [E1] Superpowers `root-cause-tracing`: observe symptom → immediate cause → what called this → keep tracing up → original trigger; fix at source, not symptom site; when stuck, temporary stack/`console.error` instrumentation. [E1: obra/superpowers `skills/systematic-debugging/root-cause-tracing.md` — `gh api` 2026-07-30]
- `FACT` [E1] Systematic-debugging Phase 1.5 points to backward tracing when error is deep in call stack. [E1: systematic-debugging SKILL.md]
- `FACT` [E1] reproduce-my-bug Step 3 path trace: symptom `file:line` → callers → offending value origin before building heavy repro. [E1: silkyland SKILL.md Step 3]
- `CLAIM` [E2] Dooley: find the source systematically (read code, explain, etc.) after reliable reproduce + shrink. [E2: Alexandria `f2370255822d37ae59c3860e`]
- `INFERENCE` [E4] Candidate **backward-trace atoms** for Toolbelt spine (thin; not a separate elevated skill by default):

  1. Pin symptom observation (error text / wrong state / failing assert).
  2. Name immediate cause (code that throws / writes bad state).
  3. Walk callers / data provenance one level at a time until original trigger.
  4. Prefer fix at trigger; if dead-end on trace, instrument then re-trace (T9B/T9E compose).
  5. Document cause in one sentence before patching.

  Premises: root-cause-tracing + silkyland path trace [E1]; pass3 “atoms under T9A, not separate skills by default” [E0: scope-pass3 §3].

### 4.5 Axis 5 — N-fix stop candidates (fence **F3**)

Working lean (not lock): ~3 (community echo). [E0: campaign-brief §0b F3]

- `FACT` [E1] Superpowers: if fix doesn’t work and count **≥ 3**, STOP and question architecture with human; “one more fix” after 2+ is a red flag; pattern = each fix reveals new shared-state/coupling elsewhere. [E1: systematic-debugging SKILL.md Phase 4.4–4.5 + Red Flags]
- `FACT` [E0] Theme 7/Execute **N=2** is verify-retry exhaustion → `verify-fail`, **not** Debug fix-cycle budget. [E0: Theme 7 report; `implementation-execute/SKILL.md`]
- `FACT` [E1] bug-investigate-fix: if verification fails, return to hypotheses — no numeric N; “one small loop only” on exhausted set. [E1: rbouschery SKILL.md §3, §6]
- `GAP` Primary vendor/academic lock on “exactly N=2 vs N=3 failed fixes before architecture.” Searched: Superpowers (N=3), Theme 7 (N=2 verify), Dooley RAG (no N). Result: community convention only for Debug N.

#### F3 pros/cons (for draft report fence table)

| Option | Meaning | Pros | Cons |
|--------|---------|------|------|
| **N=2** | After 2 failed root-cause fix attempts → architecture/human | Aligns numerically with Execute verify-retry vocabulary (familiar); stops thrash earlier; quality lean | Risk of premature escalate on hard bugs; agents may conflate with Theme 7 N=2 (must label differently, e.g. `debug-fix-cycles=2`) |
| **N=3** (lean) | Superpowers-style ≥3 → question architecture | Strong E1 echo; allows one more informed retry after re-investigate; red-flag corpus already written | Slightly more thrash budget; still arbitrary; must keep distinct from Execute N=2 |
| **Soft guidance** | “Stop thrashing / ask architecture when each fix reveals a new layer” without hard N | Thin; adaptive to bug hardness | Weak agent stop signal; hard to audit; conflicts quality-over-thinness lean if agents loop forever |

- `INFERENCE` [E4] Prefer stating F3 as **failed fix cycles after a confirmed/strong hypothesis**, not counting failed hypothesis tests. Premises: Superpowers separates hypothesis fail vs fix fail [E1]; rbouschery allows hypothesis loops [E1].
- `OPEN` Human picks F3 after deep report; T9A does not lock.

### 4.6 Axis 6 — Flaky light checklist candidates (fence **F4**)

Working lean: light checklist in method — not a third skill unless evidence demands. [E0: campaign-brief §0b F4]

- `FACT` [E1] reproduce-my-bug Step 6: identify nondeterminism (concurrency, clock, ordering, randomness, network, cache); **force** it; else document **reproduction rate** + recipe. [E1: silkyland SKILL.md Step 6 + failure modes]
- `FACT` [E1] Superpowers `condition-based-waiting`: flaky tests often use arbitrary sleep; wait for **condition** not guessed timing; document when timing *is* the subject. [E1: `condition-based-waiting.md` — `gh api` 2026-07-30]
- `CLAIM` [E2] Sporadic errors often from init, timing, dangling state, overflow, races; reduce to simplest failing case. [E2: Alexandria `08490da27bbde1f95a445ac6`, `f2370255822d37ae59c3860e`]
- `GAP` silkyland `references/flaky-bugs.md` full body not fetched this wave (pass3 also noted). Result: checklist candidates from SKILL.md Step 6 + condition-based-waiting atoms only.

#### Candidate light checklist (in-spine section)

```text
Flaky / intermittent (light):
- [ ] Frequency tagged: always | sometimes | once
- [ ] Name suspected nondeterminism class (race | clock | order | random | network | cache | init)
- [ ] Attempt to FORCE determinism (seed, freeze time, serialize, repeat harness)
- [ ] If unforced: document reproduction RATE (e.g. k/n) + exact recipe — still a repro
- [ ] Prefer condition-based waits over arbitrary sleep (when writing/adjusting tests)
- [ ] Heisenbug disappearing during investigation → finding, not “fixed”
```

#### F4 pros/cons

| Option | Pros | Cons |
|--------|------|------|
| **Checklist-in-spine** (lean) | One discoverable surface; matches thin spirit; covers common failure mode | Spine length grows; agents may skip section |
| **Companion section** (under never-fix / reproduce skill if F1→B) | Keeps fix spine shorter; flaky often is a repro problem | Two places to look if both spine+companion mention it |
| **Park thin** (omit dedicated flaky) | Shortest | Loses high-signal silkyland atom; intermittent bugs invite guess-fixes |

- `INFERENCE` [E4] Do **not** invent a third flaky-only skill in W1; F4 adjudication chooses thickness inside A/B. Premises: brief F4 lean [E0]; pass3 [E0].

### 4.7 Axis 7 — Defense-in-depth as optional post-fix (fence **F7**)

Working lean: optional post-fix note. [E0: campaign-brief §0b F7]

- `FACT` [E1] Superpowers `defense-in-depth`: after invalid-data bugs, validate at entry + business + environment (+ debug logging) so bug becomes structurally hard; single-layer checks get bypassed. [E1: `defense-in-depth.md` — `gh api` 2026-07-30]
- `FACT` [E1] root-cause-tracing recommends defense-in-depth **after** fixing at source (“BETTER: Also add…”). [E1: root-cause-tracing.md]
- `FACT` [E0] Pass3: absorb as *optional post-fix* note, not mandatory every bug — thin spirit. [E0: scope-pass3 §10 T9A]

#### F7 pros/cons

| Option | Pros | Cons |
|--------|------|------|
| **Optional post-fix note** (lean) | Thin default; agent can add layers when invalid-data / multi-path; matches Toolbelt thinness | Easy to skip when valuable; inconsistent application |
| **Recommended after invalid-data fixes** | Stronger quality; Superpowers E1 alignment when data provenance was the bug | Over-engineering risk; scope creep into “while here” refactors; conflicts minimal-fix atom if over-applied |
| **Mandatory every bug** | Maximum hardening | Violates thin spirit; slows Debug; drive-by validation sprawl |

- `INFERENCE` [E4] Candidate wording: *After an invalid-data / multi-path root cause, consider defense-in-depth (entry + business + env); skip for one-off typos/local logic errors unless recurrence risk is clear.* Premises: defense-in-depth when-to [E1]; F7 lean [E0].

### 4.8 Axis 8 — Execute→Debug seam trigger language (fence **F10**)

Working lean: wire on verify-fail / user bug / unclear Critical. [E0: campaign-brief §0b F10]

Do **not** redesign Theme 7 N=2 or Theme 8 verify here — only **handoff trigger phrases**.

- `FACT` [E0] Execute escalate vocab already includes `verify-fail` after N=2; Handoffs table says verify fails after N / design wrong → escalate human; Debug pack later. [E0: `implementation-execute/SKILL.md`]
- `FACT` [E0] Pass2 ladder seam candidates: Execute `verify-fail` after N=2; major-deviation / weird runtime; user bug outside plan; Theme 8 post-green Critical faithfulness break unclear. [E0: scope-pass2 §3.6]
- `FACT` [E0] Theme 8 owns post-green Critical / converge — Debug must not fork that SoT; only enter when cause is unclear. [E0: Theme 8 report; brief non-goals]

#### F10 candidate trigger language (exact phrases for later wiring)

| Trigger ID | Candidate agent-facing language | Into Debug |
|------------|--------------------------------|------------|
| **T-VF** | “Execute Verify exhausted (**N=2** enhanced local fixes) → status `blocked`+`verify-fail`. Symptom still unexplained — **enter Debug method spine**; do not burn more Execute verify-retries.” | Investigate + reproduce the failing Verify command/signal |
| **T-UB** | “User-reported bug / unexpected behavior outside (or orthogonal to) the active plan Done-when — **enter Debug**; do not invent plan tasks to mask investigation.” | Full spine from intake |
| **T-MD** | “Major-deviation / runtime behavior contradicts File map·Interfaces·Never — if cause unclear after raise-to-human, **enter Debug** rather than silent drive-by patches.” | Investigate; may return to Execute after root cause |
| **T-CR** | “Execute-verify / EOP Critical faithfulness issue where the **failure mechanism is unclear** — **Debug before more patches**; Theme 8 still owns the verify rubric.” | Reproduce Critical signal; hypothesize |
| **T-NYR** | “If Debug cannot reproduce → tag `NOT-YET-REPRODUCED` and escalate `needs-human` with dossier atoms — do not flip Execute task to `done`.” | Close loop / HITL |

#### F10 pros/cons (wording thickness)

| Option | Pros | Cons |
|--------|------|------|
| **Short triggers** (T-VF + T-UB only) | Thin; covers main ladder | Misses Critical / major-deviation edges |
| **Full set** (table above) | Matches pass2 seam map; clearer agent routing | More surface text in Execute/Debug handoffs |
| **Execute-only pointer** (“see Debug skill”) without phrases | Minimal Edit surface | Weak discoverability; agents may thrash under Execute |

- `INFERENCE` [E4] Minimum viable seam is **T-VF + T-UB**; T-MD/T-CR are quality add-ons once F1 surfaces exist. Premises: Execute already emits `verify-fail` [E0]; brief F10 lean [E0].
- `OPEN` Exact paste location (Execute Handoffs vs Debug When-to-use vs both) → T9D elevation wiring after fence gate.

### 4.9 Axis 9 — Transferable vs park

| Atom / surface | Transferable to Toolbelt Debug method | Park / cut |
|----------------|--------------------------------------|------------|
| Investigate → reproduce → hypothesize → root cause → minimal fix → verify same | **Yes** — spine core | — |
| Reproduce-before-fix + `NOT-YET-REPRODUCED` | **Yes** | Product-specific REPRO.md path as SoT |
| Hypothesis table 1–4 / parallel 3–5 + confirm/reject/inconclusive | **Yes** | Mandatory NDJSON collector / `npx debug-agent` server |
| Backward root-cause trace | **Yes** (atoms in spine) | Separate elevated skill by default; shipping `find-polluter.sh` |
| N-fix → architecture stop | **Yes** as F3 candidate | Equating to Theme 7 verify N=2 |
| Flaky: force nondeterminism or document rate | **Yes** light checklist (F4) | Full flaky encyclopedia / third skill |
| Condition-based waiting | **Yes** as flaky sub-atom | Shipping wait-helper libraries as Toolbelt code |
| Defense-in-depth layers | **Yes** optional post-fix (F7) | Mandatory four layers every bug |
| Same-surface repro (browser/API/CLI) | **Yes** | thermo-nuclear-plan coupling; `disable-model-invocation` packaging |
| Red-flag / rationalization lists | **Yes** (thin subset) | Partner-signal dialect tied to one human’s phrases |
| Superpowers Phase 4 “MUST create failing test” + TDD skill coupling | Prefer **failing repro**; TDD optional not law | Mandatory Superpowers TDD skill |
| verification-before-completion | Compose Theme 8 evidence culture | Duplicate as Debug-only SoT |
| Cursor Debug Mode loop | Compose (T9B) | Reimplement private debug server |
| bug-hunt-swarm parallel investigators | Park (T9F / Phase 2) | Default spine ceremony |
| Fat Debug+PR / CI / Bugbot | Phase 2 lists only (T9D) | Design lock now |

### 4.10 Axis 10 — Red flags (candidate thin list)

Drawn from Superpowers red flags / rationalizations; Toolbelt wording candidates:

- `FACT` [E1] Superpowers lists STOP signals including: quick fix now investigate later; try changing X; multiple changes at once; skip test; “probably X”; proposing solutions before tracing; “one more fix” after 2+. [E1: systematic-debugging SKILL.md Red Flags + Common Rationalizations]
- `INFERENCE` [E4] Candidate Toolbelt red-flag subset for spine:

  - Fixing without a failing repro (or without `NOT-YET-REPRODUCED`)
  - Stacking multiple speculative changes before falsifying one hypothesis
  - Treating code-read alone as reproduction
  - Claiming “fixed” without re-running the **same** repro
  - Continuing fix cycles past F3 threshold without architecture/human check
  - Leaving instrumentation in place after verified fix (cleanup — T9E)

  Premises: Superpowers [E1]; silkyland/debug-agent cleanup [E1]; brief quality lean [E0].

### 4.11 Method implications of working lean B (F1 not locked)

- `FACT` [E0] Brief working lean **B** (spine + reproduce companion); final A vs B is fence **F1** for T9D after deep. [E0: campaign-brief §0 + §0b F1]
- `INFERENCE` [E4] If F1→**B**: spine owns investigate/hypothesize/root-cause/fix/verify/stop; never-fix companion owns intake→repro→minimize→flaky→dossier + iron law enforcement. If F1→**A**: all atoms live in one skill with a hard “repro gate” section. Neither choice changes Theme 7/8 boundaries. Premises: pass2 options [E0]; pass3 B nudge [E0].

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Toolbelt Debug spine can be a thin phase checklist without Superpowers dependency | confirmed (for W1 candidates) | Community atoms converge [E1]; Theme 8 thin spirit [E0] |
| H2 | Execute N=2 and Debug N-fix stop are the same knob | rejected | Different jobs [E0 Theme 7 vs E1 Superpowers Phase 4] |
| H3 | Flaky needs its own elevated skill in W1 | rejected (pending F4) | Brief lean + pass3 “not third skill” [E0]; atoms fit checklist |
| H4 | Defense-in-depth should be mandatory | rejected as default (pending F7) | Thin spirit [E0]; companion says “when invalid data” [E1] |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Hypothesis count | Superpowers: **one** at a time [E1] | debug-agent: **3–5** parallel [E1]; rbouschery: **1–4** ranked [E1] | Prefer **1–4 serial default**; allow **3–5** when parallel instrumentation (T9E). Leave OPEN for elevation microcopy |
| Must write failing automated test before fix | Superpowers Phase 4 MUST + TDD skill [E1] | Toolbelt Theme 7/8: TDD optional; verify evidence required [E0] | Prefer **failing repro** (test \| script \| documented manual); TDD not Debug law |
| N-fix stop | Superpowers **3** [E1] | Familiarity with Execute **2** [E0] | Fence **F3** pros/cons — not locked here |
| Defense-in-depth weight | Superpowers strongly encourages multi-layer [E1] | Theme 9 thin / optional lean [E0] | Fence **F7** |

## 7. Gaps & OPEN (residual → W2)

- `GAP` silkyland `references/flaky-bugs.md` + dossier template deep-read (F4/F5 corroboration).
- `GAP` Live E0 trial of candidate spine on a Toolbelt/`verify-fail` fixture (method smoke).
- `GAP` stas00 art-of-debugging primary re-fetch for shrink-loop wording corroboration (pass3 summarized; not re-fetched this track).
- `OPEN` F3 human pick: N=2 vs N=3 vs soft — needs report pros/cons (delivered here as candidates).
- `OPEN` F4 thickness + whether flaky text lives in spine vs reproduce companion (depends F1).
- `OPEN` F7 optional vs recommended-after-invalid-data final wording.
- `OPEN` F10 paste targets in elevated Execute/Debug surfaces (T9D).
- `OPEN` F1 A vs B final (T9D) — method implications only in §4.11.
- `OPEN` Red-flag list length vs thinness (how many bullets in elevated skill).
- `OPEN` Whether `NOT-YET-REPRODUCED` becomes a first-class status token alongside Execute `blocked` reasons or stays Debug-local tag.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T9A W1 delivers a **candidate method spine + fence packs for F3/F4/F7/F10** sufficient for integrator draft-report tables; elevation waits on fence gate. Premises: §4.1–4.8; coordinator pin hard constraints; `draft-is-not-sot`.
- `INFERENCE` [E4] Theme 8 evidence iron law **composes** at VERIFY SAME REPRO; Debug does not fork plan-verify / execute-verify. Premises: Theme 8 out-of-scope Debug [E0]; pass2 concept map [E0].
- `INFERENCE` [E4] Instrumentation protocol detail (NDJSON atoms, Debug Mode vs Agent) belongs primarily to **T9E/T9B**; spine only requires “falsify with runtime/command evidence” + cleanup before done. Premises: brief track split [E0]; debug-agent packaging park [E1].

## 9. Source list (deduped)

1. `docs/research/notes/theme-9-debug/campaign-brief.md` (E0)
2. `docs/research/notes/theme-9-debug/t9-coordinator-pin.md` (E0)
3. `docs/research/notes/theme-9-debug/scope-normal-pass1.md` (E0)
4. `docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md` (E0)
5. `docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md` (E0)
6. `docs/research/reports/theme-7-execute-pocket.md` (E0 accepted)
7. `docs/research/reports/theme-8-verify-gates.md` (E0 accepted)
8. `docs/PROTOCOL.md` (E0)
9. `skills/implementation-execute/SKILL.md` (E0)
10. obra/superpowers `skills/systematic-debugging/SKILL.md` (E1 via `gh api` 2026-07-30)
11. obra/superpowers `skills/systematic-debugging/root-cause-tracing.md` (E1)
12. obra/superpowers `skills/systematic-debugging/defense-in-depth.md` (E1)
13. obra/superpowers `skills/systematic-debugging/condition-based-waiting.md` (E1)
14. silkyland/reproduce-my-bug `SKILL.md` (E1 via `gh api` 2026-07-30)
15. rbouschery/agent-skills `bug-investigate-fix/SKILL.md` (E1 via `gh api` 2026-07-30)
16. millionco/debug-agent `.agents/skills/debug-agent/SKILL.md` (E1 via `gh api` 2026-07-30)
17. Alexandria corpus=`software_engineering` Dooley Debugging chunks `08490da27bbde1f95a445ac6`, `9e26a07559361b30390a1ffc`, `f2370255822d37ae59c3860e`; Osmani `8d47c2c2c48be20b60557d8e` (E2 — 2026-07-30)
