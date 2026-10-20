# skills-v2 .work/ conventions

skills-v2 is the plugins monorepo (it *develops* agile-workflow + research-pipeline
+ the others). It now **dogfoods its own substrate**: skills-repo work — new skills,
plugin features, doc/prompt-ware changes, follow-ups — is tracked as items in `.work/`,
not in docs (build-process rule #6: items track work, the roadmap-as-document pattern
is retired).

## Foundation docs (gate-docs checks these for rolling-foundation discipline)

foundation_docs:
  - README.md
  - .claude/CLAUDE.md
  - plugins/research-pipeline/docs/build-process.md

## Release mapping

release_mapping: none

skills-v2 has **no repo-level release**. Each plugin is versioned independently by its
own semver in `plugins/<name>/.claude-plugin/plugin.json` (+ the matching
`.codex-plugin/plugin.json`), bumped via `./scripts/bump-version.sh <plugin> <major|minor|patch>`,
which commits and pushes the bump on its own. The marketplace is a local directory
(`andrewclark88-skills-v2` → this working tree), so consumers pull a plugin's new
version with `claude plugin update <plugin>@andrewclark88-skills-v2 --scope project`.
There is **no CI** — PRs merge manually after the applicable Agile Workflow review
and verification. Consequential skill or foundation changes that alter authority,
required checks, grounding, completion or cross-skill contracts use the feature
review boundary when independence is warranted. Narrow standalone fixes keep
their bounded inline lane; child stories close on verification.

Use `agile-workflow:review` and its effective weight; the receipt below records
covering evidence. Missing, failed or stale required evidence is not a pass,
including on this repository's normal path without a formal release checkpoint
([build-process §Completion](../plugins/research-pipeline/docs/build-process.md#completion)).

### Review receipts

Feature and epic review records carry a receipt directly after the
`## Review (YYYY-MM-DD)` block that `agile-workflow:review` writes:

```markdown
**Receipt**
- Reviewed: `<base>..<head>` — product scope, with any excluded paths
- Reviewer: <model/class> via <peeragent job id | fresh-context sub-agent>; independent: yes|no
- Findings: blockers N, important N, nits N, rejected N
- Accepted-fix verification: <commit(s)> verified by <who/how> | none required
```

`<head>` is a commit; a review of uncommitted work records its base commit plus
"working tree". At closure, enumerate later commits that touch a consequential path.
The receipt's listed fix commits and commits whose message names another tracked
item (which carries its own evidence) need no line. List only the exceptions:

```markdown
**Post-review changes**
- `<sha>` <subject> (<files>) — covered-by-pass | uncovered → <item id>
```

Commit messages name their item (`implement: <id>`, `fix: … (<id>)`, `review: <id>`).
`covered-by-pass` means the change was in the reviewed working tree. With no
exceptions, write `**Post-review changes**: none outside listed fixes and tracked items`.

Consequential paths are plugin skills, docs, ARD core, hooks and manifests plus the
root instruction and convention files. Enumerate them with exactly:

```bash
git log --format='%h %s' <head>..HEAD -- 'plugins/*/skills/*' \
  'plugins/*/docs/*' 'plugins/*/ard-core/*' 'plugins/*/hooks/*' \
  'plugins/*/.claude-plugin/*' 'plugins/*/.codex-plugin/*' \
  AGENTS.md .claude/CLAUDE.md .work/CONVENTIONS.md README.md
```

An exception without a line makes the evidence stale; `uncovered` routes
through normal delivery and review, and readiness then also needs that item's
evidence. A changed hash alone does not require another pass. Standalone-story
inline reviews keep the existing record. Reviews recorded before this convention
may be reconstructed from git and labeled `reconstructed`, using the head the
reviewer's own report states it assessed and classifying every later commit as
above; a reconstruction counts only when the record shows the review its effective
weight required. If the assessed head cannot be recovered, the evidence is missing.

## Overbuilding calibration

skills-v2 ships prompt-ware plugins for one maintainer's projects on two hosts
(Claude, Codex), with no CI and manual PR merges. Cost is felt as instruction
volume an agent must load, review time, and drift between restated rules — not CPU.

Likely overbuilding here: restating one rule in several skills or docs; receipts,
ledgers or status fields that mainly police agent bookkeeping; extra review or
research passes where one independent pass and an executable check would do; gate
prose without a consumer; research ceremony for reversible, low-consequence choices.

Justified complexity: conformance and parity tests at stable interfaces (ARD kernel,
manifests, hooks); citation integrity checks; Andrew's authority over method,
publication and migration; cross-host behavior.

Revisit when a check catches nothing across several arcs, when a rule needs a third
restatement, or when Andrew reports friction.

Delegated agents edit only what their assignment covers. They never delete,
revert or wholesale-replace files outside it, or discard others' uncommitted
changes; they report such conflicts instead.

## Model lineup

Andrew's standing lineup (2026-10-19); concrete IDs resolve through peeragent's
alias table. Claude host: the host model (Opus) designs, integrates and
adjudicates, and host-class sub-agents implement and research; independent
feature review is Codex `sol` medium; whole-scope methodology assessment is Codex
`sol` high; quick scenario or smoke checks are Codex `luna` high. Codex host:
independent review is Claude `opus` xhigh (`fable` high for the hardest reviews).
If the other model is unavailable, use a fresh-context sub-agent of the host model
and label it same-class. Qualified observations live in `.work/MODEL-NOTES.md`.

## Gates for release-deploy

gates_for_release:
  - tests
  - cruft
  - docs
  - patterns

skills-v2 work is skill/prompt + Python-tooling authoring; the relevant gates are
tests (e.g. `plugins/research-pipeline/scripts/tests/`, conformance, knowledge-graph
render tests), cruft, docs (rolling-foundation across plugin docs), and patterns.
`security`/`infra` are omitted — skills-v2 ships no deployed infra or secrets surface.
skills-v2 rarely cuts a formal `release-deploy`; per-plugin `bump-version.sh` is the
normal ship path.

## Tag conventions

- `[refactor]` routes feature items to `/agile-workflow:refactor-design`
- `[perf]` routes feature items to `/agile-workflow:perf-design`
- `[needs-brief]` routes epic/feature items through `/research-pipeline:brief` before design
- `[needs-research]` routes through one of `/research`, `/deep-research`, or `/research-program` before brief

## Design-skill routing

design_skill_routing:
  epic_design: research-pipeline:epic-design
  feature_design: research-pipeline:feature-design

skills-v2 develops the research-pipeline plugin and uses its research-grounded,
`[needs-brief]`/`[needs-research]`-gated design skills for its own non-trivial work.
