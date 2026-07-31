---
title: "T9B W1 — Cursor native composition (Debug Mode, Terminal, Browser, CLI)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [t9b-w1-gatherer]
depth: deep
campaign_phase: deep_wave1
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-coordinator-pin.md
  - docs/research/notes/theme-9-debug/scope-normal-pass1.md
  - docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
supersedes: null
---

# T9B W1 — Cursor native composition

**Using `research-protocol`**.

**Status:** `draft` Wave-1 gatherer note. Not Debug SoT. Does not elevate skills/rules. T9F out of W1.

## 1. Scope

- Question / goal: How should Toolbelt Debug skills **compose** Cursor natives (Debug Mode, Terminal, Browser, Checkpoints, CLI `/debug` `/logs`, Run Mode, host MCP observe-only) **without replacing** Cursor Debug Mode or inventing private debug-server APIs?
- In scope: Primary Cursor docs for Debug Mode loop atoms + prefer-when; Terminal evidence discipline; Browser console/network/file logs; Checkpoints; CLI slash commands; Run Mode implications; MCP observe stance; compose matrix by symptom class; what Toolbelt must not reimplement; fence F6/F9 evidence implications; W2 residuals.
- Out of scope: T9A method spine design locks; T9E shipping collectors / NDJSON packaging; T9F swarm; inventing Cursor private wire protocols; elevating Toolbelt surfaces; Theme 8 re-litigation.
- Comprehension / research goal type (if code): other (product-docs compose)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Read (campaign-brief, t9-coordinator-pin, pass1–3); WebFetch (Cursor primary docs + blog + help + learn); WebSearch (CLI slash-commands discovery) |
| Corpora / URLs searched | `https://cursor.com/docs/agent/debug-mode`; `https://cursor.com/blog/debug-mode`; `https://cursor.com/help/ai-features/debug-mode`; `https://cursor.com/docs/agent/tools/terminal`; `https://cursor.com/docs/agent/tools/browser`; `https://cursor.com/docs/agent/overview`; `https://cursor.com/docs/agent/security/run-modes`; `https://cursor.com/docs/cli/reference/slash-commands`; `https://cursor.com/docs/mcp`; `https://cursor.com/learn/finding-fixing-bugs` |
| Queries (exact) | Cursor IDE debug mode documentation agent hypothesize instrument 2026; site:cursor.com/docs CLI slash commands /debug /logs agent; site:cursor.com/docs agent terminal read full output logs evidence; site:cursor.com/docs MCP Sentry observe agent debugging finding bugs |
| What was *not* searched | Live E0 Toolbelt Debug Mode sessions; VS Code DAP protocol deep-read; Cursor extension source / private debug-server wire capture; JetBrains ACP Debug Mode availability beyond secondary snippets; exhaustive marketplace Sentry/Datadog MCP schemas |
| Depth | deep |
| Waves / stop_reason | W1 gatherer slice; `stop_reason: wave1_slice_coverage` |
| Provenance (optional PROV) | Entity←Cursor docs/blog/help/learn + Theme 9 scoping notes; Activity=T9B W1 compose gather; Agent=t9b-w1-gatherer |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Track is product-docs compose, not workspace recon |
| Scope boundary | Cursor agent/CLI docs + Theme 9 campaign inputs; no Toolbelt skill elevation |

## 4. Findings

### 4.1 Debug Mode loop atoms + when to prefer

- `FACT` [E1] Debug Mode is an agent loop that generates hypotheses, adds log instrumentation, uses runtime information, then makes a targeted fix — not immediate speculative coding. [E1: Cursor Docs — Debug Mode — https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Official six-step loop: (1) explore and hypothesize (multiple hypotheses); (2) add instrumentation sending data to a **local debug server in a Cursor extension**; (3) human reproduces with provided steps; (4) analyze collected logs; (5) make targeted fix; (6) verify via re-reproduction and remove instrumentation. [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Prefer Debug Mode for: reproducible-but-unclear cause; race/timing; performance/memory needing runtime profiling; regressions needing change-trace; and when standard Agent interactions struggle. [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Tips: detailed context (errors, stacks, steps); follow repro steps exactly; reproduce multiple times for races; state expected vs actual. [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Mode switch: Agent mode picker dropdown or Shift+Tab. [E1: https://cursor.com/docs/agent/debug-mode ; https://cursor.com/help/ai-features/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Help: use Agent mode when you know what to build; use Debug mode when something isn’t working and you need to find out why. [E1: https://cursor.com/help/ai-features/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Product blog: human-in-the-loop reproduce + verify is critical; if not fixed, add more logging and iterate; cleanup leaves a clean minimal change. [E1: https://cursor.com/blog/debug-mode — accessed 2026-07-30]
- `FACT` [E1] Learn guide mirrors fundamentals (repro → minimize → isolate → hypothesize → instrument → prevent regressions) and positions Debug Mode as evidence-first for trickier/intermittent bugs; simple clear stack traces may be fixed directly in Agent. [E1: https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt Debug skills should **invoke/prefer Cursor Debug Mode** (mode switch / CLI `/debug`) for unclear runtime causes rather than reimplementing the local debug-server loop. Premises: (1) E1 loop owns instrumentation→human-repro→cleanup; (2) campaign non-goal: no private API invention; (3) brief T9B compose-not-replace.

### 4.2 Terminal evidence rules

- `FACT` [E1] Agent can execute shell commands and monitor output; default uses the first terminal profile. [E1: https://cursor.com/docs/agent/overview — accessed 2026-07-30]
- `FACT` [E1] Terminal execution is gated by Run Modes (when commands run / ask / sandbox). [E1: https://cursor.com/docs/agent/tools/terminal ; https://cursor.com/docs/agent/security/run-modes — accessed 2026-07-30]
- `FACT` [E1] Heavy shell themes can truncate/misformat inline terminal output; docs recommend detecting `CURSOR_AGENT` and simplifying prompts. [E1: https://cursor.com/docs/agent/tools/terminal — accessed 2026-07-30]
- `FACT` [E1] Learn guide: paste terminal / query / build-test output into the conversation when code analysis alone is insufficient. [E1: https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt compose rule for Terminal should require **run fresh command → read complete available output (incl. exit/failures) before claiming** — aligning Theme 8 Superpowers READ-full-output discipline with Cursor terminal as the evidence surface; treat theme truncation as a known evidence hazard. Premises: (1) Theme 8 execute-verify Iron Law READ step [E0/E1 via Theme 8 notes]; (2) Terminal monitors output [E1 overview]; (3) truncation hazard [E1 terminal troubleshooting].
- `GAP` Primary Cursor Agent Terminal docs do **not** explicitly mandate “always read full output” as a product rule. Searched: `docs/agent/tools/terminal`, overview. Result: capability + Run Mode + truncation tips only. Toolbelt method may still teach READ-full as compose discipline (see Inference above).

### 4.3 Browser evidence (console / network / file logs)

- `FACT` [E1] Browser tool provides console output and network traffic for debugging; screenshots; navigate/click/type/scroll. [E1: https://cursor.com/docs/agent/tools/browser — accessed 2026-07-30]
- `FACT` [E1] Efficient log handling: browser logs are **written to files** the agent can grep and selectively read; smart prompting includes line counts and preview snippets; development-server awareness for correct ports. [E1: https://cursor.com/docs/agent/tools/browser — accessed 2026-07-30]
- `FACT` [E1] Screenshots integrate with file-read images so the agent sees browser state visually. [E1: https://cursor.com/docs/agent/tools/browser — accessed 2026-07-30]
- `FACT` [E1] Session persistence per workspace (cookies, localStorage/sessionStorage, IndexedDB); approval modes; enterprise origin allowlist. [E1: https://cursor.com/docs/agent/tools/browser — accessed 2026-07-30]
- `FACT` [E1] Learn: for frontend, agent can open a page, reproduce, check console errors and network for slow/failed requests — sees DevTools-like signals. [E1: https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt compose guidance: UI/API-in-browser symptoms → prefer Browser (console + network + greppable log files + screenshots); do not treat code-read alone as same-surface repro. Premises: browser E1; pass3 same-surface atom (community, for T9C).

### 4.4 Checkpoints (thrash undo)

- `FACT` [E1] Checkpoints auto-save snapshots before significant Agent changes; restore reverts modified files to that state; stored locally and **separate from Git**; intended for undoing Agent changes, not permanent VCS. [E1: https://cursor.com/docs/agent/overview — accessed 2026-07-30]
- `INFERENCE` [E4] During wrong-hypothesis patch thrash, prefer Checkpoint restore (or Git) over further speculative edits; Toolbelt method should mention Checkpoints as escape hatch, not reimplement snapshotting. Premises: checkpoints E1; Debug Mode cleanup ethos [E1 debug-mode].

### 4.5 CLI `/debug` and `/logs`

- `FACT` [E1] CLI slash command `/debug [prompt]` — toggle Debug mode or submit a prompt in Debug mode. [E1: https://cursor.com/docs/cli/reference/slash-commands — accessed 2026-07-30]
- `FACT` [E1] CLI slash command `/logs` — show the debug log path and copy it to the clipboard. [E1: https://cursor.com/docs/cli/reference/slash-commands — accessed 2026-07-30]
- `FACT` [E1] CLI overview claims the CLI supports the same modes as the editor (Agent / Plan / Ask via slash commands / shortcuts / `--mode`). [E1: https://cursor.com/docs/cli/overview — via WebSearch snippet corroborated by slash-commands table including `/debug` — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt compose: when working in CLI, enter Debug via `/debug` and locate runtime/debug logs via `/logs` rather than inventing a Toolbelt log path API. Premises: slash-commands E1; Debug Mode local server ownership [E1 debug-mode].
- `GAP` Exact filesystem layout / schema of what `/logs` points to (beyond “debug log path”) not specified in the slash-commands table. Searched: slash-commands page. Result: description only. Do not invent path conventions.

### 4.6 Run Mode implications

- `FACT` [E1] Run Modes (Auto-review / Allowlist / Run Everything) control autonomy for shell, MCP, and Fetch; sandboxing layers file/network limits on shell when applicable. [E1: https://cursor.com/docs/agent/security/run-modes — accessed 2026-07-30]
- `FACT` [E1] MCP follows the same Run Modes as terminal commands. [E1: https://cursor.com/docs/mcp — accessed 2026-07-30]
- `INFERENCE` [E4] Compose notes should remind agents that repro/test evidence may be blocked or sandboxed — treat approval/sandbox failure as environmental blocker, not “bug fixed.” Premises: Run Modes E1; Terminal/MCP coupling E1.

### 4.7 MCP stance — observe only; do not package in Toolbelt

- `FACT` [E1] MCP connects Cursor to external tools/data; host-configured via Customize / `mcp.json` / marketplace; agent uses listed tools when relevant. [E1: https://cursor.com/docs/mcp — accessed 2026-07-30]
- `FACT` [E1] Learn guide: MCP brings runtime/observability into the agent loop (example: pull Sentry + Datadog for checkout error spike); lists useful debugging MCPs — Sentry, Datadog, databases, Linear/GitHub Issues. [E1: https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30]
- `FACT` [E1] Learn: monitoring can feed evidence; still pairs with debugging fundamentals (repro, hypotheses, root cause). [E1: https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30]
- `INFERENCE` [E4] Toolbelt Debug should teach **“use host-configured observability MCP if present (observe/correlate)”** and must **not** ship Sentry/Datadog/collector MCP servers or NDJSON collectors inside Toolbelt. Premises: (1) MCP is host/product integration [E1 mcp]; (2) campaign/coordinator hard constraint: don’t package collectors/MCP; (3) Debug Mode already owns local instrumentation server.
- `CLAIM` [E2] Cloud Automations can trigger on Sentry issue events for investigate/propose-fix workflows — adjacent product surface, not Toolbelt packaging. [E2: https://cursor.com/docs/cloud-agent/automations — accessed 2026-07-30 via WebSearch/fetch synthesis]

### 4.8 Compose matrix — symptom class → preferred Cursor surface

Evidence-backed preference table (compose guidance, **not** elevation lock):

| Symptom class | Prefer first | Also use | Avoid / park |
|---------------|--------------|----------|--------------|
| Clear stack / obvious null / failing unit test with local repro | Agent + **Terminal** (run test, READ output) | Search/read for site of fault | Don’t open Debug Mode by default [E1 help: Agent when you know what to build] |
| Reproducible but cause unclear from code | **Debug Mode** (hypothesize→instrument→human repro→logs→fix→cleanup) | Terminal for any scripted repro; Checkpoints if thrash | Don’t invent private log-server client [GAP §4.9] |
| Race / timing / intermittent | **Debug Mode** + multi-repro tips | Terminal stress/repro scripts; flaky checklist (T9A/T9C) | Don’t “fix and hope” without runtime evidence [E1 debug-mode] |
| Perf / memory / needs profiling data | **Debug Mode** and/or paste profiler/`EXPLAIN` into Agent | Terminal for profilers; MCP APM if configured | Don’t guess hot paths from vibes [E1 learn] |
| UI / frontend visual or client JS | **Browser** (console, network, screenshots, greppable log files) | Terminal for dev server; Debug Mode if runtime path unclear across layers | Don’t treat static code-read as UI repro [E1 browser + learn] |
| API / HTTP contract from page | **Browser network** + Terminal (`curl`/tests) as needed | Host MCP if API observability configured | — |
| CLI / build / test failure | **Terminal** (full available output) | Checkpoints after bad patches | Theme truncation hazard [E1 terminal] |
| Production error spike (Sentry etc.) | Host **MCP observe** (if configured) → then local repro | Automations adjacent (product) | Don’t ship Toolbelt MCP; don’t skip local repro when possible [E1 learn + brief] |
| Wrong-hypothesis edit thrash | **Checkpoints** restore (+ Git) | Re-enter Debug Mode with cleaner hypotheses | Don’t keep patching without new evidence [E1 overview + debug-mode] |
| Working in Cursor CLI | `/debug` for Debug Mode; `/logs` for debug log path | Same compose matrix otherwise | Don’t invent Toolbelt log-path SoT [E1 slash-commands; GAP path schema] |

- `INFERENCE` [E4] Toolbelt skills should encode this matrix as **when/how to switch surfaces**, not as a parallel debug runtime. Premises: matrix rows cite E1 surfaces above; campaign T9B identity.

### 4.9 What Toolbelt must NOT reimplement

- `FACT` [E1] Instrumentation in Debug Mode targets a **local debug server running in a Cursor extension** — product-owned surface. [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30]
- `GAP` **Private debug-server wire protocol** (HTTP paths, JSON schema, auth, ports, language SDKs): **not documented** in primary Debug Mode / slash-commands / overview docs fetched this pass. Searched: debug-mode docs, blog, help, slash-commands, learn finding-fixing-bugs. Result: existence of local debug server + log analysis mentioned; **no** public wire-protocol spec. **Confirm GAP — do not invent.** Secondary community claims (HTTP/JSON POST) remain non-locking (E2/E3 from pass3).
- `INFERENCE` [E4] Toolbelt must not: replace Debug Mode; ship a competing collector/server; hardcode private endpoints; package observability MCP. Premises: GAP wire protocol; MCP host-config E1; campaign hard constraints.
- `INFERENCE` [E4] Acceptable Agent-mode fallback when Debug Mode unavailable: ordinary terminal/browser evidence + optional marked temporary logs — protocol atoms belong to T9E, still without shipping collectors. Premises: pass3 T9E split; Debug Mode prefer-when E1.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Toolbelt can compose Cursor natives via mode/tool guidance without owning debug-server APIs | confirmed (compose level) | E1 surfaces documented; wire protocol GAP |
| H2 | Primary docs publish debug-server wire protocol sufficient to reimplement | rejected | GAP §4.9 |
| H3 | Browser file-log/grep is first-class evidence for UI debug | confirmed | E1 browser.md |
| H4 | CLI `/debug` `/logs` are documented first-class entrypoints | confirmed | E1 slash-commands |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Help vs docs depth | Help page summarizes Debug as investigate with errors/stacks/runtime before fixes | Full docs spell 6-step instrument→human-repro loop | Prefer docs [E1] for loop atoms; help still valid for Agent vs Debug prefer |
| “Read full output” | Theme 8 / Superpowers Iron Law READ full output | Cursor Terminal docs omit explicit mandate | Keep as Toolbelt compose INFERENCE + Theme 8 alignment; mark Cursor-doc GAP for explicit wording |
| Wire protocol | Community/learn secondary: HTTP/JSON to local server | Primary docs: “local debug server” only | Prefer GAP; no design lock on invented schema |

## 7. Gaps & OPEN

- `GAP` Cursor private debug-server **wire protocol** — confirmed absent from primary docs (see §4.9).
- `GAP` `/logs` path/schema details beyond “show debug log path.”
- `GAP` Terminal docs lack explicit “read full output” product rule (Toolbelt may still teach it).
- `OPEN` JetBrains ACP / non-desktop Debug Mode availability — secondary snippets only; not needed for W1 compose matrix.
- `OPEN` W2: corroborate whether Agent-mode instrumentation should cite Debug Mode cleanup norms by name in skill text (T9E overlap).
- `OPEN` W2: any E0 trial of `/debug` + `/logs` path shape in CLI (optional; still no protocol invention).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

### 8.1 Fence F6 — Instrumentation home (evidence only)

- `INFERENCE` [E4] F6 working lean “section of spine (+ T9E atoms)” is consistent with compose evidence: **prefer Cursor Debug Mode** for instrumentation when available; Agent-mode protocol atoms as fallback — **not** a Toolbelt-packaged collector, and **not** “compose Debug Mode only” if Agent-mode terminal/browser evidence still needed for clear failures. Premises: §4.1 prefer-when; §4.2–4.3; §4.9 GAP; brief F6 lean.
- Candidate pros/cons for integrator (not adjudication):

| Option | Pros (evidence) | Cons (evidence) |
|--------|-----------------|-----------------|
| Section of spine (+ T9E atoms) | Teaches when to switch to Debug Mode; keeps fallback; matches thin method | Risk of colliding with Cursor “Debug Mode” naming (F2) |
| Short companion skill | Isolates instrumentation cleanup discipline | Extra surface; may duplicate T9E |
| Compose Debug Mode only | Thinnest; zero private API | Weak for clear Terminal/Browser cases; no Agent-mode fallback [E1 help/learn] |

### 8.2 Fence F9 — Always-on debug rule (evidence only)

- `INFERENCE` [E4] Primary Cursor surfaces are **mode/tool opt-in** (mode picker, `/debug`, Browser tools, MCP when configured) — no Cursor doc found requiring always-on debug behavior. Skill-only Toolbelt Debug (F9 lean: unlikely always-on rule) fits product model. Premises: mode switching E1; MCP optional E1; brief F9 lean.
- Counter-signal to watch in W2: none strong in primary docs this pass — residual only if W2 finds mandatory Cursor hooks forcing debug instrumentation.

### 8.3 Ladder / naming (pointer, not T9D)

- `INFERENCE` [E4] Naming should avoid colliding with product “Debug Mode” (F2) while skills still say “switch to Cursor Debug Mode when…”. Premises: product name E1; brief F2 OPEN.

## 9. Source list (deduped)

1. Cursor Docs — Debug Mode — https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30
2. Cursor Blog — Introducing Debug Mode — https://cursor.com/blog/debug-mode — accessed 2026-07-30
3. Cursor Help — Debug mode — https://cursor.com/help/ai-features/debug-mode — accessed 2026-07-30
4. Cursor Docs — Terminal — https://cursor.com/docs/agent/tools/terminal — accessed 2026-07-30
5. Cursor Docs — Browser — https://cursor.com/docs/agent/tools/browser — accessed 2026-07-30
6. Cursor Docs — Agent overview (tools + Checkpoints) — https://cursor.com/docs/agent/overview — accessed 2026-07-30
7. Cursor Docs — Run Modes — https://cursor.com/docs/agent/security/run-modes — accessed 2026-07-30
8. Cursor Docs — CLI slash commands — https://cursor.com/docs/cli/reference/slash-commands — accessed 2026-07-30
9. Cursor Docs — MCP — https://cursor.com/docs/mcp — accessed 2026-07-30
10. Cursor Learn — Finding and fixing bugs — https://cursor.com/learn/finding-fixing-bugs — accessed 2026-07-30
11. Cursor Docs — Cloud Automations (Sentry triggers; secondary for MCP/observe adjacency) — https://cursor.com/docs/cloud-agent/automations — accessed 2026-07-30
12. Theme 9 campaign brief / coordinator pin / pass1–3 — `docs/research/notes/theme-9-debug/` — E0 campaign inputs

## 10. Residuals → W2

| ID | Residual | Why W2 |
|----|----------|--------|
| R1 | Optional E0 CLI trial: `/debug` + `/logs` observed path shape (describe only) | Close `/logs` GAP without inventing protocol |
| R2 | Cross-check T9E Agent-mode instrumentation atoms against this compose matrix (no collector) | Avoid T9B/T9E contradiction |
| R3 | Confirm F9: still no primary-doc pressure for always-on debug rule | Fence pros/cons in integrate |
| R4 | Secondary learncursor wire claims — keep parked unless Cursor publishes primary protocol | Preserve GAP discipline |
| R5 | Parallel multi-model debug (learn page) — compose mention only vs park | Thinness vs effectiveness for integrator |

---

**W1 stop:** `wave1_slice_coverage` — primary Cursor compose surfaces covered; private wire protocol GAP confirmed; F6/F9 evidence recorded without lock; T9F out.
