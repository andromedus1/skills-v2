---
name: quality-checkpoint
description: >
  Check release readiness using configured delivery gates, document review and
  research citation lint. Reconcile actual results, unresolved findings and
  delivery-review evidence before recommending release. Use at a release boundary;
  --pending prepares an unbound scope without claiming release readiness.
---

# Quality Checkpoint

Coordinate the checks defined by the project's process. Read the plugin's
[build process](../../docs/build-process.md), project instructions and
`.work/CONVENTIONS.md`. Agile Workflow owns delivery, gates and releases;
Agentic Research owns research verification. This skill combines their evidence,
not their pass criteria or retry loops.

## 1. Establish scope and required checks

Accept a release version or `--pending`. Reuse an explicit scope from the request;
ask only when it is absent or ambiguous. Record the target items, changed files,
revision and relevant uncommitted content so later results have a known baseline.

For a version, run:

```sh
.work/bin/work-view --release <version> --paths
```

Exclude the release orchestration item from the delivery bundle. Recover archived
bodies from their `git_ref` and original active path when needed for changes,
acceptance or review evidence. An empty delivery bundle is not a successful sweep.

For `--pending`, discover terminal items across all tiers:

```sh
.work/bin/work-view --scope all --stage done --paths
```

Read their frontmatter and select unbound non-release items. `work-view` has no
`--no-release` flag; do not invent one. **Pending mode is preflight only:** report
scope, existing evidence and missing prerequisites. Do not dispatch release-only
gates with a virtual version, bind items or claim readiness. A real binding or an
explicitly configured adapter accepting the exact item set is required for a
subsequent gate run; do not invent that adapter's contract.

For a real release, resolve the required checks before dispatch:

- `gates_for_release`, when present, selects the project's delivery gates.
  Otherwise use the standard gate names: security, tests, cruft, docs,
  patterns. A missing required skill is a prerequisite failure, not an implicit skip.
- Add `research-pipeline:doc-review` for the planning corpus and
  `research-pipeline:gate-citations` for `.research/`, unless the project or caller
  explicitly excludes them. An absent activating corpus is a documented no-op.
- Reuse explicit exclusions and their reasons. Do not ask again or skip a required
  check to save time. Resolve any newly necessary exclusion with the operator.
- Resolve custom gates through the project's declared namespace and input
  contract. There is no bundled `gate-infra`; do not assume one exists.

Persist the scope and required/excluded checks in the existing release or work
record before dispatch. If pending mode has no record, report its preflight in
conversation; do not create a new tracker just for this summary.

## 2. Reconcile delivery-review evidence

Read the bundle's item records, including recovered archived bodies. Follow
`agile-workflow:review` and its effective weight; path names do not determine the
lane. Consequential changes to executable instructions or foundational contracts
use the feature boundary when independence is warranted. Child checkpoints and
narrow standalone fixes retain their existing verification/inline-review routes.

For covering review evidence, retain the assessed scope/baseline, reviewer path,
weight, findings, adjudication and accepted-fix verification. A terminal stage,
passing linter, design advisory or research verification is not a delivery-review
receipt. Honor explicit none/light policies without relabeling them independent.

A completed standard review plus verified accepted fixes remains valid; a changed
hash alone does not require another pass. Do not describe the original reviewer
as approving later corrections. If a later change introduces a materially uncovered
contract, name that gap and route it through normal delivery/review. Missing
required review blocks readiness. Resume from existing receipts and pending fixes;
never restart a completed standard pass merely because context was lost.

## 3. Execute the declared checks sequentially

Run doc-review first when required, using its supported no-argument full review
or an explicitly agreed document scope. A release version is not its module
argument. Invocation includes its own authorized Critical/High correction loop;
retain its actual `doc-review-report.md` and final severity counts, including a
capped or incomplete outcome. Capture the resulting baseline before other scans.

Then run the configured delivery gates in order: security, tests, cruft, docs,
patterns; place custom gates according to their declared dependencies. Run
citations last when required. Pass the real release version to release-bound gates.

For tests and docs, read and append the relevant policy to the invocation:

- [gate-tests-extension.md](../../docs/gate-tests-extension.md)
- [gate-docs-extension.md](../../docs/gate-docs-extension.md)

Use public skill namespaces and the host's normal skill invocation mechanism.
Wait for each result. Continue independent checks after an error where their
prerequisites still hold, recording any checks that could not run. Missing tools,
failed processes, missing reports or incomplete coverage cannot count as passes.
The checkpoint does not implement emitted findings; normal delivery owns them.

In the existing record, capture for each required check:

| Check | Assessed scope/baseline | Actual result and evidence | Remaining obligations |
|---|---|---|---|
| Skill/command and applicable pass criterion | Revision/digests and files | Report path, verdict, counts, execution error or not run | Finding IDs, accepted fixes, unavailable coverage or next owner |

Distinguish successful execution from an approving result. For citation lint,
inspect JSON: default exit zero is not proof of no broken chains. Separate broken
chains, thin attestations and advisory pattern counts; apply the citation gate's
severity policy. Advisory counts never prove semantic support or cause a new gate.

If a later action changes an earlier check's inputs, determine affected coverage
and refresh that evidence under its owner's rules. Reuse unaffected evidence with
an explicit scope comparison. Do not mark a stale report current or reset an owner's
iteration limit. Doc-review's full re-audit rule and standard delivery's accepted-fix
verification rule remain distinct.

## 4. Decide from results and unresolved work

Reconcile all release-relevant outstanding work, including previously tracked
findings that emitted no new item on this run. Query each stage separately;
`--stage` accepts one value, not a comma-separated list:

```sh
.work/bin/work-view --release <version> --stage drafting --paths
.work/bin/work-view --release <version> --stage implementing --paths
.work/bin/work-view --release <version> --stage review --paths
```

Exclude the release controller itself. Follow the gate's severity/disposition
policy for blocking versus advisory findings; surface any unresolved required
bundle work, review or dependency. A finding deduplicated against an old item is
still a finding until its required remedy is verified.

Use this precedence:

1. **Preflight only** — `--pending`; no release-readiness verdict.
2. **Incomplete checks** — any required check or review evidence is missing,
   errored, stale or lacks required coverage. List affected checks and next owners.
3. **Changes required** — checks returned blocking findings or required work remains,
   including doc-review Critical/High residuals even if no work item was emitted.
4. **Ready within checked scope** — every required check has a current successful
   result under its owner's criteria; required delivery review and corrections
   are evidenced; no blocking findings or required work remain. List nonblocking
   observations and coverage limits. This recommendation does not deploy or publish.

When several conditions apply, list every outstanding obligation even though the
primary label follows this precedence. Zero newly emitted items, zero advisories,
or process completion alone can never establish readiness.

## 5. Report and hand off

Report scope/baseline, required checks and exclusions, each result/evidence link,
new and previously tracked blocking findings, doc-review residual counts, review
coverage and the next action. Preserve this checkpoint in the existing record for
resume; reports and finding items remain at their owning skills' locations.

Route findings to normal Agile Workflow implementation/review, and unavailable
checks to their owners. After changes, resume the same checkpoint and refresh
invalidated checks. Deduplication prevents duplicate items; it does not mean a
rerun is free or that existing unresolved findings disappeared. Do not silently
repeat unchanged checks, create another correction budget, or launch a second
standard delivery review. Release execution remains an explicitly authorized
`agile-workflow:release-deploy` action.
