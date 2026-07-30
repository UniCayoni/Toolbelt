---
name: creative-systems-design
description: >-
  Design game and creative *systems* (mechanics, dynamics, aesthetics, loops,
  tuning) with plural methods (MDA-class and kin). Use when designing gameplay
  systems, economies, feedback loops, playtest/tune cycles, or systems GDD
  slices — not story, not world bible, not product UX.
---

# Creative systems design

Announce once: **Using `creative-systems-design`**.

Authority: Theme 5 accepted (T5D systems). **Methods are plural — no single SoT.**  
Run **`design-process`** spine first for non-trivial systems.

## When to use

- Gameplay systems, loops, economies, combat/progression rules as *systems*
- MDA-class lenses or equivalent (mechanics / dynamics / player experience goals)

**Out:** Narrative/quests → `creative-narrative-design`. World/characters → `creative-world-character-design`. Code architecture → `technical-design` (**do not** apply MDA as Clean Architecture). Engines/stack locks. Product UX (T5C).

## Method (plural)

Prefer an explicit loop; pick vocabulary the project agrees on:

1. **Experience / aesthetic goals** (what players should feel/do)
2. **Dynamics / loops** (runtime behavior from player + rules)
3. **Mechanics** (concrete rules, numbers, verbs)
4. **Prototype → playtest / critique → tune** (Rule of the Loop–style iteration)

MDA (Mechanics–Dynamics–Aesthetics) is one E1 lens among others (Schell tetrad, Sellers loops, Zubek mechanics/gameplay/experience). **Do not force one brand** if the team uses another coherent systems frame.

## Agent role

- Propose 2–3 system approaches with tradeoffs (`design-process`)
- Critique for broken loops, dominant strategies, unfun dynamics
- Human decides; record significant system locks (project doc or ADR if it binds tech)

## References

- Read `references/creative-systems-checklist.md` **when** running a full systems pass
- Theme 5 report (accepted)
