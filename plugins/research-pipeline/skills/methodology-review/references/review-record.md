# Comparison and review record

These fields are a writing aid, not a new frontmatter schema, database or research
tier. Decision, delivery and assessment fields belong in the loop record chosen under
the skill's [Scope and authority](../SKILL.md#scope-and-authority) (the Agile Workflow controller
skeleton and re-run fields are in [controller-and-reruns.md](controller-and-reruns.md)); comparison rows
belong in the Agentic Research artifacts that record links, while coverage mapping,
transfer and proposals belong in the loop record. Preserve dated reports; link corrections and
later assessments rather than changing what an earlier pass concluded.

## Contents

- [Record location and discovery](#record-location-and-discovery)
- [Charter and loop checkpoint](#charter-and-loop-checkpoint)
- [Component coverage and coordination](#component-coverage-and-coordination)
- [Comparison rows](#comparison-rows)
- [Transfer and proposals](#transfer-and-proposals)
- [Finding record](#finding-record)
- [Decision packet](#decision-packet)
- [Assessment report](#assessment-report)

## Record location and discovery

The standalone fallback `methodology-review-state.md` uses existing planning
metadata, so an adopter's index can consume it if its discovery rules include root
files:

```yaml
---
description: "Operational decisions and checkpoints for methodology reviews"
type: design
kind: planning
updated: YYYY-MM-DD
summary: "Review scopes, operator decisions, delivery links and assessment outcomes"
decisions:
  - "Project-method changes require operator adjudication; review progress is recorded here."
---
```

Substitute the actual date and keep `decisions` current; the initial entry records
the review's authority boundary, not a substantive project decision. Give each
review's ID and scope a named body section holding its dated assessor reports,
which link research outputs and the current baseline. They assess loop progress;
they are neither source-direct research nor a replacement for the orchestrator's
analytical outputs.

## Charter and loop checkpoint

Record the target, review questions and the skill's step 1 charter, plus completed
assessment rounds, the latest verified research artifact and the next required step.
Record the domain-map version the sample drew from, the sample checkpoint's challenge
report and operator response, and expected effort (engagements, dispatches,
assessments, rounds); add actual effort as it accrues. Effort is information for the
operator, never a cap.
Separate fixed constraints from hypotheses by checking project intent, never by
assumption.

For each required check, record its owner, actual result, assessed scope/baseline,
evidence location and remaining obligation. Mark absent, errored or stale evidence
explicitly; a tool's completion or a persisted artifact is not a successful verdict
([build process §Completion](../../../docs/build-process.md#completion)). On
correction or resume, keep earlier reports and say which coverage remains valid or
needs renewal under the owning workflow. Delivery's accepted-fix verification and
this review's fresh whole-scope assessment are distinct obligations. For a
multi-engagement program, link the actual commissioning items, which alone own
dependencies, stages and completion; never copy another item's stages or delivery
decomposition here.

## Component coverage and coordination

For a split review, the root records its ID, selected shape, considered cuts,
rationale, exclusions and remaining coupling, plus the completed-round count,
current round and shared limit. Research engagement counts and child completion
counts are different quantities. Each child gets a named section or a link to its
authoritative review item, holding the
[child contract](review-decomposition.md#run-a-child-review) inputs and its latest
assessment link. Beside the child links, record parent integration findings and the
fresh whole-scope assessment, linking (not copying) child outcomes and obligations.

After a new cut or on resume, retain prior IDs and assessments and record their
mapping to current children, changed baselines and next unfulfilled steps. The
standalone fallback holds the same fields in linked sections; no new frontmatter or
tracker is needed.

## Comparison rows

For each representative approach, record:

| Field | Content |
|---|---|
| Intended use | Users, job, context, constraints; why it is in the sample |
| Native approach | Its own concepts, workflow and configuration, before our terms |
| Scenario | Common task/input with positive, adverse and correction paths |
| Method | Acquisition, reasoning, evaluation, human decisions, action, learning as applicable |
| Evidence | Source chain and inspected revision/date; claim, demonstration or measurement |
| Consequence | Outcome quality, uncertainty, human/operating burden, limitations, tradeoffs |

These rows describe each alternative in its own terms; research never maps it onto
this project. Choose representative methods, not a vendor quota. Assign no numerical aggregate
score without agreed weights and evidence adequate for that precision.

## Transfer and proposals

Keep these in the loop record, beside the verified comparisons they draw on, and
never in the research artifact:

| Field | Content |
|---|---|
| Coverage mapping | How the alternative's capabilities relate to ours: direct, delegated, partial, explicitly excluded or unknown, including capabilities outside our categories |
| Transfer | What to retain, simplify, adopt, integrate or test here, and why context supports it |
| Proposal | The finding and decision-packet choice it feeds, by stable ID |

A proposal cites the research's non-recommending decision-relevance section. The
research states the conditions under which an alternative would win; the loop record
argues whether those conditions hold here.

## Finding record

Keep one stable ID across rounds; never mint a fresh ID to conceal persistence.
Qualify new local IDs by originating review (`R4-B/METH-003`); keep existing bare
IDs, identified by owning review plus ID. Equal local numbers in different reviews
are not duplicates and never justify a merge. Keep origin identities when ownership
or boundaries change, record aliases only for actual merges, and match handoff items
by the same identity. Record:

- Observation and evidence, affected outcome, severity/materiality rationale and confidence.
- Current approach, credible alternatives and strongest contrary evidence.
- Recommended choice and exact proposed project effect; retention is a valid choice.
- Deciding evidence or experiment, success/failure criteria and important burdens.
- Prior IDs if merged, and the assessment that verified a remedy or withdrew the finding.

Keep three facts distinct:

| Dimension | Examples |
|---|---|
| Evidence assessment | Supported finding; uncertain/needs evidence; withdrawn with reason |
| Operator decision | Unanswered; accept; modify; reject; defer; request more evidence |
| Remedy verification | Not authorized; authorized/pending; applied/awaiting assessment; verified resolved |

These are report fields, not work-item stages. An accepted proposal with queued
implementation is still pending; a rejected one can leave a supported risk.
Withdrawal needs a source/evidence rationale, not merely a rejected recommendation.
An alternative authorized remedy that resolves the issue is verified normally.

## Decision packet

For each unresolved major finding, give concise, comparable choices: recommendation,
consequence of retention, confidence, affected scope and what each choice
authorizes. Capture the decision's date, operator, actual instruction/rationale,
scope and next action, and link each emitted item; item linkage, brief alignment
and deduplication follow the skill's
[step 5](../SKILL.md#5-operator-adjudication-and-authorized-action).

## Assessment report

Record the charter/baseline and full agreed coverage, including exclusions and
unavailable evidence. Give counts and IDs for new and persistent major findings,
accepted but pending remedies, verified resolutions, evidence-based withdrawals,
retained/deferred major risks and minor observations. Link source and verification
records; end with one exit outcome from the skill and its reason. A parent report
adds actual child coverage, conflicts and cross-component scenarios checked, reuse
of prior assessments, unresolved dependencies, the root round/checkpoint and next
step.

“No new major findings; two previously identified risks remain by operator decision”
must never become “zero major findings.”
