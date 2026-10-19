---
title: Evidence on reviewer independence and warning noise
provenance: agent-synthesis
updated: 2026-10-18
summary: >
  Cross-facet synthesis on two questions about review and advisory controls for generated work. Same-model judging
  carries a measured self-preference bias, but switching to a different model removes only part of it, and grounded
  checks (references, oracle feedback, longer judge reasoning) are where judge errors fell. Human-review data
  support a gain from one reviewer to two, not beyond, and no fetched source measures whether an earlier approval
  safely covers later changes. Noisy warnings are ignored when delivered outside the work context, yet non-blocking
  review-time findings are acted on at high rates when curated by an action-rate feedback loop, explained, tiered
  and kept low in volume; false-positive thresholds are definition-specific.
key_findings:
  - "Self-preference in LLM judges is reported by several groups; with ground truth, stronger models' self-preference is mostly legitimate, but more harmful when they are wrong."
  - "A different-model judge still favours functionally similar models, so model identity is not independence; grounding is the recurring condition under which judge errors fell."
  - "No fetched study isolates same-model versus different-model review of generated code as the single varied factor."
  - "One inspector did worse than two or four; two and four did not differ; effort rose with reviewer count. Observational links between review participation and later defects did not survive independent replication."
  - "Re-review after changes is governed by documented or designed policy (approve-with-comments; diff-tied approval dismissal); no fetched source measures post-approval defect introduction."
  - "The same analysis with the same estimated false-positive rate went from near-zero action as a batch list to over 70% at diff time; delivery point mattered more than false-positive rate in that report."
  - "Published thresholds (zero effective false positives to block; under 10% for review-time checks; probation at a 10% not-useful rate) are defined by developer action, not report correctness, and were not validated against outcomes."
  - "Override or non-action is not by itself degradation: about half of outpatient alert overrides were judged appropriate."
---

# Evidence on reviewer independence and warning noise

## Question and sample

Two questions:

1. **Reviewer independence.** What evidence bears on same-model versus different-model or human review of
   generated work, on one reviewer versus several, and on re-review after changes?
2. **Warning noise.** How do people respond to advisory warnings with high false-positive rates, and what keeps
   advisory signals actionable?

The sample has 27 newly attested sources plus one reused attestation. Question 1 draws on seven LLM-evaluation
papers (2023-2025), five empirical software-engineering studies of inspection and code review (1997-2020), one
industry talk abstract and two practitioner documents. Question 2 draws on four industrial static-analysis
experience reports, an interview study, an open-source mining study (abstract only), an operations paging chapter,
a security-operations qualitative study and four clinical decision-support studies. Engagement depth is recorded
per source in the bibliography; one source was read only as an abstract
[coverity-alert-actionability-oss]{31} {confidence: abstract-only}, and many others were read as main text without
appendices or figure values.

Evidence-type labels follow the commissioning distinction: **designed** (intended or configurable behaviour),
**documented** (an organization describes its practice), **demonstrated** (the authors' own experiment or deployment
data), **independently measured** (replication, third-party measurement or aggregation of others' measurements).

## Question 1 — reviewer independence

### Same-model versus different-model judging

- **Self-preference is measured but its harm is conditional.** GPT-3.5, GPT-4 and Llama 2 favoured their own news
  summaries, with preference strength tracking self-recognition; the authors say this supports, without validating,
  a causal link, and they did not control for ground-truth quality [llm-self-recognition-preference]{12}. Self-bias
  was present in all six models examined in a self-refinement study and amplified over iterations
  [llm-self-bias-refinement]{15}. The MT-bench authors saw GPT-4 and Claude-v1 favour themselves but GPT-3.5 not,
  and could not determine whether the bias exists [llm-judge-mt-bench]{11}. On verifiable tasks, stronger models'
  self-preference mostly matched genuinely better outputs, but when the judge's own answer was wrong they preferred
  themselves more: Qwen2.5-72B's harmful self-preference propensity was 86 on MATH500 against an overall
  self-preference ratio of 55 [llm-self-preference-legitimacy]{13}. *(demonstrated in each study; convergent across
  groups {inferred: convergence})*
- **Model identity is not independence.** Judges also favoured models whose mistakes resemble their own after
  controlling for accuracy, and the authors argue it "is not sufficient to just use a held-out LM as the judge";
  they report model mistakes becoming more similar with capability [llm-judge-affinity-similarity]{14}.
  *(demonstrated)*
- **Diversity helped in one panel study.** A three-family panel agreed with human judgements better than a single
  GPT-4 judge on QA (Cohen's kappa 0.763 vs 0.627 on NQ), at seven to eight times lower cost, and each judged model
  received its largest favourable deviation when judged by itself; the panel did not beat every single judge on every
  dataset, three settings were tested, and the authors work for the vendor of one panel member
  [llm-judge-panel-poll]{16}. *(demonstrated, single group)*
- **Grounding is where judge errors fell.** A reference-guided judge cut math-grading failures from 70% to 15%
  [llm-judge-mt-bench]{11}; reference-based feedback the authors treat as oracle feedback reduced self-bias
  [llm-self-bias-refinement]{15}; chain-of-thought and long-reasoning judging lowered harmful self-preference
  [llm-self-preference-legitimacy]{13}. Model grading needs human calibration [anthropic-agent-evals]{7}.
- **Critics trade recall for false alarms.** Trained LLM critics caught more inserted bugs in short code than paid
  contractors, but hallucinated bugs and nitpicked far more; human-plus-critic teams hallucinated less than the
  critic alone without increasing comprehensiveness over it [llm-critics-catch-bugs]{17}. The authors describe a
  precision/recall tradeoff whose right balance "is not obvious" [llm-critics-catch-bugs]{17}. *(demonstrated, single
  vendor; short single-file code)*
- **Gap.** No fetched study isolates same-model versus different-model review of generated code, or of multi-file
  agent changes, as the single varied factor {inferred: aggregate}.

### One reviewer versus several

- In a randomized field experiment of 88 inspections, one-person teams were poorer than two- or four-person teams,
  two and four did not differ, and effort rose with total reviewers; the abstract nevertheless summarizes that the
  treatments "did not significantly influence the defect detection effectiveness"
  [inspection-team-size-experiment]{18}. *(demonstrated)*
- Across several organizations the median number of active reviewers was two, with "only a minimal increase" in
  comments and no extra rounds when more were active; larger reviewer sets arose when a change was judged high-risk
  after a round of review [convergent-peer-review-practices]{19}. At Google the median was one reviewer and more
  reviewers meant more comments [google-modern-code-review]{20}. Neither measures defects found.
- Low review participation was estimated to add up to five post-release defects in Qt-family projects
  [review-coverage-participation-defects]{21}, but an independent replication found review-measure effects unstable
  and models without review predictors fitting as well or better [review-measures-defects-replication]{22}.
  *(original demonstrated; replication independently measured)*
- Review finds more than defects: about 15% of review comments flag a possible defect, and comment usefulness rises
  with the reviewer's prior exposure to the code [code-reviews-do-not-find-bugs]{23}. *(documented, no methods)*

### Re-review after changes

- Repairing defects between two inspection sessions "had no effect on observed defect density" but sometimes
  lengthened the interval dramatically; very few inspections used that design [inspection-team-size-experiment]{18}.
  Over 80% of Google changes involved at most one iteration of resolving comments [google-modern-code-review]{20}.
- Google's reviewer guidance permits approval with unresolved comments when the reviewer is confident the author will
  address them, when the comments are optional, or when they are minor, and asks partial reviewers to say what they
  reviewed [google-review-speed-lgtm]{24}. *(documented)*
- GitHub can record the diff at approval and dismiss the approval as stale on any later diff change, or alternatively
  require the most recent push to be approved by someone other than its pusher; it calls dismissal safer against
  unapproved content being added after approval [github-stale-review-dismissal]{25}. *(designed, optional)*
- **Gap.** No fetched source measures defects introduced by post-approval edits, or compares re-review triggers
  {inferred: aggregate}.

## Question 2 — warning noise

### Developer response and delivery point

- At Facebook, a nightly batch list of 20-30 assigned issues was almost never acted on although the false-positive rate
  was believed to be below 20%; at diff time "the fix rate rocketed to over 70%" with "same false positive rate"
  [facebook-infer-zoncolan-scaling]{28}. *(demonstrated; before/after, uncontrolled)*
- Google reports that warnings shown at build time were ignored and that bug dashboards outside the workflow saw
  little use; checks moved to compiler errors or code review [google-static-analysis-lessons]{26}
  [google-tricorder-icse2015]{27}. *(documented)*
- Coverity describes a cycle in which low trust leads to complex true bugs being labelled false positives, and reports
  that "If people don't understand an error, they label it false" [coverity-billion-lines]{29}. Interviewed developers
  named false positives and the way warnings are presented as barriers, and asked for explanations, quick fixes and
  workflow integration [static-analysis-underuse-interviews]{30}. *(documented; independently measured perceptions)*

### Thresholds and definitions

- Google requires zero effective false positives for build-breaking checks and under 10% for code-review checks,
  where an effective false positive is a report developers did not act on; the 10% figure was "initially chosen ...
  somewhat arbitrarily" [google-static-analysis-lessons]{26}. Tricorder puts an analyzer on probation at a not-useful
  click rate of 10% or more and may turn it off above 25% [google-tricorder-icse2015]{27}. *(designed)*
- Coverity aims below 20% false positives for stable checkers and says more than 30% "easily cause problems"
  [coverity-billion-lines]{29}. Facebook defines a false positive as a report that "cannot happen" and tracks action
  rate instead [facebook-infer-zoncolan-scaling]{28}. A "99%" SOC false-positive figure turned out to be mostly benign
  triggers [soc-false-positive-alarms]{33}. These rates are not commensurable without restating their definitions
  {incommensurable: see Contradictions}.

### Non-blocking signals that are acted on

- Google's non-blocking review-time findings ran at about a 5% not-useful rate platform-wide
  [google-tricorder-icse2015]{27}, with over 5,000 "Please fix" clicks a day against 250 "Not useful" clicks
  [google-static-analysis-lessons]{26}. They are socially enforced: "Reviewers typically withhold approval of a change
  until all their comments, manual and automated, have been addressed" [google-static-analysis-lessons]{26}.
  *(demonstrated, builder-reported)*
- Clinical drug alerts are overridden in 49% to 96% of cases across studies [cpoe-alert-override-review]{34}, yet
  about 53% of outpatient overrides were judged appropriate on chart review
  [cds-outpatient-override-appropriateness]{35}. Non-action alone does not show lost attention.

### Practices associated with actionable advisories

Each practice is attested in at least one source; cross-domain support is composed.

| Practice | Evidence | Type |
| --- | --- | --- |
| Show findings on changed material at review time | [facebook-infer-zoncolan-scaling]{28} [google-static-analysis-lessons]{26} [google-tricorder-icse2015]{27} | demonstrated (builder) |
| Measure per-check action or not-useful rate; probation and removal of noisy checks | [google-tricorder-icse2015]{27} [google-static-analysis-lessons]{26} [facebook-infer-zoncolan-scaling]{28} | designed |
| Fix the message: 75% of bugs filed against one analyzer were wording misinterpretations | [google-tricorder-icse2015]{27} [coverity-billion-lines]{29} | demonstrated / documented |
| Tier by severity; non-interruptive low tier (29% vs 10% compliance; 100% vs 34% for the hard-stop tier) | [ddi-alert-tiering-compliance]{36} | demonstrated (observational) |
| Block only checks with effectively no false positives | [google-static-analysis-lessons]{26} | designed |
| Route lower-signal output to specialist queues | [facebook-infer-zoncolan-scaling]{28} [cpoe-alert-override-review]{34} | designed |
| Project-level suppression with recorded reasoning | [google-static-analysis-lessons]{26} [static-analysis-underuse-interviews]{30} [cpoe-alert-override-review]{34} | documented / perceptions |
| Cut repetition and per-encounter volume (acceptance fell about 30% per extra reminder per encounter) | [cds-alert-fatigue-repeats]{37} | independently measured |

## Cross-facet observations

- **A reviewer's false alarms are warning noise.** The critic study's hallucinated bugs and nitpicks
  [llm-critics-catch-bugs]{17} are, from the author's side, reports that will not be acted on — the effective
  false positives Google bounds for review-time checks [google-static-analysis-lessons]{26} `extends`. Adding a
  higher-recall reviewer therefore carries the noise costs documented for warnings
  [coverity-billion-lines]{29} {inferred: convergence}.
- **Grounded, explained output recurs on both sides.** Judge errors fell with reference grounding
  [llm-judge-mt-bench]{11} [llm-self-bias-refinement]{15}; warnings were dismissed when not understood
  [coverity-billion-lines]{29} and stopped drawing complaints when reworded [google-static-analysis-lessons]{26}
  {inferred: convergence}.
- **Context and familiarity matter in both.** Review comments grew more useful with reviewer familiarity
  [code-reviews-do-not-find-bugs]{23}; warnings were acted on when the author's context was "already swapped in"
  [facebook-infer-zoncolan-scaling]{28} {inferred: convergence}.

## Contradictions

| Relationship | Positions retained |
| --- | --- |
| qualifies | Self-preference read as bias without ground truth [llm-self-recognition-preference]{12}; mostly legitimate yet harmful when wrong with ground truth [llm-self-preference-legitimacy]{13}; undetermined in the MT-bench data [llm-judge-mt-bench]{11}. |
| tension | Disjoint-family panels reduce intra-model bias [llm-judge-panel-poll]{16}; rising error similarity could compromise jury independence [llm-judge-affinity-similarity]{14}. Neither tests the other's claim. |
| contradicts | On the same Qt data, lax review participation explains extra defects [review-coverage-participation-defects]{21}; review predictors add no fit [review-measures-defects-replication]{22}. |
| tension | Within one source, one-person inspections were poorer than two- or four-person ones, while the abstract reports no significant treatment effect [inspection-team-size-experiment]{18}. |
| tension | Median of two active reviewers with minimal added discussion [convergent-peer-review-practices]{19}; median of one, and more comments with more reviewers, at Google [google-modern-code-review]{20}. |
| tension | Google's static-analysis article says reviewers "typically withhold approval" until automated comments are addressed [google-static-analysis-lessons]{26}; Google's public reviewer guidance permits approval with unresolved comments under stated conditions [google-review-speed-lgtm]{24}. They may describe different comment kinds; the sources do not reconcile them. |
| tension | Tricorder: probation at a 10% not-useful rate, possible shut-off above 25% [google-tricorder-icse2015]{27}; the 2018 article: above 10% the analyzer is disabled until improved [google-static-analysis-lessons]{26}. |
| tension | Tricorder says its 10% matches Coverity [google-tricorder-icse2015]{27}; Coverity aims below 20% and flags more than 30% [coverity-billion-lines]{29}. |
| incommensurable | Effective false positive (no action) [google-static-analysis-lessons]{26}; "cannot happen" [facebook-infer-zoncolan-scaling]{28}; not-useful click ratio [google-tricorder-icse2015]{27}; override rate [cpoe-alert-override-review]{34}; benign triggers [soc-false-positive-alarms]{33}. |
| tension | Practitioner reports of eventual alarm desensitization [soc-false-positive-alarms]{33}; no time-based decline for newly deployed clinical alerts, with volume and repeat effects instead [cds-alert-fatigue-repeats]{37}. |

## Disconfirming analysis

- **Against keeping a different-model reviewer as the independence mechanism:** the similarity study shows a held-out
  model still favours similar models [llm-judge-affinity-similarity]{14}; stronger models' self-preference is mostly
  legitimate on verifiable tasks [llm-self-preference-legitimacy]{13}. Self-review is therefore not shown to be worse
  than cross-model review on generated code; what is shown is a measurable self-preference component and that
  grounding reduced judge errors.
- **Against heavier review:** two and four inspectors did not differ while effort rose
  [inspection-team-size-experiment]{18}; review measures lost explanatory power in replication
  [review-measures-defects-replication]{22}; critics with higher recall produced more false alarms
  [llm-critics-catch-bugs]{17}. For: one reviewer did worse than two [inspection-team-size-experiment]{18}, and a
  critic-assisted second review found substantial problems in 24% of flagged "flawless" items versus 6% unassisted
  [llm-critics-catch-bugs]{17}.
- **Against mandatory re-review on every change:** repair between sessions did not raise observed defect density
  [inspection-team-size-experiment]{18}, and documented practice lets approval stand over minor or trusted follow-ups
  [google-review-speed-lgtm]{24}. For: diff-tied dismissal exists because unapproved content can be added after
  approval [github-stale-review-dismissal]{25}. Neither side is measured.
- **Against "advisory warnings degrade":** non-blocking review-time findings were acted on at scale
  [google-static-analysis-lessons]{26} [google-tricorder-icse2015]{27}, and a median 36.7% of Coverity alerts in
  long-running open-source projects were fixed by code change [coverity-alert-actionability-oss]{31}
  {confidence: abstract-only}. Caveats: the Google findings are socially enforced at approval
  [google-static-analysis-lessons]{26}, and the counter-evidence is builder-reported.
- **For "noisy warnings get ignored":** build-time warnings and out-of-workflow dashboards were ignored
  [google-static-analysis-lessons]{26}; frequent pages lead to skimming and ignoring
  [sre-monitoring-distributed-systems]{32}; acceptance fell with volume and repeats [cds-alert-fatigue-repeats]{37}.
  The recurring condition is placement, volume and repetition rather than advisory status {inferred: aggregate}.

## Decision relevance

These are implications for methodology revisers, not measured effects of any particular workflow.

- **Cross-model review preference.** `extends`: the evidence supports keeping an independent check over pure
  self-review, but does not show that a different model is the active ingredient; grounding the review in executable
  checks, references or recorded criteria is more consistently associated with reduced judge error
  [llm-judge-mt-bench]{11} [llm-self-bias-refinement]{15} [llm-judge-affinity-similarity]{14}. A preference for a
  different model could be retained as a cheap reduction of the self-identity component while relying on grounded
  evidence for correctness.
- **Review weights.** `extends`: the human data support a step from zero or one reviewer to a second check more than
  adding further reviewers [inspection-team-size-experiment]{18} [convergent-peer-review-practices]{19}; scaling review
  to perceived risk is the documented practice [convergent-peer-review-practices]{19}. Reviewer false alarms have a
  cost [llm-critics-catch-bugs]{17}.
- **Covering-review reuse.** `extends`: whether an earlier review covers later changes is a policy choice in the
  sources — approval with explicit, bounded follow-ups [google-review-speed-lgtm]{24} versus diff-tied approval
  [github-stale-review-dismissal]{25}. Recording what a review covered, as Google's guidance asks of partial reviewers
  [google-review-speed-lgtm]{24}, is the attested mechanism that makes reuse checkable.
- **Citation advisories.** `extends`: the sources favour keeping advisories that are shown on changed material,
  explained, and measured for action, and removing or tiering checks whose non-action rate is high
  [google-tricorder-icse2015]{27} [facebook-infer-zoncolan-scaling]{28} [ddi-alert-tiering-compliance]{36}. Before a
  threshold is applied, the false-positive definition must be stated [google-static-analysis-lessons]{26}. Blocking is
  reserved for checks with effectively no false positives [google-static-analysis-lessons]{26}. A high dismissal rate
  can reflect correct dismissal [cds-outpatient-override-appropriateness]{35}.

## Limits

- No fetched study evaluates agent-to-agent review of multi-file changes, or warnings consumed by an automated agent.
- LLM-judge evidence concerns 2023-2025 models and short artifacts; the direction of change with newer models is
  uncertain [llm-judge-affinity-similarity]{14}.
- Human-review evidence is 1997-2020 and mostly observational; it measures comments or post-release defect counts
  rather than defects caught per review.
- Software warning evidence is mostly builder-reported; independent software evidence is one interview study and one
  abstract-only mining study. Clinical and SOC findings transfer only as analogy {inferred: aggregate}.
- No source validates a numeric threshold against adoption or abandonment outcomes.
- Cite-through prior work named inside sources (for example the FindBugs Fixit and RacerD reports, Bates et al.'s
  override-rate proposal) was not fetched.

## Revisit if

- A study compares same-model, different-family and human review of agent-generated multi-file changes against
  ground truth.
- Measured data appear on defects introduced after approval or on stale-approval dismissal outcomes.
- A controlled comparison of review-time versus batch, or blocking versus advisory, delivery of the same warnings is
  published.
- The full text of the Coverity open-source mining study is read [coverity-alert-actionability-oss]{31}.
- Evidence appears on advisories from documentation or prose linters.
