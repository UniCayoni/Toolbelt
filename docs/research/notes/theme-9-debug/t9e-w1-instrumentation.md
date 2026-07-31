---
title: "T9E W1 — Instrumentation & evidence capture"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9e-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-coordinator-pin.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
  - docs/PROTOCOL.md
supersedes: null
---

# T9E W1 — Instrumentation & evidence capture

**Using `research-protocol`.**

**Status:** `draft` gatherer note. Not Debug SoT. Not elevation authority.  
**Track:** Instrumentation & evidence capture (campaign brief §3 T9E).  
**Hard bounds:** Compose Cursor Debug Mode; teach protocol atoms; **do not** invent Cursor private debug-server wire protocols; **do not** propose shipping collectors/MCP as Toolbelt deliverables; T9F out of W1.

## 1. Scope

- Question / goal: When to prefer Cursor Debug Mode vs Agent-mode instrumentation; which **protocol atoms** (`hypothesisId`, CONFIRMED/REJECTED/INCONCLUSIVE, cleanup markers, NDJSON-shaped payloads) Toolbelt may teach **without** shipping a collector or inventing Cursor private wire protocols; terminal/browser as first-class evidence; cleanup before claiming “fixed”.
- In scope: Decision tree; Agent-mode instrumentation atoms (inspire millionco/debug-agent + JUNERDD corroboration); explicit GAP on private protocol; cleanup/leave-no-trace; hypothesis classification vocabulary candidates; evidence citation expectations; fence **F6** pros/cons material; residuals → W2.
- Out of scope: T9A method spine formalization; T9B full native compose lock; T9C transferable/park tables beyond atom extraction; T9D surface naming; T9F swarm; shipping `npx` collectors / MCP servers / Toolbelt-owned ingest endpoints; reverse-engineering Cursor extension debug-server.
- Comprehension / research goal type: adaptive (compose product tools + extract method atoms).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign-brief, t9-coordinator-pin, pass3 deepen, research-note template); WebFetch (Cursor Debug Mode docs, blog, Browser docs, Terminal docs, CLI slash-commands); `gh api` (millionco/debug-agent SKILL.md + README; JUNERDD/skills `skills/debug/SKILL.md`); WebSearch (corroboration pointers only) |
| Corpora / URLs searched | `https://cursor.com/docs/agent/debug-mode`; `https://cursor.com/blog/debug-mode`; `https://cursor.com/docs/agent/tools/browser.md`; `https://cursor.com/docs/agent/tools/terminal`; `https://cursor.com/docs/cli/reference/slash-commands`; `https://cursor.com/docs/cli/overview`; github.com/millionco/debug-agent; github.com/JUNERDD/skills |
| Queries (exact) | Cursor Debug Mode instrumentation hypothesize instrument human reproduces cleanup 2026; site:github.com JUNERDD skills debug NDJSON hypothesisId; site:cursor.com/docs CLI /debug slash command Debug Mode; site:cursor.com/docs agent terminal full output command |
| What was *not* searched | Live E0 Toolbelt debug trials; Cursor extension source / private ingest schemas; VS Code DAP deep-read; silkyland flaky refs; reverse-engineering debug-server HTTP; packaging/MCP design for Toolbelt |
| Depth | deep |
| Waves / stop_reason | Wave 1 slice; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←Cursor primary docs + community skill bodies; Activity=T9E W1 gather; Agent=t9e-w1-gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Track is product-compose + community atom extract; local Toolbelt code does not implement Debug Mode |
| Scope boundary | Theme-9 notes + external primary/community docs; no Toolbelt surface elevation |

## 4. Findings

### 4.1 Cursor Debug Mode (compose, don’t reimplement)

- `FACT` [E1] Debug Mode is for bugs that are hard to reproduce or understand; agent hypothesizes, instruments, uses runtime info before a targeted fix — not immediate speculative coding. [E1: Debug Mode — https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Official loop: (1) explore & hypothesize → (2) add instrumentation to a **local debug server in a Cursor extension** → (3) **human reproduces** with provided steps → (4) analyze logs → (5) targeted fix → (6) verify & **remove instrumentation**. [E1: same]
- `FACT` [E1] Best-fit cases listed: reproduce-but-unclear cause; race/timing; performance/memory; regressions. Prefer when “standard Agent interactions struggle.” [E1: same]
- `FACT` [E1] Blog: human marks fixed → agent removes instrumentation for a clean minimal shippable change; if not fixed, more logging + reproduce again. HITL verification is “critical.” [E1: Introducing Debug Mode — https://cursor.com/blog/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Editor switching: mode picker dropdown; Shift+Tab. [E1: Debug Mode docs]
- `FACT` [E1] CLI: `/debug [prompt]` toggles Debug mode / submits in Debug mode; `/logs` shows debug log path and copies to clipboard. [E1: Slash commands — https://cursor.com/docs/cli/reference/slash-commands — accessed 2026-07-30]
- `GAP` Exact Cursor extension debug-server wire protocol (HTTP paths, payload schema, auth, file layout beyond “local debug server” / `/logs` path pointer) — **not published as a public API to implement against**. Searched: official Debug Mode docs + blog + CLI slash-commands. Result: composition via mode switch / `/debug` / `/logs` only; **do not invent**. [E1 absence + campaign non-goal]

### 4.2 Terminal & browser as first-class evidence (Agent mode)

- `FACT` [E1] Browser: console + network for debug; browser logs **written to files** agents can grep/selectively read; screenshots via file-read images; dev-server port awareness. [E1: Browser — https://cursor.com/docs/agent/tools/browser.md — accessed 2026-07-30]
- `FACT` [E1] Terminal: Agent runs shell commands in the user’s terminal; Run Mode / sandbox govern approvals and network; heavy shell themes can truncate/misformat inline output (`CURSOR_AGENT` tip). [E1: Terminal — https://cursor.com/docs/agent/tools/terminal — accessed 2026-07-30]
- `INFERENCE` [E4] For Agent-mode debugging, **command stdout/stderr** (tests, repro scripts, CLI) and **browser console/network file logs** are first-class evidence channels that do not require Cursor Debug Mode’s private collector. Premises: (1) Browser file-log FACT; (2) Terminal executes repro commands FACT; (3) Debug Mode is a *separate* instrumentation path FACT.
- `OPEN` Official docs page for Terminal does not spell an explicit “always capture full output / never summarize away” evidence rule; Toolbelt may still teach that as method (T9A/E) without claiming it is Cursor product law. Follow-up: W2 skim any Agent overview tips if present.

### 4.3 Community Agent-mode instrumentation atoms (inspire; park packaging)

#### millionco/debug-agent

- `FACT` [E1] Workflow: 3–5 hypotheses → instrument → reproduce (test / ad hoc script / user steps) → classify each hypothesis CONFIRMED/REJECTED/INCONCLUSIVE with **cited log lines** → fix only with log proof → keep instrumentation through post-fix verify → cleanup `#region debug log` / `#endregion` via search-and-delete; re-grep zero markers; `git diff` review. [E1: millionco/debug-agent `.agents/skills/debug-agent/SKILL.md` via `gh api` 2026-07-30]
- `FACT` [E1] NDJSON-shaped payload fields taught: `sessionId`, `runId`, `hypothesisId`, `location`, `message`, `data`, `timestamp` (+ example also shows `id`). JS/TS often POST to a local ingest; other languages may append NDJSON to a log path. [E1: same]
- `FACT` [E1] Cleanup markers mandatory around each debug log; secrets/PII forbidden in logs; clear log file between runs without removing instrumentation; do not remove instrumentation before post-fix proof / user confirm. [E1: same]
- `FACT` [E1] README ships packaging via `npx debug-agent@latest init` and a long-running collector — **community product**, not Toolbelt. [E1: millionco/debug-agent README via `gh api` 2026-07-30]
- `INFERENCE` [E4] Toolbelt may teach the **protocol atoms** (hypothesis IDs, classification vocab, region markers, NDJSON-*shaped* fields, cite-log-lines, cleanup-before-done) while **parking** `npx` collector / ingest server as a Toolbelt deliverable. Premises: campaign non-goals; coordinator pin hard constraint 4; atom extract from SKILL.

#### JUNERDD/skills `debug` (optional corroboration)

- `FACT` [E1] JUNERDD `debug` skill: evidence-first runtime loop; mark hypotheses `CONFIRMED` / `REJECTED` / `INCONCLUSIVE` / `NOT_REACHED`; fix only after root cause proven; verify with fresh post-fix logs before removing instrumentation; never leave temporary probes/debug logging after successful cleanup; never log secrets. Bundles a local NDJSON collector/scripts — packaging park for Toolbelt. [E1: JUNERDD/skills `skills/debug/SKILL.md` via `gh api` 2026-07-30]
- `CLAIM` [E3] Repo README synthesizes the same prove-it loop + optional collector (community packaging). Stars/README ≠ Toolbelt SoT. [E3: JUNERDD/skills README via WebSearch/gh listing 2026-07-30]
- `INFERENCE` [E4] Corroborates classification vocabulary + cleanup-after-verify; adds optional `NOT_REACHED` candidate; **does not** justify Toolbelt shipping a collector. Premises: JUNERDD FACT; campaign park packaging.

### 4.4 Decision tree — Debug Mode vs Agent+terminal/browser vs static-only

Working tree for Toolbelt **compose guidance** (method teaching; not product replacement):

```text
Is the failure explainable from static read + existing failing test/logs alone?
├─ YES → Static-only / light Agent: cite existing evidence; minimal or no new instrumentation.
│        Prefer reproduce via terminal (failing test/command) before editing.
└─ NO → Need runtime discrimination of competing hypotheses?
         ├─ Cursor Debug Mode available AND bug fits product best-cases
         │  (unclear-but-reproducible, races/timing, perf/memory, regressions)
         │  AND human can drive repro → PREFER Debug Mode
         │     (mode picker / Shift+Tab / CLI `/debug`; use `/logs` for log path)
         ├─ Debug Mode unavailable / wrong surface / agent must drive CLI-heavy
         │  or browser-file evidence already sufficient → Agent-mode instrumentation
         │     + terminal and/or browser evidence (protocol atoms below; NO private wire invent)
         └─ Still no runtime path → document NOT-YET-REPRODUCED / blocker (T9A/reproduce);
            do not claim root cause from code-read alone.
```

- `INFERENCE` [E4] Prefer **Debug Mode** when the product loop (extension collector + human repro + auto cleanup) is available and the bug class matches docs; prefer **Agent+terminal/browser** when the agent can already obtain discriminating evidence via commands/browser file logs, or Debug Mode is unavailable; prefer **static-only** when a failing repro already exists and hypotheses are already falsified by that evidence. Premises: Debug Mode when-to-use FACT; Browser/Terminal FACTs; debug-agent Agent-fallback FACT.
- `FACT` [E0] Campaign brief working lean for fence F6: “Section of spine (+ T9E atoms)” — not a lock. [E0: `docs/research/notes/theme-9-debug/campaign-brief.md`]

### 4.5 Protocol atoms Toolbelt may teach (no collector)

Transferable **atoms** (inspire debug-agent / JUNERDD; cut packaging):

| Atom | Candidate teaching | Park |
|------|-------------------|------|
| Multi-hypothesis before fix | 3–5 falsifiable hypotheses | Exact count as law |
| `hypothesisId` on each probe | Stable IDs (H1/A/…) mapped to hypotheses | Cursor private IDs |
| Classification vocab | CONFIRMED / REJECTED / INCONCLUSIVE (+ optional NOT_REACHED) | JUNERDD-only ledger ceremony |
| NDJSON-*shaped* payload fields | `hypothesisId`, `location`, `message`, `data`, `timestamp`; optional `sessionId`/`runId` when using a file sink | Shipping ingest server; inventing Cursor wire |
| Cleanup markers | Language-appropriate `#region debug log` … `#endregion` (or equivalent) | Mandatory brand string |
| Evidence citation | Quote/cite log lines or command/browser locators before CONFIRMED | Vague “logs show…” |
| Keep probes through verify | Remove only after post-fix proof + confirm | Leaving debug forever |
| Secrets redaction | Never log tokens/PII | — |
| Clear between runs | Fresh evidence file/runId; don’t mix runs | Deleting unrelated logs |
| Revert rejected speculative fixes | Keep instrumentation; drop unproven code changes | — |

- `INFERENCE` [E4] These atoms are enough for an Agent-mode instrumentation protocol **section** without Toolbelt owning transport. Premises: atom table FACTs; campaign non-goals.

### 4.6 Cleanup / leave-no-trace (before “fixed”)

- `FACT` [E1] Cursor Debug Mode: verify then agent removes all instrumentation after confirmed fix. [E1: Debug Mode docs + blog]
- `FACT` [E1] debug-agent: grep `#region debug log`, delete regions, re-grep zero, `git diff` confirms only intentional fix remains. [E1: millionco SKILL Cleanup]
- `FACT` [E1] JUNERDD: after verification succeeds, remove every temporary probe/debug logging/breakpoint/helper/transport hook; never leave temporary instrumentation after successful cleanup. [E1: JUNERDD SKILL]
- `INFERENCE` [E4] Toolbelt should treat **cleanup as part of Done** for instrumentation-using debug — same spirit as Theme 8 verify culture, but specific to temporary probes — without re-litigating Theme 8 iron law. Premises: cleanup FACTs; coordinator pin “don’t re-litigate Theme 8”.

### 4.7 Hypothesis classification vocabulary candidates

| Candidate | Source | Notes |
|-----------|--------|-------|
| CONFIRMED | debug-agent, JUNERDD | Log-cited support |
| REJECTED | debug-agent, JUNERDD | Log-cited falsification |
| INCONCLUSIVE | debug-agent, JUNERDD | Ran but did not discriminate |
| NOT_REACHED | JUNERDD | Probe/path never hit — useful for incomplete repro |
| open / revised | Toolbelt research hypothesis-log idiom | Process status, not runtime disposition |

- `INFERENCE` [E4] Prefer CONFIRMED/REJECTED/INCONCLUSIVE as the thin default trio; consider NOT_REACHED as optional fourth for incomplete instrumentation paths. Premises: community FACTs; thin Toolbelt spirit from brief.

### 4.8 Evidence citation expectations

Minimum expectations for claiming a hypothesis disposition or “fixed” under instrumentation:

1. **Repro recipe** — command, test name, curl, or numbered human steps (and surface: terminal vs browser).
2. **Runtime artifact locator** — log line(s) / NDJSON record(s) / browser log file path+grep / terminal exit+stdout excerpt; or Debug Mode via product `/logs` path (compose, don’t parse private schema).
3. **Disposition link** — each CONFIRMED/REJECTED/INCONCLUSIVE names `hypothesisId` + cited evidence.
4. **Post-fix** — same repro; before/after evidence; then cleanup proof (no stray regions / Debug Mode cleanup done).

- `INFERENCE` [E4] Aligns cite-or-omit culture with runtime debugging: no citation → no CONFIRMED/“fixed”. Premises: PROTOCOL cite-or-omit; debug-agent “cited log line evidence” FACT.

### 4.9 Fence F6 — Instrumentation home (pros/cons material)

Working lean (not lock): **section of spine (+ T9E atoms)**. [E0: campaign-brief]

| Option | Pros | Cons |
|--------|------|------|
| **A. Section of spine** | One discoverable place with decision tree + atoms + cleanup; matches thin ladder; avoids “Debug Mode” name collision in a second skill; F6 lean | Spine length grows; risk of burying reproduce-never-fix (F5) if not careful |
| **B. Short companion skill** | Clear Agent-mode instrumentation playbook; easy to invoke when Debug Mode unavailable | Extra surface; discoverability cost; may duplicate T9A loop; packaging temptation |
| **C. Compose Debug Mode only** | Zero Toolbelt instrumentation text; trusts product cleanup/HITL | Leaves Agent-mode fallback untaught; fails when Debug Mode unavailable; community atoms unused; weak vs “evidence not assumptions” quality lean |

- `INFERENCE` [E4] Deep evidence so far favors **A (section)** or thin **B** over **C**; **A** best matches F6 working lean and “no collector packaging.” Final pick = human fence adjudication after integrated report. Premises: F6 table; Debug Mode GAP on private wire; Agent fallback need.

### 4.10 Pass-3 NDJSON cluster (local input, not re-fetch)

- `FACT` [E0] Pass-3 already framed millionco/debug-agent + JUNERDD as **atom source / park packaging**, and named GAP on Cursor private wire. [E0: `scope-normal-pass3-deepen.md` §7]
- `FACT` [E0] This W1 note deepens that cluster with primary SKILL bodies + Cursor compose docs; does not change park packaging stance.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Toolbelt can teach Agent-mode instrumentation without shipping a collector | confirmed | debug-agent/JUNERDD atoms separable from packaging; campaign non-goals |
| H2 | Cursor public docs suffice to reimplement the extension debug-server | rejected | Docs describe existence + compose entrypoints only; wire protocol GAP |
| H3 | Fence F6 should be “compose Debug Mode only” | rejected (as default) | Leaves Agent fallback + citation atoms untaught; conflicts quality lean |
| H4 | Terminal + browser file logs are enough for many Agent-mode cases without NDJSON | open | Browser FACT strong; Terminal “full output” method OPEN; needs W2/E0 trials |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| How instrumentation is transported | Cursor: local debug server in extension [E1] | Community: NDJSON file ± HTTP ingest skill packaging [E1/E3] | Prefer compose Cursor when available; teach **shape/discipline** atoms for Agent fallback; do not unify on invented Cursor wire |
| Classification vocab size | debug-agent trio [E1] | JUNERDD + NOT_REACHED [E1] | Default trio; NOT_REACHED optional |
| CLI mode table vs `/debug` | CLI overview table lists Agent/Plan/Ask [E1] | Slash-commands lists `/debug` + `/logs` [E1] | No conflict for compose: `/debug` exists; overview table incomplete for Debug — cite slash-commands for Debug entry |

## 7. Gaps & OPEN

- `GAP` Cursor extension debug-server private protocol (endpoints, schema, auth) — do not invent; compose via Debug Mode / `/debug` / `/logs`.
- `GAP` Whether Toolbelt should name a preferred Agent-mode sink (append-only file vs stdout tags vs browser console) when no collector — residual for W2 / fence text.
- `OPEN` E0 trials: same bug via Debug Mode vs Agent+terminal instrumentation — latency, cleanup reliability, citation quality.
- `OPEN` Terminal “never truncate evidence” as product vs method teaching.
- `OPEN` Exact spine wording for decision tree (T9A/T9D integrate).
- T9F parallel investigate: **out** of W1 (coordinator pin).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T9E deliverable for elevation (post-fence) is **method text**: decision tree + protocol atoms + cleanup + citation expectations — not a Toolbelt collector. Premises: H1 confirmed; packaging park; F6 lean A.
- `INFERENCE` [E4] Integrated report should carry F6 pros/cons table above for human adjudication before `/author-cursor-surfaces`. Premises: campaign fence process.
- `INFERENCE` [E4] Naming of any spine/companion must avoid colliding with product “Debug Mode” (fence F2; out of T9E lock). Premises: brief F2.

## 9. Residual → W2

1. Corroborate `/logs` artifact shape enough for citation guidance without reverse-engineering (observe-only if E0 allowed).
2. Pick thin default Agent-mode sink recommendation (file NDJSON-shaped vs tagged stdout) — still no Toolbelt collector.
3. Align T9E decision tree wording with T9A spine + T9B compose rules (no duplicate contradictory triggers).
4. Adjudication-ready F6 one-pager in draft report (pros/cons already drafted here).
5. Optional: silkyland flaky + instrumentation interaction (rate vs force) if T9A leaves OPEN.
6. Do **not** reopen T9F unless residual shows P0 ambiguity cost (brief F8).

## 10. Source list (deduped)

1. Cursor Debug Mode docs — https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30
2. Cursor blog: Introducing Debug Mode — https://cursor.com/blog/debug-mode — accessed 2026-07-30
3. Cursor Browser docs — https://cursor.com/docs/agent/tools/browser.md — accessed 2026-07-30
4. Cursor Terminal docs — https://cursor.com/docs/agent/tools/terminal — accessed 2026-07-30
5. Cursor CLI slash commands — https://cursor.com/docs/cli/reference/slash-commands — accessed 2026-07-30
6. Cursor CLI overview — https://cursor.com/docs/cli/overview — accessed 2026-07-30
7. millionco/debug-agent `.agents/skills/debug-agent/SKILL.md` + README — `gh api` 2026-07-30
8. JUNERDD/skills `skills/debug/SKILL.md` — `gh api` 2026-07-30
9. `docs/research/notes/theme-9-debug/campaign-brief.md` — E0 campaign bounds / F6 lean
10. `docs/research/notes/theme-9-debug/t9-coordinator-pin.md` — E0 W1 constraints
11. `docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md` — E0 NDJSON cluster prior
