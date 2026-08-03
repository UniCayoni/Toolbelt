---
title: "Deep T19G — GitHub patterns for applying / progressively disclosing coding standards"
status: draft
theme: theme-19-standards-apply
track: T19G
created: 2026-08-03
updated: 2026-08-03
authors: [gatherer-deep-t19g]
depth: deep
supersedes: null
aligned_with:
  - docs/research/notes/theme-19-standards-apply/campaign-brief.md
  - docs/research/notes/theme-16-host-standards/deep-t16j-bind-patterns.md
---

# Deep T19G — GitHub apply / progressive-disclosure patterns

**Using `research-protocol`.** Depth: **deep**. Draft ≠ design law.  
Fence: samples show how *others* structure selective load — not Toolbelt coding-style law.

## 1. Scope

- **Question / goal:** How do public repos / plugin packs structure STANDARDS / AGENTS / `.cursor/rules` / skills so agents load *slices* (index, globs, “read X when Y”, router-like maps) rather than dumping full guides every turn?
- **In scope:** 6–10 concrete GitHub samples with path + FACT + URL + access date; E1 on raw file fetch; E3 if discovery-only; note GAP on a true “standards router” skill.
- **Out of scope:** Inventing Toolbelt skill ids / catalog schema; copying one org guide as law; elevating surfaces; T19E Cursor product docs (primary) except when a repo restates them; T19F RAG channel.
- **Closes toward:** Theme 19 campaign track T19G (external GH apply patterns).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-03 |
| Tools used | `gh search code`; GitHub MCP `search_code`, `get_file_contents`, `get_me`; prior Theme 16 T16J pointer samples as discovery seeds (re-fetched for E1 where used) |
| Corpora / URLs searched | Public GitHub: `docs/standards` README indexes; `filename:AGENTS.md` + coding standards; `path:.cursor/rules` + `globs:`; `path:.cursor/skills` + `filename:SKILL.md` (“Read when”, load/router phrases); exact `"standards-router"` / `"standards router"` / `"which standards"` |
| Queries (exact) | `docs/standards` `filename:README.md`; `coding standards` `filename:AGENTS.md`; `globs:` `path:.cursor/rules`; `Read when` `filename:SKILL.md` `path:.cursor/skills`; `"standards-router" OR "standards router" OR "which standards" filename:SKILL.md`; `"Rule map" OR "what to read when" OR "which conventions" filename:SKILL.md`; `progressive disclosure` / `load only` / `which skill` skill searches; targeted `get_file_contents` on shortlisted repos |
| What was *not* searched | Exhaustive census of all AGENTS.md; private orgs; marketplace Cursor plugin zip installs beyond public GH trees; live Cursor rule-injection E0; Alexandria RAG (T19F); Windsurf/Cline-only packs; full Claude `.claude/rules` path-frontmatter survey (rate-limited after W1) |
| Depth | deep |
| Waves / stop_reason | **W1** discovery (`gh search` multi-pattern) → shortlist. **W2** raw fetch (MCP) of 10+ files for E1. **W3** residual: exact `"standards-router"` skill search (`total_count: 0`); agentops `skills/standards` confirmed as closest named selective-load skill. `stop_reason`: diminishing_returns — further searches restated index / pointer / glob / “read when” patterns; remaining GAPs are product-runtime or Toolbelt-shape (not more weak E3). |
| Provenance (optional PROV) | Entity=public apply surfaces (STANDARDS indexes, AGENTS pointers, `.cursor/rules` globs, skill progressive refs); Activity=deep T19G gather 2026-08-03; Agent=gatherer-deep-t19g |

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed (external GH sampling) |
| Why this mode | Campaign asks for concrete samples, not a full-repo census |
| Scope boundary | Public GitHub file contents only; no Toolbelt elevate |

## 4. Findings

### 4.1 Sample table (selective-load surfaces)

| # | Repo | Path | Pattern class | Grade |
|---|------|------|---------------|-------|
| S1 | `yfge/ai-video-studio` | `docs/standards/README.md` | Multi-file STD-* catalog + index | E1 |
| S2 | `boshu2/agentops` | `docs/standards/README.md` + `skills/standards/SKILL.md` | Language-sliced standards + **selective-load skill** | E1 |
| S3 | `Simple-XX/SimpleKernel` | `AGENTS.md` | Thin AGENTS → external standards file | E1 |
| S4 | `elastic/terraform-provider-elasticstack` | `AGENTS.md` | Start-here index → coding-standards + topic docs | E1 |
| S5 | `dnsimple/erldns` | `AGENTS.md` | Pointer to CONTRIBUTING + external guidelines | E1 |
| S6 | `dotCMS/core` | `.cursor/rules/README.md`, `frontend-context.mdc`, `docs/frontend/README.md` | Path-scoped rules + “when to load which doc” | E1 |
| S7 | `groupultra/telegram-search` | `.cursor/rules/db.mdc` | Glob path-scoped rule | E1 |
| S8 | `andraderaul/random-fy` | `.cursor/skills/follow-workspace-rules/SKILL.md` | Skill “rule map (what to read when)” | E1 |
| S9 | `pohlai88/afenda-xforge` | `.cursor/skills/ui-craft/SKILL.md` | Skill Routing table + tiered “When to Read” | E1 |
| S10 | `0xAidan/polymarket-bot-test` | `.cursor/skills/claude-api/SKILL.md` | Progressive “Read when …” reference guide | E1 |

Optional corroboration (not counted toward core 10 if space tight): `tambo-ai/tambo` `AGENTS.md` points to `devdocs/` but also inlines a large standards dump [E1]; `kiali/kiali` `AGENTS.md` *mentions* STYLE_GUIDE then largely inlines quality standards [E1]; `tiansivive/yap` `.cursor/skills/load/SKILL.md` “read when the work comes up” procedure-skill index [E1]; `uplbtools/room-tba` workflow skill “Domain skills (read when the task matches)” [E1].

### 4.2 Per-sample FACTS

- `FACT` [E1] **S1 `yfge/ai-video-studio`:** `docs/standards/README.md` indexes versioned standard objects (`STD-ARCH-001` …) as separate files under `docs/standards/`, each with id/intent/scope, and points agents at check scripts that report `standard_id` / `standard_doc` — catalog-of-slices, not one mega-guide. [E1: https://github.com/yfge/ai-video-studio/blob/762921ebf912c07eb1586db4f47ad985b7e36e2a/docs/standards/README.md — accessed 2026-08-03]

- `FACT` [E1] **S2a `boshu2/agentops` docs index:** `docs/standards/README.md` is a language/format index table (Python, Go, TypeScript, …) linking one markdown guide per language, plus “AI Agent Guidelines” structure; also points to a standards library under skill `references/`. [E1: https://github.com/boshu2/agentops/blob/83e1dd0cb5f71bf8375c09b48923592a744529c2/docs/standards/README.md — accessed 2026-08-03]

- `FACT` [E1] **S2b `boshu2/agentops` standards skill (closest “router”):** `skills/standards/SKILL.md` description triggers on “check standards” / “which standards apply”; body orders: record paths/language/risks → load `common-standards.md` **plus only matching language/checklist refs** → cite findings → stop; explicitly “Do not preload the entire reference corpus.” [E1: https://github.com/boshu2/agentops/blob/83e1dd0cb5f71bf8375c09b48923592a744529c2/skills/standards/SKILL.md — accessed 2026-08-03]

- `FACT` [E1] **S3 `Simple-XX/SimpleKernel`:** Root `AGENTS.md` conventions section says full reference is `docs/coding_standards.md` — “read it before generating any code” — rather than inlining the guide. [E1: https://github.com/Simple-XX/SimpleKernel/blob/d384aebcd9cc57c5e105c58b7ee1a47839526a68/AGENTS.md — accessed 2026-08-03]

- `FACT` [E1] **S4 `elastic/terraform-provider-elasticstack`:** `AGENTS.md` titled “start here”; before changes, follow `./dev-docs/high-level/coding-standards.md` and other topic links (contributing, testing, workflow) — thin index over external docs. [E1: https://github.com/elastic/terraform-provider-elasticstack/blob/b475e460d410b67c3458d4560e3692a3289b2ebf/AGENTS.md — accessed 2026-08-03]

- `FACT` [E1] **S5 `dnsimple/erldns`:** `AGENTS.md` Coding Standards section points to `CONTRIBUTING.md#code-standards` and the external Inaka Erlang Guidelines URL — no full style dump in AGENTS. [E1: https://github.com/dnsimple/erldns/blob/140358da7b2dbb35a15e7cce9cbe6b5076fa360e/AGENTS.md — accessed 2026-08-03]

- `FACT` [E1] **S6a `dotCMS/core` rules README:** `.cursor/rules/README.md` documents Always Apply vs globs vs Apply Intelligently vs manual `@`, lists current rules (e.g. frontend/java/test globs), and says put long details in `/docs/` and reference instead of copying into the rule. [E1: https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/.cursor/rules/README.md — accessed 2026-08-03]

- `FACT` [E1] **S6b `dotCMS/core` path-scoped + doc router:** `frontend-context.mdc` sets `alwaysApply: false` and `globs: core-web/**/*.{ts,tsx,html,scss,css}`; body says full standards live in `docs/frontend/`, and includes a **“When to load which doc”** table mapping task → `@docs/frontend/*.md`. [E1: https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/.cursor/rules/frontend-context.mdc — accessed 2026-08-03]

- `FACT` [E1] **S6c `dotCMS/core` standards index:** `docs/frontend/README.md` repeats the when-to-load table for Angular/TS/styling/testing docs and notes Cursor’s `frontend-context.mdc` points here. [E1: https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/docs/frontend/README.md — accessed 2026-08-03]

- `FACT` [E1] **S7 `groupultra/telegram-search`:** `.cursor/rules/db.mdc` frontmatter `globs:` scopes DB/migration conventions to `drizzle/**/*`, `sql/**/*`, schema/model paths — path-selective apply without always-on. [E1: https://github.com/groupultra/telegram-search/blob/29953749c4955ecd9a11442ee556a3890c3e6bba/.cursor/rules/db.mdc — accessed 2026-08-03]

- `FACT` [E1] **S8 `andraderaul/random-fy`:** Skill `follow-workspace-rules` description targets implement/refactor/review when following project standards; body has **“Rule map (what to read when)”** table mapping each `.cursor/rules/*.mdc` to triggers, then a classify → pull relevant rules → implement workflow. [E1: https://github.com/andraderaul/random-fy/blob/464f040384be24184ebedceddda4dd912e928dc7/.cursor/skills/follow-workspace-rules/SKILL.md — accessed 2026-08-03]

- `FACT` [E1] **S9 `pohlai88/afenda-xforge`:** `ui-craft` skill includes a **Routing** intent→reference table and Tier 1–4 reference sections with **“When to Read”** columns (surface-specific / opt-in), instructing not to load heavy refs (e.g. `stack.md`) unless the user opts in. [E1: https://github.com/pohlai88/afenda-xforge/blob/be9154109db15a3e60c1fa34eb7cf61dd7cb315b/.cursor/skills/ui-craft/SKILL.md — accessed 2026-08-03]

- `FACT` [E1] **S10 `0xAidan/polymarket-bot-test`:** `claude-api` skill **Reading Guide** lists numbered references with explicit **“Read when …”** conditions (tool use, streaming, batches, prompt caching, agent design) so agents load slices after language detection — progressive disclosure inside one skill pack. [E1: https://github.com/0xAidan/polymarket-bot-test/blob/80645dbf754968bf238040b05444bbdfc4d42186/.cursor/skills/claude-api/SKILL.md — accessed 2026-08-03]

### 4.3 Pattern classes observed (synthesis — labeled)

| Pattern | What selective load does | Exemplars |
|---------|--------------------------|-----------|
| **A. Standards catalog / index** | README maps module ids or languages → files | S1, S2a, S6c |
| **B. Thin AGENTS pointer** | AGENTS.md links external STYLE/STANDARDS/CONTRIBUTING; does not dump full guide | S3, S4, S5 |
| **C. Path-scoped Cursor rules** | `globs` + `alwaysApply: false` attach conventions only on matching paths | S6a/b, S7 |
| **D. Intelligent / description attach** | Rule README documents Apply Intelligently via `description` | S6a (documents mode; individual mdc vary) |
| **E. Skill “read X when Y”** | Skill body or description tells agent which reference to open for which task | S8, S9, S10 (+ yap/room-tba corroboration) |
| **F. Selective-load standards skill** | Skill whose job is choose + load matching standards modules for a change | **S2b agentops** |

- `INFERENCE` [E4] Public GH practice already shows **compose-friendly progressive disclosure** via (A)+(B)+(C)+(E); a dedicated **classify→standards modules** skill (F) exists at least once (agentops) but is not a widespread named `standards-router` product. Premises: S1–S10 FACTS; §4.4 GAP search.

### 4.4 GAP — true “standards router” skill

- `GAP` Exact skill id / title **`standards-router`** (or phrase “standards router”) in public `SKILL.md` files: GitHub MCP `search_code` query `"standards-router" OR "standards router" OR "which standards" filename:SKILL.md` returned **`total_count: 0`** for the router phrasing pair, while **“which standards apply”** appears inside agentops description (fetched by path, not via that search hit list). Result: **no widespread named standards-router skill**; closest match is **agentops `skills/standards`** (selective load by path/language/risk — S2b). Searched: 2026-08-03 MCP `search_code` + targeted path fetch.

- `GAP` Theme-19-shaped **ambient gate → catalog → module pointers only (compose-only, no findings/check body)** as a reusable public skill: not observed as a distinct pack. Closest: random-fy rule map (S8) and dotCMS when-to-load tables (S6) are **maps embedded in rules/skills**, not a separate router skill that emits pointer packets. Searched: samples above + `"Rule map" OR "what to read when"` skill search (0 hits via code search; S8 still E1 via direct fetch).

- `CLAIM` [E3] Discovery wave also surfaced mega-AGENTS that *name* STYLE_GUIDE then inline large standards (e.g. kiali, tambo) — useful as **anti-patterns for selective load**, not as apply-router exemplars. [E3: `gh search` AGENTS.md “coding standards” hits; E1 fetches of kiali/tambo heads — accessed 2026-08-03]

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Multi-file STANDARDS + README index is a recurring public pattern | confirmed | S1, S2a, S6c |
| H2 | AGENTS.md commonly points out to STANDARDS/STYLE rather than dumping | confirmed (pointer samples); mixed (mega-AGENTS still common) | S3–S5 vs kiali/tambo |
| H3 | Path-scoped `.cursor/rules` globs are used for selective conventions | confirmed | S6, S7 |
| H4 | Skills encode “read X when Y” progressive disclosure | confirmed | S8–S10 |
| H5 | A named public `standards-router` skill is common | rejected / GAP | search total_count 0; agentops is closest under different id |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| AGENTS as thin index vs dump | elastic/SimpleKernel/erldns (pointer) | kiali/tambo (large inline standards) | Both FACT; prefer pointer samples for Theme 19 selective-load intent; mega-AGENTS = counterexample |
| “Standards router” exists? | agentops selective-load skill (E1) | Exact `standards-router` skill search empty | Prefer: **mechanism exists under other names**; **named router skill id is GAP** |

## 7. Gaps & OPEN

- `GAP` Named public `standards-router` skill (exact) — see §4.4.
- `GAP` Ambient-gate-only rule that *only* points to a catalog (no always-on standards body) as a documented pack pattern — not isolated beyond Cursor’s documented modes restated in S6a.
- `OPEN` How often agentops-style “which standards apply” skills appear in private Cursor plugin marketplaces (not searched).
- `OPEN` Runtime: whether Cursor globs + intelligent apply actually keep non-matching standards out of context (needs E0 session instrument — out of scope here; T19E).

## 8. Implications (INFERENCE only)

- `INFERENCE` [E4] For Theme 19 design lean: **catalog + thin AGENTS/rule pointer + path/intelligent attach + optional selective-load skill** are already practiced publicly; Toolbelt need not invent progressive disclosure, only decide host packaging (skill vs mode vs ambient gate). Premises: §4.2–4.3.
- `INFERENCE` [E4] Strongest external analogue to a **standards application router** is **agentops `skills/standards`** (classify by change → load subset → report). Theme 19 may still choose a thinner **compose-only** variant (pointers without check/findings) — that thinner shape remains under-sampled (GAP). Premises: S2b; §4.4.
- `INFERENCE` [E4] **dotCMS** stack (globbed ambient-thin rule → `docs/frontend` when-to-load index → specific STD docs) is a high-signal **catalog + scoped rule** combo closest to campaign vocabulary “ambient gate → catalog → selective load.” Premises: S6a–c.

Do **not** lock Toolbelt skill ids or D12 amendments from these samples alone (`draft-is-not-sot`).

## 9. Source list (deduped)

1. https://github.com/yfge/ai-video-studio/blob/762921ebf912c07eb1586db4f47ad985b7e36e2a/docs/standards/README.md — accessed 2026-08-03  
2. https://github.com/boshu2/agentops/blob/83e1dd0cb5f71bf8375c09b48923592a744529c2/docs/standards/README.md — accessed 2026-08-03  
3. https://github.com/boshu2/agentops/blob/83e1dd0cb5f71bf8375c09b48923592a744529c2/skills/standards/SKILL.md — accessed 2026-08-03  
4. https://github.com/Simple-XX/SimpleKernel/blob/d384aebcd9cc57c5e105c58b7ee1a47839526a68/AGENTS.md — accessed 2026-08-03  
5. https://github.com/elastic/terraform-provider-elasticstack/blob/b475e460d410b67c3458d4560e3692a3289b2ebf/AGENTS.md — accessed 2026-08-03  
6. https://github.com/dnsimple/erldns/blob/140358da7b2dbb35a15e7cce9cbe6b5076fa360e/AGENTS.md — accessed 2026-08-03  
7. https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/.cursor/rules/README.md — accessed 2026-08-03  
8. https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/.cursor/rules/frontend-context.mdc — accessed 2026-08-03  
9. https://github.com/dotCMS/core/blob/a56098a84f293a45f5e044bc77517e05a99be587/docs/frontend/README.md — accessed 2026-08-03  
10. https://github.com/groupultra/telegram-search/blob/29953749c4955ecd9a11442ee556a3890c3e6bba/.cursor/rules/db.mdc — accessed 2026-08-03  
11. https://github.com/andraderaul/random-fy/blob/464f040384be24184ebedceddda4dd912e928dc7/.cursor/skills/follow-workspace-rules/SKILL.md — accessed 2026-08-03  
12. https://github.com/pohlai88/afenda-xforge/blob/be9154109db15a3e60c1fa34eb7cf61dd7cb315b/.cursor/skills/ui-craft/SKILL.md — accessed 2026-08-03  
13. https://github.com/0xAidan/polymarket-bot-test/blob/80645dbf754968bf238040b05444bbdfc4d42186/.cursor/skills/claude-api/SKILL.md — accessed 2026-08-03  
14. https://github.com/tambo-ai/tambo/blob/d24882e2b581a564a7bb4f2727feb15e3737452d/AGENTS.md — accessed 2026-08-03 (mega-AGENTS counterexample + `devdocs/` pointer)  
15. https://github.com/kiali/kiali/blob/99a9477656c7550fc6115c76268e2412c54932b9/AGENTS.md — accessed 2026-08-03 (complements STYLE_GUIDE but largely inlines)  
16. https://github.com/tiansivive/yap/blob/15ff565e47f6711dae005b6dd9ff5985e8f455e3/.cursor/skills/load/SKILL.md — accessed 2026-08-03  
17. https://github.com/uplbtools/room-tba/blob/81d80aa44ebf7813e4be7f95aca74f62690c3a7b/.cursor/skills/room-tba-agent-workflow/SKILL.md — accessed 2026-08-03  
18. Local: `docs/research/notes/theme-19-standards-apply/campaign-brief.md` (track T19G definition)  
19. Local: `docs/research/notes/theme-16-host-standards/deep-t16j-bind-patterns.md` (prior AGENTS pointer seeds)

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Deep stop rule applied (`stop_reason` in Method)
- [x] Method block present
- [x] Every FACT has support (URL + accessed date)
- [x] INFERENCEs list premises
- [x] No invented citations
- [x] Conflicts logged (pointer vs mega-AGENTS; router name vs mechanism)
- [x] Draft ≠ design law
