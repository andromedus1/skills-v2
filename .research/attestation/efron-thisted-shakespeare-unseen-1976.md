---
source_handle: efron-thisted-shakespeare-unseen-1976
fetched: 2026-10-20
source_url: https://www.gwern.net/docs/1976-efron.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: third-party mirror of a JSTOR scan (Biometrika 1976), OCR text extracted with PyMuPDF; tables partly read, some OCR noise
---

# Estimating the number of unseen species: How many words did Shakespeare know?

## Source structure and scope
Bradley Efron and Ronald Thisted (Stanford). *Biometrika* (1976), 63, 3, pp. 435–47 (as printed). Applies
Fisher's parametric empirical-Bayes (negative binomial) model and Good & Toulmin's nonparametric estimator,
augmented by linear programming, to Shakespeare's word-type frequencies. Engagement depth: summary, §1, §2
(estimator form), §6–7 (lower/upper bounds) and conclusions read; derivations skimmed.

## Anchored details
- **Summary:** "Shakespeare wrote 31 534 different words, of which 14376 appear only once, 4343 twice, etc. The
  question considered is how many words he knew but did not use." Conclusion: the models "are equivalent to
  supposing that Shakespeare knew at least 35 000 more words."
- **§1:** total of 884,647 words; a "type" is "any distinguishable arrangement of letters. Thus, 'girl' is a different
  type from 'girls'" — the count depends on that definition of a distinct item. For an equal-size new corpus (t = 1),
  Fisher's model and Good–Toulmin "both estimate about 11460 expected new word types, with an expected error of less
  than 150." For t = ∞: "No upper bound is possible, but we will demonstrate a lower bound".
- **§2:** the Good–Toulmin series "is useless for values of t larger than one. The geometrically increasing magnitude of
  t^x produces wild oscillations"; Euler's transformation is used to force convergence.
- **§6:** "As t gets large it becomes more and more difficult to estimate a reasonable upper bound" — e.g. a million word
  types each with tiny rate would barely affect the data yet would appear in a much larger corpus. "the Shakespeare
  data, unaided by parametric assumptions like Fisher's assumption 1, runs out of predictive power for t greater than 10."
- **§7, Table 7 (LP bounds, x0 = 9, c = 1):** t = 1: lower 11,205 / upper 11,732; t = 10: 34,640 / 86,600; t = 20:
  35,530 / 167,454; t = ∞: 35,554 / ∞ — bounds diverge as t grows.
- **Conclusions excerpt:** Fisher's negative binomial "fits the data extraordinarily well. However the linear programming
  approach produces other empirical Bayes solutions which also fit the observed data, and give smaller estimates of A(t)
  for t > 1"; all methods give very similar answers for small t.
