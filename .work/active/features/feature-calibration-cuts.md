---
id: feature-calibration-cuts
kind: feature
stage: done
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

## Implementation notes
- Execution capability: host inline for C1–C3; one worker for C4 plus a separate
  fresh-context preservation checker. Review weight: standard (default).
- C1/C2 (`.work/CONVENTIONS.md`, quality-checkpoint §2): receipt drops `Weight`;
  post-review block lists only exceptions (commits neither the receipt's listed
  fixes nor another tracked item's own commit) or one "none outside listed fixes
  and tracked items" line; closure anchor dropped (enumerate `<head>..HEAD` at
  closure); commit messages name their item. Enumeration command verified.
- C3 (`gate-citations/SKILL.md`, quality-checkpoint §3 wording): gate runs
  `--no-pattern-check`; pattern-advisory handling/reporting removed; warn-only
  counts and exit-code/JSON rules kept. Verified: exit 0, valid JSON, 0 broken,
  0 pattern flags on this repo.
- C4 (methodology-review SKILL + 2 references): 5,302 → 4,192 words (−21%).
  **Discrepancy:** target ~3,700 (−30%) not met; further cuts would have removed
  operative rules (worker stopped; preservation beats brevity). Worker inventory
  296 rules (271 direct, 25 merged, 0 dropped). Independent checker inventory 315
  rules: 310 preserved, 5 weakened, 0 missing; two material (child review items
  lost the no-research-tag rule; review-record intro routed comparison rows to the
  loop record) and three minor ("only when", "as applicable to the domain",
  "before dispatch") plus one wording issue — all restored. Headings, section
  order, frontmatter and inbound links unchanged; 29 relative links resolve.
  Scratch evidence (`/private/tmp/claude-501/c4/`) not retained, per Andrew's
  earlier call on experiment artifacts.
- Verification: RP portability ok; `git diff --check` clean.

## Review (2026-10-19)

**Verdict**: Approve with comments

**Blockers**: none.
**Important**: C4 target (~30%) unmet at 21% — receiver adjudication: **accepted
deviation**. The target was approximate; further cuts would remove operative rules;
two independent checks (fresh-context checker, 315-rule inventory; reviewer's
38-rule sample) found no lost or weakened rule after fixes. Surfaced to Andrew on
the PR; a further pass is a new decision.
**Nits**: none. **Rejected**: none.

**Notes**: standard weight, one independent pass. Reviewer verified receipt
exceptions stay traceable (other-item commits must name their item), uncovered
changes still named and routed, enumeration runs with `<head>..HEAD`; gate exit 0
with 0 broken/0 thin and identical non-pattern results (204 advisories
suppressed); methodology exit precedence and headings intact, 29 links resolve;
portability ok.

**Receipt**
- Reviewed: `31c2f65e..99f7f08c` — `.work/CONVENTIONS.md`, quality-checkpoint, gate-citations, methodology-review SKILL + 2 references
- Reviewer: Codex `gpt-6.1-sol` medium via peeragent job `20261019T203804Z-1365de42`; independent: yes (cross-model; host Claude)
- Findings: blockers 0, important 1, nits 0, rejected 0
- Accepted-fix verification: none required (deviation adjudicated)

**Post-review changes**: none outside listed fixes and tracked items
