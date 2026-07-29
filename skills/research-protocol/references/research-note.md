---
title: "{short descriptive title}"
status: draft  # draft | proposed | accepted | superseded
theme: ""  # e.g. theme-1 | theme-2 | greymatter-priming
created: YYYY-MM-DD
updated: YYYY-MM-DD
authors: []
supersedes: null
---

# {Title}

## 1. Scope

- Question / goal:
- In scope:
- Out of scope:
- Comprehension / research goal type (if code):  # adaptive | perfective | corrective | reuse | other — see PC literature via theme-1 report

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | YYYY-MM-DD |
| Tools used |  # MCP, WebFetch, shell, etc. |
| Corpora / URLs searched |  |
| Queries (exact) |  |
| What was *not* searched |  |
| Depth | normal \| deep  # default normal; see research-depth-modes.md |
| Waves / stop_reason |  # deep only |
| Provenance (optional PROV) |  # Entity←sources; Activity=this query; Agent=tools/human |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic \| as-needed \| hybrid |
| Why this mode |  |
| Scope boundary |  # packages/dirs/files included/excluded |

## 4. Findings

Use one bullet per claim. **Every non-trivial claim needs a label + grade + citation.**

Format:

```text
- `FACT` [E1] … [E1: Title — URL — accessed YYYY-MM-DD]
- `CLAIM` [E2] … [E2: Alexandria corpus=`…` source=`…` chunk_id=`…` query=`…`]
- `INFERENCE` [E4] … Premises: (1)… (2)…
- `GAP` … Searched: … Result: not found / weak
- `OPEN` … Follow-up needed:
```

Evidence grades: E0 local observation · E1 primary · E2 secondary · E3 community · E4 inference · U unverified (do not use U to lock design).

## 5. Hypothesis log (optional but recommended for code)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 |  | open \| confirmed \| rejected \| revised |  |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
|  |  |  | Prefer higher grade; else leave OPEN |

## 7. Gaps & OPEN

- 

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] …

## 9. Source list (deduped)

1. 
