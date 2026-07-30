---
title: "T5A Wave 1 Slice S1 — ADR/MADR decision-record practices"
status: draft
theme: theme-5-design
track: T5A
wave: 1
slice: T5A-S1
created: 2026-07-29
updated: 2026-07-29
authors: [t5a-w1-s1-gatherer]
supersedes: null
---

# T5A-W1-S1 — ADR/MADR practices for recording options, tradeoffs, decision, and consequences

**Using `research-protocol`; depth: deep; wave: 1; slice: T5A-S1.**

## 1. Scope

- Question / goal: What are the primary ADR/MADR decision-record practices that a human+agent design process should use to record options, tradeoffs, decision, and consequences?
- In scope: When to write an ADR; required/common sections; status lifecycle; alternatives/options; brevity; supersession; process-relevant atoms from Nygard, Fowler, MADR; reuse of Theme 2 §2.5 FACTS (E2 path citation).
- Out of scope: Clean Architecture debates; UX; game design; Superpowers/AgDR (other slices); inventing APIs; Design skill recommendations as product law; re-litigating whether ADRs exist (Theme 2 already established).
- Comprehension / research goal type (if code): other (process literature / documentation practice)

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | WebFetch (primary URLs + MADR 4.0.0 raw templates); Read (`docs/templates/research-note.md`, Theme 2 report §2.5 / related); Grep (Theme 2 ADR sections); research-protocol skill |
| Corpora / URLs searched | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions ; https://martinfowler.com/bliki/ArchitectureDecisionRecord.html ; https://adr.github.io/madr/ ; https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template.md ; https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-minimal.md ; https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-bare.md ; local `docs/research/reports/theme-2-agent-usable-documentation.md` |
| Queries (exact) | Direct URL fetches (no web search); Theme 2 path read for §2.5 reuse |
| What was *not* searched | Alexandria / RAG corpora; AWS Prescriptive Guidance ADR pages; Harmel-Law / Rowse–Shepherd examples on martinfowler.com; Medium MADR stories; Design Practice Repository; scientific MADR paper PDF; adr-tools beyond Fowler’s mention; AgDR / Superpowers; agent HITL books; vendor Plan Mode docs |
| Depth | deep |
| Waves / stop_reason | wave: 1 (slice T5A-S1). stop_reason: N/A for gatherer slice — Wave 1 primary fetch complete for assigned URLs; diminishing-returns / track stop owned by coordinator/integrator |
| Provenance (optional PROV) | Entity←Nygard 2011 blog, Fowler ADR bliki, MADR site + 4.0.0 templates, Theme 2 integrated report §2.5; Activity=T5A-W1-S1 gather; Agent=WebFetch+local read |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Slice is primary-source documentation practice, not workspace recon |
| Scope boundary | Named primary URLs + Theme 2 report path only |

## 4. Findings

### 4.1 Theme 2 reuse (do not re-litigate ADR existence)

- `FACT` [E2] Theme 2 already records ADR/MADR as the **decision log** layer: one architecturally significant decision + status lifecycle; MADR optional YAML; still prose; job is “why the system is the way it is” and supersession history. [E2: Theme 2 report §2 layer table + §2.5 — `docs/research/reports/theme-2-agent-usable-documentation.md` — accessed 2026-07-29]
- `FACT` [E2] Theme 2 §2.5 summary of Nygard sections: Title, Context, Decision, Status, Consequences; ~1–2 pages; Markdown in repo; sequential numbers; retain superseded; status proposed / accepted / deprecated / superseded. [E2: same path §2.5]
- `FACT` [E2] Theme 2 §2.5 summary of MADR: lean Markdown template; optional YAML (status, date, decision-makers, …); full sections include Context/Problem, Drivers, Options, Outcome, Pros/Cons. [E2: same path §2.5]
- `FACT` [E2] Theme 2 separates artifact roles: requirements/questions vs ADR decisions vs implementation notes. [E2: Theme 2 report §1 exec summary + §4.x artifact roles table — same path]
- `FACT` [E2] Theme 2 ADR lifecycle repeat: `proposed` / `accepted` / `deprecated` / `superseded` (keep old records); agents must not treat `draft`/`proposed` as accepted SoT. [E2: Theme 2 report §4.2 — same path]

### 4.2 When to write an ADR

- `FACT` [E1] Nygard: keep records for **“architecturally significant”** decisions — those that affect structure, non-functional characteristics, dependencies, interfaces, or construction techniques. [E1: Michael Nygard, “Documenting Architecture Decisions” — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29]
- `FACT` [E1] Nygard: one ADR describes **one** significant decision for a specific project; something that affects how the rest of the project will run. [E1: Nygard 2011 — same URL]
- `FACT` [E1] Fowler: an ADR captures and explains a **single decision** relevant to a product or ecosystem. [E1: Martin Fowler, “Architecture Decision Record” — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-07-29]
- `FACT` [E1] MADR: an Architectural Decision (AD) is a justified software design choice addressing a functional or non-functional requirement of architectural significance; the ADR details a **single AD** and its rationale. MADR states not to take “architecture” too strongly — examples include technology, IDE, library, or feature choices with architectural impact; template is offered to capture **any** (important) decision. [E1: MADR About — https://adr.github.io/madr/ — accessed 2026-07-29]
- `GAP` Exact quantitative thresholds for “architecturally significant” (e.g. mandatory checklists) were not stated as a single shared rule across these three primaries. Searched: Nygard, Fowler, MADR overview. Result: definitional guidance only; significance debates acknowledged by MADR without a universal cutoff.

### 4.3 Required / common sections (options, tradeoffs, decision, consequences)

- `FACT` [E1] Nygard format parts: **Title** (short noun phrase); **Context** (forces — technological, political, social, project-local — value-neutral); **Decision** (response in full sentences, active voice, “We will …”); **Status**; **Consequences** (resulting context; list **all** consequences — positive, negative, and neutral). [E1: Nygard 2011 — Cognitect URL]
- `FACT` [E1] Fowler: records should contain the **decision**, the **context**, and significant **ramifications**; also a brief **rationale** summarizing the problem and **trade-offs**; valuable to **explicitly list serious alternatives** with **pros and cons**; consequences may warrant an explicit section; optional to record **confidence** and context changes that should trigger reevaluation. [E1: Fowler ADR bliki]
- `FACT` [E1] MADR 4.0.0 **full** template body sections include: Context and Problem Statement; Decision Drivers (optional); Considered Options; Decision Outcome (chosen option + because justification); Consequences (optional subsection; Good/Bad framing); Confirmation (optional); Pros and Cons of the Options (per option: Good / Neutral / Bad); More Information (optional). Optional YAML frontmatter: status, date, decision-makers, consulted, informed. [E1: https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template.md — accessed 2026-07-29; also rendered on https://adr.github.io/madr/]
- `FACT` [E1] MADR 4.0.0 **minimal** template keeps: title; Context and Problem Statement; Considered Options; Decision Outcome; Consequences (Good/Bad). [E1: https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-minimal.md — accessed 2026-07-29]
- `FACT` [E1] MADR site example shows lean body: Context and Problem Statement; Considered Options; Decision Outcome (chosen option + because). [E1: https://adr.github.io/madr/ — Example]
- `CLAIM` [E1] Nygard’s original five-part template does **not** include a dedicated “Considered Options” / pros-cons section; alternatives appear as forces in Context rather than a structured options matrix. Fowler and MADR make alternatives/pros-cons more explicit. [E1: compare Nygard 2011 vs Fowler bliki vs MADR templates — same URLs]
- `INFERENCE` [E4] For a design process that must record **options + tradeoffs + decision + consequences**, MADR’s Considered Options + Pros/Cons + Decision Outcome + Consequences (or Fowler’s explicit alternatives advice layered on Nygard’s Decision/Consequences) is the process-relevant shape; Nygard alone is decision-centric with forces in Context. Premises: (1) FACT Nygard sections; (2) FACT Fowler alternatives/pros-cons; (3) FACT MADR full/minimal sections.

### 4.4 Status lifecycle and supersession

- `FACT` [E1] Nygard status values: **proposed** (stakeholders not yet agreed); **accepted** (agreed); if later ADR changes/reverses: **deprecated** or **superseded** with a reference to its replacement. Keep the old record; do not reuse numbers. [E1: Nygard 2011]
- `FACT` [E1] Fowler: status **proposed** while under discussion; **accepted** once the team accepts it and it is active; **superseded** once significantly modified or replaced — with a link to the superseding ADR. Once accepted, an ADR should **never be reopened or changed** — instead supersede — so there is a clear log of decisions and how long they governed. [E1: Fowler ADR bliki]
- `FACT` [E1] MADR optional status string examples: `proposed | rejected | accepted | deprecated | … | superseded by ADR-0123`. [E1: MADR 4.0.0 full template frontmatter]
- `FACT` [E1] Fowler and Nygard agree: do not rewrite history in place when the decision changes — keep prior record and point to the new one. [E1: Nygard 2011; Fowler ADR bliki]
- `OPEN` Whether Toolbelt should adopt Nygard’s `deprecated` vs Fowler’s narrower triad vs MADR’s inclusion of `rejected` / “superseded by ADR-NNNN” wording as the house vocabulary. Follow-up: T5A integrator / acceptance — not locked by this draft note.

### 4.5 Brevity, storage, numbering

- `FACT` [E1] Nygard: whole document should be **one or two pages**; write as a conversation with a future developer; full sentences; bullets only for visual style. Lightweight markup (Markdown or Textile). Path example: project repository `doc/arch/adr-NNN.md`. Numbers sequential and monotonic; not reused. [E1: Nygard 2011]
- `FACT` [E1] Fowler: short — typically a **single page**; inverted-pyramid style (most important first); supporting material linked, not inlined. Common location `doc/adr`; each record its own file; monotonic sequence in filename plus name capturing the decision (e.g. `0001-HTMX-for-active-web-pages`). Markdown for read/diff like code. [E1: Fowler ADR bliki]
- `FACT` [E1] MADR: aim to make writing and versioning decisions easy; initialize `docs/decisions`; filename pattern `NNNN-title-with-dashes.md`; large projects may categorize via subdirectories (numbers then local to category). [E1: https://adr.github.io/madr/]
- `FACT` [E1] MADR 4.0.0 (2024-09-17) publishes “bare” and “minimal” templates alongside the full template. [E1: MADR News on https://adr.github.io/madr/; bare file fetched at https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-bare.md]
- `GAP` Canonical single repo path (`doc/arch` vs `doc/adr` vs `docs/decisions`) is not unified across primaries. Searched: three primaries. Result: competing conventional locations; choice is project meta-decision.

### 4.6 Purpose of writing (human process; agent implications only as INFERENCE)

- `FACT` [E1] Fowler: writing ADRs serves as a **record** for later understanding and as a **thinking aid** that surfaces differing points of view for discussion/resolution. [E1: Fowler ADR bliki]
- `FACT` [E1] Nygard motivation: avoid blind acceptance or blind reversal of past decisions by making motivation and consequences visible as teams change. [E1: Nygard 2011]
- `FACT` [E2] Theme 2 INFERENCE (reused, not expanded as lock): ADR/MADR are dual — human decision log; for agents, high-signal **rationale (why)** complementary to `AGENTS.md` (how to operate). [E2: Theme 2 §2.5 — same path]
- `INFERENCE` [E4] For human+agent design processes, ADRs that include **status**, **chosen option + because**, **alternatives with pros/cons**, and **consequences** are more agent-usable than decision-only prose, because retrieval can surface why/not-why without treating draft/proposed as law. Premises: (1) Theme 2 §2.5 / §4.2 status discipline; (2) Fowler alternatives + confidence/reevaluation cues; (3) MADR Options/Outcome/Consequences structure; (4) Nygard/Fowler immutability-via-supersession. **Not** a Design skill or MVP lock.

## 5. Hypothesis log (optional)

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Process spine for T5A can treat Nygard core (Context/Decision/Status/Consequences) + explicit options/tradeoffs (Fowler/MADR) as complementary, not competing standards | open | E1 overlap on decision/context/consequences/supersession; E1 divergence on options section and status vocabulary |
| H2 | Agent-usable ADR practice = same human ADR atoms + status filtering (exclude draft/proposed from SoT) | open | Theme 2 E2; no primary in this slice states an agent-specific ADR schema |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Status vocabulary | Nygard: proposed / accepted / deprecated / superseded | Fowler: proposed / accepted / superseded (immutable once accepted); MADR adds rejected + “superseded by ADR-…” | Prefer cite-all; leave house choice **OPEN**; Theme 2 E2 currently mirrors Nygard quartet |
| Options/pros-cons section | Nygard: forces in Context; no dedicated Options | Fowler recommends listing alternatives + pros/cons; MADR templates include Considered Options (+ Pros/Cons in full) | Complementary; for options/tradeoffs recording prefer Fowler/MADR atoms |
| Length | Nygard: 1–2 pages | Fowler: typically single page | Both require brevity; no conflict on “short” |
| Default folder | Nygard `doc/arch/` | Fowler `doc/adr`; MADR `docs/decisions` | **GAP**/project choice; not locked |

## 7. Gaps & OPEN

- `GAP` No primary in this slice defines an agent-native ADR schema, machine-required fields, or HITL gate mapping (propose → critique → accept). Searched: Nygard, Fowler, MADR site/templates. Result: human/team process docs only.
- `GAP` Unified default repository path and numbering uniqueness under categorization not settled by primaries.
- `OPEN` House status enum: Nygard quartet vs Fowler triad vs MADR (incl. rejected / superseded-by pointer).
- `OPEN` Whether MADR “Confirmation” / “decision-makers|consulted|informed” RACI-like YAML should be required, optional, or omitted for Toolbelt — primaries mark them optional.
- `OPEN` Wave 2+ slices: Superpowers/AgDR, agent HITL literature, vendor Plan Mode — explicitly out of this slice.

## 8. Implications (INFERENCE only)

Label clearly. Do **not** promote to design lock without separate acceptance.

- `INFERENCE` [E4] A human+agent design process that needs to record options, tradeoffs, decision, and consequences should treat ADR/MADR as the **decision-record artifact** (one decision per file; short; versioned with code; supersede rather than silently rewrite), and should prefer templates that make **Considered Options + tradeoffs (pros/cons) + Decision Outcome + Consequences + Status** first-class. Premises: §4.2–4.5 FACTs; Theme 2 §2.5 E2.
- `INFERENCE` [E4] Agents consuming ADRs should weight **accepted** records for rationale and treat **proposed/draft** as non-SoT; superseded records remain historical context via links. Premises: Fowler immutability-via-supersession; Theme 2 §4.2; Nygard retain-superseded.
- `INFERENCE` [E4] This note does **not** authorize writing Design skills or locking Toolbelt ADR path/status enum — draft gatherer output only (`draft-is-not-sot`). Premises: Method status draft; campaign brief non-goal.

## 9. Source list (deduped)

1. Michael Nygard — Documenting Architecture Decisions — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-29
2. Martin Fowler — Architecture Decision Record — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-07-29
3. MADR — Markdown Architectural Decision Records — https://adr.github.io/madr/ — accessed 2026-07-29
4. MADR 4.0.0 full template — https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template.md — accessed 2026-07-29
5. MADR 4.0.0 minimal template — https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-minimal.md — accessed 2026-07-29
6. MADR 4.0.0 bare template — https://raw.githubusercontent.com/adr/madr/4.0.0/template/adr-template-bare.md — accessed 2026-07-29
7. Theme 2 — Agent-Usable Documentation (integrated) §2.5 / §4.2 — `docs/research/reports/theme-2-agent-usable-documentation.md` — accessed 2026-07-29
