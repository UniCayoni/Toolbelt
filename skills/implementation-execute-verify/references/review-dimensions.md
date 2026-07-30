---
title: Execute-verify review dimensions
status: active
aligned_with: docs/research/reports/theme-8-verify-gates.md
---

# Review dimensions (thin)

Post-green checklist for `implementation-execute-verify`. OpenSpec Completeness/Correctness/Coherence are **aliases only**.

## Evidence

1. Claim rests on IDENTIFY→RUN→READ→VERIFY (or Done-when + kept output) — ban should/looks/seems.
2. Expected signal matched; failures/exit codes read, not assumed.
3. Done-when / constraints ≠ “tests green alone” when the plan lists extras.

## Faithfulness *(alias Completeness + Correctness)*

1. Done-when / Files / Interfaces / Do-not / Always·Block·Never present in outcome (or explicit out-of-scope).
2. No Goal / Done-when / Interfaces rewrite; out-of-bounds → Theme 7 major-deviation.
3. No invent: missing intent → escalate.
4. Unrequested scope surfaced — not silent “bonus”.
5. Cited Design/ADR Decision followed.

## Readability / coherence *(alias Coherence)*

1. Clear module/file boundaries; naming matches local conventions.
2. No clever opacity / unexplained magic; non-obvious AI logic has intent comments where needed.
3. Pattern fit with surrounding code; glaring inconsistency only — **don’t nitpick style**.
4. No drive-by edits outside Files/Interfaces.
5. Unused leftovers removed; DRY without premature abstraction.

**Park (not Theme 8 law):** full merge/PR readiness, license/bias audits, council multi-model ceremony → later Debug/PR or house policy.
