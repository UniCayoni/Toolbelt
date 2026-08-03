---
name: implementation-closeout
description: >-
  Help define or check host closeout readiness via implementation-closeout:
  author/update a host-owned closeout profile and score criteria against cited
  evidence without owning git commit, push, PR, approve, or merge ceremony.
  Use when implementation-closeout, closeout, ship-ready, definition of done,
  ready to hand off, ready for PR check, closeout profile, or after
  execute-verify before human ship. Prefer over inventing a universal merge
  checklist or running gh merge as Toolbelt law.
---

# Implementation closeout

Announce once: **Using `implementation-closeout`**.

Authority: Theme 15 accepted (`docs/research/reports/theme-15-closeout-readiness.md`).  
**Readiness framing** — not PR/CI/Bugbot ceremony. **Draft ≠ law** (`draft-is-not-sot`).

## When to use

- Host needs a durable **closeout profile** (Definition-of-Done-style criteria)
- After non-trivial work: check “done enough to leave the Toolbelt ladder?”
- User asks ship-ready / ready for PR **check** (evidence), not “open the PR for me”
- Happy-path Stop when a profile exists or user requests closeout

**Skip** (document): trivial one-file tweak with no host profile requirement; or user only wants ceremony (`gh`/merge) → hand human / host CONTRIBUTING.

**Out of scope:** commit, push, create/approve/merge PRs, choose squash vs merge, run org CI as Toolbelt law, always-on rule.

## Instructions

1. **Classify mode:** `define-update` | `check`.
2. **Profile path** — prefer existing host file (e.g. `docs/closeout/closeout-profile.md`); else copy SoT template `docs/templates/closeout-profile.md` (or skill `references/closeout-profile.md`) into the host path the user agrees.
3. **Define/update mode**
   - Elicit host requirements (what must be true to ship/hand off).
   - Seed Toolbelt-default slots (design accept, plan Meta ready, verify, draft≠SoT, secrets; optional host standards/principles) — host may mark N/A or add rows.
   - Ceremony = optional human note only (“follow CONTRIBUTING”), never executable merge spine.
4. **Check mode**
   - Load profile; for each **required** criterion set `ready` | `blocked` | `waived` | `n/a`.
   - Every non-N/A needs an **evidence locator** (path, command+signal, accept record, run log) or explicit waiver (who/why/date).
   - **Do not invent greens.** Unproven → `blocked` or list under “NOT verified”.
   - Emit overall verdict + gaps; if `ready`, hand **human** for host ceremony.
5. **Stop** — do not open PRs or push from this skill.

Read `references/closeout-readiness-checklist.md` **when** running a full define or check session.  
Profile SoT template: Toolbelt `docs/templates/closeout-profile.md`.

## Verdict vocabulary

| Verdict | Meaning |
|---------|---------|
| `ready` | Required criteria satisfied with locators (or valid N/A) |
| `blocked` | Missing evidence or unmet criterion |
| `waived` | Host documented exception (who/why/date) |
| `n/a` | Criterion not applicable; reason recorded |

## Anti-patterns

- Becoming a PR/merge/push orchestrator  
- Universal Toolbelt PR body as law for all hosts  
- Claiming `ready` without locators  
- Treating draft research/design/plan as SoT evidence of accept  
- Forcing closeout on every trivial edit  
- Always-on rule  

## Handoffs

| Need | Use |
|------|-----|
| Full ladder | `implementation-happy-path` |
| Implementation wire | `implementation-router` |
| Missing design/plan/verify | respective leaf skills |
| Host principles / standards feedstock | **`author-standards`** |
| Method authoring | `author-cursor-surfaces` |
| GitHub ceremony | **Host / human** — not this skill |

## References

- Read `references/closeout-readiness-checklist.md` **when** defining or checking
- Read `references/closeout-profile.md` **when** creating/updating a host profile (SoT: `docs/templates/closeout-profile.md`)
- Theme 15: Toolbelt `docs/research/reports/theme-15-closeout-readiness.md` (accepted)
