---
title: "T5D Wave 2 — Corroboration (narrative, worldbuilding, GUR, GDD E3)"
status: draft
theme: theme-5-design
track: T5D
wave: 2
slice: T5D-W2
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5d-w2-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5d-coordinator-pin.md
  - docs/research/notes/theme-5-design/t5d-w1-s1-systems-mda.md
  - docs/research/notes/theme-5-design/t5d-w1-s2-narrative.md
  - docs/research/notes/theme-5-design/t5d-w1-s3-worldbuilding-characters.md
  - docs/PROTOCOL.md
---

# T5D-W2 — Corroboration (narrative / worldbuilding / GUR / GDD E3)

**Using `research-protocol`; depth: deep; wave: 2; slice: T5D-W2.**

**Status:** `draft`. Not Design SoT. Does **not** restate W1 E1/E2 FACTS as new primary law — corroborates, fills named W1 GAPs where evidence allows, or marks `GAP`. Creative process remains **plural**. **TTRPG/GM ≠ video-game systems law.**

## 1. Scope

- Question / goal: Corroborate T5D Wave-1 slices with Alexandria `game_design` + light web — narrative/interactive story/quests (W1 S2 GAPs), worldbuilding consistency methods (W1 S3), Games User Research **methods** (not marketing), GDD/template repos (**E3 discovery only**).
- In scope: Assigned W2 lanes; graded cites with chunk_id / URL; false-friend watch (TTRPG vs VG; GUR vs QA/bugfix; stars ≠ SoT).
- Out of scope: Re-deriving MDA (W1 S1); shipping engines; GreyMatter stack locks; elevating Design skills; inventing machine schemas; treating community GDD templates as industry law; deep agent creative-critique process (W3 residual if still GAP).
- Comprehension / research goal type: other (secondary corroboration + method inventory)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria MCP `list_documents`, `rag_query`, `rag_fetch_chunk`; WebSearch; `gh api` (repo metadata); Read of W1 S1/S2/S3 + coordinator pin + research-note template; research-protocol skill |
| Corpora / URLs searched | Alexandria corpus=`game_design`; https://www.inklestudios.com/ink/ ; https://github.com/inkle/ink ; https://twinery.org/ ; https://doi.org/10.14746/i.2021.38.01 ; GitHub GDD template repos (see §4.4) |
| Queries (exact) | Alexandria: `Game Narrative Toolbox interactive story structure branching quest design methods story beats player agency`; `worldbuilding consistency methods world bible continuity constraints world rules magic system coherence focus`; `games user research methods playtesting usability heuristics observational methods think-aloud survey interview RITE GUR methodology`; `RITE Rapid Iterative Test and Evaluation method fix issues between testers playtest procedure Medlock` (path_prefix=`Games User Research`); `branching with state narrative patterns linear branch and merge quest composition story and agency consistency` (path_prefix=`Elements of Game Design`); `world-building toolkit lore storysense consistency documentation for team animators artists constraints Collas`; `Story and Agency Consistency fiction world rules player agency tradeoff` (path_prefix=`Elements of Game Design`). Web: `game design document GDD template github open source`; `ink narrative scripting language Inkle documentation interactive story`; `Mochocki Koskimaa story beats GARO videogames unit operations`; `Twine interactive fiction documentation twinery.org`. Catalog: `list_documents` name_substring=`User Research` / `Narrative` / `Toolbox` / `Play` |
| What was *not* searched | Full *Game Narrative Toolbox* 1st book (absent from corpus catalog); Articy/Yarn primary docs deep; studio-internal BioWare/CDPR GDD law; Gygax method mine (W1 S3 GAP retained); agent creative-critique corpora (`ai_llm_agents`); `games_engine_graphics`; Adams *Fundamentals* body re-chase (W1 S1 GAP — not W2 target); biometric GUR deep beyond overview |
| Depth | deep |
| Waves / stop_reason | wave: **2** (slice T5D-W2). stop_reason: **w2_targets_covered_diminishing_returns** — GUR handbook + Zubek narrative patterns + Heussner/Collas worldbuilding consistency + light E1 tooling + E3 GDD inventory complete for assigned lanes; further same-book RAG would restate. Residual P0 → W3 |
| Provenance (optional PROV) | Entity←game_design books + official tooling sites + GitHub metadata; Activity=T5D-W2 corroboration; Agent=gatherer-t5d-w2-grok + Alexandria MCP + WebSearch/gh |

### 2.1 Catalog presence (E0)

- `FACT` [E0] `list_documents` name_substring=`User Research` → *Games User Research* (Drachen, Mirza-Babaei, Nacke eds.) source_id=`06ce8783a4479988`, 646 chunks. [E0: Alexandria list_documents — 2026-07-29]
- `FACT` [E0] name_substring=`Narrative` → Howard *Quests*; Serpa *Cores of Game Design*; Heussner *Advanced Game Narrative Toolbox* — **no** separate “Game Narrative Toolbox” (1st book) title in corpus. [E0: same]
- `FACT` [E0] name_substring=`Toolbox` → only Heussner *Advanced…* (source_id=`76ab3482295a5954`). [E0: same]

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Wave-2 corroboration against fixed W1 notes; not workspace recon |
| Scope boundary | `game_design` + light web/GitHub; cite only retrieved locators |

## 4. Findings

Lane labels: **A** narrative/quests · **B** worldbuilding consistency · **C** GUR methods · **D** GDD/templates E3.

### 4.1 Lane A — Narrative / interactive story / quests (fill W1 S2 GAPs)

**Corroboration of plural structure families (W1 S2 H1)**

- `FACT` [E2] Zubek (*Elements of Game Design*) catalogs narrative **choice topologies**: linear; branching; branch-and-merge; hub-and-spokes; then **composition** of small modules (often as quests/missions) into larger arcs; open-world as dense mesh of quests with main + side content. [E2: Alexandria corpus=`game_design` source=`Elements of Game Design…Zubek…epub` chunk_ids=`326f5263ce5c502970a09b63`, `b5604dfa71936b104026fb10`, `6300c45bc40fff20e79c5451`, `b81816547c47e9677e453326`, `b1e8c194f49b5fb8e906a31a` query=`branching with state…`]
- `FACT` [E2] Zubek: simple branching suffers **combinatorial explosion**; branch-and-merge reduces authoring cost but can yield illusory choices from a bird’s-eye view (often opaque on first playthrough). [E2: same source chunk_id=`b5604dfa71936b104026fb10`]
- `FACT` [E2] Zubek: **branching with state** (global/character/relationship variables queried later) is common in IF/adventure/VN; increases “spooky action at a distance” authorial/debug complexity. Hub-and-spokes increases order agency vs directed acyclic graphs. [E2: same source chunk_id=`6300c45bc40fff20e79c5451`]
- `FACT` [E2] Zubek quest module: short task-driven narrative with start conditions, end points, success/failure consequences; open worlds need **persistent stateful** quest/world tracking; special quest items can encode unlock coupling for authoring/debug. [E2: same source chunk_ids=`b81816547c47e9677e453326`, `b1e8c194f49b5fb8e906a31a`, `ac94a86ad5e4a183b470db40`]
- `INFERENCE` [E4] Zubek’s topology + quest-composition model **corroborates** W1 S2 Schell/Kramarzewski/Heussner/Howard plurality (pearls/modular/hub/open/state machines) without replacing them. Premises: W1 S2 Lane A FACTS/CLAIMS; Zubek §4.1 FACTs.

**Story ↔ fiction consistency bind (W1 S3 × S2 gap)**

- `FACT` [E2] Zubek: story vs agency is a spectrum (tight CYOA ↔ sandbox); commercial games occupy middle ground with ad hoc constraints (e.g. unkillable quest NPCs). When fiction is present, **gameplay and fiction must match**; violations include fantasy-contradicting action limits and **ludonarrative dissonance** (Hocking). Agency requires intentional action **plus** understandable action→outcome feedback. [E2: Alexandria corpus=`game_design` source=`…Zubek…` chunk_ids=`65b960bf5a4566c70d4fb97f`, `7b18eb988e69f2c900e1e354`, `bbc9d97b9a00874b18fd9900` query=`Story and Agency Consistency…`]
- `FACT` [E2] Heussner *Advanced Game Narrative Toolbox*: without thorough world-building, risk of internal inconsistencies/stereotypes and weaker narrative pipeline/artist guidelines; distinguishes **world-building** vs **lore** vs **storysense** (Kelly) vs environmental storytelling; team nomenclature consistency is a communication cost control. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_ids=`1a4e61601b07a2df218c6d18`, `83ae7ca545e50e47da4e5a2b` query=`world-building toolkit…`]
- `INFERENCE` [E4] W1 S3 world-bible constraints and W1 S2 quest/beat↔state methods meet at Zubek’s fiction–gameplay consistency + Heussner nomenclature/lore split — a **VG narrative-world bind**, not a TTRPG rulebook bind. Premises: above FACTs; W1 S3 Lane D medium distinction.

**Tooling SoT discovery (W1 S2 GAP: Twine/ink)**

- `FACT` [E1] ink (inkle) is a narrative scripting language for branching interactive stories; official site frames it as middleware for game engines; Inky editor + Writing with ink tutorial documented. [E1: https://www.inklestudios.com/ink/ — accessed 2026-07-29]
- `FACT` [E1] `inkle/ink` GitHub describes open-source ink language/runtime; points to WritingWithInk tutorial and Unity integration. [E1: https://github.com/inkle/ink — stars=`4875` via `gh api` 2026-07-29]
- `FACT` [E1] Twine is an open-source tool for interactive nonlinear stories published as HTML; official docs include Twine Reference + Cookbook; stories = passages; story formats handle playtime logic. [E1: https://twinery.org/ ; https://twinery.org/reference/en/index.html — accessed 2026-07-29]
- `GAP` Articy / Yarn Spinner primary documentation not fetched this wave. Searched: ink + Twine only. Follow-up: optional light E1 if Toolbelt needs tooling inventory completeness.
- `GAP` Tooling docs ≠ studio narrative pipeline law. Do not promote ink/Twine as required GreyMatter stack.

**GARO (W1 S2 H3)**

- `FACT` [E1] Mochocki & Koskimaa (2021) present GARO story beats as a **ludonarrative analysis** framework (microunits; unit operations + character action), with six beat types — not a studio production-pipeline standard. [E1: https://doi.org/10.14746/i.2021.38.01 — accessed 2026-07-29; corroborates W1 S2 E1 primary]
- `GAP` Studio-pipeline adoption of GARO as shared writer/designer grammar. Searched: DOI page + abstract context; Alexandria narrative books this wave. Result: academic framing only; **H3 remains open** (not confirmed as industry default).

**Still open from W1 S2**

- `GAP` Studio-primary narrative pipelines (BioWare/CDPR/etc. as design law) — not closed.
- `GAP` Machine-readable Toolbelt beat↔state schema — conceptual bridges strengthened (Zubek state/quest items; W1 Short qualities / Howard variables); **no shared contract invented**.
- `GAP` Unified industry quest template SoT — still plural checklists only.

### 4.2 Lane B — Worldbuilding consistency methods

**Corroboration of W1 S3 bible / focus / living document**

- `FACT` [E2] Hungerford (Kobold): world bible = shared “right answers”; living document with dated milestone drafts; key-facts-only (anti kitchen-sink dump); World/Cast/Appendices structure — **restates W1 S3 with same locators**, no contradiction. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`96b66444fa96442938413dfa`, `414702d6c75016e474a68ca0`, `0c80314681a37b3ead7a51e2`]
- `FACT` [E2] Baur: kitchen-sink design harms internal coherence; prefer **focus** under resource limits — corroborates W1 S3. [E2: same source chunk_id=`bd1c459c07ae309bb3d34a8f`]

**VG / interactive-story lane additions (beyond Kobold/TTRPG)**

- `FACT` [E2] Sybil Collas (in Lacombe et al. *Writing an Interactive Story*): lore coherence needs **documentation + coherence + human intelligence**; bible is imperative; documentation is for **other developers’ constraints**, not the writer’s own curiosity — role-targeted notes for animators / voice actors / environment artists; long backstory paragraphs are the wrong default. Universe should serve the story (stop gathering irrelevant facts). [E2: Alexandria corpus=`game_design` source=`Writing an Interactive Story…` chunk_id=`0bf880a9bf44084feadc87bb` query=`world-building toolkit…`]
- `FACT` [E2] Heussner world-building toolkit chapter: be **judicious** (ROI of worldbuilding time); document sparingly/effectively; color-code / outline for departments; more rules → higher change complexity (“butterfly effect”); sketch key tenets before connective tissue; pick battles with the team. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_ids=`83ae7ca545e50e47da4e5a2b`, `e657f9642fcfd331a31a5942`]
- `FACT` [E2] Krampe (Bonner ed. *Game World Architectonics*): VG worldbuilding involves interactive/responsive space, dynamic state models, and navigation/presence — distinct from static setting-bible completeness. Discovery corroboration of W1 S3 academic hit. [E2: Alexandria corpus=`game_design` source=`Game World Architectonics…` chunk_id=`6da4b7ab0422515256ccb2d5`]
- `INFERENCE` [E4] Consistency methods that transfer across media: living dated bible, focus/anti-KSD, role-targeted docs, rules+costs, skeptic alignment — **but delivery completeness still forks** by novelist / GM / published RPG / VG designer (W1 S3 Lane D; Cook). Premises: W1 S3 FACTs; Collas/Heussner FACTs above.
- `GAP` Gygax *World Builder* / *Nation Builder* method extraction — retained from W1 S3 (not mined this wave).
- `GAP` Dedicated VG systemic NPC / dialogue-tooling consistency pipeline literature — retained; Schell lenses + Collas role fields only partially close.

### 4.3 Lane C — Games User Research methods (method, not marketing)

- `FACT` [E2] *Games User Research* (Drachen, Mirza-Babaei, Nacke eds., OUP 2018) is present as a methods handbook: production process chapters + methods part covering surveys, interviews, observation, think-aloud, RITE, heuristics/playability, biometrics, reporting, game analytics. [E2: Alexandria corpus=`game_design` source=`Games User Research…Drachen…pdf` chunk_ids=`842a60ca2e7aa463d54e4a29`, `94d4292350f9a629490d1e76` query=`games user research methods…`]
- `FACT` [E2] Medlock overview (Ch.7): GUR methods table spans attitudes vs behaviors across lifecycle (envision → design/build → release → post-release), including A/B testing, benchmark/critical-facet/initial-experience/extended playtests, usability test, RITE, heuristic evaluation, interview, focus group, card sort, telemetry, ethnographic field study, diary studies, etc. — with explicit pros/cons per method. [E2: same source chunk_ids=`f0f5304b68e6dcb78bf605f8`, `ab7c375be69747a66b32ed46`]
- `FACT` [E2] Sangin (Ch.11): GUR data = **behaviors** (actions) and **attitudes** (opinions); direct observation is powerful but prone to interpretation/observer-expectancy/confirmation biases; plan observation protocols; structure usability-event capture. [E2: same source chunk_ids=`5b5b694c097be153f05f1992`, `3279ba35565e626557616ca8`]
- `FACT` [E2] Knoll (Ch.12): think-aloud = participant verbalizes thoughts during tasks; popular usability tool (cites NN/g “#1 usability tool” claim in chapter). [E2: same source chunk_id=`3279ba35565e626557616ca8`]
- `FACT` [E2] Medlock (Ch.13) **RITE**: discount usability test where analysis happens after each participant (or each day); **find a problem, fix a problem**; changed UI retested with subsequent users; requires change resources + decision-maker observation; philosophy often more portable than exact protocol; original case study Age of Empires II tutorial (Medlock et al. 2002). [E2: same source chunk_ids=`6bb709f3a16f409fe74e224e`, `11c848d4bc32df6da501bc95`, `f35b2b8048b7601b4595bb39`, `136e7c015223511995433446`]
- `FACT` [E2] Nacke framing: GUR combines HCI + game design + experimental psychology; practical aim to improve player experience; QA/bug testing is a **different** focus (technical errors). Mixed methods common; self-report alone loses real-time/under-the-hood data. [E2: same source chunk_id=`fa23b95d131b4c549e5683d5`]
- `FACT` [E2] Desurvire/Wixon PLAY + GAP heuristics and Paavilainen et al. playability/F2P heuristics appear as evaluator methods (expert review against principles), complementary to player testing — not a substitute for observational playtests. [E2: same source chunk_id=`94d4292350f9a629490d1e76`]
- `INFERENCE` [E4] For Toolbelt Design methods: treat GUR as the **empirical evaluation arm** of creative systems loops (W1 S1 playtest/designer loop), with plural method selection by question (attitude vs behavior; speed vs rigor). Do **not** equate GUR with marketing research or with QA. Premises: Medlock table; Nacke definition; RITE vs standard test.
- `GAP` Deep extraction of PLAY/GAP heuristic lists and full survey instrument design — overview only this wave.
- `GAP` Binding GUR methods to agent-run creative critique protocols — not in this handbook slice; → W3.

### 4.4 Lane D — GDD / template repos (E3 discovery only)

**Hard grade rule:** stars and template repos = **discovery inventory**, not Design SoT. No locks.

- `CLAIM` [E3] Community Markdown GDD template: `LazyHatGuy/GDDMarkdownTemplate` — “Game Design Document Markdown Template” intended for GitHub wiki; based on Artjom Kurapov template. [E3: https://github.com/LazyHatGuy/GDDMarkdownTemplate — stars=`53` via `gh api` 2026-07-29]
- `CLAIM` [E3] Beginner GDD template with advice/examples: `kosinaz/game-design-document-template-for-beginners` (MIT). [E3: https://github.com/kosinaz/game-design-document-template-for-beginners — stars=`40` via `gh api` 2026-07-29]
- `CLAIM` [E3] Web search also surfaces other community templates (e.g. LaTeX `miguelrsgoncalves/gdd_latex_template`; agent-oriented fork `wanghaisheng/openagenticgame-gdd` of LazyHatGuy). Treat as further E3 inventory only — **not** corroborated as industry standard. [E3: WebSearch `game design document GDD template github open source` — 2026-07-29]
- `GAP` Studio-authoritative GDD SoT / shared schema across AAA pipelines. Searched: public GitHub templates only. Result: plural community skeletons; no E1 studio law.
- `INFERENCE` [E4] GDD templates may later serve as **optional record shapes** under T5A decide→record vocabulary, but W2 evidence only supports E3 discovery. Premises: E3 CLAIMS; draft-is-not-sot; campaign “weak E3 / star-chasing” caveat.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W1 plural interactive-story methods corroborate under Zubek topologies | confirmed (this wave) | §4.1 Zubek FACTs |
| H2 | World bible + focus remain the continuity backbone; VG lane adds role-targeted docs | confirmed | §4.2 |
| H3 | GARO is studio-default beat grammar | open / weak | E1 academic only; no studio pipeline cite |
| H4 | GUR handbook supplies method family for playtest arm of T5D loops | confirmed (literature) | §4.3 |
| H5 | Public GDD repos can lock Toolbelt creative docs | rejected | E3 only; GAP for studio SoT |
| H6 | Agent creative critique patterns documentable from W2 shelves | rejected for W2 | Not in assigned corpora; remains W3 P0 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Completeness of world docs | Hungerford structured bible sections | Heussner/Collas document sparingly + role-targeted | Compatible: inventory ≠ dump to every reader; prefer role views (W1 conflict log retained) |
| Branch meaning | Branch-and-merge “illusory” (Zubek bird’s-eye) | Player first-play opacity (Zubek same) | Record both perspectives; no SoT |
| GUR vs playtest folklore | Schell/Sellers “playtest loops” (W1 S1) | Formal GUR method table (W2) | Complementary: S1 designer loop intent; W2 method menu for evaluation |
| TTRPG NPC fields vs VG | Ashworth GM aid (W1 S3) | Collas/Heussner VG team docs | Keep lanes; transfer fields only |

## 7. Gaps & OPEN

### Closed or softened this wave

- Softened: W1 S2 structure plurality (Zubek topologies).
- Softened: W1 S3↔S2 narrative-world bind (Zubek consistency + Heussner nomenclature).
- Softened: Twine/ink tooling SoT discovery (E1 light).
- Closed for W2 target: GUR methods inventory (E2 handbook).
- Closed for W2 target: GDD template **E3 discovery** (explicitly non-lock).

### Still GAP / OPEN (prefer GAP)

- `GAP` **Agent creative critique / HITL patterns for creative systems** (campaign W3; still P0).
- `GAP` Studio-primary narrative / GDD pipelines as law.
- `GAP` Machine-readable beat↔state / world-constraint schema (do not invent).
- `GAP` GARO industry adoption; Articy/Yarn deep; Gygax method mine; VG systemic NPC tooling.
- `GAP` Adams *Fundamentals* body cites (W1 S1; out of W2 lane).
- `OPEN` Whether Toolbelt ships a creative decision-record subtype vs ADR (cross T5A; integrator).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Candidate (draft) T5D evaluation envelope: pick structure family + bind beats/quests to state → constrain fiction with bible/role docs → evaluate with selected GUR methods (observation/RITE/heuristics/survey as fit) → human decide/record. Premises: §§4.1–4.3; W1 loops.
- `INFERENCE` [E4] Do not collapse Kobold/TTRPG worldbuilding law into VG systems law; use medium forks. Premises: W1 S3 Lane D; Krampe; campaign caveat.
- `INFERENCE` [E4] Public GDD templates are optional scaffolding at E3 — insufficient alone for Design pack locks. Premises: §4.4.
- **Non-lock reminder:** This note is `draft`.

## 9. Source list (deduped)

1. Robert Zubek — *Elements of Game Design* — Alexandria `game_design` source_id=`5d396d7aa9e0c4ca` — chunks incl. `326f5263ce5c502970a09b63`, `b5604dfa71936b104026fb10`, `6300c45bc40fff20e79c5451`, `b81816547c47e9677e453326`, `b1e8c194f49b5fb8e906a31a`, `ac94a86ad5e4a183b470db40`, `65b960bf5a4566c70d4fb97f`, `7b18eb988e69f2c900e1e354`, `bbc9d97b9a00874b18fd9900`, `881eb8a5daeaa90846eb7f6e` — **E2**
2. Tobias Heussner (ed.) — *The Advanced Game Narrative Toolbox* — source_id=`76ab3482295a5954` — chunks incl. `84bbf836a28b213352497837`, `1a4e61601b07a2df218c6d18`, `83ae7ca545e50e47da4e5a2b`, `e657f9642fcfd331a31a5942`, `054a2613b8ae6eced8579013` — **E2**
3. *Kobold Guide to Worldbuilding* — source_id=`27de5d0f404ae431` — chunks `96b66444fa96442938413dfa`, `414702d6c75016e474a68ca0`, `0c80314681a37b3ead7a51e2`, `bd1c459c07ae309bb3d34a8f` — **E2**
4. Lacombe, Feraud, et al. — *Writing an Interactive Story* — source_id=`333977d188c5a6a7` — chunk `0bf880a9bf44084feadc87bb` (Collas) — **E2**
5. Bonner (ed.) — *Game World Architectonics* — chunk `6da4b7ab0422515256ccb2d5` — **E2** discovery
6. Drachen, Mirza-Babaei, Nacke (eds.) — *Games User Research* — source_id=`06ce8783a4479988` — chunks incl. `842a60ca2e7aa463d54e4a29`, `94d4292350f9a629490d1e76`, `f0f5304b68e6dcb78bf605f8`, `ab7c375be69747a66b32ed46`, `5b5b694c097be153f05f1992`, `3279ba35565e626557616ca8`, `6bb709f3a16f409fe74e224e`, `11c848d4bc32df6da501bc95`, `f35b2b8048b7601b4595bb39`, `136e7c015223511995433446`, `fa23b95d131b4c549e5683d5`, `8f584ba651fc9e55784c8680` — **E2**
7. Mochocki & Koskimaa (2021) GARO — https://doi.org/10.14746/i.2021.38.01 — **E1**
8. ink official + GitHub — https://www.inklestudios.com/ink/ ; https://github.com/inkle/ink — **E1**
9. Twine official — https://twinery.org/ ; https://twinery.org/reference/en/index.html — **E1**
10. E3 GDD templates — https://github.com/LazyHatGuy/GDDMarkdownTemplate ; https://github.com/kosinaz/game-design-document-template-for-beginners — **E3**
11. W1 priors (local, not re-graded as new evidence): `t5d-w1-s1-systems-mda.md`, `t5d-w1-s2-narrative.md`, `t5d-w1-s3-worldbuilding-characters.md` — **E0** pin/context
12. Campaign / coordinator pins — `campaign-brief.md`, `t5d-coordinator-pin.md` — **E0**

---

## Coordinator signal

| Field | Value |
|-------|-------|
| `low_return_detected` | **yes** |
| Rationale | Assigned W2 lanes now have graded coverage (Zubek narrative topologies; Heussner/Collas worldbuilding consistency; GUR method family incl. RITE; E3 GDD inventory; light ink/Twine E1). Further Alexandria re-queries on the same books would largely restate W1+W2. Remaining high-value items are residual, not more W2 corroboration. |
| Residual **P0** for W3 | **Agent creative critique / HITL patterns** for creative systems (narrative, world/character, systems) — still `GAP` across W1 S1/S2/S3 and this W2 note; campaign brief explicitly reserves W3 for this. |
| Residual P1 (non-blocking) | Studio narrative/GDD pipelines; machine-readable beat↔state schema; GARO industry adoption; Articy/Yarn; Gygax method mine; Adams Fundamentals body |

---

## Parent return summary

**FACTS (new/corroborating):** Zubek linear/branch/merge/hub/quest/open-world + state complexity + fiction–gameplay consistency/ludonarrative dissonance; Heussner world-building/lore/storysense + judicious docs; Collas role-targeted bible for team coherence; GUR handbook method menu + RITE definition; ink/Twine E1 tooling presence; GARO remains academic E1.

**CLAIMS (E3 only):** Public GDD Markdown/beginner templates exist (low stars); not SoT.

**GAPs retained:** Agent creative critique (**P0 → W3**); studio pipelines; machine schemas; GARO industry default.

**Signal:** `low_return_detected=yes`; residual P0 = agent creative critique.
