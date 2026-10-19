---
id: feature-calibration-cuts
kind: feature
stage: drafting
tags: [research-pipeline, methodology-review, process]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Apply overbuilding-calibration cuts C1–C4

## Brief

Andrew (2026-10-19) approved cuts C1, C2, C3 and C4 proposed in
`feature-overbuild-calibration` (archived; body at its `git_ref`), after applying
the new `## Overbuilding calibration` to this fork's recent additions. C5 (leave
doc-review's loop) needs no change.

- **C1** — receipt `**Post-review changes**` block lists only exceptions: commits
  after the reviewed head that are neither the receipt's listed fix commits nor
  another tracked item's own commit; otherwise one line "none outside listed fixes
  and tracked items"; drop the closure anchor. Guarantee: an unreviewed
  consequential change after the reviewed head is still named and routed.
- **C2** — drop the receipt `Weight` line (the review block records the weight).
- **C3** — release citation gate runs with `--no-pattern-check`. Guarantee:
  integrity, thin and warn-only results unchanged.
- **C4** — compress `research-pipeline:methodology-review` (SKILL + two references,
  5,302 words) by about 30%. Guarantee: same steps, authority boundary, round
  limit, exit table and every operative rule — verified by a rule-by-rule mapping.

## Simplification opportunity

This item is the simplification.
