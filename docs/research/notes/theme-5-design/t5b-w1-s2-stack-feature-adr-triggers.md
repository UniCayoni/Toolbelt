---
title: "T5B W1 S2 — Stack/feature/service criteria + ADR triggers"
status: draft
theme: theme-5-design
track: T5B
slice: T5B-S2
wave: 1
created: 2026-07-29
updated: 2026-07-29
authors: [gatherer-t5b-s2-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/research/notes/theme-5-design/t5b-coordinator-pin.md
  - docs/research/notes/theme-5-design/t5a-track-synthesis.md
  - docs/PROTOCOL.md
---

# T5B W1 S2 — Stack/feature/service criteria + ADR triggers

**Using `research-protocol`**; depth: **deep**; wave: **1**; slice: **T5B-S2**.

**Status:** `draft`. Not Design SoT. Not permission to lock stacks, elevate Design skills, or re-litigate ADR/MADR templates (T5A / Theme 2).

## 1. Scope

- **Question / goal:** What criteria guide **stack / feature / service-boundary** design, and **when** should technical decisions become ADRs?
- **In scope:** Process triggers for writing ADRs on technical design choices (significance axes, multi-option / undocumented decisions); modular monolith vs microservices **as design criteria** (both sides); thin feature-design-before-implement criteria with E2 path to T5A spine; stack/library selection as criteria (not fad picks).
- **Out of scope:** Full ADR/MADR template re-litigation (T5A-S1 / Theme 2); Windows service/desktop deep dive (W3 if GAP); contested clean-code / standards debates (T5B-S3); Design skill elevation; grey-matter stack locks; Alexandria corroboration (W2).
- **Comprehension / research goal type:** other (technical design methodology research)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebSearch; WebFetch; local read of campaign brief, T5B pin, T5A track synthesis (spine path only) |
| Corpora / URLs searched | See §9 Source list |
| Queries (exact) | `AWS Prescriptive Guidance architectural decision records when to create ADR`; `modular monolith vs microservices design criteria Sam Newman Martin Fowler`; `site:martinfowler.com MonolithFirst OR modular monolith`; `technology stack selection criteria architecture decision frameworks libraries tools`; `ThoughtWorks Technology Radar adopt trial assess hold technology selection` |
| What was *not* searched | Alexandria `software_engineering` / books (W2); Windows service/desktop design; Clean Code / Framework Design Guidelines debates (S3); full *Building Microservices* / *Monolith to Microservices* book text; Richards & Ford *Fundamentals of Software Architecture* primary PDF (cited by AWS only); Architecture Patterns with Python; Architecture Metrics; high-signal ADR template repos beyond process triggers |
| Depth | deep |
| Waves / stop_reason | wave: **1** (primary / high-signal E1–E2). Stop for this slice: **wave1_primary_complete** — ADR trigger primaries + both-sides boundary criteria + stack-posture sources fetched; residual book-depth / Windows / Alexandria reserved for W2–W3 |
| Provenance (optional PROV) | Entity←AWS PG ADR, Nygard ADR, Fowler ADR/MonolithFirst/Premium/Trade-Offs, Google Cloud ADR, ThoughtWorks Radar FAQ, Newman/Fowler GOTO excerpt; Activity=T5B-S2 W1 gather; Agent=WebSearch/WebFetch + human campaign brief |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | External primary/secondary literature slice; no codebase recon required for W1 |
| Scope boundary | Named web primaries + local T5A spine path citation only |

## 4. Findings

### 4.1 When technical decisions become ADRs (process triggers)

Template shape / lifecycle owned by T5A + Theme 2 — **triggers only** here.

- `FACT` [E1] Nygard: keep records for **“architecturally significant”** decisions — those that affect **structure**, **non-functional characteristics**, **dependencies**, **interfaces**, or **construction techniques**. One ADR = one significant decision that affects how the rest of the project will run. [E1: Michael Nygard, “Documenting Architecture Decisions” — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29]
- `FACT` [E1] AWS Prescriptive Guidance: create an ADR for **every architecturally significant decision** affecting the project/product, including: **structure** (e.g. microservices patterns); **NFRs** (security, HA, fault tolerance); **dependencies** (coupling); **interfaces** (APIs / published contracts); **construction techniques** (libraries, frameworks, tools, processes). Cites Richards and Ford 2020. Functional and non-functional requirements are the most common inputs. [E1: AWS PG — ADR process — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — accessed 2026-07-29]
- `FACT` [E1] Fowler: an ADR captures and explains a **single decision** relevant to a product or ecosystem; writing clarifies thinking and surfaces disagreements; once accepted, do not reopen — **supersede**; record rationale/forces, serious alternatives + pros/cons, consequences; note context changes that should trigger **reevaluation**. [E1: Martin Fowler, “Architecture Decision Record” — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-07-29]
- `FACT` [E1] Google Cloud Architecture Center — prompts for when to create ADRs: (1) technical challenge with **no existing basis** for a decision (no recommended solution / SOP / blueprint / codebase precedent); (2) solution **not documented** accessibly to the team; (3) **two or more** engineering options and you want to document selection rationale. Examples include product choices (e.g. Pub/Sub vs Cloud Tasks) and HA/config choices. [E1: Google Cloud — Architecture decision records overview — https://docs.cloud.google.com/architecture/architecture-decision-records — last reviewed 2024-08-16 — accessed 2026-07-29]
- `INFERENCE` [E4] For T5B technical design, ADR triggers map cleanly onto stack/service choices: **structure** (deployable topology), **construction techniques** (languages/frameworks/libs), **interfaces/dependencies** (module/service contracts), and **NFRs** — plus Google’s multi-option / undocumented / no-prior-basis prompts. Premises: (1) Nygard E1 axes; (2) AWS E1 list; (3) Google E1 prompts; (4) Fowler E1 single-decision + alternatives.
- `INFERENCE` [E4] Not every implementation detail warrants an ADR — bar is **architectural significance** / multi-option rationale need, not every library bump. Premises: (1) Nygard “architecturally significant”; (2) AWS “every architecturally significant” (not every change); (3) Google multi-option / undocumented prompts.
- `GAP` No single shared quantitative checklist for “significant enough” across Nygard / AWS / Fowler / Google. Searched: those primaries. Result: definitional axes + prompts only. [also noted T5A-S1]

### 4.2 Stack / construction-technique selection criteria

- `FACT` [E1] AWS PG classifies **libraries, frameworks, tools, and processes** as ADR-worthy **construction techniques** when architecturally significant. [E1: AWS PG ADR process — same URL — accessed 2026-07-29]
- `FACT` [E1] ThoughtWorks Technology Radar FAQ: stack items are evaluated with adoption posture rings — **Adopt** (seriously consider; proven/mature in appropriate context — not “use everywhere”); **Trial** (ready but less proven; trial to decide toolkit fit; production experience required before Trial); **Assess** (watch closely; trial only if particularly good fit); **Caution** (warn of trouble / misuse / prefer alternatives). Quadrants include Techniques, Platforms, Tools, Languages and Frameworks. [E1: ThoughtWorks Technology Radar FAQ — https://www.thoughtworks.com/en-us/radar/faq — accessed 2026-07-29]
- `FACT` [E1] Radar FAQ: Adopt does **not** mean use for every project — “any tool should only be used in an appropriate context.” Radar is opinionated experience sample, not a comprehensive market survey or “approved tech list.” [E1: ThoughtWorks Radar FAQ — same URL — accessed 2026-07-29]
- `CLAIM` [E2] Practitioner stack frameworks commonly emphasize: constraints/NFRs first; team capability; TCO / operability; ecosystem maturity; **reversibility** (one-way vs two-way door); score candidates; spike hardest problem; document via ADR. [E2 discovery cluster — e.g. https://wolf-tech.io/blog/software-technology-stack-a-practical-selection-scorecard ; https://www.adriano-junior.com/technical-decision-framework — accessed 2026-07-29; **not** design locks alone]
- `INFERENCE` [E4] Stack criteria for Toolbelt Design methods should be **constraint- and context-driven** (fit, operability, team, reversibility, maturity posture), with ADR when the choice is significant / multi-option — not “hottest blip.” Premises: (1) AWS construction-technique ADR axis; (2) Radar context-appropriate Adopt; (3) Google product-choice ADR examples.

### 4.3 Service / deployable boundaries — modular monolith vs microservices (both sides)

Criteria for **whether** to split deployables — not a style catalog (S1 owns styles/modularity depth).

**Monolith-first / modular-within-monolith criteria (caution on early microservices)**

- `FACT` [E1] Fowler **Microservice Premium**: don’t consider microservices unless the system is **too complex to manage as a monolith**; majority of systems should be a **single monolithic application** with good modularity, not separated into services. Complexity drivers include large teams, multi-tenancy, independent evolution of business functions, scaling; biggest factor often **sheer size** (hard to modify/deploy). [E1: Martin Fowler, “Microservice Premium” — https://martinfowler.com/bliki/MicroservicePremium.html — accessed 2026-07-29]
- `FACT` [E1] Fowler **Monolith First**: successful microservice stories usually started as monoliths that grew too large; greenfield-from-scratch microservices often ended in serious trouble; premium slows teams when complexity doesn’t justify it; hard to get **stable Bounded Context** boundaries early — monolith helps discover boundaries; modular monolith path: attend to modularity at **API boundaries and data storage**. [E1: Martin Fowler, “Monolith First” — https://martinfowler.com/bliki/MonolithFirst.html — accessed 2026-07-29]
- `FACT` [E1] Fowler Monolith First also records the **counter-argument**: start with microservices to learn the rhythm, force small-team boundaries, scale development effort; especially viable for **system replacements** with stabler early boundaries; Fowler’s tentative stance: don’t start with microservices unless the team has **reasonable microservice experience**. [E1: Monolith First — same URL — accessed 2026-07-29]

**Microservices criteria / benefits (when the premium may pay)**

- `FACT` [E1] Fowler **Microservice Trade-Offs** — benefits: stronger module boundaries (esp. larger teams), **independent deployment**, technology diversity; costs: distribution (latency/failure), **eventual consistency**, operational complexity. Firm boundaries are possible in a monolith with discipline; microservices raise the probability of modularity but hurt if boundaries are wrong. Summary widely accepted: premium only worth it for more complex systems. [E1: Martin Fowler, “Microservice Trade-Offs” — https://martinfowler.com/articles/microservice-trade-offs.html — accessed 2026-07-29]
- `FACT` [E1] Sam Newman (GOTO Book Club excerpt with Fowler): use microservices when you have a **really good reason** — conscious choice for an **outcome**, not default activity; candidate outcomes include scale options, **independent deployability**, limiting blast radius / failure surface; cites James Lewis: microservices **buy you options** (options imply **cost**). [E1: “When to use microservices” — https://blog.gotocon.com/2020/07/22/when-to-use-microservices/ — accessed 2026-07-29]
- `INFERENCE` [E4] Design criteria for service boundaries (draft, not lock): prefer **modular single deployable** until complexity / team / independent-deploy / scale / failure-isolation outcomes justify the distribution premium; treat microservices as an **ADR-class structure decision** (AWS structure axis). Premises: (1) Premium + Monolith First E1; (2) Trade-Offs E1 pros/cons; (3) Newman outcome-first E1; (4) AWS structure ADR E1.
- `CLAIM` [E3] Secondary/community pieces often recommend modular monolith as sweet spot / “last resort” framing for microservices — useful discovery, need W2 book corroboration (Newman *Monolith to Microservices*, etc.) before locks. [E3: e.g. search-linked practitioner summaries — not promoted to design law]

### 4.4 Feature design before implement (thin — T5A spine)

- `FACT` [E2] T5A track synthesis (draft) merges a **design-before-implement loop**: frame problem/constraints → **criteria before solutions** → alternatives + tradeoffs → critique → **human decides** → record (ADR/MADR) → HITL gate before implementation; anti-pattern vibes-only. Lanes A/B/C kept separate. [E2 path: `docs/research/notes/theme-5-design/t5a-track-synthesis.md` §3 Spine — accessed 2026-07-29]
- `INFERENCE` [E4] For T5B feature design: apply the T5A loop **before** coding a feature that crosses stack/boundary/NFR significance; escalate to ADR when §4.1 triggers fire (structure, NFR, dependency, interface, construction technique, multi-option). Premises: (1) T5A spine E2 path; (2) §4.1 ADR trigger FACTS.
- `OPEN` Domain-specific feature decomposition heuristics (e.g. vertical slice sizing, story splitting catalogs) not gathered this slice — W2 residual only if P0 GAP remains after S1 modularity findings.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | ADR create-when for technical design is the Nygard/AWS significance axes + Google multi-option/undocumented prompts | confirmed (for this slice’s sources) | §4.1 E1 FACTS |
| H2 | Default deployable posture is modular monolith until outcome-justified premium | open (strong E1 lean; counter-arg recorded) | §4.3; W2 books may refine |
| H3 | Stack picks should use context/maturity/reversibility criteria + ADR when significant | open | Radar E1 + practitioner E2 cluster |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Monolith-first vs microservices-first | Fowler Monolith First / Premium (default monolith + modularity) [E1] | Counter-arg in same Fowler article: microservices-first for rhythm / team scaling / replacements [E1]; Trade-Offs lists microservice benefits [E1] | Cite both; choice is context/outcome + complexity vs premium — leave OPEN for project-specific ADR |
| How broad is “create ADR”? | AWS/Nygard: architecturally significant axes [E1] | Google: also “product choices” / multi-option prompts (can feel broader) [E1]; AgDR mid-session inventoriess are E3 (T5A) | Prefer significance bar for Toolbelt ADR law; Google prompts as practical create-when aids; do not import AgDR breadth |

## 7. Gaps & OPEN

- `GAP` Windows service / desktop **as design concerns** — not searched this slice; campaign brief → **W3 if named P0 GAP**.
- `GAP` Primary book depth: Newman *Building Microservices* / *Monolith to Microservices*; Richards & Ford (AWS citation); modular-monolith case studies with E0/E1 — deferred **W2**.
- `GAP` Quantitative “architecturally significant” checklist — none found across primaries.
- `OPEN` Feature-sizing heuristics beyond T5A spine — only if still P0 after S1.
- `OPEN` Alexandria corroboration of stack/boundary criteria — W2.

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T5B Design methods (later) should teach **criteria → options → decide → ADR-if-triggered**, reusing T5A spine, with service topology and stack picks as first-class ADR candidates under AWS/Nygard axes — **not** a mega-skill that picks stacks. Premises: §4.1–4.4.
- `INFERENCE` [E4] Do not lock Toolbelt/grey-matter deployable style or libraries from this draft note. Premises: `draft-is-not-sot`; remaining GAPs.

## 9. Source list (deduped)

1. Michael Nygard — Documenting Architecture Decisions — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29
2. AWS Prescriptive Guidance — Architectural decision record process — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — accessed 2026-07-29
3. Martin Fowler — Architecture Decision Record — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-07-29
4. Google Cloud Architecture Center — Architecture decision records overview — https://docs.cloud.google.com/architecture/architecture-decision-records — accessed 2026-07-29
5. Martin Fowler — Microservice Premium — https://martinfowler.com/bliki/MicroservicePremium.html — accessed 2026-07-29
6. Martin Fowler — Monolith First — https://martinfowler.com/bliki/MonolithFirst.html — accessed 2026-07-29
7. Martin Fowler — Microservice Trade-Offs — https://martinfowler.com/articles/microservice-trade-offs.html — accessed 2026-07-29
8. GOTO Blog — When to use microservices (Newman/Fowler excerpt) — https://blog.gotocon.com/2020/07/22/when-to-use-microservices/ — accessed 2026-07-29
9. ThoughtWorks Technology Radar FAQ — https://www.thoughtworks.com/en-us/radar/faq — accessed 2026-07-29
10. T5A track synthesis (spine path) — `docs/research/notes/theme-5-design/t5a-track-synthesis.md` — accessed 2026-07-29
11. Practitioner stack scorecard (E2 discovery) — https://wolf-tech.io/blog/software-technology-stack-a-practical-selection-scorecard — accessed 2026-07-29
12. Practitioner technical decision framework (E2 discovery) — https://www.adriano-junior.com/technical-decision-framework — accessed 2026-07-29
