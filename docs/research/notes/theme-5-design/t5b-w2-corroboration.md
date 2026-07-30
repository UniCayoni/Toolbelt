---
title: "T5B Wave 2 — Alexandria + web corroboration (patterns, scale, metrics, deployable boundaries)"
status: draft
theme: theme-5-design
track: T5B
wave: 2
slice: T5B-W2
created: 2026-07-29
updated: 2026-07-29
authors: [t5b-w2-gatherer-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/t5b-w1-s1-architecture-modularity.md
  - docs/research/notes/theme-5-design/t5b-w1-s2-stack-feature-adr-triggers.md
  - docs/research/notes/theme-5-design/t5b-w1-s3-clean-standards-agents.md
  - docs/research/notes/theme-5-design/t5b-coordinator-pin.md
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
---

# T5B-W2 — Corroboration (Architecture Patterns with Python; Foundations of Scalable Systems; Software Architecture Metrics; modular monolith; ADR template repos)

**Using `research-protocol`; depth: deep; wave: 2; slice: T5B-W2.**

**Status:** `draft`. Not Design SoT. Does **not** restate W1 E1 FACTS as new primary FACTS — only corroborates, softens, extends, or marks GAP. Does **not** elevate Design skills or lock grey-matter stacks.

## 1. Scope

- Question / goal: Corroborate T5B Wave-1 findings with Alexandria `software_engineering` (named books) + web; close or refine W1 GAPs on modular monolith vs microservices (both sides), component cohesion (REP/CCP/CRP), and architecture metrics / MMI; inventory high-signal ADR template repos as **E3 discovery only**.
- In scope: *Architecture Patterns with Python* (Percival/Gregory); *Foundations of Scalable Systems* (Gorton); *Software Architecture Metrics* (Ciceri et al.); modular monolith vs microservices both sides; false-friend hygiene; ADR template GitHub inventory (E3).
- Out of scope: Re-fetching Martin 2012 Clean Architecture blog / Fowler Monolith First primaries as if new; lint catalogs; grey-matter locks; T5C/T5D; Design skill drafting; Windows service/desktop deep dive (W3 only if still P0); Hexagonal Cockburn / Onion Palermo primary essays (still GAP unless closed incidentally).
- Comprehension / research goal type: other (secondary-corpus + web corroboration)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (W1 S1/S2/S3, coordinator pin, campaign brief, research-note template); research-protocol skill; Alexandria MCP `user-alexandria-rag` (`list_documents`, `rag_probe`, `rag_query`); WebSearch; WebFetch (`https://adr.github.io/adr-templates/`) |
| Corpora / URLs searched | Alexandria `software_engineering`; Fowler Monolith First / Microservice Trade-Offs (already W1; web re-hit); `https://adr.github.io/adr-templates/`; GitHub discovery for `adr/madr`, `joelparkerhenderson/architecture-decision-record`, `npryce/adr-tools` |
| Queries (exact) | Probes: (1) `Architecture Patterns with Python hexagonal ports adapters service layer unit of work modular boundaries`; (2) `Foundations of Scalable Systems architecture modularity services distributed systems tradeoffs`; (3) `Software Architecture Metrics modularity maintainability architecture decision records quality metrics`; (4) `modular monolith versus microservices when to use service boundaries independent deployability`. Path-scoped queries: APP DIP/layering/ports; APP Distributed Ball of Mud; Gorton monolith/microservices; Architecture Metrics MMI/coupling/ADR; Martin Clean Architecture `Reuse/Release Equivalence Principle Common Closure Principle Common Reuse Principle`. Untargeted: modular monolith vs microservices. Web: `modular monolith vs microservices design criteria both sides Sam Newman Martin Fowler`; `github ADR architecture decision records template repository nygard madr`; `joelparkerhenderson architecture-decision-record github npryce adr-tools` |
| What was *not* searched | Newman *Building Microservices* / *Monolith to Microservices* full book ingest (absent from catalog under title filters); Richards & Ford *Fundamentals of Software Architecture* primary PDF; Cockburn Hexagonal / Palermo Onion primary essays; Windows service/desktop design literature; `programming_algorithms_systems` corpus; full lint / SonarQube rule catalogs |
| Depth | deep |
| Waves / stop_reason | wave: **2** (slice T5B-W2). stop_reason: **w2_named_books_and_boundary_criteria_corroborated** — three campaign books present and path-scoped; REP/CCP/CRP body closed; modular-monolith both sides corroborated (Gorton + Esposito secondary + W1 Fowler E1); ADR template repos inventoried as E3; further keyword chase hits false friends / index pages |
| Provenance (optional PROV) | Entity←W1 notes + Alexandria chunks + adr.github.io + GitHub discovery; Activity=T5B-W2 corroboration; Agent=Grok gatherer + Alexandria RAG + WebSearch/WebFetch |

### 2.1 Catalog presence (target books)

- `FACT` [E0] `list_documents` `name_substring=Architecture Patterns` → *Architecture Patterns with Python* (Bob Gregory, Harry Percival), `source_id=ccc326d5d96d3dba`, 247 chunks. [E0: Alexandria list_documents — 2026-07-29]
- `FACT` [E0] `list_documents` `name_substring=Scalable` → *Foundations of Scalable Systems Designing Distributed Architectures* (Ian Gorton), `source_id=f5df94835151f90e`, 399 chunks. [E0: same]
- `FACT` [E0] `list_documents` `name_substring=Architecture Metrics` → *Software Architecture Metrics…* (Ciceri, Farley, Ford, et al.), `source_id=825b8b768e6a3ed3`, 267 chunks. [E0: same]
- `FACT` [E0] `list_documents` filters `Microservices` / `Monolith` / `Newman` / `Building Micro` returned **0** documents — Newman book texts **not** ingested under those titles. [E0: same]

### 2.2 Probe coverage

| Topic | coverage_verdict | Notes |
|-------|------------------|-------|
| Architecture Patterns with Python (untargeted) | partial | Top hits skewed to *Clean Architecture with .NET*, Khorikov, Percival TDD book — **false friends**; path_prefix required |
| Foundations of Scalable Systems | partial | Strong Gorton hits |
| Software Architecture Metrics | partial | Strong Metrics book hits |
| Modular monolith vs microservices (untargeted) | partial | Dominated by Esposito *Clean Architecture with .NET* — useful secondary on modular monolith, **false friend** for Martin CA |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Corroboration against fixed W1 notes + campaign W2 book list; not workspace recon |
| Scope boundary | `software_engineering` + named web/GitHub; cite only retrieved chunk_ids / fetched URLs |

## 4. Findings

### 4.1 False friends (discovery hygiene)

- `FACT` [E2] Untargeted “Architecture Patterns / hexagonal / ports” probes surface *Clean Architecture with .NET* (Esposito), *Clean Code Principles… Python Edition*, Unit Testing (Khorikov), Percival *TDD with Python* — not interchangeable with Percival/Gregory *Architecture Patterns with Python*. Prefer path_prefix=`Architecture Patterns with Python`. [E2: probe top_sources session 2026-07-29]
- `FACT` [E2] Untargeted modular-monolith queries rank Esposito heavily; treat as **secondary modular-monolith** evidence, not Martin CA Dependency Rule corroboration. [E2: e.g. chunk_id=`ab54c1fced4744a73f5111d7` source=`Clean Architecture with .NET…`]
- `GAP` Newman *Building Microservices* / *Monolith to Microservices* not in Alexandria catalog (title filters). W1 Fowler E1 + Gorton E2 + Esposito E2 used for both-sides boundary criteria; Newman remains web/E1 excerpt only (W1 GOTO) unless ingested later.

### 4.2 Architecture Patterns with Python — corroborates S1 modularity / DIP / ports family

**Targets W1 S1:** Dependency Rule family, DIP-at-boundary, ports/adapters vocabulary, GoF-style trade-off tables (not whole-app law).

- `CLAIM` [E2] Layered architectures divide code into roles with rules about which categories can call each other; three-layer UI / business logic / database is common; the book systematically “turns this model inside out” via DIP. [E2: Alexandria corpus=`software_engineering` source=`Architecture Patterns with Python…` chunk_id=`e40ca95ba90247f81250fb0f` query=`Dependency Inversion Principle layering…`]
- `CLAIM` [E2] DIP formal statement restated: high-level modules must not depend on low-level modules — both depend on abstractions; abstractions must not depend on details. High-level ≈ organization-caring domain concepts; low-level ≈ infrastructure the org “doesn’t care about.” [E2: same chunk_id=`e40ca95ba90247f81250fb0f`]
- `CLAIM` [E2] Repository pattern applies DIP to data access: abstract repository as port; FakeRepository / real ORM adapters; invert so ORM depends on model rather than model on ORM. [E2: chunk_id=`4d88f0137ff5eb8f6a7879bc` + chunk_id=`91473d026e2835514ad95e93`]
- `CLAIM` [E2] Folder layout: domain model; service layer (use cases); adapters = secondary/driven; entrypoints = primary/driving adapters; ports = abstract interfaces adapters implement. [E2: chunk_id=`0be3c4746bdbc7e895e1aeda`]
- `CLAIM` [E2] Service-layer trade-offs table: pros include single place for use cases, refactor-behind-API, HTTP separated from domain; cons include extra abstraction, risk of anemic domain if overused — introduce after orchestration creeps into controllers; “fat models, thin controllers” can suffice without the layer. [E2: chunk_id=`91473d026e2835514ad95e93`]
- `CLAIM` [E2] Event-based microservice integration trade-offs: avoids distributed big ball of mud / decouples services vs harder-to-see overall flows, eventual consistency, message reliability choices. [E2: chunk_id=`9037f27b5b05d168bb7d1677`]
- `CLAIM` [E2] Anti-pattern: naïve noun-based microservice split (“Batches”, orders, products…) → Distributed Ball of Mud; prefer event-driven temporal decoupling over sync noun APIs. [E2: chunk_id=`483596e765f389112afbde2b` + index chunk_id=`62731486727bd9cd1db29b31`]
- `INFERENCE` [E4] APP **corroborates** W1 S1 Dependency Rule / DIP-at-boundary / ports-adapters family as **implementable design criteria** (Python case study + explicit trade-off tables), without crowning Clean Architecture four circles as law. Premises: (1) DIP + ports CLAIMs; (2) W1 Martin Dependency Rule E1; (3) service-layer cons against over-architecture.
- `GAP` Cockburn Hexagonal / Palermo Onion **primary** essays still not fetched; APP uses ports-and-adapters terminology as practice, not primary essay corroboration.

### 4.3 Foundations of Scalable Systems — both sides of monolith vs microservices

**Targets W1 S2:** Microservice Premium / Monolith First / Trade-Offs; need book-depth both sides.

**Monolith advantages / when OK**

- `CLAIM` [E2] Monolith = logical modules built/deployed as one application sharing business logic and typically one DB; well-understood, strong framework automation, straightforward testing/deployment/monitoring on one server; scale-up simplest; scale-out via replicas + load balancer (session affinity if stateful). [E2: corpus=`software_engineering` source=`Foundations of Scalable Systems…` chunk_id=`f80c91c960bb66bc256efaba` query=`monolith advantages…`]

**Monolith pain → microservices motivations**

- `CLAIM` [E2] Monoliths become problematic via (1) **code base complexity** (team/app growth → harder features/tests/refactors, technical debt) and (2) **scale-out** that replicates the *entire* app — cannot independently scale a hot module (AdvisorChat example). [E2: chunk_id=`5fe2ac1a6380968741027bf2`]
- `CLAIM` [E2] Microservice advantages: two-pizza team scope, stack autonomy (with standardization trade-off), independent deploy if API stable, independent scale-out per service. Decomposition via DDD bounded contexts noted as essential but “beyond the scope of this chapter.” [E2: chunk_id=`5fe2ac1a6380968741027bf2` + chunk_id=`9d845f3bc2849785fc779cf6`]

**Microservices costs / balancing act (other side)**

- `CLAIM` [E2] “There is always a balancing act”: microservices are distributed; domain purity must be adjusted for distributed-communication costs and ops/monitoring complexity; merge services or duplicate data when chatty requests hurt latency/reliability. [E2: chunk_id=`9d845f3bc2849785fc779cf6`]
- `CLAIM` [E2] Cascading failures: slow downstream responses (not hard fail) create back pressure and thread exhaustion up the call chain; retries can worsen overload; resilience patterns include fail-fast/timeouts, circuit breakers, bulkheads. [E2: chunk_id=`3f92a553fe4d9248b924d082` + chunk_id=`2e6d096fc7bf1e07cf7395e3`]
- `CLAIM` [E2] Gorton: “sometimes microservices are not always the right approach” — points to Istio case study of unnecessary complexity; recommends Newman *Building Microservices* 2e for depth (book not in this corpus). [E2: chunk_id=`2e6d096fc7bf1e07cf7395e3`]

**Secondary modular-monolith lean (false-friend source, graded carefully)**

- `CLAIM` [E2] Esposito: modularity is necessary; microservices make modularity “nearly free,” but disciplined monoliths can deliver nearly the same benefits; do **not** start new projects with microservices — prefer modular monolith (well-designed monolith extractable later); reasons: operational complexity + unclear early boundaries. [E2: corpus=`software_engineering` source=`Clean Architecture with .NET…` chunk_id=`ab54c1fced4744a73f5111d7` + chunk_id=`5790e5f48cf50264e55184d8` — **secondary; not Martin CA**]
- `CLAIM` [E2] Esposito modular-monolith upsides: simpler deploy/trace/log; in-process performance; strong consistency by default; faster velocity for smaller teams; downside: cannot selectively scale modules — scale whole app / DB. [E2: chunk_id=`ce357c098f7235c4be7b55e4`]

**Web reaffirmation (no new primary beyond W1)**

- `FACT` [E1] Fowler Monolith First / Microservice Trade-Offs remain authoritative for W1 S2 lean (already cited W1); W2 web search re-surfaced same URLs — no contradiction found. [E1: https://martinfowler.com/bliki/MonolithFirst.html ; https://martinfowler.com/articles/microservice-trade-offs.html — accessed 2026-07-29]
- `CLAIM` [E3] Practitioner secondary (e.g. wojciechowski.app summarizing Newman “last resort” / modular monolith sweet spot) — discovery only; do not lock. [E3: WebSearch 2026-07-29]
- `INFERENCE` [E4] W1 S2 H2 (default modular single-deployable until outcome-justified premium) is **strengthened** by Gorton both-sides + Esposito modular-monolith caution + W1 Fowler E1; still **OPEN** for project-specific ADR, not house stack law. Premises: §4.3 CLAIMs; W1 S2 §4.3.
- `GAP` Newman book body still absent from Alexandria; Strangler / migration playbooks thin in this pass (APP index mentions Strangler; not deep-quoted).

### 4.4 Software Architecture Metrics — modularity measurement + light ADR mention

**Targets W1 S1 GAP:** Architecture Metrics / MMI deferred.

- `CLAIM` [E2] Book frame: architecture metrics keep projects maintainable, warn of architectural/technical debt; case studies from practicing architects (not pure theory). [E2: corpus=`software_engineering` source=`Software Architecture Metrics…` chunk_id=`f80c274741ad8559c3e5a63c`]
- `CLAIM` [E2] **Modularity Maturity Index (MMI)** assesses technical debt for refactor-vs-replace guidance; principles weighted: modularity 45%, hierarchy 30%, pattern consistency 25%. Criteria mix metrics tools, architecture analysis tools, and reviewer judgment. [E2: chunk_id=`2d7d97556ed5a0db85b68a01` + chunk_id=`cdda72d6332f24d393e2dce3` + chunk_id=`03a8c2f73821c262391c5250`]
- `CLAIM` [E2] MMI hierarchy criteria include class/package **cycle** percentages/sizes; pattern consistency includes separation of domain vs technical code (DDD, Quasar, Hexagonal) as reviewer judgment. [E2: chunk_id=`cdda72d6332f24d393e2dce3`]
- `CLAIM` [E2] Large cycles illustrated as maintainability disasters (e.g. 242-class cycle); prefer preventing cycles early (aligns with Martin ADP directionally). [E2: chunk_id=`8ac3fa3e146dd4e99af98c43`]
- `CLAIM` [E2] Governance metrics chapter: coupling/structural erosion, cycle groups, toxicity of cyclic dependencies, DIP named in “code cancer” discussion; useful metrics include ACD, Maintainability Level, LCOM4, size/complexity. [E2: index/body via chunk_id=`733f342e8865510b8c0c6220` + chunk_id=`c2d88c8057e1cd641042324b`]
- `CLAIM` [E2] ADRs attributed to Nygard; weekly discussion of spikes/ADRs alongside delivery metrics; case of capturing an ADR then verifying behavior “as described in the ADR.” [E2: chunk_id=`ad666e87782b1b97014d779c` + prior T5A-W2 chunks `a1b4ee7541275ccbc6a60390`, `403e33e231c9d33f127e1939` — presence/use, **not** template law]
- `INFERENCE` [E4] Metrics/MMI supply **optional measurement criteria** for modularity health (cycles, layering violations, pattern consistency) that can feed design reviews / fitness functions — complementary to W1 qualitative Dependency Rule / ADP/SDP/SAP, not a replacement ADR process. Premises: MMI CLAIMs; W1 S1 coupling FACTS; T5A owns ADR templates.
- `GAP` No quantitative “architecturally significant enough for ADR” checklist in Metrics book either (W1 S2 GAP stands).

### 4.5 REP / CCP / CRP — closes W1 S1 cohesion GAP

- `FACT` [E2] Martin component cohesion principles: **REP** — “The granule of reuse is the granule of release”; classes in a component share cohesive purpose and release tracking. **CCP** — gather classes closed to the same kinds of changes (component form of SRP / strategic OCP). **CRP** — “Don’t force users of a component to depend on things they don’t need”; classes reused together belong together; also tells what *not* to co-locate. [E2: corpus=`software_engineering` source=`Martin…Clean Architecture…2017` chunk_id=`4a0ba0a4aff55ff37d836055` + chunk_id=`d5bb9203c92af667ff7ce756` query=`Reuse/Release Equivalence Principle…`]
- `FACT` [E2] Tension diagram: over-focus REP+CRP → too many components hit by simple changes; over-focus CCP+REP → too many unneeded releases; early projects often sacrifice reuse for develop-ability (CCP-weighted), then slide toward reuse as maturity grows — component structure evolves. [E2: chunk_id=`001f5804673abc4b47f1fc25`]
- `INFERENCE` [E4] Completes W1 S1 modularity checklist with cohesion side: ADP/SDP/SAP (coupling) + REP/CCP/CRP (cohesion), with explicit tension — do not maximize all six simultaneously. Premises: these FACTS; W1 S1 §4.3.

### 4.6 Contested clean / agents (S3) — light W2 touch only

- `INFERENCE` [E4] No Alexandria contradiction found this wave that would overturn S3 “standards as constraints, not architecture SoT” or Osmani/Taulli plan-first CLAIMs; APP trade-off tables and Metrics fitness-function framing reinforce **criteria/measurement over dogma**. Premises: S3 CLAIMs (not re-fetched); §4.2–4.4.
- `GAP` Ousterhout *A Philosophy of Software Design* book still not confirmed in Alexandria (S3 GAP stands).

### 4.7 High-signal ADR template repos — E3 discovery only

**Do not re-litigate T5A template law.** Inventory for Toolbelt pointer hygiene.

- `FACT` [E1] adr.github.io ADR Templates hub documents family: **MADR**, **Nygard ADR** (title/status/context/decision/consequences), **Y-Statement**, plus pointer to joelparkerhenderson catalog; MADR stresses considered options + pros/cons. [E1: https://adr.github.io/adr-templates/ — accessed 2026-07-29]
- `FACT` [E3] High-signal GitHub inventory (discovery; stars as popularity signal only): `adr/madr` (MADR templates full/minimal/bare); `joelparkerhenderson/architecture-decision-record` (template catalog including Nygard Markdown rendering); `npryce/adr-tools` (CLI for Markdown ADR logs; fork `adr/adr-tools` adds MADR support notes). [E3: GitHub search/WebSearch 2026-07-29 — https://github.com/adr/madr ; https://github.com/joelparkerhenderson/architecture-decision-record ; https://github.com/npryce/adr-tools]
- `INFERENCE` [E4] Template **existence** and community tooling are corroborated; **when to create** remains W1 S2 Nygard/AWS/Google E1; section atoms remain T5A. Premises: this §; W1 S2; T5A notes.
- `GAP` No W2 evidence that Toolbelt must pin one template repo over another — OPEN for human accept / T5A reuse.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | W1 Dependency Rule / DIP checklist is practice-corroborated by APP ports/adapters case study | confirmed (directional) | §4.2 |
| H2 | Default modular single-deployable until justified premium survives book corroboration | confirmed (directional; still ADR-local) | §4.3; W1 S2 H2 |
| H3 | MMI/cycle metrics can operationalize ADP-style modularity health without becoming ADR law | open | §4.4 |
| H4 | REP/CCP/CRP close S1 cohesion GAP sufficiently for design checklists | confirmed for W2 | §4.5 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| When microservices pay | Fowler Premium / Monolith First: most systems should stay modular monolith [E1 W1] | Gorton: monoliths “almost inevitably” face scale/engineering pain as load grows; microservices solve independent scale [E2] | Cite both — **threshold is outcome/complexity**, not inevitability; ADR under structure axis |
| Start microservices greenfield? | Fowler counter-arg + experienced teams [E1 W1]; Esposito strong “don’t start with microservices” [E2] | Gorton focuses on growth path from monolith pain | Prefer caution for greenfield unless experience + clear outcomes; leave OPEN per project |
| “Clean Architecture” naming | Martin Dependency Rule [E1 W1] | Esposito *Clean Architecture with .NET* modular-monolith chapters [E2] | False-friend hygiene — use Esposito only for deployable-boundary claims |

## 7. Gaps & OPEN

- `GAP` Newman *Building Microservices* / *Monolith to Microservices* not in Alexandria; migration patterns (Strangler) only index-thin in APP.
- `GAP` Hexagonal/Onion **primary** essays still unfetched.
- `GAP` Quantitative ADR-significance checklist still absent across W1+W2 sources.
- `GAP` Windows service / desktop as design concerns — **not searched** W1 or W2 (see Coordinator signal).
- `GAP` APOSD book ingest still unconfirmed.
- `OPEN` House adoption of MMI / cycle gates vs qualitative checklists only.
- `OPEN` Whether Toolbelt pins `adr/madr` vs Nygard-minimal (T5A ownership).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] Design-time technical checklist can now include: Dependency Rule / DIP + ports vocabulary (S1 + APP); component coupling ADP/SDP/SAP + cohesion REP/CCP/CRP with tension; deployable posture modular-monolith-default with Gorton/Fowler costed upsides for split; optional MMI/cycle metrics as health signals; ADR when Nygard/AWS axes fire — templates from T5A/E3 inventory. Premises: §§4.2–4.7; W1 notes.
- `INFERENCE` [E4] Do **not** lock Toolbelt or grey-matter to microservices, Clean Architecture circles, or a metrics tooling vendor from this draft. Premises: `draft-is-not-sot`; conflicts §6.

## 9. Source list (deduped)

1. Alexandria `software_engineering` — Percival & Gregory, *Architecture Patterns with Python* — chunks `e40ca95ba90247f81250fb0f`, `4d88f0137ff5eb8f6a7879bc`, `91473d026e2835514ad95e93`, `0be3c4746bdbc7e895e1aeda`, `9037f27b5b05d168bb7d1677`, `483596e765f389112afbde2b`, `62731486727bd9cd1db29b31` (`source_id=ccc326d5d96d3dba`)
2. Alexandria `software_engineering` — Gorton, *Foundations of Scalable Systems* — chunks `f80c91c960bb66bc256efaba`, `5fe2ac1a6380968741027bf2`, `9d845f3bc2849785fc779cf6`, `3f92a553fe4d9248b924d082`, `2e6d096fc7bf1e07cf7395e3` (`source_id=f5df94835151f90e`)
3. Alexandria `software_engineering` — Ciceri et al., *Software Architecture Metrics* — chunks `f80c274741ad8559c3e5a63c`, `2d7d97556ed5a0db85b68a01`, `cdda72d6332f24d393e2dce3`, `03a8c2f73821c262391c5250`, `8ac3fa3e146dd4e99af98c43`, `733f342e8865510b8c0c6220`, `ad666e87782b1b97014d779c` (`source_id=825b8b768e6a3ed3`)
4. Alexandria `software_engineering` — Martin, *Clean Architecture* (2017) — REP/CCP/CRP chunks `4a0ba0a4aff55ff37d836055`, `d5bb9203c92af667ff7ce756`, `001f5804673abc4b47f1fc25`
5. Alexandria `software_engineering` — Esposito, *Clean Architecture with .NET* — modular monolith chunks `ab54c1fced4744a73f5111d7`, `5790e5f48cf50264e55184d8`, `ce357c098f7235c4be7b55e4` (**false-friend for Martin CA**; secondary for deployables)
6. Fowler — Monolith First / Microservice Trade-Offs — https://martinfowler.com/bliki/MonolithFirst.html ; https://martinfowler.com/articles/microservice-trade-offs.html — accessed 2026-07-29
7. ADR Templates hub — https://adr.github.io/adr-templates/ — accessed 2026-07-29
8. E3 GitHub discovery — https://github.com/adr/madr ; https://github.com/joelparkerhenderson/architecture-decision-record ; https://github.com/npryce/adr-tools — accessed 2026-07-29
9. W1 notes (alignment, not new SoT) — `t5b-w1-s1-architecture-modularity.md`, `t5b-w1-s2-stack-feature-adr-triggers.md`, `t5b-w1-s3-clean-standards-agents.md`

## 10. Parent return — Coordinator signal

### Corroboration summary

| W1 area | W2 result |
|---------|-----------|
| S1 Dependency Rule / DIP / ports family | **Corroborated** via APP (E2) |
| S1 REP/CCP/CRP body GAP | **Closed** (Martin E2 body + tension diagram) |
| S1 MMI / Architecture Metrics GAP | **Closed enough** for criteria (MMI + cycles); not ADR template law |
| S2 modular monolith vs microservices | **Both sides corroborated** (Gorton E2 + Esposito E2 + W1 Fowler E1); Newman book still GAP in corpus |
| S2 ADR triggers | Unchanged (W1 E1); Metrics only mentions ADR use |
| S3 clean/agents | No overturn; light reinforce via trade-off framing |
| ADR template repos | **E3 inventory** only (`adr/madr`, joelparkerhenderson, npryce/adr-tools) |

### Coordinator signal

| Field | Value |
|-------|-------|
| `low_return_detected` | **yes** |
| Rationale | Named W2 books retrieved and path-scoped; cohesion GAP closed; deployable-boundary both sides corroborated; further untargeted RAG is false-friend dominated; Newman ingest and Hexagonal primaries would be new sources, not diminishing re-queries of the same three books |
| Residual **P0** for W3 | **None required for Windows** — Windows service/desktop remains an **OPEN/non-P0 GAP** (campaign “W3 if GAP,” but nothing in T5B W1–W2 elevates it to P0 for Toolbelt Design methods). Optional W3 only if coordinator later marks Windows P0 for a product surface. |
| Suggested W3 (non-P0 / skip-ok) | Newman book if ingested; Cockburn/Palermo primaries only if integrator still needs family-primary cites; else proceed to track synthesis |

**stop_reason (gatherer):** `w2_named_books_and_boundary_criteria_corroborated` — hand off to coordinator for `low_return_plus_one` / synthesis.
