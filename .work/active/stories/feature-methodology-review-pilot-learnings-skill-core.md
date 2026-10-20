---
id: feature-methodology-review-pilot-learnings-skill-core
kind: story
stage: done
tags: [methodology-review, research-pipeline]
parent: feature-methodology-review-pilot-learnings
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-20
updated: 2026-10-20
---

# Methodology-review core revision

## Brief
Covers step 0 domain map, the charter changes, Checkpoint M, the commission packet, assessment ordering, the step 5 and 6 changes, re-run semantics, the record and decomposition changes, and scout's domain-map mode. Leaves seams for the primer attachment (S5).

## Implementation
See the parent feature's Implementation Units, Unit 3.

## Implementation notes (2026-10-20)

Traceability. Paths are relative to `skills/methodology-review/`.

| Finding | Where |
|---|---|
| F11, F31 (domain map) | SKILL.md §0; `references/domain-map.md` (halves, building, reuse, programs); `review-decomposition.md` (shared root map) |
| F14 | SKILL.md §2: discovery is a decision dimension |
| F1, F2, F28, F12 | SKILL.md §1: (operator) field marks; the overlapping-review rule; evidence-feasibility triage; expected effort as information |
| F11, F12 (checkpoint) | SKILL.md "Sample checkpoint"; `assessor-briefs.md#completeness-challenge` |
| F7, F9, F10, F13, F18, F23 | SKILL.md §3; `references/commission-packet.md` (template, default dials, non-recommending decision-relevance section, scope changes); `review-record.md` (comparison rows are research-only, plus "Transfer and proposals") |
| F19, F20, F22, F30 | SKILL.md §4: pre-check, then assessment, then packet; `assessor-briefs.md#assessment` |
| F25, F26 | SKILL.md §5 |
| Decision 3, F12 | SKILL.md §6: coverage against the map is report-only; actual versus expected effort |
| F29 | SKILL.md "Re-run and longitudinal review"; `controller-and-reruns.md#re-run-record` |
| F4, F5, F6 | Scope and authority (`methodology-review-controller`, direct minting); `controller-and-reruns.md#agile-workflow-controller` (skeleton) |

Other changes:
- Scout gained a "Domain-map mode" (`landscape-brief` plus `vocab-capture`).
- The research-composition profile row and paragraph were updated.
- The SKILL.md description was updated. `agents/openai.yaml` is unchanged, and
  its short description still fits.

**Seam left for S5.** Links to `docs/surfacing-alternatives.md` from
`domain-map.md` and `assessor-briefs.md`. The primer lines in SKILL.md are also
added in S5.

**Verification.** skill-portability passes. The link and anchor check is clean,
except for the two expected primer seams.
