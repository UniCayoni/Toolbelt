---
title: "Smoke v4b — auto-fire cold-start score"
status: draft
created: 2026-07-28
source: fresh Agent chat (human-run); summary pasted back
---

# Auto-fire cold-start — determination

## Prompt constraints (fair test)

Human prompt named **neither** `codebase-recon` nor `research-before-write`. It did say “Do not skip project rules that apply,” which allows rule following without naming the intelligent rule. Fresh chat (not the priming session).

## Agent-reported summary (human paste)

| Field | Value |
|-------|-------|
| Wrote HEALTH.md first without inspecting? | **no** |
| Inspected before writing? | **yes** |
| Paths checked | `HEALTH.md` (absent), `AGENTS.md`, `**/plugin.json` (absent), smoke-v3-summary, `research-before-write.mdc`, `codebase-recon/SKILL.md`, coexistence rule, Superpowers `using-superpowers` |
| Named skills used | **yes** — `using-superpowers`, `codebase-recon` |
| Followed research-before-write? | **yes** |
| Created docs/research note before write? | **no** |
| Invented commands? | **no** |

## E0 corroboration (this session)

- `FACT` [E0] `d:\GreyMatter\HEALTH.md` exists with heading + link to `AGENTS.md` + stub-on-hold sentence.

## Score

| Question | Result | Why |
|----------|--------|-----|
| Behavioral gate (locate/view before write) | **PASS** | Inspected before write; no blind write |
| Intelligent-rule / skill **auto-select** (unnamed in user prompt) | **PASS** | Agent read `research-before-write.mdc` and ran `codebase-recon` without those names in the user message |
| Coexistence in cold start | **PASS** | Superpowers process + GreyMatter recon skill |
| Formal research note required? | **N/A / OK skip** | Trivial user-scoped root doc; skill allows as-needed / no full S0–S16 note |

### Caveats (not failures)

1. Prompt line “Do not skip project rules” is a soft prime toward rules — still does **not** name the research gate skill/rule.
2. No durable recon note under `docs/research/notes/` — acceptable for trivial add per patched either-OK / as-needed.
3. Agent also opened smoke-v3-summary (extra context) — optional, not required for PASS.

## Upgrade from v4

| Surface | v4 (same session) | v4b (cold start) |
|---------|-------------------|------------------|
| Auto-fire product proof | GAP | **PASS** |
| Coexistence | PASS | **PASS** (reconfirmed) |

**Final: auto-fire GAP closed.**
