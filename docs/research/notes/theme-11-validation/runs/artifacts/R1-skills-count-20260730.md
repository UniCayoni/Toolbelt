---
title: "R1 smoke — skill count under Toolbelt/skills"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
authors: [theme-11-pocket-smoke]
supersedes: null
---

# R1 smoke — how many skills in `d:\Toolbelt\skills`?

## 1. Scope

- Question / goal: Count how many skills exist under `d:\Toolbelt\skills` today.
- In scope: Top-level skill directories and presence of `SKILL.md` under each.
- Out of scope: Skill content quality, plugin-local copies, elevation/redesign.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Glob (`**/SKILL.md` under `skills/`); PowerShell `Get-ChildItem` (directories + recursive `SKILL.md` count) |
| Corpora / URLs searched | none |
| Queries (exact) | glob `skills/**/SKILL.md`; list/count dirs under `d:\Toolbelt\skills` |
| What was *not* searched | Plugin install copies (`~/.cursor/plugins/...`); skill body text; marketplace manifests |
| Depth | normal |
| Waves / stop_reason | n/a (normal) |
| Provenance (optional PROV) | Entity=`d:\Toolbelt\skills`; Activity=directory listing + SKILL.md glob; Agent=pocket-smoke runner |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Single filesystem count; no design lock |
| Scope boundary | `d:\Toolbelt\skills/*` only |

## 4. Findings

- `FACT` [E0] There are **19** top-level skill directories under `d:\Toolbelt\skills` as of 2026-07-30. [E0: local listing — `d:\Toolbelt\skills` — observed 2026-07-30]
- `FACT` [E0] There are **19** `SKILL.md` files under `d:\Toolbelt\skills` (one per skill directory). [E0: glob + recursive filter `SKILL.md` — `d:\Toolbelt\skills` — observed 2026-07-30]
- `FACT` [E0] Directory names (sorted): `author-agents-md`, `author-cursor-surfaces`, `codebase-recon`, `creative-narrative-design`, `creative-systems-design`, `creative-world-character-design`, `design-process`, `docs-research`, `draft-adr`, `implementation-execute`, `implementation-execute-subagents`, `implementation-execute-verify`, `implementation-happy-path`, `implementation-plan`, `implementation-plan-verify`, `reproduce-bug`, `research-protocol`, `systematic-debug`, `technical-design`. [E0: `Get-ChildItem -Directory` — `d:\Toolbelt\skills` — observed 2026-07-30]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Skill count equals number of dirs that each contain `SKILL.md` | confirmed | Both counts = 19 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| — | — | — | none |

## 7. Gaps & OPEN

- `OPEN` Whether plugin-local Toolbelt install mirrors this exact set was not checked (out of scope).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Theme 11 R1 smoke purposes, the answer “19 skills” is sufficient. Premises: (1) E0 dir count = 19; (2) E0 `SKILL.md` count = 19.

## 9. Source list (deduped)

1. [E0] Local filesystem: `d:\Toolbelt\skills` (directory listing + `SKILL.md` glob), 2026-07-30
