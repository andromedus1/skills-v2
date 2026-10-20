---
source_handle: nickerson-taxonomy-development-method-2013
fetched: 2026-10-20
source_url: https://d-nb.info/1256597325/34
provenance: source-direct
substrate_confidence: source-direct
---

# A method for taxonomy development and its application in information systems

Robert C. Nickerson, Upkar Varshney, Jan Muntermann. Full text read (24-page PDF,
printed journal pages 336–359 visible as running folios 337–354 in the body; the
fetched PDF text does not print a journal masthead). Venue as reported by a citing
source (Lösser, Oberländer & Rau 2019): European Journal of Information Systems, 2013.

## Source structure and scope
Literature survey of 73 IS/CS/business papers proposing taxonomies (top-30 AIS-ranked
journals plus ICIS/AMCIS/ECIS/PACIS/HICSS, up to 2009); a formal problem statement
(definition of taxonomy, qualitative attributes of a useful taxonomy, required qualities
of a development method); the seven-step iterative method (Figure 1); a worked
demonstration on mobile applications; discussion and future research.

## Anchored details
- **Survey (p. 339–340, Table 1):** 73 papers; approaches classified inductive
  (statistical 14, informal 13), deductive 19, intuitive 24, other 3. "over 40% (30)
  of the surveyed papers" did not identify the method used; "nearly one-third (24)"
  classed intuitive. "There is no agreement on what represents an appropriate number of
  dimensions." No relationship found between the term used (taxonomy vs typology) and
  the development approach. Morphological analysis and use of existing taxonomies are
  noted among "other" approaches.
- **Terminology (p. 338–339):** Bailey (1994) distinguishes taxonomies (empirically
  derived) from typologies (conceptually derived); Bailey's conceptual approach builds by
  "substruction" (start from one type, add dimensions) or "reduction" (start from an
  extensive typology, eliminate dimensions until parsimonious) (attributed to Bailey
  1994, p. 24). Bailey's three-level model (conceptual, empirical, indicator) offers
  conceptual-to-empirical or empirical-to-conceptual routes. Authors opt for the single
  term "taxonomy" for both.
- **Definition (p. 340):** "A taxonomy T is a set of n dimensions Di (i = 1, …, n) each
  consisting of ki (ki ≥ 2) mutually exclusive and collectively exhaustive
  characteristics Cij (j = 1, …, ki) such that each object under consideration has one
  and only one Cij for each Di." (p. 341): "The mutual exclusive restriction means that
  no object can have two different characteristics in a dimension. The collectively
  exhaustive restriction means that each object must have one of the characteristics in a
  dimension."
- **No "best" taxonomy (p. 341):** "We want to develop useful taxonomies, but not
  necessarily 'best' or 'correct' ones, as these cannot be defined and, in fact, may be
  moving targets". Quotes Bailey: "a classification is no better than the dimensions or
  variables on which it is based"; lists Bailey's (1994, p. 34) typology weaknesses:
  lack of mutual exclusivity and collective exhaustivity, lack of parsimony, lack of
  changeability, arbitrary or ad hoc criteria, descriptive rather than explanatory.
- **Qualitative attributes (p. 341–342):** concise, robust, comprehensive, extendible,
  explanatory. Comprehensive has two readings: classify all known objects in the domain
  (empirical taxonomies) vs include all dimensions of the objects of interest (conceptual
  taxonomies). Robust "can conflict with the conciseness attribute". "These attributes
  form the necessary conditions for a taxonomy to be useful, but they do not necessarily
  identify the sufficient conditions." Only sufficient condition offered: "a taxonomy is
  useful if others use it. Clearly, this condition is tautological."
- **Method qualities (p. 342):** must reduce "arbitrary or ad hoc dimensions"; "There must
  be an ending condition in the taxonomy development method that says when to stop".
- **Meta-characteristic (p. 343):** "the most comprehensive characteristic that will serve
  as the basis for the choice of characteristics in the taxonomy. Each characteristic
  should be a logical consequence of the meta-characteristic." Chosen from purpose and
  expected users; guards against "naïve empiricism" (Aldenderfer & Blashfield). Worked
  computer-platform example: different purposes yield different meta-characteristics and
  different taxonomies. "The choice of the meta-characteristic must be done carefully as
  it impacts critically the resulting taxonomy." Authors report the meta-characteristic
  "sometimes does not become clear until part way through".
- **Ending conditions (p. 343–344):** fundamental objective condition = definition
  satisfied (MECE dimensions). Table 2, eight further objective conditions: (1) all
  objects or a representative sample examined; (2) no object merged or split in the last
  iteration; (3) at least one object classified under every characteristic of every
  dimension (else a "null" characteristic); (4) no new dimensions or characteristics added
  in the last iteration; (5) no dimensions or characteristics merged or split in the last
  iteration; (6) every dimension unique; (7) every characteristic unique within its
  dimension; (8) each cell (combination of characteristics) unique. "This list is not
  exhaustive". Table 3 subjective conditions with questions: concise (possible objective
  criterion: dimensions within "seven plus or minus two", Miller 1956), robust,
  comprehensive ("Can all objects or a (random) sample of objects within the domain of
  interest be classified? Are all dimensions of the objects of interest identified?"),
  extendible, explanatory. "Depending on the chosen ending conditions, the method may
  generate somewhat different taxonomies".
- **Approach choice (p. 345):** little data + strong domain knowledge → conceptual-to-
  empirical; little knowledge + much data → empirical-to-conceptual; little of both →
  investigate the domain before taxonomy work. Switching approach in later iterations
  gives "a different perspective".
- **E2C (p. 345–346):** subset of objects ("random sample, a systematic sample, a
  convenience sample, or some other type"); characteristics must follow from the
  meta-characteristic and "must, however, discriminate among the objects; a characteristic
  that has the same value for all or nearly all objects is of no use"; Delphi suggested
  for multiple researchers. **C2E (p. 346):** "Since this is a deductive process, little
  guidance can be given"; test: "Are there objects that have each of the characteristics
  in each dimension? If not, then the dimension may not be appropriate."
- **Evaluation (p. 346–347):** usefulness evaluation after building; "evaluating
  usefulness may come down to seeing if others use it"; if not useful, restart "perhaps
  with a different meta-characteristic".
- **Demonstration (p. 347–352):** mobile applications; meta-characteristic "High-level
  interaction between the application user and the application"; only two objective
  ending conditions used "for simplicity" (no new dimensions in last iteration; no
  additional applications need examining). Six iterations (E2C, E2C, C2E, E2C, C2E, E2C);
  15 applications drawn as convenience samples from two literature sources; final
  taxonomy 7 dimensions. Iteration 6 (E2C) examined three further applications (mobile
  auctions and financial services, mobile distance education, mobile ticketing), found no
  new characteristics or dimensions, so objective conditions met;
  "the taxonomy appears to be comprehensive". Voids in the taxonomy are read as
  opportunities for new applications (p. 353, observation 8).
- **Judgment and limits (p. 354–355):** "Even with the method that we propose the
  judgment of the researcher is required" — meta-characteristic choice, ending conditions,
  path choice, object subsets and conceptualization of dimensions "all require human
  judgment". Demonstrated "in only one domain". Future work: making ending conditions
  "more objective"; "multiple taxonomies may be developed for a domain even when starting
  with the same meta-characteristic. How to compare different taxonomies … is an open
  question"; merging taxonomies from different researchers.
