---
name: guide-implementation
description: >-
  Pocket guide for Toolbelt Implementation (formerly implementation-router):
  classify the ask, emit a wire plan over plan / plan-verify / execute /
  execute-subagents / execute-verify with explicit skips, then invoke those
  skills without restating their law. Use when guide-implementation,
  implementation-router, which plan or execute skill, wire implementation
  pocket, after design accept before coding, or when choosing execute vs
  subagents vs verify-only. Prefer over inventing ad-hoc Implementation skill
  order. Not for writing plans or executing tasks itself.
---

# Guide implementation

Announce once: **Using `guide-implementation`**.

Authority: Theme 14 accepted (`docs/research/reports/theme-14-pocket-routers.md`);  
Theme 21 fan-out (`docs/research/reports/theme-21-standards-fanout.md`).  
**Compose only** — Plan / Execute / Verify SoT stays in Themes 6–8 skills.  
**Draft ≠ law** (`draft-is-not-sot`).  
**Selection ≠ solving** — this skill guides; leaves do the work.

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
3. **Standards resolve (if-present)** — Theme 21:
   - If `standards_modules` already pinned this turn → **skip** (document).
   - Else if accepted host catalog → **Using `guide-standards`**; emit pointers for **Implementation** (technical modules matching paths/skills); attach to handoff. Do not paste module bodies.
   - Else → **no-op** (document). Do not invent Toolbelt-universal standards.
4. **Structured handoff** — fill goal, prior actions, facts+source, open question, constraints, plus `standards_catalog` / `standards_modules` (see template).
5. **Wire plan** — ordered leaves + explicit N/A skips. Default feature path:
   - `implementation-plan` → `implementation-plan-verify` → `implementation-execute` **or** `implementation-execute-subagents` → `implementation-execute-verify` (non-trivial / EOP).
6. **Invoke** each selected leaf: announce **Using `<skill>`** and follow that skill; pass `standards_modules` into Task prompts when present. Do **not** paste leaf spines here.
7. **On leaf exit** — if `blocked` / verify-fail / unclear Critical → hand off **`guide-debug`**. If design was wrong → return toward `guide-design` / happy-path classify — do not invent requirements.
8. **Stop** — summarize wire outcome for human or for `implementation-happy-path` next stage.

Read `references/guide-implementation-checklist.md` **when** running a non-trivial wire or recovering mid-pocket.  
Template SoT: Toolbelt `docs/templates/guide-implementation.md`.

## Classifier hints

| Signal | Lean |
|--------|------|
| No durable plan; non-trivial | plan → plan-verify → execute… |
| Plan exists; Meta not ready | plan-verify (fix plan if needed) |
| Meta `ready`; single worker | execute |
| Multi-task / fresh agents | execute-subagents |
| Greens done; EOP / converge | execute-verify |
| One-file trivial | document trivial-skip; careful edit without durable plan |
| Bug / verify-fail dominant | leave Implementation; **`guide-debug`** |

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
| Design not accepted | `guide-design` |
| Plan / verify / execute leaves | `implementation-plan` → `implementation-plan-verify` → `implementation-execute` (+ `-subagents`, `-verify`) |
| Debug pocket | **`guide-debug`** |
| Research unclear | `guide-research` / research leaves |
| Closeout readiness | `implementation-closeout` |
| Which standards modules apply | **`guide-standards`** (if-present; Theme 21) |
| Host principles / standards authoring | `author-standards` |
| Author surfaces | `author-cursor-surfaces` |

## References

- Read `references/guide-implementation-checklist.md` **when** wiring a session
- SoT template: Toolbelt `docs/templates/guide-implementation.md`
- Theme 14: Toolbelt `docs/research/reports/theme-14-pocket-routers.md` (accepted)
- Theme 21: Toolbelt `docs/research/reports/theme-21-standards-fanout.md` (accepted)
- Leaf law: Themes 6–8 accepted reports (via their skills)
