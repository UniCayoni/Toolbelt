---
title: "T5A W3 — Residual GAP closers (Plan Mode, ADR non-equivalence, HITL timing)"
status: draft
theme: theme-5-design
track: T5A
slice: T5A-W3
wave: 3
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5a-w3]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/t5a-w2-web-corroboration.md
  - docs/research/notes/theme-5-design/t5a-w2-alexandria-corroboration.md
  - docs/research/notes/theme-5-design/t5a-w1-s2-agent-design-process.md
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
---

# T5A W3 — Residual GAP closers

**Using `research-protocol`; depth: deep; wave: 3; slice: T5A-W3.**

**Status:** `draft`. Not Design SoT. Residual closers only. No ADR template re-research. No Superpowers/AgDR re-inventory. No Design skill elevation. No T5B/T5C/T5D.

## 1. Scope

- **Question / goal:** Close only the named P0/P1 residuals left after W2: (1) Cursor Plan Mode from official docs (+ E0 only if observable); (2) whether official docs claim Plan Mode replaces ADR/alternatives matrix; (3) one more E1/E2 on HITL design-time encoding vs per-decision gates, else confirm OPEN.
- **In scope:** Official Cursor docs/help/blog for Plan Mode; negative-claim check vs ADR; one additional HITL oversight source if easily found; Coordinator signal per campaign §4.3.
- **Out of scope:** ADR/MADR templates (S1); Superpowers/AgDR inventory (S3); open-ended fleets; Design skills; T5B/T5C/T5D; Alexandria re-query; classical ATAM.
- **Comprehension / research goal type:** other (residual GAP close)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (W2 web + Alexandria notes; campaign-brief §4.3; W1 S2 HITL conflict; research-note template; research-protocol); WebFetch (Cursor Plan Mode docs/help/blog; Cursor Agent overview; Redis HITL blog); WebSearch |
| Corpora / URLs searched | https://cursor.com/docs/agent/plan-mode ; https://cursor.com/help/ai-features/plan-mode ; https://cursor.com/blog/plan-mode ; https://cursor.com/docs/agent/overview ; https://redis.io/blog/ai-human-in-the-loop/ ; NIST AI RMF core page (Map 3.5 pin); site:cursor.com Plan Mode ADR search |
| Queries (exact) | `site:cursor.com Plan Mode ADR architecture decision record alternatives`; `human-in-the-loop design-time constraints vs per-decision approval AI agents architecture`; `NIST AI RMF human oversight decision rights design-time governance agents` |
| What was *not* searched | Alexandria re-probe; Superpowers/AgDR files; ADR template primaries; peer-reviewed GenAI-architecture MLR full texts; live Cursor IDE Plan Mode click-through / E0 UX experiment; EU AI Act Article 14 full legal primary; CSA Agentic Profile deep read (discovery only via search snippets — not used as lock) |
| Depth | deep |
| Waves / stop_reason | wave: **3**; stop_reason: **low_return_plus_one** — named P0/P1 residuals addressed; Plan Mode mostly re-pins W2 E1 with ADR non-claim added; HITL remains confirmed OPEN after one extra E2; no further residual stage |
| Provenance (optional PROV) | Entity←W2 notes + Cursor official pages + Redis blog + NIST Map 3.5 pin; Activity=T5A-W3 residual close; Agent=WebFetch/WebSearch |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Residual web/docs close only; no codebase recon |
| Scope boundary | Official Cursor surfaces + one HITL secondary; local W1/W2 as alignment (E0 pin of prior drafts), not new process law |

## 4. Findings

### 4.1 Cursor Plan Mode (official docs only)

- `FACT` [E1] Official Cursor Docs — Plan Mode: creates detailed **implementation plans before writing any code**. Flow: (1) clarifying questions; (2) codebase research; (3) comprehensive implementation plan; (4) user **reviews and edits** via chat or markdown; (5) user **clicks to build** when ready. Shift+Tab to rotate to Plan Mode; auto-suggest for complex-task keywords. Plans default to home directory; optional “Save to workspace.” [E1: https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29]
- `FACT` [E1] Official Cursor Help — Plan mode: same gate — generate/review plan **before Agent writes any code**; Shift+Tab → Plan; plan opens as editable virtual file; click **Build** when happy. When-to-use: complex features with multiple valid approaches; many files/systems; unclear requirements; **architectural decisions where you want to review the approach**. [E1: https://cursor.com/help/ai-features/plan-mode — accessed 2026-07-29]
- `FACT` [E1] Cursor product blog “Introducing Plan Mode”: plan tools + inline editor; research files/docs; clarifying questions; Markdown plan with paths/references; edit todos; build when ready; auto-suggest for complex tasks. [E1: https://cursor.com/blog/plan-mode — accessed 2026-07-29]
- `INFERENCE` [E4] Official surfaces pin a product checkpoint: **clarify → research → plan → human review/edit → Build**. Premises: Docs/Help/Blog E1 steps. Matches W2 §4.4 topology; does **not** lock Toolbelt process to Cursor UX.
- `GAP` **E0 runtime UX** (auto-suggest heuristics, exact plan file paths across IDE/JetBrains/ACP, live mode-picker behavior) **not observed** this slice — no intentional IDE click-through / experiment run. Prefer GAP over invented E0. [Searched: docs only. Result: product contracts from docs; runtime details unobserved.]
- `INFERENCE` [E4] W1 S2 / W2 Alexandria “Cursor Plan Mode OPEN for official docs” is **closed at E1 docs level**; residual E0 remains GAP. Premises: this §4.1 E1 set; W2 §4.4 already fetched same URLs — W3 re-pin confirms, does not newly invent.

### 4.2 Plan Mode vs ADR / alternatives matrix

- `FACT` [E1] Official Cursor Plan Mode docs/help/blog describe an **implementation plan** (steps, file paths, code references, todos) reviewed before Build. They do **not** state that Plan Mode is an Architecture Decision Record, replaces ADRs, or produces a criteria→options→tradeoff matrix. Searched pages: docs plan-mode, help plan-mode, blog plan-mode; WebSearch `site:cursor.com Plan Mode ADR architecture decision record alternatives` — no official page asserting ADR equivalence. [E1: https://cursor.com/docs/agent/plan-mode ; https://cursor.com/help/ai-features/plan-mode ; https://cursor.com/blog/plan-mode — accessed 2026-07-29; negative search 2026-07-29]
- `FACT` [E1] Docs *do* recommend Plan Mode when there are “multiple valid approaches” and for “architectural decisions where you want to review the approach first” — still framed as **approach/implementation planning**, not ADR field law. [E1: same Docs/Help URLs — accessed 2026-07-29]
- `OPEN` Toolbelt **must not equate** Cursor Plan Mode with Norris-style ADR options matrices / ADR lifecycle without separate evidence. Related checkpoint pattern only (plan→human gate→build ≠ criteria→options matrix→critique→decide→ADR). Follow-up: integrator language that keeps product affordance vs decision-record method distinct.
- `INFERENCE` [E4] Strengthens W2 Conflicts row “Plan Mode = ADR options matrix → no identity claim.” Premises: (1) this §4.2 FACT non-claim; (2) W1 Norris E1 ADR loop; (3) W2 §4.4 OPEN residual.

### 4.3 HITL: design-time encoding vs per-decision gates

**Prior sides (not re-litigated as new primaries):**

- Per-decision / design-level gates: Norris HITL course-correct at decision steps [E1 W1 S2]; Fowler Design-First approve levels before code [E1 W2 web]; Osmani/Albada plan-first + approve [E2 W2 Alexandria].
- Design-time encoding / scale critique of per-step HITL: Hetland “human-at-the-design-step” [E3 W2 web].

**W3 additional source (one pass):**

- `CLAIM` [E2] Redis engineering blog distinguishes three oversight models: **HITL** (human decides; system typically waits — synchronous interrupt-and-resume); **HOTL** (AI operates; humans monitor/veto); **human-out-of-the-loop** (autonomous **within pre-defined boundaries** set by humans **at design time**, without involvement during operation). States most production teams avoid full out-of-loop for high-risk tasks; also argues training-time alignment does not replace runtime interrupt/approval for inference failures. Vendor blog with product pitch — secondary, not Toolbelt lock. [E2: Jim Allen Wallace, Redis — https://redis.io/blog/ai-human-in-the-loop/ — published 2026-04-23 — accessed 2026-07-29]
- `FACT` [E1] NIST AI RMF 1.0 core (Map 3.5): **processes for human oversight** are to be **defined, assessed, and documented** per Govern policies; Govern 3.2 calls for policies differentiating roles/responsibilities for human-AI configurations and oversight. This is **design-time process definition** of oversight — it does **not** say design-time encoding replaces per-decision gates, nor the inverse. [E1: NIST AI RMF Core — https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ — accessed 2026-07-29; framework PDF https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf]
- `INFERENCE` [E4] Redis E2 **does not resolve** the Toolbelt OPEN; it **corroborates coexistence**: design-time boundaries (out-of-loop scope) and per-decision HITL gates are different models, choosable by risk — closer to W1/W2 “different layers” framing than to Hetland replacing Norris/Fowler gates. Premises: Redis three-model CLAIM; Norris/Fowler E1 gates; Hetland E3.
- `OPEN` **Confirmed OPEN** for Toolbelt Design pack: whether to emphasize per-decision design gates (Norris/Fowler E1), persistent design-time constraint encoding (Hetland E3; Redis out-of-loop boundaries E2), or a risk-tier hybrid — needs integrator + human accept. No W3 lock.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Official Cursor Plan Mode docs exist and describe plan→review→Build | confirmed (re-pin) | Docs/Help/Blog E1 — same family as W2 §4.4 |
| H2 | Official docs claim Plan Mode replaces ADR / alternatives matrix | rejected | Negative FACT §4.2 — no such claim |
| H3 | One E1/E2 source closes design-time vs per-decision HITL for Toolbelt | rejected | Redis E2 + NIST Map 3.5 E1 support coexistence / process definition; OPEN remains |
| H4 | E0 Plan Mode UX can be asserted without experiment | rejected | GAP — not observed |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| HITL timing | Norris E1 / Fowler E1: per-decision or per-design-level human gates before code | Hetland E3: prefer design-time encoding so every step need not be re-approved; Redis E2: design-time boundaries (out-of-loop) vs runtime HITL as distinct models | **OPEN confirmed** — prefer E1 for design-decision drafting gates; treat design-time encoding as complementary layer (E2/E3), not replacement law |
| Plan Mode = ADR | Cursor E1: implementation plan before Build | Norris E1: criteria/options/ADR drafting | **No identity** — FACT docs do not claim replacement; OPEN not to equate in Toolbelt without evidence |

## 7. Gaps & OPEN

- `GAP` E0 Cursor Plan Mode live UX / plan-path details across surfaces — unobserved this wave.
- `GAP` Deep CLI/API Plan Mode contract surface beyond docs snippets — not exhaustively fetched (not P0 for T5A process spine).
- `OPEN` Toolbelt must not equate Plan Mode with ADR options matrix (confirmed).
- `OPEN` Per-decision design gates vs design-time constraint encoding — confirmed OPEN after Redis E2 + NIST Map 3.5; acceptance only.
- (Carried, not re-opened here) AgDR single-lineage E3; classical ATAM; Alexandria ADR template atoms — out of W3 scope.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] T5A may cite Cursor Plan Mode as an **optional product affordance** for plan→review→build, sourced from official E1 — not as ADR/method SoT. Premises: §4.1–4.2.
- `INFERENCE` [E4] Integrator language should keep three layers distinct: (A) human design decision method (criteria/options/ADR), (B) runtime/agent oversight models (HITL/HOTL/boundaries), (C) IDE Plan Mode UX. Premises: §4.2–4.3; W1 S2 lanes.
- `INFERENCE` [E4] Further gatherer waves on these three residuals would likely restate — proceed to track synthesis under stop rule. Premises: §10 Coordinator signal; campaign-brief §4.3.

## 9. Source list (deduped)

1. Cursor Docs — Plan Mode — https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29 — **E1**
2. Cursor Help — Plan mode — https://cursor.com/help/ai-features/plan-mode — accessed 2026-07-29 — **E1**
3. Cursor Blog — Introducing Plan Mode — https://cursor.com/blog/plan-mode — accessed 2026-07-29 — **E1**
4. Cursor Docs — Agent overview (context only; no Plan Mode ADR claim) — https://cursor.com/docs/agent/overview — accessed 2026-07-29 — **E1**
5. Jim Allen Wallace / Redis — Human in the loop… — https://redis.io/blog/ai-human-in-the-loop/ — accessed 2026-07-29 — **E2**
6. NIST AI RMF Core (Map 3.5 / Govern 3.2) — https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ — accessed 2026-07-29 — **E1**
7. NIST AI RMF 1.0 PDF — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf — accessed 2026-07-29 — **E1** (framework pin)
8. Prior gatherers (alignment, not new FACTS): `t5a-w2-web-corroboration.md`; `t5a-w2-alexandria-corroboration.md`; `t5a-w1-s2-agent-design-process.md`; `campaign-brief.md` §4.3

---

## 10. Coordinator signal

| Field | Value |
|-------|--------|
| `low_return_detected` | **yes** |
| Signal | W3 Plan Mode section largely **re-pins W2 §4.4 E1** (same official URLs/steps). New closable value is thin: ADR **non-claim** FACT + Redis E2 HITL models + NIST Map 3.5 pin; HITL policy remains OPEN. |
| Named GAPs remaining after W3 | (1) E0 Plan Mode runtime UX unobserved; (2) Plan Mode ≠ ADR equivalence — confirmed OPEN (do not equate); (3) design-time encoding vs per-decision gates — **confirmed OPEN**; (4) carried out-of-scope: AgDR independent lineage, ATAM, Alexandria ADR template atoms |
| Recommend | **Proceed to track synthesis** — treat W3 as the Theme 5 **+1 residual stage** after W2 diminishing (`stop_reason`: `low_return_plus_one`). Do **not** launch another residual stage (campaign §4.3: one confirmation stage, then hard stop). Leave remaining items as confirmed `GAP`/`OPEN`. |

### Parent return summary

- **low_return_detected:** yes (Plan Mode mostly restated W2)
- **Closed / tightened:** Official Plan Mode plan→review→Build E1 re-pinned; FACT docs do not claim ADR/options-matrix replacement; Redis E2 + NIST Map 3.5 added without resolving HITL OPEN
- **Remain:** E0 Plan Mode UX GAP; Plan Mode≠ADR OPEN; HITL timing OPEN
- **Recommend:** proceed to **T5A track synthesis** (no further +1 residual stage)
