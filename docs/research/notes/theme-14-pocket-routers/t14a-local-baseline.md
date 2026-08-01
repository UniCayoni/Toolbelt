---
title: "T14A — Toolbelt local baseline (entry vs orchestrator)"
status: draft
theme: theme-14-pocket-routers
track: T14A
created: 2026-07-31
updated: 2026-07-31
authors: [gatherer]
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
  - docs/research/reports/theme-10-happy-path.md
supersedes: null
---

# T14A — Local baseline

## 1. Scope

- Question: What entry/router-like surfaces does Toolbelt already ship, and what gap remains vs pocket-local routing?
- In scope: Theme 10 happy-path; `research-scope`; `design-process`; Handoffs; packs row for Happy path
- Out of scope: Elevating new router skills

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | Read local skills/reports |
| Corpora / URLs | `skills/implementation-happy-path/SKILL.md`, `skills/research-scope/SKILL.md`, `skills/design-process/SKILL.md`, `docs/research/reports/theme-10-happy-path.md`, `docs/packs/README.md` |
| Queries | Theme 10 D1–D8; compose-only; companion vs spine |
| What was *not* searched | Full Theme 5–9 report re-read |
| Depth | normal |

## 3. Findings

- `FACT` [E0] Theme 10 accepted **shape A**: thin `implementation-happy-path` + checklist; **orchestration only**; do not restate Themes 5–9 pocket law (D8); controller may hold happy-path; workers = one pocket (D6). [E0: `docs/research/reports/theme-10-happy-path.md`]
- `FACT` [E0] Happy-path skill is a **ladder classifier + ordered invoke** of leaf skills; explicitly “compose only”; not a method pocket. [E0: `skills/implementation-happy-path/SKILL.md`]
- `FACT` [E0] `research-scope` is an accepted **companion** (Theme 12): expand/atomize/gate before gather; skip when question clear; usable in any order, not only happy-path. [E0: `skills/research-scope/SKILL.md`]
- `FACT` [E0] `design-process` is the Design pocket **spine/entry**: classify → options → human gate → handoff to plan/execute leaves. [E0: `skills/design-process/SKILL.md`]
- `FACT` [E0] Packs treat Happy path as separate shipped row that “orchestrates pockets (compose only)”. [E0: `docs/packs/README.md`]
- `INFERENCE` [E4] Toolbelt already has **two pocket-shaped routers** (research companion, design spine) + **one cross-pocket pipeline** (happy-path), but **no symmetric router** for Implementation (plan/verify/execute cluster) or Debug (reproduce vs systematic). Premises: (1) E0 facts above; (2) Implementation leaves are multiple skills without a single “classify then wire” front door.
- `GAP` Implementation/Debug pocket-local routing is only in Handoffs tables — not a discoverable entry skill. Searched: live skills list via prior session knowledge + happy-path Handoffs. Result: no `implementation-router` / `debug-router`.
- `OPEN` Whether “router pocket” is a packs umbrella vs renaming/generalizing companions — deferred to T14E / design.

## 4. Conflicts

None local.

## 5. Next

T14B–D comparators → T14E options.
