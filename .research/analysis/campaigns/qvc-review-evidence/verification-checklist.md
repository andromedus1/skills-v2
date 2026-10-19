---
title: Adversarial-read verification checklist — qvc-review-evidence
provenance: agent-verification
gate: adversarial-read
attempt: 2
updated: 2026-10-19
target: parent.md (primary); specialists/reviewer-independence.md, specialists/warning-noise.md, acquisitions.md
verdict: NEEDS-REVISION
---

# Adversarial-read verification checklist — qvc-review-evidence

Status: complete. Verdict: **NEEDS-REVISION** (see end).

## Lint regeneration

`lint-citations.py ... --no-url-check --format json` (2026-10-19): 4 files; 361 citations
(parent 121, reviewer-independence 96, warning-noise 144, acquisitions 0); 0 broken; 0 thin;
9 `reduced-substrate-attestation` (all `coverity-alert-actionability-oss`); 0
`intra-program-resolved`; 1 `substrate_confidence_omitted` (`anthropic-agent-evals`, reused);
59 pattern advisories (acquisitions 2, parent 7, reviewer-independence 27, warning-noise 23).

## Sampling statement

- **Attestations:** all 28 cited attestations (27 new + reused `anthropic-agent-evals`) read in full,
  so jobs (d) and (h) cover the whole retrieved set, not only cited handles.
  `anthropic-evaluator-optimizer` is not cited anywhere in the campaign and was not walked.
- **parent.md (primary):** exhaustive. Every claim and all 121 citation instances were walked
  semantically against the attestation bodies (summary, 8 `key_findings`, Q1, Q2, practice table,
  Cross-facet, Contradictions, Disconfirming, Decision relevance, Limits, Revisit).
- **reviewer-independence.md:** read in full. Semantic walk of all 6 `key_findings`, every body paragraph,
  the F-table, Contradictions, Disconfirming and Decision relevance (about 80 of its 96 citation
  instances; the bibliography lines were not walked).
- **warning-noise.md:** read in full. Semantic walk of all 8 `key_findings`, summary, the threshold table
  and definition notes, practices 1-8, F-table, C1-C7, Disconfirming, Limits and Decision relevance;
  numeric specifics were checked for every claim that the parent reuses and spot-checked elsewhere
  (about 110 of its 144 citation instances).
- **acquisitions.md:** all 6 candidates checked for grounding.
- **Not done:** no source was re-fetched (no web access, by instruction), so attestation fidelity to the
  original sources (`GR.6`/`GR.7`) is not tested; job (i) lineage walk was not commissioned, though
  brief-to-parent drops are reported under (c) and (e) where found.

## Findings by job

Severity key: **M** = material (load-bearing for a key finding or a decision-relevance bullet; must be
revised before `evaluate`); **m** = minor (precision or qualifier fix, should be revised); **i** = info
(no revision required; recorded for the lead).

### Part 1 — parent.md (primary target)

#### (a) Semantic citation-chain walk — parent.md

Walked: all 8 `key_findings` (L14-21), the summary (L5-12), every bullet in Q1 (L52-112), Q2 (L118-165),
Cross-facet (L169-180), Disconfirming analysis (L199-222), Decision relevance (L228-247) and Limits
(L251-260) against the cited attestation bodies (all 28 cited attestations read in full).

Supported as stated (no issue): L52-57 (self-recognition, self-bias, MT-bench self-enhancement), L57-60
(Qwen2.5-72B HSPP 86 vs SPR 55), L62-64 (affinity; "not sufficient to just use a held-out LM"), L66-70
(PoLL kappa 0.763 vs 0.627, 7-8x cost, self-judged largest delta, Cohere affiliation), L75-78 (critics;
"is not obvious"), L85-88, L89-92, L97-98, L105-110, L118-120, L124-127, L133-138, L144-146 (click
counts and "withhold approval" quote), L160, L163, L165, L169-180, L195, L215-221, L259-260.

- **A1 (M) — parent.md L234-236, Decision relevance "Review weights"; also summary L9.** "the human data
  support a step from zero or one reviewer to a second check more than adding further reviewers
  [inspection-team-size-experiment]{18} [convergent-peer-review-practices]{19}".
  (i) No cited source has a zero-reviewer condition: Porter et al. randomized 1, 2 or 4 reviewers
  (`inspection-team-size-experiment.md` L22-24). "zero" is unsupported; the nearest is McIntosh's
  self-approval measure (`review-coverage-participation-defects.md` L28-30), which is not cited here and
  whose effect the replication found low-impact (`review-measures-defects-replication.md` L30-31).
  (ii) `{19}` is not independent support for the defect claim: its "Two reviewers find an optimal number
  of defects" is a cite-through of Porter et al. plus "consensus" (`convergent-peer-review-practices.md`
  L27-30), and its own data measure comments and rounds, not defects (L31-35) — as parent L92 itself says
  ("Neither measures defects found"). Citing `{18}` and `{19}` together double-counts one experiment.
  *Revision:* drop "zero or", cite `{19}` only for the descriptive median-of-two/comments observation (or
  state it as "Rigby and Bird attribute to Porter et al. that…"), and keep `{18}` as the sole defect
  evidence.
- **A2 (M) — parent.md L102-103 and L210-211, "Re-review after changes" and Disconfirming "Against
  mandatory re-review on every change".** The Porter H3 result (repair between sessions "had no effect on
  observed defect density") compares two-session inspections *with* versus *without* repair between the
  sessions; both arms include a second inspection (`inspection-team-size-experiment.md` L17-18, L22-24,
  L48-50). It measures whether repairing first changes total defects found, not whether changes made
  after a review need re-review or introduce defects. Used at L210 as evidence "Against mandatory
  re-review on every change", it is a semantic mismatch (claim-to-source mapping, not a missing citation).
  *Revision:* either remove it from the re-review disconfirming bullet or restate it precisely ("whether
  defects were repaired between two inspection sessions did not change observed defect density; the
  design does not measure defects introduced by changes") and mark the application `extends`. (See also
  E2 for the stripped team-size-two qualifier.)
- **A3 (M) — parent.md L228-231, Decision relevance "Cross-model review preference".** "grounding the
  review in executable checks, references or recorded criteria is more consistently associated with
  reduced judge error [llm-judge-mt-bench]{11} [llm-self-bias-refinement]{15}
  [llm-judge-affinity-similarity]{14}". `{14}` contains no grounding intervention and no reduction of judge
  error (`llm-judge-affinity-similarity.md` L22-46: it shows similarity bias persisting with accuracy
  controlled). No cited source tests "executable checks" or "recorded criteria" as judge conditions
  (MT-bench: reference answers, L39-43; self-bias: reference-based InstructScore, L32-39). `extends` covers
  the application to workflow but not the citation bundle. *Revision:* move `{14}` to the clause it
  supports ("does not show that a different model is the active ingredient"); restrict the grounding
  clause to "references / reference-based feedback" with `{11}` `{15}`, and mark "executable checks or
  recorded criteria" as an `extends` generalization.
- **A4 (m) — parent.md L17 (key_finding) and L93-95.** "Observational links between review participation
  and later defects did not survive independent replication." The replication reports that on Qt the
  review measures were "similar to what McIntosh et al. found" (`review-measures-defects-replication.md`
  L30), and the finding is instability, sensitivity to variable selection, and no added fit
  (L22, L27-28), with indirect effects (L25-26). "did not survive" over-reads; the attested shape is
  "were unstable and added no model fit over traditional predictors". *Revision:* reword the key finding
  and L94-95 accordingly.
- **A5 (m) — parent.md L93.** "estimated to add up to five post-release defects in Qt-family projects":
  the source says "components with lax code review participation will contain up to five additional
  post-release defects" across Qt, VTK and ITK (`review-coverage-participation-defects.md` L10, L20-21,
  L26-27). The unit is per component, and VTK/ITK are not "Qt-family". (Same wording in
  reviewer-independence F12, see Part 2.) *Revision:* "up to five additional post-release defects per
  component in the studied Qt, VTK and ITK releases".
- **A6 (m) — parent.md L19 (key_finding).** "delivery point mattered more than false-positive rate in
  that report." The source holds the FP rate constant ("same false positive rate",
  `facebook-infer-zoncolan-scaling.md` L39-40); it does not vary FP rate, so a comparison of the two
  factors' importance is composed. *Revision:* "with the estimated FP rate unchanged, delivery point
  alone moved the fix rate from near zero to over 70%" (or mark `{inferred: …}`).
- **A7 (m) — parent.md L240-241.** "Recording what a review covered, as Google's guidance asks of partial
  reviewers [google-review-speed-lgtm]{24}, is the attested mechanism that makes reuse checkable." The
  Google guidance is about splitting coverage among concurrent reviewers of one CL
  (`google-review-speed-lgtm.md` L33-35), not reuse across later changes; the attested record that is
  actually about later changes is GitHub's recorded diff-at-approval (`github-stale-review-dismissal.md`
  L21-24). "the attested mechanism" is a definite-article comparative. *Revision:* "Two attested recording
  mechanisms: GitHub records the approved diff state {25}; Google asks partial reviewers to note which
  parts they reviewed {24}; using either to make reuse checkable `extends`".
- **A8 (i) — parent.md L74.** `[anthropic-agent-evals]{7}` ("Model grading needs human calibration") is
  supported (`anthropic-agent-evals.md` L17-18) but is design guidance placed under a bullet titled
  "Grounding is where judge errors fell"; it is not evidence that errors fell. Acceptable if the lead
  labels it *(designed)*.
- **A9 (i) — parent.md L35.** Sample count (27 new + 1 reused) matches the bibliography and lint handles.
  The commission's reuse note also lists `anthropic-evaluator-optimizer`; it is not cited anywhere in the
  campaign. No issue; recorded for the engagement record.

#### (b) Claim-shapes the lint missed — parent.md

The 7 lint pattern advisories on parent.md (L36, L52, L56, L67, L109, L162, L215) were reviewed: model
version names, a source-quoted "most recent push", and "no false positives" read off the source. None is
an unsupported composed claim. Shapes the lint did not catch:

- **B1 (m) — parent.md L7 (summary): "switching to a different model removes only part of it".** No
  attestation measures how much self-preference is removed by switching judge model. The nearest are the
  panel study's self-judged largest delta (`llm-judge-panel-poll.md` L37-38) and the affinity study's
  persisting similarity bias (`llm-judge-affinity-similarity.md` L39-46). This is a composed quantity
  claim, unmarked. *Revision:* "a different-model judge still favours similar models" (as key_finding L15
  already says), or mark `{inferred: aggregate}`.
- **B2 (m) — parent.md L236: "scaling review to perceived risk is the documented practice".** The source
  gives risk as one example ("e.g.") of why reviewers are added after a round, and says reviewer count
  "can vary to accommodate other factors, such as the complexity of a change"
  (`convergent-peer-review-practices.md` L37-39, L44-45); Google adds change size
  (`google-modern-code-review.md` L29-31). "the documented practice" is a definite-article
  generalization. *Revision:* "reviewer count is commonly varied with perceived risk, complexity or change
  size {19} {20}" (RI brief L281-283 already has this form).
- **B3 (i) — parent.md L150: "Non-action alone does not show lost attention."** Unmarked composition, but
  it paraphrases the review's own "Alert overriding may often be justified"
  (`cpoe-alert-override-review.md` L22) and the appropriateness data; acceptable. Adding `{34}` would make
  the support visible.
- Cite-throughs: the parent correctly treats FindBugs Fixit, RacerD and Bates et al. as unfetched
  (L259-260). The one over-extended cite-through is the `{19}` defect claim (A1 (ii)).

#### (c) Coherence-read for smoothed contradictions — parent.md

- **C1 (M) — synthesis-artifact self-smoothing on reviewer count: summary L9 ("Human-review data support
  a gain from one reviewer to two, not beyond"), key_finding L17, Decision relevance L234-235.** The
  parent's own Contradictions row L189 keeps the within-source tension (detailed analysis: one-person
  poorer; abstract: treatments "did not significantly influence the defect detection effectiveness"),
  but the summary, key finding and decision bullet state the one-to-two gain without it. The supporting
  qualifiers are also absent from the parent: the one-person single-session treatment was discontinued
  as ineffective (`inspection-team-size-experiment.md` L31-33, carried in RI brief L120 but not the
  parent), and the source's own summary is "Increasing team size does not always improve performance"
  (L40-41). *Revision:* summary and L234 should read "one randomized experiment found one-person
  inspections poorer than two- or four-person ones, though its abstract reports no significant treatment
  effect".
- **C2 (M) — "grounding" bundles a non-grounding condition and hides a within-corpus disagreement: summary
  L8, key_finding L15, Q1 bullet L71-74.** (i) "longer judge reasoning" / chain-of-thought is listed as a
  grounded check; it adds no external reference or oracle (`llm-self-preference-legitimacy.md` L29-30,
  L45-46). (ii) The MT-bench attestation records that a chain-of-thought judge "in many cases ... makes
  exactly the same mistake as the given answers", with only the reference-guided judge cutting failures
  (`llm-judge-mt-bench.md` L39-43). So on CoT the two sources pull in different directions on different
  metrics (math-grading failure vs harmful self-preference) — a `qualifies` relationship that neither the
  parent nor the RI brief surfaces (RI L58-60 and L107-109 repeat the CoT benefit only). (iii) The panel
  result (L66-70) is a non-grounding condition under which judge agreement with humans improved, so
  "grounding is the recurring condition" in key_finding L15 is stronger than the Q1 section it summarises.
  *Revision:* separate "reference/oracle grounding {11}{15}" from "longer judge reasoning {13}"; add a
  Contradictions row (`qualifies`: CoT lowered harmful self-preference {13} vs CoT judge repeating the
  graded answer's mistakes {11}); soften key_finding L15 to "reference grounding is the condition most
  often associated with reduced judge error; panel diversity helped in one study".
- **C3 (M) — dropped brief contradiction on volume: Disconfirming L219-222 ("The recurring condition is
  placement, volume and repetition") and practice row L165.** The warning-noise brief's C6 (`tension`)
  records that the 2006 override review found no relationship between relative alert amount and override
  percentage (`cpoe-alert-override-review.md` L30-31), against the 2017 cohort's volume effect
  (`cds-alert-fatigue-repeats.md` L28-30; the cohort itself flags the earlier null, L22-23). The parent
  Contradictions table (L184-195) omits C6 while asserting volume as a recurring condition. This is a
  correction not propagated from brief to parent (`PR.1`/`CO.1`). *Revision:* add the C6 row to the
  parent table and qualify L222.
- **C4 (M) — Decision relevance "Citation advisories" L242-247 drops caveats the parent keeps
  elsewhere.** The parent's Disconfirming L217-218 and Contradictions L191 record that Google's
  review-time findings are socially enforced at approval and that the counter-evidence is builder-reported;
  the decision bullet recommends "keeping advisories" on that evidence with neither caveat. With E1
  (click-metric undercount) and D1 (FindBugs review-time integration discontinued over effective false
  positives), the decision bullet presents the advisory-retention case more cleanly than the evidence
  sections. *Revision:* add one sentence to L242-247: the Google evidence concerns review-time findings
  that reviewers typically enforce before approval, measured by click ratios that undercount ignoring; a
  review-time integration without action-rate curation was discontinued.
- **C5 (m) — Limits L254-255 contradicts the Q1 body.** "Human-review evidence ... measures comments or
  post-release defect counts rather than defects caught per review" — the Porter experiment, used as the
  primary reviewer-count evidence (L85-88), measures observed defect density found per inspection
  (`inspection-team-size-experiment.md` L18-19). RI L260-261 words this correctly ("observational except
  for the inspection experiment"). *Revision:* adopt the RI wording.
- **C6 (m) — dropped brief contradiction C3 (batch/dashboard usefulness, `qualifies`).** The parent says
  out-of-workflow dashboards were ignored (L121-122, L219-220) and cites SRE in the same Disconfirming
  bullet (L220-221), but SRE recommends "a dashboard that monitors all ongoing subcritical problems"
  (`sre-monitoring-distributed-systems.md` L43-45), Zoncolan's master analysis is dashboard-triaged by
  security engineers, and Tricorder's code-search layer serves dedicated cleanup teams (warning-noise
  brief C3, L279-285). The parent keeps the "specialist queues" practice row (L163) but not the
  contradiction. *Revision:* add C3 as a `qualifies` row; it bears directly on whether citation
  advisories could move to a separate review queue rather than be suppressed.
- Rows carried correctly (nothing surfaced): all five RI contradictions and warning-noise C1, C2, C5, C7
  are present in the parent table with relationship types preserved; the two lead-added rows (L191,
  L192) are fairly stated. Warning-noise C4 (override ≠ failure) is represented in body L148-150 and
  Decision relevance L246-247 rather than the table; acceptable.
- **C7 (m) — relationship type at L188 (`contradicts`).** The replication states that on Qt the review
  measures were "similar to what McIntosh et al. found" and that McIntosh himself "did not believe that
  review measures could dominate traditional measures" (`review-measures-defects-replication.md` L28-30);
  the disagreement is over added explanatory power and stability, not opposite estimates. `contradicts`
  over-states commensurable opposition; `qualifies` or `tension` fits the attested positions. RI brief
  L218 hedges ("contradicts on explanatory power"); the parent drops the hedge. *Revision:* restore the
  "on explanatory power" qualifier or retype as `tension`.

#### (d) Noise-domination / relevance-weighting — parent.md

All 28 attestations were read for each Q1/Q2 claim cluster, not only the cited ones.

- **D1 (M) — parent.md L116-127 (delivery point), key_finding L19, Disconfirming L214-218.** The most
  relevant in-corpus disconfirmer of "delivery point matters more than false-positive rate" is uncited in
  the parent: Google's third FindBugs attempt posted results *as code-review comments* with suppression
  and was discontinued because "the presence of effective false positives caused developers to lose
  confidence in the tool" (`google-static-analysis-lessons.md` L41-44). Review-time delivery without
  action-rate curation failed. The warning-noise brief carries it (L61-63); the parent drops it while
  citing the same attestation 18 times for other claims. *Revision:* add it to L121-123 and to the
  Disconfirming bullet at L214-218.
- **D2 (m) — Decision relevance "Review weights" L234-237 and "Cross-model review preference" L228-233.**
  Two attested findings on *who* reviews are uncited where the decision is made: the replication
  attributes to Porter et al. that "the best predictor was the level of expertise of the reviewers.
  Varying the processes had a negligible impact" (`review-measures-defects-replication.md` L40-41; carried
  in RI L152-153), and the Microsoft abstract posits effective reviews need "people with specific set of
  skills" (`code-reviews-do-not-find-bugs.md` L19-21). The parent cites only the familiarity figure
  (L97-98). For a decision about reviewer identity and weight, reviewer expertise is more relevant than
  the reviewer-count medians cited. *Revision:* add one clause (cite-through form for the Porter
  attribution).
- **D3 (m) — Q1 "Same-model versus different-model judging" L50-81.** The commission asks about
  "agreement with human judgment"; the parent drops MT-bench's agreement result (GPT-4 non-tie
  agreement 85% vs 81% human-human, and agreement lowest "where the compared answers are close in
  quality", `llm-judge-mt-bench.md` L48-57; RI F1). The close-quality caveat is the condition most like
  subtle review findings. *Revision:* one sentence in Q1.
- **D4 (i) — affinity study and grounding.** The `llm-judge-affinity-similarity` attestation does not
  record whether its judges were given the reference answer (L17-20 says only "free-form responses with
  ground truth"). If they were, similarity bias persisting under reference-grounded judging would qualify
  the "grounding" claims (C2, A3). Not resolvable from the corpus; recommend the revision pass check the
  fetched source's setup section and extend the attestation (discipline §8: extend substrate, do not
  patch prose).
- **D5 (i) — Porter discontinued 1sX1p** — see C1.

#### (e) Quote-context walk (`GR.4`) — parent.md

- **E1 (M) — parent.md L143-147 and summary L10-11 ("non-blocking review-time findings are acted on at
  high rates").** The Tricorder not-useful rate (~5%) is a click ratio. The source's own qualifiers are
  stripped: PLEASE FIX and APPLY FIX counts "are known to be low", "Developers may ignore findings they do
  not plan to fix, rather than clicking NOT USEFUL", and Google cannot "measure how many results are
  viewed by developers" (`google-tricorder-icse2015.md` L64-66, L72-73). The warning-noise brief carries
  them (L128-131, L325-326); the parent drops them. Neither Google source reports an action rate; the
  attested high action rates are Facebook's (>70% Infer diff-time fix rate; Zoncolan ~80% action rate,
  `facebook-infer-zoncolan-scaling.md` L39-40, L55-57). *Revision:* add the undercount caveat at L143-147;
  in the summary, attribute "acted on at high rates" to the Facebook diff-time data and describe Google's
  as "low not-useful click ratios and thousands of fix requests per day".
- **E2 (m) — parent.md L102-103 and L210.** Porter's repair-between-sessions result is quoted ("had no
  effect on observed defect density"), but Section 3.7 found repair "didn't increase effectiveness when
  the team size was one, but did when the team size was two", to be "viewed with caution" (few cells)
  (`inspection-team-size-experiment.md` L36-38). The parent strips the team-size-two qualifier. Combine
  with A2.
- **E3 (M) — parent.md L161 (practice table, tiering row).** "(29% vs 10% compliance; 100% vs 34% for the
  hard-stop tier)" strips two source qualifiers: the 100% was "by design since this was a 'hard stop'"
  (`ddi-alert-tiering-compliance.md` L32-33), and the non-interruptive low tier's response was not
  collected, so "Level 3 response rates between the sites cannot be directly compared" (L31-32). The
  row's label "non-interruptive low tier" next to the compliance numbers implies the advisory tier was
  measured; the measured gain is on the interruptive Level 2 tier (11% vs 29%, L30-31). The warning-noise
  brief handles this correctly (L339-342: evidence that advisory display helps "is indirect"). This bears
  directly on the "tier citation advisories" decision. *Revision:* "(overall 29% vs 10%; Level 2
  interruptive 29% vs 11%; Level 1 100% by hard-stop design vs 34%; Level 3 information-only response not
  measured)" and label *(demonstrated, observational; advisory-tier effect indirect)*.
- **E4 (m) — key_finding L21 and L148-150 ("about half of outpatient alert overrides were judged
  appropriate").** The source's own framing: appropriateness "varied by alert type ... from 12% for renal
  recommendations to 92% for patient allergies", with drug-drug interaction overrides 12% appropriate and
  the authors calling for "further education and intervention" there
  (`cds-outpatient-override-appropriateness.md` L23, L27-31). The average without the range overstates
  how generally non-action is benign. Brief F12 carries the range. *Revision:* add "(12%-92% by alert
  type)".
- **E5 (m) — parent.md L207-209 ("24% of flagged 'flawless' items versus 6% unassisted").** In the source,
  humans reviewed only completions where the sampled critique "identified a problem", and 24% is of those
  cases; the 6% is a second contractor re-rating "flawless" completions in a separate replication
  (`llm-critics-catch-bugs.md` L39-43). The denominators differ (critique-flagged subset vs flawless
  items generally), so the 24-vs-6 contrast is not like-for-like; the source juxtaposes them without
  equating them. Same wording in RI L101-103. *Revision:* state the two denominators, or present the
  figures without "versus".
- **E6 (m) — parent.md L52-53.** "GPT-3.5, GPT-4 and Llama 2 favoured their own news summaries" holds
  for the pairwise setting; in the individual (Likert) setting "Llama doesn't give very different scores",
  and label reversal showed "no clear difference" for Llama (`llm-self-recognition-preference.md`
  L33-35, L38-40). *Revision:* "in pairwise comparisons".
- **E7 (m) — parent.md L66-67.** PoLL beat GPT-4 on NQ, but the source attributes GPT-4's weakness to
  "over-reasoning" on what is "essentially fuzzy string matching" and reports GPT-4 improved with prompt
  changes (`llm-judge-panel-poll.md` L33-34). The parent lists other caveats but not this one, which
  bears on whether the gain is from diversity. *Revision:* add the caveat.
- **E8 (i) — parent.md L132-133.** The "somewhat arbitrarily" quote omits the footnote's continuation:
  the figure "seems to be a sweet spot for developer satisfaction and matches the cutoff for similar
  systems in other companies" (`google-static-analysis-lessons.md` L63). Key_finding L20 ("not validated
  against outcomes") remains accurate; the brief carries the continuation (WN L112). Optional.
- **E9 (i) — parent.md L148.** "49% to 96% of cases" omits "Except for serious alerts for overdose, which
  are overridden in one fourth" (`cpoe-alert-override-review.md` L25-27). Optional.
- **E10 (m) — parent.md L215-217.** Coverity OSS (36.7% fixed) is used as counter-evidence to "advisory
  warnings degrade", but the attestation states "the abstract does not describe where in the projects'
  workflow the alerts were shown" (`coverity-alert-actionability-oss.md` L17-18). The parent marks
  `{confidence: abstract-only}` but drops the delivery-unknown scope note that the brief keeps (WN L101).
  *Revision:* add "delivery mode not stated".

#### (f) Analytical-tier-inheritance walk — parent.md

Nothing surfaced. Lint reports 0 `intra-program-resolved`; no `[handle]{N}` resolves to a brief, position
or glossary. The overlapping lens `.research/analysis/briefs/quality-feedback-loops.md` is never cited or
named in the parent or briefs. The specialist briefs are inherited as framing only through the parent's
own restated, re-cited claims. The decision-relevance section uses `extends` and states it gives
implications, not measured effects (L226). See Part 2 for one task-context leak in the warning-noise brief.

#### (g) Line-reference walk — parent.md

Nothing surfaced. The parent cites at handle granularity only; it makes no line, section or paragraph
range citations. Section-specific details it relies on were located in the attestation at the stated
section anchors (e.g. Tricorder IV.E probation rule, `google-tricorder-icse2015.md` L54-60; Google
footnote c, `google-static-analysis-lessons.md` L61-63; Porter Section 5.2, L43-50).

#### (h) Thin-attestation check (`GR.5`, semantic) — parent.md citations

- **H1 (i) — `anthropic-agent-evals` (reused; 20 lines, no quotations, whole-section paraphrase, no
  `substrate_confidence`).** Substantively thin, but it is cited only for "model grading ... needs human
  calibration" (parent L74), which its L17-18 states. Adequate for that claim only; it could not support
  anything more specific. Lint's deprecation notice applies; outside this engagement's authored substrate.
- **H2 (i) — `coverity-alert-actionability-oss` (abstract only, `snippet-thin`).** Honestly flagged and
  marked at every use; see E10 for the dropped scope note.
- All other 26 attestations carry section-anchored quotations or paraphrases at per-claim granularity and
  record what was not read (e.g. `google-modern-code-review` page 5; `llm-judge-affinity-similarity` lost
  coefficients). No substantively thin attestation supports a load-bearing parent claim.

### Part 2 — specialist briefs and acquisitions (load-bearing claims)

#### specialists/reviewer-independence.md (RI)

- **(a) R1 (M) — RI L9 (key_finding) and L279-280 (Decision relevance).** "Grounded checking (a reference
  answer, oracle feedback, executable tests) is the recurring condition under which judge errors fell".
  No attested study gives a judge executable tests: the ground-truth study uses MBPP+ tests to *label*
  correctness, while judges judge pairwise (`llm-self-preference-legitimacy.md` L15-18, L31). "executable
  tests" is an unattested specific in a key finding, and it is the brief-tier origin of parent A3.
  *Revision:* drop "executable tests" from the key finding, or mark the generalization `extends`.
- **(b) R2 (m) — RI L8 (key_finding).** "Switching to a different model reduces, but does not remove,
  correlated-judgement risk" — no attestation measures a reduction from switching (see B1). RI L233 has
  the same shape ("reduces only the identity component"). *Revision:* "does not remove" stands alone, or
  mark `{inferred: aggregate}`.
- **(c) R3 (m) — RI L248-249 vs RI L158-159.** The brief's own body says the Porter repair evidence
  "concerns a second inspection after repair, not re-review of a changed diff", but its Disconfirming
  bullet then uses it "Against 're-review after every change is necessary'". Internal self-smoothing; the
  body's caveat did not reach the parent (A2).
- **(c) R4 (m) — RI L58-60, L107-109.** CoT benefit stated without the MT-bench CoT-judge failure (C2).
- **(a) R5 (m) — RI L196 (F12) vs RI L137.** Body correctly says "Qt, VTK and ITK"; F12 says "Qt-family
  projects", which propagated into parent L93 (A5).
- **(e) R6 (m) — RI L246.** "Google introduced review mainly for understandability
  [google-modern-code-review]{20}" rests on a sentence the attestation records as truncated: "the
  foremost reason ... was to improve code understandability and" — continuation on the unread page 5
  (`google-modern-code-review.md` L34-36). "mainly for understandability" may drop a co-equal second
  reason. *Revision:* quote the fragment with "(continuation unread)" or drop the clause.
- **(e) R7 (m) — RI L101-103.** Same 24%-vs-6% denominator issue as E5.
- **(b) R8 (m) — RI L281.** `{19}` double-counted with `{18}` for the defect claim (A1 (ii)); the brief
  itself notes at L129-131 that the two-reviewer optimum "is attributed to the inspection literature
  rather than measured here".
- Nothing surfaced on: the MT-bench agreement and self-enhancement numbers (L37-47), the affinity example
  and quotes (L64-69), the panel numbers and caveats (L87-94), the critics comparison (L96-100, L104-105),
  the Porter detail (L118-124, correctly including the discontinued 1sX1p treatment), the practice data
  (L127-135), the McIntosh and replication detail (L137-146), the Google and GitHub policy descriptions
  (L165-176). Contradictions (L203-224) are well-formed; the evidence-type labels follow the commission.

#### specialists/warning-noise.md (WN)

- **(a) W1 (m) — WN L329-330 and F16 L260: "Zoncolan's action rate above 80% covers a funnel in which
  the security on-call can block a diff".** The attestation records the funnel (very-high-signal
  categories comment directly on diffs; lower-signal diff issues go to the on-call queue; the rest to the
  master analysis) but nothing about the on-call *blocking* diffs (`facebook-infer-zoncolan-scaling.md`
  L49-57). This is the read-but-not-attested gap. The claim is used to exclude Zoncolan from
  advisory-only evidence, so it shapes the disconfirming analysis. *Revision (discipline §8 direction):*
  if the fetched article says so, extend the attestation with the passage and re-point; otherwise reword
  to "includes a security on-call triage step" without "block".
- **(b) W2 (m) — WN L74 heading.** "At Facebook, delivery point mattered more than false-positive rate" —
  composed comparative of a factor that was held constant (A6). The body (L80-81) is correctly hedged.
- **(e) W3 (m) — WN L188.** "Issues on checked-in code are rated real less often (21% vs 74% at compile
  time)" is offered as support for delivering at the point of change; the source attributes the gap to a
  "survivor effect" (`google-static-analysis-lessons.md` L50-52) — real issues are fixed earlier and the
  ones left are less often real — not to developer receptivity at delivery time. *Revision:* add the
  authors' survivor-effect explanation or move the figure out of the delivery-point practice.
- **(e) W4 (m) — WN L19 (key_finding).** "100% vs 34% for the most severe tier" without the
  hard-stop-by-design qualifier the body (L209) and F13 (L257) carry; it is the brief-tier origin of E3.
- **(c) W5 (m) — WN summary L12.** "'Advisory' by itself is not what predicts decay; delivery point,
  curation, and volume/repetition are" — an unmarked causal-sounding generalization, stated while the
  brief's own C6 (L300-303) records a null volume-override relationship in the 2006 review. *Revision:*
  mark `{inferred: aggregate}` and soften "predicts" to "is associated with".
- **(f) W6 (i) — WN L314.** "The seed hypothesis was 'advisory (non-blocking) warnings degrade'" carries
  authoring context into the artifact body (substrate test, agent-task-context facet); the phrase does
  not appear in the commission. *Revision (optional):* "Disconfirming probe: do advisory warnings degrade
  as such?" The parent's quoted use (L214) is fine as a named position.
- Nothing surfaced on: the FindBugs history (L56-66), build-time warnings (L68-72), Facebook batch/diff
  numbers and caveats (L74-81), Coverity quotes (L83-88), interview counts (L90-96), the threshold table
  and definition notes (L108-144, including the click-undercount caveat at L128-131), SRE/SOC/clinical
  detail (L148-177), practices 2-8 (L190-239), C1-C7 (L264-310), and Limits (L352-367). The
  disconfirming analysis (L317-350) is the most careful section of the campaign: it keeps the
  social-enforcement, click-undercount and indirect-tiering caveats that the parent later drops.

#### acquisitions.md

Nothing surfaced. All six enriching candidates are grounded in an attestation that names them (reference
lists recorded in `google-static-analysis-lessons`, `facebook-infer-zoncolan-scaling`,
`ddi-alert-tiering-compliance`, `code-reviews-do-not-find-bugs`; Bates et al. named in
`cpoe-alert-override-review` with bibliographic detail deliberately left unfilled — correct `GR.9`
handling). No candidate is training-recall (`AQ.3`). None is classed blocking, so `AQ.4` does not arise;
the Imtiaz full text is enriching even though parent L215-217 leans on its abstract (flagged there).

#### Metadata spot-check (`GR.9`)

`.research/references.md` entries 11-37 list title, fetch date and source URL only; the URLs sampled (11,
18, 19, 26, 28, 31, 34, 36) match the attestations' `source_url`. Venue/DOI values in the brief
bibliographies sampled (Tricorder ICSE 2015 DOI, Facebook CACM DOI, the Rigby and Bird attribution)
match the attestation text, including the attestations' "as printed on the fetched PDF" and
"attributed by citing references" provenance notes. Nothing surfaced.

## Verdict: NEEDS-REVISION

The citation chains are mechanically sound and most claims are faithful to their attestations. The
specialist briefs, especially the warning-noise disconfirming analysis, keep most of the source
qualifiers. The revision need is concentrated in the parent synthesis, the load-bearing artifact for
the consumers. Several caveats kept in the briefs were dropped on the way up (`PR.1`), and four
decision-relevance or key-finding claims rest on a mis-mapped or over-bundled citation. No fabrication
was found: no unresolved handle, no training-recall citation, no lens cited as source, no recalled
metadata.

### Revision targets (must fix before `evaluate`; parent.md unless stated)

1. **A1** — L234-236 (and summary L9): drop "zero or"; stop citing `{19}` as defect evidence
   (cite-through of Porter); keep `{18}` alone for the defect claim. Also fix RI L281 (R8).
2. **A2 + E2** — L102-103, L210-211: the Porter repair-between-sessions result is not re-review-after-
   change evidence; restate precisely with the team-size-two qualifier, or remove it from the re-review
   disconfirming bullet. Also fix RI L248-249 (R3).
3. **A3 + R1** — L228-231 and RI L9, L279-280: remove `{14}` from the grounding clause; restrict
   attested grounding to references/reference-based feedback; mark "executable checks/tests, recorded
   criteria" as `extends`.
4. **C1** — summary L9, key_finding L17, L234: carry the Porter abstract-vs-detail tension (and the
   discontinued 1sX1p treatment) wherever the one-to-two gain is stated.
5. **C2** — summary L8, key_finding L15, L71-74: separate CoT/long reasoning from grounding; add a
   `qualifies` Contradictions row for CoT (`{13}` vs `{11}`); soften "grounding is the recurring
   condition". Mirror in RI L58-60/L107-109 (R4).
6. **C3** — add warning-noise C6 (alert volume vs override, `tension`) to the parent table; qualify L222.
7. **C4 + E1 + D1** — L143-147, summary L10-11, L242-247: add Tricorder's click-undercount caveat; credit
   "acted on at high rates" to the Facebook diff-time data; add the discontinued FindBugs code-review
   integration (`google-static-analysis-lessons` Attempt 3) to delivery point and Disconfirming; carry the
   social-enforcement caveat into the citation-advisories decision bullet.
8. **E3 + W4** — L161 and WN L19: tiering row must say the 100% was a hard stop by design and the
   information-only tier's response was not measured.

### Should fix (minor)

A4 (L17, L94-95 "did not survive"), A5/R5 (L93, RI F12 "Qt-family", per-component unit), A6/W2 (L19,
WN L74 "mattered more"), A7 (L240-241 "the attested mechanism"), B1/R2 (L7, RI L8 "reduces"), B2 (L236
"the documented practice"), C5 (L254-255 Limits vs Porter), C6 (add warning-noise C3 batch-usefulness
row), C7 (L188 `contradicts` hedge), D2 (reviewer expertise in decision bullets), D3 (MT-bench human
agreement, close-quality caveat), E4 (L21, L149 12%-92% range), E5/R7 (24% vs 6% denominators), E6
(L52 pairwise only), E7 (L66 GPT-4 over-reasoning), E10 (L215-217 delivery mode unknown), R6 (RI L246
truncated quote), W1 (WN L329-330, F16 Zoncolan "block" not attested — extend attestation or reword),
W3 (WN L188 survivor effect), W5 (WN L12 unmarked generalization).

### Info only (no action required)

A8, A9, B3, D4 (check affinity-study judge setup and extend the attestation if the source says whether
judges saw references), E8, E9, H1, H2, W6.

## Revision response (2026-10-19)

Mode: **correction** (discipline §8). Positions preserved; fixes made in place, with a `## Revisions` log in each
edited artifact (parent L306, RI L299, WN L396). Line numbers below refer to the revised files. Attestations were
extended additively from material re-fetched this session; no existing quote was altered:
`facebook-infer-zoncolan-scaling.md` L64+ (Zoncolan on-call "blocks the diff", re-fetched from the CACM PDF) and
`llm-judge-affinity-similarity.md` L48+ (§3.1 and Appendix B.9: judges graded "without access to a ground-truth
solution", re-fetched from arXiv HTML v2).

Lint after revision (`--no-url-check --format json`): 0 broken, 0 thin; parent 146 citations, RI 99, WN 144
(acquisitions 0; this checklist 8); 9 `reduced-substrate-attestation` (`coverity-alert-actionability-oss`, as
before); 1 `substrate_confidence_omitted` (`anthropic-agent-evals`, reused, unchanged). The one new pattern advisory
from revision ("the only defect evidence", comparative-superlative) was reworded (parent L259).

### Material

- **A1** — parent L259-265: "zero or" dropped; `{18}` is the sole defect evidence, scoped to "in this sample… one
  experiment"; `{19}` re-scoped to the descriptive median-of-two practice. Summary L5-13 no longer states the gain.
  RI L290-293 (R8): `{19}` now cited as "Rigby and Bird attribute the two-reviewer optimum to Porter et al."
- **A2 + E2** — parent L108-112: repair result restated with the Section 3.7 two-person qualifier ("viewed with
  caution") and an `extends` note that both arms include a second inspection, so it does not measure changes after
  review. Removed from the re-review Disconfirming bullet (L229-232), which now says it does not test that. RI L259
  (R3) and F15 L204 likewise.
- **A3 + R1** — parent L252-258: `{14}` moved to the "different model is not the active ingredient" clause (now
  supported by the extended attestation: ungrounded judges); grounding clause restricted to reference guidance and
  reference-based feedback `{11}` `{15}`; executable checks / recorded criteria stated as an untested extension.
  RI key finding L9 ("No fetched study gave judges executable tests") and decision relevance L289-290.
- **C1** — parent summary L5-13, key finding L18, body L88-92 (adds discontinued 1sX1p treatment and the Section 4
  "does not always improve performance" line), Disconfirming L221-225, decision L259-261: the abstract's
  no-significant-effect statement now travels with every one-to-two claim. RI summary L5 and Disconfirming L253.
- **C2** — parent summary, key finding L16 (adopts the suggested wording), body L72-77 (chain-of-thought separated
  from reference grounding, MT-bench CoT failure added), new `qualifies` Contradictions row L201. RI (R4): L60-62,
  L114-116, new `qualifies` contradiction L230.
- **C3** — parent new `tension` row L211 (warning-noise C6); Disconfirming L241-245 qualified with the 2006 null
  `{34}` and the aggregate marked `{inferred: aggregate}`.
- **C4 + E1 + D1** — parent L156-158 (Tricorder click-undercount caveat); summary L5-13 credits high action rates to
  Facebook diff-time data and describes Google's as low not-useful click ratios; key finding L20 and body L131-133 add
  the discontinued FindBugs review-comment integration; Disconfirming L233-240 carries undercount, social enforcement,
  builder-reported and FindBugs caveats; decision "Citation advisories" L271-281 carries them too.
- **E3 + W4** — parent table row L175: overall, Level 2, Level 1 (hard stop by design) and unmeasured Level 3 stated;
  type label "advisory-tier effect indirect"; decision bullet repeats the indirectness. WN key finding L21 and
  practice 4 L211.

### Minor

- **A4** — key finding L18 and body L97-100: "did not survive" replaced by "unstable … added no model fit"; C7 row adds
  "similar to what McIntosh et al. found".
- **A5 / R5** — parent L97-98 and RI F12 L201: "up to five additional post-release defects (per component) in the
  studied Qt, VTK and ITK releases".
- **A6 / W2** — parent key finding L20 ("At an unchanged estimated false-positive rate…"); WN heading L76 reworded;
  no comparison of factor importance remains.
- **A7** — parent L266-270: "the attested mechanism" replaced by two attested recording mechanisms (GitHub `{25}`,
  Google `{24}`), use for reuse marked as an application under `extends`.
- **B1 / R2** — parent summary no longer quantifies removal; RI key finding L8 ("does not remove") and Disconfirming
  L242 ("does not remove the similarity component").
- **B2** — parent L263-264: "reviewer count is commonly varied with perceived risk, complexity or change size
  {19} {20}".
- **C5** — parent Limits L288-289 adopts the RI wording (observational except one experiment measuring observed defect
  density).
- **C6** — parent new `qualifies` row L212 (batch/dashboard usefulness for specialist audiences, incl. SRE dashboard
  `{32}`); decision bullet notes specialist queues as an attested alternative to suppression.
- **C7** — parent L203: retyped `contradicts` → `tension`, "dispute is over explanatory power".
- **D2** — parent body L102-104 (Microsoft "specific set of skills"; cite-through of Porter via `{22}`) and decision
  L263-265.
- **D3** — parent new bullet L50-52 (85% vs 81%; agreement lowest on close-quality answers).
- **E4** — parent key finding L22 and body L162-164 (12%-92% range, renal and drug-drug interaction 12%); WN key
  finding L20.
- **E5 / R7** — parent L225-228 and RI L104-107: the two denominators stated; "versus" removed.
- **E6** — parent L53-54: "In pairwise comparisons … (Llama not in individual scoring)".
- **E7** — parent L69-70: "over-reasoning" attribution and prompt-change improvement added.
- **E10** — parent L236: "delivery mode not stated" added to the Coverity OSS figure.
- **R6** — RI L256: "foremost reason … 'to improve code understandability and' (continuation unread)".
- **W1** — True against source: re-fetched the Facebook CACM PDF; the "Funneled deployment" section says the on-call
  "validates the alarm reported, blocks the diff". Extended the attestation (L64+) per §8 direction and kept the claim,
  now quoting the passage (WN L331-333, F16 L262).
- **W3** — WN L191: survivor-effect attribution added.
- **W5** — WN summary L9-13: marked as a composed reading, "predicts" softened to "associated with", 2006 null noted;
  Disconfirming L338 marked `{inferred: aggregate}`.
- **R3, R4, R8** — covered under A2, C2, A1 above.

### Info only

- **A8** — parent L77: calibration sentence now introduced as design guidance, separate from the demonstrated results.
- **A9, H1, H2** — no change required.
- **B3** — `{34}` "Alert overriding may often be justified" now cited beside the non-action sentence (L162).
- **D4** — Resolved by re-fetch: the affinity judges graded without references (attestation L48+). This does not
  qualify the grounding claims (similarity bias was measured under ungrounded judging); parent L62 and RI L66 now state
  the condition.
- **D5** — covered by C1.
- **E8** — parent L143: "sweet spot for developer satisfaction" continuation added.
- **E9** — parent L161: overdose-alert exception added.
- **W6** — WN L316: "Disconfirming probe: do advisory (non-blocking) warnings degrade as such?"

### Not resolved / residual

- None of the listed findings was left unaddressed. Length: parent grew from about 2,900 to about 3,550 words because of
  the restored qualifiers and three new Contradictions rows; the briefs changed by under 6%.

## Adversarial re-read (2026-10-19)

Gate: `adversarial-read`, re-read after revision pass 1. Fresh-context reader; composition: discipline bundle +
adversarial-reader brief (CATALOGS §4). Line numbers refer to the revised files as of this read. Severity key as above
(**M** material, **m** minor, **i** info).

### Lint regeneration

`lint-citations.py .research/analysis/campaigns/qvc-review-evidence/ --attestation-dir .research/attestation/
--no-url-check --format json`: 0 broken chains, 0 thin, 0 `intra-program-resolved`, 0 campaign-unbound;
1 `substrate_confidence_omitted` (`anthropic-agent-evals`, reused, unchanged). Citations: parent 146 (143 resolved,
3 `reduced-substrate-attestation`, all `coverity-alert-actionability-oss`), RI 99 resolved, WN 144 (138 resolved, 6
reduced-substrate, all Coverity OSS), this checklist 8, acquisitions 0. Pattern advisories: parent 6 (L36, L53, L57,
L67, L235 model or version names and a quoted statistic; L176 "no false positives" read off the source; none is a
composed claim), RI 27, WN 23, acquisitions 2, checklist 18. A `campaign-evaluation.md` (evaluate gate, APPROVED)
appeared in the campaign directory during this read. It was not an input here and does not change these findings.

### Sampling statement

- **parent.md:** exhaustive. Read in full. Every sentence and all 146 citation instances were walked against the
  attestation bodies: frontmatter summary, 8 key findings, Q1, Q2, practice table, Cross-facet, all 13
  Contradictions rows, Disconfirming, Decision relevance, Limits, Revisit.
- **Attestations:** all 28 cited attestations read in full, including the two extensions, so jobs (d) and (h) cover the
  whole retrieved set.
- **Briefs:** every hunk of `git diff 13fe4e07` in `reviewer-independence.md` and `warning-noise.md` was read and
  walked, along with both briefs' frontmatter summaries and key findings and WN's Disconfirming analysis, Limits and
  Decision relevance (L316-394). Unchanged brief bodies were not re-walked; they were covered in attempt 2.
- **Re-fetches this session (scratchpad only; nothing committed):** (1) Facebook CACM PDF (attestation `source_url`),
  text extracted; (2) arXiv HTML v2 of 2502.04313; (3) arXiv HTML v4 of 2306.05685 (MT-bench), re-fetched to test a
  claim the revision added (see N1). Re-fetched text is used here only to verify. It is not cited. Each fix below
  goes through the attestation, as discipline §8 requires.

### Prior material findings: resolution

| Finding | Status | Evidence (revised lines) |
| --- | --- | --- |
| A1 | **Resolved** | Parent L259-262: `{18}` is the only defect evidence, scoped to "one experiment"; `{19}` is limited to practice. "zero" is gone. RI L290-293 now uses the cite-through form "Rigby and Bird attribute…". |
| A2 + E2 | **Resolved** | Parent L108-111 adds the Section 3.7 two-person qualifier ("viewed with caution") and an `extends` note that both arms include a second inspection (attested, `inspection-team-size-experiment.md` L17-18). The Disconfirming bullet (L229-232) no longer uses the result. RI L259-261 and F15 match. |
| A3 + R1 | **Resolved as scoped** | `{14}` now supports only the "not the active ingredient" clause (L253-254), backed by the extended attestation L48-57. The grounding clause cites `{11}` `{15}`. Executable checks and recorded criteria are labelled "untested". RI L9 matches. **New issue on the same bullet's exclusivity: see N1.** |
| C1 | **Resolved** | The abstract's no-significant-effect statement now accompanies the one-to-two gain in the summary (L8-10), key finding L18, body L88-92 (with the discontinued 1sX1p treatment and the Section 4 line), Disconfirming L224-225 and decision L259-261. RI summary and L253-254 match. |
| C2 | **Resolved as scoped (bundling); the revision introduced a new error** | Chain-of-thought is now separated from reference grounding (L72-77), and key finding L16 is softened. The new `qualifies` row L201 and the "evidence diverges" framing, however, rest on a claim that is false against the source and missing from the attestation. See N1. The error came from this gate's own attempt-2 wording of C2(ii). |
| C3 | **Resolved** | `tension` row L211 cites both sides correctly (`cpoe-alert-override-review.md` L29-31; `cds-alert-fatigue-repeats.md` L22-23). L243-246 qualified and marked `{inferred: aggregate}`. |
| C4 + E1 + D1 | **Resolved, but the revision added an unattested specific** | Click-undercount caveat at L156-158 (attested, Tricorder L64-66, L72-73). FindBugs Attempt 3 at L131-133, key finding L20, L239-240 and L275-276 (attested, `google-static-analysis-lessons.md` L41-44). Social enforcement and builder-reported caveats are in Disconfirming L237-239 and decision L273-276. Crediting high action rates to Facebook added "non-blocking", which neither the attestation nor the source supports. See N2. |
| E3 + W4 | **Resolved** | Parent L175 states overall, Level 2, Level 1 (hard stop by design) and an unmeasured information-only tier, with the type label "advisory-tier effect indirect". Decision L277-278 repeats this. WN key finding L21 and practice 4 L211-212 match (`ddi-alert-tiering-compliance.md` L30-33). |

**Minor and info findings, spot-checked (all walked; resolved unless noted):** A4 (L18, L98-100 "unstable … added no
model fit"), A5/R5 (L97-98; RI F12), A6/W2 (L20; WN L76), A7 (L268-270), B1/R2 (summary; RI L8, L242), B2 (L262-263),
C5 (L288-289), C6 (row L212, attested in Tricorder L42-44, Facebook L49-50 and SRE L45), C7 (L203 retyped `tension`
with the "similar to what McIntosh et al. found" quote), D2 (L101-104 correct cite-through form; the decision-bullet
compression is noted under m3), D3 (L50-52; see m1), E4 (L22, L162-164; Table 3 values match `cds-outpatient-override-appropriateness.md` L27-28),
E5/R7 (L225-228; RI L104-107), E6 (L53-54), E7 (L69-70; see i2), E10 (L236), R6 (RI L256-257), W1 (verified below),
W3 (WN L190-191), W5 (WN L9-13, L338), W6 (WN L316), A8 (L77), B3 (L162), E8 (L143), E9 (L161). Nothing reopened.

### Attestation extensions (additivity and use)

- **Additivity:** `git diff 13fe4e07 -- .research/attestation/` shows only added lines (+10 Facebook, +13 affinity).
  No existing line changed. Both additions sit under a dated "Additional anchored details (re-fetched 2026-10-19)"
  heading. Frontmatter `fetched:` stays 2026-10-18; the re-fetch date is recorded in the heading. Acceptable.
- **W1, `facebook-infer-zoncolan-scaling.md` L64-72:** verified verbatim against the re-fetched CACM PDF. The PDF
  contains "When appropriate, the on-call validates the alarm reported, blocks the diff, and provides support to
  write the code in a secure way", and the audience sentence and "At “diff time,” security related issues are pushed
  to the security engineer on-call…" also match. WN L331-333 and F16 L262 use the passage within its scope ("when
  appropriate"; "can … block"). **Within scope.**
- **D4, `llm-judge-affinity-similarity.md` L48-59:** verified verbatim against arXiv HTML v2. "This is done based on
  its own internal knowledge without access to a ground-truth solution" is in §3.1 "Experimental Setup". "To mimic
  more common, but ungrounded settings … we do not provide the judge with access to ground-truth responses or MCQ
  answer options" is in §B.9. The reference-equipped five-judge ensemble is in §B.3.2. All section labels exist.
  Parent L62 ("Judges grading without ground-truth solutions") and L253-254 ("a held-out judge grading without
  references") and RI L8 and L66-67 use the passage within its scope. **Within scope.** The conclusion in the
  revision response, that this does not qualify the grounding claims, follows: the study did not test grounded
  judges for affinity bias.

### Findings by job: revised parent.md and touched brief sections

#### (a) Semantic citation-chain walk

- **N1 (M): the "chain-of-thought diverges" claim and the "only reference guidance" exclusivity.** Locations: parent
  summary L7-8 ("judge errors fell most clearly with reference grounding, while evidence on longer judge reasoning
  diverges"), body L74-77, Contradictions row L201 ("a chain-of-thought math judge in many cases repeated the graded
  answer's mistake, and only reference guidance cut failures [llm-judge-mt-bench]{11}"), key finding L16 ("reference
  grounding is the condition most often associated with reduced judge error"), and decision L254-256 ("Reference
  guidance and reference-based feedback are *the* attested conditions under which judge error fell"). Brief: RI key
  finding L9 ("evidence on longer judge reasoning diverges"), RI L61 ("only the reference-guided judge cut failures"),
  RI L231-232 ("where a reference-guided judge did not").
  - *Attestation:* `llm-judge-mt-bench.md` L39-43 records the CoT qualitative remark and the reference-guided
    70%→15%. It records nothing about the CoT judge's failure rate. "only reference guidance cut failures" is
    therefore unattested (read-but-not-attested at the claim's critical specific).
  - *Source (re-fetched, arXiv HTML v4, §3.4 and Table 4):* "Table 4: Judge failure rate on 10 math questions with
    different prompts … Default 14/20, CoT 6/20, Reference 3/20". The CoT judge also cut failures, from 70% to 30%.
    The "same mistake" remark describes the residual cases. The claim is false against the source. Both fetched
    studies therefore show longer reasoning reducing judge error: MT-bench by less than references, and the
    legitimacy study's HSPP. The evidence does not diverge in direction. The `qualifies` row L201 states a
    contradiction that the source does not contain, and "most often" in L16 and "the attested conditions" in
    L254-255 exclude a condition with equal study count.
  - *Also stripped:* the 70%→15% figure (L72-73), the only quantitative support for "where judge errors fell most
    clearly", comes from 20 judgements on 10 math questions (one model pair, positions swapped). The attestation
    records neither n.
  - *Origin:* this gate's attempt-2 C2(ii) wording ("with only the reference-guided judge cutting failures"), which
    the revision adopted. The error is the gate's, propagated into the substrate (see (f)).
  - *Revision (discipline §8 direction, extend the substrate first):* add §3.4 / Table 4 to `llm-judge-mt-bench.md`
    (Default 14/20, CoT 6/20, Reference 3/20; 10 math questions; failure = GPT-4 judging an incorrect answer
    correct). Then correct the parent and RI:
    - Summary and body: "reference guidance cut math-grading failures most (70% to 15% on 20 judgements); chain-of-thought also reduced them (to 30%) and lowered harmful self-preference, though it often repeated the graded answer's mistakes".
    - L201 and RI L229-232: drop the row or restate it without "only". Retype it, because both sources agree that CoT helped.
    - Key finding L16: "reference grounding produced the largest reduction where compared".
    - Decision L254-256: "Reference guidance produced the largest attested reduction in judge error; chain-of-thought judging also reduced it".
    - RI L9, L61: matching corrections.
- **N2 (M): Facebook's diff-time findings described as "non-blocking".** Locations: parent summary L11-12 ("Facebook
  reports non-blocking diff-time findings acted on at high rates") and Disconfirming L233-234, where Facebook's 70% is
  newly the lead counter-evidence "Against 'advisory warnings degrade'" while the caveats (L237-240) cover only
  Google. Brief: WN summary L10-11 ("non-blocking warnings acted on at high rates at Facebook's diff time"). Both
  parent locations and the WN summary wording were introduced by this revision; the attempt-2 versions cited only
  Google and Coverity.
  - *Attestation:* `facebook-infer-zoncolan-scaling.md` says diff-time issues are "given to developers promptly as part
    of code review" (L22-23), and Infer participates as a bot in review (L40-42). It says nothing about whether those
    reports gate landing. The W1 extension (L69) shows that some Facebook diff-time security findings are blocked by
    the on-call.
  - *Source (re-fetched CACM PDF):* the only blocking statement is the Zoncolan on-call passage. The article describes
    Infer as "participating as a bot in code review … programmers come to the review tool to discuss their code with
    human reviewers". It does not say the reports are non-blocking.
  - *Why it is material:* the commission's decision is whether citation advisories should be reclassified, suppressed
    or retained (seed L64-67), so a source's advisory status carries the decision. The revision's own logic for
    Google, that "socially enforced" review findings are not purely advisory, applies equally to an unattested
    Facebook delivery mode. As written, the summary attributes to Facebook a property Facebook does not report.
  - *Revision:* summary and WN L10-11: "Facebook reports diff-time findings posted as code-review bot comments acted on
    at high rates (the source does not say whether they gate landing)". Add the same caveat at parent L237-240 beside
    the Google caveats. In WN L319-327, either move the Infer sentence out from under "Non-blocking review-time
    findings are acted on" or add that caveat. If a fetched source states Infer's diff-time reports are non-blocking,
    extend the attestation and keep the word.
- **m1: L50-52, "as the quality gap between answers widened".** The source (Table 7, attested L55-57) varies "the
  performance gap between the compared models" (win-rate disparity of model pairs), not per-answer quality. The
  heading "weakest on close calls" rests on the attestation's own gloss. *Revision:* "as the performance gap between
  the compared models widened". "Expert humans" is correct: MT-bench S2, Table 5, confirmed on re-fetch, and
  attested at L44-47 and L52.
- **m2: L20 (key finding) and L275-276 (decision).** FindBugs Attempt 3 is cited as discontinued "over effective false
  positives". The source gives two reasons; the second is that "developer customization resulted in an inconsistent
  view" (`google-static-analysis-lessons.md` L43-44). Body L131-133 carries both. The decision bullet weighs
  suppression, which is customization, so the dropped reason bears on it. *Revision:* add "and per-user
  customization" to L275-276.
- **m3: L263-264, "reviewer expertise and familiarity are attested as mattering [review-measures-defects-replication]{22}
  [code-reviews-do-not-find-bugs]{23}".** `{22}` is a cite-through of Porter et al., and body L103-104 correctly writes
  "attributes to Porter et al.". `{23}`'s expertise claim is a posit from a talk abstract with no methods (attested
  L19-21; body L102-103 says "posited … (documented, no methods)"). "Attested as mattering" upgrades both claims.
  *Revision:* "are reported as mattering (a cite-through of Porter et al. {22}; a posit and familiarity data without
  methods {23})".

#### (b) Claim-shapes the lint missed

- **m4: L272-273, "removing or tiering checks whose non-action rate is high (shortened handles for references 27, 28
  and 36)".** In `{36}`, tiering is by severity (`ddi-alert-tiering-compliance.md` L21-24), not by non-action rate.
  The composed criterion is attributed to the tiering source. The wording predates the revision. *Revision:* "removing
  checks whose non-action rate is high {27}{28}, and tiering by severity {36}".
- **m5: L278-279, "Before a threshold is applied, the false-positive definition must be stated
  [google-static-analysis-lessons]{26}".** This normative "must" is composed from the incommensurability finding
  (L149-150). `{26}` defines its own term but does not prescribe this. The wording predates the revision and sits
  under the bullet's `extends`, but the citation reads as Google's rule. *Revision:* drop the citation or mark the
  sentence `{inferred: aggregate}` with a pointer to the incommensurable row L209.
- **i1: L281, "specialist queues are an attested alternative to suppression".** No citation; under `extends`. The
  support is in row L212 and practice row L177, where routing is attested. "Alternative to suppression" is the
  synthesis's framing. Acceptable; a pointer "(see Contradictions)" would make the support visible.
- Nothing else surfaced. Revision-added comparatives such as "most clearly" (L8, L72) are addressed under N1.

#### (c) Coherence-read for smoothed contradictions

- The inverse failure, a manufactured contradiction, is N1 (row L201). It is not smoothing, but it misrepresents the
  source relationship in the same structural place.
- The new rows L211 (`tension`) and L212 (`qualifies`) are fairly stated and their relationship types fit. Row L203
  was retyped correctly.
- Summary versus body: after the revision, the summary no longer states anything stronger than the body, except the
  N1 and N2 items.
- The decision bullets now carry the caveats the evidence sections keep (C4 is resolved). One residual tension, which
  predates the revision and is acceptable: L252-253 ("supports keeping an independent check over pure self-review")
  against L218-219 ("Self-review is therefore not shown to be worse than cross-model review"). They reconcile because
  "independent check" includes grounded checks, and the bullet says so in its last clause. **i**, no action.

#### (d) Noise-domination / relevance-weighting

- For N2, the most relevant attested material on Facebook's delivery mode is the W1 extension (on-call blocking) and
  the bot-in-review passage. Neither is used next to the summary claim. This is covered by the N2 revision.
- For N1, the more relevant number (the CoT rate) is in the source but not in the retrieved set, so this is an
  attestation gap (see (h)), not a `CX.1` instance.
- Nothing else surfaced. The D2 and D3 additions use the most relevant attested passages.

#### (e) Quote-context walk (`GR.4`)

- **i2: L69-70, "GPT-4's weakness is attributed partly to 'over-reasoning'".** The source "hypothesise[s]"
  (`llm-judge-panel-poll.md` L33-34). "Attributed partly" is close enough; "hypothesised" would be exact. Optional.
- **i3: L175, "information-only tier not measured".** Accurate for the tiered site. The non-tiered site's Level 3
  compliance (9%) was measured (`ddi-alert-tiering-compliance.md` L30-31). "Not measured at the tiered site" would be
  exact. Optional.
- Revision-added quotes checked in context, with no stripped qualifier: "viewed with caution" (L110); "Increasing team
  size does not always improve performance" (L91); "did not significantly influence…" (L90); "are known to be low" /
  "Developers may ignore findings…" (L156-157); "the presence of effective false positives caused developers to lose
  confidence in the tool" (L132; see m2 for the dropped second reason elsewhere); "sweet spot for developer
  satisfaction" (L143); "Alert overriding may often be justified" (L162); "a dedicated cleanup team" (L212; the source
  also requires "higher false positive rates", which fits the row); "similar to what McIntosh et al. found" (L203);
  "over-reasoning" (L69).
- The "makes exactly the same mistake" quote (L76, L201) is accurate, but its frame strips the source's own Table 4
  context. See N1.

#### (f) Analytical-tier-inheritance walk

- Lint reports 0 `intra-program-resolved`. No handle resolves to a brief, position, glossary or checklist.
- **N1 is an analytical-tier inheritance in substance.** The "only reference guidance cut failures" specific came
  into the parent (L201) and the RI brief (L61, L232) from this gate's attempt-2 checklist paraphrase (C2(ii)), not
  from the attestation. A verification artifact's framing was asserted as source fact. The N1 revision fixes it. For
  the lead: revision passes should take a checklist's suggested wording as a pointer to the attestation, not as a
  source.
- Nothing else surfaced. The overlapping lens `quality-feedback-loops` is still uncited.

#### (g) Line-reference walk

- The parent still cites at handle granularity. The section anchors in the two attestation extensions (§3.1, §B.9,
  §B.3.2; "Funneled deployment", "People and deployments") were checked against the re-fetched sources and exist.
  Section anchors that revised prose relies on were found: Porter §3.7 and §4 (attestation L34-42), Tricorder §V.a
  (L61-67), Google Attempt 3 (L41-44), and ddi Table 3 (L30-33). Nothing surfaced.

#### (h) Thin-attestation check (`GR.5`, semantic)

- **`llm-judge-mt-bench.md` §3.4 entry (L39-43) is substantively thin for the use the revision now makes of it.** It
  gives the reference-guided rate but not the CoT rate in the same table, nor the n (20 judgements). That made the
  N1 over-read possible. Covered by the N1 revision (extend the attestation).
- `anthropic-agent-evals` and `coverity-alert-actionability-oss` are unchanged from attempt 2 (H1 and H2). Their uses
  are still within what they support (L77, L39, L236).
- Both extensions are adequately anchored (verbatim quotes with section labels).

### Verdict: NEEDS-REVISION

All eight prior material findings are resolved as scoped, the minor and info findings are addressed, and both
attestation extensions are additive, verbatim-accurate against the re-fetched sources, and used within scope. The
revision introduced two new material problems, each small to fix:

1. **N1.** Parent L7-8, L16, L72-77, L201, L254-256; RI L9, L61, L231-232. The claim that chain-of-thought evidence
   "diverges" and that "only reference guidance cut failures" is unattested and false against MT-bench Table 4 (CoT
   cut failures from 70% to 30%; references to 15%; n = 20). Extend `llm-judge-mt-bench.md` with Table 4 first, then
   correct the synthesis wording, drop or retype row L201, and remove the exclusivity in the decision bullet.
2. **N2.** Parent L11-12 and L233-240; WN L10-11 and L319-327. Facebook's diff-time findings are called
   "non-blocking"; neither the attestation nor the source says so. Reword, and add the missing caveat beside the
   Google caveats.

Minor findings that do not block: m1 (L50-52 model-gap wording), m2 (L20 and L275-276 second FindBugs reason), m3
(L263-264 cite-through compression), m4 (L272-273 tiering criterion), m5 (L278-279 composed "must" cited to Google).
Info: i1, i2, i3.

No fabrication was found: no unresolved handle, no training-recall citation, no lens cited as source, and no recalled
metadata. A light revision touching only the lines above, with the one attestation extension, should be enough. A
second full re-read is not needed: a targeted check of N1 and N2 would do.

## Bounded correction response (2026-10-19)

Operator-authorized bounded correction after the adversarial re-read (N1, N2, m1-m5, i1-i3) and the evaluate gate's
recommendations 1-5. Mode: correction (discipline §8), position preserved; the attestation was extended before any
prose changed. Line numbers refer to the files after this pass. Files touched: `parent.md`,
`specialists/reviewer-independence.md` (RI), `specialists/warning-noise.md` (WN), and
`.research/attestation/llm-judge-mt-bench.md` (additive only). Each edited artifact has a dated `## Revisions` entry;
`updated:` was already 2026-10-19 and is unchanged.

### Attestation extension (done first)

- `llm-judge-mt-bench.md` L59-82, under "Additional anchored details (re-fetched 2026-10-19, arXiv HTML v4, same
  source)". Re-fetched https://arxiv.org/html/2306.05685v4 this session. Recorded verbatim: the Table 4 caption ("Judge
  failure rate on 10 math questions with different prompts. We test LLaMA-13B vs. Vicuna-13B and swap positions. A
  failure means when GPT-4 says an incorrect answer is correct."), the row Failure rate Default 14/20, CoT 6/20,
  Reference 3/20, the full Section 3.4 paragraph, and the Section 4.2 Table 7 sentence and caption. The note records
  that the prose gives 70% and 15% only, and that the CoT value is in the table alone. `git diff` shows only added
  lines; frontmatter and existing quotes are unchanged.

### Material findings

| Item | Disposition | Changes (file:line) |
| --- | --- | --- |
| N1 | Fixed | parent L7-10 (summary: 14/20, 6/20, 3/20, 20 judgements); L19 (key finding: "the one study comparing judge prompts", CoT also reduced); L76-83 (body rewritten with n, all three rates, the "same mistake" quote kept as residual-case context); the CoT `qualifies` row was removed from Contradictions (formerly between L207 and L208), because the sources do not diverge; L225-227 (Disconfirming: CoT also reduced errors, by less); L263-266 (decision bullet: no longer "the attested conditions"). RI L9 (key finding), L39-43 (n and CoT rate), L61-63 ("also cut failures … though less"), L115-118 (longer reasoning reduced failures, by less), F6 L197, Contradictions CoT bullet removed (formerly L230-233). |
| N2 | Fixed | parent L13-15 (summary: "given to developers as part of code review … the source does not say whether they gate landing"); L242-249 (Disconfirming: Facebook gating caveat and the on-call blocking passage placed before the Google caveats); L295-296 (decision bullet caveat). WN L10-12 (summary), L320 (bullet retitled "Review-time findings are acted on"), L325-326 ("as part of code review"; "four caveats"), L329-333 (Google caveat now names Google; new Facebook gating caveat directly after it). No fetched source states that Infer's diff-time reports are non-blocking, so the word was removed, not grounded. |

### Minor and info findings

| Item | Disposition | Changes (file:line) |
| --- | --- | --- |
| m1 | Fixed | parent L53-55 (heading "rises with the gap between compared models"; "performance gap between the compared models"), now backed by the verbatim Section 4.2 sentence in the attestation extension. Same wording carried to RI L39 and F1 L192 for consistency. |
| m2 | Fixed | parent L23 (key finding), L248-249 (Disconfirming), L294 (decision): second FindBugs reason (per-user customization) added. |
| m3 | Fixed | parent L280-282: "reported as mattering (a cite-through of Porter et al.; a posit and familiarity data without methods)". |
| m4 | Fixed | parent L289-291: "removing checks whose non-action rate is high" cites Tricorder and Facebook; "tiering alerts by severity" cites the tiering study. |
| m5 | Fixed | parent L297-298: Google citation dropped; sentence marked `{inferred: aggregate}` with a pointer to the `incommensurable` row. |
| i1 | Fixed | parent L300-301: "(routing is attested; see the practice table and Contradictions)". |
| i2 | Fixed | parent L73: "the authors hypothesise GPT-4 was 'over-reasoning'". |
| i3 | Fixed | parent L182: "information-only Level 3 not collected at the tiered site". |

### Evaluator recommendations

| Rec. | Disposition | Changes (file:line) |
| --- | --- | --- |
| 1 | Fixed | Facebook "non-blocking" removed (see N2). Heading retitled at parent L157, "Review-time findings outside the commit gate, and justified non-action"; L159-161 now ground "rather than blocking commits" in the Google "Gating commits" passage and say the findings are not purely advisory. |
| 2 | Fixed | parent summary L7-8: self-preference "mostly legitimate for stronger models but more harmful when the judge is wrong"; "grading without references" restored. |
| 3 | Fixed | "most clearly" (summary, body heading) and "most often associated" (key finding) were replaced by wording scoped to the single prompt comparison (parent L9, L19, L76). The remaining "largest reduction" wording is read directly off Table 4 and scoped to that comparison. |
| 4 | Fixed | parent L182: tiering row names the metric (alert compliance) and arms (tiered vs non-tiered site). Evidence labels for the tiering study (L182) and the repeats study (L186) now both state design and setting ("observational, retrospective …"). The demonstrated / independently-measured split is kept as in WN (L48-51 label definitions): two hospitals in one delivery system vs a cohort using a commercial EHR. |
| 5 | Fixed | parent L268-275: a simplify-versus-strengthen sentence marked `{inferred: aggregate}`, built only from attested findings (self-preference and its legitimacy, similarity bias, reference grounding, the panel study), ending "No fetched source measures either option on generated code." |

### Lint

`lint-citations.py .research/analysis/campaigns/qvc-review-evidence/ --attestation-dir .research/attestation/
--no-url-check --format json`: 0 thin; 1 `substrate_confidence_omitted` (`anthropic-agent-evals`, unchanged). Lint
reports 3 `unresolved-handle` chains, all in this checklist at the re-read's m4 quotation (L732-733), which writes the
handles in shortened form. They predate this pass (present at HEAD) and are outside the edit scope, which allows
appending only. Per-file lint of `parent.md`, both briefs and `llm-judge-mt-bench.md` gives 0 broken, 0 thin. This
response section uses no citation-form tokens.

### Not resolved / residual

- The 3 unresolved-handle hits in the re-read text (L732-733) remain. A future checklist edit, if authorized, can
  spell the handles in full or put them in code formatting.
- Evaluator recommendation 6 (component-4 spot-checks) was out of scope and was not run.

## Targeted N1/N2 re-check (2026-10-19)

Operator-authorized, bounded. Fresh-context reader; composition: discipline bundle + this checklist's N1/N2
definitions. Scope: whether N1 and N2 are resolved, and whether the bounded correction added any unsupported claim in
the lines it touched (`git diff HEAD` of `parent.md`, both briefs and `llm-judge-mt-bench.md`). Line numbers refer to
the working tree as of this read. Severity key as above.

### Attestation extension

- **Additivity:** `git diff --numstat HEAD -- .research/attestation/` gives 25 added, 0 removed, all in
  `llm-judge-mt-bench.md` L59-82 under a dated heading. Frontmatter and the earlier quotes are unchanged. Additive.
- **Re-fetch (scratchpad only, not cited):** arXiv HTML v4 of 2306.05685, fetched again this session. The Table 4
  caption matches word for word ("Judge failure rate on 10 math questions with different prompts. We test LLaMA-13B
  vs. Vicuna-13B and swap positions. A failure means when GPT-4 says an incorrect answer is correct."), and so does
  the row (Default 14/20, CoT 6/20, Reference 3/20). The four Section 3.4 quotes and the Section 4.2 Table 7
  sentence also match word for word. Reading "20 judgements per prompt" off "10 math questions ... swap positions"
  and the /20 denominator is sound.
- **i (no action needed):** the Table 7 caption quote at L81-82 stops before the source's last sentence ("The y-axis
  value is the GPT-4 and human agreement."). There is no ellipsis, but nothing is distorted.

### N1: resolved, but the fix adds a new exclusivity (N3)

Resolved. "diverges", "most clearly", "only reference guidance", "most often associated" and "the attested
conditions" are gone from the parent and RI (checked with grep). The chain-of-thought `qualifies` rows were removed
from both Contradictions sections. The three Table 4 rates now appear with their n at parent L9-10, L77-79 and RI
L39-43, L61-63 and F6. Each traces to `llm-judge-mt-bench.md` L62-66, and the "same mistake" quote is now framed as
describing the remaining cases (L73). The legitimacy-study chain-of-thought result (parent L80-81, RI L59-61) traces
to `llm-self-preference-legitimacy.md` L29-30 and L45-46. The model-gap wording (parent L52-55, RI L39, F1) traces to
the extension's Section 4.2 sentence (L79).

- **N3 (M): "the one study comparing judge prompts".** Locations: parent key finding L19 ("in the one study comparing
  judge prompts"), body heading L76 ("where judge prompts were compared"), Disconfirming L226 ("in the one prompt
  comparison"), and decision L263-264 ("In the one comparison of judge prompts"). Brief: RI key finding L9. This
  exclusivity is the "the only X with Y" shape that discipline §6 forbids, and the attested corpus contradicts it.
  `llm-self-preference-legitimacy.md` L45-46 (Section 5.2) compares no-reasoning judging with chain-of-thought judging.
  `llm-judge-panel-poll.md` L33 (Section 4.3) reports GPT-4 judging improving with prompt changes. What holds is
  narrower: MT-bench is the only fetched study that sets reference-guided judging beside chain-of-thought judging. The
  impact is directional. At L19 and L263-264 the parent leaves out the second chain-of-thought result, so the
  key-findings list and the decision bullet present chain-of-thought as resting on one 20-judgement comparison, when a
  second fetched study also supports it. RI L9 contradicts itself: it says "the one study comparing judge prompts" and
  then cites "another study".
  - *Revision (wording only; no attestation change needed):* replace each phrase with something scoped to MT-bench,
    for example "in MT-bench's comparison of default, chain-of-thought and reference-guided judge prompts (20 math
    judgements per prompt)". Retitle the L76 heading the same way, for example "Reference guidance gave the largest
    reduction in MT-bench's prompt comparison". At L19 and in the L263-265 decision bullet, either add "and
    chain-of-thought judging lowered harmful self-preference in another study" or drop the exclusivity. Nothing else
    needs to change.
- **m (summary L9):** "In one 20-judgement math-grading comparison" reads as 20 judgements in total. It is 20 per
  prompt, 60 across the three prompts. Suggested wording: "a math-grading comparison of 20 judgements per prompt".

### N2: resolved

"non-blocking" no longer appears beside Facebook anywhere in the parent or WN. The remaining uses are Google-only, at
WN L20 and L329, which are supported by `google-static-analysis-lessons.md` L84-86, or generic, at WN L34, L317 and
L387. The new wording, "given to developers as part of code review", appears at parent L13-14 and L240 and WN L11
and L325. It is supported by `facebook-infer-zoncolan-scaling.md` L22-23 and the bot-in-review passage at L40-43.
The absence claim "the source does not say whether [they] gate landing" appears at parent L14-15, L244-245 and L295
and WN L11 and L332-333. It is consistent with the full-text attestation and the earlier CACM re-fetch. The on-call
caveat "can block a diff over a Zoncolan alarm" (parent L245-246) keeps the source's "When appropriate" through
"can", and traces to L69. The Facebook caveat now sits beside the Google caveats (parent L244-249; WN L332-333), as
asked.

### Other touched lines (walked; no new material issue)

- Summary L6-9 (self-preference legitimacy; ungrounded different-model judge): `llm-self-preference-legitimacy.md`
  L25-27 and `llm-judge-affinity-similarity.md` L52-57. Supported.
- Google heading and L157-161 ("rather than blocking commits ... not purely advisory"): `google-static-analysis-lessons.md`
  L84-86 and L76-78. Supported.
- FindBugs second reason (L23, L249, L294): L43-44 ("developer customization resulted in an inconsistent view").
  "Per-user" is close enough, given "user-level customization" at L82-83. Supported.
- Tiering row L182 (metric, arms, Level 3 not collected, design label): `ddi-alert-tiering-compliance.md` L14-18, L27,
  L30-33 and L40. Repeats row L186: `cds-alert-fatigue-repeats.md` L14-16. Supported.
- "the authors hypothesise ... 'over-reasoning'" (L73): `llm-judge-panel-poll.md` L33-34. Exact.
- Porter cite-through and the posit plus familiarity data (L280-282): `review-measures-defects-replication.md` L40 and
  `code-reviews-do-not-find-bugs.md` L19-21 and L28-30. Supported.
- Simplify-versus-strengthen sentence (L268-275, marked `{inferred: aggregate}`): every component traces to the cited
  attestation (`llm-self-recognition-preference.md` L21-28; `llm-self-bias-refinement.md` L21-23; legitimacy L25;
  affinity L52-57; panel L22-24 and L41-42), and the closing scope statement is present. Supported.
- m5 and i1 lines (L297-301): marked, or pointer-only. Supported.
- **m (carried over, not new):** in the split citation at L290-291, the Facebook handle stays attached to "removing
  checks whose non-action rate is high". The attestation shows filtering and promotion of high-signal categories
  (L49-54) and RacerD being kept at a fix rate of about 50% for severity (L46-48), but no removal for non-action. This
  is outside N1/N2 and the line sits under `extends`. Optional: cite Facebook for "filtering output before diff-time
  delivery" instead.

### Verdict: NEEDS-REVISION

N1 and N2 are resolved, and the MT-bench extension is additive and matches the source word for word. One new material
issue came in with the N1 fix: N3, the "one study comparing judge prompts" exclusivity at parent L19, L76, L226 and
L263-264 and RI L9. The fix is wording only. After it, a grep for "one study comparing", "one prompt comparison",
"one comparison of judge" and "where judge prompts" across the parent and RI is enough to check it. No further
adversarial pass is needed. No fabrication was found: no unresolved handle in the touched lines, no training-recall
citation, and no lens cited as a source.

## Lead spot-check (2026-10-19)

Hard-floor spot-check by the engagement lead, consuming lint, adversarial and
evaluator findings.

- **Evaluator candidates (component 4), all checked against attestations and
  supported:** Qwen2.5-72B HSPP 86 vs SPR 55 (`llm-self-preference-legitimacy`
  L40); panel 7–8× cost and Cohere affiliation (`llm-judge-panel-poll` L18,
  L24, L41); kappa 0.763 vs 0.627 (L27-28); reminder acceptance −30% per extra
  reminder (`cds-alert-fatigue-repeats` L30); 75% wording bugs, 10%/25%
  thresholds (`google-tricorder-icse2015` L31-32, L57); >80% at most one
  iteration (`google-modern-code-review` L26); ~15% defect comments
  (`code-reviews-do-not-find-bugs` L24); 24% vs 6% with distinct denominators
  (`llm-critics-catch-bugs` L43).
- **Lint pattern sample (parent, 9 flags):** "largest reduction" (L76, L264)
  matches MT-bench Table 4; "Block only checks with effectively no false
  positives" (L183) matches Google's zero effective FP for build-breaking
  checks; the Porter cite-through (L281) matches
  `review-measures-defects-replication` L40. Version/decimal flags are model
  names and cited figures.
- **N3 corrected in place** (targeted re-check, NEEDS-REVISION): exclusivity
  scoped to MT-bench in `parent.md` (summary, key finding, L76 heading,
  disconfirming, decision bullet) and `reviewer-independence.md` L9; the
  {13} chain-of-thought result restored in the summary, key finding and
  decision bullet; "20 judgements per prompt" clarified; optional Facebook
  re-point applied. Grep confirms the four exclusive phrasings are gone.
- Shortened handles quoted at the attempt-3 m4 entry rewritten as plain text
  (they were lint `unresolved-handle` hits in this record, not the synthesis).
- Lint after correction: 0 broken, 0 thin.

**Verification outcome:** lint pass; evaluate APPROVED; adversarial-read's
final targeted check NEEDS-REVISION (N3), corrected by the lead in place and
**not independently re-read**. Per Andrew's bounded-fix decision this is
recorded as **verification incomplete** with that single limitation.
