---
source_handle: kang-dse-equivalence-2010
fetched: 2026-10-20
source_url: https://www.microsoft.com/en-us/research/publication/approach-effective-design-space-exploration/
provenance: source-direct
substrate_confidence: abstract-only
---

# An Approach for Effective Design Space Exploration (Kang, Jackson & Schulte)

## Source structure and scope
Eunsuk Kang, Ethan Jackson, Wolfram Schulte; Microsoft Research publication page (record 323066, read
via the MSR JSON API). Engagement depth: abstract only; method details, evaluation and venue/year were
not read from the source. (Shaw & Petre 2024 also summarise this work.)

## Anchored details
- **Abstract, sentence 1:** "Design space exploration (DSE) refers to the activity of exploring design
  alternatives prior to implementation."
- **Abstract, problem:** "The main challenge in DSE arises from the sheer size of the design space ...
  a large system has millions, if not billions, of possibilities, and so enumerating every point in the
  design space is prohibitive."
- **Abstract, key idea:** "many of the design candidates may be considered equivalent as far as the user
  is concerned, and so only a small subset of the space needs to be explored. Our approach takes the
  user-defined notion of equivalence, and generates symmetry breaking predicates to ensure that the
  underlying exploration engine does not sample multiple equivalent design candidates."
- **Abstract, implementation:** integrated into the DSE framework FORMULA, "which uses an SMT solver to
  solve a set of global design constraints and search for valid design instances."
