---
name: methodology-review
description: >
  Compare a project's methods, workflows and assumptions with relevant products,
  projects and research. Scout alternative approaches, assess a whole project or
  selected component, and iterate through operator decisions and fresh review until
  no major findings remain or an explicit stopping condition applies. Use for
  methodological assessment or comparison with prior art, not ordinary code review
  or documentation consistency checks.
---

# Methodology Review

Review whether the project's approach serves its intended outcomes, using external
alternatives and common scenarios. The current architecture and procedures are
hypotheses to examine, not mandatory criteria for every alternative.

This skill owns the comparison framing and operator-adjudicated loop.
`agentic-research:research-orchestrator` owns grounded research, registration,
source records, refresh and verification. Read the plugin's
[build process](../../docs/build-process.md) and
[research composition](../../docs/research-composition.md). Agentic Research is a
required companion; if unavailable, report the missing prerequisite and stop the
research run rather than inventing a substitute engine.

## Scope and authority

Accept a project, component, workflow or existing review record. With no target,
use the active project's instructions and ask only if its review boundary is
unclear. Discover components; do not assume a domain, folder count, implementation
stack, product list or need for every discovered component to receive a deep pass.

Invocation authorizes investigation and review artifacts. It does not authorize
changes to the project's methods, requirements, contracts, architecture, code or
operating policy. The operator adjudicates those decisions. Routine research
choices and corrections to the review's own analysis remain the agent's work.
Prior explicit authorization remains valid within its stated scope.

Resolve one durable loop record before research. In an Agile Workflow project, use
an existing matching work item or scope a review-tracking item through
`agile-workflow:scope`. Tag it `methodology-review`; do not give that loop controller
a `research` tag or `research_dials`. Separately commissioned research items own their
engagements, so the orchestrator cannot close the controller after the first report.
Use another project's established decision tracker when applicable; never mix trackers.
Otherwise use `methodology-review-state.md` at the project root, outside `.research/`,
with the existing planning frontmatter described in the reference. Separate concurrent
reviews by named sections; do not overwrite another review or bootstrap `.work/`.

Store operator decisions, delivery links and dated full-scope assessment snapshots
in this loop record. Research comparisons and source verification remain in Agentic
Research's normal artifact map, linked from each snapshot. Do not rewrite a completed
research report to reflect operational decisions or implementation status. Consult
[review-record.md](references/review-record.md) when first recording the charter,
findings or decisions; it uses existing schemas rather than adding an ARD tier.

## 1. Set a review charter

Read project intent, instructions, relevant knowledge navigation, existing research
and current delivery state. Record:

- Intended users, jobs, outcomes, constraints and decisions this review may change.
- The agreed scope and baseline revision/digests; project-wide versus component-only
  coverage, and any deliberate exclusions.
- Current methodological assumptions, disputed requirements, and what evidence could
  change them. Distinguish operator constraints from inherited design choices.
- Common scenarios and meaningful comparison criteria: outcome quality, evidence,
  uncertainty, human effort, correction/learning, operating burden and applicability.
- Search vectors and a provisional sample covering genuinely different approaches,
  including a simpler baseline when relevant. Explain consequential exclusions.
- Confirmed research settings, completion criteria and review-round limit. Propose
  mixed scope authority and standard verification unless context calls for different
  settings; let the orchestrator settle its dials. Default to at most five complete
  assessment rounds, including the initial round; the operator may change this limit.

Use existing answers and authorization; do not repeat settled kickoff questions.
Expose material ambiguity before dependent work. A suite landscape can precede
component studies, with one pilot calibrating the rubric before wider use. This is
an option, not a fixed topology. Use `research-pipeline:research-program` when
several separately commissioned engagements and their dependencies warrant it.
Each engagement gets its own registration; an engagement closing does not close
the surrounding review loop.

## 2. Research and compare

Use `research-pipeline:scout` for missing landscape coverage, then commission the
bounded comparison through `agentic-research:research-orchestrator`. Reuse relevant
existing research through its source/refresh rules; do not automatically repeat a
whole scout each round. Supply the charter, decision relevance and proposed
landscape/comparison output. The orchestrator discovers the research facets and
runs its verification stack; this skill does not duplicate that machinery.

Ask the research engagement to:

- Describe alternatives in their own categories before mapping them to the project.
  Include different configurations, deliberately omitted work and capabilities
  outside the current inventory. A longer feature list is not a better method.
- Compare the same user job under stated constraints. Record differences in audience,
  scale and purpose that limit a comparison. A documentation gap means unknown unless
  evidence establishes absence; a provider's advertised capability is not execution
  evidence.
- Follow representative scenarios through information acquisition, interpretation,
  evaluation, human judgment, action and correction, as applicable to the domain.
  Include failure/contrary cases and the cost of maintaining the approach.
- Distinguish designed, documented, demonstrated and independently measured behavior.
  Propose decisive experiments where sources cannot settle a consequential choice;
  do not infer successful operation from coherent documents.
- Seek evidence against the project's approach and against proposed replacements.
  Preserve useful existing guarantees while making their benefit and burden testable.

Do not fetch private project content into public searches or external services.
Source acquisition is research; paid trials, deployments and experiments requiring
additional resources need their own authorized scope.

## 3. Produce findings and a decision packet

Finish the engagement's required verification before presenting recommendations as
verified. Include sample bias, comparability, source support and criteria favoring
the current design in its research seed. Where the agreed rigor includes an adversarial
read, these are lenses for that orchestrator-owned pass, not a second verification
stack. The full-scope assessor in step 5 is required for a clean exit even when the
research rigor is floor. A pass may serve both roles only if its actual scope and
structured result satisfy both requirements. Refresh the project's existing knowledge
index after new research artifacts, without bootstrapping an index on other projects.

Deduplicate findings with stable IDs. Separate methodological findings from incidental
doc/code defects. A **major** finding has evidence of a material threat to an agreed
outcome or consequential decision: an invalid method, missing necessary capability,
unjustified burden, or decision-blocking uncertainty. State the consequence and
uncertainty. A plausible alternative, an extra feature or a stylistic preference is
not major by itself. Missing evidence can require an experiment without establishing
that the current method is wrong.

For each finding, present the source-grounded observation, affected outcome, strongest
counterargument, plausible choices (including retention), recommended next action,
tradeoffs and deciding evidence. Identify exactly which project changes or experiment
would be authorized by each proposed choice. Present one manageable decision batch,
with unresolved major findings first; retain smaller observations without using them
to drive the loop indefinitely.

## 4. Operator adjudication and authorized action

Ask the operator to choose among accepting a proposal, modifying it, rejecting it,
deferring it, or requesting more evidence. Record the actual response, rationale,
selected scope and authorized next action in the operational record. A requested
change to the criteria or scope gets a new recorded baseline; it does not silently
erase a finding from the earlier scope.

- Silence, elapsed time and a pending asynchronous question are not approval.
- Partial decisions authorize only the answered portion. Continue independent research
  or explicitly authorized work while the remainder awaits adjudication.
- Agreement with a diagnosis or acceptance of a direction does not by itself authorize
  its implementation. Distinguish adoption-only, further research, filing work and
  applying a specified change. Ask only where that authorization is actually missing.
- When the operator explicitly requests filing research-derived work, invoke
  `agentic-research:research-handoff` with the source artifact, authorized finding IDs,
  exact decisions and filing destination; honor its confirmation contract. Check the
  loop record and existing items for matching review/finding IDs before emission, even
  if a refreshed research artifact has a new slug. Reuse matching items.
- Before handing emitted work to design, implementation or autopilot, reconcile each
  item's operative brief and acceptance scope to the operator's actual decision. Add
  the stable review/finding IDs, exact authorized next action, a backlink to the loop
  record and its decision, and the research-origin link. An original broader proposal
  may remain as labeled background, never as the operative instruction. Record the
  item link back in the loop record. These are work-side edits; do not alter research
  to make it agree with the decision.
- Apply authorized changes through the project's delivery workflow. This review skill
  does not bypass design, implementation, testing, review or deployment requirements.
  Record the resulting revision and evidence. If delivery occurs elsewhere or later,
  checkpoint as awaiting-change and resume when its evidence is available.

Rejecting/deferring a proposal does not falsify its evidence or verify a remedy.
Record retained risk, the operator's rationale and any revisit trigger. Do not keep
asking the same question on an unchanged baseline; reopen only for materially new
evidence, changed constraints or an explicit operator request. Correct a false finding
when the evidence warrants it, independently of whether its proposal was popular.

## 5. Fresh reassessment and exit

After an authorized change or additional deciding research, reassess the **whole
agreed review scope**, including cross-component consequences, regressions and new
major findings. A component-only charter stays component-only; a full-project charter
must not quietly shrink to edited files. Reuse current sources where sufficient and
refresh affected claims through the orchestrator. Do not restart discovery without a
named coverage or freshness gap.

Use a fresh-context assessor, with the project's cross-model preference when available.
Supply the charter, current project evidence, source-grounded comparisons and exact
operator decisions, but do not prescribe a verdict. Ask it to assess current methods
against the charter as well as verify earlier remedies. The assessment must distinguish
new findings, persistent findings, verified resolutions, evidence-based withdrawals,
and operator-retained risks. Store its dated report in the loop record, with the
research and delivery evidence it consumed. If it introduces an external claim absent
from verified research, keep the new finding provisional and route the claim through
the orchestrator before treating it as established or using it to justify a change.
A consequential provisional concern prevents a clean exit until resolved. Research
verification remains the orchestrator's job; this assessor does not replace or copy
that stack. An already independent initial assessment can supply the exit report if
no changes were required.

Read the exit from that assessment, not from the author's confidence or a targeted
grep. There is no claim that a bounded review proves universal methodological quality.

| Outcome | Required condition and next action |
|---|---|
| **Clean within reviewed scope** | Fresh full-scope assessment on the current baseline reports zero unresolved major findings, including retained/deferred major risks; all required research and delivery checks pass. Report minor observations and coverage limits. |
| **Awaiting decision** | At least one choice needed for progress is unanswered. Present the concrete decision packet and checkpoint; no dependent changes. |
| **Awaiting change or evidence** | An accepted direction has no verified remedy, or an authorized experiment/delivery is pending. Link the owner/item/evidence needed; do not call it resolved. |
| **Stopped with retained risks** | The operator elects to stop or retain/defer a material issue. List those findings and their revisit conditions. This is a dispositioned review, not a clean bill of health. |
| **Incomplete** | Required coverage/verification is unavailable, the round limit is reached, or another unchanged round would add no evidence or authorized progress. Report the limitation and the concrete next step; do not manufacture convergence. |

When several outcomes apply, report all finding statuses and choose the primary
outcome in this order: explicit operator stop (retained risks, or incomplete if none),
awaiting decision, awaiting change/evidence, incomplete, then clean. Paused portions
do not stop unrelated work that is already authorized.

A round ends with a verified comparison and full-scope assessment. Persist its count
and baseline. Do not run another unchanged round while waiting for a decision or
implementation, reset the counter on resume, lower severities to meet the exit bar,
or widen the research question indefinitely. If clean conditions are unmet at the
limit, stop as incomplete (or with the more specific pending/retained-risk outcome),
never as clean. Further rounds require the operator to extend the limit.

## Resume and report

To resume, use the supplied record path first; otherwise find the matching active
`methodology-review` work item or the project-root `methodology-review-state.md`.
If the requested review is already closed, recover its completed/archived record
through the project's retention conventions. If several records match, ask which
scope to resume. Read the current revision and linked research artifacts. Reconcile
intervening changes with the last charter, preserve earlier decisions and finding
IDs, and identify the next unfulfilled step. Never infer approval from an item's
presence or completion of its research engagement.

Report the assessed scope/baseline, approaches sampled, major findings by status,
operator decisions, authorized changes and verification, unresolved risks, and exact
exit reason. Link the research outputs and operational record. Keep the final result
usable even when the project has no implementation or no tracked work substrate.
