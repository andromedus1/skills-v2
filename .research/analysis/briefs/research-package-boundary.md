---
title: Research package boundary and methodology review
kind: research
provenance: agent-synthesis
updated: 2026-10-18
summary: Preserve the research engine and project-process boundary; test a coordinated suite experience before a full package merger, and make methodology-review research scale explicit.
key_findings:
  - "Proposed: preserve module boundaries while testing coordinated installation."
  - Current integration has a reproduced cache-selection weakness and undeclared manifest dependencies.
  - Claude documents dependency bundles; equivalent OpenAI installation behavior remains unverified.
  - "Proposed: clarify methodology-review research-scale selection and preserve its existing decision loop."
---

# Research package boundary and methodology review

## Recommendation

**Keep the engine and project-process modules distinct, and pursue a coherent
suite experience before committing to a full package merger. Start with direct
dependency integration; add an aggregate bundle only if it serves a broader suite.** This is a design
recommendation (`extends`), conditional on validating installation and routing in
the hosts actually used. It is not evidence that the current integration is good
enough, nor a veto on a future single distributable.

Separate three decisions: shared user-facing workflow, shared install/release
unit, and shared source ownership. They can be changed independently. A single
package could retain a clean internal engine boundary; a source merger does not
inherently require duplicating ARD. Conversely, a bundle can improve installation
while preserving independent modules and releases. These are architectural options,
not measured usability outcomes.

## What overlaps, and what needs what

The observed inventory has 24 Pipeline skills and four Agentic Research skills,
with no identical skill-directory names. Both manifest pairs omit a dependency
field; Pipeline's description expressly says it uses Agentic Research. A bounded
literal scan finds only a test-label mention of Pipeline inside Agentic Research.
The test guards a real fork customization: compared with the pinned upstream
revision in the observations, the Codex orchestrator policy enables implicit
invocation and a regression test enforces it. The sparse reverse-reference scan
therefore cannot establish that integration is maintenance-free. [package-observations]{1}

The following responsibility map is a **design lens**, read from the current
skill contracts, not a claim of demonstrated agent performance:

| Layer | Intended responsibility | Relationship |
| --- | --- | --- |
| Agentic Research | Research registration, decomposition, evidence records, synthesis and verification | General engine, intended to run standalone and also commission/hand off work directly |
| Research Pipeline | Prior-art intent, research-informed planning/design, knowledge navigation and project quality coordination | Its research entrypoints commission that engine; its broader project workflow also uses Agile Workflow |
| Methodology review | Compare approaches against intended outcomes, expose findings, retain operator decisions and reassess | Commissions research, then interprets findings within a continuing project review |

Lenses inspected: Pipeline's research/scout/brief/deep-research/research-program
skills and composition guide; Agentic Research's orchestrator and handoff;
methodology-review and its review-record reference. These prescriptions need
behavioral validation. The current project ownership rules are constraints the
operator may revise, not independent proof of the chosen architecture.

The overlap is chiefly **research intent and routing around one engine**, rather
than two complete engines. {inferred: convergence} The current Pipeline tree has
no files named `lint-citations.py` or `discipline.md` and no `ard-core` subtree;
the August removal commit provides historical corroboration, not a current
semantic-duplication metric. [package-observations]{1}

Thus the packages participate in one process, but “need each other” is too strong.
Pipeline's research capabilities need the engine; the engine's declared contract
does not need Pipeline. Merging these two would also leave the intended delivery
workflow's Agile Workflow dependency in place. Those dependency conclusions are
derived from declared contracts and bounded source inspection, pending host tests.

## Concrete friction and host evidence

The resolver checks explicit root, sibling directory, then caches. Its cache
fallback sorts paths lexically and takes the last match; it neither parses
compatibility ranges nor consults active-plugin state. In an isolated two-version
fixture, it selected **1.9.0 over 1.10.0**. This demonstrates fallback selection
behavior, not a demonstrated failure in a user's active installation.
[pipeline-resolver]{2} [package-observations]{1}

A second fixture confirms that the default Codex root can override a configured
Claude cache. The non-test reference scan found one caller, **gate-citations**;
research entrypoints instead prescribe namespaced skill invocation. The observed
path-selection defect is therefore narrower than the overall research interface.
A bundle alone does not repair it. [package-observations]{1} (`extends` for the
integration consequence; skill routing is a declared-contract lens.)

Claude supports direct same-marketplace dependencies as well as aggregate bundles.
A dependency in Pipeline may already provide automatic companion installation;
that should be tested before adding a bundle plugin. [claude-plugin-dependencies]{3}
The experiment is proposed, not validated host behavior.

OpenAI documents plugin names as identifiers/namespaces and a supported Codex
compatibility manifest. Both local plugins currently use that fallback without a
root manifest. [package-observations]{1} Its Claude-import guide removes `dependencies` on that
submission path. That limits portability of the Claude bundle declaration; it
does **not** prove all local Codex installs lack dependency support.
[openai-plugin-packaging]{4} [openai-claude-import]{5}

Changing to one plugin identity would therefore call for a namespace/reference
inventory and migration plan. Whether compatibility aliases are feasible remains
unverified. {inferred: consequence} [openai-plugin-packaging]{4}

## Comparable choices

The benefits and costs below are design judgments (`extends`); no user study,
token-cost benchmark or measured maintenance estimate was conducted.

| Criterion | Separate + direct dependency | Aggregate suite/bundle | One merged distributable |
| --- | --- | --- | --- |
| Dependency reality | Engine remains a companion; delivery also uses Agile Workflow | Aggregates selected companions, potentially including delivery | Makes engine internal; delivery dependency remains |
| User routing | Existing namespaces; clarify the preferred entrypoints | Same skills unless routing also changes | One namespace can simplify naming; intent choices remain |
| Host packaging | Claude mechanism documented; OpenAI path requires testing | Claude aggregate documented; OpenAI parity unverified | Internal paths possible; validate both host formats |
| Update ownership | Already redistributes and patches upstream; retain synchronization | Same existing synchronization plus bundle metadata | Same upstream obligation, with coupled release and import layout |
| Compatibility | Declare/test supported pairs; repair citation-gate resolver | Declare/test pairs; resolver repair still required | Pin engine internally; migrate namespaced references |
| Evidence integrity | One ARD authority, verified through integration | Same; bundling adds no research-quality guarantee | Keep one internal ARD authority; merging adds no quality guarantee |
| Simplification | No new package; improve setup/routing and remove redundant prompts | Useful for wider curated suites; adds an aggregate artifact | Can remove companion lookup; enlarges package and couples release |

**Existing distribution matters:** both catalogs already distribute Agentic Research
from this fork's local tree, including its Codex policy patch.
[package-observations]{1} Upstream synchronization is a shared cost under every
option, not a new tax unique to merging. Manifest repository fields identify
origin, not current distribution ownership. A merger changes how that cost is
managed; it does not create it. {inferred: consequence}

**Routing simplification is separate from packaging** (`extends`). As declared
contracts, Pipeline's five research intents all reach one orchestrator; the
orchestrator is also directly invocable. Agile Workflow retains a research skill
and an ideate skill, and Pipeline's README already calls its ideate the preferred
entrypoint for this workflow. A two-package merger leaves that third-plugin
overlap intact. Prefer one documented front door for ordinary project work,
retain direct engine access for standalone research, and test whether the five
intent aliases clarify decisions or merely add choices. Do not delete them solely
because their execution engine is shared. These are candidates for simplification,
not measured routing failures. Agentic Research's own work commissioning/handoff
also means Pipeline is not the exclusive bridge from research to delivery.

## Contradictions

No direct same-frame factual contradiction was established. Relevant design tensions:

| Relationship | Positions retained side by side | Consequence |
| --- | --- | --- |
| tension | Claude documents dependency bundles [claude-plugin-dependencies]{3}; OpenAI import removes the declaration [openai-claude-import]{5} | Avoid promising a portable one-click bundle before host validation |
| qualifies | Pipeline's manifest declares engine use [package-observations]{1}; its resolver checks file existence and lexical paths [pipeline-resolver]{2} | Declared composition does not establish compatible active-version selection |

## Disconfirming analysis

For the recommendation to preserve modules, a material counterargument is the
observed resolver weakness plus lack of manifest dependency declarations. A merged
artifact could remove that particular installed-path lookup, and a single release
could pin a tested engine. The lookup advantage concerns the citation gate;
namespaced routing and upstream synchronization need attention under every option.
These are real advantages, not dismissed as conceptual
confusion. [package-observations]{1} [pipeline-resolver]{2} (`extends` for proposed effects.)

For the claim that dependency requires merger, the contrary evidence is Claude's
documented direct dependencies and bundles. [claude-plugin-dependencies]{3} For the claim that
current separation is already sufficient, the contrary evidence is the probe and
unverified cross-host setup. No observed adoption or routing trial establishes
that either packaging option performs better.

Reconsider a full distributable merger if common scenarios consistently require
both modules, coordinated setup still fails on supported hosts, and the operator
accepts coupled releases with a repeatable upstream update mechanism. Preserve a
single authoritative ARD implementation under either choice. These are proposed
decision conditions, not findings that those conditions already hold.

## Methodology-review: placement and proposed next iteration

The provisional responsibility boundary is: methodology-review compares methods
against intended outcomes and manages adjudication/reassessment; Agentic Research
answers and verifies evidence questions. This is a design judgment, not proof of
a necessary package location.

**Countercase:** the skill already has a tracker fallback when `.work/` is absent
and does not bootstrap an index elsewhere. It is more portable than a
project-delivery-only controller. A standalone methodology plugin could serve
non-delivery audiences; placing it alongside Agentic Research could make sense
if that becomes the primary audience. Agile Workflow would suit a delivery-only
review, but is narrower than its present charter. Keeping it in Pipeline for now
reuses Scout, program coordination and project-context navigation with no new
package; move it if independent adoption or repeated coupling friction establishes
a better boundary. These are alternatives evaluated through current skill-contract
lenses, not user-adoption measurements.

The [composition guide](../../../plugins/research-pipeline/docs/research-composition.md)
already declares bounded research, decomposed campaigns and programs. The
[methodology-review skill](../../../plugins/research-pipeline/skills/methodology-review/SKILL.md)
already delegates to the engine. Credit those contracts rather than presenting
all of them as new capabilities:

| Status | What to retain or change |
| --- | --- |
| Existing: reaffirm | Scout only for missing landscape coverage; reuse prior research rather than restarting each round |
| Existing: reaffirm | Compare common scenarios and simpler baselines; separate research verification from project reassessment and operator decisions |
| Existing: reaffirm | Keep the methodology controller open when an individual research engagement completes; preserve decisions outside research artifacts |
| New clarification proposed | State a decision rule: one bounded issue → inquiry; several facets of one decision → campaign; separately commissioned decisions → program, including registered cross-engagement synthesis |
| New clarification proposed | Make research scale and verification rigor explicitly independent; leave decomposition and gates owned by Agentic Research |
| New clarification proposed | Explain how bounded findings, facet syntheses and cross-engagement conclusions each feed the same finding/adjudication loop, with targeted follow-up when uncertainty remains |

This proposes clearer commissioning and result consumption, not another research
engine. Behavioral examples should establish whether the clarification improves
methodology reviews before adding more mandatory procedure. (`extends`.)

## Limits and next decision

Evidence supports a conditional architectural direction and two reproduced resolver
behaviors. It does not establish host-version compatibility, adoption preferences,
runtime routing quality, token savings, or upstream maintainers' future plans.
No required source remained inaccessible: failed Markdown transports were resolved
by reading normal HTML. The outstanding evidence is behavioral testing, not a
missing publication.

The next proposed step is a direct-dependency/setup experiment before deciding on
an aggregate bundle, plus a methodology-review design pass around explicit scale
selection. Compare standalone research, research-backed feature design, multiple
cached engine versions and host-root precedence. Exercise the citation gate in
Codex too: it currently spells its resolver path through `CLAUDE_PLUGIN_ROOT`,
whose availability there is unverified. These are packaging trials; assess
methodology-review separately with a bounded question, a multi-facet decision and
a resumed review whose research engagement has already completed.

Implementation, release and corpus migration remain separate decisions.

## Revisions

2026-10-18 — Correction after independent challenge: added existing fork
distribution/patch costs, narrowed resolver impact and covered cross-host precedence;
distinguished direct dependency from aggregate bundles; compared identical criteria;
separated existing methodology contracts from proposed clarifications and challenged
its package placement. The recommendation still preserves the engine boundary;
the first setup experiment is now explicitly direct dependency integration.
