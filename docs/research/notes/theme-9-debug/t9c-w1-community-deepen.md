---
title: "T9C W1 — Community / vendor deepen (transferable vs park)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9c-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-coordinator-pin.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
  - docs/PROTOCOL.md
supersedes: null
---

# T9C W1 — Community / vendor deepen

**Using `research-protocol`.**

**Status:** `draft`. Not Debug SoT. E3 community sources inspire atoms only — **no design locks**, no elevation, no Superpowers dependency, no shipping collectors/MCP. Theme 8 = Verify gates (completion), **not** this Debug pocket.

## 1. Scope

- Question / goal: Deep-read community/vendor debug skills; produce **transferable atoms vs park** tables that feed Toolbelt-native Debug pocket fences (esp. F3–F8) without coupling or packaging.
- In scope: Superpowers systematic-debugging + three companions; silkyland reproduce-my-bug (+ flaky + dossier refs); rbouschery bug-investigate-fix; millionco debug-agent; stas00 art-of-debugging loop; Dimillian bug-hunt-swarm spot-check; local cursor-team-kit control-ui/cli + verify-this; optional Alexandria `software_engineering` corroboration (E2).
- Out of scope: Elevating skills; inventing Cursor private debug-server APIs; shipping NDJSON collectors; T9F design in W1; re-litigating Theme 8 iron law / N=2 / converge; PR/CI mega-pack.
- Comprehension / research goal type: reuse (extract method atoms).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | `gh api` (GitHub Contents API, base64 decode); local Read on cursor-team-kit plugin skills; Alexandria `rag_query` |
| Corpora / URLs searched | `obra/superpowers` systematic-debugging tree; `silkyland/reproduce-my-bug` SKILL + `references/*`; `rbouschery/agent-skills` bug-investigate-fix; `millionco/debug-agent` `.agents/skills/debug-agent/SKILL.md`; `stas00/the-art-of-debugging` SKILL.md; `Dimillian/Skills` bug-hunt-swarm; local `C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\cursor-team-kit\...\skills\{control-ui,control-cli,verify-this}\SKILL.md`; Alexandria corpus `software_engineering` |
| Queries (exact) | `gh api repos/<org>/<repo>/contents/<path>`; rag: `systematic debugging reproduce before fix root cause tracing hypothesis falsification flaky tests instrumentation evidence` (k=6, corpus=`software_engineering`) |
| What was *not* searched | Live E0 Toolbelt debug trials; JUNERDD full body (pass3 already parked packaging); Cursor private debug-server wire protocol; silkyland README deep product pitch beyond skill refs |
| Depth | deep |
| Waves / stop_reason | Wave 1 track T9C; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←fetched SKILL/ref bodies + local plugin skills + RAG chunks; Activity=T9C W1 deepen; Agent=t9c-w1-gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | Campaign brief Tier-A list + pass3 “not searched” flaky/dossier bodies were the W1 slice |
| Scope boundary | Community/vendor method text only; no Toolbelt surface edits |

---

## 4. Findings

### 4.0 Transferable vs park — master table

| Source | Transferable atoms (Toolbelt-native) | Park (do not ship / couple) | Grade |
|--------|--------------------------------------|-----------------------------|-------|
| **obra/superpowers** `systematic-debugging` | Iron: investigate before fix; reproduce consistently; recent-changes check; multi-component boundary logs; single hypothesis + one variable; **≥3 failed fixes → stop & question architecture**; red-flag rationalizations; verify after fix | Coupling to `test-driven-development` / `verification-before-completion` skills; Superpowers as dependency; “95% incomplete investigation” rhetoric as law | E3 [E1 body via gh] |
| **root-cause-tracing.md** | Backward trace: symptom → immediate cause → callers → original trigger; temp stack/`console.error` instrumentation when stuck; fix at source not symptom | Full narrative session examples as SoT; `find-polluter.sh` as Toolbelt asset | E3 |
| **defense-in-depth.md** | After invalid-data bugs: validate entry + business + environment (+ optional debug log); make class of bug hard to reintroduce | Mandatory four-layer every bug; over-engineering vs thin spirit | E3 |
| **condition-based-waiting.md** | Flaky tests: wait for **condition**, not arbitrary sleep; document when timing *is* the subject | Shipping `waitFor` helpers as Toolbelt code; example.ts packaging | E3 |
| **silkyland/reproduce-my-bug** | **Never-fix** prime directive; read-only app code (repro artifacts only); production = evidence only; one variable; green ≠ repro; intake → evidence sweep → path trace → repro plan gate → reproduce → minimize → flaky → dossier; `NOT-YET-REPRODUCED` / `UNVERIFIED` honesty | `seed-ah` companion dependency; `deep-plan` as required handoff; full skill ceremony as sole Debug surface | E3 |
| **silkyland** `flaky-bugs.md` | Measure rate (N runs) → identify nondeterminism class → force (seed/clock/order/race/network/cache/pollution) → deterministic / rate-based / not-yet; heisenbug: prefer passive capture | Domain-specific forcing recipes as encyclopedia | E3 |
| **silkyland** `dossier-template.md` | Compact `REPRO.md`: status line, exact command + failing output, load-bearing triggers, evidence timeline, append-only hypothesis ledger, attempt log from #0, handoff acceptance criterion | Fat dossier as mandatory every bug; quality-bar perfectionism blocking thin agents | E3 |
| **rbouschery** bug-investigate-fix | Same-surface repro (web/API/CLI/job); 1–4 falsifiable hypotheses table; confirm/reject/inconclusive; **same repro** after fix; blockers before fake plans; compact output shape | `thermo-nuclear-plan` coupling; `disable-model-invocation: true` slash-only packaging; end-to-end fix-in-one-skill as only shape | E3 |
| **millionco/debug-agent** | 3–5 hypotheses; instrument before fix; `hypothesisId` + CONFIRMED/REJECTED/INCONCLUSIVE with cited log lines; keep instrumentation through verify; `#region debug log` cleanup; revert rejected speculative code; min logs (≈2–6, ≤10) | **`npx debug-agent` collector/server**; HTTP ingest API; branding “DEBUG MODE”; “100% confidence” rhetoric; JS fetch-to-collector as required path | E3 |
| **stas00/the-art-of-debugging** | Loop: reproduce reliably → **shrink** → localize → usable signal → change one thing; pin flaky nondeterminism first; atomic debug cycles; “die” / right-file check; bisect | Unix/Python/PyTorch/CUDA recipe encyclopedia as Debug SoT; SLURM/HPC domain; sleep-to-attach recipes as default (conflicts condition-wait / no-sleep-as-fix) | E3 |
| **Dimillian** bug-hunt-swarm | Bug packet; bound brief; **read-only** parallel investigate; ranked hypotheses + smallest proof step; diagnosis-first no edits | Mandatory 4-agent ceremony; default spine; role taxonomy as Toolbelt law | E3 |
| **cursor-team-kit** control-ui / control-cli | Local harness for UI/CLI **repro + evidence** (screenshots, transcripts, console/network, deterministic waits); cleanup sessions | Shipping harnesses inside Toolbelt; hard-coded ports/selectors from other repos | E0 local plugin text |
| **cursor-team-kit** verify-this | Falsifiable claim; baseline vs treatment; VERIFIED / NOT VERIFIED / INCONCLUSIVE — **compose after Debug fix**, not Debug spine | Treating verify-this as Debug investigate skill (Theme 8 adjacent) | E0 |
| **Alexandria** Dooley / Osmani | Reproduce reliably → locate → fix one → retest; don’t guess; don’t symptom-patch; shrink/binary-search repro; sporadic causes list | Textbook chapters as elevation drivers | E2 |

### 4.1 Superpowers systematic-debugging + companions

- `FACT` [E3] Core iron law: no fixes without root-cause investigation first; four phases (investigate → pattern → hypothesis/test → implement+verify). [E3: `obra/superpowers` `skills/systematic-debugging/SKILL.md` via `gh api` 2026-07-30]
- `FACT` [E3] Phase 4: if fix fails and attempts **≥ 3**, STOP and question architecture with human partner before Fix #4. [E3: same SKILL.md §Phase 4.4–4.5]
- `FACT` [E3] Root-cause-tracing: observe symptom → immediate cause → callers → original trigger; temporary stack instrumentation via `console.error` + `Error().stack` when manual trace stalls. [E3: `root-cause-tracing.md`]
- `FACT` [E3] Defense-in-depth: after invalid-data bugs, validate at entry, business logic, environment guards, plus optional debug instrumentation. [E3: `defense-in-depth.md`]
- `FACT` [E3] Condition-based waiting: replace arbitrary `sleep`/`setTimeout` waits with polling a condition; document when timing is the subject under test. [E3: `condition-based-waiting.md`]
- `FACT` [E3] Directory also contains `find-polluter.sh`, wait example `.ts`, and test-pressure docs (listed via Contents API). [E3: `gh api` listing 2026-07-30]
- `INFERENCE` [E4] Transfer phases + N-fix stop + companions as **method atoms under T9A**; park Superpowers skill-name coupling and scripts. Premises: brief essence filter; standalone Toolbelt.

### 4.2 silkyland reproduce-my-bug (+ flaky + dossier)

- `FACT` [E3] Prime directive: no fix without failing reproduction; skill **never patches**; claims need `file:line` / log / command output or `UNVERIFIED`. [E3: silkyland `SKILL.md`]
- `FACT` [E3] Seven-step spine includes Repro Plan Gate, minimize-until-load-bearing, flaky path, and dossier handoff; failure modes include `NOT-YET-REPRODUCED`. [E3: silkyland `SKILL.md`]
- `FACT` [E3] Flaky protocol: measure rate → classify nondeterminism (concurrency, clock, ordering, randomness, network, cache, test pollution) → force → deliver deterministic, rate-based, or not-yet. [E3: `references/flaky-bugs.md`]
- `FACT` [E3] Dossier template mandates status (DETERMINISTIC / RATE-BASED / NOT-YET), exact command + verbatim failing output, append-only hypothesis ledger, attempt log starting at #0 (runnability spike), handoff that failing test is acceptance criterion. [E3: `references/dossier-template.md`]
- `INFERENCE` [E4] Strongest community evidence for fence **F5** (never-fix ± light dossier) and **F4** (flaky checklist thickness). Premises: F1 working lean B; thin spirit → light checklist not third skill.

### 4.3 rbouschery bug-investigate-fix

- `FACT` [E3] End-to-end: reproduce on same surface → 1–4 falsifiable hypotheses → test → short fix plan → implement → verify **same** repro gone. [E3: `bug-investigate-fix/SKILL.md`]
- `FACT` [E3] Explicitly couples step 4 to `thermo-nuclear-plan` when available; documents code-judo fallback; frontmatter `disable-model-invocation: true`. [E3: same]
- `FACT` [E3] If all hypotheses rejected: one small new loop only — do not spiral. [E3: same §3]
- `INFERENCE` [E4] Transfer same-surface repro + hypothesis table + same-repro verify; park thermo-nuclear + slash-only packaging. Premises: Theme 8 owns plan-verify; Toolbelt standalone.

### 4.4 millionco debug-agent (protocol atoms)

- `FACT` [E3] Workflow: 3–5 hypotheses → instrument → reproduce → classify each hypothesis CONFIRMED/REJECTED/INCONCLUSIVE with cited log lines → fix only with log proof → keep instrumentation for post-fix verify → cleanup `#region debug log` blocks; revert code from rejected hypotheses. [E3: millionco `SKILL.md`]
- `FACT` [E3] Log payload fields include `sessionId`, `runId`, `hypothesisId`, `location`, `message`, `data`, `timestamp`; NDJSON file and/or HTTP ingest via `npx debug-agent`. [E3: same]
- `CLAIM` [E3] Community packaging converges on Cursor-like instrument→repro→classify outside native Debug Mode. Stars≠SoT; park collector. Premises: pass3 cluster; brief non-goals.
- `INFERENCE` [E4] Protocol atoms feed **T9E / F6**; packaging is park. Premises: brief “inspire, don’t ship collector”; no private Cursor API invention.

### 4.5 stas00 the-art-of-debugging

- `FACT` [E3] Debugging loop: reproduce reliably → shrink payload → localize → get usable signal → change one thing and verify; flaky → pin nondeterminism first. [E3: stas00 `SKILL.md` §The debugging loop]
- `FACT` [E3] Bulk of SKILL is domain cheatsheets (Unix/strace, gdb/core, Python/py-spy, PyTorch/CUDA/multi-node). [E3: same]
- `INFERENCE` [E4] Transfer loop + shrink + localize; park encyclopedia. Premises: thin Toolbelt Debug pocket.

### 4.6 Spot-check — Dimillian swarm + cursor-team-kit

- `FACT` [E3] bug-hunt-swarm: build bug packet → bound investigation → up to **four read-only** parallel investigators (repro/scope, code path, recent change, proof/observability) → synthesize ranked hypotheses → diagnosis path; **no edits, no instrumentation, no fixes**. [E3: Dimillian `bug-hunt-swarm/SKILL.md`]
- `FACT` [E0] control-ui: local browser/CDP harness for UI repro, screenshots, console/network, before/after for verify-this; prefer deterministic interaction loop. [E0: local cursor-team-kit `control-ui/SKILL.md`]
- `FACT` [E0] control-cli: PTY/tmux harness; “Prefer deterministic waits over sleeps.” [E0: local `control-cli/SKILL.md`]
- `FACT` [E0] verify-this: falsifiable claim → baseline/treatment → VERIFIED | NOT VERIFIED | INCONCLUSIVE — verification pocket, not investigate spine. [E0: local `verify-this/SKILL.md`]
- `INFERENCE` [E4] Swarm = **F8 park evidence** (optional escalation for large/ambiguous only). control-* = compose harness atoms for T9B/T9E; verify-this = post-fix compose, Theme 8 adjacency — do not conflate with Debug. Premises: brief T9F out of W1; Theme 8 identity.

### 4.7 Alexandria corroboration (E2)

- `CLAIM` [E2] Dooley ch.17: reproduce reliably → find source → fix that one → test fix; sporadic causes include init, timing, dangling pointer, buffer, concurrency; shrink via binary search on data/code; don’t guess; don’t fix symptom. [E2: Alexandria corpus=`software_engineering` chunk_id=`08490da27bbde1f95a445ac6` source_rel_path=`…Dooley…pdf` query=`systematic debugging reproduce before fix…`; also chunk_id=`f2370255822d37ae59c3860e`, `9e26a07559361b30390a1ffc`]
- `CLAIM` [E2] Osmani: reproduce with failing inputs → locate via prints/debugger → six-step debug; verify AI code with tests. [E2: Alexandria chunk_id=`e5e3e919796f7e24f055faf9` source=`Beyond Vibe Coding…Osmani`]
- `INFERENCE` [E4] E2 textbooks corroborate reproduce→locate→fix-one→retest; no conflict with community method atoms; still not elevation law alone.

---

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Never-fix companion + light dossier is a distinct gravity well vs fix-included spine | confirmed (as community signal, not lock) | silkyland never-fix + dossier vs Superpowers/rbouschery/millionco fix-included |
| H2 | N≈3 failed-fix stop is the strongest community echo for F3 | confirmed (E3 echo) | Superpowers ≥3 → architecture; rbouschery anti-spiral softer |
| H3 | debug-agent packaging must stay parked while atoms feed T9E | confirmed | millionco mandates `npx debug-agent`; brief forbids collectors |
| H4 | Swarm stays parked for default Debug | confirmed | Dimillian ceremony cost; brief F8/T9F out |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Never-fix vs fix-in-skill | silkyland: never patches; dossier is deliverable | Superpowers / rbouschery / millionco: include fix + verify in same workflow | Log both. Fence **F1/F5**: never-fix as companion (B lean) vs atoms inside spine (A). E3 alone ≠ lock. |
| N-fix stop | Superpowers: ≥3 → architecture discussion | rbouschery: one small hypothesis re-loop, no numeric architecture stop; millionco: “iteration expected” | Log both for **F3** pros/cons (N=2 vs N=3 vs soft). Prefer not locking from E3 alone. |
| Instrument-first vs reproduce-first | millionco: instrument before/during repro as mandatory | silkyland/Superpowers: reproduce/evidence first; instrument when stuck / multi-component | Feed **F6/T9E**: prefer Cursor Debug Mode or Agent instrument when evidence insufficient — not always-on collector. |
| Defense-in-depth strength | Superpowers companion: multi-layer after invalid-data, “don’t stop at one” | Toolbelt thin spirit / brief F7 optional | **F7**: optional recommended note after invalid-data fixes, not mandatory every bug. |
| Swarm vs instrument | Dimillian: read-only, no instrumentation | millionco: must instrument | **F8**: park swarm as default; if ever used, diagnosis-only precedes instrument/fix skills. |
| Sleep | stas: inject sleep to attach debugger | Superpowers condition-wait; millionco forbids sleep-as-fix; control-cli prefers deterministic waits | Transfer: no sleep-as-fix; sleep-to-attach is niche park. |
| Verify pocket identity | verify-this / Theme 8 completion gates | Debug investigate/reproduce | Do **not** conflate — compose verify after Debug, don’t merge SoT. |

## 7. Gaps & OPEN

- `GAP` Exact Cursor extension debug-server wire protocol — not searched; **do not invent** (T9B/T9E).
- `GAP` JUNERDD / XcodeBazelMCP bodies not re-fetched this wave (pass3 park packaging stands).
- `OPEN` How thin a dossier is “light” enough for F5 without losing acceptance-criterion value → residual for W2 if integrator needs word-count options.
- `OPEN` Whether N=2 (Theme 7 verify-retry echo) vs N=3 (Superpowers) should share vocabulary across Execute vs Debug — fence F3 + F10 wording, not T9C lock.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Toolbelt Debug should extract a **portable atom set** (reproduce, falsify, backward-trace, same-repro verify, flaky force-or-rate, optional defense note, instrument-classify-cleanup) and cut all packaging/couplings listed in park column. Premises: §4.0 table; brief non-goals.
- `INFERENCE` [E4] Fence evidence package below is sufficient for draft-report pros/cons; elevation remains blocked until human fence adjudication. Premises: campaign brief §0b; `draft-is-not-sot`.

### 8.1 Fence-feeding bullets (F3–F8)

| Fence | Evidence atoms from this note |
|-------|-------------------------------|
| **F3** N-fix stop | Superpowers: ≥3 failed fixes → question architecture [E3]. rbouschery: one small re-loop, no N [E3]. millionco: expect iteration [E3]. Community echo ~3, not unanimous. |
| **F4** Flaky thickness | silkyland flaky-bugs measure→force→rate [E3]; Superpowers condition-based waiting [E3]; stas pin nondeterminism first [E3]. Supports light checklist-in-method, not third skill. |
| **F5** Reproduce companion / dossier | silkyland never-fix + dossier-template quality bar [E3]; REPRO.md fields (command, failing output, attempt #0, append-only ledger). Pros: cold handoff. Cons: agent load if full template always. |
| **F6** Instrumentation home | millionco: hypothesisId, CONFIRMED/REJECTED/INCONCLUSIVE, region cleanup, keep logs through verify [E3]; Superpowers multi-boundary logs + temp stack [E3]. Park collectors. Prefer spine section / T9E atoms + Cursor Debug Mode compose. |
| **F7** Defense-in-depth | Superpowers four layers after invalid-data [E3]. Conflict with thinness → optional post-fix note (brief lean). |
| **F8** Swarm park | Dimillian: 4 read-only agents, diagnosis-first, no instrument/fix [E3]. Cost/ceremony vs thin default → **park** unless W2 residual shows P0 ambiguity cost. T9F out of W1 design. |

### 8.2 Residual → W2 (P0/P1 only)

| ID | Priority | Residual |
|----|----------|----------|
| R1 | P1 | Adjudicate F3 with Theme 7 N=2 language: shared vocabulary vs separate Debug N=3 (no new fetches needed — integrator wording). |
| R2 | P1 | F5 “light dossier” field minimum: which dossier-template sections are load-bearing vs optional for thin companion (integrator + human fence). |
| — | — | No P0 ambiguity found that forces T9F reopen or collector packaging. |

## 9. Source list (deduped)

1. [E3] `obra/superpowers` `skills/systematic-debugging/SKILL.md` — `gh api` 2026-07-30  
2. [E3] `obra/superpowers` `skills/systematic-debugging/root-cause-tracing.md` — `gh api` 2026-07-30  
3. [E3] `obra/superpowers` `skills/systematic-debugging/defense-in-depth.md` — `gh api` 2026-07-30  
4. [E3] `obra/superpowers` `skills/systematic-debugging/condition-based-waiting.md` — `gh api` 2026-07-30  
5. [E3] `silkyland/reproduce-my-bug` `SKILL.md` — `gh api` 2026-07-30  
6. [E3] `silkyland/reproduce-my-bug` `references/flaky-bugs.md` — `gh api` 2026-07-30  
7. [E3] `silkyland/reproduce-my-bug` `references/dossier-template.md` — `gh api` 2026-07-30  
8. [E3] `rbouschery/agent-skills` `bug-investigate-fix/SKILL.md` — `gh api` 2026-07-30  
9. [E3] `millionco/debug-agent` `.agents/skills/debug-agent/SKILL.md` — `gh api` 2026-07-30  
10. [E3] `stas00/the-art-of-debugging` `SKILL.md` — `gh api` 2026-07-30  
11. [E3] `Dimillian/Skills` `bug-hunt-swarm/SKILL.md` — `gh api` 2026-07-30  
12. [E0] cursor-team-kit local `control-ui/SKILL.md`, `control-cli/SKILL.md`, `verify-this/SKILL.md` — 2026-07-30  
13. [E2] Alexandria `software_engineering` chunks `08490da27bbde1f95a445ac6`, `f2370255822d37ae59c3860e`, `9e26a07559361b30390a1ffc`, `e5e3e919796f7e24f055faf9` — rag_query 2026-07-30  
14. [E0 draft] `docs/research/notes/theme-9-debug/campaign-brief.md`, `t9-coordinator-pin.md`, `scope-normal-pass3-deepen.md` — campaign inputs (not design law)
