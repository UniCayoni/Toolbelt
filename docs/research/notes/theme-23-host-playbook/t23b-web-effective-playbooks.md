---
title: "T23B-web — Effective playbooks / getting-started / operator guides (web)"
status: draft
theme: theme-23-host-playbook
track: T23B
gatherer: T23B-web
created: 2026-08-04
updated: 2026-08-04
authors: [t23b-web-gatherer]
depth: deep
waves: W1
stop_reason: diminishing_returns_primary_corpus
supersedes: null
---

# T23B-web — Effective playbooks online

**Using `research-protocol`** (+ `research-docs` habits: Diátaxis classify, official docs as E1 hypotheses, cite-or-omit). Depth: **deep**. Draft ≠ law.

## 1. Scope

- **Question / goal:** How should effective playbooks / getting-started / operator guides be written for developer tools and agent toolkits—especially for **plugin/extension hosts** adopting a toolbox?
- **In scope:** Genre distinctions (playbook / runbook / handbook / README); structure patterns (start here, progressive disclosure, task-oriented); anti-patterns; guidance transferable to Toolbelt host adoption playbooks.
- **Out of scope:** Toolbelt surface inventory (T23A); GitHub repo comparators (T23B-gh); RAG corpus pass (T23B-RAG); elevating `docs/host-playbook.md` (T23C); learn-back (Theme 24).
- **Comprehension / research goal type:** other (secondary web research for playbook craft).

## 2. Method (REQUIRED)

| Item | Value |
|------|-------|
| Date | 2026-08-04 |
| Tools used | WebSearch, WebFetch; local read of Theme 23 campaign brief |
| Corpora / URLs searched | See §9 Source list; Method envelope below |
| Queries (exact) | See below |
| What was *not* searched | Paid books beyond free SRE pages; proprietary internal handbooks; Alexandria RAG (sibling gatherer); GitHub org playbook repos (sibling T23B-gh); non-English sources; academic HCI progressive-disclosure papers beyond product docs |
| Depth | deep |
| Waves / stop_reason | W1; `diminishing_returns_primary_corpus` — Diátaxis + AWS WA playbook/runbook + Google SRE playbook + Write the Docs + Cursor/VS Code host-facing install/onboarding docs covered; further vendor blogs largely restated E1 without new atoms |
| Provenance (optional PROV) | Entity←fetched URLs; Activity=T23B-web gather 2026-08-04; Agent=WebSearch+WebFetch |

### Exact search terms

1. `Diátaxis documentation framework tutorials how-to explanation reference`
2. `Google SRE workbook runbooks effective practices documentation`
3. `Write the Docs playbook runbook handbook documentation best practices`
4. `site:sre.google playbook OR runbook documentation`
5. `developer portal getting started documentation progressive disclosure Backstage Spotify`
6. `VS Code extension marketplace README getting started user documentation best practices`
7. `playbook vs runbook vs handbook vs README documentation distinction`
8. `site:writethedocs.org documentation principles structure getting started`
9. `Cursor docs plugins install skills getting started host project`
10. `12-factor app developer experience documentation getting started`

### URLs accessed (WebFetch / retrieved), accessed 2026-08-04

| URL | Role |
|-----|------|
| https://www.diataxis.fr/ | E1 framework overview |
| https://www.diataxis.fr/how-to-guides/ | E1 how-to principles |
| https://www.diataxis.fr/tutorials/ | E1 tutorial principles |
| https://www.diataxis.fr/reference/ | E1 reference principles |
| https://www.diataxis.fr/quality/ | E1 quality / anti-mix |
| https://www.diataxis.fr/application/ | E1 apply-first workflow |
| https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html | E1 AWS runbook BP |
| https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html | E1 AWS playbook BP |
| https://sre.google/sre-book/introduction/ | E1 Google SRE playbook MTTR claim |
| https://sre.google/workbook/on-call/ | E1 on-call playbook content |
| https://sre.google/resources/practices-and-processes/incident-management-guide/ | E1 incident prep / up-to-date playbooks |
| https://www.writethedocs.org/guide/writing/docs-principles/ | E1 WTD principles |
| https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/ | E1 README / getting-started atoms |
| https://www.writethedocs.org/guide/writing/mindshare/ | E1 taxonomy / make-it-easy (search hit; light use) |
| https://cursor.com/docs/plugins | E1 Cursor plugin host install/manage |
| https://code.visualstudio.com/api/references/extension-manifest | E1 Marketplace README as adoption surface |
| https://code.visualstudio.com/api/references/extension-guidelines | E1 Walkthroughs / Settings UX for adopters |
| https://code.visualstudio.com/api/working-with-extensions/publishing-extension | E1 README/CHANGELOG/SUPPORT packaging |
| https://12factor.net/ | E1 declarative setup for new joiners |
| https://backstage.io/ | E1 templates as “automated getting started” |
| https://backstage.spotify.com/docs/portal/getting-started | E1 portal setup wizard → checklist |
| https://www.syntasso.io/post/why-implement-progressive-disclosure-in-your-internal-developer-platform-and-portal | E2 progressive disclosure in portals |

**Search hits noted but not treated as design law (E3 / marketing):** Trainual handbook-vs-playbook; Squadcast/Runframe runbook-vs-playbook blogs; Doc Holiday / Moxo runbook how-tos.

## 3. Strategy (if workspace/code)

| Field | Value |
|-------|-------|
| Mode | as-needed |
| Why this mode | Web secondary research; no local code corroboration required for craft patterns |
| Scope boundary | Public web primary docs only |

## 4. Findings

### 4.1 Genre distinctions

- `FACT` [E1] Diátaxis identifies **four** documentation forms tied to four needs: tutorials, how-to guides, technical reference, and explanation—and proposes organizing docs around those needs. [E1: Diátaxis home — https://www.diataxis.fr/ — accessed 2026-08-04]

- `FACT` [E1] Diátaxis how-to guides are **goal-oriented directions** for work (“action and only action”; link out digression/explanation/reference); tutorials are **learning-oriented lessons**; reference is **information-oriented** austere description; explanation serves understanding. [E1: How-to / Tutorials / Reference — https://www.diataxis.fr/how-to-guides/ , https://www.diataxis.fr/tutorials/ , https://www.diataxis.fr/reference/ — accessed 2026-08-04]

- `FACT` [E1] AWS Well-Architected defines a **runbook** as a documented process to achieve a **specific outcome** (step-by-step procedure / checklist), and a **playbook** as step-by-step guides used to **investigate** an incident (discovery → root cause), often pointing to a runbook to mitigate. [E1: OPS07-BP03 / OPS07-BP04 — https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html , https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html — accessed 2026-08-04]

- `FACT` [E1] Google SRE’s public book uses **“playbook”** for recorded on-call best practices / troubleshooting steps (claimed ~3× MTTR improvement vs “winging it”), and the Workbook describes playbooks as high-level alert-response instructions (severity, impact, debugging suggestions, mitigation). [E1: SRE Book Introduction — https://sre.google/sre-book/introduction/ — accessed 2026-08-04] [E1: Being On-Call — https://sre.google/workbook/on-call/ — accessed 2026-08-04]

- `CLAIM` [E2] Industry blogs commonly contrast **runbook = technical how** vs **playbook = coordination / broader process** (roles, escalation)—this **does not match** AWS’s investigate-vs-execute split nor Google’s alert-playbook usage. Premises for caution: E3 vendors; treat as terminology hazard, not Toolbelt vocabulary. [E3 discovery only via search snippets; not used for locks]

- `FACT` [E1] Write the Docs beginners’ guide treats **README** as often the **first user interaction**: problem statement, small example, install (keep basic case short; link caveats), support, contribute, license—audience split Users vs Developers. [E1: How to write software documentation — https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/ — accessed 2026-08-04]

- `GAP` Canonical primary definition of **handbook** vs playbook/runbook in SRE/Diátaxis corpora. Searched: Diátaxis, AWS WA playbook/runbook pages, Google SRE playbook pages, WTD principles. Result: no stable handbook definition in those E1 pages; handbook distinctions appear mainly in HR/ops marketing (E3). Prefer Theme 23 brief’s working vocabulary for Toolbelt “Playbook.”

- `INFERENCE` [E4] For Theme 23, a **host adoption playbook** is closest to a **Diátaxis how-to (plus a short tutorial-shaped happy path)**, not an AWS incident-investigation playbook—but it should borrow SRE/AWS habits of **task orientation, ownership, and update-on-change**. Premises: (1) Theme 23 brief defines Playbook as host setup + use; (2) Diátaxis how-to = goal-oriented work; (3) AWS/Google “playbook” terms conflict (see §6).

### 4.2 Structure patterns

- `FACT` [E1] Diátaxis how-tos: user-need titles (“How to …”), logical sequence / flow, omit unnecessary completeness, allow adaptability, **do not** bury teaching or encyclopedic options in the action path—link to reference/explanation. [E1: https://www.diataxis.fr/how-to-guides/ — accessed 2026-08-04]

- `FACT` [E1] Diátaxis tutorials: show destination early; visible results early/often; narrative of expected output; **ruthlessly minimize explanation**; ignore options/alternatives; aspire to reliability. [E1: https://www.diataxis.fr/tutorials/ — accessed 2026-08-04]

- `FACT` [E1] Diátaxis recommends **applying ideas immediately** and iterating rather than waiting for full theory comprehension—itself a progressive “start here by doing” stance. [E1: Applying Diátaxis — https://www.diataxis.fr/application/ — accessed 2026-08-04]

- `FACT` [E1] Write the Docs content principles relevant to playbooks: **Skimmable** (descriptive headings; concepts early in paragraphs); **Exemplary** (some examples/tutorials, not for everything; separate from dense reference); **Cumulative** (prerequisites first; tutorials/examples before reference when separated); **Current** (“incorrect documentation … worse than missing”); **Nearby** sources next to code; **Unique** sources (no overlapping SoTs); **Discoverable** pointers on likely paths. [E1: Documentation principles — https://www.writethedocs.org/guide/writing/docs-principles/ — accessed 2026-08-04]

- `FACT` [E1] AWS runbook/playbook templates encode metadata atoms: desired outcome / incident purpose, tools, permissions, author, last updated, escalation POC; playbooks also stakeholders + communication plan; steps as ordered checklist; validate by having another person run it; store in VCS; update with change management. [E1: AWS OPS07-BP03/BP04 — accessed 2026-08-04]

- `FACT` [E1] Google SRE: new alerts should get a **corresponding playbook entry**; pages/consoles should link playbooks; on-callers **update playbooks when the page fires**; awareness + practice (e.g. Wheel of Misfortune) required for effectiveness. [E1: https://sre.google/workbook/on-call/ ; https://sre.google/resources/practices-and-processes/incident-management-guide/ — accessed 2026-08-04]

- `FACT` [E1] Twelve-Factor intro states methodology aims include **declarative formats for setup automation, to minimize time and cost for new developers joining the project**. [E1: https://12factor.net/ — accessed 2026-08-04]

- `FACT` [E1] Backstage positions Software Templates as **“Like automated getting started guides”** (golden-path bootstrap). [E1: https://backstage.io/ — accessed 2026-08-04]

- `FACT` [E1] Spotify Portal getting-started uses **prerequisites → setup wizard → Setup Guide checklist** (essential plugins, step-by-step config, docs/troubleshooting links, best practices)—a progressive disclosure of depth after first success. [E1: https://backstage.spotify.com/docs/portal/getting-started — accessed 2026-08-04]

- `CLAIM` [E2] Progressive disclosure in developer portals: hide advanced config until needed; opinionated defaults; avoid overwhelming bootstrap options—while still allowing “break glass” for power users. [E2: Syntasso — https://www.syntasso.io/post/why-implement-progressive-disclosure-in-your-internal-developer-platform-and-portal — accessed 2026-08-04]

### 4.3 Anti-patterns

- `FACT` [E1] AWS runbook anti-patterns include: relying on memory; manual changes without checklist; inconsistent steps/outcomes across people; **letting runbooks drift** out of sync with system/automation. [E1: OPS07-BP03 — accessed 2026-08-04]

- `FACT` [E1] AWS playbook anti-patterns include: no standard investigation path; relying on tribal knowledge; trial-and-error onboarding for troubleshooting; best practices not shared. [E1: OPS07-BP04 — accessed 2026-08-04]

- `FACT` [E1] Diátaxis: conflating tutorials with how-tos is a root of many doc problems; polluting how-tos with every option / explanation dilutes action; auto-generated reference alone is insufficient as “all documentation.” [E1: how-to-guides + reference pages — accessed 2026-08-04]

- `FACT` [E1] Write the Docs: FAQ-as-docs anti-pattern (stale, unsorted catch-all, fake “frequent” questions, quick-fix instead of real docs); **incorrect docs worse than missing**; overlapping parallel sources. [E1: beginners-guide + docs-principles — accessed 2026-08-04]

- `FACT` [E1] Diátaxis quality: docs can be “accurate, complete, consistent and also useless”; mixing modes disrupts **flow** (e.g. explanation interrupting a how-to). [E1: https://www.diataxis.fr/quality/ — accessed 2026-08-04]

- `INFERENCE` [E4] A **wall-of-reference skill catalog** as the host’s first page is an anti-pattern for adoption (violates how-to focus, skimmability, cumulative start, progressive disclosure). Premises: Diátaxis how-to/reference separation; WTD skimmable/cumulative/exemplary; portal wizard→checklist pattern.

### 4.4 Plugin / extension host adoption (end-user / consumer project)

- `FACT` [E1] Cursor plugins package rules, skills, agents, commands, MCP servers, and hooks; hosts install/manage from **Customize** (or Marketplace); scope can be **project or user**; rules modes Always / Agent Decides / Manual; skills invokable via `/skill-name`; local test path `~/.cursor/plugins/local/<name>` + reload. [E1: https://cursor.com/docs/plugins — accessed 2026-08-04]

- `FACT` [E1] Cursor documents **plugin canvases** as “shared setup templates” / “guided starting point instead of configuring everything from scratch”—onboarding affordance beyond raw component lists. [E1: https://cursor.com/docs/plugins — accessed 2026-08-04]

- `FACT` [E1] VS Code Marketplace presents extension **README.md** as the body of the extension details page; packaging guidance also calls for CHANGELOG.md and SUPPORT.md; displayName/description/keywords matter for discovery. [E1: Extension Manifest Marketplace tips — https://code.visualstudio.com/api/references/extension-manifest — accessed 2026-08-04] [E1: Publishing Extensions — https://code.visualstudio.com/api/working-with-extensions/publishing-extension — accessed 2026-08-04]

- `FACT` [E1] VS Code UX Guidelines list **Walkthroughs** as “a consistent experience for onboarding users to an extension via a multi-step checklist featuring rich content,” plus Settings for configuration. [E1: https://code.visualstudio.com/api/references/extension-guidelines — accessed 2026-08-04]

- `INFERENCE` [E4] Host playbooks for agent toolkits should mirror extension-adoption UX: **install → verify components visible → shortest happy path → when-not / next skill → compact inventory link**, with README as pointer (not encyclopedia). Premises: Cursor Customize/install facts; VS Code README+Walkthrough pattern; Diátaxis/WTD structure facts above.

## 5. Hypothesis log

| ID | Hypothesis | Status | Evidence |
|----|------------|--------|----------|
| H1 | Effective host playbooks are primarily how-to (+ short tutorial), with inventory as linked reference | confirmed (for craft recommendation; not product lock) | Diátaxis E1; WTD cumulative/exemplary; Theme 23 brief vocabulary |
| H2 | “Playbook” has one industry meaning | rejected | AWS vs Google E1 conflict (§6) |
| H3 | Stale catalogs are a first-order failure mode | confirmed (as guidance) | AWS drift anti-pattern; WTD Current; SRE update-when-fires |

## 6. Conflicts

| Topic | Source A | Source B | Resolution |
|-------|----------|----------|------------|
| Meaning of “playbook” | AWS: investigate incidents; may hand off to runbook for mitigation [E1 OPS07-BP04] | Google SRE: on-call alert-response / troubleshooting “playbook” (often includes mitigation steps) [E1 SRE intro + on-call] | **Log conflict.** For Toolbelt Theme 23, prefer brief’s definition (host setup + use). When citing ops literature, qualify “AWS playbook” vs “SRE playbook.” |
| Runbook vs playbook breadth | AWS: runbook = known procedure outcome; playbook = investigation | Vendor blogs (E3): playbook = coordination; runbook = technical how | Prefer AWS E1 for ops taxonomy; do not lock Toolbelt naming to E3 blogs. |

## 7. Gaps & OPEN

- `GAP` No E1 page found that defines **handbook** in the same rigorous quartet as Diátaxis or AWS playbook/runbook. Searched Diátaxis, AWS WA, Google SRE, WTD principles.
- `GAP` Cursor docs fetched cover **install/manage/create** plugins; thin on a prescribed **host-project operating playbook** template for a multi-skill toolkit (beyond canvases mention). Searched cursor.com/docs/plugins.
- `GAP` VS Code docs are explicit that Marketplace README content is **not highly prescriptive** (wide extension diversity)—confirmed via search hit on vscode-docs issue #5357 (community/doc maintainer reply); treat as soft guidance.
- `OPEN` Exact balance for Toolbelt: embed compact catalog in playbook vs link-only inventory appendix (Theme 23 brief listed as pre-gather GAP)—needs human lean after T23A inventory exists.
- `OPEN` Whether host playbook should include a Diátaxis-style **explanation** pocket (“why Toolbelt pockets exist”) or keep explanation only in `guide-meta` / reports.
- `OPEN` Corroborate progressive-disclosure claims with T23B-RAG / T23B-gh examples of real host playbooks.

## 8. Implications (INFERENCE only)

### 8.1 Recommended TOC atoms for a Toolbelt host playbook

`INFERENCE` [E4] Recommended **TOC atoms** (not a locked SoT outline). Premises: P1 Diátaxis how-to/tutorial/reference separation; P2 WTD README atoms + skimmable/cumulative/current/nearby/unique; P3 AWS metadata + validate-by-second-person + VCS; P4 SRE link-from-trigger + update-on-use; P5 Cursor install→Customize verification + guided start; P6 VS Code Walkthrough/README as progressive onboarding; P7 Theme 23 brief (setup + start `guide-meta` + flow map + when-not + inventory).

| # | Atom | Role (Diátaxis-ish) | Notes |
|---|------|---------------------|-------|
| A1 | **Purpose / who this is for** | Explanation (1 short ¶) or how-to preamble | Host consumer project—not plugin CONTRIBUTING |
| A2 | **Prerequisites** | How-to | Cursor version/status GAP if unknown; install path (Marketplace / local plugin path) |
| A3 | **Install & verify** | Tutorial-shaped how-to | Shortest path; expected signals in Customize (rules/skills visible) |
| A4 | **Start here (happy path)** | Tutorial / how-to | Point to `guide-meta` (or agreed entry skill); one concrete first task; expected outcome |
| A5 | **Task map (common host jobs)** | How-to index | Goal-titled links (“How to research X”, “How to implement Y”)—not skill dump |
| A6 | **When not / limits** | How-to boundaries | Explicit out-of-scope; prevents wrong-tool use |
| A7 | **Flow / handoffs** | How-to + thin explanation | Pocket → next skill; avoid embedding full PROTOCOL |
| A8 | **Compact inventory pointer** | Reference (linked) | Full matrix lives in T23A inventory / appendix—playbook stays thin |
| A9 | **Maintenance contract** | Meta how-to | Owner; “surfaces change → update playbook/inventory”; last-updated |
| A10 | **Escalation / support** | How-to | Where hosts get help (issues, SUPPORT)—WTD/VS Code pattern |
| A11 | **Pointers** | Discoverability | README + packs + `guide-meta` link back to this playbook |

**Anti-atoms (do not lead with):** full skill encyclopedia; FAQ blob; contributor CI ceremony; learn-back retrospectives (Theme 24).

### 8.2 Structural recommendations (craft)

1. Lead with **install → verify → one happy path**, then task-oriented how-tos (Diátaxis + portal wizard pattern).
2. Keep **reference inventory linked**, not inline as the first screen (WTD exemplary/cumulative; Diátaxis reference separation).
3. Title sections by **host goals**, not by machinery/skill filenames (Diátaxis how-to naming).
4. Encode **freshness**: owner, last-updated, update-when-surfaces-change (AWS + SRE + WTD Current).
5. Use README/Marketplace/Customize as **discoverability pointers** into the playbook—not as the full operator guide (VS Code/Cursor + WTD Discoverable).

## 9. Source list (deduped)

1. https://www.diataxis.fr/ — accessed 2026-08-04
2. https://www.diataxis.fr/how-to-guides/ — accessed 2026-08-04
3. https://www.diataxis.fr/tutorials/ — accessed 2026-08-04
4. https://www.diataxis.fr/reference/ — accessed 2026-08-04
5. https://www.diataxis.fr/quality/ — accessed 2026-08-04
6. https://www.diataxis.fr/application/ — accessed 2026-08-04
7. https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html — accessed 2026-08-04
8. https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html — accessed 2026-08-04
9. https://sre.google/sre-book/introduction/ — accessed 2026-08-04
10. https://sre.google/workbook/on-call/ — accessed 2026-08-04
11. https://sre.google/resources/practices-and-processes/incident-management-guide/ — accessed 2026-08-04
12. https://www.writethedocs.org/guide/writing/docs-principles/ — accessed 2026-08-04
13. https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/ — accessed 2026-08-04
14. https://cursor.com/docs/plugins — accessed 2026-08-04
15. https://code.visualstudio.com/api/references/extension-manifest — accessed 2026-08-04
16. https://code.visualstudio.com/api/references/extension-guidelines — accessed 2026-08-04
17. https://code.visualstudio.com/api/working-with-extensions/publishing-extension — accessed 2026-08-04
18. https://12factor.net/ — accessed 2026-08-04
19. https://backstage.io/ — accessed 2026-08-04
20. https://backstage.spotify.com/docs/portal/getting-started — accessed 2026-08-04
21. https://www.syntasso.io/post/why-implement-progressive-disclosure-in-your-internal-developer-platform-and-portal — accessed 2026-08-04 (E2)
22. `docs/research/notes/theme-23-host-playbook/campaign-brief.md` — local Theme 23 vocabulary (accepted brief; not playbook craft E1)

## Self-check

- [x] Depth chosen and recorded (`deep`)
- [x] Deep stop_reason recorded
- [x] Method block present
- [x] Every FACT/CLAIM has support
- [x] INFERENCEs list premises
- [x] No invented citations/quotes
- [x] Conflicts logged
- [x] Draft/proposed not treated as design law
