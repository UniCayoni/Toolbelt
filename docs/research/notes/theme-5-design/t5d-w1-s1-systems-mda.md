---
title: "T5D Wave 1 Slice S1 — Game/creative systems via MDA-class lenses and design loops"
status: draft
theme: theme-5-design
track: T5D
wave: 1
slice: T5D-S1
created: 2026-07-29
updated: 2026-07-29
authors: [t5d-w1-s1-gatherer]
supersedes: null
---

# T5D-W1-S1 — Designing game/creative systems with MDA-class lenses and systems design loops

**Using `research-protocol`; depth: deep; wave: 1; slice: T5D-S1.**

## 1. Scope

- Question / goal: How to design game/creative *systems* using MDA-class lenses (mechanics, dynamics, aesthetics) and systems design loops?
- In scope: MDA primary paper (Hunicke/LeBlanc/Zubek); Alexandria `game_design` corroboration from Schell (*Art of Game Design*), Sellers (*Advanced Game Design*), Adams/Zubek-line systems (Adams & Dormans *Game Mechanics*; Zubek *Elements of Game Design* as MDA-author follow-on); plural frameworks and iteration/tuning loops for systems design.
- Out of scope: Narrative deep dive (T5D-S2); worldbuilding deep (T5D-S3); shipping a game engine; GreyMatter creative-stack locks; applying MDA as software Clean Architecture / layered-code law; TTRPG/GM books as video-game systems law; agent creative-critique patterns (campaign W3); inventing APIs/URLs/citations.
- Comprehension / research goal type (if code): other (creative/game systems design literature)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch (MDA PDF); Alexandria MCP `list_documents`, `rag_query`, `rag_fetch_chunk` (corpus `game_design`); Read (research-note template, campaign brief T5D, peer T5A note shape); research-protocol skill |
| Corpora / URLs searched | https://users.cs.northwestern.edu/~hunicke/MDA.pdf ; Alexandria corpus=`game_design` (docs confirmed: Schell 2019; Sellers 2017; Adams *Fundamentals*; Adams & Dormans *Game Mechanics*; Zubek *Elements of Game Design*) |
| Queries (exact) | Direct PDF fetch; `list_documents` name_substring Schell/Sellers/Adams/Zubek; rag_query: "Schell Art of Game Design systems design loop iteration lenses mechanics dynamics player experience how to design game systems"; "Sellers Advanced Game Design systems design loops emergence feedback mechanics dynamics aesthetics"; "Adams Zubek game systems design mechanics dynamics loops formal systems interactive"; path_prefix=`Schell` / `Schell, Jesse` / `Michael Sellers` / `Game mechanics` / `Game Mechanics Advanced Game Design` / `Fundamentals of Game Design` with systems/MDA/iteration/Machinations questions; `rag_fetch_chunk` on Zubek MDA critique + model chunks |
| What was *not* searched | Narrative/interactive-story shelves (S2); worldbuilding/character bibles (S3); GUR methods; GDD template repos (E3 W2); `games_engine_graphics` except as incidental; pubs mirrors beyond Northwestern MDA PDF; Salen/Zimmerman *Rules of Play* full deep; agent creative-critique corpora; Clean Architecture / software architecture corpora (explicit non-goal) |
| Depth | deep |
| Waves / stop_reason | wave: 1 (slice T5D-S1). stop_reason: N/A for gatherer slice — Wave 1 primary fetch + named Alexandria systems sources complete for assigned question; diminishing-returns / track stop owned by coordinator/integrator |
| Provenance (optional PROV) | Entity←MDA PDF; Schell; Sellers; Adams & Dormans; Zubek Elements; Activity=T5D-W1-S1 gather; Agent=WebFetch+Alexandria RAG |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Slice is primary/secondary literature on creative systems design, not workspace recon |
| Scope boundary | Named MDA URL + `game_design` corpus sources listed in Method; no code edits |

## 4. Findings

### 4.1 MDA primary (E1) — what the framework is

- `FACT` [E1] Hunicke, LeBlanc, and Zubek present **MDA** (Mechanics, Dynamics, Aesthetics) as a formal approach to understanding games that bridges game design/development, criticism, and technical game research; developed/taught in the GDC Game Design and Tuning Workshop (2001–2004). [E1: Robin Hunicke, Marc LeBlanc, Robert Zubek, “MDA: A Formal Approach to Game Design and Game Research” — https://users.cs.northwestern.edu/~hunicke/MDA.pdf — accessed 2026-07-29]
- `FACT` [E1] Definitions: **Mechanics** = particular components of the game at the level of data representation and algorithms; **Dynamics** = run-time behavior of the mechanics acting on player inputs and each other’s outputs over time; **Aesthetics** = desirable emotional responses evoked in the player when she interacts with the game system. [E1: same PDF]
- `FACT` [E1] Games are framed as designed **artifacts** whose content is **behavior** via interaction, not media streaming toward the player; MDA formalizes consumption by pairing Rules↔Mechanics, System↔Dynamics, “Fun”↔Aesthetics. [E1: same PDF]
- `FACT` [E1] Each MDA component is a **lens/view**—separate but causally linked. Designer perspective: mechanics → dynamics → aesthetics. Player perspective: aesthetics set the tone, born out in observable dynamics, then operable mechanics. Considering both supports experience-driven (vs feature-driven) design and seeing how small layer changes cascade. [E1: same PDF]
- `FACT` [E1] Aesthetic taxonomy (move beyond vague “fun”): Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission — with game examples (Charades, Quake, The Sims, Final Fantasy) combining multiple goals in varying degrees; no Grand Unified Theory / formula for proportions. [E1: same PDF]
- `FACT` [E1] Dynamics create aesthetics (e.g. challenge via time pressure/opponent play; fellowship via shared information/team win conditions; expression via systems that let players leave a mark; dramatic tension via rise/release/denouement). Concrete dynamic models (e.g. 2d6 Monopoly board progress; feedback systems that widen wealth gaps) support prediction and avoiding pitfalls. [E1: same PDF]
- `FACT` [E1] Mechanics are actions/behaviors/control mechanisms afforded to the player; with content they support dynamics. Adjusting mechanics tunes dynamics (Monopoly lagging-player subsidies/taxes; time-pressure taxes). Card-game bluffing, shooter camping/sniping emerge from mechanics. [E1: same PDF]
- `FACT` [E1] Design process implied by MDA: reason from aesthetic goals → dynamics that support them → scope mechanics accordingly; then **playtesting and tuning**; aesthetic vocabulary and dynamic models articulate goals, discuss flaws, and measure progress. AI/component example: same “tag/babysitting” concept re-scoped across three aesthetic/audience passes forces different AI/navigation/mechanics — “no AI mechanics as such”; coherence from interaction of AI logic with gameplay logic. [E1: same PDF]
- `FACT` [E1] Conclusions: MDA supports formal **iterative** design/tuning; moving between three abstraction levels conceptualizes dynamic system behavior; helps control undesired outcomes and tune desired behavior. [E1: same PDF]
- `CLAIM` [E1] MDA is an analytical/design **lens for games as interactive systems**, not a prescription for software module layering or Clean Architecture dependency rules. Premises in source: definitions are about player experience, runtime behavior, and emotional goals — not package/dependency graphs. [E1: same PDF — scope/language of paper]

### 4.2 Plural methods — MDA is one framework among several (do not universalize)

- `FACT` [E2] Sellers presents MDA as “possibly best-known” of several game frameworks; quotes the paper’s three definitions; notes players approach aesthetics→dynamics→mechanics while designers often see mechanics→dynamics→aesthetics, and MDA pushes aesthetics-first — **but in practice designers start from any layer** depending on style and constraints. [E2: Alexandria corpus=`game_design` source=`Michael Sellers - Advanced Game Design_ A Systems Approach (2017, Addison-Wesley Professional) - libgen.li.pdf` chunk_id=`68a98c57018a5a7ec179acf6` query=`Sellers MDA framework…`]
- `FACT` [E2] Sellers: only mechanics are wholly in the designer’s direct control; dynamics are staged by mechanics, not created directly — pointing to a systemic “parts → loops → whole” task. [E2: same source chunk_id=`68a98c57018a5a7ec179acf6` / continuation `95d63c7f633d1f5547d64ad6`]
- `FACT` [E2] Sellers critiques MDA terminology collisions: industry “mechanics” often means recurring gameplay chunks/ludic devices with elastic chunk size; MDA’s “aesthetics” (full experience) collides with visual aesthetics and can mis-focus teams on look-and-feel. Despite difficulties, MDA remains a useful advance toward systemic understanding. Sellers also names other frameworks (e.g. FBS/SBF) as related three-layer bridges. [E2: Alexandria corpus=`game_design` source=`…Sellers…` chunk_id=`95d63c7f633d1f5547d64ad6`]
- `FACT` [E2] Zubek (*Elements of Game Design*), co-author of MDA, presents a successor three-level model: **Mechanics** (pieces), **Gameplay** (dynamic process of players interacting with game/each other), **Player experience** (subjective). Designers cannot create experience directly — they craft mechanics that produce gameplay/experience; unexpected behavior from mechanics and players must be accounted for. Distinguishes **systems design** (broad rules/mechanics/systems) vs **content design**. [E2: Alexandria corpus=`game_design` source=`Elements of Game Design (The MIT Press) (Robert Zubek)…epub` chunk_id=`a0ec3ceed827319806c7221f` and `4514792677b9aad6bda0ea85`]
- `FACT` [E2] Zubek explicitly does **not** present MDA “as is”: (1) “dynamics” for gameplay is virtually unused in industry practice; (2) MDA “aesthetics” ≠ industry visual aesthetics; (3) MDA “dynamics” ambiguously mixes systems analysis and player interaction — practice separates **game systems** from **gameplay loops** and experience; (4) designer/player at opposite ends of an MDA chain is idealized — **iterative design approaches a game from both ends simultaneously**. [E2: Alexandria corpus=`game_design` source=`…Zubek…` chunk_id=`15a4534ef3519664a59228de` + neighbor `d5fde0aff7bb2305a59b030a`]
- `FACT` [E2] Schell’s **elemental tetrad** is a different four-part lens: **mechanics, story, aesthetics, technology** — all essential and equal; none primary; each influences the others; Lens of the Elemental Tetrad asks whether all four are used, improvable, and in harmony toward a theme. Schell’s “aesthetics” here means how the game looks/sounds/smells/tastes/feels (sensory/presentation), not MDA’s emotional-response taxonomy. [E2: Alexandria corpus=`game_design` source=`Schell, Jesse - Tenth Anniversary_ The Art of Game Design…pdf` chunk_id=`186ad396a45c9a7a9837974e` / `7918cc5e718c4682220e9375`]
- `FACT` [E2] Schell: designers must see **skin and skeleton at once** — player experience and the elements causing it; skeleton-only yields theoretically beautiful but potentially horrible practice; skin-only lacks levers to improve. Designs may start in any tetrad corner; story is often most pliable. [E2: Alexandria corpus=`game_design` source=`…Schell…` chunk_id=`3cdd0806bb38ef7b0777adee` / `0bf44d39d9c7ae388a4a0e9d`]
- `FACT` [E2] Schell documents LeBlanc’s eight pleasures (Sensation…Submission) as player psychographics and cites the MDA paper as the taxonomy’s introduction. [E2: Alexandria corpus=`game_design` source=`…Schell…` chunk_id=`8c96b345b8dcdf85e5cb3be7` / `33a80febc9d4507c274203a5`; endnote chunk_id=`75f60abe08bc559742a5a359`]
- `INFERENCE` [E4] For Toolbelt Design methods: treat **MDA-class** as a family of related three-layer experience↔runtime↔rules lenses (MDA; Zubek mechanics/gameplay/experience; Sellers systemic restatement), coexisting with **non-MDA** lenses (Schell tetrad; Adams & Dormans emergence/progression + Machinations). Do **not** collapse them into one universal vocabulary or into software Clean Architecture. Premises: §§4.1–4.2 FACTS.

### 4.3 Systems design loops (how systems get designed/tuned)

- `FACT` [E2] Sellers’ **designer’s loop**: outermost balancing loop — designer views game+player as unified whole; watches players; adjusts game model to reduce gap between intent and experience; “a bunch of rules does not make a game”; simulation alone is not yet a game until interactive game+player system exists. Four principal loops named: game’s model, player’s mental model, interactive loop (incl. core loops), designer’s loop. [E2: Alexandria corpus=`game_design` source=`…Sellers…` chunk_id=`b0e8e725012e836f53a157c3` / `cd3a0b48a76ebb6689924e35` / `b735701848b6b34f912cc978`]
- `FACT` [E2] Sellers on defining a system: choose looping structure (reinforcing/balancing; engine/economy/ecology/hybrid); sketch primary loops; iterate structure; remove systems that do not serve player experience; systems design is hard because experience is hard to foresee — **prototyping and playtesting** required; balance unused systems or remove them. Designer shifts focus among whole game, looping systems, and parts. [E2: Alexandria corpus=`game_design` source=`…Sellers…` chunk_id=`406e74e8b1471d57c2f173a3` / `211b0481c1122c496a12d4e3` / `25e666486fe1c3140295a24c`]
- `FACT` [E2] Schell **Rule of the Loop**: “The more times you test and improve your design, the better your game will be” — framed as absolute truth (not a lens); waterfall violates it; spiral/agile emphasize risk assessment, prototypes, and fast loops. Formal loop: state problem → brainstorm → choose → list risks → prototype → test → state new problems. Risk-first prototyping against elemental-tetrad design briefs (example: Prisoners of Bubbleville). [E2: Alexandria corpus=`game_design` source=`…Schell…` chunk_id=`5d5464f660f4b073de40af89` / `04ff3a429f145211699e7bdb` / `4b1a9feebfaa2a2b0b3614a2` / `b480fadc6add2f2693206b17`]
- `FACT` [E2] Adams & Dormans: game mechanics create gameplay; design/test/tune core mechanics; process stages concept → elaboration → tuning; after concept, work in short iterative cycles producing playable prototypes for external playtest; do not expect to get features right first time; paper/physical/software prototypes chosen by **focus** (economy vs control scheme, etc.). Emergence from interconnected parts, feedback loops, multi-scale interaction; **Machinations** visualizes internal-economy resource/state flows and feedback for simulation before full implementation. [E2: Alexandria corpus=`game_design` source=`Game Mechanics Advanced Game Design ( etc.)…epub` chunk_id=`0af84c75017ae3731c39fe27` / `5c2cb83ab919e30c7674a160` / `5af8ea7c30718ddc87724a5d` / `5be90a168e0394521b5e9bf2` / `00417b08eee2deec115a5371`]
- `FACT` [E2] Zubek points readers to Sellers for mechanics/systems interplay and to Adams & Dormans for formal modeling/simulation (“game grammars”) before committing to in-game implementation. [E2: Alexandria corpus=`game_design` source=`…Zubek…` chunk_id=`1019dd9c9af45b2642e54eeb`]
- `FACT` [E1] MDA Monopoly/tuning section aligns: identify feedback that kills tension → propose mechanic changes → iteratively refine values via playtest; aesthetic/dynamic models measure progress. [E1: MDA PDF]
- `GAP` Adams *Fundamentals of Game Design* is present in `game_design` (two PDF copies, 79 chunks each) but Wave-1 rag_query with path filters returned mostly frontmatter/index, not usable core-mechanics chapter body for cite-or-omit claims. Relied on Adams & Dormans *Game Mechanics* (explicit systems/Machinations book) + Zubek pointer for Adams-line systems. Follow-up: targeted chunk fetch/page-aware query in W2 if Fundamentals-specific claims are needed.
- `GAP` Agent-specific creative systems workflows (propose/critique/decide with agents) not searched this slice — campaign brief flags likely GAP → W3.

### 4.4 False-friend guardrails (campaign musts)

- `INFERENCE` [E4] **Do not apply MDA as software Clean Architecture law.** MDA layers are experience/runtime/rules lenses for interactive artifacts, not dependency-rule layers for codebases (T5B territory). Premises: E1 MDA definitions/scope; campaign brief T5D caveat; absence of Clean Architecture claims in fetched sources.
- `INFERENCE` [E4] **Creative process is plural:** MDA, Zubek’s renamed triad, Sellers’ loops, Schell tetrad+Rule of the Loop, Adams & Dormans emergence/progression/Machinations are complementary tools with **terminology conflicts** (especially “aesthetics” and “dynamics”). Any later Design skill must name which lens and not pretend one vocabulary. Premises: §§4.2–4.3.
- `OPEN` Whether Toolbelt house language should prefer Zubek’s mechanics/gameplay/player-experience wording over classic MDA labels for industry communication. Follow-up: T5D integrator / human accept — not locked by this draft.

## 5. Hypothesis log (optional)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | MDA-class three-layer thinking + explicit designer/playtest loops is the Wave-1 backbone for “how to design game systems” | confirmed (as literature finding, not product lock) | §4.1 E1; §4.3 E2 |
| H2 | Schell tetrad replaces MDA | rejected | Schell uses tetrad *and* cites LeBlanc/MDA pleasures; different job (elements of a game vs MDA consumption lenses) |
| H3 | Adams Fundamentals alone suffices for systems loops | revised | Fundamentals retrieval weak this pass; Adams & Dormans + Sellers carry systems-loop FACTS |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Term “aesthetics” | MDA E1: emotional responses / kinds of fun | Schell E2: sensory look/feel quadrant of tetrad; industry visual aesthetics (Sellers/Zubek) | Prefer citing which sense; do not merge without gloss. Higher-grade primary for MDA meaning = E1 paper; Schell/Sellers/Zubek document industry collision |
| Term “dynamics” | MDA E1: runtime behavior of mechanics | Zubek E2: prefer “gameplay” + separate “systems”; industry rarely says “dynamics” | Record both; Zubek (MDA co-author) recommends not teaching MDA vocabulary as-is |
| Designer starting point | MDA E1: begin investigation with Aesthetics | Sellers E2: practice starts from any MDA layer | Both: MDA pedagogical preference ≠ exclusive practice |
| Three vs four elements | MDA triad | Schell tetrad (+ technology/story) | Different frameworks; both valid in-scope; no single winner |

## 7. Gaps & OPEN

- `GAP` Deep prose from Adams *Fundamentals* core-mechanics chapters (retrieval weak) — see §4.3.
- `GAP` Agent creative critique / HITL for systems design — deferred per campaign W3.
- `OPEN` House vocabulary: MDA vs Zubek triad labels.
- `OPEN` How T5D systems loops compose with T5A decision-record spine (ADR/options) without forcing game systems into software ADR templates — integrator.
- Out-of-slice (explicit): narrative methods (S2); worldbuilding/characters (S3); engine shipping; GreyMatter locks.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] A candidate (draft) systems-design method envelope for later Design pack drafting: (1) name desired player experience / aesthetic goals; (2) sketch dynamics/gameplay loops and feedback; (3) specify mechanics/parts that can produce them; (4) run designer loop via risk-focused prototypes + playtests; (5) tune or cut systems that do not serve experience. Premises: MDA E1; Sellers designer loop; Schell Rule of the Loop; Adams & Dormans iteration/Machinations.
- `INFERENCE` [E4] When documenting systems for agents/humans, prefer **explicit glossary** (MDA aesthetics ≠ Schell aesthetics ≠ art direction) over assuming shared terms. Premises: Sellers/Zubek terminology FACTS.
- `INFERENCE` [E4] Formal economy/feedback modeling (Machinations or equivalent) is an optional deepening of MDA “dynamic models,” not a replacement for playtest loops. Premises: Adams & Dormans; MDA Monopoly models.

## 9. Source list (deduped)

1. Robin Hunicke, Marc LeBlanc, Robert Zubek — MDA: A Formal Approach to Game Design and Game Research — https://users.cs.northwestern.edu/~hunicke/MDA.pdf — accessed 2026-07-29 — **E1**
2. Michael Sellers — Advanced Game Design: A Systems Approach (2017) — Alexandria corpus=`game_design` source_id=`f4ac855e47964985` — chunks incl. `68a98c57018a5a7ec179acf6`, `95d63c7f633d1f5547d64ad6`, `b0e8e725012e836f53a157c3`, `406e74e8b1471d57c2f173a3`, `211b0481c1122c496a12d4e3`, `cd3a0b48a76ebb6689924e35`, `b735701848b6b34f912cc978`, `25e666486fe1c3140295a24c` — **E2**
3. Jesse Schell — The Art of Game Design: A Book of Lenses (Tenth Anniversary, 2019) — Alexandria corpus=`game_design` source_id=`db6ade4db2428023` — chunks incl. `186ad396a45c9a7a9837974e`, `7918cc5e718c4682220e9375`, `3cdd0806bb38ef7b0777adee`, `5d5464f660f4b073de40af89`, `04ff3a429f145211699e7bdb`, `4b1a9feebfaa2a2b0b3614a2`, `b480fadc6add2f2693206b17`, `8c96b345b8dcdf85e5cb3be7`, `33a80febc9d4507c274203a5`, `75f60abe08bc559742a5a359` — **E2**
4. Robert Zubek — Elements of Game Design (MIT Press, 2020) — Alexandria corpus=`game_design` source_id=`5d396d7aa9e0c4ca` — chunks incl. `a0ec3ceed827319806c7221f`, `4514792677b9aad6bda0ea85`, `15a4534ef3519664a59228de`, `d5fde0aff7bb2305a59b030a`, `1019dd9c9af45b2642e54eeb` — **E2**
5. Ernest Adams & Joris Dormans — Game Mechanics: Advanced Game Design — Alexandria corpus=`game_design` source_id=`786a4fccfd3c7de7` — chunks incl. `0af84c75017ae3731c39fe27`, `5c2cb83ab919e30c7674a160`, `5af8ea7c30718ddc87724a5d`, `5be90a168e0394521b5e9bf2`, `00417b08eee2deec115a5371`, `3f3e8810d297d7f401362193` — **E2**
6. Ernest Adams — Fundamentals of Game Design (present in corpus; body retrieval weak this pass) — source_ids=`0cc9f009f74151f4` / `3d1332f32a812a63` — **GAP for chapter-body cites**
7. Campaign context (local): `docs/research/notes/theme-5-design/campaign-brief.md` — **E0** brief/pin only

---

## Parent return summary (FACTS / CLAIMS / GAPs)

**FACTS (E1 MDA):** Mechanics/Dynamics/Aesthetics defined; designer vs player causal directions; eight aesthetic goals; dynamics/feedback models; mechanics tune dynamics; iterative playtest/tuning; experience-driven scoping (incl. AI example).

**FACTS (E2 corpus):** Sellers designer + four principal loops; MDA useful but terminology collision; practice may start any MDA layer; Schell elemental tetrad + Rule of the Loop + risk prototyping; Zubek mechanics/gameplay/player-experience successor (MDA co-author rejects teaching MDA vocabulary as-is); Adams & Dormans concept→elaboration→tuning + Machinations/feedback/emergence.

**CLAIMS / INFERENCES (not locks):** MDA ≠ Clean Architecture; plural methods required; candidate loop = experience goals → dynamics/loops → mechanics → prototype/playtest/tune.

**GAPs / OPEN:** Adams Fundamentals body cites; agent creative critique (W3); house MDA vs Zubek labels; out-of-slice S2 narrative / S3 worldbuilding / engines / GreyMatter.
