---
title: "Recon: GreyMatter workspace (smoke v3 — before AGENTS.md)"
status: draft
created: 2026-07-28
skill: codebase-recon
smoke: v3
harness_announce: "Using codebase-recon"
purpose: research-before-write gate before author-agents-md
---

# Codebase reconnaissance — GreyMatter (as-needed)

**Using `codebase-recon`.**  
Coexistence: Superpowers may demand a skill first; this task is GreyMatter research/bootstrap — using GreyMatter `codebase-recon` per `research-skill-coexistence` [E0 rule file].

## S0–S2

| Field | Value |
|-------|-------|
| Goal | understand-for-X — enough layout to author `AGENTS.md` without inventing commands |
| Mode | as-needed |
| Scope | `.cursor/`, `docs/research/`; stub deferred |
| Missed-interaction risk | yes — no app/runtime code yet |

## S0 commands [E0]

- Install / Build / Test / Lint: **GAP** — no `package.json`, no root `README.md`, no `AGENTS.md` yet (`python` path check 2026-07-28).

## S6 layout [E0]

- Present: `.cursor/skills` (5), `.cursor/rules` (4 `.mdc`), `docs/research/` (PROTOCOL, templates, reports, notes)
- Absent: `AGENTS.md`, `package.json`, `README.md`, `grey-matter/` plugin stub

## S8–S9

- Locate via Python path-exists (Windows tip). Explore not required (tiny known tree).

## S13

- Graded findings in this short note (either-OK).

## S16

- Gate for **implementation-like** write of root `AGENTS.md`: layout known; commands marked GAP; human smoke requests author skill → proceed to `author-agents-md` with no invented scripts.

### Findings

1. `FACT` [E0] No root `AGENTS.md` — author skill has a real subject.  
2. `FACT` [E0] Research harness lives under `.cursor/skills` + `.cursor/rules` + `docs/research/`.  
3. `GAP` No install/build/test commands in-repo.  
4. `INFERENCE` [E4] `AGENTS.md` must point at research skills/docs and state stub-on-hold; must not invent npm scripts. Premises: (1)(2)(3).
