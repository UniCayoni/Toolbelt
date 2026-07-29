# Theme 3 / Slice D — Docs vs code verification (notes)

Status: notes only (not integrated report)  
Agent id: `t3d-docs-vs-code-verification`  
Date: 2026-07-27  
Protocol: `d:\GreyMatter\docs\research\PROTOCOL.md`

---

## 1. Scope

Verifying documentation **against the codebase / runtime** (and vice versa): documentation drift / bitrot literature and practitioner primaries; executable docs / doctests / docs-as-tests; examples in docs as contracts; conflict resolution when README/docs disagree with code (which wins, how to record); agent workflows that read docs then corroborate via code search / running examples / schema checks; relations to Theme 1 recon (docs as beacons) and Theme 2 (cite docs as E1 but mark when contradicted by E0).

Out of scope: GreyMatter plugin stub/scaffolding; locking RAG libraries; MVP feature scope.

---

## 2. Method

**Tools:** MCP `user-alexandria-rag` (`list_corpora`, `rag_query`, `rag_fetch_chunk`); WebSearch; WebFetch. Schemas fetched via `GetMcpTools` before MCP calls.

**Corpora observed (E0):** `software_engineering` (21 docs / 7712 chunks); `ai_llm_agents` (71 docs / 22720 chunks). [E0: MCP `list_corpora` observed 2026-07-27]

**Alexandria queries (`software_engineering` unless noted):**
1. `documentation drift bitrot rotting docs outdated documentation disagree with code` (k=14) — weak topical hit rate
2. `doctests executable documentation docs as tests examples as contracts verification` (k=14)
3. `outdated documentation comments inconsistent with code documentation debt maintain accuracy` (k=14)
4. `doctest literate programming executable examples documentation testing continuous documentation` (k=12)
5. `README architecture docs provide context to AI coding tools verify against source code` (k=12)
6. `ai_llm_agents`: `agent verify documentation against code search run examples hallucinations grounding citations` (k=12) — mostly RAG/hallucination grounding, weak on docs↔code specifically

**High-value `rag_fetch_chunk`:** `801784923370b6c3a0d358e9` (Clean Code comments/SoT); `19b65d1fd83a0a318bd1c898` (RSE JOSS-style checklist).

**WebSearch terms:**
- `documentation drift bitrot rotting docs codebase verification literature`
- `docs as tests doctests executable documentation examples as contracts`
- `rustdoc documentation tests code blocks executable docs as tests`
- `Diátaxis documentation code examples as contracts source of truth docs vs code`
- `Write the Docs documentation debt outdated docs bitrot`
- `OpenAPI specification single source of truth documentation contract testing Dredd`

**Primary URLs fetched / read this pass:**
- Python `doctest` docs — https://docs.python.org/3/library/doctest.html
- rustdoc Documentation tests — https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html
- Write the Docs Documentation principles — https://www.writethedocs.org/guide/writing/docs-principles/
- Tan et al. EMSE 2024 (Springer page + abstract/body excerpts) — https://link.springer.com/article/10.1007/s10664-023-10397-6
- READU arXiv HTML — https://arxiv.org/html/2607.15780v1
- Dredd docs — https://dredd.org/en/latest/
- Diátaxis PDF download (partial parse) — https://diataxis.fr/_/downloads/en/latest/pdf/
- Cross-read local notes: Theme 1 `t1c` (beacons), Theme 2 `t2b`/`t2c` (Diátaxis, SoT hierarchy, cite conflicts)

**Also noted from search (not always full-text):** Aghajani et al. documentation-issue taxonomy (cited inside Tan et al.); Write the Docs “Testing your documentation” guide (search hit; fetch timed out); MIUCC 2025 review on documentation drift (DOI only this pass).

---

## 3. Findings

### 3.1 Drift / bitrot / outdated docs (literature + practitioner)

- `FACT` [E1] Outdated documentation is a pervasive SE problem: hinders effectiveness, misleads users/developers, contributes to ageing/confusion, demotivates newcomers; docs can go stale “silently” (no crash) so developers often do not notice that code changes obsolete docs. [E1: Tan, Wagner & Treude, “Detecting outdated code element references in software repository documentation,” *Empirical Software Engineering* 29:5 (2024) — https://link.springer.com/article/10.1007/s10664-023-10397-6 — accessed 2026-07-27]

- `FACT` [E1] Tan et al. cite Aghajani et al. (2019): “up-to-dateness problems” account for **39%** of documentation *content* issues; prior surveys: more than two-thirds of participants believe their system documentation is outdated. [E1: same Tan et al. Introduction]

- `FACT` [E1] Empirical scale (Tan et al.): analysed >3,000 GitHub projects; **28.9%** of most popular projects currently contain ≥1 outdated code-element reference; **82.3%** outdated at least once in history; stale refs often persist years. Detection heuristic: extract code-element refs from README/wiki via regex; flag when documentation still names an element after all source instances are deleted. [E1: same]

- `FACT` [E1] READU frames **README bugs** = factually incorrect *repository-level* documentation (README/howto/tutorial/build guides—not only the filename README). Key insight: bugs often appear as **inconsistencies** vs another source of truth—**internal** (code/config/other docs) or **external** (dependency APIs, tools, services). Detection framed as consistency checking because README bugs often lack an executable oracle. [E1: Baek, Krampf & Pradel, “READU…,” arXiv:2607.15780 — https://arxiv.org/html/2607.15780v1 — accessed 2026-07-27]

- `FACT` [E1] Write the Docs principle **Current**: “Consider incorrect documentation to be worse than missing documentation.” Also: keep docs up to date when software changes faster than docs; prefer version-agnostic wording to reduce maintenance; support versioned docs for users on older software. [E1: Write the Docs — Documentation principles — https://www.writethedocs.org/guide/writing/docs-principles/ — accessed 2026-07-27]

- `FACT` [E1] Write the Docs **Nearby**: store doc sources as close as possible to the code they document (comment blocks or same-repo text files) so doc changes merge with code changes. **Unique**: eliminate content overlap across sources to avoid parallel (non-)maintenance. [E1: same]

- `FACT` [E1] Write the Docs **ARID**: Accept (some) Repetition In Documentation—strict DRY fails for docs because some business logic must be restated; generators help but still need human input; awareness that code/doc dual writing implies updating both. [E1: same]

- `FACT` [E2] Clean Code: comments often become wrong as code moves; “Inaccurate comments are far worse than no comments at all”; “Truth can only be found in one place: the code… It is the only source of truly accurate information.” [E2: Alexandria corpus=`software_engineering` source=`Clean Code_ A Handbook of Agile Software Craftmanship...pdf` chunk_id=`801784923370b6c3a0d358e9` query=`"outdated documentation comments inconsistent..."`]

- `CLAIM` [E3] Practitioner blogs (e.g. “documentation rot”) argue rot is a **workflow** problem—no verification that docs match code—and recommend colocation, CI checks, broken-example detection. Useful for discovery; not design-locking alone. [E3: e.g. devonair.ai blog hit via WebSearch 2026-07-27]

- `GAP` MIUCC 2025 review DOI `10.1109/miucc66482.2025.11196773` surfaced in search as a survey of drift detection (heuristic → LLM/multi-agent); full text not retrieved this pass.

### 3.2 Executable docs / doctests / docs-as-tests

- `FACT` [E1] Python `doctest`: searches text for interactive sessions (`>>>` / `...`), executes them, verifies output matches. Documented use cases include tutorial docs “liberally illustrated with input-output examples” with flavor of “**literate testing**” or “**executable documentation**.” [E1: Python 3 docs — https://docs.python.org/3/library/doctest.html — accessed 2026-07-27]

- `FACT` [E1] `doctest.testfile()` / CLI can check examples in **plain text/Markdown** files (file treated as one giant docstring); recommended pattern: text files of interactive examples + `testfile()` / `DocFileSuite()`. [E1: same]

- `FACT` [E1] rustdoc: documentation examples are executable tests so examples stay “up to date and working”; pass = compile + run without panic (use `assert!`); attributes: `ignore`, `should_panic`, `no_run` (compile only—e.g. network examples), `compile_fail`, edition markers; README can be included under `#[cfg(doctest)]` for testing without publishing as main docs. [E1: The rustdoc book — Documentation tests — https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html — accessed 2026-07-27]

- `INFERENCE` [E4] Executable examples turn a subset of documentation claims into **fail-loud contracts** in CI; prose/narrative claims remain unverified unless separately checked. Premises: Python/rustdoc purpose statements [E1]; Tan “silent” staleness [E1].

### 3.3 Examples as contracts; schemas as contracts

- `FACT` [E1] Diátaxis **reference**: purpose is accurate, complete, reliable technical description; users need “truth and certainty”; reference should be “wholly authoritative”; architecture of reference should reflect the product; some API reference can be **auto-generated** so it “remains faithfully accurate to the code”; short examples illustrate without becoming how-to. [E1: Diátaxis (PDF) — https://diataxis.fr/_/downloads/en/latest/pdf/ — accessed 2026-07-27; consistent with Theme 2 note `t2b` citing diataxis.fr]

- `FACT` [E1] Dredd: language-agnostic CLI that validates an **API description document** (API Blueprint / OpenAPI) against a live backend—reads the description and checks whether the implementation replies as documented. [E1: Dredd docs — https://dredd.org/en/latest/ — accessed 2026-07-27]

- `INFERENCE` [E4] For APIs, OpenAPI/JSON Schema + contract tests (Dredd-class tools, Schemathesis, etc.) make the **machine-readable description** the checkable contract; narrative docs should stay consistent with the schema, but schema+runtime checks outrank prose when they conflict. Premises: Dredd [E1]; Theme 2 `t2b` OpenAPI/tool-schema inference; Write the Docs newsletter consensus on OpenAPI as SoT (search hit Oct 2024 — treat as E3 pending full fetch).

- `FACT` [E2] Research Software Engineering checklist items treat docs as claims to validate: “Does installation proceed as outlined in the documentation?”; “Have the functional claims… been confirmed?” (commands perform as described in README); “Example usage” / “Functionality documentation” / “Automated tests… so that functionality… can be verified.” [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python...pdf` chunk_id=`19b65d1fd83a0a318bd1c898`]

### 3.4 When docs disagree with code — which wins, how to record

- `FACT` [E2] Clean Code hard line for **comments vs code**: code is the only truly accurate source; inaccurate comments worse than none. [E2: chunk_id=`801784923370b6c3a0d358e9`]

- `FACT` [E1] Write the Docs: incorrect docs worse than missing; prefer fixing/removing wrong content over leaving it. [E1: WTD principles — Current]

- `FACT` [E1] READU operationalizes conflict as **contradictory facts** (doc statement + contradicting internal/external fact); repair targets the documentation when code/external API is treated as truth for the bug class studied. [E1: READU arXiv HTML]

- `INFERENCE` [E4] **Layered authority for agents (candidate, not product lock):**
  1. **E0 runtime / code / schema / tests** win for “what the system does now.”
  2. **Machine contracts** (OpenAPI, JSON Schema, typed signatures, doctests that pass in CI) win over untested prose.
  3. **E1 narrative docs** remain citable for intent, how-to, and declared API *when not contradicted*.
  4. On conflict: **prefer code/runtime**, cite both, mark docs as `CONTRADICTED` / stale; do not silently trust README.
  Premises: Clean Code SoT [E2]; WTD Current [E1]; READU consistency framing [E1]; GreyMatter PROTOCOL evidence grades [E0: PROTOCOL.md]; Theme 2 SoT hierarchy [local note `t2c`].

- `FACT` [E1] OpenAI citation guidance (relevant to recording conflict): cite conflicts explicitly when sources disagree; never invent locators. [E1: as recorded in Theme 2 `t2c` — OpenAI Citation Formatting — accessed 2026-07-27 in that note]

### 3.5 Agent workflows: read docs → verify with code / examples / schemas

- `FACT` [E1] Cursor documents a **verifier subagent** pattern: skeptical validation that claimed-complete work exists and works; run tests; do not accept claims at face value. [E1: via Theme 2 `t2c` citing https://cursor.com/docs/subagents — accessed 2026-07-27]

- `FACT` [E1] Theme 1 product patterns: explore/search before edit; instruction files list verification commands (`AGENTS.md` / CLAUDE.md). [E1: Theme 1 notes `t1b` — agents.md, Cursor search/explore, Claude best practices — accessed 2026-07-27]

- `FACT` [E2] Osmani / AI-era guidance: treat AI outputs as drafts; verify functionality; confirm against original goal; check tests/coverage. [E2: Alexandria `Beyond Vibe Coding...` hits under README/AI-context queries, e.g. chunk_id=`ae5ea30721760ce3b23ed7af`]

- `INFERENCE` [E4] A docs-first agent path should be: (1) read README/architecture docs as **hypothesis beacons**, (2) corroborate symbols/commands/paths via search + file read, (3) run documented examples or contract tests when cheap, (4) check schemas/OpenAPI against runtime if applicable, (5) on mismatch record E0 vs E1 conflict. Premises: beacon hypothesis verification [E1 PC via Theme 1 `t1c`]; READU internal/external checkers [E1]; doctest/rustdoc/Dredd [E1].

- `GAP` Alexandria `ai_llm_agents` queries on “verify documentation against code” mostly returned RAG citation / hallucination material, not a dedicated docs↔code verification playbook. [E0: rag_query results 2026-07-27]

### 3.6 Relation to Theme 1 (docs as beacons) and Theme 2 (E1 docs vs E0)

- `FACT` [E1] Program comprehension: **beacons** are cues indexing into knowledge; hypothesis verification depends heavily on presence/absence of beacons (Brooks via von Mayrhauser & Vans / Storey). [E1: Theme 1 `t1c` citing von Mayrhauser & Vans 1995; Storey et al.]

- `INFERENCE` [E4] Repository docs (README, architecture notes, AGENTS.md) act as **beacons** for agents: useful for top-down hypotheses, but beacons can be **false** when drifted—so Theme 3 verification is the “resolve / revise / abandon hypothesis” step from PC literature. Premises: beacons [E1 Theme 1]; drift prevalence [E1 Tan]; WTD Current [E1].

- `INFERENCE` [E4] Theme 2 protocol mapping: cite official/vendor/repo docs as **E1**; if local code/runtime observation contradicts, keep the E1 citation but label claim as contradicted by **E0**, and prefer E0 for “what works now.” Aligns with PROTOCOL “prefer higher evidence grade” and OpenAI “cite conflicts.” Premises: PROTOCOL.md [E0]; Theme 2 `t2c` SoT table; Tan/READU [E1].

---

## 4. Contradictions / conflicts found

| Conflict | Resolution for notes |
|----------|----------------------|
| Clean Code “code is only truth” vs Diátaxis “reference must be authoritative” for users | Different scopes: Martin targets **comments adjacent to evolving code**; Diátaxis targets **published reference** that *should* mirror product (ideally generated). For agents: code/runtime wins on factual conflict; regenerate/fix reference rather than invent from stale prose. |
| Dredd-class tools treat API **description as oracle** vs Clean Code “code wins” | Spec-first API design makes the description the intended contract; implementation is then defective relative to the contract. Record which process the project uses (spec-first vs code-first). If unspecified, GreyMatter research default: **E0 observed behavior** + note whether a machine contract exists. |
| Docs-as-tests vs “no executable oracle” for README prose (READU) | Only a subset of doc claims are executable; consistency checking / search corroboration covers the rest. |
| Alexandria SE corpus weak on “documentation drift” as named topic | Do not invent corpus evidence; rely on E1 papers/web primaries for drift epidemiology. |

---

## 5. Gaps

- `GAP` Full text of Aghajani et al. 2019 documentation-issue study not read this pass (only via Tan et al. citation).
- `GAP` Write the Docs “Testing your documentation” page fetch timed out; search abstract lists CI build, link checks, Vale—`OPEN` to re-fetch.
- `GAP` Diátaxis `/reference/` HTML fetch timed out; PDF used instead.
- `GAP` Schemathesis / Spectral official docs not fetched; mentioned only via secondary search synthesis.
- `GAP` No GreyMatter-local E0 experiment running doctests/rustdoc/Dredd in this pass.
- `GAP` Alexandria lacks primary EMSE/PC papers on doc-code sync; practitioner books dominate SE shelf.
- `OPEN` Preferred conflict log schema for GreyMatter templates (fields below are candidates only).

---

## 6. Candidate patterns for templates (docs–code corroboration)

Still cited; not product locks.

### 6.1 Template steps — Docs↔code corroboration pass

1. **Ingest docs as hypotheses (beacons), not facts.** Read README / architecture / AGENTS.md / relevant Diátaxis how-to+reference. Tag claims as `DOC_CLAIM`. [E1 WTD Nearby/Current; E1 Theme 1 beacons; E4 §3.6]

2. **Extract checkable atoms.** Paths, symbol names, CLI commands, env vars, API routes, version pins, code fences. Prefer atoms that can be grepped, executed, or schema-validated. [E1 Tan element-ref idea; E1 READU internal facts]

3. **Corroborate internally (E0).** For each atom: code search / file existence / signature match / config read. Record `MATCH` | `MISSING` | `RENAMED` | `AMBIGUOUS`. [E1 Tan; E1 READU Definition 1]

4. **Corroborate externally when claimed.** Package versions (`npm view`/etc.), URLs, dependency APIs—only if docs assert them. [E1 READU Definition 2 / external checker]

5. **Execute contracts when available.** Run doctests / `cargo test --doc` / documented smoke commands / OpenAPI contract tests. Prefer CI-equivalent commands from `AGENTS.md`. [E1 Python doctest; E1 rustdoc; E1 Dredd; E1 agents.md via Theme 1]

6. **Resolve authority.** On conflict: prefer E0 code/runtime (and machine schemas if project is contract-first); keep E1 doc citation with status `CONTRADICTED_BY_E0` (or `STALE`). Never silently drop the doc claim. [E2 Clean Code; E1 WTD; E1 OpenAI cite conflicts via Theme 2]

7. **Write a conflict record** (candidate fields): `doc_locator`, `doc_quote`, `code_locator`/`command`/`schema_path`, `observation`, `winner` (`code`|`schema`|`doc`|`unresolved`), `evidence_grades`, `repair_suggestion` (update docs vs fix code—human decision). [E4 from READU alert shape + PROTOCOL labels]

8. **Verifier pass.** Skeptical check that claimed corroboration actually ran (tests green, paths exist)—Cursor verifier pattern. [E1 Cursor subagents via Theme 2]

### 6.2 Template step — Examples-as-contracts policy

- Mark code fences: `executable` (must pass CI) | `illustrative` (`no_run` / ignore) | `anti-example` (`compile_fail` / should_panic). [E1 rustdoc attributes; E1 Python doctest]

### 6.3 Template step — Beacon hygiene (Theme 1 link)

- After recon, list which README/architecture beacons were **confirmed**, **revised**, or **abandoned**—mirrors PC hypothesis lifecycle. [E1 Theme 1 `t1c`]

### 6.4 Template step — Theme 2 citation discipline

- Docs cited as E1 OK; if contradicted, claim label stays but grade/note shows E0 override. Do not demote the URL; demote the **assertion**. [E0 PROTOCOL; E4 §3.6]

---

## 7. Source list (deduped)

**Alexandria / local**
- `software_engineering` corpus (list_corpora 2026-07-27)
- Clean Code (Martin) chunk `801784923370b6c3a0d358e9`
- Research Software Engineering with Python chunk `19b65d1fd83a0a318bd1c898`
- Beyond Vibe Coding (Osmani) chunks under README/AI verification queries
- `d:\GreyMatter\docs\research\PROTOCOL.md`
- Theme 1 notes `t1b`, `t1c`; Theme 2 notes `t2b`, `t2c`

**Primary / official web**
- Tan, Wagner & Treude, EMSE 2024 — https://link.springer.com/article/10.1007/s10664-023-10397-6
- Baek, Krampf & Pradel, READU — https://arxiv.org/html/2607.15780v1
- Python doctest — https://docs.python.org/3/library/doctest.html
- rustdoc Documentation tests — https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html
- Write the Docs Documentation principles — https://www.writethedocs.org/guide/writing/docs-principles/
- Diátaxis PDF — https://diataxis.fr/_/downloads/en/latest/pdf/
- Dredd — https://dredd.org/en/latest/
- Cursor Subagents (via Theme 2) — https://cursor.com/docs/subagents
- OpenAI Citation Formatting (via Theme 2) — https://developers.openai.com/api/docs/guides/citation-formatting

**Secondary / discovery-only**
- WebSearch hits on documentation rot blogs, Docsie glossary, Schemathesis guides, WTD newsletters — E3 unless re-fetched as primary
