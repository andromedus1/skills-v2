---
id: feature-ar-fork-citation-matcher
kind: feature
stage: implementing
tags: [agentic-research, methodology-review]
parent: null
depends_on: [feature-qvc-minor-remedies]
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Fork-owned agentic-research: anchor-aware version-number matcher

## Brief

Andrew decided on 2026-10-19 that the fork owns `agentic-research` going forward
(see `feature-claude-methodology-repeat`, "Operator decisions — follow-ups").
First change: QVC-S/METH-001's version-number matcher in
`plugins/agentic-research/ard-core/kernel/lint-citations.py`.

- Suppress version-number advisories in `source-direct` attestations (tier
  suppression, matching CATALOGS §3 "without an in-corpus anchor").
- On analytical lines with resolved citations, suppress only when a cited
  attestation contains the matched version token (experiment variant B).
- Add positive and negative conformance fixtures that distinguish current,
  blanket-citation and token-aware behavior (modeled on the scratch experiment's
  labeled fixtures; see the controller's experiment section).
- Roll forward ownership statements in `AGENTS.md` and
  `docs/project-navigation.md`; keep catalogs/docs consistent with the kernel.

Evidence: scratch experiment (fixture precision 0.40 → 0.84, recall 0.90 →
0.80; real-corpus flags 174 → 60, with 112 attestation flags removed and no
observed recall loss). Synthetic fixtures; not field measurement.

Out of scope: matcher-shape changes (case-insensitive `version`, dotless `vN`,
section refs, arXiv IDs) unless design shows they are cheap and tested; other
kernel rules.

## Simplification opportunity

The gate-citations version-advisory caveat prose may shrink once the matcher
stops flagging attestation metadata.

## Design decisions

- **Ownership (Andrew, 2026-10-19):** the fork owns `agentic-research`; stated
  interpretation (whole plugin, starting with the citation matcher) was not
  corrected. AGENTS.md and project-navigation roll forward accordingly.
- Suppression is default behavior, not a CLI flag (judgment: one behavior, no
  configuration surface; the experiment's flag existed only to compare variants).
- Out of scope (judgment, per brief): matcher-shape gaps (case-insensitive
  `Version`, dotless `vN`, section refs, arXiv IDs) were not tested; parked.
- Depends on `feature-qvc-minor-remedies`: both edit `gate-citations/SKILL.md`
  and the fork-patch section of `docs/project-navigation.md`.

## Architectural choice

Options: (A) tier suppression only — simplest, removes 112/115 real flags but
keeps cited-line noise; (B) tier + token-aware cited-line suppression — best
fixture precision/recall balance (0.84 / 0.80), costs one read per resolved
cited attestation; (C) tier + blanket cited-line suppression — recall 0.50,
rejected. Choose **B**, matching CATALOGS §3's own definition ("without an
in-corpus anchor"): a source-direct attestation is the anchor tier, and a cited
attestation that contains the token anchors the claim. Known hole: a coincident
token in an unrelated passage of the cited attestation — documented, not
fixed.

## Implementation Units

### Unit 1 (trickiest): anchor-aware version-number suppression
**File**: `plugins/agentic-research/ard-core/kernel/lint-citations.py`

```python
ANCHOR_STATUSES = {"resolved", "reduced-substrate-attestation"}

def _version_core(line: str, m: re.Match) -> str | None:
    """Maximal digit/dot run overlapping the match (re-joins 'version 1' + '9.0')."""

def _attestation_has_token(core: str, att_body: str) -> bool:
    """Dotted core: exact token not embedded in a longer number.
    Undotted core: 'version N' / 'vN' form, case-insensitive."""
```

In `lint_file`, build `anchored: dict[int, list[str]]` (line → bodies of cited
attestations whose resolution status is in `ANCHOR_STATUSES`; read each body
once per run via a small cache). In the `version-number` branch, after the
URL/inline-code skip: `if is_attestation: continue`; then
`if lineno in anchored and core and any(_attestation_has_token(core, b) for b in anchored[lineno]): continue`.
Update the header comment (L30) to describe the rule.

**Acceptance**:
- [ ] On the scratch experiment's fixtures (rebuild from the controller record
      if the scratch tree is gone) the lint reproduces variant B's flags.
- [ ] On this repo's `.research/` the version-number count drops from the
      current matcher's total by the attestation-tier flags, with every remaining
      suppression on an analytical line explained by a token-bearing cited
      attestation.
- [ ] No change to integrity results or other pattern categories (diff JSON
      outputs before/after apart from version-number entries).

### Unit 2: conformance fixtures
**Files**: `plugins/agentic-research/ard-core/kernel/conformance/{analysis,attestation,briefs}/…`,
`expected.json`, `README.md`.
- Negative: version tokens in a source-direct attestation; a cited analytical
  line whose attestation contains the token.
- Positive: an uncited fabricated version; a cited line whose attestation lacks
  the version (the case blanket suppression would lose).
- README notes the coincident-token limitation.

**Acceptance**: [ ] `python3 run.py` passes with the new checks; [ ] the suite
fails against the previous lint (proves it distinguishes) and against a blanket
cited-line variant.

### Unit 3: documentation and ownership roll-forward
**Files**: `AGENTS.md` (Ownership: fork owns `research-pipeline` and
`agentic-research`; upstream owns the rest plus documented patches),
`docs/project-navigation.md` (replace "Narrow Agentic Research fork patches" /
"kernel unchanged" with fork ownership of Agentic Research),
`plugins/agentic-research/ard-core/CATALOGS.md` §3 item 2 (state what counts as
an anchor) then `python3 tools/gen-contract.py` and `--check`,
`plugins/research-pipeline/skills/gate-citations/SKILL.md` (shrink the version
caveat to the documented residual noise), and the agentic-research README if it
states upstream ownership.
**Acceptance**: [ ] `gen-contract.py --check` passes; [ ] no remaining claim that
the AR kernel is upstream-owned or unchanged; [ ] AGENTS.md's "Never copy its
kernel into research-pipeline" boundary preserved.

## Implementation Order
1. Unit 2 negative/positive fixtures (red against current lint) → 2. Unit 1 →
3. Unit 3 → integrated verification → one standard feature review with receipt.

## Testing
Conformance (extended) is the regression suite; JSON before/after diff on the
real corpus; skill metadata test for AR.

## Risks
- **Coincident tokens hide a fabricated version** — documented limitation;
  fallback: restrict token match to the attestation's quoted passages.
- **Performance** on large corpora (one read per cited attestation) — cached
  per run; fallback: skip token check above a size bound.
- **Ownership roll-forward conflicts with future upstream merges** — accepted by
  Andrew's decision; upstream drift comparisons for AR no longer apply.
