---
title: Upstream learnings landscape — nklisch/skills since 2026-08-01 and peeragent 0.8.1 to 0.8.3
kind: research
provenance: agent-synthesis
updated: 2026-10-19
summary: Breadth map of 224 upstream nklisch/skills commits (43f7f4bf..638867b6) and peeragent 0.8.2/0.8.3, each mapped to this fork as already-have, conflicts, adopt, adapt or not-relevant, plus a Workbench ideas pass with evidence for and against transfer.
key_findings:
  - "Upstream agile-workflow changes are compatibility work plus one behavioural addition: a fresh-context, cross-model skeptic in bold-refactor (shared with code-audit)."
  - "ux-ui-design 1.0.0 removes the seven pipeline skills; adopting it also requires edits to fork-owned research-pipeline epic-design and feature-design, which still invoke the removed names."
  - "prose-craft, sol-calibration and declaudify are additive and have no fork consumers; sol-calibration overlaps agile-workflow principles and gate-cruft."
  - "Antigravity manifests are the whole change for agentic-research, agent-coordination, nates-toolkit and workflow; adopting them adds a third parity channel."
  - "peeragent 0.8.2/0.8.3 change only Windows npm-shim launching; macOS behaviour and the peer skill text are unchanged."
  - "Workbench's transferable ideas centre on costed machinery (overbuilding calibration, machinery forecast), design-review priorities and local model notes; its rapid churn and add-then-remove history argue for adopting ideas, not text."
---

# Upstream learnings landscape — nklisch/skills since 2026-08-01 and peeragent 0.8.1 → 0.8.3

## Scope and reading depth

The survey covers `nklisch/skills` from merge base 43f7f4bf to `upstream/main`
638867b6 (2026-10-02): 224 commits, 226 files, +13842/−12470
[upstream-learnings-observations]{38}. Per area it records what changed
upstream, the reason given in commit messages, items and docs, and the
evidence of use in the upstream record. It then maps each change to this
fork. Workbench (159 commits) is read for ideas only. The survey also covers
`nklisch/peeragent` releases v0.8.2 and v0.8.3.

Upstream content was read from local Git objects at the named revisions.
Each attestation names the public URL for the same revision. Verification
rigor is `floor`: citation lint plus a lead spot-check. No independent
semantic pass was run.

## Landscape by area

| Area | Upstream change (its own terms) | Evidence of use in the upstream record |
|---|---|---|
| agile-workflow (10) | 0.16.14 → 0.16.16; UI callers repointed to the `ux-ui` concierge; bold-refactor skeptic; Antigravity manifest; Workbench-stamp bump test | Release summary for ux-ui-design 1.0.0 names the caller updates [upstream-ux-ui-concierge]{41}; no use of the skeptic recorded [upstream-bold-refactor-skeptic]{40} |
| code-audit (5) | 0.2.0 → 0.2.2 [upstream-learnings-observations]{38}; same skeptic and open-lens framing; cousin note to Workbench provocation; Antigravity manifest | None beyond authoring commits [upstream-bold-refactor-skeptic]{40} |
| ux-ui-design (3) | Seven pipeline skills replaced by one interview-first `ux-ui` concierge; −10008 lines | Delivery review evidence only; no later change besides the bump [upstream-ux-ui-concierge]{41} |
| prose-craft (9) | Interview-first drafting, reader-path plan, style profiles, model-voice catalog, optional parallel drafts, audience/domain language | Dogfood pass on its own ten docs [upstream-prose-craft-delta]{42} |
| sol-calibration (8, new) | Posture interview writing an AGENTS.md block; proportionality self-check; overbuilder review | Three follow-up commits 2026-08-23 to 08-29; no external use recorded [upstream-learnings-observations]{38} |
| declaudify (2, new) | Claude-only `UserPromptSubmit` hook injecting a static writing guide | None beyond creation [upstream-declaudify]{44} |
| agentic-research, agent-coordination, nates-toolkit, workflow (1 each) | Antigravity root `plugin.json` only | n/a |
| Workbench (159; ideas pass) | 0.5.0 → 0.26.11 [upstream-learnings-observations]{38}; see the ideas pass | Upstream runs its own repository on Workbench [upstream-work-conventions]{55} |
| peeragent (4 commits) | Windows npm-shim launch fix (0.8.2), multiline fix (0.8.3) | Validated on Windows; live agent tasks not exercised on Linux/macOS [peeragent-v083-release]{57} |

## Per-area findings

### agile-workflow

The plugin's version moved 0.16.14 → 0.16.16; a same-day 0.16.17 bump was
reverted [upstream-agile-workflow-delta]{39}. Upstream has kept agile-workflow
in "Maintenance mode (KTLO)" since before the merge base. New capability goes
to Workbench [upstream-agile-workflow-delta]{39}.

- **UI callers.** `scope`, `epic-design`, `feature-design` and `ideate` stop
  invoking `/ux-ui-design:palette`, `:screens` and `:flows`. They now offer the
  `/ux-ui-design:ux-ui` concierge and record mock paths only when mocks are
  produced [upstream-agile-workflow-delta]{39}. This is the caller half of the
  ux-ui-design restructure [upstream-ux-ui-concierge]{41}.
- **bold-refactor skeptic.** Lens tables become "a starting set, not a closed
  list". A fresh-context reviewer of "a different model class ... when one is
  available" must return kill / narrow / pass verdicts before any suggestion
  reaches the user [upstream-agile-workflow-delta]{39}. The commit message
  says the same requirement now applies across all
  provocation/bold-refactor skills, and the reviewer "defaults to no"
  [upstream-bold-refactor-skeptic]{40}. No upstream commit in the range
  records a use of the skeptic [upstream-bold-refactor-skeptic]{40}.
- **Packaging.** It gains an Antigravity root `plugin.json`
  [upstream-agile-workflow-delta]{39}. Its bump test gains a "Test group 9"
  that advances Workbench's dogfood `workbench_version` stamp
  [upstream-agile-workflow-delta]{39}.

### code-audit

code-audit `bold-refactor` gets the same open-lens framing and a "Skeptical
review" paragraph ("Generate without caution; let the reviewer do the
filtering") [upstream-bold-refactor-skeptic]{40}. A cousin note points at
Workbench's `skills/ideate/references/provocation.md`, so editors treat the
two texts as deliberate adaptations [upstream-bold-refactor-skeptic]{40}. The
fork's Workbench copy has no such file [upstream-learnings-observations]{38}.

### ux-ui-design

Version 1.0.0 replaces `ux-ui-principles`, `palette`, `components`, `motion`,
`screens`, `flows` and `adopt` with one concierge. Tier ordering, the AGENTS.md
auto-installer, pipeline enforcement and fixed option counts are gone
[upstream-ux-ui-concierge]{41}. The release marks the removed invocations as
**breaking** and keeps the `.mockups/` layout [upstream-ux-ui-concierge]{41}.
Upstream named "Trigger regression (one description replacing seven)" as its
top risk. The independent review returned four material findings, and the
user redirected the work twice [upstream-ux-ui-concierge]{41}. The record
holds delivery verification but no post-release use
[upstream-ux-ui-concierge]{41}.

At fork HEAD, 19 grep lines still use the removed names. They include
fork-owned `plugins/research-pipeline/skills/epic-design/SKILL.md` and
`feature-design/SKILL.md` [upstream-learnings-observations]{38}.

### prose-craft

0.1.3 → 0.3.1. `prose-draft` now opens with an alignment interview, "never
applies style or structure silently", and adds a reader-path plan and a
six-field brief [upstream-prose-craft-delta]{42}. A later commit tells it not
to "routinely suggest plain technical language" [upstream-prose-craft-delta]{42}.
The new `model-voice/` catalog names eight specific model versions
[upstream-prose-craft-delta]{42}. Parallel drafts recruit writers of different
model classes and merge by beat-anchored fusion
[upstream-prose-craft-delta]{42}. Usage evidence is a dogfood pass in which a
fresh-context review returned 7 material and 11 polish findings, all accepted
[upstream-prose-craft-delta]{42}. No fork plugin outside prose-craft
references these skills [upstream-learnings-observations]{38}.

### sol-calibration (new)

`calibrate-posture` interviews the user and writes a posture block between
`sol-calibration:start/end` markers in project and/or global `~/AGENTS.md`
[upstream-sol-calibration]{43}. `proportionality-check` is "Not a gate". It
asks the agent to name the threat and its victim, and treats a 25x
machinery-to-feature ratio as a smell. It explicitly does not license skipping
verification that a convention requires [upstream-sol-calibration]{43}.
`overbuilder-review` "separates guarantees from proof mechanisms" and reads any
existing Workbench `## Overbuilding calibration` [upstream-sol-calibration]{43}.
The motivating item says "Sol often needs reasonable stop boundaries". Another
item names "existing AGENTS.md rigor rules" and plugin-injected instructions
as pulls toward heavier posture [upstream-sol-calibration]{43}.

### declaudify (new)

A Claude Code-only hook injects a static guide on every user turn. Its first
bullet is "Do not talk like Claude. You are not Claude." The other bullets ask
for plain technical language, treat the visible chat as the only shared
context, and require separating facts from inferences [upstream-declaudify]{44}.
It is not registered for Codex or Antigravity [upstream-declaudify]{44}.

### Antigravity manifests (single-commit areas)

3ed9c532 adds `plugins/<name>/plugin.json` for Antigravity and an
`.agents/plugins.json` registry. It extends the parity posture: "Codex and
Antigravity get the equivalent in the same change"
[upstream-agy-multichannel]{45}. `bump-version.sh` now checks and bumps the
third manifest [upstream-agy-multichannel]{45}. For agentic-research,
agent-coordination, nates-toolkit and workflow, this manifest is the whole
change in the range [upstream-agy-multichannel]{45}. Upstream agentic-research
stays at 0.6.5; the fork is at 0.7.0 [upstream-learnings-observations]{38}.

### Root and marketplace

The upstream Claude catalog adds `sol-calibration`, `declaudify` and
`theatre-feedback`. The last is a `git-subdir` source in `nklisch/theatre`
[upstream-learnings-observations]{38}. `docs/PRINCIPLES.md` was created in a commit titled "Reconcile Workbench setup
with 0.15.1 contract" [upstream-root-principles]{59}. Two of its rules, "File
real bugs, fix bad tests" and "Never game a test", do not appear by name in
the fork's agile-workflow principles (a phrase check, not a semantic
comparison), which already carry "Leave It Simpler", "Compatibility Is
Earned" and "Tests Earn Their Keep"
[upstream-root-principles]{59} [upstream-learnings-observations]{38}.

### peeragent 0.8.1 → 0.8.3

v0.8.2 fixed Windows npm-shim launches but rejected newlines, blocking
peeragent's own instruction header. It is superseded
[peeragent-v082-release]{56}. v0.8.3 forwards arguments through deferred
environment expansion. It caps quoted arguments at cmd.exe's 8191 characters,
and "native executables and Unix launches retain direct execution"
[peeragent-v083-release]{57}. In code, non-Windows builds define
`commandContext` as the previous `exec.CommandContext` call. No file under
`plugin/skills/` changed [peeragent-v081-v083-compare]{58}. Locally, Claude
caches 0.8.1 and Codex caches 0.8.3, with identical `skills/` directories. The
fork's marketplace entry has no version pin and still describes "peer and
peer-review skills", but both releases ship only `peer`
[upstream-learnings-observations]{38}.

## Workbench ideas pass

Workbench is the upstream workflow successor. Its guide says its `.work/`
schema is mutually exclusive with agile-workflow's and calls agile-workflow
"the maintenance-mode alternative" [upstream-workbench-guide]{46}. The themes
below are ideas only.

1. **Overbuilding calibration.** Conventions hold a short, user-confirmed
   statement of likely overbuilding and justified complexity, applied by
   every design and review [upstream-workbench-guide]{46}. Upstream's own
   entry names "receipts and counters, exhaustive validators" as likely
   overbuilding [upstream-work-conventions]{55}.
2. **Machinery forecast.** Before a design binds, compare the minimum
   coherent chain with the proposed chain. Be skeptical of "parallel ledgers,
   receipts, status files" and "bespoke validators ... built mainly to police
   agent-generated bookkeeping". Keep the forecast conversational: "Do not create an
   artifact, fixed packet, or new gate for it"
   [upstream-workbench-assurance-machinery]{48}.
3. **Simplification posture.** `hygiene` / `balanced` / `structural` sets how
   far behaviour-preserving reduction reaches. Simplicity is counted in
   durable concepts and operating cost, not lines
   [upstream-workbench-simplification]{47}.
4. **Design-review priorities.** In order: right problem, best-fit solution,
   important omissions, repository fit, then correctness as a baseline.
   Concurrency-protocol reviews stop after two rounds unless hangs, crashes
   or corruption remain [upstream-workbench-design-review]{54}.
5. **Adaptive review boundaries.** One shared pass can cover several
   deliveries and "replaces per-feature passes rather than adding to them"
   [upstream-workbench-guide]{46}. Design review is aligned once per run and
   is optional [upstream-workbench-review-boundaries]{51}.
6. **Commit before handing back; stable review targets.** Reviews target an
   identified commit or base/head range, and uncommitted inspection is only
   advisory [upstream-workbench-git-posture]{50}.
7. **Local model notes.** An optional, pruned `.work/MODEL-NOTES.md`
   separates verified, user-reported and tentative observations, with "No
   scores, win rates, universal tiers" [upstream-workbench-model-notes]{52}.
8. **Research rigor and ownership.** An `adaptive` rigor level picks the
   lowest credible gate without source- or agent-count thresholds.
   `.research/CONVENTIONS.md` declares an owning provider, and other
   providers defer. "Stop after the same failure recurs twice"
   [upstream-workbench-research-rigor]{53}.
9. **Verification cadence.** Each check runs once, at the cheapest boundary
   that can catch what it protects. "A check that cannot fail is not a gate".
   With several sessions on one machine, merge first and gate after. A
   delegated job "never deletes a worktree, branch, or build folder it did
   not create" [upstream-workbench-verification-cadence]{49}.
10. **Inline-first execution and model alignment.** With no stated preference,
    design, implementation and corrections stay inline. Before any
    multi-agent task, models are aligned with the user
    [upstream-workbench-guide]{46}.

**Volatility.** Workbench went from 0.5.0 to 0.26.11, and 67 of its 159
commits are version bumps [upstream-learnings-observations]{38}. A
`context-scan` skill was removed six days after it was added. A SessionStart
hook was removed about seven weeks after it was added, and the guide now says
"Workbench has no session hook" [upstream-learnings-observations]{38}
[upstream-workbench-guide]{46}. Review caps were bounded and then uncapped
the next day. A later commit restored guidance that earlier consolidations
had dropped [upstream-learnings-observations]{38}. {inferred: aggregate}
Ideas that persisted across these revisions are steadier than any single
snapshot's text.

## Mapping to this fork

This section `extends` the sources. It reads the fork's own rules as lenses,
not evidence: Workbench is prior art and never a migration target, research
stays with Agentic Research, upstream owns its plugins except documented fork
patches, and the fork owns `research-pipeline`, marketplace composition and
`.work/`. Classifications are proposals for the operator.

| Area / idea | Mapping | Files a change touches (owner) | Main reason not to adopt |
|---|---|---|---|
| agile-workflow UI caller rewrites | adopt only together with ux-ui-design 1.0.0; skip otherwise | `plugins/agile-workflow/skills/{scope,epic-design,feature-design,ideate}/SKILL.md` (upstream); `plugins/research-pipeline/skills/{epic-design,feature-design}/SKILL.md` (fork); `docs/agile-workflow-guide.md`, `docs/ux-ui-design-guide.md` | Breaks the explicit `/ux-ui-design:*` invocations the fork's design skills use; no post-release usage evidence |
| bold-refactor skeptic (agile-workflow + code-audit) | adopt | `plugins/agile-workflow/skills/bold-refactor/SKILL.md`, `plugins/code-audit/skills/bold-refactor/SKILL.md` (upstream) | Adds a reviewer call to every run with no recorded use; the code-audit cousin note would dangle without Workbench's `provocation.md` |
| Workbench-stamp bump test (group 9) | not-relevant; conflicts textually | `plugins/agile-workflow/scripts/tests/bump-version.test.sh` (upstream test carrying a fork guard) | The fork does not dogfood Workbench; `REPO12` collides with the fork's refuse-on-main guard |
| Antigravity manifests (all plugins + `bump-version.sh`) | adapt only if Antigravity loads these plugins; otherwise not-relevant | `plugins/*/plugin.json`, `.agents/plugins.json`, `scripts/bump-version.sh` (fork-patched), `AGENTS.md` (fork) | Adds a third parity channel to a fork whose rules validate Claude and Codex shapes; research-pipeline would need its own manifest |
| ux-ui-design 1.0.0 | adopt (with callers) or skip; the main simplification opportunity | `plugins/ux-ui-design/**` (upstream) plus the caller rows above | Breaking change; trigger-regression risk named upstream; fork use of the UI pipeline was not inspected |
| prose-craft 0.3.1 | adopt | `plugins/prose-craft/**` (upstream) | Interview friction on every draft; model-voice files name model versions that will age; parallel drafts multiply cost |
| sol-calibration | adapt or skip (new plugin, additive catalog entry) | `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json` (fork) | Overlaps agile-workflow principles and gate-cruft; writes a managed block into a global `~/AGENTS.md` path that may not match each host's global file; its far posture end ("skip security and verification") [upstream-sol-calibration]{43} conflicts with standing durable rules |
| declaudify | not-relevant (operator style choice) | marketplace catalogs (fork) | Claude-only every-turn context injection outside the parity posture; no use evidence |
| agentic-research upstream | not-relevant (fork is ahead, 0.7.0 vs 0.6.5) | none, unless Antigravity is adopted | Only change is the Antigravity manifest |
| agent-coordination, nates-toolkit, workflow | follow the Antigravity decision | `plugins/<name>/plugin.json` (upstream) | Same as Antigravity |
| Root principles: "File real bugs, fix bad tests"; "Never game a test" [upstream-root-principles]{59} | adapt into the fork's agile-workflow principles as a documented fork patch, or skip | `plugins/agile-workflow/docs/PRINCIPLES.md`, `skills/principles/**` (upstream; fork patch) | Upstream keeps them as repository rules, not agile-workflow principles; patching a KTLO plugin increases sync drift |
| theatre-feedback catalog entry | not inspected | marketplace catalogs (fork) | Content not read |
| peeragent 0.8.2/0.8.3 | already-have in effect; no action on macOS | optional: fork marketplace description ("peer-review skills") [upstream-learnings-observations]{38} (fork) | Nothing to adopt; the fix is Windows-only |
| Stale Workbench 0.5.0 in fork catalogs | open question (refresh, keep or delist) | marketplace catalogs (fork), `plugins/workbench/**` (upstream) | No sync is authorised by this engagement |
| W1 overbuilding calibration | adapt (convention prose) | `.work/CONVENTIONS.md` (fork); optional read-step in research-pipeline design skills (fork) | Agile-workflow principles already state proportional rigor; another convention to maintain |
| W2 machinery forecast | adapt | `plugins/research-pipeline/skills/feature-design/SKILL.md`, `epic-design` (fork) | Overlaps the existing 2–3 option and pre-mortem steps |
| W3 receipts/validators skepticism | adapt as a methodology-review question, not a change | fork review-receipt convention, verification records (fork) | The fork adopted receipts deliberately; this lens is upstream's opinion, not evidence |
| W4 design-review priorities | adapt | research-pipeline design self-checks (fork); agile-workflow review (upstream; fork patch) | Partly present already; patching review adds drift |
| W5 adaptive review boundaries | already-have in part | agile-workflow review (upstream), `.work/CONVENTIONS.md` (fork) | Shared passes delay feedback, which upstream itself names as the trade-off |
| W6 commit-before-handback, stable targets | already-have (receipts name `base..head`) | — | — |
| W7 local model notes | adapt | new optional `.work/MODEL-NOTES.md` convention (fork) vs `plugins/agile-workflow/skills/principles/references/models.md` (fork-patched) | Duplicates the global models reference; another file to prune |
| W8 research rigor/ownership | adapt selectively (owner frontmatter; repeat-failure stop) | `.research/CONVENTIONS.md` (fork), agentic-research orchestrator (fork-maintained) | ARD already stops on a second NEEDS-REVISION; `adaptive` rigor weakens the explicit kickoff dial |
| W9 verification cadence / merge-first | not-relevant now; adopt the rule that delegated jobs never delete what they did not create, if wanted | agile-workflow implement-orchestrator (upstream; fork patch) | The fork has no CI and merges PRs manually |
| W10 inline-first, model alignment | already-have in part (implement vs implement-orchestrator) | — | — |
| W11 opt-in release gates as named lenses | already-have (`gates_for_release`, `scan-*` libraries) | — | — |

The fork has no `## Overbuilding calibration` in `.work/CONVENTIONS.md`.
It does carry a review receipt template and states it has no CI. Its
`.research/CONVENTIONS.md` has no `owner:` frontmatter
[upstream-learnings-observations]{38}.

## Contradictions

- **Receipts.** Upstream's calibration lists "receipts and counters,
  exhaustive validators" as likely overbuilding [upstream-work-conventions]{55}.
  The fork's conventions require a review receipt and post-review commit
  enumeration [upstream-learnings-observations]{38}. Relationship: `tension`.
  The two are opposite design choices for the same audit need, and neither
  source measures outcomes.
- **Attesting repository files.** Workbench research grounds "fetched
  external sources, not repository files" [upstream-workbench-research-rigor]{53}.
  This survey's observation record is attested by `source_path`
  [upstream-learnings-observations]{38}. Relationship:
  `incommensurable`: the two providers define different evidence classes.
- **Fresh context vs inline.** Bold-refactor requires a fresh-context,
  cross-model skeptic before the user sees anything
  [upstream-bold-refactor-skeptic]{40}. Workbench defaults to inline-first
  execution and keeps review independence optional unless requested
  [upstream-workbench-guide]{46}. Relationship: `qualifies`: the skeptic
  applies to provocation output, while Workbench's default applies to
  delivery.

## Disconfirming analysis

Searched for evidence against each adopt/adapt candidate:

- **Skeptic.** No recorded use. The message records only the prose method
  used to write it [upstream-bold-refactor-skeptic]{40}.
- **ux-ui 1.0.0.** Upstream records a top trigger-regression risk, four
  material review findings and two mid-course redirections. Nothing after the
  release shows the concierge in use [upstream-ux-ui-concierge]{41}.
- **prose-craft.** The usage evidence found is self-application to its own
  docs [upstream-prose-craft-delta]{42}.
- **sol-calibration.** It was motivated by one model family's tendencies
  ("Sol often needs reasonable stop boundaries"). Its follow-up items treat
  plugin-injected instructions as part of the over-rigor problem
  [upstream-sol-calibration]{43}. {inferred: tension} Adding it to a fork
  that already injects knowledge-index and substrate context at session start
  could feed the problem it targets.
- **Workbench ideas.** Removals within days or weeks and the restored
  guidance show that individual mechanisms did not hold
  [upstream-learnings-observations]{38}. The machinery-forecast and
  overbuilding-calibration themes recur across the guide, references and
  upstream's own conventions [upstream-workbench-guide]{46}
  [upstream-workbench-assurance-machinery]{48} [upstream-work-conventions]{55}.
- **peeragent.** Searched the compare for non-Windows behaviour changes. The
  Unix path is unchanged [peeragent-v081-v083-compare]{58}. The release
  notes that live agent tasks were not exercised on Linux or macOS
  [peeragent-v083-release]{57}, so the conclusion that macOS behaviour is
  unchanged rests on code inspection, not a run.

## Not inspected

- Workbench was read at theme level: the guide, nine references, upstream
  conventions and commit subjects. Most of its 79 changed files, its SPEC and
  VISION, and its scripts were not read.
- `nklisch/theatre` (theatre-feedback) content; `.knowledge/index.json`,
  `docs/ARCHITECTURE.md`, `docs/SPEC.md`, `docs/VISION.md` and
  `scripts/check-workbench-sync.py` diffs; the ux-ui-design 1.0.0 reference
  library text.
- Whether the operator uses ux-ui-design, prose-craft or Antigravity in other
  projects. Other projects were out of scope.
- Rebuilt work-view and peeragent binaries were not executed; peeragent
  v0.8.0 → v0.8.1 is outside the commissioned range.
