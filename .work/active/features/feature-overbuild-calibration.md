---
id: feature-overbuild-calibration
kind: feature
stage: implementing
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
