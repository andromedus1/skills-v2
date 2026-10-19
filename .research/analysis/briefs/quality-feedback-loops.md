---
title: Evidence and limits for quality-feedback loops
provenance: agent-synthesis
updated: 2026-10-18
summary: Explicit criteria and observed outcomes support evaluation, while studies disagree about intrinsic self-correction under different conditions.
key_findings:
  - Evaluator-optimizer guidance describes clear criteria and measurable refinement value as best-fit conditions.
  - Self-correction findings are conditional; repeated model judgment alone is not a correctness guarantee.
  - "Proposed implication: record checked outcomes and preserve bounded unresolved exits."
---

# Evidence and limits for quality-feedback loops

## Question and sample

When should an agent workflow use evaluator feedback and repeated correction?
This bounded sample combines engineering guidance with both positive and negative
self-correction findings. Paper engagement is limited to source-read abstracts;
the empirical results are reported claims, not independently replicated findings.

## Comparison

| Approach | Attested behavior and limitation |
| --- | --- |
| Evaluator-optimizer | Separate generation/evaluation calls suit clear criteria and demonstrable improvement. The separate Agents section stresses environmental feedback and describes iteration limits as common controls. Guidance from 2024; tooling has since changed. [anthropic-evaluator-optimizer]{6} |
| Agent evaluation | Inspect the resulting environment state, not just the agent's claim. Code, model and human graders have different limits; model judgments need human calibration. [anthropic-agent-evals]{7} |
| Same-model refinement | Authors report gains over one-step generation using one model for feedback/refinement, across tasks from dialogue to mathematical reasoning. Transfer is unestablished here. [self-refine]{8} |
| Intrinsic reasoning correction | Authors report difficulty and occasional degradation without external feedback in their studied reasoning setting. [intrinsic-self-correction-limits]{9} |
| Conditioned intrinsic correction | Authors report positive self-correction with fair prompts and zero temperature across tested models. [intrinsic-self-correction-prompting]{10} |

## Contradictions

| Relationship | Positions retained |
| --- | --- |
| tension | Positive refinement results [self-refine]{8} and negative reasoning results [intrinsic-self-correction-limits]{9} prevent a universal claim from either abstract. Tasks and procedures are not treated as identical. |
| tension | The conditioned positive account [intrinsic-self-correction-prompting]{10} challenges a broad reading of intrinsic-correction failure [intrinsic-self-correction-limits]{9}. {ambiguous: whether the earlier experiment lacked the later conditions; abstracts do not establish this.} The former page says in submission; the latter identifies ICLR 2024. |
| qualifies | Evaluator-optimizer guidance describes clear criteria and measurable refinement value as best-fit conditions [anthropic-evaluator-optimizer]{6}; grader limitations [anthropic-agent-evals]{7} qualify treating an evaluator verdict as ground truth. |

## Disconfirming analysis

The positive studies oppose rejecting iteration outright. The negative study
opposes assuming another self-check improves reasoning. The later conditioned
study also opposes generalizing the negative finding to all prompts and settings.
[self-refine]{8} [intrinsic-self-correction-limits]{9}
[intrinsic-self-correction-prompting]{10}

Engineering guidance also favors simpler approaches when sufficient.
[anthropic-evaluator-optimizer]{6}

## Design implications

`extends`: a workflow can declare its criteria, required checks, assessed baseline,
actual results and remaining obligations before claiming success. This translates
the distinction between observed outcomes and narrative completion into an
operational record. [anthropic-agent-evals]{7}

`extends`: add bounded correction where useful feedback changes the result.
Report unresolved outcomes at the cap. This is a proposed control rule, not a
measured advantage of this implementation.
[anthropic-evaluator-optimizer]{6}

## Limits

This sample does not compare current model families, prove the benefit of
cross-model over same-model review, prescribe a universal severity threshold, or
justify a fixed number of retries. Local failure examples and execution tests must
establish whether a concrete workflow change helps.
