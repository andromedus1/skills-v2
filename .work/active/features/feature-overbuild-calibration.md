---
id: feature-overbuild-calibration
kind: feature
stage: review
tags: [research-pipeline, process]
parent: null
depends_on: [feature-upstream-sync-2026-10]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Overbuild calibration and machinery forecast

## Brief

Adapt upstream's anti-overbuilding posture: a short proportionality/overbuilding calibration section in .work/CONVENTIONS.md read by design and review; a 'machinery forecast' step (simplest working chain vs proposed, skepticism toward receipts/validators that mainly police agent bookkeeping) in research-pipeline feature-design and epic-design; re-examine this fork's recent receipts and checks against it and propose cuts; add the delegation safety rule (delegated jobs never delete what they did not create). Depends on the sync because both edit RP feature/epic-design. Decided by Andrew 2026-10-19 — see `feature-upstream-learnings-2026-10`,
"Operator decisions"; research: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.

## Simplification opportunity

Expected to remove or shrink ceremony rather than add it; the receipts review may trim the receipt convention.

## Design decisions
- **Calibration text (Andrew, 2026-10-19): use the drafted section as written**
  (context; likely overbuilding; justified complexity; revisit triggers).
- **Cuts (Andrew): propose only.** Applying the calibration to recent receipts
  and checks yields a proposal list for Andrew; nothing is removed here.
- Machinery forecast is conversational, not a gate or artifact (Workbench
  `assurance-machinery.md` "Forecast consequential machinery"); trigger only when
  a proposal adds a state owner, ledger/receipt/status record, validator, retry or
  correction loop, or crosses hosts/plugins.
- Delegation safety rule lives in `.work/CONVENTIONS.md` (peer skill is
  upstream-owned peeragent).

## Implementation Units
1. `.work/CONVENTIONS.md`: add `## Overbuilding calibration` (confirmed text) and a
   one-line delegation rule ("Delegated agents never delete, revert or overwrite
   files they did not create in that job; they report instead").
2. `plugins/research-pipeline/skills/feature-design/SKILL.md` Phase 5a and
   `epic-design/SKILL.md` decomposition step: read the project's
   `## Overbuilding calibration` when present; raise a machinery forecast when the
   trigger applies — one user action and failure prevented, new state and why the
   existing owner cannot handle it, simplest working chain vs proposed, what each
   added link buys, recommendation and question. ≤ 10 lines each; no new section
   template, gate or artifact.
3. Cuts proposal (in this item): apply the calibration to the receipt convention,
   quality-checkpoint §2, doc-review, gate-citations and methodology-review; list
   concrete trims with the guarantee each preserves.
**Acceptance**: [ ] calibration text matches the confirmed draft; [ ] forecast
text in both skills stays ≤ 10 lines and names no new artifact/gate; [ ] RP
portability passes; [ ] cuts list present with per-item guarantee; nothing removed.

## Risks
- Calibration ignored like other prose — mitigated by placing it where design and
  review already read (CONVENTIONS) and by the forecast hook in design skills.

## Proposed cuts (for Andrew; nothing removed)

Calibration applied to this fork's recent receipts and checks (evidence refreshed
2026-10-19 after review). Each row names the guarantee that must survive.

| # | Target | Evidence | Proposed trim | Guarantee preserved |
| --- | --- | --- | --- | --- |
| C1 | Review receipt `**Post-review changes**` block (`.work/CONVENTIONS.md` receipts; quality-checkpoint §2) | Four receipted reviews: every enumerated commit was the review's own fix commit; round 2's only receipt finding was two unfilled `<closure>` placeholders — bookkeeping about bookkeeping | Keep `Reviewed`, `Reviewer`/independence and `Accepted-fix verification`. Require the post-review block only when a consequential commit after the reviewed head is *not* a listed fix commit; drop the closure-range anchor (git computes it) | Unreviewed consequential changes stay visible; reuse stays checkable |
| C2 | Receipt `Weight` line | The review skill already requires the review record to state the effective weight, pass count and closure reason | Drop only the receipt `Weight` line; keep `Findings` counts (the upstream record lists findings but not counts) | Weight stays in the review record; counts stay in the receipt |
| C3 | gate-citations pattern-advisory reporting (QVC-S/METH-004, retained) | Release gate prescribes no action for advisories; engagements already lint and spot-check patterns; releases are rare here | Run the gate with `--no-pattern-check`, keeping integrity and warn-only counts | Broken-chain integrity and warn-only visibility unchanged; pattern review stays inside engagements |
| C4 | methodology-review instruction volume: SKILL 2,641 words + references 2,661 = 5,302 (QVC-E/METH-002 consolidation removed only duplicated completion rules) | The calibration names instruction volume as this repo's main cost; QVC showed the protocol works but is long | One compression pass targeting −30% across SKILL + references: merge restated authority/stop rules, move outcome-precedence prose into the table | Same steps, authority boundary, round limit and exit table |
| C5 | doc-review 5-iteration loop with a full dispatched re-audit each iteration | Only a read-only fresh-context dry run exists (feature-qvc-minor-remedies review, `64bf8ae2`); no correction loop has run, so its cost is unmeasured | No trim now — needs evidence. Revisit after its first real correction run | — |

Not proposed: research rigor dials (today's floor-rigor scout was proportionate),
conformance/parity tests (justified complexity), operator authority rules.

## Implementation notes
- Execution capability: host inline (three small prose edits plus analysis).
- Review weight: standard (default).
- Files: `.work/CONVENTIONS.md` (calibration section + delegation rule);
  RP `feature-design/SKILL.md` (machinery forecast after Phase 5a, 1 paragraph);
  RP `epic-design/SKILL.md` (forecast in Phase 5 pre-mortem, 6 lines).
- Verification: RP portability ok; calibration text equals the confirmed draft
  (rewrapped only); forecast adds no artifact, template or gate.
- Discrepancies: none.
