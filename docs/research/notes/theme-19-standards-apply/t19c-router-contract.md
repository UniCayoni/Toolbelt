---
title: "T19C — Standards-router contract (normal)"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
depth: normal
authors: [research-gatherer]
---

# T19C — Router contract

**Using `research-protocol`.** Depth: **normal** (deepen with external comps in T19E–G).

## 1. Scope

Classifier inputs, handoff fields, skip rules — family resemblance to impl/debug routers.

## 2. Findings (local pattern transfer)

- `FACT` [E0] `implementation-router`: classify → structured handoff → wire plan → invoke leaves; **selection ≠ solving**; intelligent skip when leaf named. [E0: `skills/implementation-router/SKILL.md`]
- `FACT` [E0] `debug-router`: same family; default one entry leaf; optional wire; refuse ceremony. [E0: `skills/debug-router/SKILL.md`]
- `INFERENCE` [E4] Standards-router should stay **compose-only**: output = module pointers (+ optional bind reminder), not re-authoring standards or running Plan/Execute. Premises: Theme 14 L-rules; campaign brief.
- `INFERENCE` [E4] Candidate classifier dimensions (session lean): **action** (author skill / write research note / implement code / closeout check), **wording** (user phrases), **skill id** in use or about to invoke, **path globs** touched, **perceived intent** (when ambiguous → ask or core-only). Premises: campaign brief; T19B success sketch.
- `INFERENCE` [E4] Handoff fields (family): goal, prior, facts+source, open question, constraints, plus **`standards_modules: [{id, path, reason}]`** and **`catalog_status: absent|draft|accepted`**. Premises: impl-router template pattern [E0 template exists].
- `OPEN` Exact enum of classify labels — design after deep comps / T19I.
- `OPEN` Whether pocket routers call standards-router vs duplicate if-present resolve (T19J later).

## 3. Anti-patterns (proposed)

- Pasting full module bodies into router output  
- Routing to Toolbelt-universal style when host catalog absent  
- Becoming global meta-router for all skills  
