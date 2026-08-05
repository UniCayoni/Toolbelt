---
title: "T24G-web — Continual-learning loops for proposed durable rules/skills/docs"
status: draft
theme: theme-24-author-learning
track: T24G
gatherer: T24G-web
created: 2026-08-05
updated: 2026-08-05
authors: [t24g-web-gatherer]
depth: deep
waves: W1
stop_reason: diminishing_returns_primary_corpus
supersedes: null
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
---

# T24G-web — Continual-learning comparators (web)

**Using `research-protocol`**. Depth: **deep** (Wave 1 gatherer). Draft ≠ law. Prefer papers/official docs (E1) over SEO blogs.

## 1. Scope

- **Question / goal:** What proven patterns exist for learning loops that produce **proposed** durable rules / skills / docs with **human gates** (never auto-accept as workspace SoT)?
- **In scope:** Reflexion; ExpeL; Voyager; MemGPT/Letta; structured agentic SE / continuous-improvement for coding agents; postmortems → runbooks/action items; transfer map to Cursor **host/workspace harvest** vs research-only.
- **Out of scope:** Alexandria RAG pass (T24G-RAG); GitHub org/repo scrape (T24G-gh); elevating `author-learning`; rewriting Toolbelt plugin `skills/*`; personal (non-workspace) memory as primary SoT; auto-accept as Toolbelt law.
- **Comprehension / research goal type:** other (secondary web research for continual-learning pattern atoms).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | WebSearch, WebFetch; local read of Theme 24 campaign brief + deep campaign board |
| Corpora / URLs searched | See §9 Source list; Method envelope below |
| Queries (exact) | See below |
| What was *not* searched | Alexandria RAG (sibling); GitHub code search beyond named repos in SERP; paid books; classic Wooldridge “agent-oriented programming” survey corpus beyond naming note; non-English sources; fine-tuning / weight-update continual learning (outside Theme 24 non-parametric harvest) |
| Depth | deep |
| Waves / stop_reason | W1; `diminishing_returns_primary_corpus` — core papers (Reflexion, ExpeL, Voyager, MemGPT) + Letta official memory docs + Google SRE/Cloud postmortem E1 + SASE arXiv vision covered; further SEO “agent memory” blogs restated same atoms without new human-gate mechanisms |
| Provenance (optional PROV) | Entity←fetched URLs; Activity=T24G-web gather 2026-08-05; Agent=WebSearch+WebFetch |

### Exact search terms

1. `Reflexion language agents verbal reinforcement learning Shinn paper arxiv`
2. `ExpeL experiential learning LLM agents Zhao paper arxiv`
3. `Voyager Minecraft LLM agent lifelong learning Wang paper arxiv`
4. `MemGPT Letta agent memory system official documentation`
5. `MemGPT Towards LLMs as Operating Systems arxiv 2310.08560`
6. `AOP agentic continuous improvement coding agents postmortem runbook`
7. `Agentic Oriented Programming continuous improvement coding agents human approval`
8. `Google SRE postmortem best practices runbooks documentation continuous improvement`
9. `arXiv Structured Agentic Software Engineering SASE 2509.06216`
10. `site:docs.letta.com sleeptime dreaming memory consolidation human`

### URLs accessed (WebFetch / retrieved), accessed 2026-08-05

| URL | Role |
|-----|------|
| https://arxiv.org/abs/2303.11366 | E1 Reflexion abstract/paper landing |
| https://arxiv.org/abs/2308.10144 / https://arxiv.org/html/2308.10144v2 | E1 ExpeL |
| https://andrewzh112.github.io/expel/ | E1 ExpeL project page (methodology summary) |
| https://arxiv.org/abs/2305.16291 | E1 Voyager |
| https://voyager.minedojo.org/ | E1 Voyager project site |
| https://arxiv.org/abs/2310.08560 | E1 MemGPT |
| https://docs.letta.com/guides/core-concepts/memory/context-hierarchy/ | E1 Letta context hierarchy |
| https://docs.letta.com/guides/core-concepts/memory/memory-blocks/ | E1 Letta memory blocks |
| https://docs.letta.com/guides/agents/architectures/sleeptime | E1 Letta dreaming / sleeptime |
| https://arxiv.org/abs/2509.06216 / https://arxiv.org/html/2509.06216v2 | E1/E2 SASE vision (agentic SE) |
| https://sre.google/sre-book/postmortem-culture/ | E1 Google SRE postmortem culture |
| https://cloud.google.com/architecture/framework/reliability/conduct-postmortems | E1 Google Cloud WAF postmortems |

**Attempted / weak:** `https://raw.githubusercontent.com/boshu2/agentops/main/docs/cdlc.md` → 404 on WebFetch 2026-08-05; AgentOps CDLC claims kept at **E3** from SERP snippets only (not design law).

**Search hits noted but not treated as design law (E3 / marketing):** Prompting Guide Reflexion page; Hackernoon runbooks-RAG blog; brightcoding AgentOps blog; PDCA Claude-skill repos; agentic-pipeline README.

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Web secondary research; no local code corroboration required for external pattern atoms |
| Scope boundary | Public papers + official product/SRE docs; Theme 24 host harvest fence from accepted campaign brief |

## 4. Findings

### 4.1 Pattern atoms (external systems)

- `FACT` [E1] **Reflexion** reinforces language agents via **linguistic feedback** (not weight updates): agents verbally reflect on task feedback, store reflective text in an **episodic memory buffer**, and use it to improve subsequent trials. [E1: Reflexion — https://arxiv.org/abs/2303.11366 — accessed 2026-08-05]

- `FACT` [E1] Reflexion reports large task gains on decision-making, reasoning, and coding (e.g., HumanEval pass@1 claim vs GPT-4 baseline in abstract) while remaining flexible about feedback type/source. [E1: Reflexion — https://arxiv.org/abs/2303.11366 — accessed 2026-08-05]

- `FACT` [E1] **ExpeL** gathers trajectories by trial-and-error (with reflection on failures), stores successes/failures in an **experience pool**, then **extracts and iteratively refines natural-language insights** (add/edit/vote), and at inference recalls insights + similar successful trajectories—without parametric updates. [E1: ExpeL project methodology — https://andrewzh112.github.io/expel/ — accessed 2026-08-05] [E1: ExpeL arXiv — https://arxiv.org/abs/2308.10144 — accessed 2026-08-05]

- `FACT` [E1] ExpeL also studies **transfer** of insights across task distributions (e.g., HotpotQA → FEVER) via adaptation with target few-shots. [E1: ExpeL project — https://andrewzh112.github.io/expel/ — accessed 2026-08-05]

- `FACT` [E1] **Voyager** is an open-ended lifelong learning agent with (1) automatic curriculum, (2) ever-growing **skill library** of executable code indexed for retrieval, (3) iterative prompting using environment feedback, execution errors, and **self-verification** before committing a skill—without fine-tuning. [E1: Voyager — https://arxiv.org/abs/2305.16291 — accessed 2026-08-05] [E1: Voyager site — https://voyager.minedojo.org/ — accessed 2026-08-05]

- `FACT` [E1] Voyager commits a program to the skill library only after self-verification confirms task completion; skills are compositional and claimed to alleviate catastrophic forgetting vs some continual-learning baselines. [E1: Voyager — https://arxiv.org/abs/2305.16291 — accessed 2026-08-05]

- `FACT` [E1] **MemGPT** proposes **virtual context management** (OS-inspired hierarchy): manage tiers so a limited LLM context window can support extended document analysis and multi-session agents that “remember, reflect, and evolve.” [E1: MemGPT — https://arxiv.org/abs/2310.08560 — accessed 2026-08-05]

- `FACT` [E1] **Letta** (product lineage of MemGPT) documents a **context hierarchy**: always-in-context editable **memory blocks** (optional `read_only`); partial in-context **files**; out-of-context **archival memory** via insert/search tools; optional external RAG. Importance + scale drive which tier. [E1: Letta context hierarchy — https://docs.letta.com/guides/core-concepts/memory/context-hierarchy/ — accessed 2026-08-05]

- `FACT` [E1] Letta memory blocks persist across interactions, are always visible, and agents can update them via memory tools; docs explicitly suggest use cases such as **tool-usage guidelines to avoid past mistakes** and **read-only shared policies**. [E1: Letta memory blocks — https://docs.letta.com/guides/core-concepts/memory/memory-blocks/ — accessed 2026-08-05]

- `FACT` [E1] Letta **dreaming / sleeptime** uses background subagents to review recent conversations, consolidate useful lessons, and update memory without interrupting active work; humans can also teach with `/remember` (agent places the lesson and commits to MemFS). [E1: Letta Memory & dreaming — https://docs.letta.com/guides/agents/architectures/sleeptime — accessed 2026-08-05]

- `FACT` [E1] Google SRE defines a **postmortem** as a written record of incident, impact, mitigation, root cause(s), and **follow-up actions to prevent recurrence**; primary goals include documentation, understanding causes, and **effective preventive actions**. [E1: SRE Book Ch.15 — https://sre.google/sre-book/postmortem-culture/ — accessed 2026-08-05]

- `FACT` [E1] SRE practice includes **formal review** of postmortem drafts (completeness, root-cause depth, action-plan appropriateness/priority, stakeholder sharing) and the best practice **“No Postmortem Left Unreviewed.”** [E1: SRE Book Ch.15 — https://sre.google/sre-book/postmortem-culture/ — accessed 2026-08-05]

- `FACT` [E1] Google Cloud Well-Architected reliability guidance restates the postmortem workflow: create → capture facts → root-cause analysis → **plan for the future** → **execute the plan**, with blameless culture and wide sharing. [E1: Conduct thorough postmortems — https://cloud.google.com/architecture/framework/reliability/conduct-postmortems — accessed 2026-08-05]

- `CLAIM` [E1] **Structured Agentic Software Engineering (SASE)** vision paper argues durable, version-controlled artifacts should replace ephemeral chat: human-authored BriefingScript / LoopScript / **MentorScript** (best-practices guide); agent-generated Consultation Request Packs (CRPs) and Merge-Readiness Packs (MRPs); humans reply with **Version Controlled Resolutions (VCRs)**. [E1: Hassan et al. arXiv:2509.06216 — https://arxiv.org/abs/2509.06216 — accessed 2026-08-05]

- `FACT` [E1] The same SASE paper states that when a human gives a contextual correction, the agent should **propose a general rule for the coach to approve** before adding it to MentorScript (“Inferred Mentorship”), and that explicit generalizable guidance must be captured durably to prevent repeated mistakes. [E1: arXiv:2509.06216v2 HTML — https://arxiv.org/html/2509.06216v2 — accessed 2026-08-05]

- `GAP` Classic acronym **AOP** (“Agent-Oriented Programming”) vs product **AgentOps** / **agentic** continuous improvement: searched `AOP agentic continuous improvement coding agents postmortem runbook`; strongest structured human-gate literature hit was SASE (MentorScript + VCR). AgentOps “CDLC / forge / flywheel” appears in community repos/blogs but raw `docs/cdlc.md` WebFetch 404’d → insufficient E1 for Toolbelt locks. Searched: AOP + agentops CDLC. Result: naming collision; treat AgentOps as **E3 discovery only**.

- `CLAIM` [E3] Community AgentOps-style systems describe postmortem → extract learnings (`forge`) → score/promote (`flywheel`) into a local `.agents/` corpus with validation gates—pattern-relevant as discovery, **not** corroborated primary paper here. [E3: SERP/docs hits for boshu2/agentops — not WebFetch-verified 2026-08-05]

### 4.2 Cross-cutting loop shapes (evidence-backed)

| Loop shape | Sources | Human gate in source? | Durable artifact |
|------------|---------|----------------------|------------------|
| Reflect → episodic text → next trial | Reflexion | Typically **no** (auto reuse in buffer) | Episodic reflections (trial-scoped) |
| Experience pool → NL insight extract/vote → recall | ExpeL | **No** human accept in paper loop | Insight set + trajectories |
| Verify-then-commit skill to library | Voyager | **No** human; self-verification critic | Executable skill programs |
| Tiered memory + optional background consolidate | MemGPT / Letta | Partial: `/remember`, read-only blocks, human review of MemFS; agent also self-writes | Memory blocks / MemFS / archival |
| Postmortem → reviewed action items → system/docs change | Google SRE / Cloud WAF | **Yes** — review, priority, execute plan | Postmortem + tracked follow-ups / manuals |
| Propose general rule → coach approve → MentorScript | SASE | **Yes** (explicit coach approval) | Versioned mentorship rules |
| Extract → promote to corpus (AgentOps-like) | Community | Claimed gates; **E3 only** here | Local agent corpus |

### 4.3 Transfer map — Cursor plugin **host/workspace harvest** vs research-only

Theme 24 accepted lean: candidates → **proposed** host skills / standards / AGENTS via author path; **never auto-promote**; not Toolbelt plugin skill rewrite. [E0: campaign brief path=`docs/research/notes/theme-24-author-learning/campaign-brief.md` — observed 2026-08-05]

| External pattern | Transfers to host harvest (comparator) | Research-only / do **not** copy as Toolbelt law |
|------------------|----------------------------------------|--------------------------------------------------|
| Reflexion verbal reflection + episodic buffer | After closeout/failure: emit **candidate** reflection atoms with evidence pointers | Auto-inject reflections as always-on rules without human accept |
| ExpeL insight extraction + add/edit/vote | Structured harvest of NL insights from success/fail trajectories; vote/score as quality filter input | Autonomous insight pool treated as accepted standards |
| Voyager verify-then-commit skill library | Evidence gate before proposing a host skill (tests/run outcome/self-check); retrieval by description | Unattended curriculum; auto-commit executable skills without human gate; Minecraft-specific stack |
| MemGPT/Letta tiers | Map: always-on blocks ≈ AGENTS/standards; files/archival ≈ RAG/docs; `read_only` policies ≈ accepted host modules | Agent self-editing workspace SoT; personal chat memory as primary SoT; product-specific MemFS runtime |
| Letta `/remember` + dreaming | Explicit human teach; optional offline consolidate → **proposed** candidates for review | Background dream auto-merging into accepted host law |
| SRE postmortem → action items + review | Triggered, blameless, evidence-backed writeups; owned follow-ups that update runbooks/docs; “left unreviewed = failed” | Auto-merge agent-written runbooks; blame culture; complexity for one-off incidents (Cloud WAF warns against over-engineering) |
| SASE MentorScript + coach-approve inferred rules | Closest literature match to **proposed durable rules with human gate**; VCR as accept artifact | Full ACE/AEE product vision; inventing BriefingScript languages as Toolbelt requirement |
| AgentOps forge/flywheel | Discovery: extract→score→promote pipeline shape | Copy CDLC ceremony, `.agents/` schema, or auto-promote as law (E3; fetch unverified) |

### 4.4 Answer to the track question (labeled)

- `INFERENCE` [E4] **Proven pattern for proposed durable rules/skills/docs with human gates** is closest to the **SRE postmortem → reviewed action items → update living docs** loop plus the **SASE “propose general rule → coach approve → MentorScript”** mentorship pattern; research agent loops (Reflexion/ExpeL/Voyager) prove **non-parametric learning from experience** but mostly **omit** a human acceptance gate before durable promotion. Premises: (1) Reflexion/ExpeL/Voyager facts above; (2) SRE review + preventive actions facts; (3) SASE inferred-mentorship + VCR claim; (4) Theme 24 hard fence never auto-promote [E0 campaign brief].

- `INFERENCE` [E4] For Cursor host harvest, a transferable composite is: **evidence-gated extract** (ExpeL/Voyager/Reflexion atoms) → **structured candidate** → **human review/accept** (SRE/SASE) → **author path** into host skills/standards/AGENTS—not into Toolbelt plugin skills. Premises: transfer table §4.3 + campaign brief lean.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Non-parametric agent learning commonly stores NL insights or skills without human accept | confirmed | Reflexion, ExpeL, Voyager E1 |
| H2 | Human-gated durable promotion is better attested in ops/SE process literature than in agent benchmark papers | confirmed | SRE + SASE vs Reflexion/ExpeL/Voyager |
| H3 | “AOP” in the brief maps cleanly to a single primary paper | rejected / revised | Naming collision; SASE is best E1 for human-gated mentorship; AgentOps E3 only |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Auto self-improve vs human gate | Voyager “without human intervention”; Letta agent-managed blocks | SRE review; SASE coach approve MentorScript | Prefer **both** as pattern classes: auto loops are research efficacy; **human gates** are the Theme 24 transfer requirement. No single source defines Toolbelt law. |
| Memory as SoT | Letta agent-updated MemFS / blocks | Theme 24 park: personal memory ≠ primary workspace SoT | Prefer Theme 24 accepted fence for product; Letta remains comparator only. |

## 7. Gaps & OPEN

- `GAP` No E1 primary paper found in this pass that evaluates **Cursor-plugin host-workspace harvest** with proposed-only elevation specifically.
- `GAP` AgentOps CDLC/forge/flywheel not WebFetch-verified (404); leave to T24G-gh if still needed.
- `OPEN` Whether ExpeL-style insight voting is a good quality filter for T24F (cross-track) without inventing metrics.
- `OPEN` Mapping Letta `read_only` blocks ↔ Theme 16 accepted host standards modules (E0 local) deferred to integrator / T24C.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Wave-1 design implication for `author-learning` (still draft): treat external agent “memory/skill libraries” as **candidate factories**, and treat SRE/SASE review/approve as the **promotion gate**—aligns with draft≠SoT. Premises: §4.3–4.4.
- `INFERENCE` [E4] Do **not** lock Toolbelt on Voyager auto-commit, Letta self-write SoT, or AgentOps flywheel auto-promote. Premises: Theme 24 hard fence + grade limits on E3.

## 9. Source list (deduped)

1. https://arxiv.org/abs/2303.11366 — Reflexion (Shinn et al.)
2. https://arxiv.org/abs/2308.10144 — ExpeL (Zhao et al.)
3. https://andrewzh112.github.io/expel/ — ExpeL project page
4. https://arxiv.org/abs/2305.16291 — Voyager (Wang et al.)
5. https://voyager.minedojo.org/ — Voyager project site
6. https://arxiv.org/abs/2310.08560 — MemGPT (Packer et al.)
7. https://docs.letta.com/guides/core-concepts/memory/context-hierarchy/
8. https://docs.letta.com/guides/core-concepts/memory/memory-blocks/
9. https://docs.letta.com/guides/agents/architectures/sleeptime
10. https://arxiv.org/abs/2509.06216 — Agentic Software Engineering / SASE (Hassan et al.)
11. https://arxiv.org/html/2509.06216v2 — SASE HTML
12. https://sre.google/sre-book/postmortem-culture/
13. https://cloud.google.com/architecture/framework/reliability/conduct-postmortems
14. `docs/research/notes/theme-24-author-learning/campaign-brief.md` — E0 Theme 24 lean

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Stop rule applied (`diminishing_returns_primary_corpus`)
- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented citations/APIs
- [x] Conflicts logged
- [x] Draft/proposed not treated as design law
