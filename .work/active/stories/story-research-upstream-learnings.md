---
id: story-research-upstream-learnings
kind: story
stage: done
tags: [research]
parent: feature-upstream-learnings-2026-10
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
research_refs: [upstream-learnings-2026-10-landscape]
research_dials:
  scope_authority: mixed
  verification_rigor: floor
  intent: map-landscape
  output_kind: landscape-brief
---

# Scout: what changed upstream since 2026-08-01 and what could transfer

## Commission

Breadth survey (research-pipeline `scout` intent) of `nklisch/skills`
`upstream/main` (`638867b6`) against this fork since merge base `43f7f4bf`, plus
`nklisch/peeragent` 0.8.1 → 0.8.3 (latest release 2026-10-11). Sources are
first-party: `git log`/`git diff 43f7f4bf..upstream/main -- plugins/<name>` in
this repo, upstream `.work/` items and docs at `upstream/main`, and the public
peeragent repository/releases.

For each area, describe the upstream change in its own terms (what, why — from
commit messages, items and docs — and evidence of use), then map it to this fork:
already have / conflicts with fork policy / could adopt / could adapt / not
relevant, with the files a change would touch and who owns them (upstream-owned
plugin vs fork-owned `research-pipeline`/`agentic-research`). Areas:
agile-workflow (10 commits), code-audit (5), ux-ui-design (3; large removal),
prose-craft (9), new plugins sol-calibration and declaudify, single-commit
touches (agentic-research, agent-coordination, nates-toolkit, workflow), peeragent,
and **Workbench as an ideas pass only** (159 commits): map themes and process
ideas that could transfer to agile-workflow/research-pipeline, never as a
migration target, no per-commit analysis. Seek evidence against adopting as well
as for.

Consumer: Andrew via `feature-upstream-learnings-2026-10` decision packet.
Decision relevance: which upstream changes to adopt, adapt or skip. Dials set
with Andrew 2026-10-19: mixed scope, **floor** rigor. Per ARD SPEC §3.1/§7, if
the engagement fans out to several specialists, the isolated `evaluate` gate
re-enters the floor for the cross-specialist synthesis.

## Full registration

```yaml
intent: map-landscape
output_kind: landscape-brief
consumer: methodology-revisers
verification_rigor: floor
temporal_contract: write-once-on-converge
```

## Engagement record

### Kickoff (delegated; dials confirmed by Andrew at scope time)

- Read dials: `scope_authority: mixed`, `verification_rigor: floor`,
  `intent: map-landscape`, `output_kind: landscape-brief`. Scout framing:
  prior-art landscape, neutral, no winner selected.
- `decision_relevance` (from the commission): which upstream changes
  (per area, plus Workbench ideas and peeragent 0.8.1 → 0.8.3) to adopt,
  adapt or skip in `feature-upstream-learnings-2026-10`'s decision packet.
- Remaining registration: `consumer: methodology-revisers`;
  `temporal_contract: write-once-on-converge`; `primitives_extends: []`;
  `primitives_opts_out: []`; `analytical_artifact_type: per-campaign-brief`.
- Substrate-check: no prior `.research/` artifact covers this upstream range or
  peeragent. `research-package-boundary` and `qvc-review-evidence` were used
  only as lenses (not cited).

### Decomposition (Checkpoint A, surface-and-proceed)

Declared portion (scoping): the eight commissioned areas. Emergent
candidates:

1. **One inline facet** covering every area against one fork-mapping frame.
   Sources are first-party Git objects and two release pages, read in one
   context with full fork state. This serializes the reading.
2. **Two specialists**: non-Workbench plugin changes plus peeragent, and a
   Workbench ideas pass, with a lead cross-join. This parallelizes the large
   Workbench diff, but each specialist would need the fork-policy mapping
   context, and the cross-join would bring in `evaluate`.
3. **Four specialists** (delivery plugins, content plugins, Workbench,
   peeragent). Finer, but it splits one mapping table across four authors for
   a breadth brief.

Chosen: candidate 1 (light path, inline). The output is a single mapping
table whose value depends on consistent fork-policy judgement, and Workbench
is commissioned as an ideas pass, not a per-commit analysis. Self-flag: the
reading was serialized, so Workbench was read at theme level (the guide, nine
references, upstream conventions and commit subjects). The brief lists what
was not read.

### Acquisition and synthesis

- 22 new attestations (corpus numbers 38–59) appended to
  `.research/references.md`; bibliography at
  `.research/reference/upstream-learnings-2026-10/BIBLIOGRAPHY.md`.
  Upstream content was read from local Git objects at 638867b6 and the named
  commits, and each attestation carries the public URL of the same revision.
  peeragent was read through the public GitHub API (releases v0.8.1–v0.8.3,
  compare v0.8.1...v0.8.3, compare v0.8.3...main). No private content was
  sent.
- A generated machine observation record
  (`.research/reference/upstream-learnings-2026-10/repository-observations.json`,
  `provenance: generated-listing`) holds the commit lists, versions,
  add/remove events, fork greps and local peeragent cache versions.
- Output: `.research/analysis/briefs/upstream-learnings-2026-10-landscape.md`.
- Acquisition gaps (light path, carried here; no blocking candidates):
  enriching only. These are the `nklisch/theatre` (theatre-feedback) content;
  the Workbench SPEC, VISION and scripts; the ux-ui-design 1.0.0 reference
  library; and the operator's use of ux-ui-design, prose-craft or Antigravity
  in other projects. Queue promotion is not written; it is the operator's call
  via `/agentic-research:research-handoff`.

### Verification (floor)

Effective gates for this shape are `lint` and lead `spot-check`.
`adversarial-read` is not selected at floor. `evaluate` is reachability-pruned:
no specialists were dispatched, so no cross-specialist synthesis exists for it
to fence (ARD SPEC §3.1/§7). **The evaluate gate did not apply.**

- **Lint (hard floor)** on the final brief, with URL liveness:
  90 resolved citations, 0 broken, 0 thin, 0 high (`--exit-code-on high`
  exit 0), no attestation-tier audit findings, no `substrate_confidence`
  omissions. 22 advisories:
  - 19 `version-number`: plugin and release versions, each attested in
    the observation record or area attestations;
  - 1 `count-without-unit-citation` (L21, cited on the next line);
  - 2 `comparative-superlative`: L132 quotes declaudify's "only shared
    context", and L246 uses "only together" as a restriction, not a
    superlative.

  None is an unsupported composed claim. Zero broken or thin chains does not by
  itself establish semantic support.
- **Lead spot-check** covered all lint pattern categories and the load-bearing
  claims:
  - 44 quoted strings in the brief checked against their cited attestations.
    Seven did not match at first. Corrections: a case fix (`Maintenance
    mode`); citations added in mapping rows for the sol-calibration,
    root-principles and peeragent-description quotes; two paraphrases taken
    out of quotation marks.
  - 221 quoted strings in the attestations checked against the Git sources.
    The ten non-matches were diff `+` markers, elisions or commit subjects
    outside the checked set, all confirmed by hand. One punctuation fix was
    made (sol-calibration).
  - Semantic corrections in place:
    - the "replaces per-feature passes" quote was re-pointed from
      review-boundaries {51} to the guide {46}, where it occurs;
    - the root-principles absence claim was narrowed to a phrase check;
    - the sol-calibration "three follow-up items in two days" wording was
      corrected to three follow-up commits from 2026-08-23 to 08-29;
    - "Workbench setup created PRINCIPLES.md" was narrowed to the commit
      title;
    - an unsupported "recent rules" claim was removed.
- Outcome: floor gates passed; stage set to `done` (`research_completion`
  is unset in `.work/CONVENTIONS.md`, so the default is `close-to-done`).
  Known limitation for consumers: floor rigor means no independent
  semantic-support read. The fork-mapping section is composed (`extends`)
  from project rules read as lenses.

### Next step

Run `/agentic-research:research-handoff upstream-learnings-2026-10-landscape`
only if Andrew wants work items emitted. The decision packet in
`feature-upstream-learnings-2026-10` consumes the brief directly.
