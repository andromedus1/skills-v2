---
source_handle: callaghan-stopping-recommendations-2024
fetched: 2026-10-20
source_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11583672/fullTextXML
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: Europe PMC full-text XML, tag-stripped to text and read locally
---

# Computer-assisted screening in systematic evidence synthesis requires robust and well-evaluated stopping criteria

## Source structure and scope
Callaghan M, Müller-Hansen F, Bond M, Hamel C, Devane D, Kusa W, O'Mara-Eves A, Spijker R,
Stevenson M, Stansfield C, Thomas J, Minx JC. Systematic Reviews 2024 (DOI
10.1186/s13643-024-02699-7, PMC11583672). Commentary with consensus recommendations from tool
developers and guideline authors. Engagement depth: full text.

## Anchored details
- "Where machine learning-prioritised screening is employed in systematic reviews, stopping
  rules should transparently manage and communicate the risk of missing relevant studies."
- Where pragmatic/economic criteria decide stopping, "communicating the potential consequences
  for recall at that point, using complementary stopping criteria, is still beneficial".
- PRISMA amendment for ML only requires reporting automation tools "without requiring a rationale
  for stopping decisions."
- Evaluation problem: most studies simulate ML ordering on selected datasets, so "Reliability
  observed in individual evaluations may therefore be dependent on the specific experimental
  setup, or even be achieved by over-optimising the stopping criteria"; differing metrics make
  comparisons hard; "some tools recommend stopping rules based on simple heuristics which are not
  connected to any theoretical estimate of the recall achieved".
- "stopping after X consecutive records ... cannot (without further analysis) reliably inform
  users about the potential to have missed studies"; one evaluation over 100 runs found "the 5th
  percentile of recall achieved when stopping after 50 consecutive excluded records was as low as
  53%".
- "any reliable stopping criteria will require that more records are screened than the minimum
  required to meet the recall target."
- Reporting: authors should state whether they pre-set a recall target and confidence; reporting
  "confidence levels across a range of recall targets" to "give a complete picture of the risks
  of stopping at any given point".
- Evaluations "should identify the conditions under which a stopping rule cannot be relied upon";
  effects of combining criteria should be evaluated.
