---
source_handle: inspection-team-size-experiment
fetched: 2026-10-18
source_url: https://userweb.cs.txstate.edu/~rp31/papersSQ/PorterEtAl_TSE.pdf
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (18-page PDF, text extracted; figures not read as images)"
---

# An Experiment to Assess the Cost-Benefits of Code Inspections in Large Scale Software Development

## Source structure and scope
Adam A. Porter, Harvey P. Siy, Carol A. Toman, Lawrence G. Votta. IEEE Transactions on Software
Engineering, vol. 23, no. 6, June 1997, pp. 329-346 (as printed on the fetched PDF; a copy hosted on
a Texas State University course page). A randomized field experiment on a live Lucent Technologies
compiler project: 88 code inspections over 18 months (June 1994 to December 1995), reviewers drawn
from a pool of 11 experienced developers. Treatments are labelled sessions x persons, with or without
repair between sessions (e.g. 1sX2p, 2sX1pN, 2sX2pR). Effectiveness is observed defect density
(defects per KNCSL, "thousand noncommentary source lines"); total defect content was unknowable.

## Anchored details
- **Abstract:** three variables were randomized: "1) the number of reviewers on each inspection team
  (1, 2, or 4), 2) the number of teams inspecting the code unit (1 or 2), and 3) the requirement that
  defects be repaired between the first and second team's inspections." Headline:

  > Our results showed that these treatments did not significantly influence the defect detection effectiveness, but that certain combinations of changes dramatically increased the inspection interval.

- **Section 1.1, "Team Size":** inspections are usually done by "a team of four to six reviewers"; Buck
  (uncontrolled data, cited by the authors) showed "no difference in the effectiveness of three, four, and
  five-person teams".
- **Section 2.4.4:** treatments were discontinued if too ineffective or slow; "several treatments were
  discontinued because they were either ineffective (1sX1p treatment), or because they were taking too long
  to complete (all two-session treatments which required repair between sessions)."
- **Section 3.7, "Analysis of Effectiveness Data":** "There was no difference between two- and four-person
  inspections, but both performed better than one-person inspections." With total reviewers held constant,
  splitting into two teams made "no differences in effectiveness". Repair between sessions "didn't increase
  effectiveness when the team size was one, but did when the team size was two", which the authors say
  "should be viewed with caution" (only four 2sX2pR and five 2sX1pR inspections). Observations:
  "increasing the number of reviewers did not necessarily lead to increased defect discovery".
- **Section 4 (summary list):** "Increasing team size does not always improve performance. (1sX1p < 1sX2p,
  but 1sX2p = 1sX4p)" and "Repairing defects between sessions does not guarantee improved inspection
  performance."
- **Section 5.2, "Main Results":**

  > Team Size (H1) . We found no difference in the interval or effectiveness of inspections of two- or four-person teams. The effectiveness of one-reviewer teams was poorer than both of the others.

  For practitioners, "reducing the default number of reviewers from four to two may significantly reduce
  effort without increasing interval or reducing effectiveness." On serializing sessions (H3): "repairing
  defects in between multiple sessions had no effect on observed defect density, but in some cases increased
  interval dramatically."
- **Section 5.1, "Fundamental Issues in Industrial" experimentation:** effectiveness ideally is the proportion of defects found, but "we never know how
  many defects are in the original code unit"; defect counts do not weight severity.
- **Section 3.5, "Analysis of Effort Data":** "effort increases with the total number of reviewers while the
  number of sessions and the repair between sessions have no effect"; four-reviewer inspections required
  significantly more effort than two-reviewer inspections, and two-reviewer more than one-reviewer. Median
  effort across treatments was "about 22 person-hours per KNCSL".
