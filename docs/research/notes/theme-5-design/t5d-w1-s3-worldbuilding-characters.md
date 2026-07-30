---
title: "T5D W1 S3 — Worldbuilding bibles & characters/personalities (consistency constraints)"
status: draft
theme: theme-5-design
track: T5D
slice: T5D-S3
wave: 1
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5d-s3-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
---

# T5D W1 S3 — Worldbuilding bibles & characters/personalities

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T5D-S3**.

**Status:** `draft`. Not Design SoT. Methods only — not lore dumps. **IP:** short paraphrase preferred; no large copyrighted excerpts.

## 1. Scope

- **Question / goal:** How to design **worldbuilding bibles** and **characters/personalities** with **consistency constraints** usable by humans and (later) agents?
- **In scope:** World-bible structure; focus vs kitchen-sink; inside-out / outside-in / top-down / bottom-up process patterns; world-rule / magic-system constraints; character-function and personality-consistency methods; TTRPG/GM vs novelist vs video-game design distinctions.
- **Out of scope:** MDA / systems design (S1); full narrative structure (S2); agent creative critique (W3); engine locks; GreyMatter stack locks; fan wikis as E1.
- **Comprehension / research goal type:** other (creative-method research)

**Hard lane rule (campaign):** TTRPG/GM books ≠ video-game systems law. Do not collapse into one “worldbuilding law.”

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria RAG (`rag_probe`, `list_documents`, `rag_query`, `rag_fetch_chunk`); local read of campaign brief + research-note template + sibling gatherer format |
| Corpora / URLs searched | Alexandria `game_design` only (Wave 1 primary corpus per campaign brief) |
| Queries (exact) | `worldbuilding bible consistency constraints world rules character design`; `Kobold Guide to Worldbuilding consistency rules constraints world bible design principles what makes a world coherent`; `Schell Art of Game Design world building characters personalities consistency lenses how to design fictional worlds and characters`; `worldbuilding prompts questions checklist consistency geography culture history magic systems world rules`; `Lens of the World Lens of Character Function Character Traits Character Web Status consistency world properties`; `How to Write a World Bible Cast of Characters races cultures appendices timelines key facts Hungerford`; `Worldbuilding Inside Out Outside In Pramas Monte Cook kinds of worldbuilding focus kitchen sink`; `how to design non-player characters personality motivation consistency NPC method traits goals`; `Lens of the World ask yourself these questions what makes a game world feel real consistent`; `Chris Pramas Worldbuilding Inside Out Outside In method approach start with characters or map`; `Monte Cook Different Kinds of Worldbuilding novelist game master game designer canvas backdrop`; `GCPESRIAH PERSIA worldbuilding ingredients list Kevin Anderson categories`; `NPC entry structure name description phrases backstory desires secrets how to use customize consistency`; `Outside In broad framework large but shallow focus detail strengths weaknesses Pramas` |
| What was *not* searched | Web primary for MDA (S1); narrative structure deep dive (S2); `games_engine_graphics`; Gygax World Builder / Nation Builder deep extraction (listed, not mined as method SoT this slice); Bonner *Game World Architectonics* academic anthology beyond one discovery hit; agent creative-critique patterns (W3); GDD template repos (E3 → W2); live product agent workflows |
| Depth | deep |
| Waves / stop_reason | wave: **1** (Alexandria primary / high-signal methods). Stop for this slice: **wave1_primary_complete** — Kobold bible + focus/KSD + Pramas IO/OI + Schell world/character lenses + prompt/ingredient guides + NPC method fields covered; diminishing returns on further W1 RAG rephrasing. Residual: W2 narrative cross-link / GDD E3; W3 agent critique |
| Provenance (optional PROV) | Entity←`game_design` books (Kobold, Schell, Presley, Day, Anderson, Ashworth); Activity=T5D-S3 W1 gather; Agent=Alexandria RAG + gatherer-t5d-s3-grok |

**IP note:** Findings paraphrase methods and structure; quote lengths kept minimal. Do not treat retrieved lore/examples as Toolbelt content to republish.

**Coverage probe (pre-query):** `rag_probe` on worldbuilding bible / consistency → verdict **partial** (top source: Kobold Guide to Worldbuilding). Proceeded with targeted `rag_query`.

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Creative-method slice; no codebase recon |
| Scope boundary | Alexandria `game_design` only; methods/constraints extraction; no lore inventory |

## 4. Findings

Findings are **lane-separated**. Do not collapse novelist / GM / published RPG designer / video-game designer into one law.

### 4.1 Lane A — World bible as continuity / constraint artifact (human-shared)

- `FACT` [E2] Scott Hungerford defines a **world bible** as an organized collection of facts, histories, maps, pictures, character backgrounds, and related setting information used so writers, editors, designers, and artists share the “right answers”; also used as a flip-through package for business partners. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding (Jeff Grubb)…pdf` chunk_id=`96b66444fa96442938413dfa` query=`How to Write a World Bible…`]
- `FACT` [E2] Hungerford: bibles act as **loophole / continuity guards** — without written constraints, external partners (example: film treatment wanting to destroy a floating capital) will discover gaps that undermine the property; analogous risk from players if details are not thought through. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_id=`414702d6c75016e474a68ca0` query=`How to Write a World Bible…`]
- `FACT` [E2] Hungerford bible **structure** (non-linear assembly OK): **(1) World** — name/placeholder, one-page introduction summarizing world + characters + **central conflict**, races/cultures (initially ~1 page each: one-line summary, languages, customs/taboos/religion, factions; lifespan called out as culturally telling), magic/technology (1-page physics summary then category pages; daily life for poor and wealthy), currency/economy; **(2) Cast** — key characters (~1 page each initially; italics for secret info), monsters/menaces (ecology + drive, not only stats); **(3) Appendices** — timelines/histories (named events/holidays; leave expansion room), cartography, glossary (start with ~30–40 essential terms). [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`0c80314681a37b3ead7a51e2`, `f57f2a35a6993e59856732ac`, `db0365696d3b396d30aff570`, `73e1d64710ca404a4b13f59f` query=`How to Write a World Bible…`]
- `FACT` [E2] Hungerford consistency practices: put **key facts that matter** (not kitchen-sink dump); bible is a **living document** — update from playtest/player assumptions; **date milestone drafts**; bold first use of important vocabulary. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`0c80314681a37b3ead7a51e2`, `414702d6c75016e474a68ca0`]
- `CLAIM` [E2] Licensed-universe chapter (Silverstein / practitioners): many licensors lack a usable bible; constraints often surface as “you find out what you can’t do when you try it and they tell you no”; licensee should push boundaries while licensor defines “too far.” Method takeaway: **explicit allow/deny constraints beat tribal knowledge** when available. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_id=`1b745832e5d8db11429108c6` query=`How to Write a World Bible…`]
- `INFERENCE` [E4] For human+agent use, Hungerford’s bible is already a **shared constraint store**: short intro + conflict, glossary of essential terms, per-entity page caps, secret/public split, dated versions. Agents can be instructed to **read bible before inventing**; humans own acceptance of changes. Premises: (1) Hungerford shared-answers + living-document FACTs; (2) campaign human-decide spine (T5A). Not a lock.

### 4.2 Lane B — Consistency via focus, world rules, and process strategies

- `FACT` [E2] Wolfgang Baur defines **kitchen sink design (KSD)** as providing every option (races, terrains, nations, religions) so any adventure can fit — framed as **abdication of design responsibility** / feature creep; novelty of more acreage/humanoids/gods costs **internal coherence**. Alternative: **focus** — emphasize richest sections; deliver coherent material over time; resist completeness-for-its-own-sake. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`96f98b02a664cfd992ca8748`, `bd1c459c07ae309bb3d34a8f` query=`Worldbuilding Inside Out… kitchen sink`]
- `FACT` [E2] Baur: game design = decisions within **resource constraints** (pages, art, time); a world can never be fully described — so choose useful, inspiring material under that limit. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_id=`e7d8c1e282eaf6f7cb30e6fb`]
- `FACT` [E2] Chris Pramas: two processes — **inside out** (local start → expand organically; practical for RPG campaigns / novels; build what you need as conflict/culture/secondary cast demand) and **outside in** (large shallow framework → zoom detail; Greyhawk-style broad strokes for customization). No single right way; can mix. Outside-in flaw: big issues take time; may miss fine detail until zoom. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`2faf13d33d9d2f3c78e32e8d`, `096a6529a2af130b1de941f7`, `60feef5d4efef8118f88c33c` query=`Chris Pramas…`]
- `FACT` [E2] M. D. Presley: worldbuilding as **craft**; strategies **top-down** (rules/large ideas → details) vs **bottom-up** (granular → coherent whole); audiences encounter worlds **inside-out** (session-relevant details first). Fantasy conceits ordered roughly Geography → Biology → Physics/magic → Metaphysics → Technology → Culture; types: exsecting / unchanged / divergent / additive. Glossary: **Terra De Facto** — unstated aspects default to real-world rules. [E2: Alexandria corpus=`game_design` source=`101 Worldbuilding Prompts…epub` chunk_ids=`0dd71270c5a8438c61a81677`, `54b279b1620162ebf23dec09`, `e84eebfb9d06df73e892012b` query=`worldbuilding prompts…`]
- `FACT` [E2] Kylie Day: magic systems need **rules** and a **price**; characters should not do anything anytime without cost; highlight only answers used in the story; plan how/when/why world info is shown. [E2: Alexandria corpus=`game_design` source=`How to Get to Know Your Storys World…epub` chunk_id=`06f9bfc55fd1b9710f65b505` query=`worldbuilding prompts…`]
- `FACT` [E2] Kevin J. Anderson: questions as building blocks; align answers for **internal consistency**; “play the geekiest fanboy skeptic: Does it make sense?”; magic cannot be a “spell of plot convenience”; PERSIA (Political, Economic, Religion, Society, Intellectual, Arts) expanded to **GCPESRIAH** checklist (Geography, Climate, Politics, Economics, Society, Religion, Intellectual/Science, Arts, History — illustrated in review section); **don’t include everything** in the delivered story. [E2: Alexandria corpus=`game_design` source=`Worldbuilding From Small Towns…epub` chunk_ids=`5a7c9d7931bdf38a6133db61`, `d7e190908fe7579c17acb804`, `025f120b63aec80af2f8be6a`, `af4507ced830ab58bb563d40` query=`GCPESRIAH…`]
- `FACT` [E2] Baur (technology essay): tech/magic power-ups should be designed into the **rules set**; language/terminology choices constrain audience reception (fantasy vs tech trigger words) — a creative **audience constraint**, not just flavor. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_id=`8a1cf96e37ad6b148beec10c`]
- `FACT` [E2] Jonathan Roberts (maps): maps sell the **illusion** of a larger consistent world without exhaustive detail; map features should hang together believably. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_id=`95743144beb12ae3e0cae17d`]
- `INFERENCE` [E4] Operational consistency constraints extractable as checklist items (not lore): (a) focus/anti-KSD scope bound; (b) magic/physics one-pager + costs; (c) Terra De Facto default; (d) answer-alignment skeptic pass; (e) glossary of locked terms; (f) dated bible versions. Premises: §§4.1–4.2 FACTs.

### 4.3 Lane C — Characters & personalities (function, traits, relationships)

- `FACT` [E2] Jesse Schell (*Art of Game Design*): **Lens of the World** — world exists apart; game is a doorway; questions include how the world is better than reality, multiple gateways, single-story vs many-stories capacity. [E2: Alexandria corpus=`game_design` source=`Schell…Art of Game Design…pdf` chunk_id=`09cd3103da188ae3449584fd` query=`Lens of the World…`]
- `FACT` [E2] Schell: imaginative worlds need **internal consistency**; one contradiction can break immersion/projection; episodic integrity — out-of-character or contradictory world changes can spoil the whole series from the guest’s POV. [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_id=`a6be08f8db840cace07b7227` query=`Schell… consistency…`]
- `FACT` [E2] Schell **Character Tip #1 / Lens of Character Function**: list **functions the game needs** (hero, mentor, tutor, bosses, hostage, etc.) separately from imagined characters; map characters↔roles; allow multi-role folding; change characters to fit roles. [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_ids=`5d37f280b164ab7e1fca9cd6`, `a999998ffeda4eafddc0f80a`, `1816c88f4095b9f59c9df86a` query=`Lens of Character Function…`]
- `FACT` [E2] Schell **Character Tip #2 / Lens of Character Traits**: optional full “character bible” dump is possible, but prefer a **small distilled trait list** that persists across situations; traits should show in words, actions, and appearance (including animation/movement). Mentions character bible as exhaustive listing exercise. [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_ids=`1816c88f4095b9f59c9df86a`, `0b6620b973f311863b2c5ed6`, `afc2df1479cccbce2f14b5b2`]
- `FACT` [E2] Schell further tools: **Interpersonal Circumplex** (friendliness × dominance relative to a reference character); **Lens of the Character Web** (how each character feels about each other; unused/similar connections); **Lens of Status** (relative status behaviors; conflicts/changes of status; player expression of status). [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_ids=`afc2df1479cccbce2f14b5b2`, `1e2345284a56f9d51401fb7d`, `65fa2bd87e771a4371c334c8`, `c5f13ef5c0d9f45bc9259e2b`]
- `FACT` [E2] Jeff Ashworth (*Game Master’s Book of Non-Player Characters*) — **TTRPG/GM toolkit**, not a video-game systems manual. Method-relevant entry pattern: name + common phrase + read-aloud description + GM-only backstory + **Wants & Needs** + **Secret or Obstacle** + **Carrying**; organize by environment then proximity to power (insider/outsider). Explicitly for **narrative consistency** of everyday denizens and on-the-fly play. Customize freely; details are optional hooks. [E2: Alexandria corpus=`game_design` source=`The Game Masters Book of Non-Player Characters…pdf` chunk_ids=`580cdacdfc3cab0074462e13`, `aaabd6c5008dc9d3e4c4be15`, `ae81429f48daa5406e466b94`, `73bef3a464d0788ec86d51a1`, `2ba4ade677bc22a83418c05a` query=`NPC entry structure…`]
- `INFERENCE` [E4] Human+agent character consistency pack (candidate, not lock): **function list** + **3–7 locked traits** + **wants/needs** + **secret/public split** + **relationship/status notes** — enough for critique prompts (“does this line violate traits?”) without a novel-length character dump. Premises: Schell tips; Ashworth fields; Hungerford cast pages.

### 4.4 Lane D — Medium / role distinctions (do not conflate)

- `FACT` [E2] Monte Cook: novelists, game designers, and GMs use “worldbuilding” differently. Novelist: backdrop — only story-needed world on the page; excess is often waste. Game designer: more detail because PCs may go anywhere; plus “teach to fish” flavor so GMs can generate appropriate material. GM: between — multiple possible stories for the table, but can build as needed for the current group. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`30cddb1e4781b0e3422f87dd`, `b7d3485e95f57daec4d4d358` query=`Monte Cook Different Kinds…`]
- `FACT` [E2] Cook/Baur context: published RPG settings often act as a **canvas** with many adventure options (feeds KSD pressure); novels tend toward one primary story focus. [E2: Alexandria corpus=`game_design` source=`Kobold Guide to Worldbuilding…` chunk_ids=`30cddb1e4781b0e3422f87dd`, `96f98b02a664cfd992ca8748`]
- `FACT` [E2] Schell character/world chapters are framed for **game design** (avatars, functions for gameplay roles, animation/voice process, transmedia gateways) — not GM improvisation manuals. [E2: Alexandria corpus=`game_design` source=`Schell…` chunk_ids=`09cd3103da188ae3449584fd`, `5d37f280b164ab7e1fca9cd6`, `c5f13ef5c0d9f45bc9259e2b`]
- `FACT` [E2] Ashworth NPC book is explicitly a **5e/System Reference Document–adjacent GM aid** for table improvisation and side quests — method pattern transferable as **fields**, not as video-game AI companion design law. [E2: Alexandria corpus=`game_design` source=`The Game Masters Book of Non-Player Characters…` chunk_id=`ae81429f48daa5406e466b94`]
- `CLAIM` [E2] Academic anthology hit (Krampe in Bonner ed.): video-game worldbuilding involves interactive space, dynamic state models, and immersion via navigation — distinct from static setting bibles. Discovery only for this slice; not method-locked. [E2: Alexandria corpus=`game_design` source=`Game World Architectonics…pdf` chunk_id=`6da4b7ab0422515256ccb2d5` query=`worldbuilding prompts…`]
- `GAP` Dedicated **video-game character pipeline** SoT (casting, systemic NPC AI, dialogue tools) beyond Schell lenses — not fully covered; W2/W3 if needed.
- `GAP` Gygax *World Builder* / *Nation Builder* / *Living Fantasy* present in corpus but not mined for method extraction this slice (risk: lore/table dumps vs methods).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | A world bible with scoped sections + glossary + living dated drafts is the primary W1 pattern for multi-author/human continuity | confirmed (Kobold/Hungerford) | §4.1 |
| H2 | Anti-kitchen-sink **focus** is the main coherence constraint at setting scale | confirmed (Baur) | §4.2 |
| H3 | Distilled traits + character functions beat exhaustive personality essays for game characters | confirmed (Schell) | §4.3 |
| H4 | Novelist / GM / published designer / VG designer need separate method profiles in any Toolbelt Design skill | open (strong W1 support; skill shape deferred) | §4.4; campaign false-friend caveat |
| H5 | Same bible fields can serve agents as read-before-generate constraints | open | INFERENCE only; agent critique → W3 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Completeness vs focus | Hungerford/Anderson encourage structured coverage (bible sections / GCPESRIAH) | Baur anti-KSD / Anderson “don’t include everything” in delivery | **No hard conflict** if checklist = design-time inventory and delivery = focused subset. Leave OPEN how large the inventory should be for agent contexts |
| Inside-out vs outside-in | Pramas inside-out for speed/organic growth | Pramas outside-in for framework/customization | Pramas: mix OK; choose by time-to-play and medium |
| Exhaustive character bible vs distilled traits | Schell mentions exhaustive character bible exercise | Schell prefers small trait list for use | Prefer distilled traits for playable consistency; exhaustive dump optional prep |
| Novelist backdrop vs designer canvas | Cook: novelist waste if not story-focused | Cook: designer needs go-anywhere detail | **Lane D** — medium-dependent; do not force one completeness rule |

## 7. Gaps & OPEN

- `GAP` W2 corroboration with narrative slice (S2) — how story structure binds world/character constraints.
- `GAP` GDD / template-repo inventories (E3) — campaign W2.
- `GAP` Gygaxian Fantasy Worlds method extraction (tables vs principles).
- `GAP` Video-game systemic NPC / dialogue consistency tooling literature.
- `OPEN` Agent creative critique / HITL for world+character drafts — Wave 3 slice.
- `OPEN` Exact machine-readable schema for Toolbelt world/character constraint files — not evidenced; do not invent.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] Any later Design skill for worldbuilding should **fork by medium**: novelist backdrop · GM living campaign · published RPG canvas · video-game world/characters — sharing only transferable constraints (focus, rules+costs, glossary, traits, functions). Premises: §4.4.
- `INFERENCE` [E4] Minimum viable **world constraint pack** (candidate): one-page conflict/theme intro; magic/physics rules+costs; Terra De Facto default; essential glossary; focus boundary (what is *not* in scope); dated version. Premises: Hungerford; Presley; Day; Baur.
- `INFERENCE` [E4] Minimum viable **character constraint pack** (candidate): role/function; 3–7 traits; wants/needs; secret vs public; key relationships/status. Premises: Schell; Ashworth; Hungerford cast.
- `INFERENCE` [E4] Human+agent workflow (ties to T5A, not locked here): human owns bible acceptance; agent proposes within constraints and flags contradictions; kitchen-sink expansion requires human scope change. Premises: §4.1 INFERENCE; T5A spine.

## 9. Source list (deduped)

1. *Kobold Guide to Worldbuilding* (Open Design / Kobold Press; essays incl. Hungerford, Baur, Pramas, Monte Cook, Roberts, et al.) — Alexandria `game_design` source_id=`27de5d0f404ae431` — key chunk_ids: `96b66444fa96442938413dfa`, `414702d6c75016e474a68ca0`, `0c80314681a37b3ead7a51e2`, `f57f2a35a6993e59856732ac`, `db0365696d3b396d30aff570`, `73e1d64710ca404a4b13f59f`, `96f98b02a664cfd992ca8748`, `bd1c459c07ae309bb3d34a8f`, `e7d8c1e282eaf6f7cb30e6fb`, `2faf13d33d9d2f3c78e32e8d`, `096a6529a2af130b1de941f7`, `60feef5d4efef8118f88c33c`, `30cddb1e4781b0e3422f87dd`, `b7d3485e95f57daec4d4d358`, `8a1cf96e37ad6b148beec10c`, `95743144beb12ae3e0cae17d`, `1b745832e5d8db11429108c6` — **E2**
2. Jesse Schell — *The Art of Game Design: A Book of Lenses* (3rd / Tenth Anniversary) — Alexandria `game_design` source_id=`db6ade4db2428023` — key chunk_ids: `09cd3103da188ae3449584fd`, `a6be08f8db840cace07b7227`, `5d37f280b164ab7e1fca9cd6`, `a999998ffeda4eafddc0f80a`, `1816c88f4095b9f59c9df86a`, `0b6620b973f311863b2c5ed6`, `afc2df1479cccbce2f14b5b2`, `1e2345284a56f9d51401fb7d`, `65fa2bd87e771a4371c334c8`, `c5f13ef5c0d9f45bc9259e2b`, `f726a26fa863078af7f641be` — **E2**
3. M. D. Presley — *101 Worldbuilding Prompts* — Alexandria source_id=`2df4b254a3197b85` — chunk_ids: `0dd71270c5a8438c61a81677`, `54b279b1620162ebf23dec09`, `e84eebfb9d06df73e892012b` — **E2**
4. Kylie Day — *How to Get to Know Your Story’s World With Worldbuilding Questions* — Alexandria source_id=`e6d07b56084977c7` — chunk_id=`06f9bfc55fd1b9710f65b505` — **E2**
5. Kevin J. Anderson — *Worldbuilding: From Small Towns to Entire Universes* — Alexandria source_id=`8d7f72eede859d07` — chunk_ids: `5a7c9d7931bdf38a6133db61`, `d7e190908fe7579c17acb804`, `025f120b63aec80af2f8be6a`, `af4507ced830ab58bb563d40` — **E2**
6. Jeff Ashworth — *The Game Master’s Book of Non-Player Characters* — Alexandria source_id=`adb18be70bce6b39` — chunk_ids: `580cdacdfc3cab0074462e13`, `aaabd6c5008dc9d3e4c4be15`, `ae81429f48daa5406e466b94`, `73bef3a464d0788ec86d51a1`, `2ba4ade677bc22a83418c05a` — **E2** (TTRPG/GM)
7. Discovery only: Marc Bonner (ed.) *Game World Architectonics* — chunk_id=`6da4b7ab0422515256ccb2d5` — **E2** discovery (interactive VG worldbuilding), not method-locked
8. Listed unused this slice: Gygax *World Builder* / *Living Fantasy* / *Nation Builder*; Kobold Guides to Plots/Magic/Monsters — **GAP** for method mining
9. Campaign context (local): `docs/research/notes/theme-5-design/campaign-brief.md` — **E0** brief only

---

## Parent return summary (FACTS / CLAIMS / GAPs)

**FACTS (E2 Alexandria):** Hungerford world bible = World / Cast / Appendices + living dated drafts + key-facts-only + continuity guard. Baur: kitchen-sink design harms coherence; prefer focus under resource limits. Pramas: inside-out vs outside-in (mix OK). Presley: top-down/bottom-up; audience inside-out; Terra De Facto; conceit order. Day/Anderson: magic rules+costs; skeptic consistency pass; GCPESRIAH inventory ≠ dump everything into story. Schell: world integrity / immersion fragility; Character Function + distilled Traits + Web + Status. Ashworth: GM NPC fields (phrase, wants/needs, secret/obstacle, carrying) for table consistency — TTRPG lane. Cook: novelist vs designer vs GM worldbuilding differ.

**CLAIMS:** Explicit allow/deny beats missing licensor bibles; academic interactive-space worldbuilding ≠ setting-bible law.

**GAPs / OPEN:** S2 narrative bind; GDD E3; Gygax method mine; VG systemic NPC tooling; W3 agent critique; no invented machine schema.
