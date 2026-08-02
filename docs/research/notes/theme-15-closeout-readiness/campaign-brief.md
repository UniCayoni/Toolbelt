---
title: "Theme 15 — Closeout readiness (research campaign brief)"
status: accepted
theme: theme-15-closeout-readiness
created: 2026-08-02
updated: 2026-08-02
authors: [scope-agent]
scope_note: Comparator channels (RAG/GitHub/web/research) made explicit 2026-08-02
aligned_with:
  - docs/templates/research-campaign-brief.md
  - docs/research/reports/theme-12-research-scoping.md
  - docs/research/reports/theme-10-happy-path.md
  - docs/research/reports/theme-13-contributor-workflow.md
  - docs/research/reports/theme-14-pocket-routers.md
supersedes: null
---

# Research campaign brief — Theme 15 Closeout readiness

Authority: Theme 12 accepted. Used by skill **`research-scope`**.  
Companion only — does **not** replace `research-protocol` notes/grades.  
**Draft ≠ law** until human accepts scope / later report.

## Header

```text
Title / idea: Closeout readiness — a Toolbelt surface that helps hosts *define and
  check* their own ship/PR/handoff closeout from evidence + requirements, without
  Toolbelt owning git/PR/merge/push ceremony (workspace-personal).
Complexity: theme/campaign
Host note path: docs/research/notes/theme-15-closeout-readiness/
Date: 2026-08-02
Scoped by: agent (session: scope before deep gather)
Enough-to-start (agent propose): yes — problem bounded; Phase 2 parks clear;
  approach lean stated; tracks cover baseline + DoD analogues + shape + wiring.
Human accept scope: accepted 2026-08-02
```

## Working vocabulary (session lean — not locked)

| Term | Means | Not |
|------|--------|-----|
| **Closeout** | Host-defined “done enough to leave the Toolbelt ladder” (ship / PR / handoff / archive) | A universal merge checklist |
| **Closeout readiness** | Framing + checking readiness against *that host’s* criteria + available evidence | Running `gh pr create` / merge / push |
| **Ceremony** | GitHub/Git ops: branch, commit author, PR body, approve, merge, tags | Method grades / verify greens |
| **Evidence** | Verify results, smokes, accepts, design/plan Meta ready, human decisions | Invented “tests passed” |
| **Host closeout profile** | Durable artifact the host owns (path TBD in design) | Plugin-hardcoded PR law |

## Expand (short)

What must be true / looked up / decided before / during gather?

```text
- Bound against Themes 9–10/13 Phase 2: PR/CI mega-pack stays out unless this theme
  explicitly *replaces* that park with a thinner readiness pocket
- Product thesis: plugin helps *define/check* closeouts; host/workspace owns ceremony
- Look up: Definition of Done / release readiness / “ship checklist” patterns (primary +
  skill-pack analogues) — what transfers without becoming ceremony law
- Look up: how Toolbelt already stops (happy-path step Stop; CONTRIBUTING; execute-verify)
- Decide shape: skill + template vs template-only vs “pointer in happy-path only”
- Decide name/domain: e.g. implementation-closeout vs ship-readiness vs closeout-readiness
- Decide relationship to routers: new pocket entry? leaf after execute-verify? happy-path stage?
- Risk: skill that secretly becomes “how to open a PR” — must stay falsifiable out-of-scope
- Risk: empty meta (“write your own checklist”) with no structure — must still be useful
```

## Tracks

| ID | Track name | Question | In scope | Out of scope | Priority | Depth lean | Next skill(s) |
|----|------------|----------|----------|--------------|----------|------------|---------------|
| T15A | Local baseline & parks | What did Themes 9–10/13 already decide about PR/CI/stop, and what gap remains for *readiness* vs *ceremony*? | Happy-path Stop; Phase 2 parks; CONTRIBUTING; verify gates | Re-opening Debug/Verify method | P0 | normal | `research-codebase-recon` + short protocol note |
| T15B | Problem & success criteria | What should “useful closeout readiness” mean for Toolbelt users (solo + multi-agent), falsifiably? | Outcomes, non-goals, quality bar | Concrete skill text yet | P0 | normal | `research-protocol` |
| T15C | DoD / readiness analogues | How do industry + agent skill packs express Definition of Done, release/ship readiness, or handoff checklists *without* owning VCS ceremony? | Multi-channel gather (see § Comparator discovery); contrast focuses | Importing merge queues / required reviewers as Toolbelt law | P0 | normal→deep if thin | `research-docs` + protocol + Alexandria + gh/web |
| T15D | Evidence binding | How should readiness bind to Toolbelt evidence (Meta ready, execute-verify, smokes, human accept, draft≠SoT) without inventing passes? | Mapping table; cite-or-omit; blocked/intent-gap | New verify grades | P0 | normal | `research-protocol` + recon |
| T15E | Host artifact & ceremony boundary | Where should a host closeout profile live, and what must stay explicitly host/workspace (gh, Actions, CODEOWNERS)? | Path conventions; profile fields; “ceremony = host” rule | Implementing Automations/Actions in Toolbelt | P1 | normal | protocol |
| T15F | Shape options | Skill + template vs router vs happy-path-only pointer; naming; packs row; relationship to `implementation-router` / happy-path Stop | Options matrix + risks (empty meta vs ceremony creep) | Elevation before accept | P0 | normal | integrator after A–E |
| T15G | Happy-path / router wire | If elevated, how does closeout attach to ladder without owning PR Phase 2 ceremony? | Optional stage after execute-verify / Stop rewrite | Forcing closeout on every trivial tweak | P1 | normal | after F lean |

## Enough? / stop

```text
Agent enough-to-start?: yes — for *scope accept*, then a normal first wave (T15A–D + F),
  not an immediate deep fleet. Deep (T15C expand / more comparators) only if normal is thin
  or human asks.
Open GAPs / OPENs before gather:
  - Exact theme/surface id (`implementation-closeout` vs `closeout-readiness` vs other) — OPEN
  - Whether this *closes* Phase 2 “CI/Bugbot pack” or only *narrows* it — OPEN until F
  - Whether Bugbot/CI appear only as *optional host criteria slots* — lean yes, not locked
stop_reason (if stopping scope without gather): waiting human accept | revise | defer
Human gate: accepted 2026-08-02 — normal gather authorized
```

## Comparator discovery (required channels for T15C + support for T15B/F)

Not optional “nice to have” — normal wave should **touch each channel** at least once; deep expands within channels that pay rent. Cite-or-omit; E3 community = discovery only (no design locks alone).

| Channel | Use for | Example queries / targets (not exhaustive) |
|---------|---------|-----------------------------------------------|
| **Alexandria RAG** | Software eng + agent practice on DoD, release readiness, handoffs, Definition of Ready | Corpora: prefer `software_engineering`, `ai_llm_agents` (maybe `programming_algorithms_systems`). Questions: Definition of Done, ship/release checklist, Definition of Ready, handoff acceptance criteria, “done vs shipped” |
| **GitHub (repos + code)** | How skill packs / agent plugins phrase “ready for PR”, ship, closeout, handoff — *compare focuses* | `gh` / GitHub MCP: `SKILL.md` + README hits for “definition of done”, “ready for pr”, “ship checklist”, “release readiness”, “closeout”; sample 3–6 packs (not one cherry-pick) |
| **Web / primary docs** | Official or canonical product docs | GitHub Docs (PR templates, required reviews — as **host ceremony** analogy only); Scrum/Agile Alliance or similar **primary** DoD pages if fetchable; Anthropic/agent “effective” guidance only if it speaks readiness/handoff |
| **Research / secondary sites** | Structured comparisons, catalogs | Agent pattern catalogs, engineering blogs graded **E2/E3**; academic/secondary on DoD only with clear citation — no invented papers |
| **Local Toolbelt (T15A/D)** | Bound against parks + verify/accept evidence | Themes 9–10/13/14; happy-path Stop; execute-verify; CONTRIBUTING |

**Compare focuses (explicit axes for T15C notes):**

```text
- Ceremony-heavy (merge/approve/CI gates) vs readiness/evidence-heavy
- Team process DoD vs solo/agent closeout
- Fixed universal checklist vs host-defined profile
- “Ready for PR” as git step vs “ready to leave the method ladder”
- What Toolbelt should adopt vs park vs host-only
```

## Recommended gather order (after accept)

1. **Normal wave:** T15A → T15B → T15D (local + problem + evidence) **in parallel with T15C light pass across all comparator channels** (RAG + GitHub + web + ≥1 research/secondary source)  
2. **Integrator lean** on T15F (shape) — human accept lean  
3. **Deep / more T15C–E** only if lean needs more comparator meat or artifact design is contested — deepen the *paying* channels, don’t add random ones  
4. Draft Theme 15 report → accept → elevate (if any)

Do **not** auto-launch deep gatherer fleets from this brief alone.

## Explicit non-goals (scope fence)

- Skill that commits, pushes, opens/approves/merges PRs, or chooses squash vs merge  
- Universal “Toolbelt PR body format” as law for all hosts  
- Replacing host CONTRIBUTING / branch protection  
- Fat CI/Bugbot product inside the plugin  

## After accept

Hand off per track; keep draft notes until human accepts an integrated report.  
Elevation only after accept — prefer quality lean: useful structure for *defining* closeouts, zero ceremony ownership.
