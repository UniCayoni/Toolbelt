---
title: "Systematic debug checklist"
status: active
aligned_with: docs/research/reports/theme-9-debug-pocket.md
created: 2026-07-30
---

# Systematic debug — checklist

Authority: Theme 9 accepted. Read from skill `debug-systematic` when running a full session.

## Progress

```text
Debug Progress:
- [ ] 0 Intake (expected vs actual, artifacts, surface)
- [ ] 1 Reproduce same surface (or NOT-YET-REPRODUCED)
- [ ] 1b Flaky path if intermittent (measure → force → rate)
- [ ] 2 Evidence path chosen (Terminal / Browser / Debug Mode / Agent instrument / MCP observe)
- [ ] 3 Hypothesis table (falsifiable; statuses updated)
- [ ] 4 Root cause named (backward trace)
- [ ] 5 Minimal fix applied
- [ ] 6 VERIFY SAME REPRO (evidence kept)
- [ ] 7 Instrumentation cleaned / Checkpoints if thrash
- [ ] 8 Stop if debug-fix-cycles≥3 or architecture → human
```

## Hypothesis table (template)

| # | Hypothesis | If true, we'd see… | Quick test | Status |
|---|------------|-------------------|------------|--------|
| 1 | | | | open \| confirmed \| rejected \| inconclusive |

## Red flags

- No repro and still patching  
- Code-read treated as reproduction  
- Stacked speculative fixes without falsifying  
- Skipping same-repro verify  
- Past `debug-fix-cycles`=3 without escalate  
- Saying “N=2” without qualifying Execute vs Debug budget  

## Compose quick matrix

| Symptom | Prefer |
|---------|--------|
| Clear stack / failing test | Terminal + READ output |
| Unclear / race / perf | Cursor Debug Mode (+ human repro) |
| UI | Browser |
| Edit thrash | Checkpoints |
| Prove-only | `debug-reproduce` |
