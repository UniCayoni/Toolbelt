---
title: "T24F-web — What makes a guideline/pattern GOOD (web primary sources)"
status: draft
theme: theme-24-author-learning
track: T24F
created: 2026-08-05
updated: 2026-08-05
authors: [t24f-web-gatherer]
depth: deep
wave: W1
supersedes: null
aligned_with:
  - docs/research/notes/theme-24-author-learning/campaign-brief.md
  - docs/research/notes/theme-24-author-learning/deep-campaign-board.md
hard_fences:
  - draft ≠ Toolbelt / host law
  - no auto-accept; host standards quality track only
  - not rewriting Toolbelt plugin skills/*
---

# T24F-web — Guideline / pattern quality (web gatherer)

**Using `research-protocol`**. Depth: **deep** (Wave 1 gatherer). **Draft ≠ SoT.** Findings feed Theme 24 host-standards quality track (T24F); they do **not** auto-promote candidates into host standards.

## 1. Scope

- **Question / goal:** What makes a pattern, structure, or guideline **good**, and how should candidates be **tested** before promotion into host standards?
- **In scope:** Public primary/secondary web sources on coding-standards design; Google engineering style / eng-practices principles; ISO/IEEE guidance where findable; “good requirements” SMART/checkable criteria transferable to standards; Diátaxis only where tied to guideline/docs quality.
- **Out of scope:** Auto-accept as Toolbelt law; Theme 23 playbook; CI/PR ceremony as SoT; inventing Cursor private APIs; locking host catalog modules from this note alone.
- **Comprehension / research goal type:** other (method / quality contract for author-learning harvest)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-05 |
| Tools used | WebSearch; WebFetch; local read of fetched page extracts |
| Corpora / URLs searched | Google eng-practices; Google style guides; *Software Engineering at Google* (Abseil HTML ch.08); Diátaxis quality page; IEEE SA / ISO catalog pages for 29148, 25030, 5055; IEEE 830-1998 text (redistributed PDF); Mannion & Keepence SMART paper (university PDF); ASME DETC2024 abstract on 29148 well-formedness |
| Queries (exact) | `Google engineering practices style guide principles good coding standards`; `ISO IEEE software coding standards requirements quality guidance site:iso.org OR site:ieee.org`; `SMART requirements criteria checkable verifiable IEEE 830 OR ISO 29148`; `Google style guide "exceptions" OR "when to use" coding standards design principles`; `Diátaxis documentation quality criteria for standards guidelines`; `Google JavaScript Style Guide "avoids giving advice that isn't clearly enforceable"`; `ISO/IEC/IEEE 29148 characteristics of individual requirements verifiable`; `SRE error budget coding standards OR style guide rules quality analogy` |
| What was *not* searched | Paid ISO/IEEE full-text purchase portals beyond free abstracts; proprietary Google internal style-arbiter tooling docs; Alexandria RAG (parallel T24F-RAG); local Theme 16 quality notes as web evidence |
| Depth | deep |
| Waves / stop_reason | W1 gatherer only; stop when primary Google + requirements-quality + Diátaxis functional-quality axes covered; residual ISO body text paywalled → GAP; SRE error budgets omitted (not about rule quality) |
| Provenance (optional PROV) | Entity=web primary docs; Activity=T24F-web gather 2026-08-05; Agent=subagent |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed (web primary/secondary only) |
| Why this mode | Board assigns T24F-web as parallel web gatherer; E0/RAG elsewhere |
| Scope boundary | Public URLs; no host `docs/standards/` invent; no Toolbelt skill rewrite |

## 4. Findings

### 4.1 What “good” means for style / coding guidelines (Google primary)

- `FACT` [E1] Google’s *Software Engineering at Google* ch.08 distinguishes **rules** (mandatory, universally enforceable except approved need-to-use exceptions) from **guidance** (recommendations / best practices with room for variance). Style guides collect the “do’s and don’ts … that must be followed” and are treated as canon for coding practices. [E1: Style Guides and Rules — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Creating rules should start from the **goal** being advanced (“What goal are we trying to advance?”), not from a wishlist of rules. At Google’s stated scale goals, rules should manage complexity while keeping the codebase manageable and engineers productive. [E1: Creating the Rules / Guiding Principles — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Overarching principles for Google style rules: **pull their weight**; **optimize for the reader**; **be consistent**; **avoid error-prone and surprising constructs**; **concede to practicalities when necessary**. [E1: Guiding Principles — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] “Pull their weight” means not everything belongs in a style guide: each rule has nonzero learning/adaptation cost; self-evident or vanishingly rare bad practices may be omitted; “too many” rules is measured by what engineers must **remember**, moderated by tooling that automates adherence. [E1: Rules must pull their weight; TL;DR tooling footnote — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Google C++ Style Guide states the same core goals publicly (pull weight; optimize for reader; consistency local/community; avoid surprising/dangerous and hard-to-maintain constructs; be mindful of scale; concede to optimization when necessary) and says understanding goals clarifies when a rule may be **waived** and what argument would be needed to **change** a rule. [E1: Goals of the Style Guide — https://google.github.io/styleguide/cppguide.html — accessed 2026-08-05]

- `FACT` [E1] Google JavaScript Style Guide focuses on hard-and-fast rules followed universally and “avoids giving advice that isn't clearly enforceable (whether by human or tool).” Examples are non-normative; optional formatting in examples must not be enforced as rules. Terminology uses RFC 2119 must/should/may. [E1: Introduction — https://google.github.io/styleguide/jsguide.html — accessed 2026-08-05]

- `FACT` [E1] Style-guide rule categories (Google): rules to **avoid dangers**; rules to **enforce best practices**; rules to **ensure consistency** (including arbitrary-but-decided choices that end bikeshedding). Much good advice is intentionally **left out** of style guides. [E1: The Style Guide — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Google eng-practices code-review standard: style guide is absolute authority for style; points not in the guide are personal preference (consistency with existing local style, else accept author). Design is almost never “pure style”; weigh on engineering principles / data. Prefer continuous improvement of code health over perfection. [E1: The Standard of Code Review — https://google.github.io/eng-practices/review/reviewer/standard.html — accessed 2026-08-05]

- `FACT` [E1] Eng-practices distinguishes style-guide **requirements** vs **recommendations**; non-guide style comments should be prefixed “Nit:” and must not block submission on personal preference alone. [E1: What to look for in a code review (Style / Consistency) — https://google.github.io/eng-practices/review/reviewer/looking-for.html — accessed 2026-08-05]

### 4.2 How to test / change candidates before elevating rules (Google primary)

- `FACT` [E1] Style-guide updates are **solution-based**: identify an existing problem and present the change as a fix. Problems are **proven with patterns found in existing code**, not hypotheticals. Documented pros/cons/reasoning behind prior rulings enable reevaluation when conditions change. [E1: Changing the Rules / The Process — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Community discussion precedes arbiter approval; proposals may be rejected as unnecessary, too ambiguous, or not beneficial. Final decisions are **trade-off judgments** against agreed style-guide goals, not personal preference. [E1: The Process / The Style Arbiters — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] New / poorly understood language features may start with **restrictive** rules; waiver-request patterns are observed to extract good vs bad practice before widening the rule. Clear valid exemption patterns may imply the rule should be clarified/amended—or kept if false-positive waiver requests remain common. [E1: Enforcing best practices; Exceptions — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] Prefer **automated** enforcement (formatters, static analyzers) for technical rules when feasible: improves scale, reduces interpretation variance and forgotten rules; judgment-heavy or social rules may remain human-enforced. Informal internal estimate cited: ~90% of C++ style-guide rules could be automatically verified (mid-2018 survey). [E1: Applying the Rules / Error Checkers — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

- `FACT` [E1] TL;DRs from the chapter: aim for resilience to time and scaling; know the data so rules can be adjusted; not everything should be a rule; consistency is key; automate enforcement when possible. [E1: TL;DRs — https://abseil.io/resources/swe-book/html/ch08.html — accessed 2026-08-05]

### 4.3 “Good requirements” criteria transferable to standards wording

- `FACT` [E1] IEEE SA abstract for ISO/IEC/IEEE 29148:2018 states the document “defines the construct of a good requirement, provides attributes and characteristics of requirements,” and discusses life-cycle application; it supersedes IEEE 830-1998 among others. [E1: IEEE/ISO/IEC 29148-2018 — https://standards.ieee.org/standard/29148-2018.html — accessed 2026-08-05]

- `FACT` [E1] ISO/IEC/IEEE 29148:2018 §5.2.5 requires each individual requirement to be: **Necessary**, **Appropriate**, **Unambiguous**, **Complete**, **Singular**, **Feasible**, **Verifiable**, **Correct**, **Conforming**. Verifiable means structured/worded so realization can be proven; “Verifiability is enhanced when the requirement is measurable.” [E1: ISO/IEC/IEEE 29148:2018 §5.2.5 — characteristics; official catalog https://standards.ieee.org/standard/29148-2018.html — accessed 2026-08-05; full clause text observed via IEEE-copyrighted redistribution used for research extract]

- `FACT` [E1] 29148 §5.2.6 set-level characteristics: **Complete**, **Consistent**, **Feasible**, **Comprehensible**, **Able to be validated**. §5.2.7 rejects vague/subjective/open-ended language (e.g. “user friendly,” “easy to use,” “as appropriate,” unbounded “all/always/never”) as harming verifiability. Prefer stating **what** is needed, not **how**. [E1: ISO/IEC/IEEE 29148:2018 §§5.2.6–5.2.7 — same source path as above — accessed 2026-08-05]

- `FACT` [E2] Peer-reviewed secondary confirms the same nine individual well-formedness characteristics for 29148:2018 and frames automated assessment of them. [E2: ASME DETC2024-139583 abstract — https://doi.org/10.1115/detc2024-139583 — accessed 2026-08-05]

- `FACT` [E1] IEEE Std 830-1998 (superseded) lists good-SRS characteristics: correct; unambiguous; complete; consistent; ranked for importance/stability; **verifiable**; modifiable; traceable. A requirement is verifiable iff there exists a finite cost-effective process (person or machine) to check the product meets it; examples of nonverifiable wording include “works well,” “good human interface,” “shall usually happen.” [E1: IEEE Std 830-1998 §4.3 / §4.3.6 — https://wildart.github.io/MISG5020/standards/IEEE-830-1998.pdf — accessed 2026-08-05; superseded by 29148]

- `FACT` [E2] Mannion & Keepence adapt SMART for requirements as Specific, Measurable, Attainable, Realisable, Traceable — a practical checklist for expression quality (not proof of need-correctness). Measurable ≈ can verify after construction that the requirement was met. [E2: SMART Requirements (ACM SIGSOFT SEN 1995) — https://wstomv.win.tue.nl/edu/2ip30/references/smart-requirements.pdf — accessed 2026-08-05]

- `INFERENCE` [E4] Transfer to host-standard candidates: treat each candidate rule like a “requirement on contributors/agents” — prefer necessary, singular, unambiguous, feasible, and **checkable** (tool, review checklist, or explicit human judgment criterion); demote vibes (“write good code,” “be clean”) unless made measurable or explicitly scoped as non-blocking guidance. Premises: (1) 29148/830 verifiability criteria; (2) Google enforceability / rules-vs-guidance split; (3) T24F question is pre-promotion testing for host standards.

### 4.4 ISO software-quality frameworks (abstract-level)

- `FACT` [E1] ISO/IEC 25030:2019 abstract: framework for quality requirements (elicit, define, use, govern); uses ISO/IEC 25010/25012 models; does **not** prescribe specific quality measures or development processes. Confirmed current as of 2025 review note on ISO page. [E1: ISO/IEC 25030:2019 — https://www.iso.org/standard/72116.html — accessed 2026-08-05]

- `GAP` Full normative text of ISO/IEC 25030:2019, ISO/IEC 5055:2021, and purchasable 29148 PDF via ISO.org store was not freely WebFetchable this pass (paywall / timeouts). Searched: ISO catalog pages; IEEE SA abstract. Result: abstracts + 29148 clause text via redistribution only for 29148 characteristics.

- `CLAIM` [E2] ISO/IEC 5055:2021 (from search-snippet abstract) defines automated source-code quality measures based on counting violations of good architectural/coding practices that can cause operational risk or excess cost — relevant as an **automated-violation** analogy for enforceable standards, not as host coding law. [E2: search synthesis pointing to https://www.iso.org/standard/80623.html — full abstract page fetch timed out 2026-08-05; treat as weak until re-fetched]

### 4.5 Diátaxis (docs quality tied to guideline quality)

- `FACT` [E1] Diátaxis separates **functional quality** (accuracy, completeness, consistency, usefulness, precision — objective, measurable, independent dimensions) from **deep quality** (flow, fit to needs, beauty — subjective judgment). Deep quality is conditional on functional quality. [E1: Towards a theory of quality in documentation — https://diataxis.fr/quality/ — accessed 2026-08-05]

- `FACT` [E1] Diátaxis **cannot address** functional quality directly; it can help **expose** functional lapses (e.g. gaps become visible when structure mirrors code). It offers principles for deep quality, not a formula guaranteeing excellence. [E1: Diátaxis and quality — https://diataxis.fr/quality/ — accessed 2026-08-05]

- `INFERENCE` [E4] For host standards as reference-like law surfaces: require functional-quality gates (accurate, complete, consistent, useful, precise wording) **before** debating “feels good” pedagogy; keep tutorials/how-tos out of normative modules (Diátaxis mode separation). Premises: (1) Diátaxis functional vs deep; (2) Google JS enforceability / non-normative examples; (3) Theme 16 host-standards separation of law vs guidance (not re-proven here — OPEN to T24C-E0).

### 4.6 SRE / error budgets

- `GAP` SRE error-budget literature found addresses **service reliability vs feature velocity**, not coding-guideline or standards-rule quality. Searched: `SRE error budget coding standards OR style guide rules quality analogy`. Result: no clear primary mapping to rule quality → **omitted** per scope fence (do not stretch analogies).

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Good host-standard candidates are goal-tied, weight-pulling, reader-optimized, consistent, and enforceable (tool or clear human check) | confirmed (external pattern) | Google ch.08 + C++/JS guides + eng-practices |
| H2 | Pre-promotion tests should require demonstrated recurrence in real artifacts + documented trade-offs + arbiter/human accept | confirmed (external pattern) | Google changing-rules process |
| H3 | Requirements SMART/29148 verifiability maps cleanly onto standard-clause wording tests | confirmed (transfer) | 29148 §5.2.5–7; 830 §4.3.6; Mannion SMART |
| H4 | Error budgets are a useful direct metaphor for standards “rule budgets” | rejected for this pass | No primary tying budgets to rule quality |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Consistency vs progress | Eng-practices: style guide absolute; else local consistency | C++ guide / SWE book: consistency is tie-breaker; don’t freeze old style forever; concede practicalities | Prefer higher-detail primary: consistency strong but not absolute; waivers/exceptions + documented goal trade-offs |
| Completeness of “good requirement” lists | IEEE 830 (8 SRS qualities) | 29148 (9 individual + 5 set) | Prefer **29148** (current); treat 830 as historical transferable verifiability lesson |
| SMART expansion of “T” | Classic management SMART = Time-bounded | Mannion = Traceable for requirements | Cite Mannion as adapted E2; do not claim universal SMART definition |

## 7. Gaps & OPEN

- `GAP` Official paywalled full text of ISO/IEC 25030, 5055, and ISO-hosted 29148 not retrieved via free WebFetch.
- `GAP` No primary found that operationalizes “error budget for style rules.”
- `OPEN` How Theme 16 accepted host-standards anatomy maps these external tests onto Toolbelt `author-standards` / proposed-only elevate (handoff to T24C-E0 + T24F-RAG + integrator).
- `OPEN` Concrete host smoke checklist wording (still draft feedstock; human accept later).

## 8. Implications (INFERENCE only)

**Not design locks. Host standards quality track T24F. No auto-accept.**

- `INFERENCE` [E4] Candidate promotion gate (external-pattern synthesis): (1) state the **goal** the rule advances; (2) show **recurrent evidence** in real host artifacts (not hypothetical); (3) write as **necessary / singular / unambiguous / feasible**; (4) define a **check** (tool, review question, or explicit judgment criterion) — else ship as guidance/nit, not law; (5) document pros/cons and waiver surface; (6) human arbiter accept → proposed → accepted. Premises: H1–H3 findings.
- `INFERENCE` [E4] Prefer fewer high-weight rules + automation over large advisory corpora mislabeled as standards. Premises: pull-weight + automate-enforcement FACTS.
- `INFERENCE` [E4] Separate **functional** wording quality (checkable) from pedagogical “deep quality” packaging; do not block promotion solely on deep quality, and do not promote on deep quality without functional quality. Premises: Diátaxis FACTS + 29148 verifiability.

## 9. Source list (deduped)

1. https://abseil.io/resources/swe-book/html/ch08.html — *Software Engineering at Google*, Style Guides and Rules (accessed 2026-08-05)
2. https://google.github.io/styleguide/cppguide.html — Google C++ Style Guide, Goals (accessed 2026-08-05)
3. https://google.github.io/styleguide/jsguide.html — Google JavaScript Style Guide, Introduction (accessed 2026-08-05)
4. https://google.github.io/eng-practices/review/reviewer/standard.html — The Standard of Code Review (accessed 2026-08-05)
5. https://google.github.io/eng-practices/review/reviewer/looking-for.html — What to look for in a code review (accessed 2026-08-05)
6. https://standards.ieee.org/standard/29148-2018.html — IEEE/ISO/IEC 29148-2018 catalog abstract (accessed 2026-08-05)
7. ISO/IEC/IEEE 29148:2018 §§5.2.5–5.2.7 — characteristics / language criteria (research extract from IEEE-copyrighted redistribution; catalog as official locator)
8. https://doi.org/10.1115/detc2024-139583 — ASME DETC2024 well-formed requirements / 29148 characteristics (accessed 2026-08-05)
9. https://wildart.github.io/MISG5020/standards/IEEE-830-1998.pdf — IEEE Std 830-1998 (superseded) (accessed 2026-08-05)
10. https://wstomv.win.tue.nl/edu/2ip30/references/smart-requirements.pdf — Mannion & Keepence, SMART Requirements (accessed 2026-08-05)
11. https://www.iso.org/standard/72116.html — ISO/IEC 25030:2019 abstract (accessed 2026-08-05)
12. https://diataxis.fr/quality/ — Diátaxis quality theory (accessed 2026-08-05)
13. https://www.iso.org/standard/80623.html — ISO/IEC 5055:2021 (abstract fetch incomplete / GAP)

## 10. Gatherer stop

```text
wave: W1
stop_reason: diminishing_returns_primary_axes_covered
covered: Google rule-quality principles + change/test process; 29148/830/SMART checkability; Diátaxis functional quality; ISO abstracts
deferred: RAG corroboration (T24F-RAG); E0 Theme 16 bind; full paid ISO bodies
fence: draft ≠ law; no auto-accept to host standards
```
