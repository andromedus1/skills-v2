---
id: feature-qvc-review-receipts
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline, review]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Review receipts that make covering-review reuse checkable

## Brief

Operative remedy for QVC-R/METH-002 (alias QVC-E/METH-005), accepted by Andrew
on 2026-10-19 — see `feature-claude-methodology-repeat`, "Operator decisions —
round 1 packet". Research origin:
`.research/analysis/campaigns/qvc-review-evidence/parent.md` (covering-review
reuse is a policy choice; recording what a review covered makes reuse
checkable).

Fork-only change to `.work/CONVENTIONS.md` and `research-pipeline`
`quality-checkpoint` §2: a review receipt records the reviewed `base..head`,
reviewer class and path, weight, findings, accepted-fix verification, and a
one-line coverage classification for each post-review change to a consequential
file (covered by the pass / covered by verification of a named finding /
uncovered → normal delivery). "Stale" means a post-review change with no
classification.

Out of scope: any added review pass; mandatory re-review; changes to upstream
agile-workflow templates.

## Simplification opportunity

Replace the current author-judged "materially uncovered" prose with the receipt
field where possible, rather than adding a parallel rule.
