---
title: "Campaign evaluation — solution-space-decomposition (round 1)"
provenance: agent-verification
gate: evaluate
updated: 2026-10-20
target: parent.md + clusters/generation.md + clusters/completeness.md
evaluator: isolated Claude Opus (xhigh) via peeragent, empty working directory, discipline + brief + seed + synthesis inlined
verdict: NEEDS-REVISION
---


# Campaign evaluation: solution-space decomposition

**Verdict: `NEEDS-REVISION`.** The synthesis is careful, well hedged and close to approvable. The problems are bounded corrections. None needs a reversal.

- **Gap in the seed's question:** the seed asks for stopping rules. The synthesis says which stopping rules fail, but never says when the challenge should stop and depth research begin.
- **Weakened join seams between the cluster files and parent.md:**
  - One side of a contradiction was dropped.
  - A cluster open question became a recommendation without notice.
  - Recommendations 6, 8 and 9 conflict over sequencing.
- **Groundedness posture:** several claims look better grounded than they are. Absence claims are cited to sources that cannot show an absence, an `extends` marker was lost between files, and some qualifiers were removed.

I used only the seed, the discipline bundle, the role brief and the three synthesis files. I verified no citations.

---

## 1. Coverage

**Strengths.** The synthesis covers all of the following:
- Generation strategies (§2).
- Tests for whether an approach is genuinely different (§3).
- Completeness signals and failed stopping rules (§4).
- Recommendations mapped to the four steps (§5).

It also answers "which completeness signal" with recommendation 9's frame-relative descriptive statement. The scope states that transfer is analogical, and the open questions and revisit conditions are useful.

**Gaps:**

- **C1: stopping rules have no positive answer.** §4 says that "no new items in N", saturation and taxonomy ending conditions fail or are unvalidated. Recommendation 9 says how to report the result. The synthesis never says what decides whether the process iterates the challenge or commissions depth research. It also does not list this as an open question for human judgement. Discipline §6 allows that route when an absolute value is load-bearing. The seed names stopping rules directly, so this is the largest coverage gap.
- **C2: no feedback path from step 4 to step 1.** Recommendation 11 asks depth facets to report whether new sources open new categories. Nothing says what happens next, such as reopening the map or re-running the challenge. That path matters because the synthesis's own evidence says missed items can add categories (Kitchenham). Step 4 has one recommendation; steps 1–3 have three or more each.
- **C3: recommendation 9 omits signals the completeness cluster calls measured.** The cluster's transfer observations list four "something is missing" signals:
  - recall against an independently built known set;
  - overlap between independent repetitions;
  - new items opening new categories;
  - yield per iteration.

  It also lists a circularity guard: keep the known set out of strategy-building (hausner, cochrane). Recommendation 9 drops the known-set signal and yield per iteration, and does not carry the guard. It also lists six components without naming the main signal the challenge should report.
- **C4: one positive stopping band is missing.** The quasi-gold-standard band of 70–80% (zhang) appears in the completeness cluster but not in parent.md. It applies to items, not families. Even so, it should either appear with that limit or be excluded explicitly.
- **C5: a scope choice for steps 1–2 was dropped.** RIPL defines a landscape as "an entire population", while WIPO advises "a handful of the most important technical approaches". This directly affects how the domain map and sample are scoped, but it is not in parent.md.
- **Minor:** two advocated moves from the generation cluster are missing from the recommendations without explanation:
  - SDM's best-consequence-per-objective, then hybrids;
  - separating the person who abstracts the problem from the person who searches.

## 2. Coherence

- **H1: recommendations 6, 8 and 9 conflict over sequencing.**
  - Recommendation 6 has the challenger enumerate families before seeing the sample.
  - Recommendation 8 then shows the challenger candidate families from the map.
  - Recommendation 9 reports the overlap between passes, but does not say which challenger list to use. If the list includes candidates the challenger saw in step 8, the overlap is inflated by exposure.
  - By §4's own known-set limit, judging membership of map candidates can only find gaps between the sample and the map. It cannot find families the map itself missed.

  Neither limit is stated.
- **H2: the fault-tree evidence is misframed.** Parent §1 and the generation cluster's §1 say "Generators overrate their own completeness" and cite the fault-tree study (fischhoff). As both files describe it, participants judged a pruned tree they were shown. They did not judge their own lists. On that description, the finding is about reviewers of a presented structure underweighting what it omits. That is a risk for recommendation 8 and support for recommendation 6. It is not evidence about generators.
- **H3: recommendation 9's rationale combines two different problems.**
  - The tension row is about a single diversity-seeking pass producing singletons by design.
  - Recommendation 9 extends that to "deliberately varied challenge passes", meaning different cues across passes. The synthesis itself says Chao-type estimates remain lower bounds when detection rates differ.
  - The perspective-based-reading row is the more relevant conflict: passes designed to minimise overlap work against capture–recapture.

  Recommendation 9 also keeps an option open ("apply … only when its sampling assumptions are justified") without saying whether any design in the four steps qualifies. The process produces at most an author sample, one challenger and an optional second pass. Set that against the synthesis's own "at least two passes" and "fewer than four inspectors" guidance and say plainly whether an estimate is ever available.
- **H4: a self-contradiction on certification.** Parent §4 says "Certification-style reporting gives confidence across a range of targets". The summary says estimates "are not certification", and the cluster gives the source's position as confidence across targets "rather than one verdict".
- **H5: sample coverage needs a caveat.** §4 "What small samples support" presents sample coverage as estimable. The next bullet says diversity-seeking removes the repetition that frequency estimators rely on. The completeness table lists Good–Turing coverage next to the f1/f2 estimators. The document does not say whether sample coverage shares that limit, so a reader may treat it as the safe figure to report.
- **H6: the pooling evidence may be circular.** The pooling result reads "each listed 36% of 39". If the 39-item reference is the pooled union, then "more complete than any one" is true by definition. The synthesis's own cap on relative recall ("actual recall could be close to zero") would then apply. The Disconfirming entry "Supported in a weaker form" therefore says little about the challenger's real task: finding families that every lister missed.
- **H7 (minor): vocabulary is inconsistent.**
  - "Charter sample" is never defined and differs from the seed's "comparison sample".
  - The declared evidence levels are advocated, demonstrated and measured, but the tables also use "Designed" and "Mixed".
  - Confidence depths vary: `abstract` and `abstract-only`.
  - §5 uses deployment terms such as "challenger" without defining them. That is acceptable for adoption recommendations, but a reader without the deployment's context could not interpret them, which fails discipline §2's project-framing test.

## 3. Contradictions

There is a structured Contradictions section, and most rows are substantive. The `incommensurable` row on LLM diversity is used well, and the far-field `contradicts` row is a real disagreement. The problems are at the join seams:

- **X1: one side of a contradiction is missing (most material).** The generation cluster records a tension:
  - Exposure to AI ideas narrowed collective diversity (doshi-hauser).
  - Exposure increased it in a dynamic pool (ashkinaze, `{confidence: search-summary}`).

  parent.md never cites doshi-hauser. Only the widening countercase survives, in the summary, key findings and §2. As a result, the only evidence on exposure that reaches the parent is the lowest-depth source, and it points one way. That is the evidence base for recommendation 6, whose premise is that a challenger should not be exposed to the sample. This is resolution by omission.
- **X2: an open question became a recommendation.** The generation cluster passes this open question to the parent: "Whether a challenger shown the sample it is challenging is anchored by it". parent.md drops it from its Open questions and recommends the answer in recommendation 6. The support is a transfer from upfront examples in an objectives study. The recommendation can stay, but the open question should be restored and the recommendation marked `extends`.
- **X3: other relevant tensions were not carried forward:**
  - celebrity personas versus ordinary personas, which affects recommendation 7's choice of cues;
  - RIPL versus WIPO (see C5);
  - few distinct alternatives versus objectives raising the number of alternatives, which affects recommendation 4;
  - Kastner versus Rücker on whether capture–recapture is usable.

  Leaving some out is reasonable compression, but these bear directly on the recommendations.
- The categories `qualifies` row compares one source with itself, not two sources. That is acceptable but worth knowing.

## 4. Groundedness (how claims present; candidates for spot-check)

There are no composed effort estimates. "Lowest similarity of any prompt" is a superlative that stays within one study.

- **G1: absence claims are cited as if sources showed them.**
  - Parent §4 bullet 1 says "landscape, taxonomy and design-space practice measures item recall …" and cites zhang and sampson. Judging by their handles, these cover software-engineering search and Cochrane recall, not taxonomy or design-space practice.
  - The §2 table says "Never tested against later-found objects". "Never" is universal; the cluster only says none was found, and drops szopinski.
  - "No coverage comparison" and "No locatable sweet spot" are unmarked.

  All of these need `{inferred: absence}` and wording limited to the attested corpus.
- **G2: prose notes stand in for markers.** Examples include "(coverage-estimation specialist, marked inferred)", "(LLM specialist, marked `extends`)" and "The landscape-mapping specialist found …". Specialist briefs are analytical-tier material, and a downstream check reads markers, not prose. Use the closed vocabulary instead.
- **G3: the `extends` marker was lost.** Calderon on recall and judging-not-enumerating on omission are marked `extends` in the generation cluster but appear unmarked in parent §1 as explanations.
- **G4: the human part of the omission claim is unsupported.** The summary and key findings say "Reviewers and models detect omissions far less often". Parent §4 cites only a model study (the 6–7x figure). The cluster's human evidence is one abstract-level experiment that reports "more", not 6–7x.
- **G5: one case is presented as "a measured signal".** Parent §4 drops the cluster's "one case" label for Kitchenham, and the inference is unmarked.
- **G6: the 39% figure is reframed without a marker.** The key finding turns a screening heuristic (50 consecutive irrelevant items, or a baseline rate) into "the last pass added nothing". The cluster also groups two rules together. Mark this as a transfer, and check whether 39% applies to each rule or to both combined.
- **G7: Gettys et al. (1987) has no visible grounding.** It appears only in Revisit-if, in both parent.md and the generation cluster. No cite-through in either body names it, and acquisition candidates must point to a fetched source.
- **G8: some handles map to more than one `{N}`:**

  | Handle | Numbers used |
  |---|---|
  | meincke-prompting-idea-variance-2024 | {117}, {300}, {363} |
  | judging-not-enumerating-omissions-2026 | {321}, {366} |
  | kitchenham-slr-repeatability-2011 | {260}, {375} |
  | ritchey-psm-gma-2006 | {101}, {263} |

  Confirm that each pair resolves to the same source and attestation.
- **G9: other dropped qualifiers:**
  - "no quality loss" no longer says "in the successful arms";
  - "fixed agent lenses" is listed as a measured remedy, but the cluster says it recovered about 26% of the diversity lost in debate;
  - the cluster key finding gives "18–22% unseen" without "median";
  - the "Categories" row is labelled "Measured" although the source cannot separate the category effect from the second pass.
- **G10: the Disconfirming analysis covers only the negative propositions.** It does not test the positive prescriptions:
  - the purpose-first key (one abstract-only source plus one 38-worker study);
  - the warning-plus-target second pass (one population);
  - judging over enumerating (the "with a reference" condition);
  - full field coverage (demonstrated only).

## 5. Priority-ordered recommendations

These are all corrections that keep the existing positions. Log them in Revisions.

1. **Address stopping (C1, C2).** Add either a grounded stopping or escalation decision for the challenge, or an explicit open question for human judgement. Also add the feedback path from depth facets back to the map.
2. **Restore the doshi-hauser side of the exposure contradiction (X1)** in the Contradictions section and the key findings, and reconsider recommendation 6's evidence base.
3. **Restore the challenger-anchoring open question (X2)** and mark recommendation 6 `extends`.
4. **Fix the sequencing of recommendations 6, 8 and 9 (H1, C3).**
   - Compute overlap only from the challenger's list made before exposure.
   - State that map-candidate judging cannot find gaps in the map itself.
   - Add the held-out known-set signal and circularity guard, and name the main signal.
5. **Reframe the fault-tree evidence (H2)** as evidence about reviewers of a presented structure, and link it to recommendation 8.
6. **Make recommendation 9's estimator conditions concrete (H3, H5).** Name which assumption each design violates, and say whether any pass design in the four steps supports an estimate. State whether the diversity-seeking caveat applies to sample coverage.
7. **Fix the omission-detection claim (G4)** so it rests on models, or add the human evidence with its depth.
8. **Fix the marker problems (G1–G3, G5, G6):** absence markers, closed vocabulary in place of specialist notes, the lost `extends`, "one case", and the transfer marker on the 39% figure.
9. **Ground or drop Gettys et al. (G7), and reconcile the duplicate `{N}` numbers (G8).**
10. **Carry the decision-relevant tensions (C5, X3)** on scope, personas and capture–recapture usability, and add disconfirming entries for the positive prescriptions (G10).
11. **Minor fixes:** "Certification-style" (H4), the vocabulary issues (H7), and the qualifiers in G9.

## Spot-checks (questions I'd have liked to check in the attestations)

- **bond-carlson-keeney-objectives-2008:** is the 39-objective reference the pooled union?
- **fischhoff:** did participants generate lists or evaluate a tree they were shown?
- **judging-not-enumerating:** were human reviewers tested, and what does "with a reference" mean?
- **callaghan-2020:** does 39% apply to each rule or to both combined?
- **creative-mad-debate:** what baseline is the 26% recovery measured against?
- **Gettys 1987:** which attestation names it?
- **The four `{N}` pairs in G8.**
- **zhang and sampson:** do they support the claim about taxonomy and design-space practice?
- **nickerson and szopinski:** do they support "never tested"?