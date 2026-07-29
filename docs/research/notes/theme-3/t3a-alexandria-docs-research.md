# Theme 3A — Critically researching / evaluating software documentation (Alexandria)

Status: notes only (not integrated report)  
Agent: t3a-alexandria-docs-research  
Date: 2026-07-27  
Corpora: `software_engineering`, `ai_llm_agents`

---

## 1. Scope

From Alexandria corpora `software_engineering` and `ai_llm_agents`: practices and pitfalls for **critically researching and evaluating software documentation itself** — outdated docs, verifying docs against code/tests, documentation quality, docs-driven development, RAG-over-docs pitfalls, and agent use of documentation.

Out of scope for this note: GreyMatter plugin stub; locking RAG library choices; MVP feature scope.

---

## 2. Method

| Item | Detail |
|------|--------|
| Tools | MCP `user-alexandria-rag`: `GetMcpTools` → `rag_probe` → `rag_query` (k≥10) → `rag_fetch_chunk` (neighbors 0–1 for high-value) |
| Date | 2026-07-27 |
| Corpora | `software_engineering`, `ai_llm_agents` only |
| Protocol | `d:\GreyMatter\docs\research\PROTOCOL.md` (incl. E3 as discovery channel for docs limitations; not design locks alone) |

### Probes (coverage_verdict)

1. `software_engineering` — “software documentation quality evaluation outdated docs verifying documentation against code” → **partial** (max≈0.60; Osmani, Taulli, Winteringham, Silen, Khorikov)
2. `ai_llm_agents` — “documentation quality RAG over docs pitfalls agent use of documentation outdated docs” → **partial** (max≈0.71; n8n book, Freed et al., Brener, Kimothi)
3. `software_engineering` — “docs-driven development documentation driven development README as specification” → **partial** (max≈0.60; Silen, RSE Python, Taulli, Osmani)
4. `software_engineering` — “verify documentation against tests code examples doctest living documentation” → **partial** (max≈0.81; Osmani, Khorikov, Clean Code, Architecture Patterns with Python)
5. `ai_llm_agents` — “LLM agents retrieving and using software documentation critically evaluating sources” → **partial** (max≈0.60; MCP landscape paper, GraphRAG, RAG cookbooks)

### Exact `rag_query` questions (k≥10)

| # | Corpus | Question | k |
|---|--------|----------|---|
| Q1 | `software_engineering` | How to critically evaluate software documentation quality; outdated documentation; verifying docs against code | 12 |
| Q2 | `software_engineering` | Verify documentation against tests; doctest; living documentation; executable documentation examples | 12 |
| Q3 | `software_engineering` | Documentation-driven development; README as specification; writing docs before code | 12 |
| Q4 | `ai_llm_agents` | RAG over documentation pitfalls; stale or outdated documents in retrieval; grounding agents in docs | 12 |
| Q5 | `ai_llm_agents` | How LLM agents retrieve and use software documentation; critically evaluating documentation sources | 12 |
| Q6 | `software_engineering` | outdated API documentation checking AI code against official documentation cross-reference docs | 12 |
| Q7 | `software_engineering` | doctest executable documentation documentation generators keep docs in sync with code | 10 |
| Q8 | `ai_llm_agents` | stale documents removing outdated knowledge base maintenance documentation freshness | 10 |

### High-value `rag_fetch_chunk` IDs

- `e90b23a2a0acaf64ae846e3b` (+ neighbor `35a29bce0149220c70a53f48`) — Silen component docs principle / TOC
- `b594c791e9f5df63210b2a27` — Silen API comments vs unit tests; sync risk
- `ff546c171d6fc47942f2d123` (+ neighbor) — Percival/Gregory living documentation via tests
- `ed447de467e4cb5154816afc` — RSE “Be clear, but document”; audience / docstrings
- `cdf2fef2d9835808c8e69c32` — Osmani cross-ref AI output with official docs
- `8411b5b257f01503ad0e5438` (+ neighbor) — Pai RAG limitations / contradictory info
- `0991d43e2f307ae1e73a2e76` — Dhyani time-aware retrieval
- `5f4edca6d36c32a0625e7133` — McGrattan stale embeddings / deletion propagation
- Also used via query hits (not all re-fetched): `7ad59e94345f1956cce8b01f`, `99f7ef9ce905aeb4fe2cc7bf`, `f67f72d851685fbe9c6f94ea`, `ceedebc7cee340c2db876655`, `14be14681fd3b70b037c2d8e`, `bdf322688af0799a04b1c0d5`, `2e6aecd11f138f79287b5364`, `2d19f4e86374cd14dbfecf65`, `6a0749181f0bcc03e1cfde54`, `373acdb75e7f59fe7c94a532`, `c213fe2bda4956ed27807b25`, `9df6a235b40bdb0aeff2ac82`, `58b40fa2e9ea33ba5549f269`

---

## 3. Findings

### Documentation quality & structure

- `FACT` **[E2]** Software-component documentation’s main purpose is fast onboarding: easy/dev-container env setup, problem-domain understanding, and OOD documentation. Docs should live in the same repo as code: root `README.MD` plus split files under `docs/` to reduce merge conflicts. Example TOC: purpose, feature list (link Gherkin instead of duplicating), architecture/data-flow/OOD diagrams by subdomain (not one giant class diagram), auto-generated library API docs, implementation notes (errors, algorithms, perf, security), build/test setup instructions.  
  [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)…pdf` chunk_id=`e90b23a2a0acaf64ae846e3b` / neighbor=`35a29bce0149220c70a53f48` query=`"Documentation-driven development…"` / fetch]

- `FACT` **[E2]** Documentation generators (e.g. Sphinx) that scan code for names/docstrings beat manual copy-paste of API docs, which is “time-consuming” and “prone to errors as more functions are added.”  
  [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python…pdf` chunk_id=`6a0749181f0bcc03e1cfde54` query=`"Documentation-driven development…"`]

- `FACT` **[E2]** Doc quality heuristics for human-facing docs (audience, simplicity, consistency, examples/diagrams, explain *why* as well as *how*). README is the repo “welcome mat”; keeping it updated as the project grows is called out as hard.  
  [E2: Alexandria corpus=`software_engineering` source=`AI-Assisted Programming… (Tom Taulli).pdf` chunk_id=`2e6aecd11f138f79287b5364` / `2d19f4e86374cd14dbfecf65` query=`"Documentation-driven development…"`]

- `FACT` **[E2]** “Be clear, but document”: even good names don’t answer *why* the software does X or why not a simpler way; define audience to choose docstring vs tutorial/cookbook/FAQ depth; docstrings should start with active verbs and describe either I/O transform or side effects (not both without redesign).  
  [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python…pdf` chunk_id=`ed447de467e4cb5154816afc` query=`"How to critically evaluate…"`]

- `FACT` **[E2]** Research-software journals / peer review assess installability and how well software is documented — an external critical-feedback channel for doc quality.  
  [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python…pdf` chunk_id=`85ab90419d61b96092ab56b0` query=`"How to critically evaluate…"`]

- `CLAIM` **[E3-eligible discovery / still E2 book]** Docs and release notes often languish under delivery pressure; LLMs can draft comments/release notes but comment volume creates a maintenance burden to keep comments and code aligned.  
  [E2: Alexandria corpus=`software_engineering` source=`Software Testing with Generative AI (Mark Winteringham).pdf` chunk_id=`bdf322688af0799a04b1c0d5` query=`"How to critically evaluate…"`]

### Outdated docs & keeping docs ↔ code in sync

- `FACT` **[E2]** For **libraries**, public-API comments should feed auto-generated API docs specifically “to avoid situations where API comments and docs are out of sync.” For non-library components, prefer inferring behavior from interface + implementation + well-named unit tests rather than duplicating narrative API docs.  
  [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)…pdf` chunk_id=`b594c791e9f5df63210b2a27` query=`"doctest executable documentation…"`]

- `FACT` **[E2]** Feature lists can link Gherkin feature files so the same information is not stored in two places — a structural anti-duplication pattern for docs↔behavior sync.  
  [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)…pdf` chunk_id=`e90b23a2a0acaf64ae846e3b`]

- `FACT` **[E2]** Team warning pattern: AI/Copilot may suggest an **outdated library**; treat that as a known failure mode in team knowledge-sharing. When integrating a library, draft with AI then **cross-reference official documentation** to verify accuracy.  
  [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani).epub` chunk_id=`cdf2fef2d9835808c8e69c32` query=`"How to critically evaluate…"`]

- `INFERENCE` **[E4]** Premises: (1) AI suggestions can encode outdated APIs/libraries [Osmani]; (2) README/API narrative drifts unless generated from source or linked to executable specs [Silen, Taulli]. → Critically evaluating software docs for agents/humans should treat **freshness vs authoritative source** (official docs, generated API, tests/Gherkin) as a first-class check, not only prose clarity.  
  Premises cited above.

- `GAP` No strong retrieved method labeled “documentation QA” / “docs linter against AST” / “doctest as CI for prose examples” as a dedicated practice in these corpora for this pass (doctest named in probes but Q7 hits were mostly Sphinx/TOC/index noise).

### Verifying docs against code / tests (“living documentation”)

- `FACT` **[E2]** Domain-language tests “act as living documentation for our model”; new members can read them to learn how the system works; they also serve as “executable documentation” when exploring design at the domain layer (with the trade-off that tightly coupled tests must be replaced when design changes).  
  [E2: Alexandria corpus=`software_engineering` source=`Architecture Patterns with Python…pdf` chunk_id=`ff546c171d6fc47942f2d123` query=`"Verify documentation against tests…"`]

- `FACT` **[E2]** Unit-test names + assertions specify scenarios and expected behavior when narrative comments are omitted under TDD.  
  [E2: Alexandria corpus=`software_engineering` source=`Clean Code Principles And Patterns Python Edition (Petri Silen)…pdf` chunk_id=`b594c791e9f5df63210b2a27`]

- `FACT` **[E2]** Coding agents that can run the project test suite can catch mistakes and iterate until tests pass; humans still “Trust but verify” via PR review. Environment mismatch can leave failing tests if the agent cannot run the full suite.  
  [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani).epub` chunk_id=`373acdb75e7f59fe7c94a532` / related Execute/Verify sections query=`"Verify documentation against tests…"`]

- `INFERENCE` **[E4]** Premises: tests-as-living-docs [Percival/Gregory]; auto-gen API from comments [Silen]; agent verify-via-tests [Osmani]. → A practical “docs truth hierarchy” for evaluation: **executable tests / Gherkin > generated API from source > curated official docs > secondary prose / AI summaries**, with lower layers checked against higher when they conflict.  
  Premises cited above.

- `GAP` Little direct evidence of workflows that **diff prose documentation against code** (e.g. CI that fails when README examples diverge from current CLI). Mostly adjacent patterns (generate from source; link features; tests as docs).

### Docs-driven development

- `GAP` Named practice **“documentation-driven development” / “docs before code as specification”** did not surface as a first-class method in probe/query hits. Closest material is README-as-welcome-mat, Sphinx from docstrings, Silen TOC + Gherkin links, and AI-assisted README drafting — not “write the docs first, then implement.”

- `OPEN` Search primary sources / other corpora for Diátaxis, Docs as Code, “README-driven development,” executable books, or ADR-first workflows if Theme 3 templates need an explicit DDD-for-docs pattern.

### RAG over documentation — pitfalls (high coverage)

- `FACT` **[E2]** RAG pitfalls include: (1) over-reliance on surface-level retrieved snippets vs deeper understanding; (2) retrieval as the pipeline bottleneck; (3) retrieved docs contradicting parametric memory with no ground truth for the LLM to resolve. Causes of contradiction include **outdated/incorrect training data**, bad user context, or **incorrect/irrelevant retrieval**. RECALL benchmark / Liu et al.: factual inconsistencies tend to make models prefer prompt (retrieved) info; confidence drops under contradiction — usable as a processing signal.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Designing Large Language Model Applications… (Suhas Pai).pdf` chunk_id=`8411b5b257f01503ad0e5438` query=`"RAG over documentation pitfalls…"`]

- `FACT` **[E2]** Over-reliance on retrieved docs → outdated responses if documents are not refreshed; KB freshness is resource-intensive; chunk size trades irrelevant detail vs lost context; multi-hop / conflicting sources are hard; hallucination can persist even after relevant retrieval; “sophisticated verification mechanisms… most RAG systems currently lack.”  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering Retrieval-Augmented Generation…epub` chunk_id=`7ad59e94345f1956cce8b01f` / `21d493c3dee9d9d9eaa308db` query=`"RAG over documentation pitfalls…"`]

- `FACT` **[E2]** RAG/search chatbot maintenance requires **adding new documents and removing stale documents**.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Effective Conversational AI… (Freed, Jacobs, Rózsa).pdf` chunk_id=`99f7ef9ce905aeb4fe2cc7bf` query=`"stale documents removing outdated…"`]

- `FACT` **[E2]** Timestamp / metadata filtering and **time-aware retrieval** help avoid outdated evidence misleading the generator; prioritize temporal relevance for evolving domains.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`A Simple Guide to Retrieval Augmented Generation (Abhinav Kimothi).pdf` chunk_id=`9df6a235b40bdb0aeff2ac82`; `RAG with Python Cookbook… (Deepak Dhyani).pdf` chunk_id=`0991d43e2f307ae1e73a2e76` queries as above]

- `FACT` **[E2]** Answer quality is bounded by assembled context: incomplete, **outdated**, or overly generic context yields matching failures regardless of model sophistication; filter/rerank before generation.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Vector Databases for Enterprise AI… (Emma McGrattan).pdf` chunk_id=`c213fe2bda4956ed27807b25` query=`"RAG over documentation pitfalls…"`]

- `FACT` **[E2]** Source-document changes can leave **stale embeddings** that still retrieve “normally”; need lineage to regenerate; deletion of sources must cascade to embeddings.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Vector Databases for Enterprise AI… (Emma McGrattan).pdf` chunk_id=`5f4edca6d36c32a0625e7133` query=`"stale documents removing outdated…"`]

- `FACT` **[E2]** Corrective RAG (CRAG): retrieval evaluator scores correct/incorrect/ambiguous; incorrect → web search supplementation; knowledge strips re-evaluated — addresses flawed initial retrieval (latency and evaluator accuracy caveats).  
  [E2: Alexandria corpus=`ai_llm_agents` source=`A Simple Guide to Retrieval Augmented Generation (Abhinav Kimothi).pdf` chunk_id=`f67f72d851685fbe9c6f94ea` query=`"RAG over documentation pitfalls…"`]

- `FACT` **[E2]** Knowledge-base hygiene practices: remove outdated/conflicting entries; normalize; version-control the KB; data audits; return source documents with answers; confidence thresholding.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`Mastering RAG for AI Agents… (Jason Brener).epub` chunk_id=`ceedebc7cee340c2db876655` / `14be14681fd3b70b037c2d8e` / monitoring section `647c5fbdd91aadbba7283046`]

- `CLAIM` **[E2 practice book; treat as soft]** Agentic RAG setup: clean outdated/irrelevant data; consistent structure; metadata (date, type, author); hybrid keyword+semantic search; date/type/source filters; “quality agents” that validate completeness/accuracy; example “Technical Documentation Assistant” that searches API docs + examples + troubleshooting.  
  [E2: Alexandria corpus=`ai_llm_agents` source=`n8n BOOK FOR BEGINNERS…epub` chunk_id=`58b40fa2e9ea33ba5549f269` query=`"stale documents…"`]

### Agent use of documentation

- `FACT` **[E2]** Human–AI pairing workflow for library integration: AI drafts → human reviews → **cross-references official documentation**. Teams should share warnings about outdated suggestions.  
  [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani).epub` chunk_id=`cdf2fef2d9835808c8e69c32`]

- `FACT` **[E2]** Some coding agents allow controlled internet access specifically for needs such as fetching package updates or **documentation**; verification loop = compile/run tests, then human PR review.  
  [E2: Alexandria corpus=`software_engineering` source=`Beyond Vibe Coding… (Addy Osmani).epub` chunks under Execute/Verify, e.g. `8288af2502849bd398a94eab` / `373acdb75e7f59fe7c94a532` query=`"Verify documentation against tests…"`]

- `FACT` **[E2]** Enterprise “Copilot for Docs”-style systems described as ranking answers by user background and staying updated with repos / private docs (product claim in secondary text).  
  [E2: Alexandria corpus=`software_engineering` source=`AI-Assisted Programming… (Tom Taulli).pdf` chunk_id=`2e6aecd11f138f79287b5364`]

- `INFERENCE` **[E4]** Premises: agents retrieve/snippet-ground [Pai, McGrattan]; stale KB yields stale answers [Josyula, Freed]; humans must cross-check official docs [Osmani]. → Agents using software docs need **freshness metadata + source citation + optional official-docs fetch + test/executable verification**, not retrieval alone.  
  Premises cited above.

### PROTOCOL note on E3 (docs limitation discovery)

- `OPEN` This pass’s Alexandria hits are overwhelmingly **E2 books/guides**, not GitHub issues/forums. Per PROTOCOL, E3 (issues, blogs, anecdotes) is a first-class *discovery* channel for outdated-docs / docs bugs but cannot alone lock design. **No E3 primary hits were retrieved from these corpora** for “docs lie / version X docs wrong” style reports. Follow-up: issue trackers / Discourse / Stack Overflow for concrete outdated-docs failure cases, then corroborate with E0/E1.

---

## 4. Contradictions / conflicts found

1. **Where truth lives for APIs**  
   - Silen: library users need generated API docs from comments; non-library code should lean on tests/implementation, not separate API docs.  
   - Taulli / Silen TOC: still emphasize README + narrative docs for humans.  
   - *Resolution for integrator:* not a hard conflict — **audience split** (library consumers vs in-repo developers).

2. **Tests as documentation vs coupling**  
   - Percival/Gregory: domain tests are living/executable docs **and** tightly coupled (must be replaced on redesign); prefer service-layer tests for day-to-day change.  
   - Silen: well-named unit tests can replace comments on logic.  
   - *Resolution:* living docs are valuable but not free; document the gear/trade-off.

3. **Trust retrieved docs vs parametric memory**  
   - Pai / Liu et al.: on factual conflict, models often prefer **prompt/retrieved** content; outdated retrieved docs can therefore *win* over better internal knowledge.  
   - Desired behavior (Pai): ignore incorrect retrieved content — “extremely challenging” without ground truth.  
   - *Conflict remains open for design:* retrieval freshness/authority gating is required if docs RAG is used.

4. **AI-generated documentation**  
   - Winteringham/Taulli/Osmani encourage LLM-drafted docs/comments/READMEs for speed.  
   - Same sources warn of mis-explanation, comment/code drift, and need for human review.  
   - *Resolution:* generation ≠ verification; treat AI docs as drafts under the same sync rules.

---

## 5. Gaps

| Gap | What was searched | Result |
|-----|-------------------|--------|
| Formal **docs quality metrics** / readability scores for software docs | Q1–Q3, probes | Mostly TOC/heuristics and journal peer review; no metric suite |
| Explicit **docs↔code CI verification** (doctest, snippet runners) | Q2, Q7 | Living tests + Sphinx; weak/absent doctest practice hits |
| Named **documentation-driven development** | Q3 + probe | Absent as named method |
| **E3 community reports** of specific outdated official docs | All AI/SE queries | Not in corpora as issue/forum evidence |
| Agent **critical evaluation rubrics** specifically for documentation sources | Q5 | Adjacent RAG pitfalls + Osmani cross-ref; no rubric checklist |
| Primary standards (Diátaxis, Docs as Code, Write the Docs) | Path via these corpora | Not surfaced in top hits this pass |

---

## 6. Candidate patterns for templates (still cited)

Patterns below are **candidates only** — not design locks.

1. **Repo-colocated docs skeleton** — README + `docs/`; TOC covering purpose, features (link Gherkin), architecture diagrams by subdomain, generated API, env/build/test.  
   [Silen `e90b23a2a0acaf64ae846e3b`]

2. **Single source of truth ladder** — Prefer auto-generated API / linked executable features / tests over duplicated prose; for libraries, comments → generated docs to prevent comment/doc desync.  
   [Silen `b594c791e9f5df63210b2a27`, `e90b23a2a0acaf64ae846e3b`]

3. **Tests-as-living-docs (with gear)** — Domain-language tests for executable docs when exploring model; prefer lower-coupling layers for routine changes.  
   [Percival/Gregory `ff546c171d6fc47942f2d123`]

4. **Official-docs cross-check for AI output** — When integrating libraries or accepting agent code, verify against official documentation; share “outdated suggestion” warnings.  
   [Osmani `cdf2fef2d9835808c8e69c32`]

5. **Trust-but-verify agent loop** — Agent runs tests/build; human reviews PR; do not treat retrieval or passing partial tests as sufficient.  
   [Osmani Verify chunks]

6. **RAG docs hygiene** — Remove stale docs; timestamp/metadata filters; time-aware retrieval; cascade deletes to embeddings; return sources; confidence thresholds; optional CRAG-style retrieval evaluation.  
   [Freed `99f7ef9ce905aeb4fe2cc7bf`; Kimothi `9df6a235b40bdb0aeff2ac82` / `f67f72d851685fbe9c6f94ea`; Dhyani `0991d43e2f307ae1e73a2e76`; McGrattan `5f4edca6d36c32a0625e7133` / `c213fe2bda4956ed27807b25`; Brener `ceedebc7cee340c2db876655`]

7. **Contradiction / confidence signal** — When retrieved docs conflict with model knowledge or each other, treat low confidence / dual sources as need for higher-authority check (tests, official versioned docs), not silent merge.  
   [Pai `8411b5b257f01503ad0e5438`; Josyula challenges chunks]

8. **Audience-first doc type selection** — Match docstring vs tutorial/cookbook/FAQ to audience; explain *why* not only *how*.  
   [RSE `ed447de467e4cb5154816afc`; Taulli `2e6aecd11f138f79287b5364`]

---

## 7. Source list (deduped)

### `software_engineering`

- Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani) — epub (`34e9b0c879911f25`)
- Clean Code Principles And Patterns Python Edition (Petri Silen) — pdf (`36685a7cb512e211`)
- Research Software Engineering with Python… (Irving, Hertweck, Johnston et al.) — pdf (`fa269d33b0dfa321`)
- Architecture Patterns with Python (Bob Gregory, Harry Percival) — pdf (`ccc326d5d96d3dba`)
- AI-Assisted Programming… (Tom Taulli) — pdf (`d26c6134e46d77d4`)
- Software Testing with Generative AI (Mark Winteringham) — pdf (`e0b74e3ceb5f3167`)
- Software Development, Design, and Coding… 3rd ed. (Dooley, Kazakova) — pdf (`386bdd875b27fc9d`) — mostly code-review context; weak on docs-eval
- Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov) — pdf (`b661cce5e1029b9c`) — peripheral
- Clean Architecture with .NET (Dino Esposito) — epub (`c4ea4b0865650dac`) — TOC/index noise on “docs in sync”
- Test-Driven Development with Python (Harry Percival) — pdf (`5aa410f625b2a819`) — index hit “documentation, tests as”

### `ai_llm_agents`

- Designing Large Language Model Applications… (Suhas Pai) — pdf (`07e030e7d4c21918`)
- Mastering Retrieval-Augmented Generation (Josyula et al.) — epub (`c9f22a829cc137b4`)
- Mastering RAG for AI Agents… (Jason Brener) — epub (`f138b0648b0502ed`)
- A Simple Guide to Retrieval Augmented Generation (Abhinav Kimothi) — pdf (`34e76f8a0cbe6b3a`)
- RAG with Python Cookbook… (Deepak Dhyani) — pdf (`cb7b5b35d25d4ab6`)
- Vector Databases for Enterprise AI… (Emma McGrattan) — pdf (`ccae4bb1630474b7`)
- Effective Conversational AI… (Andrew Freed, Cari Jacobs, Enikő Rózsa) — pdf (`fbdaea05c79120d1`)
- AI Engineering… (Chip Huyen) — pdf (`d897e858aa0a690a`) — memory/contradiction handling peripheral
- n8n BOOK FOR BEGINNERS… (Arsath Natheem S) — epub (`7d30f493f423e22e`)
- Ultimate Milvus… (Prashanth Raghu) — epub (`9a4ed9f3709dc0e2`) — mostly infra “stale” noise; low value for software-docs theme

### Local / protocol

- [E0: path=`d:\GreyMatter\docs\research\PROTOCOL.md` observed 2026-07-27]
