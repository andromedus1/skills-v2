---
id: story-research-quality-feedback
kind: story
stage: done
tags: [research]
parent: feature-quality-verification
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
research_dials:
  scope_authority: mixed
  verification_rigor: standard
  intent: calibrate-external
  output_kind: synthesis-brief
---

# Ground bounded quality-feedback and verification loops

## Commission

What evidence and primary engineering guidance support evaluator-driven correction
loops, and what limits prevent repeated checking from producing false confidence?
Consumer: methodology-revisers. Decision relevance: change quality checks only if
external evidence plus local assessment identifies missing criteria, verifier
independence, correction feedback, stopping or traceable outcome state. Preserve
proportionate one-pass review where repeated checking has no established benefit.

User approved the quality-enforcement pilot and resulting local implementation.
Carry forward mixed scope and standard verification from the same work arc.

## Full registration

```yaml
intent: calibrate-external
output_kind: synthesis-brief
consumer: methodology-revisers
verification_rigor: standard
temporal_contract: write-once-on-converge
primitives_extends: []
primitives_opts_out: []
decision_relevance: Identify when evaluator feedback and bounded correction improve assurance, versus merely adding repeated self-judgment, to choose justified workflow enforcement changes.
scope_authority: mixed
analytical_artifact_type: per-campaign-brief
```

## Substrate check and decomposition

Existing research-package-boundary informs composition/ownership only. No existing
brief answers this feedback-quality question. It is a framing lens, not source
substrate. Local skill/framework rules are objects of operational assessment in
the parent item, never source attestations in this research engagement.

Candidates: (1) one bounded comparison of feedback/verification designs; (2)
specialists by plugin, which duplicates the local operational assessment; (3)
specialists by research paper versus engineering guidance, which separates
mutually qualifying evidence. Select (1), light inline research with no specialist
fan-out. Self-flag: a small sample cannot establish universal model reliability;
seek both evidence for iterative refinement and contrary self-correction evidence.

Source plan: primary descriptions of evaluator/optimizer workflows, empirical
iterative-refinement work and contrary self-correction results. Read actual sources,
attest before synthesis, lint, one independent adversarial pass, then lead
spot-check. Gate outcomes and research completion stay here; the surrounding
methodology review continues independently.

## Verification checkpoint (2026-10-18)

Artifacts committed at 48971393; revisions are currently uncommitted. Five primary
sources attested before synthesis. Paper engagement is abstract/metadata only.
No necessary source remained inaccessible: a challenged OpenReview page had an
accessible arXiv counterpart. No source supports a general cross-model advantage.

Lint: 16 resolving citations; no broken chains, thin flags or patterns. Five optional
substrate_confidence omissions are metadata notices, not failed support checks.
Captured output: `/tmp/qve-research-lint.json`; command uses canonical lint,
explicit .research/attestation, --no-url-check, JSON and --exit-code-on high.

Independent adversarial pass `20261018T224044Z-6d8d1ec7` returned NEEDS-REVISION:
R1 frontmatter conflated a proposed control rule with source findings and generalized
pattern suitability; R2 placed Agents-section feedback/limits under evaluator-optimizer.
Accepted and corrected both. Also restored human-calibration wording, one-step
comparison baseline, abstract task range, uncertain contradictory relationship,
publication-status distinction and guidance age; moved acquisition history here.
Optional confidence metadata remains omitted; it is not a reason to manufacture
source confidence or rerun verification. Unused attestation details need not all
be forced into a decision-focused brief.

Lint after revision still passes with the 17 resolved/no-defect results (one added source citation).
Second adversarial pass `20261018T224727Z-f72abde7` is running on the revised artifact.
Lead source spot-check and consumption of its returned findings remain pending.
The story stays implementing; neither worker exit nor artifact existence closes it.

## Verified engagement completion (2026-10-18)

Second adversarial job f72abde7 returned NEEDS-REVISION for a remaining modal
overstatement in the contradiction row; it also requested compatible relationship
markers and source-anchor precision. The driver surfaced that result to Andrew,
kept this item implementing, corrected all instances and ran one explicitly bounded
correction check under the existing completion authority. There was no silent
restart, new engagement, extra methodology round or unrecorded success claim.

Continuation job `20261018T225153Z-6f86d928` returned terminal success and actual
**APPROVED**, covering jobs a–h with no material issue. The independent reviewer
also corrected its own prior paraphrase-as-quotation: the primary source says the
pattern is particularly effective under the named conditions. The driver used
source-read wording, not that earlier reviewer quote. No further research pass ran.

Lead terminal spot-check: consumed both NEEDS-REVISION reports and the APPROVED
correction report; checked the current 17 resolving chains and sampled the
load-bearing claims against all five fetched sources. Rechecked source sections
for evaluator suitability versus Agents stopping conditions and actual-outcome
versus human-calibrated grading; checked the three abstract-level result claims,
comparison baseline, task range and unresolved conditions. Swept corrected modal
claims and paragraph anchors across brief/frontmatter/attestations. No fabricated
counts, quotes or effort estimates found; no lint pattern category fired. The
uncertain relationship remains explicit and implementation suggestions remain
marked extends. No further corrections were needed.

Assessed brief SHA-256: `4edfb99a9181dc4bed28827a21f672a7581138f326afedb63b6860b7cfd81c74`. Lint: 17 resolved, zero broken/thin/pattern
findings; optional metadata notices remain nonblocking. Standard adversarial
verification: APPROVED after the recorded corrections. Lead spot-check: passed.
Isolated evaluator: not applicable to this one-facet, non-cross-synthesis shape;
no floor was pruned. Source engagement remains abstract-limited for the papers.

Outputs: `.research/analysis/briefs/quality-feedback-loops.md`, five attestations,
corpus references and the quality-feedback-loops bibliography. Default
research_completion close-to-done applies. This child research checkpoint is done;
QVE remains open for implementation, delivery verification and fresh assessment.
