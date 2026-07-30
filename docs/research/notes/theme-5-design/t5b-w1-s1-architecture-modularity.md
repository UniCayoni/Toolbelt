---
title: "T5B Wave 1 Slice S1 — Architecture style, modularity, dependency criteria"
status: draft
theme: theme-5-design
track: T5B
wave: 1
slice: T5B-S1
created: 2026-07-29
updated: 2026-07-29
authors: [t5b-w1-s1-gatherer-grok]
supersedes: null
---

# T5B-W1-S1 — Architecture style / modularity / dependency criteria (design-time)

**Using `research-protocol`; depth: deep; wave: 1; slice: T5B-S1.**

## 1. Scope

- Question / goal: What architecture style, modularity, and dependency criteria should guide technical design at **design-time** (before / while shaping structure — not lint catalogs or stack locks)?
- In scope: Clean Architecture Dependency Rule and layer intents; family resemblance to Hexagonal/Onion/etc.; GoF pattern role (vocabulary, problem/solution/consequences — not whole-app architecture); Framework Design Guidelines concepts for **reusable library** boundaries when present in corpus; Martin component-coupling principles (ADP, SDP, SAP) as modularity criteria; process vocabulary handoff to T5A spine (**options → decide → ADR**) without re-researching ADR templates.
- Out of scope: Full lint catalogs; grey-matter / Brain stack locks; T5C (UX/UI); T5D (worldbuilding/game systems); writing Design skills; modular monolith vs microservices debate (Wave 2); contested Clean Code style wars (other T5B slice); Windows service/desktop specifics (Wave 3 if still GAP).
- Comprehension / research goal type (if code): other (architecture literature / design-time criteria)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch (Martin Clean Architecture blog); Alexandria MCP `user-alexandria-rag` (`rag_probe`, `rag_query`); Read (research-note template, T5A gatherer shape, campaign brief T5B section); research-protocol skill |
| Corpora / URLs searched | https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html ; Alexandria corpus=`software_engineering` (Martin *Clean Architecture* 2017; GoF *Design Patterns* 1994; Cwalina/Barton/Abrams *Framework Design Guidelines*; secondary hits noted as false friends) |
| Queries (exact) | WebFetch URL above. Probes: (1) `Clean Architecture Dependency Rule source code dependencies point inward`; (2) `Gang of Four Design Patterns Elements of Reusable Object-Oriented Software modular boundaries`; (3) `Framework Design Guidelines layered architecture reusable library boundaries`. Queries: (A) Clean Architecture dependency rule / layers / DIP crossing; (B) GoF purpose / modular boundaries / coupling; (C) Framework Design Guidelines reusable library boundaries / layered architecture; (D) ADP / SDP / SAP component coupling; (E) GoF path_prefix=`Erich Gamma` pattern name/problem/solution/consequences |
| What was *not* searched | Web search beyond named URL; AWS Prescriptive Guidance; Fowler ADR pages (T5A); Architecture Patterns with Python full W2 pass; Architecture Metrics / MMI deep pass; Hexagonal primary Cockburn essay; Onion primary Palermo essay; DCI / BCE primaries; stack-selection criteria (T5B-S2); agent-assisted technical design (T5B-S3); `programming_algorithms_systems` corpus |
| Depth | deep |
| Waves / stop_reason | wave: 1 (slice T5B-S1). stop_reason: N/A for gatherer slice — Wave 1 primary fetch + corpus corroboration complete for assigned targets; diminishing-returns / track stop owned by coordinator/integrator |
| Provenance (optional PROV) | Entity←Martin 2012 blog + Martin 2017 book chunks + GoF 1994 chunks + FDG 2020 chunks; Activity=T5B-W1-S1 gather; Agent=Grok gatherer + WebFetch + Alexandria RAG |

### 2.1 Probe coverage (session)

| Topic | Probe verdict | Notes |
|-------|---------------|-------|
| Clean Architecture Dependency Rule | `partial` | Strong Martin book hits; secondary “clean” titles also surface |
| GoF modular boundaries | `partial` | Primary GoF PDF present; secondary .NET/Dooley paraphrases compete |
| Framework Design Guidelines | `partial` | FDG epub present; layered-architecture principle retrievable |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Slice is primary + corpus literature gather, not workspace recon |
| Scope boundary | Named Clean Architecture URL + `software_engineering` RAG only; T5A spine as vocabulary pointer only |

## 4. Findings

### 4.1 False friends (discovery hygiene)

- `FACT` [E2] Queries for “Clean Architecture” also retrieve secondary titles (*Clean Architectures in Python*, *Clean Code Principles…*, *Clean Architecture with .NET*) and index-only TOC pages — useful for discovery, not interchangeable with Martin primary. [E2: Alexandria corpus=`software_engineering` chunk_id=`e6d3c57223eb8759580341a1` source=`Clean Architectures in Python…` query=`Clean Architecture dependency rule…`; also chunk_id=`a8f4e91eac146a3a86a8cd01` TOC]
- `FACT` [E2] GoF queries surface secondary catalogs (*Design Patterns in .NET*, Dooley/Kazakova) alongside the 1994 Gamma et al. PDF — prefer GoF primary chunks for FACT locks. [E2: corpus=`software_engineering` chunk_id=`d9135aa9bbe0b535c4d31020` source=`Software Development, Design, and Coding…` vs chunk_id=`e61a7eb1b4daf78a580f20be` source=`…Design Patterns_ Elements…`]
- `CLAIM` [E2] *Beyond Vibe Coding* chunks that name GoF / hexagonal as AI-era guidance are adjacent but out of this slice’s primary criteria job (agent-assisted technical design → T5B-S3). [E2: corpus=`software_engineering` chunk_id=`a8fa8f8a8d841cb82574341f` source=`Beyond Vibe Coding…`]
- `GAP` Hexagonal (Cockburn) and Onion (Palermo) **primary** essays were not fetched this slice; only Martin’s citation of them as related family members. Searched: Martin 2012 blog. Result: names + shared objective stated; no independent primary text.

### 4.2 Clean Architecture — style criteria (primary blog + book corroboration)

- `FACT` [E1] Martin presents Clean Architecture as an integration of related styles that share **separation of concerns** via layers (at least business rules + interfaces): Hexagonal / Ports and Adapters, Onion, Screaming Architecture, DCI, BCE. [E1: Robert C. Martin, “The Clean Architecture” — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — accessed 2026-07-29]
- `FACT` [E1] Stated system qualities of these architectures: independent of frameworks; testable business rules without UI/DB/web server; independent of UI; independent of database; independent of any external agency (business rules don’t know the outside world). [E1: same URL]
- `FACT` [E1] **Dependency Rule:** source code dependencies can only point **inwards**; nothing in an inner circle may know anything about an outer circle — including names of functions, classes, variables, or other named entities; outer-circle data formats (esp. framework-generated) must not be used by inner circles. Outer circles are mechanisms; inner circles are policies. [E1: same URL]
- `FACT` [E2] Martin 2017 book restates the Dependency Rule as: “Source code dependencies must point only inward, toward higher-level policies,” with the same name-mention prohibition. [E2: Alexandria corpus=`software_engineering` source=`Martin, Robert - Clean Architecture… (2017…)` chunk_id=`56915a48c933328edd85d8c1` query=`Clean Architecture dependency rule…`]
- `FACT` [E1] Layer intents (schematic four circles; more allowed if Dependency Rule holds): **Entities** (enterprise-wide / most general business rules); **Use Cases** (application-specific rules; orchestrate entities); **Interface Adapters** (convert formats for UI/DB/services; MVC Presenters/Views/Controllers live here; SQL stays here); **Frameworks and Drivers** (outermost details / glue). [E1: Martin 2012 blog — same URL]
- `FACT` [E1] Circles are schematic — may need more than four; Dependency Rule always applies; inward = higher abstraction / policy; outermost = concrete detail. [E1: same URL]
- `FACT` [E1] Crossing boundaries: flow of control may move outward (e.g. controller → use case → presenter), but **source code dependencies** still point inward; resolve with **Dependency Inversion** — inner circle defines an interface (e.g. use-case output port); outer circle implements it. [E1: same URL]
- `FACT` [E2] Book corroborates DIP-at-boundary: use case must not call presenter by name; call an interface in the inner circle that the presenter implements. [E2: corpus=`software_engineering` chunk_id=`85866aa3ccd8af5774e1627f` source=`Martin…Clean Architecture…2017` query=`Clean Architecture dependency rule…`]
- `FACT` [E1] Data crossing boundaries should be simple isolated structures convenient for the **inner** circle; do not pass Entities or DB row structures that would force inner code to know outer frameworks. [E1: Martin 2012 blog]
- `FACT` [E2] Use-case request/response models must not depend on framework types (e.g. HTTP request/response); Entities are higher-level than use cases — use cases depend on Entities, not vice versa. [E2: corpus=`software_engineering` chunk_id=`02fedfa782c5c70f54ae4fbb` source=`Martin…Clean Architecture…2017` query=`Clean Architecture dependency rule…`]

### 4.3 Modularity / dependency criteria at component level (Martin book)

- `FACT` [E2] **Acyclic Dependencies Principle (ADP):** “Allow no cycles in the component dependency graph.” Cycles cause “morning after” breakage and make build order hard; break cycles via DIP (introduce interface in the depended-on direction) or extract a new shared component so the graph is a DAG. [E2: corpus=`software_engineering` chunk_id=`d942b2c8f07de5d30c49e6bf` + chunk_id=`805b9ef1302c05be69b6b48b` source=`Martin…Clean Architecture…2017` query=`Acyclic Dependencies Principle…`]
- `FACT` [E2] Component dependency structure is **not** designed wholly top-down at project start; it evolves with the system. Component diagrams map **buildability/maintainability**, not primarily the functional decomposition of the app. [E2: chunk_id=`805b9ef1302c05be69b6b48b` + chunk_id=`37081febd14716937a0357e0` same source]
- `FACT` [E2] **Stable Dependencies Principle (SDP):** “Depend in the direction of stability.” A component expected to be volatile must not be depended on by a hard-to-change component; stability here ≈ difficulty of change (often driven by fan-in), not merely change frequency. [E2: chunk_id=`37081febd14716937a0357e0` + chunk_id=`9c46cca2c35c220da5c6dd74` same source/query=`Stable Dependencies Principle…`]
- `FACT` [E2] Not all components should be maximally stable — some must remain unstable/changeable; SDP violations include stable components depending on intended-flexible ones. [E2: chunk_id=`e6b563b2f127f31915e1670b` same source]
- `FACT` [E2] **Stable Abstractions Principle (SAP):** “A component should be as abstract as it is stable.” Stable components should be extensible via interfaces/abstract classes; SDP+SAP together amount to DIP for components (dependencies toward stability and abstraction). [E2: chunk_id=`0ff31e93aaa3b529fd98eac6` same source]
- `FACT` [E2] Book TOC/structure also names component **cohesion** principles (REP, CCP, CRP) as sibling criteria to coupling principles — present in corpus; detailed body excerpts for REP/CCP/CRP were not pulled as deep quotes this slice. [E2: chunk_id=`a8f4e91eac146a3a86a8cd01` TOC; index mentions in chunk_id=`c74d24b634b18e89402fd972`]
- `GAP` Full prose definitions and tension-diagram guidance for REP / CCP / CRP were not retrieved as standalone body chunks in this pass. Searched: ADP/SDP/SAP-focused queries + TOC. Result: names confirmed; detailed cohesion criteria deferred or Wave 2 residual.

### 4.4 GoF design patterns — modularity vocabulary (not architecture law)

- `FACT` [E2] GoF: a pattern has four essential elements — **name** (design vocabulary), **problem** (when to apply), **solution** (abstract arrangement of elements), **consequences** (results/trade-offs; critical for evaluating alternatives). [E2: Alexandria corpus=`software_engineering` source=`Erich Gamma… Design Patterns… (1994…)` chunk_id=`e61a7eb1b4daf78a580f20be` query=`Design Patterns Gang of Four purpose…`]
- `FACT` [E2] GoF: design patterns are **not** linked lists/hash tables reusable as-is, and **not** complex domain-specific designs for an entire application or subsystem; they describe communicating objects/classes customized to a general design problem in a context. [E2: chunk_id=`925358a3c14dc1682070fd2d` same source]
- `FACT` [E2] GoF distinguishes **frameworks** (cooperating classes forming a reusable design for a *specific class* of software; architectural guidance via abstract classes) from catalog patterns (usable across nearly any application; do not dictate an application architecture the way a framework does). [E2: chunk_id=`8b70d64bac387c267bbbfce3` + glossary-style chunk_id=`0a8bc4057b93fbb0eb260e37` same source]
- `FACT` [E2] GoF glossary: **coupling** = “The degree to which software components depend on each other.” [E2: chunk_id=`0a8bc4057b93fbb0eb260e37`]
- `FACT` [E2] GoF organizes 23 patterns by purpose into creational / structural / behavioral (class vs object scope). [E2: secondary corroboration Dooley chunk_id=`d155dffa15687208a6cde6fc`; primary classification discussion chunk_id=`26ff235ddf4c4cb41327f251`]
- `FACT` [E2] GoF: consequences help evaluate design alternatives; Applicability/Consequences/Implementation sections guide decisions — patterns describe more of the **why** of a design, not only results. [E2: chunk_id=`1623ad9154b122122a46fffb` + chunk_id=`925358a3c14dc1682070fd2d`]
- `INFERENCE` [E4] At design-time, GoF supplies **named options and consequence checklists** for object-level modularity; Clean Architecture / component principles supply **dependency direction and layer boundaries**. Premises: (1) GoF four elements + not whole-app architecture; (2) Martin Dependency Rule + ADP/SDP/SAP.

### 4.5 Framework Design Guidelines — reusable library boundaries (optional corpus hit)

- `FACT` [E2] FDG scope: best practices for designing **frameworks** = reusable OO libraries, from large system frameworks to medium reusable layers to small shared components; focus is **publicly accessible API** programmability, not general implementation detail. [E2: Alexandria corpus=`software_engineering` source=`…Framework Design Guidelines… (2020…)` chunk_id=`e39abc8d88190455be0e7491` query=`Framework Design Guidelines reusable library boundaries…`]
- `FACT` [E2] Historical motivation: without common rules, stitched components “did not fit together well”; consistency and seamless integration of reusable components became necessary for productivity. [E2: chunk_id=`657205256b23d77d355b07b4` same source]
- `FACT` [E2] **Principle of Layered Architecture** (FDG §2.2.4): factor API set into **low-level** types (power/expressiveness) and **high-level** types (convenience wrapping lower layer); layered design enables both power and ease of use; CONSIDER layered frameworks; AVOID mixing complex low-level with high-level APIs in one namespace; DO ensure layers of a feature area are well integrated so developers can move between layers without rewriting the whole app. [E2: chunk_id=`43c8c10d530454caac5b5cdf` + chunk_id=`cd06bd5c2a37897da741dc22` query=`Framework Design Guidelines Principle of Layered Architecture…`]
- `FACT` [E2] FDG stresses **consistency** as a key quality of well-designed frameworks; guidelines are trade-off-aware (guidelines not rigid rules); prefer postponing a half-done feature; consider evolvability/backward compatibility when trading off. [E2: chunk_id=`025079b812235517bb184dae` + chunk_id=`09763ec11b600a4e14ad412a`]
- `CLAIM` [E2] FDG layered APIs are about **consumer-facing library surface** factoring, not the same claim as Clean Architecture’s policy-vs-mechanism Dependency Rule — related vocabulary (“layers”), different problem (API usability vs business-rule isolation). [E2: compare FDG chunk_id=`43c8c10d530454caac5b5cdf` with Martin Dependency Rule E1 blog]
- `GAP` FDG “breaking changes” appendix and full extensibility chapter body were not deeply retrieved. Searched: layered architecture + reusable boundaries queries. Result: fundamentals + layering principles only.

### 4.6 Design-time process handoff (T5A spine vocabulary only)

- `INFERENCE` [E4] Architecture/modularity criteria from this slice are **decision content** (what constraints/options to weigh); recording **options → tradeoffs → decision → consequences** remains the T5A ADR/MADR spine — do not re-derive templates here. Premises: (1) campaign brief T5A/T5B split; (2) T5A-W1-S1 already covers ADR/MADR section shapes; (3) GoF/Martin both emphasize consequences/trade-offs when choosing designs.
- `OPEN` Whether Toolbelt later mandates Clean Architecture circles as a house style vs treating Dependency Rule + ADP/SDP as criteria checklists inside ADRs. Follow-up: T5B integrator / human accept — not locked by this draft.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Design-time technical guidance should center on **dependency direction** (inward/policy-over-mechanism) plus **acyclic, stability-aware** component graphs, not on a fixed four-circle diagram. | open | Supported by Martin blog+book FACTS; circle count explicitly schematic |
| H2 | GoF patterns are modularity **micro-vocabulary**, not a substitute for architecture style selection. | open | GoF “not entire application” FACT |
| H3 | FDG layering applies when shipping **reusable libraries/plugins**, as a complementary boundary lens to CA for apps. | open | FDG scope + layered principle FACTS; CA vs FDG CLAIM |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Meaning of “layers” | Clean Architecture: policy inward, mechanisms outward (Dependency Rule) [E1 blog] | FDG: high-level convenience APIs vs low-level power APIs for library consumers [E2 FDG] | Prefer distinguishing contexts: **app policy isolation** vs **library API factoring**. Do not merge into one lock. |
| When to design component graph | Martin: component structure evolves; not top-down first [E2 ADP chunks] | Common expectation that large decomposition is early functional architecture [noted by Martin as counterintuitive] | Prefer Martin E2 for component *dependency* graphs; leave functional vs deployable decomposition OPEN for Wave 2 (modular monolith / services). |

## 7. Gaps & OPEN

- `GAP` Primary Hexagonal / Onion / BCE / DCI texts not fetched.
- `GAP` REP / CCP / CRP body detail thin in this pass.
- `GAP` Modular monolith vs microservices tradeoffs deferred to Wave 2.
- `GAP` Architecture Metrics / MMI pattern-consistency measurements deferred (secondary hit only).
- `OPEN` House adoption of CA circles vs Dependency-Rule-as-checklist.
- `OPEN` How strictly FDG applies outside .NET / outside published libraries (e.g. internal Toolbelt plugins).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] A design-time checklist for technical architecture could ask: (1) Which dependencies point **outward** illegally? (2) Are component deps a **DAG**? (3) Do stable/policy modules depend on volatile details? (4) Are boundary-crossing types simple and inward-convenient? (5) For reusable surfaces, are high/low API layers factored for consumers? Premises: §§4.2–4.5 FACTS.
- `INFERENCE` [E4] Pattern application should be justified with GoF-style **problem + consequences**, then recorded via T5A options/ADR when architecturally significant. Premises: GoF four elements; T5A spine vocabulary.
- `INFERENCE` [E4] Do **not** treat this draft as grey-matter stack law, lint policy, UX structure, or skill text. Premises: scope out-list; `draft-is-not-sot`.

## 9. Source list (deduped)

1. Robert C. Martin, “The Clean Architecture” (2012-08-13) — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — accessed 2026-07-29
2. Alexandria `software_engineering` — Martin, Robert, *Clean Architecture: A Craftsman’s Guide to Software Structure and Design* (2017) — chunks `56915a48c933328edd85d8c1`, `85866aa3ccd8af5774e1627f`, `02fedfa782c5c70f54ae4fbb`, `d942b2c8f07de5d30c49e6bf`, `805b9ef1302c05be69b6b48b`, `37081febd14716937a0357e0`, `9c46cca2c35c220da5c6dd74`, `e6b563b2f127f31915e1670b`, `0ff31e93aaa3b529fd98eac6`, `a8f4e91eac146a3a86a8cd01`
3. Alexandria `software_engineering` — Gamma, Helm, Johnson, Vlissides, *Design Patterns* (1994) — chunks `e61a7eb1b4daf78a580f20be`, `925358a3c14dc1682070fd2d`, `8b70d64bac387c267bbbfce3`, `0a8bc4057b93fbb0eb260e37`, `26ff235ddf4c4cb41327f251`, `1623ad9154b122122a46fffb`
4. Alexandria `software_engineering` — Cwalina, Barton, Abrams, *Framework Design Guidelines* (2020) — chunks `e39abc8d88190455be0e7491`, `657205256b23d77d355b07b4`, `43c8c10d530454caac5b5cdf`, `cd06bd5c2a37897da741dc22`, `025079b812235517bb184dae`, `09763ec11b600a4e14ad412a`
5. False-friend / secondary (cited only for hygiene): *Clean Architectures in Python* (`e6d3c57223eb8759580341a1`); Dooley/Kazakova (`d9135aa9bbe0b535c4d31020`, `d155dffa15687208a6cde6fc`); *Beyond Vibe Coding* (`a8fa8f8a8d841cb82574341f`)

## 10. Parent return — short FACT / GAP summary

**FACTS (design-time criteria candidates):**
- Dependency Rule: source deps only inward; inner must not name outer; frameworks/UI/DB are outer details (Martin 2012 E1 + 2017 E2).
- Boundary crossing uses DIP; pass simple inward-convenient data, not framework rows (E1/E2).
- Component criteria: ADP (no cycles), SDP (depend toward stability), SAP (stable ≈ abstract) (Martin 2017 E2).
- GoF: name/problem/solution/consequences; patterns ≠ whole-app architecture; coupling = inter-component dependence (GoF E2).
- FDG (when building reusable libraries): layered high/low APIs, consistency, public-API focus (FDG E2).

**GAPS:** Hexagonal/Onion primaries; REP/CCP/CRP body depth; monolith vs microservices (W2); MMI metrics; house lock of CA circles vs checklist.

**Out (honored):** lint catalogs, grey-matter locks, T5C/T5D, Design skills. T5A reused only as options→decide→ADR vocabulary.
