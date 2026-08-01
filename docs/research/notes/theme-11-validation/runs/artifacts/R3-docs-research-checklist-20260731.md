---
title: "R3 smoke — Cursor Debug Mode (docs-research)"
status: draft
theme: theme-11-validation
surface_id: R3
created: 2026-07-31
---

# R3 — Cursor Debug Mode (short D0–D3 + GAP)

**Using `docs-research`**.

## D0 — Identity & pin

| Field | Value |
|-------|-------|
| Product | Cursor (IDE agent) |
| Status | in_use (this session) |
| Docs URL | https://cursor.com/docs/agent/debug-mode |
| Docs accessed | 2026-07-31 |
| App/build version | `GAP` — not read from About this run |

## D2 — Classify

Page = **explanation / how-to hybrid** (what Debug Mode is + how it works). Not machine API reference.

## Findings

- `FACT` [E1] Debug Mode helps find root causes for tricky/hard-to-reproduce bugs by generating hypotheses, adding log instrumentation, using runtime information, then making a targeted fix — instead of immediately writing speculative code. [E1: https://cursor.com/docs/agent/debug-mode — accessed 2026-07-31]
- `FACT` [E1] Flow includes: explore/hypothesize → instrument (logs to local debug server in Cursor extension) → user reproduces → analyze logs → targeted fix → verify and remove instrumentation. [E1: same]
- `GAP` Private debug-server **wire schema** (message shapes, endpoints, auth) — not documented on the public Debug Mode page. Searched: that URL body. Result: describes “local debug server” existence only; no schema. Do not invent.

## One-paragraph answer (smoke)

Cursor **Debug Mode** is an agent mode for hard bugs: the agent hypothesizes causes, instruments code with logs sent to a local debug server, asks you to reproduce, analyzes runtime evidence, applies a focused fix, then cleans up instrumentation after you verify.
