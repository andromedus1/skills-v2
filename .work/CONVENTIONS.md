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
- Weight: <none|light|standard|thorough|maximum> (source: caller|convention|default)
- Findings: blockers N, important N, nits N, rejected N
- Accepted-fix verification: <commit(s)> verified by <who/how> | none required
```

`<head>` is a commit; a review of uncommitted work records its base commit plus
"working tree" and classifies the resulting commits at closure. At closure, list
every later commit that touches a consequential path:

```markdown
**Post-review changes** (`<head>..<closure>`)
- `<sha>` <subject> (<files>) — covered-by-pass | fix-of:<finding> verified <how> | other:<item id> | uncovered → <item id>
```

`covered-by-pass` means the change was in the reviewed working tree; `other` marks
another tracked item's work, which that item's own evidence covers.

Consequential paths are plugin skills, docs, ARD core, hooks and manifests plus the
root instruction and convention files. Enumerate them with exactly:

```bash
git log --format='%h %s' <head>..<closure> -- 'plugins/*/skills/*' \
  'plugins/*/docs/*' 'plugins/*/ard-core/*' 'plugins/*/hooks/*' \
  'plugins/*/.claude-plugin/*' 'plugins/*/.codex-plugin/*' \
  AGENTS.md .claude/CLAUDE.md .work/CONVENTIONS.md README.md
```

An enumerated commit without a line makes the evidence stale; `uncovered` routes
through normal delivery and review, and readiness then also needs that item's
evidence. A changed hash alone does not require another pass. Standalone-story
inline reviews keep the existing record. Reviews recorded before this convention
may be reconstructed from git and labeled `reconstructed`, using the head the
reviewer's own report states it assessed and classifying every later commit as
above; a reconstruction counts only when the record shows the review its effective
weight required. If the assessed head cannot be recovered, the evidence is missing.

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
