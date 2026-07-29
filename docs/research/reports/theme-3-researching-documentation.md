# Theme 3 — Researching documentation (integrated report)

**Date:** 2026-07-27  
**Status:** integrated  
**Protocol:** `docs/research/PROTOCOL.md`  
**Integrator scope:** Theme 3 only — merge listed notes; no new facts; no plugin stub; no MVP locks.

## Sources (merged)

| ID | Path | Role |
|----|------|------|
| N-T3A | `docs/research/notes/theme-3/t3a-alexandria-docs-research.md` | Alexandria: docs quality, living docs, RAG-over-docs pitfalls |
| N-T3B | `docs/research/notes/theme-3/t3b-official-docs-reading-methods.md` | Official reading methods: Diátaxis, version pin, contracts, `llms.txt` |
| N-T3C | `docs/research/notes/theme-3/t3c-forums-issues-limitations.md` | Limitation scan: issues/forums/changelogs; E3→E0/E1 ladder |
| N-T3D | `docs/research/notes/theme-3/t3d-docs-vs-code-verification.md` | Docs↔code drift, executable docs, conflict resolution |
| C-T3 | `docs/research/sources/coordinator-t3-docs-research-kickoff.md` | Coordinator kickoff: PROTOCOL E3 exception, Docs as Code, drift |

**Cross-links only (not re-researched):**  
- Theme 1 report: `docs/research/reports/theme-1-codebase-research-for-agents.md` (docs as beacons; recon → verify)  
- Theme 2 report: `docs/research/reports/theme-2-agent-usable-documentation.md` (Diátaxis layers; E1 docs vs E0; cite conflicts)

Integrator method: merge notes only; conflicts resolved by higher evidence grade; remaining conflicts and all `GAP`/`OPEN` retained.

---

## 1. Executive summary

1. Critically researching software docs is a **composed protocol** (version pin → Diátaxis classify → contracts/reference → deltas → E3 limitation scan → docs↔code verify)—not a single vendor “how to read docs” standard. [N-T3B GAP; E4 composition]
2. Pin **docs version to installed product version**; treat RTD `latest` as development foreshadowing unless researching unreleased APIs. [N-T3B E1 RTD/SemVer; N-T3C E4]
3. Diátaxis trust order for *behavioral/API truth*: **reference / machine contracts** > how-to (path-specific) > explanation (intent) > tutorial (orientation only). [N-T3B E1 + E4]
4. `llms.txt` is a **navigation index** for agents, not API truth; prefer linked reference/OpenAPI/`.md` pages. [N-T3B E1; Theme 2 cross-link]
5. PROTOCOL: **E3** (issues/forums) is first-class for *discovering* limitations/outdated docs, but **cannot alone lock design**—promote via E0/E1. [E0 PROTOCOL; N-T3C; C-T3]
6. Docs drift is common and often **silent** (no crash): Tan et al. report high rates of outdated code-element refs; Aghajani taxonomy validates community channels as discovery surfaces. [N-T3C/N-T3D E1]
7. Prefer **changelog + SemVer** over git logs / marketing release notes for “what changed”; search known-issues/limitations when present. [N-T3B/N-T3C E1]
8. Executable examples (doctest, rustdoc, OpenAPI contract tests) turn a *subset* of doc claims into fail-loud contracts; prose still needs consistency checks. [N-T3D E1]
9. On docs↔code conflict for “what the system does now”: prefer **E0 runtime/code** (and machine schemas when contract-first); keep the E1 citation marked contradicted—do not silently drop it. [N-T3D E4; Theme 2 SoT]
10. RAG-over-docs needs freshness hygiene (remove stale, timestamp filters, cascade embedding deletes, return sources); outdated retrieved context can *win* over better parametric knowledge. [N-T3A E2 Pai/McGrattan]
11. Docs-as-code (VCS, review, co-location) lowers staleness risk but **does not alone prevent drift**—verification still required. [N-T3B E1 WTD; C-T3 E2 Sourcegraph]
12. Named “documentation-driven development” and a universal vendor “OpenAPI beats human reference” rule were **not** found as E1 this pass—remain `GAP`/`OPEN`. [N-T3A; N-T3B]

---

## 2. Unified documentation research protocol (D0–D14)

Ordered steps for researching *public / product / project documentation*. Full sequence is `INFERENCE` [E4] composed from N-T3B §6, N-T3C §6.1, N-T3D §6.1, and N-T3A candidate patterns—no single primary lists this exact GreyMatter checklist.

| Step | Agent action | Evidence |
|------|--------------|----------|
| **D0 — Identity & version pin** | Record product/package name, homepage, docs root. Capture **installed version** (E0: CLI/`--version`/package manager) and **docs version or URL slug** (RTD flyout / `/en/vX.Y/` / `latest`\|`stable`). Flag skew if `installed ≠ docs`. | `FACT` [E1 N-T3B RTD Versions; SemVer]; `INFERENCE` [E4 N-T3C §3.7] |
| **D1 — Locate entry indexes** | Open official docs home; optional `/llms.txt` + `.md` mirrors; repo `docs/` / tagged release docs if docs-as-code. | `FACT` [E1 N-T3B llmstxt.org; Write the Docs Docs as Code; AWS DL.EAC.5] |
| **D2 — Classify with Diátaxis compass** | Before extracting claims, label each page: tutorial / how-to / reference / explanation (action×cognition × acquisition×application). Do not mix roles when citing. | `FACT` [E1 N-T3B Diátaxis compass; SWE book singular purpose via N-T3B] |
| **D3 — Prefer contracts for API / behavioral truth** | Prefer OpenAPI/IDL/generated or hand-written **reference**; treat tutorials/quickstarts as non-exhaustive. Use how-tos only for the matched goal path. | `FACT` [E1 N-T3B OAS; Diátaxis reference; Learn OpenAPI companion; Microsoft developer-content]; `INFERENCE` [E4 N-T3B §3.1] |
| **D4 — Read deltas / upgrades** | Read Keep a Changelog (or equivalent) + SemVer major/minor for the span of interest; note Deprecated→Removed and Breaking; prefer changelog over git log / marketing release notes. | `FACT` [E1 N-T3B Keep a Changelog; SemVer]; `INFERENCE` [E4 N-T3C §3.6] |
| **D5 — Official limitation surfaces (E1 first)** | Search CHANGELOG/Releases/NEWS, migration/breaking-changes guides, and any “Known issues” / Limitations / Compatibility / Status page for the version range. Record `GAP` if absent. | `FACT` [E1 N-T3C Keep a Changelog; SemVer]; `GAP` [N-T3C known-issues not standardized] |
| **D6 — Canonicalization** | Prefer docs co-owned with code (same VCS, owners, PR review) over orphaned wikis; deprecate duplicate copies when evaluating freshness. | `FACT` [E1 N-T3B SWE ch.10; WTD Docs as Code; AWS DL.EAC.5]; `FACT` [E1 N-T3D WTD Nearby/Unique] |
| **D7 — E3 limitation scan (discovery only)** | Search GitHub Issues/Discussions (docs labels, bugs, `reason:"not planned"`), vendor forums, SO for symptoms/version strings. Capture URL, date, claimed versions, maintainer stance. Grade as `CLAIM` [E3]. | `FACT` [E1 N-T3C GitHub search docs; Aghajani]; `FACT` [E0 PROTOCOL E3 exception]; cookbook [N-T3C §6.3] |
| **D8 — E3→E0/E1 corroboration ladder** | Promote only after: version match → changelog/release ack → local reproduce (E0) and/or source/tests/PR (E0/E1). Classify failure mode (product bug / docs drift / version skew / won’t-fix / user error). If only E3 remains → `CLAIM`/`OPEN`; **do not lock design**. | `INFERENCE` [E4 N-T3C §3.8]; `FACT` [E0 PROTOCOL] |
| **D9 — Anti-pattern self-check** | Reject single angry unreproduced reports; do not ignore “not planned”; do not confuse docs bug vs product bug; do not cite fixed issues against older installs; do not prefer forum over changelog when both exist; do not treat staff “tracking” as shipped. | `FACT`/`INFERENCE` [N-T3C §3.9] |
| **D10 — Docs as hypotheses (beacons)** | Ingest README / architecture / AGENTS.md / relevant how-to+reference as **DOC_CLAIM** hypotheses—not ground truth. (Theme 1 beacons: useful but can be false when drifted.) | `INFERENCE` [E4 N-T3D §3.6]; Theme 1 report cross-link; `FACT` [E1 N-T3D WTD Current] |
| **D11 — Extract checkable atoms** | Paths, symbols, CLI commands, env vars, API routes, version pins, code fences—prefer greppable/executable/schema-validatable atoms. | `FACT` [E1 N-T3D Tan element-refs; READU] |
| **D12 — Corroborate & execute** | Internal: code search / file exist / signature / config → `MATCH`\|`MISSING`\|`RENAMED`\|`AMBIGUOUS`. External: only if docs assert package/URL/API facts. Execute doctests / doc tests / smoke commands / OpenAPI contract tests when available. | `FACT` [E1 N-T3D Python doctest; rustdoc; Dredd; READU]; Theme 1 agents.md verify commands |
| **D13 — Resolve authority & record conflict** | On conflict for current behavior: prefer E0 code/runtime (+ machine schemas if contract-first); keep E1 citation with status `CONTRADICTED_BY_E0` / `STALE`. Never invent; cite both sides. Optional verifier pass that corroboration actually ran. | `INFERENCE` [E4 N-T3D §3.4–3.5]; Theme 2 cite-conflicts; `FACT` [E2 N-T3D Clean Code comments]; `FACT` [E1 N-T3D WTD Current] |
| **D14 — Freshness / RAG hygiene (if retrieving docs)** | Prefer timestamped/versioned sources; remove or filter stale KB entries; cascade deletes to embeddings; return source citations; treat retrieval↔model contradictions as need for higher-authority check (D12–D13), not silent merge. | `FACT` [E2 N-T3A Freed/Kimothi/Dhyani/McGrattan/Pai/Brener]; `INFERENCE` [E4 N-T3A] |

---

## 3. How to read official docs

### 3.1 Diátaxis types (select before extracting claims)

| Type | User need | Research use | Trust for full API / edge cases |
|------|-----------|--------------|----------------------------------|
| **Tutorial** | Learn / acquire skill | Orientation; single reliable path; minimize alternatives | **Low** — not for exhaustive API truth |
| **How-to** | Get a real-world job done | Task path for a competent user | **Medium** — path-specific; may omit options |
| **Reference** | Facts while working | Consult for truth/certainty; map ↔ territory; may be auto-generated | **High** for parameters/behavior |
| **Explanation** | Understand why | Intent / mental model / design | **High** for intent; **not** for parameter tables |

Compass (action/cognition × acquisition/application) decides type. Mixing expansive “why” into reference harms both. Auto-generated API reference is powerful for fidelity but is still only the reference quadrant—not all documentation. [E1 N-T3B Diátaxis pages]

**Default trust order for behavioral/API truth** (`INFERENCE` [E4 N-T3B]): reference + machine contracts > how-to > explanation > tutorial.

Fuchsia/Google/Microsoft align on separating procedures/concepts/reference; Microsoft foundations developer docs on **reference + code examples**. [E1 N-T3B]

### 3.2 Version pin

- Read the Docs hosts multiple versions so users can read docs for the **specific version** they run; `latest` → default branch (often main); `stable` → greatest stable SemVer (excludes pre-releases); root redirect uses project **Default version** (platform default often `latest`; many projects reconfigure to `stable`—**check, do not assume**). [E1 N-T3B/N-T3C RTD]
- SemVer: released versions MUST NOT be modified; MAJOR = incompatible; deprecations via docs + minor before removal in major. [E1 SemVer via N-T3B/N-T3C]
- Anti-pattern: reading `latest` docs while running an older install (or vice versa) fabricates false docs bugs or product bugs. [E4 N-T3C]

### 3.3 Reference vs tutorial (and OpenAPI)

- OAS: a proper OpenAPI Description lets consumers interact **without** requiring source, additional docs, or traffic inspection; Learn OpenAPI is a **companion**—always refer to the OAS text for format reference; human docs can be generated from the machine description. [E1 N-T3B]
- For *product* API truth when an OpenAPI Description is maintained: prefer OpenAPI paths/schemas/parameters over narrative tutorials; use tutorials for workflows/side effects not in the contract. [E4 N-T3B]
- `OPEN`/`GAP`: no single E1 vendor page globally declaring “OpenAPI always wins over human reference” when they conflict—resolve per product source-of-truth statement. [N-T3B]

### 3.4 `llms.txt`

- Proposal: `/llms.txt` Markdown index (H1 name required; optional summary; H2 file lists; `Optional` section skippable) for LLM inference under small context windows; companion clean `.md` URLs. [E1 N-T3B llmstxt.org]
- Treat as **index only**; still choose which linked page is normative via Diátaxis/contracts. Aligns with Theme 2 discovery-layer framing. [E4 N-T3B; Theme 2 report]

### 3.5 Docs-as-code (research implication)

Write the Docs: same tools as code (Git, markup, reviews, automated tests); can block merges without docs. Prefer VCS-co-evolving sources over orphaned copies. [E1 N-T3B; C-T3] AWS DL.EAC.5 echoes versioned machine-readable docs in the releasable branch. [E1 N-T3B]

---

## 4. Limitation scan + E3 corroboration + anti-patterns

### 4.1 Why scan community channels

- PROTOCOL: E3 is first-class *discovery* for limitations/bugs/outdated behavior; still not alone for design locks. [E0 PROTOCOL; C-T3]
- Aghajani et al. (ICSE 2019): mined 878 documentation-related artifacts from mailing lists, SO, issues, PRs—community channels are a validated discovery surface. [E1 N-T3C]
- Tan et al. (EMSE 2024): up-to-dateness ≈ **39%** of documentation *content* issues (via Aghajani); docs stale “silently”; **28.9%** of most popular studied projects had ≥1 outdated code-element reference currently; **82.3%** historically. [E1 N-T3C/N-T3D]

### 4.2 Surfaces to scan (ordered)

1. **E1 first:** CHANGELOG / Releases / migration / known-issues / deprecations for version span. [N-T3C]
2. **Issues:** `is:issue`, labels `bug`/`documentation`/`docs`, `reason:"not planned"`, date/`comments:`/`reactions:` filters; `gh issue list --search`. Nested boolean better on repo Issues UI than assuming identical global search. [E1 N-T3C]
3. **Discussions:** prefer `is:answered` + maintainer answers as stronger E3 leads; Discussions are pre-issue. [E1 N-T3C]
4. **Forums / SO:** discover symptoms and version strings; accepted/high-score still E3. Cursor forum staff “known” replies are E3 until mirrored in E1 or reproduced E0. [N-T3C CLAIM examples]

### 4.3 E3→E0/E1 corroboration ladder

| Step | Action | Grade if successful |
|------|--------|---------------------|
| 1 | Capture E3 lead (URL, date, version claims, maintainer stance) | E3 `CLAIM` |
| 2 | Match installed vs docs vs report versions | E0 if observed locally |
| 3 | Search changelog / release / migration for acknowledgment | E1 if official |
| 4 | Reproduce minimal case | E0 |
| 5 | Inspect source / tests / linked PR (if OSS) | E1/E0 |
| 6 | Only E3 remains | Keep `CLAIM`/`GAP`/`OPEN` — **no design lock** |

**Failure-mode taxonomy** [E4 N-T3C]: product bug | docs bug/drift | version skew | won’t-fix / not planned limitation | user error / env.

### 4.4 Anti-patterns

| Anti-pattern | Prefer |
|--------------|--------|
| One angry issue as fact | Multiplicity + maintainer ack + corroboration |
| Ignore `reason:"not planned"` / Won’t Fix | Cite close reason as intentional limitation candidate |
| Confuse docs bug vs product bug | Reproduce against SoT (code vs docs page) |
| Cite closed-fixed issue on older install | Diff versions; read Fixed in changelog |
| Prefer forum over changelog when both exist | Changelog/release first for deltas |
| Assume `latest` docs = installed | Pin docs to install |
| Staff “we’re tracking it” = shipped fix | Keep OPEN until release notes or E0 |

---

## 5. Docs↔code verification

### 5.1 Drift / bitrot

- Outdated docs mislead users/developers and age silently; Write the Docs **Current**: incorrect documentation worse than missing; **Nearby** (colocate with code); **Unique** (avoid parallel maintenance); **ARID** (some repetition inevitable). [E1 N-T3D]
- READU: README bugs = factually incorrect *repository-level* docs; detect as **inconsistencies** vs internal (code/config/docs) or external (dependency APIs) SoTs—often no executable oracle. [E1 N-T3D]
- Clean Code (comments): inaccurate comments worse than none; truth in code. [E2 N-T3D] Scope differs from Diátaxis published reference (see Conflicts).
- Docs-as-code alone does not prevent drift; agents treating docs as ground truth and rewriting docs to match inferences is a risk—verify against code. [C-T3 E2 Sourcegraph]
- Alexandria living-docs patterns: domain tests as executable docs; generate API from comments for libraries; link Gherkin instead of duplicating feature lists; cross-check AI library suggestions against official docs. [E2 N-T3A]

### 5.2 Executable docs / examples as contracts

- Python `doctest`: interactive sessions in text/Markdown as literate/executable documentation. [E1 N-T3D]
- rustdoc: doc examples compile+run as tests (`ignore`, `no_run`, `compile_fail`, etc.); README includable under `#[cfg(doctest)]`. [E1 N-T3D]
- Dredd: validate API Blueprint/OpenAPI description against live backend. [E1 N-T3D]
- Mark fences: `executable` | `illustrative` | `anti-example`. [E4 N-T3D from rustdoc/doctest]
- Only a **subset** of claims are executable; consistency/search covers the rest. [E4 N-T3D; READU]

### 5.3 Conflict resolution (docs vs code)

**Layered authority (candidate, not product lock)** [E4 N-T3D]:

1. **E0** runtime / code / schema / tests → “what the system does now”
2. **Machine contracts** (OpenAPI, JSON Schema, typed signatures, passing doctests) over untested prose
3. **E1 narrative docs** for intent/how-to/declared API *when not contradicted*
4. On conflict: prefer code/runtime; cite both; mark docs `CONTRADICTED`/`STALE`; do not silently trust README

Spec-first APIs may treat the description as intended contract (implementation defective relative to it)—**record which process the project uses**; if unspecified, GreyMatter research default: E0 observed behavior + note whether a machine contract exists. [N-T3D Conflicts]

Theme 2 alignment: cite docs as E1; if contradicted by E0, demote the **assertion**, not the URL. [N-T3D; Theme 2 report]

### 5.4 Agent workflow (docs-first → verify)

Read docs as beacon hypotheses → extract atoms → corroborate via search/read → run examples/contracts → schema/runtime checks → record E0 vs E1 conflicts → skeptical verifier pass. [E4 N-T3D; Theme 1 recon/verify; Theme 2 verifier subagent citation via N-T3D]

---

## 6. Conflicts table

| Conflict | Sources | Resolution for integrator |
|----------|---------|---------------------------|
| Where API “truth” lives (generated API vs tests vs README) | N-T3A Silen vs Taulli TOC | **Audience split**: library consumers → generated API from comments; in-repo developers → tests/implementation + README. Not a hard conflict. |
| Tests as living docs vs coupling cost | N-T3A Percival/Gregory vs Silen | Living docs valuable; document gear—prefer lower-coupling layers for routine change. |
| Retrieved docs vs parametric memory under contradiction | N-T3A Pai / Liu et al. | Models often prefer prompt/retrieved content; outdated retrieval can win. Requires freshness/authority gating (D14 + D13)—design conflict remains open. |
| AI-drafted docs vs sync burden | N-T3A Winteringham/Taulli/Osmani | Generation ≠ verification; treat AI docs as drafts under same sync rules. |
| Clean Code “code is only truth” vs Diátaxis “authoritative reference” | N-T3D | Different scopes: comments next to evolving code vs published reference that *should* mirror product (ideally generated). Agents: code/runtime wins on factual conflict; fix/regenerate reference. |
| Dredd “description as oracle” vs “code wins” | N-T3D | Spec-first vs code-first process; if unspecified, prefer E0 + note contract existence. |
| Changelog as SoT vs incomplete changelogs | N-T3C Keep a Changelog | Good changelog *ought* to be SoT; inconsistent ones mislead. Absence of Fixed ≠ proof bug open—check Releases/commits/issues. |
| Nested boolean search (Issues UI) vs global qualifier docs | N-T3C | Do not assume identical boolean support everywhere. |
| Vendor forum “known” vs official docs lag | N-T3C Cursor E3 examples | Stronger than random posts still E3 until E1 or E0. |
| Keep a Changelog human-only vs OpenAPI/`llms.txt` machine formats | N-T3B | Compatible if roles stay separate (delta vs contract vs index). |
| RTD default `latest` vs projects pointing default at `stable` | N-T3B | Researchers must check project default. |
| Human reference vs OpenAPI when they disagree | N-T3B | Remains `OPEN`/`GAP`—product-specific SoT statements. |

---

## 7. Gaps & OPEN (deduped)

| ID | Item | Origin |
|----|------|--------|
| G1 | No single primary “Documentation Research Protocol” from Google/Microsoft/AWS analogous to Diátaxis for *reading* | N-T3B |
| G2 | Named **documentation-driven development** / docs-before-code as first-class method absent in Alexandria this pass | N-T3A |
| G3 | Formal docs quality metrics / readability suites weak | N-T3A |
| G4 | Dedicated docs↔code CI (doctest-as-CI for prose) weakly evidenced in Alexandria; stronger via web E1 (doctest/rustdoc) | N-T3A; N-T3D |
| G5 | No vendor-agnostic E1 “limitation scan checklist” standard; practice composed | N-T3C |
| G6 | “Known issues” page locations not standardized across ecosystems | N-T3C |
| G7 | Global “OpenAPI beats human reference” E1 rule not found | N-T3B |
| G8 | ~~IETF RFC 2119… not surveyed~~ **Closed secondary** — see sec-p1 | N-T3B |
| G9 | Sphinx/MkDocs/Docusaurus versioning UX not deeply fetched | N-T3B |
| G10 | Stack Overflow Help page fetch timed out (operators from search synthesis) | N-T3C |
| G11 | Cursor official changelog fetch timed out | N-T3C |
| G12 | ~~Write the Docs “Testing your documentation” timed out~~ **Closed secondary** | N-T3D; sec-p0 |
| G13 | Full Aghajani 2019 text: T3C fetched preprint; T3D only via Tan citation | N-T3C/N-T3D |
| G14 | MIUCC 2025 drift-detection survey full text not retrieved | N-T3D |
| G15 | ~~Schemathesis/Spectral official docs not fetched~~ **Narrowed secondary** — Schemathesis RTD + Spectral overview | N-T3D; sec-p1 |
| G16 | No GreyMatter-local E0 experiment running doctest/rustdoc/Dredd this pass | N-T3D |
| G17 | Alexandria weak on named “documentation drift” / E3 issue reports; web E1 carried epidemiology | N-T3A; N-T3C; N-T3D |
| G18 | Agent critical-evaluation **rubric checklist** for doc sources not found as such | N-T3A |
| O1 | Per-ecosystem known-issues URL catalog (npm, PyPI, crates, NuGet, Unity, …) | N-T3C |
| O2 | ~~Preferred conflict-log schema fields~~ **Closed [E4]** — `templates/claim-citation.md` | N-T3D; sec-p1 |
| O3 | Whether to automate GitHub search as a skill vs checklist-only | N-T3C (out of research lock scope) |
| O4 | Diátaxis / Docs as Code / README-driven / ADR-first as explicit DDD-for-docs pattern if templates need it | N-T3A |
| O5 | Coordinator: GitHub filtering-issues URL 404 this kickoff—classic qualifier docs OK in N-T3C; semantic Issues search GA noted in C-T3 | C-T3; N-T3C |

---

## 8. Implications for GreyMatter templates (INFERENCE only)

Candidate template payloads—**not design locks**. Premises: D0–D14 composition + N-T3A/B/C/D §6 patterns + PROTOCOL E3 exception.

1. **Docs research checklist** encoding D0–D14 with mandatory version-pin fields `(installed_version, docs_version_or_URL, changelog_span)`.
2. **Diátaxis claim tag** on every extracted assertion (`tutorial`\|`how-to`\|`reference`\|`explanation`) before trust weighting.
3. **Limitation-scan submodule** with GitHub/SO/forum query cookbook + E3→E0/E1 ladder + anti-pattern self-check (N-T3C §6.1).
4. **Docs↔code corroboration pass** with `DOC_CLAIM` → atoms → `MATCH/MISSING/...` → executable contracts → conflict record (`doc_locator`, `doc_quote`, `code_locator`, `winner`, `evidence_grades`).
5. **Examples-as-contracts policy** marking fences executable/illustrative/anti-example.
6. **Beacon hygiene link to Theme 1:** after recon, list README/architecture beacons confirmed / revised / abandoned.
7. **Theme 2 citation discipline:** E1 docs URLs retained; contradicted assertions labeled `CONTRADICTED_BY_E0`.
8. **RAG ingestion hygiene** (if GreyMatter retrieves third-party docs): stale removal, timestamps, embedding cascade, source return, contradiction → escalate to D12–D13.
9. **Repo docs skeleton** (when *authoring* GreyMatter docs later): README + `docs/`; prefer generated API / linked executable features over duplicated prose—still a candidate from N-T3A, not a lock.
10. Do **not** lock: RAG library choice, plugin stub, MVP scope, or “OpenAPI always wins” without per-product SoT.

---

## 9. Source index

### Protocol / local reports

| Source | Grade | Via |
|--------|-------|-----|
| `docs/research/PROTOCOL.md` | E0 | All |
| `docs/research/reports/theme-1-codebase-research-for-agents.md` | Cross-link | N-T3D |
| `docs/research/reports/theme-2-agent-usable-documentation.md` | Cross-link | N-T3D |
| Notes N-T3A…D; source C-T3 | — | This report |

### Official / primary web (E1)

| Source | URL |
|--------|-----|
| Diátaxis (home, start-here, tutorials, how-tos, reference, explanation, compass, …) | https://www.diataxis.fr/ |
| Write the Docs — Docs as Code | https://www.writethedocs.org/guide/docs-as-code/ |
| Write the Docs — Documentation principles | https://www.writethedocs.org/guide/writing/docs-principles/ |
| llms.txt | https://llmstxt.org/index.md |
| Keep a Changelog 1.1.0 / 2.0.0 | https://keepachangelog.com/ |
| Semantic Versioning 2.0.0 | https://semver.org/spec/v2.0.0.html |
| Read the Docs — Versions | https://docs.readthedocs.com/platform/latest/versions.html |
| OpenAPI Specification v3.2.0 | https://spec.openapis.org/oas/v3.2.0 |
| OpenAPI Learn | https://learn.openapis.org/ |
| Google developer style guide | https://developers.google.com/style |
| Fuchsia documentation types | https://fuchsia.dev/fuchsia-src/contribute/docs/documentation-types |
| SWE at Google — Documentation (ch.10) | https://abseil.io/resources/swe-book/html/ch10.html |
| Microsoft Writing Style Guide — Developer content | https://learn.microsoft.com/en-us/style-guide/developer-content/ |
| Microsoft Open Specs MS-DOCO | https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-doco/85e7630a-9dd5-462c-98ed-ce5451567c6d |
| AWS Well-Architected DevOps DL.EAC.5 | https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.5-integrate-technical-and-operational-documentation-into-the-development-lifecycle.html |
| GitHub — Searching issues and PRs | https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests |
| GitHub — Searching discussions | https://docs.github.com/en/search-github/searching-on-github/searching-discussions |
| GitHub — Discussions best practices | https://docs.github.com/en/discussions/guides/best-practices-for-community-conversations-on-github |
| GitHub — Filtering/searching issues | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests |
| GitHub Blog — nested Issues queries | https://github.blog/developer-skills/application-development/github-issues-search-now-supports-nested-queries-and-boolean-operators-heres-how-we-rebuilt-it/ |
| GitHub Changelog — Issues search GA (2026-04-02) | https://github.blog/changelog/2026-04-02-improved-search-for-github-issues-is-now-generally-available/ |
| Stack Overflow — How do I search? | https://stackoverflow.com/help/searching |
| Aghajani et al. ICSE 2019 preprint | https://csnagy.github.io/research/pdfs/2019/Aghajani2019-preprint.pdf |
| Tan et al. EMSE 2024 | https://link.springer.com/article/10.1007/s10664-023-10397-6 |
| READU (Baek et al.) | https://arxiv.org/html/2607.15780v1 |
| Python doctest | https://docs.python.org/3/library/doctest.html |
| rustdoc Documentation tests | https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html |
| Dredd | https://dredd.org/en/latest/ |
| Cursor Subagents (via Theme 2 / N-T3D) | https://cursor.com/docs/subagents |
| OpenAI Citation Formatting (via Theme 2 / N-T3D) | https://developers.openai.com/api/docs/guides/citation-formatting |

### Alexandria (E2) — representative

| Corpus | Works (high-signal for Theme 3) |
|--------|----------------------------------|
| `software_engineering` | Silen *Clean Code Principles…*; Osmani *Beyond Vibe Coding*; RSE with Python; Percival/Gregory *Architecture Patterns with Python*; Taulli *AI-Assisted Programming*; Winteringham *Software Testing with Generative AI*; Martin *Clean Code* |
| `ai_llm_agents` | Pai *Designing LLM Applications*; Josyula et al. *Mastering RAG*; Brener *Mastering RAG for AI Agents*; Kimothi *Simple Guide to RAG*; Dhyani *RAG with Python Cookbook*; McGrattan *Vector Databases…*; Freed et al. *Effective Conversational AI* |

### E3 / secondary (discovery only — not design locks)

| Source | Role |
|--------|------|
| Cursor Community Forum threads (docs indexing; chat migration) | E3 leads [N-T3C] |
| Promptless / Mintlify / Fern / devonair docs-drift blogs | E3 practitioner [N-T3C; N-T3D] |
| Sourcegraph docs-as-code blog; Docsie glossary | E2/E3 [C-T3] |
| Staleguard / sync-docs product claims | E3 until E0 [C-T3] |

---

*End of Theme 3 integrated report.*
