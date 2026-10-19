---
title: Reviewer independence, reviewer count and re-review after changes
provenance: agent-synthesis
updated: 2026-10-19
summary: LLM judges measurably favour their own and similar models' outputs, but much of that preference tracks real quality, and reference-based feedback reduced it; diverse panels and human-plus-model teams show bounded gains in single-group studies. One randomized inspection experiment finds one reviewer weaker than two and little gain from two to four, though its abstract reports no significant treatment effect; links between review measures and later defects are weak or unstable. No fetched source measures defects introduced by changes made after an approval; re-review rules found are documented or designed policies.
key_findings:
  - Judge favouritism toward a judge's own (and functionally similar) outputs is reported by several independent groups across tasks; a ground-truth study finds stronger models' self-preference mostly legitimate yet more harmful when they are wrong.
  - Switching to a different model does not remove correlated-judgement risk; a similarity study finds judges grading without references favour functionally similar models, and model errors growing more alike with capability.
  - Reference grounding (a reference answer or reference-based oracle feedback) is associated with reduced judge error; in MT-bench's comparison of default, chain-of-thought and reference-guided judge prompts (10 math questions, 20 judgements per prompt), a reference-guided judge cut failures most (14/20 default to 3/20) and a chain-of-thought judge also cut them (to 6/20), and chain-of-thought and long-reasoning judging lowered harmful self-preference in another study. Model identity alone was not the varied factor in most studies. No fetched study gave judges executable tests.
  - A randomized inspection experiment found one-person teams poorer than two- or four-person teams and no difference between two and four, with effort rising with reviewer count; its abstract reports no significant treatment effects on effectiveness overall.
  - Practice data show a median of two reviewers in several organizations and a median of one at Google; observational links between review participation and post-release defects did not hold up robustly in an independent replication.
  - Re-review after changes is governed by documented policy (approval with comments for minor follow-ups; optional dismissal of stale approvals on any diff change), not by measured outcomes in the fetched sources.
---

# Reviewer independence, reviewer count and re-review after changes

## Question and sample

What evidence bears on (a) same-model versus different-model or human review of generated work,
(b) one reviewer versus several, and (c) whether a completed review should be repeated after later
changes? The sample is 15 newly attested sources plus one reused attestation: seven LLM-evaluation
papers (2023-2025 arXiv versions, read as full or near-full text via arXiv HTML), five empirical
software-engineering studies of inspection and code review (1997-2020), one two-page industry talk
abstract, and two practitioner documents (Google's public review guidelines; GitHub branch-protection
documentation). Each finding is labelled by evidence type:

- **designed** — a system's intended or configurable behaviour;
- **documented** — an organization describes its own practice;
- **demonstrated** — the authors' own experiment or analysis;
- **independently measured** — replication or measurement by a party other than the original authors.

Most LLM results concern 2023-2025 models and short, single-turn artifacts (chat answers, summaries,
QA, short code snippets); none studies multi-file agent-generated changes reviewed by another agent.

## LLM-judge bias and agreement with humans

**Agreement with humans.** On MT-bench, GPT-4's non-tie agreement with 58 expert human labelers
reached 85%, above the 81% agreement among the humans themselves; agreement rose from about 70% to
nearly 100% as the performance gap between the compared models widened [llm-judge-mt-bench]{11}. The
same study found GPT-4 could misgrade basic math it could solve, being influenced by the answers under
review, and that a reference-guided judge (answer first, then grade against that reference) cut the
math-grading failure rate from 70% to 15% (14/20 to 3/20 judgements on 10 math questions, one model pair
with positions swapped), with a chain-of-thought judge at 6/20 [llm-judge-mt-bench]{11}. Model grading is nondeterministic
and needs human calibration [anthropic-agent-evals]{7}. *(demonstrated; 2023 judges, chat tasks.)*

**Self-preference.** The MT-bench study observed GPT-4 favouring itself with a 10% higher win rate and
Claude-v1 with a 25% higher win rate relative to humans, but GPT-3.5 did not favour itself and the
authors state they "cannot determine" whether a self-enhancement bias exists [llm-judge-mt-bench]{11}.
On news summarization, GPT-3.5, GPT-4 and Llama 2 disproportionately favoured their own summaries,
and self-preference strength correlated linearly with the model's ability to recognize its own text;
the authors say this provides evidence toward, not validation of, a causal link, and that they did not
control for ground-truth quality [llm-self-recognition-preference]{12}. *(demonstrated.)*

**Legitimate versus harmful self-preference.** Using verifiable tasks (MATH500, MMLU, MBPP+ code), a
2025 study found that stronger models' self-preference mostly coincides with their outputs actually
being better, but that when the judge's own answer is wrong and the alternative is right, stronger
models prefer themselves more: Qwen2.5-72B showed harmful self-preference propensity of 86 on MATH500
versus an overall self-preference ratio of 55; on MBPP+ large models ranged from about 50 to 75 against
overall ratios below 40 [llm-self-preference-legitimacy]{13}. Chain-of-thought judging lowered harmful
self-preference, and long chain-of-thought reasoning models lowered it further, across the models tested
[llm-self-preference-legitimacy]{13}. In MT-bench math grading, a chain-of-thought judge also cut failures (6/20
against 14/20 with the default prompt), though less than a reference-guided judge (3/20), and in many cases still
"makes exactly the same mistake as the given answers" [llm-judge-mt-bench]{11}.
*(demonstrated; this study shares an author with the summarization study, so it is not fully
independent of it.)*

**Similarity, not only identity.** A 2025 study of nine open-weight judges, grading without access to
ground-truth solutions, found judge scores favour models whose mistakes resemble the judge's own, after
controlling for accuracy; for example, a
Qwen2.5-72B judge scored Qwen2.5-7B 71% correct but the more accurate Llama-3.1-70B 67%
[llm-judge-affinity-similarity]{14}. The authors argue it "is not sufficient to just use a held-out LM
as the judge", report model mistakes becoming more similar as capability increases, and warn this could
undermine juries "by compromising independence" [llm-judge-affinity-similarity]{14}. *(demonstrated.)*

**Self-refinement loops.** Across six models and three task types, self-bias was present in all models
examined and was amplified over iterative self-refinement, with self-estimated improvement outpacing
true improvement; feedback from a reference-based model the authors treat as an oracle reduced the bias
and produced real gains [llm-self-bias-refinement]{15}. The "external" feedback here had reference access,
so the result supports grounded feedback rather than a different ungrounded model
`extends`.

Taken together, judge favouritism toward the judge's own outputs is reported by separate groups on
chat, summarization, QA, translation and math tasks
[llm-judge-mt-bench]{11} [llm-self-recognition-preference]{12} [llm-self-bias-refinement]{15}
[llm-judge-affinity-similarity]{14} {inferred: convergence}. That convergence is the closest this sample
comes to **independently measured** evidence for the LLM-judge findings; its size and harm are
contested by the ground-truth study [llm-self-preference-legitimacy]{13}.

## Independence and defect detection

**Diverse panels.** A three-model panel from three disjoint families (Command R, Claude Haiku, GPT-3.5)
agreed with human judgements better overall than a single GPT-4 judge on QA tasks (Cohen's kappa 0.763
vs 0.627 on NQ) and tracked Chatbot Arena rankings better (Pearson 0.917 vs 0.817), at seven to eight
times lower cost [llm-judge-panel-poll]{16}. Each scored model received its largest favourable deviation
from human judgement when judged by itself [llm-judge-panel-poll]{16}. The panel was not uniformly
better than every single judge (Haiku 0.873 vs panel 0.867 on HotPotQA), the authors tested three
settings only and left math and reasoning untested, and the authors are employed by the vendor of one
panel member [llm-judge-panel-poll]{16}. *(demonstrated; single group.)*

**Model critics versus human reviewers on code.** RLHF-trained LLM critics caught many more
human-inserted bugs than experienced contractors who spent a median of about fifty minutes per example,
and model critiques were preferred over human ones in 63% of cases on naturally occurring errors
[llm-critics-catch-bugs]{17}. Models hallucinated bugs and nitpicked far more than humans;
human-plus-critic teams hallucinated less than the critic alone but did not increase comprehensiveness
over it [llm-critics-catch-bugs]{17}. Among training completions a first annotator had rated "flawless"
and a sampled critique flagged, critique-assisted contractors found a substantial problem in 24% of cases; in a
separate replication without critiques, a second contractor rated "flawless" completions similarly poorly 6% of the
time. The denominators differ [llm-critics-catch-bugs]{17}. The
code was short and single-file, and inserted bugs differ from natural model errors
[llm-critics-catch-bugs]{17}. *(demonstrated; single vendor.)*

**What the independence evidence does and does not show.** The detection improvements in this sample
came from adding a differently-informed check: a reference answer [llm-judge-mt-bench]{11}, reference-based
oracle feedback [llm-self-bias-refinement]{15}, heterogeneous model families [llm-judge-panel-poll]{16}, or a
trained critic plus a human [llm-critics-catch-bugs]{17}. Longer judge reasoning adds no external reference; it
lowered harmful self-preference [llm-self-preference-legitimacy]{13} and cut math-grading failures, by less than a
reference answer did and with graded answers' mistakes still repeated in many cases [llm-judge-mt-bench]{11}
{inferred: aggregate}. No fetched study isolates "same model versus
different model" as the single varied factor on review of generated code; the panel study varies family
and count together, and the critic study varies training and human assistance
{inferred: aggregate}.

## Human code review: reviewer count

**Randomized inspection experiment.** In 88 inspections on a live Lucent compiler project, teams of one,
two or four reviewers were randomly assigned. In the detailed analysis, two- and four-person teams did not
differ, both outperformed one-person teams, and the one-person single-session treatment was discontinued
as ineffective; effort rose with total reviewers [inspection-team-size-experiment]{18}. The abstract,
however, summarizes that the treatments "did not significantly influence the defect detection
effectiveness" [inspection-team-size-experiment]{18}. Effectiveness was observed defect density because
true defect content was unknowable, and severity was not weighted [inspection-team-size-experiment]{18}.
*(demonstrated.)*

**Practice data.** Across Android, Chrome, AMD and three Microsoft products, the median number of
active reviewers was two, even where three or four were invited; alongside the Microsoft data the authors
report "only a minimal increase" in comments and no increase in review rounds when more reviewers were active; the "two reviewers find an
optimal number of defects" practice is attributed to the inspection literature rather than measured here
[convergent-peer-review-practices]{19}. Larger review sets arose when someone judged a change high-risk
after a round of review [convergent-peer-review-practices]{19}. At Google, the median reviewer count was
one, fewer than 25% of changes had more than one reviewer, and — unlike the earlier report — more
reviewers meant more comments per change [google-modern-code-review]{20}. Neither study reports defects
found by reviewer count. *(practice measured from logs; the Google figures are in-house.)*

**Review participation and later defects.** In Qt, VTK and ITK, components with low review
participation (many self-approved, hasty, or undiscussed changes) were estimated to carry up to five
additional post-release defects, while review coverage was significant in only two of four releases
[review-coverage-participation-defects]{21}. An independent replication on the original Qt data and on
Chrome found review-measure effects unstable and sensitive to variable selection; models without review
predictors fit as well or better, and only prior defects, module size and minor authors had direct effects
[review-measures-defects-replication]{22}. In that replication, five or more reviewers were associated
with a higher chance of post-release defects (20% to 33%) via mediating authorship variables; elsewhere the
authors suggest modules with prior defects "probably invite more scrutiny with a larger review team"
[review-measures-defects-replication]{22}.
*(original: demonstrated; replication: independently measured.)*

**What reviewers find.** A Microsoft talk abstract reports that only about 15% of review comments flag a
possible defect, that comment usefulness rises with the reviewer's prior exposure to the code (33% useful
on first exposure, about 67% by the third), and that usefulness falls for very large reviews
[code-reviews-do-not-find-bugs]{23}. The replication attributes to the inspection experiment that reviewer
expertise mattered more than process structure [review-measures-defects-replication]{22}.
*(documented; no methods given.)*

## Re-review after changes

**Measured evidence is thin.** The closest experimental evidence concerns a second inspection after
repair, not re-review of a changed diff: repairing defects between two inspection sessions "had no effect
on observed defect density" but sometimes lengthened the interval dramatically, with very few
with-repair inspections [inspection-team-size-experiment]{18}. At Google, over 80% of changes involved at
most one iteration of resolving comments [google-modern-code-review]{20}. *(demonstrated / in-house
measured.)*

**Documented practice: approval can cover follow-up edits.** Google's public reviewer guidance tells
reviewers to grant approval while leaving unresolved comments when they are confident the author will
address them, when the comments are optional, or when the suggestions are minor (imports, typos, an
applied suggested fix, an unused dependency); reviewers who check only part of a change should say which
parts [google-review-speed-lgtm]{24}. *(documented.)*

**Designed platform policy: approval can be tied to the exact diff.** GitHub records the diff state at
approval and can optionally dismiss an approval as stale when any later push, branch update, or
merge-base change alters that diff; an alternative requires the most recent push to be approved by
someone other than its pusher, which GitHub presents as a compromise for complex pull requests while
noting that dismissing stale reviews is safer against unapproved content being added after approval
[github-stale-review-dismissal]{25}. *(designed; optional settings, not evidence of effectiveness.)*

No fetched source measures how often post-approval edits introduce defects, or compares
"re-review every change" with "re-review only material changes" {inferred: aggregate}.

## Findings by evidence type

| # | Finding | Evidence type | Sources |
| --- | --- | --- | --- |
| F1 | GPT-4 (2023) as a judge agrees with expert humans about as well as humans agree with each other on chat preference (85% vs 81%, non-tie); agreement rises with the performance gap between the compared models. | demonstrated | [llm-judge-mt-bench]{11} |
| F2 | LLM judges favour their own outputs (and outputs of similar models) across several task types; the MT-bench observation was itself inconclusive. | independently measured (separate groups, different setups) | [llm-judge-mt-bench]{11} [llm-self-recognition-preference]{12} [llm-self-bias-refinement]{15} [llm-judge-affinity-similarity]{14} [llm-judge-panel-poll]{16} |
| F3 | With ground truth, stronger judges' self-preference is mostly legitimate, but harmful self-preference when wrong is larger in stronger models; long reasoning reduces it. | demonstrated | [llm-self-preference-legitimacy]{13} |
| F4 | Using a different model does not remove favouritism toward functionally similar models; model errors grow more similar with capability. | demonstrated | [llm-judge-affinity-similarity]{14} |
| F5 | Self-refinement amplifies self-bias; reference-grounded feedback reduces it and yields real gains. | demonstrated | [llm-self-bias-refinement]{15} |
| F6 | A reference-guided judge cut math-grading failures most (3/20 vs 14/20 default; chain-of-thought 6/20; 10 questions, 20 judgements per prompt). | demonstrated | [llm-judge-mt-bench]{11} |
| F7 | A diverse three-family panel tracks human judgement better than a single GPT-4 judge in QA and Arena ranking, more cheaply, but not better than every single judge on every dataset. | demonstrated (single group) | [llm-judge-panel-poll]{16} |
| F8 | Trained LLM critics catch more inserted bugs in short code than paid human reviewers but hallucinate more; human-plus-critic teams cut hallucinations without adding comprehensiveness. | demonstrated (single vendor) | [llm-critics-catch-bugs]{17} |
| F9 | One-person inspection teams were poorer than two- or four-person teams; two and four did not differ; effort rose with team size. Abstract reports no significant treatment effect overall. | demonstrated (randomized field experiment) | [inspection-team-size-experiment]{18} |
| F10 | Median active reviewers is two across several organizations; more reviewers added little discussion and no extra rounds there. | independently measured (practice, not effectiveness) | [convergent-peer-review-practices]{19} |
| F11 | At Google the median is one reviewer, and more reviewers mean more comments. | documented (in-house log measurement) | [google-modern-code-review]{20} |
| F12 | Low review participation is associated with more post-release defects (up to five per component) in the studied Qt, VTK and ITK releases. | demonstrated (observational) | [review-coverage-participation-defects]{21} |
| F13 | Review measures add little explanatory power for post-release defects once size, prior defects and authorship are modelled; effects are unstable. | independently measured (replication) | [review-measures-defects-replication]{22} |
| F14 | A minority of review comments concern defects; reviewer familiarity with the code raises usefulness. | documented | [code-reviews-do-not-find-bugs]{23} |
| F15 | Repairing between inspection sessions did not raise observed defect density overall (a cautioned small-cell gain for two-person teams) and lengthened interval; it does not test changes after review. | demonstrated (small cells) | [inspection-team-size-experiment]{18} |
| F16 | Approval may be granted with unresolved minor or trusted follow-up comments. | documented | [google-review-speed-lgtm]{24} |
| F17 | Approvals can be configured to lapse on any diff change, or to require a non-pusher approval of the latest push. | designed | [github-stale-review-dismissal]{25} |

## Contradictions

- **Self-preference as bias versus as legitimate preference** — `qualifies`. The summarization study
  treats self-preference as favouring own outputs judged equal by humans, without ground-truth quality
  control [llm-self-recognition-preference]{12}. The ground-truth study finds stronger models' self-preference
  mostly legitimate, yet harmful self-preference larger when they err [llm-self-preference-legitimacy]{13}.
  The MT-bench study could not determine whether the bias exists [llm-judge-mt-bench]{11}.
- **Diverse panels reduce bias versus correlated errors undermine juries** — `tension`. The panel study reports
  reduced intra-model bias from disjoint families [llm-judge-panel-poll]{16}; the similarity study argues
  growing error similarity could compromise jury independence [llm-judge-affinity-similarity]{14}. They differ in
  judges, tasks and metrics, so neither tests the other's claim directly.
- **Two reviewers versus one reviewer as the converged norm** — `tension`. The multi-organization study reports
  convergence on two reviewers with minimal added discussion beyond that [convergent-peer-review-practices]{19};
  the Google study reports a median of one and more comments with more reviewers [google-modern-code-review]{20}.
  Neither measures defects found, and organizational context differs.
- **Review participation explains defects versus it does not** — `contradicts` on explanatory power, using the
  same Qt data: the original estimates up to five additional defects from lax participation
  [review-coverage-participation-defects]{21}; the replication finds models without review predictors fit as well or
  better [review-measures-defects-replication]{22}.
- **Inspection team size: effect versus no significant effect** — `tension` inside one source. The detailed
  analysis and main-results section report one-person teams poorer than two- or four-person teams; the abstract
  reports no significant influence of treatments on effectiveness [inspection-team-size-experiment]{18}.

## Disconfirming analysis

- **Against "a different-model reviewer is clearly better than same-model self-review":** searched every LLM
  attestation for evidence that same-model judging is adequate. Found: GPT-3.5 did not favour itself and the
  MT-bench authors could not confirm the bias [llm-judge-mt-bench]{11}; stronger models' self-preference is
  mostly legitimate on verifiable tasks [llm-self-preference-legitimacy]{13}; a held-out model still favours
  similar models [llm-judge-affinity-similarity]{14}. The claim therefore stands only in a weakened form:
  self-review carries a measured bias, and a different model does not remove the similarity component of it.
- **Against "diverse panels beat single judges":** a single small judge beat the panel on one QA dataset, the
  study covers three settings, and the authors are an interested vendor [llm-judge-panel-poll]{16}.
- **Against "LLM critics outperform humans":** human-only critiques had far fewer hallucinations and nitpicks,
  the human cohort is not best-possible human performance, and the bugs were inserted into short snippets
  [llm-critics-catch-bugs]{17}.
- **Against "more reviewers find more defects":** two and four reviewers did not differ in the randomized
  experiment [inspection-team-size-experiment]{18}; more active reviewers brought little extra discussion
  [convergent-peer-review-practices]{19}; review measures lost explanatory power in replication and five or more
  reviewers coincided with more defects [review-measures-defects-replication]{22}. Evidence for the opposite: one
  reviewer was poorer than two [inspection-team-size-experiment]{18}, and more reviewers meant more comments at
  Google [google-modern-code-review]{20}. The supported reading, from one experiment whose abstract reports no
  significant treatment effect, is a gain from one to two, not beyond.
- **Against "review is mainly a defect filter":** most comments concern maintainability, not defects
  [code-reviews-do-not-find-bugs]{23}; Google's foremost reason for introducing review was "to improve code
  understandability and" (continuation unread) [google-modern-code-review]{20}.
- **Against "re-review after every change is necessary":** documented practice lets an approval stand over
  minor or trusted follow-ups [google-review-speed-lgtm]{24}. (The repair-between-sessions result is not evidence here;
  see Re-review after changes.) For it: a platform designer offers stale-approval
  dismissal because unapproved content can be added after approval [github-stale-review-dismissal]{25}. Neither side
  is measured.

## Limits

- No fetched study evaluates agent-to-agent review of multi-file, repository-scale changes; the code-critic study
  explicitly lacks multi-file support and repository navigation [llm-critics-catch-bugs]{17}.
- LLM results are tied to 2023-2025 models; the similarity study reports errors converging with capability
  [llm-judge-affinity-similarity]{14}, so the direction of change over time is itself uncertain.
- Human-review evidence is older (1997-2020), observational except for the inspection experiment, and mostly
  measures comments or post-release defect counts, not defects caught per review.
- The Microsoft figures come from a two-page talk abstract without methods [code-reviews-do-not-find-bugs]{23}.
- Several coefficient values in the similarity paper and some tables in other papers did not survive text
  extraction and were not cited; one page of the Google case study did not extract [google-modern-code-review]{20}.
- No source measures defects introduced by post-approval edits, or the cost and benefit of re-review triggers.

## Revisit if

- A study compares same-model, different-family and human review of agent-generated multi-file changes against
  ground truth (tests, seeded defects).
- A replication of reviewer-count effects on defects found (not comments) appears for modern tool-based review.
- Measured data appear on defects introduced after approval, or on outcomes of stale-approval dismissal policies.
- Newer judge models show self-preference or affinity bias disappearing or growing under ground-truth checks.

## Decision relevance

For a workflow that prefers cross-model review of agent-generated work: the evidence supports keeping an
independent check over pure self-review, but frames its value as reducing correlated judgement rather than
guaranteeing detection; grounding checks in references appears more consistently associated with error
reduction than model identity alone {inferred: aggregate}, and extending that to tests is untested `extends`. One
inspection experiment suggests a second reviewer adds more than further reviewers, though its abstract reports no
significant effect [inspection-team-size-experiment]{18}; Rigby and Bird attribute the two-reviewer optimum to Porter
et al. rather than measuring it [convergent-peer-review-practices]{19}. Human-review data also suggest that
reviewer count is commonly scaled to perceived risk or change size [convergent-peer-review-practices]{19}
[google-modern-code-review]{20}. Whether an earlier review "covers" later
changes is a policy choice in the sources (approve-with-comments for minor follow-ups versus diff-tied approval),
not an empirically settled question.

## Revisions

- 2026-10-19 — Correction (position preserved): restored qualifiers, separated chain-of-thought from reference
  grounding, re-scoped citations; see `../verification-checklist.md`, "Revision response (2026-10-19)".
- 2026-10-19 — Correction (position preserved), bounded pass after the adversarial re-read: with the MT-bench
  attestation extended by Table 4, chain-of-thought judging is stated as also cutting math-grading failures (6/20
  against 14/20 default and 3/20 reference; 20 judgements per prompt), the chain-of-thought `qualifies` row was
  removed because the sources do not diverge, and the agreement breakdown now reads as a performance gap between
  compared models; see `../verification-checklist.md`, "Bounded correction response (2026-10-19)".
- 2026-10-19 (lead spot-check correction): N3 — "the one study comparing judge prompts" scoped to MT-bench's
  default/chain-of-thought/reference comparison. See `../verification-checklist.md`, "Lead spot-check (2026-10-19)".

## Sources (corpus numbering)

7. **anthropic-agent-evals** — reused existing attestation (corpus number 7).
11. **llm-judge-mt-bench** — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang et al. (UC Berkeley and others). arXiv 2306.05685 v4 (24 Dec 2023); NeurIPS 2023 Datasets and Benchmarks Track per arXiv comments. Fetched 2026-10-18. Source: https://arxiv.org/abs/2306.05685. Engagement: partial (main text sections 1, 3.3-4.2).
12. **llm-self-recognition-preference** — LLM Evaluators Recognize and Favor Their Own Generations. Arjun Panickssery, Samuel R. Bowman, Shi Feng. arXiv 2404.13076 v1 (15 Apr 2024). Fetched 2026-10-18. Source: https://arxiv.org/abs/2404.13076. Engagement: partial (main text).
13. **llm-self-preference-legitimacy** — Do LLM Evaluators Prefer Themselves for a Reason? Wei-Lin Chen, Zhepei Wei, Xinyu Zhu, Shi Feng, Yu Meng. arXiv 2504.03846 v3 (12 Dec 2025). Fetched 2026-10-18. Source: https://arxiv.org/abs/2504.03846. Engagement: partial (main text, limitations).
14. **llm-judge-affinity-similarity** — Great Models Think Alike and this Undermines AI Oversight. Shashwat Goel, Joschka Strüber, Ilze Amanda Auzina et al. arXiv 2502.04313 v2 (12 Jun 2025). Fetched 2026-10-18. Source: https://arxiv.org/abs/2502.04313. Engagement: partial (sections 1, 3, 5, 7; Appendix B).
15. **llm-self-bias-refinement** — Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement. Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, William Yang Wang. arXiv 2402.11436 v2 (18 Jun 2024). Fetched 2026-10-18. Source: https://arxiv.org/abs/2402.11436. Engagement: partial (main text, limitations).
16. **llm-judge-panel-poll** — Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models. Pat Verga et al. (Cohere). arXiv 2404.18796 v2 (1 May 2024). Fetched 2026-10-18. Source: https://arxiv.org/abs/2404.18796. Engagement: partial (main text).
17. **llm-critics-catch-bugs** — LLM Critics Help Catch LLM Bugs. Nat McAleese, Rai (Michael Pokorny), Juan Felipe Cerón Uribe, Evgenia Nitishinskaya, Maja Trębacz, Jan Leike (OpenAI). arXiv 2407.00215 v1 (28 Jun 2024). Fetched 2026-10-18. Source: https://arxiv.org/abs/2407.00215. Engagement: partial (main text; figure values not read).
18. **inspection-team-size-experiment** — An Experiment to Assess the Cost-Benefits of Code Inspections in Large Scale Software Development. Adam A. Porter, Harvey P. Siy, Carol A. Toman, Lawrence G. Votta. IEEE Transactions on Software Engineering 23(6), June 1997, pp. 329-346 (as printed). Fetched 2026-10-18. Source: https://userweb.cs.txstate.edu/~rp31/papersSQ/PorterEtAl_TSE.pdf. Engagement: full-text.
19. **convergent-peer-review-practices** — Convergent Contemporary Software Peer Review Practices. Peter C. Rigby and Christian Bird (attributed by citing references; PDF title block absent). ESEC/FSE '13 per the PDF's ACM notice. Fetched 2026-10-18. Source: https://users.ece.utexas.edu/~miryung/teaching/EE379K-Spring2014/Papers/Paper%204.pdf. Engagement: full-text.
20. **google-modern-code-review** — Modern Code Review: A Case Study at Google. Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, Alberto Bacchelli. ICSE-SEIP 2018 (as printed). Fetched 2026-10-18. Source: https://storage.googleapis.com/gweb-research2023-media/pubtools/4476.pdf. Engagement: partial (page 5 did not extract).
21. **review-coverage-participation-defects** — The Impact of Code Review Coverage and Code Review Participation on Software Quality: A Case Study of the Qt, VTK, and ITK Projects. Shane McIntosh, Yasutaka Kamei, Bram Adams, Ahmed E. Hassan. MSR '14 (as printed). Fetched 2026-10-18. Source: https://rebels.cs.uwaterloo.ca/papers/msr2014_mcintosh.pdf. Engagement: partial (abstract, RQ results, metric definitions).
22. **review-measures-defects-replication** — Do Code Review Measures Explain the Incidence of Post-Release Defects? Case Study Replications and Bayesian Networks. Andrey Krutauz, Tapajit Dey, Peter C. Rigby, Audris Mockus. arXiv 2005.09217 v1 (19 May 2020). Fetched 2026-10-18. Source: https://arxiv.org/abs/2005.09217. Engagement: partial (results, conclusions, limitations).
23. **code-reviews-do-not-find-bugs** — Code Reviews Do Not Find Bugs: How the Current Code Review Best Practice Slows Us Down. Jacek Czerwonka, Michaela Greiler, Jack Tilford (Microsoft). Two-page talk abstract; venue not printed (attributed to ICSE SEIP 2015 by the Google case study). Fetched 2026-10-18. Source: https://www.michaelagreiler.com/wp-content/uploads/2019/02/Code-Reviews-Do-Not-Find-Bugs.-How-the-Current-Code-Review-Best-Practice-Slows-Us-Down.pdf. Engagement: full-text.
24. **google-review-speed-lgtm** — Speed of Code Reviews (and Every Line exceptions), Google Engineering Practices Documentation. Google. Undated public pages. Fetched 2026-10-18. Source: https://google.github.io/eng-practices/review/reviewer/speed.html. Engagement: full-text.
25. **github-stale-review-dismissal** — About protected branches. GitHub Docs. Undated. Fetched 2026-10-18. Source: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches. Engagement: partial (required-reviews section).
