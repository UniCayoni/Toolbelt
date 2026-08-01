---
title: "Theme 11 — Plugin surface validation normal scope (pass 1)"
status: draft
theme: theme-11-validation
created: 2026-07-30
updated: 2026-07-30
authors: [coordinator]
depth: normal
aligned_with:
  - docs/packs/README.md
  - docs/PROTOCOL.md
  - docs/templates/research-depth-modes.md
  - docs/research/reports/theme-8-verify-gates.md
  - docs/research/reports/theme-10-happy-path.md
supersedes: null
---

# Theme 11 — Plugin surface validation: normal research pass 1

**Using `research-protocol`**; depth: **normal** (methodology + matrix — decide whether to escalate deep).

**Status:** `draft`. Not validation SoT.  
**Identity:** How Toolbelt proves shipped surfaces **work as designed** with evidence — claim rubrics, E0 smokes, hybrid chat/subagent runs, tune loop. **Not** a new method pocket redesign. **Not** PR/CI pack.

## 1. Scope

- Question: What’s the best methodical way to test each Toolbelt surface against its design claims, with comparative evidence/metrics? Does that require a **deep** research campaign before first runs?
- In: Surface inventory; claim→check pattern; run lanes (fresh chat vs subagent); metrics; fixture lean; community/vendor eval atoms (light); deep-vs-normal verdict.
- Out: Running the smokes this pass; elevating a validation skill; inventing Cursor private test APIs; shipping skillprobe/OpenAI harness as Toolbelt dependency.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-30 |
| Tools used | Glob skills/rules; Grep theme notes for E0/smoke/G11; WebSearch skill eval; WebFetch OpenAI eval-skills blog; Read research-depth-modes |
| Corpora / URLs | Local Toolbelt; https://developers.openai.com/blog/eval-skills ; WebSearch hits (skillprobe, skill-test, agent-catalog-eval — E3 discovery) |
| Queries (exact) | Cursor agent skill evaluation smoke test rubric LLM agent skill testing methodology 2025 2026 |
| What was *not* searched | Exhaustive skillprobe/OpenAI cookbook bodies; live E0 Toolbelt smokes; Cursor private eval product APIs |
| Depth | normal |
| stop_reason | Methodology + deep-gate criteria sufficient; remaining truth needs **E0 runs**, not more secondary pages |

## 3. E0 — What we already have (Toolbelt)

| Asset | Count / note | Citation |
|-------|----------------|----------|
| Skills | **19** `skills/*/SKILL.md` | [E0: Glob 2026-07-30] |
| Rules | **4** `.mdc` (2 always-on grades/draft≠SoT; 2 intelligent) | [E0: Glob] |
| Packs | Research→Happy-path shipped; PR stub | [E0: packs README] |
| Verdict grammar | Theme 8 PASS / PASS WITH NOTES / NEEDS REVISION | [E0: theme-8 report] |
| Evidence culture | cite-or-omit; iron law; `draft-is-not-sot` | [E0: PROTOCOL + rules] |
| Deferred E0 | Themes 7–9 repeatedly left “live E0 trial” OPEN | [E0: theme-7 W2 note G11 pattern; theme notes] |

- `FACT` [E0] No dedicated validation pack/skill/fixture suite exists in Toolbelt today. [E0: packs + skills inventory]
- `FACT` [E0] Happy-path already defines the compose order to validate last (E2E). [E0: theme-10 report]
- `INFERENCE` [E4] Toolbelt already owns the **grading vocabulary**; Theme 11 needs a **runtime harness process**, not new research grades. Premises: Theme 8 verdicts; PROTOCOL; missing E0 suite.

## 4. Community / vendor atoms (E1/E3)

### 4.1 OpenAI — Testing Agent Skills Systematically with Evals (E1)

- `FACT` [E1] Eval = prompt → captured run (trace + artifacts) → small checks → score over time. [E1: https://developers.openai.com/blog/eval-skills — accessed 2026-07-30]
- `FACT` [E1] Split success: outcome / process / style / efficiency; keep must-pass list small. [E1: same]
- `FACT` [E1] Name+description are activation API — test explicit `/` invoke **and** implicit trigger **and** negative controls. [E1: same]
- `FACT` [E1] Prefer deterministic checks on behavior (commands run, files exist) before LLM-as-judge; let real failures grow the suite. [E1: same]
- `INFERENCE` [E4] Map to Toolbelt: process goals = announce Using + spine steps + handoffs; outcome = artifact shape (plan Meta, dossier fields); style = anti-patterns avoided; efficiency = no thrash past N budgets. Premises: OpenAI categories [E1]; Themes 6–9 law [E0].

### 4.2 Other (E3 discovery only — no lock)

| Surface | Signal | Park for now |
|---------|--------|--------------|
| skillprobe | Subprocess Cursor/Claude; YAML scenarios; measure pass-rate / variance | Optional Phase B automation |
| skill-test / LLM-judge | Rubric schemas for qualitative | Only where deterministic checks fail |
| agent-catalog-eval | before/after fixtures + judge | Heavy; not MVP |

- `CLAIM` [E3] Industry converging on scenario fixtures + assertions + optional judge. Stars≠SoT; no Toolbelt dependency required to start. [E3: WebSearch 2026-07-30]

## 5. Proposed Toolbelt validation method (candidate)

### 5.1 Per-surface unit

For each skill/rule:

1. **Claim card** — extract falsifiable claims from SKILL + accepted theme report (when-to-use, spine musts, skips, handoffs, anti-patterns).  
2. **Smoke prompt** — minimal fixture + one pinned prompt (explicit `/skill` first).  
3. **Run** — capture evidence (announce, steps taken, artifacts, commands).  
4. **Score** — checklist → **PASS / PASS WITH NOTES / NEEDS REVISION** (Theme 8 grammar).  
5. **Tune** — only NEEDS REVISION + high-signal NOTES; re-smoke that surface.  
6. **Log** — note under `docs/research/notes/theme-11-validation/runs/`.

### 5.2 Run lanes (hybrid)

| Lane | Use for | Why |
|------|---------|-----|
| **Fresh chat** | Discovery: description trigger, `/name`, happy-path cold start, always-on rules | Subagents skip discovery |
| **Subagent** | Parallel pocket smokes with pinned “Using X” + fixture | Throughput; isolation |
| **Controller + worker** | execute-subagents + happy-path controller behavior | Theme 7/10 claims |

- `INFERENCE` [E4] Human lean “subagents” is right for **batch pocket smokes**; wrong as sole lane. Premises: OpenAI trigger tests [E1]; Theme 10 cold-start [E0].

### 5.3 Metrics (MVP vs later)

| Metric | MVP? | Notes |
|--------|------|-------|
| Claim checklist pass-rate per surface | **Yes** | Primary |
| Explicit invoke success (`/` / Using) | **Yes** | Process |
| Implicit trigger (3–5 prompts) | Yes for happy-path + 2–3 core skills | Description as API |
| Negative control (should NOT fire) | Sample | Avoid over-trigger |
| Artifact schema checks (plan Meta, dossier 8 fields) | **Yes** where applicable | Deterministic |
| Anti-pattern count | **Yes** | Binary flags |
| Multi-run pass-rate / Wilson CI | Later | skillprobe-style; needs automation |
| Token/thrash efficiency | Later | Optional |

### 5.4 Fixture lean

- Small **host smoke workspace** (or temp dir) with tiny code + optional fake bug — not Toolbelt method SoT as the only SUT for Design/Plan/Execute.  
- Toolbelt repo OK as SUT for `research-codebase-recon`, `research-docs`, `author-*`, happy-path **routing** smokes.  
- Rubrics/claim cards **read-only** for the agent under test (OpenAI reward-hacking caution — E3/E1 spirit).

### 5.5 Run order

1. Always-on rules (tiny)  
2. Research utilities  
3. Design → Plan → Plan-verify → Execute → Execute-verify → Debug  
4. Creative design skills (lighter / sample)  
5. **`implementation-happy-path` E2E last**

## 6. Surface matrix (smoke inventory)

| ID | Surface | Lane lean | Priority |
|----|---------|-----------|----------|
| R1–R6 | research-protocol, research-codebase-recon, research-docs, research-draft-adr, author-agents-md, author-cursor-surfaces | subagent + 1 fresh for discovery | P0 |
| D1–D5 | design-process + technical + 3 creative | subagent (creative can sample 1) | P0 design-process+technical; P1 creative |
| P1–P2 | implementation-plan, plan-verify | subagent | P0 |
| E1–E3 | execute, -subagents, execute-verify | subagent (+ controller pair) | P0 |
| G1–G2 | debug-systematic, debug-reproduce | subagent | P0 |
| H1 | implementation-happy-path | **fresh chat** + controller | P0 |
| U1–U2 | draft-is-not-sot, research-protocol-grades | fresh chat | P0 |
| U3–U4 | research-before-write, coexistence | fresh / as-needed | P1 |

~19 skills + 4 rules ≈ **one claim card + one smoke each** before deep automation.

## 7. Deep research — escalate or not?

| Question | Verdict |
|----------|---------|
| Need deep gatherer fleet to **start** validating the plugin? | **No** |
| Why | Method atoms already exist in Toolbelt + OpenAI E1; industry harnesses are optional packaging; truth is E0 |
| When deep **would** pay | Choosing/shipping an automated harness (skillprobe-class); defining multi-run statistical gates; building a durable “eval pack” product surface |
| Risk of deep-first | Delay E0; restate eval blogs without closing “does Toolbelt work?” |

### Escalation criteria (explicit)

Escalate to **deep** only if human wants **≥1** of:

1. Toolbelt-native **automated** eval harness design (CI-ready), or  
2. Locked **multi-run** metrics (min_pass_rate, variance classes), or  
3. Contested LLM-judge rubric as first-class SoT  

Otherwise: **normal methodology accept → Wave 1 E0 smokes → tune → optional deep for automation**.

- `INFERENCE` [E4] **Stay on normal for methodology; treat first smoke wave as the real validation campaign.** Premises: §3–§5; OpenAI “start small / failures drive coverage” [E1]; research-depth-modes stop when residual needs E0 experiments [E0: research-depth-modes.md].

## 8. Gaps & OPEN

| ID | Item |
|----|------|
| GAP | No Cursor-official “plugin skill test suite” API found this pass — compose Task/chat + artifacts |
| OPEN | Exact fixture repo path (`docs/research/fixtures/` vs sibling smoke repo) |
| OPEN | Whether to elevate a thin `toolbelt-surface-validate` skill later or keep process in theme notes |
| OPEN | Model pin for smokes (`cursor-grok-4.5-high-fast` vs others) — affects variance |

## 9. Implications

- `INFERENCE` [E4] Next human gate: accept this methodology → author claim cards + smoke prompts (can be coordinator or light parallel) → run P0 smokes → integrate findings → tune. Deep only if automation goals trip §7 criteria. Premises: §7; draft≠SoT.
