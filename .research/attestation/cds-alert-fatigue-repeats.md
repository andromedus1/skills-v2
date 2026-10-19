---
source_handle: cds-alert-fatigue-repeats
fetched: 2026-10-18
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5387195/
provenance: source-direct
substrate_confidence: source-direct
engagement_depth: "full-text (PMC HTML article, converted to text; Tables 1-2 read; Figure 1 read via caption)"
---

# Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system

## Source structure and scope
Jessica S Ancker and co-authors (Weill Cornell Medical College and others). BMC Med Inform Decis Mak. 2017 Apr
10;17:36, doi 10.1186/s12911-017-0430-8 (as read on PMC). Retrospective cohort study of electronic health record
data, January 2010 to June 2013, 112 ambulatory primary care clinicians in a network of federally qualified health
centers using one commercial EHR; 1,266,325 best-practice advisories (BPAs, clinical reminders) and 326,203
drug-drug and drug-allergy alerts. Tests two alert-fatigue mechanisms: cognitive overload and desensitization over
time. Clinician-level negative binomial models; results as incident rate ratios (IRR).

## Anchored details
- **Background:** distinguishes "cognitive overload" (too much information to separate relevant from irrelevant) from
  "desensitization" (declining response with repeated exposure over time). Notes that an earlier systematic review
  "noted that across studies there was no evidence of a relationship between alert volume and percentage overridden".
- **Methods (proxy for uninformative alerts):** "repeated alerts, defined as alerts presented to the same clinician for
  the same patient in the same year"; the authors note manual review of informativeness "was not feasible".
- **Results, Table 1:** median percent of BPAs accepted per clinician 19.4%; median percent of drug alerts accepted
  per clinician 0.0 (IQR 0.0-0.3).
- **Abstract, Results:**

  > Likelihood of reminder acceptance dropped by 30% for each additional reminder received per encounter, and by 10% for each five percentage point increase in proportion of repeated reminders.

  "Alert acceptance was associated with work complexity and repeated alerts, but not with the amount of work." "The
  newly deployed reminders did not show a pattern of declining response rates over time, which would have been
  consistent with desensitization." Nurse practitioners "were 4 times as likely to accept drug alerts as physicians."
- **Results (repeats):** "if the first instance was overridden, the chance of subsequent instances being overridden
  was 87.9%" for BPAs (51.9% if the first was accepted); for drug alerts 99.9% vs 58.4%.
- **Results (drug alerts):** effect sizes similar to BPAs "but statistical significance was lower because of low
  acceptance rates (overall less than 1%".
- **Desensitization analysis:** only 6 newly deployed alerts qualified; "Only one of 6 alerts showed an early peak in
  response rate followed by a drop". That alert was the 2012 flu immunization reminder for patients over 65, and "it
  seems likely that the decrease was due to patients reporting that they had received immunizations elsewhere."
- **Limitations:** observational, novel unvalidated metrics, single commercial EHR "with interruptive alerts"; "no
  manual review was conducted to distinguish appropriate from inappropriate overrides"; "we cannot conclude
  definitively that reducing override rates would reduce rate of inappropriate overrides."
