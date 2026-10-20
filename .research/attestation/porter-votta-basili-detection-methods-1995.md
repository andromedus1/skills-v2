---
source_handle: porter-votta-basili-detection-methods-1995
fetched: 2026-10-20
source_url: https://drum.lib.umd.edu/bitstreams/332d6328-bdce-4726-9102-e00bac748f9a/download
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: University of Maryland DRUM repository PDF (technical-report version), text extracted with PyMuPDF; the font encoding dropped most digits, so numeric results (percentages, counts) were NOT recoverable and are not recorded here
---

# Comparing Detection Methods for Software Requirements Inspections: A Replicated Experiment

## Source structure and scope
Adam A. Porter, Lawrence G. Votta Jr., Victor R. Basili (University of Maryland; AT&T Bell Laboratories).
Published in IEEE Transactions on Software Engineering 21(6), 1995 (venue per the search-result listing; the
repository PDF carries no venue line). Randomized partial-factorial experiment: forty-eight computer-science
graduate students in sixteen three-person teams inspected two requirements specifications (water level
monitoring, automobile cruise control) using Ad Hoc, Checklist or Scenario (defect-based) methods.
Engagement depth: abstract, method (§II.B fault taxonomy and method relationships), §IV conclusions and §V
read; numeric values unreadable in extraction.

## Anchored details
- **Abstract:** usual Ad Hoc or Checklist methods "force all reviewers to rely on nonsystematic techniques to search
  for a wide variety of faults"; hypothesis that a Scenario method, "in which each reviewer uses different, systematic
  techniques to search for different, specific classes of faults", performs better. Results: "(1) the Scenario method
  had a higher fault detection rate than either Ad Hoc or Checklist methods, (2) Scenario reviewers were more
  effective at detecting the faults their scenarios are designed to uncover, and were no less effective at detecting
  other faults than both Ad Hoc or Checklist reviewers, (3) Checklist reviewers were no more effective than Ad Hoc
  reviewers, and (4) Collection meetings produced no net improvement in the fault detection rate — meeting gains were
  offset by meeting losses."
- **§II.B fault taxonomy:** "Faults are divided into two broad types: omission — in which important information is
  left unstated and commission — in which incorrect, redundant, or ambiguous information is put into the SRS by the
  author." Omission subtypes in the figure: missing functionality, missing performance, missing environment, missing
  interface; commission: ambiguous information, inconsistent information, incorrect or extra functionality, wrong
  section. The checklist is a refinement of the taxonomy; scenarios replace checklist items with procedures. Scenarios
  used: data type inconsistencies, incorrect functionality, missing (or ambiguous) functionality.
- **Fig. (method relationships):** "Moving from Ad Hoc to Checklist to Scenario there is more detail and less
  coverage"; "the Checklist is a subset of the Ad Hoc and the Scenarios are a subset of the Checklist."
- **§IV conclusions:** scenarios "helped reviewers focus on specific fault classes" without compromising detection of
  other classes; "the scenarios appeared to be better suited to the fault profile of the WLMS than the CRUISE. This
  indicates that poorly designed scenarios may lead to poor inspection performance"; "The Checklist method — the
  industry standard, was no more effective than the Ad Hoc detection method"; conclusions "apply only to the
  experimental setting".
- **§V future work:** "In many instances a single reviewer found a fault, but the fault was not subsequently recorded at
  the collection meeting" — asks whether reviewers forget or are "talked out of the fault at the team meeting".
