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

## Methodology review QVC — charter and checkpoint 1

Baseline: `e3e2e070` (product content identical to `a36137fa`). Root round: 1
allocated; 0 complete; shared limit: 5. Instruction source verified: skills load
from this working tree (the local-directory marketplace resolves
`agile-workflow:scope` to `plugins/agile-workflow/skills/scope`), and the review
protocol was read from `plugins/research-pipeline/skills/methodology-review/`.

**Users and jobs.** Operators and agents who conduct grounded research, change
skills/prompt-ware, and claim that research, delivery or a release checkpoint is
complete. **Outcome.** Completion claims are backed by required, current evidence;
feedback is actionable; correction cost is bounded; the operator spends attention
where risk warrants it.

**Fixed constraints.** Agile Workflow + Research Pipeline remain the process;
Agentic Research owns grounded research and its verification stack; Andrew
adjudicates project-method changes; no CI exists, PRs merge manually; both Claude
and Codex plugin shapes must keep working. **Hypotheses under review** (inherited
design choices, not constraints): the QVE-era rules that missing/stale evidence
is not a pass; review weights with one standard independent pass; reuse of a
covering review plus verified fixes; quality-checkpoint reconciliation of owner
records; root-round limits; citation-advisory classification; and the amount of
prose these rules occupy.

**Topics (children).** Coordinated review — three children feed one combined
decision packet at the root. Considered cuts: unsplit (would bury the citation
signal question, which has its own local mechanics); by plugin (would repeat the
shared "what counts as evidence" question three times); by topic (chosen). A
program shape was not chosen because Andrew adjudicates all three in one batch
and no child has an independent change schedule. The root owns the shared
question "what evidence establishes completion" and the cross-child scenarios.

| Child | Scope and contribution | Evidence plan |
| --- | --- | --- |
| QVC-E | Quality criteria, evidence and bounded correction loops across Research Pipeline, Agentic Research and methodology-review, including lessons from doc-review | Local contract map + `quality-feedback-loops` brief + supplementary research |
| QVC-R | Independent review of consequential prompt/skill changes, review weights, and reuse of a completed review plus verified corrections | Local routing map + supplementary research on evaluator independence |
| QVC-S | Citation-warning signal and noise, including version-number advisories | Reproduce current lint/gate behavior on this corpus + supplementary research on warning noise |

**Criteria.** Detection of material defects; independence and scope of
verification; authority; interruption/resume recovery; operator and agent cost;
false-positive burden; portability across hosts; maintenance and prose burden;
whether the rule is enforced by anything other than reader compliance.

**Scenarios.** (1) Success path: research converges, delivery reviewed, checkpoint
ready. (2) A required check fails or is missing. (3) Output changes after review.
(4) Correction limit exhausted with blockers. (5) Interrupted review resumed in a
new session or other host. (6) A small prompt edit vs. a consequential contract
change. (7) A citation lint run with real and spurious warnings.

**Comparison sample (provisional).** Evaluator-optimizer and agent-eval guidance;
same-model refinement vs. intrinsic-correction limits (existing brief); LLM-judge
self-preference and cross-model judging evidence; human code-review practice
(single reviewer, re-review on change); static-analysis warning practice
(false-positive tolerance, alert fatigue); and a simpler baseline: an ordinary
PR checklist with one reviewer and no reconciliation layer.

**Research settings.** Reuse `quality-feedback-loops` (abstract-limited). One
supplementary engagement, commissioned through a separate `[research]` story with
mixed scope authority and standard verification, covers the named gaps the
existing brief disclaims: cross-model vs. same-model review evidence, and
warning-noise tolerance. Doc-review lessons and QVC-S mechanics are local.

**Required checks and owners.**

| Check | Owner | Evidence that establishes it | Result |
| --- | --- | --- | --- |
| Supplementary research converged at standard rigor | agentic-research orchestrator | Engagement record with gate results | pending |
| Child assessments returned | QVC children | Dated reports below | pending |
| Fresh whole-scope assessment | Codex via peeragent (fallback: fresh Claude) | Dated report in this record | pending |
| QVE comparison | root | Section comparing QVC vs QVE after independent findings | pending |
| Delivery checks for any authorized change | agile-workflow review | Item review record | not authorized |

Exit: none yet. Next: commission research; dispatch children blinded to QVE's
returns and assessments.
