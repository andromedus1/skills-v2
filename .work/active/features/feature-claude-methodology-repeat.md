---
id: feature-claude-methodology-repeat
kind: feature
stage: drafting
tags: [methodology-review, research-pipeline, agentic-research]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-18
updated: 2026-10-18
---

# Claude-driven methodology review repeat (QVC)

## Brief

This item is the root loop controller for review `QVC`: a Claude-driven repeat of
the completed Codex-driven `QVE` methodology review on the same three topics. It
owns the charter, component returns, operator decisions and dated assessments.
Separately commissioned research owns its own engagements; their completion
cannot close this controller.

Invocation authorizes investigation and review artifacts only. Changes to project
methods, skills, contracts or policy require Andrew's adjudication of a decision
packet; publication, package merge, corpus migration and automatic adoption of
findings remain out of scope.

## Strategic decisions

- **Settings**: mixed scope authority, standard research verification, whole-review
  decomposition with adaptive research inside each part, five root rounds — carried
  forward from QVE as established by the capture below.
- **Independence from QVE findings**: Claude forms component findings from the
  current baseline, its skills and the grounding research before reading QVE's
  component returns, assessments and adjudications; comparison with QVE follows as
  a separate step. Agreement is not a target. QVE's charter and topics are inputs.
- **Fresh assessor**: Codex through `peeragent:peer`, per the project's cross-model
  preference when Claude drives; fall back to a fresh-context Claude assessor and
  record the limitation if Codex is unavailable.

## Simplification opportunity

None proposed at scope time. The review itself may identify checks, prose or
duplicate review paths that QVE added and that do not earn their cost.

## Original capture (historical context)

Andrew requested a Claude-driven session to repeat the methodology-review exercise
on the same topics as the completed Codex-driven run. Capture this for next session;
do not start the exercise during the current wrap-up. Claude should drive the work,
with the existing project preference for Codex when independent cross-model review
is called for.

The same topics are:

- Quality criteria, evidence and bounded correction loops across Research Pipeline,
  Agentic Research and methodology-review, including lessons from doc-review.
- Independent review of consequential prompt/skill changes, review weights, and
  reuse of a completed review plus verified corrections.
- Citation-warning signal and noise, including version-number advisories.

Retain the broader package-boundary context: Research Pipeline owns project process;
Agentic Research owns grounded research. The established settings were mixed scope,
standard research verification, and whole-review decomposition with adaptive
research inside each part. Compare Claude's findings with the earlier run without
treating agreement as the required outcome. Follow the current local skill and
project process when scoping the repeat; prior implementation is evidence to assess.

## Recover the prior work

- Start with `plugins/research-pipeline/skills/methodology-review/SKILL.md` and its
  two references. Verify the session is using this checkout's current instructions;
  the previous arc did not publish or refresh installed plugin caches.
- Grounding: `.research/analysis/briefs/quality-feedback-loops.md` and its source
  records. Its paper coverage is abstract/metadata limited, not a universal
  effectiveness or model-comparison result.
- Completed controller: `.work/archive/feature-quality-verification.md`.
  Recover the full body with
  `git show 0b1c2978:.work/active/features/feature-quality-verification.md`.
- Research verification: `.work/archive/story-research-quality-feedback.md`;
  full body at
  `git show 0b1c2978:.work/active/stories/story-research-quality-feedback.md`.
- Prior product baseline: `6419b3bc`; final assessment at `a2f03eaa`; archived at
  `d32f12fe`. QVE closed clean within reviewed scope after 3 of 5 root rounds.
  Preserve that completed history and its counts. Establish the current baseline
  at next-session kickoff rather than assuming these revisions remain current.
- Evidence: 13 synthetic forward scenarios per host, 57/57 ARD conformance checks,
  one standard independent feature review plus verified fixes, and fresh methodology
  assessments. The full work record preserves coverage limits and actual outcomes;
  temporary test artifacts may not survive to the next session. No live release
  was exercised.

Related parked observations are `idea-release-checkpoint-handoff` and
`idea-citation-advisory-coverage`. They are inputs to consider, not preselected fixes.
The unrelated Pi backlog remains separate. This capture does not authorize a
publication, package merge, corpus migration, or automatic adoption of new findings.

## Methodology review QVC — charter and checkpoint 1

Baseline: `e3e2e070` (product content identical to `a36137fa`). Root round: 1
allocated; 0 complete; shared limit: 5. Instruction source verified: skills load
from this working tree (the local-directory marketplace resolves
`agile-workflow:scope` to `plugins/agile-workflow/skills/scope`), and the review
protocol was read from `plugins/research-pipeline/skills/methodology-review/`.

**Users and jobs.** Operators and agents who conduct grounded research, change
skills/prompt-ware, and claim that research, delivery or a release checkpoint is
complete. **Outcome.** Completion claims are backed by required, current evidence;
feedback is actionable; correction cost is bounded; the operator spends attention
where risk warrants it.

**Fixed constraints.** Agile Workflow + Research Pipeline remain the process;
Agentic Research owns grounded research and its verification stack; Andrew
adjudicates project-method changes; no CI exists, PRs merge manually; both Claude
and Codex plugin shapes must keep working. **Hypotheses under review** (inherited
design choices, not constraints): the QVE-era rules that missing/stale evidence
is not a pass; review weights with one standard independent pass; reuse of a
covering review plus verified fixes; quality-checkpoint reconciliation of owner
records; root-round limits; citation-advisory classification; and the amount of
prose these rules occupy.

**Topics (children).** Coordinated review — three children feed one combined
decision packet at the root. Considered cuts: unsplit (would bury the citation
signal question, which has its own local mechanics); by plugin (would repeat the
shared "what counts as evidence" question three times); by topic (chosen). A
program shape was not chosen because Andrew adjudicates all three in one batch
and no child has an independent change schedule. The root owns the shared
question "what evidence establishes completion" and the cross-child scenarios.

| Child | Scope and contribution | Evidence plan |
| --- | --- | --- |
| QVC-E | Quality criteria, evidence and bounded correction loops across Research Pipeline, Agentic Research and methodology-review, including lessons from doc-review | Local contract map + `quality-feedback-loops` brief + supplementary research |
| QVC-R | Independent review of consequential prompt/skill changes, review weights, and reuse of a completed review plus verified corrections | Local routing map + supplementary research on evaluator independence |
| QVC-S | Citation-warning signal and noise, including version-number advisories | Reproduce current lint/gate behavior on this corpus + supplementary research on warning noise |

**Criteria.** Detection of material defects; independence and scope of
verification; authority; interruption/resume recovery; operator and agent cost;
false-positive burden; portability across hosts; maintenance and prose burden;
whether the rule is enforced by anything other than reader compliance.

**Scenarios.** (1) Success path: research converges, delivery reviewed, checkpoint
ready. (2) A required check fails or is missing. (3) Output changes after review.
(4) Correction limit exhausted with blockers. (5) Interrupted review resumed in a
new session or other host. (6) A small prompt edit vs. a consequential contract
change. (7) A citation lint run with real and spurious warnings.

**Comparison sample (provisional).** Evaluator-optimizer and agent-eval guidance;
same-model refinement vs. intrinsic-correction limits (existing brief); LLM-judge
self-preference and cross-model judging evidence; human code-review practice
(single reviewer, re-review on change); static-analysis warning practice
(false-positive tolerance, alert fatigue); and a simpler baseline: an ordinary
PR checklist with one reviewer and no reconciliation layer.

**Research settings.** Reuse `quality-feedback-loops` (abstract-limited). One
supplementary engagement, commissioned through a separate `[research]` story with
mixed scope authority and standard verification, covers the named gaps the
existing brief disclaims: cross-model vs. same-model review evidence, and
warning-noise tolerance. Doc-review lessons and QVC-S mechanics are local.

**Required checks and owners.**

| Check | Owner | Evidence that establishes it | Result |
| --- | --- | --- | --- |
| Supplementary research converged at standard rigor | agentic-research orchestrator | Engagement record with gate results | pending |
| Child assessments returned | QVC children | Dated reports below | pending |
| Fresh whole-scope assessment | Codex via peeragent (fallback: fresh Claude) | Dated report in this record | pending |
| QVE comparison | root | Section comparing QVC vs QVE after independent findings | pending |
| Delivery checks for any authorized change | agile-workflow review | Item review record | not authorized |

Exit: none yet. Next: commission research; dispatch children blinded to QVE's
returns and assessments.

## Component returns — root round 1 (2026-10-18)

Children ran blinded to QVE's returns, assessments and adjudications. Reports are
recorded as returned (condensed only for layout); the root has not yet integrated them.

### QVC-S — citation-warning signal (returned 2026-10-18)

Scope: canonical lint `plugins/agentic-research/ard-core/kernel/lint-citations.py`
(+ `catalogs.json`, `CATALOGS.md` §3, `conformance/`), gate adapter
`gate-citations/SKILL.md`, consumers (`quality-checkpoint/SKILL.md:128-131`,
AR fork patch `verification-record.md:26-33`), `.research/` corpus. Baseline
`e3e2e070`. Not covered: a real release gate run (idempotency/emission), URL
checks, verified external warning-noise evidence. Parked idea read only after the
classification was written (`/private/tmp/claude-501/qvcs/classification.txt`).

Reproduction: the gate's exact command (`--no-url-check --format json`) → exit 0;
17 files; 35 citations all resolved; 0 broken/thin; `substrate_confidence_omitted`
5; `campaign_unbound` 0; 13 pattern flags (version-number 10, named-feature-claim 2,
comparative-superlative 1). `--exit-code-on high|medium|low` → exit 0. Conformance
57/57. Classification: version-number 10/10 false positives (9 in source-direct
attestations — arXiv "version 2", manifest and fixture versions; 1 analytical line
anchored by a citation two lines later); named-feature 1 FP + 1 ambiguous;
superlative 1 ambiguous-leaning-FP. 0/13 true defects; ≈85% FP by definition; the
gate prescribes no action for advisories (`SKILL.md:101-105`). Probe: arXiv IDs,
`§4.2`, `0.71`, `Python 3.12` flagged; `ICLR 2024`, dates, `GPT-4`, code, URLs not;
"version 1.9.0" splits into two matches. Masking check: a high unresolved handle on
an advisory line still reports high and trips `--exit-code-on high`; advisories do
not mask integrity failures. Sample: one corpus, two briefs — recall on real
fabricated claims cannot be estimated here.

| ID | Finding (all minor) | Recommendation / would authorize | Owner |
| --- | --- | --- | --- |
| QVC-S/METH-001 | Version matcher (`lint-citations.py:70`) ignores citations and tier; in attestations only URL/code are suppressed (`:466-469`) while decimal/count/effort rules are tier-suppressed (`:470-484`), contrary to the category's "without an in-corpus anchor" definition (`CATALOGS.md:116`); conformance has no negative fixture. Counter: cheap, grouped, deliberate recall trade (`:369-375`) | Scratch-only precision/recall experiment first; then possibly an upstream proposal (tier/citation suppression + negative fixtures). No repo edits | agentic-research (kernel unchanged by fork policy, `docs/project-navigation.md:66`) |
| QVC-S/METH-002 | "Exit 0 is not a pass" is prose-only and stated three times (gate `:100-101`, checkpoint `:128-131`, verification-record `:26-27`); gate omits `--exit-code-on medium`, which matches its own blocking policy | Edit only `gate-citations/SKILL.md` Phase 3 command and interpretation; keep the JSON-validity check (crash also exits 1) | research-pipeline |
| QVC-S/METH-003 | Gate drops warn-only `campaign_unbound` / `substrate_confidence_omitted`; conformance fixture `c9-f1-real` resolves `intra-program-resolved`, severity none, visible only in `campaign_unbound` (`:584-587`) → silently clean through the gate. Exposure here nil | One reporting line with both list counts; no items/threshold. Matching verification-record line is an AR fork patch — Andrew's call | research-pipeline (+ AR fork patch) |
| QVC-S/METH-004 | Gate-level pattern reporting has no consumer: engagements already lint and spot-check (`research-orchestrator/SKILL.md:88,96,230`); checkpoint says advisory counts never create a gate; 9/13 flags are attestation-only. Counter: only signal on briefs edited post-engagement | Decide with METH-001: retain, report by tier, or `--no-pattern-check` at the gate | research-pipeline |

Incidental defects (gate-citations SKILL): non-broken status list `:93-95` omits
`acquisition-candidate`; stage table `:113-119` and item Status list omit
`non-canonical-handle` and `duplicate-frontmatter-key` (pre-existing drift that
survived a reviewed adjacent edit); version caveat `:102-104` omits arXiv IDs, `§x.y`
and "version N"; example JSON paths `:83,89` use `.research/briefs/`.

Versus `idea-citation-advisory-coverage`: agrees with METH-003 (counts 0/5); adds the
silently-clean fabricated campaign case; contradicts its premise that version-number
work is complete — residual noise is in the matcher and the gate's missing consumer.
METH-002 and incidentals 1, 2, 4 are new.

Sibling implications: QVC-E — METH-002 is a reader-compliance rule triplicated;
incidental 2 is copied-contract drift. QVC-R — a reviewed prose-only edit missed
adjacent contract drift. Evidence requests: static-analysis FP tolerance (Tricorder
~10% effective FP, recalled unverified), warn-only alert fatigue, METH-001 experiment.

Child exit: **awaiting change or evidence** — no major findings; supplementary
research pending; METH-001–004 minor proposals await batch adjudication.

### QVC-E — quality criteria, evidence and correction loops (returned 2026-10-18)

Scope: build-process, research-composition, quality-checkpoint, doc-review,
gate-docs-extension, methodology-review (+refs); research-orchestrator,
verification-record, evaluator/adversarial-reader briefs; `.work/CONVENTIONS.md`;
tests and CI; agile `review`/`release-deploy` interfaces only. Baseline `e3e2e070`
(checked at `acf477a4`). Ran read-only (scratch `/private/tmp/claude-501/qvce`):
conformance 57/57; resolver test pass; skill-portability and skill-metadata
**fail under default python3** (no PyYAML), pass in a scratch venv; citation lint
0 broken/0 thin/13 advisories. Unavailable: live release or checkpoint run, any
doc-review run (no report in history), supplementary research, adopter projects.

Enforcement map: citation syntax and skill shape are mechanical (not in CI; shape
tests environment-fragile); "missing/errored/stale ≠ pass", covering-review reuse,
doc-review's fresh-audit exit and cap, ARD's one-revision rule, methodology round
limit and release-readiness precedence are reader compliance (or author judgment).
CI (`.github/workflows/`) covers only Workbench and view binaries.

| ID | Sev. | Finding | Recommendation / would authorize |
| --- | --- | --- | --- |
| QVC-E/METH-001 | **major** (conf. medium) | Every evidence/correction rule in scope is enforced only by reader compliance and has no durable behavioral regression evidence: tests are shape-only (`skill-portability.test.sh:18-71`), not in CI, and error by default; the rewritten quality-checkpoint has never run live and `release-deploy/SKILL.md` never invokes it; earlier scenario artifacts were temporary. Grounding: outcomes are environment state, regression evals protect capability (`anthropic-agent-evals`), and "local failure examples and execution tests must establish whether a concrete workflow change helps" (brief:64-67). Decision-blocking uncertainty for retain-vs-simplify, not proof the rules are wrong. Counter: the rewrite fixed real defects (nonexistent `gate-infra`; zero items read as clean); model-graded evals are noisy; manual PR merge backstops | Experiment: durable scenario fixtures for the charter's 7 scenarios with expected-outcome labels and a manual (peeragent) runner, plus a retrospective audit of closed items' evidence tables; run against current rules and a compressed variant. Would authorize fixture/runner files under `plugins/research-pipeline/scripts/tests/` via normal delivery; no skill-text changes |
| QVC-E/METH-002 | minor | One contract ("missing/errored/stale ≠ pass; process success or zero items ≠ approval") restated on ≥7 surfaces (`build-process.md:157-158,184-188`; `research-composition.md:51-52`; `quality-checkpoint/SKILL.md:34,118-119,128,162-163,172-173`; `verification-record.md:10-11,24-27`; `CONVENTIONS.md:35-36`; `methodology-review/SKILL.md:77`; `review-record.md:56`); "child ≠ parent convergence" four times. methodology-review ≈5,300 words/≈108 negations. Counter: skills load alone; this review's charter shows the protocol working | Defer until METH-001's harness can compare variants (candidates: canonical `build-process.md` §Completion with one-line local applications; compress methodology-review). Authorizes nothing yet |
| QVC-E/METH-003 | minor | Correction-loop bounds uneven: ARD well bounded (`research-orchestrator/SKILL.md:232-235`); doc-review cap 5 (`doc-review/SKILL.md:291,297`) but its report has no baseline/iteration/capped fields (`:221-228`), so checkpoint rules `quality-checkpoint:105,137-139` are uncheckable and an interrupted loop resets its cap; agile thorough/maximum has no numeric cap (`review/SKILL.md:76,233-237`); methodology's default 5 is unjustified by grounding (brief:64-66), though adjustable; `review-decomposition.md:135-136` ambiguous on whether research revisions count | Add baseline, iteration and capped fields to the doc-review report template; authorizes that edit only |
| QVC-E/METH-004 | minor (could be major where docs merge unreviewed) | doc-review's autonomous Critical/High fixing (`:287,293`) includes resolving foundation-doc contradictions (`:213`), which can change stated intent (vs `build-process.md:20-21`; its own `:348`); checkpoint makes it required/blocking (`quality-checkpoint:66,103-105,164-165`). Its target model is stale: roadmap phases, blocking-brief lines, MCP/BigQuery/TS specifics (`:120-139,151-153,188-203`) vs retired roadmap pattern (`CONVENTIONS.md:3-7`); substantively unchanged since bootstrap port; overlaps gate-docs Check 1. Transferable strength: exit read from a fresh full-scope audit with explicit non-re-audit list (`:304-317`), already in methodology-review. Non-transferable: no stable IDs, full re-audit regardless of fix size, same-host reviewer, emphatic prose | Andrew decides doc-review's role (retain; mechanical-only autofix + route contradictions to operator; retarget to `foundation_docs` + `.work`; drop from required set where gate-docs covers it). Would authorize scoping one feature item |
| QVC-E/METH-005 | minor | Post-review "materially uncovered" is author-judged (`quality-checkpoint:92-97`, `build-process.md:119-122`, `CONVENTIONS.md:32-34`, `verification-record.md:36-39`) with no recorded diff anchor | Record reviewed sha and `git diff --stat <reviewed>..HEAD` at closure; owned primarily by QVC-R |
| QVC-E/METH-006 | minor | "Missing required evidence is not a pass" (`CONVENTIONS.md:35-36`) binds to nothing on the actual ship path: `scripts/bump-version.sh` runs no tests and commits/pushes (`:157,194`); no plugin-bump check list; release path dormant (cf. `idea-release-checkpoint-handoff`). Simpler baseline (PR checklist: shape tests, conformance, resolver test, reviewed sha, verified fixes) fits better; item evidence tables still add resume value. Counter: a checklist is also compliance-only | CONVENTIONS edit and/or PR template |

Incidental defects: I-1 ARD hard-floor lint command is repo-relative
(`research-orchestrator/SKILL.md:88,227`), failing outside skills-v2 (upstream);
I-2 tests need undeclared PyYAML; I-3 doc-review uses `${CLAUDE_PLUGIN_ROOT}` only
(`:17`) and stale non-namespaced `knowledge/lint`, `/knowledge-index`
(`:58,323,349`); I-4 foundation doc `build-process.md` missing from
`docs/knowledge-index.yaml`, so doc-review discovery skips it; I-5 no upstream-drift
test for the AR fork patch (`docs/project-navigation.md:60-68`); I-6
`bump-version.sh` pushes with no branch guard.

Scenario walk: success coherent on paper but checkpoint unreachable from
`release-deploy`; missing check consistent "not a pass" by compliance only;
changed-after-review has three defensible but different policies, delivery lacks
a diff anchor; exhausted limit handled by ARD/methodology, not doc-review or
thorough review; cross-host resume durable except doc-review loop state; small vs
consequential author-classified.

Sibling implications: QVC-R — uncapped thorough review, author-judged materiality,
doc-review's same-host reviewer vs any cross-model requirement, unguarded push.
QVC-S — "JSON not exit code" triplicated; mechanical alternative via
`--exit-code-on`. Evidence requests: ER-1 reliability/variance of scenario or
model-graded regression evals for prompt changes; ER-2 PR/review checklist
compliance vs defect outcomes; ER-3 safe/unsafe autofix classes in linters/doc
tools; ER-4 diminishing returns and iteration caps in refinement loops. Local
experiment (needs authorization): doc-review on a seeded-drift fixture.

Child exit: **awaiting decision** (METH-001 experiment; METH-004 doc-review role);
secondary awaiting evidence (ER-1–4). No remedies pending.

### QVC-R — independent review routing, weights and reuse (returned 2026-10-18)

Scope: agile `review` (+4 refs), principles Part IV, `advisory-review.md`,
`models.md`, `subagents.md`; review steps in autopilot, implement-orchestrator,
implement, fix, scope; hook capsule (`prompt-context.py:103-120`); CONVENTIONS;
build-process Delivery/Completion; quality-checkpoint; RP feature/epic-design
advisory text; user-level "Cross-model review" rule; grounding brief; git/PR state.
Ownership diffed against upstream: review/principles/autopilot/scope/fix match
upstream except fork additions in `models.md` (Kimi/Pi); CONVENTIONS,
build-process, quality-checkpoint, RP design skills and user instructions are
fork/Andrew-owned. Not read: gate internals, release-deploy, doc-review internals,
Codex `openai.yaml`. No review, peeragent call or scenario test run — text, repo
and git facts only. Enforcement: all in-scope rules are reader compliance; tests
(`convert-review-weight.test.sh`, portability inventory) are structural.

| ID | Sev. | Finding | Recommendation / would authorize | Owner |
| --- | --- | --- | --- | --- |
| QVC-R/METH-001 | **major** (conf. medium) | Independent-review routing is set by item kind, chosen by size/cohesion (`scope/SKILL.md:111-114`; `fix/SKILL.md:158-181`); standalone stories never get an independent reviewer (`review/SKILL.md:84-87,115-117`). The fork's consequence rule is conditional — "use the feature review boundary *when independence is warranted*" (`CONVENTIONS.md:27-30`), reworded at `build-process.md:119-122` and `quality-checkpoint/SKILL.md:81-84`. A one-line authority/stop-rule edit gets only the author's inline check. Counter: agents already scope such work as features; cheap standalone stories are deliberate; release checkpoints rare | (b) Fork-only operative list used at scope/fix time: authority, required checks, completion/stop criteria, grounding or cross-skill contract changes are scoped as a feature (possibly one-story) regardless of size. Authorizes rewriting `CONVENTIONS.md:26-36` only. (c) upstream scope-table criterion optional | fork (c: upstream) |
| QVC-R/METH-002 | **major** (conf. medium-high) | Covering-review reuse is undecidable: upstream receipt template (`substrate-side-effects.md:81-91`; `review/SKILL.md:243-244`) lacks reviewed range, reviewer class and fix-verification fields that fork consumers require (`quality-checkpoint:86-90`; `CONVENTIONS:34-35`). "Stale evidence is not a pass" (`CONVENTIONS:35-36`; `build-process:184-187`; `quality-checkpoint:162`) vs "a changed hash alone does not require another pass" (`quality-checkpoint:92-93`; `build-process:120-121`), bridged only by author-judged "materially uncovered". Instance: `6419b3bc` after review record `c1827823` added new contract text (candidate eligibility, AR probe placement, research-tag exclusion, capped doc-review refresh) and closed on verification alone. Resume "from existing receipts" (`quality-checkpoint:96-97`) presumes fields the template lacks | (b) Fork receipts name `<base>..<head>`, reviewer class/path and fix commits; each post-review change to a consequential file gets a one-line coverage classification (pass / named-finding fix verification / uncovered → normal delivery); "stale" = unclassified post-review change. Authorizes CONVENTIONS and quality-checkpoint §2 receipt-field edits. (c) upstream template; (d) authorized experiment: same-reviewer delta confirmation on fix diffs that add normative text | fork (c: upstream) |
| QVC-R/METH-003 | **major** (facts high; materiality medium) | The assumed human PR gate is not operating and changes go live before it: instructions require PRs and manual merge (`~/dev/CLAUDE.md`; `CONVENTIONS:26-27`), but `main`/`origin/main` last moved 2026-06-09 (`86204084`), HEAD is 63 first-parent commits ahead incl. every QVE-era contract change, no PR open; the marketplace source is the working tree, so commits are live pre-merge. The agent review lane is the only independent check. Counter: solo maintainer adjudicates packets in real time; branch may be intended as one later PR | Andrew chooses: (a) retain and document agent review as the gate; (b) PR per arc with Andrew reviewing consequential contract diffs; (c) point the marketplace at `main` or a release worktree | operator + fork |
| QVC-R/METH-004 | minor | "Standard = one pass" restated ≈10 places (`review/SKILL.md:65-89,221-237,306-310`; `principles/SKILL.md:399-427,461-469`; `advisory-review.md:13-24`; `deep-review.md:15-27`; `substrate-side-effects.md:36-46`; `autopilot:330-347`; `implement-orchestrator:185-196`; `prompt-context.py:114-115`; fork `build-process:114-117`; user rule). Covering-review contract thrice in fork files with different triggers; CONVENTIONS forbids a "file-triggered peer pass" that no longer exists (removed `4575547d`) | One fork statement in build-process Delivery; quality-checkpoint keeps release reconciliation; CONVENTIONS keeps repo triggers + link; user rule shrinks to reviewer preference + "follow the workflow's weight". Authorizes those fork files and Andrew's instructions | fork / Andrew |
| QVC-R/METH-005 | minor (uncertain) | Independence stops at detection: author adjudicates proposals (`principles/SKILL.md:471`; `review/SKILL.md:205-219`), verifies own fixes and judges materiality; rejected proposals never surfaced to Andrew; lenses are code-oriented (`review-lenses.md`; `deep-review.md:73-103`) with no prompt-ware lens (authority, stop rules, cross-skill conflicts, cross-host invocation, resume). Counter: receiver ownership prevents reviewer-driven over-engineering | Prompt-ware lens list in reviewer packet (CONVENTIONS or `.agents/rules`); list rejected/downgraded blockers in completion summary for consequential changes; scenario-walk fix verification as an experiment | fork |
| QVC-R/METH-006 | minor | Duplicate passes: single-feature autopilot gets feature review + final completion review of the same bundle (`autopilot:313-318`; 10–30 min each, `models.md:50-52`); methodology controller as feature gets feature review + fresh assessor though methodology-review allows one pass to serve both (`SKILL.md:155-156,242-243`) | Upstream note, low priority | upstream |

Incidental defects: fork `feature-design/SKILL.md:194` and `epic-design/SKILL.md:231`
cite "Cross-Model Advisory Review policy (Part IV)" (actual title "Risk-Driven
Advisory Review", `principles:388`), a non-existent `peer-review` loop (peeragent
0.8.1 exposes `peer`), and skip rather than fall back to a fresh-context reviewer
(`principles:450`); `models.md:202` Codex "model auto-selected" cannot honor
`deep-review.md:43-47` precedence and receipts can't show the model (upstream);
`docs/project-navigation.md:60-68` omits the fork's `models.md` additions (+22 lines
vs `upstream/main`), against `AGENTS.md:25-26`.

Scenario walk: small prompt edit → inline lane (METH-001); consequential contract
change → sound once routed as feature; changed after review → author decides
(METH-002); reviewer unavailable → consistent labeled fallback or block; Codex vs
Claude driving symmetric except Codex model pinning; disputed findings → author
adjudicates, no escalation (METH-005); resume → receipts lack baseline (METH-002).
Simpler baseline differs mainly in who judges post-review materiality.

Sibling implications: QVC-E — METH-002 instances the root's shared evidence
question; check AR verification records and doc-review reports for baselines; one
owner for "missing/stale ≠ pass". QVC-S — citation gate runs only in rare release
checkpoints and PRs are inactive, so judge warnings inside engagements.
Evidence requests: LLM-judge self-preference magnitude and extension to
self-adjudication/self-verification; cross-model vs same-model fresh-context
detection; human review practice (reviewer count; stale-approval dismissal,
Gerrit copy rules; material vs trivial classification); prompt diff size vs
behavioral impact; local experiment (replay `6419b3bc` + seeded authority edit,
author self-verification vs Codex delta confirmation).

Child exit: **awaiting decision** — majors METH-001–003; evidence requests 1–3 pending.

## Operator decision — intended-use weighting (2026-10-19)

Andrew stated methodology-review's intended jobs: (1) review domain methods built
with the research skills, over time — motivating case the data-science component
of project-blueprint; (2) analyze a whole process suite and each component; (3)
pair with `research-pipeline:scout` to surface alternatives and improvements.

Root observation offered for context (not a child finding): program/component
shape fits job 2; scout is positioned as a gap-filler rather than a discovery
front end (job 3, untested); the skill models a convergent bounded loop with no
longitudinal reopen or prior-review comparison guidance (job 1 — this QVC/QVE
comparison had to invent its blind-then-compare method); all runs so far are
skills-v2 reviewing itself.

**Decision (Andrew, "i like option 1"):** keep QVC's scope to its three topics.
Amend the charter criteria — before any root assessment — so the root
integration, fresh assessor and decision packet weigh proposals by their effect
on those three jobs (e.g. burden of evidence ceremony on a domain review).
Child assessments predate this criterion and are not re-run. Follow-on: a pilot
of methodology-review + scout on project-blueprint's data-science component,
parked for later; it requires Andrew to place project-blueprint in scope and is
not authorized by this decision.

## Root integration — round 1 (2026-10-19)

Inputs: the three child returns above (baseline `e3e2e070`), the supplementary
research `.research/analysis/campaigns/qvc-review-evidence/parent.md` (verified
except one lead-corrected N3 rewording not independently re-read; see the
research story), the intended-use weighting decision, and root spot-checks.
Severities below are the children's; the root records counter-evidence but does
not reclassify — that is the fresh assessor's job.

### Root spot-checks of child facts
- QVC-R/METH-003 confirmed: `main` = `origin/main` = `86204084` (2026-06-09);
  63 first-parent commits ahead at baseline; last PR #48 merged 2026-06-09;
  `known_marketplaces.json` source is the working-tree directory.
- QVC-E/METH-001 "release-deploy never invokes quality-checkpoint" confirmed by
  grep; nuance: the documented pipeline runs quality-checkpoint as a separate
  operator step before `release-deploy`, so it is operator-sequenced rather than
  unreachable.
- QVC-R/METH-002 instance (`6419b3bc` after review record `c1827823`): the
  commit closed on accepted-fix verification, but QVE's round-3 fresh assessor
  read the `4575547d→6419b3bc` correction diff. No escape is shown for that
  instance; the general mechanism stands.
- QVC-R/METH-001 instance found: standalone story
  `story-fix-research-orchestrator-codex-discovery` (`c7d0de75`) changed a
  cross-plugin invocation policy through the inline lane; it carried a
  regression test and no harm is known.

### Deduplication (origin IDs retained)
| Cluster | Members | Note |
| --- | --- | --- |
| C1 Enforcement and completion evidence (root shared question) | QVC-E/METH-001 (major), QVC-E/METH-006, QVC-S/METH-002, QVC-R/METH-003 (major) | Different faces of one question; see interactions |
| C2 Review routing and reuse | QVC-R/METH-001 (major), QVC-R/METH-002 (major) **alias** QVC-E/METH-005, QVC-R/METH-005, QVC-R/METH-006 | E-005 and R-002 are the same mechanism; R-002 owns it |
| C3 Duplicated contracts and prose burden | QVC-E/METH-002 **overlaps** QVC-R/METH-004; QVC-S/METH-002's triplicated rule is an instance | Children disagree on timing (E defers, R consolidates now) |
| C4 doc-review as a correction loop | QVC-E/METH-003, QVC-E/METH-004 | |
| C5 Citation signal | QVC-S/METH-001…004 | |

### Cross-child interactions
1. **R-003 removes E-001's main counterargument.** E-001's counterargument was
   that manual PR merge backstops reader-compliance rules. Under R-003 that
   backstop is not operating, and E-006 shows the actual ship path
   (working-tree marketplace + `bump-version.sh`) runs neither review nor
   tests. Combined: on the current path, the agent's own review lane and reader
   compliance are the only quality controls between a commit and live use.
2. **R-001 × C3/C5:** small prose edits — the class where QVC-S found adjacent
   contract drift surviving a reviewed edit — route to the inline lane by size.
3. **E-004 × R-001/R-003:** doc-review's autonomous Critical/High edits to
   foundation docs are not routed through review and, via the working-tree
   marketplace, are live on commit.
4. **S-004 × R-003/E-006:** gate-level citation advisories surface only in
   release checkpoints, which this repo rarely runs; their only practical
   consumer is the in-engagement lint.

### Live evidence from this round's own research loop
The supplementary engagement exercised ARD's correction loop for real:
attempt-2 adversarial read → NEEDS-REVISION; revision introduced N1 by adopting
the reader's own suggested wording as source fact; a second independent read
caught it (and N2); the bounded correction introduced N3; the targeted check
caught that. Demonstrated here: (a) correction passes can introduce errors,
including verifier-originated ones; (b) each independent re-read caught
material errors the reviser missed; (c) ARD's surface-the-second-NEEDS-REVISION
rule worked and produced an operator decision. This is n=1 and is evidence for
C1/C2 (independent checks earn their cost on consequential claims; author
self-verification of fixes is weak), not a general measurement.

### Research mapping (implications, not measured effects on this workflow)
- **C2 / cross-model preference.** Independent checking over pure self-review is
  supported; a different model is not shown to be the active ingredient — a
  held-out judge grading without references still favoured similar models
  {14}; reference guidance gave the largest reduction in MT-bench's
  judge-prompt comparison, with chain-of-thought also reducing failures {11},
  {13}. Retaining the cross-model preference is cheap; grounding review in
  recorded criteria or executable scenarios is untested but is where the
  evidence points (bears on R-005, E-001).
- **C2 / reviewer count and routing.** A step to a second check matters more
  than further reviewers, with the inspection study's own non-significant
  abstract caveat {18}; reviewer count varies with perceived risk in practice
  {19}{20}. Supports routing by consequence (R-001) rather than more passes
  (R-006).
- **C2 / covering-review reuse.** The sources treat reuse as a policy choice
  (approve-with-bounded-follow-ups {24} vs diff-tied dismissal {25}); neither
  is measured. Recording what a review covered is the documented practice that
  makes reuse checkable (supports R-002 option b, not mandatory re-review).
- **C5 / citation advisories.** Warnings delivered outside the work context were
  ignored, while review-time findings on changed material were acted on at high
  rates (Facebook's diff-time data; Google's are socially enforced at approval);
  blocking is reserved for effectively zero-false-positive checks; thresholds
  require a stated false-positive definition; high dismissal can be correct.
  Supports S-002 (mechanical exit on broken chains, which are ~zero-FP), S-004
  (gate-level pattern reports lack a consumer), and an action-measured S-001
  experiment. Transfer to prose linters and agent consumers is untested.
- **C1 / E-001.** Agent-evaluation guidance favours checking resulting state and
  calibrated graders {7}; the new research adds no measurement of prompt-ware
  regression suites. E-001's experiment remains the deciding evidence.

### Intended-use weighting (operator criterion)
- Job 1 (domain methods reviewed over time): C3's prose burden and the
  missing longitudinal reopen/compare guidance weigh against adding more rules;
  proposals that add mechanism (fields, flags, fixtures) rank above more prose.
- Job 2 (suite + components): the program/coordinated shape worked in QVE and
  QVC; no finding threatens it.
- Job 3 (scout pairing): untested; the parked pilot is the deciding evidence.

### Comparison with QVE (formed after the blind child returns)
| Topic | QVE | QVC | Relationship |
| --- | --- | --- | --- |
| Checkpoint correctness | Major E/METH-001 (zero items ≈ ready), E/METH-002 (invalid `work-view` flags, no `gate-infra`); fixed and verified | Not re-raised; QVC-E notes the rewrite fixed real defects | QVC confirms QVE's fixes hold |
| Enforcement | Accepted prose rules at each owner (E/METH-003, I01) | E-001 (major): those rules are compliance-only with no durable behavioral evidence; QVE's forward scenarios were temporary | New; challenges QVE's remedy type, not its diagnosis |
| PR gate / ship path | Not raised; O-1 parked release duplication | R-003 (major), E-006 | New |
| Review routing | R/METH-001: stale `/peer-review`; rejected file-triggered peer gates | R-001 (major): routing by size, not consequence | Different angle; QVC agrees file triggers are wrong but finds the consequence rule conditional |
| Covering-review reuse | Adopted "changed hash from verified fixes does not invalidate standard review" | R-002 (major) / E-005: reuse undecidable without recorded range | Direct tension with a QVE-adopted rule |
| Duplication | Not raised (QVE added several of the restatements) | E-002, R-004 | New; partly a consequence of QVE's remedy |
| doc-review | Minor obs 3: autonomous edits under generic coverage rule | E-003, E-004 | Agreement, QVC broader (stale target model, unpersisted cap) |
| Citation noise | S/METH-001 retained; matcher unchanged | S-001: experiment before any matcher change | Agreement on minor; QVC adds precision measurement on corpus (0/13 true) |
| Warn-only lists | I04 parked (`idea-citation-advisory-coverage`) | S-003 | Agreement; QVC adds silently-clean fabricated-campaign demonstration |
| Exit-code rule | Prose "exit 0 is not a pass" adopted | S-002: make it mechanical | Refinement |

Pattern: QVE assessed whether contracts **execute correctly** and fixed them
with clarified prose; QVC asks whether the rules are **enforced at all** and
what they cost, and finds the dominant risk outside the documents (PR gate,
ship path, routing at scope time). QVC's majors are largely invisible to a
contract-reading review. Limitation: QVC children read the post-QVE files, so
some findings (duplication) are partly reactions to QVE's remedies.

### Root status
Majors carried to the fresh assessor: QVC-E/METH-001, QVC-R/METH-001,
QVC-R/METH-002 (alias QVC-E/METH-005), QVC-R/METH-003. No operator decisions on
findings yet; no remedies authorized. Root round 1: integration done; fresh
whole-scope assessment next (Codex via peeragent, fallback fresh Claude).
Assessor limitation to record: Codex drove QVE, so it partly assesses its own
earlier remedies.
Fresh assessor dispatched 2026-10-19: Codex `gpt-6.1-sol` high via peeragent,
job `20261019T144048Z-e4a7e91b`, read-only, prompt does not prescribe a verdict.
Job success will mean only that the worker finished.

## QVC parent assessment 1 (2026-10-19)

Codex `gpt-6.1-sol` high, peeragent job `20261019T144048Z-e4a7e91b`, terminal
`success` (worker finished; the substantive outcome is below). Assessed HEAD
`b875b48e`; product content unchanged from `e3e2e070`. Report preserved verbatim:

> **QVC root round 1 assessment — 2026-10-19**
> 
> **Outcome: Awaiting decision.** Two distinct major findings remain unresolved: QVC-R/METH-002 is supported; QVC-R/METH-003 requires evidence. No remedies were authorized or applied. No repository files were changed, staged or committed.
> 
> Assessed baseline and coverage
> 
> HEAD was `b875b48ea2b1e1acad16b3110846531c214521e5`. Product files are unchanged from the children’s `e3e2e070` baseline, identified by the charter as product-equivalent to `a36137fa`.
> 
> I assessed all three topics, their interactions and all seven charter scenarios. I applied Andrew’s intended-use weighting: reviewing domain methods over time, reviewing suites and components, and pairing methodology-review with Scout. The first and third jobs remain untested outside this repository; that limits effectiveness claims without establishing a methodological defect.
> 
> I read the [root record](/Users/andromedus/dev/skills-v2/.work/active/features/feature-claude-methodology-repeat.md), methodology-review protocol and both references; build-process and research-composition; quality-checkpoint, gate-citations, doc-review and gate-docs extension; review routing, weights, receipt template and review lenses; relevant scope, fix, autopilot and release-deploy sections; verification-record and relevant AR orchestrator sections; scripts, workflows and selected Codex metadata.
> 
> Research inputs were the [supplementary synthesis](/Users/andromedus/dev/skills-v2/.research/analysis/campaigns/qvc-review-evidence/parent.md), its engagement record, evaluation and verification conclusions, selected load-bearing attestations, and `quality-feedback-loops.md`. I recovered QVE’s full controller through Git, including its final assessment and the `6419b3bc` correction diff.
> 
> **Independence limitation:** Codex drove QVE. This assessment therefore challenges some rules adopted under my model’s earlier direction. I judged those rules from current evidence; QVE’s prior acceptance supplies neither a presumption of correctness nor a reason to reject QVC.
> 
> Checks run
> 
> | Check | Result |
> |---|---|
> | ARD conformance | **57/57 passed** |
> | Companion resolver test | Passed |
> | RP portability and AR metadata tests, default Python | Both failed: missing PyYAML |
> | Same tests using the existing scratch PyYAML environment | Both passed; no installation required |
> | Current corpus lint, without URL checks | 51 files, 443 citations, **0 broken, 0 thin** |
> | Lint severity thresholds: high, medium, low | All exited 0 |
> | Advisory output | 273 patterns; 5 omitted-confidence notices; no unbound campaigns |
> | Product diff since child baseline | Empty |
> | Working tree and `git diff --check` | Clean when checked |
> | Git state | Local `main` and `origin/main` remain `86204084`; HEAD is 77 first-parent commits ahead |
> | Live GitHub PR query | **Blocked:** could not connect to `api.github.com` |
> 
> The current advisory total includes newly added research and verification records. It cannot be compared directly with the child’s historical 13-warning sample as a precision measurement.
> 
> An attempted scratch replay of the historical corpus stopped at its extraction-path guard before extraction or lint execution. I therefore **did not independently reproduce** the historical 0/13 true-defect classification. I did inspect the matcher, suppression rules, canonical status handling and conformance checks.
> 
> Findings
> 
> “Persistent” below means carried from the child returns; this is the first parent assessment. Major counts deduplicate QVC-E/METH-005 into QVC-R/METH-002.
> 
> | ID | Evidence status | My severity | Rationale |
> |---|---|---|---|
> | **QVC-E/METH-001** | Supported, narrowed | **Minor** | A rerunnable behavioral regression suite is absent, but QVE retains behavioral results and QVC’s research loop supplies operational evidence; lack of automation alone does not establish material failure or justify a mandatory harness. |
> | QVC-E/METH-002 | Supported | Minor | Repeated contracts are directly observable; consequential maintenance or operator burden has not been demonstrated. |
> | QVC-E/METH-003 | Supported, narrowed | Minor | Doc-review’s report omits baseline and iteration state, weakening resume; resetting the cap is a risk rather than observed behavior, and adjustable/default iteration counts need not have universally measured optimal values. |
> | QVC-E/METH-004 | Supported | Minor | Doc-review combines autonomous contradiction repair with an outdated planning model; unintended changes to intent are plausible, but no such correction was demonstrated and higher-level authority constraints still apply. |
> | **QVC-E/METH-005** | Supported | **Major; alias R/METH-002** | Missing review-input anchors are the same evidence-reconstruction problem as R/METH-002, counted once. |
> | QVC-E/METH-006 | Supported, narrowed | Minor | `bump-version.sh` contains no review/test gate or branch guard; this does not erase the applicable delivery obligations or establish that installed hosts consume every edit immediately. |
> | **QVC-R/METH-001** | Supported, narrowed | **Minor** | Kind-based routing leaves consequentiality to judgment, but the proposed universal trigger list is an alternative policy; the actual invocation-policy fix had reproduction and regression evidence, with no demonstrated need for another reviewer. |
> | **QVC-R/METH-002** | Supported, narrowed | **Major** | Required reuse evidence is not captured by the generic receipt template, making reliable scope reconstruction depend on exceptional record keeping; this materially threatens current-evidence decisions during ordinary resume. |
> | **QVC-R/METH-003** | **Uncertain—needs evidence** | **Major uncertainty** | The review/publication boundary remains consequential, but stale local refs do not prove current PR absence, and installed-cache evidence contradicts the claimed automatic exposure of every working-tree commit. |
> | QVC-R/METH-004 | Supported, narrowed | Minor | Duplication exists; measured burden does not. Keeping an explicit prohibition against duplicate file-triggered passes is not necessarily stale merely because the old trigger was removed. |
> | QVC-R/METH-005 | Uncertain—needs evidence | Minor | Author adjudication is explicit and rejected proposals have a durable receipt field; evidence does not establish that this allocation of authority causes material failures. |
> | **QVC-R/METH-006** | **Withdrawn with evidence reason** | None | Feature, aggregate-completion and methodology assessments have different contracts, and methodology-review expressly permits combined coverage; overlapping inputs do not establish redundant assessment. |
> | QVC-S/METH-001 | Supported, narrowed | Minor | The matcher ignores same-line anchors and source-direct status; its exact historical false-positive rate and the recall cost of suppression remain unverified here. |
> | QVC-S/METH-002 | Supported | Minor | Default exit zero requires JSON interpretation, but parsing is already an explicit adapter duty; an exit threshold would supplement that duty rather than enforce the whole gate. |
> | QVC-S/METH-003 | Supported | Minor | The consumer reporting contract omits warn-only lists; current exposure is five confidence omissions and zero unbound campaigns. |
> | QVC-S/METH-004 | Supported, narrowed | Minor | Gate advisories lack a required disposition consumer, but post-engagement edits remain a credible use; removing the signal is not yet justified. |
> 
> **Counts:** two unresolved distinct majors—one supported, one uncertain. Zero new independent major findings; zero accepted-pending remedies; zero verified resolutions; zero operator-retained or deferred major risks. Twelve additional findings remain minor. One finding is withdrawn.
> 
> Evidence-based corrections and withdrawals
> 
> - **R/METH-002’s alleged QVE escape is refuted.** QVE’s final assessor explicitly read the `4575547d→6419b3bc` correction diff. This instance does not demonstrate unreviewed closure. The general receipt gap remains supported.
> - **“Every commit is live” is refuted as a blanket claim.** Claude’s installed-plugin registry identifies cached copies from `c7d0de75`; its Research Pipeline cache lacks methodology-review. A directory marketplace identifies a source, not sufficient proof of immediate installed-host execution.
> - **“Checkpoint unreachable” is rejected.** The build process explicitly places quality-checkpoint before release-deploy. It is operator-sequenced.
> - **R/METH-006 is withdrawn** for the distinct-contract reason above.
> 
> On the QVE covering-review rule, I retain the distinction between verified accepted fixes and newly uncovered contracts. Research does not establish that every changed hash requires another review. **R/METH-002 supports better evidence receipts, not mandatory re-review of all fixes.**
> 
> Seven-scenario assessment
> 
> | Scenario | Assessment |
> |---|---|
> | 1. Research, delivery and checkpoint succeed | Contracts compose coherently; the current research engagement itself has not fully satisfied verification. No live release was exercised. |
> | 2. Required check fails or is missing | Consumers explicitly prohibit treating execution, artifacts or zero items as approval; the current engagement visibly preserves its failed verification state. |
> | 3. Output changes after review | Reuse can be legitimate, but ordinary receipts inadequately anchor assessed inputs and subsequent corrections: R/METH-002. |
> | 4. Correction limit exhausted | AR and methodology-review expose unresolved exits; doc-review has a cap but weak durable iteration state; thorough delivery review has no numeric cap. |
> | 5. Interrupted or cross-host resume | Root and research records support reconstruction; doc-review loop state and generic delivery receipts are weaker. Installed/source divergence also limits assumptions about active instructions. |
> | 6. Small versus consequential prompt edit | Judgment-based escalation exists; size alone is insufficient, but evidence does not justify requiring independent review for every listed contract edit. |
> | 7. Real and spurious citation warnings | Integrity checks and advisory patterns are mechanically separate; no broken/thin findings appeared. Warning precision and fabricated-claim recall remain unmeasured here. |
> 
> Cross-child interactions
> 
> - **Confirmed:** weak receipt capture combines with changed-input checks to make resume costly or uncertain. A small receipt improvement serves longitudinal and component reviews more directly than additional repeated policy prose.
> - **Confirmed:** this research engagement shows corrections can introduce new errors, including verifier-originated wording. Independent rereads detected them. This supports explicit correction evidence; it does not prove a universal need for repeated delivery review.
> - **Rejected as overstated:** R/METH-003 does not establish immediate publication, so it cannot remove every counterargument to E/METH-001 or prove that reader compliance is the sole operating control.
> - **Confirmed, bounded:** doc-review’s autonomous edits can invalidate earlier scans and create delivery-review obligations. No unauthorized intent change was observed.
> - **Confirmed:** engagement lint is a practical advisory consumer. Rare release checkpoints reduce the observed value of gate-level reporting without proving it useless.
> - **Not established:** more automation, more reviewers or fewer warnings would improve domain-review outcomes enough to earn their cost.
> 
> Minor observations and intended-use weighting
> 
> The strongest low-cost candidate is a compact review receipt containing assessed base/head, reviewer path/class, weight, findings and accepted-fix verification. Adding another review loop is not supported by the available evidence.
> 
> Doc-review’s report-state omissions and stale discovery assumptions deserve bounded attention. Its ownership needs clarification before broad autonomous foundation corrections are relied upon.
> 
> Keep the cross-model preference as a preference. The supplied research does not establish cross-model superiority for this workflow. Likewise, external warning thresholds should not be imported into citation lint without matching definitions and local measurements.
> 
> The root’s longitudinal and Scout-pairing observations remain pilot questions. The protocol already has resume and changed-evidence rules; absent dedicated longitudinal wording is not itself a major defect.
> 
> Coverage limits and required next step
> 
> I did not run live doc-review, quality-checkpoint, release-deploy, model-based scenario evaluations, publication, or an adopter-project pilot. I did not inspect every gate, hook, metadata file, research source or specialist passage, and did not re-fetch sources. No new external claims are introduced.
> 
> The [research engagement](/Users/andromedus/dev/skills-v2/.work/active/stories/story-research-qvc-review-evidence.md) remains **verification incomplete**: its final targeted adversarial check returned NEEDS-REVISION; the lead corrected N3 without an independent reread. This assessment does not close that owner-controlled obligation.
> 
> The GitHub connection failure prevented current PR-state verification. I stopped further checks as instructed; the child/root assertion that no PR is open remains unverified.
> 
> **Exit: Awaiting decision.** Andrew must adjudicate the supported receipt gap and clarify the intended review/publication boundary. Recommended packet: authorize compact receipt fields without adding a review pass; clarify the operating boundary after PR evidence is available; defer broader harness and policy expansion pending measured need.
> 
> **Next required step:** the root driver records this report as completed assessment round **1 of 5**, then presents that decision packet while preserving the GitHub blocker and outstanding N3 verification obligation.

### Host adjudication

- **Accepted** the assessor's severity calls as the round-1 parent result: two
  distinct unresolved majors — QVC-R/METH-002 (supported; alias QVC-E/METH-005)
  and QVC-R/METH-003 (uncertain, needs evidence). QVC-E/METH-001 and
  QVC-R/METH-001 reclassified minor with evidence rationale; QVC-R/METH-006
  withdrawn (distinct review contracts). The root does not override these.
- **Evidence supplied for QVC-R/METH-003 after the assessment** (local, not
  external): `gh pr list --state open` on `andrewclark88/skills-v2` returns 0;
  the newest PR is #48, merged 2026-06-09. Exposure: the registry pins user-scope
  installs to cache `c7d0de75` (the assessor's point stands for the registry),
  but in this repository's Claude Code sessions skills execute from the working
  tree — `agile-workflow:scope`/`park` launched from `plugins/…` in the checkout,
  and `research-pipeline:methodology-review` is available although absent from
  the cached 0.2.0. So the documented PR gate is not operating, and working-tree
  edits are live at least for sessions in this repo; behavior in other projects
  is unverified. Presented to Andrew as decision-relevant evidence; the
  assessor's classification is not rewritten.
- **Incidental (outside charter):** `.claude/settings.json` enables
  `workbench@nklisch-skills`, while `AGENTS.md`/`.claude/CLAUDE.md` say not to
  activate Workbench here. Noted for Andrew; no action taken.
- Research obligation unchanged: `story-research-qvc-review-evidence` is
  verification incomplete (N3 lead-corrected, not independently re-read).

**Root round 1 complete: 1 of 5.** Outcome: **Awaiting decision.** Next: one
decision packet to Andrew, majors first.

## Operator decisions — round 1 packet (Andrew, 2026-10-19)

| Finding(s) | Decision | Authorizes | Item |
| --- | --- | --- | --- |
| QVC-R/METH-002 (major; alias QVC-E/METH-005) | **Accept** "Add receipt fields" | Fork-only change to `.work/CONVENTIONS.md` and `quality-checkpoint` §2: receipts record reviewed `base..head`, reviewer class/path, weight, findings, accepted-fix verification, and a one-line coverage classification of post-review changes to consequential files. No added review pass; no upstream template change | `feature-qvc-review-receipts` |
| QVC-R/METH-003 (major) | **Accept** "PR per arc" | Resume PRs: open one at the close of each arc, starting with this long-lived branch; Andrew reviews diffs of consequential contract files before merge. Docs stay as written. Opening/pushing a PR is still confirmed with Andrew at the time | this arc's close |
| QVC-S/METH-002, QVC-S/METH-003, gate-citations incidentals | **Accept** "Citation gate tidy-up" | Scope into one fork-only follow-up feature | `feature-qvc-minor-remedies` |
| QVC-E/METH-003, QVC-E/METH-004 | **Accept** "doc-review state + scope" | Report fields; mechanical-only autonomous fixes with foundation-doc contradictions routed to the operator; retarget retired roadmap checks | `feature-qvc-minor-remedies` |
| QVC-E/METH-002, QVC-R/METH-004 | **Accept** "Consolidate duplicate rules" | One canonical fork statement with one-line local pointers; drop `research-composition` restatements; weigh by domain-review burden | `feature-qvc-minor-remedies` |
| QVC-E incidentals I-2, I-6; QVC-R incidentals (Part IV/`peer-review` refs, undocumented `models.md` patch) | **Accept** "Repo hygiene" | Declare PyYAML for tests; branch guard in `bump-version.sh`; fix stale references; document the fork patch | `feature-qvc-minor-remedies` |
| QVC-S/METH-001 | **Experiment** "Citation matcher precision" | Scratch-only fixtures; no repo edits | run now |
| Research N3 | **Experiment** "Close research N3" | One independent re-read of the N3 lines | run now |
| QVC-E/METH-001 (minor) | Not selected | Scenario harness not authorized; parked blueprint pilot remains the evidence path | — |
| QVC-R/METH-001, QVC-R/METH-005, QVC-S/METH-004 (minor) | Not selected | Retained as minor observations; no change | — |

Partial authorization only: each item's operative brief is limited to the row
above. Next: deliver both features through normal design → implement →
review; record experiment results; then allocate root round 2 for a fresh
whole-scope reassessment on the changed baseline.

Research update (2026-10-19): `story-research-qvc-review-evidence` closed
**verified** after an independent N3 re-read (APPROVED). Root correction to the
integration's research mapping (C2): the MT-bench "reference guidance" was the
judge's own independently generated answer, not external ground truth, so it
weakly supports "grounding" in recorded criteria or executable checks; that
extension remains untested.

## Experiment result — QVC-S/METH-001 citation matcher precision (2026-10-19)

Scratch-only, as authorized; repo unmodified. Artifacts (temporary, not
retained by the repo): `/private/tmp/claude-501/qvcs-exp/` — fixture builder,
52 labeled lines (20 P / 29 N / 1 excluded / 2 scored both ways), scorer,
variant diff, per-run outputs.

| Run | Fixture precision | Fixture recall | Flags at `e3e2e070` | Flags at `f2fa9439` |
| --- | --- | --- | --- | --- |
| Current matcher | 0.40 | 0.90 | 10 | 174 (112 attestation) |
| A: tier + any cited line suppressed | 0.77 | 0.50 | 1 | 59 |
| B: tier + cited line suppressed only if the cited attestation contains the token | 0.84 | 0.80 | 1 | 60 |

- Corpus noise grew 10 → 174 version flags with the new research attestations;
  the real corpora contain no observed true positives, so field recall cost is
  unmeasurable here. QVC-S/METH-001's "worsens as attestations accumulate" is
  now demonstrated on this corpus.
- Tier suppression removed 112/115 real suppressed flags with no observed
  recall loss; A loses all cited-but-unsupported fabrications (8 fixtures); B
  loses only coincident-token cases (2). All runs miss `Version 3` (case) and
  dotless `vN` — matcher-shape gaps. Residual noise under A/B is mostly section
  refs, arXiv IDs, percentages, decimals and model names (heuristic triage).
- Conformance 57/57 for all variants; the suite cannot distinguish them (no
  negative fixture).
- Experimenter recommendation (synthetic fixtures; not field measurement):
  tier suppression; if citation-line suppression, token-aware form B; ship any
  proposal with positive/negative conformance fixtures.
- Ownership: the kernel is agentic-research (upstream ARD); the fork policy keeps
  the kernel unchanged. Any change is an upstream proposal or a documented
  fork patch — a new operator decision for the round-2 packet. Not authorized.

## Operator decisions — follow-ups (Andrew, 2026-10-19)

- **Matcher ownership:** "let's grab our own version — nathan hasn't been as
  focused on this stuff anymore, so it's probably best we just own it
  ourselves." The fork takes ownership of `agentic-research`, beginning with the
  citation matcher (tier suppression + token-aware cited-line suppression,
  variant B) shipped with positive/negative conformance fixtures; ownership
  statements in `AGENTS.md` and `docs/project-navigation.md` roll forward.
  Scoped as `feature-ar-fork-citation-matcher`. Interpretation (whole plugin vs
  lint only) stated to Andrew for correction.
- **Experiment artifacts:** not retained as an archive (Andrew: "we don't need
  them"). Their durable value is carried as conformance fixtures in the matcher
  feature; the summary above remains the record.
- **Proceed:** design `feature-qvc-review-receipts` now and work toward this
  branch's PR (push/PR still confirmed at the time).

## Delivery of round-1 decisions (2026-10-19)

| Decision | Item | Outcome |
| --- | --- | --- |
| QVC-R/METH-002 receipts | `feature-qvc-review-receipts` | done — Codex review (Request changes → 1 blocker, 1 important fixed `7eb12d33`); receipt in item |
| Minor bundle (S-002, S-003, E-002/R-004, E-003/E-004, hygiene) | `feature-qvc-minor-remedies` (4 checkpoints) | done — Codex review (2 doc-review blockers, 2 important fixed `3b1a9b6a`); receipt in item |
| Fork ownership + QVC-S/METH-001 matcher | `feature-ar-fork-citation-matcher` | done — Codex review (1 important fixed `d8afde36`); conformance 57 → 77; corpus version flags 174 → 60 |
| QVC-R/METH-003 PR per arc | this arc's close | pending — PR to be opened after round 2, confirmed with Andrew |

Parked during delivery: `idea-architecture-roadmap-links`, `idea-version-matcher-shape`.

## Root round 2 allocation (2026-10-19)

Changed product baseline: `c6c2b6fb` (from `e3e2e070`). Round 2 of 5 allocated;
1 complete. Fresh whole-scope assessor: Codex via peeragent (fresh job). Scope:
the full QVC charter (three topics, interactions, seven scenarios, intended-use
weighting), verifying remedies for decided findings and assessing new or
persistent findings on the changed baseline. Not prescribed a verdict.

## QVC parent assessment 2 (2026-10-19)

Codex `gpt-6.1-sol` high, peeragent job `20261019T160106Z-cd5ebb2b`, terminal
`success` (worker finished; substantive outcome below). Assessed HEAD `10ce06bb`,
product-equivalent to the allocated baseline `c6c2b6fb`. Report preserved verbatim:

> **QVC root round 2 assessment — 2026-10-19**
> 
> Assessed HEAD `10ce06bb9804a07765c327002f5ef95cb419688e`, product-equivalent to allocated baseline `c6c2b6fb`. Inspected the product changes from `e3e2e070`, all three topics, their interactions, seven scenarios, and Andrew’s intended-use weighting. No repository files were changed, staged or committed; scratch artifacts remain under `/tmp/qvc-r2-checks`.
> 
> **Independence limitation:** Codex reviewed all three delivered features in separate jobs and assessed round 1; Codex also drove QVE. This assessment has fresh context but shares that model lineage. Conclusions below rest on inspected evidence.
> 
> I read the [root record](/Users/andromedus/dev/skills-v2/.work/active/features/feature-claude-methodology-repeat.md), protocol and references, three delivered features and four checkpoint stories, changed product surfaces, relevant unchanged delivery/research contracts, verified research synthesis, engagement record, and quality-feedback brief. Unaffected child assessments were reused; changed remedies and interactions were reassessed.
> 
> **Checks run**
> 
> | Check | Result |
> |---|---|
> | ARD conformance | **77/77 passed** |
> | Generated catalog consistency | Passed |
> | RP skill portability; AR skill metadata | Passed using supported Python fallback with cached PyYAML copied into scratch |
> | Missing-PyYAML paths | Both exit 2 with installation hint |
> | Companion resolver | Passed |
> | Bump-version regression suite | **70/70 passed**, including refusal on `main` before changes |
> | Research refresh tests | All passed |
> | Knowledge-index lint | 0 errors, 0 warnings |
> | Affected plugins’ Claude/Codex manifest identity/version parity | Passed |
> | Citation lint through gate resolver, `--no-url-check --format json --exit-code-on medium` | Exit 0; valid JSON; 51 files, 445 citations, **0 broken, 0 thin** |
> | Gate severity fixtures | High/medium exit 1; low exits 0; valid JSON and broken chains preserved |
> | Matcher comparison on current corpus | Version warnings **174 → 60**; all other JSON unchanged |
> | Regression discrimination | Old matcher fails 12 checks; span-only mutant fails the two dotted-token checks |
> | Working tree; whitespace | Clean; `git diff --check` passed |
> 
> Current advisories: 60 version, 52 decimal-attribution, 41 superlative, 5 count, 3 named-feature. Warn-only counts: 0 unbound campaigns, 5 omitted-confidence notices. These counts establish neither semantic support nor field precision/recall.
> 
> **Receipt verification**
> 
> All three receipts record reviewed inputs, reviewer path/class, independence, weight, finding counts and accepted-fix verification. Their records evidence one standard independent pass followed by host verification, consistent with the delivery policy.
> 
> I ran the convention’s exact enumeration command on the recorded fix ranges and recovered closure ranges:
> 
> | Feature | Reviewed head → closure | Enumerated consequential commits |
> |---|---|---|
> | Review receipts | `a27d41d3 → 7853f361` | `7eb12d33`, correctly classified |
> | Minor remedies | `64bf8ae2 → 6334a196` | `3b1a9b6a`, correctly classified |
> | Citation matcher | `672ccdc5 → c6c2b6fb` | `d8afde36`, correctly classified |
> 
> No enumerated commit lacks a classification. However, the latter two records still contain literal `<closure>` placeholders. Their coverage is recoverable and complete, but their documentary compliance is unfinished.
> 
> **Findings**
> 
> Severity describes the current residual consequence. E/METH-005 remains an alias of R/METH-002.
> 
> | ID | Status | Severity | Rationale |
> |---|---|---|---|
> | QVC-E/METH-001 | persistent | Minor | Durable automated behavioral coverage remains absent. Existing operational evidence does not establish material failure or justify the unselected harness. |
> | QVC-E/METH-002 | verified resolved | Minor originally | Authorized local consolidation landed; operative evidence rules and canonical pointers survive. |
> | QVC-E/METH-003 | verified resolved | Minor originally | Report now records baseline, iteration, capped state, residuals and fixes. Interrupted-loop behavior remains unexercised. |
> | QVC-E/METH-004 | verified resolved | Minor originally | Foundation/work discovery replaces retired phase checks; contradictions require operator decisions; post-loop fixes are prohibited. |
> | QVC-E/METH-005 | partially resolved | Alias | See R/METH-002; counted once. |
> | QVC-E/METH-006 | partially resolved | Minor | Main-branch guard works. The bump path still lacks automatic review/test enforcement; broader enforcement was not authorized. |
> | QVC-R/METH-001 | persistent | Minor | Consequentiality still requires scoping judgment. No new evidence establishes material failure requiring universal escalation. |
> | QVC-R/METH-002 | partially resolved | **Minor residual; originally major** | Reviewed-input anchors and complete classifications resolve the material reconstruction gap. Two recoverable closure placeholders remain; no uncovered commit was found. |
> | QVC-R/METH-003 | pending remedy | **Major** | PR-per-arc was accepted and is due at this arc’s close. Its pending state is expected, not delivery failure; completion is not yet evidenced. |
> | QVC-R/METH-004 | verified resolved | Minor originally | Fork-local reuse restatements were consolidated without adding passes. Upstream-owned repetitions remain outside the authorized remedy. |
> | QVC-R/METH-005 | persistent | Minor | Receiver adjudication remains. Records expose findings and accepted fixes; no demonstrated material failure supports escalation. |
> | QVC-R/METH-006 | withdrawn | None | Distinct feature, aggregate and methodology contracts still support round 1’s withdrawal. |
> | QVC-S/METH-001 | verified resolved | Minor originally | Tier/token suppression and discriminating fixtures implement variant B. Independently reproduced 112 attestation and 2 analytical suppressions. |
> | QVC-S/METH-002 | verified resolved | Minor originally | Gate threshold matches blocking policy; JSON validation remains mandatory. |
> | QVC-S/METH-003 | verified resolved | Minor originally | Both warn-only lists now have explicit reporting without item emission or thresholds. |
> | QVC-S/METH-004 | persistent | Minor | Gate advisories still lack mandatory disposition. Post-engagement edits remain a credible consumer; removal remains unsupported. |
> | **QVC/METH-001** | **new** | Minor | Doc-review’s archive template uses `<kind>s`, producing `storys`. Actual recovery of the archived research story fails there and succeeds under `stories`. Its incomplete-coverage rule prevents silent approval. |
> 
> **Counts:** **1 unresolved major**, which is also the **1 accepted pending remedy**: R/METH-003. **7 verified resolutions**, 2 partial resolutions with minor residuals, 4 persistent minor findings, 1 new minor finding, and 1 carried withdrawal. Zero new or persistent unremedied majors beyond the pending PR remedy; zero operator-retained/deferred major risks.
> 
> The accepted hygiene remedies also landed: dependency declaration/error hints, corrected advisory references and fallback wording, documented fork patches, and the tested branch guard.
> 
> **Seven scenarios and cross-child interactions**
> 
> | Scenario | Assessment |
> |---|---|
> | 1. Successful research, delivery and checkpoint | Research now records completed verification, including N3 approval. Delivery receipts compose with checkpoint reconciliation; no live release was exercised. |
> | 2. Required check fails or is missing | Local operative rules survived consolidation. Gate fixtures preserve failures and distinguish blocking severity. |
> | 3. Output changes after review | Anchored receipts and enumerated classifications support reuse without claiming the original reviewer approved later fixes. |
> | 4. Correction limit exhausted | Doc-review exposes iteration/cap/residual state; checkpoint still blocks residual Critical/High findings and prohibits unchanged capped retries. |
> | 5. Interrupted or cross-host resume | Receipts and report fields improve reconstruction. Closure placeholders, archive pluralization and untested interrupted execution remain limits. |
> | 6. Small versus consequential edits | Feature/standalone routing and standard-pass limits remain intact. No evidence warrants the unselected universal trigger rule. |
> | 7. Real and spurious citation warnings | Suppression reduces measured corpus noise without changing integrity output. Positive fixtures retain unsupported cited versions. |
> 
> I specifically checked consolidation against completion/reuse guarantees; doc-review fixes against authority and checkpoint residual handling; fork ownership against ARD’s single-engine boundary; matcher suppression against integrity checks; and the bump guard against publication expectations. No new major regression was established.
> 
> For Andrew’s three intended jobs, receipts support longitudinal reconstruction, coordinated reviews retain whole-scope integration, and Scout remains available for evidence gaps. Effects on domain-review burden and effectiveness remain **provisional**, pending the separately parked pilot. This assessment introduces no new external factual claims. Research retains its recorded limitations, particularly the judge-generated MT-bench reference and unestablished transfer to agent review or prose-warning consumers.
> 
> **Coverage limits:** I did not run live doc-review correction/resume, quality-checkpoint item emission, release-deploy, publication, adopter-project trials, or new model-based scenario evaluations. I did not re-fetch sources, inspect every attestation/gate/hook, exercise the uv bootstrap path, or re-query remote PR state. Historical synthetic precision/recall was not independently replayed. No execution blocker remains for this read-only assessment.
> 
> **Exit: Awaiting change or evidence.** The accepted PR-per-arc remedy has not yet completed. Passing local checks and feature reviews cannot substitute for that obligation.
> 
> **Next required step:** the host records this as completed root round **2 of 5**, fills the two closure anchors, carries the archive-path correction as minor work, and completes the arc-close PR remedy with Andrew’s required confirmation and consequential-diff review. No additional standard feature-review pass is required merely to refresh hashes.

### Host adjudication

- Accepted as the round-2 parent result. **Root round 2 complete: 2 of 5.**
  Outcome: **Awaiting change or evidence** — the only unresolved major is
  QVC-R/METH-003, whose accepted remedy (PR per arc) is due at this arc's close.
- Closure anchors filled (record-only): `feature-qvc-minor-remedies`
  `64bf8ae2..6334a196`; `feature-ar-fork-citation-matcher` `672ccdc5..c6c2b6fb`.
  The enumerations the assessor ran on those ranges already matched the
  recorded lines; QVC-R/METH-002's residual is thereby closed at record level.
- QVC/METH-001 (new, minor): doc-review archive recovery path `<kind>s` yields
  `storys`. Small correctness fix routed through the standalone fix lane.
- Retained minors (operator-unselected, unchanged): QVC-E/METH-001,
  QVC-R/METH-001, QVC-R/METH-005, QVC-S/METH-004; QVC-E/METH-006 partially
  resolved (guard only). No new major.
- Next: fix QVC/METH-001; then open the arc PR with Andrew's confirmation;
  after the PR exists, a short fresh check of the remedy can close round 3
  if the outcome warrants.

## QVC/METH-001 fix and PR target decision (2026-10-19)

- QVC/METH-001 fixed through the standalone lane:
  `story-fix-doc-review-archive-path` (`cc4fec42`, inline review `2591b783`);
  upstream shorthand parked as `idea-kind-plural-shorthand`.
- PR target (Andrew, 2026-10-19): **"PR on andromedus1"** — open the arc PR inside
  `andromedus1/skills-v2` against its `main` (`ec94cd04`, 2026-05-30), because the
  current credentials (`gh` account `andromedus1`) cannot push to
  `andrewclark88/skills-v2`. The PR therefore also carries the 19 first-parent
  commits merged to `andrewclark88` main by 2026-06-09 (PRs #29–#48). This
  choice is the operator's confirmation to push and open the PR.

## Checkpoint — PR opened (2026-10-19)

- QVC-R/METH-003 remedy applied in part: branch pushed to `andromedus1`
  (`a36137fa..f3c1569f`) and PR opened —
  https://github.com/andromedus1/skills-v2/pull/1 (base `main` `ec94cd04`), with
  a review guide of the QVC arc's consequential contract files. The accepted
  remedy also requires Andrew's review of those diffs before merge; that is
  pending and is Andrew's action.
- Root rounds: **2 of 5 complete**. No round 3 is allocated now: an unchanged
  reassessment before Andrew's PR review would add no evidence. Next: after
  Andrew reviews/merges (or requests changes), allocate round 3 for a fresh
  whole-scope check of R/METH-003's completion; expected exit if nothing else
  changes is clean within reviewed scope with the recorded minor retentions.
- Current primary outcome: **Awaiting change or evidence** (operator PR review).

## Root round 3 allocation (2026-10-19)

- PR https://github.com/andromedus1/skills-v2/pull/1 **merged** 2026-10-19T17:08Z
  (merge `faa24449`). Andrew: "i have merged the PR after review." GitHub records
  no review object; the review evidence is Andrew's statement in session.
- Product baseline: `faa24449` (product delta since round 2's `10ce06bb`:
  `story-fix-doc-review-archive-path` only). Round 3 of 5 allocated; 2 complete.
  Fresh assessor: Codex via peeragent, reusing round-2 coverage for unchanged
  scope and checking R/METH-003 completion, the post-round-2 fix and any
  regression. Records continue on branch `chore/qvc-close`.
