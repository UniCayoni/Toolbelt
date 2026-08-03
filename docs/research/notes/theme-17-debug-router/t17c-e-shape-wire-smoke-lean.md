---
title: "T17C–E — Shape, wire map, smoke lean"
status: draft
theme: theme-17-debug-router
created: 2026-08-02
depth: normal
---

# T17C–E — Shape / wire / smoke lean

**Draft lean** — not design law until report accept.

## T17C Shape (O1)

| Surface | Spec |
|---------|------|
| Skill | `skills/debug-router/SKILL.md` |
| `disable-model-invocation` | **false** / omit (discoverable) |
| Template | `docs/templates/debug-router.md` → refresh → `references/debug-router-checklist.md` |
| Authority | Theme 17 report (amends Theme 14 D4); leaf law Theme 9 |
| Pattern | Clone `implementation-router`: classify → handoff fields → wire → invoke Using leaf |

## T17D Wire map

| File | Edit |
|------|------|
| `implementation-happy-path` | classifier Bug + step 5 + Handoffs → **`debug-router`** |
| happy-path checklist/template | Debug stage → debug-router |
| `implementation-router` | exit / Handoffs / template → **`debug-router`** |
| Execute / -subagents / execute-verify | keep leaf targets; add “repro-first; use `debug-router` when which Debug path is unclear” |
| `docs/packs/README.md` | Routers row: Debug **`debug-router`** |
| Theme 14 report | note D4 superseded by Theme 17 (in Theme 17 report amends) |

## T17E Smoke plan (ID **R8** or **D1** — lean **R8** `debug-router`)

| Part | Prompt lean | Pass |
|------|-------------|------|
| A | Prove-only → reproduce | Using debug-router; invoke reproduce |
| B | T-VF / fix → systematic | invoke systematic; no Execute N=2 burn |
| C | Negative: open PR | refuse ceremony |
| D | User named debug-reproduce | intelligent skip |

Lane: in-session + fresh (2/2).
