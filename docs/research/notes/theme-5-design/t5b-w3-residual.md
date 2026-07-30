---
title: "T5B Wave 3 — Residual GAP closers (+1 after low_return)"
status: draft
theme: theme-5-design
track: T5B
wave: 3
slice: T5B-W3
created: 2026-07-29
updated: 2026-07-29
authors: [t5b-w3-gatherer-grok]
supersedes: null
aligned_with:
  - docs/research/notes/theme-5-design/t5b-w2-corroboration.md
  - docs/research/notes/theme-5-design/campaign-brief.md
  - docs/PROTOCOL.md
---

# T5B-W3 — Residual GAP closers (+1 confirmation stage)

**Using `research-protocol`; depth: deep; wave: 3; slice: T5B-W3; this IS the +1 confirmation stage.**

**Status:** `draft`. Not Design SoT. Residual closers only after W2 `low_return_detected=yes`. No Windows deep dive. No open-ended fleets. No Design skill elevation. No grey-matter stack locks.

## 1. Scope

- **Question / goal:** Theme 5 §4.3 **+1 residual stage** after T5B-W2 low-return: try **easy closers** only on named residuals that one fetch / catalog check might close; confirm remaining `GAP`/`OPEN`; stop.
- **In scope:** Cockburn Hexagonal / Palermo Onion **primary** URLs (easy web fetch); quick Alexandria `list_documents` re-check for Newman / APOSD ingest; Coordinator signal with `stop_reason: low_return_plus_one`.
- **Out of scope:** Windows service/desktop literature (W2: **not P0**); Newman book body chase / ingest; Architecture Metrics re-query; ADR template re-litigation (T5A); Design skills; T5C/T5D; further residual stages after this one.
- **Comprehension / research goal type:** other (residual GAP close / +1 confirmation)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (W2 corroboration, campaign-brief §4.3, research-note template, research-protocol / depth modes); Alexandria MCP `list_documents`; WebSearch; WebFetch (Cockburn hexagonal; Palermo Onion part 1) |
| Corpora / URLs searched | Alexandria `software_engineering` (name filters only); https://alistair.cockburn.us/hexagonal-architecture ; https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/ ; discovery via WebSearch for Cockburn / Palermo primaries |
| Queries (exact) | Alexandria `list_documents` `name_substring=Microservices` / `Newman` / `Philosophy of Software`; WebSearch `Alistair Cockburn Hexagonal Architecture ports and adapters primary essay`; WebSearch `Jeffrey Palermo Onion Architecture primary essay site:jeffreypalermo.com` |
| What was *not* searched | Windows service/desktop design literature; Newman *Building Microservices* / *Monolith to Microservices* full-text web deep dive; Richards & Ford FSA PDF; Architecture Metrics / APP re-RAG; lint catalogs; grey-matter product surfaces |
| Depth | deep |
| Waves / stop_reason | wave: **3** (slice T5B-W3 = Theme 5 **+1** after W2 low_return). stop_reason: **`low_return_plus_one`** — Hexagonal/Onion primary GAPs closed by one fetch each; Newman/APOSD catalog still empty; Windows left confirmed non-P0 GAP (not searched); no further residual stage |
| Provenance (optional PROV) | Entity←W2 residuals + Cockburn/Palermo primaries + Alexandria catalog E0; Activity=T5B-W3 +1 residual; Agent=Grok gatherer |

### 2.1 Prior low_return pin (from W2)

- `FACT` [E0] T5B-W2 Coordinator signal: `low_return_detected=yes`; Residual P0 for Windows = **none** (Windows OPEN/non-P0); suggested optional W3 = Newman if ingested, Cockburn/Palermo primaries if family-primary cites still needed. [E0: `docs/research/notes/theme-5-design/t5b-w2-corroboration.md` §10 — 2026-07-29]
- `FACT` [E0] Campaign §4.3: after low_return detect, run **exactly one** +1 residual stage on named P0/P1 GAPs that might still close; then hard stop with `stop_reason=low_return_plus_one`. [E0: `docs/research/notes/theme-5-design/campaign-brief.md` §4.3]

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | +1 confirmation only; easy closers on named residuals |
| Scope boundary | Two primary essay URLs + catalog presence checks; no Windows deep dive |

## 4. Findings

### 4.1 Hexagonal Architecture — Cockburn primary **CLOSED**

- `FACT` [E1] Alistair Cockburn, *Hexagonal architecture* (HaT Technical Report 2005.02, dated 2005-09-04 on page): alternative name **Ports and Adapters**; intent — allow an application to be driven equally by users, programs, automated tests, or batch scripts, and developed/tested in isolation from eventual run-time devices and databases. [E1: https://alistair.cockburn.us/hexagonal-architecture — accessed 2026-07-29]
- `FACT` [E1] Mechanism: events arrive at a **port**; a technology-specific **adapter** converts them into a procedure call/message for the application; outputs leave via a port to an adapter for the receiving technology; the application interacts with adapters without knowing the nature of the outside devices. [E1: same URL]
- `FACT` [E1] Hexagon visual purpose: (a) inside–outside asymmetry and similar nature of ports (escape one-dimensional layered picture); (b) room for a defined number of ports — hexagon shape is not because six is special. A **port** = purposeful conversation; typically multiple adapters per port (GUI, FIT, batch, HTTP, mock DB, real DB, …). Primary/driving vs secondary/driven flavors noted for implementation. [E1: same URL]
- `FACT` [E1] Explicit link to DIP: cites Martin Dependency Inversion / Fowler Dependency Injection as showing how to create swappable **secondary** actor adapters. [E1: same URL — Related Patterns]
- `INFERENCE` [E4] Closes W2 `GAP` “Hexagonal primary essay unfetched.” Corroborates W1/W2 ports-adapters / DIP-at-boundary family as **named primary pattern**, without crowning hexagon shape or any folder layout as Toolbelt law. Premises: these E1 FACTS; W2 APP ports CLAIMs; W1 Martin Dependency Rule E1.
- `INFERENCE` [E4] Cockburn primary and Martin Clean Architecture Dependency Rule are **related family**, not identical documents — do not collapse names in integrator language. Premises: Cockburn ports/adapters E1; Martin Dependency Rule from W1 (not re-fetched).

### 4.2 Onion Architecture — Palermo primary **CLOSED**

- `FACT` [E1] Jeffrey Palermo, *The Onion Architecture : part 1* (2008-07): pattern for long-lived / complex-behavior apps (explicitly **not** appropriate for small websites); emphasizes interfaces for behavior contracts and externalization of infrastructure. [E1: https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/ — accessed 2026-07-29]
- `FACT` [E1] Fundamental rule: code may depend on layers more central; code **must not** depend on layers further out — “all coupling is toward the center.” Domain Model at center; repository **interfaces** in application core; UI / Infrastructure / Tests on the edges; implementing repository classes outside the core, coupled to a particular data-access method. [E1: same URL]
- `FACT` [E1] Relies heavily on Dependency Inversion; database is **not** the center — external storage via infrastructure implementing core-meaningful interfaces. Palermo states Hexagonal and Onion **share** the premise: externalize infrastructure and write adapter code so infrastructure does not become tightly coupled. [E1: same URL]
- `INFERENCE` [E4] Closes W2 `GAP` “Onion primary essay unfetched.” Aligns with W1/W2 Dependency Rule / DIP / ports family as another named vocabulary for inward coupling — still **not** a stack lock. Premises: these E1 FACTS; §4.1; W2 APP folder/ports CLAIMs.
- `GAP` Palermo parts 2–4 and Cockburn later “Hexagonal Architecture Explained” PDF **not** deep-read this +1 stage (part 1 + 2005 article suffice for primary cite close). Follow-up only if integrator needs four-tenets wording from part 3/4.

### 4.3 Easy catalog checks — Newman / APOSD **still GAP**

- `FACT` [E0] Alexandria `software_engineering` `list_documents` `name_substring=Microservices` → **0** documents. [E0: Alexandria list_documents — 2026-07-29]
- `FACT` [E0] Same corpus `name_substring=Newman` → **0** documents. [E0: same]
- `FACT` [E0] Same corpus `name_substring=Philosophy of Software` → **0** documents (APOSD ingest still unconfirmed). [E0: same]
- `GAP` Newman *Building Microservices* / *Monolith to Microservices* book body still unavailable in this corpus — **confirmed GAP** after +1 catalog re-check. Searched: title filters above. Result: not ingested. W1 Fowler E1 + W2 Gorton/Esposito remain the both-sides deployable-boundary evidence.
- `GAP` Ousterhout *A Philosophy of Software Design* still not confirmed in Alexandria — **confirmed GAP** (S3 carry). No web deep-dive this stage.

### 4.4 Windows — confirmed non-P0; **not searched**

- `FACT` [E0] W2 explicitly marked Windows service/desktop as **OPEN/non-P0** and “None required for Windows” as Residual P0 for W3. [E0: W2 §10]
- `GAP` Windows service / desktop as design concerns — **confirmed GAP / not elevated**; intentionally **not searched** in this +1 stage per W2 + parent instruction. Prefer confirmed GAP over weak E3 chase.
- `INFERENCE` [E4] Do not block T5B track synthesis on Windows literature. Premises: W2 non-P0 pin; campaign +1 scope.

### 4.5 Other named residuals — confirm and stop (no chase)

- `GAP` Quantitative “architecturally significant enough for ADR” checklist — still absent; **confirmed GAP** (W1 S2 / W2 Metrics). Not closable by one URL fetch; no further search.
- `GAP` Strangler / Newman-depth migration playbooks — still thin; **confirmed GAP** pending Newman ingest or separate campaign.
- `OPEN` House adoption of MMI / cycle gates vs qualitative checklists only — unchanged; acceptance only.
- `OPEN` Whether Toolbelt pins `adr/madr` vs Nygard-minimal — T5A ownership; unchanged.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | One WebFetch closes Cockburn Hexagonal primary GAP | **confirmed** | §4.1 E1 |
| H2 | One WebFetch closes Palermo Onion primary GAP | **confirmed** | §4.2 E1 |
| H3 | Newman / APOSD appear in Alexandria since W2 | **rejected** | §4.3 E0 zeros |
| H4 | Windows should be deep-dived in +1 stage | **rejected** | W2 non-P0; §4.4 |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Pattern naming (Hexagonal vs Onion vs Clean) | Cockburn Ports & Adapters [E1] | Palermo Onion [E1]; Martin Dependency Rule [E1 W1]; APP ports practice [E2 W2] | Cite as **related family** (externalize infra / inward coupling / DIP); do **not** treat as one interchangeable SoT name |
| (No new deployable-boundary conflicts) | — | — | W2 Fowler vs Gorton conflict log stands; not re-opened |

## 7. Gaps & OPEN

**Closed this wave**

- Hexagonal Architecture Cockburn **primary** essay — closed (§4.1).
- Onion Architecture Palermo **primary** essay (part 1) — closed (§4.2).

**Confirmed remaining (stop; no further +1)**

- `GAP` Newman books not in Alexandria (catalog re-check failed).
- `GAP` APOSD book ingest unconfirmed.
- `GAP` Windows service/desktop design — non-P0; not searched.
- `GAP` Quantitative ADR-significance checklist.
- `GAP` Deep Strangler / migration playbooks.
- `OPEN` MMI/cycle gates vs qualitative checklists.
- `OPEN` ADR template repo pin (T5A).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] T5B design-time vocabulary can now cite **primary** Hexagonal (Cockburn) and Onion (Palermo) alongside Martin Dependency Rule and APP practice — still as **criteria/family**, not mandatory folder law or grey-matter stack. Premises: §4.1–4.2; W1/W2; `draft-is-not-sot`.
- `INFERENCE` [E4] Remaining residuals are **unavailable corpus**, **non-P0**, or **acceptance OPEN** — further gatherer waves would violate §4.3 hard stop. Premises: §4.3–4.5; campaign-brief §4.3.
- `INFERENCE` [E4] Proceed to **T5B track synthesis**; integrator merges W1+W2+W3 without inventing Newman/Windows/APOSD facts. Premises: Coordinator signal §10.

## 9. Source list (deduped)

1. Alistair Cockburn — Hexagonal architecture (Ports and Adapters) — https://alistair.cockburn.us/hexagonal-architecture — accessed 2026-07-29 — **E1**
2. Jeffrey Palermo — The Onion Architecture : part 1 — https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/ — accessed 2026-07-29 — **E1**
3. Alexandria `software_engineering` — `list_documents` filters Microservices / Newman / Philosophy of Software — 2026-07-29 — **E0** (all zero)
4. Prior gatherer (alignment): `docs/research/notes/theme-5-design/t5b-w2-corroboration.md`
5. Campaign stop rule: `docs/research/notes/theme-5-design/campaign-brief.md` §4.3

---

## 10. Coordinator signal

| Field | Value |
|-------|--------|
| `low_return_detected` (prior) | **yes** (W2) |
| This stage | Theme 5 **+1 confirmation** (T5B-W3) |
| `stop_reason` | **`low_return_plus_one`** |
| Closed | Cockburn Hexagonal primary (E1); Palermo Onion primary part 1 (E1) |
| Confirmed GAP/OPEN (no further chase) | Newman corpus absent; APOSD absent; Windows non-P0 (not searched); ADR-significance checklist; MMI adoption OPEN; template pin OPEN (T5A) |
| Recommend | **Proceed to T5B track synthesis.** Do **not** launch another residual stage (campaign §4.3: one confirmation stage, then hard stop). |

### Parent return summary

- **Stage:** T5B-W3 = Theme 5 +1 after W2 `low_return_detected=yes`
- **Closed:** Hexagonal (Cockburn E1) + Onion (Palermo E1) primary essay GAPs
- **Confirmed open:** Newman/APOSD catalog empty; Windows left non-P0 untouched; ADR-significance / MMI / template-pin unchanged
- **`stop_reason`:** `low_return_plus_one`
- **Recommend:** **T5B track synthesis** (no further +1)
