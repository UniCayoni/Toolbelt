---
title: "T5D W1 S2 — Narrative / storylines / quests / interactive story methods"
status: draft
theme: theme-5-design
track: T5D
slice: T5D-S2
wave: 1
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5d-s2-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
---

# T5D W1 S2 — Narrative / storylines / quests / interactive story

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T5D-S2**.

**Status:** `draft`. Not Design SoT. **Creative process is plural** — no single story method is accepted as sole law for Toolbelt / GreyMatter.

**T5A spine (vocabulary only):** options → critique → decide → record. Used here only as a shared process label set for human+agent loops; does not import T5A ADR/HITL locks into narrative craft.

## 1. Scope

- **Question / goal:** How to design **storylines / narrative / quests / interactive story** for games (and similar interactive experiences) with methods usable by **humans + agents**?
- **In scope:** Narrative design definitions; story vs plot (linear experience vs branching construct); interactive structure families (string-of-pearls, story machine, modular/graph/open); quest design flows and state/trigger linkage; story-beat ↔ player-action / system-state links where sources support; light web method framing (storylets, GARO beats).
- **Out of scope:** MDA / systems-design deep (T5D-S1); worldbuilding / characters deep (T5D-S3); IP-violating dumps of copyrighted plot texts; fanfic wikis as E1; locking a single “story SoT” process; elevating Design skills.
- **Comprehension / research goal type:** other (creative methodology research)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria `rag_query` (corpus=`game_design`); WebSearch; WebFetch (Emily Short storylets process); local read of campaign brief + research-note template + T5A note shape |
| Corpora / URLs searched | Alexandria `game_design` (Heussner *Advanced Game Narrative Toolbox*; Schell *Art of Game Design* 10th anniv.; Kramarzewski/De Nucci *Practical Game Design*; Howard *Quests*; Quaye event-DB quest handlers — secondary); Emily Short blog; Mochocki & Koskimaa 2021 (GARO story beats) |
| Queries (exact) | Alexandria: `advanced game narrative toolbox interactive story design methods story structure`; `quests design quest structure player action objectives rewards`; `Schell Art of Game Design story chapters storytelling narrative`; `quest design flow steps process causality quest chain exposition design method`; `Jesse Schell Art of Game Design story storytelling lenses narrative experience chapter` (+ `path_prefix=Schell`); `interactive narrative branching story strings of pearls player agency plot structure linear nonlinear open`; `Step 3 General Information …`; Web: `interactive narrative design method story beats player agency game writing process` |
| What was *not* searched | Full Schell Ch.18 indirect-control deep dive; Adams fundamentals as narrative primary; Sellers; full Game Narrative Toolbox (1st book) primary pass; Twine/Ink/Yarn primary docs; GDC talks corpus; TTRPG adventure-design manuals as video-game law; fan wikis; copyrighted full plot transcriptions; agent-specific narrative critique patterns (W3 / T5D residual) |
| Depth | deep |
| Waves / stop_reason | wave: **1**. Stop for this slice: **wave1_primary_complete** — high-signal Alexandria narrative/quest/Schell hits + light E1/E2 web framing; diminishing returns on further W1 workshop-pedagogy chase; W2 corroboration / GDD templates / agent critique reserved per campaign brief |
| Provenance (optional PROV) | Entity←game_design books + practitioner/academic web; Activity=T5D-S2 W1 gather; Agent=Alexandria RAG + WebSearch/WebFetch + gatherer-t5d-s2-grok |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Method/literature slice; no codebase recon |
| Scope boundary | Narrative/quest/interactive-story methods only; no MDA or world-bible deep |

## 4. Findings

Findings are **lane-separated**. Do **not** collapse into one universal narrative pipeline.

### 4.1 Lane A — Definitions & plural interactive forms

- `CLAIM` [E2] **Game narrative design** = telling a story in a videogame using techniques/devices available (including gameplay + visual/acoustic methods) for an entertaining/engaging player experience; **narrative designer** = champion of interactive story combining writer + game designer roles. Glossary also defines: linear narrative (same events/order every playthrough); open narrative (player chooses order of content); player agency (belief that choices/actions drive story events); quest (task/group of tasks as self-contained storyline within/alongside larger plot). [E2: Alexandria corpus=`game_design` source=`The advanced game narrative toolbox (Heussner, Tobias)…pdf` chunk_id=`84bbf836a28b213352497837` query=`advanced game narrative toolbox interactive story`]
- `CLAIM` [E2] **Stories are always linear** (one playthrough’s experienced journey); **plots** may be linear or nonlinear (underlying multi-path construct). Quests = narrative-facing **obstacles/tasks** protagonists overcome — not characters, not goals, not the plot itself; pure skill-test mechanics without narrative relation are out of quest scope in this framing. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_id=`4e4c8b3e65056bbc2e73b7b6` query=`…story structure`]
- `CLAIM` [E2] Schell Ch.17 (*One Kind of Experience Is the Story*): interactive storytelling is **more challenging** than traditional storytelling but **not fundamentally different**; traditional story craft still applies. Two dominant **real-world methods**: (1) **String of pearls** / rivers-and-lakes — noninteractive story beats (string) alternating with goal-directed free play (pearls); (2) **Story machine** — game as generator of tellable event sequences with little prescripted story. Branching-tree “dream” faces combinatorial explosion; fusing branches often empties choice of meaning. [E2: Alexandria corpus=`game_design` source=`Schell, Jesse - Tenth Anniversary_ The Art of Game Design…pdf` chunk_ids=`c884812b2c8802ba036211cd`, `f5a5c4f100ed3c2ed5511a88`, `04cefcc87f95687056b125e6`, `cd910cc244efac5bbd9e8a01`, `a5090723d8bb7be5a7800e73` query=`Schell … story`]
- `CLAIM` [E2] Schell lenses for story work include **Lens of the Story Machine** (choices, conflict variety, personalization, interest curves, tellability) and **Lens of Story** (need for story; player interest; mutual support with tetrad elements). [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_ids=`cd910cc244efac5bbd9e8a01`, `f43c7b0f2a397dfd6c3ef637` query=`Schell … story`]
- `CLAIM` [E2] *Practical Game Design*: game narrative unfolds through play — mechanics/dynamics at least as important as written story; ideal that skipping cutscenes/text still leaves a sensible story via play. Structure families: **linear** (String of Pearls); linear with extended exploration that does not change story course; **modular** (graph/tree/rejoining branches; parallel plots); open/non-linear challenges noted. Linear narrative is not “bad.” [E2: Alexandria corpus=`game_design` source=`Practical Game Design…Kramarzewski…pdf` chunk_ids=`6c77267cbacb0be08ddfde7b`, `94e9bb090e24366770f7634d`, `dcc0e2bc0e90f481d85e61c0` query=`interactive narrative branching…`]
- `INFERENCE` [E4] For Toolbelt, treat string-of-pearls, story-machine, modular/graph, open-order, and storylet/quality systems as **parallel options**, not a ranked SoT. Premises: (1) Schell two-method dominance + dream critique; (2) Kramarzewski modular taxonomy; (3) campaign brief “creative process is plural.”

### 4.2 Lane B — Quest design methods (human-usable checklists)

- `CLAIM` [E2] Heussner sample **quest-chain design flow** (MMORPG-like): (1) Background/lore; (2) High concept/hook (1–2 sentences; fun/unique/lore/purpose); (3) General info (quest count, locations, NPCs/factions, items, special mechanics; uniqueness + lore paragraphs); (4) Quest graph; (5) Region map (designer art); (6) Player-facing summary (clear verbs); (7) Player info texts — description / in-progress / debriefing; (8) Gameplay info — unlock, giver, closing condition/objective, level band, rewards; then loop 6–8 per quest. Keys: **iteration + observation**; escalate stakes while alternating intensity; use three-act / hero’s-journey patterns as progression guides at multiple scales. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_ids=`77c2c863c49b89fdbb9d8ee4`, `ecc086646ffa60e0a5da6019`, `39687eeae0b6952880c4fc4c`, `6c862b91e00db202d67c436e`, `05b11f1176ae6eacfac5e7d9`, `e91d3bbac65e2b513f46362c` query=`quest design flow…`]
- `CLAIM` [E2] Quest **causality** (purpose + consequence) and **environmental storytelling**: design environment with level/audio/visual before overwriting quest text; show/play don’t dump backstory; avoid overloading quest text with life-story exposition. Quests are a main vehicle (with dialogue) for interactive exposition via tasks. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_ids=`cfb3e7d8f899c8aa4be5365d`, `bfc4eade8abe5af9d4c35401` query=`quests design…` / `quest design flow…`]
- `CLAIM` [E2] Schell **focus** + **flow channel** (Ch.9, via Heussner): quest challenges must match acquired skill or players lose focus (boredom/anxiety); progression across quest chains must escalate difficulty with skill growth. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_ids=`87b1681b953e39947a0eed6b`, `7259d19bd02c325054229099` query=`Schell … story` / `quest design flow…`]
- `CLAIM` [E2] Howard *Quests*: break quest into **flow / spaces / objects / characters**; flowchart stages; typology includes fetch/delivery/dungeon/escort/kill (and combinations); quests ≠ synonymous with narratives but storylines motivate/reward; **quest systems** = networked rules/tasks/storylines managed by scripting; main vs side quests extend Campbell “road of trials.” Design → concepts → plans → processes before engine implementation. [E2: Alexandria corpus=`game_design` source=`Quests Design, Theory, and History…Howard…pdf` chunk_ids=`3a6191afa94dcc991b4e28dc`, `f0e5d3723da63ce307035ca4`, `0266ed74a0773b8aa259e646`, `d0150ffdfc0cc2c2dcec3620` query=`quests design…`]
- `CLAIM` [E2] Howard: quests as **state machines** — stages/nodes, trigger events bump logic, variables for objective/journal/UI/world state; plan major stages/challenges first, then triggers, then branching choices; think in both thematic and mechanical terms. [E2: Alexandria corpus=`game_design` source=`Quests…Howard…` chunk_id=`f7420930869a2fd393342eb1` query=`Step 3 General Information…`]
- `GAP` Unified “industry-standard” quest template across studios. Searched: Heussner flow + Howard workshop decomposition. Result: multiple compatible checklists, no single SoT. Follow-up: W2 GDD/template repos (E3) if needed.

### 4.3 Lane C — Story beats ↔ player action / system state

- `FACT` [E1] Mochocki & Koskimaa (2021): **story beat** as microunit of dramatic action with **GARO** — Goal (story-value binary, e.g. locked/unlocked), Action, Reaction (opposing force), Outcome (value change or not). Six beat types: Action, Interaction, Inaction, Mental, Emotion, Sensory. Framed as ludonarrative unit usable as Bogost-style unit operation **and** narrative microunit. [E1: Michał Mochocki & Raine Koskimaa, “Story beats in videogames as value-driven choice-based unit operations,” *Images* 2021 — https://doi.org/10.14746/i.2021.38.01 — accessed 2026-07-29]
- `FACT` [E1] Same paper: beats link **player/character verbs** to contested **story values** that map to game-state-like binaries (alive/dead, hostile/friendly, known/unknown, mission fail/succeed); Outcome is the state change (or failed change). [E1: Mochocki & Koskimaa 2021 — same DOI — accessed 2026-07-29]
- `FACT` [E1] Emily Short (practitioner): storylet-based IF process — identify goals → high-level arc(s) with **progress qualities** + key moments + optional subordinate beats → recurring gameplay/fiction patterns (+ paper/electronic prototype) → refine **qualities** (fungible stats tracking story effects across modules) → implement through-line (qualities → storylets → extras) → iterate (guidance, branches, pacing, prose). Qualities are the explicit **system state** layer gating/unlocking content. [E1: Emily Short, “Mailbag: Development Process for Storylet-based Interactive Fiction” — https://emshort.blog/2020/02/18/mailbag-development-process-for-storylet-based-interactive-fiction/ — accessed 2026-07-29]
- `CLAIM` [E2] Howard: moving between quest stages sets variables (next objective, journal text, mini-map target, world/narrative indicators); object interaction can update quest state (Creation Kit–style). [E2: Alexandria corpus=`game_design` source=`Quests…Howard…` chunk_ids=`f0e5d3723da63ce307035ca4`, `f7420930869a2fd393342eb1` query=`quests design…`]
- `CLAIM` [E2] Quaye (architecture-oriented): procedural quest handlers as event-driven objects with fields (giver, prompt, target/lost item, receiver, reward events) responding to enter/dead/moved/complete events — concrete **action → event → state/reward** wiring (kill/find/escort patterns). Treat as implementation pattern illustration, not narrative-craft law. [E2: Alexandria corpus=`game_design` source=`Event-Database Architecture…Quaye…pdf` chunk_ids=`a369048bae26354a185132b1`, `4e278478e66e3f8dc33f17a7`, `384f067c73ec97acc5462186` query=`quests design…`]
- `CLAIM` [E2] Heussner Step 8: gameplay information block includes unlock conditions, quest giver, **closing condition (objective)**, rewards — the design artifact that binds story beat completion to system checks. [E2: Alexandria corpus=`game_design` source=`…advanced game narrative toolbox…` chunk_id=`05b11f1176ae6eacfac5e7d9` query=`quest design flow…`]
- `GAP` Canonical Toolbelt schema mapping “story beat ↔ ECS/component state” for agents. Searched: GARO + Short qualities + Howard variables + Quaye handlers. Result: strong conceptual bridges; no shared machine-readable narrative-state contract in this slice. Follow-up: W2/W3 if product needs a record format.
- `GAP` Agent-specific narrative critique / HITL loops beyond T5A vocabulary reuse. Searched: this slice’s narrative sources + Caldwell AI-assist note (discovery only). Result: Caldwell chunk notes collaborative AI for story options but not a Toolbelt process lock. [E2 discovery: Alexandria corpus=`game_design` source=`Story Structure and Development…Caldwell…pdf` chunk_id=`60799a75df434dbb5b593520` — not promoted to method law.] Follow-up: T5D W3 agent creative critique if still OPEN.

### 4.4 Lane D — Human+agent usable process (options → critique → decide → record)

- `INFERENCE` [E4] A plural, agent-friendly narrative workflow can reuse T5A spine **labels** without locking one craft school: **options** = enumerate structure family (pearls / machine / modular / storylets) + quest-chain hooks; **critique** = check causality, agency meaningfulness, flow-channel fit, beat↔state wiring, exposition load; **decide** = human owns story values, structure choice, and which branches fuse; **record** = quest graph + beat/GARO or quality table + gameplay closing conditions (not prose dump alone). Premises: (1) Lane A plural forms; (2) Lane B checklists; (3) Lane C state links; (4) T5A spine as vocabulary-only per slice brief.
- `INFERENCE` [E4] Agents are comparatively strong at drafting options matrices, flowchart stubs, quality inventories, and consistency diffs; weak at owning “is this choice meaningful?” and emotional/thematic judgment — mirrors Short’s human goal-setting and Schell’s choice-meaning critique. Premises: (1) Short E1 process starts with human goals; (2) Schell E2 fusion-empties-choice; (3) draft-is-not-sot / human acceptance for creative locks.
- `OPEN` Whether GreyMatter / Toolbelt should ship a **narrative decision-record** subtype (vs reusing ADR/MADR). Follow-up: after T5A acceptance + T5D synthesis — do not invent here.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | No single interactive-story method dominates practice; at least pearls + machine + modular/storylets coexist | confirmed (for this slice) | Schell two methods; Kramarzewski modular; Short storylets |
| H2 | Usable quest design always binds objectives to explicit close conditions / state variables | confirmed (sources agree) | Heussner Step 8; Howard state machine; Short qualities; Quaye events |
| H3 | GARO is a good default beat grammar for human+agent shared language | open | E1 paper exists; not yet corroborated against studio pipelines in W2 |
| H4 | Agent creative narrative critique patterns are documentable as first-class methods | open | GAP this slice; W3 residual |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Are “nonlinear stories” possible? | Marketing claim of nonlinear stories (noted by Heussner) | Heussner: stories linear per playthrough; plots may branch | Prefer Heussner distinction; treat marketing language as non-technical |
| Is branching tree the ideal? | Dream of richly branching AI stories (Schell antagonist position) | Schell: combinatorial explosion + weak fused choices; pearls & story machine dominate | Prefer Schell “what works”; keep branching as costly option, not default SoT |
| Quests vs missions naming | Howard: quest vs mission genre connotation | Heussner glossary “quest” | Naming is genre-flavored; structure methods transfer — no lock |

## 7. Gaps & OPEN

- `GAP` Studio-primary narrative pipelines (BioWare/CDPR/etc. GDD law) not fetched this wave.
- `GAP` Twine / ink / Yarn / Articy primary documentation as tooling SoT.
- `GAP` Machine-readable beat↔state schema for agents.
- `OPEN` T5D W3: agent creative critique patterns if still needed after S1/S3.
- `OPEN` Cross-track: whether narrative records share ADR shape (T5A) or need a creative template.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For humans+agents designing interactive narrative: pick a **structure family** explicitly (options), run a **quest/beat checklist** (critique), bind beats to **state/qualities/close conditions** (decide+record), and refuse a single story SoT. Premises: H1–H2; Lanes A–D.
- `INFERENCE` [E4] Do not treat Campbell/Vogler alone as game narrative law — Howard and Schell both treat monomyth as partial/flexible material for activity systems, not a rigid Hollywood template. Premises: Howard E2 on enriching Campbell; Schell E2 on traditional craft + interactive constraints.
- **Non-lock reminder:** This note is `draft`. No architecture, library, or GreyMatter narrative stack locks.

## 9. Source list (deduped)

1. Alexandria `game_design` — Heussner (ed.), *The Advanced Game Narrative Toolbox* — chunk_ids: `84bbf836a28b213352497837`, `4e4c8b3e65056bbc2e73b7b6`, `bfc4eade8abe5af9d4c35401`, `cfb3e7d8f899c8aa4be5365d`, `87b1681b953e39947a0eed6b`, `7259d19bd02c325054229099`, `77c2c863c49b89fdbb9d8ee4`, `ecc086646ffa60e0a5da6019`, `39687eeae0b6952880c4fc4c`, `6c862b91e00db202d67c436e`, `05b11f1176ae6eacfac5e7d9`, `e91d3bbac65e2b513f46362c`, `fa6ca2ac2a37794202cf7887`
2. Alexandria `game_design` — Schell, *The Art of Game Design* (10th Anniversary) — chunk_ids: `417336dd7c22819e65f65581`, `c884812b2c8802ba036211cd`, `f5a5c4f100ed3c2ed5511a88`, `04cefcc87f95687056b125e6`, `cd910cc244efac5bbd9e8a01`, `a5090723d8bb7be5a7800e73`, `f43c7b0f2a397dfd6c3ef637`, `cc21e2b2f82d0fc275eea71f`
3. Alexandria `game_design` — Kramarzewski & De Nucci, *Practical Game Design* (2nd ed.) — chunk_ids: `6c77267cbacb0be08ddfde7b`, `94e9bb090e24366770f7634d`, `dcc0e2bc0e90f481d85e61c0`, `fc1cef6971d4121dfcd64631`
4. Alexandria `game_design` — Howard, *Quests* (2nd ed.) — chunk_ids: `3a6191afa94dcc991b4e28dc`, `8abd4ba8ed9128e272a3b8d3`, `9d084b5d31b29f32c9a74287`, `f0e5d3723da63ce307035ca4`, `0266ed74a0773b8aa259e646`, `d0150ffdfc0cc2c2dcec3620`, `f7420930869a2fd393342eb1`, `298c2729d9827435d8cda820`, `e626988bd6d2778a697b6e0f`
5. Alexandria `game_design` — Quaye, *Event-Database Architecture… Vol. 2* — chunk_ids: `a369048bae26354a185132b1`, `4e278478e66e3f8dc33f17a7`, `384f067c73ec97acc5462186`
6. Alexandria `game_design` — Caldwell, *Story Structure and Development* — chunk_id=`60799a75df434dbb5b593520` (AI-assist discovery only)
7. Mochocki & Koskimaa (2021), GARO story beats — https://doi.org/10.14746/i.2021.38.01 — accessed 2026-07-29
8. Emily Short (2020), storylet development process — https://emshort.blog/2020/02/18/mailbag-development-process-for-storylet-based-interactive-fiction/ — accessed 2026-07-29
9. Campaign brief — `docs/research/notes/theme-5-design/campaign-brief.md` (scope pins; not narrative evidence)
