# Theme 2 / Slice C — Anti-assumption, provenance, explicit uncertainty

Status: notes only (not integrated report)  
Agent id: `t2c-anti-assumption-provenance`  
Created: 2026-07-27  
Protocol: `docs/research/PROTOCOL.md`

## 1. Scope

Patterns that force **explicit uncertainty, provenance, and non-assumption** for research / agent-facing templates:

- Epistemic markers / uncertainty language in technical and scientific writing
- Provenance in research software and reproducible research (FAIR / FAIR4RS)
- “Sources of truth” hierarchies and competing-truth anti-patterns
- Separating requirements vs design vs implementation documentation
- Failure modes: agents treating drafts as facts; missing citations; scope creep from vibes
- Official / vendor guidance on “do not invent” APIs/facts and verification-before-claim

Out of scope for this note: GreyMatter product stub, RAG library locks, MVP feature scope.

## 2. Method (tools, queries, date)

**Date:** 2026-07-27

**Tools:**

| Tool | Use |
|------|-----|
| Alexandria `rag_query` | corpora `software_engineering`, `ai_llm_agents` |
| Web search / fetch | NIST AI RMF + GAI Profile; GO FAIR; FAIR4RS; OpenAI Model Spec + citation docs; Anthropic Constitution; Nygard ADR; CASRAI hedging; Cursor subagents docs |
| Local protocol | `d:\GreyMatter\docs\research\PROTOCOL.md` |

**Alexandria queries (representative):**

1. `software_engineering`: “provenance reproducibility sources of truth requirements vs design vs implementation documentation uncertainty epistemic markers”
2. `software_engineering`: “requirements specification vs design document vs implementation documentation single source of truth document hierarchy ADR architecture decision”
3. `software_engineering`: “vibe coding assumptions AI generated code review verify provenance outdated APIs trust AI output without testing”
4. `ai_llm_agents`: “do not invent APIs verification before claim hallucination grounding citations uncertainty provenance agent failure modes treating drafts as facts”
5. `ai_llm_agents`: “verify claims before stating do not invent APIs tools schemas ground answers in sources refuse when uncertain”

**Web primary targets:** NIST AI 100-1; NIST AI 600-1; go-fair.org; RDA FAIR4RS; openai/model_spec; OpenAI citation formatting; anthropic.com/constitution; cognitect.com ADR post; cursor.com/docs/subagents.

## 3. Findings

### 3.1 Epistemic markers / uncertainty language

- `FACT` [E1 / E2]: In research writing, **epistemic modality markers** qualify the writer’s commitment to a proposition (hedges vs boosters). Hedging is treated as a normal, necessary feature of scientific communication, not optional decoration. [E2: Vázquez & Giner, *RAEI* 21 (2008) — https://doi.org/10.14198/raei.2008.21.10 — accessed 2026-07-27] [E2: Lingard, *Perspectives on Medical Education* — https://pmejournal.org/articles/10.1007/S40037-019-00559-Y — accessed 2026-07-27]

- `FACT` [E2]: Practical hedging inventory commonly includes: modal verbs (*may/might/could*); epistemic lexical verbs (*suggest/indicate/appear/seem*); epistemic adverbs (*possibly/probably/likely*); approximators (*approximately/generally*). Over-stacking hedges is flagged as a mistake; under-hedging (overclaiming) is also flagged. [E2: CASRAI “Hedging in Academic Writing” — https://casrai.org/guides/hedging-in-academic-writing — accessed 2026-07-27] [E1: PMC review — https://pmc.ncbi.nlm.nih.gov/articles/PMC10151619/ — accessed 2026-07-27]

- `FACT` [E1]: OpenAI Model Spec ranks outcomes: **confident right > hedged right > no answer > hedged wrong > confident wrong**, and instructs assistants to express uncertainty when knowledge/reasoning/tools are insufficient; default language includes “I don’t know”, “I’m not sure”, “I think”, “It might be”. [E1: OpenAI Model Spec — https://github.com/openai/model_spec/blob/main/model_spec.md — section `express_uncertainty` — accessed 2026-07-27]

- `FACT` [E1]: Anthropic Constitution requires **calibrated** honesty: acknowledge uncertainty/lack of knowledge; avoid conveying more or less confidence than warranted. [E1: Anthropic “Claude’s Constitution” — https://www.anthropic.com/constitution — accessed 2026-07-27]

- `INFERENCE` [E4]: Research templates that force claim labels (`FACT`/`CLAIM`/`INFERENCE`/`GAP`/`OPEN`) and evidence grades are an operationalization of epistemic hedging for agent-written notes. Premises: (a) hedges exist to match wording to evidence strength [E2 CASRAI]; (b) GreyMatter protocol already requires those labels [E0: `PROTOCOL.md`].

### 3.2 Provenance in research software & reproducible research

- `FACT` [E1]: FAIR data principle **R1.2**: “(Meta)data are associated with detailed provenance.” [E1: GO FAIR principles — https://www.go-fair.org/fair-principles/ — accessed 2026-07-27]

- `FACT` [E1]: FAIR4RS **R1.2**: “Software is associated with detailed provenance.” Provenance metadata covers why/how software came to be, who contributed what/when/where; extends beyond VCS change logs; supports authenticity and trust. [E1: FAIR4RS Principles v1.0 — https://www.rd-alliance.org/system/files/FAIR4RS%20principles%20v1.0.pdf — accessed 2026-07-27]

- `FACT` [E2]: Research Software Engineering guidance for **code provenance** of an analysis: archive (1) analysis scripts/notebooks, (2) software environment description, (3) ordered data-processing steps; use persistent identifiers (DOI via Zenodo/GitHub release); distinguish **reproducibility** (short shelf-life exact re-run) from **inspectability** (enduring ability to see what was run and which decisions mattered). [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python...pdf` chunk_id=`02425b323121386cf89fa1ff` query=`"provenance reproducibility..."`] [E2: same source chunk_id=`b5853e13e66d118a3478fb93`] [E2: same source key points chunk_id=`245896ed8d8a34a06ee63e98`]

- `FACT` [E1]: NIST AI RMF: maintaining **provenance of training data** and attributing decisions to data subsets supports transparency and accountability; MEASURE should include **measures of uncertainty** with formalized reporting. [E1: NIST AI 100-1 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf — accessed 2026-07-27]

- `FACT` [E1]: NIST Generative AI Profile elevates **content provenance** as a primary consideration; inventory entries should include data provenance (source, signatures, versioning, watermarks); defines **confabulation** as confidently stated erroneous/false content; lists **information integrity** risks when content fails to distinguish fact/opinion/fiction or acknowledge uncertainties. [E1: NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf — accessed 2026-07-27]

- `CLAIM` [E2]: Chunk-level multi-source attribution through the retrieval→generation chain, plus explicit uncertainty communication when sources do not address a query, is a published pattern for transparent RAG systems. [E2: Alexandria corpus=`ai_llm_agents` source=`Design Patterns for Transparent RAG Systems.pdf` chunk_id=`811137196bb835f1886c1f4b` query=`"do not invent APIs..."`]

### 3.3 Sources-of-truth hierarchies

- `FACT` [E2]: Treating a live “model database” as schema truth **alongside** Git creates a **competing source of truth**; recommended pattern: schema (and reference data that is part of schema) lives in VCS as the single source of truth; no structural changes outside source control. [E2: Alexandria corpus=`software_engineering` source=`Unit Testing Principles, Practices, and Patterns...pdf` chunk_id=`2ba8415fb25d9e2b8d612185` query=`"provenance reproducibility..."`]

- `INFERENCE` [E4]: For research notes, a hierarchy should prevent drafts/chat vibes from outranking primary sources. Premises: (a) competing SoT is an anti-pattern in SE literature above; (b) NIST/FAIR treat provenance metadata as first-class; (c) agent confabulation risks inventing “authoritative” citations [E1 NIST AI 600-1; E2 Devlin RAG book]. Candidate hierarchy for templates (not product-locked):

  1. Local observation / tool output for this session (E0)
  2. Primary standards & official vendor docs (E1)
  3. Peer-reviewed / canonical textbooks & corpus chunks with path+chunk id (E1–E2)
  4. Secondary guides (E2)
  5. Community anecdotes (E3) — hypothesis only
  6. Model prior / “vibes” / undated chat drafts — never a SoT; must be labeled `U`/`OPEN` or omitted

### 3.4 Separating requirements vs design vs implementation docs

- `FACT` [E1]: Architecture Decision Records (Nygard): short, versioned records of **one** architecturally significant decision; sections Context / Decision / Status / Consequences; status lifecycle includes proposed → accepted → superseded (keep old records). Explicitly for decisions that affect structure, NFRs, dependencies, interfaces, construction techniques—not a dump of implementation detail. [E1: Michael Nygard, Cognitect — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — accessed 2026-07-27] [E1: Martin Fowler bliki — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html — accessed 2026-07-27]

- `FACT` [E2]: Classic waterfall phases still enumerate distinct artifacts even when process order is rejected: product requirements → models/rules → architecture outline → code → test → deploy. The invariant is **separation of concerns across document types**, not waterfall timing. [E2: Alexandria corpus=`software_engineering` source=`Clean Architecture with .NET...epub` chunk_id=`64a02120e1b3c1000c80f09f` query=`"requirements specification vs design..."`]

- `FACT` [E2]: “Definition of done” examples separate architectural design documentation updates from implementation/tests/user docs—signaling that design docs are not synonymous with code. [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition...pdf` chunk_id=`f41010b0c258a33ce7823f9c` query=`"requirements specification vs design..."`]

- `CLAIM` [E2]: Martin argues “architecture” vs “design” is not a hard ontological split at all levels; still, project practice commonly separates **what** (requirements), **why/decision** (ADR), and **how now** (implementation). Treat any absolute “design ≠ architecture” claim as contested. [E2: Alexandria corpus=`software_engineering` source=`Clean Architecture...Martin.pdf` chunk_id=`6df95f6ad286571fd8de38cd` query=`"requirements specification vs design..."`]

- `GAP`: No strong primary hit in this pass for an ISO/IEEE mandatory three-tier template (SRS vs SDD vs code) tailored to agent research notes. Open for follow-up (e.g., IEEE 29148 / 1016) if templates need standards IDs.

### 3.5 Failure modes (agents + research writing)

- `FACT` [E2]: LLM hallucination examples explicitly include **invented citations** and **nonexistent APIs/libraries**. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG...Devlin.pdf` chunk_id=`46acde20f77ec664012a1371` query=`"do not invent APIs..."`]

- `FACT` [E2]: In agentic systems, hallucinated content can drive **real-world actions** without human verification; mitigations include grounding, real-time verification, action validation, fallbacks when reliability is uncertain, uncertainty-aware decisions. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Agentic AI Systems.pdf` chunk_id=`38cde04ca3b1fe75d686de25` query=`"do not invent APIs..."`]

- `FACT` [E2]: Prompt pattern: use ONLY provided CONTEXT; if absent, say “Not enough information…”; critic must flag any claim lacking CONTEXT support. [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG...Devlin.pdf` chunk_id=`404e0d9bf9cb17c7c7483fcb` query=`"do not invent APIs..."`]

- `FACT` [E2]: Production guidance: do not guess when underspecified; escalate when grounding is insufficient rather than inventing. [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex...epub` chunk_id=`f6db83cbefcb3eb041e52205` query=`"verify claims before stating..."`]

- `FACT` [E2]: Faithfulness evaluation: decompose answer into claims and verify each against retrieved context; unsupported claims = hallucination signal. [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook...pdf` chunk_id=`5011051c80b358c733d60f72` query=`"do not invent APIs..."`]

- `FACT` [E2]: Vibe-coding literature: humans remain responsible; treat AI as intern—“trust but verify”; review AI output; verify provenance of suspiciously specific AI-generated code; AI-assisted engineering keeps requirements/blueprint ahead of improvisation. [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding...Osmani.epub` chunk_ids=`49b2ca032561247cddb762d0`, `514d2dd24d2d8e4639f44355`, `b3694eb5a09fea5097b333f0` queries as listed in Method]

- `CLAIM` [E3/E2]: Independent audits report fabrication (invented data/citations/math with false precision) as a dominant honesty failure even under constitutions that require calibrated uncertainty—reinforces that **policy alone is insufficient** without verification affordances. [E3/E2: Alignment Forum / arXiv SURF discussion of Anthropic constitution adherence — https://www.alignmentforum.org/posts/Tk4SF8qFdMrzGJGGw/how-well-do-models-follow-their-constitutions — accessed 2026-07-27; treat as contested relative to vendor claims]

- `INFERENCE` [E4]: “Treating drafts as facts” and “scope creep from vibes” map to: (1) missing status fields on docs (draft vs accepted); (2) missing SoT hierarchy; (3) improvisational vibe coding without requirements/ADR gates. Premises: ADR status lifecycle [E1 Nygard]; vibe vs AI-assisted engineering contrast [E2 Osmani]; NIST information-integrity risk when uncertainty is not acknowledged [E1 AI 600-1].

### 3.6 Official / vendor “do not invent” & verification-before-claim

- `FACT` [E1]: OpenAI citation formatting: **Never invent source IDs, line ranges, or block locators** not returned by tools; **Never invent new block IDs**; **Never cite outside knowledge or outside authorities** when citation mode is context-bound; cite conflicts explicitly when sources disagree. [E1: OpenAI API “Citation Formatting” — https://developers.openai.com/api/docs/guides/citation-formatting — accessed 2026-07-27]

- `FACT` [E1]: OpenAI Model Spec: reduce execution/factual errors via avoid-errors + express-uncertainty + stay-in-bounds; clarify uncertainty rather than deceive. [E1: OpenAI Model Spec — https://github.com/openai/model_spec/blob/main/model_spec.md — accessed 2026-07-27]

- `FACT` [E1]: Cursor docs describe a **verifier subagent** pattern: skeptical validation that claimed-complete work actually exists and works; run tests; do not accept claims at face value. [E1: Cursor Subagents — https://cursor.com/docs/subagents — accessed 2026-07-27]

- `FACT` [E1]: NIST MAP 2.2: document the AI system’s **knowledge limits** and how humans oversee outputs. [E1: NIST AI 100-1 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf — accessed 2026-07-27]

- `GAP`: No single official Cursor page titled “do not invent APIs” was found in this pass; closest E1 affordances are verifier subagent + general agent tool-use docs. Treat “do not invent APIs” as **widely attested failure mode** [E2 Devlin] plus **citation non-invention** [E1 OpenAI], not as a Cursor-branded statute.

## 4. Contradictions / conflicts found

1. **Architecture vs design:** Martin (Clean Architecture) downplays a sharp architecture/design split; ADR practice and waterfall-derived artifact lists assume a practical split among requirements / decisions / implementation. Prefer: keep **artifact roles** separate even if ontology is fuzzy.
2. **Vendor honesty vs empirical fabrication:** Anthropic Constitution demands calibrated uncertainty; SURF-style audits claim fabrication remains common. For templates: encode both the **norm** (E1 constitution/spec) and the **operational control** (cite-or-omit, verify, faithfulness checks)—do not assume model compliance.
3. **Reproducibility vs inspectability:** Exact bit-for-bit reproducibility decays; inspectable provenance remains valuable. Templates should require inspectability always; exact env freeze when claiming reproducibility.

## 5. Gaps

| ID | Gap | Searched |
|----|-----|----------|
| G1 | IEEE/ISO SRS–SDD–code triad not deeply retrieved this pass | Alexandria SE + web (ADR/Nygard/Fowler found; IEEE 29148/1016 not fetched) |
| G2 | W3C PROV-O / PROV-DM not fetched as primary | Web RDM results mentioned PROV extensions (PRAETOR) but no direct PROV-DM quote |
| G3 | Cursor-official “never invent APIs” wording | Cursor agent/subagents docs; no exact phrase found |
| G4 | Epistemic-marker standards for **software** docs (not academic papers) | Strong academic hedging literature; thinner SE-specific style guides in corpora |
| G5 | Quantitative thresholds for faithfulness (e.g., “>80%”) appear in cookbook literature | Treat as `CLAIM`/practice tip, not design lock |

## 6. Candidate patterns for templates (still cited)

Actionable constraints suitable for research-note / agent templates. Each remains cited; none are GreyMatter product features.

1. **Claim labeling mandatory** — Every non-trivial statement carries `FACT`/`CLAIM`/`INFERENCE`/`GAP`/`OPEN` + evidence grade. Aligns with epistemic hedging [E2 CASRAI; E1 OpenAI Model Spec] and local protocol [E0 PROTOCOL].

2. **Cite-or-omit** — No citation → no factual claim; never invent source IDs/authors/URLs. [E1 OpenAI citation formatting; E2 Devlin invented-citations failure mode]

3. **Context-only answering for grounded modes** — “Use ONLY provided CONTEXT; else state insufficient information.” [E2 Devlin critic/reviser prompts; E2 Transparent RAG P9]

4. **Method block required** — Tools, queries, date, corpora/URLs recorded per note (already PROTOCOL). Supports FAIR/FAIR4RS provenance intent [E1 GO FAIR; E1 FAIR4RS] and NIST documentation expectations [E1 AI RMF].

5. **Document status fields** — `draft` / `proposed` / `accepted` / `superseded` on every research or design artifact; agents must not treat `draft`/`proposed` as accepted SoT. [E1 Nygard ADR status lifecycle]

6. **Artifact role separation** — Distinct files/sections for: (a) requirements / questions, (b) design decisions (ADR-style: context/decision/consequences), (c) implementation notes / code pointers. Do not collapse into one “vibes doc.” [E1 Nygard; E2 Esposito waterfall steps as invariant roles]

7. **Sources-of-truth precedence table** — Explicit ranking (local observation → primary docs → peer literature → secondary → community → model prior). Competing SoT forbidden. [E2 Khorikov model-DB anti-pattern; E1 NIST provenance]

8. **Uncertainty ranking preference** — Prefer hedged truth or silence over confident falsehood. [E1 OpenAI Model Spec outcome ranking]

9. **Verification-before-claim for APIs/tools** — Before asserting an API/library/CLI flag exists: open schema, official docs, or local probe; else `GAP`/`OPEN`. [E2 Devlin nonexistent APIs; E1 Cursor verifier pattern; E2 Osmani trust-but-verify]

10. **Conflicting sources protocol** — When sources disagree, cite both and describe disagreement; do not silently pick one. [E1 OpenAI citation formatting]

11. **Inspectability minimum for analyses** — Scripts + env description + step order + PID where published. [E2 RSE with Python provenance chapter; E1 FAIR R1.2]

12. **Human/escalation gate on low grounding** — If retrieval/context insufficient for high-stakes claim, escalate or refuse rather than invent. [E2 LlamaIndex HITL; E2 Agentic AI Systems; E1 NIST knowledge limits MAP 2.2]

13. **Faithfulness self-check (optional template step)** — Decompose claims → check each against cited chunks before marking note complete. [E2 RAG Cookbook faithfulness]

14. **AI-assistance disclosure when relevant** — Note when AI drafted content that may need provenance review. [E2 Osmani transparency/attribution; E1 NIST content provenance]

## 7. Source list (deduped)

### Primary / official (E1)

- NIST, *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- NIST, *AI RMF: Generative Artificial Intelligence Profile*, NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf
- GO FAIR, FAIR Principles — https://www.go-fair.org/fair-principles/
- RDA FAIR4RS Working Group, *FAIR Principles for Research Software (FAIR4RS Principles) v1.0* — https://www.rd-alliance.org/system/files/FAIR4RS%20principles%20v1.0.pdf
- OpenAI Model Spec — https://github.com/openai/model_spec/blob/main/model_spec.md
- OpenAI, Citation Formatting — https://developers.openai.com/api/docs/guides/citation-formatting
- Anthropic, Claude’s Constitution — https://www.anthropic.com/constitution
- Michael Nygard, “Documenting Architecture Decisions” — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Martin Fowler, Architecture Decision Record — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
- Cursor Docs, Subagents (verifier pattern) — https://cursor.com/docs/subagents
- GreyMatter Research Protocol — `d:\GreyMatter\docs\research\PROTOCOL.md` (E0 for local rules)

### Secondary / corpus (E2)

- Irving et al., *Research Software Engineering with Python* (Alexandria `software_engineering`)
- Khorikov, *Unit Testing Principles, Practices, and Patterns* (Alexandria `software_engineering`)
- Osmani, *Beyond Vibe Coding* (Alexandria `software_engineering`)
- Esposito, *Clean Architecture with .NET* (Alexandria `software_engineering`)
- Silén, *Clean Code Principles and Patterns* (Alexandria `software_engineering`)
- Martin, *Clean Architecture* (Alexandria `software_engineering`)
- Devlin, *Building LLM Agents with RAG…* (Alexandria `ai_llm_agents`)
- *Design Patterns for Transparent RAG Systems* (Alexandria `ai_llm_agents`)
- Polzer, *RAG with Python Cookbook* (Alexandria `ai_llm_agents`)
- *Building Agentic AI Systems* (Alexandria `ai_llm_agents`)
- Gheorghiu, *Building Data-Driven Applications with LlamaIndex* (Alexandria `ai_llm_agents`)
- Funderburk, *Building Natural Language and LLM Pipelines* (Alexandria `ai_llm_agents`)
- CASRAI, Hedging in Academic Writing — https://casrai.org/guides/hedging-in-academic-writing
- Lingard, “The academic hedge…” — https://pmejournal.org/articles/10.1007/S40037-019-00559-Y
- Vázquez & Giner (2008) — https://doi.org/10.14198/raei.2008.21.10
- OpenAIRE / FAIR how-to (provenance under Reusable) — http://www.openaire.eu/how-to-make-your-data-fair

### Community / contested (E3)

- Alignment Forum / SURF discussion of constitution adherence — https://www.alignmentforum.org/posts/Tk4SF8qFdMrzGJGGw/how-well-do-models-follow-their-constitutions
