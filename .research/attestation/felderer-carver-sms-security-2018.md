---
source_handle: felderer-carver-sms-security-2018
fetched: 2026-10-20
source_url: https://arxiv.org/abs/1801.06810
provenance: source-direct
substrate_confidence: source-direct
source_class: book-chapter guideline (arXiv 1801.06810v1, 21 Jan 2018); secondary synthesis of SE mapping guidelines plus a survey of ten security mapping studies
---

# Guidelines for Systematic Mapping Studies in Security Engineering (Felderer and Carver, 2018)

## Source structure and scope
Michael Felderer (University of Innsbruck) and Jeffrey C. Carver (University of Alabama);
book chapter preprint. §1.2 summarises the SE systematic mapping study (SMS) process and
guideline families; §1.3 surveys ten security-engineering mapping studies; §1.4 gives
security-specific guidance. Engagement depth: full text extracted; §1.2.1.2, §1.2.1.5,
§1.2.2, §1.4.2 and §1.4.5 read closely.

## Anchored details
- **§1.2.1.2 Searching:** methods are automated searching, manual searching of selected
  venues, backward snowballing and forward snowballing; researchers "often combine these
  methods to develop a search strategy that achieves a good level of coverage" (attributed to
  Kitchenham, Budgen and Brereton's EBSE book, ref [17]).
- **§1.2.1.2 Completeness (attributed to [17]):** "The goal of the search process is to achieve
  an acceptable level of completeness within the reviewer's constraints of time and human
  resources"; developing a search strategy "is an iterative process, involving refinement
  based on some determination of the level of completeness achieved. An essential basis for
  the subjective assessment of completeness is comparison of the search results against a
  known set of papers." The known set can come from an informal automated search, personal
  knowledge, a previous review, or a quasi-gold standard built by manual search of
  topic-specific venues over a restricted period; if the string misses known-set papers, the
  string must be modified.
- **§1.2.1.5:** the classification scheme may be revised iteratively as knowledge is gained;
  data extraction should be validated by two independent researchers extracting from the same
  papers and reconciling discrepancies.
- **§1.2.2, Table 1.1:** four guideline families — Kitchenham, Petersen, Biolchini, social
  science; Kitchenham and Petersen are most used. The Petersen 2015 update was based on "a
  systematic map of 52 mapping studies"; "researchers often combine guidelines when performing
  SMSs because the individual guidelines are not sufficient" (attributed to Petersen et al.
  2015, ref [25]).
- **§1.4.2:** "using a broad search string will help prevent premature elimination of
  potentially relevant studies"; choose synonyms (example: security -> secure, authorization,
  authentication, access control); search strings differ per venue; pilot-test the string
  using a reference set of papers known to be relevant.
- **§1.4.5:** the identified security mapping studies "rarely discuss data extraction
  explicitly". Mapping studies in a sub-field can complement classification schemes from
  baseline studies (e.g. a model-based security testing scheme extending a model-based testing
  taxonomy), allowing comparison with baseline results. Generic facets offered: subject types
  (algorithm/theory, model, language, protocol, process, tool), research-type facet (solution
  proposal, philosophical, evaluation, validation, opinion, experience) and validation types
  (experiment, case study, survey, proof, discussion/argument).
