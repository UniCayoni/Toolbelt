# T1C — Program comprehension / codebase understanding methods (notes)

Status: notes only (not integrated report)  
Created: 2026-07-27  
Agent: t1c-program-comprehension-methods  
Protocol: `docs/research/PROTOCOL.md`

## 1. Scope

Classical and modern **program comprehension / codebase understanding** methods that may transfer to AI-agent research protocols:

- Top-down vs bottom-up comprehension
- Beacons, plans, systematic vs as-needed reading
- Architecture recovery and dependency mapping
- Research software engineering (RSE) practices for reproducible investigation

Out of scope for this note: GreyMatter plugin stub/scaffolding; locking RAG/GraphRAG library choices; MVP feature scope.

## 2. Method (tools, queries, date)

**Date:** 2026-07-27

**Tools:**

1. Alexandria MCP `user-alexandria-rag`: `GetMcpTools` → `list_corpora`, `describe_corpus`, `list_documents`, `rag_probe`, `rag_query` on corpus `software_engineering` (21 docs / 7712 chunks; hierarchical retrieval unavailable).
2. Web search + open full-text / PDF fetches for landmark PC papers (von Mayrhauser & Vans 1995; Storey et al. cognitive design elements; Ducasse/Pollet SAR taxonomy PDF; Storey 2005/2006 survey materials).
3. Local protocol file read: `d:\GreyMatter\docs\research\PROTOCOL.md` [E0].

**Alexandria probes (corpus=`software_engineering`):**

| Question / topic | Verdict |
|------------------|---------|
| program comprehension top-down bottom-up beacons plans systematic vs as-needed reading | partial |
| architecture recovery dependency mapping codebase understanding reverse engineering | partial |
| research software engineering reproducible investigation documentation version control testing | partial |
| von Mayrhauser Vans Storey Letovsky Brooks program comprehension model | partial |

**Alexandria rag_query questions (k=6–10):**

- How do developers recover software architecture, map dependencies, and understand layered structure of a codebase?
- research software engineering practices for reproducible investigation documentation version control testing project organization
- how programmers read and understand unfamiliar code systematically bottom-up top-down beacons plans
- AI assisted codebase understanding exploration navigating large codebases mental model
- cyclic dependencies package dependency graph architecture review visualization understanding codebase for new developers
- Make build automation provenance FAIR data inspectable reproducible analyses documentation README LICENSE

**Web / open PDF landmarks sought:** von Mayrhauser & Vans (IEEE Computer 1995); Storey / Storey–Fracchia–Müller cognitive design elements; Littman et al. systematic vs as-needed; Letovsky cognitive processes; Ducasse & Pollet architecture reconstruction taxonomy; related course slides used only as secondary pointers when primary open text available.

**Corpus composition note [E0]:** `software_engineering` is dominated by practitioner books (Clean Architecture, Architecture Patterns with Python, Software Architecture Metrics, RSE with Python, Beyond Vibe Coding, etc.). Classical empirical PC papers are **not** indexed as primary documents in this corpus (probe/list_documents).

---

## 3. Findings

### 3.1 Shared elements of classical cognition models

- `FACT` [E1] Program comprehension during maintenance/evolution is framed as using existing knowledge to acquire new knowledge and build a **mental model** of the software; strategies formulate hypotheses then resolve, revise, or abandon them. [E1: von Mayrhauser & Vans, “Program Comprehension During Software Maintenance and Evolution,” *IEEE Computer*, 28(8), 1995 — open PDF https://www.cs.kent.edu/~jmaletic/cs63902/Papers/ProgramComprehension/von_mayrhauser-1995.pdf — DOI https://doi.org/10.1109/2.402076 — accessed 2026-07-27]

- `FACT` [E1] Mental-model static entities include text structures, chunks, **plans**, **hypotheses**, **beacons**, and **rules of discourse**; dynamic elements include strategies, chunking, and cross-referencing across abstraction levels. [E1: same von Mayrhauser & Vans 1995 PDF]

- `FACT` [E1] The survey compares six models: Letovsky (1986); Shneiderman & Mayer (1979); Brooks (1983); Soloway, Adelson & Ehrlich top-down; Pennington bottom-up; and von Mayrhauser & Vans integrated metamodel. [E1: same; also Crossref metadata via DOI page]

- `FACT` [E1] Authors note many models assume the goal is to understand **all** of the code; specialized tasks may use strategies for **partial** understanding; open questions include scalability of small-program experiments to large-scale maintenance. [E1: von Mayrhauser & Vans 1995]

### 3.2 Top-down vs bottom-up

- `FACT` [E1] **Bottom-up:** read source, chunk statements into higher abstractions, aggregate until high-level understanding; Shneiderman & Mayer distinguish syntactic vs semantic knowledge; Pennington’s **program model** (control-flow) then **situation model** (data-flow / functional). [E1: Storey, Fracchia & Müller, “Cognitive Design Elements to Support the Construction of a Mental Model during Software Exploration,” open PDF https://plg.uwaterloo.ca/~migod/846/papers/storey-jss.pdf — accessed 2026-07-27; consistent restatement in von Mayrhauser & Vans 1995]

- `FACT` [E1] **Top-down:** Brooks — reconstruct domain knowledge and map to code via hierarchical hypotheses verified by **beacons**; Soloway & Ehrlich — top-down when code/type is familiar, using **programming plans** and **rules of discourse**. [E1: Storey et al. JSS PDF; von Mayrhauser & Vans 1995]

- `FACT` [E1] **Opportunistic / hybrid:** Letovsky — knowledge base + layered mental model + assimilation that may proceed top-down or bottom-up depending on cues; inquiry episodes (question → conjecture → search). [E1: von Mayrhauser & Vans 1995; Storey et al. JSS PDF]

- `FACT` [E1] **Integrated metamodel** (von Mayrhauser & Vans): programmers switch among top-down domain model, program model, and situation model; any process may activate at any time (differs from strictly sequential Pennington staging). [E1: Storey et al. JSS PDF summarizing von Mayrhauser & Vans; von Mayrhauser & Vans 1995]

- `CLAIM` [E2] Practitioner SE books discuss top-down/bottom-up mainly as **design/decomposition** (stepwise refinement), not as empirical PC theory — useful analogy but not a substitute for PC models. [E2: Alexandria `software_engineering` source=`Software Development, Design, and Coding... (Dooley & Kazakova).pdf` chunk_id=`f9e86aad8c6bbcd8899a58c1` query=`how programmers read and understand unfamiliar code systematically...`]

### 3.3 Beacons, plans, rules of discourse

- `FACT` [E1] **Beacon:** cues indexing into knowledge (e.g., swap-in-loop or procedure name `Sort` as beacon for sorting); useful for high-level understanding; hypothesis verification depends heavily on presence/absence of beacons (Brooks). [E1: von Mayrhauser & Vans 1995; Storey et al. JSS PDF]

- `FACT` [E1] **Plans:** schemas with slot types/fillers; programming plans (search/sort/sum, control constructs) vs domain plans; causal knowledge about information flow between parts. [E1: von Mayrhauser & Vans 1995]

- `FACT` [E1] **Rules of discourse:** programming conventions (coding standards, expected algorithm/data-structure use) that set expectations for retrieving plans; experts perform better on plan-like than non-plan-like code (Soloway, Adelson & Ehrlich, as reported). [E1: von Mayrhauser & Vans 1995]

- `FACT` [E1] **Delocalized plans:** conceptually related code in non-contiguous locations; inquiry episodes often triggered by them; local clues alone can mislead maintainers. [E1: Storey et al. JSS PDF; Letovsky & Soloway “Delocalized Plans and Program Comprehension,” *IEEE Software*, 1986 — DOI https://doi.org/10.1109/ms.1986.233414 abstract/metadata — `GAP` full text not read this pass]

### 3.4 Systematic vs as-needed reading

- `FACT` [E1] Littman et al. (1986) observed two macro-strategies: **systematic** (methodical reading, tracing control- and data-flow for global understanding → static + causal knowledge) vs **as-needed** (only task-relevant code → mostly static knowledge, weaker mental model, more errors from missed causal interactions). [E1: Storey et al. JSS PDF restating Littman et al., “Mental models and software maintenance,” *Empirical Studies of Programmers*, 1986, pp. 80–98]

- `FACT` [E1] Systematic reading of **entire** large programs is often unrealistic; as-needed is common in practice. [E1: Storey et al. JSS PDF]

- `GAP` Primary Littman et al. 1986 full text not obtained this pass (book chapter / ESP proceedings). Claims above rely on Storey’s careful secondary synthesis of that study. Prefer primary read on follow-up. `OPEN`

### 3.5 Architecture recovery & dependency mapping

- `FACT` [E1] Architecture is **not** explicitly represented in code like classes/packages; successful systems evolve so conceptual vs implemented architecture drifts (erosion/drift/mismatch) — motivating software architecture reconstruction (SAR). [E1: Pollet, Ducasse et al., “Towards A Process-Oriented Software Architecture Reconstruction Taxonomy,” open PDF http://staff.cs.upt.ro/~ioana/arhitrec/SARtaxonomy.pdf — accessed 2026-07-27; journal version Ducasse & Pollet, *IEEE TSE*, 2009 — DOI https://doi.org/10.1109/tse.2009.19]

- `FACT` [E1] SAR taxonomy axes: goals, processes (**bottom-up / top-down / hybrid**), inputs (source, dynamic, historical, human expertise, styles/viewpoints), techniques (automation spectrum), outputs (architectural views, conformance, etc.). Bottom-up recovery closely related to Tilley extract–abstract–present cycle. [E1: same SAR taxonomy PDF]

- `FACT` [E1] Reverse-engineering activity sets: data gathering (static/dynamic), knowledge organization/abstraction, information exploration (navigation/analysis/presentation); exploration held as key to understanding. [E1: Storey et al. JSS PDF citing Tilley et al.]

- `FACT` [E2] Practitioner dependency guidance: dependencies form a network/graph; layered architectures constrain who may call whom; DIP keeps high-level modules independent of low-level details. [E2: Alexandria `Architecture Patterns with Python...pdf` chunk_id=`e40ca95ba90247f81250fb0f` query=`How do developers recover software architecture...`]

- `FACT` [E2] Large **cyclic dependency** groups hinder isolation testing and make a randomly picked file potentially depend on almost everything — harder for newcomers to understand; package/namespace cycles especially harmful to architectural intent. [E2: Alexandria `Software Architecture Metrics...pdf` chunk_id=`1d71c4d5be5874d033ad5637` query=`cyclic dependencies package dependency graph...`]

- `FACT` [E2] Acyclic dependency graphs matter for release/test isolation; cycles collapse components into effectively one unit (“morning after syndrome”). [E2: Alexandria corpus=`software_engineering` source=`Martin, Robert - Clean Architecture_ a Craftsman's Guide to Software Structure and Design (2017, Prentice Hall) - libgen.li.pdf` chunk_id=`c97d40655cde9d36e2f2450a` page=143 query=`cyclic dependencies package dependency graph...`]

- `FACT` [E2] Visualizing the real dependency structure often reveals relaxed layering / unexpected bypasses that code review discipline missed. [E2: Alexandria same Martin Clean Architecture PDF chunk_id=`4e455075dd9766e48133bdee` query=`How do developers recover software architecture...`]

- `INFERENCE` [E4] Architecture recovery for agents maps cleanly onto PC strategies: bottom-up SAR ≈ extract–abstract–present; top-down SAR ≈ hypothesis/style-driven matching of expected architecture to code; hybrid ≈ integrated metamodel switching. Premises: SAR taxonomy process axis [E1 Ducasse/Pollet]; PC integrated metamodel [E1 von Mayrhauser/Storey].

### 3.6 Research software engineering — reproducible investigation

- `FACT` [E2] RSE approach rests on three related but distinct concepts: **open science**, **reproducible research** (anyone with data+software can re-run to same result), **sustainable software**; conflating them is incorrect (open≠reproducible). [E2: Alexandria `Research Software Engineering with Python...pdf` chunk_id=`b3f66c91f85ac315cc9fb4e4` query=`research software engineering practices...`]

- `FACT` [E2] Version control (esp. Git) tracks revision history and who changed what; cornerstone of reproducible research in this text. [E2: same source chunk_id=`b633a4e092c122ea3dee54b9`]

- `FACT` [E2] Project layout template (Noble 2009 style): `bin/` programs, `data/` immutable raw, `results/` derived, `docs/` documentation; boilerplate README, LICENSE, CONTRIBUTING, CONDUCT, CITATION. [E2: same source chunk_id=`b71421fc4a4481471f0e7759`]

- `FACT` [E2] Provenance checklist: publish data+code; DOIs/ORCID; FAIR data; archive env + analysis scripts + processing steps; make analyses **inspectable as well as reproducible**. [E2: same source chunk_ids=`245896ed8d8a34a06ee63e98`, `02425b323121386cf89fa1ff`]

- `FACT` [E2] Build managers (Make) encode dependency order of multi-step analyses so steps are not forgotten and others can re-run. [E2: same source chunk_id=`baa84d0e510e0ecb2f189152`]

- `FACT` [E2] Testing: unit/integration/regression, coverage, CI; assertions and pytest-style frameworks listed as learning objectives/key points. [E2: same source chunk_ids=`c298696c91585e8aff2cbdd9`, `245896ed8d8a34a06ee63e98`]

### 3.7 Modern / AI-era codebase understanding (practitioner)

- `CLAIM` [E3/E2] Practitioner claim (Sourcegraph/Cody narrative): ~80% of developer time is reading/understanding code, not creating it; whole-codebase scan + library context improves AI assistance. [E2/E3: Alexandria `AI-Assisted Programming... (Taulli).pdf` chunk_id=`780619c4a3a54d9451e22e30` — secondary/practitioner; treat as hypothesis for agent design, not empirical PC result]

- `FACT` [E2] Guidance for large codebases with AI: prefer models with large context; provide rich context (data models, patterns, error handling); iterative refine rather than one-shot; self-critique of generated code. [E2: Alexandria `Beyond Vibe Coding... (Osmani).epub` chunk_id=`fde4258e50a780245d5d83d6`]

- `FACT` [E2] Distinguishes **vibe coding** (exploratory, low scaffolding) vs **AI-assisted engineering** (plan → targeted AI → human review); warns evolving production systems need quality/understandability of underlying code. [E2: same source chunk_ids=`1022d8da38d4091cca8c5f43`, `49b2ca032561247cddb762d0`]

- `INFERENCE` [E4] AI “as-needed” retrieval over snippets without causal/control-flow tracing mirrors Littman as-needed risks (missed interactions). Premises: Littman strategies [E1 via Storey]; Osmani/Taulli emphasize full-context / review discipline [E2].

### 3.8 Transferable steps for agent research protocols

Candidate protocol steps (each tied to evidence; not GreyMatter product design locks):

1. `INFERENCE` [E4] **State the comprehension goal** (adaptive/perfective/corrective/reuse/leverage or “understand for X”) — von Mayrhauser tables of tasks/activities. Premises: [E1 von Mayrhauser 1995].

2. `INFERENCE` [E4] **Choose strategy mode:** systematic (broader control/data-flow pass) vs as-needed (task slice), and record which — Littman via Storey. Premises: [E1 Storey JSS]. For large systems, plan **scoped systematic** regions rather than whole-repo systematic.

3. `INFERENCE` [E4] **Alternate top-down and bottom-up:** start with domain/architecture hypotheses when familiar; fall back to program-model (structure/control-flow) when unfamiliar; build situation-model (data/functional) as evidence accumulates — integrated metamodel. Premises: [E1 Storey JSS; von Mayrhauser 1995].

4. `INFERENCE` [E4] **Seek beacons and plans; flag delocalized plans:** names, idioms, discourse-rule matches as hypothesis evidence; when related logic is scattered, run inquiry episodes (question → conjecture → search). Premises: [E1 von Mayrhauser; Storey; Letovsky abstract].

5. `INFERENCE` [E4] **Recover architecture explicitly:** extract dependencies → abstract modules/layers → present views; compare expected vs implemented (conformance); note cycles as comprehension hazards. Premises: [E1 Ducasse/Pollet]; [E2 Architecture Metrics; Clean Architecture].

6. `INFERENCE` [E4] **Make the investigation reproducible (RSE):** version-control notes and artifacts; immutable raw inputs; scripted/Make-like pipeline for analyses; document env; separate open vs reproducible vs sustainable claims. Premises: [E2 RSE with Python].

7. `INFERENCE` [E4] **Keep a written mental-model artifact** (hypotheses, confirmed/rejected, open inquiries, dependency sketch) analogous to annotation layer / dangling-purpose links in Letovsky. Premises: [E1 von Mayrhauser on Letovsky].

8. `INFERENCE` [E4] If using AI tools: treat outputs as conjectures requiring verification against code; prefer rich project context over isolated snippets. Premises: [E2 Osmani; Taulli]; aligned with hypothesis-driven PC [E1].

---

## 4. Contradictions / conflicts found

- `FACT` [E1] Model conflict (documented, not unresolved error): Pennington-style staging (situation model after full program model) vs von Mayrhauser & Vans (situation model after **partial** program model; concurrent switching). Storey explicitly notes this difference. [E1: Storey et al. JSS PDF]

- `FACT` [E1] Letovsky: assimilation is opportunistic top-down **or** bottom-up by cue; integrated metamodel: **any** of three processes may activate anytime — related but not identical. [E1: Storey et al. JSS PDF]

- `CLAIM` [E2 vs E1] Clean Code “Stepdown Rule” (read code as top-down narrative of abstractions) is an **authoring** guideline, not an empirical claim about how maintainers actually comprehend unfamiliar systems. Do not equate with Brooks/Soloway top-down comprehension without caveat. [E2: Alexandria `Clean Code...pdf` chunk_id=`869ed3f4a4fd4aef95f4a2cc`; contrast E1 PC literature]

- No contradiction found that RSE “reproducible” equals “open”; Irving et al. explicitly separates them. [E2]

---

## 5. Gaps

- `GAP` Alexandria `software_engineering` does **not** index primary PC papers (von Mayrhauser, Storey journal articles, Letovsky, Littman, Pennington, Brooks) as documents — only partial topical overlap via practitioner books. Confirmed via `list_documents` + probes [E0].

- `GAP` Littman et al. 1986 primary full text not read this pass; Soloway et al. CACM 1988 on documentation for delocalized plans not full-text this pass.

- `GAP` Letovsky 1987 *JSS* “Cognitive processes in program comprehension” — DOI known (10.1016/0164-1212(87)90032-x); full text not obtained this pass (cite via von Mayrhauser/Storey secondary + IEEE Software 1986 abstract).

- `GAP` Storey 2006 *Software Quality Journal* “Theories, tools and research methods in program comprehension” — Springer page/abstract accessed; full paywalled; used open Storey–Fracchia–Müller JSS PDF and open IWPC/course PDF mirrors for theory content. Prefer SQJ primary on follow-up. DOI: https://doi.org/10.1007/s11219-006-9216-4

- `GAP` Ducasse & Pollet *IEEE TSE* 2009 full publisher PDF not required (open CSMR/taxonomy PDF used); journal pagination/citation should be verified against publisher copy when integrating.

- `GAP` No empirical study retrieved this pass that **directly** measures LLM/agent comprehension strategies against Littman systematic/as-needed outcomes. AI transfer remains `INFERENCE`/`OPEN`.

- `GAP` Feature location / concept assignment literature (related to as-needed navigation) not surveyed deeply this slice. `OPEN`

- `OPEN` How to operationalize “beacon” detection for agents (static heuristics vs embedding similarity vs name/API patterns) without inventing psychology claims.

---

## 6. Candidate patterns for templates (still cited)

| Pattern ID | Pattern (for later templates) | Evidence |
|------------|-------------------------------|----------|
| PC-GOAL | Declare maintenance/comprehension task type before exploring | [E1 von Mayrhauser 1995] |
| PC-STRAT | Label session strategy: systematic \| as-needed \| hybrid; justify scope | [E1 Storey←Littman] |
| PC-HYPO | Hypothesis log: why/how/what conjectures; accept/reject/revise | [E1 von Mayrhauser←Letovsky/Brooks] |
| PC-BEACON | Record beacons/plans/discourse matches used as evidence | [E1 von Mayrhauser; Storey] |
| PC-INQUIRY | Inquiry episode: question → conjecture → search → result | [E1 Storey←Letovsky] |
| PC-MODEL | Maintain parallel notes: domain / program (control) / situation (data+function) | [E1 integrated metamodel] |
| SAR-EXTRACT | Dependency extract → abstract modules → present view → conformance check | [E1 Ducasse/Pollet; Tilley via Storey] |
| SAR-CYCLES | Flag cyclic dependency groups as comprehension/testability hazards | [E2 Architecture Metrics; Clean Architecture] |
| RSE-LAYOUT | Separate code / raw data / results / docs; never mutate raw | [E2 RSE with Python] |
| RSE-PROV | Record env + steps + versions; prefer inspectable automation (Make/CI) | [E2 RSE with Python] |
| AI-VERIFY | Treat AI summaries as conjectures; verify against code/deps | [E2 Osmani; E1 hypothesis-driven PC] |

---

## 7. Source list (deduped)

### Primary / open full text (E1)

1. A. von Mayrhauser & A. M. Vans, “Program Comprehension During Software Maintenance and Evolution,” *IEEE Computer*, 28(8):44–55, 1995. DOI: https://doi.org/10.1109/2.402076 — open PDF: https://www.cs.kent.edu/~jmaletic/cs63902/Papers/ProgramComprehension/von_mayrhauser-1995.pdf
2. M.-A. D. Storey, F. D. Fracchia, H. A. Müller, “Cognitive Design Elements to Support the Construction of a Mental Model during Software Exploration,” *Journal of Systems and Software* (special issue on Program Comprehension), ~1999 — open PDF: https://plg.uwaterloo.ca/~migod/846/papers/storey-jss.pdf (also WPC’97 related: https://rigi.cs.uvic.ca/downloads/papers/pdf/wpc97.pdf)
3. D. Pollet, S. Ducasse, et al., “Towards A Process-Oriented Software Architecture Reconstruction Taxonomy,” CSMR 2007 related open PDF: http://staff.cs.upt.ro/~ioana/arhitrec/SARtaxonomy.pdf — journal: S. Ducasse & D. Pollet, “Software Architecture Reconstruction: A Process-Oriented Taxonomy,” *IEEE TSE*, 35(4):573–591, 2009. DOI: https://doi.org/10.1109/tse.2009.19

### Abstract / metadata only or secondary this pass (mark carefully)

4. S. Letovsky & E. Soloway, “Delocalized Plans and Program Comprehension,” *IEEE Software*, 1986. DOI: https://doi.org/10.1109/ms.1986.233414 — abstract/metadata; full text `GAP`
5. S. Letovsky, “Cognitive processes in program comprehension,” *J. Systems and Software*, 1987. DOI: https://doi.org/10.1016/0164-1212(87)90032-x — not full-text this pass; content via (1)(2)
6. D. C. Littman, J. Pinto, S. Letovsky, E. Soloway, “Mental models and software maintenance,” in *Empirical Studies of Programmers*, 1986, pp. 80–98 — primary `GAP`; content via (2)
7. M.-A. Storey, “Theories, tools and research methods in program comprehension: past, present and future,” *Software Quality Journal*, 14:187–208, 2006. DOI: https://doi.org/10.1007/s11219-006-9216-4 — Springer abstract; full text `GAP` this pass; mirrors/slides used as E2 pointers only where they quote (2)/(1)

### Alexandria corpus=`software_engineering` (E2 / E0 retrieval)

8. Damien Irving, Kate Hertweck, Luke Johnston, et al., *Research Software Engineering with Python* — multiple chunks (see §3.6)
9. Christian Ciceri, Dave Farley, Neal Ford, et al., *Software Architecture Metrics* — cycle groups / understandability
10. Robert C. Martin, *Clean Architecture* — ADP, cycles, visualization of actual structure (chunks `c97d40655cde9d36e2f2450a`, `4e455075dd9766e48133bdee`)
11. Harry Percival & Bob Gregory, *Architecture Patterns with Python* — dependency graphs, layers, DIP
12. Addy Osmani, *Beyond Vibe Coding* — AI-era understanding / engineering vs vibe coding
13. Tom Taulli, *AI-Assisted Programming* — codebase-scale AI tools narrative
14. Robert C. Martin, *Clean Code* — Stepdown Rule (authoring, not PC empirics)
15. John F. Dooley & Vera A. Kazakova, *Software Development, Design, and Coding* — stepwise refinement top-down/bottom-up (design, not PC empirics)
16. Dino Esposito, *Clean Architecture with .NET* — modularity / monolith comprehension challenges

### Local

17. `d:\GreyMatter\docs\research\PROTOCOL.md` — [E0] observed 2026-07-27

### Searched but weak / absent in Alexandria for classical PC authors

18. Direct probes for “von Mayrhauser Storey Letovsky Brooks” → partial; top hits were unrelated practitioner books (Taulli, Dooley, Esposito) — classical theory must come from web/primary PDFs, not this corpus alone.
