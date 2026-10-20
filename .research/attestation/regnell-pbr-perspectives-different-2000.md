---
source_handle: regnell-pbr-perspectives-different-2000
fetched: 2026-10-20
source_url: https://lup.lub.lu.se/search/files/2596645/777880.pdf
provenance: source-direct
substrate_confidence: source-direct
extraction_pipeline: Lund University repository PDF (author manuscript with LUP cover page), text extracted with pypdf; figures not read
---

# Are the Perspectives Really Different? Further Experimentation on Scenario-Based Reading of Requirements

## Source structure and scope
Björn Regnell, Per Runeson, Thomas Thelin (Lund University). *Empirical Software Engineering* 5(4),
331–356, 2000, DOI 10.1023/A:1009848320066 (citation as printed on the repository cover page).
Controlled experiment (partial replication using the University of Maryland PBR lab package): 30 MSc
students, 10 per perspective (user / designer / tester), two requirements documents (ATM, parking
garage). Also summarises nine prior scenario-based reading experiments. Engagement depth: full text
read except appendix data tables.

## Anchored details
- **Abstract:** "The basic assumption behind PBR is that the perspectives find different defects and a
  combination of several perspectives detects more defects compared to the same amount of reading with a
  single perspective." Results: "(1) there is no significant difference among the three perspectives in
  terms of defect detection rate and number of defects found per hour, (2) there is no significant
  difference in the defect coverage of the three perspectives, and (3) a simulation study shows that 30
  subjects is enough to detect relatively small perspective differences". "a combination of multiple
  perspectives may not give higher coverage of the defects compared to single-perspective reading".
- **§1 definitions:** Ad Hoc ("no guidance"), Checklist ("a list of issues and questions, capturing the
  knowledge of previous inspections"), Scenario-based reading (reviewers follow scenarios "which aim at
  constructing a model, instead of just passive reading"); variants Defect-Based Reading (DBR, specific
  defect classes) and Perspective-Based Reading (PBR, points of view of document users).
- **§2 prior studies, as summarised by the authors (cite-through):**
  - Maryland-95 (Porter et al. 1995): DBR higher detection than Ad Hoc or Checklist; DBR higher only for
    "those defects that the scenarios were designed to uncover, while all three methods have similar
    detection rates for other defects"; "Checklist reviewers do not have significantly higher detection rates
    than Ad Hoc reviewers"; collection meetings "no net improvement".
  - NASA (Basili et al. 1996): PBR beat Ad Hoc on general documents for individuals, not on NASA-specific
    documents; reviewers with more experience did not have higher detection rates.
  - Kaiserslautern (Ciolkowski et al. 1997): PBR beat Ad Hoc; "detection rates of five different defect
    classes are not significantly different among the perspectives."
  - Bari (Fusaro et al. 1997), Linköping (Sandahl et al. 1998): DBR not significantly better than Ad
    Hoc/Checklist; Strathclyde (Miller et al. 1998) mixed by document; Lucent (Porter and Votta 1998)
    replicated Maryland-95 with professionals.
  - Hayes (1999) meta-analysis: "effect sizes for the inspection methods are inhomogeneous across the
    experiments". "The results of the different studies vary substantially."
- **§3:** PBR's purpose is "that the perspectives detect different kinds of defects in order to minimise the
  overlap among the reviewers"; if all find the same defects, causes may be an inappropriate approach,
  insufficient scenario support, or a need for other perspectives. Links to capture-recapture defect-content
  estimation, which "uses the overlap among the defects that the reviewers find to estimate the number of
  remaining defects" (Eick et al. 1992; Miller 1999, as cited).
- **§6.2:** "the defect findings of each perspective seem similarly spread over the defect space"; chi-square
  test on which defects each perspective found.
- **§7:** none of H0,EFF, H0,RATE, H0,FOUND ("The perspectives are assumed to find the same defects") could be
  rejected; "the advantages of PBR can be questioned". Individual PBR detection rate 0.252 vs NASA study 0.249
  (pilot) and 0.321 (main run).
- **§8 threats / caveat:** unrealistic setting, non-optimal perspectives, motivation/training, small n; "A
  single study, like this, is no sufficient basis for changing the attitudes towards PBR."
