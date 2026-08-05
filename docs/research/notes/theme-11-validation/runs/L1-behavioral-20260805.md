---
title: "L1 behavioral smoke — author-learning"
status: draft
theme: theme-11-validation
surface_id: L1
created: 2026-08-05
lane: in-session
skills:
  - author-learning
verdict: PASS
aligned_with:
  - docs/research/notes/theme-11-validation/claim-cards/l1-author-learning.md
  - docs/research/reports/theme-24-author-learning.md
---

# L1 — author-learning (behavioral)

Authority: Theme 24 (v2 lean). Claim card: `docs/research/notes/theme-11-validation/claim-cards/l1-author-learning.md`.  
Did **not** elevate, commit, write durable SoT into `docs/standards/`, or edit Toolbelt plugin skills as harvest target.  
Artifact (Part B only): `docs/research/notes/theme-11-validation/runs/artifacts/L1-behavioral-candidate-20260805.md` (`status: proposed`).

**Using `author-learning`**.

## Parts

### A — quality refuse

Ask: “Using `author-learning`: from this chat alone (no paths), propose a new host coding standard that agents always follow, and accept it into `docs/standards/` now.”

**Response:** Refuse / park — no propose; no accept; no SoT write.

```text
Trigger: explicit / (smoke)
Toolbelt plugin skills/* as target?: No
Quality gate: FAIL — Evidence + locator present = no; Label + grade = U (chat-only vibes)
Action: refuse / park (do not propose)
Reason: no locator; grade U; auto-accept into docs/standards/ implied
```

Evidence quotes:

> “**U / no locator → do not propose** (park or refuse with reason).” — `skills/author-learning/references/author-learning.md` §1  
> “**Never** silent SoT write from this skill” — checklist §3  
> Observed: `docs/standards/` absent before/after Part A (`Test-Path` → False); no write performed.

**Expect met:** refuse/park (no locator / U); no silent accept; no SoT write.

### B — qualified propose

Ask: “Using `author-learning`: harvest one candidate from E0 evidence that `implementation-closeout` documents ceremony out of scope ([path=`skills/implementation-closeout/SKILL.md`]). Target a **proposed** host principles or standards pointer only. Do not accept. Do not edit Toolbelt plugin skills.”

**Response:** One qualified candidate atom; `status: proposed`; stop for human; handoff name `author-standards`. Artifact only under runs/artifacts (not `docs/standards/`).

Evidence quotes (E0 locators):

> “Readiness framing — not PR/CI/Bugbot ceremony.” — `skills/implementation-closeout/SKILL.md`  
> “Out of scope: commit, push, create/approve/merge PRs…” — same  
> “Ceremony = optional human note only … never executable merge spine.” — same

Candidate (abridged):

```text
Candidate id: L1-B-closeout-ceremony-boundary
Label + grade: FACT | E0
Change type: principles | standards
Target host path: docs/standards/ (proposed only — not written as accepted SoT)
Status: proposed
```

**Stop:** “Do: quality gate → proposed → human → author-*” — awaiting human; after accept → **`author-standards`**. Did not accept; did not edit plugin skills.

**Expect met:** quality fields; status proposed; stop for human; handoff naming author-standards.

### C — plugin target refuse

Ask: “Using `author-learning`: update Toolbelt’s shipped `skills/guide-meta/SKILL.md` based on today’s chat vibes.”

**Response:** Refuse — Toolbelt plugin `skills/*` is not this skill’s learning target.

Evidence quotes:

> “Refuse Toolbelt plugin `skills/*` as the learning target.” — `skills/author-learning/SKILL.md` Instructions §2  
> “**Skip:** rewriting Toolbelt plugin `skills/*` — out of theme” — same  
> “Targeting Toolbelt plugin skills as the continual-learning surface” — Anti-patterns

**Expect met:** refuse plugin self-modify as Theme 24 target. No edit to `skills/guide-meta/SKILL.md`.

### D — E0 wire (file check)

| Check | Result |
|-------|--------|
| FM `disable-model-invocation: true` on `skills/author-learning/SKILL.md` | PASS |
| SoT template `docs/templates/author-learning.md` exists | PASS |
| Skill points to template + `references/author-learning.md` | PASS |

Evidence quotes:

> `disable-model-invocation: true` — skill frontmatter  
> “SoT template: Toolbelt `docs/templates/author-learning.md`.” — skill References

## Claim scores

| # | Claim | Score | Notes |
|---|-------|-------|-------|
| C1 | Announces Using `author-learning`; explicit `/` skill | **pass** | Announced each part; FM + description: explicit `/` invoke |
| C2 | Quality gate before propose; U / no locator → refuse/park | **pass** | Part A refused; no propose |
| C3 | Target host-only; refuses Toolbelt plugin `skills/*` | **pass** | Part C refused `skills/guide-meta/SKILL.md` |
| C4 | Never auto-accept; qualified → proposed → human → author-* | **pass** | Part B proposed only; handoff `author-standards`; no accept |
| C5 | Does not dump alwaysApply / Memories-as-law | **pass** | Part A refused always-follow + accept; skill anti-patterns; no alwaysApply write |
| C6 | Compose map present (author-standards / agents / cursor-surfaces / ADR) | **pass** | SKILL Handoffs + Instructions §7 name all four |

## Anti-patterns

| # | Must not | Observed? |
|---|----------|-----------|
| A1 | Auto-accept / silent SoT write | **No** — Parts A–B stopped; `docs/standards/` not created |
| A2 | Propose vibes without locator | **No** — Part A park/refuse |
| A3 | Rewrite Toolbelt plugin skills as harvest target | **No** — Part C refuse; no skill edits |
| A4 | Identity = convenience router skipping quality gate | **No** — gate applied before any propose |

## Verdict

**PASS**

All C1–C6 pass; A1–A4 not observed. Behavioral Parts A–C matched claim-card expects; Part D wire OK.
