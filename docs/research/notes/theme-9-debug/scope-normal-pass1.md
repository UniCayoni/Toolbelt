---
title: "Theme 9 — Debug pocket normal scope (pass 1)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/packs/README.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 9 — Debug pocket: normal research pass 1

**Using `research-protocol`**; depth: **normal** (scoping — what to expand then brief for deep).

**Status:** `draft`. Not Debug SoT.  
**Identity:** Theme 9 is the **Debug / investigate / reproduce** pocket — **distinct from** Theme 8 Verify gates (Plan/Execute completion evidence). Lean: evidence over assumptions; quality/readability of diagnosis; Toolbelt-native method (inspire, don’t depend).

## 1. Scope

- Question: How should agents **debug methodically** (investigate, reproduce, validate with evidence), what do community/Cursor surfaces teach, and what should Toolbelt own vs park?
- In: Systematic debugging method; reproduce-before-fix; hypothesis+instrumentation; Cursor built-in tools; GitHub skills inventory; RAG corroboration; boundary vs Verify/PR.
- Out: Elevating skills; full PR/merge pack design; inventing Cursor private APIs; deep fleets (later).

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | WebSearch; WebFetch (Cursor agent overview, Debug Mode); `gh api` Superpowers systematic-debugging + verification-before-completion; Alexandria `rag_probe` + `rag_query` (`software_engineering`, `ai_llm_agents`); Read Theme 8 G10 leftovers; Grep cursor-team-kit skills |
| Queries (exact) | Cursor agent debugging browser terminal; systematic debugging SKILL.md GitHub; Alexandria: systematic debug reproduce hypothesis; AI agents investigate failures evidence |
| What was *not* searched | Exhaustive fork tree of every Superpowers mirror; live E0 Toolbelt debug trials; full IDE debugger protocol (VS Code DAP) deep-read |
| Depth | normal |
| stop_reason | Pass-1 inventory complete; expansion needed on concept map + surface options + Cursor Debug Mode atoms |

## 3. E0 — Toolbelt boundary (input)

- `FACT` [E0] Packs: **Debug / PR / workflow** is stub; Theme 8 Verify is shipped and explicitly **not** Debug. [E0: `docs/packs/README.md`; Theme 8 report]
- `FACT` [E0] Theme 8 G10 leftovers for later Debug/PR include: systematic debugging / root-cause playbooks; PR create/finish; Copilot PR packaging; git ceremony; fat Review pack; Bugbot/CI babysit. [E0: `t8d-w1-surface-elevation.md` §4.6]
- `FACT` [E0] Execute already owns Done-when verify + N=2 + major-deviation HITL; execute-verify owns post-green + EOP converge. Debug should **not** re-own those as SoT. [E0: Theme 7/8 reports]

## 4. Cursor built-in surfaces (E1)

| Surface | What it provides for debug | Citation |
|---------|---------------------------|----------|
| **Debug Mode** | Hypothesize → instrument (logs to local debug server) → **human reproduces** → analyze runtime logs → targeted fix → verify + remove instrumentation | [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-30] |
| **Agent Terminal** | Run shell/tests/builds; read output; Run Mode / sandbox controls when commands execute | [E1: https://cursor.com/docs/agent/tools/terminal ; overview tools — accessed 2026-07-30] |
| **Browser tool** | Navigate/interact; console + network for UI/API debug; screenshots | [E1: https://cursor.com/docs/agent/tools/browser — via WebSearch/snippets 2026-07-30; full fetch timed out once] |
| **Search / read / edit** | Locate symbols, read stacks, apply minimal patches after root cause | [E1: agent overview] |
| **Checkpoints** | Local rollback of agent edits (not Git) — useful when debug thrashing | [E1: agent overview] |
| **CLI `/debug`, `/logs`** | Toggle Debug mode; show debug log path | [E1: CLI slash-commands via WebSearch] |
| **Bugbot / review-bugbot** | PR/diff review subagent — **adjacent** (review), not full debug method | [E0: cursor skill `review-bugbot`] |
| **MCP** | Extends observation (Sentry, Playwright, Chrome DevTools, etc.) — host-configured, not Toolbelt packaging by default | [E1/E3: Cursor MCP docs / guides] |

- `FACT` [E1] Cursor Debug Mode’s explicit pitch is **runtime evidence rather than guessing at fixes**, with human-in-the-loop reproduction. [E1: debug-mode docs]
- `INFERENCE` [E4] Toolbelt Debug method should **compose with** Cursor Debug Mode / terminal / browser — teach *when/how* to use them in a discipline — not replace Cursor’s instrumentation server. Premises: Debug Mode E1; Toolbelt standalone spirit.

## 5. Community / GitHub skill cluster (E1/E3)

| Surface | Transferable atoms | Park |
|---------|-------------------|------|
| **obra/superpowers `systematic-debugging`** | Iron law: no fixes without Phase 1; 4 phases (investigate → pattern → hypothesis → implement); reproduce or gather more; 3-fix stop → architecture question; red-flag wording | Mandatory TDD coupling; Superpowers packaging |
| **verification-before-completion** | Evidence before “fixed” claims — already Theme 8 execute-verify lean | Don’t duplicate as Debug-only SoT |
| **reproduce-my-bug** (silkyland) | **Never fix** skill; evidence sweep; ranked hypotheses; minimal failing test; flaky protocol; REPRO dossier | Product-specific dossier path |
| **bug-investigate-fix** (rbouschery) | Reproduce on same surface (browser/API/CLI); hypothesis test; verify repro gone | Thermo-nuclear-plan coupling; slash-only |
| **investigate** (turbo) | Characterize–isolate–hypothesize–test; diagnose without fixing | Heavy multi-agent ceremony |
| **cursor-team-kit `control-cli` / `control-ui` / `verify-this`** | Harness patterns for CLI/UI evidence; compare raw artifacts | Team-kit packaging; not Toolbelt SoT |
| **ci-fix** skills | Log → root cause → patch → re-run | CI/PR pack adjacency |

- `FACT` [E1] Superpowers systematic-debugging iron law and four phases fetched via GitHub API 2026-07-30. [E1: obra/superpowers `skills/systematic-debugging/SKILL.md`]
- `CLAIM` [E3] Reproduce-before-fix and hypothesis ranking appear across multiple independent skill repos (WebSearch 2026-07-30). Stars≠SoT.

## 6. Alexandria / RAG corroboration (E2)

| Corpus | Probe | Signal |
|--------|-------|--------|
| `software_engineering` | systematic debug reproduce root cause | **partial** — strong Osmani + Dooley chunks |
| `ai_llm_agents` | agents investigate failures evidence | **partial** — tool validate/retry/escalate; weaker pure “debug method” |

Key corroborated claims (cite chunks):

- `CLAIM` [E2] Don’t guess; don’t fix symptoms — find root cause systematically; reproduce reliably then find source then fix one thing then test. [E2: Dooley *Software Development…* chunk_ids `9e26a07559361b30390a1ffc`, `08490da27bbde1f95a445ac6`, `f2370255822d37ae59c3860e` — query SE 2026-07-30]
- `CLAIM` [E2] Reduce to simplest failing case (binary-search data/code). [E2: Dooley `f2370255822d37ae59c3860e`]
- `CLAIM` [E2] Osmani: systematically reproduce bugs; verify AI output with tests; don’t assume correct. [E2: Beyond Vibe Coding `8d47c2c2c48be20b60557d8e`]
- `CLAIM` [E2] Agent tooling: validate outputs, intelligent retry, fall back, **log everything** for observability/debug. [E2: Albada *Building Applications with AI Agents* `cf0e47b3b89230ab3cf41578`]
- `CLAIM` [E2] Escalation protocols when agent can’t handle situation. [E2: Bhavsar *Mastering AI Agents* `c9715770c65951cc74d89aa9`]
- `GAP` RAG weak on Cursor-specific Debug Mode / browser console workflows — rely on Cursor E1 docs, not Alexandria.

## 7. Gaps needing expansion (pass 2)

| Gap | Why |
|-----|-----|
| Concept map: investigate vs reproduce vs fix vs verify-fix | Avoid colliding with Theme 8 execute-verify |
| Surface shape options (skill(s) vs compose Cursor Debug Mode) | Elevation later |
| Flaky / intermittent protocol | Community strong; Toolbelt need? |
| Instrumentation discipline (add/remove logs) | Align with Cursor Debug Mode |
| PR/CI slice vs pure Debug | Split or phased pocket |
| How Toolbelt wires from Execute `verify-fail` / HITL into Debug | Ladder seam |

## 8. Implications (pass 1)

- `INFERENCE` [E4] Theme 9 core is a **method pocket**: reproduce → evidence → hypothesis → root cause → minimal fix → re-verify symptom — composed with Cursor tools. Premises: §4–§6.
- `INFERENCE` [E4] Pass 2 warranted before deep brief. Premises: §7.
