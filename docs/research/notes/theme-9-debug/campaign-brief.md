---
title: "Theme 9 — Debug pocket deep research campaign brief"
status: draft
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: deep
campaign_phase: accepted_elevated
aligned_with:
  - docs/research/notes/theme-9-debug/scope-normal-pass1.md
  - docs/research/notes/theme-9-debug/scope-normal-pass2-expand.md
  - docs/research/notes/theme-9-debug/scope-normal-pass3-deepen.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/PROTOCOL.md
supersedes: null
---

# Theme 9 — Debug pocket campaign brief

**Using `research-protocol`** · depth: **deep**.

**Status:** `draft` brief. **Wave 1 launched** 2026-07-30. Not Debug SoT.  
**Identity:** Method pocket for **investigate → reproduce → evidence → root cause → minimal fix → re-verify**. **Not** Theme 8 Verify gates (Plan/Execute completion). **Not** a fat PR mega-pack by default (PR/CI may be Phase 2).

**Scoping:** [`pass1`](./scope-normal-pass1.md) + [`pass2`](./scope-normal-pass2-expand.md) + [`pass3`](./scope-normal-pass3-deepen.md).  
**Human (2026-07-30):** Accepted quality/effectiveness leans below; fence items stay open until **after deep report**, with pros/cons, **before** any surface elevation.

---

## 0. Locked campaign leans (human-accepted)

| Decision | Lock |
|----------|------|
| Quality / effectiveness over thinness-alone | Prefer evidence culture even if that nudges **B** |
| Surface working lean | **B** (spine + reproduce companion) — *final A vs B still a fence item after deep* |
| T9E in W1 | **Yes** |
| T9F in W1 | **No** (park / Phase 2 unless residual forces reopen) |
| PR / CI / Bugbot | **Phase 2** — T9D lists only, no design lock now |
| Subagents | `cursor-grok-4.5-high-fast` |
| Stop | `low_return_plus_one` |
| Non-goals | Standalone; no Cursor private API invention; no shipping collectors/MCP; don’t re-own Theme 8 |

---

## 0b. Fence items — decide **after deep**, **before** elevate

Deep tracks must gather evidence and the draft report must include a short **pros/cons** for each row. Human picks; then `/author-cursor-surfaces`. Do **not** elevate while these are open.

| ID | Fence | Working lean (not lock) | What deep must deliver |
|----|-------|-------------------------|------------------------|
| F1 | **A vs B final** — one spine skill vs spine + never-fix companion | B preferred | Pros/cons vs Toolbelt thinness, discoverability, ladder seams |
| F2 | **Skill names** (avoid “Debug Mode” collision) | OPEN | 2–3 name candidates + collision check |
| F3 | **N-fix stop** before architecture / escalate | ~3 (community echo) | Pros/cons of N=2 vs N=3 vs soft guidance |
| F4 | **Flaky protocol thickness** — checklist-in-spine vs companion section vs park thin | Light checklist in method | Pros/cons; don’t invent third skill unless evidence demands |
| F5 | **Reproduce companion shape** — never-fix only vs never-fix + light dossier | Never-fix + light dossier | Pros/cons; template size vs agent load |
| F6 | **Instrumentation home** — section of spine vs short companion vs “compose Debug Mode only” | Section of spine (+ T9E atoms) | Pros/cons; no collector packaging |
| F7 | **Defense-in-depth** — optional note vs recommended after invalid-data fixes | Optional post-fix note | Pros/cons vs thin spirit / over-engineering |
| F8 | **T9F swarm** — stay parked vs residual reopen | Parked | Only reopen if W2/residual shows P0 ambiguity cost |
| F9 | **Always-on debug rule** | Unlikely (skill-only) | Confirm skill-only unless deep finds strong counter |
| F10 | **Execute→Debug seam wording** | Wire on verify-fail / user bug / unclear Critical | Exact trigger language for handoffs |

**Process:** draft report → human fence adjudication (this table) → accept theme → elevate + author-cursor-surfaces.

---

## 1. Purpose

| Field | Value |
|-------|-------|
| Theme | **Debug / investigate / reproduce** pocket |
| Goal | Teach agents to debug with **evidence and reproduction**, not assumptions; compose Cursor native tools; Toolbelt-native surfaces |
| Form | Prefer **thin spine skill(s)** over fat Debug+PR cookbook |
| Ladder | … → Execute / execute-verify → **Debug (this)** → (later) PR/workflow |

**Non-goals:** Re-litigate Theme 8 evidence iron law / N=2 / converge; re-own Plan validate; Superpowers as dependency; mandatory TDD as Debug law; shipping MCP servers or NDJSON collectors inside Toolbelt; inventing Cursor private debug-server APIs.

**Essence filter:** Standalone Toolbelt method. Inspire from Superpowers systematic-debugging (+ companions), reproduce-my-bug, Cursor Debug Mode, debug-agent NDJSON pattern — **extract atoms, cut coupling**.

**Quality lean:**

1. Reproduce before fix (or document why not / `NOT-YET-REPRODUCED`)  
2. Hypotheses falsified with runtime/command evidence  
3. Root cause over symptom patches (backward trace when stack is deep)  
4. Verify the **same** repro after fix; clean instrumentation  
5. Thin discoverable surfaces; escalate don’t thrash  

---

## 2. Why Theme 9 (from normal passes)

| Already elsewhere | Still missing |
|-------------------|---------------|
| Theme 8: plan-verify + execute-verify (completion/quality gates) | Systematic **bug investigation** when something is wrong |
| Execute: Done-when run + N=2 + HITL | Reproduce / hypothesis / root-cause playbook |
| Cursor Debug Mode / terminal / browser (product) | Toolbelt method for **when/how** to use them + Agent-mode fallback |
| G10 leftovers listed | Pocket design starts here |

**Pass-3 deltas (high signal):** never-fix + REPRO dossier (silkyland); root-cause-tracing / defense-in-depth / condition-waiting companions; Browser greppable log files; community NDJSON “debug-agent” cluster as **compose atoms** not packaging; swarm = optional park.

---

## 3. Tracks (proposed)

### T9A — Debug method spine

Formalize investigate → reproduce (shrink) → hypothesize/falsify → root-cause (backward trace) → minimal fix → verify same repro; red flags; stop after N failed fixes → architecture question; **flaky light checklist** (force nondeterminism or document rate); optional defense-in-depth note after invalid-data fixes; seam from Execute `verify-fail` / user bug reports.

### T9B — Cursor native composition

Deep-read / lock compose rules: Debug Mode (hypothesize → instrument → human repro → logs → fix → cleanup), Terminal (full output), Browser (console/network + file logs), Checkpoints, CLI `/debug` `/logs`; Run Mode implications; host MCP as **observe** (Sentry etc.), don’t package. How Toolbelt skills **invoke/compose** without replacing Cursor Debug Mode.

### T9C — Community / vendor deepen

Deep-read + transferable vs park: Superpowers systematic-debugging + `root-cause-tracing` / `defense-in-depth` / `condition-based-waiting`; silkyland reproduce-my-bug (dossier/flaky refs); rbouschery bug-investigate-fix; millionco debug-agent (+ JUNERDD corroboration); stas00 art-of-debugging loop atoms; spot-check investigate / control-ui/cli / verify-this. RAG refresh if needed.

### T9D — Surface shape & elevation

Working lean **B**; keep **A** as first-class alternative with pros/cons (fence **F1**). Defer **C/D**. Naming candidates (fence **F2**); wiring from Execute/Verify (fence **F10**); Phase 2 PR/CI **list only**.

### T9E — Instrumentation & evidence capture *(new from pass 3)*

When to prefer Cursor Debug Mode vs Agent-mode instrumentation; **protocol atoms** inspired by debug-agent NDJSON (`hypothesisId`, CONFIRMED/REJECTED/INCONCLUSIVE, cleanup regions) **without** shipping a collector; terminal/browser evidence as first-class; never invent private Cursor wire protocols; cleanup before claiming done.

### T9F — Parallel investigate *(optional; park by default)*

bug-hunt-swarm-style read-only multi-agent diagnosis for large/ambiguous bugs only. Include in W1 only if human opts in; else Phase 2 / residual.

**Optional gap fleet:** Only if W2 names P0.

---

## 4. Shared protocol

- Cite-or-omit; FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U  
- Subagents: `cursor-grok-4.5-high-fast` (default unless human changes)  
- Notes: `docs/research/notes/theme-9-debug/`  
- Report: `docs/research/reports/theme-9-debug-pocket.md`  
- Theme 7+8 = **input law** (boundaries)  
- Stop: low-return → **+1 residual** → `low_return_plus_one`  
- Elevate only after accept → then **`/author-cursor-surfaces`**

| Phase | Shape |
|-------|-------|
| Approve brief | **Done** (leans + fence table) |
| W1 | Parallel **T9A–T9E** light (T9F out) |
| W2 | Corroboration |
| W3 / +1 | Residual → `low_return_plus_one` |
| Integrate | Draft report **including § fence pros/cons (F1–F10)** |
| Fence gate | Human adjudicates F1–F10 |
| Accept + elevate | Then `/author-cursor-surfaces` — **not before fence gate** |

---

## 5. Candidate elevation (after fence gate only)

| Candidate | Notes |
|-----------|-------|
| Thin systematic-debug / investigate skill | If F1 → A or B |
| Reproduce companion (never-fix ± dossier) | If F1 → B; shape via F5 |
| Instrumentation protocol | Prefer section of spine (F6) unless deep disagrees |
| Wire from Execute verify-fail / Handoffs | Almost certain (F10) |
| Always-on debug rule | Unlikely (F9) |
| Fat Debug+PR pack / default swarm | Deferred (F8) |
| Compose-only (no skill) | Weak default |

---

## 6. Approval gate

- [x] Human accepted quality/effectiveness leans (working **B**, T9E in, T9F out, PR Phase 2)  
- [x] Fence items F1–F10 recorded — adjudicate **after deep**, **before** elevate  
- [x] Subagent model `cursor-grok-4.5-high-fast`  
- [x] Stop `low_return_plus_one`  
- [x] Launch Wave 1 (2026-07-30)  

Hard rule: no elevation while F1–F10 open; no inventing Cursor private debug APIs.
