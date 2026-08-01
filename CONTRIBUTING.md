# Contributing to Toolbelt

Thank you for interest in improving **Toolbelt** — a Cursor **agent utility** plugin (research → design → plan → execute → verify → debug → happy-path). This is not an application runtime or Brain/RAG product.

Authority for this guide: accepted Theme 13 report — [`docs/research/reports/theme-13-contributor-workflow.md`](./docs/research/reports/theme-13-contributor-workflow.md).

## Non-negotiables (read first)

1. **Draft is not law.** Notes/reports/designs/plans/ADRs with `status: draft` or `proposed` are **not** accepted sources of truth. Do not merge changes that treat them as SoT. See always-on rule `draft-is-not-sot` and [`docs/PROTOCOL.md`](./docs/PROTOCOL.md).
2. **Cite-or-omit.** Research and design locks need evidence grades (E0–E4/U) and claim labels (FACT/CLAIM/INFERENCE/GAP/OPEN). Prefer `GAP`/`OPEN` over invention.
3. **Human accept before method/skill law.** Pocket or skill changes that set Toolbelt method usually go through research (and often `research-scope` for fuzzy multi-surface work) → integrated report → **human accept** → elevate via **`author-cursor-surfaces`**. A green CI check (when we add CI later) does not replace accept.
4. **Domain-first skill names.** New skills: `{domain}-{stage?}-{action?}` kebab-case; YAML `name` **must** match the folder (`research-*`, `design-*`, `implementation-*`, `debug-*`, `author-*`). See [CHANGELOG.md](./CHANGELOG.md) rename table.
5. **Disclose AI/agent assistance** on issues and PRs (what model/harness/plugins, or “hand-written”). See the pull request template.

## Ways to contribute

| Kind | Preferred path |
|------|----------------|
| Typos / small docs clarity | PR directly (still fill the PR template) |
| Bugs in skills/rules/docs | GitHub **Issue** with repro / expected vs actual |
| Proposals, method questions, “should we…?” | GitHub **Discussions** (if enabled) or Issue — discuss before large work |
| New or changed **skills / rules / method** | Issue or Discussion → research notes as needed → human accept → `/author-cursor-surfaces` (or equivalent) → sync + Reload |
| Architecture / process locks | Prefer `research-draft-adr` after design/research; `proposed` ≠ law until accepted |

### What we usually will not merge

- Drive-by new skills that skip Theme 4 reinforce (`author-cursor-surfaces`), accept gates, or domain-first naming  
- PRs that promote draft research/design to “the way Toolbelt works” without human accept  
- Imports of third-party git/PR/CI/TDD packs as Toolbelt law (Toolbelt is standalone)  
- Fat CI/Bugbot/CLA changes unless separately researched and accepted (still Phase 2 for CI/Bugbot)

## Local setup (contributors)

1. Fork and clone [github.com/UniCayoni/toolbelt](https://github.com/UniCayoni/toolbelt).
2. From the clone root:

```text
python scripts/sync-toolbelt-local-plugin.py
```

3. **Developer: Reload Window** → Customize → Plugins → confirm **Toolbelt**.
4. After editing `docs/PROTOCOL.md` or `docs/templates/`, run:

```text
python scripts/refresh-skill-references.py
python scripts/sync-toolbelt-local-plugin.py
```

Then Reload again.

Details: [README.md](./README.md).

## Changing skills or rules

1. Clarify outcome with maintainers (Issue/Discussion) for non-trivial work.  
2. Use **`author-cursor-surfaces`** (Theme 4): pushy description, `name`==folder, thin always-on rules, compose don’t paste other skills’ spines.  
3. Wire Handoffs; update [docs/packs/README.md](./docs/packs/README.md) and README skill tables when adding surfaces.  
4. Refresh references + sync + Reload; smoke the surface if you touched behavior (Theme 11 claim-card style is welcome).  
5. Do **not** invent Cursor private APIs; use `research-docs` / `research-protocol` when unsure.

## Research & design changes

- Fuzzy / multi-surface themes: start with **`research-scope`** (track board + human enough-to-start).  
- Depth: default **normal**; **deep** only when asked or clearly needed ([`docs/templates/research-depth-modes.md`](./docs/templates/research-depth-modes.md)).  
- Design: `design-process` → domain skill → **human accept** before plan/implement locks.  
- Happy-path orchestration: `implementation-happy-path` — PR/CI is **not** owned there (Phase 2).

## Pull requests

1. Prefer one logical change per PR.  
2. Use the repository **pull request template** (complete every section).  
3. Link Issues/Discussions for method or skill work.  
4. A **human** should review the full diff before you request review (especially for agent-authored PRs).  
5. Expect maintainers to ask for research notes or accept gates on method changes.

## Further reading

| Doc | Role |
|-----|------|
| [`docs/PROTOCOL.md`](./docs/PROTOCOL.md) | Research evidence grades |
| [`docs/packs/README.md`](./docs/packs/README.md) | Pack inventory |
| [`docs/research/reports/`](./docs/research/reports/) | Accepted theme method SoT |
| [`CHANGELOG.md`](./CHANGELOG.md) | User-facing changes / renames |
| Theme 13 report | Contributor workflow decisions |

## License

By contributing, you agree your contributions are licensed under the repository [MIT License](./LICENSE).
