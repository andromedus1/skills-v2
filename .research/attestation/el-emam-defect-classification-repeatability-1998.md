---
source_handle: el-emam-defect-classification-repeatability-1998
fetched: 2026-10-20
source_url: https://www.ehealthinformation.ca/web/default/files/wp-files/isern-98-09.pdf
provenance: source-direct
substrate_confidence: source-direct
---

# The Repeatability of Code Defect Classifications

Khaled El Emam and Isabella Wieczorek, Fraunhofer IESE. International Software
Engineering Research Network Technical Report ISERN-98-09. Full text read (21 pp.).

## Source structure and scope
Reliability study of a defect classification scheme adapted from IBM's Orthogonal Defect
Classification (ODC) / SEI Personal Software Process, using real code-inspection data
(two inspector pairs, 605 logged defects; 99 and 41 defects found by both inspectors).

## Anchored details
- **§1:** "since defect classifications are subjective, it is necessary to ensure that they
  are repeatable"; ODC's semantic classification is believed "likely to be accurate", but
  "While special care has been taken in defining classification schemes that are believed
  to be repeatable, this has not been, to our knowledge, empirically demonstrated through
  systematic investigation." Low-reliability class variables make chi-square analyses
  "quite misleading".
- **§2.2:** the scheme was locally adapted — two ODC classes removed as not applicable,
  four classes added (Data, Environment, Naming Conventions, Understandability); 11
  classes with guiding questions (Table 2).
- **§2.3:** Cohen's kappa used; interpretation guide: below 0.4 inadequate, above 0.6 good,
  above 0.75 excellent. Footnote: agreement differs from association.
- **§3.1:** only 23% and 24% of defects were found by both inspectors (inspector
  specialisation).
- **§3.2, Table 6:** kappa 0.66 (data set 1) and 0.82 (data set 2), both significant.
- **§3.3:** Monte Carlo sensitivity analysis (1000 iterations) — simulated means 0.80 and
  0.76; probability of kappa ≤ 0.6 "close to zero".
- **§3.4:** disagreement concentrated between "Data" and "Assignment"; developers reported
  difficulty distinguishing them; merging them raised data-set-1 kappa from 0.66 to 0.73;
  recommendation: refine or merge the two classes.
- **§3.5 limitations:** one document type (code), one activity (inspections), one project;
  "early to make statements on the reliability of this defect classification scheme for
  other types of documents and for other activities."
