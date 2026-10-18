---
id: feature-quality-verification
kind: feature
stage: implementing
tags: [methodology-review, research-pipeline, agentic-research, review]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
research_refs: [quality-feedback-loops]
---

# Enforce meaningful quality checks across the research workflow

## Brief

Use the quality-enforcement question as a real methodology-review pilot, then
implement the supported gaps across Research Pipeline, Agentic Research and
methodology-review. Absorbs idea-quality-verification-loop,
cross-model-review-prompt-ware and version-number-warn-noise. Andrew authorized
the suggested research → live pilot → implementation sequence and all three
backlog items: "let's move forward with all of that work".

This item owns the live review controller and subsequent cohesive implementation.
Research commissioning is separate; its completion cannot close this controller.
The package dependency/install experiments, citation-gate resolver repairs, Pi,
publication, cache installation and upstream messaging are outside this scope.

## Strategic decisions and authority

- Preserve the retained Agile Workflow + Research Pipeline process and ARD's
  authoritative research ownership. Workbench is prior art, not a migration target.
- Compare existing checks before adding loops; implementation targets evidenced
  gaps rather than imposing one identical loop on every layer.
- Carry forward Andrew's mixed-scope and standard research-verification preference.
- User authorization covers local investigation, work tracking, design and tested
  fixes for these three items. Honor existing delivery review weights and prior
  decisions. Ask only for a consequential new direction beyond that brief.
- No new service, tracker, public skill family or UI is proposed. Medium scope;
  three related implementation units are provisional until research and assessment.
- The citation backlog's old Pipeline-vendoring path is historical. Inspect current
  canonical ownership and preserve generated-data contracts before choosing a fix.

## Simplification opportunity

Reuse existing research verification and delivery-review machinery; make outcomes
and evidence explicit at their owners. Avoid duplicate independent reviews for
already-reviewed content, nested unlimited correction loops, host-specific hooks
without demonstrated need, and a copied citation kernel in Research Pipeline.

## Acceptance

- Ground the quality-loop choice in primary external evidence and current local
  contracts, distinguishing designed behavior from executed evidence.
- Exercise actual component assessment, parent integration and a durable resume
  checkpoint on this repository; do not describe synthetic tests as a live pilot.
- Enforce meaningful success/failure outcomes without treating missing checks,
  retained major risks, process completion or warning counts as proof of quality.
- Resolve the three absorbed ideas, preserving existing review weights and user
  authority, with proportionate behavioral/structural checks on both host shapes.
- Complete one independent standard feature review, verify accepted fixes, and
  obtain a fresh whole-scope methodology assessment for any clean pilot outcome.

## Methodology review QVE — charter and checkpoint 1

Baseline: 70348687, plus this scope record. Root round: 1 allocated; 0 complete;
shared limit: 5. Scope: quality enforcement, independent review routing and
citation warning signal in the retained workflow. Excludes claims about all
possible agent tasks, release publication and infrastructure changes.

Users: operators and agents conducting grounded research and changing skills.
Outcome: completion claims backed by the required evidence, with actionable
feedback and bounded correction cost. Criteria: detection of material defects,
independence and scope of verification, authority, interruption recovery, cost,
false-positive burden, portability and maintenance ownership. Compare common
success, failed-check, changed-output, exhausted-limit and resumed-review paths.

Shape: review program with three focused component assessments. An unsplit
review would obscure independently changeable policies; a cut by plugin would
repeat shared questions about evidence and closure. Each child has one cycle in
root round 1. Root owns shared quality criteria, external evidence and integration.
Children inherit baseline, limits and exact authorization; parent assesses combined
consequences. Their reports live in named sections here, with root/parent backlinks.

| Child | Scope and contribution | Research / next checkpoint |
| --- | --- | --- |
| QVE-E | Quality thresholds, feedback and stopping across the workflow; identify existing guarantees and any missing enforcement | Reuse one shared bounded external engagement, then compare local contracts |
| QVE-R | Independent review of consequential skill/doc changes; avoid unreviewed changes and duplicate passes | Local routing inspection plus shared external evidence; return scoped assessment |
| QVE-S | Citation pattern warnings as an actionable quality signal; preserve true citation-integrity checks | Reproduce current behavior and inspect ownership; return scoped assessment |

New findings use originating review IDs. Initial outcome: none yet. No research
or assessment has completed at this checkpoint. Next: grounded comparison and
component reports, then parent decision packet using existing implementation
approval where the proposed change fits this scoped brief.

## Original backlog inputs (historical context)

The following captures preserve the original requests and old paths. Current
ownership and implementation decisions above and in later assessments control.

### idea-quality-verification-loop.md

```text
---
id: idea-quality-verification-loop
created: 2026-10-18
updated: 2026-10-18
tags: [research-pipeline, agentic-research, methodology-review]
---

# Borrow doc-review's quality verification loop

Consider whether the loop Andrew describes in doc-review—requiring an explicit
quality level and checking that it has been reached—can be borrowed for
research-pipeline, agentic-research, and/or methodology-review. Explore feasibility
and where this belongs when this idea is picked up; no implementation is requested
as part of the current methodology-review decomposition work.
```

### cross-model-review-prompt-ware.md

```text
---
id: cross-model-review-prompt-ware
created: 2026-06-09
tags: [agile-workflow, research-pipeline, review, workflow, medium-priority]
---

The peeragent cross-model (Codex) review loop earned its keep during the ARD arc — it
caught real false-assurance bugs in single-author **prompt-ware** that the test suite
structurally cannot (over-claimed `N` enforcement, the isolated-evaluator passage-support
gap, a parallel-INDEX write race). Those bugs lived in SKILL.md / docs prose, not code.

**Already wired (verified 2026-06):**
- `agile-workflow:review` runs a cross-model peer pass on its standard/deep lanes.
- `research-pipeline:feature-design` / `epic-design` run a cross-model advisory pass
  under autopilot for risky decisions.

**The gap:** changes to the **skills/docs themselves** (the prompt-ware that defines the
pipeline) get no automatic cross-model pass. The ARD arc's review was a manual
`/peer-review` invocation that only happened because the user asked. A future
high-blast-radius prompt/skill edit could ship without it.

**Possible fixes (decide when next touching the review/checkpoint skills):**
- A documented convention: "run `/peer-review` before merging foundational prompt/skill
  changes" (cheapest; relies on discipline).
- A checkpoint/gate option in `quality-checkpoint` that triggers a cross-model pass when
  the bundle touches `*/skills/*/SKILL.md` or plugin `docs/`.
- A PreToolUse/Stop hook nudge when SKILL.md edits are detected on a branch.

Tracks the `multi-model-review-setup` memory's deferred-wiring note. Medium priority.
```

### version-number-warn-noise.md

```text
---
id: version-number-warn-noise
created: 2026-06-09
tags: [research-pipeline, citation-lint, vendored, low-priority]
---

The vendored ARD citation lint's pattern catalog flags any `X.Y`-shaped string as a
`version-number` advisory `[warn]` — including innocuous prose and titles like
"OAuth 2.0" (confirmed in the ARD-arc e2e run), not just numbered `## Sources` lists.

**Impact:** cosmetic only. It's an advisory `[warn]`, never a broken chain, and
`research-pipeline:gate-citations` ignores pattern flags (never emits items for them).
But it's noisier than the producer docs imply ("numbered Sources lists trip it"), which
can erode trust in an otherwise-clean lint ("my clean brief has 3 warnings").

**Constraint:** the pattern lives in the **vendored** `plugins/research-pipeline/scripts/catalogs.json`.
Pin-don't-fork — do NOT patch it locally (the verbatim guard + conformance assume the
vendored kernel is byte-identical to the pinned ARD release).

**Fix options:** (a) tighten the `version-number` pattern upstream in ARD, then pull it
on the next ARD re-sync (see `docs/ard-adoption-plan.md` § Re-sync procedure); or
(b) raise it to ARD as a false-positive report. Low priority.

Surfaced by the post-arc review; see `plugins/research-pipeline/docs/ard-adoption-plan.md`
§ Deferred follow-ups.
```

## Component returns — root round 1 (2026-10-18)

All children inherit QVE's charter, 70348687 baseline (91b8c5eb only adds work
records), root round 1 allocated / 0 complete / limit 5, authority and exclusions.
Root/parent backlink for each is this item's QVE section. Child outcomes are
**awaiting change or evidence**; returned reports alone complete no root round.
These are local operational assessments, not research-source attestations.

### QVE-E — quality criteria and outcomes

Driver assessment: doc-review already fixes Critical/High findings and requires a
fresh audit with a cap; methodology-review already requires a whole-scope assessment
and zero unresolved major findings; AR already owns lint, adversarial reading,
conditional evaluation and terminal spot-check. Standard delivery review already
prescribes one independent pass then verified correction. No evidence supports a
uniform repeated loop across all these owners.

- **QVE-E/METH-001, major, supported contract ambiguity:** quality-checkpoint's
  Phase 4 first branch equates zero emitted blockers with readiness. Gate errors
  and doc-review residual Critical/High counts can coexist with zero emitted items.
  Its earlier error-blocker instruction is contrary evidence; this is inconsistent
  closure prose, not a demonstrated production false-clean incident.
- **QVE-E/METH-002, major execution gap:** actual `work-view --stage done
  --no-release --paths` exits 1 (unknown flag); `--stage implementing,drafting
  --paths` exits 0 with no matches despite current items in both stages. No
  gate-infra skill exists in either plugin. Base gates require a real release,
  while doc-review accepts no release-version argument. These interfaces cannot
  execute the advertised virtual sweep faithfully.
- **QVE-E/METH-003, minor clarification:** record actual required-check outcomes,
  scope/baseline and evidence in existing research/review records. Process success
  is not an approving verdict. Preserve existing owner-specific stops and weights.

Prefer a result-based checkpoint with supported discovery and explicit incomplete
preflight for unbound work, over a new universal loop or leaving the contract
unchanged. Required missing/error/stale checks and residual blockers prevent
readiness. No remedy applied; research verification and parent assessment pending.

### QVE-R — independent delivery-review routing

Fresh component assessor `/root/quality_review_routing` inspected current contracts
and recovered two archived records; it did not rerun their historical peer jobs.
`agile-workflow:implement` supports prose features and invokes normal feature
review; `agile-workflow:review` owns weights, one-pass standard, child verification,
and standalone inline review. Historical missing-review claim is superseded by
these rules and recorded Claude passes at `ca4f0daa` (feature-methodology-review)
and `7c17b1de` (feature-methodology-review-decomposition).

- **QVE-R/METH-001, minor:** `.work/CONVENTIONS.md` still names manual `/peer-review`
  and the absorbed backlog item. Replace this stale route and clarify reuse of
  covering delivery review plus accepted-fix verification. No escaped defect was
  demonstrated; existing feature routing is strong contrary evidence.
- **QVE-R/METH-002, minor:** build-process's light/standard/deep shorthand conflicts
  with canonical weights none/light/standard/thorough/maximum. Deep lenses do not
  authorize extra standard passes.

Prefer a concise project/Pipeline convention and checkpoint evidence reconciliation.
Reject unconditional file-triggered peer gates or hooks: they duplicate reviews,
ignore deliberate story exceptions, and require new host/deduplication machinery
without an observed routing miss. A changed hash from accepted verified fixes does
not invalidate standard review; materially uncovered contracts require their normal
review owner. Recover archived review bodies through git_ref. No remedies applied.
Next: root integration, actual cross-host execution and fresh whole-scope assessment.

### QVE-S — citation-warning signal

Fresh component assessor `/root/quality_citation_signal` ran 17 synthetic CLI
fixtures at each threshold none/low/medium/high and compared the public shim.
Raw temporary evidence: `/tmp/qve-s-fixtures-3cc8zvv3/summary.json` and
`baseline-checks.json`. These are synthetic experiments, not research substrate.
Reproduce via canonical `ard-core/kernel/lint-citations.py <fixture>
--attestation-dir <fixtures>/attestation --analysis-dir <fixtures>/analysis
--no-url-check --format json --exit-code-on low`.

Observed version warnings for neutral OAuth 2.0 prose/headings, version-bearing
source titles, hierarchical 1.1 labels, decimals, quoted/source-direct version
prose, factual v2.1.0 and lower-case version 3 claims, including cited claims.
Ordinary numbered 1./2. Sources lists and existing code/URL/frontmatter masks
produce none; upper-case Version 3 is also missed. Advisory-only cases exit zero
at every threshold. A missing-handle control exits zero by default and one at all
blocking thresholds. The shim matches all 17 high-threshold runs. Conformance
57/57 and catalog generation check pass. The ARD tree matches upstream 43f7f4bf
at the assessed baseline; generated catalogs contain descriptions, not matchers.

- **QVE-S/METH-001, minor:** broad token matching produces reproduced false
  positives. Warning fatigue/trust effects are plausible, not measured. The
  advisory status, preserved recall and existing ban on emitting pattern items
  are strong contrary evidence against treating this as an integrity failure.
- **QVE-S/METH-002, minor:** gate-citations incorrectly attributes these warnings
  to ordinary numbered Sources lists. Correct the trigger explanation and separate
  execution, broken chains, thin attestations, advisory counts and semantic support.

Child recommends bounded canonical narrowing plus clearer reporting, with positive
controls for explicit/unprefixed/comparative version facts. Retaining matching with
clearer reporting is the fallback if recall or maintenance costs dominate. Do not
suppress headings or cited lines wholesale. No remedy applied; parent must choose
and record the tradeoff. Canonical changes require an explicit narrow fork patch;
retired Pipeline vendoring is not current ownership. Root owns integration and
external evidence; no second unchanged child cycle is requested.

### Pending independent integration checkpoint

Claude Opus fresh-context job `20261018T224044Z-6d8d1ec7` is commissioned for two
separately reported duties: standard adversarial verification of the external
brief, and initial full-charter QVE assessment combining all three reports.
The lead spot-check, parent decision/design, actual implementation, live record
resume exercise, cross-host verification, standard feature review and fresh
post-change whole-scope assessment remain outstanding. No clean outcome yet.
## QVE parent assessment 1 and adjudication (2026-10-18)

Independent Claude Opus job `20261018T224044Z-6d8d1ec7` returned terminal success,
with two separate substantive results: research **NEEDS-REVISION**, methodology
**Awaiting change or evidence**. Success means the worker completed, not that
its subjects passed. Assessment baseline remains 70348687 for product contracts;
48971393 adds the scope, source evidence and child records only.

The assessor evaluated the full QVE charter using all three reports, shared
scenarios and research, inspected the checkpoint/conventions/citation surfaces,
and independently reproduced both unsupported query behaviors, missing infra
gate, OAuth advisory and conformance 57/57. It found one unresolved major issue:
**QVE-E/METH-001**, strengthened by the silent empty combined-stage query. No actual
false-clean release was observed. **QVE-E/METH-002** remains a required material
execution correction, but its visible failures are not independently major; the
silent query risk is counted once under METH-001. This evidence-based classification
avoids duplicate major counts rather than withdrawing either remedy.

QVE-E/METH-003, QVE-R/METH-001/002 and QVE-S/METH-001/002 remain minor. New
**QVE/METH-I01, minor**: the result-evidence rule must also reach build-process
Completion and local delivery conventions, because this repository normally ships
without a repo-level release checkpoint. The assessor recommends keeping citation
matching and improving reports: token narrowing risks recall and ongoing kernel
fork maintenance without measured corpus-wide benefit. That is contrary to QVE-S's
preferred matcher change; parent selects reporting/clarity and records retained
minor raw noise. No new matcher work item is warranted without observed burden.

Coverage limits: initial assessor consumed child evidence but did not reread AR
orchestrator, upstream implement/review/release-deploy, hooks or recovered historical
review bodies; it repeated one of the 17 citation fixtures. Research source checking
was attestation-based; the driver owns actual-source spot-check. These limits remain
explicit, and all post-change full-scope obligations remain open. No remedies are
verified at this point; child minor counts did not determine the parent's verdict.

Round 1 is now complete: **1 completed of 5**, no round 2 allocated yet. Primary
outcome: **Awaiting change or evidence**. Research corrections/verification,
implementation, delivery review and fresh whole-scope assessment are outstanding.

### Recovered live handoff

Fresh-context `/root/qve_resume` restored the actual record at clean 48971393 to
`/tmp/qve-live-resume.md`, before this result was integrated. It correctly recovered
three children, existing authority, baseline, round 1 allocated / 0 complete / limit
5, pending research and the already commissioned peer job. It did not infer worker
success, close research or root rounds, reset counters, duplicate dispatch or ask
again for settled permission. It identified the missing durable job result as the
next evidence gap. This is an executed real-record handoff exercise, not a simulated
crash or a new assessment; this section persists its result. The assessment above
now supersedes that pending state without discarding its checkpoint history.

### Shape refinement from returned evidence

The component returns reveal a shared adoption schedule and coupled readiness
contract, rather than three independent change schedules. Refine **review program →
coordinated review**, preserving QVE-E/R/S, findings, charter, baseline history and
shared count. Children feed one parent decision and reassessment. This is routine
decomposition within the authorized scope, not a new operator decision or fresh
round allowance. No research or delivery owner changes.

## Design decisions and implementation design

Research Pipeline feature-design directional pass: existing user answers pin
scope, whole-review decomposition, mixed/standard research, local iteration and
all three absorbed ideas. Zero unresolved strategic questions remain. No UI or
new external side effect is proposed. The independent research revision gate is
still pending; no research-completion claim or product implementation is made yet.

### Options and selected approach

1. A common repeated quality engine: uniform appearance, but duplicates ARD,
   changes agreed standard-review cost and combines incompatible closure rules.
2. **Selected: explicit evidence at existing owners, with a corrected checkpoint.**
   Fix reproduced interfaces and ambiguous readiness, clarify review reuse and
   group noisy advisories. Preserve every owner's rigor, authority and stop rules.
3. Keep current prose or add only a filename-triggered review hook: smaller patch
   or more automatic reminders, but neither fixes the observed false-empty query
   and incomplete-result readiness paths; the hook adds unsupported coordination.

Parent decision uses Andrew's existing authorization for tested in-scope fixes.
Retain canonical citation matching and known minor raw advisory noise. This is a
technical precision/recall and maintenance choice; no claim of noise elimination.
The old vendoring prohibition is historical, but upstream ownership still requires
any selected AR change to be a documented narrow fork patch. The planned AR patch
only clarifies verification records and changes no kernel/schema/profile.

### Unit 1 — checkpoint contract (trickiest unit)

File: `plugins/research-pipeline/skills/quality-checkpoint/SKILL.md`.
Public inputs remain `<version>` and `--pending`; outputs are existing work/release
record sections, owned gate findings/reports and a readiness recommendation.

- Real version: supported work-view release query; exclude release controller;
  recover archived bodies, scope and review evidence. Resolve configured delivery
  gates plus applicable doc-review/citations and explicit existing exclusions.
- Pending: supported all-tier done query plus frontmatter null-binding selection;
  preflight only, no invented release ID, implicit binding or unsupported gate call.
- Doc-review uses its supported document arguments, before scans where possible;
  capture its mutations/current baseline and actual root report path.
- Sequential supported public skill calls; preserve gate extension policies.
- Record each required check's scope/baseline, criterion, result/evidence and
  unresolved obligations. Missing/error/stale/uncovered results prevent readiness.
- Query drafting, implementing and review separately. Reconcile existing findings
  and owner thresholds; zero new items cannot erase residual doc-review findings.
- Outcome precedence: preflight; incomplete checks; changes required; ready within
  checked scope. List all obligations even when several labels apply.
- Reuse standard review with its accepted-fix verification; changed hash alone is
  insufficient to demand another pass. New materially uncovered contracts return
  to the ordinary delivery owner. Do not alter none/light or story exceptions.

Acceptance: the seven forward cases distinguish failed/capped checks, all-pass with
verified standard fixes, uncovered new authority, stale scans, advisory-only lint,
missing research verdict and real-binary pending discovery. Both hosts must produce
actual checkpoint artifacts from raw cases without expected-answer prompting.

### Unit 2 — verification records and delivery routing

Files: AR `skills/research-orchestrator/SKILL.md` plus directly linked
`references/verification-record.md`; methodology-review SKILL and review-record
reference; RP build-process/research-composition; `.work/CONVENTIONS.md`.

Use existing body/transcript/campaign homes, not a new schema/tracker. Make required
gates, actual results, scope/input identity and next obligations recoverable. A
worker's successful process without an approving report is not a passed gate.
Preserve AR's floor/reachability/isolation and second-pass stop, methodology's
whole-charter fresh assessor/shared limit, and standard delivery's one-pass policy.
Record the AR wording-only fork exception in current project navigation. Update
Completion so non-release delivery also requires actual evidence.

### Unit 3 — citation signal and documentation alignment

File: RP `skills/gate-citations/SKILL.md`. Preserve JSON, canonical matcher,
thresholds and item emission. Report execution, broken chains, thin attestations
and grouped advisory counts/examples separately, with raw lint output available.
Correct numbered-list examples; explain default exit zero and semantic limitations.
Align RP README and gate-extension references with configured sequential checks;
remove nonexistent infra and fixed-eight-gate claims in the touched process docs.

### Verification and risks

Run existing RP portability and AR metadata checks; validate changed skill shapes,
linked reference paths and both manifest/marketplace forms. Existing canonical
conformance/catalog checks protect unchanged ARD ownership; inspect upstream drift.
Run the independent raw-input forward cases on Codex and Claude, then actual local
pending discovery. Regenerate knowledge indexes from sources and lint them.

Main risks: stricter readiness could accidentally force extra standard reviews;
fixtures include covering review plus verified fixes. Missing checks could be
silently excluded; declaration/result cases exercise unavailable evidence.
Doc-review mutations can stale earlier scans; test explicit changed-input coverage.
Citation clarity cannot remove raw heuristic noise; preserve that limitation.

One cohesive inline implementation owner; the research story remains its own
commissioning checkpoint. No implementation fan-out or extra delivery stories are
needed. Effective feature review weight is standard. After verified implementation,
run one independent delivery pass and a fresh whole-charter methodology assessment;
a combined dispatch must return distinct outcomes and actually cover both duties.

## Implementation start

Execution capability: current Codex quality-first driver, inline under the no-code
deliverable exception. Effective review weight: standard (project/default).
Independent component discovery already mapped the integration surface; no extra
implementation exploration or fan-out is needed. Product changes fix reproduced
local contracts and do not depend on the research's disputed modal wording. The
research story remains open while its surfaced correction check runs; no completion
or clean-pilot claim can bypass that obligation.

The design's seven initial forward scenarios are expanded to nine per host by adding
a missing required skill and a previously tracked open finding queried through the
actual binary. This protects false-clean paths without testing exact prose.
## Implementation and verification checkpoint (2026-10-18)

Implemented the three units at their existing owners. Quality-checkpoint now uses
configured gates, supported single-stage discovery, pending preflight, current
result evidence, existing review receipts and residual doc-review findings. It
runs doc-review before scans and preserves each owner's correction limits.
Research and methodology records now retain required results and pending work.
Citation summaries separate execution/chain/thin/advisory/semantic facts without
changing the detector or JSON. Updated delivery conventions, build-process,
composition, README and both extension docs; documented the narrow AR record patch.

Simplification: replaced the fixed eight-gate/fake-release recipe with one
configured sequence and removed stale infra, report-path, parallel-doc-review and
manual peer-review directions. No generic quality engine, score, hook, new gate,
work schema, kernel copy or mandatory additional standard review was introduced.
The canonical ARD kernel remains unchanged; minor raw version-warning noise remains.
The companion invocation example now accepts either host's plugin-root variable;
resolver selection behavior itself is outside scope and unchanged.

Research commissioning completed at 8870f1b9 with an actual APPROVED correction
check and lead spot-check. Its record preserves the surfaced second NEEDS-REVISION
and bounded correction verification rather than claiming a first-pass approval.
No research gate is now pending. Root round count remains 1 completed of 5.

Executed validation:

- RP skill-portability and AR skill-metadata checks pass under uv/PyYAML.
- Canonical ARD conformance: 57/57; generated catalog check passes.
- Four changed SKILLs pass the system quick validator and stricter portable
  frontmatter checks: quality-checkpoint 170 lines, gate-citations 203,
  methodology-review 290, research-orchestrator 415. New reference is under 200.
- Linked new resources resolve; affected Claude/Codex manifest identity/version and
  skill discovery match. Both marketplace inventories and normalized source
  coordinates match. The first ad-hoc checker wrongly required identical host
  description prose and compared external source objects to paths; inspection
  confirmed existing host-specific descriptions and equivalent git-subdir shapes,
  so the checker was corrected rather than editing valid manifests.
- The documented companion invocation resolves a usable canonical lint with either
  PLUGIN_ROOT or CLAUDE_PLUGIN_ROOT. No cache/version or resolver logic changed.
- Knowledge regeneration: 16 documents, no lint errors/warnings. git diff --check
  passes. No unrelated runtime build is applicable to these instruction changes.
- Actual repository pending discovery: supported all-tier done query plus null
  release-binding selection finds 13 items (including the completed research child).
  Result is preflight only; no binding, virtual release gate or readiness claim.

Forward fixture root:
`/var/folders/z5/_qtmw2jj3jb1rgyklh1ngm1r0000gn/T/quality-forward-sqo9t_13/`.
Fresh Codex worker executed all nine raw cases and wrote actual result.md files;
driver read each. No expected answers, feature design or prior conclusions were
provided. Results: residuals → incomplete plus capped High; covered_fix → ready
within supplied scope without another standard reviewer; uncovered_change → missing
new-contract review; stale_check → refresh affected scans; unavailable → required
skill missing; tracked → changes required for the real queried open finding;
pending → preflight only using actual binary; advisories → zero items, grouped
nonblocking patterns, no semantic claim; research_receipt → unresolved/missing
verdict and terminal spot-check, commissioning stays open. All intended invariants
held. Captured gate facts are labeled hypothetical, not claimed live gate executions.

Claude forward job `20261018T225256Z-810fc8ce` is still running. Its actual outputs,
standard independent feature review and fresh whole-charter QVE assessment remain
required before closure. The live pilot evidence is the actual component assessments,
parent integration, source research and recovered record; the nine-case exercises
are separate synthetic forward tests. No general effectiveness claim follows.

No durable test code was added for prose matching. Existing structural interfaces,
real command behavior and independent task execution provide proportionate evidence.
No adjacent work item was emitted; the resolver/package-install experiments and Pi
remain outside this arc. Any difference from the provisional child advice is recorded
in the parent decision, particularly retaining citation matching.

## Integrated verification and QVE round 2 allocation

Claude forward job 810fc8ce returned terminal success with all nine actual reports.
Driver read every report from both hosts. Outcomes match the recorded invariants;
both used actual supported work-view queries for pending/tracked cases. The initial
tracked fixture accidentally retained a no-binding-authority sentence copied from
pending. Claude correctly surfaced that contradiction. Driver preserved initial
inputs/results, corrected the fixture to its intended authorized binding, and
reran only tracked on both hosts. Native Codex and Claude continuation job
`20261018T225656Z-80609280` both returned the intended changes-required result for
the still-open High finding, without a duplicate standard reviewer. This repaired
test input did not require a product change or a broader rerun.

All implementation acceptance evidence is now present. The synthetic runs' writes
were deliberately restricted to result.md rather than actual release/commissioning
records; that fixture limit is not an unperformed production migration. Real-record
resume and actual repository preflight evidence are recorded separately above.

Product baseline: **4575547d**. No product contracts changed after that commit.
Research child is done, both-host verification is green, and this feature advances
to review. Effective delivery weight remains **standard, one independent pass**.

Allocate **QVE root round 2**, with **1 completed of 5**. The fresh combined
assessment will cover QVE-E/R/S and the whole charter on this baseline; existing
child findings/IDs and original coverage remain inputs. No independent child
cycle is allocated. One fresh Claude dispatch will perform two explicit duties:
standard integrated feature review, and full-charter methodology assessment.
Their outcomes must remain separate; neither a completed process nor the partial
initial assessment supplies a clean final verdict.

## Standard review and QVE round 2 (2026-10-18)

Fresh Claude Opus xhigh via peeragent job `20261018T225833Z-56043ead` returned
terminal success with two actual reports. Delivery verdict: **Approve with
comments**, no reviewer-designated blockers. This is the single standard feature
pass. Product snapshot 4575547d, operational HEAD 13711e20. The report below is
preserved verbatim; host adjudication follows and controls next actions.

> I made no repository edits, staging or commits. Scratch output is under `/tmp/rvw-*` only.
> 
> # Duty 1: feature review of feature-quality-verification (standard weight, one independent pass)
> 
> **Verdict: Approve with comments.** I found no blockers. The new checkpoint now works with the real `work-view` interface, ties readiness to actual results and leftover doc-review findings, and reuses a completed standard review instead of asking for another. There are two Important issues, both on less common paths, and four nits. The host owns how to classify them.
> 
> ## Blockers
> None.
> 
> ## Important
> - **I-1. Pending preflight counts `[research]` engagements that release-deploy never binds.** `quality-checkpoint/SKILL.md:36-41` picks every unbound, done, non-release item from `--scope all --stage done`. Release-deploy leaves out `tags: [research]` items when Agentic Research is installed (`release-deploy/SKILL.md:91-113` and `:144-147`), and it is installed here.
>   - On this repository the query returns 13 items. Two of them are research items: `active/stories/story-research-quality-feedback.md` and `archive/story-research-package-boundary.md`. The feature record (`feature-quality-verification.md:504-506`) accepts all 13 as correct.
>   - Impact: the preflight overstates scope. Nothing becomes falsely "ready", because pending mode only reports and release-deploy filters again.
>   - Fix: in pending mode, drop `[research]` items using `work-view --scope all --tag research --paths`, as release-deploy does, and correct the record to 11.
> - **I-2. Refreshing doc-review after it hits its cap contradicts "no new correction budget".** The checkpoint says to refresh changed checks under each owner's rules without resetting iteration limits (`:118-122`), and forbids "another correction budget" (`:167-168`).
>   - doc-review has no report-only mode (`doc-review/SKILL.md:25-29`). Every run is an authorized Critical/High fix loop with its own cap of 5 (`:287-297`). So once a capped High finding is fixed through normal delivery, the only supported way to refresh starts a new loop.
>   - Both hosts' `residuals` results described a continuation that doesn't exist:
>     - Codex: "do not restart another five-iteration loop… obtain the owner's required fresh full audit".
>     - Claude: "without starting a new correction budget".
>   - Impact: no false "ready" (the result stays Incomplete), but the resume path after a cap can stall or invent an interface.
>   - Fix, one sentence: once remediation has changed doc-review's inputs, a new normal doc-review run is the refresh, with its own loop and cap. Only re-running on an unchanged capped baseline is forbidden.
> 
> ## Nits
> - **N-1.** `:92` gives a fixed gate order. Release-deploy uses `gates_for_release` order (`:5`, `:414`), and agile-workflow's opt-in `gate-refactor` is a configured gate, not a custom one (`:57`). Suggest "in `gates_for_release` order (default …)".
> - **N-2.** `:86-88` says "or an explicitly agreed document scope". doc-review only accepts no argument, a module name, or `--system-only`.
> - **N-3.** `:75` treats none and light alike. A `light` review may include one fresh-context pass (`review/SKILL.md:74`).
> - **N-4.** `gate-docs-extension.md:123` still says "via the Skill tool". The matching line in gate-tests-extension was made host-neutral.
> 
> ## Optional (existing before this change)
> - **O-1.** A real-version checkpoint needs items already bound to the release. Release-deploy binds them and then runs the same gates straight away, so the usual path either runs the gates twice or depends on binding by hand. Also, `:60-62` gives no place to save the checkpoint when no release file exists yet.
> 
> ## Considered and not raised
> - No committed text-matching tests: not a defect. The structural tests, real command runs and forward runs are proportionate.
> - `work-view --stage bogus` exits 0 with no output. That is upstream binary behavior. The skill now uses only valid single stage values and treats an empty version bundle as a failure. I'm keeping it as a limitation.
> - No case for a file-triggered pass, a shared quality engine, a fixed retry count or a stricter review weight.
> 
> ## Notes
> - **Scope:** 70348687..13711e20. Product contracts are at 4575547d; 4575547d..HEAD only changes the feature record. No agile-workflow or `ard-core` files changed, and no manifests or versions changed.
> - **Checks I ran, all passing:**
>   - `work-view` behavior reproduced: `--no-release` exits 1; a comma-separated `--stage` returns nothing with exit 0; the pending query returns 13 items.
>   - The documented citation-lint command runs under both `PLUGIN_ROOT` and `CLAUDE_PLUGIN_ROOT`: 35 resolved citations, 0 broken chains, 13 advisories.
>   - Brief lint: 17 resolved, 0 patterns. The brief's SHA-256 matches the recorded `4edfb99a…`.
>   - ARD conformance 57/57.
>   - RP portability, AR metadata and resolver tests pass.
>   - Knowledge index regenerated from a clean copy matches the committed files, apart from timestamps.
>   - `git diff --check` is clean, and the changed skills' frontmatter contains only `name` and `description`.
> - **Forward cases:** I read all 18 `result.md` files plus the tracked-case history.
>   - Outcomes are consistent across hosts, and the tracked fixture correction was legitimate.
>   - Limit: several fixtures state the coverage answer outright (stale_check, uncovered_change). They test precedence and review reuse more than detection.
>   - Fixture gate facts are inputs, not real gate runs.
>   - Not exercised: an empty real-version bundle, a lint error or missing JSON, an unsupported doc-review argument.
> - **Skipped:** security, runtime and infrastructure scans. The change is prose skills and generated YAML only; no code, secrets, infrastructure or hooks changed.
> 
> # Duty 2: QVE root round 2, whole-charter methodology assessment
> 
> **Outcome: Clean within reviewed scope at 4575547d/13711e20, provided the host's Duty 1 adjudication confirms there are no blockers.** There are no unresolved major findings, and the required research checks pass. If the host classifies I-1 or I-2 as a blocker, the outcome becomes **Awaiting change or evidence** until the fix is verified. This is not a claim of universal quality.
> 
> **Coverage:** the whole charter, meaning QVE-E, QVE-R and QVE-S plus how they interact, across the success, failed/missing, changed-output, exhausted-limit and resume paths.
> - **Contracts read directly this pass:** quality-checkpoint (new and baseline), doc-review, review, implement, release-deploy, the five agile-workflow gates' arguments, gate-citations, the AR orchestrator's verification-depth and completion sections, `verification-record.md`, ARD SPEC §3/§7, methodology-review and its references, conventions, build-process, composition, README and navigation.
> - **Evidence consumed:** the brief and story gate history (two NEEDS-REVISION results, then APPROVED and the lead spot-check), the component returns, parent assessment 1, the live handoff and the forward results.
> 
> | ID | State | Evidence |
> |---|---|---|
> | E/METH-001 (major) | **Verified resolved** | Outcome precedence `:141-155`; one stage per query `:130-134`; an empty bundle is not a sweep `:32`; doc-review residuals block `:146-147`; both hosts' residuals, tracked, stale_check and unavailable cases agree. Not downgraded. |
> | E/METH-002 | Verified resolved for every named defect | The new pending selection has one new minor defect, logged as I02. |
> | E/METH-003 | Verified resolved | AR `verification-record.md`, methodology record rules, build-process `:184-190`, research_receipt on both hosts. |
> | R/METH-001 | Verified resolved | CONVENTIONS `:26-36`; checkpoint §2; covered_fix and uncovered_change on both hosts; this feature itself used one standard pass. |
> | R/METH-002 | Verified resolved | build-process `:114-117` (nit N-3 remains). |
> | S/METH-001 | **Kept as a minor limitation** | Matcher untouched; reporting is now grouped. The real corpus has 13 advisories (10 `version-number`), mostly attestation metadata such as "arXiv version 2", with some genuine version facts. Zero noise is not required. |
> | S/METH-002 | Verified resolved | gate-citations `:102-105`, verification-record `:31`. |
> | QVE/METH-I01 | Verified resolved | CONVENTIONS `:35-36`, build-process Completion. |
> | **QVE/METH-I02 (new, minor)** | Open | Pending scope includes research engagements (Duty 1 I-1). |
> | **QVE/METH-I03 (new, minor)** | Open | Refresh after a cap is ambiguous (Duty 1 I-2). The result stays Incomplete, so it is safe; it is not major. |
> 
> There are no evidence-based withdrawals and no new major findings.
> 
> **Criteria:**
> - **Detection and independence:** improved. Worker exit, emitted-item counts and lint exit codes are no longer treated as a pass.
> - **Authority:** preserved. The checkpoint never deploys or publishes.
> - **Recovery:** the real-record handoff worked and the round counts were carried forward.
> - **Cost:** no added passes.
> - **False-positive burden:** better reported, but raw noise remains.
> - **Portability and ownership:** both hosts work. The AR change is a documented narrow fork patch, and the kernel is unchanged.
> 
> **Other minor observations kept on record:**
> - The unknown-stage behavior in `work-view` noted under Duty 1.
> - After the research's second NEEDS-REVISION, the driver surfaced it and ran one bounded check under prior authority, with no fresh operator response recorded. That fits AR's rule that it be surfaced, not looped silently, but the contract doesn't say who authorizes that follow-up check.
> - The forward fixtures' limited ability to tell outcomes apart, as noted under Duty 1.
> - The gate duplication in O-1.
> - The research is based on paper abstracts and supports no claim that cross-model review is better.
> 
> **Remaining obligations:**
> 1. The host adjudicates Duty 1, closes the feature review, and records this report with its date and baseline in the QVE record. Recording it completes root round 2, making it **2 of 5**.
> 2. If the host fixes I02 or I03 first, those edits come after this assessment and are not covered by it. Verify them under standard accepted-fix verification. Minor-only corrections don't need another methodology round, but the record should say so.
> 3. I made no new external claims, so nothing is provisional.
> 
> Coverage limits: I did not rerun the 17 QVE-S fixtures, re-read the archived review bodies (ca4f0daa, 7c17b1de) or the hooks, or observe a live release gate run.

### Host adjudication and next obligations

- I-1 / QVE/METH-I02: accepted. Driver independently reproduced the same gap before
  the reviewer returned. Treat as a small current-cycle adapter correction because
  correct pending scope is an acceptance contract. The read-only mode prevents a
  false-ready/binding consequence; methodological severity remains minor. Use
  release-deploy's target-project activation probe and parsed exact tag query for
  active and archived records. The earlier 13-candidate claim is superseded:
  corrected discovery is **11**, excluding story-research-quality-feedback and
  story-research-package-boundary. No binding/gates occurred.
- I-2 / QVE/METH-I03: accepted as a small current-cycle resume-contract correction.
  Directly read doc-review's arguments and Phase 4: no report-only mode, each normal
  invocation includes its five-iteration loop. After authorized delivery materially
  changes inputs, refresh through a new normal invocation with its own cap. Never
  rerun an unchanged capped baseline to gain attempts. Other owners' limits and
  standard delivery's no-rereview rule remain intact. The current behavior safely
  refuses readiness, so this remains a minor methodology finding.
- These two acceptance corrections must be verified before this feature closes;
  they are fixed inline, without new implementation stories or a second standard
  independent delivery pass. Stage returns to implementing for that verification.
- N-1..N-4: accepted small clarifications in the same touched contracts: preserve
  gates_for_release order; spell supported doc-review arguments; describe none/light
  by the actual review performed; make the docs-extension invocation host-neutral.
- O-1: valid pre-existing integration/cost concern below the current blocker bar.
  Parked via agile-workflow:park as idea-release-checkpoint-handoff (34d75ecd).
  No new release integration is designed or executed in this arc.
- No new major methodological finding. Existing major E/METH-001 is verified
  resolved, not downgraded. Retain S/METH-001 as minor raw heuristic noise.
- Reject the report's advice that minor-only changes never need another methodology
  round: methodology-review step 6 requires a fresh whole-charter assessment on
  the changed baseline. This is distinct from, and does not repeat, the completed
  standard delivery review. No further external research gap was identified.
- Keep the noted evidence limits: synthetic gate facts, limited discovery challenge
  in some cases, no live release, abstract-limited papers, no claim of cross-model
  superiority, surfaced AR second-revision follow-up history, unknown-stage binary
  behavior. None is represented as a passing execution that did not occur.

Round **2 complete of 5**, with current outcome **Awaiting change or evidence**
because the host is applying and verifying the accepted corrections. The reviewer's
conditional clean report does not cover later edits. Child coverage QVE-E/R/S and
finding IDs remain unchanged. No child/root allowance is reset. A fresh round 3
will be allocated only after the corrected baseline and evidence are committed.

### Correction verification in progress

The two raw pending-boundary cases passed on both hosts. Active AR: two delivery
candidates, excluding exact research tags in both tiers. Inactive AR: four candidates,
including ordinary research tags. research-ops remains eligible, bound/release
records remain excluded, and the probe is run in the fixture project rather than
this monorepo. Both reports retain preflight-only status and missing evidence.
Claude job 20261018T230616Z-454549fb and fresh native qve_pending_boundary completed;
driver read all four actual reports. Targeted candidate used only the pending fix.

Doc-review changed/unchanged capped-baseline cases and a rerun of residuals are
running on both hosts against the current correction. Earlier residual reports
are retained as pre-review-result.txt, not represented as post-fix coverage.
