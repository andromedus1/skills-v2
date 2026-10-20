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

- `landscape-mapping`: handshake echo matches; lint 137 resolved, with 2 low
  `unreachable-source` URL-liveness warnings on one handle that WebFetch did
  read. It reused the design-space specialist's GMA attestations and deleted
  its own duplicate.

**Emergent facet 7, `analogous-domain-search`.** This covers distant and
analogous-domain search, design-by-analogy and fixation. `landscape-mapping`
flagged it as covered only lightly, and it is the measured basis for one of the
lateral moves (an alternative found in an unrelated field). Dispatched with
bibliography block 400–449.
- `taxonomy-construction`: handshake echo matches; lint 119 resolved, 0 broken;
  15 attestations authored and 3 reused. Its suggested facet (reconciling
  independent classifications) falls within `coverage-estimation`'s
  inter-rater scope, so there is no new dispatch.
  **Privacy incident:** the specialist sent one Unpaywall API request carrying the
  operator's email address as the `email` parameter. That should have been a
  placeholder. It was reported to the operator, and the dispatch instructions now
  forbid personal data in external requests.
- `design-space-methods`: handshake echo matches; lint 118 resolved, with 13
  low `unreachable-source` URL-liveness warnings that change between runs; 0
  high. It reused two LLM-ideation attestations under its own numbers
  (duplicate `references.md` entries for the same handle are expected and left
  as they are).

**Emergent facet 8, `decision-option-generation`.** This covers value-focused
thinking, act and objective generation, and option-generation prompts.
`design-space-methods` reported it as the strongest measured evidence on
incompleteness, and its central source was held only at press-release depth.
Dispatched with bibliography block 450–499. The remaining suggestions
(ideation-metric validity, inter-rater reliability of dimension choice) fall
within `coverage-estimation`.

**Program-scale threshold (8 facets across 3+ domains).** The orchestrator
escalates at 7+ facets so that one cross-join does not over-widen. All eight
facets serve one question and one consumer, so splitting them into separately
registered campaigns would duplicate the seed and decision relevance. Instead
the synthesis is nested:

- **Cluster syntheses:**
  - `clusters/generation.md`: design-space, analogous-domain,
    decision-option and LLM ideation;
  - `clusters/completeness.md`: search completeness, coverage estimation,
    taxonomy and landscape mapping.
- **Composition:** each cluster is composed from its own specialist briefs,
  then `parent.md` from the two clusters.
- **Gates:**
  - lint runs on every cluster and on the parent;
  - `adversarial-read` covers both clusters and the parent;
  - `evaluate` receives both clusters plus the parent as its synthesis output.

This keeps each cross-join at four facets while every cross-specialist
synthesis still passes the reachability-required gates.
- `coverage-estimation`: handshake echo matches; lint 171 resolved, 0 broken; 19
  attestations authored and 8 reused; no personal data sent. Its two suggested
  facets (a deduplication protocol for kinds; techniques that make absence
  visible) are already partly evidenced across the returned briefs. They go
  into the parent as open questions and `Revisit if` triggers, not a ninth
  dispatch, since the fan-out is already past the program-scale threshold.
- `analogous-domain-search`: handshake echo matches; lint 108 resolved, with 8
  low URL-liveness warnings and 0 high; 21 attestations authored, 4 reused; no
  personal data sent. Its suggested facet (problem framing and reformulation) is
  carried as an open question in the parent, not a new dispatch.
- `decision-option-generation`: handshake echo matches; lint 109 resolved, 0
  broken; 15 attestations authored and 2 reused. Its suggested facets (part-list
  cueing; under-weighting of a residual "other" bucket) are already evidenced in
  its own brief, so there is no new dispatch.

**Checkpoint B (surface-and-proceed) and composition (2026-10-20).**

- **Cross-cluster contradictions** are recorded in each cluster and in the
  parent. The main ones:
  - diversity-seeking sampling versus estimator assumptions;
  - perspective-based review (minimise overlap) versus capture–recapture (needs
    overlap);
  - mixed effects of domain distance;
  - categories helping only as a second pass.
- **Clusters and parent:** `clusters/completeness.md`, `clusters/generation.md`
  and `parent.md`. All lint at 0 broken.
- **Lead corrections:**
  - 24 attestations carried nonstandard `substrate_confidence` values, which the
    lint was reading as source-direct. They were normalized to `search-summary`
    or `snippet`; the lint gap is parked as
    `idea-lint-substrate-confidence-enum`.
  - Malformed `{N]` braces were found in lead drafts and fixed.
- **Bibliography:** 181 entries merged into `references.md` in block order, with
  no duplicate numbers and 0 handle↔number mismatches across the campaign. Gaps
  inside blocks are left as gaps.
- **Acquisitions:** `acquisitions.md` written with 2 blocking entries (the
  Siebert & Keeney 2015 full text; Gettys 1987) and enriching entries. Promotion
  to `.work/` is proposed to the operator, not written.
