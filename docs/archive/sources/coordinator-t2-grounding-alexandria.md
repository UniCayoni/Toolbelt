# Coordinator notes — Theme 2 grounding (Alexandria)

Date: 2026-07-27  
Agent: parent coordinator  
Method: `rag_probe` + `rag_query` on corpus `ai_llm_agents`  
Protocol: `docs/research/PROTOCOL.md`

## Queries

1. `RAG citation attribution grounding faithfulness prevent hallucination evidence provenance in answers` (k=12)

## Findings

- **FACT [E2]** RAG reduces hallucinations by grounding answers in retrieved evidence rather than model parameters alone. [Alexandria `ai_llm_agents` / Deepak Dhyani *RAG with Python Cookbook* / cited chunks on grounding]
- **FACT [E2]** **Cited answer / cited response prompting**: require explicit source IDs or short quotes tied to retrieved docs; increases transparency and verifiability. [same; recipes on cited answer chain / cited response prompting]
- **FACT [E2]** **Confidence-aware prompting**: model should express certainty, flag gaps, or say when answer cannot be found; pairs with similarity-based retrieval confidence. [Dhyani]
- **FACT [E2]** **Faithfulness (groundedness)**: ratio of answer claims inferable from context to total claims; decompose answer into atomic statements then judge support. [Polzer *RAG with Python Cookbook*; Raieli/Iuculano; Bratanic/Hane *Essential GraphRAG*]
- **CLAIM [E2]** Production heuristic often cited: aim faithfulness &gt; ~80%; &lt;~70% suggests systematic hallucination risk. [Polzer] — treat as book guidance, not a universal standard.
- **FACT [E2]** Faithfulness ≠ quality alone: pair with **answer relevancy** and **context precision**; metrics move independently. [Polzer]
- **FACT [E2]** **Structured output prompting** (JSON/tables/schemas) reduces ambiguity for downstream machine use. [Dhyani]
- **FACT [E2]** Evidence-highlighted prompting: extract/highlight supporting sentences for a query. [Dhyani]
- **INFERENCE [E4]** For GreyMatter research notes: require claim decomposition-friendly structure (atomic FACT bullets + citations) and explicit GAP/confidence markers — premises: faithfulness eval + confidence-aware prompting above.

## Gaps

- **GAP**: No single industry-standard citation *schema* for agent research notes found in this query (formats vary: `[1]`, source IDs, quotes).
- **GAP**: Academic primary papers on attribution (e.g. specific ACL papers) not fetched this pass — OPEN for integrator.

## Source list

- Deepak Dhyani — RAG with Python Cookbook (Alexandria)
- Dominik Polzer — RAG with Python Cookbook (Alexandria)
- Raieli & Iuculano — Building AI Agents with LLMs, RAG, and Knowledge Graphs (Alexandria)
- Bratanic & Hane — Essential GraphRAG (Alexandria)
