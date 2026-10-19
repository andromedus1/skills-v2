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
  revisions twice introduced new errors that only the next independent read caught.

## Recent observations

- 2026-10-19 — Codex gpt-6.1-sol medium via peeragent; four feature reviews
  (receipts, minor remedies, citation matcher, upstream sync). Found a
  reconstruction loophole, two doc-review blockers and a conformance gap; all
  reproduced and fixed by the owner. Owner-verified.
- 2026-10-19 — Codex gpt-6.1-sol high; three whole-scope methodology assessments
  (QVC rounds 1–3). Reclassified child majors with evidence, withdrew one, caught
  closure placeholders and the `storys` path bug. Owner-verified. Limit: the same
  lineage drove the earlier QVE review, so independence on its remedies is partial.
- 2026-10-19 — Codex gpt-6.1-sol sandbox could not reach the GitHub API or the uv
  cache/PyPI, so a review returned Block on unrun tests. Environment limit, not a
  model failure; run network- or uv-dependent tests on the host. Owner-verified.
- 2026-10-19 — Claude Opus 5.5 sub-agents, research synthesis revisions: one
  adopted the verifier's suggested wording as source fact (N1), one introduced an
  exclusivity claim (N3); independent re-reads caught both
  (`.research/analysis/campaigns/qvc-review-evidence/verification-checklist.md`).
  Owner-verified.
- 2026-10-19 — Claude Opus 5.5 adversarial reader stalled (600 s watchdog, no
  output) on a ~1,000-line corpus; a re-dispatch told to write findings
  incrementally completed. Likely assignment size or harness, not model. Tentative.
- 2026-10-19 — Codex gpt-6-luna high on a bounded scenario check (receipt rules)
  matched Claude's outcomes but surfaced fewer ambiguities (Claude's reader found
  A–G, which led to fixes). One sample. Tentative.
