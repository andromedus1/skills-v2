---
id: story-research-qvc-review-evidence
kind: story
stage: done
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

## Engagement record

### Kickoff (autonomous delegation; dials confirmed at scope time)

- Read dials: `scope_authority: mixed`, `verification_rigor: standard`,
  `intent: calibrate-external`, `output_kind: synthesis-brief`.
- `decision_relevance` (from the commission body): whether to retain, simplify
  or strengthen the cross-model review preference, review weights and
  covering-review reuse; and whether citation advisories should be
  reclassified, suppressed or retained.
- Remaining registration fields settled at dispatch: `consumer:
  methodology-revisers`; `temporal_contract: write-once-on-converge`;
  `primitives_extends: []`; `primitives_opts_out: []`;
  `analytical_artifact_type: per-campaign-brief`.
- Substrate-check: overlapping prior work is
  `.research/analysis/briefs/quality-feedback-loops.md` (lens only, never
  cited) and its attestations `anthropic-agent-evals` {7} and
  `anthropic-evaluator-optimizer` {6} (reusable as sources). No prior
  attestation covers judge bias, code-review practice or static-analysis
  warning response.

### Decomposition (Checkpoint A, surface-and-proceed)

Declared portion (from scoping): the two commissioned questions. Emergent
candidates considered:

1. One inline facet covering both questions. Cheapest, but the questions draw
   on disjoint literatures (LLM evaluation and software-engineering review
   versus static analysis and alert operations), so one author serialises two
   independent acquisition passes.
2. Two facets, one per question: `reviewer-independence` and
   `warning-noise`. Matches the declared split, keeps each literature with one
   specialist, and leaves a thin but real cross-join (both bear on when an
   additional check earns its cost).
3. Four facets: LLM-judge bias; human code-review practice; static-analysis
   false positives; alert fatigue and triage practice. Finer, but splits
   tightly coupled evidence (judge bias and multi-reviewer detection answer
   the same independence question) and multiplies cross-join work for a
   synthesis-brief output.

Chosen: candidate 2 (two specialists, parallel). Self-flag: the cross-join is
modest; the parent synthesis is mainly a side-by-side mapping onto the
decision questions, not a merged thesis. Corpus numbering: specialists use
provisional blocks, compacted by the lead into contiguous corpus-wide numbers
after both return.

### Fan-out and synthesis

- Two research specialists dispatched in parallel (discipline bundle inlined
  verbatim + specialist brief + facet params; model opus):
  `reviewer-independence` (15 new attestations, provisional 11-25) and
  `warning-noise` (12 new attestations, provisional 41-52, compacted by the
  lead to 26-37). Corpus numbers 11-37 appended to `.research/references.md`;
  bibliography at `.research/reference/qvc-review-evidence/BIBLIOGRAPHY.md`.
- Checkpoint B (surface-and-proceed): contradictions carried into
  `parent.md` § Contradictions, including two the lead added at the
  cross-join: Google reviewer guidance (approve with unresolved comments)
  versus Google static-analysis article (reviewers typically withhold approval
  until automated comments are addressed); and Tricorder 2015 (probation at
  10%, possible shut-off above 25%) versus the 2018 article (disabled above 10%
  until improved). The latter was also added to the warning-noise brief as C7
  before verification.
- Acquisition offgas: `acquisitions.md` written (0 blocking, 6 enriching).
  The lead verified the reference-list groundings of four enriching
  candidates against the fetched PDFs/HTML and extended the attestations
  `google-static-analysis-lessons`, `facebook-infer-zoncolan-scaling`,
  `code-reviews-do-not-find-bugs` and `ddi-alert-tiering-compliance` with
  those reference-list entries (additive substrate extension; no cited claim
  changed). One public search found no open full text for the abstract-only
  Imtiaz et al. source. Queue promotion is proposed, not written (operator
  decision via `/agentic-research:research-handoff`).

### Verification (in progress)

- Lint (hard floor), with URL liveness: 3 files, 361 resolved citations,
  0 broken, 0 thin, 57 pattern advisories. Grouped: version-number and
  decimal-with-attribution (model names such as GPT-3.5/Qwen2.5, decimals,
  bibliography lines); comparative-superlative on source-named phrases
  ("most recent push", "most severe tier", "least serious tier", "no false
  positives"); one count-without-unit (L37 warning-noise, cited on the next
  line); one named-feature-claim (L219 warning-noise, cited inline);
  reduced-substrate-attestation info on the abstract-only
  `coverity-alert-actionability-oss`; deprecation notice for the reused
  `anthropic-agent-evals` attestation lacking `substrate_confidence` (not
  edited: outside this engagement's authored substrate). Advisories reviewed;
  none is an unsupported composed claim. Zero broken/thin does not by itself
  establish semantic support.
- Adversarial read, attempt 1: the reader stalled (watchdog, no progress for
  600s) without writing a checklist or verdict. Recorded as not run, not as a
  pass. Re-dispatch pending.
- Resume (2026-10-19, lead session): the first engagement worker ended with
  the adversarial read unrun. Gate catalog for this shape: lint and spot-check
  (hard floor), adversarial-read (standard profile), and `evaluate`, which ARD
  SPEC §7/§3.1 places in the floor of any cross-specialist synthesis shape
  regardless of profile. Adversarial read attempt 2 dispatched with incremental
  checklist writing to `verification-checklist.md`; evaluate follows its
  verdict; lead spot-check last. Stage remains `implementing`.
- Adversarial read, attempt 2 (first completed): **NEEDS-REVISION**. Checklist
  `.research/analysis/campaigns/qvc-review-evidence/verification-checklist.md`.
  Lint rerun 361 resolved, 0 broken/thin, 59 advisories (2 from
  `acquisitions.md`). No fabrication; material issues are caveats stripped at
  synthesis and mis-scoped citations (A1, A2+E2, A3+R1, C1, C2, C3, C4+E1+D1,
  E3+W4) plus minor findings. `parent.md` checked exhaustively; briefs ~80/96
  and ~110/144 citations; sources not re-fetched. Revision pass dispatched;
  then adversarial re-read. A second NEEDS-REVISION is surfaced to Andrew.
- Revision pass 1 (2026-10-19): all material, minor and info findings
  dispositioned in the checklist's `## Revision response`; two attestations
  extended additively from re-fetched sources (W1, D4; lead verified zero removed
  lines). Lead lint rerun: 0 broken, 0 thin, 0 high/medium. Parent grew ~22%
  from restored qualifiers. Next: adversarial re-read (attempt 3; a further
  NEEDS-REVISION is surfaced to Andrew) and `evaluate` (isolated: synthesis +
  seed only), dispatched in parallel on the same revised synthesis.
- `evaluate` (isolated): **APPROVED** with non-material corrections
  (`campaign-evaluation.md`).
- Adversarial re-read (attempt 3): **NEEDS-REVISION** — prior material findings
  resolved except C2, whose fix introduced N1 (MT-bench chain-of-thought also
  cut failures, 14→6 of 20 vs reference 3 of 20; synthesis states a
  contradiction the source lacks; the wording originated in the attempt-2
  checklist and was copied as fact). N2: Facebook diff-time findings called
  "non-blocking" without support. Minor m1–m5. Both attestation extensions
  verified against re-fetched sources. Second NEEDS-REVISION surfaced to Andrew
  per the orchestrator; no further revision without his decision.
- **Operator decision (Andrew, 2026-10-19): bounded fix.** One final targeted
  correction of N1 (MT-bench attestation extended from a re-fetched Table 4
  first), N2, m1–m5 and the evaluator's recommendations 1–5. Verification: a
  targeted N1/N2 re-check plus lead spot-check, not a full third read. If that
  check fails, mark verification incomplete and proceed with the limitation.
- Targeted N1/N2 re-check: N1 and N2 resolved; new **N3** (exclusive "one
  study comparing judge prompts" — other attestations also compare prompts).
  Lead spot-check: evaluator candidates and lint pattern sample supported; N3
  corrected in place (scoping + restored {13} result); lint 0 broken / 0 thin.
- **Outcome: verification incomplete** per Andrew's bounded-fix rule — the
  final targeted adversarial check returned NEEDS-REVISION and its N3 fix was
  made by the lead without an independent re-read. Stage stays `implementing`;
  consumers treat the synthesis as verified except that limitation. Closing it
  needs only an independent read of the N3 lines.
- Independent N3 re-read (operator-authorized, 2026-10-19): **APPROVED** —
  N3 resolved, no new material issue. Verification now complete at standard
  rigor (+ evaluate): lint pass; adversarial-read APPROVED on the final lines;
  evaluate APPROVED; lead spot-check done. Lead fixed one relative link in the
  RI revision log (non-substantive).
- **Known limitations carried to consumers:** in MT-bench the "reference" is
  the judge's own independently generated answer, not external ground truth
  (`llm-judge-mt-bench.md` L41-42; stated in the RI brief, not in `parent.md`);
  "judge error" there means an incorrect answer judged correct. Other reader
  notes (wording "another study" twice; Tricorder probation qualifier at
  parent L290-291) are informational and left as recorded in the checklist.
  Stage → done.
