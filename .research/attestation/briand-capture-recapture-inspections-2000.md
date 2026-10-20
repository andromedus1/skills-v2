---
source_handle: briand-capture-recapture-inspections-2000
fetched: 2026-10-20
source_url: https://www.ehealthinformation.ca/web/default/files/wp-files/2001-A-Comprehensive-Evaluation.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: NRC Canada technical-report PDF (ERB-1084, March 2001; states it is also published in IEEE Trans. Software Eng. 26(6):518-540, 2000), text extracted with PyMuPDF; tables partly read
---

# A Comprehensive Evaluation of Capture-Recapture Models for Estimating Software Defect Content

## Source structure and scope
L.C. Briand, K. El-Emam, B.G. Freimut, O. Laitenberger. NRC Canada Institute for Information
Technology report ERB-1084 (March 2001), whose cover states "Also published in IEEE Trans. Software
Eng. 26(6): 518-540; 2000." Empirical evaluation of biological capture-recapture models (M0, Mt, Mh,
Mth) and estimators (MLE, Jackknife, Chao) for predicting total defects from real requirements-inspection
data where the true defect count is known (NASA/GSFC PBR experiments, Basili et al. 1996). Engagement
depth: abstract, §1–3 (models, assumptions, data), Discussion and Conclusions read; per-condition result
tables in §4 not audited.

## Anchored details
- **Abstract:** few studies "compare the actual number of remaining defects to the one predicted by a
  capture-recapture model on real software engineering artifacts". "Our results show that models are
  strongly affected by the number of inspectors ... When the number of inspectors is too small, no model is
  sufficiently accurate and underestimation may be substantial." Recommends "a model taking into account that
  defects have different probabilities of being detected and the corresponding Jackknife estimator"; calibrating
  by historical relative error has "theoretical limitations ... which were then confirmed by the data".
- **§1:** each inspector is a trapping occasion; a defect found by one inspector and found again by another is
  "recaptured". Alternatives to estimation for re-inspection decisions: participants' subjective judgement
  (reported median relative error of zero in El Emam et al. 2000, as cited, but reliance "dilutes the
  transparency"), historical-average benchmarks, density thresholds. Summary: models "tend to underestimate
  the number of defects. In particular, using a small number of inspectors (defined as less than four) will lead
  to rather inaccurate estimates."
- **§2.1 assumptions (Lincoln–Petersen):** closure valid for inspections; equal capture probability "may be
  violated, for example, when there are some defects that are easier to detect than others" — "the third
  assumption ... requires most attention". Footnote: "Some of the assumptions are also violated when the models
  and their estimators are applied in biology."
- **§2 models:** M0 (no variation), Mh (defects differ in detectability; inspectors equal), Mt (inspectors differ;
  defects equal), Mth (both). Chao's Mh (1987) and Mt (1989) estimators "have been designed for situations in
  which many animals were detected only once or twice" — possibly appropriate with few or weak inspectors.
- **§3, number of occasions:** biology rule of thumb of five trapping occasions, "though a number of 7 or 10 was
  deemed more appropriate", but "no quantitative justification or evidence is provided for this recommendation"
  (as reported by the authors).
- **§3 data:** ATM (17 pp., 29 defects), PG (16 pp., 27 defects), two NASA documents (27 pp., 15 defects);
  defects classified as omission, ambiguous information, incorrect fact, extraneous, miscellaneous.
  "a particular defect could manifest itself in several places ... two or more inspectors could localize the same
  defect in different places and describe it differently, which could bias some of the capture-recapture
  estimates"; two individuals consolidated defect lists "to avoid duplicate defect counts".
- **Discussion and Conclusions:** "capture-recapture models ought not be used with less than 4 inspectors unless
  shown to work in a particular environment" (Miller 1998, as cited, found some models workable with 3). For 4–5
  inspectors, Mh with the Jackknife estimator "most appropriate based on absolute bias, failure rate, and tendency
  for extreme overestimation"; Mh-type median relative error "between 5% and 16%". No "compelling evidence" that
  the two-source Mth model did better. "In most of the cases, we have observed that the models underestimate the
  total number of defects." Some models had a high failure rate (no estimate) with few inspectors; "several models
  should be used to prevent failure to obtain an estimate."
