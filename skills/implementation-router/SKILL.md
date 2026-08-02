---
name: implementation-router
description: >-
  Pocket router for Toolbelt Implementation: classify the ask, emit a wire plan
  over plan / plan-verify / execute / execute-subagents / execute-verify with
  explicit skips, then invoke those skills without restating their law. Use when
  implementation-router, which plan or execute skill, wire implementation
  pocket, after design accept before coding, or when choosing execute vs
  subagents vs verify-only. Prefer over inventing ad-hoc Implementation skill
  order. Not for writing plans or executing tasks itself.
---

# Implementation router

Announce once: **Using `implementation-router`**.

Authority: Theme 14 accepted (`docs/research/reports/theme-14-pocket-routers.md`).  
**Compose only** — Plan / Execute / Verify SoT stays in Themes 6–8 skills.  
**Draft ≠ law** (`draft-is-not-sot`).  
**Selection ≠ solving** — this skill routes; leaves do the work.

## When to use

- After design (or documented skip) when Implementation wiring is unclear
- Choosing among plan / plan-verify / execute / -subagents / execute-verify
- Controller wants pocket-local routing without the full happy-path
- User asks which Implementation skill to run next

**Skip** (document): user already named a single leaf and scope is clear — invoke that leaf directly.

**Out of scope:** Re-teaching Plan/Execute/Verify spines; task decomposition (that is `implementation-plan`); Debug method law; PR/CI; global skill discovery meta-router.

## Instructions

1. **Classify** impl ask: `full-ladder` | `plan-only` | `plan+verify` | `execute` | `execute-subagents` | `execute-verify` | `resume-blocked` | `trivial-skip`.
2. **Preconditions** — design/ADR accepted paths, or documented Design skip / trivial exception. Do not treat draft design as law.
3. **Structured handoff** — fill goal, prior actions, facts+source, open question, constraints (see template).
4. **Wire plan** — ordered leaves + explicit N/A skips. Default feature path:
   - `implementation-plan` → `implementation-plan-verify` → `implementation-execute` **or** `implementation-execute-subagents` → `implementation-execute-verify` (non-trivial / EOP).
5. **Invoke** each selected leaf: announce **Using `<skill>`** and follow that skill. Do **not** paste its spine here.
6. **On leaf exit** — if `blocked` / verify-fail / unclear Critical → hand off `debug-reproduce` and/or `debug-systematic` (Debug router deferred; use leaves). If design was wrong → return toward `design-process` / happy-path classify — do not invent requirements.
7. **Stop** — summarize wire outcome for human or for `implementation-happy-path` next stage.

Read `references/implementation-router-checklist.md` **when** running a non-trivial wire or recovering mid-pocket.  
Template SoT: Toolbelt `docs/templates/implementation-router.md`.

## Classifier hints

| Signal | Lean |
|--------|------|
| No durable plan; non-trivial | plan → plan-verify → execute… |
| Plan exists; Meta not ready | plan-verify (fix plan if needed) |
| Meta `ready`; single worker | execute |
| Multi-task / fresh agents | execute-subagents |
| Greens done; EOP / converge | execute-verify |
| One-file trivial | document trivial-skip; careful edit without durable plan |
| Bug / verify-fail dominant | leave Implementation; Debug leaves |

## Anti-patterns

- Restating Theme 6–8 pocket law in this skill  
- Becoming a second `implementation-plan` (decomposing tasks here)  
- Mandatory full ladder when user asked verify-only or execute-only  
- Always-on / global skill meta-router behavior  
- Giving a worker this router **and** expecting them to implement — workers get **one leaf**  
- Silent skips of human design accept or Meta `ready` without documenting exception  

## Handoffs

| Need | Use |
|------|-----|
| Full Toolbelt ladder | `implementation-happy-path` |
| Design not accepted | `design-process` |
| Plan / verify / execute leaves | `implementation-plan` → `implementation-plan-verify` → `implementation-execute` (+ `-subagents`, `-verify`) |
| Bug / root cause | `debug-reproduce` / `debug-systematic` |
| Research unclear | `research-scope` / research leaves |
| Closeout readiness | `implementation-closeout` |
| Author surfaces | `author-cursor-surfaces` |

## References

- Read `references/implementation-router-checklist.md` **when** wiring a session
- SoT template: Toolbelt `docs/templates/implementation-router.md`
- Theme 14: Toolbelt `docs/research/reports/theme-14-pocket-routers.md` (accepted)
- Leaf law: Themes 6–8 accepted reports (via their skills)
