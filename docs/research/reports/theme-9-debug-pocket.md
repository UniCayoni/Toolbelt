---
title: "Theme 9 — Debug pocket (integrated report)"
status: accepted
theme: theme-9-debug
created: 2026-07-30
updated: 2026-07-30
accepted: 2026-07-30
acceptance_scope: method_guidance_t9_debug_pocket
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: low_return_plus_one
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-9-debug/campaign-brief.md
  - docs/research/notes/theme-9-debug/t9-w2-align.md
  - docs/research/notes/theme-9-debug/t9-w3-plus1-residual.md
  - docs/research/reports/theme-7-execute-pocket.md
  - docs/research/reports/theme-8-verify-gates.md
  - skills/systematic-debug/SKILL.md
  - skills/reproduce-bug/SKILL.md
supersedes: null
---

# Theme 9 — Debug pocket (integrated report)

**Status:** **accepted** (method guidance) — 2026-07-30.  
**Elevated:** `systematic-debug` + `reproduce-bug` (+ Execute / Execute-verify / -subagents wire).  
**Campaign stop:** `low_return_plus_one`.

**Using `research-protocol`** · integrator merge.

**Identity:** Method pocket for **investigate → reproduce → evidence → root cause → minimal fix → re-verify**.  
**Not** Theme 8 Verify gates. **Not** a fat PR/CI/Bugbot pack (Phase 2 list only).

Standalone Toolbelt (inspire; **do not depend** on Superpowers / silkyland / debug-agent packaging).

### Elevation decisions (accepted 2026-07-30 — quality leans)

| ID | Decision |
|----|----------|
| F1 | **B** — spine + never-fix reproduce companion |
| F2 | Spine **`systematic-debug`**; companion **`reproduce-bug`** (avoid `debug-mode` / bare `debug`) |
| F3 | **`debug-fix-cycles` = 3** (failed fix cycles after strong/confirmed hypothesis); **≠** Execute `verify-retry N=2` |
| F4 | **Light flaky checklist** in method (measure → force → rate / not-yet); not a third skill |
| F5 | Companion = **never-fix + 8-field light dossier** (`docs/templates/repro-light.md`) |
| F6 | Instrumentation = **section of spine** (compose Cursor Debug Mode; Agent protocol atoms; no collector) |
| F7 | Defense-in-depth = **optional** post-fix note (esp. invalid-data) |
| F8 | T9F swarm **parked** |
| F9 | **Skill-only** — no always-on debug rule |
| F10 | Full seam: **T-VF / T-UB / T-MD / T-CR / T-NYR** |
| FC-PARKS | Collectors; private Cursor wire; PR/CI/Bugbot Phase 2; Superpowers/TDD coupling; thermo-nuclear |

---

## 1. Executive summary

1. Theme 7/8 own Execute verify-retry and Plan/Execute verify companions. Theme 9 adds systematic **bug investigation** with evidence culture.  
2. Deep campaign closed with `low_return_plus_one`.  
3. Elevated thin **B** surfaces; compose Cursor natives; no private wire / collectors.  
4. Quality lean: reproduce before fix; falsify with evidence; same-repro verify; escalate don’t thrash.

---

## 2. Sources merged

Notes under `docs/research/notes/theme-9-debug/` (pass1–3, W1 T9A–T9E, W2-ALIGN, PLUS1). Input law: Theme 7 + Theme 8 accepted reports. Subagents: `cursor-grok-4.5-high-fast`.

---

## 3. Method spine (accepted)

```text
0. Intake
1. Reproduce same surface — or NOT-YET-REPRODUCED (no guess-fix)
   └─ intermittent → flaky light checklist
2. Evidence path: Terminal / Browser / prefer Cursor Debug Mode when unclear runtime /
   Agent instrumentation atoms when Debug Mode unavailable (no private wire, no collector)
3. Hypothesize → falsify → backward root-cause
4. Minimal fix → VERIFY SAME REPRO → cleanup
5. Stop after debug-fix-cycles=3 or architecture smell → human
   (≠ Execute verify-retry N=2)
```

Never-fix path: use **`reproduce-bug`** first when the job is prove-the-bug / dossier only.

---

## 4. Boundaries

| Theme 9 owns | Theme 7 / Execute | Theme 8 | Later / park |
|--------------|-------------------|---------|--------------|
| `systematic-debug` + `reproduce-bug` | `verify-retry N=2`, HITL, task loop | plan-verify / execute-verify | PR/CI/Bugbot Phase 2 |
| Compose Debug Mode / Terminal / Browser | Done-when Verify | Evidence iron law / converge | T9F swarm; collectors |
| Agent instrumentation teaching | major-deviation / verify-fail escalate | Faithfulness/readability | Private Cursor wire; always-on debug rule |

**Confirmed GAP:** Cursor extension debug-server private wire — compose via Debug Mode / `/debug` / `/logs` only.

---

## 5. Vocabulary (accepted)

| Token | Meaning |
|-------|---------|
| `verify-retry N=2` | Theme 7 Execute Done-when mismatch budget — unchanged |
| `debug-fix-cycles` (=3) | Debug thrash stop after strong/confirmed hypothesis |
| `NOT-YET-REPRODUCED` | Honest unreproduced; dossier/monitor; no guess-fix |
| `CONFIRMED` / `REJECTED` / `INCONCLUSIVE` | Hypothesis status from runtime evidence |

---

## 6. Seam triggers (F10 accepted)

| ID | Trigger → Debug |
|----|-----------------|
| T-VF | Execute `verify-fail` after verify-retry N=2 exhausted |
| T-UB | User-reported bug / unexpected behavior outside plan |
| T-MD | Major-deviation / weird runtime beyond plan Files |
| T-CR | Execute-verify Critical / unclear faithfulness break |
| T-NYR | Need never-fix first → `reproduce-bug` then spine fix |

Do **not** burn more Execute verify-retries under Debug.

---

## 7. Parks / Phase 2

| Park now | Phase 2 list only |
|----------|-------------------|
| T9F swarm; collectors; private Cursor wire; always-on debug rule | PR create/finish; Copilot PR; CI babysit; Bugbot; git ceremony |
| Superpowers TDD coupling; thermo-nuclear; silkyland product deps | — |

---

## 8. Elevation status

| Surface | Status |
|---------|--------|
| `systematic-debug` | **Shipped** |
| `reproduce-bug` | **Shipped** |
| `docs/templates/repro-light.md` | **Shipped** |
| Execute / -subagents / execute-verify wire | **Shipped** |
| Always-on debug rule | **Rejected** |
| PR/CI mega-pack | **Out of scope** (Phase 2) |

---

## 9. Acceptance checklist

- [x] Human adjudicated F1–F10 (quality recommended leans)  
- [x] Human accepts this report as Theme 9 method guidance  
- [x] Elevate skills + wire + packs via `author-cursor-surfaces`  
- [ ] Sync local plugin + Reload Window (operator)
