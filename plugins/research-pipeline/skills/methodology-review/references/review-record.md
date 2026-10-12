# Comparison and review record

Use these fields in the project's existing records. They are a writing aid, not a
new frontmatter schema, database or research tier. Keep analytical snapshots under
Agentic Research's artifact conventions; keep decisions and delivery state in the
project's work/decision record. Preserve dated reports and link corrections or later
assessments rather than retroactively changing what an earlier pass concluded.

## Record location and discovery

Use the matching `methodology-review` tracking item in Agile Workflow, without a
`research` tag/dials on the loop controller. An engagement may close independently;
the controller tracks the still-open decisions and reassessments. Other established
project trackers keep their own conventions.

The standalone fallback is the fixed project-root `methodology-review-state.md`,
never a file under `.research/`. Use existing planning metadata so an adopter's index
can consume it if its discovery rules include root files:

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

Substitute the actual date and keep decisions current; the initial entry records
the review's authority boundary, not a substantive project decision. Record the review ID and
scope in a named body section; use additional sections for concurrent reviews.
Append dated assessor reports in the relevant section, linking the research outputs
and current baseline. Those reports assess loop progress; they are not source-direct
research or a replacement for the orchestrator's analytical outputs. This record
uses the existing planning schema, not a new frontmatter contract.

## Charter and loop checkpoint

Record the target, baseline, jobs/outcomes, constraints, questions, criteria,
scenarios, included/excluded scope, research settings, completed assessment rounds
and round limit. Link the latest verified research artifact and next required step.
For a multi-engagement program, link its actual commissioning items; only those items
own dependencies, stages and completion. Do not copy delivery decomposition here.

Separate fixed constraints from hypotheses. For example, a required jurisdiction
can be fixed while a manually curated catalog is an approach to compare. Do not
assume either distinction without checking project intent.

## Comparison rows

For each representative approach, record:

| Field | Content |
|---|---|
| Intended use | Users, job, context and constraints; why it belongs in the sample |
| Native approach | Its own concepts, workflow and configuration before translating to our terms |
| Coverage mapping | Direct, delegated, partial, explicitly excluded or unknown; additional capabilities outside our current categories |
| Scenario | Common task/input and its positive, adverse and correction paths |
| Method | Acquisition, reasoning, evaluation, human decisions, action and learning as applicable |
| Evidence | Specific source chain and inspected revision/date; distinguish claims, demonstrations and measurements |
| Consequence | Outcome quality, uncertainty, human/operating burden, limitations and tradeoffs |
| Transfer | What could be retained, simplified, adopted, integrated or tested here; why context supports transfer |

Choose representative methods, not a fixed vendor quota. Explain excluded families
that could affect the decision. Do not assign a numerical aggregate score without
agreed weights and evidence adequate for that precision.

## Finding record

Use a stable ID, such as METH-001, across rounds. Record:

- Observation and evidence, affected outcome, severity/materiality rationale and confidence.
- Current approach, credible alternatives and strongest contrary evidence.
- Recommended choice and the exact proposed project effect; retention is a valid choice.
- Deciding evidence or experiment, success/failure criteria and important burdens.
- Prior finding IDs if merged, and the assessment that verified a remedy or withdrew
  the finding. Do not mint a fresh ID to conceal persistence.

Keep three different facts visible:

| Dimension | Examples |
|---|---|
| Evidence assessment | Supported finding; uncertain/needs evidence; withdrawn with reason |
| Operator decision | Unanswered; accept; modify; reject; defer; request more evidence |
| Remedy verification | Not authorized; authorized/pending; applied/awaiting assessment; verified resolved |

These are report fields, not new work-item stages. An accepted proposal with a queued
implementation is still pending; a rejected proposal can leave a supported risk.
Withdrawal requires a source/evidence rationale, not merely a rejected recommendation.
If an alternative authorized remedy resolves the issue, verify it normally.

## Decision packet

Present concise, comparable choices for each unresolved major finding. Include the
recommendation, consequence of retention, confidence, affected scope and what the
choice authorizes. Ask about adoption, experiments, filing or implementation only
when the user's intent does not already settle that action. Reuse the user's existing
answer rather than imposing a second approval ceremony.

Capture the decision's date, operator, actual instruction/rationale, scope and next
action. Link each emitted work item. The item must link back to this decision and
carry the stable review/finding IDs, research origin, authorized next action and an
operative brief/acceptance boundary matching that decision. For example, a decision
to pilot an approach in one workflow cannot leave a broader rollout as the item's
brief. Keep the broader research proposal only as clearly labeled background.
Deduplicate by review/finding identity across refreshed research slugs. A decision
about one finding must not become blanket permission for later findings or changes.

## Assessment report

Record the charter/baseline and full agreed coverage, including any exclusions or
unavailable evidence. Report counts and IDs for new/persistent major findings,
accepted but pending remedies, verified resolutions, evidence-based withdrawals,
retained/deferred major risks and minor observations. Link the source and verification
records. End with one exit outcome from the skill and its reason.

A useful final assessment can say “no new major findings; two previously identified
risks remain by operator decision.” It must not turn that into “zero major findings.”
