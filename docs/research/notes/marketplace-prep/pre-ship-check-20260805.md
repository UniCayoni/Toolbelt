---
title: "Pre-ship check — Toolbelt (2026-08-05)"
status: draft
theme: marketplace-prep
created: 2026-08-05
authors: [reviewer]
aligned_with:
  - docs/research/notes/marketplace-prep/review-plugin-submission-2026-07-30.md
  - .cursor-plugin/plugin.json
---

# Pre-ship check — Toolbelt (2026-08-05)

**Intent:** Final gate before marketplace / public ship. **Draft ≠ law.**  
**HEAD:** `edfd97d` on `main` (synced with `origin/main`).

## Verdict

| Layer | Result |
|-------|--------|
| **In-repo packaging** | **READY** |
| **Method / smokes** | **READY** (Themes 11–25 on `main`; Theme 24 regression 4/4) |
| **Operator / GitHub** | **NOT READY to submit** — repo still **private**; Discussions off |

Do **not** submit to marketplace until G0 (public) is done. Local/private distribution via clone+sync is fine today.

---

## 1. Packaging (E0 — 2026-08-05)

| Check | Result |
|-------|--------|
| `plugin.json` valid JSON | PASS |
| `name` `toolbelt`, version `0.1.0`, MIT, author, homepage/repository | PASS |
| `logo` → `assets/logo.png` (present; ~857KB on GitHub) | PASS |
| Skills `name` == folder | **27/27** PASS |
| Rules `.mdc` | **4** (3 always-on + `research-before-write`) |
| LICENSE / CONTRIBUTING / PR template | PASS |
| Host playbook + catalog | PASS |
| Local sync `~/.cursor/plugins/local/toolbelt` skills | **27** PASS |
| `markdownlint-cli2` (Theme 25 config) | **0** issues |
| Working tree clean vs `origin/main` | PASS |

## 2. Method readiness (summary)

| Area | Status |
|------|--------|
| Research → Design → Plan → Execute → Verify → Debug | shipped |
| `guide-*` + `guide-meta` | shipped |
| Host standards + resolve gate | shipped |
| Closeout (readiness, not ceremony) | shipped |
| Happy-path | shipped |
| Host playbook (Theme 23) | shipped |
| `author-learning` (Theme 24) + smoke L1/M1/C1/PB1 | shipped |
| Docs hygiene lint (Theme 25) | shipped |
| Parks still OK | UX T5C; Phase 2 CI/Bugbot; dual-era schema; creative deep smokes |

## 3. Operator blockers (must do before marketplace submit)

| # | Item | E0 2026-08-05 |
|---|------|----------------|
| G0 | Make **`UniCayoni/toolbelt` public** | **BLOCKER** — `private: true` |
| G1 | Enable **Discussions** | pending — `has_discussions: false` |
| G2 | Verify Contributing tab + PR template in GitHub UI | operator after public |
| G3 | Reload → Customize → Plugins: **27** skills; spot `/guide-meta`, `/author-learning` | operator (local sync already 27) |
| G4 | Confirm marketplace name `toolbelt` free at submit | operator |
| G5 | Optional: bump `0.1.0` → `1.0.0` for first listing | decide at submit |

Publish URL: https://cursor.com/marketplace/publish

## 4. README nits (non-blocking)

- Opening blurb still under-emphasizes `guide-meta` / `author-learning` vs body tables — optional polish after public.
- Verify-after-sync skill count **27** matches disk (PASS).

## 5. Recommendation

1. **Ship-ready as a private/local plugin today** (clone + sync).  
2. **Before marketplace:** public repo → Discussions → UI verify → Reload smoke → submit.  
3. No further method themes required for v0.1.0 listing unless you want 1.0.0 + README blurb polish in the same cut.
