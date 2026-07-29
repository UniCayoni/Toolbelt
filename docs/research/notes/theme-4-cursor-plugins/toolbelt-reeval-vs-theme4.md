---
title: "Toolbelt plugin re-eval vs Theme 4 Cursor plugins research"
status: draft
theme: theme-4-cursor-plugins
created: 2026-07-29
updated: 2026-07-29
aligned_with: docs/research/reports/theme-4-cursor-plugin-components.md
product: Toolbelt local Cursor plugin
---

# Toolbelt re-eval (Theme 4 rubric)

Using Theme 4 integrated report as review rubric (draft implications — not design locks until accepted).

## 1. What Toolbelt is / ships

| Surface | Present? | Notes |
|---------|----------|-------|
| Manifest `.cursor-plugin/plugin.json` | yes | `name`, `version`, `description`, `author`, `license`, `keywords` |
| Skills (5) | yes | recon, docs-research, research-protocol, author-agents-md, draft-adr |
| Rules (4) | yes | 2× `alwaysApply: true`, 2× intelligent (`false`) |
| Agents / Commands / Hooks / MCP | **no** | Aligns with Theme 4: avoid plugin agents until wire-up GAP closes; no hooks/MCP needed for method pack |
| Marketplace multi-plugin | no | Single-plugin repo — fine |
| Host `AGENTS.md` in plugin | no | Correct — plugins don’t package AGENTS.md [T4N] |

Delivery: `refresh-skill-references.py` → `sync-toolbelt-local-plugin.py` → Reload (matches T4K local-test path).

## 2. Verdict by area

### Manifest — **fix recommended (low)**

| Check | Status | Evidence / action |
|-------|--------|-------------------|
| Required `name` kebab-case | OK | `toolbelt` |
| Schema `displayName` | **Missing** | Theme 4: schema accepts it; template/official plugins use it [T4M]. Add e.g. `"displayName": "Toolbelt"`. |
| Description / version / author / license | OK | Present |
| Explicit component path overrides | OK (absent) | Auto-discovery of `skills/` + `rules/` is correct |

### Composition / architecture — **OK (no change)**

- Skills + thin rules only matches Theme 4 “prefer skills for workflows, rules for short always-on” [T4B/T4C].
- No plugin `agents/` — correct given T4L GAP.
- No hooks for hard write-deny — matches ADR 0001 soft gate + Theme 4 (hooks optional/deferred).
- Coexistence rule for Superpowers — good vs T4I Superpowers-as-real-plugin shape.

### Rules — **mostly OK; one soft gap**

| Rule | Mode | Theme 4 fit |
|------|------|-------------|
| `research-protocol-grades` | always | Thin always-on grades — **good** (token-tax aware) |
| `draft-is-not-sot` | always | Thin epistemic guard — **good** |
| `research-before-write` | intelligent | Points at `codebase-recon` — **good**; no long checklist in rule |
| `research-skill-coexistence` | intelligent | Soft staging — **good** |

**Gap:** Intelligent rules have `description` but **no `globs`**. That’s valid for Agent Decides / on-request attach [T4B], but cold agents may under-trigger coexistence / explore-before-write unless description match is strong. Optional enhance: pushier descriptions (when/keywords) like skills.

### Skills — **structure OK; cold-start writing polish recommended**

| Skill | FM | Progressive disclosure | Theme 4 cold-start |
|-------|-----|------------------------|---------------------|
| `codebase-recon` | name+description | checklist in `references/` | Body lean enough; description has when-triggers — **good**; could add gotcha (“empty PowerShell ≠ missing files”) already in body not description |
| `docs-research` | name+description | D0–D14 in refs | **good**; description could add keywords: “API docs”, “version pin”, “OpenAPI”, “Cursor docs” |
| `research-protocol` | name+description | PROTOCOL + templates in refs | **good**; description already lists labels/grades |
| `author-agents-md` | + `disable-model-invocation: true` | skeleton/refs | Correct slash-like [T4C]; description OK |
| `draft-adr` | + `disable-model-invocation: true` | adr template | Correct slash-like |
| name == folder | all match | — | Normative MUST [T4M] — **OK** |

**Gaps vs Spec writing (T4H) — polish, not broken:**

1. Descriptions are solid but not maximally “pushy” (Spec/skill-creator: imperative + user-intent + keywords). Especially `research-protocol` / `docs-research` may under-fire on vague “look this up” prompts.
2. Bodies point to `references/` but rarely say **conditional** “read X **when** Y” (T4H best practice). Most say “Copy references/…” which is fine for checklists; optional strengthen for PROTOCOL.md (“read when writing FACT/CLAIM”).
3. No Spec-only FM (`license`, etc.) — correctly omitted (runtime OPEN) [T4M].
4. No `paths` scoping — OK for global method skills; optional later if monorepo-scoped variants appear.
5. Line counts ≪ 500 — budgets OK.

### SoT / sync pipeline — **OK with process gap**

- Docs templates → skill `references/` via refresh script — correct progressive disclosure.
- **Process gap:** no automated “refs must match SoT” check in CI/smoke; drift possible if someone edits refs directly or forgets refresh. Theme 4 testing matrix: static validate recommended [T4K].

### Testing / smoke — **coverage gap (expected)**

Theme 4: Cursor has no official harness. Toolbelt has archive smoke history but **no documented current smoke checklist** in README beyond sync+Reload. Recommend adding a short “Verify” section (Customize lists skills/rules; `/author-agents-md` visible; always-apply rules present) — does not invent a Cursor API.

### Docs / README — **small gaps**

- README mentions `workspaceOpen`→`pluginPaths` limitation — fine as E0/ops note.
- Sync scripts hardcode `d:\Toolbelt` — portability OPEN from prime recon; fix if repo moves.
- No `displayName` called out.
- Theme 4 report not yet linked from README/research index beyond research README (partially done).

## 3. Priority fix / cover list

### Do now (cheap, evidenced)

1. **Add `displayName`** to `plugin.json` [T4M].
2. **Pushier skill `description`s** (especially auto-apply trio) with extra when/keywords [T4H].
3. **README Verify** subsection: Reload → Customize → confirm 5 skills + 4 rules; try `/draft-adr` or `/author-agents-md` [T4K].
4. Optional: one-line **conditional reference** wording in skill Instructions [T4H].

### Do soon (process)

5. **Drift guard:** document “never edit `skills/*/references/` by hand; edit `docs/` + refresh” more loudly; optional hash-check script exit≠0 on DRIFT.
6. Intelligent rule descriptions: add when-trigger keywords for coexistence / explore-before-write.

### Do not (Theme 4 says leave / avoid)

7. Do **not** add plugin `agents/` for Task isolation until Cursor docs close T4L.
8. Do **not** add hard `preToolUse` hooks unless soft gate fails in E0 trials (ADR 0001).
9. Do **not** ship plugin-root `AGENTS.md` as a component [T4N].
10. Do **not** lock Spec-only skill FM until Cursor runtime known [T4M].

### Optional future packs (already stubbed)

11. Quality/workflow packs per `docs/packs/` — out of Theme 4 plugin-mechanics review.

## 4. Overall scorecard

| Dimension | Grade | One-liner |
|-----------|-------|-----------|
| Packaging shape | A− | Missing only `displayName` |
| Component choice | A | Skills+thin rules; correctly no agents/hooks/MCP |
| Skill structure | A− | Refs + SoT sync good; descriptions can be pushier |
| Rules discipline | A | Thin always-on; long checklists stay in skills |
| Testing story | B | Sync+Reload only; add Verify checklist |
| Alignment to Theme 4 residuals | A | Avoids known Cursor GAPs (agents wire-up, AGENTS-in-plugin) |

**Bottom line:** Toolbelt’s design matches Theme 4 well. Highest-value fixes are manifest `displayName`, colder-start skill/rule descriptions, and an explicit local Verify/smoke blurb — not a redesign.

## 5. Applied (2026-07-29)

Cheap + optional polish applied in-tree:

- [x] `displayName` on `.cursor-plugin/plugin.json`
- [x] Pushier skill descriptions (all five)
- [x] README Verify subsection
- [x] Conditional “read references when …” wording on skills
- [x] Pushier intelligent-rule descriptions (`research-before-write`, `research-skill-coexistence`)

Still deferred: SoT↔refs drift guard script (soon list).
