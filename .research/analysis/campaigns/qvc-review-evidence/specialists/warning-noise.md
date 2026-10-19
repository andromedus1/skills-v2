---
title: "Warning noise: how people respond to noisy advisory signals, and what keeps them actionable"
provenance: agent-synthesis
updated: 2026-10-19
summary: >
  Evidence from industrial static analysis (Google, Facebook, Coverity), developer interview and mining studies,
  operations paging guidance, security-operations alarm triage, and clinical decision-support alert overrides on
  how people respond to warnings with high false-positive rates, which numeric thresholds have been used and under
  what definitions, and which practices keep advisory signals acted on. The sources converge that noisy warnings
  delivered outside the work context are ignored, but they also show diff-time findings, given to developers as part
  of code review, acted on at high rates at Facebook (the source does not say whether those reports gate landing),
  and review-time findings drawing low not-useful click ratios (which undercount ignoring) at Google, where they are
  curated by an action-rate feedback loop and socially enforced before approval. As a composed reading,
  delivery point, curation, and volume/repetition are more associated with decay than advisory status as such, though
  one review found no volume-override relationship.
key_findings:
  - "Same analysis, same estimated false-positive rate: Facebook reports a near-zero fix rate for a nightly batch bug list versus over 70% when reported at diff time (demonstrated, small uncontrolled batch sample)."
  - "Google's published thresholds are definition-specific: zero effective false positives for build-breaking checks, under 10% effective false positives for code-review checks, analyzer probation at a not-useful click rate of 10% or more and possible shut-off above 25% (designed)."
  - "Coverity's vendor experience: more than 30% false positives 'easily cause problems', aim below 20% for stable checkers; a not-understood true report is commonly labelled false (documented)."
  - "Google found compiler warnings ignored and moved checks to errors or code review; yet non-blocking code-review findings run at about a 5% platform not-useful click ratio, which undercounts ignoring, with thousands of fix requests per day (documented and demonstrated)."
  - "Clinical alerts are overridden in 49% to 96% of cases across studies, but about half of outpatient overrides were judged appropriate (12%-92% by alert type), so override rate is not a direct measure of degradation (independently measured; demonstrated)."
  - "Severity tiering, with only higher-severity alerts interrupting and the lowest tier information-only, was associated with 29% vs 10% overall compliance and 29% vs 11% on the interruptive Level 2 tier; the most severe tier was 100% by hard-stop design vs 34%, and the information-only tier's response was not collected (demonstrated, observational)."
  - "Acceptance falls with alert volume and within-patient repeats (about 30% per extra reminder per encounter; 10% per 5-point rise in repeat share), but no desensitization over time was found for newly deployed alerts (independently measured)."
  - "Numeric thresholds are not commensurable across sources: 'effective false positive' (no action taken), 'false positive' (cannot happen), 'not-useful rate' (click ratio), and 'override rate' measure different things."
---

# Warning noise: how people respond to noisy advisory signals, and what keeps them actionable

## Question and sample

**Question.** How do developers (and, in adjacent domains, operators, security analysts, and clinicians) respond to
advisory or lint/static-analysis warnings with high false-positive rates? What false-positive levels have been
tolerated, under what definitions? Which practices keep advisory signals actionable? And, as a disconfirming
probe: where are advisory, non-blocking signals acted on?

**Sample.** Twelve sources, eleven read in full text and one abstract-only:

- Industrial static analysis experience reports: Google [google-static-analysis-lessons]{26},
  [google-tricorder-icse2015]{27}; Facebook [facebook-infer-zoncolan-scaling]{28}; Coverity [coverity-billion-lines]{29}.
- Third-party software engineering studies: an interview study of 20 developers
  [static-analysis-underuse-interviews]{30}, and a commit-mining study of Coverity alerts in five open-source projects
  [coverity-alert-actionability-oss]{31} (abstract only).
- Operations paging guidance: Google SRE [sre-monitoring-distributed-systems]{32}.
- Security operations: a survey and interview study of SOC analysts [soc-false-positive-alarms]{33}.
- Clinical decision support: a literature review of override rates [cpoe-alert-override-review]{34}, an override
  appropriateness study [cds-outpatient-override-appropriateness]{35}, a severity-tiering comparison
  [ddi-alert-tiering-compliance]{36}, and an alert-fatigue mechanism study [cds-alert-fatigue-repeats]{37}.

**Evidence-type labels used below.** *Designed*: a system's stated policy or intended design. *Documented*: an
organization describes its practice or experience without reporting its own measurement. *Demonstrated*: the
authors' own measured deployment or experiment data. *Independently measured*: measurement by parties other than
the system's builders, or aggregation of others' measurements.

Most software evidence comes from the organizations that built the tools. Independent software measurement in this
sample is limited to the interview study and the abstract of the mining study.

## Developer response to noisy warnings and tool adoption

**Noise and poor delivery lead developers to ignore warnings.** Google lists the reasons engineers ignore static
analysis warnings as not integrated, not actionable, not trustworthy because of false positives, not manifest in
practice, too expensive to fix, and not understood [google-static-analysis-lessons]{26}. Google's three failed
FindBugs integrations give a detailed organizational account. A nightly bug dashboard "saw little use because a bug
dashboard was outside the developers’ usual workflow". In a 2009 Fixit week engineers reviewed 3,954 warnings, but
"only 16% (640) were actually fixed", although 44% of reviewed issues led to a filed bug. A code-review integration
with user-level suppression was discontinued because "the presence of effective false positives caused developers
to lose confidence in the tool" and per-user customization gave inconsistent views [google-static-analysis-lessons]{26}.
The authors summarize that Google developers "have a strong bias to ignore static analysis, and any false positives
or poor reporting give them a justification for inaction" [google-static-analysis-lessons]{26}. *(Documented; the
Fixit counts are demonstrated.)*

**Warnings at build time were ignored at Google.** The Clang team enabled new diagnostics "as a compiler error (not a
warning, which the Clang team found Google developers ignored)" [google-static-analysis-lessons]{26}. The Tricorder
paper says the same: "we have found warnings shown when building are often ignored" [google-tricorder-icse2015]{27}.
By January 2018 Google's C++ and Java builds had a "compiler warnings-free default", with results shown either as
errors or in code review [google-static-analysis-lessons]{26}. *(Documented; no ignore rate is reported.)*

**At Facebook, moving the same analysis to diff time raised the fix rate at an unchanged estimated false-positive rate.** Infer's first deployment was a nightly batch
run whose issues were hand-assigned to developers. "We assigned 20–30 issues to developers, and almost none of them
were acted on", although the team believed the false positive rate was below 20%. Switched to diff time, "the fix
rate rocketed to over 70%. The same program analysis, with same false positive rate, had much greater impact"
[facebook-infer-zoncolan-scaling]{28}. Developers explained this by context switching and relevance. In review
there is "mental context already swapped in", and a comment on the diff that introduced an issue reaches someone
for whom it is likely relevant [facebook-infer-zoncolan-scaling]{28}. *(Demonstrated. This is a before/after change, not a
controlled comparison, and the batch arm is 20-30 issues.)*

**Trust collapses through a feedback loop.** Coverity describes "a vicious cycle" in which "low trust causes complex
bugs to be labeled false positives, leading to yet lower trust", and notes that "If people don’t understand an error,
they label it false" [coverity-billion-lines]{29}. The first few reports carry outsized weight: "if the first N reports
are false positives (N = 3?), people tend to utter variants on “This tool sucks.”" Coverity "completely abandoned some
analyses that might generate difficult-to-understand reports" [coverity-billion-lines]{29}. *(Documented, vendor
experience.)*

**Developers' own accounts agree.** In a study of 20 interviewed developers, all thought static analysis was beneficial,
but "false positives and the way in which the warnings are presented" were barriers [static-analysis-underuse-interviews]{30}.
Fourteen of the 20 described harm from poorly presented output. Nineteen of the 20 said many tools do not explain the
problem well enough to act on, and 19 of the 20 stressed workflow integration. Several said volume would be less
burdensome with better presentation [static-analysis-underuse-interviews]{30}. One participant said of a lint tool's
warnings: "sifting through them is so, arduous that whenever I just look at it I’m like ehhh forget this"
[static-analysis-underuse-interviews]{30}. *(Independently measured, as self-reported perceptions.)*

**In long-running open-source use of Coverity, real alerts are acted on slowly.** In five open-source projects that used Coverity for at
least five years, 27.4% to 49.5% of alerts (median 36.7%) were fixed by code changes, and fixes were small (median 4
lines). Developers still took a median of 96 days to fix them [coverity-alert-actionability-oss]{31}
{confidence: abstract-only}. The abstract does not say how alerts reached developers. *(Independently measured.)*

## False-positive thresholds and their definitions

The numbers in this literature rest on different definitions, so they cannot be compared directly
{incommensurable: see Contradictions C1}.

| Threshold | Context | Definition it is measured under | Label | Source |
|---|---|---|---|---|
| Zero effective false positives | Google build-breaking (compiler) checks | Effective false positive: developers "did not take positive action after seeing the issue" | designed | [google-static-analysis-lessons]{26} |
| Under 10% effective false positives | Google code-review checks | Same; "Developers should feel the check is pointing out an actual issue at least 90% of the time" | designed | [google-static-analysis-lessons]{26} |
| 10% "initially chosen ... somewhat arbitrarily" | Origin of the 10% figure | Described as "a sweet spot for developer satisfaction" matching other companies' cutoffs | documented | [google-static-analysis-lessons]{26} |
| Not-useful rate of 10% or more puts an analyzer on probation; above 25% may turn it off | Tricorder feedback policy | NOT USEFUL / (NOT USEFUL + PLEASE FIX + APPLY FIX) clicks | designed | [google-tricorder-icse2015]{27} |
| Not-useful rate about 5% platform-wide (under 4% excluding probation); best analyzers 0-3% | Tricorder, 2014 | Same click ratio | demonstrated | [google-tricorder-icse2015]{27} |
| Under 20% for "stable" checkers; more than 30% "easily cause problems" | Coverity commercial tool | Report-correctness sense ("false-error messages"); measurement not specified | designed / documented | [coverity-billion-lines]{29} |
| Believed under 20%, yet batch fix rate near zero | Infer nightly batch | "a false positive is one that cannot happen"; the authors avoid claiming FP rates and track action rate | demonstrated | [facebook-infer-zoncolan-scaling]{28} |
| Maximum override rate of 40% (proposed by Bates et al., cited through the review, "do not offer an explanation") | Clinical drug alerts | Override rate (alert did not change the order) | documented (cite-through) | [cpoe-alert-override-review]{34} |

Notes on the definitions:

- Google defines a false positive by **developer action**. An incorrect report that developers fix anyway for
  readability does not count; a true fault the developer did not understand and so ignored does count
  [google-static-analysis-lessons]{26}. Tricorder adds that "to a developer, a false positive is any report that they
  did not want to see" [google-tricorder-icse2015]{27}.
- Facebook uses the **technical** definition: a false positive is a report that "cannot happen" in any run. It adds
  that the rate "is challenging to measure for a large, rapidly changing codebase", so it reports action rates instead
  [facebook-infer-zoncolan-scaling]{28}.
- The Tricorder **not-useful rate** is a feedback-click ratio. The authors say it undercounts both sides: fixes happen
  before review or in editors, and "Developers may ignore findings they do not plan to fix, rather than clicking NOT
  USEFUL" [google-tricorder-icse2015]{27}. Footnote 6 says Google cannot "measure how many results are viewed by
  developers" [google-tricorder-icse2015]{27}.
- In security operations, a "99%" false-positive figure from one analyst turned out to be "mostly benign triggers and
  not necessarily a measurement of the performance of the technology itself". Benign triggers are true matches that the
  organization chooses to ignore for business reasons [soc-false-positive-alarms]{33}. This is close to Google's
  action-based sense and far from Facebook's technical sense {inferred: convergence}.
- In clinical systems, **override** is the measured outcome, and override is not equivalent to a false positive. Two
  studies in the review found 36.5% and 39% of alerts were false positives. Reviewers agreed with 95.6% of physicians'
  overrides of valid alerts, and 48% of true-positive alerts were overridden in one study [cpoe-alert-override-review]{34}.
- Tricorder's admission criteria add a **frequency** condition alongside the false-positive bar: "if a warning occurs
  too frequently, it’s likely that it’s not causing any real problems" [google-tricorder-icse2015]{27}.
- The 10% figure's two Google descriptions differ in tone. The 2015 paper says it "matches that used by other analysis
  platforms such as Coverity" [google-tricorder-icse2015]{27}, while the 2018 article says it was "initially chosen by
  the first author somewhat arbitrarily" [google-static-analysis-lessons]{26}. Neither describes how the figure was
  validated against outcomes.

## Alert fatigue in adjacent domains

**Operations paging.** Google SRE describes the same failure: "When pages occur too frequently, employees second-guess,
skim, or even ignore incoming alerts, sometimes even ignoring a "real" page that’s masked by the noise"
[sre-monitoring-distributed-systems]{32}. Email alerts are "Sometimes known as "alert spam," as they are rarely read or
acted on". In the Bigtable case the team "disabled email alerts, as there were so many that spending time diagnosing
them was infeasible" [sre-monitoring-distributed-systems]{32}. *(Documented.)*

**Security operations.** SOC analysts largely agreed their tools frequently produce false positives (Disagree:Agree
2:14) and that alert volume is overwhelming (4:12). One analyst said "We know 99% of the alarms we generate are false
positives, but we still have to look at them" [soc-false-positive-alarms]{33}. The authors report that alarm validation
"can cause alarm burnout and eventually desensitization", and that "the lack of explainability causes alarm
desensitization" [soc-false-positive-alarms]{33}. *(Independently measured perceptions, n = 20 survey and n = 21
interviews; no measured ignore rate.)*

**Clinical decision support.**

- **Override rates.** Across nine quantitative studies, drug safety alerts were overridden in 49% to 96% of cases, apart
  from serious overdose alerts (about one fourth). One study saw overrides rise from about 50% to 75% over five years
  [cpoe-alert-override-review]{34}. The leading reason given for overriding was "alert fatigue caused by poor
  signal-to-noise ratio because the alert was not serious, was irrelevant, or was shown repeatedly", and 22% of general
  practitioners in one survey admitted overriding interaction alerts without checking [cpoe-alert-override-review]{34}.
  *(Independently measured, aggregated.)*
- **Override appropriateness.** In one outpatient center, 52.6% of 157,483 alerts were overridden. On chart review, an
  average of 53% of overrides were appropriate, ranging from 12% (renal recommendations and drug-drug interactions) to
  92% (allergy alerts) [cds-outpatient-override-appropriateness]{35}. *(Demonstrated; the center built its own system.)*
- **Mechanism.** Among 112 primary care clinicians, BPA acceptance fell about 30% for each additional reminder per
  encounter and about 10% for each 5-point rise in the share of within-patient repeats. Workload as such had no effect,
  and newly deployed reminders showed no decline over time. Only one of six alerts showed a peak-then-drop pattern, which
  the authors attribute to an external cause [cds-alert-fatigue-repeats]{37}. Repeats also showed path dependence: once a
  repeated BPA was overridden, later instances were overridden 87.9% of the time, versus 51.9% if the first was accepted.
  Drug alert acceptance was under 1% overall, a floor effect [cds-alert-fatigue-repeats]{37}. *(Independently measured.)*

## Practices that keep advisory signals actionable

Each practice below is attested in at least one source. Where a practice is supported across domains, that is marked
as composed.

1. **Deliver at the point of change, on changed lines.** Facebook's batch-to-diff-time switch is direct
   single-source evidence [facebook-infer-zoncolan-scaling]{28}. Google calls code review "a sweet spot" and shows
   results only "when a developer is changing the code in question, before the change is committed"
   [google-static-analysis-lessons]{26}. Tricorder shows most analyses "on changed lines by default"
   [google-tricorder-icse2015]{27}. Issues on checked-in code are rated real less often (21% vs 74% at compile time), which the authors attribute to a
   "survivor effect", not to delivery-time receptivity [google-static-analysis-lessons]{26}. *(Demonstrated.)*
2. **Measure action, not just correctness, and remove noisy checks.** Tricorder's not-useful rate drives probation at
   10% or more and possible shut-off above 25%. The analyzer contract allows disabling when "No one is fixing bugs filed
   against the analyzer" or results "are annoying developers" [google-tricorder-icse2015]{27}. In practice the team
   "rarely had to permanently disable an analyzer" but disabled noisy ones temporarily while sub-checks were revised
   [google-static-analysis-lessons]{26}. Facebook tracks action rate and missed bugs rather than FP rate
   [facebook-infer-zoncolan-scaling]{28}. In clinical systems, override monitoring "is said to be necessary to keep the
   override rate within acceptable limits" [cpoe-alert-override-review]{34}, and SRE reviews page frequency "in quarterly
   reports with management" [sre-monitoring-distributed-systems]{32}. *(Designed; documented.)*
3. **Fix the message before the check.** For one analyzer, "75% of all bugs filed against the tool ... were due to
   misinterpretations of the result wording" and were fixed by rewording or documentation links
   [google-tricorder-icse2015]{27}. A printf check's "Not useful" reports, all on correct findings, stopped after the
   diagnostic text was changed [google-static-analysis-lessons]{26}. Clinical guidance asks for justification ("no
   black-box warnings") and clear seriousness [cpoe-alert-override-review]{34}, and SOC analysts tie lack of
   explainability to desensitization [soc-false-positive-alarms]{33}. Coverity reports that not-understood reports get
   labelled false [coverity-billion-lines]{29}. *(Demonstrated at Google; documented elsewhere;
   {inferred: convergence} across domains.)*
4. **Tier by severity, and block only checks that cannot be wrong.** In the clinical tiering comparison, the tiered site
   kept Level 1 (hard stop) and Level 2 interactions interruptive and showed the least serious tier (71.4% of alerts)
   as information only.
   Compliance was 29% vs 10% overall, 29% vs 11% on the interruptive Level 2 tier, and 100% vs 34% for the most
   severe tier, where a hard stop was enforced [ddi-alert-tiering-compliance]{36}. Google requires "no effective false positives" before a check can break the
   build. Teams that ask to block commits usually have "highly specific custom checks with no false positives"
   [google-static-analysis-lessons]{26}. Before enabling a check as an error, Google fixes all existing instances, which
   lets it "“ratchet” the quality" without regressions [google-static-analysis-lessons]{26}. SRE requires every page to be
   "actionable" and routes subcritical issues to dashboards rather than email [sre-monitoring-distributed-systems]{32}.
   *(Demonstrated, clinical; designed, Google and SRE.)*
5. **Route lower-signal output to specialist audiences.** Zoncolan's funnel: very-high-signal categories comment
   directly on diffs, lower-signal diff issues go to a security on-call, and everything else lands in a master analysis
   triaged by security engineers. Promotion to diff time "involves improving the signal by filtering the output", and
   about a third of categories qualify [facebook-infer-zoncolan-scaling]{28}. Google offers higher-noise analyses as an
   optional code-browsing layer for teams with "a dedicated cleanup team" [google-tricorder-icse2015]{27}. Clinical
   guidance suggests directing low-specificity alerts to pharmacists or nurses [cpoe-alert-override-review]{34}.
   *(Designed; demonstrated for Zoncolan's action rate.)*
6. **Configure suppression per project and record the reasoning.** Google moved from user-level to project-level
   configuration after user customization "caused discrepancies within and across teams and resulted in declining use of
   tools" [google-static-analysis-lessons]{26}. One developer abandoned a tool after "discovering teammates were committing
   new instances" of flagged code [google-tricorder-icse2015]{27}. Most interviewed developers wanted a way "to
   temporarily ignore or suppress certain warnings", disliked turning warnings fully off, and wanted to record their
   judgement about a warning [static-analysis-underuse-interviews]{30}. Clinical systems that ask for an override reason
   find it "triggers physicians to rethink" and "can help adjust the knowledge database" [cpoe-alert-override-review]{34}.
   *(Documented; independently measured perceptions.)*
7. **Cut repetition and volume, not only false positives.** Acceptance tracks reminders per encounter and the share of
   repeats [cds-alert-fatigue-repeats]{37}. Clinical guidance recommends preventing "Annoying repetition"
   [cpoe-alert-override-review]{34}. Tricorder's frequency criterion makes a similar point for code
   [google-tricorder-icse2015]{27}. *(Independently measured, clinical; designed, Google.)*
8. **Provide fixes and visible peer accountability.** Reviewers can click "Please fix" and "typically withhold approval
   of a change until" comments are addressed [google-static-analysis-lessons]{26}. Tricorder notes "peer accountability,
   where the reviewer will see if the author chose to ignore analysis results" [google-tricorder-icse2015]{27}.
   Interviewees named lack of quick fixes as the difficulty they mentioned most often [static-analysis-underuse-interviews]{30}.
   *(Designed; independently measured perceptions.)*

## Findings table

| # | Finding | Label | Source(s) |
|---|---|---|---|
| F1 | Nightly batch delivery gave a near-zero fix rate; the same analysis at diff time exceeded 70% (batch sample 20-30 issues) | demonstrated | [facebook-infer-zoncolan-scaling]{28} |
| F2 | Bug dashboards outside the workflow saw little use; a Fixit fixed 16% of 3,954 reviewed warnings | documented / demonstrated | [google-static-analysis-lessons]{26} |
| F3 | Build-time compiler warnings were ignored at Google; checks moved to errors or code review | documented | [google-static-analysis-lessons]{26}, [google-tricorder-icse2015]{27} |
| F4 | Code-review check bar of under 10% effective FP; build-breaking checks need zero | designed | [google-static-analysis-lessons]{26} |
| F5 | Not-useful rate: probation at 10% or more, possible shut-off above 25%; about 5% platform-wide in 2014; best analyzers 0-3% | designed / demonstrated | [google-tricorder-icse2015]{27} |
| F6 | More than 30% FP "easily cause problems"; target below 20% for stable checkers; misunderstood true reports get labelled false | documented / designed | [coverity-billion-lines]{29} |
| F7 | Developers cite false positives, presentation, poor explanations, missing quick fixes, and workflow disruption as barriers | independently measured (perception, n=20) | [static-analysis-underuse-interviews]{30} |
| F8 | 27.4%-49.5% of Coverity alerts in five OSS projects were fixed by code changes, median 96 days to fix | independently measured {confidence: abstract-only} | [coverity-alert-actionability-oss]{31} |
| F9 | Frequent pages lead to skimming and ignoring; email alerts are "rarely read or acted on"; every page should be actionable | documented / designed | [sre-monitoring-distributed-systems]{32} |
| F10 | SOC analysts report overwhelming false positives, but much "FP" volume is benign triggers; lack of explainability linked to desensitization | independently measured (perception) | [soc-false-positive-alarms]{33} |
| F11 | Drug safety alerts overridden in 49%-96% of cases; fatigue from irrelevant or repeated alerts given as the leading reason | independently measured (aggregate) | [cpoe-alert-override-review]{34} |
| F12 | About half of outpatient overrides were appropriate (12%-92% by alert type) | demonstrated | [cds-outpatient-override-appropriateness]{35} |
| F13 | Severity tiering with information-only low tier: 29% vs 10% compliance; severe tier 100% (hard stop) vs 34% | demonstrated (observational) | [ddi-alert-tiering-compliance]{36} |
| F14 | Acceptance falls with alert volume and repeats; no time-based desensitization for new alerts | independently measured | [cds-alert-fatigue-repeats]{37} |
| F15 | Non-blocking review-time findings acted on at scale: over 5,000 "Please fix" clicks per day and about 3,000 applied fixes per day vs 250 "Not useful" per day (Jan 2018) | demonstrated | [google-static-analysis-lessons]{26} |
| F16 | Zoncolan action rate above 80% across its funnelled deployment (in which the security on-call can validate an alarm and block the diff); RacerD fix rate about 50% and still valued for severity | demonstrated | [facebook-infer-zoncolan-scaling]{28} |

## Contradictions

**C1. Definitions of "false positive" (relationship: `incommensurable`).** Google's effective false positive is
defined by developer inaction [google-static-analysis-lessons]{26}. Facebook's false positive is a report that
"cannot happen" [facebook-infer-zoncolan-scaling]{28}. Tricorder's operational metric is a click ratio
[google-tricorder-icse2015]{27}. Clinical studies measure overrides, which the review separates from alert
appropriateness [cpoe-alert-override-review]{34}. SOC analysts separate false alarms from benign triggers
[soc-false-positive-alarms]{33}. A threshold from one frame (such as 10% effective FP) cannot be checked against a
rate from another (such as a 20% technical FP estimate or a 50% override rate) without restating it. These are
recorded side by side, not merged.

**C2. What the 10% figure matches (relationship: `tension`).** Tricorder says its 10% threshold "matches that used by
other analysis platforms such as Coverity" [google-tricorder-icse2015]{27}. Coverity's own article states "We aim for
below 20% for “stable” checkers" and that more than 30% "easily cause problems" [coverity-billion-lines]{29}. The
sources are five years apart and may refer to different checker populations {inferred: tension}. The fetched material
does not resolve this.

**C3. Usefulness of batch reports (relationship: `qualifies`).** Facebook and Google report batch lists and dashboards
going unused by general developers [facebook-infer-zoncolan-scaling]{28}, [google-static-analysis-lessons]{26}. But
Zoncolan's master analysis is actively triaged by security engineers through a dashboard
[facebook-infer-zoncolan-scaling]{28}. Google's code-browsing layer serves teams with "a dedicated cleanup team"
[google-tricorder-icse2015]{27}. An interviewee valued batch results "to communicate, broadcast to the team a sense of
progress" [static-analysis-underuse-interviews]{30}. Batch output appears to fail as an action channel for general
developers while still serving specialist or tracking audiences.

**C4. Does override equal failure? (relationship: `qualifies`).** SRE guidance holds that "Every page should be
actionable". It asks of each rule whether one will "ever be able to ignore this alert, knowing it’s benign", and how
that scenario can be avoided [sre-monitoring-distributed-systems]{32}. The clinical sources show that a large share of
overrides are justified. About half of outpatient overrides were appropriate [cds-outpatient-override-appropriateness]{35},
reviewers agreed with 95.6% of overrides of valid alerts in one study, and "Alert overriding may often be justified"
[cpoe-alert-override-review]{34}. Ancker et al. note they "cannot conclude definitively that reducing override rates
would reduce rate of inappropriate overrides" [cds-alert-fatigue-repeats]{37}.

**C5. Desensitization (relationship: `tension`).** The SOC study reports that alarm validation can lead to burnout
"and eventually desensitization", based on practitioner accounts [soc-false-positive-alarms]{33}. Ancker et al. tested
time-based desensitization on newly deployed alerts and did not find it, though they did find volume and repeat effects
[cds-alert-fatigue-repeats]{37}. The two use different methods (perception vs log analysis) and populations.

**C6. Alert volume and override (relationship: `tension`).** The 2006 review observed no relationship between relative
alert amount and percentage overridden, attributing this possibly to the small number of studies
[cpoe-alert-override-review]{34}. The 2017 cohort study found acceptance falling with more reminders per encounter
[cds-alert-fatigue-repeats]{37}, and itself flags the earlier null finding.

**C7. What happens at a 10% not-useful ratio (relationship: `tension`).** The 2015 Tricorder paper puts an analyzer
on probation at a not-useful rate of 10% or more and says it may be turned off above 25% [google-tricorder-icse2015]{27}.
The 2018 article says that if the ratio "goes above 10%, the Tricorder team disables the analyzer until the author(s)
improve it", while also reporting that permanent disabling was rare [google-static-analysis-lessons]{26}. The two
Google accounts describe the same feedback loop with different consequences at the same figure; the fetched material
does not say whether the policy changed between them.

## Disconfirming analysis

Disconfirming probe: do advisory (non-blocking) warnings degrade as such? I searched the attested sources for cases
where advisory signals are acted on, and for cases where an apparent degradation is something else.

- **Review-time findings are acted on.** Tricorder code-review results do not block submission by
  default. Some teams want analyzers "to actually block commits, rather than just appear in the code-review tool",
  usually for zero-FP custom checks [google-static-analysis-lessons]{26}. Yet the platform
  not-useful rate was about 5%, and an average changelist had "two please-fix clicks and no not-useful clicks"
  [google-tricorder-icse2015]{27}. Codebase instances of a ClangTidy check "decreased dramatically" after it was shown
  in review [google-tricorder-icse2015]{27}. Infer reports at diff time as part of code review, with a fix rate over
  70% [facebook-infer-zoncolan-scaling]{28}. This disconfirms a blanket "advisory degrades" claim, with four caveats:
  - The counter-evidence is the builders' own data, and Tricorder's click metrics undercount ignoring
    [google-tricorder-icse2015]{27}.
  - Google's review-time findings are non-blocking by default but socially enforced: "Reviewers typically withhold
    approval of a change until all their comments, manual and automated, have been addressed"
    [google-static-analysis-lessons]{26}.
  - The Facebook source does not say whether Infer's diff-time reports gate landing
    [facebook-infer-zoncolan-scaling]{28}, so the over-70% fix rate is not shown to come from purely advisory delivery.
  - Zoncolan's action rate above 80% covers a funnel in which the security on-call "validates the alarm reported,
    blocks the diff" when appropriate [facebook-infer-zoncolan-scaling]{28}, so it is not evidence about purely
    advisory signals.
- **In long-running tool use, many alerts are acted on, just slowly.** A median 36.7% of Coverity alerts in long-running
  open-source projects were fixed by code change [coverity-alert-actionability-oss]{31} {confidence: abstract-only}.
  This is higher than the near-zero figures from batch deployments in the industrial reports
  {inferred: divergence}, though the definitions and time windows differ.
- **Where degradation is reported, placement and volume recur more than advisory status** {inferred: aggregate}. Ignored
  advisories in this sample are build-time compiler warnings [google-static-analysis-lessons]{26}, dashboards and batch
  lists outside the workflow [google-static-analysis-lessons]{26}, [facebook-infer-zoncolan-scaling]{28}, high-volume
  email alerts [sre-monitoring-distributed-systems]{32}, and high-volume, repeated, interruptive clinical alerts
  [cds-alert-fatigue-repeats]{37}. In the clinical tiering study the low tier was information-only, and "by design at
  the tiered site, no response was collected for Level 3 alerts" [ddi-alert-tiering-compliance]{36}. So the evidence that
  advisory-only display helps is indirect: making the low tier advisory went with higher compliance on the tiers that
  stayed interruptive {inferred: aggregate}.
- **Override is not the same as degradation.** Clinical appropriateness data show many overrides are correct decisions
  [cds-outpatient-override-appropriateness]{35}, [cpoe-alert-override-review]{34}. A high non-action rate on an advisory
  can reflect correct dismissal of low-value warnings rather than lost attention.
- **No time-decay found where it was tested.** Newly deployed reminders did not show declining response over time
  [cds-alert-fatigue-repeats]{37}. This cuts against an "exposure alone wears signals down" mechanism, though it was
  tested on 6 alerts.
- **Search outcome.** The disconfirming evidence is substantial for "advisory at review time, curated, low-volume". I
  found none, in the attested sources, for advisories delivered as high-volume batch output to general developers.

## Limits

- **Builder-reported evidence.** The software numbers (F1-F6, F15, F16) come from organizations reporting on their own
  tools in experience-report venues. None of them reports a control group {inferred: aggregate}, and the Facebook batch arm is 20-30
  issues.
- **Thin independent software measurement.** Independent software evidence is one 20-person interview study
  (perceptions) and one mining study read only as an abstract [coverity-alert-actionability-oss]{31}.
- **Adjacent-domain transfer.** The clinical and SOC findings involve interruptive alerts, safety stakes, and
  professional populations unlike developers reading lint output. Using them for software is an analogy
  {inferred: aggregate}.
- **Thresholds are not validated against outcomes.** Google calls its 10% figure initially "somewhat arbitrarily"
  chosen [google-static-analysis-lessons]{26}. The clinical 40% maximum override rate is reported without explanation
  [cpoe-alert-override-review]{34}.
- **Not fetched.** Prior work cited inside these sources was not fetched or attested: the FindBugs Fixit paper, the
  RacerD fix-rate paper, the Shah et al. ambulatory tiering study, and the Bates et al. override-rate proposal. Claims
  that depend on them appear only as cite-through.

## Revisit if

- An independent, controlled or quasi-experimental study compares the same warnings delivered at review/diff time vs
  batch, or blocking vs advisory, for developers.
- The full text of the Coverity open-source mining study [coverity-alert-actionability-oss]{31} is read, especially
  how alerts were delivered and the severity-lifespan analysis.
- New evidence ties a numeric false-positive or not-useful threshold to adoption or abandonment outcomes.
- Evidence appears on advisory warnings in documentation or prose linters, as opposed to code analyzers.
- Evidence appears on warnings whose consumer is an automated agent rather than a human.

## Decision relevance

For someone deciding whether a citation linter's non-blocking advisories should be reclassified, suppressed, or kept,
the sources suggest the question is less "advisory or blocking" and more about the following {inferred: aggregate}:

- **Delivery point.** Are advisories shown on the changed material at review time?
- **Action rate.** Is the action rate (or a not-useful rate) per check measured, with noisy checks put on probation or
  removed?
- **Explanation.** Does each advisory explain itself and suggest a fix?
- **Volume and repetition.** Are repeats and volume kept low?
- **Blocking.** Is blocking reserved for checks that are effectively never wrong?

Thresholds such as 10% are only meaningful once the false-positive definition being used is stated.

## Revisions

- 2026-10-19 — Correction (position preserved): restored tiering, click-undercount and survivor-effect qualifiers,
  softened the summary generalization, and extended the Zoncolan attestation with the on-call blocking passage; see
  `../verification-checklist.md`, "Revision response (2026-10-19)".
- 2026-10-19 — Correction (position preserved), bounded pass after the adversarial re-read: removed "non-blocking"
  for Facebook's diff-time findings (summary and Disconfirming analysis), retitled the review-time disconfirming
  bullet, and added the caveat that the Facebook source does not say whether those reports gate landing; see
  `../verification-checklist.md`, "Bounded correction response (2026-10-19)".

## Sources (corpus numbering)

26. **google-static-analysis-lessons** — Lessons from Building Static Analysis Tools at Google. Caitlin Sadowski, Edward Aftandilian, Alex Eagle, Liam Miller-Cushon, Ciera Jaspan. Communications of the ACM 61(4), April 2018. Fetched 2026-10-18. Source: https://6826.csail.mit.edu/2020/papers/google-analysis-cacm.pdf. Engagement: full-text.
27. **google-tricorder-icse2015** — Tricorder: Building a Program Analysis Ecosystem. Caitlin Sadowski, Jeffrey van Gogh, Ciera Jaspan, Emma Söderberg, Collin Winter (Google). ICSE 2015, Florence. Fetched 2026-10-18. Source: https://www.cs.umd.edu/class/spring2019/cmsc414/papers/tricorder-building-a-program-analysis-ecosystem.pdf. Engagement: full-text.
28. **facebook-infer-zoncolan-scaling** — Scaling Static Analyses at Facebook. Dino Distefano, Manuel Fähndrich, Francesco Logozzo, Peter W. O'Hearn. Communications of the ACM 62(8), August 2019. Fetched 2026-10-18. Source: https://6826.csail.mit.edu/2020/papers/facebook-infer-cacm.pdf. Engagement: full-text.
29. **coverity-billion-lines** — A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World. Al Bessey, Ken Block, Ben Chelf, Andy Chou, Bryan Fulton, Seth Hallem, Charles Henri-Gros, Asya Kamsky, Scott McPeak, Dawson Engler. Communications of the ACM 53(2), February 2010. Fetched 2026-10-18. Source: https://6826.csail.mit.edu/2019/papers/coverity.pdf. Engagement: full-text.
30. **static-analysis-underuse-interviews** — Why Don't Software Developers Use Static Analysis Tools to Find Bugs? Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, Robert Bowdidge. Venue not printed on the fetched PDF (cited as ICSE 2013 in source 41). Fetched 2026-10-18. Source: https://people.cs.gmu.edu/~johnsonb/docs/icse2013.pdf. Engagement: full-text.
31. **coverity-alert-actionability-oss** — How Do Developers Act on Static Analysis Alerts? An Empirical Study of Coverity Usage. Nasif Imtiaz, Brendan Murphy, Laurie Williams. IEEE ISSRE 2019 (October 2019). Fetched 2026-10-18. Source: https://www.microsoft.com/en-us/research/?p=690690. Engagement: abstract.
32. **sre-monitoring-distributed-systems** — Monitoring Distributed Systems (Chapter 6, Site Reliability Engineering). Written by Rob Ewaschuk, edited by Betsy Beyer; Google, published by O'Reilly, copyright 2017. Fetched 2026-10-18. Source: https://sre.google/sre-book/monitoring-distributed-systems/. Engagement: full-text.
33. **soc-false-positive-alarms** — 99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms. Bushra A. Alahmadi, Louise Axon, Ivan Martinovic (University of Oxford). 31st USENIX Security Symposium, 2022. Fetched 2026-10-18. Source: https://www.usenix.org/system/files/sec22summer_alahmadi.pdf. Engagement: full-text.
34. **cpoe-alert-override-review** — Overriding of Drug Safety Alerts in Computerized Physician Order Entry. Heleen van der Sijs, Jos Aarts, Arnold Vulto, Marc Berg. J Am Med Inform Assoc 13(2), 2006. Fetched 2026-10-18. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC1447540/. Engagement: full-text.
35. **cds-outpatient-override-appropriateness** — Overrides of medication-related clinical decision support alerts in outpatients. Karen C Nanji, Sarah P Slight, Diane L Seger, et al. J Am Med Inform Assoc 21(3), 2014 (epub 2013). Fetched 2026-10-18. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3994856/. Engagement: full-text.
36. **ddi-alert-tiering-compliance** — Tiering Drug-Drug Interaction Alerts by Severity Increases Compliance Rates. Marilyn D Paterno, Saverio M Maviglia, Paul N Gorman, Diane L Seger, Eileen Yoshida, Andrew C Seger, et al. J Am Med Inform Assoc 16(1), 2009. Fetched 2026-10-18. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2605599/. Engagement: full-text.
37. **cds-alert-fatigue-repeats** — Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system. Jessica S Ancker, et al. BMC Medical Informatics and Decision Making 17:36, 2017. Fetched 2026-10-18. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5387195/. Engagement: full-text.
