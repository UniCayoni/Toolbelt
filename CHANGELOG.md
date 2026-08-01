# Changelog

All notable changes to the Toolbelt Cursor plugin are documented here.

Format inspired by [Keep a Changelog](https://keepachangelog.com/). Versioning follows semver for marketplace releases.

## [Unreleased]

### Added

- Theme 12: companion skill `research-scope` + template `research-campaign-brief` (expand/atomize tracks before gather)

### Changed

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
