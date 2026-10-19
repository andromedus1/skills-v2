# Model notes

Pruned, qualified observations about models used in this repository. They inform
model choices; they are not rankings, scores, availability claims or approvals.
Each note names the date, model and effort, harness, task shape, outcome, evidence
pointer and uncertainty, and says whether it is owner-verified, user-reported or
tentative. Record successes and corrections as well as failures; separate model
behavior from harness limits, unclear briefs and oversized tasks. Delegates
propose observations; the outcome owner edits and prunes this file at handoff and
completion. Not indexed by the knowledge index.

## Working guidance

- Codex `sol` (gpt-6.1-sol) at medium is a strong independent reviewer for skill
  and contract prose changes; expect material findings, and adjudicate them.
  Evidence: four standard reviews on 2026-10-19 (receipts in archived QVC items,
  `git_ref 0a651cba`). Owner-verified. Limit: one repository, prose-heavy diffs.
- Research revisions need a targeted independent re-read: Claude sub-agent
  revisions twice introduced new errors that only the next independent read caught
  (`.research/analysis/campaigns/qvc-review-evidence/verification-checklist.md`).

## Recent observations

Claude sub-agents in these notes inherited the host session model (Claude Opus 5.5,
user/session-reported); the model ID is not recorded in the artifacts themselves.

- 2026-10-19 — Codex gpt-6.1-sol medium via peeragent; four feature reviews
  (receipts, minor remedies, citation matcher, upstream sync). Found a
  reconstruction loophole, two doc-review blockers and a conformance gap; all
  reproduced and fixed by the owner. Owner-verified. Evidence: `## Review` +
  receipts in `git show 0a651cba:.work/active/features/feature-qvc-review-receipts.md`,
  `…/feature-qvc-minor-remedies.md`, `…/feature-ar-fork-citation-matcher.md`, and
  `feature-upstream-sync-2026-10` (review record).
- 2026-10-19 — Codex gpt-6.1-sol, high (rounds 1–2) and medium (round 3); QVC
  whole-scope methodology assessments. Reclassified child majors with evidence,
  withdrew one, caught closure placeholders and the `storys` path bug.
  Owner-verified. Evidence: `git show 0a651cba:.work/active/features/feature-claude-methodology-repeat.md`
  (sections "QVC parent assessment 1/2/3", L495/L734/L889). Limit: the same lineage
  drove the earlier QVE review, so independence on its remedies is partial.
- 2026-10-19 — Codex gpt-6.1-sol medium sandbox could not reach the GitHub API or
  the uv cache/PyPI, so two reviews returned Block on unrun tests. Environment
  limit, not a model failure; run network- or uv-dependent tests on the host.
  Owner-verified. Evidence: `feature-upstream-sync-2026-10` and
  `feature-ar-research-rigor-ideas` review records.
- 2026-10-19 — Claude sub-agents (host-inherited model), research synthesis
  revisions: one adopted the verifier's suggested wording as source fact (N1), one
  introduced an exclusivity claim (N3); independent re-reads caught both.
  Owner-verified behavior; model attribution user/session-reported. Evidence:
  `.research/analysis/campaigns/qvc-review-evidence/verification-checklist.md`.
- 2026-10-19 — Claude sub-agent (host-inherited model) adversarial reader stalled
  (600 s watchdog, no output) on a ~1,000-line corpus; a re-dispatch told to write
  findings incrementally completed. Likely assignment size or harness, not model.
  Tentative. Evidence: `git show 0a651cba:.work/active/stories/story-research-qvc-review-evidence.md`
  (L145).
- 2026-10-19 — Codex gpt-6-luna high on a bounded scenario check (receipt rules)
  matched the Claude sub-agent's outcomes but surfaced fewer ambiguities (the
  Claude reader found A–G, which led to fixes). One sample. Tentative. Evidence:
  `git show 0a651cba:.work/active/features/feature-qvc-review-receipts.md`
  ("Unit 3 forward scenarios", L227).
