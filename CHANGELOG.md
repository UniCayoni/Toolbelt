# Changelog

All notable changes to the Toolbelt Cursor plugin are documented here.

Format inspired by [Keep a Changelog](https://keepachangelog.com/). Versioning follows semver for marketplace releases.

## [Unreleased]

### Added

- Theme 22: **`guide-meta`** + template — thin global front door (classify → one next surface); **not** always-on
- Theme 19: **`guide-standards`** + standards catalog/module templates + always-on thin **`standards-resolve-gate`** (selective module apply; empty/absent no-op)
- Theme 18: recon conditional **S12b** (git history / recency) + `author-standards` derive conflict-tiebreak glue (default 12m window; host override)
- Theme 12: companion skill `guide-research` + template `research-campaign-brief` (expand/atomize tracks before gather)
- Theme 13: `CONTRIBUTING.md` + `.github/pull_request_template.md` (contributor path; CI/Bugbot still Phase 2)
- Theme 14: pocket router layer — `guide-implementation` + template; packs **Routers / pocket entry** row (`guide-research` / `guide-design` documented as de-facto routers; `guide-debug` deferred)
- Theme 15: `implementation-closeout` + `closeout-profile` template (host-defined readiness check; ceremony out of scope)
- Theme 16: `author-standards` + `principles-profile` / `standards-profile` templates (host feedstock; brownfield derive → proposed)
- Theme 17: `guide-debug` + template (Debug pocket classify/wire; amends Theme 14 D4)

### Changed

- Theme 21: T19J fan-out — all pocket **`guide-*`** run if-present **`guide-standards`** resolve (already-pinned skip; research/design lean principles modules; impl/debug lean technical). Single sync cutover.
- Theme 20: pocket entry skills renamed to symmetric **`guide-*`** prefix (hard cutover; Reload Window after sync):
  - `research-scope` → `guide-research`
  - `design-process` → `guide-design`
  - `implementation-router` → `guide-implementation`
  - `debug-router` → `guide-debug`
  - `standards-router` → `guide-standards`
- Theme 19: Theme 16 D12 clarified — always-on **resolve gate** allowed; always-on standards **bodies** still forbidden
- Theme 14: `implementation-happy-path` thins to chain pocket routers/entries (Implementation stage → `guide-implementation`) instead of listing every Implementation leaf
- Theme 15: happy-path optional closeout stage before Stop; Phase 2 narrowed to CI/Bugbot/merge automation (readiness is Theme 15)
- Theme 16: Plan / Execute / Closeout / happy-path / `author-agents-md` handoffs to `author-standards`; closeout profile optional C9 for host standards
- Theme 17: happy-path + `guide-implementation` → `guide-debug`; Execute keeps direct-leaf hot path with repro-first
- **Breaking skill renames** (domain-first ids; Reload Window after sync):
  - `codebase-recon` → `research-codebase-recon`
  - `docs-research` → `research-docs`
  - `draft-adr` → `research-draft-adr`
  - `technical-design` → `design-technical`
  - `creative-systems-design` → `design-systems`
  - `creative-narrative-design` → `design-narrative`
  - `creative-world-character-design` → `design-world-character`
  - `systematic-debug` → `debug-systematic`
  - `reproduce-bug` → `debug-reproduce`

## [0.1.0] — 2026-07-30

### Added

- Research pack: `research-protocol`, `codebase-recon`, `docs-research`, `draft-adr`, `author-agents-md`, `author-cursor-surfaces`
- Design pack: `guide-design`, `technical-design`, creative-* skills
- Plan / Execute / Verify / Debug / Happy-path skills (Themes 6–10)
- Always-on rules: `research-protocol-grades`, `draft-is-not-sot`; intelligent `research-before-write`
- Theme 11 E0 P0 validation (18/18 PASS)
- Marketplace prep: `homepage`, `repository`, `logo` (`assets/logo.png`), this changelog

### Changed

- Live surfaces scrubbed of Superpowers / grey-matter peer coupling (standalone wording)
- Removed `research-skill-coexistence` rule
