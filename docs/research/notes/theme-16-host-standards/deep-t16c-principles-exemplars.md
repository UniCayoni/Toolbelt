---
title: "Deep T16C — Agent-readable foundational principles exemplars"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
updated: 2026-08-02
depth: deep
track: T16C
authors: [gatherer-t16c-principles]
supersedes: null
related:
  - docs/research/notes/theme-16-host-standards/t16c-foundational-principles.md
  - docs/research/notes/theme-16-host-standards/campaign-brief.md
---

# Deep T16C — Agent-readable foundational principles exemplars

**Using `research-protocol`.** Depth: deep. Cite-or-omit. Draft ≠ SoT.

## 1. Scope

- **Question / goal (close G1):** Find **agent-readable foundational principles** exemplars — philosophy / tone / values docs (not checkable coding standards). Prefer primary sources with short quotes.
- **In scope:** Company eng culture / operating / leadership principles; open-source `PRINCIPLES.md` / `ENGINEERING_VALUES.md` / culture-like files; Shape Up philosophy excerpts if principles-like; relation to AGENTS.md / contributor guides; anatomy and length/tone patterns.
- **Out of scope:** Lintable style guides as design locks; Toolbelt-universal morality rule; elevating any exemplar as host law; Thoughtworks Radar as a principles template (channel checked — see findings).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-02 |
| Tools used | WebSearch; WebFetch (primary URLs + GitHub raw); GitHub MCP `search_code` / path samples; Alexandria RAG `rag_query` |
| Corpora / URLs searched | Alexandria `software_engineering`, `ai_llm_agents`; amazon.jobs LPs; Netflix culture; Stripe jobs culture; Google eng-practices + styleguide philosophy; Basecamp Shape Up ch.1–2; Thoughtworks Radar FAQ; Airbnb Eng Medium posts; raw GitHub paths listed in §9 |
| Queries (exact) | Web: Google eng practices philosophy; Amazon Leadership Principles; Netflix culture memo; Stripe operating principles; Airbnb engineering culture; Thoughtworks Technology Radar principles. GitHub: `filename:PRINCIPLES.md`; `filename:ENGINEERING_PRINCIPLES.md`; `filename:ENGINEERING_VALUES.md`; `filename:CULTURE.md`; `principles filename:AGENTS.md`. RAG: engineering principles vs coding standards; project principles AGENTS.md; architecture principles / Agentic Mesh principle definition |
| What was *not* searched | Private/internal company wiki dumps; exhaustive scrape of all 8000+ `PRINCIPLES.md` hits; non-English culture decks; paid HBR cases beyond public snippets |
| Depth | deep |
| Waves / stop_reason | Single gatherer deep pass for T16C exemplars. **stop_reason:** diminishing returns — primary company pages fetched with quotes; ≥8 GitHub raw exemplars sampled; RAG on both target corpora; filename searches for CULTURE/ENGINEERING_VALUES largely noise or low-signal; further hits unlikely to change anatomy pattern or G1 close |
| Provenance (optional PROV) | Entity=principles exemplars; Activity=web+gh+rag gather 2026-08-02; Agent=gatherer-t16c-principles |

## 3. Strategy

| Field | Value |
|-------|-------|
| Mode | systematic (named channels) + hybrid sampling of GitHub filename hits |
| Why this mode | Campaign brief comparator channels; G1 needs primary exemplars not secondary summaries alone |
| Scope boundary | Philosophy/tone/values; exclude checkable coding standards except as contrast |

## 4. Findings

### 4.1 What makes a doc “principles” vs “standards” (real exemplars)

- `FACT` [E1] Amazon’s Leadership Principles page frames LPs as used “every day… discussing ideas for new projects or deciding on the best way to solve a problem,” with named principles (e.g. Customer Obsession, Ownership, Bias for Action) each given a short behavioral paragraph — decision/culture language, not file-format or lint rules. Quote: “We use our Leadership Principles every day…” [E1: Amazon Leadership Principles — https://www.amazon.jobs/content/en/our-workplace/leadership-principles — accessed 2026-08-02]
- `FACT` [E1] Stripe’s public culture page states operating principles “describe how we work – how we make decisions, collaborate, and serve our users” and “began as a way to make our implicit culture explicit,” listing few named behaviors (Users first; Create with craft and beauty; Move with urgency and focus; Collaborate egolessly; Stay curious; Obsess over talent). [E1: Stripe’s Operating Principles — https://stripe.com/jobs/culture — accessed 2026-08-02]
- `FACT` [E1] Netflix’s culture memo opens as culture based on “four core principles” (The Dream Team; People Over Process; Uncomfortably Exciting; Great and Always Better) and expands into narrative sections on values, decision rights (“context not control”), and minimal rules (e.g. expenses: “Act in Netflix’s best interests.”). [E1: Netflix Culture — https://jobs.netflix.com/culture — accessed 2026-08-02]
- `FACT` [E1] Google’s eng-practices “Standard of Code Review” separates a **senior principle** of continuous improvement (“favor approving a CL once it… improves the overall code health… even if the CL isn’t perfect”) from a **Principles** subsection that elevates “Technical facts and data overrule opinions” and states that on **style**, “the style guide is the absolute authority,” while design choices are weighed on “underlying principles.” This is an explicit principles-vs-style-guide fence inside one primary doc. Quote: “On matters of style, the style guide is the absolute authority.” [E1: The Standard of Code Review — https://google.github.io/eng-practices/review/reviewer/standard.html — accessed 2026-08-02]
- `FACT` [E1] Google’s documentation styleguide **Philosophy** page is imperative/philosophy sections (Radical simplicity; Readable source text; Minimum viable documentation; Better is better than best) without checkable formatting tables — principles-for-docs, not a coding standard. Quote: “Brief and utilitarian is better than long and exhaustive.” [E1: Philosophy — https://google.github.io/styleguide/docguide/philosophy.html — accessed 2026-08-02]
- `FACT` [E1] Holochain’s `PRINCIPLES.md` states intent as “shared principles we want to uphold… The intention is not to be a prescription for how we make every decision, but rather a set of guiding principles.” [E1: holochain/holochain `PRINCIPLES.md` — https://raw.githubusercontent.com/holochain/holochain/develop/PRINCIPLES.md — accessed 2026-08-02]
- `FACT` [E1] AWS Containers Roadmap `PRINCIPLES.md` titles itself principles that “embody the culture of the container services organization” and “build on the Amazon Leadership Principles,” organized as People / Priorities / Product bullets (reliability, UX, open source) — culture layer, not CI lint. [E1: aws/containers-roadmap `PRINCIPLES.md` — https://raw.githubusercontent.com/aws/containers-roadmap/master/PRINCIPLES.md — accessed 2026-08-02]
- `CLAIM` [E2] Secondary literature distinguishes XP “coding standards” (team must follow sensible standards for collective ownership) from broader process philosophy (e.g. 40-hour week, on-site customer) — standards as coordination mechanism inside a larger values stack. [E2: Alexandria corpus=`software_engineering` source=`Software Development, Design, and Coding…` chunk_id=`33b1067eee2c779641678ac3` query=`engineering principles vs coding standards`]
- `CLAIM` [E2] Agentic Mesh defines a good principle as “a foundational guideline that frames values and shapes decision making… providing guideposts and guardrails,” durable when “technologies will shift.” [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh…` chunk_id=`1e5ba341f84966972cd48b4f` query=`foundational guideline frames values`]
- `INFERENCE` [E4] Across these exemplars, **principles** docs optimize for *decision tone / conflict resolution / continuity* (few named north-stars + rationale); **standards** docs optimize for *checkable conformity* (style authority, ops checklists). Premises: Amazon/Stripe/Netflix/Holochain FACTS + Google style-vs-principles FACT + E2 claims above.
- `GAP` Google C++ Style Guide also uses the word “principle” (e.g. “Optimize for the reader, not the writer”) inside a **standards** document — lexical overlap does not make it a principles-genre exemplar for T16C. Searched: styleguide primary; Result: principles-as-rationale-inside-standards, not a standalone philosophy memo. [E1 contrast: https://google.github.io/styleguide/cppguide.html — accessed 2026-08-02 via search/fetch]

### 4.2 Typical section anatomy of principles docs

Observed recurring anatomy (from primary samples):

| Section pattern | Exemplars |
|-----------------|-----------|
| Purpose / “why this doc exists” | Holochain (“living document…”); Stripe (“make implicit culture explicit”); Netflix intro |
| Named principle list (title + 1–3 sentence body) | Amazon LPs; Stripe OPs; Netflix four cores |
| Grouped themes (People / Process / Product) | aws/containers-roadmap |
| Narrative expansion under each principle | Netflix (long); Shape Up “Principles of Shaping” (chapter) |
| Values nested under a principle | Netflix Dream Team → Selflessness, Judgment, Candor… |
| Reasoning / Benefits / Guidelines under each principle | SLSA `spec/principles.md` |
| Explicit non-prescription disclaimer | Holochain |
| Domain design axioms (numbered) | OCI runtime-spec `principles.md`; OpenMined PySyft `principles.md` |
| Living / evolve note | Netflix (“culture (and this document) will, too”); Holochain |

- `FACT` [E1] SLSA guiding principles pages use a repeated micro-structure: principle title → explanation → **Reasoning** → **Guidelines** or **Benefits** (and sometimes Corollary/Example). [E1: slsa-framework/slsa `spec/principles.md` — https://raw.githubusercontent.com/slsa-framework/slsa/main/spec/principles.md — accessed 2026-08-02]
- `FACT` [E1] Basecamp Shape Up “Principles of Shaping” structures philosophy as contrast pairs (wireframes too concrete / words too abstract) then properties (rough, solved, bounded) — process philosophy anatomy, not a style checklist. [E1: Principles of Shaping — https://basecamp.com/shapeup/1.1-chapter-02 — accessed 2026-08-02]
- `FACT` [E1] Holochain’s principles file then continues into Documentation / Testing subsections that look operational — genre blur: same file mixes guiding intent with concrete practice expectations. [E1: holochain/holochain `PRINCIPLES.md` — accessed 2026-08-02]
- `INFERENCE` [E4] A reusable anatomy for agent-loadable principles is: (1) purpose + fence (“guide, don’t prescribe every decision”), (2) ≤N named principles with short rationale, (3) optional anti-patterns / “not this”, (4) evolution note. Premises: Holochain + Stripe + Amazon + SLSA FACTS.

### 4.3 Short vs long; imperative vs narrative

- `FACT` [E1] Amazon LPs: **short-form imperative titles** + brief narrative paragraphs; ~16 items on one page. [E1: amazon.jobs LPs — accessed 2026-08-02]
- `FACT` [E1] Stripe: **six** principle headings with ~1 paragraph each; intermediate length; mostly imperative lead-ins (“Users first.”). [E1: stripe.com/jobs/culture — accessed 2026-08-02]
- `FACT` [E1] Netflix: **long-form narrative memo** with four cores at top, then multi-section storytelling; includes quotes and extended policy examples. [E1: jobs.netflix.com/culture — accessed 2026-08-02]
- `FACT` [E1] Perkeep `doc/principles.md`: ultra-short bullet sketch with TODO; philosophy fragments (“Put the user in control. Own your data.”). [E1: https://raw.githubusercontent.com/perkeep/perkeep/master/doc/principles.md — accessed 2026-08-02]
- `FACT` [E1] PySyft `principles.md`: long **numbered** list (18+) of “X-first” axioms with blockquote “📜” expansions — imperative slogans + explanatory narrative. [E1: https://raw.githubusercontent.com/OpenMined/PySyft/dev/principles.md — accessed 2026-08-02]
- `FACT` [E1] Shape Up principles chapter: long narrative + case study; process philosophy at book-chapter length. [E1: basecamp.com/shapeup/1.1-chapter-02 — accessed 2026-08-02]
- `INFERENCE` [E4] Agent-readable sweet spot in the sample set is **short named list + one paragraph rationale each** (Amazon/Stripe/aws containers/nextdns AGENTS Core Principles); mega-memos (Netflix, Shape Up chapters) remain valuable but need section anchors for load. Premises: length FACTS above + nextdns FACT in §4.4.

### 4.4 Relation to AGENTS.md / contributor guides

- `FACT` [E1] GitHub code search `principles filename:AGENTS.md` returns many hits; sampled **nextdns/nextdns** `AGENTS.md` embeds a **Core Principles** section (Privacy first; Reliability and safety; …) *before* Agent Instructions / Testing — principles as loadable agent context inside AGENTS.md, not a separate standards file. Quote (structure): `## Core Principles` then numbered privacy/reliability items. [E1: https://raw.githubusercontent.com/nextdns/nextdns/master/AGENTS.md — accessed 2026-08-02]
- `FACT` [E1] Other sampled AGENTS.md files use “Key Principles” / “Operating Principles” / “Design Principles” headings (search text_matches: hunvreus/devpush, nipreps/mriqc, aspiers/stow, etc.). [E1: GitHub MCP `search_code` query=`principles filename:AGENTS.md` — observed 2026-08-02]
- `FACT` [E1] Separate `ENGINEERING_VALUES.md` exists but is rare: search `filename:ENGINEERING_VALUES.md` reported `total_count`: 10; sampled paths include `bdbch/ai-dotfiles/instructions/ENGINEERING_VALUES.md` (agent instruction pack: DX + “Agentic coding should accelerate my learning”) and `Mornieur/Design-System/docs/philosophy/ENGINEERING_VALUES.md` (Simplicity First, Explicit Trade-Offs, …). [E1: GitHub MCP search + raw fetches — accessed 2026-08-02]
- `FACT` [E1] `filename:PRINCIPLES.md` is common (`total_count` ≈ 8040 on search); popular/public samples include aws/containers-roadmap, holochain/holochain, opencontainers/runtime-spec, tensorflow/agents (Google AI principles copy), perkeep, OpenMined/PySyft, slsa-framework/slsa. [E1: GitHub MCP `search_code` query=`filename:PRINCIPLES.md` — observed 2026-08-02]
- `FACT` [E1] Airbnb engineering culture is published as **blog posts** (not a repo `PRINCIPLES.md` in this search): “At the core our philosophy is this: engineers own their own impact.” Later posts advise “guiding them with principles” and reviewing engineering values. [E1: https://medium.com/airbnb-engineering/engineering-culture-at-airbnb-345797c17cbe — accessed 2026-08-02]
- `CLAIM` [E2] Agent literature argues principles steer autonomous agents toward org values and provide durable reference points across sessions/tech change. [E2: Alexandria corpus=`ai_llm_agents` chunk_id=`1e5ba341f84966972cd48b4f` / related `0476fa273518ec98ee1300a8`]
- `INFERENCE` [E4] Today’s dominant “agent-readable principles” pattern is **section inside AGENTS.md** (or sibling instruction file), not a universal separate `PRINCIPLES.md` genre; company culture memos are often web/PDF and must be linked/copied for agents. Premises: nextdns/AGENTS FACT + ENGINEERING_VALUES rarity FACT + company web FACTS.
- `GAP` No systematic primary survey in this pass of CONTRIBUTING.md → PRINCIPLES.md link frequency across top repos. Searched: filename PRINCIPLES/AGENTS/ENGINEERING_VALUES; Result: AGENTS embedding observed; CONTRIBUTING link pattern not measured.

### 4.5 Channel notes (requested comparators)

- `FACT` [E1] Thoughtworks Technology Radar FAQ describes a twice-yearly **technology recommendation** snapshot (blips, rings Adopt/Trial/Assess/Caution), not an org philosophy/values principles document. [E1: https://www.thoughtworks.com/radar/faq — accessed 2026-08-02]
- `INFERENCE` [E4] Radar is a poor T16C principles exemplar (wrong genre); useful only as contrast — recommendation catalog ≠ foundational principles. Premises: FAQ FACT.
- `FACT` [E1] `filename:CULTURE.md` search returned many unrelated link-dumps / interview Q lists / non-eng “culture” pages; high `total_count` but weak signal for company eng culture memos in-repo. [E1: GitHub MCP `search_code` query=`filename:CULTURE.md` — observed 2026-08-02]
- `FACT` [E1] tensorflow/agents `PRINCIPLES.md` is a copy of “AI at Google: our principles” (ethics/use constraints), showing PRINCIPLES.md filename used for company AI ethics as well as team culture. [E1: https://raw.githubusercontent.com/tensorflow/agents/master/PRINCIPLES.md — accessed 2026-08-02]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Principles docs are fewer, stabler, decision-oriented vs checkable standards | confirmed (for sampled primaries) | Amazon/Stripe/Netflix/Holochain/Google fence FACTS |
| H2 | Agent-readable form is usually AGENTS.md section, not separate PRINCIPLES.md | confirmed (pattern) / still OPEN as “best” shape | nextdns + search FACTs; shape track OPEN |
| H3 | Thoughtworks Radar is a principles exemplar | rejected | FAQ FACT |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Word “principle” inside style guides | Google C++ Style Guide uses “principle” for reader-optimization rules | Campaign T16C wants philosophy ≠ coding standards | Prefer genre by **checkability + purpose**; treat C++ guide as standards-with-rationale, not T16C exemplar |
| Holochain PRINCIPLES.md content | Declares non-prescriptive guiding principles | Same file includes concrete testing/doc layout rules | Note as **genre blur**; cite both layers; do not treat whole file as pure philosophy |

## 7. Gaps & OPEN

- `GAP` **Named genre “project PRINCIPLES.md for coding agents”** still thin as a *separate* standard path — most agent-facing principles appear inside AGENTS.md / instruction packs. Searched: GH PRINCIPLES + AGENTS + ENGINEERING_VALUES + RAG ai_llm_agents. Result: AGENTS embedding common; dedicated PRINCIPLES for agents uncommon.
- `GAP` **CONTRIBUTING ↔ principles linking** not quantified across popular repos.
- `GAP` **CULTURE.md** filename is a poor discovery key (noise); Netflix/Stripe culture live on careers sites, not `CULTURE.md`.
- `GAP` No primary in this pass proving a shared industry conflict stack (ADR > principles > standards); prior T16C note’s stack remains `INFERENCE` only.
- `OPEN` Host shape choice: separate `PRINCIPLES.md` vs section in AGENTS.md vs section in standards pack (campaign shape track / T16K).
- `OPEN` Ideal length/token budget for agent load (short Stripe-like vs long Netflix) — no measured agent-eval evidence here.
- `OPEN` Whether ethics/AI principles files (tensorflow/agents copy) should share the same host slot as product/eng philosophy.

## 8. Implications (INFERENCE only — not design law)

- `INFERENCE` [E4] For Toolbelt hosts closing T16C: treat principles as **loadable continuity** (named few + rationale + fence), distinct from checkable standards profiles consumed by Plan/Execute/Closeout. Premises: §4.1–4.4.
- `INFERENCE` [E4] Prefer citing company web primaries or repo PRINCIPLES with purpose disclaimers; do not treat Thoughtworks Radar or style guides as principles templates. Premises: §4.5 + Google fence FACT.
- `INFERENCE` [E4] If agents already load AGENTS.md, a **Core Principles** section (nextdns pattern) is the path of least friction observed; a separate PRINCIPLES.md remains viable when humans want a stable, rarely-edited continuity artifact. Premises: §4.4 FACTS.

## 9. Source list (deduped)

1. https://www.amazon.jobs/content/en/our-workplace/leadership-principles
2. https://jobs.netflix.com/culture
3. https://stripe.com/jobs/culture
4. https://google.github.io/eng-practices/review/reviewer/standard.html
5. https://google.github.io/eng-practices/
6. https://google.github.io/styleguide/docguide/philosophy.html
7. https://basecamp.com/shapeup/0.3-chapter-01
8. https://basecamp.com/shapeup/1.1-chapter-02
9. https://www.thoughtworks.com/radar/faq
10. https://medium.com/airbnb-engineering/engineering-culture-at-airbnb-345797c17cbe
11. https://raw.githubusercontent.com/aws/containers-roadmap/master/PRINCIPLES.md
12. https://raw.githubusercontent.com/holochain/holochain/develop/PRINCIPLES.md
13. https://raw.githubusercontent.com/opencontainers/runtime-spec/main/principles.md
14. https://raw.githubusercontent.com/perkeep/perkeep/master/doc/principles.md
15. https://raw.githubusercontent.com/slsa-framework/slsa/main/spec/principles.md
16. https://raw.githubusercontent.com/OpenMined/PySyft/dev/principles.md
17. https://raw.githubusercontent.com/tensorflow/agents/master/PRINCIPLES.md
18. https://raw.githubusercontent.com/nextdns/nextdns/master/AGENTS.md
19. https://raw.githubusercontent.com/bdbch/ai-dotfiles/main/instructions/ENGINEERING_VALUES.md
20. https://raw.githubusercontent.com/Mornieur/Design-System/main/docs/philosophy/ENGINEERING_VALUES.md
21. Alexandria `software_engineering` chunk_id=`33b1067eee2c779641678ac3`
22. Alexandria `ai_llm_agents` chunk_id=`1e5ba341f84966972cd48b4f` (also related `0476fa273518ec98ee1300a8`)
23. GitHub MCP searches 2026-08-02: `filename:PRINCIPLES.md`, `filename:ENGINEERING_PRINCIPLES.md`, `filename:ENGINEERING_VALUES.md`, `filename:CULTURE.md`, `principles filename:AGENTS.md`

## 10. Sampled GitHub paths (raw snippets — for integrator)

| Path | Snippet / role |
|------|----------------|
| `aws/containers-roadmap/PRINCIPLES.md` | Culture principles building on Amazon LPs; People/Priorities/Product |
| `holochain/holochain/PRINCIPLES.md` | Explicit non-prescription guiding principles + later practice sections |
| `opencontainers/runtime-spec/principles.md` | “5 principles of Standard Containers” domain axioms |
| `perkeep/perkeep/doc/principles.md` | Ultra-short philosophy bullets |
| `slsa-framework/slsa/spec/principles.md` | Guiding principles with Reasoning/Benefits |
| `OpenMined/PySyft/principles.md` | Numbered “X-first” product principles |
| `tensorflow/agents/PRINCIPLES.md` | Google AI principles (ethics genre) |
| `nextdns/nextdns/AGENTS.md` | Core Principles section inside AGENTS.md |
| `bdbch/ai-dotfiles/instructions/ENGINEERING_VALUES.md` | Agent-pack engineering values (DX / learning) |
| `Mornieur/Design-System/docs/philosophy/ENGINEERING_VALUES.md` | Short values: Simplicity First, Explicit Trade-Offs |

---

**Self-check:** Depth recorded; stop_reason recorded; Method present; FACT/CLAIM cited; INFERENCEs listed premises; no invented URLs; draft ≠ SoT; GAPs named.
