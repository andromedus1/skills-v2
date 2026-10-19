---
id: feature-claude-methodology-repeat
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline, agentic-research]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
---

# Claude-driven methodology review repeat (QVC)

## Brief

This item is the root loop controller for review `QVC`: a Claude-driven repeat of
the completed Codex-driven `QVE` methodology review on the same three topics. It
owns the charter, component returns, operator decisions and dated assessments.
Separately commissioned research owns its own engagements; their completion
cannot close this controller.

Invocation authorizes investigation and review artifacts only. Changes to project
methods, skills, contracts or policy require Andrew's adjudication of a decision
packet; publication, package merge, corpus migration and automatic adoption of
findings remain out of scope.

## Strategic decisions

- **Settings**: mixed scope authority, standard research verification, whole-review
  decomposition with adaptive research inside each part, five root rounds — carried
  forward from QVE as established by the capture below.
- **Independence from QVE findings**: Claude forms component findings from the
  current baseline, its skills and the grounding research before reading QVE's
  component returns, assessments and adjudications; comparison with QVE follows as
  a separate step. Agreement is not a target. QVE's charter and topics are inputs.
- **Fresh assessor**: Codex through `peeragent:peer`, per the project's cross-model
  preference when Claude drives; fall back to a fresh-context Claude assessor and
  record the limitation if Codex is unavailable.

## Simplification opportunity

None proposed at scope time. The review itself may identify checks, prose or
duplicate review paths that QVE added and that do not earn their cost.

## Original capture (historical context)

Andrew requested a Claude-driven session to repeat the methodology-review exercise
on the same topics as the completed Codex-driven run. Capture this for next session;
do not start the exercise during the current wrap-up. Claude should drive the work,
with the existing project preference for Codex when independent cross-model review
is called for.

The same topics are:

- Quality criteria, evidence and bounded correction loops across Research Pipeline,
  Agentic Research and methodology-review, including lessons from doc-review.
- Independent review of consequential prompt/skill changes, review weights, and
  reuse of a completed review plus verified corrections.
- Citation-warning signal and noise, including version-number advisories.

Retain the broader package-boundary context: Research Pipeline owns project process;
Agentic Research owns grounded research. The established settings were mixed scope,
standard research verification, and whole-review decomposition with adaptive
research inside each part. Compare Claude's findings with the earlier run without
treating agreement as the required outcome. Follow the current local skill and
project process when scoping the repeat; prior implementation is evidence to assess.

## Recover the prior work

- Start with `plugins/research-pipeline/skills/methodology-review/SKILL.md` and its
  two references. Verify the session is using this checkout's current instructions;
  the previous arc did not publish or refresh installed plugin caches.
- Grounding: `.research/analysis/briefs/quality-feedback-loops.md` and its source
  records. Its paper coverage is abstract/metadata limited, not a universal
  effectiveness or model-comparison result.
- Completed controller: `.work/archive/feature-quality-verification.md`.
  Recover the full body with
  `git show 0b1c2978:.work/active/features/feature-quality-verification.md`.
- Research verification: `.work/archive/story-research-quality-feedback.md`;
  full body at
  `git show 0b1c2978:.work/active/stories/story-research-quality-feedback.md`.
- Prior product baseline: `6419b3bc`; final assessment at `a2f03eaa`; archived at
  `d32f12fe`. QVE closed clean within reviewed scope after 3 of 5 root rounds.
  Preserve that completed history and its counts. Establish the current baseline
  at next-session kickoff rather than assuming these revisions remain current.
- Evidence: 13 synthetic forward scenarios per host, 57/57 ARD conformance checks,
  one standard independent feature review plus verified fixes, and fresh methodology
  assessments. The full work record preserves coverage limits and actual outcomes;
  temporary test artifacts may not survive to the next session. No live release
  was exercised.

Related parked observations are `idea-release-checkpoint-handoff` and
`idea-citation-advisory-coverage`. They are inputs to consider, not preselected fixes.
The unrelated Pi backlog remains separate. This capture does not authorize a
publication, package merge, corpus migration, or automatic adoption of new findings.
