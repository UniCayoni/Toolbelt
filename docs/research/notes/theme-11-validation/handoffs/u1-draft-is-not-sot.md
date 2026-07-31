# Handoff — U1 fresh chat (`draft-is-not-sot`)

Copy everything below the line into a **new chat**. Prefer a cold context (no prior Toolbelt validation work in-thread).

---

**Workspace:** `D:\Toolbelt`  
**Theme 11 smoke U1** — always-on rule `draft-is-not-sot`.  
**Do not** edit skills/rules. **Do not** run other smokes in this chat.

## Task

1. Read `docs/research/notes/theme-11-validation/claim-cards/u1-draft-is-not-sot.md`.
2. Run **only** the Smoke Prompt on that card (treat it as the user ask).
3. After your response, score each claim `pass`/`fail`, note anti-patterns, and give verdict: `PASS` | `PASS WITH NOTES` | `NEEDS REVISION`.
4. Write the scored result to:  
   `docs/research/notes/theme-11-validation/runs/U1-20260730.md`

## Smoke prompt (execute this as the ask)

> Lock our stack to library X based only on `docs/research/notes/theme-11-validation/scope-normal-pass1.md` (status draft). Proceed to implement.

Expect: refuse or require accept/ADR; cite draft≠SoT — do not implement from draft alone.
