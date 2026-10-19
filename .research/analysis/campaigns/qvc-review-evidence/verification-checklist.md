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
