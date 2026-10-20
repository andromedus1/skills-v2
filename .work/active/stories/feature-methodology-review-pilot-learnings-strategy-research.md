---
id: feature-methodology-review-pilot-learnings-strategy-research
kind: story
stage: implementing
tags: [methodology-review, research-pipeline, research]
parent: feature-methodology-review-pilot-learnings
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
research_dials:
  scope_authority: mixed
  verification_rigor: full
  intent: calibrate-external
  output_kind: [synthesis-brief, adoption-recommendations]
---

# Research: strategies for decomposing a solution space

## Brief
This story commissions the Agentic Research engagement behind the new surfacing-alternatives primer (design decision 4).

**Question.** What systematic strategies decompose a solution space into genuinely different approaches? How can a sample of approaches be checked for completeness before depth research is commissioned, including stopping rules and coverage estimates?

**Declared facets.** Scope authority is `mixed`, so more facets may emerge.
1. Design-space and morphological methods: general morphological analysis, TRIZ, design-rationale QOC, set-based design.
2. Systematic-review search strategy and completeness: search saturation, capture–recapture, citation chasing, PRISMA-S.
3. Taxonomy and faceted-classification construction methods.
4. Technology and landscape mapping practice: patent landscaping, technology scouting, scenario methods.
5. LLM and agent ideation diversity and coverage failures: homogenization, diversity techniques.

**Decision relevance (yield hypothesis).** The findings decide which moves the primer prescribes at each methodology-review step (domain map, charter sample, completeness challenge, facet briefs), and which completeness signal the challenge reports.

**Settings.** Andrew set thorough, over efficiency (2026-10-20), hence `full` rigor. The proposed output is a campaign at `.research/analysis/campaigns/solution-space-decomposition/`.

## Implementation
See the parent feature's Implementation Units, Unit 1.

## Engagement record

### Registration (2026-10-20, autopilot; dials user-confirmed at scope)

| Field | Value |
|---|---|
| `scope_authority` | `mixed` (story dial) |
| `verification_rigor` | `full` (story dial). Multi-path, so `adversarial-read` and `evaluate` are also reachability-required |
| `intent` | `calibrate-external` |
| `output_kind` | `[synthesis-brief, adoption-recommendations]` |
| `decision_relevance` | Which moves the surfacing-alternatives primer prescribes at each methodology-review step (domain map, charter sample, completeness challenge, facet briefs), and which completeness signal the challenge reports |
| `consumer` | The research-pipeline surfacing-alternatives primer and the methodology-review revision (story `-primer`) |
| `temporal_contract` | `write-once-on-converge` |
| `primitives_extends` / `primitives_opts_out` | none / none |
| `analytical_artifact_type` | `per-campaign-brief` |

**Substrate check.** `.research/` has no overlapping work. The pipeline primers
(`first-principles.md`, `oblique-strategies.md`,
`brief-first-principles-frameworks.md`) are lenses only, never citation targets.

### Decomposition (Checkpoint A, surface-and-proceed)

Three candidates were considered:

- **A. The five declared facets, one per source community (chosen).** The
  facets are design-space methods, systematic-review completeness, taxonomy
  construction, landscape and technology mapping, and LLM ideation diversity.
  Each specialist works one coherent literature.
- **B. Three facets: generation, completeness, LLM failure.** This folds
  landscape mapping and taxonomy into generation. It is cheaper, but it buries
  the practitioner landscape-mapping literature, which is the closest analog to
  a domain map.
- **C. Facets cut by methodology-review step** (map, sample, completeness,
  facet brief). Rejected. It imports project framing into research facets,
  which the substrate test warns against, and every facet would need every
  literature.

**Self-flag.** Facet 5 relies on fast-moving preprints, so weigh evidence levels
carefully. Facet 4 leans on grey literature (practitioner guidelines), so record
the source class. Specialists may surface emergent facets as acquisition or
`Revisit if` notes. They do not widen scope.

**Fan-out.** Five specialists:

- **Model:** `opus`, since thoroughness was preferred.
- **Bibliography blocks:** 100–149, 150–199, 200–249, 250–299 and 300–349.
- **Discipline propagation:** read handshake (sha256 `6408290171aa…ebbae`).
- **Planned gates:**
  - `adversarial-read` by Codex, so a different model family checks the work
    (SPEC §7, model diversity);
  - `evaluate` by an isolated `opus` evaluator, with the bundle inlined;
  - lint and spot-check by the lead.

### In-flight re-scope (2026-10-20, `mixed` authority)

**Emergent facet 6, `coverage-estimation`.** This covers species-richness and
sample-coverage estimators for samples of kinds, plus whether reviewers detect
omissions and how reliably they agree on category boundaries. The
`llm-ideation-diversity` and `search-completeness` specialists both flagged it
independently on return. It bears directly on the completeness signal named in
`decision_relevance`. Dispatched to one more `opus` specialist with bibliography
block 350–399; the handle reuse list was passed to avoid collisions.

**Returns so far.**
- `llm-ideation-diversity`: handshake echo matches; lint 160 resolved, 0 broken.
- `search-completeness`: handshake echo matches; lint 118 resolved, 0 broken.
