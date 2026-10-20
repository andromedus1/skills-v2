---
title: "Solution-space decomposition: adversarial-read verification checklist"
provenance: agent-verification
gate: adversarial-read
updated: 2026-10-20
target:
  - .research/analysis/campaigns/solution-space-decomposition/parent.md
  - .research/analysis/campaigns/solution-space-decomposition/clusters/completeness.md
  - .research/analysis/campaigns/solution-space-decomposition/clusters/generation.md
verdict: NEEDS-REVISION
---

# Adversarial-read checklist

Discipline read handshake: `6408290171aaeefdf82fd3277d01558ce2b811665c427024286dbeb0f66ebbae`.
Read the complete discipline and adversarial-reader role brief; consulted CATALOGS §4.

Scope: parent, both clusters, all eight complete specialist briefs, their reference
sidecars, and all 156 unique attestations cited by those briefs. Two focused,
read-only harness agents covered the generation and completeness source pools
(75 and 86 attestations respectively, with overlap); the driving reader assessed
the parent and adjudicated findings against the relevant attestations. Also
checked the reference registry and supplied lint report: 1,429 resolved/non-broken
citations, zero broken, zero structurally thin, 250 pattern advisories. Those
mechanical results do not establish semantic support. This pass assesses the
existing attestation chains; it does not independently reacquire external papers.

Locations below are relative to
`.research/analysis/campaigns/solution-space-decomposition/`, except paths beginning
`.research/attestation/`, which are repository-relative. Line numbers refer to the
assessed inputs. Only this checklist was written. Findings are proposed corrections;
the source artifacts remain unchanged and the gate remains unsuccessful until
the required revisions are reconciled into them.

## (a) Semantic citation-chain walk

- [ ] **R1 — The adoption rule assigns an unsupported lower-bound guarantee.**
  **Claim:** `parent.md:185` says to treat *any overlap-based count* as a lower bound.
  Yet the challenger is deliberately given different cues (`parent.md:175`), and
  the parent already acknowledges that diversity-seeking sampling conflicts with
  the estimators' assumptions (`parent.md:133`).
  **Evidence:** `.research/attestation/chao-colwell-chao2-inequality-2017.md:33`
  specifies the incidence model, and `:36`, `:40`, `:53`, `:81` give the particular
  Chao estimator, equality/near-unbiasedness conditions and lower-bound interpretation.
  `.research/attestation/bron-chao-estimator-tar-2024.md:36` records the Poisson and
  independence assumptions. Other capture–recapture models can exhibit extreme
  overestimation and fail to produce an estimate
  (`.research/attestation/briand-capture-recapture-inspections-2000.md:49`).
  **Fix:** report the adjudicated observed union, additions, overlap, classification
  boundary and uncovered cells descriptively. Distinguish that observed count from
  an estimated total. Apply a named model-based lower-bound estimate only when its
  sampling assumptions are justified, with uncertainty and transfer limits; do not
  assign a statistical bound to arbitrary deliberately varied challenge passes.
  Reconcile the broader phrasing in `clusters/completeness.md:230` as well.

- [ ] **R2 — Estimator requirements and the negative validation finding lose their scope.**
  **Claims:** `parent.md:117`, `parent.md:16`, `parent.md:23`,
  `clusters/completeness.md:12`, `clusters/completeness.md:20` and
  `clusters/completeness.md:116` generalize a two-pass/random-remainder requirement
  to every estimator. `specialists/search-completeness.md:145` is an upstream
  instance. Separately, `parent.md:15` says no field has a validated estimator for
  completeness of a set of kinds; `clusters/completeness.md:9` and `:17` similarly
  deny measured kind-completeness practice without restricting the kind of kinds.
  **Evidence:** Cochrane's two-search statement is specifically about
  capture–recapture (`.research/attestation/cochrane-handbook-ch4-searching-2025.md:40`).
  Abundance data use individual frequencies from a sample, while incidence data
  use repeated sampling units
  (`.research/attestation/chao-hill-numbers-rarefaction-2014.md:29`, `:39`;
  `.research/attestation/chao-colwell-chao2-inequality-2017.md:30`). Ecological
  estimation has measured evaluations in its own setting
  (`.research/attestation/chao-sufficient-sampling-2009.md:13`, `:20`;
  `.research/attestation/chao-hill-numbers-rarefaction-2014.md:36`).
  **Fix:** state the input/independence requirements separately for capture–recapture,
  incidence estimators, abundance estimators and random-remainder screening tests.
  Restrict the absence finding to validation for **families of methods or approaches
  in the attested corpus**, as `clusters/completeness.md:61` already does. Preserve
  the distinction between probability-mass coverage and the fraction of kinds
  represented. Update both summaries and the originating specialist sentence.

- [ ] **R3 — Taxonomy ending conditions are reduced to last-iteration stability.**
  **Claims:** `parent.md:129` says ending conditions check *only* the last iteration;
  `clusters/completeness.md:139` calls them stability checks over that iteration.
  The compressed table entry at `clusters/completeness.md:79` inherits the omission.
  **Evidence:** `.research/attestation/nickerson-taxonomy-development-method-2013.md:68`
  records MECE, examination of all objects or a representative sample, populated
  characteristics and uniqueness checks alongside iteration-stability conditions.
  Its `:96` distinguishes the demonstration's selected two objective conditions
  from the full proposed set.
  **Fix:** say that *some* conditions check last-iteration stability and that the
  demonstration used a selected subset. Retain the broader conditions and the
  narrower supported conclusion: they do not validate coverage of unseen families.

- [ ] **R4 — A specific cited sampling-unit count never reached its attestation.**
  **Claims:** `clusters/completeness.md:122`,
  `specialists/coverage-estimation.md:77` and `:204` give an example with 12 units.
  **Evidence:** `.research/attestation/chao-colwell-chao2-inequality-2017.md:76`
  records Q1/Q2, 36.3 and the interval 29.1–68.8, but not the number of sampling units;
  no other part of that attestation supplies 12. This is read-but-not-attested,
  rather than a broken handle or an empty attestation.
  **Fix:** return to the fetched source's §7.3/sample-design passage, confirm and
  record the unit count with its anchor in the attestation before retaining the
  citation. If source-true, extend the substrate rather than deleting an accurate
  detail to hide the gap. If the source does not confirm it, correct the claim and
  record that correction explicitly.

R5–R9 below identify additional semantic-support failures encountered in this walk.
Other reviewed headline specifics—including the warning/target increments, screening
failure percentages, purpose/mechanism experiment and omission benchmark results—are
present in their cited attestations; their domains and qualifications still matter.

## (b) Claim-shapes the mechanical lint missed

- [ ] **R5 — The human recovery fraction is composed into a claim about LLMs.**
  **Claim:** `parent.md:8` attributes roughly one-third-to-one-half recovery of
  later-recognised alternatives to unaided generation by people **or language models**.
  **Evidence:** `.research/attestation/bond-carlson-keeney-improving-objectives-2010.md:52`
  records 30–50% for human objectives;
  `.research/attestation/siebert-keeney-alternatives-2015.md:22` records less than
  half for human alternatives, at abstract-only depth. The LLM attestations instead
  measure response similarity, distinct outputs or category combinations; they do
  not attest that recovery fraction against later recognition.
  **Fix:** split the human recovery result from the LLM collective-homogeneity
  result. Do not reuse the human denominator or fraction for model-generated families.

- [ ] **R6 — Pooling is given an unsupported necessary condition.**
  **Claims:** `parent.md:75` says pooling helps *only across different generators*;
  `clusters/generation.md:93` says only if they draw from different regions;
  `clusters/generation.md:216` calls ensemble benefits disconfirmed.
  `specialists/llm-ideation-diversity.md:231` contains the upstream restriction.
  **Evidence:** `.research/attestation/artificial-hivemind-homogeneity-2025.md:24`
  reports high average embedding similarity, not zero marginal discoveries;
  `:28` says ensembles **may not** provide diversity, and `:33` states measurement
  and mechanism limits. Same-model cue changes produced gains
  (`.research/attestation/deng-brucks-toubia-llm-idea-diversity-barriers-2026.md:29`).
  **Fix:** replace the categorical restriction with: changing model identity alone
  does not establish independent coverage; assess overlap and marginal additions
  under distinct prompts/cues. Distinguish model identity, statistical independence
  and semantic diversity; none is a substitute for the others.

The global conditional/analogical disclaimer at `parent.md:146` is useful and is
not treated as absent. Recommendations such as marginal dimension coverage,
principle-level family naming and candidate judgement remain proposed transfers,
not validated methodology-review procedures. Keep that status explicit when the
primer extracts individual recommendations: full-field coverage is coverage of
parameter values, not all configurations (`.research/attestation/ritchey-psm-gma-2006.md:42`);
membership-judgement evidence has one-shot/reference limitations
(`.research/attestation/judging-not-enumerating-omissions-2026.md:29`, `:32`);
placeholder evidence concerns surface deletion with original and edited documents
available (`.research/attestation/fu-absencebench-omission-2025.md:17`, `:38`).

## (c) Coherence-read for smoothed contradictions

- [ ] **R7 — A universal exposure/consensus mechanism survives despite counterevidence.**
  **Claims:** `clusters/generation.md:10`, `:19`, `:74`, `:76` and `:234` compress
  heterogeneous results into an exposure/consensus ordering effect. `parent.md:12`,
  `:21` and especially the recommendation's rationale at `parent.md:174` inherit it.
  **Evidence:** `.research/attestation/creative-mad-debate-diversity-2026.md:19`
  explicitly records voting matching direct-generation diversity **despite the same
  consensus mechanism**, isolating debate dynamics. High AI-example exposure increased
  collective diversity in another setting
  (`.research/attestation/ashkinaze-ai-ideas-collective-diversity-2024.md:16`, `:19`;
  abstract-only, metrics unaudited). The latter appears in the generation contradiction
  table at `:209` but does not constrain the main headline.
  **Fix:** name the tested conditions—upfront examples in the objectives experiment,
  similarity-feedback prompts and standard multi-agent debate—rather than asserting
  exposure or consensus is inherently narrowing. Bring the voting control and the
  qualified exposure countercase into the argument and summaries. Retain independent
  generation before discussion as Bond's prescription
  (`.research/attestation/bond-carlson-keeney-improving-objectives-2010.md:55`).
  In §5 #6 replace the consensus rationale with the measured standard-debate result.

R1 also exposes internal smoothing: the lower-bound adoption rule suppresses the
diversity-versus-estimation tension retained in `parent.md:133` and `:202`. R2
similarly reconciles the summaries with the narrower body. Near/far analogy and
incommensurable human/LLM metrics remain visibly distinguished; no additional
material smoothing finding was established for those comparisons.

## (d) Noise-domination / relevance-weighting

- [ ] **Carry the better-supporting and disconfirming attestations into the revised claims.**
  This job examined the full retrieved source pools, not only the parent/cluster
  citation lists. R2 requires the abundance-data account from Chao 2014 beside the
  Cochrane/Callaghan evidence; those sources cannot support an all-estimator rule.
  R6 requires the same-model cue evidence rather than treating Hivemind's similarity
  result as a no-pooling theorem. R7 requires the voting control already present
  in its cited attestation and the qualified Ashkinaze countercase currently confined
  to a contradiction row. Exact locations and fixes are given in those findings.
  No further material case of a less-relevant citation displacing a better retrieved
  attestation was established.

## (e) Quote-context and qualifier walk

- [ ] **R8 — Correlational findings become causal quantity/quality rules.**
  **Claims:** `clusters/generation.md:189`, `:206`, `parent.md:205` and
  `specialists/decision-option-generation.md:13` say more options lower/lowered mean
  quality and raise/raised maximum quality or originality.
  **Evidence:** `.research/attestation/delmissier-option-generation-ideation-2015.md:55`
  records problem-dependent correlations, with mean-quality associations controlling
  maximum quality; direct fluency–choice-quality correlations were nonsignificant.
  `.research/attestation/schweizer-creative-option-generation-2016.md:28` explicitly
  records between-person correlations. The decision brief body preserves this at
  `specialists/decision-option-generation.md:197`, but its summary and downstream
  syntheses strengthen the interpretation.
  **Fix:** use "was associated with," retain the problem dependence and conditioning,
  and distinguish mean quality, maximum quality and decision quality. These data
  do not establish that reducing a charter sample improves decisions.

- [ ] **R9 — Restore source-depth, attribution and conditional qualifiers at these loci.**
  - `parent.md:165`: "preferring few clearly distinct families" cites the 2016
    Bayreuth release without its secondary-report qualification or task context.
    `.research/attestation/siebert-novices-press-2016.md:12` and `:21` specify an
    institutional report of a publication-title task, not an audited primary study
    of approach-family samples. Preserve "as reported by the university release"
    and title-set context; retain the conditional transfer. The cluster already
    models the provenance correctly at `clusters/generation.md:192`.
  - `parent.md:80`: "Too abstract lowers fit" cites a review without identifying
    the underlying cite-through. The attestation explicitly attributes that result
    to Zahner et al., and says the appropriate balance is unclear
    (`.research/attestation/vasconcelos-crilly-inspiration-fixation-2016.md:42`).
    Attribute it as the review's report of Zahner et al.; do not present it as a
    directly audited primary finding or an established optimal abstraction level.
  - `parent.md:86`: the more-time null cites the 2015 press release alongside the
    full-text objectives result without separating provenance. Identify which
    alternative-generation result is reported by the release
    (`.research/attestation/siebert-keeney-press-2015.md:12`, `:29`).
  - `clusters/completeness.md:123`: the quotation "ought not be used with less than
    4 inspectors" drops "unless shown to work in a particular environment";
    the same passage notes cited models workable with three
    (`.research/attestation/briand-capture-recapture-inspections-2000.md:49`).
    Restore that exception and study scope, preserving the empirical small-inspector
    warning without turning it into a universal minimum; reconcile the compressed
    wording at `clusters/completeness.md:20` and `parent.md:121`.
  - `parent.md:79`, `:204` and `clusters/generation.md:114`, `:203` imply an
    established categories/timing advantage. The attestation cannot separate the
    first second-pass result from the second opportunity itself and finds no reliable
    category benefit over a motivated deeper review in the later experiment
    (`.research/attestation/bond-carlson-keeney-improving-objectives-2010.md:31`, `:45`).
    Retain the observed intervention gains but qualify the category-specific/timing
    explanation with those two limitations.

R3 and R6 are additional qualifier losses. Reduced-depth sources generally retain
their cited specifics; an abstract or short record is not automatically a thin
attestation. No separate material verbatim-misquotation finding was established
beyond the inspector quotation's omitted exception.

## (f) Analytical-tier-inheritance walk

- [x] No analytical artifact was found masquerading as a source-handle target;
  the supplied lint contains no `intra-program-resolved` citation. Cluster and
  specialist names are framing/input descriptions, not attestation substitutes.
  However, source-direct handles do not prevent **semantic drift through the
  lineage**: R2's two-pass rule propagates from search specialist to completeness
  cluster to parent; R6's pooling restriction propagates from LLM specialist to
  generation cluster to parent; R8's careful specialist body becomes causal in its
  summary and downstream. Correct all listed occurrences, not just the parent.

## (g) Line-reference walk

- [x] No invalid explicit source-line/paragraph-range citation was found in the
  targets; they primarily use handle/number citations. Checked the attestation
  section anchors relevant to the disputed claims. The section-anchored numerical
  example has the **missing-specific** defect R4, not a nonexistent range. No
  additional sub-attestation range defect was established.

## (h) Substantively thin-attestation check

- [x] No substantively empty or whole-source-only attestation was found behind the
  reviewed load-bearing claims. The reduced-depth records generally contain the
  particular abstract/snippet result being cited. R4 is a specific missing datum
  in an otherwise substantive attestation; R9 concerns lost qualifications, not
  an allegation that short records are intrinsically inadequate. No additional
  GR.5 finding is asserted.

## Required reconciliation

Checklist verification passed: required frontmatter, jobs a–h, findings R1–R9,
69 explicit file:line references, final verdict and whitespace. The 1,429
specialist/cluster/parent citation occurrences match their registry handle/number
pairs and attestation source URLs. `git diff --check` passed. Hash comparison
confirmed all 238 snapshotted research input files remained unchanged; this
checklist was the sole addition within that assessed scope.

Resolve R1–R9 in the named artifacts and upstream occurrences. Preserve the
conditional transfer to methodology reviews; do not turn either the challenge's
overlap or marginal dimension coverage into a calibrated estimate of unseen
approach families. For corrections to existing artifacts, record their correction
mode and reconcile affected summaries/body text. The zero-broken lint result does
not discharge these semantic findings. No missing credential, network or permission
blocked this local verification; source reacquisition for R4 belongs to the revision.

NEEDS-REVISION
