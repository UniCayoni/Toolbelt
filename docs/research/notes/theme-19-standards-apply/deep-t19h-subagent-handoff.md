---
title: "Deep T19H — Subagent / Task standards module handoff"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
depth: deep
track: T19H
---

# Deep T19H — Subagent handoff (light residual)

**Using `research-protocol`.** Depth: **deep** (light residual).

## 1. Scope

How parent vs subagent should receive module pointers.

## 2. Findings

- `FACT` [E0] Theme 14 / impl-router / debug-router use structured handoff fields (goal, prior, facts+source, open question, constraints) — not full leaf spines. [E0: `skills/implementation-router/SKILL.md`, `skills/debug-router/SKILL.md`]
- `FACT` [E2] Context Engineering multi-agent pattern: Orchestrator packages Librarian style-guide result + Researcher facts for Writer — child gets **selected** context, not whole library. [E2: T19F chunk_ids `d51865d1ce28efb07216b934`, `07fcd3699bc730f7b2bf0b28`]
- `INFERENCE` [E4] O1 handoff lean: parent runs standards-router (or ambient gate triggers it) → pass `standards_modules[{id,path,reason}]` into Task/subagent prompt; child **loads those paths** and does not re-dump catalog unless modules missing / `GAP`. Premises: E0 router family; E2 orchestrator packaging; O1.
- `INFERENCE` [E4] If child is a fresh agent with no modules in prompt → re-resolve via standards-router (idempotent) rather than invent. Premises: selective-load; draft≠SoT.
- `GAP` Cursor plugin `agents/` Task-type wire still Theme 4 GAP — do not lock plugin-agent packaging. [E0: Theme 4 report prior]
- `stop_reason` Named T19H atoms closed from local + T19F transfer; no further primary API for Task standards fields.

## 3. Proposed handoff field (design later)

```text
standards_catalog: path | absent
standards_modules:
  - id: …
    path: …
    reason: action|skill|path|wording
```
