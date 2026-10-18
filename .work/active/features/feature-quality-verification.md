---
id: feature-quality-verification
kind: feature
stage: drafting
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
