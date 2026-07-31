---
title: "Reproduce-bug checklist"
status: active
aligned_with: docs/research/reports/theme-9-debug-pocket.md
created: 2026-07-30
---

# Reproduce-bug — checklist

Authority: Theme 9 accepted. Read from skill `reproduce-bug` when running a full prove session.

```text
Repro Progress:
- [ ] Intake
- [ ] Evidence sweep (read-only)
- [ ] Path trace (enough to aim)
- [ ] Reproduce on same surface (must fail)
- [ ] Minimize to load-bearing steps
- [ ] Flaky: measure → force → rate / not-yet (if needed)
- [ ] Light dossier 8 fields written
- [ ] Status honesty self-check
- [ ] Handoff to systematic-debug / fixer (no product patch here)
```

## Quality bar

- Fixer can run the repro in under a minute when deterministic  
- Attempt #0 records runnability  
- Ledger is append-only  
- Status never oversells  
