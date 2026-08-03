---
title: "Smoke T16 — derive candidates (proposed)"
status: proposed
smoke: S1
created: 2026-08-02
---

# Derive candidates (proposed only)

**Using `author-standards`** mode `derive`.  
**Not accepted.** Do not elevate. Signals from Toolbelt E0 only.

| ID | Candidate | Signal | Confidence |
|----|-----------|--------|------------|
| D1 | Skill folders use kebab-case matching `name` FM | `skills/*/SKILL.md` pattern | high |
| D2 | Research notes use FACT/CLAIM/GAP labels | `docs/PROTOCOL.md` + always-on grades rule | high |
| D3 | Prefer templates under `docs/templates/` + refresh to skill refs | `scripts/refresh-skill-references.py` | high |

## Dual-era / quarantine

```text
None for smoke. No .git-blame-ignore-revs requirement asserted.
```

## Next

Human accept → merge into standards profile; until then **proposed** only.
