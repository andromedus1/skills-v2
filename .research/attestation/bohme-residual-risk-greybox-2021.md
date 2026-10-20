---
source_handle: bohme-residual-risk-greybox-2021
fetched: 2026-10-20
source_url: https://mboehme.github.io/paper/FSE21.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: author-hosted PDF of the ESEC/FSE '21 paper, text extracted with PyMuPDF; abstract, §1 and evaluation-measure passages read; per-subject result tables not audited
---

# Estimating Residual Risk in Greybox Fuzzing

## Source structure and scope
Marcel Böhme (Monash University; MPI-SP), Danushka Liyanage (Monash University), Valentin Wüstholz
(ConsenSys). Proceedings of ESEC/FSE '21, August 23–28, 2021, Athens, 12 pages, doi 10.1145/3468264.3468570
(as printed in the ACM reference format on p. 1). Studies estimators of discovery probability / residual risk when
the sampler adapts to what it has already found. Engagement depth: abstract, introduction, estimator-performance
definitions (§5.4) and contribution list read; detailed results not audited.

## Anchored details
- **Abstract:** "For any errorless fuzzing campaign, no matter how long, there is always some residual risk that a
  software error would be discovered if only the campaign was run for just a bit longer." Discovery probability ("the
  probability that the next generated input increases code coverage") is argued to be "an excellent upper bound" on
  residual risk. "We find that estimators for blackbox fuzzing systematically and substantially under-estimate the true
  risk. An engineer—who stops the campaign when the estimators purport a risk below the maximum allowable risk—is vastly
  misled. She might need execute a campaign that is orders of magnitude longer to achieve the allowable risk." Key
  challenge: "adaptive bias: The probability to discover a specific error actually increases over time." Contributes "the
  first probabilistic analysis of adaptive bias" and "two novel classes of estimators".
- **§1:** if the bug probability stayed constant, residual risk could be cast as a "sunrise problem" with the Laplace
  estimator; "in the presence of adaptive bias, the Laplace estimator severely under-estimate the residual risk for
  greybox campaigns. The true risk is orders of magnitude higher than the estimator purports. A practitioner would abort the
  campaign many days earlier than necessary, and assume a higher degree of confidence in the correctness than warranted."
- **§1 contributions:** discovery probability observed to follow a power law; "discovery probability can be extrapolated by
  several orders of magnitude with high accuracy" at "the cost of measuring ground truth".
- **Estimator preference:** "An estimator that overestimates residual risk is preferred over one that underestimates the
  risk"; a good estimator should have "a small and positive mean bias"; the maximum-likelihood estimator of residual risk
  "is neither conservative nor accurate."
- **Mechanism (§4 excerpt):** new seeds are more likely to be chosen next yet may never have been fuzzed, while old seeds may
  have been fuzzed thousands of times, so estimates from pooled ("global") incidence frequencies are biased.
