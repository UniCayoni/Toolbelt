# Theme 2 Slice A — Grounding, Citation, Attribution, Faithfulness

Status: notes only (not integrated report)  
Created: 2026-07-27  
Agent: t2a-grounding-citation-rag

## 1. Scope

How to keep LLM/agent answers **grounded**: citations, attribution, evidence spans, faithfulness, and anti-hallucination patterns from RAG/GraphRAG and agent literature.

Focus questions:

1. What citation formats work for machines vs humans?
2. How should docs encode provenance so agents don't fill gaps with assumptions?
3. What evaluation notions (faithfulness, citation precision) matter for research notes?

Out of scope (per PROTOCOL): plugin stubs, locking RAG/GraphRAG library choices, MVP feature scope.

## 2. Method

| Item | Detail |
|------|--------|
| Date | 2026-07-27 |
| Protocol | `d:\GreyMatter\docs\research\PROTOCOL.md` |
| Alexandria MCP | `user-alexandria-rag` |
| Primary corpus | `ai_llm_agents` (71 docs / 22,720 chunks; active index `v1`) |
| Tools | `list_corpora` → `rag_probe` → `rag_query` → `rag_fetch_chunk` |
| Probe questions | (1) citation/attribution/grounding/faithfulness; (2) provenance metadata; (3) RAGAS faithfulness/citation precision; (4) GraphRAG provenance; (5) negative rejection / insufficient evidence |
| Probe verdicts | (1) partial; (2) partial; (3) **strong**; (4) partial; (5) used via `rag_query` |
| Web primary (E1) | RAGAS docs (faithfulness, context precision); ALCE arXiv/ACL; AIS / Rashkin et al.; Azure AI Content Safety groundedness; Azure OpenAI Assistants file search annotations |
| Web secondary | Synthesis pages used only as pointers; claims below cite E1/E2 |

Searched but weakly covered in Alexandria for *machine-checkable evidence-span schemas* (char offsets, quote hashes): see Gaps.

## 3. Findings

### 3.1 Citation formats: machines vs humans

- **FACT (E1)** — ALCE formalizes long-form answers as statements with per-statement citation lists, using boxed numeric markers such as `[1][2]`. Systems must retrieve passages, generate answers, and cite supporting passages; each statement may cite multiple passages (capped at three in their experiments).  
  [E1: Gao et al., ALCE / EMNLP 2023 — https://ar5iv.labs.arxiv.org/html/2305.14627 — accessed 2026-07-27]

- **FACT (E1)** — ALCE instruction templates require citing for any factual claim, using `[1][2][3]`, at least one and at most three documents per sentence, and a minimum sufficient subset when multiple documents support a sentence. That pattern is optimized for **automatic** NLI-based citation checks (machines), while remaining readable to humans.  
  [E1: ALCE paper Appendix instructions — https://ar5iv.labs.arxiv.org/html/2305.14627 — accessed 2026-07-27]

- **FACT (E1)** — Vendor Assistants / file-search APIs return **structured annotations** (`file_citation`, `file_id`, filename) alongside message text; client code replaces annotation placeholders with human-facing `[index]` markers and a citation list. Machines consume the annotation objects; humans see inline markers + filenames.  
  [E1: Azure OpenAI Assistants file search — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/file-search — accessed 2026-07-27]

- **CLAIM (E2)** — Practitioner RAG cookbooks describe “cited response prompting” / “cited answer chains”: assign stable IDs to retrieved docs, inject `doc_id + text` into context, and prompt the model to answer with `[1]`, `[2]`-style markers. Useful pattern; evidence grade is secondary (book recipes, not a peer-reviewed standard).  
  [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook Learn principles of RAG with LLM and agentic AI, with 120+ recipes (English Edition) (Deepak Dhyani)...pdf` chunk_id=`68dfe8a137e1819b57d6e4c4` / `db1ec52be1a9e9d7bcdbf486` / `de417837b9a4f499627e85f9` query=`"How do RAG systems cite sources..."`]

- **CLAIM (E2)** — Transparent-RAG design patterns argue **document-level** citations are too coarse for claim verification; prefer **chunk-level** provenance retained through chunking → embedding → retrieval → generation, with metadata: source, chunk, page/content, URL, timestamp, and hyperlinks for human verification.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Design Patterns for Transparent RAG Systems.pdf` chunk_id=`811137196bb835f1886c1f4b` query=`"provenance metadata source attribution"`]

- **INFERENCE (E4)** — Premises: (P1) ALCE uses numeric passage IDs + NLI over cited passages; (P2) vendors expose structured `file_id` annotations; (P3) transparent-RAG patterns push chunk-level metadata. Therefore dual-layer citations work best: **machine layer** = stable IDs + optional quote/offset payload; **human layer** = short inline markers + titles/URLs/quotes.  
  Premises from E1 ALCE, E1 Azure file search, E2 Transparent RAG patterns above.

### 3.2 Provenance encoding so agents don’t fill gaps

- **FACT (E1)** — AIS (Attributable to Identified Sources) defines attribution as verifying that NLG output about the external world is supported by an **independent, provided source**—not by the model’s parametric memory alone.  
  [E1: Rashkin et al., Measuring Attribution in NLG Models — https://arxiv.org/abs/2112.12870 — ACL Anthology https://aclanthology.org/2023.cl-4.2/ — accessed 2026-07-27]

- **CLAIM (E2)** — Context-grounded prompting: instruct the model to answer **only** from retrieved documents; treat the prompt as a guardrail against speculation. Confidence-aware prompting: express certainty, flag gaps, or say the answer cannot be found.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook... (Deepak Dhyani)...pdf` chunk_id=`e5e1a719dd2653b15baee2e9` / `53131aa8568aaf65b39f65aa` query=`"negative rejection refuse answer when evidence insufficient"`]

- **CLAIM (E2)** — **Negative rejection**: when retrieval fails to find appropriate context, models that still answer produce hallucinations; stricter prompts that allow refusal, plus query rewriting (e.g. HyDE), are prescribed mitigations. RGB benchmark explicitly scores rejection rate.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Building AI Agents with LLMs, RAG, and Knowledge Graphs...pdf` chunk_id=`536a5a965cd8b9a2492e2324`; source=`A Simple Guide to Retrieval Augmented Generation...pdf` chunk_id=`229f6f848dc5f578ff7e146e` query=`"negative rejection..."`]

- **CLAIM (E2)** — Enterprise vector/RAG guidance: encode governance metadata on sources and embeddings—e.g. `authoritative`, `status=current|draft|deprecated`, stable `source_document_id`, embedding model version, creation timestamp. Retrieval policies should **exclude** draft/deprecated docs and, if no authoritative source is available, return **insufficient evidence** rather than generate from incomplete context.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Vector Databases for Enterprise AI... (Emma McGrattan)...pdf` chunk_id=`ad3091f0e811b1d396f42cf1` / neighbor `45fc31f4e94d03bad258da6c` query=`"document provenance metadata"`]

- **CLAIM (E2)** — Agent literature: provenance/integrity for agent data includes lineage (origin, transforms), timestamps, source IDs, cryptographic hashes/signatures; immutable/append-only logs support audit. Vague prompts invite the model to fill gaps.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Building Applications with AI Agents... (Michael Albada)...pdf` chunk_id=`780fb7c0c4af5ff4e71cea5d`; source=`Agentic Mesh...pdf` chunk_id=`3882173e32b14e57682ec8a2` / `b8745e0586fdcaad9df23fb0` query=`"provenance... agents"`]

- **CLAIM (E2)** — Agentic Mesh-style policies as executable natural-language constraints: e.g. “Do not generate or insert factual claims not present in the source data.” Purpose/policies should be machine-readable *and* human-auditable.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Agentic Mesh...pdf` chunk_id=`b8745e0586fdcaad9df23fb0`]

- **CLAIM (E2)** — LlamaIndex-style node relationships can encode provenance (where a node originated, how nodes connect) to support source tracing during query.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Building Data-Driven Applications with LlamaIndex...epub` chunk_id=`5937e4239c929487ebd6ad78` query=`"provenance"`]

- **CLAIM (E2)** — GraphRAG adds relational/entity context beyond passages (“RAG finds facts; GraphRAG explains how facts fit together”), but hybrid designs still combine graph triples with textual passages for generation—citations should cover both structured and unstructured evidence.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG, Knowledge Graphs, and Reflection...pdf` chunk_id=`89728d682e9efffbb605e0f1`; source=`Building AI Agents with LLMs, RAG, and Knowledge Graphs...pdf` chunk_id=`d67f112ce613ad5cdde53229` query=`"GraphRAG evidence provenance"`]

- **INFERENCE (E4)** — Premises: (P1) AIS requires identified sources; (P2) retrieval policies can force “insufficient evidence”; (P3) confidence/negative-rejection patterns exist. Therefore provenance for agents should mark **coverage gaps explicitly** (missing fields, draft status, low retrieval score) rather than omit them—omission is what invites parametric fill-in.  
  Premises from E1 AIS + E2 Vector DB / RAG cookbook chunks above.

### 3.3 Evaluation notions that matter for research notes

- **FACT (E1)** — **Faithfulness** (RAGAS): fraction of claims in the response that can be inferred from `retrieved_contexts`; score in [0,1]. Procedure: decompose response into claims → check each against context → supported/total. Distinct from “correct vs world”; it is “supported by retrieved context.”  
  [E1: RAGAS Faithfulness docs — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/ — accessed 2026-07-27]

- **FACT (E1)** — **Context precision** (RAGAS): evaluates whether relevant chunks are ranked above irrelevant ones among `retrieved_contexts` (precision@k style aggregation). Variants exist with/without reference answers, and ID-based precision comparing retrieved vs reference context IDs.  
  [E1: RAGAS Context Precision docs — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/ — accessed 2026-07-27]

- **FACT (E1)** — ALCE **citation recall**: for each statement, at least one citation and NLI entailment of the statement from the concatenated cited passages (aligned with AIS). **Citation precision**: penalize irrelevant citations (citation does not support statement *and* removing it does not hurt support). Prioritizes recall for truthfulness; precision for reviewer burden. Automatic metrics show substantial/moderate agreement with humans (Cohen’s κ ≈ 0.70 recall, ≈ 0.53 precision in their study).  
  [E1: ALCE — https://ar5iv.labs.arxiv.org/html/2305.14627 — accessed 2026-07-27]

- **FACT (E1)** — Azure AI Content Safety **groundedness detection** classifies whether LLM text is grounded in provided `groundingSources` (QnA or Summarization; Medical/Generic domains); optional reasoning mode and correction. English-optimized; separate from citation-quality metrics.  
  [E1: Azure groundedness concepts — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness — accessed 2026-07-27]

- **CLAIM (E2)** — Practitioner summaries of RAG eval converge on a triad: context relevance / answer faithfulness / answer relevance; plus abilities such as noise robustness, negative rejection, information integration, counterfactual robustness (RGB). GraphRAG eval books apply RAGAS faithfulness + context recall + answer correctness and interpret high faithfulness + lower recall as “not inventing, but missing evidence.”  
  [E2: Alexandria corpus=`ai_llm_agents` source=`A Simple Guide to Retrieval Augmented Generation...pdf` chunk_id=`85e57440ca38a8efd4ed56c4` / `48a0f8d6f2bfa8504ef492c6`; source=`Essential GraphRAG...pdf` chunk_id=`3809cbdd14d030b1ae2097c7` / `6f70389d0294fd7f378f63b9`; source=`RAG with Python Cookbook (Dominik Polzer)...pdf` chunk_id=`e0d6789e356f89dd30b6e1bd`; source=`Building Natural Language and LLM Pipelines...pdf` chunk_id=`4a7b977c97d31e3125acf8df` query=`"RAGAS faithfulness..."`]

- **INFERENCE (E4)** — Premises: (P1) PROTOCOL already requires evidence grades and claim labels; (P2) faithfulness checks support-from-context, not world truth; (P3) citation precision/recall check claim↔source links. For GreyMatter **research notes**, the operational notions that map cleanly are: **faithfulness** (no unsourced claims), **citation recall** (every factual claim has a supporting cite), **citation precision** (cites are necessary/relevant), plus **negative rejection** (refuse or label `GAP`/`U` when evidence is weak)—rather than optimizing answer “fluency” alone.  
  Premises: PROTOCOL E0–E4 + E1 RAGAS/ALCE + E2 RGB/negative rejection.

### 3.4 Anti-hallucination / grounding patterns (operational)

- **CLAIM (E2)** — Core pattern: retrieve → condition generation on evidence → cite → optionally verify. Agentic RAG may loop: generate → assess sufficiency → rewrite query / re-retrieve until confidence or budget stops.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`RAG with Python Cookbook... (Deepak Dhyani)...pdf` chunk_id=`7fa14a485552f5d2cfb406cb`]

- **CLAIM (E2)** — Evidence highlighting / extractive spans before or beside generation improves transparency; structured JSON outputs improve machine parseability of claims and citations.  
  [E2: Alexandria `ai_llm_agents` Dhyani cookbook chunks `1354a7a409b199b16bb16d99`, `db1ec52be1a9e9d7bcdbf486`]

- **CLAIM (E2)** — Transparent RAG P9: default prompt language such as “Sources do not directly address this…” when gaps exist.  
  [E2: Alexandria `Design Patterns for Transparent RAG Systems.pdf` chunk_id=`811137196bb835f1886c1f4b`]

- **CLAIM (E2)** — Production monitoring suggestions include tracking Recall@k, groundedness, hallucination rate, and logging each generated claim with supporting context for audit.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Building LLM Agents with RAG, Knowledge Graphs, and Reflection...pdf` chunk_id=`11ee4eff7e99e9451c20cb0d`]

## 4. Contradictions / conflicts found

1. **Faithfulness vs answer correctness** — High faithfulness with incomplete retrieval can still yield wrong answers relative to ground truth (GraphRAG book example: faithfulness ~0.97 vs lower correctness/recall). Conflict is definitional, not factual error: do not treat faithfulness as end-to-end truth.  
   [E2: Essential GraphRAG chunk `3809cbdd14d030b1ae2097c7`]

2. **Citation precision definitions** — ALCE automatic precision can false-penalize “partial support” citations; human schemes (Liu et al., discussed in ALCE) allow partial support. Conflict: stricter machine NLI vs human partial-credit.  
   [E1: ALCE limitations sections — https://ar5iv.labs.arxiv.org/html/2305.14627]

3. **Human vs machine citation goals** — ALCE notes humans often prefer redundant citations for credibility; precision metrics that punish redundancy can fight UX.  
   [E1: ALCE citation precision design notes]

4. **Parametric vs context preference** — RAG literature reports models sometimes prefer strong parametric beliefs over conflicting retrieved context unless prompts are strict. Conflict for grounding policy design.  
   [E2: Raieli/Iuculano chunk `536a5a965cd8b9a2492e2324`]

## 5. Gaps

- **GAP** — No strong Alexandria hit for a standardized **evidence-span schema** (char offsets, quote hashes, page+bbox) as a first-class interchange format across tools. Vendor annotations are file-level; ALCE is passage-level; Transparent RAG wants chunk-level—but a single portable schema is not established in retrieved material.
- **GAP** — Limited primary coverage in this pass of **Microsoft GraphRAG** paper’s own citation conventions (corpus discusses GraphRAG generally; Microsoft-specific citation UX not probed deeply).
- **GAP** — OpenAI Responses API citation/`index` semantics noted in community threads; not treated as E1 here (forum = E3). Prefer official OpenAI docs in a follow-up.
- **GAP** — No local GreyMatter runtime observation of citation UX (E0) in this pass—notes are literature-only.
- **OPEN** — Should GreyMatter research notes require quote-level spans, or is passage/`chunk_id` + grade enough for integrator merge?
- **OPEN** — Should agents emit dual payloads (human markdown + machine JSON claims[]) by default?

## 6. Candidate patterns for templates (still cited)

Candidate conventions for agent-facing research notes / answer envelopes (not locked):

### C1 — Dual citation layer

| Layer | Format | Purpose |
|-------|--------|---------|
| Machine | Stable IDs: `corpus`, `source_rel_path` or `doc_id`, `chunk_id`, optional `char_start`/`char_end` or quote | Deterministic fetch / NLI / RAGAS-style checks |
| Human | Inline `[n]` or PROTOCOL-style `[E#: Title — URL — date]` plus short quote | Verification by readers |

Aligned with ALCE numeric cites + Azure annotations + PROTOCOL Alexandria citation form.  
[E1: ALCE; E1: Azure file search; E0: PROTOCOL.md]

### C2 — Claim object (structured)

```text
claim_id | claim_text | support: [evidence_ref...] | status: supported|partial|unsupported|insufficient_evidence | confidence: high|medium|low
```

Supports faithfulness-style claim decomposition and ALCE statement-level citation.  
[E1: RAGAS faithfulness; E1: ALCE]

### C3 — Provenance fields on source docs / chunks

Minimum useful metadata suggested by enterprise RAG guidance:

- `source_id`, `uri`/`path`, `title`
- `version` / `content_hash`, `retrieved_at` / `published_at`
- `status`: `current` | `draft` | `deprecated`
- `authoritative`: bool
- `chunk_id`, `page` (if any), `heading_path`
- For GraphRAG: `entity_ids` / `triple_ids` when structured evidence is used

Policy: if no `authoritative=current` hit for regulated questions → emit insufficient evidence, do not answer from parametric knowledge.  
[E2: McGrattan Vector Databases chunk `ad3091f0e811b1d396f42cf1`; E2: GraphRAG hybrid chunks]

### D — Anti-assumption / gap encoding in prose

Mirror PROTOCOL labels in generated answers:

- Supported factual statements → `FACT` + citation  
- Weak / secondary → `CLAIM`  
- Logical step → `INFERENCE` + premises  
- Searched, not found → `GAP`  
- Needs follow-up → `OPEN`  
- Plausible but unevidenced → `U` / refuse  

Plus explicit refusal language when retrieval confidence is low (confidence-aware / negative rejection).  
[E0: PROTOCOL.md; E2: Dhyani confidence-aware + Kimothi/RGB negative rejection]

### E — Eval checklist for research-note quality

| Metric | Question it answers | Prefer when |
|--------|---------------------|-------------|
| Faithfulness | Are claims supported by cited/retrieved context? | Always for grounded notes |
| Citation recall | Does every factual statement have supporting cite(s)? | Always |
| Citation precision | Are cites relevant/necessary? | When citation spam is a risk |
| Context precision / recall | Did retrieval surface the right evidence? | Diagnosing wrong answers that are still “faithful” |
| Negative rejection / GAP rate | Does the agent refuse or label when evidence is missing? | Anti-hallucination |
| Answer correctness (vs gold) | Is it true in the world / gold set? | Separate from faithfulness |

[E1: RAGAS; E1: ALCE; E2: RGB summary in Kimothi]

### F — Prompt / policy skeleton (candidate)

```text
Use only provided sources. Cite every factual claim with source IDs.
If sources are insufficient, say so (insufficient_evidence) — do not invent.
Prefer quotes or evidence spans for contested claims.
Separate observation from inference.
```

[E2: context-grounded + Agentic Mesh policy examples; E1: ALCE instructions]

## 7. Source list (deduped)

### E0 — Local

- `d:\GreyMatter\docs\research\PROTOCOL.md` (observed 2026-07-27)
- Alexandria `list_corpora` / probe / query / fetch via MCP `user-alexandria-rag` (2026-07-27)

### E1 — Primary web

- Gao, Yen, Yu, Chen — *Enabling Large Language Models to Generate Text with Citations* (ALCE), EMNLP 2023 — https://ar5iv.labs.arxiv.org/html/2305.14627 — https://aclanthology.org/2023.emnlp-main.398.pdf
- Rashkin et al. — *Measuring Attribution in Natural Language Generation Models* (AIS) — https://arxiv.org/abs/2112.12870 — https://aclanthology.org/2023.cl-4.2/
- RAGAS Faithfulness — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
- RAGAS Context Precision — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/
- Azure AI Content Safety groundedness — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness
- Azure OpenAI Assistants file search (annotations) — https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/file-search

### E2 — Alexandria `ai_llm_agents` (selected)

- Dhyani — *RAG with Python Cookbook* (cited answer / confidence / context-grounded / evidence highlighting)
- Polzer — *RAG with Python Cookbook* (faithfulness LLM-as-judge recipe)
- Kimothi — *A Simple Guide to Retrieval Augmented Generation* (RAGAS triad, RGB abilities)
- Bratanic & Hane — *Essential GraphRAG* (RAGAS eval, faithfulness prompts)
- Funderburk — *Building Natural Language and LLM Pipelines* (Ragas four metrics)
- Bouchard & Peters — *Building LLMs for Production* (Ragas metrics example)
- McGrattan — *Vector Databases for Enterprise AI* (retrieval policy, lineage, insufficient evidence)
- Albada — *Building Applications with AI Agents* (data provenance/integrity; GraphRAG)
- Broda — *Agentic Mesh* (policies: no claims absent from source data)
- Gheorghiu — *Building Data-Driven Applications with LlamaIndex* (node provenance relationships)
- Devlin — *Building LLM Agents with RAG, Knowledge Graphs, and Reflection* (GraphRAG hybrid; audit logging claims)
- Raieli & Iuculano — *Building AI Agents with LLMs, RAG, and Knowledge Graphs* (GraphRAG steps; negative rejection)
- *Design Patterns for Transparent RAG Systems.pdf* (multi-level attribution, uncertainty communication)

### Not used as strong claims

- Community forum threads on Responses API citation `index` (E3 only; flagged OPEN)
)
