---
title: "Theme 16 — Deep campaign board"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
---

# Theme 16 deep campaign board

**Using `research-protocol`**.  
**depth:** deep  
**Scope / O1 lean:** accepted 2026-08-02  
**Normal wave:** complete (`normal-wave-summary-20260802.md`)

## Campaign-specific stop rule (human)

Default Toolbelt deep stop = diminishing returns (first restating wave).  
**This campaign:** **+2** — require **two successive** residual/corroboration passes that fail to close named P0/P1 GAPs (or only restate FACTS) before halt. Prefer confirmed GAP over weak E3 spam.

```text
stop_rule: diminishing_returns_plus_2
```

## Named GAPs to close (from normal)

| ID | GAP / OPEN | Track | Priority | Status |
|----|------------|-------|----------|--------|
| G1 | Agent-readable principles exemplars (primary) | T16C | P0 | **mostly closed** — `deep-t16c-principles-exemplars.md` (agent-only PRINCIPLES genre thin) |
| G2 | Broader typology + exemplars (primary style guides) | T16D/F | P0 | **mostly closed** — `deep-t16d-f-typology-exemplars.md` |
| G3 | Git/history recency recipe for brownfield | T16I | P0 | **mostly closed** — deep H/I + git-era primary (N-month default still GAP) |
| G4 | GitHub pack / STANDARDS.md / PRINCIPLES.md sampling | T16F/C | P0 | **mostly closed** (STANDARDS); PRINCIPLES on T16C |
| G5 | Anatomy templates from real host docs | T16E | P1 | **partial** — anatomy in T16D/F deep |
| G6 | Bind patterns in agent skill packs (AGENTS/CLAUDE load) | T16J | P1 | **mostly closed** — `deep-t16j-bind-patterns.md` (precedence/wire slots OPEN) |
| G7 | Evolution / deprecate / obsolete guidance patterns | T16H | P1 | **mostly closed** — ADR/Obsolete/changelog patterns in H/I deep |
| G8 | Conflict: two eras of style in one repo | T16I | P0 | **mostly closed** — dual-era + blame-ignore recipe (E4) |

## Waves

| Wave | Focus | Status |
|------|-------|--------|
| W0 | Pin (this board) | done |
| W1 | Primary + high-signal SoT per thin track | **done** (C/D-F/H-I/J) |
| W2 | Corroboration RAG/web/gh | **partial done** (`deep-w2-corroboration-rag-gh.md`) |
| W2b | Git era primary (G3/G8) | **done** (`deep-t16i-git-era-primary.md`) |
| W3 | Residual GAP closers | **done** — `deep-w3-residual-gaps.md` ([W3 gaps](66802294-16e6-40d4-83ed-2a80b5d6f23f)) |
| W3+1 | Extra residual (+1 of +2) | **done** — `deep-w3p1-residual-confirmed-gaps.md` ([W3+1](2d539357-1472-4264-8ad5-9eb1e5c8f471)); diminishing=false |
| W3+2 | Extra residual | **done** — `deep-w3p2-residual-last-gaps.md` ([W3+2](656e25d9-51ce-480d-ab12-399643eb0bb1)); **diminishing=true** (1/2) |
| W3+3 | Second successive diminishing pass (+2 of +2) | **done** — `deep-w3p3-final-diminishing.md` ([W3+3](6b8eacde-e777-4ca7-af75-56ce8d6e0183)); diminishing=true (2/2) |
| Stop | `diminishing_returns_plus_2` | **halted** — two successive diminishing passes |
| Integrate | Draft Theme 16 report | **done (draft)** — `docs/research/reports/theme-16-host-standards.md` |

## W1 gatherers (parallel)

| Track | Agent | Note target | Status |
|-------|-------|-------------|--------|
| T16C | [Principles](3daaed3c-8691-47d7-87ae-b4f22a714a74) | `deep-t16c-principles-exemplars.md` | **done** |
| T16D/F | [Typology](90190643-8b72-4cc3-98a6-1bf54c3e8cd5) | `deep-t16d-f-typology-exemplars.md` | **done** |
| T16H/I | [Brownfield](f8e2f118-6b23-4d61-8a1e-d1d2fa92526b) | `deep-t16h-i-brownfield-git.md` | **done** |
| T16J | [Bind](30cbdd32-6010-46bc-a73f-0d8a4edfc74d) | `deep-t16j-bind-patterns.md` | **done** |

## Progress log

- 2026-08-02: Deep authorized; stop_rule = diminishing_returns_plus_2
- 2026-08-02: O1 lean marked accepted; W1×4 dispatched; W2 RAG/gh + git primary written
- 2026-08-02: W1 T16D/F landed — G2/G4 mostly closed; residual a11y/i18n + CONTRIBUTING corpus parked for W3 if still P1
- 2026-08-02: W1 T16H/I landed — G3/G7/G8 mostly closed; residual: normative N-month window, recon+history wiring, Feathers primary
- 2026-08-02: W1 T16J landed — G6 mostly closed; residual: AGENTS precedence, Plan/Execute wire slots, T16K packaging
- 2026-08-02: W1 T16C landed — G1 mostly closed; W1 complete → start W3 residual (+2 stop rule)
- 2026-08-02: W3 closed agent PRINCIPLES exemplars + CONTRIBUTING→style + Mozilla a11y; confirmed GAP: conflict stack, Feathers deprecate, Cursor AGENTS precedence; W3+1 started
- 2026-08-02: W3+1 closed CONTRIBUTING→PRINCIPLES + deprecate lifecycle; still GAP: conflict stack, Cursor AGENTS precedence; W3+2 started
- 2026-08-02: W3+2 diminishing=true — both residuals stay CONFIRMED GAP; W3+3 = second successive diminishing pass then halt
- 2026-08-02: W3+3 diminishing=true — **STOP**; draft integrated report written; await human accept before elevate
