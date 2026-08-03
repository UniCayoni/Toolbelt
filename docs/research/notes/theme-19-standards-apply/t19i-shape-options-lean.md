---
title: "T19I — Shape options lean (standards apply)"
status: accepted
theme: theme-19-standards-apply
created: 2026-08-03
updated: 2026-08-03
accepted: 2026-08-03
accepted_by: human (Jonathan)
depth: normal
authors: [integrator]
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
  - docs/research/notes/theme-19-standards-apply/t19a-local-baseline.md
  - docs/research/notes/theme-19-standards-apply/t19b-problem-success.md
  - docs/research/notes/theme-19-standards-apply/t19c-router-contract.md
  - docs/research/notes/theme-19-standards-apply/t19d-catalog-modules.md
---

# T19I — Shape options lean

**Using `research-protocol`.** Integrator lean from normal wave — **not SoT until human accepts**.

## Options

| ID | Shape | Pros | Cons |
|----|-------|------|------|
| **O1** | New skill **`standards-router`** + catalog template + thin ambient rule (`alwaysApply: true`, empty/absent no-op) | Matches pocket-router family; author-standards stays author/derive/bind; clear compose | Amends Theme 16 D12; new skill count |
| **O2** | `author-standards` gains mode **`resolve`** (+ same catalog/rule) | Fewer skills | Fat skill; mixes authoring with ambient apply |
| **O3** | Catalog + Plan/Execute bind only (no ambient, no router) | Minimal change | Fails session intent (side-door / selective load) |
| **O4** | Ambient rule embeds / generates full standards | Strong apply | Violates selective-load + thin always-on culture |

## Recommended lean: **O1**

1. **Skill `standards-router`** — classify → `standards_modules[]` pointers; compose-only; intelligent skip if modules already pinned.  
2. **Catalog template** — index + module stubs; one-file profile = single module still valid.  
3. **Ambient gate** — thin always-on rule: if no accepted catalog/modules → **no-op**; else invoke/follow standards-router resolve (do **not** paste module bodies in the rule).  
4. **Amend Theme 16 D12** on elevate: forbid always-on *standards bodies*; allow always-on *resolve gate*.  
5. **Keep** `author-standards` for principles/standards/derive/bind-check.  
6. **D10** remains for Plan/Execute/Closeout; router feeds them pointers.  
7. **Expand later (T19J):** pocket routers get `if present` call into standards-router — not this theme’s elevate must.  
8. **Parks:** global meta-router; writing Toolbelt style content; dual-era schema v2.

## Deep next (after lean accept)

T19E (Cursor/peer ambient patterns), T19F (RAG), T19G (GitHub) under `diminishing_returns_plus_2`; residual T19H subagent handoff.

## Human gate

```text
Accept O1 lean? accepted 2026-08-03
Deep T19E–G: authorized with lean
stop_rule: diminishing_returns_plus_2
```
