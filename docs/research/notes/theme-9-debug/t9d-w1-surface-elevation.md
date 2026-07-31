---
title: "T9D W1 — Surface shape & elevation candidates (Debug pocket)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9d-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-coordinator-pin.md
  - docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/packs/README.md
supersedes: null
---

# T9D W1 — Surface shape & elevation candidates (Debug pocket)

**Using `research-protocol`**.

**Status:** `draft` gatherer note. **Not** Debug SoT. **No elevation** — candidates + pros/cons only. T9F out of W1.

---

## 1. Scope

- Question / goal: Propose Toolbelt Debug-pocket **surface shape** options (A/B/C/D), **naming** candidates (avoid Cursor “Debug Mode”), **reproduce companion** and **instrumentation home** packaging options, **skill-only vs always-on rule**, **Execute/Verify→Debug wiring** prose, **elevation order** (post fence-gate only), and a **Phase 2 PR/CI/Bugbot leftover list** (list only).
- In scope: Fence **F1, F2, F5, F6, F9, F10** evidence + candidate pros/cons; Theme 8 elevation pattern as E0 inspiration; collision check vs existing Toolbelt skill names; packs stub alignment.
- Out of scope: Elevating skills/rules; designing method spine body (T9A); Cursor compose deep-read (T9B); community deep-read (T9C); full instrumentation protocol atoms (T9E — coordinate only); T9F swarm design; inventing Cursor private debug APIs; shipping collectors/MCP; locking A vs B.
- Comprehension / research goal type: perfective (new pocket packaging candidates; no product ship this wave).

---

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (brief, coordinator pin, pass2/pass3, Theme 8 report, packs README, Theme 8 T8D note, shipped Plan/Execute/verify SKILLs); Glob (`skills/*/SKILL.md`, `rules/`); Grep (debug/reproduce/investigate under skills + rules) |
| Corpora / URLs searched | None this slice (local E0 + draft scoping notes only) |
| Queries (exact) | skill names under `d:\Toolbelt\skills`; debug\|reproduce\|investigate\|instrument under skills/rules; Theme 8 companion naming / elevation order / G10 leftovers |
| What was *not* searched | Live Cursor skill-discovery UX; Alexandria; GitHub community skill bodies (T9C); Cursor Debug Mode primary re-fetch (T9B); T9A/T9E peer notes (may land in parallel); plugin.json keyword collision beyond directory names |
| Depth | deep |
| Waves / stop_reason | W1 gatherer slice; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←Theme 9 brief/pass2–3 + Theme 8 accepted report + shipped skills; Activity=T9D W1 surface/elevation gather; Agent=t9d-w1-gatherer |

---

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | hybrid |
| Why this mode | Surface options already named in pass2 (systematic); naming/wiring need E0 inventory of shipped skills + Theme 8 elevation precedent (as-needed) |
| Scope boundary | Included: `docs/research/notes/theme-9-debug/{campaign-brief,t9-coordinator-pin,scope-normal-pass*}`, `docs/research/reports/theme-8-verify-gates.md`, `docs/research/notes/theme-8-verify/t8d-w1-surface-elevation.md` (G10/elevation-order pattern), `docs/packs/README.md`, `skills/**/SKILL.md`, `rules/*.mdc`. Excluded: writing skills; T9A/T9E method bodies; PR/CI design |

---

## 4. Findings

### 4.1 Input law & working leans (not locks)

- `FACT` [E0] Brief §0: quality/effectiveness over thinness-alone; surface **working lean B** (spine + reproduce companion); final A vs B still fence **F1**; T9F out of W1; PR/CI/Bugbot = Phase 2 list-only via T9D; elevate only after fence gate + accept. [E0: `docs/research/notes/theme-9-debug/campaign-brief.md` §0, §0b, §4–§5]
- `FACT` [E0] Coordinator pin: W1 = T9A‖T9B‖T9C‖T9D‖T9E; do not elevate; fence F1–F10 = evidence + candidate pros/cons only; W1 stop per track `wave1_slice_coverage`. [E0: `docs/research/notes/theme-9-debug/t9-coordinator-pin.md`]
- `FACT` [E0] Packs: **Debug / investigate** = deep Wave 1 in flight; **PR / workflow** = stub later; Verify gates shipped and explicitly **not** Debug. [E0: `docs/packs/README.md`]
- `FACT` [E0] Theme 8 accepted: elevated companions `implementation-plan-verify` + `implementation-execute-verify`; hybrid orchestration; **skill-only** (no always-on verify rule); Debug/PR out of scope. [E0: `docs/research/reports/theme-8-verify-gates.md` elevation decisions D1–D3, §5]
- `FACT` [E0] Pass-2 named surface options **A/B/C/D**; pass-3 marked **B slightly stronger** after never-fix + dossier evidence. [E0: `scope-normal-pass2-expand.md` §3.5; `scope-normal-pass3-deepen.md` §10–§11]
- `INFERENCE` [E4] Theme 8 naming pattern for companions is **`{pocket-spine}-{role}`** hyphenated skills (`implementation-plan-verify`, `implementation-execute-verify`), companions-first then orchestrator wires, skill-only default. Theme 9 may mirror that *shape* without copying the `implementation-*-verify` names (different pocket). Premises: Theme 8 report D1/D3; T8D §4.8; shipped skill frontmatter names.

### 4.2 F1 — Options A/B/C/D vs thinness + quality lean

| Option | Shape | Pros | Cons |
|--------|-------|------|------|
| **A. Thin spine skill** | One skill holds investigate → reproduce → hypothesize → root-cause → fix → re-verify (+ light flaky checklist in-spine) | Thinnest discoverable Toolbelt surface; matches Theme 6 single-spine pocket; one announce/`Using`; lowest skill-count sprawl | Reproduce-never-fix gravity competes with fix steps inside one doc (agent may skip hard gate); weaker match to quality lean “evidence not assumptions”; flaky/dossier may bloat spine |
| **B. Spine + reproduce companion** *(working lean)* | Spine owns full method; companion = never-fix reproduce (± light dossier) invoked at hard gate / user “repro this” | Matches quality lean + silkyland never-fix gravity [E0 pass3]; Theme 7/8 “spine + named supplement” precedent [E0 Theme 8]; clear handoff artifact for fixer; keeps spine thinner on intake/flaky | Two surfaces to discover/maintain; risk agents skip companion; name + description triggers must make handoff obvious |
| **C. Compose-only** | Rules/docs pointing at Cursor Debug Mode + Theme 8 verify; no Toolbelt debug skill | Absolute minimum Toolbelt surface count | Weak Toolbelt method discoverability; fails packs “Debug / investigate” pocket intent; agents fall back to ad-hoc or Cursor Mode alone without Toolbelt discipline [E0 pass2 §3.5] |
| **D. Fat Debug+PR pack** | Many skills (CI, Bugbot, git, PR, swarm, …) now | Covers packs stub row + Theme 8 G10 leftovers in one wave | Sprawl; conflicts thin Toolbelt spirit **now**; brief defers PR/CI Phase 2 + T9F park [E0 brief §0] |

- `FACT` [E0] Brief fence F1 working lean **B preferred**; keep A first-class until human fence adjudication; defer C/D. [E0: campaign-brief §0b F1; §5]
- `INFERENCE` [E4] For integrator fence table: recommend presenting **A and B as the live choice**; treat C as reject-by-default (discoverability); D as Phase-2/stub only. Quality lean nudges B; thinness nudges A — human picks after deep report. Premises: brief §0 quality lean; F1; pass3 B-slightly-stronger.
- `INFERENCE` [E4] Do **not** invent a third elevated skill for flaky protocol unless W2 shows spine+companion overload (F4 owned by T9A; T9D notes only: flaky stays checklist, not surface). Premises: brief F4; pass3 “not a third skill”.

### 4.3 F2 — Skill name candidates + collision check

**Existing Toolbelt skill directory names (E0 inventory):**  
`author-agents-md`, `author-cursor-surfaces`, `codebase-recon`, `creative-narrative-design`, `creative-systems-design`, `creative-world-character-design`, `design-process`, `docs-research`, `draft-adr`, `implementation-execute`, `implementation-execute-subagents`, `implementation-execute-verify`, `implementation-plan`, `implementation-plan-verify`, `research-protocol`, `technical-design`.  
**No** existing `*debug*`, `*reproduce*`, `*investigate*`, or `*instrument*` skill dirs. [E0: Glob `skills/*/SKILL.md`]

**Rules touching “debug” (E0):** only `research-skill-coexistence.mdc` mentions Superpowers “debug systematically” as process layer — not a Toolbelt debug surface name. [E0: `rules/research-skill-coexistence.mdc`]

**Collision hazards:**

| Hazard | Why it matters |
|--------|----------------|
| Cursor product **“Debug Mode”** / CLI `/debug` | Brief F2: avoid naming that reads as the product mode |
| Superpowers `systematic-debugging` | Soft echo if Toolbelt uses near-identical slug (inspire OK; don’t imply dependency) |
| Theme 8 `*-verify` | Must not imply Debug owns Plan/Execute completion gates |
| Generic `debug` alone | High collision with Cursor mode + community “debug-agent” cluster |

**Name candidates (2–4; draft only — not locks):**

| # | Candidate slug | Role | Collision notes | Fit |
|---|----------------|------|-----------------|-----|
| N1 | `systematic-debug` | Spine (A or B) | Shares stem “debug” with Cursor Debug Mode but **≠** `debug-mode` / “Debug Mode”; soft Superpowers echo (`systematic-debugging`) | Clear method gravity; pass2 example |
| N2 | `investigate-reproduce` | Spine (A or B) | Avoids product phrase “Debug Mode”; no Toolbelt collision | Emphasizes quality lean; slightly longer |
| N3 | `implementation-debug` | Spine | Parallel to Theme 6–8 `implementation-*` namespace; still contains “debug”; must Out-of-scope vs `*-verify` | Ladder continuity; risk agents confuse with verify companions |
| N4 | `reproduce-bug` | Companion (if F1→B) | Distinct from Cursor Debug Mode; mirrors pass2 example; no Toolbelt collision | Never-fix companion gravity; pair with N1 or N2 |

**Alternate companion slugs (if N4 rejected):** `never-fix-reproduce`, `implementation-reproduce` (namespace parallel; heavier).

- `INFERENCE` [E4] Prefer **avoiding** exact product strings `debug-mode`, `Debug Mode`, and bare `debug` as the skill `name:`. Prefer N1 or N2 for spine + N4 for companion under lean B; N3 only if human wants strict `implementation-*` ladder naming and accepts “debug” stem. Premises: F2; Theme 8 naming pattern; E0 skill inventory.
- `GAP` Live Cursor skill picker ranking / description collision with native Debug Mode — not measured this slice. Follow-up: W2 smoke after draft descriptions exist.
- `OPEN` Final pair after F1 adjudication (A needs one name; B needs spine+companion pair).

### 4.4 F5 — Reproduce companion shape options

| Shape | Pros | Cons |
|-------|------|------|
| **R1. Never-fix only** | Thinnest companion; hard gate is the product; minimal agent load | Weak handoff artifact for fixer; flaky/rate documentation may scatter into chat |
| **R2. Never-fix + light dossier** *(brief working lean)* | Durable repro command + failing output + eliminated hypotheses; matches silkyland Steps 6–7 atoms [E0 pass3]; supports Execute/Debug resume across sessions | Template size vs agent load; risk dossier becomes ceremony if not capped “light” |
| **R3. Full reproduce-my-bug port** | Maximum fidelity to community skill | Too fat for Toolbelt thin spirit; product-specific paths; conflicts “extract atoms, cut coupling” |

- `FACT` [E0] Brief F5 working lean: never-fix + light dossier; pass3 strengthens B and argues named flaky checklist inside method — still not a third skill. [E0: campaign-brief §0b F5; pass3 §4, §10]
- `INFERENCE` [E4] Under lean **B**, elevate at most **one** reproduce companion; prefer **R2** with a short dossier template (candidate path e.g. `docs/templates/repro-light.md` or skill `references/` — **not authored this wave**). Under lean **A**, fold R1/R2 atoms into spine sections (no companion). Premises: F1/F5; Theme 8 thin companions + progressive disclosure.

### 4.5 F6 — Instrumentation home options (coordinate with T9E)

T9D owns **packaging home** only. T9E owns protocol atoms (hypothesisId / CONFIRMED|REJECTED|INCONCLUSIVE / cleanup regions / when Debug Mode vs Agent). Do **not** duplicate T9E bodies here; do **not** propose shipping collectors/MCP.

| Home | Pros | Cons |
|------|------|------|
| **I1. Section of spine** *(brief working lean)* | One discoverable place; no third skill; Theme 6 “light in-spine” precedent | Spine length; T9E atoms must stay progressive-disclosure short |
| **I2. Short companion skill** | Isolates NDJSON/file protocol when Debug Mode unavailable | Skill sprawl vs thin spirit; may duplicate Cursor Debug Mode teaching; only if W2 shows I1 overload |
| **I3. Compose Cursor Debug Mode only** | Zero Toolbelt instrumentation text | Leaves Agent-mode / no-Debug-Mode hosts without protocol; conflicts T9E existence in W1 |

- `FACT` [E0] Brief F6 lean: section of spine (+ T9E atoms); no collector packaging. [E0: campaign-brief §0b F6, §5]
- `INFERENCE` [E4] Packaging recommendation for fence: **I1** default; I2 only if integrator/T9E show spine bloat; I3 reject as sole home (compose remains **part of** I1 via T9B). Premises: F6; pass3 T9E track; coordinator “don’t ship collectors”.

### 4.6 F9 — Always-on rule vs skill-only

| Option | Pros | Cons |
|--------|------|------|
| **Skill-only** *(working lean: unlikely always-on)* | Matches Theme 6 #10 + Theme 8 D3 + packs “intelligent / opt-in except thin always-on (draft≠SoT)” [E0]; debug is situational (not every chat) | Agents may miss pocket unless description triggers + Execute/Verify handoffs are strong |
| **Always-on debug rule** | Forces evidence culture | High false-trigger cost; fights thin opt-in norm; Debug Mode already a product switch — Toolbelt rule would stack ceremony |

- `FACT` [E0] Packs README: keep new rules intelligent/opt-in by default except thin always-on (`draft-is-not-sot`). [E0: `docs/packs/README.md`]
- `FACT` [E0] Theme 8 rejected always-on verify rule (D3). [E0: theme-8-verify-gates.md]
- `INFERENCE` [E4] **Confirm skill-only** unless W2 finds strong counter (e.g. repeated verify-fail→patch thrash with zero Debug invoke in live trials — not observed this slice). No always-on debug rule candidate for elevation. Premises: F9 lean; Theme 8 D3; packs README.

### 4.7 F10 — Execute→Debug / Verify→Debug wiring (candidate prose)

**Current E0 gap:** Execute Handoffs still say “Debug pack later” on verify-fail; execute-verify Handoffs say “PR / debug / merge → Later Debug/PR pack”. [E0: `skills/implementation-execute/SKILL.md` Handoffs; `skills/implementation-execute-verify/SKILL.md` Handoffs]

**Do not** replace Execute **N=2** verify-retry budget with Debug’s fix-stop budget (pass2 / Theme 7 boundary). [E0: pass2 §3.6; Theme 7/8 reports]

#### Candidate trigger language (draft)

| From | Trigger (candidate wording) | Into Debug |
|------|----------------------------|------------|
| `implementation-execute` / `-subagents` | After Done-when Verify exhausted → `blocked` + **`verify-fail`**, and symptom/cause still unclear (not a known Files/Interfaces fix) | Announce Debug spine; **reproduce the failing Verify** (same command/surface) before further patches |
| Execute | **`major-deviation`** / weird runtime beyond plan Files | Debug spine (compose Cursor Debug Mode when cause unclear / needs runtime logs) |
| Ad-hoc | User reports a bug outside the plan | Full Debug spine (investigate → reproduce gate → …) |
| `implementation-execute-verify` | Post-green finding **Critical** (or Important) where faithfulness/evidence break is **unclear** — not a trivial plan typo | Debug spine **before** more patches; then return to Execute/verify with evidence |
| Either verify companion | Reviewer suspects wrong root cause / thrashing patches | Stop patch loop → Debug reproduce + falsify |

#### Candidate Handoffs rows (post-elevate only — not applied now)

**Execute (replace “Debug pack later” row):**

| Need | Use |
|------|-----|
| Verify fails after N=2 / cause unclear | **`{spine-name}`** (Debug pocket) — reproduce failing Verify; do not invent; HITL if blocked |
| User bug / weird runtime | **`{spine-name}`**; optional **`{reproduce-companion}`** when never-fix repro needed first |

**Execute-verify:**

| Need | Use |
|------|-----|
| Critical / unclear failure after green | **`{spine-name}`** before more code patches |
| PR / merge / CI babysit | Phase 2 PR/workflow pack — **not** Debug method |

- `INFERENCE` [E4] Wire strength: “almost certain” per brief §5 — exact slug placeholders resolve after F1/F2 fence. Premises: F10; pass2 §3.6; brief §5.
- `OPEN` Bounce vs warn if Execute continues patching after verify-fail without Debug invoke — leave to integrator/fence (mirrors Theme 8 G4 openness pattern).

### 4.8 Elevation order candidates (post fence-gate / accept only)

Hard rule: **no elevation** while F1–F10 open; order below is **candidate sequence after** draft report → human fence adjudication → theme accept → `/author-cursor-surfaces`. Theme 8 pattern cited as **E0 inspiration** only (not a lock that Theme 9 must copy every step). [E0: theme-8-verify-gates.md; t8d-w1 §4.8; campaign-brief §4]

**Order candidate if F1 → B:**

1. Fence gate + accept Theme 9 report (method + F1–F10 decisions)
2. Elevate spine skill (N1 or N2 or N3 as adjudicated)
3. Elevate reproduce companion (N4 / R2 as adjudicated)
4. Wire Execute + Execute-subagents Handoffs/triggers (F10)
5. Wire Execute-verify Handoffs for Critical/unclear → Debug
6. Update `docs/packs/README.md` Debug / investigate → shipped (surfaces named); keep PR/workflow stub
7. Explicitly **do not** elevate: always-on debug rule (F9); C/D fat pack; T9F swarm; PR/CI/Bugbot skills; collectors/MCP

**Order candidate if F1 → A:**

1. Fence gate + accept  
2. Elevate single spine (reproduce + light dossier sections in-spine)  
3. Wire Execute / Execute-verify / -subagents (F10)  
4. Packs README update  
5. Same explicit non-elevations as above  

- `INFERENCE` [E4] Prefer **skills-first then wires** (Theme 8 companions-first precedent) so Handoffs targets exist. Premises: t8d-w1 §4.8; Theme 8 elevation status.

### 4.9 Phase 2 PR/CI/Bugbot leftover list (no design)

List only — **not** Theme 9 Wave 1 elevation. Sources: packs stub; Theme 8 G10; brief §0 PR Phase 2; T9F park.

| Leftover | Note |
|----------|------|
| PR create / finish / merge workflows | Packs PR/workflow stub |
| Copilot PR-skills packaging | Theme 8 G10 defer |
| Git / worktree / commit ceremony as SoT | Theme 8 G10 / Theme 6–7 non-imports |
| Bugbot / `review-bugbot` as Debug method | Review ≠ debug method [E0 pass1]; Phase 2 adjacency |
| CI babysit / merge-queue automation | Theme 8 G10; `ci-fix` / `loop-on-ci` community adjacency |
| Fat Review / multi-skill Quality pack | Deferred option D |
| T9F bug-hunt-swarm / parallel investigate | Parked unless residual P0 |
| Foreign CLI deps as Toolbelt runtime | Park |
| Shipping NDJSON collectors / MCP debug servers | Explicit non-goal |

- `FACT` [E0] Brief: PR/CI/Bugbot Phase 2 — T9D lists only, no design lock now. [E0: campaign-brief §0]

### 4.10 Theme 8 elevation pattern (E0 inspiration summary)

| Pattern | Theme 8 (accepted) | Theme 9 candidate use |
|---------|--------------------|------------------------|
| Companions | `implementation-plan-verify` + `implementation-execute-verify` | If B: spine + `reproduce-bug` (names TBD) |
| Hybrid orchestration | Plan/Execute own loop; companions hold gates | Execute owns task loop/N=2; Debug owns investigate/reproduce method when triggered |
| Skill-only | No always-on verify rule | No always-on debug rule (F9) |
| Elevate order | Accept → companions → wire orchestrators → packs | Accept+fence → skill(s) → wire Execute/Verify → packs |
| Explicit out | Debug/PR | PR/CI/Bugbot/swarm/collectors |

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | A and B remain the only live F1 choices; C/D stay deferred | open (lean confirmed in brief) | §4.2; brief F1 |
| H2 | Lean B best matches quality-over-thinness alone | open | Brief §0; pass3 B-stronger |
| H3 | Skill names can avoid product “Debug Mode” while staying discoverable | open | §4.3 candidates |
| H4 | Reproduce companion = never-fix + light dossier if B | open | F5 lean; pass3 |
| H5 | Instrumentation home = spine section (I1); T9E owns atoms | open | F6; coordinate T9E |
| H6 | Always-on debug rule stays rejected | open (strong lean reject) | F9; Theme 8 D3 |
| H7 | Execute verify-fail + Verify Critical/unclear are primary wires | open | F10; pass2 §3.6 |

---

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Thinness vs quality (A vs B) | Thinness favors A | Quality lean + pass3 favor B | Fence F1 after deep report — working lean B, A first-class; **no lock this note** |
| `implementation-*` namespace vs distinct debug slug | N3 ladder continuity | N1/N2 avoid verify confusion + softer Cursor collision | OPEN — F2 human pick |
| Instrumentation companion vs section | I2 isolation | I1 thinness + brief lean | Prefer I1; reopen only if T9E/W2 shows bloat |

---

## 7. Gaps & OPEN

- Final F1 A vs B — human fence after integrated report  
- Final skill slugs (F2) + description trigger phrases (post-name)  
- Dossier template path/size cap (F5) — author at elevate, not W1  
- T9E atom length vs I1 spine budget — coordinate in integrate  
- Live E0 trials of verify-fail→Debug handoff — W2 residual  
- Bounce/warn policy if agents ignore Debug after verify-fail — OPEN  
- T9F reopen criteria — only if W2 residual shows P0 ambiguity cost (brief F8)

**Residual → W2**

1. Corroborate name collision with Cursor skill picker / description UX (GAP in §4.3)  
2. After T9A/T9E land: confirm I1 spine length still thin enough (else I2 reopen)  
3. Draft concrete Handoffs diffs against chosen slugs (still no elevate)  
4. Optional: one dry-run scenario table (verify-fail → reproduce → fix → execute-verify) for integrator fence appendix  

---

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] Integrator should present F1 as **A vs B** with the pros/cons table in §4.2; working recommendation **B** per brief lean; C/D deferred with reasons.
- `INFERENCE` [E4] Naming shortlist for fence: spine **`systematic-debug`** or **`investigate-reproduce`** (+ optional `implementation-debug`); companion **`reproduce-bug`** if B.
- `INFERENCE` [E4] Wiring: replace Execute/Verify “Debug pack later” stubs with trigger prose in §4.7 after accept — preserve N=2 ownership on Execute.
- `INFERENCE` [E4] Elevation only post fence-gate; order skills→wires→packs; skill-only; Phase 2 list in §4.9 stays unlist-designed.

---

## 9. Source list (deduped)

1. `docs/research/notes/theme-9-debug/campaign-brief.md` — E0  
2. `docs/research/notes/theme-9-debug/t9-coordinator-pin.md` — E0  
3. `docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md` — E0 (draft scoping)  
4. `docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md` — E0 (draft scoping)  
5. `docs/research/notes/theme-9-debug/scope-normal-pass1.md` — E0 (boundary / G10 pointer)  
6. `docs/research/reports/theme-8-verify-gates.md` — E0 (accepted; elevation pattern inspiration)  
7. `docs/research/notes/theme-8-verify/t8d-w1-surface-elevation.md` — E0 (G10 list + elevation-order pattern)  
8. `docs/packs/README.md` — E0  
9. `skills/implementation-plan-verify/SKILL.md` — E0 (companion naming)  
10. `skills/implementation-execute-verify/SKILL.md` — E0 (companion naming + Handoffs)  
11. `skills/implementation-execute/SKILL.md` — E0 (verify-fail + Handoffs stub)  
12. `skills/implementation-execute-subagents/SKILL.md` — E0 (Debug later boundary)  
13. Glob `d:\Toolbelt\skills/*/SKILL.md` — E0 (name inventory)  
14. `rules/research-skill-coexistence.mdc` — E0 (only debug-adjacent rule hit)  
15. `docs/templates/research-note.md` — template  
