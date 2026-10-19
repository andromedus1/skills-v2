---
title: Campaign evaluation — qvc-review-evidence
provenance: agent-verification
gate: evaluate
updated: 2026-10-19
target: parent.md (after revision pass 1)
verdict: APPROVED
---

# Campaign evaluation — qvc-review-evidence (2026-10-19)

Isolated `evaluate` gate (ARD SPEC §7). Inputs: discipline bundle, evaluator
brief, seed (Commission + Full registration only), `parent.md` after revision
pass 1. Persisted by the lead from the evaluator's inline return.

**Verdict: APPROVED**, with non-material corrections recommended.

## 1. Coverage
Complete against the commission. Q1: self-preference {11}–{15}; agreement with
human judgment (MT-bench 85% vs 81%, panel kappa); defect detection partly via
{17}, with the isolated same- vs different-model gap stated; one vs several
reviewers {18}–{23}; re-review {18},{20},{24},{25} with a measurement gap. Q2:
developer response {26}–{30}; thresholds/definitions incl. incommensurability;
alert fatigue (clinical, SOC); practices (suppression, tiers, routing —
"classification" thin but acceptable). Evidence-type labels throughout;
disconfirming analysis present; all decision targets addressed; transfer gap to
prose/citation linters and agent consumers acknowledged. Small gap: the
cross-model bullet never weighs "simplify" against "strengthen". Sample count
consistent (28 handles).

## 2. Coherence
Strong, with seams: (a) the "Non-blocking signals that are acted on" heading
leads with Google findings that are socially enforced at approval; (b) summary
calls Facebook diff-time findings "non-blocking", which the body does not say;
(c) tiering row does not label arms/metric; (d) inconsistent evidence-type labels
for observational studies {36} vs {37}.

## 3. Contradictions
Present, substantive, not smoothed (13 rows, correct relationship vocabulary).
Mild smoothing only in the frontmatter summary: "measured self-preference bias"
flattens the qualifies row; "without references" dropped from the
different-model-judge clause.

## 4. Groundedness
Strong posture. Unmarked composed comparatives: "where judge errors fell most
clearly" and "the condition most often associated with reduced judge error"
(across {11},{13},{15}) lack `{inferred}` markers. Spot-check candidates: Facebook
"non-blocking"; Qwen2.5-72B 86 vs 55 metrics; panel-vendor affiliation {16};
7–8× cost {16}; ~30% per reminder {37}; tiering figures {36}; 75% wording bugs
{27}/{29}; >80% one iteration {20}; ~15% defect comments {23}; 24% vs 6% {17}.

## 5. Recommendations (priority order)
1. Ground or remove "non-blocking" for Facebook; retitle/qualify the
   "Non-blocking signals" heading.
2. Bring the summary up to key-finding qualifiers (self-preference harmful
   mainly when wrong; restore "without references").
3. Mark or reword the "most clearly"/"most often" comparatives.
4. Label tiering arms/metric; harmonise {36}/{37} evidence labels.
5. Optionally state simplify vs strengthen in the cross-model bullet.
6. Run the component-4 spot-checks.
