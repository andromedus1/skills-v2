---
source_handle: shaw-petre-design-spaces-2024
fetched: 2026-10-20
source_url: https://arxiv.org/abs/2407.18502
provenance: source-direct
substrate_confidence: source-direct
---

# Design Spaces and How Software Designers Use Them: a sampler (Shaw & Petre 2024)

## Source structure and scope
Mary Shaw (CMU) and Marian Petre (Open University); Designing '24 workshop (ACM, doi
10.1145/3643660.3643941), arXiv 2407.18502; 8 pages read in full. Sections: 1 What are design spaces?;
2 Structured design spaces (2.1–2.5); 3 Integrative design spaces (3.1–3.3); 4 How designers use design
spaces (4.1–4.4); 5 Conclusion. The authors state it "is not a comprehensive survey, let alone a
systematic review" (§5) — a curated sampler of examples.

## Anchored details
- **§1:** a design space is a perspective chosen on the "space of possibilities" to "reduce the number of
  alternatives and dependencies". Cites Woodbury and Burrow: worthy designs are "a vanishingly small subset
  of the space ... the problem is not whether a good design exists but whether it is accessible to a
  designer searching the space." Cites Schön: more variables "than can be represented in a finite model" —
  "Hence design spaces are helpful—but incomplete."
- **§1 (structured vs integrative):** structured spaces associated with explicit knowledge, depth-first
  search, "treatment of decisions as independent", reductionist reasoning; integrative spaces with tacit
  knowledge, breadth-first search, attention to dependencies, holistic reasoning; "In both cases, designers
  often revise the aspects under consideration as the design evolves".
- **§2 definition quoted from Shaw's earlier work:** "a design space is a discrete Cartesian space in which
  the dimensions correspond to design decisions, the values on each dimension are the choices for the
  corresponding decision, and points in the space correspond to complete design solutions". Structured
  approaches may assume independence among choices.
- **§2 (dimension selection):** "Defining a design space explicitly entails selecting which dimensions to
  consider ... the design dimensions of interest are highly dependent on context, and they are likely to
  change as the designer's understanding of the problem evolves."
- **§2.1:** design spaces used to compare existing designs are "less subject to the risk of
  oversimplification than other uses, because the current set of designs is known"; Shaw compared three
  teams' traffic-simulator designs — all three made different decisions on where signals attach. Römer &
  Mattern compared 15 wireless sensor network implementations on 14 dimensions; Sima derived a 4-dimension
  hierarchical space from 26 RISC and 14 CISC processors (as reported by Shaw & Petre).
- **§2.2:** Shaw & Clements "Boxology" classified architecture styles into six major classes (data flow,
  call-and-return, interacting processes, data-centered repositories, data-sharing, hierarchical), each
  with variants; produced selection rules of thumb.
- **§2.3:** Lane interviewed designers of six systems to build UI design spaces — functional space 25
  dimensions (3–5 alternatives each), structural 19 dimensions (2–7 each); rules recommending structural
  choices were "validated ... statistically against the actual designs produced by his subjects" (as
  reported). Baum et al. added correlations (dependence, incompatibility, tradeoff) between dimensions.
- **§2.5:** hardware/software DSE uses genetic algorithms, pruning, ILP; Kang et al. "systematically
  eliminated equivalent candidates, based on a user-defined equivalence".
- **§3.2:** Penders et al. inter-dependency rules between dimensions "form a navigation guide"; claimed
  advantage "to enforce a systematic decision for each dimension in the space".
- **§4.1:** design spaces "help designers to check for coverage by prompting them to consider alternatives
  systematically within the space", and help "reduce the alternatives in a reasoned way".
- **§4.2:** Brooks notes the rational systematic-search model is "vastly oversimplified: real designers
  just don't work that way"; designers "satisfice, stopping the search when an acceptable, if not optimal
  solution is found". "A hierarchical representation ... tends to encourage making decisions in the order
  embedded in the hierarchy."
- **§4.3:** Goel and Pirolli protocol studies (as reported): problem structuring recurs periodically
  throughout the task, not only at the start.
- **Footnote 1:** Petre and van der Hoek identified 66 expert-designer practices; e.g. "Experts generate
  alternatives. #45", "Experts keep options open. #30", "Experts know when to stop. #42".
