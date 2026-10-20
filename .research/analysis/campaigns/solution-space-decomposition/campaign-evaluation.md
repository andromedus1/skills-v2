---
title: "Campaign evaluation — solution-space-decomposition (round 1)"
provenance: agent-verification
gate: evaluate
updated: 2026-10-20
target: parent.md + clusters/generation.md + clusters/completeness.md
evaluator: isolated Claude Opus (xhigh) via peeragent, empty working directory, discipline + brief + seed + synthesis inlined
verdict: APPROVED (round 3)
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

---

# Round 2 (2026-10-20)


# Campaign evaluation, round 2: solution-space decomposition

**Verdict: `NEEDS-REVISION`.** The remaining work is narrow. parent.md now answers the stopping question, includes both sides of the exposure contradiction, and fixes most marker problems. Two material issues remain. Both can be corrected in place; neither needs a reversal.

1. **N1.** Recommendations 9 and 10 do not separate families missing from the map from families that are on the map but not sampled. Recommendation 10 also contradicts recommendation 9 on which held-out check triggers escalation.
2. **N2.** The cluster files still contain five claims that parent.md has corrected. The generation cluster's revisions log also records one of those corrections as done when it is not.

Inputs: the seed, the discipline bundle, the role brief, my round-1 evaluation and the three revised files. I verified no citations.

## Round-1 findings

"Partly" means parent.md is fixed but a cluster file still has the uncorrected claim, or only part of the finding was addressed.

| Finding | Status | Reason |
|---|---|---|
| C1 stopping | Resolved | §4 now says there is no attested family-level stopping rule (`{inferred: absence}`). Rec 10 gives an escalation trigger, marked as an inference. Open questions includes "when to stop". The decision to start depth research is left to human judgement, which is the route discipline §6 allows. The trigger's wording has a problem (N1). |
| C2 feedback path | Resolved | Rec 12 sends a new category back as a map refresh and a re-challenge. Rec 10 does the same for the challenge. |
| C3 signals in rec 9 | Resolved | The primary signal is named. Held-out known families and new families per pass are added, and rec 3 carries the circularity guard. How the primary signal is defined is a problem (N1). |
| C4 QGS band | Resolved | §4 bullet 1 includes it, limited to items. |
| C5 scope choice | Resolved | Covered in rec 2 and in a Contradictions row. |
| Minor: SDM and abstractor/searcher moves | Partly | Both now appear in §2 as advocated moves. §5 still neither adopts nor excludes them. |
| H1 sequencing | Resolved | Steps (a)–(d) are ordered. Overlap is computed only from the challenger's pre-exposure list. The limit of map-candidate judging is stated, and fischhoff is linked to 8(d). |
| H2 fault tree | Partly | Parent §1 and generation §1 are reframed. But the generation cluster's Transfer-relevant observations still cites fischhoff for "Generators' own judgements of completeness … are unreliable", and that file's revisions log records H2 as done. |
| H3 estimator conditions | Resolved | Rec 9 now says plainly that no model-based estimate, including sample coverage, is supported for these passes (`{inferred: aggregate}`). There is a reasoning gap, listed in the notes. |
| H4 certification | Resolved | — |
| H5 sample coverage | Resolved | §4 adds the shared-assumption caveat, and rec 9 excludes sample coverage. |
| H6 pooling | Resolved | The circularity is stated in the §2 table and in Disconfirming. My round-1 question ("if the 39 is the pooled union") is now stated as fact, so it needs a spot-check. "On average" was dropped from the 36% figure. |
| H7 vocabulary | Partly | The four steps and "charter sample" are defined. Still inconsistent: confidence depths use both `abstract` and `abstract-only`. The labels "Prescribed" (parent §2) and "designed" (completeness table) are outside the declared set. "Author" (recs 7 and 9) and "operator" (rec 10) are not defined. |
| X1 exposure contradiction | Resolved in parent | doshi-hauser now appears in the key findings, §2 and Contradictions. The generation cluster still has the problem (N2). |
| X2 anchoring question | Resolved | The open question is restored, and rec 6 is marked. |
| X3 other tensions | Resolved | Personas, RIPL/WIPO, Kastner/Rücker, and few distinct alternatives versus more alternatives are all carried. Recs 2, 4 and 7 refer to them. |
| G1 absence claims | Resolved | `{inferred: absence}` is on the table cells and in §4. §4 bullet 1 is reworded to "Search practice". |
| G2 prose notes | Resolved | The claim-level notes about specialists are gone. Scope-level lines about specialists remain in the clusters (see notes). |
| G3 lost `extends` | Resolved | A marker is restored. Its form is questionable (see notes). |
| G4 omission claim | Partly | parent.md now rests the claim on models, with the human study at abstract depth. The completeness cluster's summary and key finding still say "humans and models". |
| G5 one case | Resolved | Now says "measured in one case". |
| G6 39% figure | Partly | parent.md splits the figure by rule and marks the transfer. The completeness cluster's key finding still applies "stopping when the last run added nothing" to both rules, with no marker. |
| G7 Gettys | Partly | parent.md's Revisit-if now cites Gettys through delmissier, which needs a spot-check. The generation cluster's Revisit-if still names Gettys et al. (1987), and nothing in that file cites through to it. |
| G8 duplicate `{N}` | Resolved as asked | The log says they were verified. Duplicates remain within single files: kitchenham {260} and {375} in the completeness cluster, and meincke {117} and {300} in the generation cluster. This is cosmetic. |
| G9 dropped qualifiers | Resolved | "Successful arms", "median" and the mixed label on the categories row are restored. The lens figure is restated, but its baseline needs a note. |
| G10 disconfirming entries | Resolved | Entries are added for the four positive prescriptions. |

## New issues

### Material

**N1. The primary signal and the escalation trigger do not separate gaps in the map from gaps in the sample (recs 9 and 10).**

- Rec 4 draws the sample to cover every value of each dimension, not every family. Families that are on the map but not sampled are therefore normal and intended.
- Rec 9's primary signal is "families in the challenger's pre-exposure list that the sample lacks". That count lumps those intended exclusions together with families the map never had. Rec 8(d) makes exactly this distinction, but rec 9 drops it.
- Rec 10 escalates when "the challenge … misses held-out known families". Rec 9, however, reports "held-out known families the map missed", and rec 10's remedy is "refresh the map". As written, the trigger tests the challenger's sensitivity, but the remedy repairs the map.
- **Fix:**
  - Report the primary count in two parts: families absent from the map, and families on the map but not sampled. For the second part, say whether the family carries a dimension value the sample does not cover.
  - Trigger a map refresh on the first part and on held-out families the map missed.
  - If the held-out set is also meant to test the challenger, say so separately. When the challenger misses held-out families, a quiet challenge is weak evidence. The remedy then is a stronger challenge, not a map refresh.

This is the seed's central decision: which signal the challenge reports, and when to stop.

**N2. The cluster files are not reconciled with the parent's corrections.** Discipline §8 says a correction is not discharged until it appears at every tier. These cluster passages still say what parent.md has corrected:

- **Generation cluster, Transfer-relevant observations:** fischhoff is still used as evidence about generators (H2), while the file's revisions log says H2 is done.
- **Generation cluster summary, key finding 3 and §2.1 "Tested narrowing conditions":** exposure to AI ideas appears only as the widening case. That is ashkinaze, at search-summary depth, with no marker in the summary or the key finding. The narrowing case (doshi-hauser) appears only in the Contradictions table. This one-sidedness was already there in round 1 and I did not flag it. It is the same problem X1 fixed in parent.md.
- **Completeness cluster summary and key finding:** omission is called the weaker capability "for humans and models" (G4).
- **Completeness cluster key finding:** the 39% figure is applied to "stopping when the last run added nothing" for both rules, with no transfer marker (G6).
- **Generation cluster Revisit-if:** Gettys is named without a cite-through (G7).

**Fix:** correct each passage in place, add revisions-log entries, and correct the H2 line in the generation cluster's log.

### Notes (minor)

- **Marker form.** `{inferred: extends}` merges two separate markers from the bundle. It appears in parent §1, §4, the §5 header and recs 6, 10 and 12, and in generation §1. Use `extends` for claims that go beyond the source, and keep `{inferred: <verb>}` for claims composed across attestations. The revisions log says rec 6 is "marked `extends`".
- **Rec 9's reasoning.**
  - It says the passes "fall short of capture–recapture's independent-capture assumption" without saying why. That comes right after rec 6 designs the challenger to be independent.
  - §4 also says Chao-type estimates remain lower bounds under heterogeneous detection. So "differing cues create heterogeneous detection" does not by itself rule out an estimate.
  - The synthesis already has the real reasons; state them:
    - the sample is a purposive draw from the map, not a capture;
    - there are only two or three occasions;
    - shared model priors may correlate the passes (artificial-hivemind).
- **Numeric targets.** Rec 7's numeric target is designed to force additions. Count additions only after rec 5's family-versus-variation adjudication. Record whether each came from the unforced pass or the targeted pass, so the target does not drive the primary signal.
- **Lens-anchored debate.** The 26.2% gain is measured over homogeneous debate, which itself fell below single-agent generation. The §2 table lists it as a widening strategy without saying whether it beats independent generation.
- **36% figure.** "Each executive listed 36%" drops "on average".
- **§4 heading.** "Stopping rules that fail" includes taxonomy ending conditions that are untested, not shown to fail.
- **Kastner/Rücker row.** In parent.md's Contradictions table this row says "both abstract-level" in prose instead of using `{confidence: abstract}` markers.
- **Del Missier/Schweizer row.** In parent.md this `qualifies` row reads as agreement. It dropped the generation cluster's opposing side: Johnson and Raab, as reported, found poorer choices for time-pressured experts.
- **Purpose-first disconfirming entry.** "No contrary result was found" is an absence claim with no marker.
- **Cluster scope lines.** "Evidence levels follow the specialist briefs" and "where the specialist marked them" describe the authoring process, which fails discipline §2's agent-task-context test.

## Spot-checks

The revision introduced these new specifics. Confirm that each one is recorded in its attestation, since discipline §4 requires the detail to be there before it is cited:

- **bond-carlson-keeney-objectives-2008:** the 39-objective reference is the pooled union of the executives' lists, and 36% is an average.
- **delmissier-option-generation-ideation-2015:** names Gettys et al. (1987) as an act-generation study.
- **callaghan-statistical-stopping-2020:** 39.67% for the baseline-rate rule and 39% for the 50-consecutive-misses rule.
- **siebert-novices-press-2016:** "paper-title task".
- **fu-absencebench-omission-2025:** "with both documents available".
- **chao-colwell-chao2-inequality-2017 {350}:** sample coverage is computed from the singleton and doubleton counts. The cluster cites coverage to {351} instead.
- **creative-mad-debate-diversity-2026:** how lens-anchored debate compares with single-agent generation.
- **fischhoff-slovic-lichtenstein-fault-trees-1978:** participants judged a pruned tree they were shown; laypeople and mechanics took part.

## Priority-ordered recommendations

1. **N1:** split the primary signal into absent-from-map and on-map-but-unsampled. Make rec 10's held-out trigger consistent with rec 9, and match each trigger to the right remedy.
2. **N2:** reconcile the five cluster passages with parent.md and correct the generation cluster's H2 log entry.
3. Then the notes, starting with the marker form.

All of these are corrections, so log them in Revisions. The revision pass only needs to cover recs 9–10 and the listed cluster passages before going back into adversarial-read.

---

# Round 3 (2026-10-20, final)


# Campaign evaluation, round 3 (final check): solution-space decomposition

**Verdict: `APPROVED`.** N1 and N2 are both resolved. This revision introduced no new material issue. The items below are minor and do not block. They can be fixed and logged in a later correction pass without going back into adversarial-read.

I used only what was in the dispatch: the seed, the discipline bundle, the role brief, my round-2 evaluation and the three revised files. I could not check any citation.

## Material findings from round 2

| Finding | Status | Basis |
|---|---|---|
| **N1** primary signal and trigger | Resolved | Rec 9 now splits the primary signal into two parts: (i) families absent from the map, and (ii) families on the map but not sampled, with a check for uncovered dimension values. Intended exclusions are declared not to be gaps. Families are counted after the rec 5 adjudication, and each addition is tagged by pass. Rec 10 gives each trigger its own remedy: part (i) and held-out families absent from the map lead to a **map refresh**; part (ii) leads to a **sample revision**; a challenger that misses held-out families leads to a **stronger challenge**. Recs 9 and 10 now use the same held-out wording. |
| **N2** cluster reconciliation | Resolved | I checked all five passages. **Generation, Transfer-relevant observations:** fischhoff now concerns reviewers of a presented decomposition, and the claim about generators rests on linsey and ding. The round-1 log entry is annotated to say this was corrected in round 2. **Generation summary, key finding 3 and §2.1:** both sides of the exposure finding now appear. **Completeness summary and key finding:** the omission claim now rests on models, with the human study at abstract-only depth. **Completeness 39% key finding:** the figure is given per rule, with a transfer clause. **Generation Revisit-if:** Gettys is now a cite-through via delmissier. |

## Round-2 notes

| Note | Status |
|---|---|
| Marker form | Resolved. No `{inferred: extends}` is left in any of the three files. |
| Rec 9 reasoning | Resolved. All three reasons are stated, and the heterogeneous-detection argument is gone. One leftover: "inspection guidance advises four or more" drops the exception "unless shown to work in a particular environment", which §4 keeps. |
| Numeric targets | Resolved. Additions are counted after adjudication, and the unforced and targeted passes are recorded separately. |
| Lens-anchored debate | Resolved. The baseline is now stated. One leftover: "a comparison with single-agent generation is not attested" is an absence claim with no `{inferred: absence}` marker. |
| 36% "on average" | Resolved in both parent.md and the generation cluster. |
| §4 heading | Resolved. |
| Kastner/Rücker row | Resolved in the Contradictions table. The §4 body still uses `{confidence: abstract}` for the same sources (see the vocabulary note below). |
| Del Missier/Schweizer row | Resolved: the Johnson and Raab side is back. It adds a new specific, "less consistent", which the generation cluster does not have. This needs a spot-check. |
| Purpose-first absence marker | Resolved. |
| Cluster scope lines | Partly. The scope sections are clean. But the completeness §2 table footer still says "evidence labels follow the specialist briefs", while the completeness log says process-describing lines were removed. |

Items still marked "Partly" in the round-2 table: the SDM and abstractor/searcher moves are still neither adopted nor excluded in §5 (unchanged). The confidence vocabulary still mixes `abstract` and `abstract-only`. The G8 duplicate `{N}` numbers are cosmetic and unchanged.

## New issues

**Material:** none.

**Notes (do not block), most important first:**

1. **Re-challenges should be independent.** Rec 10's remedies ("re-challenge" and the new "stronger challenge (more distinct cues, another targeted pass)") don't say the new pass must happen before the challenger is exposed. By step (d) the challenger has seen the sample and the map candidates. "Another targeted pass" from the same challenger would then be post-exposure, which recs 6 and 8 keep out of the counts. **Fix:** add one clause: "run any re-challenge or stronger challenge as a fresh pass under recs 6–8".
2. **The part (ii) trigger rarely fires under rec 4.** If the sample meets full field coverage, no on-map family can carry an uncovered value. The sample-revision trigger then fires only when the draw failed rec 4, or when adjudication reclassified a family (rec 11). Say so. Also, full field coverage covers single values, not combinations, so part (ii) cannot flag a family whose difference lies in an uncovered combination. State that as a known limit.
3. **Wrong depth label on the exposure finding.** Parent key finding 2, and the generation summary and key finding 3, end the two-study sentence with "(abstract-level)". The body marks ashkinaze `{confidence: search-summary}`, which is shallower than abstract, and gives doshi-hauser no marker. So the label overstates the widening study's depth and understates the narrowing study's. **Fix:** "(the widening study at search-summary depth)".
4. **The pooling caveat was not carried down.** The generation summary, key finding 3, §2.1 and Disconfirming analysis still call the pooled lists "a more complete set". They omit the parent's caveat that the reference was the pooled union itself. This predates this revision and I missed it in round 2. It is the same reconciliation problem as N2, but the claim is the source's own quote and goes no further than it, so it does not block.
5. **Completeness log accuracy.** The table footer from the scope-lines row is still there despite the log entry. The same footer also puts prose inside a marker (`{inferred: aggregate — rows are composed …}`), as do the `{inferred: absence across …}` markers in two places.
6. **Smaller items:**
   - Generation §2.1 bullet 2 repeats the ashkinaze widening sentence that the section intro already gives.
   - The completeness §3.3 heading still puts the baseline-rate rule under "nothing new in the last run". The key finding is fixed.
   - The completeness key finding moves "median" from coverage to stopping points ("median … stopping points left 18–22%"). The body says median coverage at the stopping points was 78–82%.
   - Rec 9 cites kitchenham for "empty cells", which is nickerson's signal (rec 8(d)).
   - Rec 10's "gives weak evidence" should say of what: "its quiet result is weak evidence of completeness".

## Spot-checks

The round-2 spot-check list is still open, since I cannot verify it. Add one item:

- **delmissier-option-generation-ideation-2015:** Johnson and Raab, as reported, found "poorer, less consistent" choices for time-pressured experts.