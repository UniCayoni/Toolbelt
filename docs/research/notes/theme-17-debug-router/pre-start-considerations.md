---
title: "Theme 17 (proposed) — Debug router pre-start considerations"
status: accepted
theme: theme-17-debug-router
created: 2026-08-02
updated: 2026-08-02
accepted: 2026-08-02
acceptance_scope: lean_locks_classifier_and_execute_hop
accepted_by: human (Jonathan)
authors: [coordinator]
aligned_with:
  - docs/research/reports/theme-14-pocket-routers.md
  - docs/research/reports/theme-9-debug-pocket.md
  - docs/research/reports/theme-10-happy-path.md
  - skills/implementation-router/SKILL.md
  - skills/implementation-happy-path/SKILL.md
supersedes: null
---

# Debug router — pre-start considerations

**Using `research-protocol`** (recon only; **depth: normal**).  
**Not** a campaign brief yet — feedstock for enough-to-start / lean.  
Sources: Theme 14 accepted + elevate pattern; Theme 9 Debug law; live skills (post Theme 16, **23** skills).

## 1. Why Theme 14 deferred it (facts)

| Source | What it said |
|--------|----------------|
| Theme 14 D4 | Defer `debug-router`; Debug stays leaf Handoffs + happy-path classifier |
| T14E O1 lean | Elevate `implementation-router` and **optionally** `debug-router` |
| T14A | Both Implementation and Debug lacked discoverable pocket entry — Implementation was the larger fan-out |

**INFERENCE:** Deferral was **sequencing/cost**, not a product veto. O1 already contemplated Debug as a sibling pocket router.

## 2. What Theme 14 already locked (must inherit)

These are accepted law for *any* pocket router — Debug is not a special exemption:

| # | Constraint |
|---|------------|
| L1 | Layer model: leaf = method SoT; router = classify + wire; happy-path = optional caller |
| L2 | Vocabulary **router** (not guide) |
| L3 | **Compose-only** — do not restate leaf law |
| L4 | **Selection ≠ solving** — no task decomposition in the router (T14 D5; T14D OPEN closed as “pure select” for Implementation) |
| L5 | Structured handoff fields (goal, prior, facts+source, open question, constraints) — checklist/template, not always-on rule |
| L6 | Explicit skips / intelligent skip when leaf already obvious (T14B juew lean) |
| L7 | Workers get **one leaf**, not the router wire |
| L8 | **Park** global meta `skill-router` / always-on |
| L9 | Elevate via **`author-cursor-surfaces`** + smoke (I1 pattern) |

**Template clone pattern:** `docs/templates/implementation-router.md` + skill + refresh mapping + packs Routers row update.

## 3. What Theme 9 already locked (Debug leaves — router must not reopen)

| Token / decision | Meaning for router |
|------------------|-------------------|
| F1 B | Two leaves only: `debug-systematic` + `debug-reproduce` |
| Iron law | No product fix without repro or `NOT-YET-REPRODUCED` |
| F3 | `debug-fix-cycles=3` ≠ Execute `verify-retry N=2` |
| F10 seams | T-VF, T-UB, T-MD, T-CR, T-NYR |
| F8 / parks | No swarm, collectors, private Debug Mode wire, always-on debug rule, PR pack |

Router **classifies into** those leaves and **hands back** to Implementation / Design / human — it does not own investigate method.

## 4. Where the project stands now (E0)

```text
Research entry     → research-scope (de facto)
Design entry       → design-process (de facto)
Implementation     → implementation-router (shipped)
Debug              → leaves only (deferred router) ← this campaign
Cross-pocket       → implementation-happy-path
Closeout           → implementation-closeout (optional)
Host standards     → author-standards (Theme 16)
```

**Live “Debug router deferred” call sites (must rewire):**

- `implementation-happy-path` step 5 + classifier Bug row + Handoffs  
- Happy-path checklist template  
- `implementation-router` step 6 / wire plan / Bug handoff (exit → `debug-router`, not raw leaves)

Execute / execute-verify / -subagents already point at Debug leaves — after elevate, prefer **handoff to `debug-router`** when ask is “which Debug path?”; keep direct leaf invoke when user already named one leaf (intelligent skip).

## 5. Considerations to settle before / in campaign brief

### 5.1 Shape — **accepted** 2026-08-02

| Question | Decision |
|----------|----------|
| Theme id | **Theme 17** amending Theme 14 D4 |
| Depth | **normal** (no deep fleet unless classifier ambiguity appears) |
| Skill name | `debug-router` |
| Slash vs discoverable | **no** `disable-model-invocation` (like impl-router) |
| Template | `docs/templates/debug-router.md` (clone impl-router shape) |

### 5.2 Classifier — **accepted** 2026-08-02

Debug has **two** leaves — classifier is smaller than Implementation but **higher stakes** (wrong path = fix-without-repro).

| Ask lean | Wire |
|----------|------|
| Prove / minimize / dossier only | `debug-reproduce` → stop or hand systematic |
| Investigate + fix (repro exists or will be made) | `debug-systematic` (may call reproduce internally per Theme 9) |
| Prove-first then fix (T-NYR) | optional wire: `debug-reproduce` → `debug-systematic` |
| User already named one leaf | skip router → that leaf |
| Design wrong / need ADR | exit Debug → `design-process` / happy-path |

- **Default:** one **entry leaf** only.
- **Optional wire** reproduce → systematic only for explicit prove-then-fix / T-NYR (not the default).
- Systematic still prefers reproduce inside Theme 9 spine when needed.

### 5.3 Seam ownership — **accepted** 2026-08-02

| Inbound | After |
|---------|--------|
| Happy-path Bug / T-* | → **`debug-router`** |
| Impl-router verify-fail / unclear Critical | → **`debug-router`** |
| Execute N=2 / execute-verify hot path | **Direct leaf OK** with repro-first rule: no solid repro / prove-first → `debug-reproduce` (or router); repro in hand → `debug-systematic` |
| Pocket-local “which Debug skill?” | → **`debug-router`** |

Document the Execute split in skill Handoffs so classification SoT does not thrash.

### 5.4 Outbound after Debug

| Exit | Next |
|------|------|
| Fixed + same-repro green | human / optional closeout / return Implementation if mid-feature |
| `NOT-YET-REPRODUCED` | human / monitor — no guess-fix |
| `debug-fix-cycles` exhausted / architecture | human |
| Root cause = design/intent gap | `design-process` / plan — not more Debug thrash |

### 5.5 Explicit non-goals (carry parks)

- Global skill-router  
- Third Debug skill / swarm  
- PR/CI/Bugbot ceremony  
- Restating systematic spine in the router  
- Renaming `research-scope` / `design-process` (still Theme 14 park)  
- Always-on debug rule  

### 5.6 Validation

Mirror Theme 14 I1:

| Smoke | Assert |
|-------|--------|
| Classify prove-only → reproduce | announce Using debug-router; invoke reproduce |
| Classify fix / T-VF → systematic | invoke systematic; no Execute N=2 burn |
| Negative: “debug the product and open a PR” | refuse ceremony; route Debug only |
| Intelligent skip | user says `/debug-reproduce` → no forced router |

In-session + fresh preferred (Theme 15/16 bar).

### 5.7 Research budget

| Track | Needed? |
|-------|---------|
| Local baseline (call sites, Theme 9 F10) | yes — short E0 |
| New community deep on routers | **no** — T14B/D already feedstock |
| Classifier lean + wire matrix | yes — one lean note |
| Elevate + wire + smoke | yes |

Enough-to-start: **yes** — lean locks accepted 2026-08-02.

## 6. Start sequence (in progress)

1. [x] Human accept lean locks (§5.1–5.3) — 2026-08-02  
2. [x] Campaign brief accept → normal wave T17A–E — 2026-08-02  
3. [ ] Report accept → **`author-cursor-surfaces`** elevate `debug-router` + template  
4. [ ] Rewire happy-path + impl-router; document Execute direct-leaf rule  
5. [ ] Smoke 2/2 → commit/push (noreply author/committer)

## 7. Self-check

- [x] Cite Theme 14/9/live skills; no invented Cursor APIs  
- [x] draft ≠ SoT  
- [x] Parks retained  
