# Changelog

All notable changes to the Toolbelt Cursor plugin are documented here.

Format inspired by [Keep a Changelog](https://keepachangelog.com/). Versioning follows semver for marketplace releases.

## [Unreleased]

### Added

- Theme 12: companion skill `research-scope` + template `research-campaign-brief` (expand/atomize tracks before gather)
- Theme 13: `CONTRIBUTING.md` + `.github/pull_request_template.md` (contributor path; CI/Bugbot still Phase 2)
- Theme 14: pocket router layer — `implementation-router` + template; packs **Routers / pocket entry** row (`research-scope` / `design-process` documented as de-facto routers; `debug-router` deferred)
- Theme 15: `implementation-closeout` + `closeout-profile` template (host-defined readiness check; ceremony out of scope)
- Theme 16: `author-standards` + `principles-profile` / `standards-profile` templates (host feedstock; brownfield derive → proposed)
- Theme 17: `debug-router` + template (Debug pocket classify/wire; amends Theme 14 D4)

### Changed

- Theme 14: `implementation-happy-path` thins to chain pocket routers/entries (Implementation stage → `implementation-router`) instead of listing every Implementation leaf
- Theme 15: happy-path optional closeout stage before Stop; Phase 2 narrowed to CI/Bugbot/merge automation (readiness is Theme 15)
- Theme 16: Plan / Execute / Closeout / happy-path / `author-agents-md` handoffs to `author-standards`; closeout profile optional C9 for host standards
- Theme 17: happy-path + `implementation-router` → `debug-router`; Execute keeps direct-leaf hot path with repro-first
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
- Design pack: `design-process`, `technical-design`, creative-* skills
- Plan / Execute / Verify / Debug / Happy-path skills (Themes 6–10)
- Always-on rules: `research-protocol-grades`, `draft-is-not-sot`; intelligent `research-before-write`
- Theme 11 E0 P0 validation (18/18 PASS)
- Marketplace prep: `homepage`, `repository`, `logo` (`assets/logo.png`), this changelog

### Changed

- Live surfaces scrubbed of Superpowers / grey-matter peer coupling (standalone wording)
- Removed `research-skill-coexistence` rule
