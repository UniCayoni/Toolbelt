---
title: "Theme 5 — Normal scoping for deep-track prep"
status: draft
theme: theme-5-design
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: normal
campaign_phase: brief_scoping
note: >
  Post-scope decision: T5C deferred from active Theme 5 deep campaign;
  see t5c-ux-placeholder.md. This note still records T5C prep for when re-opened.
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
supersedes: null
---

# Theme 5 — What each track needs for deep research

**Using `research-protocol`** · depth: **normal** (scoping only — not Wave 1 of the deep campaign).

**Question:** For each of T5A–T5D, what must deep research cover, which sources/corpora are ready, and where are the caveats / GAPs?

---

## 1. Scope

- In: Inventory of deep Wave targets, Alexandria readiness, primary URL targets, false-friend risks, recommended gatherer slices
- Out: Running deep Wave 1–3; writing Design skills; locking methods

---

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | normal |
| Tools | Alexandria `list_corpora`, `list_documents`, `rag_probe`; WebSearch; local Theme 2 report (ADR facts) |
| Corpora | `software_engineering` (21 docs), `ai_llm_agents` (71), `game_design` (58), `programming_algorithms_systems` (23), `games_engine_graphics` (listed, not deeply probed) |
| Queries | ADR/tradeoffs; HITL agent design; UX/a11y; MDA/systems/narrative |
| What was *not* searched | Full `rag_query` evidence pulls; Cursor Plan Mode product docs pin; exhaustive Superpowers SKILL.md read; WCAG normative text beyond discovery |
| Stop_reason | N/A — normal mode done when per-track deep-prep is actionable |

---

## 3. Cross-track findings

- `FACT` [E0] Alexandria corpora available for Theme 5: `software_engineering`, `ai_llm_agents`, `game_design`, `programming_algorithms_systems`, `games_engine_graphics` (plus unrelated shelves). [E0: `list_corpora` 2026-07-29]
- `FACT` [E0] No dedicated HCI / UX / WCAG shelf exists. [E0: corpus inventory]
- `CLAIM` [E2] Theme 2 already established ADR/MADR as decision-rationale layer (Nygard, Fowler, MADR). T5A/T5B deep should **reuse** Theme 2 facts, not re-litigate ADR existence. [E2: `docs/research/reports/theme-2-agent-usable-documentation.md` §2.5]
- `INFERENCE` [E4] T5C deep will be **web/E1-heavy**; Alexandria is secondary at best for product UX. Premises: (1) no UX corpus [E0]; (2) SE UX probe returned AI-coding books, not HIG/WCAG [E0 probe].
- `INFERENCE` [E4] T5D has the strongest RAG shelf for domain content; agent *workflow* for creative design remains a likely GAP. Premises: (1) 58 `game_design` docs [E0]; (2) scoping web shows agent skills as E3 community patterns.

---

## 4. Per-track deep-prep

### T5A — Agent / AI-assisted design process

| Need for deep | Detail |
|---------------|--------|
| Core questions | Human design loop (options→tradeoffs→decide→record); agent roles (propose/critique/draft); HITL gates; relationship to ADR/AgDR; anti-patterns (vibes-only, premature lock) |
| Wave 1 (primary) | Nygard ADR (Cognitect 2011); Fowler ADR bliki; MADR; reuse Theme 2 ADR FACTS |
| Wave 2 | Alexandria `ai_llm_agents` (agent books — orchestration/HITL); `software_engineering` (*Beyond Vibe Coding*, *AI-Assisted Programming* — grade carefully); Superpowers `brainstorming` / `writing-plans` **structure inventory** (E3); AgDR / decision-audit community specs (E3→corroborate or GAP) |
| Wave 3 | Residual: vendor Plan Mode docs only if still OPEN after W1–2 |
| Alexandria readiness | `ai_llm_agents` probe HITL/design → **partial**; `software_engineering` ADR probe → **partial** (top hits skewed to Clean Code / Framework Guidelines — false friends) |
| Caveats | Do not treat Superpowers or AgDR as universal SoT; separate **decision records** (Theme 2) from **agent process orchestration**; RAG “agent design” often means multi-agent *systems*, not product design loops |

**Recommended deep gatherer slices (T5A):**

1. Decision-record lineage (ADR/MADR) + Theme 2 cross-link  
2. Agent-assisted design process (HITL, critique, alternatives) from E1/E2 books + vendor docs  
3. Community agent workflows (Superpowers, AgDR) — structure only, E3  

### T5B — Technical design

| Need for deep | Detail |
|---------------|--------|
| Core questions | Architecture styles & tradeoffs; modular boundaries; stack/feature design criteria; services/apps as design concerns; clean/standards as *constraints* (contested); agent-assisted architecture |
| Wave 1 | Clean Architecture (Martin blog + book in SE corpus); GoF Design Patterns (in corpus); Framework Design Guidelines (.NET — in corpus); AWS ADR PG / Fowler ADR (decision *when*) |
| Wave 2 | Modular monolith vs microservices debates (cite both); *Architecture Patterns with Python*; *Foundations of Scalable Systems*; *Software Architecture Metrics*; high-signal ADR/template repos (E3 discovery) |
| Wave 3 | Windows service / desktop app design only if still a named P0 GAP |
| Alexandria readiness | `software_engineering` **strong** for architecture/clean/patterns; `programming_algorithms_systems` **weak for design-intent** (algorithms/concurrency — use only when design of systems performance is in scope) |
| Caveats | Clean Code ≠ architecture SoT; grade schools of thought; Theme 1 recon ≠ this track; do not lock grey-matter stacks |

**Recommended deep gatherer slices (T5B):**

1. Architecture styles + dependency/modularity criteria  
2. Decision criteria for stack/feature/service boundaries + ADR trigger conditions  
3. Contested “clean” / standards literature (both sides) + agent-assisted technical design  

### T5C — Product / UX / UI — **deferred after this scope**

> Decision (2026-07-29): **not in active Theme 5 deep campaign**. Parked targets below remain valid for re-open. See [`t5c-ux-placeholder.md`](./t5c-ux-placeholder.md).

| Need for deep | Detail |
|---------------|--------|
| Core questions | UX process & IA; design systems vs one-offs; a11y as design constraint; agent-assisted flows/wireframes; critique/verification |
| Wave 1 | **WCAG 2.2** (W3C Recommendation); Apple HIG; Material Design 3 — pin versions in coordinator note |
| Wave 2 | Design-system method docs; WAI ARIA patterns; community design-system / checklist repos (E3); optional game_design UX-adjacent books only if clearly product-UI (else leave to T5D) |
| Wave 3 | Figma MCP / annotation tooling — methods only, not product locks |
| Alexandria readiness | **Weak / absent as UX SoT.** SE UX probe → *Beyond Vibe Coding* etc. (false friends). No WCAG/HIG in catalog. |
| Caveats | Taste ≠ research; AI UI generators ≠ methods; do not collapse into T5B; Toolbelt frontend user-rule aesthetics = E0 preference only |

**Recommended deep gatherer slices (T5C):**

1. Accessibility + platform HIG (E1 web)  
2. UX process / design systems methods (E1/E2 web)  
3. Agent-assisted UI design + verification (E2/E3; mark GAP if thin)  

### T5D — Creative & game systems

| Need for deep | Detail |
|---------------|--------|
| Core questions | Systems design loops; MDA-class lenses; narrative methods; world bibles; character consistency; agent critique roles |
| Wave 1 | MDA paper (Hunicke et al. PDF — E1 web); Schell *Art of Game Design* (in corpus); Adams *Fundamentals* / mechanics texts; Sellers *Advanced Game Design* |
| Wave 2 | Narrative toolbox / interactive story; worldbuilding guides; GUR / Games User Research (method, not marketing); high-signal GDD/template repos (E3); engine corpus only when design-relevant |
| Wave 3 | Agent-specific creative workflows if still GAP after W2 |
| Alexandria readiness | `game_design` **strong** (58 docs: Schell, Adams, Sellers, Zubek, narrative, worldbuilding, systems). Probe MDA/systems → **partial** but high max scores on systems texts. |
| Caveats | Plural methods — no single story SoT; TTRPG/GM books ≠ video-game systems law; IP when sampling; do not apply MDA as code-architecture law; separate systems vs narrative gatherers if notes explode |

**Recommended deep gatherer slices (T5D):**

1. Systems / MDA / mechanics–dynamics–aesthetics  
2. Narrative + quests + interactive story  
3. Worldbuilding + characters + consistency constraints  
4. (Optional W3) Agent creative critique patterns  

---

## 5. Corpus readiness summary

| Track | Primary Alexandria | Verdict | Deep implication |
|-------|-------------------|---------|------------------|
| T5A | `ai_llm_agents` + SE | partial | Wave 1 must be web/E1 ADR + process; RAG corroborates agent books |
| T5B | `software_engineering` | strong (arch) | Wave 1 can lean RAG + classic E1 URLs; algorithms corpus secondary |
| T5C | *(none dedicated)* | weak/absent | Wave 1 almost entirely official web (WCAG/HIG/Material) |
| T5D | `game_design` | strong | Wave 1 can lean RAG + MDA PDF; still need agent-workflow GAP hunt |

---

## 6. GAPs / OPEN (scoping)

- `GAP` Dedicated UX/HCI Alexandria coverage for T5C. Searched: corpus list + SE UX probe. Result: no shelf; false friends.
- `GAP` Standalone MDA paper may not be ingested (web E1 still required).
- `OPEN` Whether Cursor Plan Mode / vendor design modes warrant a pinned D0 for T5A Wave 1 — decide at deep kickoff.
- `OPEN` Whether T5D should hard-split systems vs narrative into two deep fleets (budget call).

---

## 7. Sources (scoping)

1. Alexandria `list_corpora` / `list_documents` / `rag_probe` — 2026-07-29  
2. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — Nygard ADR  
3. https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — Fowler ADR  
4. https://www.w3.org/TR/WCAG22/ — WCAG 2.2  
5. https://users.cs.northwestern.edu/~hunicke/MDA.pdf — MDA  
6. https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — Clean Architecture  
7. Theme 2 report — ADR/MADR FACTS  
8. Web discovery: AgDR, Superpowers brainstorming (E3 only)
