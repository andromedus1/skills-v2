---
id: idea-claude-methodology-repeat
created: 2026-10-18
updated: 2026-10-18
tags: [methodology-review, research-pipeline, agentic-research]
---

# Next session: Claude-driven methodology review

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
