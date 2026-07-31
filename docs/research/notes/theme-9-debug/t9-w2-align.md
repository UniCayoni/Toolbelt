---
title: "T9 W2-ALIGN — Corroborate W1 residuals (F3/F4/F5 + fence stubs)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9-w2-align-gatherer]
depth: deep
campaign_phase: deep_wave2
aligned_with:
  - docs/research/notes/theme-9-debug/t9a-w1-method-spine.md
  - docs/research/notes/theme-9-debug/t9b-w1-cursor-compose.md
  - docs/research/notes/theme-9-debug/t9c-w1-community-deepen.md
  - docs/research/notes/theme-9-debug/t9d-w1-surface-elevation.md
  - docs/research/notes/theme-9-debug/t9e-w1-instrumentation.md
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
supersedes: null
---

# T9 W2-ALIGN — Corroborate W1 residuals

**Using `research-protocol`**; depth: **deep**; wave: **2**; slice: **W2-ALIGN**.

**Status:** `draft`. Not Debug SoT. No elevation. No collector packaging. No private Cursor API invention. Does **not** re-litigate Theme 8 verify gates.

## 1. Scope

- Question / goal: Corroborate / reconcile Wave-1 residuals — **not** a new Tier-A hunt. Close named P1 gaps with fetches where needed; assemble integrator-ready fence pros/cons stubs (F1–F10) from W1; confirm T9F stays parked.
- In scope: silkyland `flaky-bugs.md` + `dossier-template.md` E1 atoms (F4/F5); F3 vs Theme 7 Execute verify-retry **N=2** vocabulary; merged decision tree (T9A / T9B compose / T9E); F5 light-dossier field minimum; F1–F10 pros/cons assembly; T9F park confirmation; human/E0-only residual list.
- Out of scope: Live E0 Debug Mode trials; elevating skills; writing the full theme report; Theme 8 iron law / N=2 / converge redesign; inventing Cursor private debug-server wire; shipping collectors/MCP.
- Comprehension / research goal type: reuse (align / corroborate)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (all five `t9*-w1-*.md`, campaign-brief, t9-w1-track-board, Theme 7/8 reports, `implementation-execute/SKILL.md`); Shell `gh api` (silkyland/reproduce-my-bug `references/*`) |
| Corpora / URLs searched | `silkyland/reproduce-my-bug` Contents API: `references/` listing + `references/flaky-bugs.md` + `references/dossier-template.md`; local Theme 7–9 docs |
| Queries (exact) | `gh api repos/silkyland/reproduce-my-bug/contents/references`; `…/references/flaky-bugs.md`; `…/references/dossier-template.md` |
| What was *not* searched | Live E0 Debug Mode / CLI `/debug` `/logs` trials; silkyland `evidence-sweep.md` / `repro-harness.md` deep-read (listed but not required for P1); new Tier-A community hunt; Theme 8 rubric re-open |
| Depth | deep |
| Waves / stop_reason | Wave 2 ALIGN only. `stop_reason`: **`diminishing_returns_on_align`** — named P1 residuals closed with E1 fetches or confirmed GAP/OPEN for human/E0; fence stubs assembled; no P0 forcing T9F reopen. Campaign stop remains coordinator `low_return_plus_one`. |
| Provenance (optional PROV) | Entity←W1 T9A–T9E + Theme 7/8 accepted boundaries + silkyland E1 refs; Activity=W2-ALIGN corroboration; Agent=t9-w2-align-gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Systematic attack of W1-named P1 residuals; opportunistic E1 fetch only where W1 left GAP |
| Scope boundary | Align / reconcile only — no new surface design; no elevation |

## 4. Findings

### 4.0 W1 retained (input; not re-litigated)

- `FACT` [E0] W1 tracks T9A–T9E complete; T9F out of W1 with no P0 reopen signal. [E0: `t9-w1-track-board.md` — accessed 2026-07-30]
- `FACT` [E0] Theme 7 accepted: verify-retry **N=2** then `blocked`+`verify-fail`. [E0: `docs/research/reports/theme-7-execute-pocket.md` O-N]
- `FACT` [E0] Shipped Execute: Done-when mismatch → up to **N=2** enhanced local fixes, then `blocked`+`verify-fail`. [E0: `skills/implementation-execute/SKILL.md`]
- `FACT` [E0] Theme 8: Debug/PR out of scope; Theme 7 **N=2 frozen** for Execute verify-retry. [E0: `docs/research/reports/theme-8-verify-gates.md` D14–D21 + FC-PARKS]
- `FACT` [E0] Fence F1–F10 stay open until after deep report; working leans ≠ locks. [E0: `campaign-brief.md` §0b]

### 4.1 P1 close — silkyland flaky + dossier (F4 / F5)

**Repo listing (path present):**

- `FACT` [E1] `silkyland/reproduce-my-bug` `references/` contains: `dossier-template.md`, `evidence-sweep.md`, `flaky-bugs.md`, `repro-harness.md`. [E1: `gh api` contents listing 2026-07-30]

#### 4.1.1 `flaky-bugs.md` atoms (F4)

- `FACT` [E1] Protocol: intermittent = unidentified nondeterminism; job is find source then **FORCE** it. Steps: (A) measure rate (default 10–20 runs); (B) classify source with force levers; (C) force → deliver deterministic / rate-based / not-yet. [E1: silkyland `references/flaky-bugs.md` — `gh api` 2026-07-30]
- `FACT` [E1] Nondeterminism classes + force levers: concurrency/races; time/clock; ordering; randomness; external/network; shared state/cache; test pollution. [E1: same — Step B table]
- `FACT` [E1] Success preference order: (1) deterministic repro with forcing recipe; (2) rate-based + measured rate + loop-until-fail script; (3) not-yet with evidence + eliminated hypotheses + monitoring — never dress not-yet as reproduced. [E1: same — Step C]
- `FACT` [E1] Heisenbugs: prefer passive capture; lean on non-timing force levers (seeds, clock) before sleeps. [E1: same — Heisenbugs]
- `INFERENCE` [E4] Corroborates T9A W1 light checklist + T9C F4 lean: **checklist-in-method**, not a third skill; force-or-rate is the load-bearing atom. Premises: this E1; T9A §4.6 [E0]; T9C §4.2 [E0].
- `INFERENCE` [E4] Optional polish for elevated flaky checklist (still light): add **measure N runs before forcing** + heisenbug passive-capture tip. Premises: flaky-bugs Steps A + Heisenbugs [E1]; T9A checklist already had force/rate [E0].

#### 4.1.2 `dossier-template.md` atoms (F5)

- `FACT` [E1] Dossier is cold-handoff deliverable (`REPRO.md` or `docs/repro/<slug>.md`). Status line: **DETERMINISTIC / RATE-BASED (n/N) / NOT-YET-REPRODUCED**. [E1: silkyland `references/dossier-template.md` — `gh api` 2026-07-30]
- `FACT` [E1] Full template sections: Symptom; The reproduction (artifact, command, failing output, load-bearing triggers, optional forcing recipe); Evidence timeline; Hypotheses (append-only killed + suspected); Attempt log from #0; Handoff (failing test = acceptance criterion; drift conditions; deep-plan / monitoring optional). [E1: same]
- `FACT` [E1] Quality bar: fixer runs repro in under a minute; every timeline row sourced; attempt #0 = runnability spike; append-only ledger; status never oversells. [E1: same — Quality bar]
- `INFERENCE` [E4] Full silkyland template is **too fat** as mandatory Toolbelt companion always-on text (agent load); F5 “light dossier” should keep the quality bar’s load-bearing fields and park ceremony (deep-plan coupling, long timeline tables). Premises: dossier E1; brief thin spirit + F5 lean [E0 campaign-brief]; T9C R2 [E0]; T9D R2 [E0].

### 4.2 P1 close — F3 reconcile (Debug N-fix vs Theme 7 N=2)

| Budget | Owner | Meaning | Citation |
|--------|-------|---------|----------|
| Execute **verify-retry N=2** | Theme 7 / `implementation-execute` | After Done-when Verify mismatch, ≤2 enhanced local fixes inside Files/Interfaces → then `blocked`+`verify-fail` | [E0: Theme 7 O-N; Execute SKILL] |
| Debug **failed-fix-cycle stop** (fence F3) | Theme 9 Debug pocket (candidate) | After investigation + strong/confirmed hypothesis, stop thrashing root-cause patches → architecture / human | [E0: T9A §4.5; E1 Superpowers ≥3 via T9A/T9C] |

- `FACT` [E0] T9A already rejected conflating the two budgets (H2). [E0: `t9a-w1-method-spine.md` §5 H2]
- `FACT` [E0] Pass2 / brief: do not replace Execute N=2 with Debug’s fix budget. [E0: campaign-brief non-goals; T9A §4.0 citing scope-pass2]
- `INFERENCE` [E4] **Recommend separate vocabulary** (candidate wording for integrator / fence — **not lock**):

  | Concept | Candidate token | Do **not** say |
  |---------| | ----------------- | ---------------- |
  | Execute Done-when retry budget | `verify-retry N=2` (keep Theme 7 language) | “debug N=2” for Execute |
  | Debug root-cause thrash stop | `debug-fix-cycles` (or `failed-fix-cycles`) with chosen N | Reuse bare `N=2` without qualifier |
  | Seam after Execute exhaustion | Trigger **T-VF**: enter Debug method; do not burn more **verify-retries** | “retry N again” under Execute |

  Premises: Theme 7 O-N [E0]; T9A F3 table + T-VF [E0]; T9C R1 [E0]; Theme 8 freezes Execute N=2 [E0].

#### F3 pros/cons (integrator stub — working leans labeled)

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **N=2** `debug-fix-cycles` | Stops thrash earlier; familiar number | Premature escalate on hard bugs; **highest conflation risk** with Execute verify-retry unless vocab separated | Viable only with strict separate tokens |
| **N=3** `debug-fix-cycles` | Strong Superpowers E1 echo [E0 via T9A/T9C]; room for one informed retry after re-investigate | Slightly more thrash; still arbitrary | **Brief working lean ~3** |
| **Soft** (no hard N) | Adaptive; thin | Weak stop signal; audit-hard; fights quality-over-thinness | Weak default |

- `INFERENCE` [E4] Prefer counting **failed fix cycles after a confirmed/strong hypothesis**, not failed hypothesis tests. Premises: T9A §4.5 [E0].
- `OPEN` Human picks F3 after fence gate; ALIGN does not lock.

### 4.3 P1 close — unified decision tree (T9A + T9B + T9E)

**Sources merged:** T9A spine checklist §4.1 [E0]; T9B compose matrix §4.8 [E0]; T9E tree §4.4 [E0].

#### 4.3.1 Merged candidate tree (not elevated)

```text
0. INTAKE — expected vs actual; artifacts; frequency; surface (test/CLI/UI/API/prod signal)
1. Can you REPRODUCE on the same surface (or document NOT-YET-REPRODUCED)?
   ├─ NO → NOT-YET-REPRODUCED dossier atoms; escalate needs-human / observe; no guess-fix
   └─ YES → shrink to load-bearing; if intermittent → flaky light checklist (force or rate)
2. Is failure already explained by static read + existing failing test/logs?
   ├─ YES → light Agent path: cite evidence → root-cause → minimal fix → VERIFY SAME REPRO
   │        Prefer Terminal (run test/command, READ available output)
   └─ NO → need runtime discrimination?
            ├─ Unclear cause / race / timing / perf / regression + Debug Mode available
            │  + human can drive repro → PREFER Cursor Debug Mode
            │     (picker / Shift+Tab / CLI `/debug`; `/logs` for product log path)
            ├─ UI / frontend → Browser (console, network, greppable log files, screenshots)
            │  (+ Debug Mode if cross-layer cause still unclear)
            ├─ CLI / build / test → Terminal first
            ├─ Prod spike + host MCP configured → MCP observe → still seek local repro
            └─ Debug Mode unavailable / agent-driven CLI-heavy → Agent-mode instrumentation
               (hypothesisId + CONFIRMED|REJECTED|INCONCLUSIVE + cleanup; NO private wire;
                NO Toolbelt collector)
3. HYPOTHESIZE (1–4 serial default; 3–5 if parallel instrument) → FALSIFY → ROOT CAUSE (backward)
4. MINIMAL FIX → VERIFY SAME REPRO → cleanup instrumentation / Checkpoints if thrash
5. STOP / ESCALATE — after `debug-fix-cycles` threshold (F3) or architecture smell → human
   (separate from Execute `verify-retry N=2`)
```

#### 4.3.2 Conflict log (tree merge)

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Hypothesis count | T9A: 1–4 serial default; 3–5 parallel [E0] | T9E: 3–5 before instrument [E0]; Superpowers: one-at-a-time [E0 via T9A] | **Keep T9A compose table** — serial 1–4 default; 3–5 when instrumenting in parallel |
| Instrument-first vs reproduce-first | millionco via T9C/T9E: instrument early [E0] | silkyland/Superpowers/T9A: reproduce/evidence first [E0] | **Reproduce (or NOT-YET) before product fix**; instrument when discrimination needed (step 2) — not always-on collector |
| Clear stack → Agent vs Debug Mode | T9B/T9E: clear fail → Terminal/Agent [E0] | Cursor Debug Mode still valid if cause unclear after stack [E1 via T9B] | Prefer Terminal first for clear local repro; escalate to Debug Mode when still unclear |
| “Read full output” | Theme 8 / Toolbelt compose discipline [E0 T9B] | Cursor Terminal docs omit explicit mandate [E0 T9B GAP] | Keep as Toolbelt compose teaching; do not claim Cursor product law |
| Private wire | Community collector HTTP [E0 T9E] | Cursor primary docs: local server exists, no public wire [E0 T9B/T9E GAP] | **GAP stands** — compose mode/`/debug`/`/logs` only |

### 4.4 P1 close — F5 light-dossier field minimum

**Shortest field list** (candidate for never-fix companion lean — **not lock**). Derived from silkyland E1 load-bearing quality bar + T9C transferable atoms; cuts deep-plan coupling and optional fat sections.

| # | Field | Why keep | Source |
|---|-------|----------|--------|
| 1 | **Status** — `DETERMINISTIC` \| `RATE-BASED (n/N)` \| `NOT-YET-REPRODUCED` | Prevents oversell | [E1 dossier] |
| 2 | **Symptom** — expected vs actual (+ frequency if known) | Intake | [E1 dossier Symptom] |
| 3 | **Command / steps** — exact repro | Cold run | [E1 “The reproduction”] |
| 4 | **Failing output** — verbatim excerpt | Evidence | [E1] |
| 5 | **Load-bearing triggers** — short list (or “unknown”) | Minimize/shrink | [E1] |
| 6 | **Hypothesis ledger** — append-only killed/open (can be bullets) | Honesty / handoff | [E1 Hypotheses] |
| 7 | **Attempt #0+** — at least runnability / first repro attempt | Anti-fabrication | [E1 Attempt log] |
| 8 | **Handoff acceptance** — “fix done when this repro turns green” (or monitoring if NOT-YET) | Same-repro verify seam | [E1 Handoff] |

**Park / optional (not in light minimum):** long Evidence timeline table; environment encyclopedia; deep-plan pointer; permanent regression-test law beyond “prefer keep failing repro”; silkyland product path `docs/repro/<slug>.md` as Toolbelt SoT.

- `INFERENCE` [E4] Under F1→**B** + F5 lean R2: companion teaches never-fix + this 8-field minimum; full silkyland template remains inspiration. Under F1→**A**: same fields as spine section. Premises: §4.1.2; T9D §4.4 [E0]; T9C §8.2 R2 [E0].
- `OPEN` Exact template path (`docs/templates/repro-light.md` vs skill `references/`) → elevate-time / T9D — not authored here.

### 4.5 Fence pros/cons stubs F1–F10 (integrator-ready)

Working leans labeled **not locks**. Citations prefer W1 notes (E0) + new silkyland E1 where relevant.

#### F1 — A vs B final (spine alone vs spine + never-fix companion)

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **A** One spine | Thinnest; one announce | Iron-law competes with fix steps | First-class alternative |
| **B** Spine + reproduce companion | Quality lean; never-fix gravity; Theme 8 spine+supplement pattern | Two surfaces | **Preferred** [E0 brief; T9D §4.2] |
| **C** Compose-only | Zero Toolbelt skill | Weak pocket discoverability | Defer/reject default |
| **D** Fat Debug+PR | Covers Phase 2 leftovers early | Sprawl; brief defers | Phase 2 only |

Cite: [E0: T9D §4.2; campaign-brief §0b F1; T9C never-fix vs fix-in-skill conflict]

#### F2 — Skill names (avoid “Debug Mode”)

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| Spine `systematic-debug` or `investigate-reproduce` | Discoverable; ≠ product mode | Soft Superpowers / “debug” stem echo | Shortlist [E0 T9D §4.3] |
| Companion `reproduce-bug` (if B) | Never-fix gravity | Needs strong description triggers | Pair under B |
| `implementation-debug` | Ladder namespace | Confuse with `*-verify` | Optional only |
| Bare `debug` / `debug-mode` | — | Product collision | **Avoid** |

Cite: [E0: T9D §4.3; T9B §8.3]. `GAP`: live Cursor skill-picker collision — human/E0 later.

#### F3 — N-fix stop (see §4.2)

Working lean: **~3** with token `debug-fix-cycles` (separate from Execute `verify-retry N=2`). Soft = weak. Cite: [E0: T9A §4.5; T9C §8.1; Theme 7 O-N].

#### F4 — Flaky protocol thickness

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **Checklist-in-spine** (or in reproduce companion if B) | Covers force/rate; thin; silkyland E1 | Section skip risk | **Light checklist** |
| Companion-only flaky skill | Isolates encyclopedia | Third skill sprawl | Avoid unless overload |
| Park thin (omit) | Shortest | Loses high-signal intermittent path | Weak vs quality lean |

Cite: [E0: T9A §4.6; T9C §4.2]; [E1: silkyland `flaky-bugs.md` this note §4.1.1].

#### F5 — Reproduce companion shape

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| Never-fix only | Thinnest | Weak cold handoff | Viable thin |
| **Never-fix + light dossier** | Cold fixer pickup; status honesty | Template load if uncapped | **Preferred** — use §4.4 8-field min |
| Full silkyland port | Max fidelity | Fat; product paths; deep-plan coupling | Park |

Cite: [E0: T9D §4.4; T9C §4.2]; [E1: dossier-template this note §4.1.2].

#### F6 — Instrumentation home

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **Section of spine (+ T9E atoms)** | One place; decision tree; no collector | Spine length | **Preferred** |
| Short companion | Isolates Agent protocol | Sprawl; packaging temptation | Reopen only if bloat |
| Compose Debug Mode only | Thinnest text | No Agent fallback; quality lean conflict | Reject as sole home |

Cite: [E0: T9E §4.9; T9B §8.1; T9D §4.5]. Private wire GAP stands.

#### F7 — Defense-in-depth

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **Optional post-fix note** | Thin default | Easy to skip when valuable | **Preferred** |
| Recommended after invalid-data | Stronger quality; Superpowers echo | Over-engineering risk | Viable quality nudge |
| Mandatory every bug | Max hardening | Violates thin / minimal-fix | Reject |

Cite: [E0: T9A §4.7; T9C §8.1 F7].

#### F8 — T9F swarm

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **Stay parked** | Thin default; Dimillian ceremony cost | Large-ambiguity bugs lack parallel read-only path | **Park** |
| Reopen now | Multi-agent diagnosis | P0 cost not shown in W1/W2 | No reopen |

- `FACT` [E0] W1 T9C/T9E/track-board: no P0 ambiguity forcing reopen. [E0: T9C §8.2; T9E §9; track-board]
- `INFERENCE` [E4] **T9F stays parked.** No W2 ALIGN finding raises P0 ambiguity cost. Premises: above FACTs; brief F8.

#### F9 — Always-on debug rule

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **Skill-only** | Theme 8 D3 + packs opt-in; situational pocket | Miss if handoffs weak | **Confirm skill-only** |
| Always-on rule | Forces evidence culture | False triggers; stacks on product Debug Mode | Unlikely |

Cite: [E0: T9D §4.6; T9B §8.2]. No primary-doc counter-signal in W1; ALIGN adds none.

#### F10 — Execute→Debug seam wording

| Option | Pros | Cons | Working lean |
|--------|------|------|--------------|
| **T-VF + T-UB minimum** | Covers verify-fail + user bug | Misses Critical/major-deviation edges | Minimum viable |
| Full T-VF/T-UB/T-MD/T-CR/T-NYR | Clearer routing [E0 T9A §4.8] | More handoff text | Quality set once surfaces exist |
| Pointer-only (“see Debug”) | Minimal edit | Weak discoverability | Weak |

Cite: [E0: T9A §4.8; T9D §4.7]. Do **not** redesign Theme 7 N=2.

### 4.6 T9F park confirmation

- `FACT` [E0] Brief F8 working lean: parked; reopen only if residual shows P0 ambiguity cost. [E0: campaign-brief §0b F8]
- `FACT` [E0] W1: Dimillian swarm = ceremony; diagnosis-first park; T9F out. [E0: T9C §4.6, §8.2]
- `INFERENCE` [E4] ALIGN finds **no P0** (contradictory method SoT, missing atom blocking all fences, or swarm-required ambiguity) → **do not reopen T9F swarm**. Premises: §4.1–4.5 closures; conflict log has resolutions without swarm.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | silkyland flaky/dossier E1 corroborates F4 light checklist + F5 light dossier without third skill | confirmed | §4.1 |
| H2 | Execute N=2 and Debug fix-stop must use separate vocabulary | confirmed (align) | §4.2; Theme 7 O-N; T9A H2 |
| H3 | T9A/T9B/T9E trees merge without P0 contradiction | confirmed | §4.3 conflict log |
| H4 | T9F must reopen in W2 | rejected | §4.6 |
| H5 | Full silkyland dossier should be mandatory Toolbelt text | rejected | §4.4 light minimum |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| N numeric | Theme 7 **verify-retry N=2** [E0] | Superpowers Debug **≥3** fix stop [E0 via T9A] | Separate tokens (§4.2); F3 human pick |
| Dossier thickness | silkyland full template [E1] | Toolbelt thin + F5 lean [E0] | Light 8-field minimum (§4.4) |
| Decision tree | See §4.3.2 | — | Merged tree + logged resolutions |

## 7. Gaps & OPEN

### Closed this wave (were W1 P1)

| ID | Was | Now |
|----|-----|-----|
| T9A flaky/dossier GAP | Unfetched bodies | **Closed** — E1 §4.1 |
| T9C R1 F3 vocab | Integrator wording | **Closed candidate** — §4.2 (human still picks N) |
| T9C R2 F5 field min | OPEN | **Closed candidate** — §4.4 |
| T9E R3 tree align | OPEN | **Closed candidate** — §4.3 |

### Residuals that need **human** and/or **E0 only** (do not invent)

| ID | Needs | Residual |
|----|-------|----------|
| R-H1 | Human fence | Adjudicate F1–F10 using §4.5 stubs (after integrate report) |
| R-H2 | Human | Final F3 N + accept `debug-fix-cycles` vs alternate token |
| R-H3 | Human | Final F2 slug pair after F1 |
| R-E0-1 | E0 (optional) | Live Debug Mode / CLI `/debug`+`/logs` path shape observe-only |
| R-E0-2 | E0 (optional) | verify-fail → Debug handoff dry-run on a fixture |
| R-E0-3 | E0 (optional) | Cursor skill-picker description collision smoke |
| R-OPEN-1 | Integrate polish | Agent-mode default sink recommendation (file NDJSON-*shaped* vs tagged stdout) — still no collector [E0 T9E GAP] |
| R-OPEN-2 | Integrate / elevate | Bounce vs warn if Execute patches after verify-fail without Debug [E0 T9D OPEN] |
| R-OPEN-3 | Elevate-time | Light dossier template path + Execute Handoffs paste targets |
| R-PARK | — | Cursor private debug-server wire — **confirmed GAP**; do not invent [E0 T9B/T9E] |
| R-PARK | — | T9F swarm — stay parked (§4.6) |
| R-OUT | — | Theme 8 verify gates — do not re-open |

**Not claimed closed:** live trials, human fence picks, skill elevation, full theme report.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Integrator can draft `theme-9-debug-pocket.md` fence § from §4.5 without another Tier-A gatherer wave for F3/F4/F5 atoms. Premises: P1 closures; `draft-is-not-sot`.
- `INFERENCE` [E4] PLUS1 should only chase human/E0 residuals in §7 — not new community Tier-A. Premises: stop rule; track-board W2 focus.
- `INFERENCE` [E4] Elevation remains blocked until fence gate + theme accept. Premises: campaign-brief §4–§5.

## 9. Source list (deduped)

1. `docs/research/notes/theme-9-debug/t9a-w1-method-spine.md` (E0)
2. `docs/research/notes/theme-9-debug/t9b-w1-cursor-compose.md` (E0)
3. `docs/research/notes/theme-9-debug/t9c-w1-community-deepen.md` (E0)
4. `docs/research/notes/theme-9-debug/t9d-w1-surface-elevation.md` (E0)
5. `docs/research/notes/theme-9-debug/t9e-w1-instrumentation.md` (E0)
6. `docs/research/notes/theme-9-debug/campaign-brief.md` (E0)
7. `docs/research/notes/theme-9-debug/t9-w1-track-board.md` (E0)
8. `docs/research/reports/theme-7-execute-pocket.md` (E0 accepted)
9. `docs/research/reports/theme-8-verify-gates.md` (E0 accepted)
10. `skills/implementation-execute/SKILL.md` (E0)
11. silkyland/reproduce-my-bug `references/flaky-bugs.md` (E1 via `gh api` 2026-07-30)
12. silkyland/reproduce-my-bug `references/dossier-template.md` (E1 via `gh api` 2026-07-30)
13. silkyland/reproduce-my-bug `references/` listing (E1 via `gh api` 2026-07-30)

---

## Return summary (for coordinator)

| Field | Value |
|-------|-------|
| Note path | `docs/research/notes/theme-9-debug/t9-w2-align.md` |
| stop_reason | `diminishing_returns_on_align` |
| F3 headline | Separate vocab: Execute `verify-retry N=2` vs Debug `debug-fix-cycles` (lean ~3); do not merge budgets |
| F4 headline | silkyland flaky E1 corroborates measure→force→rate/not-yet; light checklist (not third skill) |
| F5 headline | Never-fix + **8-field light dossier** minimum; full silkyland template parked as inspiration |
| T9F | **Stays parked** — no P0 reopen |
| Left for PLUS1 / integrate | Human fence F1–F10; optional E0 trials; integrate report; Agent sink polish; Handoffs paste — **no new Tier-A hunt** |
