# Theme 2 — Agent-Usable Documentation

**Date:** 2026-07-27  
**Status:** integrated  
**Protocol:** `docs/research/PROTOCOL.md`

## Sources (merged)

| ID | Path | Role |
|----|------|------|
| N-T2A | `docs/research/notes/theme-2/t2a-grounding-citation-rag.md` | Grounding, citation, faithfulness |
| N-T2B | `docs/research/notes/theme-2/t2b-agent-doc-formats.md` | Doc formats & structures |
| N-T2C | `docs/research/notes/theme-2/t2c-anti-assumption-provenance.md` | Anti-assumption, provenance, uncertainty |
| C-T2G | `docs/research/sources/coordinator-t2-grounding-alexandria.md` | Coordinator Alexandria grounding |
| C-WEB | `docs/research/sources/coordinator-web-agent-doc-formats.md` | Coordinator web formats (llms.txt / AGENTS.md) |
| C-T2P | `docs/research/sources/coordinator-t2-provenance-rse.md` | Coordinator RSE provenance |

Integrator method: merge notes only; no new research; conflicts resolved by higher evidence grade; remaining conflicts and all `GAP`/`OPEN` retained.

---

## 1. Executive summary

- Agent-usable docs are **layered**: discovery (`llms.txt`), repo behavior (`AGENTS.md` / tool-specific rules), human IA (Diátaxis), decision rationale (ADR/MADR), and machine contracts (OpenAPI / JSON Schema)—not one file format. [N-T2B; C-WEB]
- Prefer **short always-on instructions** plus **retrieval/tools** for large knowledge; stuffing full wikis into system prompts fights context limits. [N-T2B E1 OpenAI Agents SDK; E1 llmstxt.org]
- Research notes should use a **dual citation layer**: machine-stable IDs (`corpus` / `source` / `chunk_id`, optional spans) + human inline markers / PROTOCOL-style citations. [N-T2A E4 from ALCE + Azure annotations + Transparent RAG]
- Operational eval notions for notes: **faithfulness**, **citation recall**, **citation precision**, plus **negative rejection** / `GAP` when evidence is weak—not fluency alone. Faithfulness ≠ world truth. [N-T2A E1 RAGAS/ALCE; C-T2G]
- Provenance for agents must mark **coverage gaps and doc status** (`draft`/`current`/`deprecated`); omission invites parametric fill-in. [N-T2A E4; N-T2C status fields]
- **Cite-or-omit** and **never invent** source IDs, line ranges, APIs, or authorities not returned by tools/docs. [N-T2C E1 OpenAI citation formatting; E2 invented citations]
- Prefer **hedged right or silence** over confident wrong (OpenAI Model Spec ranking); claim labels + evidence grades operationalize epistemic hedging. [N-T2C E1 Model Spec; E0 PROTOCOL]
- Sources-of-truth hierarchy: E0 local observation → E1 primary → E1–E2 literature → E2 secondary → E3 community → model prior never as SoT. Competing SoTs are an anti-pattern. [N-T2C E4; E2 Khorikov]
- Separate artifact roles: requirements/questions vs ADR decisions vs implementation notes—do not collapse into one “vibes” doc. [N-T2C; N-T2B ADR]
- RSE provenance triad for inspectability: scripts/notebooks + environment description + ordered steps; exact re-runability decays, inspectability endures. [N-T2C; C-T2P]
- Portable SoT for coding agents: `AGENTS.md`; Claude imports via `@AGENTS.md`; Cursor adds `.mdc` only when activation metadata is needed. Nested merge algorithms differ across tools—do not assume one. [N-T2B]
- No industry-standard portable **evidence-span schema** or mandatory AGENTS.md/llms.txt YAML schema found; quote-level spans vs chunk_id remain **OPEN**. [N-T2A; N-T2B; C-T2G; C-WEB]

---

## 2. Documentation layer model

Orientation: **human-oriented**, **agent-oriented**, or **dual**. Layers are complementary.

| Layer | Format | Orientation | Primary job | Machine-parseable? | When to use |
|-------|--------|-------------|-------------|--------------------|-------------|
| Discovery index | `llms.txt` (+ optional `.md` / ctx expand) | Agent-oriented (Markdown dual-readable) | Curated site/doc index for LLM inference under context limits | Spec is Markdown with fixed order; parsers/CLI exist | Public docs sites; packaging “what to read” |
| Repo instructions | `AGENTS.md` | Agent-oriented | Build/test/style/boundaries for coding agents | Freeform Markdown; **no** required schema | Cross-tool in-repo agent ops; complements human README |
| Runtime activation | Cursor `.cursor/rules/*.mdc`; Claude `CLAUDE.md` / `.claude/rules/` | Agent-oriented | Conditional / scoped / always-on prompt injection | YAML frontmatter for when/paths | Tool-specific activation; keep portable ops in `AGENTS.md` |
| Human doc IA | Diátaxis (tutorials / how-tos / reference / explanation) | Human-oriented framework | Separate writing modes for four user needs | No machine schema | Structuring *what* humans (and retrieving agents) need; not an agent file convention |
| Decision log | ADR (Nygard) / MADR | Dual | One architecturally significant decision + status lifecycle | MADR optional YAML; still prose | Why the system is the way it is; supersession history |
| Tool/API contracts | OpenAPI / JSON Schema | Machine-first | Parameters & I/O for tools and APIs | Yes | Tool calling, validation, generated clients—not narrative onboarding |
| Human entry | README / CONTRIBUTING | Human-oriented | Humans first; agents may fall back | Usually no | Marketing / contribution UX; keep agent ops out when possible |

### 2.1 `llms.txt` (llmstxt.org) — FACT [E1]

- Markdown at `/llms.txt` (or optional subpath): concise, expert-oriented guidance and links instead of scraping HTML. Motivated by small context windows. [N-T2B; C-WEB]
- Spec order: optional BOM → **H1 name (only required section)** → optional blockquote summary → zero+ non-heading detail sections → zero+ **H2 sections of file lists**; items `[name](url)` plus optional `: notes`. [N-T2B; C-WEB]
- H2 named **`Optional`**: URLs may be skipped when shorter context is needed. [N-T2B; C-WEB]
- Companion practice: clean Markdown twins (URL + `.md`); tooling such as `llms_txt2ctx`; complementary to `robots.txt` / `sitemap.xml`; mainly **inference**-time. [N-T2B; C-WEB]
- **INFERENCE [E4]** — Discovery layer for **published documentation**, not a substitute for in-repo coding instructions. [N-T2B]
- **CLAIM [E3]** (coordinator) — Complementary framing: `AGENTS.md` = how to work *in this repo*; `llms.txt` = where to find accurate *dependency/docs* indexes. Treat as CLAIM until a primary states it. [C-WEB]

### 2.2 `AGENTS.md` — FACT [E1]

- Open format: “README for agents” for build steps, tests, conventions that would clutter a human README; no required schema. [N-T2B; C-WEB]
- Sample sections: Dev environment tips, Testing instructions, PR instructions. [N-T2B]
- Cursor: plain markdown alternative to `.cursor/rules`; no metadata/globs; root + nested; combine with parents, **more specific take precedence**. [N-T2B]
- Claude Code reads **`CLAUDE.md`**, not `AGENTS.md`; recommend `@AGENTS.md` import or symlink. [N-T2B]
- Nested / nearest-file precedence is a common pattern; exact merge algorithms differ by tool. [N-T2B; C-WEB]
- Stewardship messaging under Agentic AI Foundation / Linux Foundation appears on agents.md materials—verify if used for legal claims. [C-WEB]
- Codex layered discovery / ~32 KiB cap: reported via secondary/search; **OPEN** to reconfirm on primary (308 this research pass). [N-T2B]

### 2.3 Cursor / Claude / OpenAI — “docs as context” — FACT [E1]

- **Cursor:** Rules inject persistent context; modes via frontmatter (always / description / globs / manual `@`); best practices include &lt;500 lines, split rules, concrete examples, `@` file refs; Team → Project → User precedence. Plain `.md` under `.cursor/rules` is ignored. [N-T2B]
- **Claude Code:** `CLAUDE.md` + auto memory every session as **context, not enforced config** (use hooks to block); target &lt;200 lines; path-scoped rules with YAML `paths`; load order managed → user → project → local; closer later. [N-T2B]
- **OpenAI Agents SDK:** Local `RunContextWrapper.context` (not sent to LLM) vs LLM context via history; tactics: Agent `instructions`, run `input`, function tools, retrieval/web search. [N-T2B]
- **INFERENCE [E4]** — Prefer short always-on instructions + tools/retrieval for large docs. Premises: SDK split + llms.txt context motivation. [N-T2B]

### 2.4 Diátaxis — FACT [E1] (from N-T2B; coordinator Diátaxis fetch was GAP/OPEN)

| Type | Need |
|------|------|
| Tutorial | Practical **lesson** (learning experience) |
| How-to | Directions for a **competent** user achieving a real goal |
| Reference | Accurate technical **facts**, propositional |
| Explanation | Discursive **understanding**, “tell me about…” |

**INFERENCE [E4]** — Human authoring/architecture; agents benefit when retrieval surfaces the *right type*. Not itself an agent file format. [N-T2B]  
Coordinator pass timed out on diataxis.fr; N-T2B recovered via HTTP—prefer N-T2B E1 for Diátaxis facts. [C-WEB GAP vs N-T2B FACT]

### 2.5 ADR / MADR — FACT [E1]

- **Nygard:** Title, Context, Decision, Status, Consequences; ~1–2 pages; Markdown in repo; sequential numbers; retain superseded. Status: proposed / accepted / deprecated / superseded. [N-T2B; N-T2C]
- **MADR:** Lean Markdown template; optional YAML (status, date, decision-makers, …); full sections include Context/Problem, Drivers, Options, Outcome, Pros/Cons. [N-T2B]
- **INFERENCE [E4]** — Dual: human decision log; for agents, high-signal **rationale** (why) complementary to `AGENTS.md` (how to operate). [N-T2B]
- Coordinator SE corpus ADR hit was thin; prefer Nygard/MADR primaries. [C-T2P]

### 2.6 OpenAPI / JSON Schema — FACT [E1]

- OpenAPI Description is JSON/YAML; Schema Objects relate to JSON Schema (OAS 3.1+ aligned with Draft 2020-12 concepts). [N-T2B]
- OpenAI function tools: JSON schema for parameters → structured tool call → execute → return. [N-T2B]
- **INFERENCE [E4]** — Contract layer for callable tools; narrative reference should stay consistent, but schemas win for validation. [N-T2B]
- **GAP** — No primary asserting OpenAPI *as* AGENTS.md replacement; different layers. [N-T2B]

### 2.7 Frontmatter vs freeform — FACT / INFERENCE

- Use frontmatter when the **runtime** needs activation metadata (Cursor/Claude rules; MADR optional YAML). [N-T2B]
- Keep portable agent instructions as plain Markdown (`AGENTS.md`, `llms.txt`). [N-T2B; C-WEB]
- Use schemas for executable contracts. [N-T2B]
- Community “under 150 lines” for AGENTS.md is **CLAIM [E3]**, not a single primary standard. [N-T2B]
- Formal JSON Schema for AGENTS.md / llms.txt intentionally absent; any strict template would be local convention only. [N-T2B]
- Full AGENTS.md “v1.1” frontmatter proposal is GitHub issue discussion—not ratified. [C-WEB]

### 2.8 Integrator when-to-use cheat sheet

| Need | Prefer |
|------|--------|
| Public docs discovery under context limits | `llms.txt` + `.md` pages |
| Cross-tool repo coding instructions | `AGENTS.md` |
| Cursor-only conditional/scoped rules | `.cursor/rules/*.mdc` |
| Claude path-scoped / memory | `CLAUDE.md` + `.claude/rules/` (import AGENTS.md) |
| Human doc IA / writing quality | Diátaxis types |
| Decision rationale history | ADR/MADR |
| Tool/API I/O enforcement | JSON Schema / OpenAPI |
| Large knowledge on demand | Retrieval/tools, not always-on paste |

---

## 3. Citation & grounding conventions for agent research notes

### 3.1 Dual citation layer — INFERENCE [E4] from E1/E2

| Layer | Format | Purpose |
|-------|--------|---------|
| Machine | Stable IDs: `corpus`, `source_rel_path` or `doc_id`, `chunk_id`; optional `char_start`/`char_end` or quote | Deterministic fetch / NLI / faithfulness-style checks |
| Human | Inline `[n]` or PROTOCOL-style `[E#: Title — URL — date]` plus short quote | Reader verification |

Aligned with: ALCE numeric passage cites + NLI checks [E1]; Azure Assistants structured `file_citation` / `file_id` annotations with human `[index]` replacement [E1]; Transparent RAG chunk-level provenance metadata [E2]; PROTOCOL Alexandria citation form [E0]. [N-T2A]

**Related FACTS:**

- ALCE: long-form answers as statements with per-statement citation lists (`[1][2]`); retrieve → generate → cite; cite factual claims; typically 1–3 docs per sentence; minimum sufficient subset. Optimized for automatic NLI citation checks while remaining human-readable. [N-T2A E1]
- Practitioner “cited response prompting”: stable IDs in context; answer with `[1]`/`[2]` markers. [N-T2A E2; C-T2G E2]
- Document-level cites are too coarse for claim verification; prefer chunk-level provenance through the pipeline (source, chunk, page/content, URL, timestamp). [N-T2A E2]

### 3.2 Claim objects (structured) — candidate pattern [N-T2A]

```text
claim_id | claim_text | support: [evidence_ref...] | status: supported|partial|unsupported|insufficient_evidence | confidence: high|medium|low
```

Supports faithfulness-style claim decomposition (RAGAS) and ALCE statement-level citation. [N-T2A E1]  
Structured JSON/tables/schemas reduce ambiguity for machine use; evidence highlighting improves transparency. [N-T2A E2; C-T2G E2]

### 3.3 Provenance fields on sources / chunks — CLAIM [E2] + INFERENCE [E4]

Minimum useful metadata (enterprise RAG guidance):

- `source_id`, `uri`/`path`, `title`
- `version` / `content_hash`, `retrieved_at` / `published_at`
- `status`: `current` | `draft` | `deprecated`
- `authoritative`: bool
- `chunk_id`, `page` (if any), `heading_path`
- GraphRAG: `entity_ids` / `triple_ids` when structured evidence is used

Policy pattern: if no authoritative/current hit for regulated questions → emit insufficient evidence; do not answer from parametric knowledge. [N-T2A E2]  
AIS: attribution means output about the external world is supported by an **independent, provided source**—not parametric memory alone. [N-T2A E1]

### 3.4 Grounding / anti-hallucination operational patterns

| Pattern | Summary | Grade |
|---------|---------|-------|
| Context-grounded prompting | Answer only from retrieved docs | E2 [N-T2A; C-T2G] |
| Confidence-aware prompting | Express certainty, flag gaps, or refuse | E2 [N-T2A; C-T2G] |
| Negative rejection | When retrieval fails, refuse rather than invent; RGB scores rejection | E2 [N-T2A] |
| Transparent RAG P9 | Default language when sources do not address the query | E2 [N-T2A; N-T2C] |
| Agentic Mesh-style policy | “Do not generate factual claims not present in source data” | E2 [N-T2A] |
| Retrieve → condition → cite → optionally verify; agentic loop on sufficiency | Core grounding loop | E2 [N-T2A] |
| GraphRAG hybrid | Cite both structured (triples/entities) and unstructured passages | E2 [N-T2A] |

**INFERENCE [E4]** — Mark coverage gaps explicitly (missing fields, draft status, low retrieval score); omission invites parametric fill-in. Premises: AIS + insufficient-evidence policies + confidence/negative-rejection. [N-T2A]

### 3.5 Evaluation notions for research notes

| Metric | Question | Prefer when | Grade |
|--------|----------|-------------|-------|
| **Faithfulness** (RAGAS) | Are claims inferable from retrieved/cited context? Score [0,1]; decompose → check support | Always for grounded notes | E1 [N-T2A] |
| **Citation recall** (ALCE) | Every statement has ≥1 citation and NLI entailment from cited passages (AIS-aligned) | Always | E1 [N-T2A] |
| **Citation precision** (ALCE) | Cites are necessary/relevant (penalize irrelevant) | When citation spam is a risk | E1 [N-T2A] |
| **Context precision** (RAGAS) | Relevant chunks ranked above irrelevant | Diagnosing wrong-but-“faithful” answers | E1 [N-T2A] |
| **Negative rejection / GAP rate** | Refuse or label when evidence missing | Anti-hallucination | E2 [N-T2A] |
| **Answer correctness** (vs gold/world) | Is it true outside the retrieved set? | Separate from faithfulness | E1/E2 [N-T2A] |
| Azure groundedness detection | Classifies grounding in provided `groundingSources` | Vendor monitoring path | E1 [N-T2A] |

Practitioner triad: context relevance / answer faithfulness / answer relevance; RGB abilities include noise robustness, negative rejection, information integration, counterfactual robustness. High faithfulness + lower recall can mean “not inventing, but missing evidence.” [N-T2A E2; C-T2G]

**CLAIM [E2]** — Production heuristic “faithfulness &gt; ~80% / &lt;~70% risk” appears in cookbook literature; not a universal standard; do not design-lock. [C-T2G; N-T2C G5]

**INFERENCE [E4]** — For GreyMatter research notes, map cleanly to: faithfulness + citation recall + citation precision + negative rejection / `GAP`/`U`—rather than optimizing fluency alone. Premises: PROTOCOL labels + RAGAS/ALCE + RGB. [N-T2A; C-T2G]

Automatic ALCE metrics: substantial/moderate human agreement (κ ≈ 0.70 recall, ≈ 0.53 precision in their study). [N-T2A E1]

---

## 4. Anti-assumption / provenance constraints

### 4.1 Sources-of-truth hierarchy — INFERENCE [E4] (candidate, not product-locked)

| Rank | Source class | Grade band | Role |
|------|--------------|------------|------|
| 1 | Local observation / tool output for this session | E0 | Hard fact for machine/session |
| 2 | Primary standards & official vendor docs | E1 | Strong claim |
| 3 | Peer-reviewed / canonical textbooks & corpus chunks with path+chunk id | E1–E2 | Strong–soft |
| 4 | Secondary guides | E2 | Soft; prefer linking to primary |
| 5 | Community anecdotes | E3 | Hypothesis / caveat only |
| 6 | Model prior / “vibes” / undated chat drafts | — | **Never a SoT**; label `U`/`OPEN` or omit |

Competing SoT anti-pattern: e.g. live “model database” as schema truth alongside Git—schema/reference data that is part of schema should live in VCS as single SoT. [N-T2C E2 Khorikov]

### 4.2 Document status fields — FACT [E1] ADR + CLAIM [E2] retrieval policy

- ADR lifecycle: `proposed` / `accepted` / `deprecated` / `superseded` (keep old records). [N-T2C; N-T2B]
- Retrieval/governance metadata pattern: `status=current|draft|deprecated`, `authoritative`, stable `source_document_id`, timestamps; exclude draft/deprecated; insufficient evidence if no authoritative source. [N-T2A E2]
- **Constraint:** agents must not treat `draft`/`proposed` as accepted SoT. [N-T2C candidate pattern]

### 4.3 Cite-or-omit & non-invention — FACT [E1]

OpenAI citation formatting:

- Never invent source IDs, line ranges, or block locators not returned by tools
- Never invent new block IDs
- Never cite outside knowledge/authorities when citation mode is context-bound
- Cite conflicts explicitly when sources disagree

[N-T2C E1]

Failure modes attested in literature: invented citations; nonexistent APIs/libraries; hallucinated content driving real-world agent actions without verification. [N-T2C E2]  
Cursor closest E1 affordance: **verifier subagent** (skeptical validation, run tests, do not accept claims at face value)—not a Cursor page titled “do not invent APIs.” [N-T2C]

### 4.4 Uncertainty & epistemic markers

- Scientific hedging (modals, epistemic verbs/adverbs, approximators) matches wording to evidence strength; over- and under-hedging are both errors. [N-T2C E1/E2]
- OpenAI Model Spec outcome ranking: **confident right > hedged right > no answer > hedged wrong > confident wrong**; express uncertainty when knowledge/tools insufficient. [N-T2C E1]
- Anthropic Constitution: calibrated honesty—acknowledge uncertainty; avoid over/under-confidence. [N-T2C E1]
- NIST AI RMF: provenance of training data; MEASURE should include measures of uncertainty. [N-T2C E1]
- NIST AI 600-1: content provenance; **confabulation** = confidently stated erroneous content; information-integrity risk when fact/opinion/fiction or uncertainties are not distinguished. [N-T2C E1]
- **INFERENCE [E4]** — PROTOCOL claim labels + evidence grades operationalize epistemic hedging for agent-written notes. [N-T2C]

Mirror PROTOCOL labels in generated answers:

| Label | Use |
|-------|-----|
| `FACT` | Supported factual statements + citation (E0–E2) |
| `CLAIM` | Weak / secondary / contested |
| `INFERENCE` | Logical step + premises |
| `GAP` | Searched, not found / weak coverage |
| `OPEN` | Needs follow-up |
| `U` | Plausible but unevidenced — refuse or omit |

[N-T2A; N-T2C; E0 PROTOCOL]

### 4.5 Research software / FAIR provenance — FACT [E1/E2]

- FAIR R1.2: (meta)data associated with detailed provenance. [N-T2C E1 GO FAIR]
- FAIR4RS R1.2: software associated with detailed provenance (why/how, who/what/when/where; beyond VCS logs). [N-T2C E1]
- RSE code provenance triad: (1) analysis scripts/notebooks, (2) software environment description, (3) ordered data-processing steps; PIDs (e.g. DOI) when published; env capture examples (`pip freeze`, `conda env export`). [N-T2C; C-T2P]
- Reproducibility (exact re-run) has short shelf-life; **inspectability** endures. [N-T2C; C-T2P]
- Open science ≠ reproducible research ≠ sustainable software—related but distinct. [C-T2P]
- Method block required (tools, queries, date, corpora/URLs)—already PROTOCOL; supports FAIR/FAIR4RS intent and NIST documentation expectations. [N-T2C]

### 4.6 Artifact role separation

| Role | Typical artifact | Notes |
|------|------------------|-------|
| What / questions | Requirements / research questions | Not implementation dump |
| Why / decision | ADR/MADR (context, decision, consequences, status) | One significant decision per record |
| How now | Implementation notes / code pointers | Distinct from design decisions |

Classic phase lists still enumerate distinct artifacts even when waterfall timing is rejected—invariant is **separation of concerns across document types**. [N-T2C E2]  
Architecture vs design ontology is contested (Martin); keep **artifact roles** separate even if ontology is fuzzy. [N-T2C conflict]

### 4.7 Candidate constraint checklist (cited; not product-locked)

1. Claim labeling mandatory + evidence grade [N-T2C; PROTOCOL]
2. Cite-or-omit; never invent IDs/authors/URLs [N-T2C E1 OpenAI]
3. Context-only answering for grounded modes; else insufficient information [N-T2C E2; N-T2A]
4. Method block required [PROTOCOL; FAIR/NIST]
5. Document status fields; drafts not accepted SoT [N-T2C; Nygard]
6. Artifact role separation [N-T2C]
7. Explicit SoT precedence table; competing SoT forbidden [N-T2C]
8. Prefer hedged truth or silence over confident falsehood [N-T2C E1 Model Spec]
9. Verification-before-claim for APIs/tools/schemas (probe or `GAP`/`OPEN`) [N-T2C]
10. Conflicting sources: cite both; describe disagreement [N-T2C E1 OpenAI]
11. Inspectability minimum for analyses [N-T2C; C-T2P]
12. Human/escalation gate on low grounding / high-stakes claims [N-T2C; NIST MAP 2.2]
13. Optional faithfulness self-check before marking note complete [N-T2C; N-T2A]
14. AI-assistance disclosure when relevant for provenance review [N-T2C]

---

## 5. Conflicts table

| ID | Topic | Positions | Resolution (higher grade / policy) |
|----|-------|-----------|--------------------------------------|
| C1 | Faithfulness vs answer correctness | High faithfulness with incomplete retrieval can still be wrong vs gold [E2 GraphRAG books] | Definitional: do **not** treat faithfulness as end-to-end truth; pair with context recall/correctness when diagnosing. Prefer E1 RAGAS definition. |
| C2 | Citation precision (machine vs human) | ALCE auto precision can false-penalize partial support; human schemes may allow partial credit [E1 ALCE] | Keep both notions; for agents prefer machine NLI for audit, allow human partial-credit review notes. |
| C3 | Redundant citations | Humans may prefer redundant cites for credibility; precision metrics punish redundancy [E1 ALCE] | Dual layer: machine precision for checks; human layer may retain helpful redundant markers when UX needs them. |
| C4 | Parametric vs retrieved context | Models may prefer parametric beliefs over conflicting retrieved context unless prompts are strict [E2] | Grounded mode: context-only + refuse; cite conflicts when sources disagree [E1 OpenAI]. |
| C5 | Instruction file names | `AGENTS.md` vs `CLAUDE.md` vs `.cursor/rules/*.mdc` [E1 each] | Prefer `AGENTS.md` as portable SoT; Claude `@AGENTS.md`; Cursor AGENTS.md + `.mdc` only when globs/modes needed. |
| C6 | Nested precedence merge | Cursor: more specific wins; Claude: concatenate, closer last; Codex claimed root→cwd later override [E1 / OPEN] | Same *idea* (local wins); **do not assume one merge algorithm**. |
| C7 | Structured vs freeform | llms.txt/AGENTS.md freeform vs Cursor/Claude frontmatter vs OpenAPI schemas | Different layers: discovery / behavior / activation / I/O—not competing standards. |
| C8 | Diátaxis vs agent files | Human doc IA vs agent prompt files | Complementary, not competing. |
| C9 | Architecture vs design split | Martin softens split; ADR/practice keep artifact roles [E2/E1] | Keep artifact roles separate even if ontology is fuzzy. |
| C10 | Vendor honesty vs fabrication | Constitutions/specs demand calibrated uncertainty; audits claim fabrication remains common [E1 vs E3] | Encode **norm** (E1) and **controls** (cite-or-omit, verify, faithfulness)—do not assume model compliance. |
| C11 | Reproducibility vs inspectability | Exact re-run decays; inspectability endures [E2 RSE] | Require inspectability always; exact env freeze when claiming reproducibility. |
| C12 | Diátaxis fetch coverage | Coordinator: GAP/OPEN on diataxis.fr timeout; N-T2B: E1 via HTTP | Prefer N-T2B E1 Diátaxis facts; retain coordinator fetch fragility as method note. |
| C13 | Alexandria vs format specs | Alexandria weak/absent for llms.txt/AGENTS.md/Diátaxis [N-T2B] | Do not use Alexandria as evidence for those format specs; use web E1. |

---

## 6. Gaps & OPEN (deduped)

### Gaps

| ID | Gap | Source |
|----|-----|--------|
| G1 | No strong standardized **evidence-span schema** (char offsets, quote hashes, page+bbox) as portable interchange; vendor annotations often file-level; ALCE passage-level; Transparent RAG wants chunk-level | N-T2A; C-T2G |
| G2 | Limited primary coverage of Microsoft GraphRAG paper’s own citation UX conventions | N-T2A |
| G3 | OpenAI Responses API citation/`index` semantics only in community threads this pass (E3); prefer official docs follow-up | N-T2A |
| G4 | No GreyMatter-local E0 observation of citation UX or adopted format files | N-T2A; N-T2B |
| G5 | Direct WebFetch timeouts: agents.md site / diataxis.fr (partially recovered via raw README / HTTP) | N-T2B; C-WEB |
| G6 | ~~OpenAI Codex AGENTS.md guide HTTP 308; discovery/32 KiB details need primary re-fetch~~ **Closed secondary** — 32 KiB default + discovery order confirmed | N-T2B; sec-p0 |
| G7 | `llms-full.txt` / Mintlify naming: secondary blogs; confirm against llmstxt.org before treating as spec | N-T2B |
| G8 | Formal JSON Schema for AGENTS.md / llms.txt intentionally absent | N-T2B; C-WEB |
| G9 | IEEE/ISO SRS–SDD–code triad (e.g. IEEE 29148 / 1016) not deeply retrieved for agent research notes | N-T2C |
| G10 | W3C PROV-O / PROV-DM not fetched as primary | N-T2C |
| G11 | No Cursor-official page titled “do not invent APIs” | N-T2C |
| G12 | Epistemic-marker standards for **software** docs thinner than academic hedging literature | N-T2C |
| G13 | Quantitative faithfulness thresholds (e.g. &gt;80%) are cookbook CLAIM, not standard | N-T2C; C-T2G |
| G14 | ~~Lamprecht et al. 2020 primary not locked~~ **Closed secondary** — Lamprecht 2020 + FAIR4RS v1.0 fetched; prefer FAIR4RS v1.0 for normative R-principles | C-T2P; sec-elevation |
| G15 | Academic AIS/ALCE-class papers: coordinator pass noted some ACL primaries not fetched there; N-T2A did fetch ALCE/AIS—prefer N-T2A for those | C-T2G vs N-T2A |

### OPEN

| ID | Question | Source |
|----|----------|--------|
| O1 | ~~Should GreyMatter research notes require quote-level spans…?~~ **Closed [E4]:** chunk_id+grade (+ locator) enough; spans optional | N-T2A; sec-p1 |
| O2 | ~~Should agents emit dual payloads by default?~~ **Closed [E4]:** markdown default; `claims[]` optional for merge | N-T2A; sec-p1 |
| O3 | Whether GreyMatter public docs should ship `/llms.txt` vs repo-only `AGENTS.md` (product decision, not evidenced) | N-T2B |
| O4 | Best mapping of Diátaxis types → RAG chunk metadata labels for agents | N-T2B |
| O5 | ~~Reconfirm Codex AGENTS.md layering / size caps~~ **Closed** — see secondary P0 | N-T2B; sec-p0 |
| O6 | AGENTS.md “v1.1” frontmatter proposals—not ratified; do not require | C-WEB |

---

## 7. Implications for GreyMatter templates

**INFERENCE only** — premises from merged E0–E2 above; **not** MVP locks, library locks, or plugin stubs (PROTOCOL out of scope).

1. **Layer templates separately** — skeletons for `llms.txt`, `AGENTS.md`, ADR/MADR, Cursor `.mdc` / Claude path rules, and tool JSON Schema should remain distinct files/roles rather than one mega-doc. Premises: §2 layer model [N-T2B].

2. **Research-note envelope** — Require PROTOCOL claim labels + evidence grades; dual citation (PROTOCOL/human + Alexandria machine IDs); optional claim-object fields (`support`, `status`, `confidence`); mandatory Method block. Premises: PROTOCOL + §3 + §4.3–4.4.

3. **Status + SoT table in every research/design artifact** — `draft|proposed|accepted|superseded|deprecated|current` as applicable; embed SoT precedence so drafts/chat cannot outrank E0/E1. Premises: §4.1–4.2.

4. **Grounded-mode policy text** — Context-only; cite every factual claim; on insufficient evidence emit `GAP`/`insufficient_evidence` / refuse; cite disagreements; never invent source IDs or APIs—verify via schema/docs/probe or leave OPEN. Premises: §3.4, §4.3, §4.7.

5. **Eval checklist for note quality** — Faithfulness, citation recall, citation precision, negative-rejection/`GAP` rate; treat answer correctness vs gold as a separate check; do not lock numeric faithfulness thresholds. Premises: §3.5.

6. **Inspectability for analyses** — When notes report runs/results: scripts + env description + ordered steps (+ PID if published). Premises: §4.5, C-T2P.

7. **Portable agent instructions** — Prefer `AGENTS.md` as shared SoT; tool-specific activation metadata only where required; document that nested merge semantics differ. Premises: §2.2, conflict C5–C6.

8. **Diátaxis as retrieval taxonomy (optional)** — If chunking human docs for agents, label tutorial/how-to/reference/explanation to improve routing—without treating Diátaxis as an agent file format. Premises: §2.4; OPEN O4.

---

## 8. Source index

### E0 — Local

- `d:\GreyMatter\docs\research\PROTOCOL.md` (observed 2026-07-27)
- Slice notes and coordinator sources listed in Sources table above
- Alexandria MCP observations recorded inside N-T2A / N-T2C / C-T2G / C-T2P (2026-07-27)

### E1 — Primary (selected)

| Source | Topic |
|--------|-------|
| https://llmstxt.org/ / index.md | llms.txt spec |
| https://raw.githubusercontent.com/agentsmd/agents.md/main/README.md ; https://agents.md/ | AGENTS.md |
| https://cursor.com/docs/rules.md | Cursor rules / AGENTS.md |
| https://cursor.com/docs/subagents | Verifier subagent |
| https://code.claude.com/docs/en/memory.md | CLAUDE.md / rules / AGENTS.md import |
| https://diataxis.fr/start-here/ ; /explanation/ | Diátaxis |
| https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Nygard ADR |
| https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | ADR bliki |
| https://adr.github.io/madr/ | MADR |
| https://openai.github.io/openai-agents-python/context/ | LLM vs local context |
| https://developers.openai.com/api/docs/guides/function-calling | JSON Schema tools |
| https://developers.openai.com/api/docs/guides/citation-formatting | Never invent citations |
| https://github.com/openai/model_spec/blob/main/model_spec.md | Express uncertainty ranking |
| https://www.anthropic.com/constitution | Calibrated honesty |
| https://spec.openapis.org/oas/latest.html | OpenAPI |
| Gao et al. ALCE (EMNLP 2023) — https://ar5iv.labs.arxiv.org/html/2305.14627 | Citation generation / precision / recall |
| Rashkin et al. AIS — https://arxiv.org/abs/2112.12870 | Attribution |
| RAGAS Faithfulness / Context Precision docs | Eval metrics |
| Azure groundedness; Azure Assistants file search | Groundedness / annotations |
| NIST AI 100-1; NIST AI 600-1 | Provenance, uncertainty, confabulation |
| GO FAIR; FAIR4RS v1.0 | Provenance principles |

### E2 — Alexandria / secondary (selected)

| Corpus / work | Topic |
|---------------|-------|
| `ai_llm_agents` — Dhyani, Polzer RAG cookbooks | Cited answers, confidence, faithfulness recipes |
| `ai_llm_agents` — Kimothi; Bratanic/Hane Essential GraphRAG; Raieli/Iuculano | RAGAS triad, RGB, GraphRAG |
| `ai_llm_agents` — Transparent RAG patterns; McGrattan Vector DBs; Albada; Broda Agentic Mesh; Devlin; Gheorghiu LlamaIndex | Provenance, policies, failure modes |
| `software_engineering` — Irving et al. RSE with Python | Code provenance triad, inspectability |
| `software_engineering` — Khorikov; Osmani; Esposito; Silén; Martin | SoT, vibe coding, doc roles |
| CASRAI / academic hedging literature | Epistemic markers |

### E3 / contested (do not drive locks)

- Community threads on Responses API citation `index` [N-T2A]
- Alignment Forum / SURF constitution-adherence discussion [N-T2C]
- Codex AGENTS.md details pending primary re-fetch [N-T2B]
- AGENTS.md v1.1 frontmatter GitHub issue [C-WEB]
- Secondary writeups on AGENTS.md ↔ llms.txt complementarity [C-WEB]

### Not used as strong claims for format specs

- Alexandria hits for llms.txt / AGENTS.md / Diátaxis (low-signal / absent) [N-T2B]
- Ciceri et al. ADR mention-only [C-T2P]

---

*End of Theme 2 integrated report. No plugin stub. No MVP locks. Remaining `GAP`/`OPEN`/`U` retained explicitly.*
