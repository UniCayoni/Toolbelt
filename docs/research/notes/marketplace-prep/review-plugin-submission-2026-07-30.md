---
title: "review-plugin-submission — Toolbelt (2026-07-30)"
status: draft
theme: marketplace-prep
created: 2026-07-30
updated: 2026-07-31
authors: [reviewer]
prep_applied: 2026-07-30
aligned_with:
  - skills review-plugin-submission (create-plugin plugin)
  - https://cursor.com/docs/reference/plugins.md
  - docs/research/reports/theme-13-contributor-workflow.md
supersedes: null
---

# Review plugin submission — Toolbelt

**Using `review-plugin-submission`**.  
**Target:** `d:\Toolbelt` (single-plugin repo `https://github.com/UniCayoni/toolbelt`).  
**Intent:** Pre-publish readiness (not submitting yet).

## Final recommendation

**In-repo packaging P1** largely done (2026-07-30+). Theme 13 contributor docs elevated (2026-07-31).  
**Still not submitted.** Blockers are mostly **operator / GitHub Settings** — see **§ Pre-marketplace operator checklist** below.  
Publish when ready: [marketplace/publish](https://cursor.com/marketplace/publish).

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
| Skills `skills/*/SKILL.md` | **20** | PASS (incl. `research-scope`; domain-first renames) |
| Rules `rules/*.mdc` | **3** | PASS |
| Agents | none | OK — not required; Theme 4 intentional |
| Commands | none | OK — skills cover invoke |
| Hooks | none | OK |
| MCP | none | OK — not a Brain/RAG plugin |
| Root `marketplace.json` | none | OK for **single-plugin** repo |

## 3. Component metadata — **PASS**

| Check | Result |
|-------|--------|
| Skills: `name` + `description`; `name` == folder | **20/20** PASS |
| Rules: `description` + `alwaysApply` | **3/3** PASS |
| Agents / commands frontmatter | N/A |

## 4. Repository / marketplace integration — **IN PROGRESS**

| Check | Result |
|-------|--------|
| Multi-plugin `marketplace.json` | N/A — omit for single-plugin |
| Public GitHub repo | **PENDING operator** — E0 2026-07-31: still **private** (`gh api`); marketplace + relative `logo` raw resolution need **public** |
| Open source / no binaries | PASS (markdown + scripts) |
| Contributor docs on default branch | **PENDING push** — `CONTRIBUTING.md` + `.github/pull_request_template.md` (Theme 13) must be on `main` |

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

### P0 — blockers before submit (operator)

| # | Item | Status |
|---|------|--------|
| G0 | **Make GitHub repo public** | **pending** — required for marketplace + `logo` via `raw.githubusercontent.com` |
| G1 | **Push** Theme 13 + any unpushed `main` commits (`CONTRIBUTING`, PR template, renames, etc.) | **pending** until `git status` clean & synced with origin |
| G2 | Confirm marketplace listing can see public `repository` / homepage | after G0 |

### P1 — do before publish

| # | Item | Status |
|---|------|--------|
| 1 | `repository` / `homepage` on `plugin.json` | **done** |
| 2 | `assets/logo.png` + `"logo"` | **done** (verify icon **displays** after G0) |
| 3 | README GitHub / marketplace install | **done** |
| 4 | `CHANGELOG.md` | **done** |
| 5 | Local sync + Reload smoke (Customize → Plugins → skills count **20**) | **operator** |
| 6 | Confirm marketplace `name` `toolbelt` uniqueness at submit | **operator** at publish |

### P1 — GitHub contributor readiness (Theme 13 → marketplace hygiene)

Treat as **required before marketplace** so the public listing points at a contribution-ready repo:

| # | Item | Where | Status |
|---|------|--------|--------|
| C1 | `CONTRIBUTING.md` on default branch | repo root | **in-repo**; needs **push** (G1) |
| C2 | `.github/pull_request_template.md` on default branch | `.github/` | **in-repo**; needs **push** (G1) |
| C3 | After push: open github.com/…/toolbelt → **Contributing** tab / sidebar link works | GitHub UI | **operator** |
| C4 | After push: **New pull request** shows the template body | GitHub UI | **operator** |
| C5 | **Enable Discussions** (Settings → General → Features) for proposal intake | GitHub Settings | **pending** (`has_discussions: false` E0 2026-07-31) |
| C6 | README “Contribute” link resolves on GitHub | README | **in-repo**; verify after G1 |

### P2 — nice / decide later

7. Optional `category` / `tags` at submit time  
8. Version bump `0.1.0` → `1.0.0` on first marketplace listing  
9. Do **not** add empty `agents/` / `hooks` / `mcp.json` just to look complete  
10. CODEOWNERS / branch protection — optional quality later  

### Out of scope / keep parked

- Multi-plugin marketplace layout — not needed for this repo shape  
- MCP / Brain surfaces — product boundary  
- CLA / fat CI as day-one contribution blockers (Theme 13 D7)  

---

## Pre-marketplace operator checklist (single list)

Do in roughly this order:

1. [ ] Commit + **push** all pending Toolbelt work to `main` (incl. Theme 13 contributor files)  
2. [ ] Make **`UniCayoni/toolbelt` public** (Settings → General → Danger Zone / Change visibility)  
3. [ ] Enable **Discussions** (Settings → Features)  
4. [ ] Verify **Contributing** tab + **PR template** on GitHub  
5. [ ] Verify **logo** loads in Customize → Plugins (after public)  
6. [ ] **Reload Window**; smoke Customize → Plugins → **20** skills; spot-check `/research-scope` or `/research-codebase-recon`  
7. [ ] At submit: confirm `toolbelt` name free; bump to `1.0.0` if you want first listing semver  
8. [ ] Submit at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish)  

Cross-link: Theme 13 report acceptance checklist operator rows.

---

## Submission checklist (Cursor reference crosswalk)

| Checklist item | Status |
|----------------|--------|
| Valid `plugin.json` | PASS |
| Unique kebab `name` | PASS (uniqueness vs marketplace registry = confirm at submit) |
| Clear `description` | PASS |
| Frontmatter on skills/rules | PASS |
| Logo relative path | PASS (display needs **public** repo — G0) |
| README usage/config | PASS |
| Variables / `${VAR}` | N/A |
| Relative valid paths | PASS |
| Tested locally | PASS (Theme 11 E0); re-smoke after sync (P1 #5) |
| Multi-plugin marketplace.json | N/A |
| Contributor path for public forks | Theme 13 shipped in-repo; GitHub UI checks C3–C5 **operator** |
