---
title: "T14B — Skill-pack router / orchestrator comparators"
status: draft
theme: theme-14-pocket-routers
track: T14B
created: 2026-07-31
updated: 2026-07-31
authors: [gatherer]
aligned_with:
  - docs/research/notes/theme-14-pocket-routers/campaign-brief.md
supersedes: null
---

# T14B — Skill-pack comparators

## 1. Scope

- Question: How do public agent-skill repos express routing vs orchestration vs leaf work?
- In scope: Superpowers entry skill; GitHub code hits for `skill-router` / orchestrator skills
- Out of scope: Importing their packaging/CI as Toolbelt law

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-31 |
| Tools used | GitHub MCP `get_file_contents`, `search_code`; `gh search` |
| Corpora / URLs | `obra/superpowers` `skills/using-superpowers/SKILL.md`; `juew/Skill-Routing-Kit` `skills/skill-router/SKILL.md`; `AndurilCode/craftwork` `skills/skill-router/SKILL.md` |
| Queries | `router OR orchestrat path:skills filename:SKILL.md`; `"happy path" OR orchestrat path:skills` |
| What was *not* searched | Exhaustive catalog of all 6k code hits; agentskills.io full spec re-read |
| Depth | normal |

## 3. Findings

- `FACT` [E1] Superpowers `using-superpowers` is a **global meta-entry**: invoke relevant skills before acting; process skills before implementation skills; workers/subagents told to ignore it. [E1: obra/superpowers — https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md — accessed 2026-07-31]
- `FACT` [E1] `juew/Skill-Routing-Kit` `skill-router` is **routing-assistance only**: diagnose which skill applies; “does not replace … process skills, or subagent orchestration”; explicit **when not to use** when a domain skill is obvious; output = recommended / helper / do-not-use. [E1: https://github.com/juew/Skill-Routing-Kit/blob/main/skills/skill-router/SKILL.md — accessed 2026-07-31]
- `FACT` [E1] `AndurilCode/craftwork` `skill-router` is an **attention-recovery composition layer**: “Does NOT perform tasks — scans, matches, plans”; patterns SINGLE / PIPELINE / PARALLEL→CONVERGE / ORCHESTRATED; skip greetings & mid-execution follow-ups. [E1: https://github.com/AndurilCode/craftwork/blob/main/skills/skill-router/SKILL.md — accessed 2026-07-31]
- `CLAIM` [E3] Multiple community packs use a dedicated **router skill** as meta-layer (discovery + composition plan), separate from leaf executors — discovery via GitHub code search, not a single canonical standard. [E3: GitHub search `filename:SKILL.md` router/orchestrat — accessed 2026-07-31]
- `INFERENCE` [E4] Two router archetypes appear in skill packs: **(A) diagnostic/meta** (which skill?) vs **(B) composition planner** (which pattern + ordered skills). Toolbelt pocket routers lean closer to **scoped B inside one pocket**, not global A. Premises: (1) juew vs craftwork E1; (2) Theme 10 already owns cross-pocket ladder.
- `GAP` No single GitHub “official” skill-routing standard found analogous to Actions `workflow_call`. Searched: code search + Superpowers. Result: community patterns only.
- `OPEN` Whether Toolbelt wants a **global** skill-router (Superpowers-like) in addition to pocket routers — likely **park** (conflicts with description-based discovery + thin always-on rules).

## 4. Conflicts

| Topic | Source A | Source B | Prefer |
|-------|----------|----------|--------|
| Always invoke router | craftwork “Always invoke for new substantive requests” | juew “Do not use when domain skill obvious”; Superpowers forces process skills | Toolbelt lean: **intelligent skip** (juew + Theme 12 skip culture) |

## 5. Next

T14C GitHub Actions analogy; T14D agentic patterns.
