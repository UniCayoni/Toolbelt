---
title: "T5B Wave 1 Slice S3 — Contested clean/standards + agent-assisted technical design"
status: draft
theme: theme-5-design
track: T5B
wave: 1
slice: T5B-S3
created: 2026-07-29
updated: 2026-07-29
authors: [t5b-w1-s3-gatherer]
supersedes: null
---

# T5B-W1-S3 — Contested clean code / coding standards as design-time constraints; agents without premature lock

**Using `research-protocol`; depth: deep; wave: 1; slice: T5B-S3.**

## 1. Scope

- Question / goal: How should contested clean code / coding standards act as **design-time constraints**, and how do agents participate in technical design **without premature lock**?
- In scope: Clean Code / Clean Architecture literature (contested — both sides); coding standards as *constraints* (not architecture SoT); agent-assisted technical design from *Beyond Vibe Coding* and *AI-Assisted Programming*; separation from Theme 1 recon-only work; conflict log where schools disagree.
- Out of scope: Elevating lint packs / full lint catalogs as product; grey-matter stack locks; ADR template law (owned by T5A-S1 / Theme 2 — do not re-litigate); T5C UX; Design skill elevation; crowning a “winner” among clean-code schools.
- Comprehension / research goal type (if code): other (design-method literature / secondary corpus + web critique)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Alexandria MCP (`rag_probe`, `rag_query`); WebSearch; WebFetch (Martin Clean Architecture blog; fabianletsch critique; qntm critique; Ousterhout/Martin discussion README via fetch); Read (research-note template, campaign brief / T5B pin / scope prep excerpts); research-protocol skill |
| Corpora / URLs searched | Alexandria `software_engineering`; https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html ; https://fabianletsch.de/blog/clean-code-is-a-lie/ ; https://qntm.org/clean ; https://github.com/johnousterhout/aposd-vs-clean-code/ ; https://earezki.com/clean-code-the-truth/ (discovery via search snippet); https://ambrosiogabe.github.io/code/2022/02/02/a-review-of-clean-code/ (discovery) |
| Queries (exact) | Alexandria: `Clean Code Robert Martin what is clean code meaningful names small functions single responsibility comments as failure`; `Clean Architecture dependency rule entities use cases interface adapters frameworks details independent of frameworks testable`; `Beyond Vibe Coding AI assisted programming technical design architecture planning agents coding standards before implementation`; `AI-Assisted Programming Tom Taulli planning design specifications architecture before coding agents`; `functions should be small do one thing Single Responsibility Principle Boy Scout Rule schools of thought`; `Keeping Options Open architecture defer decisions frameworks details later screaming architecture`; `Be the Architect and the Editor in Chief coding standards maintainability constraints plan-first AI-assisted engineering`; `requirements planning design software development lifecycle AI tools before coding modular programming prompts`; WebSearch: `critiques of Clean Code Robert Martin overengineering`; `John Ousterhout Philosophy of Software Design deep modules critique Clean Code` |
| What was *not* searched | Full lint rule catalogs; grey-matter product code; ADR/MADR primary URLs (T5A-S1); GoF / Framework Design Guidelines (other T5B slices); *A Philosophy of Software Design* book body in Alexandria (not confirmed ingested — used public Ousterhout↔Martin discussion + secondary reviews); theme-1 report body beyond campaign/scope citations; Superpowers skill bodies |
| Depth | deep |
| Waves / stop_reason | wave: 1 (slice T5B-S3). stop_reason: N/A for gatherer slice — Wave 1 primary gather complete for assigned clean/standards + agent-assisted targets; diminishing-returns / track stop owned by coordinator/integrator |
| Provenance (optional PROV) | Entity←Martin Clean Code/Architecture (Alexandria) + Clean Architecture blog; Osmani Beyond Vibe Coding; Taulli AI-Assisted Programming; web critiques (qntm, Letsch, Ousterhout discussion); Activity=T5B-W1-S3 gather; Agent=Alexandria+WebFetch+WebSearch |

**Probe coverage (pre-query):** Clean Code / Clean Architecture / Beyond Vibe Coding / AI-Assisted Programming probes on `software_engineering` returned **partial** (usable; not absent).

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Literature + corpus gather; not workspace recon |
| Scope boundary | Contested clean/standards + agent-assisted technical design only; no Theme 1 recon pass |

## 4. Findings

### 4.1 Separation: constraints vs architecture SoT vs Theme 1 recon

- `FACT` [E0] Campaign / T5B pin put **full lint catalogs**, **grey-matter stack locks**, and **Theme 1-style comprehension-only recon** out of T5B scope; clean/standards are in scope as **design-time constraints**. [E0: `docs/research/notes/theme-5-design/campaign-brief.md` §T5B; `t5b-coordinator-pin.md` §1 — observed 2026-07-29]
- `FACT` [E0] Scope prep caveat: **“Clean Code ≠ architecture SoT”**; grade schools of thought; Theme 1 recon ≠ this track. [E0: `docs/research/notes/theme-5-design/scope-normal-deep-prep.md` T5B caveats — observed 2026-07-29]
- `INFERENCE` [E4] Treat coding standards (naming, function size preferences, DRY intensity, formatter/linter *policy*) as **constraint inputs** to design decisions — not as the architecture decision record itself, and not as a substitute for understanding an existing codebase (Theme 1 recon). Premises: (1) FACT E0 scope boundaries; (2) FACT Clean Architecture “keeping options open” / dependency rule (below); (3) FACT Martin himself frames Clean Code as a *school of thought* (below).

### 4.2 Clean Code school (Martin) — what it claims [E2 Alexandria]

- `CLAIM` [E2] Martin presents Clean Code as professional obligation: “Writing clean code is what you must do in order to call yourself a professional.” [E2: Alexandria corpus=`software_engineering` source=`[Robert C. Martin series 2009_ 1] Martin, Robert C - Clean Code_ A Handbook of Agile Software Craftmanship (2010, Prentice Hall) - libgen.li.pdf` chunk_id=`2e5aa642994e7144cf3de76f` query=`Clean Code Robert Martin what is clean code…`]
- `CLAIM` [E2] Martin’s “Schools of Thought” section: the book’s techniques are the Object Mentor school; “None of these different schools is absolutely right. Yet within a particular school we act as though the teachings and techniques are right.” [E2: same source chunk_id=`b035ef0db28bce56a31f8326` query=`…schools of thought`]
- `CLAIM` [E2] Function-size rule (authoritative within the school, not research-backed in-text): “The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that. This is not an assertion that I can justify. I can’t provide any references to research…” Ideal illustrated as “two, or three, or four lines long.” [E2: same source chunk_id=`5514070bb9ebefc9c2aceafe` query=`functions should be small…`]
- `CLAIM` [E2] Boy Scout Rule: leave the campground cleaner than you found it — incremental cleanup on check-in. [E2: same source chunk_id=`2ff9a77aff91bdd3ad275420`]
- `CLAIM` [E2] Clean code definitions from invited experts differ (Stroustrup: elegant/efficient/one thing well; Feathers: looks like someone who cares; Jeffries/Beck simple-code rules). Martin collects them rather than proving a single metric. [E2: same source chunk_ids=`2cc1558f7f2cfa20c93e1eea`, `246f515aecf39ba37bc09bd8`]
- `FACT` [E2] Contested nature is **internal** to the book: Martin acknowledges plural schools and non-absolute rightness while still presenting rules stridently. [E2: chunk_id=`b035ef0db28bce56a31f8326`]

### 4.3 Clean Architecture (Martin) — design-time structure, not lint [E1 blog + E2 book]

- `FACT` [E1] Martin blog “The Clean Architecture” (2012): family of related architectures (Hexagonal, Onion, Screaming, DCI, BCE) share separation of concerns; systems Independent of Frameworks / Testable / Independent of UI / Independent of Database / Independent of external agency; **Dependency Rule**: source dependencies point only inward. [E1: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html — accessed 2026-07-29]
- `CLAIM` [E2] Book restates Dependency Rule and layers: Entities, Use Cases, Interface Adapters, Frameworks and Drivers; “Nothing in an inner circle can know anything at all about something in an outer circle.” [E2: Alexandria corpus=`software_engineering` source=`Martin, Robert - Clean Architecture_ a Craftsman's Guide to Software Structure and Design (2017, Prentice Hall) - libgen.li.pdf` chunk_id=`56915a48c933328edd85d8c1` query=`Clean Architecture dependency rule…`]
- `CLAIM` [E2] “Keeping Options Open”: leave details (DB, web, REST, DI frameworks, etc.) undecided as long as possible so high-level policy can be developed and experiments run; “the longer you wait… the more information you have.” [E2: same source chunk_id=`e3839997c9903d39ff7ad191`]
- `CLAIM` [E2] Screaming Architecture: good architecture centers use cases and **defers** framework/DB/web choices; frameworks are tools, not ways of life. [E2: same source chunk_ids=`13b06c2acfc5ec20e4c8b0a8`, `cbc51c7258ed4deb3a8d9048`]
- `INFERENCE` [E4] Clean Architecture’s deferral language is closer to **anti-premature-lock for structural decisions** than Clean Code’s function/style rules; do not collapse “clean” style preferences into architecture SoT. Premises: (1) FACT/CLAIM Dependency Rule + options-open; (2) FACT E0 “Clean Code ≠ architecture SoT”; (3) CLAIM Clean Code as school.

### 4.4 Critiques and alternative school — cite both sides [E2/E3 web]

**Do not crown a winner.** Conflict logged in §6.

- `CLAIM` [E3] qntm (2020): Clean Code’s function chapter mixes sound advice with extreme size rules; quotes Martin’s unresearched small-function claim and 2–4 line ideal; argues example “clean” refactors become hard to follow via tiny methods + shared mutable state. [E3: https://qntm.org/clean — accessed 2026-07-29; community essay]
- `CLAIM` [E3] Fabian Letsch: techniques (small functions, naming, DRY) are useful tools, but Clean Code is “dangerous” when it turns tradeoffs into moral absolutes; “there is no such thing as universally ‘clean’ code, only code that makes the right tradeoffs for its context.” [E3: https://fabianletsch.de/blog/clean-code-is-a-lie/ — accessed 2026-07-29]
- `CLAIM` [E3] earezki (search/discovery): recommends reading *A Philosophy of Software Design* or *The Pragmatic Programmer* instead of treating Clean Code as bible; criticizes dogmatic 2–4 line functions and zealous abstraction. [E3: https://earezki.com/clean-code-the-truth/ — discovery via WebSearch 2026-07-29; full body not re-fetched — treat as E3 discovery]
- `CLAIM` [E2] Ousterhout↔Martin public discussion (2024–2025): Ousterhout prefers **deep** methods (much functionality, simple interface) over excessive decomposition into **shallow**/entangled methods; states Clean Code’s length advice “encourages programmers to create teeny-tiny methods that suffer from both shallow interfaces and entanglement”; both agree modular design is good and over-decomposition is possible; they **disagree how far** to decompose. [E2: https://github.com/johnousterhout/aposd-vs-clean-code/ — primary discussion text fetched 2026-07-29; Method Length + Summary sections]
- `CLAIM` [E3] Secondary reviews of APOSD contrast “deep modules” with Clean Code’s many-small-methods mantra (Warne; Dargo blogs via search). [E3: WebSearch hits https://henrikwarne.com/2021/07/12/book-review-a-philosophy-of-software-design/ ; https://www.sandordargo.com/blog/2023/01/25/deep-vs-shallow-modules — discovery; book body not retrieved from Alexandria]
- `GAP` Alexandria did not return *A Philosophy of Software Design* book chunks in this slice’s probes/queries. Searched: software_engineering probes/queries above. Result: critique school represented via public discussion + web reviews, not book ingest.

### 4.5 Agent-assisted technical design without premature lock [E2 Alexandria]

#### Beyond Vibe Coding (Osmani)

- `CLAIM` [E2] Distinguishes **vibe coding** (prompt-first, weak upfront planning → risk of haphazard architecture) from **AI-assisted engineering** (“plan-first”): outline what to build, define **constraints and acceptance criteria** before letting AI loose; AI augments, does not replace engineer judgment. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani)…` chunk_ids=`1022d8da38d4091cca8c5f43`, `054c45ce9edf298e82ce235a` query=`Beyond Vibe Coding AI assisted…` / `Be the Architect…`]
- `CLAIM` [E2] For complex algorithms, mission-critical systems, legacy integration, performance-critical paths: AI as assistant/research partner; **human keeps control of architecture and optimization decisions**. [E2: same source chunk_id=`9345993f3e432f7f2adc5e36`]
- `CLAIM` [E2] Golden rules include: verify AI output against original goal; treat AI output as drafts; stay engaged in decision making; **align team on AI usage standards before** AI-driven development; never merge AI code you do not understand; document rationale. [E2: same source chunk_ids=`09ad186b10a9d65f51d16d09`, `ae5ea30721760ce3b23ed7af`]
- `CLAIM` [E2] “70% problem”: AI excels at boilerplate/routine; struggles with edge cases, **architectural decisions**, production readiness. Durable skills: system design, debugging, architecture. [E2: same source chunk_id=`ae5ea30721760ce3b23ed7af`]
- `CLAIM` [E2] Maintainability chapter frame: enforce consistent styles / refactor AI code; human review focus for machine-generated contributions; seniors as “architect and editor in chief,” mentor and set standards. [E2: same source chunk_ids=`cc47dc0b67418704ab099359`, `634a910c0923868be309129c`]

#### AI-Assisted Programming (Taulli)

- `CLAIM` [E2] Book covers AI tools across requirements, planning, design, coding, debugging, testing; offers modular-programming methodology aligned with prompt-sized generation. [E2: Alexandria corpus=`software_engineering` source=`AI-Assisted Programming Better Planning, Coding, Testing, and Deployment (Tom Taulli)…` chunk_id=`055e90365ff17306461fb880`]
- `CLAIM` [E2] Ch.7 focuses on brainstorming, market research, PRDs/SRS, planning styles, TDD — then Ch.8 Coding; conclusion: mix AI with tried-and-true methods for a strong project base. [E2: same source chunk_ids=`3188a631fef6e20b898fe8ad`, `1bb93187654fb8ea0295c90a`]
- `CLAIM` [E2] Modular programming advice for AI: tools will not produce an advanced app from a simple prompt; break work into clear pieces with clear inputs/outputs; Capilnean quote — focus on problem/approach, ask for single-job verifiable units. [E2: same source chunk_id=`b3100d36097cd210708b4686`]
- `CLAIM` [E2] Takeaway tone: AI tools are sidekicks, not replacements; lack “smarts or independence of a real developer.” [E2: same source chunk_id=`c6c4210ba8a844afb8cbe165`]

### 4.6 How agents participate without premature lock (synthesis atoms only)

- `INFERENCE` [E4] Agent-safe participation pattern consistent with retrieved sources: (a) human-owned **intent + constraints + acceptance criteria** first; (b) agents propose options / drafts / modular slices; (c) humans decide architecture-significant choices and record them elsewhere (ADR process — T5A/Theme 2, not this slice); (d) contested style rules enter as **named constraints or open tradeoffs**, not silent universal law. Premises: Osmani plan-first + golden rules; Taulli modular prompts; Martin options-open; critique literature against moral absolutes.
- `OPEN` Whether Toolbelt should encode a house “default school” (Object Mentor vs APOSD-deep vs local hybrid) for agent prompts. Follow-up: T5B integrator / human accept — not lockable from this draft.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Contested clean-code rules are safer as explicit design-time constraints/tradeoffs than as architecture SoT | open (supported directionally) | §4.1–4.4 |
| H2 | Plan-first + human architecture control reduces premature lock vs vibe-first agent coding | open (supported in Osmani/Taulli CLAIMs) | §4.5 |
| H3 | Extreme function-size rules as automated lint packs would overfit one school | open | Critiques §4.4 + Martin’s own “no research” admission |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Function / method length & decomposition | Martin Clean Code: prefer very small (illustratively 2–4 line) functions [E2 `5514070bb9ebefc9c2aceafe`] | Ousterhout APOSD discussion: warn against shallow/entangled teeny methods [E2 github discussion]; qntm/Letsch critiques [E3] | **Unresolved — cite both.** Prefer neither as SoT. Design-time: record chosen constraint + tradeoff, or leave OPEN. |
| Moral framing of “clean” | Martin professional/absolute tone within school [E2 `2e5aa642994e7144cf3de76f`] + schools caveat [`b035ef0db28bce56a31f8326`] | Letsch: tradeoffs ≠ moral absolutes [E3 fabianletsch] | Leave OPEN; treat as contested constraint language |
| Architecture deferral vs style enforcement | Clean Architecture keep options open on frameworks/DB [E2 `e3839997c9903d39ff7ad191`] | Clean Code Boy Scout / continuous local cleanup [E2 `2ff9a77aff91bdd3ad275420`] | Different layers: structural deferral ≠ forbidding incremental hygiene; do not equate |

## 7. Gaps & OPEN

- `GAP` No Alexandria ingest confirmed for Ousterhout *A Philosophy of Software Design* book text in this pass.
- `GAP` No E0 observation of Toolbelt’s current lint/formatter policy in this slice (intentionally out — lint catalogs).
- `OPEN` House vocabulary for “constraint vs ADR vs recon note” when agents propose style changes that look architectural.
- `OPEN` How strongly to bind agents to project coding standards files vs allowing propose-only deviations (needs accept, not this draft).

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance. **Out of this slice’s authority:** elevating lint packs; grey-matter locks; ADR template law (S1/T5A).

- `INFERENCE` [E4] For Theme 5 Design skills later: teach agents to **surface contested standards as constraints and alternatives**, not to unilaterally “Clean Code” a codebase into one school.
- `INFERENCE` [E4] Prefer plan-first / constraint-first agent workflows (Osmani; Taulli modular slices) when the decision is technical design; use vibe-style generation only where exploration is cheap and architecture is not being locked.
- `INFERENCE` [E4] Keep three lanes distinct in any future surface: (1) **recon/comprehension** (Theme 1), (2) **architecture decisions** (ADR — T5A/T5B-S2), (3) **coding-standard constraints** (this slice — contested, local, revisable).

## 9. Source list (deduped)

1. Alexandria `software_engineering` — Martin, *Clean Code* (chunk_ids: `2e5aa642994e7144cf3de76f`, `b035ef0db28bce56a31f8326`, `5514070bb9ebefc9c2aceafe`, `2ff9a77aff91bdd3ad275420`, `2cc1558f7f2cfa20c93e1eea`, `246f515aecf39ba37bc09bd8`)
2. Alexandria `software_engineering` — Martin, *Clean Architecture* (chunk_ids: `56915a48c933328edd85d8c1`, `5bfcbf2c773b7f885a79b790`, `e3839997c9903d39ff7ad191`, `13b06c2acfc5ec20e4c8b0a8`, `cbc51c7258ed4deb3a8d9048`, `8408974b16c9f5389a841ab1`)
3. Alexandria `software_engineering` — Osmani, *Beyond Vibe Coding* (chunk_ids: `1022d8da38d4091cca8c5f43`, `054c45ce9edf298e82ce235a`, `9345993f3e432f7f2adc5e36`, `09ad186b10a9d65f51d16d09`, `ae5ea30721760ce3b23ed7af`, `cc47dc0b67418704ab099359`, `634a910c0923868be309129c`)
4. Alexandria `software_engineering` — Taulli, *AI-Assisted Programming* (chunk_ids: `055e90365ff17306461fb880`, `3188a631fef6e20b898fe8ad`, `1bb93187654fb8ea0295c90a`, `b3100d36097cd210708b4686`, `c6c4210ba8a844afb8cbe165`)
5. Robert C. Martin, “The Clean Architecture” — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
6. qntm, “It's probably time to stop recommending Clean Code” — https://qntm.org/clean
7. Fabian Letsch, “Clean Code Is Dangerous” — https://fabianletsch.de/blog/clean-code-is-a-lie/
8. johnousterhout/aposd-vs-clean-code — https://github.com/johnousterhout/aposd-vs-clean-code/
9. earezki, “Clean Code: The Cult of Dogma…” — https://earezki.com/clean-code-the-truth/ (discovery)
10. Local campaign/scope/pin — `docs/research/notes/theme-5-design/campaign-brief.md`, `scope-normal-deep-prep.md`, `t5b-coordinator-pin.md`
