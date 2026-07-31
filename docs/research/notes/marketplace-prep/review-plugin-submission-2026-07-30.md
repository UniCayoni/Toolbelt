---
title: "review-plugin-submission — Toolbelt (2026-07-30)"
status: draft
theme: marketplace-prep
created: 2026-07-30
updated: 2026-07-30
authors: [reviewer]
prep_applied: 2026-07-30
aligned_with:
  - skills review-plugin-submission (create-plugin plugin)
  - https://cursor.com/docs/reference/plugins.md
supersedes: null
---

# Review plugin submission — Toolbelt

**Using `review-plugin-submission`**.  
**Target:** `d:\Toolbelt` (single-plugin repo `https://github.com/UniCayoni/toolbelt`).  
**Intent:** Pre-publish readiness (not submitting yet).

## Final recommendation

**Prep P1 applied 2026-07-30** — packaging + polish checklist items closed in-repo.  
**Still not submitted** — human should re-smoke local load, then publish when ready at [marketplace/publish](https://cursor.com/marketplace/publish).  
Remaining before submit: live Cursor load check; confirm marketplace `name` uniqueness at submit time; optional brand logo swap.

---

## 1. Manifest validity — **PASS**

| Check | Result |
|-------|--------|
| `.cursor-plugin/plugin.json` exists + valid JSON | PASS |
| `name` lowercase kebab-case (`toolbelt`) | PASS |
| `description`, `version` (`0.1.0`), `author.name`, `license` (`MIT`) | PASS |
| Declared path overrides | N/A (folder discovery; no absolute/`..` paths) |
| `LICENSE` file present | PASS |
| Optional `homepage` / `repository` | **PASS** (GitHub) |
| Optional `logo` | **PASS** (`assets/logo.png` — brand icon) |
| Optional `author.email` | **PASS** (GitHub noreply) |
| `displayName` | present (community/template practice; not in reference required table) |

## 2. Component discoverability — **PASS** (intentional omissions)

| Component | Present | Notes |
|-----------|---------|-------|
| Skills `skills/*/SKILL.md` | **19** | PASS |
| Rules `rules/*.mdc` | **3** | PASS |
| Agents | none | OK — not required; Theme 4 intentional |
| Commands | none | OK — skills cover invoke |
| Hooks | none | OK |
| MCP | none | OK — not a Brain/RAG plugin |
| Root `marketplace.json` | none | OK for **single-plugin** repo |

## 3. Component metadata — **PASS**

| Check | Result |
|-------|--------|
| Skills: `name` + `description`; `name` == folder | **19/19** PASS |
| Rules: `description` + `alwaysApply` | **3/3** PASS |
| Agents / commands frontmatter | N/A |

## 4. Repository / marketplace integration — **PASS (single-plugin)**

| Check | Result |
|-------|--------|
| Multi-plugin `marketplace.json` | N/A — omit for single-plugin |
| Public GitHub repo | PASS (`UniCayoni/toolbelt`) |
| Open source / no binaries | PASS (markdown + scripts) |

## 5. Documentation quality — **PASS** (after prep)

| Check | Result |
|-------|--------|
| Purpose / scope clear | PASS |
| Component coverage (skills/rules tables) | PASS |
| Installation | **PASS** — GitHub clone + relative `scripts/sync-…`; contributor path retained |
| `CHANGELOG.md` | **PASS** |
| Logo | **PASS** |

---

## Prioritized fix list

### P0 — blockers before submit

*(none for structural validity)*

### P1 — do before publish

| # | Item | Status |
|---|------|--------|
| 1 | `repository` / `homepage` on `plugin.json` | **done** |
| 2 | `assets/logo.png` + `"logo"` | **done** (brand icon from Downloads) |
| 3 | README GitHub / marketplace install | **done** |
| 4 | `CHANGELOG.md` | **done** |
| 5 | Local sync + Reload smoke | **operator** — after this prep |

### P2 — nice / decide later

6. Optional `category` / `tags` at submit time  
7. Version bump `0.1.0` → `1.0.0` on first marketplace listing  
8. Do **not** add empty `agents/` / `hooks` / `mcp.json` just to look complete  

### Out of scope / keep parked

- Multi-plugin marketplace layout — not needed for this repo shape  
- MCP / Brain surfaces — product boundary  

---

## Submission checklist (Cursor reference crosswalk)

| Checklist item | Status |
|----------------|--------|
| Valid `plugin.json` | PASS |
| Unique kebab `name` | PASS (uniqueness vs marketplace registry = confirm at submit) |
| Clear `description` | PASS |
| Frontmatter on skills/rules | PASS |
| Logo relative path | PASS |
| README usage/config | PASS |
| Variables / `${VAR}` | N/A |
| Relative valid paths | PASS |
| Tested locally | PASS (Theme 11 E0); re-smoke after prep sync |
| Multi-plugin marketplace.json | N/A |
