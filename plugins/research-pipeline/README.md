# research-pipeline

Research-grounded process overlay for projects using the `agile-workflow`
substrate and the `agentic-research` engine. Adds research-first planning,
architecture rigor, knowledge-index integration, and cascading doc review.

This plugin is **additive**: it does not replace the delivery substrate or the
research engine. It layers project-process skills over both so work reaches the
`.work/` queue with grounded decisions.

`agentic-research` is a required companion and the single authoritative ARD
implementation. The familiar `/scout`, `/research`, `/brief`,
`/deep-research`, and `/research-program` entrypoints are intent profiles that
commission its orchestrator. See [research composition](docs/research-composition.md).

## What's in here

| Layer | Skills |
|---|---|
| **Research intents** | `/research` (bounded question), `/deep-research` (multi-facet decision), `/research-program` (coordinated research arcs) |
| **Prior art and methods** | `/scout` (landscape), `/methodology-review` (decision-mapped focused, coordinated or program reviews with adaptive research and whole-scope reassessment) |
| **Foundation docs** | `/ideate` (super-layer: produces VISION/SPEC/ARCHITECTURE + research-plan + PRINCIPLES), `/architecture` |
| **Substrate planning** | `/epicize`, `/epic-design`, `/feature-design`, `/update-epicize`, `/brief` |
| **Quality** | `/doc-review` (cascading), `/quality-checkpoint` (configured checks and readiness evidence), `/gate-citations` (research-corpus citation integrity), `/test-quality`, `/security-review` |
| **Lifecycle** | `/init-project`, `/expand`, `/update-documentation`, `/knowledge-index` |
| **Knowledge viz** | `/knowledge-graph` (interactive corpus graph + index-integrity linter; sibling to `agile-workflow:board`) |
| **Auto-loaded** | `/engineering-principles` (code-design), `/build-process` (methodology) |

## Skill catalog

See the [top-level README](../../README.md) for the full catalog.

## Compatibility with agile-workflow

This plugin operates on Nathan Klisch's `agile-workflow` substrate. Same `.work/` format, same frontmatter schema, same `work-view` query tool. On shared projects, our skills check tags (`[needs-brief]`, `[needs-research]`) to decide when to run; his skills ignore them.

**Methodology review** maps decisions to a focused, coordinated or program
shape, adapting research within each component. Durable child-to-parent records
preserve results, shared assessment rounds and resume state; a fresh whole-scope
assessment determines the explicit parent exit. See the
[methodology-review skill](skills/methodology-review/SKILL.md) and its linked
record and decomposition references.

**Where we extend his skills**: our `quality-checkpoint` orchestrator invokes
configured gates and reconciles actual outcomes, delivery-review evidence and
doc-review residual findings. `--pending` is preflight only: it reports candidate
scope and owner eligibility without dispatching release gates or claiming
readiness. Each owner keeps its own verification and correction policy. A
completed standard delivery review plus verified accepted fixes remains covering
evidence; uncovered material contracts follow normal delivery review. No
infrastructure gate is assumed. The release-time citation gate is an adapter over
Agentic Research's authoritative validator. Grouped advisory reporting improves
signal without changing the lint kernel or semantic-verification rules; see the
[citation gate](skills/gate-citations/SKILL.md) and [verification record](../agentic-research/skills/research-orchestrator/references/verification-record.md).

**Where we don't duplicate**: `implement`, `implement-orchestrator`, `cruft-cleaner`, `bold-refactor`, `repo-eval`, `e2e-test-design`, `extract-patterns`, `refactor-design`, `feature`, `release` — defer to his.

## Naming collisions

Two skills exist in both plugins:
- `/ideate` — ours is the canonical entry for our workflow (produces all Nathan's foundation docs + research-plan + auto-`/scout`). His `/agile-workflow:ideate` remains available but is redundant for our users.
- `/research` — ours is the process-aware entrypoint into Agentic Research; his
  is a single-shot reference helper. Use ours for project-grounded investigation.

Disambiguate via namespace when needed: `/research-pipeline:ideate` vs `/agile-workflow:ideate`.
