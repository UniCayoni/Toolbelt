---
title: "Theme 5 — Design pocket deep research campaign brief"
status: draft
theme: theme-5-design
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: deep
campaign_phase: accepted_elevated
aligned_with:
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
  - docs/research/reports/theme-4-cursor-plugin-components.md
  - docs/research/notes/theme-5-design/scope-normal-deep-prep.md
  - docs/research/notes/theme-5-design/t5c-ux-placeholder.md
supersedes: null
---

# Theme 5 — Design campaign brief

**Using `research-protocol`** (campaign planning — **deep gatherers not launched**).

**Status:** `draft` brief. Not Design SoT. Not permission to write Design skills yet.

**Active deep tracks:** **T5A, T5B, T5D** only.  
**Deferred:** **T5C** (Product/UX/UI) — placeholder only until RAG or equivalent queryable corpus is ready. See [`t5c-ux-placeholder.md`](./t5c-ux-placeholder.md).

**Scoping evidence:** [`scope-normal-deep-prep.md`](./scope-normal-deep-prep.md) (2026-07-29).

---

## 1. Purpose

| Field | Value |
|-------|-------|
| Pocket | **Design** (next after Research) |
| Goal | Evidence-backed methods for **how to design** (with AI/agents and without), across design *types*, so Toolbelt can later elevate Cursor surfaces via `author-cursor-surfaces` |
| Depth | **`deep` for active tracks** (T5A, T5B, T5D) — each runs Wave 1→2→3 + stop rule; then cross-track integrate |
| Deferred | **T5C** — not in this campaign wave; re-open per placeholder readiness gate |
| Non-goal now | Writing production Design skills mid-research; locking stacks/libraries; Brain/RAG product MVP; running T5C deep without readiness |

Ladder: Research (Themes 1–4) → **Design (this campaign)** → later Build/Verify packs as needed.

---

## 2. Campaign scale & caution (read first)

This is a **large multi-track deep campaign**, not one normal lookup. Scoping confirmed **uneven corpus readiness** and **different false-friend risks per track** — treat each track’s caveats as first-class.

| Risk | Mitigation |
|------|------------|
| Scope explosion (“design everything”) | **Three active** isolated tracks (+ T5C placeholder); no cross-contamination (architecture ≠ worldbuilding) |
| Context / agent fleet burnout | Low-return detect → **+1 residual stage** → hard stop (§4.3); stagger T5A then T5B+T5D |
| False universal skill | Integrator must **reject** one mega-skill that claims to cover all design types (incl. claiming UX while T5C deferred) |
| Draft inflation | All notes/reports stay `draft` until human **accept**; elevate only after accept + `author-cursor-surfaces` |
| Cursor packaging drift | Design *methods* ≠ Cursor plugin contracts; Theme 4 remains SoT for surfaces |
| Weak E3 / star-chasing | High stars = discovery; corroborate with E1/E0/E2 before locks |
| RAG false friends | “agent design” often means multi-agent *systems*, not product design loops; TTRPG books ≠ video-game systems law |
| Uneven Alexandria | T5B/T5D RAG-strong; T5A partial; **T5C deferred** until UX shelf or queryable site corpus |

**Hard rule:** Do not start deep Wave 1 gatherers until this brief is human-approved (or explicitly waived).

---

## 3. Tracks — deep prep (from normal scope)

**Active tracks** below **must** apply `research-depth-modes`: Wave 1 primary → Wave 2 corroboration → Wave 3 residual GAPs → track draft synthesis. Then campaign integrator → Theme 5 report(s) for **T5A/B/D** (T5C listed as deferred/OPEN only).

### T5A — Agent / AI-assisted design process (spine)

| Field | Value |
|-------|-------|
| Question | How should humans + coding/creative agents run a **design process** (options, constraints, tradeoffs, decision, record)? |
| Why first | Shared spine for T5B/T5D (and later T5C); prevents each domain reinventing “how to decide” |
| In scope | Design loops, critique, alternatives matrices, ADRs/design docs, agent roles (propose/critique/decide), HITL gates, anti-patterns |
| Out of scope | Domain content of games/UI/arch; Cursor plugin FM (Theme 4); re-litigating Theme 2 ADR existence |
| Alexandria | `ai_llm_agents` + `software_engineering` — probes **partial**; ADR queries false-friend to Clean Code / Framework Guidelines |
| Caveats | Process lit ≠ product law; human methods ≠ agent orchestration ≠ coding-agent decision capture; Superpowers/AgDR = E3 structure inventory only |

**Deep must cover (scoping):**

| Wave | Targets |
|------|---------|
| W1 | Nygard ADR; Fowler ADR; MADR; **reuse Theme 2 ADR FACTS** |
| W2 | Agent HITL/critique books in `ai_llm_agents`; *Beyond Vibe Coding* / *AI-Assisted Programming* (grade carefully); Superpowers `brainstorming`/`writing-plans` structure; AgDR/community decision-audit (E3→corroborate or GAP) |
| W3 | Vendor Plan Mode docs only if still OPEN |

**Gatherer slices:** (1) ADR/MADR + Theme 2 cross-link · (2) Agent-assisted design process · (3) Community agent workflows (E3)

---

### T5B — Technical design

| Field | Value |
|-------|-------|
| Question | How to design **code architecture, features, stacks, services/apps, coding/clean standards** (design-time), including with agents? |
| In scope | Architecture styles/tradeoffs, modular boundaries, stack selection *criteria*, Windows services/desktop as design concerns, clean/standards as constraints, feature design before implement |
| Out of scope | Full lint catalogs; grey-matter stack locks; Theme 1-style comprehension-only recon |
| Alexandria | `software_engineering` **strong** (Clean Architecture, GoF, Clean Code, scalable systems, architecture metrics, AI-assisted programming). `programming_algorithms_systems` **weak for design-intent** — secondary only |
| Caveats | “Clean code” contested — cite both sides; stack picks need criteria not fads; Windows-specific ≠ portable architecture |

**Deep must cover (scoping):**

| Wave | Targets |
|------|---------|
| W1 | Martin Clean Architecture (blog + corpus book); GoF; Framework Design Guidelines; ADR *when to decide* (AWS PG / Fowler) |
| W2 | Modular monolith vs microservices (both sides); Architecture Patterns with Python; Foundations of Scalable Systems; Architecture Metrics; high-signal ADR/template repos (E3) |
| W3 | Windows service/desktop design only if named P0 GAP remains |

**Gatherer slices:** (1) Architecture styles + modularity · (2) Stack/feature/service criteria + ADR triggers · (3) Contested clean/standards + agent-assisted technical design

---

### T5C — Product / UX / UI design — **DEFERRED (placeholder)**

| Field | Value |
|-------|-------|
| Status | **Not in active campaign** — see [`t5c-ux-placeholder.md`](./t5c-ux-placeholder.md) |
| Question (held) | How to design **UI, UX systems, interaction, information architecture** with/for agents? |
| Why deferred | No UX/HCI Alexandria shelf; web-only deep would be thin / over-claim prone |
| Re-open when | (1) UX corpus ingested + good `rag_probe`, **or** (2) documented queryable site corpus with high-signal hits, **or** (3) human waives and accepts web/E1-first deep |
| Deep gatherers | **Do not launch** until readiness gate passes |

Parked wave targets and caveats remain in the placeholder + scoping note — not copied here as active work.

---

### T5D — Creative & game systems design

| Field | Value |
|-------|-------|
| Question | How to design **game systems, storylines, worldbuilding, characters/personalities** (and similar creative systems) with/for agents? |
| In scope | Systems design loops, narrative structure methods, world bibles, character consistency, play/fantasy constraints, agent roles for creative critique |
| Out of scope | Shipping a game engine; locking GreyMatter creative stack; fan wikis as E1 |
| Alexandria | `game_design` **strong** (58 docs: Schell, Adams, Sellers, Zubek, narrative, worldbuilding, systems). `games_engine_graphics` only when design-relevant |
| Caveats | Creative process is plural; TTRPG/GM books ≠ video-game systems law; IP when sampling repos; do not apply MDA as code-architecture law; agent-specific creative workflow likely GAP |

**Deep must cover (scoping):**

| Wave | Targets |
|------|---------|
| W1 | MDA paper (Hunicke et al. PDF — E1 web; may be absent from RAG); Schell *Art of Game Design*; Adams fundamentals/mechanics; Sellers *Advanced Game Design* |
| W2 | Narrative/interactive story; worldbuilding; GUR methods; GDD/template repos (E3) |
| W3 | Agent creative critique patterns if still GAP |

**Gatherer slices:** (1) Systems / MDA · (2) Narrative · (3) Worldbuilding + characters · (4 optional W3) Agent creative critique  

**Budget OPEN:** hard-split systems vs narrative into two fleets if notes explode.

---

## 4. Shared research protocol (all tracks)

### 4.1 Depth (mandatory)

For **each active** track (T5A, T5B, T5D):

1. Coordinator pin (scope, date, corpora)  
2. **Wave 1** — primary / canonical methods (E1/E2 preferred)  
3. **Wave 2** — Alexandria + web + high-signal GitHub/repos  
4. **Wave 3** — residual GAP closers only  
5. Track synthesis note (draft)  

Then:

6. **Campaign integrate** → `docs/research/reports/theme-5-*.md` (draft) — T5C = deferred/OPEN link only  
7. Human accept (full / facts-only / slice)  
8. **Only then** elevate Design skills/rules via `/author-cursor-surfaces` (no UX skill from this wave)

### 4.2 Evidence discipline

- Cite-or-omit; FACT/CLAIM/INFERENCE/GAP/OPEN; E0–E4/U  
- Prefer GAP over invention  
- Conflicts: both sides; higher grade wins; runtime E0 when applicable  
- Stars/downloads = **discovery**, not acceptance  
- Theme 2 ADR FACTS are reusable; do not duplicate as new research theater  

### 4.3 Stop rule (per track + campaign)

Base signals (from `research-depth-modes`) that a track is in **low return**:

- New notes only restate FACTS without closing named GAPs, **or**
- Residuals need unrun experiments / unavailable corpora, **or**
- User budget exhausted  

**Theme 5 refinement — +1 confirmation stage (mandatory for this campaign):**

| Step | Action |
|------|--------|
| 1. Detect | Coordinator records `low_return_detected` (which signal, which wave/note IDs) |
| 2. +1 stage | Run **exactly one** more residual stage on that track — only named P0/P1 GAPs that might still close; no new open-ended fleets |
| 3. Hard stop | After that +1 stage, **stop** that track’s gatherers even if some GAPs remain → leave as confirmed `GAP`/`OPEN` |
| 4. Record | Method: `stop_reason` = `low_return_plus_one` (or `budget` / `unavailable` if those short-circuit) |

**Short-circuit (no +1):** If the signal is **user budget exhausted**, or residuals are clearly **unavailable** (no corpus, no runnable experiment), hard-stop immediately — do not spend the +1 stage.

Do **not** chain multiple “+1” stages. One confirmation stage per track after first low-return detect, then stop.

Campaign-level stop: after **T5A, T5B, and T5D** syntheses exist **or** human truncates remaining *active* tracks with explicit waiver. T5C deferred does **not** block campaign stop.

### 4.4 Note paths

```text
docs/research/notes/theme-5-design/
  campaign-brief.md              ← this file
  scope-normal-deep-prep.md      ← normal scoping (done)
  t5c-ux-placeholder.md          ← T5C deferred (no gatherers)
  t5a-*/ t5b-*/ t5d-*/           ← deep gatherer notes (later)
docs/research/reports/
  theme-5-design-*.md            ← integrated T5A/B/D (later, draft until accept)
```

### 4.5 Parallelism

| Phase | Parallelism |
|-------|-------------|
| Brief + normal scope | Serial (done) |
| T5A Wave 1–3 | Deep fleet for T5A only (**recommended first**) |
| T5B / T5D | May run **in parallel after T5A spine synthesis** |
| T5C | **No fleet** until placeholder readiness gate |
| Integrate | Serial merge; no new facts; no invented T5C |

**Default recommendation:** Complete **T5A** through track synthesis before launching T5B+T5D deep fleets.

### 4.6 Coexistence

- Superpowers may dispatch agents; Toolbelt owns templates/grades/depth/stop  
- Inventory Superpowers design skills as **E3 process structures** in T5A — do not merge git/PR policies  
- Do not invent Design skills during gatherer waves  
- `author-cursor-surfaces` is for **post-accept** elevation  

---

## 5. Candidate elevation targets (post-accept only — not commitments)

Illustrative; final skill set requires accepted Theme 5 + human choose:

| Candidate surface | Likely track | Notes |
|-------------------|--------------|-------|
| Design-process skill (options→tradeoffs→decision→ADR) | T5A | Spine; coexist with Superpowers brainstorming |
| Technical design / architecture skill | T5B | Point at `draft-adr`; not a lint pack |
| UX/UI design skill | T5C | **Deferred** with track — elevate only after T5C deep + accept |
| Creative/systems / narrative skill(s) | T5D | May split systems vs narrative |
| Thin always-on rule: “draft design ≠ accepted architecture” | cross | Mirror draft≠SoT |

Pack stub: future Design pocket under `docs/packs/` (README already notes Theme 5).

---

## 6. Out of scope for Theme 5 (this campaign wave)

- **T5C deep research** (deferred — placeholder only)  
- Implementing game/engine/UI product features  
- Grey-matter Brain stack locks  
- Expanding Research pocket with more lookup skills  
- Cursor plugin packaging research (Theme 4 owns it)  
- Hard hooks / marketplace submission  

---

## 7. Approval gate

Before deep Wave 1:

- [x] Human approves this brief (with amendments below) — 2026-07-29  
- [x] Track order: **T5A first**, then parallel T5B+T5D after spine synthesis  
- [x] T5D: start as **single fleet**; hard-split systems vs narrative only if notes explode  
- [x] Budget: stagger per §4.5; apply **+1 confirmation stage** stop rule (§4.3)  
- [x] **T5C deferred** — placeholder until RAG/queryable corpus ready  

**Amendments from human:**

| Item | Decision |
|------|----------|
| T5C | **Defer** — placeholder; not in active campaign until readiness gate |
| Track order | **T5A first**, then T5B+T5D |
| T5D split | Single fleet default; split if explode |
| Stop rule | **+1 residual stage** after low-return detect, then hard stop (`low_return_plus_one`) |
| Budget notes | Stagger; no endless fleets |
| Extra in/out of scope | T5C out of this wave |

**Kickoff:** Brief is ready for deep Wave 1 on **T5A** when you say go.

---

## 8. Method (this brief)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Depth | deep (campaign definition); scoping + T5C defer + stop-rule +1 |
| Tools | Read PROTOCOL, depth-modes, Theme 2/4; Write brief / T5C placeholder |
| What was *not* searched | Deep Wave 1 fleets; full rag_query; UX corpus ingest |
| Stop_reason | N/A — brief phase (campaign uses `low_return_plus_one`) |

## 9. Sources for brief framing

1. [`scope-normal-deep-prep.md`](./scope-normal-deep-prep.md) — normal scoping  
2. [`t5c-ux-placeholder.md`](./t5c-ux-placeholder.md) — T5C defer  
3. Toolbelt `docs/templates/research-depth-modes.md`  
4. Toolbelt `docs/PROTOCOL.md`  
5. Theme 2 / Theme 4 reports  
6. Coordinator discussion 2026-07-29 (Design pocket + T5C defer)
