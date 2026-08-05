---
title: "T24C-E0 — Host author surfaces and handoffs (local SoT)"
status: draft
theme: theme-24-author-learning
created: 2026-08-05
updated: 2026-08-05
authors: [gatherer-t24c-e0]
depth: deep
waves: W1
stop_reason: single_domain_local_sot_covered_named_gaps_retained
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
supersedes: null
---

# T24C-E0 — Host author surfaces and handoffs (local SoT)

**Using `research-protocol`**. Depth: **deep** Wave 1 gatherer (T24C). **Draft ≠ law** — map only; do not elevate.

## 1. Scope

- **Question / goal:** From LOCAL Toolbelt SoT only (E0 file reads), map how host feedstock is authored today and what handoffs **author-learning** should reuse — without elevating anything.
- **In scope:** Theme 16/15 accepted reports; Theme 23 fences only; author-* + closeout skills; draft-is-not-sot; standards-resolve-gate; PROTOCOL grades/cite-or-omit; Theme 24 campaign brief (accepted scope).
- **Out of scope:** Theme 23 playbook content beyond fences; Cursor private APIs; RAG/web/GitHub; inventing `author-learning` surface shape (T24D); auto-accept recommendations; rewriting Toolbelt plugin `skills/*` as the learning target.
- **Comprehension / research goal type:** reuse (map existing author paths for a future harvest skill).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | Read (local files); Grep (Theme 23 fences; closeout for author-learning mention); Glob (`docs/standards/index.md` presence) |
| Corpora / URLs searched | none (E0 local only) |
| Queries (exact) | path reads listed in Source list; grep `fence|not|Theme 24|learn-back` on theme-23 report; grep `author-learning|learn-back` under `skills/implementation-closeout` (no matches); Glob `docs/standards/index.md` → 0 |
| What was *not* searched | RAG, web, GitHub, Cursor product docs, runtime AGENTS/Team/Project precedence experiments, host repos outside Toolbelt |
| Depth | deep |
| Waves / stop_reason | W1 gatherer T24C-E0; `stop_reason=single_domain_local_sot_covered_named_gaps_retained` (no further local SoT files required for this track’s handoff map) |
| Provenance (optional PROV) | Entity←listed paths; Activity=E0 gather for T24C; Agent=gatherer-t24c-e0 |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | systematic |
| Why this mode | Must-read path set from campaign brief / deep board; handoff map needs full mode + skill coverage |
| Scope boundary | Toolbelt repo paths under `docs/research/reports/`, `docs/research/notes/theme-24-author-learning/`, `skills/{author-standards,author-agents-md,author-cursor-surfaces,implementation-closeout,research-draft-adr}/`, `rules/{draft-is-not-sot,standards-resolve-gate}.mdc`, `docs/PROTOCOL.md`. Excluded: Theme 23 playbook body beyond fences; non-must-read templates except where skills point (noted as GAP if not opened). |

## 4. Findings

### 4.1 Theme 24 target + fences (scope SoT)

- `FACT` [E0] Theme 24 accepted lean targets **host/workspace-bound** skills + host standards/principles/AGENTS — **not** Toolbelt plugin `skills/*`. [E0: path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` — Accepted lean O1 Target — observed 2026-08-05]
- `FACT` [E0] Theme 24 hard fences include: never auto-promote; draft≠SoT; evidence-based; not PR/CI ceremony; not Theme 23 playbook; not Toolbelt plugin self-modify. [E0: path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` — Hard fence / Parks — observed 2026-08-05]
- `FACT` [E0] Skill lean name (elevate later): **`author-learning`** (author-* pocket); historical label learn-back. [E0: path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` — Skill lean — observed 2026-08-05]
- `FACT` [E0] Theme 23 accepted report fences Theme 24 out: playbook is **not** Theme 24 learn-back; D1 records split learn-back → Theme 24; parks include Theme 24. [E0: path=`docs/research/reports/theme-23-host-playbook.md` — §§1–2 D1/D10 — observed 2026-08-05]
- `FACT` [E0] Deep board hard fences repeat: host/workspace target only; never recommend auto-accept as Toolbelt law; no invented Cursor private APIs. [E0: path=`docs/research/notes/theme-24-author-learning/deep-campaign-board.md` — Hard fences — observed 2026-08-05]

### 4.2 Modes: derive → proposed → human accept

- `FACT` [E0] `author-standards` modes include `principles` \| `standards` \| `derive` \| `bind-check`. [E0: path=`skills/author-standards/SKILL.md` — Modes table — observed 2026-08-05]
- `FACT` [E0] Mode `derive` delivers **proposed** candidates from recon + history → **human accept**; skill out-of-scope includes **auto-promote derive**; emit proposed edits/candidate list — **never** silent SoT. [E0: path=`skills/author-standards/SKILL.md` — Modes + derive step 5 + Out of scope — observed 2026-08-05]
- `FACT` [E0] Theme 16 D9: brownfield derive → quarantine legacy → **proposed** until human accept; D12: no auto-promote derive. [E0: path=`docs/research/reports/theme-16-host-standards.md` — Elevation D9/D12 — observed 2026-08-05]
- `FACT` [E0] Always-apply `draft-is-not-sot`: notes/reports with `status: draft` or `proposed` are **not** accepted design law; proposed ADRs are not architecture law. [E0: path=`rules/draft-is-not-sot.mdc` — observed 2026-08-05]
- `FACT` [E0] `standards-resolve-gate`: draft/proposed profiles stay non-law; **authoring** → `author-standards`. [E0: path=`rules/standards-resolve-gate.mdc` — steps 5 — observed 2026-08-05]
- `FACT` [E0] `research-draft-adr`: ADR status enum includes `proposed` \| `accepted` \| …; set `proposed` until human accepts — **proposed ≠ project law**. [E0: path=`skills/research-draft-adr/SKILL.md` — House defaults + step 2 — observed 2026-08-05]
- `FACT` [E0] `author-cursor-surfaces`: new surfaces stay draft/proposed until human accepts (`draft-is-not-sot`). [E0: path=`skills/author-cursor-surfaces/SKILL.md` — Caveat 5 + Stop — observed 2026-08-05]
- `FACT` [E0] Theme 16 conflict lean (host-authored method, not industry SoT): design/ADR > principles > standards > inferred-from-code. [E0: path=`docs/research/reports/theme-16-host-standards.md` — D5; also `skills/author-standards/SKILL.md` step 7 — observed 2026-08-05]
- `INFERENCE` [E4] Author-learning outputs, if elevated later, should stop at **proposed** host deltas and require **human accept** before law — mirroring derive/ADR/surface patterns. Premises: (1) Theme 24 never auto-promote; (2) derive/proposed/accept already the host feedstock pattern in Theme 16 + author-standards; (3) draft-is-not-sot alwaysApply.

### 4.3 Surfaces authored today (what exists)

- `FACT` [E0] Host **principles** and **standards** profiles: authored via `author-standards` from templates; lean defaults `docs/standards/principles.md`, `docs/standards/standards-profile.md` (host path OPEN at Theme 16 D4). [E0: path=`skills/author-standards/SKILL.md` — Paths; path=`docs/research/reports/theme-16-host-standards.md` — D3/D4 — observed 2026-08-05]
- `FACT` [E0] **AGENTS.md**: authored via `author-agents-md` (budgets, progressive disclosure); keep short pointers to principles/standards — do not dump full standards into AGENTS. [E0: path=`skills/author-agents-md/SKILL.md`; path=`skills/author-standards/SKILL.md` — Anti-patterns / Handoffs — observed 2026-08-05]
- `FACT` [E0] **Cursor skills/rules/commands/hooks**: authored via `author-cursor-surfaces`; clarify location: Toolbelt plugin vs host `.cursor/` vs personal skills. [E0: path=`skills/author-cursor-surfaces/SKILL.md` — Instructions step 1 — observed 2026-08-05]
- `FACT` [E0] **ADRs**: authored via `research-draft-adr` to host `docs/adr/NNNN-…`; architecture-sized locks routed away from standards. [E0: path=`skills/research-draft-adr/SKILL.md`; path=`skills/author-standards/SKILL.md` — Skip ADR-sized → research-draft-adr — observed 2026-08-05]
- `FACT` [E0] **Closeout profile**: authored/checked via `implementation-closeout` (`define-update` \| `check`); template SoT `docs/templates/closeout-profile.md`; host lean `docs/closeout/closeout-profile.md`. [E0: path=`skills/implementation-closeout/SKILL.md`; path=`docs/research/reports/theme-15-closeout-readiness.md` — D2–D4 — observed 2026-08-05]
- `FACT` [E0] Apply path (not authoring): when accepted host standards **catalog** exists → `guide-standards` via `standards-resolve-gate`; missing/unaccepted catalog → **no-op**. [E0: path=`rules/standards-resolve-gate.mdc` — observed 2026-08-05]
- `FACT` [E0] This Toolbelt workspace has **no** `docs/standards/index.md` at gather time (Glob 0) — resolve gate no-op here; does not invent host catalog. [E0: Glob `docs/standards/index.md` under `d:\Toolbelt` — observed 2026-08-05]

### 4.4 Handoff table (skill vs standards vs principles vs AGENTS vs ADR vs host skill edit)

Routing observed in existing author skills + Theme 16/15. **Reuse candidates for author-learning** — not new law bodies.

| Candidate kind | Primary author skill | Mode / artifact | Do not confuse with | Evidence |
|----------------|----------------------|-----------------|---------------------|----------|
| Host **standards** profile (checkable rules) | `author-standards` | `standards` or `derive` → proposed profile | Toolbelt-universal coding law; always-on rule dump | [E0: `skills/author-standards/SKILL.md`; Theme 16 D2/D6/D7] |
| Host **principles** (philosophy/tone) | `author-standards` | `principles` → proposed; AGENTS pointer only | Mixing lint rules into principles blob | [E0: `skills/author-standards/SKILL.md`; Theme 16 D8] |
| **AGENTS.md** house ops / budgets / pointers | `author-agents-md` | root/nested AGENTS.md | Full standards corpus in AGENTS; `llms.txt` as agent config | [E0: `skills/author-agents-md/SKILL.md` Handoffs] |
| **ADR** / architecture or process lock | `research-draft-adr` | `docs/adr/NNNN-…` status proposed→accepted | Standards “architecture” type (parked → ADR) | [E0: `skills/research-draft-adr/SKILL.md`; Theme 16 D6; author-standards Skip] |
| **Host skill / rule / command / hook** edit | `author-cursor-surfaces` | host `.cursor/` (or host plugin) path agreed with user | Toolbelt plugin `skills/*` rewrite as Theme 24 target | [E0: `skills/author-cursor-surfaces/SKILL.md` step 1; Theme 24 brief Target] |
| **Closeout** criteria / readiness check | `implementation-closeout` | `define-update` \| `check` | PR/merge ceremony; always-on | [E0: `skills/implementation-closeout/SKILL.md`; Theme 15] |
| **Apply** (load modules at work time) | `guide-standards` (via resolve gate) | pointers only when catalog accepted | Authoring feedstock | [E0: `rules/standards-resolve-gate.mdc`] |
| Bind discoverability | `author-standards` | `bind-check` | Inventing Cursor AGENTS vs Team/Project precedence | [E0: `skills/author-standards/SKILL.md` bind-check; Theme 16 GAP] |

- `FACT` [E0] Cross-handoffs already wired among author skills: `author-standards` ↔ `author-agents-md` ↔ `author-cursor-surfaces`; standards ↔ ADR; closeout ↔ `author-standards` for feedstock. [E0: Handoffs tables in the four skills above — observed 2026-08-05]
- `GAP` No live skill named `author-learning` / learn-back under Toolbelt `skills/` was in the must-read set; campaign brief states elevate later. Searched: campaign brief + closeout skill body. Result: skill not elevated yet.
- `GAP` `implementation-closeout` handoffs list `author-standards` and `author-cursor-surfaces` but **do not** mention `author-learning` or a post-check harvest step. Searched: `skills/implementation-closeout/` for `author-learning|learn-back` — zero matches (2026-08-05).

### 4.5 Closeout as possible trigger

- `FACT` [E0] Theme 24 accepted trigger lean: optional after closeout, explicit ask, and/or other evidence-gated loop ends; prefer `author-learning` (+ optional closeout hook); avoid always-on. [E0: path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` — Accepted lean Trigger/Skill glue — observed 2026-08-05]
- `FACT` [E0] Theme 15 / closeout: happy-path **optional** closeout before Stop; skip trivial by default; no always-on rule. [E0: path=`docs/research/reports/theme-15-closeout-readiness.md` — D7/D9; path=`skills/implementation-closeout/SKILL.md` — Skip — observed 2026-08-05]
- `FACT` [E0] Theme 16 D11: keep `implementation-closeout`; closeout criteria **may reference** standards/principles. [E0: path=`docs/research/reports/theme-16-host-standards.md` — D11 — observed 2026-08-05]
- `FACT` [E0] Closeout check seeds optional host standards/principles slots; feedstock authoring points to `author-standards`. [E0: path=`skills/implementation-closeout/SKILL.md` — define-update + Handoffs — observed 2026-08-05]
- `INFERENCE` [E4] Closeout is a **plausible optional trigger** for author-learning (after a non-trivial check/verdict), not a mandatory always-on step — matching Theme 24 trigger lean + Theme 15 skip-trivial. Premises: (1) Theme 24 Trigger row; (2) Theme 15 D7/D9; (3) closeout skill has no harvest hook today (GAP above).
- `OPEN` Exact closeout→author-learning wire (prompt? handoff line? separate invoke?) is not specified in local SoT files read; belongs to T24A / elevate design — do not invent.

### 4.6 Protocol discipline (binding on this note and future harvest)

- `FACT` [E0] PROTOCOL: cite-or-omit; labels FACT/CLAIM/INFERENCE/GAP/OPEN; grades E0–E4/U; prefer absence over invention; draft/proposed deep outputs ≠ design law until acceptance. [E0: path=`docs/PROTOCOL.md` — Non-negotiables + grades + depth — observed 2026-08-05]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Author-learning should **route** candidates into existing author-* skills rather than invent new law bodies | confirmed (as local lean) | Theme 24 O1 + handoff tables in author-standards / agents / cursor-surfaces / ADR |
| H2 | Closeout already invokes harvest | rejected | No author-learning mention in closeout skill; Theme 24 trigger is optional / elevate later |
| H3 | Derive mode is the closest existing pattern for “proposed candidates from evidence → human accept” | confirmed (local) | author-standards derive + Theme 16 D9/D12 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| T24C track depth in campaign brief (`normal`) vs deep board W1 gatherer | Campaign brief Tracks table: T24C depth `normal` | Deep board: W1 includes T24C-E0 under deep campaign | Prefer campaign **execution** context: this note is deep W1 gatherer as boarded; track depth “normal” describes expected research weight, not forbidding a Method-envelope E0 note. No factual conflict on handoffs. |
| Theme 23 vs Theme 24 ownership | Theme 23 parks Theme 24 / not learn-back | Theme 24 owns author-learning | Resolved by accepted split (Theme 23 D1; Theme 24 brief). |

## 7. Gaps & OPEN

- `GAP` No elevated `author-learning` skill/surface in must-read SoT (elevate deferred).
- `GAP` No closeout→harvest hook text in `implementation-closeout` today.
- `GAP` Host default path for standards catalog/profiles remains OPEN at Theme 16 D4 (lean examples only); this gatherer did not open template files beyond skill pointers.
- `GAP` Cursor AGENTS.md vs Team/Project/User alwaysApply win-order remains product-undefined (Theme 16 retained GAP) — do not invent precedence for author-learning routing.
- `OPEN` T24A: when to run/skip (including closeout hook shape).
- `OPEN` T24B: candidate atom fields + evidence requirements.
- `OPEN` T24D: author-learning skill/rule/hook shape and Cursor affordances.
- `OPEN` T24E: elevate + smoke refuse auto-accept.
- `OPEN` Whether personal (non-workspace) memory is ever a secondary channel — Theme 24 parks it as primary SoT; no further local API found.

## 8. Implications (INFERENCE only)

Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] Author-learning should be a **router/harvester** that emits structured **proposed** deltas and then hands to existing skills: `author-standards` (principles/standards/derive), `author-agents-md`, `author-cursor-surfaces` (host path only), `research-draft-adr` — not a new standards body. Premises: §4.4 FACT table; Theme 24 Target; Theme 16 O1.
- `INFERENCE` [E4] Learning **target** must stay host/workspace surfaces; edits to Toolbelt plugin `skills/*` are Theme 23/playbook/maintenance concerns, not Theme 24 harvest. Premises: Theme 24 Target; Theme 23 fence; author-cursor-surfaces location clarify.
- `INFERENCE` [E4] **Never auto-accept** must remain hard: proposed-only until human accept, same as derive/ADR/surfaces. Premises: Theme 24 Hard fence; Theme 16 D12; draft-is-not-sot.
- `INFERENCE` [E4] Optional **post-closeout** invoke is consistent with shipped closeout optionality; wiring is still OPEN (T24A). Premises: §4.5.
- `INFERENCE` [E4] Conflict stack for routing contested learnings: prefer ADR-sized → ADR; principles vs standards split already in author-standards; inferred-from-code is lowest. Premises: Theme 16 D5/D6; author-standards step 7.

## 9. Source list (deduped)

1. `d:\Toolbelt\docs\research\notes\theme-24-author-learning\campaign-brief.md`
2. `d:\Toolbelt\docs\research\notes\theme-24-author-learning\deep-campaign-board.md`
3. `d:\Toolbelt\docs\research\reports\theme-16-host-standards.md`
4. `d:\Toolbelt\docs\research\reports\theme-15-closeout-readiness.md`
5. `d:\Toolbelt\docs\research\reports\theme-23-host-playbook.md` (fences / D1 / D10 only)
6. `d:\Toolbelt\skills\author-standards\SKILL.md`
7. `d:\Toolbelt\skills\author-agents-md\SKILL.md`
8. `d:\Toolbelt\skills\author-cursor-surfaces\SKILL.md`
9. `d:\Toolbelt\skills\implementation-closeout\SKILL.md`
10. `d:\Toolbelt\skills\research-draft-adr\SKILL.md` (ADR handoff row; opened for table completeness)
11. `d:\Toolbelt\rules\draft-is-not-sot.mdc`
12. `d:\Toolbelt\rules\standards-resolve-gate.mdc`
13. `d:\Toolbelt\docs\PROTOCOL.md` (grades / cite-or-omit / depth skim)
14. E0 Glob: `docs/standards/index.md` absent under `d:\Toolbelt` (2026-08-05)
