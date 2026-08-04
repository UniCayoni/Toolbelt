---
title: "Toolbelt guide-standards checklist"
status: active
aligned_with:
  - docs/research/reports/theme-19-standards-apply.md
  - docs/research/reports/theme-21-standards-fanout.md
created: 2026-08-03
updated: 2026-08-04
---

# Guide-standards checklist

Authority: Theme 19 accepted; Theme 21 fan-out callers. Used by skill `guide-standards`.  
**Compose only** — emit **pointers**; do not paste module rule tables here.

## Catalog gate

```text
Catalog path (e.g. docs/standards/index.md): 
Catalog status: absent | draft | proposed | accepted
Accepted modules available?: yes | no
If absent / none accepted → STOP (no-op). Do not invent Toolbelt-universal standards.
```

## Classifier

```text
Action: author-skill | research-note | implement-code | design | plan | closeout | other
Caller pocket guide (if any): guide-research | guide-design | guide-implementation | guide-debug | ambient | explicit
Wording / user phrases:
Skill id in use or next:
Paths touched / likely:
Perceived intent (if ambiguous → ask or core-only):
Pocket lean:
  research/design → principles / method-inclination modules for that pocket
  implementation/debug → technical modules (naming/layout/tests/safety) matching paths
  Do not auto-apply Impl technical modules on research/design entry unless catalog row matches
```

## Structured handoff

```text
Goal (one sentence):
Prior actions / results:
Key facts + where from:
Open question:
Constraints (draft≠SoT; accepted modules only):
standards_catalog: path | absent
standards_modules:
  - id:
    path:
    reason: action | skill | path | wording | core
```

## Wire / load

```text
- [ ] Emit module pointers only (paths)
- [ ] Worker / self loads those files — not the whole catalog corpus
- [ ] Subagent Task: copy standards_modules into prompt
- [ ] Intelligent skip if modules already pinned this turn
```

## Stop

```text
Do not: dump full standards into chat; auto-promote draft/proposed; claim industry SoT for Toolbelt defaults
Hand: Plan/Execute/Closeout bind (Theme 16) | author-standards if authoring needed
```
