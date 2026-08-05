---
title: "T24F — RAG gather: good vs bad guidelines/patterns/standards candidates"
status: draft
theme: theme-24-author-learning
track: T24F
created: 2026-08-05
updated: 2026-08-05
authors: [deep-wave1-gatherer]
supersedes: null
depth: deep
waves: "Wave 1 gatherer (RAG surface)"
stop_reason: "diminishing returns on additional same-corpus style/pattern queries; evidence clustered around practitioner books (E3); thin on formal evidence-based standards catalogs"
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
hard_fences:
  - not Toolbelt plugin self-modify
  - not auto-accept
  - draft ≠ law
---

# T24F — What retrieved evidence says about GOOD vs BAD catalog candidates

**Using `research-protocol`**. Depth: **deep** (Wave 1 gatherer). Status: **draft** — discovery only; not host catalog law; not auto-accept.

## 1. Scope

- **Question / goal:** What does Alexandria RAG retrieval say about identifying **GOOD vs BAD** guidelines / patterns / standards candidates for a **host** catalog (Theme 24 author-learning → proposed feedstock)?
- **In scope:** Coding/style standards quality; checkable rules vs vague principles; pattern quality criteria; style-guide anti-patterns; evidence-oriented engineering measurement signals.
- **Out of scope:** Toolbelt plugin `skills/*` rewrite; auto-promote to accepted SoT; Theme 23 playbook; CI ceremony as primary; inventing host module bodies.
- **Comprehension / research goal type:** reuse (harvest quality tests for candidate filter) + other (campaign method feedstock).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | Alexandria MCP `user-alexandria-rag`: `list_corpora`, `rag_query` (schema via GetMcpTools); research-protocol note template |
| Corpora / URLs searched | Registered corpora: `ai_llm_agents`, `data_sql`, `finance_trading`, `game_design`, `games_engine_graphics`, `programming_algorithms_systems`, `software_engineering` (active index `v1` each). Queries mostly `corpus=all` or scoped `software_engineering` / `games_engine_graphics`. |
| Queries (exact) | See §2.1 |
| What was *not* searched | Web / primary standards orgs (ISO/IEEE official pages as live fetch); GitHub style-guide repos; Toolbelt host `docs/standards/` (no accepted catalog observed at gather time); Theme 16 report body; `rag_fetch_chunk` deep re-read beyond query payloads; hierarchical retrieval / query_transform |
| Depth | deep |
| Waves / stop_reason | Wave 1 RAG gatherer. Stop: further queries returned overlapping GoF/Clean Code/FDG/Gregory hits; evidence-based query largely index noise + architecture-metrics fitness-function material — diminishing returns. |
| Provenance (optional PROV) | Entity←Alexandria chunks; Activity=`rag_query` 2026-08-05; Agent=deep-wave1-gatherer |

### 2.1 Exact queries

1. `What makes good software coding standards guidelines style guides? Quality criteria for useful standards documents` — corpus=`all`, k=10
2. `checkable rules versus vague principles in coding standards style guides enforceable guidelines` — corpus=`all`, k=10
3. `software design pattern quality criteria how to identify good patterns versus bad patterns` — corpus=`all`, k=10
4. `anti-patterns for style guides coding standards guidelines what makes bad standards documents fail` — corpus=`all`, k=10
5. `evidence-based software engineering standards guidelines empirical research what works best practices quality criteria` — corpus=`software_engineering`, k=12
6. `encode coding style into IDE formatter linter enforce team rules automatically checkable conventions vs personal preference` — corpus=`all`, k=10
7. `design patterns wrong place increase complexity misuse anti-pattern when not to use patterns consequences trade-offs` — corpus=`all`, k=10
8. `Framework Design Guidelines principles clarity for reader over brevity required vs optional conventions do and don't` — corpus=`software_engineering`, k=10
9. `coding standards minimal set why and how much religious debates interfaces names consistency make errors stick out` — corpus=`games_engine_graphics`, k=8

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed (RAG discovery surface for T24F) |
| Why this mode | Campaign brief assigns T24F → RAG+web+E0; this note is RAG-only gatherer |
| Scope boundary | Alexandria retrieval only; no host file edits beyond this note |

## 4. Findings

Evidence grade note: retrieved books/guides are **community / practitioner literature** → label honestly as **`CLAIM` [E3]** unless a chunk is a primary standard text cited as such. Do **not** lock host catalog design from E3 alone.

### 4.1 What “good” standards / guidelines look like (signals)

- `CLAIM` [E3] Coding standards serve two primary purposes: (1) readability / understandability / maintainability; (2) preventing foot-guns via a smaller, more testable language subset. A **minimal** set is advised; debates are often “religious.” [E3: Alexandria corpus=`games_engine_graphics` source=`[Game Engine Architecture] Gregory…` chunk_id=`bb1f52f880644cd381614eed` query=`coding standards minimal set…` quote=`"Coding standards exist for two primary reasons"` / `"at least a minimal set"`]

- `CLAIM` [E3] Priority convention goals include: clean minimal interfaces; intuitive names (no lookup-table schemes); avoid global-namespace clutter; consistency (invent when greenfield, **follow existing** when editing); and conventions that make **common errors stick out** (not merely “neat” code). [E3: corpus=`games_engine_graphics` chunk_id=`61715e65fc3a014358ef8211` query=`coding standards minimal set…` quote=`"Make errors stick out"` / `"Be consistent"`]

- `CLAIM` [E3] Team formatting rules beat personal favorites; agree once, **encode into the IDE formatter**, stick to it — readers must trust that formatting gestures mean the same across files. [E3: corpus=`software_engineering` source=`Clean Code… Martin` chunk_id=`861a282dc2c1828b5f6b1495` query=`encode coding style into IDE formatter…` quote=`"if he works in a team, then the team rules"` / `"encoded those rules into the code formatter"`]

- `CLAIM` [E3] Uniform formatting should be tool-enforced (e.g. Black/Blue) because divergent personal formatters cause merge-conflict waste. [E3: corpus=`software_engineering` source=`Clean Code Principles And Patterns Python…` chunk_id=`b471efe460863595f5023b43` query=`encode coding style…` quote=`"preferably use a tool like Black or Blue to enforce"`]

- `CLAIM` [E3] Framework/API guidelines that matter to consumers can be treated as stronger than internal coding-style suggestions; style appendix is explicitly **not required** because it has “no direct effect on most users of a framework.” Style principles: **clarity for the reader over brevity of the writer**; prefer expressions that reduce noise in future diffs. [E3: corpus=`software_engineering` source=`Framework Design Guidelines…` chunk_id=`0dd1833076c70d52564cb33a` query=`Framework Design Guidelines principles…` quote=`"not required and should be treated as a set of suggestions"` / `"clarity wins"`]

- `CLAIM` [E3] Good guideline presentation uses a **strength ladder** (DO / CONSIDER / AVOID / DO NOT), presented as guidelines managing trade-offs rather than absolute laws; novel API concepts should be rare. [E3: corpus=`software_engineering` chunk_id=`66a5513db4b3b22b06edb31f` quote=`"DO, CONSIDER, AVOID, and DO NOT"`; chunk_id=`09763ec11b600a4e14ad412a` quote=`"guidelines, rather than rules"` / `"managing trade-offs"`]

- `CLAIM` [E3] A useful UI/style guide is often “this, not this” — examples of correct vs incorrect use; purpose is **not** to solve every problem but to give tools/boundaries for new cases. [E3: corpus=`game_design` source=`The Pocket Mentor for Video Game UX UI…` chunk_id=`9a66abb5fef13ce16a85fb07` query=`What makes good software coding standards…` quote=`"boils down to this, not this"` / `"isn't to solve every problem"`]

- `CLAIM` [E3] Consistency of the style guide itself: set standards, stick to them; avoid special cases; propagate changes board-wide. [E3: corpus=`game_design` source=`Practical Game Design…` chunk_id=`bef9f8afffd0215bcd8d1857` query=`checkable rules versus vague principles…` quote=`"Avoid special cases and exceptions at all costs"`]

### 4.2 Checkable rules vs vague principles

- `CLAIM` [E3] Checkable layer: formatter/linter alignment (“Variable name should be lowercase”, “Line too long”); run formatter to match project style. [E3: corpus=`software_engineering` source=`Beyond Vibe Coding… Osmani` chunk_id=`efcf2ca4206b2f35ee812647` query=`encode coding style…` / anti-patterns query quote=`"Run the code through your formatter or linter"`]

- `CLAIM` [E3] Naming quality is only **partially** automated — reviews should still focus on proper/uniform naming; static analysis alone is insufficient. [E3: corpus=`software_engineering` chunk_id=`b471efe460863595f5023b43` quote=`"static code analysis tools can only partially do is ensure proper and uniform naming"`]

- `CLAIM` [E3] For LLM/agent guidance, a **precise schema / semantic blueprint** beats an open-ended request for predictable adherence to structure and style. [E3: corpus=`ai_llm_agents` source=`Context Engineering for Multi_Agent Systems…` chunk_id=`f6fa8ae1bbec7038fc4c7e1d` query=`checkable rules versus vague principles…` quote=`"precise schema rather than an open-ended request"`]

- `CLAIM` [E3] Vague success criteria (and vague references) are called out as prompt/process failure modes — implies catalog candidates that cannot state checkable success conditions are weak. [E3: corpus=`software_engineering` chunk_id=`02a3a1fd4b0e19f0db7ed8e4` query=`checkable rules…` (index hit: `"success criteria (vague), in prompts"`); chunk_id=`34a02ff8b47a7bad549f160f` quote=`"Vague references like “the above code”"`]

- `INFERENCE` [E4] Host-catalog candidates that are **machine-checkable** (formatter/linter/fitness function) are stronger keepers than aspirational slogans; principles still belong when they define judgment where tools stop (naming intent, trade-offs). Premises: (1) Martin/Silen formatter encode claims; (2) Silen naming partial-automation claim; (3) FDG required-vs-optional distinction.

### 4.3 Pattern / design-pattern quality criteria

- `CLAIM` [E3] A pattern’s essential elements: **name**, **problem** (when to apply / context / conditions), **solution** (abstract arrangement, not one concrete implementation), **consequences** (trade-offs; critical for evaluating alternatives). [E3: corpus=`software_engineering` source=`Design Patterns GoF` chunk_id=`e61a7eb1b4daf78a580f20be` query=`design patterns wrong place…` quote=`"four essential elements"` / `"consequences are … critical for evaluating"`; also Dooley chunk_id=`d9135aa9bbe0b535c4d31020`]

- `CLAIM` [E3] Pattern catalog entries that follow a strict shared format (name, intent, motivation, applicability, structure, participants, collaborations, consequences) improve usability for design — not only analysis. [E3: corpus=`game_design` source=`Game Mechanics Advanced Game Design…` chunk_id=`dd9e66a0e6086fb0d1b3a72c` query=`software design pattern quality criteria…` quote=`"follow a strict format"` / `"Applicability"` / `"Consequences"`]

- `CLAIM` [E3] Good pattern use requires knowing the **problem first**, then selecting/adapting the pattern; wrong-place application “needlessly increas[es] the complexity … with little gain.” [E3: corpus=`games_engine_graphics` source=`Game Development Patterns…` chunk_id=`204c62007f1e47090b52dae8` query=`design patterns wrong place…` quote=`"when implemented in the wrong place"` / `"needlessly increasing the complexity"`]

- `CLAIM` [E3] Pattern knowledge ≠ mandatory use; “it is the knowledge of the pattern that holds the most important value, not using the pattern itself” (KISS). Patterns add complexity/performance cost; prefer simpler solutions for simple problems. [E3: corpus=`games_engine_graphics` chunk_id=`4e72e59c91aecd86e3541ba9` quote=`"K.I.S.S"` / `"knowledge of the pattern"`]

- `CLAIM` [E3] Patterns get a bad rap when applied to the wrong problem and make things worse (even if correctly implemented). [E3: corpus=`games_engine_graphics` source=`Game Programming Patterns Nystrom` chunk_id=`ed705e4a177fb3e3de6b7bc4` query=`design patterns wrong place…` quote=`"apply good patterns to the wrong problem"`]

### 4.4 Anti-patterns / “bad candidate” signals

- `CLAIM` [E3] Abuse: using pattern recognition as a substitute for documenting module design (“improving code readability” via reverse-engineering patterns). [E3: corpus=`game_design` chunk_id=`77d4d0e08bad3f2af35a3ec9` query=`software design pattern quality criteria…` / wrong-place query quote=`"abuse of design patterns"` / `"Reverse engineering"`]

- `CLAIM` [E3] Some named patterns are widely regarded as anti-patterns in practice (example retrieved: Singleton ~ global value / design flaws). [E3: corpus=`programming_algorithms_systems` source=`C# Notes for Professionals…` chunk_id=`60db73513d64102a4da03ebe` query=`anti-patterns for style guides…` quote=`"widely regarded as an anti-pattern"`]

- `CLAIM` [E3] Inconsistent naming / failing to apply standard style are debt contributors (often mitigable with assistants); pressure/shortcuts amplify bad outcomes. [E3: corpus=`software_engineering` chunk_id=`fae0a5840683ec9777245a0c` query=`anti-patterns for style guides…` quote=`"Inconsistent naming conventions"` / `"Failing to apply standard style conventions"`]

- `CLAIM` [E3] Overly complex rewrites for simple style fixes (agent case study) — actionable, tiered response templates beat vague or overbuilt guidance. [E3: corpus=`ai_llm_agents` chunk_id=`27e8eca6eb37cd8a7df2e7a1` query=`What makes good…` / anti-patterns quote=`"overly complex rewrites for simple style fixes"`]

- `CLAIM` [E3] Multi-agent / complex orchestration for simple tasks is an anti-pattern: start simplest; add complexity only when evaluation shows benefit. [E3: corpus=`ai_llm_agents` source=`Designing Multi-Agent Systems…` chunk_id=`241d13a9842d335e3d2d0d63` query=`design patterns wrong place…` quote=`"Start with the simplest pattern that could work"` / `"Common Anti-Pattern"`]

### 4.5 Evidence-oriented / measurable standards (thin but present)

- `CLAIM` [E3] Architecture quality work ties guidelines to **measurable** quality attributes and **fitness functions**; automate when meaningful; align effort to stakeholder quality goals (ISO 25010 catalog referenced in-book). [E3: corpus=`software_engineering` source=`Software Architecture Metrics…` chunk_id=`a81370e6d1c6e7757d943af8` query=`evidence-based software engineering…` quote=`"fitness function"` / `"ISO … 25010"`; related TOC chunk_id=`5b534e0d50274da08d3fd4f5`]

- `GAP` Direct hits for “evidence-based software engineering” as a methodology corpus were **weak** — query 5 returned substantial index/TOC noise from AI-coding books plus architecture-metrics material; no strong EBSE primary-study synthesis chunk rose as top evidence in this pass. Searched: query 5 on `software_engineering` k=12. Result: thin/noisy.

### 4.6 Hard fences (campaign / protocol — local)

- `FACT` [E0] Theme 24 accepted lean hard-fences: never auto-promote; draft≠SoT; evidence-based; **not** Toolbelt plugin self-modify; host feedstock only. [E0: path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` observed 2026-08-05]
- `FACT` [E0] This note `status: draft` — not accepted catalog law (`draft-is-not-sot`). [E0: this file frontmatter]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Good host-catalog candidates state purpose (readability vs foot-gun), strength (DO vs CONSIDER), and checkability (lint/format/fitness) | confirmed (as E3 discovery signal) | Gregory; FDG ladder; Martin/Silen formatter |
| H2 | Good pattern candidates require problem/applicability + consequences; “pattern name only” is a bad candidate | confirmed (E3) | GoF four elements; Doran wrong-place; Nystrom |
| H3 | “This not that” examples + refuse-to-solve-everything improve guideline quality | confirmed (E3, UI-style-adjacent) | Brewer style guide chunk |
| H4 | Corpora contain strong EBSE / empirical standards-quality meta-analyses for catalog filters | rejected / thin | Query 5 noisy; GAP recorded |
| H5 | Required API/consumer-facing rules should outrank optional formatting preferences in a catalog | open (plausible) | FDG required vs style appendix — needs host Theme 16 alignment |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| How much coding standard | Gregory: minimal set; avoid religious overreach | Clean Code / Silen: team must pick one style and encode/enforce | Prefer both: **minimal + enforced** for format; keep judgment principles fewer and strength-labeled. OPEN for host policy weight. |
| Patterns as readability aid | GoF/Dooley: vocabulary aids understanding | Quaye: pattern-spotting abused as substitute for design docs | Cite both: vocabulary good; reverse-eng substitute **bad candidate**. |
| Style guide completeness | Brewer: not every problem | Practical Game Design: avoid exceptions at all costs | OPEN: completeness vs rigidity — FDG CONSIDER/AVOID ladder mediates. |

## 7. Gaps & OPEN

- `GAP` Thin retrieval on formal **anti-patterns for style-guide documents** themselves (most “anti-pattern” hits were code/pattern misuse, not meta-guide failure modes).
- `GAP` Weak EBSE / empirical “what works” literature in top ranks for query 5.
- `GAP` No E0 pass in this note against a live host `docs/standards/` catalog (catalog missing / not accepted at gather — standards-resolve no-op).
- `OPEN` How to score checkable vs principle candidates in T24B atom fields (handoff to integrator + T24B).
- `OPEN` Web/primary-standard gatherer still needed per campaign (T24F = RAG+web+E0).

## 8. Implications (INFERENCE only)

Label clearly. **Do not** promote to design lock without human acceptance.

- `INFERENCE` [E4] For host catalog **keep** filters, prefer candidates that: (a) name a recurring problem + context; (b) state consequences/trade-offs; (c) offer check path (tool/example/test) or explicit strength (DO vs CONSIDER); (d) show this/not-this; (e) stay minimal and team-consistent. Premises: §4.1–4.3 CLAIMs.
- `INFERENCE` [E4] For host catalog **reject / park** filters, flag candidates that: (a) are pattern names without problem/consequences; (b) increase complexity without stated problem; (c) substitute vibes for checkable success; (d) conflict with existing local convention without migration note; (e) imply auto-accept. Premises: §4.2–4.4 + E0 fences.
- `INFERENCE` [E4] Distinguish **consumer-facing / API-law** modules from **optional style** modules when routing harvest → standards (FDG appendix distinction). Premises: chunk `0dd1833076c70d52564cb33a`.

## 9. Source list (deduped)

1. Alexandria `games_engine_graphics` — Gregory, *Game Engine Architecture* — chunk_ids `bb1f52f880644cd381614eed`, `61715e65fc3a014358ef8211`
2. Alexandria `software_engineering` — Martin, *Clean Code* — `861a282dc2c1828b5f6b1495`
3. Alexandria `software_engineering` — Silen, *Clean Code Principles And Patterns Python* — `b471efe460863595f5023b43`
4. Alexandria `software_engineering` — Cwalina/Barton/Abrams, *Framework Design Guidelines* — `0dd1833076c70d52564cb33a`, `66a5513db4b3b22b06edb31f`, `09763ec11b600a4e14ad412a`, `9111f534f9b249739023c356`
5. Alexandria `software_engineering` — Gamma et al., *Design Patterns* — `e61a7eb1b4daf78a580f20be`, `925358a3c14dc1682070fd2d`, `1623ad9154b122122a46fffb`
6. Alexandria `software_engineering` — Dooley/Kazakova — `d9135aa9bbe0b535c4d31020`, `f21a0b4aaa9697af55928760`
7. Alexandria `software_engineering` — Osmani, *Beyond Vibe Coding* — `efcf2ca4206b2f35ee812647`, `1cbcb7b0e7b0c4ebe1fc137f`, `3a1b985f972b4f955812e20d`, `02a3a1fd4b0e19f0db7ed8e4`
8. Alexandria `software_engineering` — Esposito, *Clean Architecture with .NET* — `f39c5f586518dd88f13e438c`, `fae0a5840683ec9777245a0c`, `f798d52805120ef8e7a58563`
9. Alexandria `software_engineering` — *Software Architecture Metrics* — `a81370e6d1c6e7757d943af8`, `5b534e0d50274da08d3fd4f5`
10. Alexandria `games_engine_graphics` — Doran/Casanova, *Game Development Patterns* — `204c62007f1e47090b52dae8`, `4e72e59c91aecd86e3541ba9`, `c4935dd625549f3244caa60d`
11. Alexandria `games_engine_graphics` — Nystrom, *Game Programming Patterns* — `ed705e4a177fb3e3de6b7bc4`
12. Alexandria `game_design` — Brewer, *Pocket Mentor… UX UI* — `9a66abb5fef13ce16a85fb07`
13. Alexandria `game_design` — Kramarzewski/De Nucci — `bef9f8afffd0215bcd8d1857`
14. Alexandria `game_design` — *Game Mechanics Advanced Game Design* — `dd9e66a0e6086fb0d1b3a72c`, `dd09c2c0cc69fe7d95d56702`
15. Alexandria `game_design` — Quaye — `77d4d0e08bad3f2af35a3ec9`
16. Alexandria `programming_algorithms_systems` — GoalKicker C# / Python notes — `60db73513d64102a4da03ebe`, `5d249d5b23ef3e0c0aa44d43`
17. Alexandria `ai_llm_agents` — Context Engineering… — `f6fa8ae1bbec7038fc4c7e1d`; Bhavsar — `27e8eca6eb37cd8a7df2e7a1`; Dibia — `241d13a9842d335e3d2d0d63`
18. E0 — `docs/research/notes/theme-24-author-learning/campaign-brief.md`

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Stop rule applied (`stop_reason` in Method)
- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented chunk IDs
- [x] Conflicts logged
- [x] Draft not treated as design law
