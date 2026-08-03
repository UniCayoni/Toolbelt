---
title: "T19D — Catalog / modules (normal)"
status: draft
theme: theme-19-standards-apply
created: 2026-08-03
depth: normal
authors: [research-gatherer]
---

# T19D — Catalog / modules

**Using `research-protocol`.** Depth: **normal**.

## 1. Scope

How host standards split + index so routers point without dumping all rules.

## 2. Findings

- `FACT` [E0] Current SoT is one standards profile + one principles profile; dual-era is an optional section inside standards profile — not separate module files. [E0: `docs/templates/standards-profile.md`, `principles-profile.md`]
- `FACT` [E0] Theme 16 D4: host default paths OPEN; frontmatter purpose required. [E0: Theme 16 report]
- `FACT` [E0] Theme 16 D6 caps v1 types (naming, layout, patterns, tests/docs, safety, optional API). [E0: same]
- `INFERENCE` [E4] Catalog lean (proposed): `docs/standards/index.md` (or host path) lists modules with `id`, `path`, `status`, `types[]`, `applies_to_paths[]`, `applies_to_skills[]` / pockets; modules are small markdown files or typed slices. Premises: campaign selective-load; D4/D6; T19A GAP.
- `INFERENCE` [E4] Principles stay separate altitude (Theme 16 D8); router may always point **core** principles when any standards module loads, or only when intent is decision-tone — OPEN. Premises: D8; campaign fence.
- `INFERENCE` [E4] Single-file profile remains valid **v0 host shape**; catalog is additive for hosts that split — router treats one-file as a single module. Premises: D4 OPEN paths; avoid forced migrate.
- `GAP` No Toolbelt catalog template yet. [E0]
- `OPEN` Exact schema field names — deep T19G/D + T19I.

## 3. Dual-era note

Dual-era profile schema v2 remains parked (Theme 18); catalog may later link quarantine globs per module — not P0 for apply router.
