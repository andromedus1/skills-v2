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
