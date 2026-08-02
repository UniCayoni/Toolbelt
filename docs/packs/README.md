# Toolbelt packs

| Pack | Status | Surfaces |
|------|--------|----------|
| **Research** | shipped | `research-codebase-recon`, `research-docs`, `research-protocol`, **`research-scope`** (Theme 12 companion), `author-agents-md`, `research-draft-adr`, `author-cursor-surfaces` |
| **Design** | shipped (Theme 5 accept) | `design-process`, `design-technical`, `design-systems`, `design-narrative`, `design-world-character`; rule `draft-is-not-sot` (includes draft design ≠ accepted). **UX (T5C) deferred** |
| **Plan** | shipped (Theme 6 accept + elevate) | `implementation-plan` (+ wire to `implementation-plan-verify`); template `docs/templates/plan-minimal.md`; house path `docs/plans/`; rule `draft-is-not-sot` (draft plans ≠ law). See `docs/research/reports/theme-6-plan-pocket.md` |
| **Execute** | shipped (Theme 7 accept + elevate) | `implementation-execute`, `implementation-execute-subagents` (+ wire to `implementation-execute-verify` + Debug handoffs); consumes `docs/plans/` + Theme 6 Plan law. See `docs/research/reports/theme-7-execute-pocket.md` |
| **Verify gates** | shipped (Theme 8 accept + elevate) | `implementation-plan-verify`, `implementation-execute-verify`; wired from Plan/Execute/-subagents. **Not** Debug/PR. See `docs/research/reports/theme-8-verify-gates.md` |
| **Debug / investigate** | shipped (Theme 9 accept + elevate) | `debug-systematic`, `debug-reproduce`; template `docs/templates/repro-light.md`; wired from Execute / -subagents / execute-verify. **Not** Theme 8 Verify. See `docs/research/reports/theme-9-debug-pocket.md` |
| **Routers / pocket entry** | shipped (Theme 14) | De facto: `research-scope`, `design-process`. New: **`implementation-router`** (+ template). Happy-path **chains** these. **`debug-router` deferred.** Global meta-router **parked**. See `docs/research/reports/theme-14-pocket-routers.md` |
| **Happy path** | shipped (Theme 10; composition Themes 14–15) | `implementation-happy-path`; template `docs/templates/happy-path.md`; caller of pocket routers + optional closeout. See Theme 10/14/15 reports |
| **Closeout readiness** | shipped (Theme 15) | **`implementation-closeout`** + templates `closeout-profile` / `closeout-readiness-checklist`. Host-defined criteria + evidence check. **Ceremony (PR/merge/CI automation) still Phase 2 / host.** See `docs/research/reports/theme-15-closeout-readiness.md` |
| **Validation / E0 smokes** | shipped (Theme 11 accept; no new elevation) | P0 E0 smokes + Theme 12/14 deltas. Evidence `docs/research/notes/theme-11-validation/runs/`. See `docs/research/reports/theme-11-validation.md` |
| **Contributor / GitHub** | shipped (Theme 13 docs) | Root [`CONTRIBUTING.md`](../../CONTRIBUTING.md) + [`.github/pull_request_template.md`](../../.github/pull_request_template.md). **CI / Bugbot ceremony automation still Phase 2.** See Theme 13 report |

Keep new rules **intelligent / opt-in** by default except thin always-on (draft≠SoT). Elevate further surfaces only after accepted research. UX skills wait on [`docs/research/notes/theme-5-design/t5c-ux-placeholder.md`](../research/notes/theme-5-design/t5c-ux-placeholder.md).
