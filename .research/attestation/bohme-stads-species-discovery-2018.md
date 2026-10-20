---
source_handle: bohme-stads-species-discovery-2018
fetched: 2026-10-20
source_url: https://arxiv.org/pdf/1803.02130
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: arXiv PDF v2 (4 Apr 2018), text extracted with pypdf; tables partly read from extraction, figures not read
---

# STADS: Software Testing as Species Discovery — Spatial and Temporal Extrapolation from Tested Program Behaviors

## Source structure and scope
Marcel Böhme (National University of Singapore / Monash University). arXiv 1803.02130v2, dated 4 April
2018; the PDF header reads "Publication date: April 2018" (journal: ACM TOSEM per the arXiv
listing's search-result summary, not verified from the PDF). Maps automated software testing / fuzzing
onto ecological species-richness estimation; evaluates a multinomial model on six open-source programs
fuzzed with AFL for a cumulative 8.2 months. Engagement depth: abstract, §1, §2 (motivating example
incl. Table 1), §3 assumptions, §4 estimator survey excerpts, §6 RQ results excerpts, §9 challenges.

## Anchored details
- **Abstract:** a fuzzer run for a week has "no means (i) to estimate the total number of feasible program
  branches ... (ii) to estimate the additional time required to cover 10% more branches ... or (iii) to
  assess the residual risk that a vulnerability exists when no vulnerability has been discovered." The
  framework "draws from over three decades of research in ecological biostatistics"; the "preliminary
  empirical study demonstrates a good estimator performance even for a fuzzer with adaptive sampling bias".
- **§1.3 hypothesis:** "rare species which have been discovered explain the species within the fuzzer's
  search space that remain undiscovered"; estimators based on singleton and doubleton species "demonstrate
  a good performance". Species = paths, branches, crashes, mutants, states etc.; multinomial model (one
  species per input) and Bernoulli product model (several species per input).
- **§1.3 evaluation summary:** two estimators (species coverage Ĝ, Good–Turing discovery probability Û)
  and one extrapolator Ŝ(n+m*) show "a reasonably low bias and high precision"; despite adaptive bias
  "the methodologies are statistically consistent, meaning that bias decreases and precision increases as
  more test inputs are generated."
- **§2, Table 1 (statement-coverage extrapolation):** estimates within ±1 percentage point of empirical in
  eight of eleven cases; "Between 10 and 15 minutes, there is a sudden coverage increase by 12 percentage
  points that is explained by the adaptive sampling of AFL. The extrapolation was not able to forecast this
  sudden increase." (e.g. from 10 min, extrapolated 83.3% vs empirical 71.7% at 15 min.)
- **§2.1 / §4.1, discovery probability:** Good–Turing estimate Û = f1/n (singletons over samples) = the
  probability that the next input discovers a new species; its inverse estimates inputs expected before the
  next discovery; presented as a residual-risk bound.
- **§3 assumption:** "we must assume that the relative species abundances ... does not substantially change
  during the fuzzing campaign. However, in practice this assumption might not hold" — feedback-directed
  fuzzers have "adaptive sampling bias".
- **§4 estimator survey:** first-order jackknife ≈ S(n) + f1; second-order jackknife ≈ S(n) + 2f1 − f2
  (Burnham and Overton give higher orders, as attributed). "Chao1-type estimators provide a lower bound ...
  rather than a point estimate. When there are a large number of undiscovered species, it will be
  statistically impossible to obtain a good estimate of species richness. Hence, a good lower bound is often
  more practical than an imprecise point estimate."
- **§6 RQ.3 (bias of Ŝ):** for four of six subjects bias within ±10% of true richness within 12 hours; two
  took 48 hours. Bias was sometimes systematically negative, sometimes positive (positive mean bias of 6.2,
  1.6 and 1.4 at one minute for three subjects; −0.9, −0.7, −0.2 for three others). Named sources of bias:
  campaign ramp-up ("there is simply not sufficient data to extrapolate well ... no discernible asymptote"),
  varying seed quality, adaptive bias, many rare species, sudden discovery surges. "Even at 100 hours, the
  empirical value may still substantially underestimate the true species richness."
- **§6 extrapolation finding:** "Sudden surges in the number of discovered paths are not anticipated
  resulting in negative bias"; "We do not find very strong evidence that the rule of thumb in ecology to keep
  the extrapolation within twice the sampling effort applies ... Other sources of bias and imprecision seem
  to have a stronger impact."
- **§9.1:** program behaviours are "megadiverse" (very high richness, very low evenness); Colwell et al.
  suggest coverage-based estimators where many rare species are expected (as attributed).
- **§9.1.3 Endemism:** species reachable only via "magic numbers" are like Madagascar's endemics — "A global
  survey of the biodiversity in rain forests would miss many species if the 'magic island' of Madagascar
  remains uninvestigated ... Hence, it is sensible only to provide an improved lower bound".
- **§9.2.1 Misidentification:** Austen et al. (as cited) found "even taxonomic experts were correct in only
  60% of cases when asked whether two images showed the same or different species of bumblebees"; the
  guarantees hold "modulo the dynamic analyzer's capability to identify the correct species".
- **§9.2.2 Morphospecies:** individuals that differ from known species but not enough to be assigned their own
  species; compared to the test-oracle problem.
- **§9.4:** claims hold "w.r.t. that fuzzer" — a biased but non-adaptive sampler yields valid statements
  about what that sampler would find; non-adaptive bias is compared to light traps luring some species more.
