---
title: "T6 gap closure — durable GAPs lean-closed (no further deep fleet)"
status: draft
theme: theme-6-plan
created: 2026-07-29
updated: 2026-07-29
authors: [coordinator]
depth: normal
aligned_with:
  - docs/research/reports/theme-6-plan-pocket.md
  - docs/research/notes/theme-6-plan/t6-w3-plus1-residual.md
  - docs/research/notes/theme-6-plan/t6-w2-rag-schema-paste-link.md
  - docs/PROTOCOL.md
supersedes: null
---

# T6 gap closure — research needed?

**Using `research-protocol`**; depth: **normal** (gap triage + lean-close; not a new deep wave).

**Human (2026-07-29):** Decisions 1–11 accepted; elevation (#12) still pending. Asked for one more research run **if needed**, else lean to recommended gap closes.

## 1. Scope

- Question: Do durable Theme 6 GAPs still need gatherer research, or close via accepted method + recommended leans?
- In: Numeric paste budget; portable schema; `[P]` token; validating-plans refs; BMAD live examples.
- Out: Elevating Plan skills (pending human #12); inventing E1 numbers; new deep fleet.

## 2. Method

| Item | Value |
|------|-------|
| Date | 2026-07-29 |
| Tools used | Read (Theme 6 report; W2 RAG schema; W3 residual; human session decisions) |
| What was *not* searched | Fresh web/RAG/GitHub fleets — prior waves already marked these durable |
| Depth | normal |
| stop_reason | **no_further_research_needed** — each GAP either unreproducible by more search or closable by house convention from decisions 1–11 |

## 3. Verdict per GAP

| Durable GAP | More research? | Why | Close as |
|-------------|----------------|-----|----------|
| Numeric paste budget | **No** | W1–W3: principles yes, numeric E1 absent; further docs won't invent quotas | **Lean:** T0–T3 guidance only (decision 6) — do not invent numbers |
| Portable JSON task schema SoT | **No** | W2: candidate field bag; no industry SoT schema | **Lean:** freeze **markdown template fields** from decisions 1–9 (below); JSON schema later only if tooling needs it |
| Vendor `[P]` token | **No** | Spec Kit has `[P]` [E1 T6D/W2]; Anthropic/Cursor/OpenAI do not prescribe Toolbelt token | **Lean:** optional `parallel-safe` / `[P]` marker when decision-2 criteria met; not required Plan SoT |
| validating-plans `references/*.md` | **No** | Confirmed 404; SKILL.md summary already extracted V1–V8 | **Lean:** ignore upstream skill; Plan owns V1–V8 light checks (decision 5) |
| Live BMAD `epics.md` examples | **No** | Nice-to-have; grammar already from primary templates | **Lean:** skip for elevation |

- `FACT` [E0] Human accepted decisions 1–11 and deferred skill elevation (#12). [E0: session 2026-07-29]
- `INFERENCE` [E4] Spawning another deep fleet for these five GAPs would burn context without changing elevation inputs. Premises: W2/W3 durable GAP labels; table above; human lean-ready.

## 4. Frozen candidate fields (for pending elevation)

House convention candidates from decisions **1–9** + W2 candidate bag. **Not elevated until #12.**

### Plan document (`docs/plans/YYYY-MM-DD-<slug>-plan.md` when non-trivial)

| Field / section | Required? | Notes |
|-----------------|-----------|-------|
| Goal | yes | T0 |
| design_ref / ADR refs | yes (non-trivial) | T1 path + extract; Decision restated or cited |
| Global Constraints / Always · Block If · Never | yes | T0; hybrid density |
| Out-of-scope / do-not | yes | T0 |
| Coverage map (design section → chapter/tasks) | yes when multi-section | Decision 8 |
| File / Code Map | yes | Paths; exclusive-write notes if any parallel |
| exec_default | yes | `serial_implement_review` unless parallel-safe stated |
| Tasks[] | yes | See task unit |
| Status vocab | yes when tracking | `ready` · `in_progress` · `blocked` (intent-gap / verify-fail / needs-human) · `done` |
| Pre-exec self-check (V1–V8 light) | yes before handoff | Decision 5 |
| Full code snippets in steps | **no** (not required) | Hybrid: interfaces/signatures OK; no mandatory impl dumps |
| TDD ceremony steps | **no** | Optional; verify required |
| GWT AC | optional | When user/story-shaped (decision 3) |

### Task unit

| Field | Required? |
|-------|-----------|
| id | yes |
| objective | yes |
| files[] (create/modify) | yes |
| interfaces (consumes/produces) or binding contracts | yes when coding |
| deps[] | yes (may be empty) |
| done_when + verify_command + expected_signal | yes |
| gwt[] | optional |
| parallel_safe / `[P]` | optional — only if independence + exclusive writes or worktree stated |
| status | optional until execution |
| do_not[] | optional task-local |

### Paste tiers (guidance, no numbers)

| Tier | Use |
|------|-----|
| T0 | Goal, constraints/do-not, interfaces, verify, this-packet file list |
| T1 | Path + section + extract instruction |
| T2 | Long ADR/design/research bodies on demand |
| T3 | Never: chat history, exploration dumps |

## 5. Implications

- `INFERENCE` [E4] Theme 6 method accept can record gap closes above without another deep campaign. Elevation (#12) can proceed from frozen fields when human authorizes `author-cursor-surfaces`.
- Skills still **not** written in this note.

## 6. Gaps remaining after close

None blocking elevation. Optional future E0: trial paste tiers on a real Toolbelt change (measurement, not SoT hunt).
