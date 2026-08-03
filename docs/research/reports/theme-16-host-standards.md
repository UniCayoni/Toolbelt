---
title: "Theme 16 — Host standards (integrated report)"
status: accepted
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
accepted: 2026-08-02
acceptance_scope: method_guidance_t16_host_standards
accepted_by: human (Jonathan)
authors: [integrator]
depth: deep
stop_reason: diminishing_returns_plus_2_two_successive_diminishing_passes_w3p2_w3p3
protocol: docs/PROTOCOL.md
aligned_with:
  - docs/research/notes/theme-16-host-standards/campaign-brief.md
  - docs/research/notes/theme-16-host-standards/t16k-shape-options-lean.md
  - docs/research/notes/theme-16-host-standards/deep-campaign-board.md
  - docs/research/notes/theme-16-host-standards/normal-wave-summary-20260802.md
  - docs/research/reports/theme-15-closeout-readiness.md
  - docs/research/reports/theme-14-pocket-routers.md
supersedes: null
---

# Theme 16 — Host standards

**Status:** **accepted** (method guidance) — 2026-08-02.  
**Elevated:** via `/author-cursor-surfaces` — `author-standards` + principles/standards profile templates; Plan/Execute/Closeout bind; packs row.  
**Depth:** deep (`diminishing_returns_plus_2`).  
**O1 lean:** accepted 2026-08-02.  
**Using `research-protocol`** · integrator (merge only; no new facts).

## 1. Executive summary

Help hosts **define and maintain** principles + checkable standards feedstock that Plan, Execute, and Closeout can bind to. Optional brownfield **derive** proposes candidates from recon + history (recency/conflict) — never silent SoT. Not Toolbelt-universal coding law. Keep `implementation-closeout`; AGENTS.md stays short pointers.

## 2. Elevation decisions (accepted)

| # | Decision |
|---|----------|
| D1 | Theme id **`theme-16-host-standards`** |
| D2 | Shape **O1** — skill **`author-standards`** with modes `principles` \| `standards` \| `derive` \| light `bind-check` |
| D3 | Templates **`docs/templates/principles-profile.md`** + **`docs/templates/standards-profile.md`** |
| D4 | Host default paths OPEN (lean: e.g. `docs/standards/` or host-chosen); frontmatter purpose required — filename alone is overloaded |
| D5 | **Conflict stack (host-authored):** design/ADR > principles > standards > inferred-from-code — **industry SoT for this ladder = CONFIRMED GAP**; ship as Toolbelt method lean after accept |
| D6 | **v1 standard types:** naming · layout · patterns (prefer/avoid) · tests/docs · safety/secrets (+ optional API/error). **Park:** performance, i18n, a11y (exemplar exists but not v1 type law), process/PR, architecture → ADR |
| D7 | **Anatomy (standards):** purpose, scope, rules, examples, exceptions, enforcement pointer, evolution/version |
| D8 | **Principles:** philosophy/tone/continuity; short imperative or narrative; separate file *or* AGENTS “Core Principles” section — both evidenced |
| D9 | **Brownfield derive:** recon → host-declared recency/churn+blame (respect `.git-blame-ignore-revs`) → prefer hot-path eras / quarantine legacy → **proposed** until human accept; dual-era via suppressions / touch-to-clean / format wave |
| D10 | **Bind:** Plan/Execute/Closeout load profiles when present, skip when absent; AGENTS short pointer → profile/skill (Cursor/Claude/Codex patterns). AGENTS vs Team/Project/User conflict = **product-undefined GAP** |
| D11 | Keep **`implementation-closeout`**; closeout criteria may reference standards/principles |
| D12 | No always-on standards rule; no auto-promote derive; no closeout rename this theme |

## 3. Deep campaign method

| Field | Value |
|-------|-------|
| stop_rule | `diminishing_returns_plus_2` (human) |
| stop_reason | W3+2 and W3+3 successive `diminishing=true` on remaining residuals |
| Waves | Normal T16A–K → Deep W1 (C/D-F/H-I/J) → W2 RAG/gh + git primary → W3 → W3+1 → W3+2 → W3+3 |

### Note index

| Wave | Notes |
|------|-------|
| Normal | `t16a`…`t16j`, `t16k` (accepted), `normal-wave-summary-20260802.md` |
| Deep W1 | `deep-t16c-principles-exemplars.md`, `deep-t16d-f-typology-exemplars.md`, `deep-t16h-i-brownfield-git.md`, `deep-t16j-bind-patterns.md` |
| Deep W2 | `deep-w2-corroboration-rag-gh.md`, `deep-t16i-git-era-primary.md` |
| Residual | `deep-w3-residual-gaps.md`, `deep-w3p1-residual-confirmed-gaps.md`, `deep-w3p2-residual-last-gaps.md`, `deep-w3p3-final-diminishing.md` |
| Board | `deep-campaign-board.md` |

## 4. Confirmed GAPs retained (do not invent)

| GAP | Implication for elevate |
|-----|-------------------------|
| Named industry conflict stack ADR > principles > standards | Author as **accepted Toolbelt method**, not “industry already says” |
| Cursor AGENTS.md vs Team/Project/User / alwaysApply win-order | Document as undefined; prefer non-conflicting pointers; E0 experiment optional later |
| Normative N-month recency default for derive | Host-declared window; no Toolbelt numeric law |
| Recon skill lacks git/history steps | Wire in elevate or follow-up track |

## 5. Acceptance checklist (human)

- [x] Campaign scope accepted — 2026-08-02  
- [x] O1 lean accepted — 2026-08-02  
- [x] Deep gather stopped under `diminishing_returns_plus_2` — 2026-08-02  
- [x] Human accepts this report (D1–D12) — 2026-08-02  
- [x] Elevate `author-standards` + templates + Plan/Execute/Closeout bind via `author-cursor-surfaces`  
- [x] Smoke S1 — in-session + fresh **2/2 PASS** (2026-08-02)
- [x] Packs/README/CHANGELOG + sync local plugin  

- [ ] **Parked:** reinforce Theme 14/15 elevations — `docs/research/notes/parked/author-surfaces-reinforce-t14-t15.md`

## 6. Parks

- Toolbelt-universal coding standard as law  
- Rename `implementation-closeout`  
- Always-on standards rule  
- Auto-promote brownfield derive  
- Fat CI / ceremony as standards content  
- debug-router / global meta-router (unrelated)
