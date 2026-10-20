---
source_handle: falessi-odc-feasibility-2006
fetched: 2026-10-20
source_url: https://www.scitepress.org/Papers/2006/13112/13112.pdf
provenance: source-direct
substrate_confidence: source-direct
---

# Exploring Feasibility of Software Defects Orthogonal Classification

Davide Falessi, Giovanni Cantone (Univ. of Roma "Tor Vergata"). Proceedings of the First
International Conference on Software and Data Technologies (ICSOFT 2006), pp. 107–117,
DOI 10.5220/0001311201070117 (as printed on p. 107). Full text read (11 pp.).

## Source structure and scope
Controlled experiment: 112 sophomore students (110 analysed after two outliers removed),
six hours of training, classifying 24 seeded-defect code segments (Java and C++) by IBM
ODC v5.11 "Defect Type" (seven categories incl. null) over three hours; 2,600+ data
fields.

## Anchored details
- **§1.1:** cites prior ODC agreement studies with divergent findings — El Emam &
  Wieczorek report high cohesion; Henningsson & Wohlin (2004, eight subjects, thirty
  defects) report "there might be subjectivity in classification".
- **§1.2:** many empirical works assume "defects can be classified objectively, whatever
  the classification model might be. In the absence of enough evidence for such an
  assumption, all those empirical results could be questioned."
- **§3 measures:** Effectiveness = share of the most frequent categorization; Orthogonality
  = share of subjects assigning exactly one category (not zero or two); Discrepancy =
  average probability a categorization differs from others' for the same defect;
  Affinity = confusion between pairs of categories.
- **§4.1.1 / §6:** mean effectiveness 69%; orthogonality 97%.
- **§5.1.4:** discrepancy averaged 43% (theoretical max 86%), "exactly the mean between the
  discrepancy's minimum and maximum theoretic values; as a result, ODC seems to be quite
  dependent from the categorizers' subjectivity"; discrepancy fell from 60% to 17% as
  training grew.
- **§5.1.5 / §6:** strongly affine (confused) categories: Assignment/Initialization,
  Algorithm/Method, Interface/OO Message; Interface/OO Message given in place of
  Relationship; Algorithm/Method in place of Checking — confirming Henningsson & Wohlin;
  calls for improved category definitions.
- **§5.2 threats:** few defect samples (12 per language, two per category); students not
  professionals; small code segments; possible participant interaction.
- **§6:** expectation that experts approach objective categorization "still needs empirical
  evidence".
