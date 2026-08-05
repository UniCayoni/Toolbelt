# Toolbelt

Reusable Cursor **agent utility** plugin: research method (PROTOCOL grades, codebase recon, documentation research, **guide-research** companion, ADRs, `AGENTS.md` authoring, Cursor surface authoring, **host standards**), Design, Plan, Execute, **Verify gates**, **Debug**, and **happy-path** orchestration (`implementation-happy-path`).

**Scope:** agent method (research → design → plan → execute → verify → debug).

**Host setup & use:** [docs/host-playbook.md](./docs/host-playbook.md) · [surface catalog](./docs/host-playbook-catalog.md) · start with `/guide-meta`

**Repo:** [github.com/UniCayoni/toolbelt](https://github.com/UniCayoni/toolbelt) · **License:** MIT · See [CHANGELOG.md](./CHANGELOG.md) · **Contribute:** [CONTRIBUTING.md](./CONTRIBUTING.md)

## Install

### From GitHub (consumers / marketplace prep)

1. Clone or add the plugin from the public repo:

```text
git clone https://github.com/UniCayoni/toolbelt.git
```

2. Load it as a **local plugin** (until listed on the Cursor marketplace):

```text
# From the clone root (adjust path to your machine)
python scripts/sync-toolbelt-local-plugin.py
```

Or copy/symlink the repo to `~/.cursor/plugins/local/toolbelt`.

3. **Developer: Reload Window** → Customize → Plugins → confirm **Toolbelt** (`toolbelt`).

When published: install from [Cursor marketplace](https://cursor.com/marketplace) (or Teams dashboard) as **toolbelt** — submit flow: [marketplace/publish](https://cursor.com/marketplace/publish).

### Contributor sync (this checkout)

If you already have the repo checked out (e.g. development):

```text
python scripts/sync-toolbelt-local-plugin.py
```

(On Windows with a fixed clone path you may use an absolute path to that script.) Then **Reload Window**.

Operational load uses `~/.cursor/plugins/local/toolbelt`. Cursor `workspaceOpen`→`pluginPaths` auto-load remains a known limitation on some builds — prefer the sync script.

### Verify after sync

1. **Developer: Reload Window**
2. **Customize** → Plugins: `toolbelt` (display name **Toolbelt**) is listed
3. Skills: Research + Design + Plan/Execute/Verify/Debug leaves + pocket **`guide-*`** + **`guide-meta`** + happy-path + closeout + author-standards (**26** total)
4. Rules: grades + draft≠SoT + **standards-resolve-gate** always-on; explore-before-write available (intelligent)
5. Smoke: `/guide-meta`, `/guide-design`, `/implementation-plan`, `/author-cursor-surfaces` (or Customize → Skills)

## After editing method SoT

Edit `docs/PROTOCOL.md` and `docs/templates/`, then refresh skill runtime copies:

```text
python scripts/refresh-skill-references.py
python scripts/sync-toolbelt-local-plugin.py
```

Reload Window after sync. **Elevating or revising skills/rules:** use `/author-cursor-surfaces` (Theme 4 reinforce) before treating as SoT.

## Layout

```text
skills/          Research + Design + Plan + Execute + Verify + Debug + guide-* + guide-meta + Closeout + Host standards + Happy-path + authoring (26)
rules/           Grades + draft≠SoT + standards-resolve-gate (always); explore-before-write (intelligent)
assets/          Logo and static assets (marketplace)
docs/PROTOCOL.md Method law
docs/templates/  Checklist/template SoT (skills copy into references/)
docs/plans/      Durable implementation plans (non-trivial)
docs/design/     Design notes (when used)
docs/adr/        ADRs
docs/research/   Theme reports + gatherer notes (method history)
docs/archive/    Smoke, sources, elevation map, harness ADR (frozen)
docs/packs/      Pack index (Research / Design / Plan / Execute / Verify / Debug / Happy-path shipped; PR stub)
```

## Skills

### Research

| Skill | Use when |
|-------|----------|
| `research-codebase-recon` | Unfamiliar repo / before non-trivial implementation |
| `research-docs` | Third-party or product docs with version pin |
| `research-protocol` | Full Method-envelope research notes; **normal** (default) vs **deep** theme campaigns |
| `guide-research` | Companion: expand/atomize concept → tracks → enough-to-start before gather |
| `author-agents-md` | Create/revise `AGENTS.md` (`/` invoke) |
| `author-standards` | Host principles + checkable standards profiles; brownfield derive (`/` invoke) |
| `guide-standards` | Selective host standards modules (pointers only; catalog if-present) |
| `research-draft-adr` | Record an architecture/process decision (`/` invoke) |
| `author-cursor-surfaces` | Author/compose skills, rules, commands, hooks to Theme 4 standards (`/` invoke) |

### Design

| Skill | Use when |
|-------|----------|
| `guide-design` | Shared design spine + human gate |
| `design-technical` | Code architecture / stack / services |
| `design-systems` | Game/creative systems |
| `design-narrative` | Story / quests / interactive narrative |
| `design-world-character` | World bible / characters |

### Plan → Verify → Execute → Verify → Debug → Happy path

| Skill | Use when |
|-------|----------|
| `guide-meta` | Cold/fuzzy front door: which Toolbelt skill next (not always-on) |
| `guide-implementation` | Implementation pocket: wire plan → verify → execute → execute-verify |
| `guide-debug` | Debug pocket: wire prove vs investigate/fix (`debug-reproduce` / `debug-systematic`) |
| `implementation-closeout` | Host closeout profile define/check (readiness; not PR merge) |
| `implementation-happy-path` | Feature ladder / controller: chain pocket guides + optional closeout |
| `implementation-plan` | Hybrid implementation plans for agents |
| `implementation-plan-verify` | Graded plan validate before Meta `ready` |
| `implementation-execute` | Execute approved plans (Done-when, N=2) |
| `implementation-execute-subagents` | Controller + fresh implementers |
| `implementation-execute-verify` | Post-green quality/readability + EOP converge |
| `debug-systematic` | Investigate / root-cause / fix with evidence (compose Cursor Debug Mode) |
| `debug-reproduce` | Never-fix: prove bug + light dossier before patch |

Announce **Using `<skill-name>`** once when a Toolbelt skill applies.

## Note output paths

Prefer the **host project’s** research notes directory:

1. `docs/research/notes/` if it exists in the workspace
2. Else a path the user specifies
3. Else ask before writing

Do not assume paths from other products or plugins.

## Growth

Future packs (PR/workflow, UX/T5C, standards) land as additional flat `skills/<name>/` entries after accepted research + `/author-cursor-surfaces`. See [docs/packs/README.md](./docs/packs/README.md). Do not pile new always-apply rules without need.

Plugin packaging / skill-authoring policy: accepted Theme 4 report — [docs/research/reports/theme-4-cursor-plugin-components.md](./docs/research/reports/theme-4-cursor-plugin-components.md). Full surface audit: [docs/research/notes/theme-8-verify/author-surfaces-full-plugin-audit.md](./docs/research/notes/theme-8-verify/author-surfaces-full-plugin-audit.md). Marketplace prep + **pre-publish operator checklist** (public repo, Discussions, Contributing/PR UI, Reload smoke): [docs/research/notes/marketplace-prep/review-plugin-submission-2026-07-30.md](./docs/research/notes/marketplace-prep/review-plugin-submission-2026-07-30.md).
