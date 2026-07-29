---
title: "Recon: GreyMatter before CONTRIBUTING.md (smoke v4 coexistence)"
status: draft
created: 2026-07-28
skill: codebase-recon
smoke: v4
harness_announce: "Using codebase-recon"
superpowers_announce: "Using superpowers:using-superpowers"
---

# Codebase recon (as-needed) — before CONTRIBUTING.md

**Using `superpowers:using-superpowers`** — relevant skills: GreyMatter `codebase-recon` (research artifact), later `verification-before-completion` before pass claims.  
**Using `codebase-recon`** — fill grades; do not invent paths.

## Goal

Enough layout to add root `CONTRIBUTING.md` pointing at existing E0 files only.

## S0–S2

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Scope | root docs pointers; no package ecosystem |
| Risk | yes — no app code |

## E0 locate (Python path-exists)

| Path | Exists |
|------|--------|
| `AGENTS.md` | yes (v3) |
| `docs/research/README.md` | yes |
| `docs/research/PROTOCOL.md` | yes |
| `docs/adr/0001-soft-explore-before-edit.md` | yes |
| `CONTRIBUTING.md` | **no** (pre-write) |
| `package.json` | no |

## S16

Research notes OK. Implementation write of `CONTRIBUTING.md` allowed after this pin — content = links to E0 paths only.

### Findings

1. `FACT` [E0] `AGENTS.md` + research README exist; `CONTRIBUTING.md` absent.  
2. `INFERENCE` [E4] Safe CONTRIBUTING body is pointers only. Premises: (1); no invent commands.
