---
title: "Theme 9 — Debug pocket normal scope (pass 3 deepen)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-9-debug/scope-normal-pass1.md
  - docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 9 — Debug pocket: normal research pass 3 (deepen)

**Using `research-protocol`**; depth: **normal** (follow Tier-A leads from pass 1–2; enrich tracks before deep Wave 1).

**Status:** `draft`. Not Debug SoT.  
**Trigger:** Human asked for one more scoping pass using prior findings — dig for more tracks under the same parameters (GitHub / Cursor / RAG / evidence-first).

## 1. Scope

- Question: What concrete atoms / surfaces / track splits emerge when we deep-fetch the Tier-A items named in pass 1–2?
- In: Full bodies of systematic-debugging companions, reproduce-my-bug, bug-investigate-fix; Cursor Browser + Debug Mode corroboration; NDJSON / “debug-agent” family; parallel investigate; flaky dossier; RAG refresh.
- Out: Elevating skills; launching deep Wave 1; inventing Cursor private debug-server APIs; shipping MCP/collectors inside Toolbelt.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools | `gh api` content fetch; WebSearch; WebFetch (browser.md OK; learn/finding-fixing-bugs timed out); Alexandria `rag_query` (`software_engineering`) |
| Exact fetches | `obra/superpowers` `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md` (+ dir listing); `silkyland/reproduce-my-bug` `SKILL.md`; `rbouschery/agent-skills` `bug-investigate-fix/SKILL.md`; `stas00/the-art-of-debugging` `SKILL.md`; `Dimillian/Skills` `bug-hunt-swarm/SKILL.md`; `millionco/debug-agent` `.agents/skills/debug-agent/SKILL.md`; Cursor `docs/agent/tools/browser.md` |
| Queries | Cursor debug mode instrumentation; github agent skill debug-agent NDJSON; flaky / instrumentation SKILL.md search |
| Not searched | Live E0 Toolbelt debug trials; VS Code DAP deep-read; silkyland `references/flaky-bugs.md` full body (linked, not fetched) |
| Depth | normal |
| stop_reason | Tier-A bodies + new surface cluster captured; enough to amend brief tracks; further detail → deep T9C/T9E |

## 3. Findings — Superpowers companions (E1)

Dir under `skills/systematic-debugging/`: `SKILL.md`, `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`, `find-polluter.sh`, condition-based-waiting example, test-pressure docs. [E1: `gh api` listing 2026-07-30]

| Companion | Transferable atoms | Park |
|-----------|-------------------|------|
| **root-cause-tracing** | Trace **backward** to original trigger; don’t patch symptom at deep stack; when stuck, temporary stack/`console.error` instrumentation; find test polluters | Full narrative examples as SoT |
| **defense-in-depth** | After invalid-data bugs, validate at **entry + business + environment** layers so bug becomes structurally hard | Over-engineering every fix; Toolbelt thin spirit |
| **condition-based-waiting** | Flaky tests: wait for **condition**, not arbitrary sleep; document when timing *is* the subject | Shipping wait helpers as Toolbelt code |

- `FACT` [E1] Root-cause-tracing core: observe symptom → immediate cause → callers → original trigger; add defense-in-depth when fixing. [E1: `root-cause-tracing.md`]
- `INFERENCE` [E4] These belong as **method atoms under T9A/T9C**, not separate elevated skills by default. Premises: Theme 8 thin spirit; pass2 lean A/B.

## 4. Findings — reproduce-my-bug (E1 deepen)

Seven-step spine fetched: Intake → Evidence sweep → Path trace → Reproduce → Minimize → **Flaky path** → **Dossier**. [E1: silkyland `SKILL.md`]

| Atom | Detail |
|------|--------|
| Prime directive | **No fix without failing reproduction**; skill **never patches** |
| Hard rules | App code read-only except repro artifacts; production = evidence only (local/dev bench); one variable at a time; repro must **fail** (green ≠ repro) |
| Flaky | Identify nondeterminism (concurrency, clock, ordering, randomness, network, cache); **force** it; else document **reproduction rate** + recipe |
| Deliverable | `REPRO.md` / dossier: command + failing output + eliminated hypotheses; root cause optional/`UNVERIFIED`; handoff to fixer |
| Failure modes | `NOT-YET-REPRODUCED`; path not runnable locally → report blocker first |

- `FACT` [E1] Flaky protocol and dossier steps are first-class in reproduce-my-bug (Steps 6–7). [E1: silkyland SKILL.md]
- `INFERENCE` [E4] Strengthens surface option **B** (spine + never-fix companion) and argues for a **named flaky checklist** inside method — still not a third skill. Premises: pass2 A/B; thin Toolbelt.

## 5. Findings — bug-investigate-fix (E1 deepen)

End-to-end: Reproduce → Hypotheses (1–4, falsifiable table) → Test hypotheses → short fix plan → Implement → **Verify same repro gone**. [E1: rbouschery]

| Atom | Detail |
|------|--------|
| Same-surface repro | Web→browser; API→curl; CLI→flags; jobs→local hook — not code-read-as-repro |
| Hypothesis discipline | Specific, falsifiable, tied to symptoms; record confirms/rejects/inconclusive |
| Stop | One small hypothesis loop if all rejected — don’t spiral |
| Verify | Re-run **same** minimal repro; report before→after |

- `FACT` [E1] Skill couples fix planning to **thermo-nuclear-plan** when available; documents fallback “code judo” short plan. [E1: rbouschery SKILL.md]
- `INFERENCE` [E4] Transfer workflow atoms; **park** thermo-nuclear coupling and `disable-model-invocation` slash-only packaging. Premises: Toolbelt standalone; Theme 8 already has plan-verify.

## 6. Findings — Cursor native (E1 deepen)

### 6.1 Browser (full fetch)

- Console + network for debug; screenshots via file-read images; **browser logs written to files** agent can grep selectively; dev-server awareness (correct ports). [E1: https://cursor.com/docs/agent/tools/browser.md — accessed 2026-07-30]
- Session persistence per workspace (cookies/storage); approval modes; enterprise origin allowlist. Security/approval atoms for compose guidance, not Toolbelt packaging.

### 6.2 Debug Mode corroboration

- Official loop: explore/hypothesize → instrument (logs to **local debug server** in extension) → **human reproduces** → analyze → targeted fix → verify + remove instrumentation. [E1: cursor.com/docs/agent/debug-mode; blog/debug-mode — via WebSearch 2026-07-30]
- Secondary (E2/E3): instrumentation as HTTP/JSON (or file) posts; language-agnostic; multi-model parallel debug mentioned on learn pages — treat as CLAIM until primary learn page fetched (fetch timed out this pass). [E2/E3: learncursor / davidgomes / WebSearch snippets]
- Learn “finding-fixing-bugs”: MCP observability (Sentry/Datadog) as **evidence feed**, not replace local repro. [E2: WebSearch snippet of cursor.com/learn/finding-fixing-bugs]

- `INFERENCE` [E4] Toolbelt should teach **when to prefer Cursor Debug Mode** vs Agent+terminal/browser evidence — and **must not** reimplement Cursor’s private debug server. Premises: Debug Mode E1; standalone spirit.

## 7. Findings — NDJSON / “debug-agent” cluster (E1/E3)

| Surface | Signal | Toolbelt lean |
|---------|--------|---------------|
| **millionco/debug-agent** | Hypotheses → NDJSON logs (`sessionId`, `runId`, `hypothesisId`, …) → user repro → CONFIRMED/REJECTED/INCONCLUSIVE → fix only with log proof → cleanup `#region debug log` | **Atom source** for “Agent-mode instrumentation protocol” when Debug Mode unavailable; **park** shipping npx collector |
| **JUNERDD/skills `debug`** | Evidence-first + optional local NDJSON collector (README synthesis) | Park packaging; same protocol atoms |
| **XcodeBazelMCP swift-agent-debug-log** | NDJSON schema aligned with Cursor DEBUG MODE for iOS | Domain park; schema corroboration only |

- `FACT` [E1] debug-agent SKILL mandates 3–5 hypotheses, instrumentation before fix, cited log evidence, keep instrumentation until post-fix verify. [E1: millionco/debug-agent SKILL.md]
- `CLAIM` [E3] Community is converging on Cursor-like “instrument → repro → classify hypotheses” outside Debug Mode. Stars≠SoT.
- `GAP` Exact Cursor extension debug-server wire protocol — **do not invent**; compose via mode switch / CLI `/debug`.

## 8. Findings — other Tier-A adjacent (E1/E3)

| Surface | Transferable | Park |
|---------|--------------|------|
| **stas00/the-art-of-debugging** | Loop: reproduce reliably → **shrink** payload → localize → usable signal; pin flaky nondeterminism first | Unix/Python/PyTorch recipe encyclopedia as SoT |
| **Dimillian bug-hunt-swarm** | Bug packet; bound investigation; **four read-only** parallel investigators; diagnosis-first **no edits/instrumentation/fixes** | Mandatory 4-agent ceremony; fat orchestration |

- `INFERENCE` [E4] Swarm = optional **escalation** for large/ambiguous bugs, not default spine (conflicts thin Toolbelt + burns context). Premises: pass2 thin lean; Theme 8 hybrid not “always swarm”.

## 9. RAG refresh (E2)

`rag_query` `software_engineering` (k=6) again supports: reproduce reliably before locating/fixing; sporadic causes (init, timing, races, …); shrink/binary-search repro; Osmani-style reproduce → locate (prints/debugger) → … [E2: Dooley ch.17 chunks; Osmani Beyond Vibe Coding — 2026-07-30]

No new conflicting school found.

## 10. Track amendments (input to brief)

| Track | Change |
|-------|--------|
| **T9A** | Absorb: root-cause backward trace; 3-fix / architecture stop; flaky **light** checklist (force nondeterminism or rate); shrink repro; defense-in-depth as *optional post-fix* note not mandatory every bug |
| **T9B** | Absorb: Browser file-log/grep evidence; Debug Mode vs Agent instrumentation stance; MCP observe-only; checkpoints on thrash; human-repro HITL |
| **T9C** | Deepen companions + reproduce-my-bug dossier/flaky + debug-agent NDJSON + art-of-debugging loop; transferable vs park tables |
| **T9D** | Unchanged A/B/C/D; **B slightly stronger** after never-fix + dossier evidence |
| **T9E (new)** | **Instrumentation & evidence capture** — when to use Cursor Debug Mode; Agent-mode NDJSON/file protocol atoms (inspire, don’t ship collector); cleanup markers; hypothesisId discipline; no private API invention |
| **T9F (optional / park default)** | Parallel read-only investigate (swarm) — only if W2 shows P0 need |

## 11. Surface lean update

| Option | Pass-3 nudge |
|--------|----------------|
| A thin spine | Still viable if flaky + reproduce rules live **inside** one skill |
| **B spine + reproduce companion** | **Slightly preferred** — never-fix + dossier is a distinct gravity well matching user “evidence not assumptions” |
| C compose-only | Weaker — Browser/Debug Mode docs alone don’t encode Toolbelt ladder seams |
| D fat pack | Still deferred; swarm/CI/Bugbot stay Phase 2 |

## 12. Implications

- `INFERENCE` [E4] Normal scoping is now **pass1+2+3**; amend campaign brief with **T9E**; keep deep Wave 1 gated on human approve. Premises: `draft-is-not-sot`; user requested pass3 not deep launch.
- Fourth normal pass: **skip** unless human wants silkyland flaky reference deep-read or live E0 trials.
