---
id: story-research-qvc-review-evidence
kind: story
stage: implementing
tags: [research]
parent: feature-claude-methodology-repeat
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

# Ground reviewer independence and warning-noise evidence for QVC

## Commission

Two evidence gaps that `quality-feedback-loops` explicitly disclaims, for the
QVC methodology review (`feature-claude-methodology-repeat`):

1. **Reviewer independence.** What evidence bears on same-model versus
   different-model (or human) review of generated work — e.g. LLM-judge
   self-preference/self-enhancement bias, agreement with human judgment, and
   whether independence improves defect detection? What does human code-review
   practice and research say about one reviewer versus several, and about
   re-review after changes?
2. **Warning noise.** What evidence describes developer response to advisory or
   lint warnings with high false-positive rates (e.g. static-analysis adoption,
   effective false-positive thresholds, alert fatigue), and what practices keep
   advisory signals actionable (suppression, classification, severity tiers)?

Consumer: methodology-revisers (QVC children QVC-R and QVC-S, and the root
assessment). Decision relevance: whether to retain, simplify or strengthen the
current cross-model review preference, review weights and covering-review reuse;
and whether citation advisories should be reclassified, suppressed or retained.
Seek evidence against the current approach as well as for it. Distinguish
designed, documented, demonstrated and independently measured behavior.

Andrew authorized the Claude-driven QVC repeat; mixed scope and standard
verification carry forward from the established settings. Do not send private
project content to external services.

## Full registration

```yaml
intent: calibrate-external
output_kind: synthesis-brief
consumer: methodology-revisers
verification_rigor: standard
temporal_contract: write-once-on-converge
```
