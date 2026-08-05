---
title: "T5A W2 — Web/community corroboration of W1 (HITL, AgDR lineage, ADR triggers, Plan Mode)"
status: draft
theme: theme-5-design
track: T5A
slice: T5A-W2-WEB
wave: 2
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5a-w2-web]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/t5a-w1-s2-agent-design-process.md
  - docs/research/notes/theme-5-design/t5a-w1-s3-community-agent-workflows.md
  - docs/PROTOCOL.md
---

# T5A W2 — Web corroboration of W1

**Using `research-protocol`; depth: deep; wave: 2; slice: T5A-W2-WEB.**

**Status:** `draft`. Not Design SoT. Superpowers / AgDR remain E3 structure inventory only — not Toolbelt law. No Design skill elevation. No git/PR policy merge.

## 1. Scope

- **Question / goal:** Corroborate or weaken W1 CLAIMs / E3 inventory with additional web E1–E2 sources (and official vendor docs where available).
- **In scope:** (1) Independent sources on human-led AI design / alternatives-before-code / HITL decision ownership beyond Salesforce/Nava where possible; (2) whether me2resh AgDR has a second independent lineage; (3) AWS (and similar) ADR **process triggers** — when to create ADRs; (4) Cursor Plan Mode **only** from official Cursor docs.
- **Out of scope:** Re-inventory of Superpowers `brainstorming` / `writing-plans` SKILL.md (done in S3); T5B architecture styles content; ADR/MADR template field law (S1); Alexandria corpora (separate W2 surface if scheduled); inventing product behavior.
- **Comprehension / research goal type:** other (corroboration pass)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (W1 S2 + S3 notes; research-note template); WebSearch; WebFetch |
| Corpora / URLs searched | See §9; Method queries below |
| Queries (exact) | `human-led AI architectural decisions alternatives before code HITL`; `AWS Architecture Decision Records when to create ADR`; `Agent Decision Record AgDR me2resh independent`; `site:cursor.com Plan Mode official documentation`; `"agent decision record" OR "AgDR" -me2resh architecture`; `human oversight AI software architecture decision ownership alternatives matrix`; `Nygard architecture decision records when to write ADR` |
| What was *not* searched | Alexandria corpora; Superpowers SKILL.md re-read; AgDR SPEC re-inventory; NIST AI RMF full text; EU AI Act Article 14 primary legal text; E0 Cursor IDE Plan Mode click-through; peer-reviewed GenAI-architecture MLR full texts |
| Depth | deep |
| Waves / stop_reason | wave: **2**; stop_reason: **w2_web_corroboration_diminishing** — independent E1 design-before-code + ADR triggers + official Plan Mode + AgDR lineage probe complete; further vendor-blog chase low signal |
| Provenance (optional PROV) | Entity←W1 notes + vendor/academic web; Activity=T5A-W2-WEB gather; Agent=WebSearch/WebFetch |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Web corroboration of prior gatherer notes; no codebase recon |
| Scope boundary | External web primaries/secondaries only; local W1 notes as alignment context (E0 pin), not new process law |

## 4. Findings

### 4.1 Human-led AI design / alternatives-before-code / HITL ownership (beyond Salesforce)

**Target W1 claims:** S2 Lane A — human-owned criteria → options → critique → decide; AI as partner not owner; design-before-implement spine (`INFERENCE` E4 from Norris/Nava/Fowler).

- `FACT` [E1] Martin Fowler (Thoughtworks) documents **Design-First Collaboration**: AI coding assistants default to generating implementation immediately, embedding design decisions invisibly (“Implementation Trap”). Proposes progressive design levels before code: Capabilities → Components → Interactions → Contracts → Implementation. **Key constraint: no code until Level 5 is approved**; each level is a human checkpoint to agree/disagree/redirect. [E1: Martin Fowler, “Design-First Collaboration” — https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html — published 2026-03-03 — accessed 2026-07-29]
- `FACT` [E1] Fowler Design-First scales levels to task complexity (simple utility may start at Contracts; multi-component at Capabilities); states investment pays for non-trivial work where misunderstanding is costly. [E1: same URL — accessed 2026-07-29]
- `INFERENCE` [E4] Fowler Design-First **corroborates** W1 S2 design-before-implement / human gate before code **independently of Salesforce** (different author org; progressive alignment vs Norris prompt-chained ADR loop). Premises: (1) Fowler E1 no-code-until-approved; (2) S2 Norris E1 human decide / criteria-before-options. Does **not** prove identical process steps.
- `FACT` [E1] MIT CISR research briefing “Designing Decision Rights for AI” (Sebastian et al.): decision rights should vary by **ambiguity × risk**; maintain **clear human accountability**. Breaks decisions into frame / act / learn. For **strategic** (high ambiguity, high risk): human executive sponsors own framing and learning; AI supports acting (surfacing options/analysis). [E1: MIT CISR — https://cisr.mit.edu/publication/2026_0601_AIDecisionMatrix_SebastianWeillHaskampVomBrocke — published 2026-06-18 — accessed 2026-07-29]
- `CLAIM` [E2] MIT CISR: companies adjust human/AI allocation across frame/act/learn by decision type while keeping human accountability; named business owner accountable for agent outcomes (One NZ illustration). Method: 30 executive interviews 2025–2026 — secondary for Toolbelt process locks beyond the stated matrix. [E2: same MIT CISR briefing — accessed 2026-07-29]
- `INFERENCE` [E4] MIT CISR **corroborates** W1 propose-vs-decide ownership for high-ambiguity/high-risk design decisions (human-led framing + accountability). Premises: (1) MIT CISR strategic cell E1; (2) S2 Norris architect accountable E1. Scope is enterprise decision rights, not coding-agent ADR drafting specifically.
- `CLAIM` [E3] Thor Henning Hetland argues execution-time per-action HITL becomes a rubber-stamp bottleneck at agent scale; pivot to **design-time** encoding of judgment (constraints, skills, memory) so agents inherit constraints before writing code. Slogan: “Human-in-the-loop does not mean human-at-every-step… human-at-the-design-step.” Practitioner blog — discovery/E3, not lock. [E3: https://wiki.totto.org/blog/2026/03/16/the-human-in-the-loop--at-design-time/ — accessed 2026-07-29]
- `OPEN` Tension from W1 S2 Conflicts table (Norris course-correct HITL vs design-time-constraint blogs) **remains OPEN** for Toolbelt: Fowler/Norris support **per-decision design gates before code**; Hetland argues **encoding judgment so every step need not be re-approved**. Both may apply at different layers; no W2 resolution.
- `GAP` Additional peer-reviewed / standards-grade primary on GenAI architectural decision loops (beyond MIT CISR briefing + Salesforce) not fetched this slice. Searched: HITL / alternatives / decision-ownership queries. Result: many governance blogs (LaunchReady, COMPEL, RACI posts) — left as discovery, not promoted.
- `INFERENCE` [E4] W1 S2 H1 (“human-owned criteria + options + critique + decide is dominant W1 vendor pattern”) is **strengthened beyond single-vendor Salesforce** by Fowler E1 Design-First, but “dominant industry pattern” remains overclaim — revise to **multi-source corroborated pattern among high-signal design practitioners**, not universal. Premises: Fowler E1; Norris E1; MIT CISR strategic cell.

### 4.2 AgDR — second independent source?

**Target W1:** S3 AgDR structure FACTS graded E3; GAP on adoption/independent corroboration.

- `FACT` [E3] Primary AgDR (Agent Decision Record) artifacts remain on `me2resh/agent-decision-record` and the author blog `me2resh.com` (same lineage inventoried in S3). [E3: https://github.com/me2resh/agent-decision-record ; https://me2resh.com/blog/agent-decision-records — accessed 2026-07-29]
- `GAP` **No second independent source** found that defines, endorses, or normatively extends the me2resh AgDR Markdown SPEC as a separate lineage. Searched: `"agent decision record" OR "AgDR" -me2resh`; marketplace mirrors. Result: ClaudePluginHub `/decide` page is a **mirror/index** of the same me2resh repo — not independent authorship. Repo contributors listed in search snippets include me2resh (+ minor Mohammed-Ashour) — still single-project lineage. **Mark: AgDR (me2resh) remains single-author / single-repo E3.**
- `FACT` [E3] Homonym collision: a distinct project uses the acronym **AgDR** for **Atomic Genesis Decision Record** (cryptographic inference-time audit / PPP triplet), unrelated to me2resh Markdown agent decision docs. [E3: https://github.com/aiccountability-source/AgDR-FSv2.1 ; W3C CG issue mentioning accountability.ai AgDR — https://github.com/w3c-cg/ai-agent-protocol/issues/34 — accessed 2026-07-29]
- `INFERENCE` [E4] Homonym AgDR must not be cited as corroboration of me2resh Agent Decision Records. Premises: (1) different purpose/media (crypto audit vs Markdown options table); (2) different orgs. Treat name collision as **GAP risk** for future gatherers.
- `CLAIM` [E3] S3 GAP on adoption/effectiveness beyond author anecdotes **stands** — W2 web pass found no independent case study / standards body adoption of me2resh AgDR. [E3: negative search result 2026-07-29]

### 4.3 ADR process triggers (AWS + similar) — when to create

**Target:** Process triggers only (not T5B architecture style content). Compare lightly to AgDR “when to create” inventory from S3 as E3 contrast, not law.

- `FACT` [E1] AWS Prescriptive Guidance: project members should create an ADR for **every architecturally significant decision** that affects the software project/product, including: structure (e.g. patterns such as microservices); non-functional requirements (security, HA, fault tolerance); dependencies; interfaces (APIs/contracts); construction techniques (libraries, frameworks, tools, processes). Cites Richards and Ford 2020. [E1: AWS Prescriptive Guidance — ADR process — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — accessed 2026-07-29]
- `FACT` [E1] AWS Prescriptive Guidance ADR lifecycle (process): Proposed → team review (accept / rework / reject) → Accepted becomes **immutable**; later change requires a **new** ADR that can supersede the prior. Team consults ADRs in code/architecture reviews. [E1: same AWS ADR process URL — accessed 2026-07-29]
- `FACT` [E1] Michael Nygard’s original ADR post: keep records for **architecturally significant** decisions — those that affect structure, non-functional characteristics, dependencies, interfaces, or construction techniques. [E1: Michael Nygard, “Documenting Architecture Decisions” — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29]
- `FACT` [E1] Google Cloud Architecture Center ADR overview — prompts for when to create ADRs: (1) technical challenge with **no existing basis** for a decision; (2) solution **not documented** accessibly to the team; (3) **two or more** engineering options and you want to document selection rationale. ADR should capture key options, drivers, and decision. [E1: https://docs.cloud.google.com/architecture/architecture-decision-records — last reviewed 2024-08-16 — accessed 2026-07-29]
- `CLAIM` [E2] AWS Architecture Blog best practices emphasize short readout meetings, single decision per ADR, separate design exploration from the decision record, timely decide (prefer try-fast over endless discussion for reversible decisions), team ownership of approval. Process hygiene — not significance taxonomy. [E2: https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/ — accessed 2026-07-29]
- `INFERENCE` [E4] AWS + Nygard + Google Cloud **corroborate** a shared process trigger family: write an ADR when the choice is **architecturally significant** and/or has **multiple options needing rationale**, not for every trivial change. Premises: AWS E1 significance list; Nygard E1 same axes; Google E1 multi-option / undocumented / no prior basis prompts.
- `INFERENCE` [E4] Contrast (not Toolbelt lock): S3 AgDR “create when” includes library choice, pattern, convention, mid-session agent choices [E3 S3]. AWS/Nygard bar is **architecturally significant** axes — narrower than AgDR’s agent-detected decision patterns. Premises: (1) AWS E1 list; (2) S3 AgDR SPEC §7 / README triggers E3. Do not merge AgDR triggers into ADR law.
- `GAP` This slice did not re-fetch Theme 2 / T5A-S1 ADR template FACTS. Process triggers above are complementary, not a template lock.

### 4.4 Cursor Plan Mode (official docs only)

**Target W1:** S2 `OPEN` — Cursor Plan Mode not verified; Thangamuthu secondary mention. Campaign reserved W3 residual.

- `FACT` [E1] Official Cursor docs: **Plan Mode** creates detailed implementation plans **before writing any code**. Agent researches codebase, asks clarifying questions, generates a reviewable plan the user can edit; user clicks to **build** when ready. Plans default to home directory; “Save to workspace” optional. [E1: Cursor Docs — Plan Mode — https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29]
- `FACT` [E1] Official docs — when Plan Mode works best: complex features with **multiple valid approaches**; tasks touching many files/systems; unclear requirements; **architectural decisions** where you want to review the approach first. For quick/repeated tasks, Agent mode is fine. [E1: same Cursor docs URL — accessed 2026-07-29]
- `FACT` [E1] Official help article restates: generate/review plan before Agent writes code; Shift+Tab to Plan; Build when happy. [E1: https://cursor.com/help/ai-features/plan-mode — accessed 2026-07-29]
- `FACT` [E1] Cursor product blog “Introducing Plan Mode”: plan tools + inline editor; researches files/docs; clarifying questions; Markdown plan with paths/references; edit todos; auto-suggest Plan for complex tasks. [E1: https://cursor.com/blog/plan-mode — accessed 2026-07-29]
- `INFERENCE` [E4] Official Plan Mode docs **corroborate** the W1 plan-then-human-review-then-build checkpoint pattern (Thangamuthu CLAIM / Superpowers inventory topology) at product level: clarify → research → plan → human edit/approve → build. Premises: Cursor E1 how-it-works steps; S2 Thangamuthu plan-then-execute CLAIM. Does **not** lock Toolbelt to Cursor UX or Superpowers paths.
- `OPEN` Residual for W3 / E0: live Cursor IDE behavior (auto-suggest heuristics, exact plan file locations across IDE vs JetBrains ACP, whether Plan Mode enumerates alternatives matrices vs implementation plans). Docs describe **implementation plans**, not Norris-style ADR options matrices — do not invent equivalence.
- `GAP` Deep Plan Mode API/contract surface (CLI flags beyond docs snippets) not exhaustively fetched; sufficient for closing the “no official docs” OPEN from W1.

### 4.5 Cross-slice corroboration status (W1 → W2)

| W1 item | W2 status |
|---------|-----------|
| S2 Norris/Nava human-led criteria→options→decide | **Corroborated** by independent Fowler Design-First E1 + MIT CISR decision-rights E1 (not Salesforce-only) |
| S2 Fowler vibe-coding anti-pattern | Not re-litigated; Design-First E1 adds positive design-gate pattern from same author org family |
| S2 Thangamuthu plan-then-execute / Cursor mention | **Strengthened** by Cursor official Plan Mode E1; product claims no longer sole E2/E3 |
| S2 HITL vs design-time encoding conflict | **Still OPEN** (Hetland E3 fetched; does not defeat per-decision design gates) |
| S3 AgDR structure E3 | Unchanged; **lineage remains single-author E3** + homonym GAP |
| S3 Superpowers structure E0/E3 | Not re-inventoried (per task hard rule) |
| ADR when-to-create | **New E1** AWS + Nygard + Google Cloud process triggers |

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W1 design-before-code / human decide pattern is Salesforce-only | rejected | Fowler Design-First E1; MIT CISR strategic cell E1 |
| H2 | me2resh AgDR has independent second normative source | rejected (for this wave) | GAP — mirrors only; homonym AgDR is different artifact |
| H3 | Cloud vendors document ADR creation triggers at process level | confirmed | AWS PG E1; Google Cloud E1; Nygard E1 |
| H4 | Official Cursor Plan Mode docs exist and match plan-then-build | confirmed | cursor.com/docs + help + blog E1 |
| H5 | Design-time constraint encoding replaces per-decision HITL | open | Hetland E3 vs Norris/Fowler E1 gates — unresolved |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| HITL timing | Norris E1: architect course-corrects AI content at decision steps; Fowler E1: approve each design level before code | Hetland E3: per-step execution HITL fails at scale; prefer design-time infrastructure | **OPEN** — different layers (decision quality vs runtime agent volume). Prefer E1 for design-decision drafting; do not lock anti-per-decision-HITL from E3 |
| AgDR acronym | me2resh Agent Decision Record (Markdown options/Y-statement) E3 | Atomic Genesis Decision Record (crypto audit) E3 | **Do not conflate**; me2resh remains uncorroborated single lineage |
| ADR vs AgDR create-when | AWS/Nygard: architecturally significant axes E1 | AgDR: library/pattern/convention/mid-session E3 | Prefer AWS/Nygard/Google for **ADR process triggers**; AgDR triggers stay E3 inventory only |
| Plan Mode = ADR options matrix | Cursor docs: implementation plan before code E1 | Norris: criteria/options/ADR drafting E1 | No identity claim — related checkpoint pattern only (`INFERENCE` E4) |

## 7. Gaps & OPEN

- `GAP` Independent second source for me2resh AgDR SPEC — **none found**; single-author E3 stands.
- `GAP` AgDR acronym collision (Atomic Genesis Decision Record) — document carefully in integrator merge.
- `GAP` Alexandria corroboration still deferred (not this slice).
- `GAP` Classical non-AI design methods (ATAM etc.) still not primary-fetched (S2 residual).
- `OPEN` Whether Toolbelt Design pack should emphasize per-decision gates (Fowler/Norris) and/or persistent design-time constraint encoding (Hetland) — needs integrator + human accept.
- `OPEN` E0 verification of Cursor Plan Mode UX details / plan file paths across surfaces — optional W3.
- `OPEN` Whether Cursor Plan Mode should be cited as normative Toolbelt process vs optional product affordance — acceptance decision, not gatherer lock.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] T5A design-before-implement spine can cite **multi-source E1** (Salesforce Norris + Fowler Design-First + MIT CISR human accountability for strategic decisions) — stronger than W1 Salesforce-centric H1. Premises: §4.1.
- `INFERENCE` [E4] AgDR must remain **E3 pattern library / discovery only** until an independent lineage or acceptance review; homonym risk argues for spelling out “Agent Decision Record (me2resh)” in any future Design pack draft. Premises: §4.2.
- `INFERENCE` [E4] ADR **when-to-create** guidance for Toolbelt process can lean on AWS Prescriptive Guidance + Nygard significance axes + Google multi-option prompts (E1), kept separate from AgDR mid-session triggers. Premises: §4.3.
- `INFERENCE` [E4] Cursor Plan Mode is now **documentable from official E1** as a plan→review→build product gate; still not Design SoT and not a substitute for ADR options analysis. Premises: §4.4.

## 9. Source list (deduped)

1. Martin Fowler — Design-First Collaboration — https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html — accessed 2026-07-29 — **E1**
2. MIT CISR — Designing Decision Rights for AI (Sebastian et al.) — https://cisr.mit.edu/publication/2026_0601_AIDecisionMatrix_SebastianWeillHaskampVomBrocke — accessed 2026-07-29 — **E1** (interview method → treat applied org claims carefully as **E2**)
3. Thor Henning Hetland — The Human in the Loop — at Design Time — https://wiki.totto.org/blog/2026/03/16/the-human-in-the-loop--at-design-time/ — accessed 2026-07-29 — **E3**
4. AWS Prescriptive Guidance — Architectural decision record process — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — accessed 2026-07-29 — **E1**
5. AWS Architecture Blog — Master architecture decision records (ADRs) — https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/ — accessed 2026-07-29 — **E2**
6. Michael Nygard — Documenting Architecture Decisions — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29 — **E1**
7. Google Cloud — Architecture decision records overview — https://docs.cloud.google.com/architecture/architecture-decision-records — accessed 2026-07-29 — **E1**
8. Cursor Docs — Plan Mode — https://cursor.com/docs/agent/plan-mode — accessed 2026-07-29 — **E1**
9. Cursor Help — Plan mode — https://cursor.com/help/ai-features/plan-mode — accessed 2026-07-29 — **E1**
10. Cursor Blog — Introducing Plan Mode — https://cursor.com/blog/plan-mode — accessed 2026-07-29 — **E1**
11. me2resh/agent-decision-record — https://github.com/me2resh/agent-decision-record — accessed 2026-07-29 — **E3** (lineage check only)
12. Me2resh blog — Agent Decision Records — https://me2resh.com/blog/agent-decision-records — accessed 2026-07-29 — **E3**
13. Homonym discovery: aiccountability-source/AgDR-FSv2.1 — https://github.com/aiccountability-source/AgDR-FSv2.1 — accessed 2026-07-29 — **E3** (not me2resh AgDR)
14. W1 alignment (local): `docs/research/notes/theme-5-design/t5a-w1-s2-agent-design-process.md`; `t5a-w1-s3-community-agent-workflows.md` — **E0** prior gatherer drafts

---

## Parent return summary

**Corroborations**

- Design-before-code / human gates: **strengthened** by Fowler Design-First (E1) and MIT CISR human accountability for strategic decisions (E1) — no longer Salesforce-only.
- Plan-then-build: Cursor **official** Plan Mode docs (E1) close W1 “no official docs” gap and support checkpoint pattern.
- ADR when-to-create: AWS PG + Nygard + Google Cloud (E1) give process triggers (significance / multi-option / undocumented).

**Conflicts / weakenings**

- Hetland (E3) still tensions with per-decision HITL — **OPEN**.
- me2resh AgDR: **not corroborated**; single lineage; **homonym** Atomic Genesis Decision Record must not be merged.
- AgDR create-when (broad, mid-session) vs AWS/Nygard significance bar — keep separate grades.

**Residual OPEN for W3**

- E0 Cursor Plan Mode UX / plan-path details; Plan Mode ≠ ADR options matrix.
- Design-time encoding vs per-decision gates acceptance.
- Alexandria surface (if scheduled); classical ATAM baseline still GAP.
