---
title: "Theme 9 — Debug pocket normal scope (pass 2 expand + analysis)"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/notes/theme-9-debug/scope-normal-pass1.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/research/reports/theme-7-execute-pocket.md
supersedes: null
---

# Theme 9 — Debug: pass 2 expand + analysis

**Using `research-protocol`**; depth: **normal**.

**Lean:** evidence over assumptions; diagnosis quality; Toolbelt standalone; compose Cursor native tools; thin method over fat Debug mega-pack.

## 1. Scope

Close pass-1 gaps enough to write a Theme 9 **deep campaign brief**. Decide if a third normal pass is needed.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Synthesis of pass-1 evidence; re-read Cursor Debug Mode; Theme 7/8 boundaries; WebSearch reproduce-my-bug / bug-investigate-fix atoms |
| What was *not* searched | Full VS Code DAP protocol; production APM vendor bake-offs; live E0 Toolbelt trials |
| Depth | normal |
| stop_reason | Expansion gaps closed at discovery level; remaining unknowns are deep-track grade |

## 3. Expanded concept map (for deep)

### 3.1 Pocket jobs (distinct)

| Job | Meaning | Toolbelt home (candidate) |
|-----|---------|---------------------------|
| **Investigate** | Characterize symptom; read errors/stacks; gather logs/state; recent changes | Debug spine |
| **Reproduce** | Reliable trigger; minimal steps/command/test; same surface as report (UI/API/CLI) | Debug spine (hard gate) |
| **Hypothesize + falsify** | Single testable hypothesis; one variable; instrumentation when needed | Debug spine; Cursor Debug Mode compose |
| **Root-cause** | Trace to origin (not symptom site); pattern compare working vs broken | Debug spine |
| **Fix minimally** | One change addressing cause; no drive-by | Debug → may hand off to Execute/plan if large |
| **Verify fix** | Re-run **same** repro; evidence before “fixed” | Debug + Theme 8 evidence iron law (compose, don’t fork) |
| **Plan/Execute verify** | Done-when / post-green / converge | **Theme 8** — not Debug |
| **PR / CI babysit** | Merge workflows, Bugbot loops | Later PR slice or Phase 2 of this pocket |

### 3.2 Method spine (candidate — not elevated)

```text
0. Symptom intake (expected vs actual; artifacts: error, steps, env)
1. INVESTIGATE — read full error/stack; recent changes; locate code
2. REPRODUCE — tight loop (test/script/manual); if can't → gather more, don't guess
3. HYPOTHESIZE — write one hypothesis; instrument if needed (Cursor Debug Mode OK)
4. FALSIFY — smallest experiment; kill or confirm hypothesis
5. ROOT CAUSE — document cause (not just symptom)
6. FIX — minimal; optional failing test first (TDD optional, not law)
7. VERIFY — same repro green + no vibes; clean instrumentation
8. ESCALATE — after N failed fix cycles or architecture smell → human (align Theme 7 HITL spirit)
```

- `INFERENCE` [E4] Align N-failed-fixes stop with Superpowers “3 then architecture” as **candidate**, not lock — deep will choose Toolbelt N. Premises: pass-1 Superpowers E1; Theme 7 N=2 is verify-retry not debug-fix budget.

### 3.3 Cursor composition (expanded)

| Cursor surface | Role in spine |
|----------------|---------------|
| Debug Mode | Preferred when cause unclear / race / needs runtime logs; human reproduces |
| Terminal | Repro commands, tests, builds; **READ** full output |
| Browser | UI repro; console/network evidence |
| Search/read | Static investigation before/during |
| Checkpoints | Undo thrash during wrong-hypothesis patches |
| MCP (host) | Optional observation (Sentry, Playwright) — teach “use if configured”, don’t ship MCP in Toolbelt |
| Bugbot | Park in PR slice — review ≠ debug method |

### 3.4 Flaky / intermittent (light expand)

- Measure/force nondeterminism (race, time, env) before guessing — community reproduce-my-bug / Dooley sporadic causes.  
- Deep should decide how thin Toolbelt’s flaky protocol is (candidate: short checklist, not a separate skill).

### 3.5 Surface-shape options (for deep brief)

| Option | Shape | Pros | Cons |
|--------|-------|------|------|
| **A. Thin spine skill** | e.g. `systematic-debug` or `investigate-debug` | Matches Superpowers gravity; clear entry | Name collision with Cursor Debug Mode |
| **B. Spine + reproduce companion** | investigate/fix + `reproduce-bug` (never-fix) | Strong evidence culture | Two surfaces |
| **C. Compose-only** | Rules/docs that point at Cursor Debug Mode + Theme 8 verify | Thinnest | Weak discoverability of Toolbelt method |
| **D. Fat Debug+PR pack** | Many skills (CI, Bugbot, git) | Covers stub row | Sprawl; conflicts thin Toolbelt spirit **now** |

- `INFERENCE` [E4] Entering deep lean: **A or B**; **D deferred**; PR/CI as optional Phase 2 track. Premises: Theme 8 thin spirit; packs stub; user ask focuses investigate/reproduce.

### 3.6 Ladder seam (Execute → Debug)

| From | Trigger | Into Debug |
|------|---------|------------|
| Execute `verify-fail` after N=2 | Symptom persists / unknown why | Investigate + reproduce failing Verify |
| Major-deviation / weird runtime | Beyond plan Files | Debug Mode / investigate |
| User reports bug outside plan | Ad-hoc | Full Debug spine |
| Theme 8 post-green Critical | Faithfulness break unclear | Debug before more patches |

Do **not** replace Execute N=2 with Debug’s fix budget.

## 4. Analysis — third normal pass?

| Question | Verdict |
|----------|---------|
| Need more discovery before briefing deep? | **No** — concept map, Cursor E1, community Tier A, RAG corroboration, surface options named |
| Remaining unknowns | Exact skill names, N-fix budget, flaky depth, PR phase scope — **deep-track** |
| Third normal pass | **Done** — see [`scope-normal-pass3-deepen.md`](./scope-normal-pass3-deepen.md) (human-requested deepen) |

## 5. What deep research must cover (input to brief)

1. **T9A** — Method spine (investigate / reproduce / hypothesize / root-cause / fix / verify)  
2. **T9B** — Cursor native composition (Debug Mode, terminal, browser, checkpoints, MCP stance)  
3. **T9C** — Community deepen (systematic-debugging, reproduce-my-bug, bug-investigate-fix, control-ui/cli atoms) → transferable vs park  
4. **T9D** — Surface shape A/B (+ PR Phase 2?) + elevation + wiring from Execute/Verify  

## 6. Implications

- `INFERENCE` [E4] Combine pass 1+2 into Theme 9 deep **campaign brief**; do not elevate from these drafts. Premises: `draft-is-not-sot`.
