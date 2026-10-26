---
id: feature-methodology-review-codex-pilot-revision
kind: feature
stage: implementing
tags: [methodology-review, research-pipeline, prose]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-26
---

# Methodology-review: revision from the Codex Knowledge pilot

## Brief

The Codex-driven repeat of the Knowledge methodology review (project-blueprint,
research-pipeline 0.6.0 / Agentic Research 0.10.0) closed **Stopped with retained
risks** after 24 dispatches and one root round, with modest incremental decision
yield. Its handoff names five candidate skill changes with behavioral acceptance
tests. This feature adjudicates them against current text, separates skill gaps
from host mistakes and ARD-owned source problems, delivers a small revision with
forward-scenario regression checks, and writes a bounded next-pilot plan in a
different domain. The goal is decision usefulness and proportional execution, not
family count, defect count or a Clean verdict.

Evidence (read-only, private checkout):
`~/dev/project-blueprint/data-knowledge-blueprint/.work/review-evidence/knowledge-methodology-review-2026-10-20-codex/`
— `skills-v2-handoff.md`, `pilot-lessons.md`, `pilot-log.md` (P01–P27),
`round1-lead-adjudication.md`, `round1-assessment-clarification.md`,
`predecessor-sample-crosswalk.md`.

Non-goals: restarting or editing the Knowledge review or its decisions, running
EX-1/EX-9, inspecting other Blueprint components, launching the next pilot,
publishing a plugin version, or copying ARD discipline into research-pipeline.

## Simplification opportunity

Prefer sharpening existing rules over new artifacts or gates. The sample
checkpoint's unconditional "absent from the map → refresh" remedy is replaced by a
decision-tied one, which removes an implied refresh/re-challenge loop rather than
adding a budget. No new mandatory report, schema field or verification layer.

## History

Created 2026-10-19 as `idea-blueprint-methodology-pilot`: Andrew's intended jobs
(domain-method review over time, suite and component review, scout pairing) and the
decision to pilot on project-blueprint's Knowledge component first. The first
pilot's findings were delivered by `feature-methodology-review-pilot-learnings`
(research-pipeline 0.6.0). The item stayed parked as the home for the Codex
repeat's findings; this feature files them.

## Adjudication (2026-10-26)

Each candidate was checked against the current 0.6.0 text (SKILL.md SHA-256
`652bdf6c…5b01`, unchanged since the pilot).

| # | Candidate (pilot evidence) | Class | Current text and gap | Decision |
|---|---|---|---|---|
| C1 | Breadth to bounded comparison (P06, P12, P15, P19, P21) | Skill gap, partial | Value coverage is the only named sample check, and "absent from the map → refresh" is unconditional. Each fresh challenge can find valid candidates, so the refresh/re-challenge cycle has no decision-tied exit. The operator-judgement and "repeat only on material change" rules already exist. | Adopt: value coverage becomes a floor, exclusions are checked for decision-relevant principles and combinations, and refresh applies to decision-bearing absences. Decision-remote ones become recorded coverage limits. Held-out absence still refreshes. No budget and no quiet-pass exit. |
| C2 | Map sources are not comparison evidence; old sample vs regenerated map (P26, P27, assessor §5) | Skill gap, wording | Step 3 says "reuse sufficient current research", but the packet lists only the map. Re-runs reuse the map with no mapping of the predecessor sample. ARD's relevance check caught P26 and stays the gate. | Adopt: one packet field for decision-relevant evidence beyond the map's sources. A re-run records a predecessor-sample crosswalk with covered, partial or prior-comparison-only status. |
| C3 | Exit for inherited explicit retention; first assessment as exit (P27) | Skill gap, contract ambiguity; cost one dispatch | The rank 1 label "on explicit operator stop" is narrower than its condition. The assessor brief says a step-4 assessment returns statuses only, which conflicts with step 6's "independent initial assessment can be the exit report". | Adopt: align the rank 1 label and condition, say that an inherited explicit retention on an unchanged basis needs no closure question, and let one full-scope assessment count once for both purposes. |
| C4 | Blind-input isolation and neutral dimensions (P04, P06, P08, P18, P20, P22, P23) | Skill gap, partial; the rest is host execution | The brief stages inputs but does not mention automatic context (working-tree status, memory, instructions) or frame values that encode families. | Adopt: define blindness as input isolation, add a frame-value leak check, and report a cued challenge as a bounded claim. Mechanism-neutral, with safety instructions preserved. P20 within-stage persistence: not adopted (it would cost another dispatch for a measurement nobody consumes). |
| C5 | Phase and next gate at checkpoints (P24) | Host communication; minimal clarification | The phases are defined, but nothing requires a checkpoint message to state the overall phase. | Adopt one sentence in Resume and report. |

Not adopted, with owners: P10 (contradictory host prompt), P02 (output overflow),
the wrong controller stage, the bibliography-parser assumption and P23 (cleanup
deletion) are host errors. P14 and the qualifier-stripping catch are ARD source
discipline, which already caught them. P03 registration duplication has no defect
conclusion. P16 (primer examples share Knowledge's domain): no evidence that
removing them helps; the different-domain pilot tests it. The effort forecast miss
(5 vs 18 front-end dispatches) stays information, not a cap. The next pilot
measures it again.

## Outline

Targets: `plugins/research-pipeline/skills/methodology-review/SKILL.md` and its
`references/{domain-map,assessor-briefs,commission-packet,controller-and-reruns}.md`.
Edit existing sentences in place, and keep detail in the references.

1. **SKILL.md, sample checkpoint (C1):** value coverage is a floor. Exclusions
   are checked for principles or combinations that a recorded decision turns on.
   The remedy for a family absent from the map is conditional on decision
   relevance. Held-out absence still triggers a refresh.
2. **domain-map.md (C1, C4):** the refresh trigger matches item 1. The frame
   check covers values that near-name families.
3. **commission-packet.md (C2):** an evidence-reuse field.
4. **controller-and-reruns.md (C2):** a predecessor-sample crosswalk in the re-run
   steps and record.
5. **SKILL.md exit table and step 6, assessor-briefs.md (C3):** the rank 1 wording,
   inherited retention, and the single-assessment rule.
6. **assessor-briefs.md, completeness challenge (C4):** input isolation and the
   cued-challenge limit.
7. **SKILL.md, Resume and report (C5):** a phase line at every checkpoint.
8. **Next-pilot plan:** a backlog idea, `idea-methodology-review-next-pilot`. It
   declares jobs, the decision, constraints, an effort forecast and deciding
   evidence. Launching the pilot and choosing the component need their own scope.

Acceptance:
- The forward scenarios below pass on both hosts. Fresh readers see only the
  changed files and the scenario packet, never the expected outcomes.
- skill-portability passes and `git diff --check` is clean.
- Relative links and anchors resolve.
- SKILL.md does not grow by more than about 15 lines.
- The Claude and Codex plugin manifests are unchanged, because no version bump
  is in scope.

## Forward scenarios (behavioral regression)

Expected outcomes are recorded here so later revisions can re-run the packet.
Readers get only the scenario text.

| ID | Planted case | Expected behavior |
|---|---|---|
| FS1 | A sample covers every value of every dimension but excludes a family whose principle (cross-owner joins) is what decision D2 turns on. The family is on the map. | Flag the exclusion despite full value coverage. Remedy: revise the sample, or record a principle-level reason for the operator. Do not require every grid cell. |
| FS2 | A fresh challenge finds three valid families absent from the map. One bears on an in-scope decision. Two bear on no recorded decision. A held-out family is present. | Refresh the map through scout for the decision-bearing family only, then re-challenge the affected decisions. Record the two remote families with their relevance as explicit coverage limits for the operator's coverage decision. No blanket expansion and no waiting for a quiet pass. |
| FS3 | A regenerated map cites 48 sources. Older verified research in the project holds measured and disconfirming results for decision D1, and none of it is in the map. | The commission packet names that older evidence for the comparison before source review. The map is not the evidence corpus. No methodology-review source gate is added. |
| FS4 | Re-run: the predecessor sampled "full wiki configuration". The new map has only neighboring families. The old research is inside its TTL. | The crosswalk records prior-comparison-only or partial coverage at its dated depth. It claims no equivalence, does not treat the TTL as making product claims current, and commissions no automatic new landscape. |
| FS5 | Re-run: KMR-01 is a major finding that the operator explicitly retained in the predecessor. No trigger fired and the basis is unchanged. The first fresh full-scope assessment finds no new major finding and no new choice. | Exit: Stopped with retained risks from that one assessment. No closure question and no second assessment. Variant: a named revisit trigger fired, so reopen that decision (Awaiting decision). |
| FS6 | Before the stage-1 challenge, the working tree's status lists files named after map families, and the frame's values near-name the families. | Coarsen the frame values and remove or isolate the exposed names before dispatch. Otherwise report the challenge as cued, with that limit. Required safety and project instructions stay. No particular tool is required. |
| FS7 | The map is source-approved and the challenge is done. The host messages the operator. | The message says the review is at its sample checkpoint, that comparison and whole-scope assessment remain, and that a response is needed. It does not present the review as finished. |
