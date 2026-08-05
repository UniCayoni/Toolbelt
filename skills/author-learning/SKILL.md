---
name: author-learning
description: >-
  Quality-gated harvest of workspace learnings into proposed host feedstock
  (host skills, standards/principles, AGENTS pointers, ADRs). Use when
  author-learning, learn from this session, harvest learnings, capture friction
  into standards, post-closeout lessons, continual improvement for this
  workspace, or promote session evidence to host skills. Explicit / invoke.
  Prefer over vibes-as-standards or auto-updating AGENTS/skills. Not for
  rewriting Toolbelt plugin skills. Never auto-accept.
disable-model-invocation: true
---

# Author learning

Announce once: **Using `author-learning`**.

Explicit skill (`/author-learning`). **Quality-gated harvest** — not a convenience router.  
Authority: Theme 24 accepted (`docs/research/reports/theme-24-author-learning.md`).  
**Draft ≠ law** (`draft-is-not-sot`). Ease is a side effect of a clean method, not the goal.  
**Compose** into existing author skills after human accept — do not invent a parallel law body.

## When to use

- Explicit ask to harvest lessons into **host** skills / standards / AGENTS / ADR
- After non-trivial `implementation-closeout` **when** citable friction or lessons exist
- User wants workspace continual improvement with evidence discipline

**Skip** (document): trivial edit with nothing durable to cite; pure chat with no locator; user only wants ceremony.  
**Skip:** rewriting Toolbelt plugin `skills/*` — out of theme; use contributor path / `author-cursor-surfaces` on the plugin only when that is the agreed job (not this skill’s default target).

**Out of scope:** Auto-accept / silent SoT; always-on harvest; Memories as standards law; PR/CI ceremony; Brain/RAG product; act-by-default promotion.

## Intent

Keep only learnings that survive **evidence + guideline-quality** floors, then stage as **proposed**. Human accept is the **last** gate, not the only gate.

## Instructions

1. **Confirm trigger** — explicit `/` or evidence-warranted closeout (citable friction). Refuse ambient “learn everything.”
2. **Bound target** — host/workspace paths only (host `.cursor/skills`, `docs/standards/`, `AGENTS.md`, host ADRs). Refuse Toolbelt plugin `skills/*` as the learning target.
3. **Harvest** candidate scraps with locators (paths, commands+signals, accept records, run notes). Prefer recurrence / corroboration over one-shot anecdote.
4. **Quality gate first** — for each candidate, apply checklist §1. **U / no locator → do not propose** (park or refuse with reason).
5. **Emit only qualified** candidates as `proposed` (checklist §2 atoms). Park/refuse the rest explicitly.
6. **Human accept** — present qualified proposals; accept / reject / edit. Do **not** write durable SoT in this step.
7. **Compose after accept** — hand off:
   - principles/standards → **`author-standards`**
   - AGENTS pointer → **`author-agents-md`**
   - host skill/rule/hook → **`author-cursor-surfaces`** (host path)
   - architecture/process lock → **`research-draft-adr`**  
   Announce **Using `<skill>`**; do not paste those spines here.
8. **Stop** — no auto-promote; no stop-hook SoT loops from this skill.

Read `references/author-learning.md` **when** running a full harvest or multi-candidate session.  
SoT template: Toolbelt `docs/templates/author-learning.md`.

## Anti-patterns

- Identity = “make standards updates easy”  
- Router that skips the quality gate  
- Proposing uncited or grade-U items for a human rubber-stamp  
- Auto-accept / act-by-default  
- Dumping learnings into `alwaysApply` rules or Memories-as-law  
- Targeting Toolbelt plugin skills as the continual-learning surface  
- Always-on harvest every chat  

## Handoffs

| Need | Use |
|------|-----|
| Write/derive host standards | **`author-standards`** |
| AGENTS.md | **`author-agents-md`** |
| Host Cursor skill/rule/hook | **`author-cursor-surfaces`** |
| ADR | **`research-draft-adr`** |
| Closeout readiness check | `implementation-closeout` |
| Which standards apply (load) | `guide-standards` |
| Fuzzy which Toolbelt skill | `guide-meta` |

## References

- Read `references/author-learning.md` **when** harvesting or gating candidates (checklist §0–§5)
- SoT template: Toolbelt `docs/templates/author-learning.md`
- Theme 24: Toolbelt `docs/research/reports/theme-24-author-learning.md` (accepted)
- Related: `author-standards`, `author-agents-md`, `author-cursor-surfaces`, `implementation-closeout`
