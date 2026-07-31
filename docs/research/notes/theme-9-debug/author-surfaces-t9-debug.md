---
title: "Theme 9 — author-cursor-surfaces elevation note"
status: accepted
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
aligned_with:
  - docs/research/reports/theme-9-debug-pocket.md
  - skills/systematic-debug/SKILL.md
  - skills/reproduce-bug/SKILL.md
supersedes: null
---

# Theme 9 — author-cursor-surfaces

**Using `author-cursor-surfaces`**.

| Field | Value |
|-------|-------|
| Outcome | Elevate Debug pocket per accepted Theme 9 (F1–F10 quality leans) |
| Mode | author + compose (wire Execute/Verify) |
| Scaffold | no (Theme 4 alone) |
| Surfaces | `systematic-debug`, `reproduce-bug`, `docs/templates/repro-light.md` |
| Wire | `implementation-execute`, `-subagents`, `implementation-execute-verify` (+ plan-verify identity wording) |
| Always-on rule | Rejected (F9) |
| Status | Accepted with report; operator sync + Reload remaining |

## Verify

- [x] `name` == folder; pushy descriptions; references gated  
- [x] Paths relative under plugin  
- [ ] Operator: `python scripts/sync-toolbelt-local-plugin.py` + Reload Window  
