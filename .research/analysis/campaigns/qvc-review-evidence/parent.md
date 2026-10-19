---
title: Evidence on reviewer independence and warning noise
provenance: agent-synthesis
updated: 2026-10-19
summary: >
  Cross-facet synthesis on two questions about review and advisory controls for generated work. Same-model judging
  carries a measured self-preference that, with ground truth, is mostly legitimate for stronger models but more
  harmful when the judge is wrong; a different-model judge grading without references still favours similar
  models. In MT-bench's math-grading comparison (20 judgements per prompt), reference guidance cut judge failures most (14/20
  to 3/20) and chain-of-thought also cut them (to 6/20); chain-of-thought lowered harmful self-preference in another study; reference-based feedback reduced self-bias in another study. One
  randomized experiment found one-person inspections poorer than two- or four-person ones, though its abstract
  reports no significant treatment effect; no fetched source measures whether an earlier approval safely covers
  later changes. Noisy warnings are ignored when delivered outside the work context. Facebook reports diff-time
  findings, given to developers as part of code review, acted on at high rates (the source does not say whether
  they gate landing); Google reports low not-useful click ratios, which undercount ignoring, for review-time
  findings that reviewers typically enforce. False-positive thresholds are definition-specific.
key_findings:
  - "Self-preference in LLM judges is reported by several groups; with ground truth, stronger models' self-preference is mostly legitimate, but more harmful when they are wrong."
  - "A different-model judge grading without references still favours functionally similar models, so model identity is not independence; in MT-bench's comparison of default, chain-of-thought and reference-guided judge prompts (20 math judgements per prompt), reference guidance produced the largest reduction in judge failures and chain-of-thought also reduced them, and chain-of-thought lowered harmful self-preference in another study; panel diversity helped in one study."
  - "No fetched study isolates same-model versus different-model review of generated code as the single varied factor."
  - "In one randomized experiment one inspector did worse than two or four, which did not differ, though its abstract reports no significant treatment effect; effort rose with reviewer count. Links between review participation and later defects were unstable and added no model fit in an independent replication."
  - "Re-review after changes is governed by documented or designed policy (approve-with-comments; diff-tied approval dismissal); no fetched source measures post-approval defect introduction."
  - "At an unchanged estimated false-positive rate, moving one analysis from a nightly batch list to diff time moved its fix rate from near zero to over 70% (uncontrolled); a Google code-review integration of FindBugs was still discontinued over effective false positives and inconsistent per-user customization."
  - "Published thresholds (zero effective false positives to block; under 10% for review-time checks; probation at a 10% not-useful rate) are defined by developer action, not report correctness, and were not validated against outcomes."
  - "Override or non-action is not by itself degradation: on average about half of outpatient alert overrides were judged appropriate (12% to 92% by alert type)."
---

# Evidence on reviewer independence and warning noise

## Question and sample

Two questions:

1. **Reviewer independence.** What evidence bears on same-model versus different-model or human review of
   generated work, on one reviewer versus several, and on re-review after changes?
2. **Warning noise.** How do people respond to advisory warnings with high false-positive rates, and what keeps
   advisory signals actionable?

The sample has 27 newly attested sources plus one reused attestation: for Question 1, seven LLM-evaluation papers
(2023-2025), five inspection and code-review studies (1997-2020), a talk abstract and two practitioner documents; for
Question 2, four industrial static-analysis reports, an interview study, a mining study read only as an abstract
[coverity-alert-actionability-oss]{31} {confidence: abstract-only}, an SRE chapter, a SOC study and four clinical
decision-support studies. Many were read as main text without appendices or figure values.

Evidence-type labels: **designed** (intended or configurable behaviour), **documented** (an organization describes
its practice), **demonstrated** (the authors' own experiment or deployment data), **independently measured**
(replication, third-party measurement or aggregation of others' measurements).

## Question 1 — reviewer independence

### Same-model versus different-model judging

- **Agreement with humans rises with the gap between compared models.** GPT-4's non-tie agreement with expert humans
  was 85% against 81% among humans, rising from about 70% to nearly 100% as the performance gap between the compared
  models widened
  [llm-judge-mt-bench]{11}. *(demonstrated)*
- **Self-preference is measured but its harm is conditional.** In pairwise comparisons GPT-3.5, GPT-4 and Llama 2
  favoured their own summaries (Llama not in individual scoring), tracking self-recognition; the authors claim
  evidence toward, not validation of, a causal link, without ground-truth control
  [llm-self-recognition-preference]{12}. Self-bias was present in all six models of a self-refinement study and
  amplified over iterations [llm-self-bias-refinement]{15}. The MT-bench authors saw GPT-4 and Claude-v1, but not GPT-3.5,
  favour themselves and could not determine whether the bias exists [llm-judge-mt-bench]{11}. On verifiable tasks, stronger models'
  self-preference mostly matched better outputs, but rose when the judge was wrong: Qwen2.5-72B's harmful
  self-preference propensity was 86 on MATH500 against an overall ratio of 55 [llm-self-preference-legitimacy]{13}.
  *(demonstrated; convergent across groups {inferred: convergence})*
- **Model identity is not independence.** Judges grading without ground-truth solutions favoured models whose mistakes
  resemble their own after controlling for accuracy; the authors argue it "is not sufficient to just use a held-out LM
  as the judge" and report mistakes becoming more similar with capability [llm-judge-affinity-similarity]{14}.
  *(demonstrated)*
- **Diversity helped in one panel study.** A three-family panel agreed with human judgements better than a single
  GPT-4 judge on QA (Cohen's kappa 0.763 vs 0.627 on NQ) at seven to eight times lower cost, and each judged model
  received its largest favourable deviation when judged by itself. The panel did not beat every single judge on every
  dataset, three settings were tested, the authors hypothesise GPT-4 was "over-reasoning", and it improved with
  prompt changes, and the authors work for the vendor of one panel member [llm-judge-panel-poll]{16}.
  *(demonstrated, single group)*
- **Reference guidance gave the largest reduction in MT-bench's judge-prompt comparison.** On 10 math questions (one
  model pair, positions swapped: 20 judgements per prompt), GPT-4 judged an incorrect answer correct 14/20 times with
  the default prompt, 6/20 with chain-of-thought and 3/20 with a reference-guided prompt; even with chain-of-thought
  the judge "in many cases ... makes exactly the same mistake as the given answers" [llm-judge-mt-bench]{11}.
  Reference-based feedback the authors treat as oracle feedback reduced self-bias [llm-self-bias-refinement]{15}, and
  chain-of-thought and long-reasoning judging lowered harmful self-preference [llm-self-preference-legitimacy]{13}.
  *(demonstrated; the prompt comparison is 20 judgements per condition)* Design guidance adds that model grading
  needs human calibration [anthropic-agent-evals]{7}.
- **Critics trade recall for false alarms.** Trained LLM critics caught more inserted bugs in short code than paid
  contractors but hallucinated and nitpicked far more; human-plus-critic teams hallucinated less than the critic alone
  without being more comprehensive, and the right precision/recall balance "is not obvious"
  [llm-critics-catch-bugs]{17}. *(demonstrated, single vendor; short single-file code)*
- **Gap.** No fetched study isolates same-model versus different-model review of generated code, or of multi-file
  agent changes, as the single varied factor {inferred: aggregate}.

### One reviewer versus several

- In a randomized field experiment of 88 inspections, one-person teams were poorer than two- or four-person teams
  (the one-person single-session treatment was discontinued as ineffective), two and four did not differ, and effort
  rose with total reviewers; yet the abstract says the treatments "did not significantly influence the defect
  detection effectiveness", and the summary list says "Increasing team size does not always improve performance"
  [inspection-team-size-experiment]{18}. *(demonstrated; one experiment)*
- Across several organizations the median number of active reviewers was two, with "only a minimal increase" in
  comments and no extra rounds when more were active; larger reviewer sets arose when a change was judged high-risk
  after a round of review [convergent-peer-review-practices]{19}. At Google the median was one reviewer and more
  reviewers meant more comments [google-modern-code-review]{20}. Neither measures defects found.
- Components with lax review participation were estimated to carry up to five additional post-release defects in the
  studied Qt, VTK and ITK releases [review-coverage-participation-defects]{21}; a replication on the Qt data and Chrome
  found review-measure effects unstable, with models without review predictors fitting as well or better
  [review-measures-defects-replication]{22}. *(original demonstrated; replication independently measured)*
- About 15% of review comments flag a possible defect, usefulness rises with the reviewer's prior exposure to the
  code, and effective reviews are posited to need "people with specific set of skills"
  [code-reviews-do-not-find-bugs]{23} *(documented, no methods)*; the replication attributes to Porter et al. that "the
  best predictor was the level of expertise of the reviewers" [review-measures-defects-replication]{22}.

### Re-review after changes

- Repairing defects between two inspection sessions "had no effect on observed defect density" but sometimes
  lengthened the interval dramatically; a section-level analysis found repair helped two-person but not one-person
  teams, to be "viewed with caution" given few such inspections [inspection-team-size-experiment]{18}. Both arms
  include a second inspection, so this does not measure defects introduced by changes after a review `extends`. Over
  80% of Google changes involved at most one iteration of resolving comments [google-modern-code-review]{20}.
- Google's reviewer guidance permits approval with unresolved comments when the reviewer is confident the author will
  address them, when the comments are optional, or when they are minor, and asks partial reviewers to say what they
  reviewed [google-review-speed-lgtm]{24}. *(documented)*
- GitHub records the diff at approval and can dismiss the approval as stale on any later diff change, or instead
  require the latest push to be approved by a non-pusher; it calls dismissal safer against unapproved content added
  after approval [github-stale-review-dismissal]{25}. *(designed, optional)*
- **Gap.** No fetched source measures defects introduced by post-approval edits, or compares re-review triggers
  {inferred: aggregate}.

## Question 2 — warning noise

### Developer response and delivery point

- At Facebook, a nightly batch list of 20-30 assigned issues was almost never acted on although the false-positive rate
  was believed to be below 20%; at diff time "the fix rate rocketed to over 70%" with "same false positive rate"
  [facebook-infer-zoncolan-scaling]{28}. *(demonstrated; before/after, uncontrolled)*
- Google reports that warnings shown at build time were ignored and that bug dashboards outside the workflow saw
  little use; checks moved to compiler errors or code review [google-static-analysis-lessons]{26}
  [google-tricorder-icse2015]{27}. An earlier FindBugs integration that posted review comments was discontinued because
  "the presence of effective false positives caused developers to lose confidence in the tool" and per-user
  customization gave inconsistent views [google-static-analysis-lessons]{26}. *(documented)*
- Coverity reports that low trust gets complex true bugs labelled false positives: "If people don't understand an
  error, they label it false" [coverity-billion-lines]{29}. Interviewed developers named false positives and warning
  presentation as barriers and asked for explanations, quick fixes and workflow integration
  [static-analysis-underuse-interviews]{30}. *(documented; independently measured perceptions)*

### Thresholds and definitions

- Google requires zero effective false positives for build-breaking checks and under 10% for code-review checks,
  where an effective false positive is a report developers did not act on; the 10% figure was "initially chosen ...
  somewhat arbitrarily", though it "seems to be a sweet spot for developer satisfaction"
  [google-static-analysis-lessons]{26}. Tricorder puts an analyzer on probation at a not-useful click rate of 10% or
  more and may turn it off above 25% [google-tricorder-icse2015]{27}. *(designed)*
- Coverity aims below 20% false positives for stable checkers and says more than 30% "easily cause problems"
  [coverity-billion-lines]{29}. Facebook defines a false positive as a report that "cannot happen" and tracks action
  rate instead [facebook-infer-zoncolan-scaling]{28}. A "99%" SOC false-positive figure turned out to be mostly benign
  triggers [soc-false-positive-alarms]{33}. These rates are not commensurable without restating their definitions
  {incommensurable: see Contradictions}.

### Review-time findings outside the commit gate, and justified non-action

- Google's review-time findings appear in the code-review tool rather than blocking commits, which some teams request
  for checks with no false positives [google-static-analysis-lessons]{26}, but they are not purely advisory (see the
  enforcement quote below). They ran at about a 5% not-useful click ratio platform-wide
  [google-tricorder-icse2015]{27}, with over 5,000 "Please fix" clicks a day against 250 "Not useful" clicks
  [google-static-analysis-lessons]{26}. The ratio undercounts both sides: fix clicks "are known to be low", "Developers
  may ignore findings they do not plan to fix, rather than clicking NOT USEFUL", and views cannot be measured
  [google-tricorder-icse2015]{27}. They are socially enforced: "Reviewers typically withhold approval of a change until
  all their comments, manual and automated, have been addressed" [google-static-analysis-lessons]{26}.
  *(demonstrated, builder-reported)*
- Clinical drug alerts are overridden in 49% to 96% of cases across studies, apart from serious overdose alerts, and
  "Alert overriding may often be justified" [cpoe-alert-override-review]{34}; on chart review an average of 53% of
  outpatient overrides were appropriate, from 12% (renal, drug-drug interaction) to 92% (allergy)
  [cds-outpatient-override-appropriateness]{35}. Non-action alone does not show lost attention.

### Practices associated with actionable advisories

Each practice is attested in at least one source; cross-domain support is composed.

| Practice | Evidence | Type |
| --- | --- | --- |
| Show findings on changed material at review time | [facebook-infer-zoncolan-scaling]{28} [google-static-analysis-lessons]{26} [google-tricorder-icse2015]{27} | demonstrated (builder) |
| Measure per-check action or not-useful rate; probation and removal of noisy checks | [google-tricorder-icse2015]{27} [google-static-analysis-lessons]{26} [facebook-infer-zoncolan-scaling]{28} | designed |
| Fix the message: 75% of bugs filed against one analyzer were wording misinterpretations | [google-tricorder-icse2015]{27} [coverity-billion-lines]{29} | demonstrated / documented |
| Tier by severity, interrupting only for serious tiers (alert compliance, tiered site vs non-tiered site: overall 29% vs 10%; interruptive Level 2 29% vs 11%; Level 1 100% by hard-stop design vs 34%; information-only Level 3 not collected at the tiered site) | [ddi-alert-tiering-compliance]{36} | demonstrated (observational, retrospective logs at two hospitals in one delivery system); advisory-tier effect indirect |
| Block only checks with effectively no false positives | [google-static-analysis-lessons]{26} | designed |
| Route lower-signal output to specialist queues | [facebook-infer-zoncolan-scaling]{28} [cpoe-alert-override-review]{34} | designed |
| Project-level suppression with recorded reasoning | [google-static-analysis-lessons]{26} [static-analysis-underuse-interviews]{30} [cpoe-alert-override-review]{34} | documented / perceptions |
| Cut repetition and per-encounter volume (acceptance fell about 30% per extra reminder per encounter) | [cds-alert-fatigue-repeats]{37} | independently measured (observational, retrospective cohort of clinicians using one commercial EHR) |

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
| tension | On the same Qt data, lax participation is estimated to add defects [review-coverage-participation-defects]{21}; the replication finds Qt review measures "similar to what McIntosh et al. found" but unstable and adding no fit [review-measures-defects-replication]{22}. The dispute is over explanatory power. |
| tension | Within one source, one-person inspections were poorer than two- or four-person ones, while the abstract reports no significant treatment effect [inspection-team-size-experiment]{18}. |
| tension | Median of two active reviewers with minimal added discussion [convergent-peer-review-practices]{19}; median of one, and more comments with more reviewers, at Google [google-modern-code-review]{20}. |
| tension | Reviewers "typically withhold approval" until automated comments are addressed [google-static-analysis-lessons]{26}; Google's reviewer guidance permits approval with unresolved comments under stated conditions [google-review-speed-lgtm]{24}. Unreconciled; they may concern different comment kinds. |
| tension | Tricorder: probation at a 10% not-useful rate, possible shut-off above 25% [google-tricorder-icse2015]{27}; the 2018 article: above 10% the analyzer is disabled until improved [google-static-analysis-lessons]{26}. |
| tension | Tricorder says its 10% matches Coverity [google-tricorder-icse2015]{27}; Coverity aims below 20% and flags more than 30% [coverity-billion-lines]{29}. |
| incommensurable | Effective false positive (no action) [google-static-analysis-lessons]{26}; "cannot happen" [facebook-infer-zoncolan-scaling]{28}; not-useful click ratio [google-tricorder-icse2015]{27}; override rate [cpoe-alert-override-review]{34}; benign triggers [soc-false-positive-alarms]{33}. |
| tension | Practitioner reports of eventual alarm desensitization [soc-false-positive-alarms]{33}; no time-based decline for newly deployed clinical alerts, with volume and repeat effects instead [cds-alert-fatigue-repeats]{37}. |
| tension | No relationship between relative alert amount and override percentage, possibly from few studies [cpoe-alert-override-review]{34}; acceptance falling with reminders per encounter, the cohort itself noting the earlier null [cds-alert-fatigue-repeats]{37}. |
| qualifies | Batch lists and out-of-workflow dashboards went unused by general developers [facebook-infer-zoncolan-scaling]{28} [google-static-analysis-lessons]{26}; security engineers triage Zoncolan's master analysis by dashboard [facebook-infer-zoncolan-scaling]{28}, a code-search layer serves teams with "a dedicated cleanup team" [google-tricorder-icse2015]{27}, and SRE favours a dashboard for subcritical problems [sre-monitoring-distributed-systems]{32}. |

## Disconfirming analysis

- **Against keeping a different-model reviewer as the independence mechanism:** the similarity study shows a held-out
  model still favours similar models [llm-judge-affinity-similarity]{14}; stronger models' self-preference is mostly
  legitimate on verifiable tasks [llm-self-preference-legitimacy]{13}. Self-review is therefore not shown to be worse
  than cross-model review on generated code; what is shown is a measurable self-preference component and that
  reference grounding reduced judge errors, as did chain-of-thought judging, by less, in MT-bench's prompt comparison
  [llm-judge-mt-bench]{11}.
- **Against heavier review:** two and four inspectors did not differ while effort rose
  [inspection-team-size-experiment]{18}; review measures lost explanatory power in replication
  [review-measures-defects-replication]{22}; critics with higher recall produced more false alarms
  [llm-critics-catch-bugs]{17}. For: one reviewer did worse than two, though the abstract reports no significant
  effect [inspection-team-size-experiment]{18}; and among "flawless"-rated completions where a critic flagged a
  problem, critique-assisted contractors found a substantial problem in 24%, while in a separate replication without
  critiques a second contractor rated "flawless" completions similarly poorly 6% of the time; the denominators differ
  [llm-critics-catch-bugs]{17}.
- **Against mandatory re-review on every change:** documented practice lets approval stand over minor or trusted
  follow-ups [google-review-speed-lgtm]{24}. For: diff-tied dismissal exists because unapproved content can be added
  after approval [github-stale-review-dismissal]{25}. Neither side is measured; the repair-between-sessions result does
  not test changes after approval (see Re-review after changes).
- **Against "advisory warnings degrade":** Facebook's diff-time reports, given to developers as part of code review,
  were fixed at over 70% [facebook-infer-zoncolan-scaling]{28}; Google's review-time findings drew low not-useful click ratios and thousands
  of fix requests a day [google-static-analysis-lessons]{26} [google-tricorder-icse2015]{27}; a median 36.7% of
  Coverity alerts in long-running open-source projects were fixed by code change, delivery mode not stated
  [coverity-alert-actionability-oss]{31} {confidence: abstract-only}. Caveats: the Facebook source does not say
  whether those diff-time reports gate landing, and at diff time the security on-call can block a diff over a
  Zoncolan alarm [facebook-infer-zoncolan-scaling]{28}; the Google findings are socially enforced at approval
  [google-static-analysis-lessons]{26} and their click ratios undercount ignoring [google-tricorder-icse2015]{27}; the
  counter-evidence is builder-reported; and Google's earlier FindBugs review integration was discontinued over
  effective false positives and inconsistent per-user customization [google-static-analysis-lessons]{26}.
- **For "noisy warnings get ignored":** build-time warnings and out-of-workflow dashboards were ignored
  [google-static-analysis-lessons]{26}; frequent pages lead to skimming and ignoring
  [sre-monitoring-distributed-systems]{32}; acceptance fell with volume and repeats [cds-alert-fatigue-repeats]{37},
  though an earlier review found no volume-override relationship [cpoe-alert-override-review]{34}. Placement, volume and
  repetition recur more than advisory status where degradation is reported {inferred: aggregate}; dashboards still
  served specialist audiences (see Contradictions).

## Decision relevance

These are implications for methodology revisers, not measured effects of any particular workflow.

- **Cross-model review preference.** `extends`: the evidence supports keeping an independent check over pure
  self-review, but does not show that a different model is the active ingredient: a held-out judge grading without
  references still favoured similar models [llm-judge-affinity-similarity]{14}. In MT-bench's comparison of judge
  prompts (20 math judgements each), reference guidance produced the largest reduction in judge error and
  chain-of-thought judging also reduced it [llm-judge-mt-bench]{11}; chain-of-thought and long-reasoning judging
  lowered harmful self-preference [llm-self-preference-legitimacy]{13}; and reference-based feedback reduced self-bias [llm-self-bias-refinement]{15};
  extending this to executable checks or recorded criteria is untested. A different-model preference could be
  retained to avoid self-judging, which gave each model its largest favourable deviation in one panel study
  [llm-judge-panel-poll]{16}, while relying on grounded evidence for correctness. On simplifying versus strengthening
  {inferred: aggregate}: simplifying to same-model review would drop the guard against a measured self-preference
  component [llm-self-recognition-preference]{12} [llm-self-bias-refinement]{15}, though stronger models'
  self-preference is mostly legitimate on verifiable tasks [llm-self-preference-legitimacy]{13}; keeping a different
  but ungrounded model does not remove similarity bias [llm-judge-affinity-similarity]{14}; strengthening has attested
  gains from reference grounding [llm-judge-mt-bench]{11} [llm-self-bias-refinement]{15} and, in one study, from a
  diverse panel at lower cost than a single GPT-4 judge [llm-judge-panel-poll]{16}. No fetched source measures either
  option on generated code.
- **Review weights.** `extends`: in this sample, defect evidence on reviewer count comes from one experiment in which two
  inspectors beat one and four added effort without gain, while its abstract reports no significant effect
  [inspection-team-size-experiment]{18}; the median of two active reviewers is practice, not defect measurement
  [convergent-peer-review-practices]{19}. Reviewer count is commonly varied with perceived risk, complexity or change
  size [convergent-peer-review-practices]{19} [google-modern-code-review]{20}, and reviewer expertise and familiarity
  are reported as mattering (a cite-through of Porter et al. [review-measures-defects-replication]{22}; a posit and
  familiarity data without methods [code-reviews-do-not-find-bugs]{23}). Reviewer
  false alarms have a cost [llm-critics-catch-bugs]{17}.
- **Covering-review reuse.** `extends`: whether an earlier review covers later changes is a policy choice in the
  sources — approval with explicit, bounded follow-ups [google-review-speed-lgtm]{24} versus diff-tied approval
  [github-stale-review-dismissal]{25}. Two recording mechanisms are attested — GitHub's recorded diff at approval
  [github-stale-review-dismissal]{25} and Google's request that partial reviewers note what they reviewed
  [google-review-speed-lgtm]{24}; using either to make reuse checkable is an application.
- **Citation advisories.** `extends`: the sources favour keeping advisories that are shown on changed material,
  explained, and measured for action, removing checks whose non-action rate is high [google-tricorder-icse2015]{27}, and tiering alerts by severity [ddi-alert-tiering-compliance]{36}. That
  evidence is builder-reported; Google's review-time findings are typically enforced before approval and measured by
  click ratios that undercount ignoring [google-static-analysis-lessons]{26} [google-tricorder-icse2015]{27}; an earlier
  review-time integration was discontinued over effective false positives and per-user customization
  [google-static-analysis-lessons]{26}; Facebook's source does not say whether its diff-time reports gate landing
  [facebook-infer-zoncolan-scaling]{28}; and the tiering gain was measured on interruptive tiers, so the advisory-tier
  benefit is indirect [ddi-alert-tiering-compliance]{36}. Before a threshold is applied, the false-positive definition
  must be stated {inferred: aggregate} (see the `incommensurable` row in Contradictions). Blocking is reserved for
  checks with effectively no false positives [google-static-analysis-lessons]{26}. A high dismissal rate can reflect
  correct dismissal [cds-outpatient-override-appropriateness]{35}, and specialist queues are an alternative to
  suppression (routing is attested; see the practice table and Contradictions).

## Limits

- No fetched study evaluates agent-to-agent review of multi-file changes, or warnings consumed by an automated agent.
- LLM-judge evidence concerns 2023-2025 models and short artifacts; the direction of change with newer models is
  uncertain [llm-judge-affinity-similarity]{14}.
- Human-review evidence is 1997-2020 and observational except for one inspection experiment measuring observed defect
  density; the rest measures comments, practice or post-release defects, not defects caught per review.
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

## Revisions

- 2026-10-19 — Correction (position preserved) after adversarial read: restored stripped source qualifiers, separated
  chain-of-thought from reference grounding, re-scoped decision-bullet citations, and added three Contradictions rows;
  see `verification-checklist.md`, "Revision response (2026-10-19)".
- 2026-10-19 — Correction (position preserved), bounded pass after the adversarial re-read: the MT-bench attestation
  was extended with Table 4 first, then chain-of-thought is stated as also reducing judge failures (14/20 default,
  6/20 chain-of-thought, 3/20 reference; 20 judgements) and the chain-of-thought `qualifies` row was removed because
  the source does not diverge; "non-blocking" was removed for Facebook's diff-time findings, with a gating caveat
  beside the Google caveats; the second FindBugs reason, the Porter cite-through, the tiering criterion and arms, the
  composed threshold rule, the model-gap wording and evidence labels were corrected; the summary was aligned with the
  key findings and a simplify-versus-strengthen sentence added; see `verification-checklist.md`, "Bounded correction
  response (2026-10-19)".
- 2026-10-19 (lead spot-check correction): N3 from the targeted re-check — the "one study comparing judge prompts"
  exclusivity was scoped to MT-bench's default/chain-of-thought/reference comparison, the chain-of-thought result on
  harmful self-preference [llm-self-preference-legitimacy]{13} restored where it had been omitted, "20 judgements"
  stated per prompt, and the Facebook citation removed from "removing checks" (its attestation describes filtering, not
  removal). See `verification-checklist.md`, "Lead spot-check (2026-10-19)".
