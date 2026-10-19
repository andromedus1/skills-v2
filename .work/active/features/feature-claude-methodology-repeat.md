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
