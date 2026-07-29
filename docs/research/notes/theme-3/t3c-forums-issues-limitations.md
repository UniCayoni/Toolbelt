# Theme 3 / Slice C — Forums, issues, and limitation discovery

Status: notes only (not integrated report)  
Agent id: `t3c-forums-issues-limitations`  
Created: 2026-07-27  
Protocol: `docs/research/PROTOCOL.md`  
Focus: How researchers/agents discover **limitations, bugs, and outdated behavior** that official docs omit or lag on (PROTOCOL **E3** as first-class *discovery* channel; still not alone enough to lock design).

## 1. Scope

In scope:

- GitHub Issues / Discussions **search patterns** for limitation discovery
- Vendor forums (e.g. Cursor Community Forum) and Stack Overflow as E3 discovery
- Changelogs, migration guides, “known issues” / release notes
- **Version matching** (docs version vs installed product/package version)
- Corroborating E3 findings with E0/E1 (reproduce, release notes, source)
- Anti-patterns: single angry issue as fact; ignoring closed-as-wontfix / “not planned”; confusing docs bugs vs product bugs

Out of scope: GreyMatter plugin stub; locking RAG libraries; MVP feature scope.

## 2. Method (tools, queries, date)

**Date:** 2026-07-27

**Tools:**

| Tool | Use |
|------|-----|
| WebSearch | GitHub issue/discussion search; docs drift; Aghajani et al.; Keep a Changelog; Read the Docs versions; Cursor forum |
| WebFetch | GitHub Docs (issues + discussions search); Keep a Changelog 1.1.0; SemVer 2.0.0; Read the Docs Versions; GitHub Discussions best practices; Aghajani preprint PDF |
| Alexandria `rag_query` | corpus=`all` — troubleshooting via forums/GitHub; issue labeling / “won’t fix” |

**Web queries (representative):**

1. `GitHub docs searching issues advanced search qualifiers 2026`
2. `documentation drift outdated docs vs software version known issues changelog`
3. `Cursor forum known issues changelog migration guide documentation`
4. `GitHub Discussions search qualifiers Stack Overflow search operators`
5. `IEEE software documentation inconsistency code documentation alignment`
6. `Read the Docs versions matching installed package docs.version known issues`
7. `Keep a Changelog known issues page versioned documentation`

**Alexandria query:**

1. `How to discover documentation limitations bugs outdated behavior via GitHub issues forums changelogs known issues version matching`

**Primary URLs fetched (success):**

- https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
- https://docs.github.com/en/search-github/searching-on-github/searching-discussions
- https://docs.github.com/en/discussions/guides/best-practices-for-community-conversations-on-github
- https://keepachangelog.com/en/1.1.0/
- https://semver.org/spec/v2.0.0.html
- https://docs.readthedocs.com/platform/latest/versions.html
- https://csnagy.github.io/research/pdfs/2019/Aghajani2019-preprint.pdf

**Fetch timeouts / partial (note as weaker access this pass):**

- https://stackoverflow.com/help/searching (timeout; used search-snippet synthesis + secondary refs)
- https://cursor.com/changelog (timeout; Cursor forum threads used as E3 examples only)

## 3. Findings

### 3.1 PROTOCOL stance on E3 for docs research

- `FACT` [E0]: GreyMatter PROTOCOL grades forums, blogs, GitHub issues, anecdotes as **E3 — Community report**: “Hypothesis / caveat only,” with an explicit **exception for docs research**: E3 is a first-class *discovery* channel for limitations/bugs/outdated behavior, but still **cannot alone lock design** — corroborate with E0/E1 when possible. [E0: path=`d:\GreyMatter\docs\research\PROTOCOL.md` observed 2026-07-27]

- `INFERENCE` [E4]: A “limitation scan” pipeline should treat E3 as a **lead generator** (queries, issue titles, forum categories), then promote claims only after E0 reproduce and/or E1 changelog/docs/source confirmation. Premises: PROTOCOL E3 exception + non-negotiable “no unsupported claims.”

### 3.2 Why forums/issues matter: docs drift is real and silent

- `FACT` [E1]: Academic/empirical work treats **outdated / inconsistent documentation** as a first-class SE problem. Aghajani et al. (ICSE 2019) mined **878** documentation-related artifacts from **mailing lists, Stack Overflow, issue repositories, and pull requests**, producing a taxonomy of documentation issues spanning content, presentation, process, and tools — i.e., community channels are a validated discovery surface for doc problems. [E1: Aghajani et al., “Software Documentation Issues Unveiled,” ICSE 2019 preprint — https://csnagy.github.io/research/pdfs/2019/Aghajani2019-preprint.pdf — accessed 2026-07-27]

- `FACT` [E1]: Tan et al. (Empirical Software Engineering, 2024) report that “up-to-dateness problems” accounted for **39%** of documentation *content* issues in Aghajani et al. (2019); outdated docs “get outdated silently” (no crash); in their study of 3,000+ GitHub projects, **28.9%** of most popular projects contained ≥1 outdated code-element reference, and **82.3%** were outdated at least once historically. [E1: Tan et al., “Detecting outdated code element references in software repository documentation,” Empir. Softw. Eng. — https://link.springer.com/article/10.1007/s10664-023-10397-6 — accessed 2026-07-27]

- `CLAIM` [E3]: Practitioner blogs (vendor/docs tooling) frame documentation drift as a **detection** problem: reliable upstream signals include public-interface code changes, support tickets/community reports, and release notes/changelogs — not calendar audits alone. Treat as synthesis/hypothesis, not design lock. [E3: Promptless “Documentation Drift Is a Detection Problem…” — https://promptless.ai/blog/technical/documentation-drift-detection-problem — accessed 2026-07-27] [E3: Mintlify “How to Stop Documentation Drift…” — https://www.mintlify.com/library/how-to-stop-documentation-drift — accessed 2026-07-27]

- `GAP`: No single vendor-agnostic “official checklist” titled “limitation scan for public docs packages” was found as an E1 standard. Agents must assemble practice from GitHub search docs + versioned docs platforms + empirical SE results + PROTOCOL E3 rules.

### 3.3 GitHub Issues — primary search patterns (E1)

- `FACT` [E1]: GitHub documents issue/PR search qualifiers usable in combination: `is:issue` / `type:issue`, `is:open` / `is:closed`, `repo:`, `org:`, `user:`, `label:`, `in:title|body|comments`, date filters `created:` / `updated:` (ISO8601), `comments:`, `reactions:`, exclusion via leading `-`. [E1: GitHub Docs — Searching issues and pull requests — https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests — accessed 2026-07-27]

- `FACT` [E1]: Closed issues can be filtered by **close reason**: `reason:completed` vs `reason:"not planned"` — critical for limitation discovery so “won’t fix / not planned” is visible rather than treated as “fixed.” [E1: same GitHub Docs page — accessed 2026-07-27]

- `FACT` [E1]: On a repository’s Issues UI (and issues dashboard), GitHub supports **boolean AND/OR and nested parentheses** for advanced filters (example form: `is:issue state:open (type:Bug OR type:Epic)`). Global code-search-style OR historically differed; prefer UI advanced filters for nested boolean when needed. [E1: GitHub Blog, nested queries — https://github.blog/developer-skills/application-development/github-issues-search-now-supports-nested-queries-and-boolean-operators-heres-how-we-rebuilt-it/ — accessed 2026-07-27] [E1: GitHub Docs filtering/searching issues — https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests — accessed 2026-07-27]

- `FACT` [E1]: `gh issue list --search "<query>"` and `gh pr list --search` accept the same search query language via CLI. [E1: GitHub Docs filtering page (CLI tool section) — accessed 2026-07-27]

**Candidate limitation-oriented query patterns** (compose per package; still E3 until corroborated):

| Intent | Example pattern (adapt `repo:` / `org:`) |
|--------|------------------------------------------|
| Open bugs matching a feature | `is:issue is:open label:bug <keyword>` |
| Docs-specific issues | `is:issue label:documentation OR label:docs <keyword>` |
| Stale but still open | `is:issue is:open updated:<YYYY-MM-DD` + keyword |
| Closed as won’t fix / not planned | `is:issue is:closed reason:"not planned" <keyword>` |
| High engagement leads | `is:issue <keyword> comments:>20` or `reactions:>50` |
| Regression after release | `is:issue <keyword> created:>=YYYY-MM-DD` + version string in body |
| Docs vs product | `is:issue (label:documentation OR in:title docs) <API name>` |

- `INFERENCE` [E4]: Prefer **multiplicity signals** (many independent reports, maintainer confirmation, linked PRs) over a single high-emotion issue. Premises: E3 is discovery-only per PROTOCOL; Aghajani taxonomy shows issues mix content bugs, process complaints, and tool bugs.

### 3.4 GitHub Discussions — discovery vs action

- `FACT` [E1]: GitHub positions Discussions for brainstorming / feedback / polls; Issues for bug reports and planned improvements; recommends **opening an issue when ready to take action** from a discussion. [E1: Best practices for community conversations — https://docs.github.com/en/discussions/guides/best-practices-for-community-conversations-on-github — accessed 2026-07-27]

- `FACT` [E1]: Discussion search qualifiers include `in:title|body|comments`, `repo:` / `org:` / `user:`, `is:open|closed`, `is:answered|unanswered`, `is:locked|unlocked`, `category:`, `label:`, `answered-by:`, `comments:`, `created:` / `updated:`. [E1: Searching discussions — https://docs.github.com/en/search-github/searching-on-github/searching-discussions — accessed 2026-07-27]

- `INFERENCE` [E4]: For limitation scans, treat **answered discussions with maintainer answers** as stronger E3 leads than unanswered threads; still promote to E0/E1 before design lock. Premises: Discussions are explicitly “pre-issue”; PROTOCOL forbids E3-only locks.

### 3.5 Vendor forums & Stack Overflow (E3 discovery)

- `FACT` [E2]: Practitioner SE guidance treats project issues as a searchable Q&A archive; labels such as Bug / Question / Won’t Fix structure triage; “Question” issues often recycle into documentation. [E2: Alexandria corpus=`software_engineering` source=`Research Software Engineering with Python...pdf` chunk_id=`d879796ee260fc0fb11b949b` / `fb40afc85558bdd37c087734` / `b7a8e1231f30bd42a5edef73` query=`"documentation limitations..."`]

- `CLAIM` [E3]: Cursor’s Community Forum (`forum.cursor.com`) is an active Bug Reports / Support surface where staff sometimes mark issues “known,” give workarounds, or confirm schema/migration failures that official docs may lag. Example: staff confirmation of chat migration/`conversationState` loss after major updates. [E3: https://forum.cursor.com/t/chats-show-chat-too-old-conversation-corrupted-after-update-conversationstate-lost-no-migration-performed/154934 — accessed 2026-07-27] [E3: https://forum.cursor.com/t/cursor-3-agent-chat-history-gone-in-2-5-after-upgrade/156530 — accessed 2026-07-27]

- `CLAIM` [E3]: Multiple Cursor forum threads report `@Docs` indexing / retrieval failures (0 pages indexed, JS-heavy sites, cache issues). Useful as **E3 leads about the docs tooling itself**, not as facts about third-party APIs. [E3: e.g. https://forum.cursor.com/t/docs-are-not-loading/155923 — accessed 2026-07-27]

- `FACT` [E1]: Stack Overflow documents advanced search operators (`is:question`, `isaccepted:`, `hascode:`, `score:`, tag OR via `[tag] or [tag]`, `created:`, etc.) for narrowing reports. [E1: Stack Overflow Help — How do I search? — https://stackoverflow.com/help/searching — accessed 2026-07-27 via search synthesis; full page fetch timed out this pass]

- `INFERENCE` [E4]: SO answers with accepted/high-score answers are still E3 (community consensus ≠ product truth); use them to discover **symptoms and version strings**, then verify against changelog/source.

### 3.6 Changelogs, migration guides, known-issues pages

- `FACT` [E1]: Keep a Changelog defines human-oriented release notes with typed sections: Added / Changed / Deprecated / Removed / Fixed / Security; warns that **inconsistent** changelogs are dangerous because users treat them as SoT; requires deprecations/removals/breaking changes to be explicit; recommends ISO dates and SemVer statement. [E1: Keep a Changelog 1.1.0 — https://keepachangelog.com/en/1.1.0/ — accessed 2026-07-27]

- `FACT` [E1]: SemVer 2.0.0: MAJOR = incompatible API changes; MINOR = backward-compatible additions (and deprecations); PATCH = backward-compatible bug fixes; released versions MUST NOT be modified; deprecation path requires docs update + minor release before removal in a major. [E1: https://semver.org/spec/v2.0.0.html — accessed 2026-07-27]

- `FACT` [E1]: SemVer FAQ: if a breaking change is accidentally shipped as minor, fix with a new release restoring compatibility; “document the offending version and inform users.” [E1: same SemVer page — accessed 2026-07-27]

- `INFERENCE` [E4]: A limitation scan should always open **CHANGELOG / Releases / migration guide / “Breaking changes” / “Known issues”** for the **exact version range** spanning installed → docs-viewed. Premises: Keep a Changelog + SemVer + PROTOCOL E1 preference.

- `GAP`: “Known issues” pages are common in enterprise products but **not standardized**; location varies (release notes footer, status page, support KB, pinned GitHub Discussion). Agents should search site/`site:` for `known issues`, `limitations`, `compatibility`, `breaking changes` and record **GAP** if absent.

### 3.7 Version matching (docs version vs installed version)

- `FACT` [E1]: Read the Docs publishes multiple versions so users can “read the exact documentation for the specific version of the project they are using”; `latest` tracks default branch (often pre-release); `stable` tracks greatest SemVer-compatible tag excluding pre-releases; default root URL redirects to configured Default version (often `latest`, sometimes `stable`). Non-stable and latest versions can show **warning notifications**. [E1: Read the Docs — Versions — https://docs.readthedocs.com/platform/latest/versions.html — accessed 2026-07-27]

- `INFERENCE` [E4]: **Anti-pattern:** reading `latest` docs while running an older installed package (or vice versa) produces false “docs bugs” or false “product bugs.” Limitation scan step 0: record `(installed_version, docs_version_or_URL, changelog_span)`. Premises: RTD versioning purpose + SemVer immutability of released versions.

- `CLAIM` [E3]: Even documentation *about* changelogs can drift (e.g. keepachangelog.com historical version-mismatch issues) — illustrates that docs sites themselves need version checks. [E3: GitHub issue olivierlacan/keep-a-changelog#320 — accessed 2026-07-27 via search]

### 3.8 Corroborating E3 with E0 / E1

Recommended promotion ladder (candidate pattern; not product-locked):

| Step | Action | Grade if successful |
|------|--------|---------------------|
| 1 | Capture E3 lead (issue/forum/SO) with URL, date, version claims, maintainer stance | E3 `CLAIM` |
| 2 | Match version: installed vs docs vs issue report | E0 if versions observed locally |
| 3 | Search changelog / release notes / migration guide for acknowledgment | E1 if official |
| 4 | Reproduce minimal case locally (or in CI sandbox) | E0 |
| 5 | If open-source: inspect source / tests / linked PR that closed the issue | E1/E0 |
| 6 | If only E3 remains after search | Keep as `CLAIM`/`GAP`/`OPEN` — **do not lock design** |

- `FACT` [E0]: PROTOCOL already requires this corroboration for design locks. [E0: `PROTOCOL.md`]

- `INFERENCE` [E4]: Distinguishing failure modes:
  - **Product bug:** behavior wrong vs documented/expected contract; corroborate E0 + possibly fixed in later changelog (E1).
  - **Docs bug / drift:** code correct; docs wrong/outdated; Aghajani “content” issues; fix is doc PR, not product workaround.
  - **Version skew:** docs for vN+1, install is vN — not a product bug.
  - **Won’t fix / not planned:** product limitation by policy; document as known limitation (E1 if official; else E3 with close reason cited).
  - **User error / env:** single unreproducible report — do not elevate.

### 3.9 Anti-patterns (explicit)

| Anti-pattern | Why it fails | Prefer |
|--------------|--------------|--------|
| Treat one angry issue as fact | Selection bias; may be misconfig | Require corroboration or multiplicity + maintainer ack |
| Ignore `reason:"not planned"` / Won’t Fix | Misses intentional limitations | Cite close reason; treat as known constraint candidate |
| Confuse docs bug vs product bug | Wrong fix path; pollutes RAG | Reproduce against source of truth (code vs docs page) |
| Cite closed-fixed issue without checking *your* version | Fix may be in newer release | Diff versions; read Fixed section in changelog |
| Prefer forum over changelog when both exist | E3 over E1 | Changelog/release notes first for “what changed” |
| Assume `latest` docs = installed | RTD/default often tracks main | Pin docs version to install |
| Treat staff “we’re tracking it” as shipped fix | Awareness ≠ remediation | Keep OPEN until release notes or E0 shows fix |

- `FACT` [E2]: RSE literature: issues labeled **Won’t Fix** are closed when out of scope or not actually a bug; maintainers should explain and keep contributors engaged. [E2: Alexandria `software_engineering` RSE Python chunk_id=`fb40afc85558bdd37c087734`]

## 4. Contradictions / conflicts found

1. **E3 volume vs truth:** Community channels are the richest place to *find* doc/product gaps (Aghajani; Cursor forum), but PROTOCOL forbids treating them as design locks without E0/E1. No conflict if grades are kept separate.

2. **GitHub search power differs by surface:** Nested boolean AND/OR is documented for repository Issues UI advanced filters; global search qualifier docs emphasize classic qualifiers. Agents should not assume identical boolean support everywhere.

3. **Changelogs as SoT vs incomplete changelogs:** Keep a Changelog says a good changelog *ought* to be SoT for notable changes, while also warning that inconsistent changelogs mislead. Inference: absence of a Fixed entry is not proof a bug is open — check Releases, commit history, and issues.

4. **Vendor forum “known issue” vs official docs:** Staff forum confirmations (Cursor) can be stronger than random user posts but still lag or omit from `cursor.com/docs` / changelog. Grade as E3 until mirrored in E1 or reproduced E0.

## 5. Gaps

- `GAP`: No ISO/IEEE “limitation scan” checklist for third-party docs consumers found as a normative standard this pass.
- `GAP`: Stack Overflow Help page fetch timed out; operators cited from search synthesis — re-fetch before locking SO-specific template text.
- `GAP`: Cursor official changelog page fetch timed out; release-note corroboration path for Cursor remains OPEN for Theme 3 integration.
- `GAP`: Alexandria returned weak direct hits on “docs drift detection”; stronger primary evidence came from web E1 (Aghajani, Tan, GitHub, Keep a Changelog, RTD, SemVer).
- `OPEN`: Per-ecosystem “known issues” URL conventions (npm, PyPI, crates.io, NuGet, Unity) need a follow-up catalog.
- `OPEN`: Whether GreyMatter should automate GitHub search queries as a skill vs checklist-only — out of scope for this note.

## 6. Candidate patterns for templates

### 6.1 Limitation scan checklist (any public docs package)

Use when ingesting or relying on a third-party docs package. Record grades per PROTOCOL.

1. **Identity**
   - [ ] Package / product name, homepage, docs root URL
   - [ ] Installed version (E0: package manager / About / CLI `--version`)
   - [ ] Docs version or URL slug viewed (E0: RTD flyout / path `/en/vX.Y/` / “latest|stable”)
   - [ ] Flag version skew if `installed ≠ docs`

2. **Official surfaces (E1 first)**
   - [ ] CHANGELOG / Releases / NEWS for installed..current span
   - [ ] Migration / upgrade / breaking-changes guide
   - [ ] Explicit “Known issues” / Limitations / Compatibility matrix / Status page
   - [ ] Deprecations listed (SemVer/Keep a Changelog expectation)

3. **Issue tracker scan (E3 discovery)**
   - [ ] `repo:ORG/NAME is:issue <feature> label:bug`
   - [ ] Docs labels: `label:documentation` / `label:docs`
   - [ ] Closed not-planned: `is:closed reason:"not planned" <feature>`
   - [ ] High-signal: `comments:>N` / `reactions:>N` / maintainer participated
   - [ ] Discussions: `is:answered category:<…> <feature>` if enabled

4. **Forum / SO scan (E3 discovery)**
   - [ ] Vendor forum category Bug Reports / Known Issues
   - [ ] SO: `[tag] is:question <symptom>` + version in body; prefer accepted/high-score as leads only
   - [ ] Capture URLs, dates, claimed versions, staff vs user posts

5. **Corroboration gate (before design lock)**
   - [ ] Reproduce locally → E0 or mark unreproducible
   - [ ] Confirm in changelog/release → E1 or note absence
   - [ ] Inspect source/tests/PR if available → E1/E0
   - [ ] Classify: product bug | docs drift | version skew | won’t-fix limitation | user error
   - [ ] If only E3 remains → `CLAIM` + `OPEN`; **do not lock design**

6. **Anti-pattern self-check**
   - [ ] Not elevating a single angry unreproduced report
   - [ ] Not ignoring closed “not planned”
   - [ ] Not mixing docs bug with product bug in one claim
   - [ ] Not citing a fixed issue against an older install without version check

### 6.2 Evidence label cheat-sheet for this slice

| Finding type | Typical grade | Label |
|--------------|---------------|-------|
| GitHub Docs search syntax | E1 | `FACT` |
| Keep a Changelog / SemVer / RTD Versions | E1 | `FACT` |
| Aghajani / Tan empirical results | E1 | `FACT` |
| Forum “known issue” staff reply | E3 | `CLAIM` until E0/E1 |
| Local reproduce | E0 | `FACT` |
| Assembled checklist | E4 from premises above | `INFERENCE` / candidate pattern |

### 6.3 Suggested issue/discussion query cookbook (copy-adapt)

```text
# Open product bugs for a keyword
repo:ORG/NAME is:issue is:open label:bug KEYWORD

# Documentation content problems
repo:ORG/NAME is:issue label:documentation KEYWORD

# Intentional non-fixes (limitations)
repo:ORG/NAME is:issue is:closed reason:"not planned" KEYWORD

# Recent regression window
repo:ORG/NAME is:issue KEYWORD created:>=2026-01-01

# Discussions with answers
repo:ORG/NAME is:discussions is:answered KEYWORD
```

## 7. Source list (deduped)

**Protocol / local**

- `d:\GreyMatter\docs\research\PROTOCOL.md` (E0)

**GitHub (E1)**

- https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
- https://docs.github.com/en/search-github/searching-on-github/searching-discussions
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests
- https://docs.github.com/en/discussions/guides/best-practices-for-community-conversations-on-github
- https://github.blog/developer-skills/application-development/github-issues-search-now-supports-nested-queries-and-boolean-operators-heres-how-we-rebuilt-it/

**Versioning / changelogs / docs platforms (E1)**

- https://keepachangelog.com/en/1.1.0/
- https://semver.org/spec/v2.0.0.html
- https://docs.readthedocs.com/platform/latest/versions.html

**Empirical SE (E1)**

- Aghajani et al. ICSE 2019 preprint: https://csnagy.github.io/research/pdfs/2019/Aghajani2019-preprint.pdf
- Tan et al. Empir. Softw. Eng.: https://link.springer.com/article/10.1007/s10664-023-10397-6

**Stack Overflow (E1 partial)**

- https://stackoverflow.com/help/searching

**E3 examples / practitioner (not design locks)**

- https://forum.cursor.com/ (Bug Reports threads cited in §3.5)
- https://promptless.ai/blog/technical/documentation-drift-detection-problem
- https://www.mintlify.com/library/how-to-stop-documentation-drift
- https://ferndesk.com/blog/documentation-drift

**Alexandria (E2)**

- corpus=`software_engineering` — Research Software Engineering with Python (issue labeling, Won’t Fix, questions→docs)
- corpus=`ai_llm_agents` — n8n beginner handbook (forums/GitHub for known issues; weak on docs-drift method)

---

*End of notes. Integrator: merge with Theme 3 A/B; keep E3 leads separate from E0/E1 locks; candidate checklist §6.1 is the main template payload.*
