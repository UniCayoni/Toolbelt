---
title: Light converge (EOP)
status: active
aligned_with: docs/research/reports/theme-8-verify-gates.md
---

# Light converge (end-of-plan)

Owned by `implementation-execute-verify`. **EOP-only** by default (not after every task).

## Hard rules

1. **Append-only** — new `## Convergence` section + new `### Task C###` blocks; Meta Status sync (S1) allowed.
2. **Forbidden silent rewrites** — Goal; Global constraints; Out of scope; Coverage/File maps; existing Task bodies/IDs/Status; Pre-exec history.
3. **No application code edits** in the converge pass.
4. **Present findings first**, then append only if actionable.
5. **Clean converge** — leave plan byte-for-byte unchanged (no empty Convergence header).
6. Re-runs → `## Convergence 2`, … — never rewrite prior Convergence. Task IDs: continue **global max `C*`** (`C001`, `C002`, …).

## Gap types

| Type | Meaning |
|------|---------|
| `missing` | Promised work absent |
| `partial` | Started / incomplete vs Done-when |
| `contradicts` | Code conflicts with plan/design |
| `unrequested` | Scope creep / bonus not in plan |

## Append shape

```markdown
## Convergence

### Task `C001` — <imperative title>

- [ ] Status: `ready`
- **Objective:**
- **Files:**
- **Interfaces (consumes / produces):**
- **Deps:** (none | prior task ids)
- **Done when:**
- **Verify:** `command` → expected signal
- **Gap type:** missing | partial | contradicts | unrequested
- **Source-ref:** <Goal | Coverage:… | Task:… | design:…>
- **Do-not (task-local):**
```

After append: re-enter `implementation-execute` for new `ready` tasks.
