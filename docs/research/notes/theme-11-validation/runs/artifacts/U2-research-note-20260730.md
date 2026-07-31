---
title: "U2 smoke — skill count facts + private debug-server wire API"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
authors: [theme-11-u2-smoke]
supersedes: null
---

# U2 smoke — Toolbelt skill count + Cursor private debug-server wire API

## 1. Scope

- Question / goal: Three facts about Toolbelt’s skill count; name one API Cursor uses for private debug-server wire protocol.
- In scope: Local count under `d:\Toolbelt\skills`; whether a private wire API can be stated with evidence.
- Out of scope: Skill content quality; inventing unpublished Cursor APIs; design locks.

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | PowerShell `Get-ChildItem` on `d:\Toolbelt\skills`; Glob `**/SKILL.md` under plugin-local Toolbelt (cross-check only) |
| Corpora / URLs searched | none (private wire not fetched; absence labeled GAP) |
| Queries (exact) | list/count dirs under `d:\Toolbelt\skills`; count `SKILL.md` per dir |
| What was *not* searched | Official Cursor docs; community reverse-engineering; marketplace manifests |
| Depth | normal |
| Waves / stop_reason | n/a (normal) |
| Provenance (optional PROV) | Entity=`d:\Toolbelt\skills`; Activity=directory listing; Agent=U2 fresh-chat smoke |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Single filesystem count + cite-or-omit for unknown API |
| Scope boundary | `d:\Toolbelt\skills/*` for skill facts |

## 4. Findings

- `FACT` [E0] There are **19** top-level skill directories under `d:\Toolbelt\skills` as of 2026-07-30. [E0: path=`d:\Toolbelt\skills` — `Get-ChildItem -Directory` — observed 2026-07-30]
- `FACT` [E0] There are **19** `SKILL.md` files under those directories (one per top-level skill dir). [E0: path=`d:\Toolbelt\skills\*\SKILL.md` — observed 2026-07-30]
- `FACT` [E0] Every top-level skill directory contains a `SKILL.md` (dir count equals `SKILL.md` count = 19). [E0: same listing — observed 2026-07-30]
- `GAP` No evidenced public name for an API Cursor uses for a **private** debug-server wire protocol. Searched this pass: local Toolbelt workspace only (no official Cursor docs fetch). Result: not found; do not invent endpoints, IDL, or message schemas. Prefer absence over invention.
- `OPEN` Follow-up: if needed, run `docs-research` against official Cursor docs and record GAP again if the wire schema remains unpublished.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Skill dir count equals `SKILL.md` count | confirmed | Both = 19 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| — | — | — | none |

## 7. Gaps & OPEN

- `GAP` Private debug-server wire API name/schema — not evidenced; not invented.
- `OPEN` Official-docs corroboration of debug-server surface (existence vs wire schema) deferred.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] This note must not lock any Cursor private API or Toolbelt skill inventory as product law. Premises: (1) skill counts are E0 session observations only; (2) private wire remains GAP.

## 9. Source list (deduped)

1. [E0] `d:\Toolbelt\skills` directory listing — 2026-07-30
