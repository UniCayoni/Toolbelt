---
title: "T17A — Local baseline (Debug handoff call sites)"
status: draft
theme: theme-17-debug-router
track: T17A
created: 2026-08-02
depth: normal
---

# T17A — Local baseline

**Using `research-protocol`**. depth: normal.

## Method

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools | Grep/Read skills + Theme 9/14 reports |
| Depth | normal |
| stop_reason | Call-site map complete; no further E0 needed |

## Findings

| Label | Claim | Grade |
|-------|-------|-------|
| FACT | No `debug-router` skill exists; Debug pocket = `debug-systematic` + `debug-reproduce` only. | E0 |
| FACT | Happy-path step 5 + Bug classifier + Handoffs point at leaves; text says “Debug router deferred”. | E0 `implementation-happy-path` |
| FACT | `implementation-router` step 6 / wire checklist / Bug handoff → leaves; “Debug router deferred”. | E0 |
| FACT | Execute / -subagents / execute-verify Handoffs → Debug leaves with prove-first wording (matches accepted Execute hot-path lean). | E0 |
| FACT | Theme 9 F10 seams T-VF/T-UB/T-MD/T-CR/T-NYR are documented on `debug-systematic`. | E0/E1 Theme 9 report |
| FACT | Theme 14 D4 deferred debug-router; O1 optionally included it. | E0 Theme 14 report |

## Rewire inventory (post-elevate)

| Surface | Change |
|---------|--------|
| happy-path | Bug row + step 5 + Handoffs → `debug-router` |
| happy-path checklist / template | drop “deferred” |
| implementation-router | step 6 + wire + Handoffs → `debug-router` |
| implementation-router template | debug handoff line → router |
| Execute / -verify / -subagents | keep direct leaf; add one-line repro-first / “or debug-router when which-path unclear” |
| packs Routers row | Debug: `debug-router` |

## GAP

None blocking. OPEN: exact Execute Handoff sentence length (keep thin).
