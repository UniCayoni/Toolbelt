---
title: "Theme 10 — implementation-happy-path campaign brief"
status: draft
theme: theme-10-happy-path
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
campaign_phase: accepted_elevated
aligned_with:
  - docs/research/notes/theme-10-happy-path/scope-normal-pass1.md
  - docs/packs/README.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 10 — `implementation-happy-path` brief

**Using `research-protocol`** · depth: **normal** (compose — deep fleet not planned).

**Status:** `draft`. Not workflow SoT.  
**Scoping:** [`scope-normal-pass1.md`](./scope-normal-pass1.md).

---

## 0. Locked / proposed

| Item | Value |
|------|-------|
| Skill name | **`implementation-happy-path`** (human) |
| Form | Thin **orchestration** skill + checklist (lean **A**) |
| Always-on rule | **No** |
| Deep gatherers | **Not required** — pocket SoT already accepted |
| PR/CI | Still Phase 2 stub — pointer only |

---

## 1. Purpose

Cold-start / controller skill that sequences shipped Toolbelt pockets:

`research? → design → (adr?) → plan → plan-verify → execute|/subagents → execute-verify → debug?`

Each step **invokes** existing skills (`Using X`); does not restate pocket law.

---

## 2. Elevation candidates (post-accept)

| Deliverable | Notes |
|-------------|-------|
| `skills/implementation-happy-path/SKILL.md` | Classifier + numbered compose map + anti-patterns |
| `references/implementation-happy-path-checklist.md` (and/or `docs/templates/happy-path.md`) | Progress checklist; G1 pick at elevate |
| Wire | packs row; README skills table; Handoffs from `design-process` / `research-codebase-recon` / plan / execute (entry pointers) |
| Subagent note | Controller may hold happy-path; workers = one pocket |

---

## 3. Approval gate

- [x] Human accepts pass-1 lean (name, shape A, no deep fleet, no always-on) — 2026-07-30  
- [x] Research = **as-needed preface**  
- [x] Checklist SoT = `docs/templates/happy-path.md` (+ skill references)  
- [x] Elevated via `author-cursor-surfaces`  

Hard rule: orchestration only; do not paste Plan/Execute/Debug bodies into the orchestrator.
