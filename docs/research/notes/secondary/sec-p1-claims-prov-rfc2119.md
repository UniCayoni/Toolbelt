# Secondary P1 — Claim citation defaults, W3C PROV, RFC 2119 (+ D12 tools)

Status: notes only (not integrated report)  
Created: 2026-07-27  
Agent: `sec-p1-claims-prov-rfc2119`  
Closes / shrinks: **T2-O1**, **T2-O2**, **T2-G10**, **T3-G8**, **T3-O2**, optional **T3-G15**

## 1. Scope

1. **Claim citation defaults (T2-O1 / O2):** Whether GreyMatter research notes should require quote spans vs `chunk_id`+grade, and whether dual markdown + JSON `claims[]` should be default or optional. Recommend with premises; mark as `INFERENCE` [E4]; do not invent standards.
2. **W3C PROV (T2-G10):** Minimal PROV-DM / PROV-O terms useful for research-note provenance.
3. **RFC 2119 (T3-G8):** How MUST/SHOULD/MAY in docs affect researcher trust; tie to Theme 3 **D3**.
4. **Optional D12 tools (T3-G15):** Schemathesis and Spectral — one paragraph each on OpenAPI contract-testing relevance.
5. **Conflict-log field schema (T3-O2):** Propose a local convention grounded in Theme 3 notes (INFERENCE).

Out of scope: plugin stub, product locks, elevating skills.

## 2. Method (tools, queries, date)

| Item | Detail |
|------|--------|
| Date | 2026-07-27 |
| Protocol | `d:\GreyMatter\docs\research\PROTOCOL.md` |
| Priorities | `d:\GreyMatter\docs\research\SECONDARY_PRIORITIES.md` |
| Local priors (E0) | Theme 2 report O1/O2/G10; Theme 2 notes `t2a`, `t2c`; Theme 3 notes `t3b`, `t3d`; templates `claim-citation.md`, `documentation-research.md` |
| Web fetch (E1) | PROV-DM REC 2013-04-30; PROV-O REC 2013-04-30; RFC 2119; RAGAS Faithfulness docs; Schemathesis site + GitHub README; Spectral GitHub README |
| Web fetch failures | `https://www.w3.org/TR/prov-dm/` timed out (used dated REC URL); Schemathesis ReadTheDocs index timed out (used schemathesis.io + raw GitHub README); Spectral concepts URL 404 (used raw GitHub README) |
| Alexandria | `rag_query` corpus=`ai_llm_agents` question on PROV — no W3C PROV primary in corpus (general provenance prose only; not used as PROV standard evidence) |
| Searched / not inventing | No portable industry evidence-span schema found in Theme 2; reconfirmed as GAP |

## 3. Findings

### 3.1 Claim citation defaults (T2-O1 / O2)

#### Premises from primaries / local protocol (not inventing a standard)

- `FACT` [E1] — ALCE models long-form answers as statements with per-statement citation lists (numeric markers); citation recall/precision operate over **cited passages**, not mandatory character-offset quote spans. [E1: Gao et al., ALCE — https://ar5iv.labs.arxiv.org/html/2305.14627 — as recorded Theme 2 `t2a` / Theme 2 report; accessed prior pass 2026-07-27]
- `FACT` [E1] — RAGAS Faithfulness decomposes a response into claims and checks whether each claim is inferable from `retrieved_contexts` (context text), score in [0,1]. It does **not** require a portable quote-span schema. [E1: RAGAS Faithfulness — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/ — accessed 2026-07-27]
- `FACT` [E0] — PROTOCOL Alexandria citation form requires `corpus` / `source` / `chunk_id` (if available) / `query`; does **not** mandate quote spans. Optional short quotes appear in human citation practice and templates. [E0: `PROTOCOL.md`; `templates/claim-citation.md`]
- `FACT` [E0] — Theme 2 report: dual citation layer = machine-stable IDs (`corpus`/`source`/`chunk_id`, **optional** spans) + human PROTOCOL-style markers; **no industry-standard portable evidence-span schema** found; O1/O2 left OPEN. [E0: `reports/theme-2-agent-usable-documentation.md`]
- `FACT` [E1] — Vendor Assistants file-search annotations are typically **file_id / file_citation** structured objects + human `[index]` markers—not a universal char-span interchange format. [E1: as recorded Theme 2 `t2a` Azure file search]
- `GAP` — Still no primary that defines a mandatory portable quote-span / char-offset / quote-hash schema for research notes across tools. Prefer absence over invention.

#### Recommendation A — Quote spans vs `chunk_id`+grade (closes T2-O1 as local convention)

- `INFERENCE` [E4] — **Default required locator for grounded notes: passage/`chunk_id` (or URL+section for non-Alexandria E1) + evidence grade + claim label. Quote spans / `char_start`–`char_end` / short verbatim quotes are RECOMMENDED (optional) when cheap and when the claim is contested, high-stakes, or will feed automatic NLI.** Do **not** require quote spans as a hard gate for note completeness.

  Premises:
  1. ALCE and RAGAS verify against **passage/context text** identified by retrieval IDs, not a mandated offset schema [E1].
  2. PROTOCOL already treats `chunk_id` as first-class and does not require spans [E0].
  3. Theme 2 explicitly found no portable span standard; inventing one as mandatory would over-claim [E0 Theme 2 G1/O1].
  4. Short quotes remain useful for human audit and conflict records (see §3.5) without elevating spans to a global schema [E4 from Theme 3 conflict candidates + OpenAI “cite conflicts / don’t invent locators” via Theme 2].

#### Recommendation B — Dual markdown + JSON `claims[]` (closes T2-O2 as local convention)

- `INFERENCE` [E4] — **Human markdown research notes (PROTOCOL sections + inline citations) remain the default deliverable. Structured `claims[]` (JSON sidecar or fenced block matching `claim-citation.md` claim object) is OPTIONAL by default; SHOULD emit when the note will be machine-merged, faithfulness-scored, or elevated into a skill/template audit.** Do **not** make dual payload mandatory for every exploratory note.

  Premises:
  1. ALCE/RAGAS benefit from claim decomposition, but their papers/docs do not prescribe dual markdown+JSON as a documentation format [E1].
  2. Azure-style dual layer is **annotations + human text**, not “always emit claims.json” [E1 Theme 2].
  3. Existing template already defines claim objects as “preferred structured form” without forcing every note to ship JSON [E0 `claim-citation.md`].
  4. Mandatory dual payload increases agent failure modes (drift between prose and JSON) without a primary requiring it [E4].

### 3.2 W3C PROV — minimal vocabulary for research notes (T2-G10)

- `FACT` [E1] — PROV defines provenance as a record of people, institutions, entities, and activities involved in producing/influencing/delivering data or a thing; used for trust, integration, and credit. [E1: PROV-DM — https://www.w3.org/TR/2013/REC-prov-dm-20130430/ — Abstract / §1 — accessed 2026-07-27]
- `FACT` [E1] — **Core starting-point types** (PROV-O / PROV-DM): `Entity`, `Activity`, `Agent`. [E1: PROV-O §2 — https://www.w3.org/TR/prov-o/ ; PROV-DM §2.1 — accessed 2026-07-27]
- `FACT` [E1] — Informal / formal definitions (abbrev.):
  - **Entity** — physical, digital, conceptual, or other thing with some fixed aspects (may be real or imaginary).
  - **Activity** — something that occurs over a period of time and acts upon or with entities (consume, process, transform, generate, …).
  - **Agent** — something that bears some form of responsibility for an activity, an entity’s existence, or another agent’s activity. Common types: `prov:Person`, `prov:SoftwareAgent`, `prov:Organization`.
  [E1: PROV-DM §2.1.1, §2.1.3, §5.1.1–5.1.2, §5.3.1]
- `FACT` [E1] — **Core relations** useful for notes:

  | Relation | Rough meaning |
  |----------|----------------|
  | `wasGeneratedBy` | Entity produced by an Activity |
  | `used` | Activity began utilizing an Entity |
  | `wasDerivedFrom` | Entity₂ transformed/updated/constructed from Entity₁ |
  | `wasAttributedTo` | Entity ascribed to an Agent |
  | `wasAssociatedWith` | Agent had a role in an Activity |
  | `actedOnBehalfOf` | Agent delegated responsibility |
  | `startedAtTime` / `endedAtTime` | Activity bounds |
  [E1: PROV-O Starting Point list; PROV-DM §2.1 tables]

- `FACT` [E1] — **Expanded terms** especially useful for research writing: `wasQuotedFrom`, `wasRevisionOf`, `hadPrimarySource`, `Bundle` (provenance of provenance), `SoftwareAgent`. [E1: PROV-O Expanded list; PROV-DM §5.2 / §5.4]
- `INFERENCE` [E4] — Map GreyMatter note concepts onto PROV **lightly** (vocabulary aid, not full RDF export by default):

  | Note concept | PROV analogue |
  |--------------|---------------|
  | Source doc / chunk / URL / file | `Entity` |
  | Research pass / fetch / corroboration run | `Activity` |
  | Human researcher / Cursor agent / tool | `Agent` (`Person` / `SoftwareAgent`) |
  | Note claim or note file derived from sources | `wasDerivedFrom` (+ optional `wasQuotedFrom` when quoting) |
  | Method block + agent id | `wasAssociatedWith` / `wasAttributedTo` |
  | Conflict-log entry revising an earlier claim | `wasRevisionOf` or new entity + `wasDerivedFrom` |

  Premises: PROV core definitions [E1]; Theme 2 provenance needs (lineage, attribution, timestamps) [E0 `t2c`]; PROTOCOL Method/citation fields [E0].

- `GAP` — Full PROV-CONSTRAINTS validation and RDF serialization for GreyMatter notes not surveyed this pass; not required to close T2-G10 vocabulary gap.

### 3.3 RFC 2119 and researcher trust (T3-G8 → D3)

- `FACT` [E1] — RFC 2119 (BCP 14) defines requirement keywords for IETF documents: **MUST** / **REQUIRED** / **SHALL** = absolute requirement; **MUST NOT** / **SHALL NOT** = absolute prohibition; **SHOULD** / **RECOMMENDED** = valid reasons to ignore exist, but implications must be understood and carefully weighed; **SHOULD NOT** / **NOT RECOMMENDED** = analogous for avoidance; **MAY** / **OPTIONAL** = truly optional; implementations must interoperate with and without the option. Authors should include the standard incorporation phrase. [E1: RFC 2119 — https://www.rfc-editor.org/rfc/rfc2119 — accessed 2026-07-27]
- `FACT` [E1] — Guidance: use these imperatives **sparingly** and **only** where required for interoperation or to limit potentially harmful behavior—not to impose a preferred method when interoperability does not require it. Security section: failing a MUST/SHOULD (or doing MUST NOT/SHOULD NOT) can have subtle security effects; authors should elaborate implications. [E1: RFC 2119 §§6–7]
- `FACT` [E1] — Note: RFC page states it was updated by **RFC 8174** (clarifies that only **uppercase** keywords carry the special meanings when lower-case uses are also present). Researchers should treat lowercase “must/should” in product prose as ordinary English unless the doc adopts 2119/8174 explicitly. [E1: RFC 2119 info header on rfc-editor page; RFC 8174 not fully re-fetched this pass — mark partial]
- `INFERENCE` [E4] — For Theme 3 **D3** (prefer contracts for API / behavioral truth): RFC 2119 keywords in **official / normative** docs are a **trust and weight signal**, not proof of runtime truth.

  Practical weighting for docs research:
  1. Doc that **declares** RFC 2119/8174 interpretation + uses capitalized MUST/SHOULD → treat normative claims as higher-commitment **contract language** (still corroborate with schema/code/tests under D12).
  2. Capitalized MUST without incorporation phrase → likely intending IETF-style force; still weaker than an explicit BCP 14 adoption statement.
  3. lowercase must/should in tutorials/how-tos → **guidance**, not absolute contract; prefer OpenAPI/IDL/reference + executable checks for behavioral truth (aligns D3).
  4. Absence of 2119 discipline does **not** prove docs are untrustworthy; presence does **not** override E0 code/runtime on conflict.

  Premises: RFC 2119 definitions + sparingly guidance [E1]; D3 prefers contracts/reference over tutorials [E0 Theme 3 report / `t3b`]; docs↔code conflict prefers E0 when contradicted [E0 `t3d`].

### 3.4 Optional — Schemathesis & Spectral for D12 (T3-G15)

- `FACT` [E1] — **Schemathesis** generates property-based tests from OpenAPI (2.0/3.x) or GraphQL schemas; validates responses against the schema; detects schema violations / crashes / edge cases; integrates CLI, pytest, CI (GitHub Action, Docker). Schema is treated as the source of test generation. [E1: https://schemathesis.io/ and https://github.com/schemathesis/schemathesis README — accessed 2026-07-27]
- `INFERENCE` [E4] — For **D12 (corroborate & execute)**: when a project publishes OpenAPI, Schemathesis is a strong **executable contract** check that the implementation matches documented request/response shapes—complementing Dredd-class tools already noted in Theme 3. Premises: Schemathesis primary claims [E1]; Theme 3 D12 OpenAPI contract-testing candidate [E0 `t3d`].

- `FACT` [E1] — **Spectral** (Stoplight) is a JSON/YAML linter with ready rulesets for OpenAPI v2/v3.x, AsyncAPI, and Arazzo; requires a ruleset (e.g. `.spectral.yaml` extending `spectral:oas`); `spectral lint` enforces style/quality and structural rules on the API description itself (not live HTTP fuzzing). [E1: https://raw.githubusercontent.com/stoplightio/spectral/develop/README.md — accessed 2026-07-27]
- `INFERENCE` [E4] — For **D12**: Spectral catches **description-quality / style-guide / structural** issues before or beside runtime contract tests; Schemathesis exercises **runtime conformance**. Use Spectral for static OpenAPI hygiene; Schemathesis (or Dredd) for live verify. Premises: Spectral README [E1]; D12 execute-contracts step [E0 Theme 3].

### 3.5 Conflict-log field schema (T3-O2)

Grounded in Theme 3 `t3d` candidate fields + PROTOCOL labels + READU-style contradiction recording + OpenAI “cite conflicts” (via Theme 2). **Local convention only** — not an external standard.

- `INFERENCE` [E4] — Proposed **conflict-log** entry schema for `documentation-research` / docs↔code corroboration:

| Field | Required | Type / values | Purpose |
|-------|----------|---------------|---------|
| `conflict_id` | yes | stable string | Merge / reference |
| `recorded_at` | yes | ISO date or datetime | Freshness |
| `doc_locator` | yes | URL, path, heading path, or PROTOCOL citation | Where the doc claim lives |
| `doc_quote` | recommended | short verbatim span | Human/machine audit; optional if `chunk_id` + paraphrase clearly labeled |
| `doc_claim` | yes | atomic statement tagged `DOC_CLAIM` | Hypothesis from docs |
| `code_locator` | if code side | path + symbol / lines | Internal corroboration target |
| `command` | if runtime | shell/test command observed | E0 execution evidence |
| `schema_path` | if contract | OpenAPI/JSON Schema path or operationId | Contract-first projects |
| `observation` | yes | free text + `MATCH`\|`MISSING`\|`RENAMED`\|`AMBIGUOUS`\|`CONTRADICTED` | What was seen |
| `winner` | yes | `code` \| `schema` \| `doc` \| `unresolved` | Authority call for “what is true now” |
| `evidence_grades` | yes | e.g. `{doc: E1, observation: E0}` | PROTOCOL grades on each side |
| `claim_labels` | recommended | FACT/CLAIM/… on surviving assertion | Post-resolution labeling |
| `status` | yes | `open` \| `resolved` \| `stale_doc` \| `stale_code` \| `needs_human` | Workflow |
| `repair_suggestion` | recommended | `update_docs` \| `fix_code` \| `update_schema` \| `unknown` | Explicitly human-decided when unsure |
| `citations` | yes | list of PROTOCOL-style cites | Both sides retained; never silent-drop |
| `prov_note` | optional | light PROV: entities/activity/agent ids | Optional link to §3.2 vocabulary |

  Premises: `t3d` §6.1 step 7 candidate fields [E0]; PROTOCOL conflict = cite both, prefer higher grade [E0]; READU contradictory-facts shape [E1 via `t3d`]; OpenAI cite-conflicts [E1 via Theme 2]; D3/D12 winner prefers code/schema/runtime when docs conflict [E4 `t3d`].

## 4. Contradictions / conflicts found

| Topic | Tension | Resolution for GreyMatter notes |
|-------|---------|----------------------------------|
| Quote spans vs chunk IDs | Transparent-RAG (E2) prefers fine-grained spans; ALCE/RAGAS/PROTOCOL operate at passage/`chunk_id` | Spans optional; chunk_id+grade default [§3.1] |
| Dual JSON always vs markdown-only | Structured claims aid eval; dual payloads can drift | JSON optional; required only for machine audit paths [§3.1] |
| RFC 2119 MUST vs runtime | Normative prose can still be stale vs code | D3 weights keywords; D12/E0 wins on conflict [§3.3] |
| Spectral vs Schemathesis | Both “OpenAPI quality” | Static lint vs runtime property tests — complementary [§3.4] |

## 5. Gaps

- `GAP` — Portable industry evidence-span schema still not found (Theme 2 G1 remains).
- `GAP` — RFC 8174 full text not re-fetched; only noted as updater of 2119.
- `GAP` — Schemathesis ReadTheDocs stable index timed out; claims taken from official site + GitHub README.
- `GAP` — Spectral hosted concepts doc 404; claims taken from official GitHub README.
- `OPEN` — Whether conflict-log should live as YAML frontmatter, table in markdown, or JSONL sidecar when skills are elevated (product/format choice — deferred).

## 6. Candidate patterns for templates (still cited)

1. **Claim locator default** — Require `chunk_id` or URL+section + grade; quote span optional. [§3.1 E4]
2. **claims[] emission** — Optional sidecar; SHOULD when faithfulness/merge automation expected. [§3.1 E4]
3. **PROV light mapping** — Use Entity/Activity/Agent + wasDerivedFrom/wasAttributedTo vocabulary in Method/provenance blurbs; no mandatory RDF. [§3.2 E1+E4]
4. **D3 keyword scan** — Note whether docs adopt RFC 2119/8174; weight capitalized MUST/SHOULD as normative intent, then corroborate. [§3.3 E4]
5. **D12 OpenAPI toolkit** — Spectral (lint description) + Schemathesis or Dredd (runtime). [§3.4 E1]
6. **Conflict-log table** — Use §3.5 field set in `documentation-research` template. [§3.5 E4]

## 7. Source list (deduped)

**Local (E0)**  

- `d:\GreyMatter\docs\research\PROTOCOL.md`  
- `d:\GreyMatter\docs\research\SECONDARY_PRIORITIES.md`  
- `d:\GreyMatter\docs\research\reports\theme-2-agent-usable-documentation.md`  
- `d:\GreyMatter\docs\research\reports\theme-3-researching-documentation.md`  
- `d:\GreyMatter\docs\research\notes\theme-2\t2a-grounding-citation-rag.md`  
- `d:\GreyMatter\docs\research\notes\theme-2\t2c-anti-assumption-provenance.md`  
- `d:\GreyMatter\docs\research\notes\theme-3\t3b-official-docs-reading-methods.md`  
- `d:\GreyMatter\docs\research\notes\theme-3\t3d-docs-vs-code-verification.md`  
- `d:\GreyMatter\docs\research\templates\claim-citation.md`  

**Primary web (E1)**  

- W3C PROV-DM — https://www.w3.org/TR/2013/REC-prov-dm-20130430/ (and https://www.w3.org/TR/prov-dm/)  
- W3C PROV-O — https://www.w3.org/TR/prov-o/  
- RFC 2119 — https://www.rfc-editor.org/rfc/rfc2119  
- RAGAS Faithfulness — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/  
- Schemathesis — https://schemathesis.io/ ; https://github.com/schemathesis/schemathesis  
- Spectral — https://github.com/stoplightio/spectral (develop README)  
- ALCE / Azure file search — via Theme 2 `t2a` (not re-fetched this pass)

**Alexandria**  

- `rag_query` on PROV — no W3C PROV hit; unused for standard claims
