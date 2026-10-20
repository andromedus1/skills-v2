---
source_handle: kornish-ulrich-opportunity-spaces-2011
fetched: 2026-10-20
source_url: https://leeds-faculty.colorado.edu/kornish/LKpapers/Kornish-Ulrich-Opportunity-Spaces-MgtSci-2011.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: author-hosted publisher PDF, text extracted with PyMuPDF; §1–5 read, §6–8 and appendices skimmed
---

# Opportunity Spaces in Innovation: Empirical Analysis of Large Samples of Ideas

## Source structure and scope
Laura J. Kornish (University of Colorado) and Karl T. Ulrich (Wharton). *Management Science* 57(1),
January 2011, pp. 107–128, doi 10.1287/mnsc.1100.1247 (as printed). Analyses repetition among 1,368 ideas
in five data sets generated in parallel by independent individuals (mostly course participants contributing
about five ideas each), uses human raters to judge identical/similar ideas, and estimates total opportunity-space
size with a capture–recapture-style model. Engagement depth: abstract, §1–5 read; §6 (similarity clusters and
value) partly read.

## Anchored details
- **Abstract:** "redundancy is quite small in absolute terms in our data, even for a narrowly defined domain";
  proposes "a method to extrapolate how many unique ideas would result from an unbounded effort by an unlimited
  number of comparable idea generators" — about one thousand unique ideas for the narrowest domain and more than two
  thousand for broader ones; "the ideas that are least similar to others are not generally the most valuable ones."
- **§1, footnote 1:** the number of ideas could be argued infinite "because a detail can always be tweaked"; the space
  "can be thought of as finite if ideas that are highly similar are counted together and if ideas that are highly
  'distant' are assumed to be very unlikely to be generated."
- **§1:** the method "can be used to find the total number of unique ideas or to find the total number of themes or
  'neighborhoods' of ideas."
- **§3 model:** probability the next idea is unique p_n = e^(−a·n); expected unique ideas u_n = (1/a)(1 − e^(−a·n));
  arises when there are T unique ideas "each is equally likely to be drawn" (as in Lincoln–Petersen); T = 1/a.
  Sequential draws assumed independent "as in parallel search".
- **§4 independence caveats:** within-person dependence (self-censoring or variations on a theme) and between-person
  dependence via shared experience; "Our analysis assumes a particular generating process and attempts to estimate
  the size of the opportunity space to which it has access. Different processes would result in different sizes"
  (e.g. children vs engineers vs surgeons generating surgical-instrument ideas). Ideas are independent only "in the
  sense that the generation of idea N does not depend on an observation of ideas 1 through N−1".
- **§5.1 identity judgement:** a pair is "identical" when enough raters who saw it say so; majority threshold (50% of
  exposed raters) and consensus threshold (70%) — "arbitrary cutoffs for the definition of identical, which is why we
  report results for two different thresholds"; outlier raters who formed extremely large "identical" groups were
  excluded above the 95th percentile of group size.
- **§5.1 results:** at consensus threshold, 85–90% of ideas in four data sets were identical to no other; in the
  narrowest domain (Classroom Technologies), 68%.
- **§5.2, Table 4 (consensus threshold):** e.g. Classroom Technologies N = 311, u = 271, T ≈ 1,103 (95% interval
  806–1,493); Web-Based Products N = 249, u = 238, T ≈ 2,735 (1,493–4,762). Dawkins's (1991) approximation
  u²/(2(n−u)) underestimates T by ~10% (four sets) and ~20% (fifth), as reported. "The confidence intervals are wide,
  but appropriately so". Fig. 4: 765 ideas required to reach T/2 for Classroom Technologies; 1,895 for Web-Based.
- **§5.2 resolution qualifier:** "the identical threshold defines a level of resolution beyond which two ideas are
  categorized as the same idea", so T is "the total number of ideas that are distinct enough from one another to exceed
  that threshold."
- **§5.4, relaxing equal likelihood:** using the empirical clique-size distribution, "The estimates of T do not change much
  ... In every case, accounting for the nonuniform distribution raises the estimate somewhat" (Table 5, e.g. 1,103 → 1,192).
- **§5.5:** simulated self-censoring of five ideas per person leaves predicted unique counts "virtually identical".
