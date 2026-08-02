---
title: "T15F — Shape options lean (closeout readiness)"
status: accepted
theme: theme-15-closeout-readiness
track: T15F
created: 2026-08-02
updated: 2026-08-02
authors: [integrator-draft]
aligned_with:
  - docs/research/notes/theme-15-closeout-readiness/t15a-local-baseline.md
  - docs/research/notes/theme-15-closeout-readiness/t15b-problem-success.md
  - docs/research/notes/theme-15-closeout-readiness/t15c-dod-analogues.md
  - docs/research/notes/theme-15-closeout-readiness/t15d-evidence-binding.md
---

# T15F — Shape options lean

**Status:** draft lean for human — **not** design law. Premises from T15A–D only.

## Options

| ID | Shape | Pros | Cons / risks |
|----|--------|------|----------------|
| **O1** | Skill + template: help **author/update** host closeout profile + **check** readiness against evidence | Useful; matches DoD/frontier pattern; ceremony stays out | New skill count; needs clear anti-ceremony fence |
| **O2** | Template-only + happy-path pointer (“fill host closeout”) | Minimal surface | Weak agent discoverability; empty-meta risk |
| **O3** | Happy-path Stop rewrite only (longer pointer text) | Tiny delta | Does not help define/check; under-delivers thesis |
| **O4** | Full PR/CI/Bugbot pack (Phase 2 mega) | — | **Reject** — conflicts with accepted product lean + parks |
| **O5** | Global always-on closeout rule | — | **Reject** — Toolbelt thin always-on culture |

## Agent lean (quality-over-ease)

Prefer **O1**:

1. Skill name lean (OPEN until design): e.g. `implementation-closeout` or `closeout-readiness` — domain-first; not `pr-merge`.
2. Two modes in one skill: **define/update profile** | **check readiness** (classifier).
3. Template SoT under `docs/templates/` (host may copy to `docs/closeout/` or repo root — path in design).
4. Profile = criteria slots + evidence locators + N/A/waiver; **no** `gh` merge spine.
5. Happy-path Stop → optional “run closeout-readiness check if host profile exists / user asks”; never force on trivial.
6. Narrow Phase 2: **ceremony/CI/Bugbot automation** still Phase 2 / host; **readiness framing** becomes this theme’s elevate target.
7. Packs: new row or extend Contributor — lean **Closeout readiness** under Implementation/Happy-path adjacent (decide in design).

## Parks

- Merge/approve/push automation  
- Universal PR body as Toolbelt law  
- Always-on rule  
- Bugbot product inside plugin  

## Human gate

**Accepted O1 lean** — 2026-08-02 (human).
