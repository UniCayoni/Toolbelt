---
title: "Toolbelt guide-meta checklist"
status: active
aligned_with:
  - docs/research/reports/theme-22-meta-guide.md
  - docs/research/reports/theme-23-host-playbook.md
created: 2026-08-04
updated: 2026-08-04
---

# Guide-meta checklist

Authority: Theme 22 accepted. Used by skill `guide-meta`.  
**Compose only** — name **one** next surface; do not paste pocket / leaf law here.  
**Not always-on.**

## Classifier

```text
Ask class:
  feature-ladder | research | design | implementation-pocket | debug
  | standards-resolve | standards-author | author-surfaces | closeout
  | leaf-direct | trivial | unclear | out-of-toolbelt
Named skill already?: yes (which) | no
Ambiguity: high | medium | low
```

## Next surface (exactly one)

```text
Next: guide-research | guide-design | guide-implementation | guide-debug
    | guide-standards | implementation-happy-path | author-standards
    | author-cursor-surfaces | implementation-closeout | <named-leaf>
    | none (document skip / out of scope)
Reason (one line):
Smallest sufficient?: yes | no (why larger entry)
```

## Anti-ceremony reminders

```text
- Prefer pocket guide over happy-path unless full feature ladder requested
- Trivial one-file → none / careful edit (not the ladder)
- guide-standards no-op when catalog absent = expected
- Host setup / adopt Toolbelt → docs/host-playbook.md (not pasted into meta)
```

## Structured handoff

```text
Goal (one sentence):
Prior actions / results:
Key facts + where from:
Open question for next skill:
Constraints:
```

## Stop

```text
Do: announce Using guide-meta once; hand off; stop composing
Do not: always-on behavior; PIPELINE of many skills; re-teach pocket spines;
      invent Toolbelt-universal standards; PR/merge ceremony
```
