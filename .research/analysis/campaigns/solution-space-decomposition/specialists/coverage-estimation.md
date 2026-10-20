---
title: Coverage estimation for samples of kinds, and reviewer detection of omissions
provenance: agent-synthesis
updated: 2026-10-20
summary: >-
  Within-specialist brief on two linked questions. First, how ecological species-richness and
  sample-coverage estimators (Chao1/Chao2, iChao, jackknife, ACE, Good–Turing coverage and discovery
  probability, rarefaction/extrapolation, Hill numbers, accumulation curves) estimate how complete a
  sample of distinct kinds is, what they assume, how they behave with few singletons and doubletons, and
  how they have been carried into vocabulary size, software testing, inspection defect counts and idea
  generation. Second, what the evidence says about whether human or model reviewers detect missing items,
  how structured and free review compare, and when independent passes disagree because of classification
  rather than retrieval. Main findings: singleton/doubleton estimators are lower bounds under
  heterogeneity; sample coverage is estimable when richness is not; estimates are relative to the
  sampling process and to the identity threshold that defines a "kind"; small, adaptive or few-pass
  samples underestimate; omissions are detected markedly less often than commissions by both humans and
  models; and a large share of between-pass disagreement in reviews and mappings is classification, not
  retrieval.
---

# Coverage estimation and omission detection

## Scope and evidence key

This brief covers (A) estimator theory for counting distinct kinds from an incomplete sample and its
validity for small, heterogeneous samples, and (B) evidence on whether reviewers detect what is missing
and on the reliability of category boundaries. Capture–recapture for systematic-review searches,
technology-assisted-review stopping rules and LLM idea-diversity saturation are covered by sibling
specialists and appear here only where the estimator theory needs them.

Evidence labels used below:

- **Designed / advocated**: a procedure proposed or recommended without a test against known truth.
- **Demonstrated**: shown on worked examples or a single case.
- **Measured**: compared against known truth, in simulation, a benchmark or a controlled experiment.

Engagement depth: most sources were read in full text. Five are abstract-level or extractor-level only:
[link-heterogeneity-nonidentifiability-2003]{356}, [ciolkowski-pbr-meta-analysis-2009]{369},
[aguilar-fault-type-code-review-2025]{370}, [wohlin-mapping-reliability-2013]{374} and the body findings of
[schmitz-rahmann-richness-estimation-review-2025]{357}. Claims resting on them carry that limit.

## Part A: Estimating how complete a sample of kinds is

### A1. What the estimators take as input

Ecology distinguishes two data shapes. **Abundance data** counts individuals of each species in one
sample. **Incidence data** records only whether each species was detected in each of T sampling units
(traps, quadrats, timed surveys) [chao-colwell-chao2-inequality-2017]{350}. Incidence data suits cases where
individuals are hard to define or count, and replicated incidence records "account for spatial (or
temporal) heterogeneity" [chao-colwell-chao2-inequality-2017]{350}. Gotelli and Colwell stress that the unit
of replication (individual versus sample of individuals) "turns out to be far from trivial"
[gotelli-colwell-quantifying-biodiversity-2001]{353}.

Every estimator below uses the **frequency counts**: f1 (or Q1) is the number of kinds seen exactly once
(singletons, or "uniques" in incidence data), f2 (Q2) the number seen exactly twice (doubletons,
"duplicates") [chao-hill-numbers-rarefaction-2014]{351} [chao-colwell-chao2-inequality-2017]{350}. The
underlying idea: "The greater the number of rare species in a dataset, the more likely it is that other
species are present that were not represented" [gotelli-colwell-quantifying-biodiversity-2001]{353}.
Frequent kinds "carry negligible information about the undetected species"
[chao-colwell-chao2-inequality-2017]{350}.

### A2. Chao1 / Chao2 and their improved forms

- **How it works.** Chao2 = S_obs + ((T−1)/T)·Q1²/(2Q2). When Q2 = 0 the bias-corrected form
  S_obs + ((T−1)/T)·Q1(Q1−1)/2 is used. Chao1 is the abundance-data analogue
  [chao-colwell-chao2-inequality-2017]{350} [bohme-stads-species-discovery-2018]{359}. iChao2 (Chiu et al.
  2014, as reviewed) adds information from Q3 and Q4 to tighten the bound
  [chao-colwell-chao2-inequality-2017]{350}.
- **What it claims.** It is a lower bound derived from a Cauchy–Schwarz inequality. The bound is exact
  only if detection probabilities are homogeneous, "a very restrictive condition, one that is almost never
  satisfied". The relaxed condition for near-unbiasedness: undetected kinds and singletons share about the
  same mean detection probability. Frequent kinds may then be as heterogeneous as they like
  [chao-colwell-chao2-inequality-2017]{350}. Otherwise "the data do not contain sufficient information to
  accurately estimate species richness, and the Chao2 formula provides a universal nonparametric lower
  bound" [chao-colwell-chao2-inequality-2017]{350}. Chao1 is "valid under all types of species abundance
  distribution" as a lower bound [chao-sufficient-sampling-2009]{352}.
- **How it behaves on small counts.** Worked example: 12 point counts with Q1 = 9 and Q2 = 4 gave a
  Chao2 of 36.3, with a 95% interval of 29.1 to 68.8. The interval is log-transformed and right-skewed, and
  its lower limit never falls below S_obs [chao-colwell-chao2-inequality-2017]{350}. If Q1 = 0, the estimate
  collapses to S_obs ("sampling is complete") [chao-colwell-chao2-inequality-2017]{350}.
- **Evidence.** *Measured indirectly* in ecology: procedures built on Chao1/Chao2 asymptotes (effort
  prediction, rarefaction/extrapolation) were tested by subsampling large inventories and on simulated
  assemblages [chao-sufficient-sampling-2009]{352} [chao-hill-numbers-rarefaction-2014]{351}. Measured on mixed real and
  simulated data in a 2025 benchmark: singleton-based methods "yield accurate asymptotic lower bounds for
  several of the tested simulated species compositions, but tend to underestimate the true richness for
  heterogeneous populations and small samples containing 1% to 5% of the population"
  [schmitz-rahmann-richness-estimation-review-2025]{357}.

### A3. Jackknife and coverage-based (ACE/ICE) estimators

- **Jackknife.** The first-order jackknife adds roughly f1 unseen kinds; the second-order adds roughly
  2f1 − f2 [bohme-stads-species-discovery-2018]{359}.
- **Measured against known defect counts.** In software requirements inspections, capture–recapture
  models with the jackknife estimator under heterogeneous detectability (Mh-JK) were recommended for four
  to five inspectors. Their median relative error was 5–16%. Across models, "In most of the cases, we have
  observed that the models underestimate the total number of defects"
  [briand-capture-recapture-inspections-2000]{362}.
- **ACE/ICE.** These coverage-based estimators sit among the more complex alternatives, which Chao and
  Colwell report were not more useful than the simple ones for biological applications
  [chao-colwell-chao2-inequality-2017]{350}.
- **Zero counts.** The 2025 benchmark reports, via extractor, that Good–Turing and jackknife-type estimators
  fail when singleton or doubleton counts are zero [schmitz-rahmann-richness-estimation-review-2025]{357}
  {confidence: extractor-level, not verified against the article body}.

### A4. Good–Turing sample coverage and discovery probability

- **Definition.** Sample coverage is the share of the assemblage's total abundance (or incidence
  probability) that belongs to kinds already observed. Turing and Good's estimator is roughly
  "one minus the proportion of singletons" [chao-hill-numbers-rarefaction-2014]{351}. The incidence version
  is Ĉ = 1 − (Q1/U)·[(T−1)Q1 / ((T−1)Q1 + 2Q2)], with a modified form when Q2 = 0
  [chao-colwell-chao2-inequality-2017]{350}.
- **It is not a count of missing kinds.** "The estimated complement of coverage is not an estimate of the
  number of unseen species, but rather it estimates the proportion of the total individuals in the
  assemblage that belong to undetected species" [chao-hill-numbers-rarefaction-2014]{351}. "A tiny
  percentage of coverage can contain an infinite number of rare species"
  [chao-hill-numbers-rarefaction-2014]{351}.
- **Why it matters.** Richness in highly diverse assemblages is hard to estimate, "whereas sample coverage
  can be accurately estimated" [chao-hill-numbers-rarefaction-2014]{351}.
- **Discovery probability.** The complement of coverage, f1/n, is the probability that the next sample
  reveals a new kind. In software testing it is read as an upper bound on residual risk
  [bohme-stads-species-discovery-2018]{359} [bohme-residual-risk-greybox-2021]{360}. *Measured* in the
  software-testing setting (below, A7).

### A5. Rarefaction, extrapolation, Hill numbers and accumulation curves

- **Accumulation and rarefaction curves.** A taxon accumulation curve "rises relatively rapidly at first,
  then much more slowly". Raw counts "can be validly compared only when taxon accumulation curves have
  reached a clear asymptote" [gotelli-colwell-quantifying-biodiversity-2001]{353}. Rarefaction
  (interpolation) has an unbiased analytic estimator. It "cannot be used for extrapolation"
  [chao-colwell-chao2-inequality-2017]{350} [gotelli-colwell-quantifying-biodiversity-2001]{353}.
- **Extrapolation range.** For richness (Hill number q = 0), extrapolation "is reliable up to no more than
  double the reference sample size" because the asymptote estimate is only a lower bound
  [chao-hill-numbers-rarefaction-2014]{351}. Short-range extrapolation is robust even when the richness
  estimator is biased [chao-colwell-chao2-inequality-2017]{350}. For q ≥ 1 (Shannon- and Simpson-type
  diversity), extrapolation is nearly unbiased out to the asymptote [chao-hill-numbers-rarefaction-2014]{351}.
  Theory sets the outer limit. Good–Toulmin predicts new kinds only up to a doubling of the sample. Smoothed
  estimators provably reach about log n times the sample, and "this range is the best possible"
  [orlitsky-suresh-wu-unseen-species-2016]{354}. Without a minimum-probability assumption, estimating the
  total number of kinds is impossible: "there could be infinitely many symbols with arbitrarily small
  probabilities that will never be observed" [orlitsky-suresh-wu-unseen-species-2016]{354}.
- **Coverage-based standardisation.** Comparing equal-size samples may compare "a nearly complete sample to
  a very incomplete one". Standardising to equal coverage compares "equal population fractions"
  [chao-colwell-chao2-inequality-2017]{350}. A sample-completeness curve shows how much effort reaches a
  given coverage [chao-hill-numbers-rarefaction-2014]{351}. *Measured and demonstrated* in ecology; tooling
  includes iNEXT and SpadeR [chao-colwell-chao2-inequality-2017]{350}.

### A6. Effort-to-completion and stopping rules

- **The "no singletons" rule.** Sampling is complete when every kind has been seen at least twice. In
  practice this is operationalised as estimated undetected kinds below 0.5 [chao-sufficient-sampling-2009]{352}.
  The rule can be expensive: "by the time the total sampling effort is extensive enough to reveal two
  individuals of each species found only once ... single individuals of additional species will have
  inevitably surfaced" [chao-sufficient-sampling-2009]{352}.
- **Effort needed.** Across seven published data sets, detecting all estimated species needed 1.05 to
  10.67 times the original effort (median about 2.23). Detecting 90% needed 0.33 to 1.10 times (median
  about 0.80). The method is "slightly conservative for small sample sizes"
  [chao-sufficient-sampling-2009]{352}. *Measured* by subsampling two large inventories.

### A7. Applications outside ecology

- **Vocabulary.** Shakespeare's 31,534 word types include 14,376 seen once and 4,343 seen twice. The
  analysis yields "at least 35 000 more words" as a lower bound. "No upper bound is possible", and the data
  "runs out of predictive power for t greater than 10" [efron-thisted-shakespeare-unseen-1976]{355}. In
  linear-programming bounds, lower and upper estimates diverge as extrapolation grows (at t = 10, 34,640
  versus 86,600) [efron-thisted-shakespeare-unseen-1976]{355}. On Hamlet, 20% of the text gave an accurate
  total-vocabulary estimate with modern estimators [orlitsky-suresh-wu-unseen-species-2016]{354}.
  *Measured.*
- **Software testing.** STADS maps fuzzing onto species discovery (paths, branches or crashes as species).
  - Estimators were statistically consistent despite adaptive sampling, but bias in the first hours was
    sometimes positive and sometimes negative. For four of six programs the estimate came within ±10% of
    true richness by 12 hours; two programs took 48 hours [bohme-stads-species-discovery-2018]{359}.
  - Sudden discovery surges were not anticipated by extrapolation, for example a 12-point jump in
    statement coverage that the extrapolation missed [bohme-stads-species-discovery-2018]{359}.
  - A follow-up found that blackbox estimators "systematically and substantially under-estimate the true
    risk" under adaptive sampling. A campaign "orders of magnitude longer" might be needed
    [bohme-residual-risk-greybox-2021]{360}.
  - *Measured.*
- **Inspection defect counts.** Each inspector is a trapping occasion
  [briand-capture-recapture-inspections-2000]{362}. Models "ought not be used with less than 4 inspectors
  unless shown to work in a particular environment". With too few inspectors, "underestimation may be
  substantial" [briand-capture-recapture-inspections-2000]{362}. *Measured* against known seeded defects.
- **Ideas.** Kornish and Ulrich estimated the size of an "opportunity space" from repetition among 1,368
  ideas generated independently. They used a one-parameter model in which each unique idea is equally
  likely to be drawn [kornish-ulrich-opportunity-spaces-2011]{361}.
  - The estimates (for example T ≈ 1,103, with a 95% interval of 806 to 1,493, from 271 unique ideas among
    311) are "wide, but appropriately so". Relaxing equal likelihood raised them "somewhat"
    [kornish-ulrich-opportunity-spaces-2011]{361}.
  - Meincke et al. applied the same estimator to GPT-4 idea pools. They stress that it estimates "only the
    possible number of unique ideas that can be found with a particular technique"
    [meincke-prompting-idea-variance-2024]{363}.
  - *Demonstrated.* No known-truth comparison was available.
- **Document review.** Chao's estimator is used as a stopping criterion. Under heterogeneity it "provides a
  lower bound", and point-estimate criteria "tend to underestimate"
  [bron-chao-estimator-tar-2024]{364}. Covered in depth by the search-completeness specialist.

### A8. Validity for small, heterogeneous samples

1. **Heterogeneity turns estimates into lower bounds and can make the total unidentifiable.**
   Heterogeneity is why Chao-type estimators are lower bounds [chao-colwell-chao2-inequality-2017]{350}
   [bron-chao-estimator-tar-2024]{364}. Beyond that, "reasonable alternative models may predict essentially
   identical observations from populations of substantially different sizes ... even with very large
   samples" [link-heterogeneity-nonidentifiability-2003]{356}. For hyperdiverse groups, estimators "often
   fail to reach any asymptote at all" [gotelli-colwell-quantifying-biodiversity-2001]{353}.
2. **Few sampling occasions give wide intervals and underestimates.** See the 29.1–68.8 interval from 12
   units [chao-colwell-chao2-inequality-2017]{350}, the under-four-inspectors threshold
   [briand-capture-recapture-inspections-2000]{362}, and underestimation at 1–5% sampling fractions
   [schmitz-rahmann-richness-estimation-review-2025]{357}. Ecology's own rule of thumb of five trapping
   occasions is reported to lack "quantitative justification" [briand-capture-recapture-inspections-2000]{362}.
3. **Dependent or adaptive sampling biases estimates downward.** The models assume relative abundances do
   not change as sampling proceeds [bohme-stads-species-discovery-2018]{359}. When the sampler adapts to
   what it has found, estimators underestimate residual risk [bohme-residual-risk-greybox-2021]{360}. In
   ideas, within-person and shared-background dependence are acknowledged
   [kornish-ulrich-opportunity-spaces-2011]{361}.
4. **The estimate is relative to the sampling process.**
   - Software testing: claims hold "w.r.t. that fuzzer" [bohme-stads-species-discovery-2018]{359}.
   - Idea generation: "Different processes would result in different sizes" (children versus engineers
     versus surgeons) [kornish-ulrich-opportunity-spaces-2011]{361}.
   - Unreachable "endemic" kinds, the "magic island", are missed entirely, so "it is sensible only to
     provide an improved lower bound" [bohme-stads-species-discovery-2018]{359}.
5. **The identity threshold defines the kind.**
   - Kornish and Ulrich's total is "the total number of ideas that are distinct enough from one another to
     exceed that threshold". The threshold was set at 50% or 70% rater agreement and described as
     "arbitrary cutoffs" [kornish-ulrich-opportunity-spaces-2011]{361}.
   - Efron and Thisted count "girl" and "girls" as different types
     [efron-thisted-shakespeare-unseen-1976]{355}.
   - Higher ranks always saturate sooner than lower ones: "the number of genera reaches an asymptote sooner
     than the number of species" [gotelli-colwell-quantifying-biodiversity-2001]{353}.
6. **Purposive sampling reduces the repetition that estimators feed on.**
   - Maximum-information sampling reaches every code in far fewer steps than random sampling, but "only
     yields between 1 and 3 observations per code" [van-rijnsoever-saturation-simulation-2017]{358}.
   - Saturation depends "more ... on the mean probability of observing codes than on the number of codes"
     [van-rijnsoever-saturation-simulation-2017]{358}.
   - {inferred: tension} Frequency-count estimators read many singletons as many missing kinds. A
     deliberately diversity-seeking sampler produces many singletons by design, so Q1/Q2 from such a
     sampler does not have the random-sampling meaning the estimators assume.

### Summary table

| Method | Input | What it reports | Evidence | Main limit |
|---|---|---|---|---|
| Chao1 / Chao2 (bias-corrected; iChao) | f1, f2 (Q1, Q2; Q3, Q4) | Lower bound on total kinds, with CI | Measured (ecology; inspections via Mh; TAR) | Lower bound only under heterogeneity; wide CI on few units |
| Jackknife (1st/2nd order) | f1, f2 | Point estimate of total | Measured (inspections: Mh-JK at 4–5 inspectors) | Underestimates with few occasions |
| Good–Turing coverage / discovery probability | f1, f2, n or U | Share of the assemblage already represented; chance that the next sample is new | Measured (ecology; fuzzing) | Not a count of missing kinds; underestimates under adaptive sampling |
| Rarefaction / extrapolation (iNEXT, Hill numbers) | full frequency vector | Expected kinds at smaller or larger effort, by size or by coverage | Measured | q = 0 reliable to about 2× effort; theory caps near log n |
| Effort to completion (Chao et al. 2009) | f1, f2 | Extra effort to reach g% of the estimate | Measured (subsampling) | Minimum effort only; slightly conservative at small n |
| Repetition model (Kornish–Ulrich) | N ideas, u unique | Opportunity-space size relative to one generating process | Demonstrated | Equal-likelihood assumption; rater-set identity threshold |

## Part B: Do reviewers detect what is missing?

### B1. Omissions are detected less often than commissions

- **Language models.**
  - Given the original and the edited document side by side, Claude-3.7-Sonnet reached 69.6% F1 at
    identifying removed content; across 14 models, averages ranged from 71.2% down to 14.7%, and the top
    GitHub pull-request score was 40.0% [fu-absencebench-omission-2025]{365}.
  - Inference-time reasoning added 7.9%. Placeholders marking where content was removed added 35.7%
    [fu-absencebench-omission-2025]{365}.
  - The authors say the benchmark covers only "surface-form omission". Semantic absences ("omitted reasoning
    steps or missing evidence") are expected to be harder [fu-absencebench-omission-2025]{365}.
  - In a separate study, models detected planted over-inclusions "6-7x more often than planted omissions".
    In production, failures were "omission-first at 10:1" [judging-not-enumerating-omissions-2026]{366}.
  - *Measured.*
- **Human code reviewers.** In one 54-student experiment, "the tester detects more faults by commission than
  by omission" [aguilar-fault-type-code-review-2025]{370}. *Measured*, abstract-level only.
- **Human coders also under-apply categories.** In blind expert verification, the verifier preferred an
  LLM's application of a code over "the human omission" across 12 codes [liu-agreement-not-quality-coding-2026]{377}.
  Also, "two coders can reliably agree while both under-applying a code"
  [liu-agreement-not-quality-coding-2026]{377}. *Measured*, with a single verifier.
- **The inspection literature's definition.** Omission means "important information is left unstated".
  Commission means "incorrect, redundant, or ambiguous information is put into the SRS"
  [porter-votta-basili-detection-methods-1995]{368}.

### B2. Structured versus free review

- **Scenarios.** Defect-class scenarios beat Ad Hoc and Checklist reading in the original experiment.
  Reviewers were better on "the faults their scenarios are designed to uncover" and "no less effective" on
  others. "Checklist reviewers were no more effective than Ad Hoc reviewers". Scenarios fitted one document's
  fault profile better than the other's, and "poorly designed scenarios may lead to poor inspection
  performance" [porter-votta-basili-detection-methods-1995]{368}. *Measured.*
- **Replications diverge.** Regnell et al. summarise Bari and Linköping (scenario reading not significantly
  better), Strathclyde (mixed by document), Lucent (replicated Maryland-95) and Kaiserslautern (PBR beat ad
  hoc, yet detection rates for five defect classes did not differ among perspectives). Hayes's meta-analysis
  found effect sizes "inhomogeneous across the experiments" [regnell-pbr-perspectives-different-2000]{367}.
- **Perspective-based reading.** It assumes that "the perspectives find different defects". Regnell et al.
  found no significant difference in which defects the user, designer and tester perspectives found. "a
  combination of multiple perspectives may not give higher coverage of the defects compared to
  single-perspective reading" [regnell-pbr-perspectives-different-2000]{367}. A later aggregation found PBR
  teams more effective than ad hoc but "less effective when compared to checklists", with "strong indicators
  of researcher bias" [ciolkowski-pbr-meta-analysis-2009]{369}. *Measured*; the meta-analysis is
  abstract-level only.
- **Coverage trades off against detail.** Moving from Ad Hoc to Checklist to Scenario gives "more detail and
  less coverage" by construction [porter-votta-basili-detection-methods-1995]{368}. *Designed.*
- **Team size and meetings.**
  - Two- and four-person code inspections did not differ in effectiveness. Both beat one person
    [inspection-team-size-experiment]{371}.
  - Collection meetings produced "no net improvement", because meeting gains were offset by losses
    [porter-votta-basili-detection-methods-1995]{368}.
  - Individually found faults were sometimes never recorded, raising the question whether a reviewer was
    "talked out of the fault" [porter-votta-basili-detection-methods-1995]{368}.

### B3. Overlap between independent reviewers as a completeness signal

Overlap between independent passes is the input to capture–recapture defect-content estimation
[regnell-pbr-perspectives-different-2000]{367} [briand-capture-recapture-inspections-2000]{362}. Two design
goals pull against each other {inferred: tension}:

- Methods like PBR aim to *minimise* overlap by giving reviewers different targets
  [regnell-pbr-perspectives-different-2000]{367}.
- Capture–recapture needs overlap, and it assumes that whether one pass catches an item does not depend on
  whether another did [briand-capture-recapture-inspections-2000]{362}.

Regnell et al. frame their perspective-difference test as complementary to work on whether capture–recapture
can be used with PBR inspections [regnell-pbr-perspectives-different-2000]{367}.

### B4. When independent passes disagree because of classification rather than retrieval

- **Retrieval and classification are separable.** In real code inspections, only 23–24% of defects were
  found by both inspectors, so retrieval overlap was low. Yet classification agreement on the shared defects
  was good: kappa 0.66 and 0.82. Disagreement concentrated in one confusable pair (Data/Assignment), and
  merging the pair raised kappa to 0.73 [el-emam-defect-classification-repeatability-1998]{372}.
- **Classification can dominate.** With students and seven ODC categories, discrepancy averaged 43% against a
  maximum of 86%. It fell from 60% to 17% as training grew, and recurring confused pairs were identified
  [falessi-odc-feasibility-2006]{373}.
- **Matching duplicates is itself a classification step.**
  - "two or more inspectors could localize the same defect in different places and describe it differently,
    which could bias some of the capture-recapture estimates". Lists had to be consolidated by two people
    [briand-capture-recapture-inspections-2000]{362}.
  - Idea identity needed rater thresholds. Outlier raters who lumped many ideas as "identical" were excluded
    [kornish-ulrich-opportunity-spaces-2011]{361}.
  - Even taxonomic experts were "correct in only 60% of cases" judging whether two bumblebee images showed
    the same species (Austen et al., as cited) [bohme-stads-species-discovery-2018]{359}.
- **Mapping studies.** Two mapping studies of the same topic differed "when it comes to papers included and
  in terms of classification" [wohlin-mapping-reliability-2013]{374}. Two independent SLRs shared 6 of 32
  papers. The 10 additional relevant papers "would have had an impact" on a published review "by adding three
  new categories to the framework" [kitchenham-slr-repeatability-2011]{375}. Missing items thus produced
  missing categories.
- **Where the dendrogram is cut.** In card sorting, base clusters were stable across studies (90.9–96.5%
  similarity). However, "two people can produce different content structures" from the same dendrogram
  depending on where it is cut [katsanos-card-sort-cross-study-reliability-2019]{376}.
- **Agreement is not correctness.** Human–human agreement (Jaccard 0.52) exceeded human–LLM agreement (0.30),
  yet a blind verifier preferred the two at indistinguishable rates. Human consensus sometimes encoded "shared
  conservative bias" [liu-agreement-not-quality-coding-2026]{377}.

## Failure modes and limits

- **Illusory completeness from Q1 = 0 or a flat curve.**
  - Chao2 collapses to S_obs when no singletons remain [chao-colwell-chao2-inequality-2017]{350}.
  - A coverage-based completeness estimate says nothing about kinds the sampler cannot reach, the "magic
    island" [bohme-stads-species-discovery-2018]{359}.
  - Coverage measures abundance share, not the count of kinds [chao-hill-numbers-rarefaction-2014]{351}.
- **Unanticipated surges.** Extrapolation does not foresee step changes in discovery
  [bohme-stads-species-discovery-2018]{359}.
- **Downward bias under adaptivity and few passes**
  [bohme-residual-risk-greybox-2021]{360} [briand-capture-recapture-inspections-2000]{362}
  [schmitz-rahmann-richness-estimation-review-2025]{357}.
- **Benchmark-transfer risk.** Estimators validated on small, asymptotic benchmark datasets may not predict
  performance on not-yet-asymptotic, very rich ones [gotelli-colwell-quantifying-biodiversity-2001]{353}.
- **Pooling heterogeneous samples inflates singletons**, which "reflects the pooling of heterogeneous
  samples" rather than genuine rarity [chao-sufficient-sampling-2009]{352}.
- **Omission blindness of local review.** The proposed cause in models is that attention "cannot easily
  attend to 'gaps'", since absences correspond to no key [fu-absencebench-omission-2025]{365}. An omission "resists audit" because finding it is the authoring
  problem itself [judging-not-enumerating-omissions-2026]{366}.
- **Structured-review gains are conditional on scenario fit and do not replicate uniformly**
  [porter-votta-basili-detection-methods-1995]{368} [regnell-pbr-perspectives-different-2000]{367}.

## Disconfirming analysis

Searches for disconfirming evidence, claim by claim:

- **"Singleton-based estimators are reliable for small samples."** Disconfirmed for heterogeneous
  populations at 1–5% sampling fractions [schmitz-rahmann-richness-estimation-review-2025]{357}. Qualified by
  the fact that Chao-type estimators are framed as lower bounds, not point estimates
  [chao-colwell-chao2-inequality-2017]{350}. The near-unbiased claim holds only under the rare-kind
  homogeneity condition. No attested source shows that condition holds for kinds of methods or approaches.
- **"The 2× extrapolation rule is general."** STADS found no "very strong evidence" for it in software testing.
  Other bias sources mattered more [bohme-stads-species-discovery-2018]{359}. Orlitsky et al. prove a wider
  range (about log n) for new-kind prediction [orlitsky-suresh-wu-unseen-species-2016]{354}. The rule is a
  field heuristic tied to q = 0 lower-bound asymptotes [chao-hill-numbers-rarefaction-2014]{351}.
- **"More reviewers / more perspectives find more missing items."**
  - Perspectives did not find different defects [regnell-pbr-perspectives-different-2000]{367}.
  - Four reviewers were no better than two [inspection-team-size-experiment]{371}.
  - Meetings added nothing on net [porter-votta-basili-detection-methods-1995]{368}.
  - Disconfirming evidence for the opposite claim: scenario-based reading did raise detection in Maryland-95
    and Lucent [regnell-pbr-perspectives-different-2000]{367} [porter-votta-basili-detection-methods-1995]{368}.
- **"Checklists improve detection."** Disconfirmed in Maryland-95 (no better than ad hoc)
  [porter-votta-basili-detection-methods-1995]{368}. Partly supported by the PBR aggregation, where checklists
  outperformed PBR teams [ciolkowski-pbr-meta-analysis-2009]{369}. See Contradictions.
- **"Reasoning fixes omission detection in models."** Only partly: +7.9% on surface omission
  [fu-absencebench-omission-2025]{365}. Gap closure held only "where a rule can be executed" and was
  unreliable on test suites [judging-not-enumerating-omissions-2026]{366}.
- **"Inter-rater agreement certifies category quality."** Disconfirmed in one single-verifier study
  [liu-agreement-not-quality-coding-2026]{377}. Agreement and validity are not separated in the
  other classification sources: practitioner kappa of 0.66–0.82 was read as adequate, and merging one
  confused pair raised it [el-emam-defect-classification-repeatability-1998]{372}.
- **"Idea-space size estimates generalise."** The authors confine them to the generating process and
  identity threshold [kornish-ulrich-opportunity-spaces-2011]{361}
  [meincke-prompting-idea-variance-2024]{363}. No attested source validates an idea-space estimate against a
  known total.

## Contradictions

| Sources | Relationship | Positions |
|---|---|---|
| [porter-votta-basili-detection-methods-1995]{368} vs [ciolkowski-pbr-meta-analysis-2009]{369} | `tension` | Porter et al.: Checklist reviewers "no more effective than Ad Hoc" (individual detection, defect-based scenarios context). Ciolkowski: PBR teams "less effective when compared to checklists" (team effectiveness, aggregated experiments). Different outcome levels and comparators; not stated in one frame. |
| [porter-votta-basili-detection-methods-1995]{368} vs [regnell-pbr-perspectives-different-2000]{367} | `qualifies` | Porter et al.: role-specific scenarios focus reviewers on distinct fault classes. Regnell et al.: three PBR perspectives found statistically indistinguishable defect sets, questioning PBR's core assumption. |
| [chao-hill-numbers-rarefaction-2014]{351} vs [bohme-stads-species-discovery-2018]{359} vs [orlitsky-suresh-wu-unseen-species-2016]{354} | `tension` | Chao et al.: richness extrapolation reliable to about double the reference sample. Böhme: little evidence the 2× rule applies in fuzzing; other biases dominate. Orlitsky et al.: provable prediction to about log n times the sample. Different estimands (asymptote-based richness curve vs number of new kinds in a future sample) and settings. |
| [el-emam-defect-classification-repeatability-1998]{372} vs [falessi-odc-feasibility-2006]{373} | `tension` (already noted by Falessi) | El Emam & Wieczorek: kappa 0.66–0.82 among practitioners. Falessi & Cantone: 43% average discrepancy among trained students. Different subjects, schemes and measures. |
| [chao-colwell-chao2-inequality-2017]{350} vs [schmitz-rahmann-richness-estimation-review-2025]{357} | `qualifies` | Chao & Colwell: simple Chao estimators are the most useful in biological practice. Schmitz & Rahmann: which estimator is most accurate depends on species composition; singleton methods underestimate in heterogeneous, small samples. |

## Transfer-relevant observations

Stated in the source fields' own terms:

- Frequency-count estimators need each kind's detection counted across replicated, roughly independent
  sampling units. In incidence form, the unit is the sampling occasion, and the inputs are how many kinds
  were seen in exactly one or exactly two units [chao-colwell-chao2-inequality-2017]{350}
  [briand-capture-recapture-inspections-2000]{362}.
- Inspection studies found estimates unreliable below four occasions
  [briand-capture-recapture-inspections-2000]{362}.
- The quantities these fields treat as robustly estimable from small samples are:
  - sample coverage and discovery probability [chao-hill-numbers-rarefaction-2014]{351};
  - short-range extrapolation [chao-colwell-chao2-inequality-2017]{350}.
- The total number of kinds is reported as a lower bound with a skewed interval
  [chao-colwell-chao2-inequality-2017]{350}.
- Every count of kinds is conditional on:
  - the identity or resolution threshold that merges near-duplicates
    [kornish-ulrich-opportunity-spaces-2011]{361} [efron-thisted-shakespeare-unseen-1976]{355};
  - the taxonomic rank counted [gotelli-colwell-quantifying-biodiversity-2001]{353};
  - the generating process that defines which kinds are reachable [kornish-ulrich-opportunity-spaces-2011]{361}
    [bohme-stads-species-discovery-2018]{359}.
- In the inspection and annotation literatures, detecting absence is a distinct and weaker capability than
  judging presence, for humans and models alike [fu-absencebench-omission-2025]{365}
  [judging-not-enumerating-omissions-2026]{366} [aguilar-fault-type-code-review-2025]{370}. Marking where
  absence occurs (placeholders) recovers much of the gap in the surface-omission setting
  [fu-absencebench-omission-2025]{365}.
- Disagreement between independent passes has two separable components: which items each pass found
  (retrieval), and how found items are named, matched and categorised (classification). The sources measure
  these separately [el-emam-defect-classification-repeatability-1998]{372}
  [briand-capture-recapture-inspections-2000]{362} [wohlin-mapping-reliability-2013]{374}.
- {inferred: convergence} Several sources find classification disagreement concentrated in a few
  confusable category pairs and responsive to definition refinement or training
  [el-emam-defect-classification-repeatability-1998]{372} [falessi-odc-feasibility-2006]{373}.

## Revisit if

- A study validates a richness or coverage estimator against a known total for kinds of *methods, designs
  or approaches* (rather than species, words, code paths or defects).
- Evidence appears on frequency-count estimators applied to LLM-generated samples with known
  ground truth, including how temperature, prompting or multi-agent sampling changes the meaning of
  singletons.
- A replication tests omission detection on semantic absences (missing approaches, missing evidence)
  rather than surface deletions, for humans or models.
- The full text of the Ciolkowski aggregation, Link (2003) or Wohlin et al. (2013) is acquired, which could
  change the strength of B2, A8.1 and B4.
- New estimators for adaptive or purposive sampling (beyond greybox fuzzing) are published.
