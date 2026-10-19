---
id: feature-calibration-cuts
kind: feature
stage: implementing
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

## Design decisions
All directional choices are Andrew's (Brief). C4 runs now rather than after the
blueprint pilot (Andrew chose "C4 compress now").

## Implementation Units
1. **C1 + C2** — `.work/CONVENTIONS.md` `### Review receipts` (drop `Weight` line;
   post-review block = exceptions or one "none" line; no closure anchor; keep the
   exact enumeration command) and `quality-checkpoint/SKILL.md` §2 (classify only
   exceptions; the receipt's fix commits and other tracked items' own commits need
   no line).
2. **C3** — `gate-citations/SKILL.md`: add `--no-pattern-check` to the gate
   command; remove pattern-advisory handling/reporting that no longer applies;
   keep warn-only counts and the exit-code/JSON rules. Check quality-checkpoint
   and build-process for advisory wording that would now be false.
3. **C4** — methodology-review SKILL + `references/review-record.md` +
   `references/review-decomposition.md`: (a) inventory every operative rule in the
   current text as a numbered list; (b) rewrite to ≤ ~3,700 words total, merging
   restatements and moving outcome-precedence prose into the exit table; keep
   frontmatter, section structure and any anchors linked from elsewhere; (c) map
   each inventoried rule to its new location. A separate fresh-context agent then
   checks the mapping against both texts before review.
**Acceptance**: [ ] receipt template/rules match C1–C2 and the enumeration command
still runs verbatim; [ ] gate command includes `--no-pattern-check` and the gate
text has no orphaned advisory handling; [ ] methodology-review word count ≤ ~3,700
with a complete rule mapping verified independently; [ ] RP portability passes.
