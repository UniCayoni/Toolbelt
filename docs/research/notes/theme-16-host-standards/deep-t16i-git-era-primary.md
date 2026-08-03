---
title: "Theme 16 deep — Git era / formatter migration (primary)"
status: draft
theme: theme-16-host-standards
created: 2026-08-02
depth: deep
track: T16I
closes_gaps: [G3, G8]
---

# Theme 16 deep — Git era signals (primary)

**Using `research-protocol`**.  
**depth:** deep  
**Method:** Primary docs for blame-ignore + style migration; complements brownfield gatherer.

## Findings

### Tooling FACTS (era noise vs signal)

| Label | Claim | Grade | Citation |
|-------|-------|-------|----------|
| FACT | `git blame` supports `--ignore-rev` and `--ignore-revs-file`; ignored commits are skipped when attributing lines; config `blame.ignoreRevsFile`. | E1 | https://git-scm.com/docs/git-blame (fetched 2026-08-02) |
| FACT | `git blame --since=<date>` / revision ranges can limit annotation to recent history; lines unchanged since boundary are blamed on the boundary commit. | E1 | same |
| FACT | Black’s official migration guide: bulk reformat commit + list full 40-char SHAs in `.git-blame-ignore-revs`; optional `git config blame.ignoreRevsFile .git-blame-ignore-revs`; GitHub/GitLab web blame respect the file (GitLab ≥17.10 per Black docs). | E1 | https://black.readthedocs.io/en/stable/guides/introducing_black_to_your_project.html |
| CLAIM (secondary) | Prefer ignore-list only for **pure formatting** commits; mixed logic+format commits should not be ignored. | E3 | how2.sh / community guides summarizing same practice |

### Implications for Theme 16 brownfield recipe (labeled)

| Label | Claim | Grade |
|-------|-------|-------|
| INFERENCE | When deriving standards from code, **formatter mega-commits** are era boundaries — treat as noise for “what humans meant,” not as evidence of preferred local style before accept. | E4 | premises: Black guide + git blame ignore |
| INFERENCE | Recency signals useful for derive: (a) paths with recent non-ignored blame; (b) hot paths via log/churn; (c) quarantine dirs with only ancient blame. Exact thresholds host-chosen — OPEN for Toolbelt defaults. | E4 | premises: git `--since` + recon lean |
| INFERENCE | Two eras in one repo: documented strategies include big-bang format+ignore-revs, or format-only-touched-lines; standards profiles should allow **scope** (new code / path globs) not only global law. | E4 | premises: Black guide + Osmani formatter advice (W2 note) |
| GAP | No primary “standards derivation from blame majority vote” algorithm found — Toolbelt recipe remains proposed method, not industry SoT. | — | — |

## Remaining OPEN

- Default recency window (N months) for Toolbelt derive mode  
- Whether `author-standards` `derive` should require `.git-blame-ignore-revs` presence check (E0 host)
