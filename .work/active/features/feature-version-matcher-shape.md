---
id: feature-version-matcher-shape
kind: feature
stage: implementing
tags: [agentic-research, citations, lint]
parent: null
depends_on: []
release_binding: null
gate_origin: null
created: 2026-10-19
updated: 2026-10-19
---

# Close version-number matcher shape gaps in the citation lint

## Brief

The `version-number` pattern in the ARD citation lint
(`plugins/agentic-research/ard-core/kernel/lint-citations.py:76`) has shape gaps
that the QVC-S/METH-001 experiment surfaced and `feature-ar-fork-citation-matcher`
left out of scope (that feature shipped tier suppression and token-aware
cited-line suppression, variant B; corpus version flags 174 → 60).

- **Recall:** case-insensitive `Version N` (e.g. `Version 3`) and dotless `vN`
  (e.g. `v2`) are not matched. Every experiment variant missed them.
- **Precision:** residual noise under variant B is mostly section refs (`§4.2`),
  arXiv IDs (`2310.06825`), percentages, decimal statistics and model names
  (heuristic triage, synthetic fixtures; not field measurement).

Close both sides without regressing the anchor rules: a newly matched form must
still be suppressible by the same tier and token-aware cited-line anchors
(`_version_core`, the attestation-body token check at `:439-454`), and new
precision exclusions must not hide plausible fabricated version claims. Ship
labeled positive and negative conformance fixtures for each new form and each
exclusion so the suite can tell variants apart, and report corpus flag counts
before and after.

The fork owns `agentic-research` (operator decision 2026-10-19, recorded in
`feature-claude-methodology-repeat`), so the kernel lint is editable here.
Recall additions raise the flag count while exclusions lower it; the design
must state the net trade and its fixture evidence.

## Simplification opportunity

The suppression-policy header comment (`lint-citations.py:28-38`) and any
prose caveat that lists unmatched or noisy version shapes should shrink to
match the new behavior rather than grow. No other deletions identified; the
`scripts/lint-citations.py` shim forwards to the kernel and needs no change.

## Design decisions

Operator answers (Andrew, 2026-10-19), from a scratch measurement on this repo's
`.research/` corpus (93 version flags at `457c5222`, all outside attestations;
conformance 77/77 under every variant):

- **Bibliography entries anchor by their own handle**: anchor by entry handle. A
  version on a bibliography/references entry line is anchored when the attestation
  the entry names contains the token (same token-aware check as cited lines).
  Largest single precision gain (65 → 35 in the scratch run).
- **Decimal statistics**: statistic keyword/operator list. A single-dot number
  after a statistic word or operator, or chained from one by `vs`/`to`/`and`, is
  not a version. Rejected: requiring a version context (would drop lowercase
  package names such as `numpy 1.26`).
- **Model names**: keep flagging. `GPT-3.5`, `Llama-3.1-70B` stay in scope — an
  invented model version is the category's target, and cited lines whose
  attestation names the model are already suppressed.
- **Dotless `vN`** (host judgment): match only as a standalone token
  (`(?<![\w-])[vV]\d+\b`), either case. Hyphen- or word-joined forms
  (`Claude-v1`, handle segments such as `peeragent-v082-release`) do not match.

## Architectural choice

Options considered: (A) one larger regex with negative lookbehinds for each noise
shape; (B) keep the match regex simple and add a per-line exclusion helper the
`version-number` branch consults, plus bibliography lines fed into the existing
`anchored` map; (C) a token classifier that replaces regex matching. Chosen: **B**.
Python lookbehinds must be fixed-width, so `§`/`Section 3.3-` ranges and statistic
chains cannot be expressed cleanly in (A); (C) rewrites a heuristic the fork only
needs to tune. B keeps every existing anchor path unchanged — bibliography anchoring
reuses `anchored` and `_attestation_has_token`, so a bibliography entry is anchored
by exactly the rule a cited line is.

No new state, records or cross-plugin contracts. The scratch run's net trade on this
corpus: recall additions add 5 lines (3 after arXiv-revision exclusion), exclusions
and bibliography anchoring remove ~60; the residue (~30) is real release versions on
uncited lines plus model names, as decided.

## Implementation Units

All code in `plugins/agentic-research/ard-core/kernel/lint-citations.py`; the
`scripts/lint-citations.py` shim forwards unchanged.

### Unit 1: Version-noise exclusions (trickiest — design first)

```python
# Document-structure references: §3.1, §§2-4, Section 3.7, sections 1, 3.3-4.2,
# Table 4.1, Fig. 2.3, Appendix B.9, Eq. 3.2 — the token is a locator, not a version.
_VERSION_STRUCT_PRE = re.compile(
    r"(?i)(?:§+\s*|\b(?:sections?|secs?\.|tables?|tabs?\.|figures?|figs?\.|"
    r"appendix|appendices|app\.|chapters?|ch\.|eqs?\.|equations?)\s+)"
    r"(?:[A-Z]?[\d.]+\s*(?:[-–,/]|and|&)\s*)*[A-Z]?\.?$")
_ARXIV_ID = re.compile(r"\d{4}\.\d{4,5}")                 # 2306.05685 (fullmatch on core)
_ARXIV_REV_PRE = re.compile(r"(?i)\barxiv\b[^.;)\n]{0,24}$")   # "arXiv HTML v2", "arXiv 2306.05685 v4"
_ARXIV_REV_POST = re.compile(r"\s+of\s+(?:arxiv:?\s*)?\d{4}\.\d{4,5}", re.I)  # "v4 of 2306.05685"
# Statistic words stand alone; short symbols (p, r, ρ, α) count only with an
# operator, so "Python 3.11 or 3.12" and "R 4.3" still fire.
_STAT_PRE = re.compile(
    r"(?i)(?:\b(?:kappa|κ|pearson|spearman|kendall|correlation|accuracy|precision|"
    r"recall|f1|auc|bleu|rouge(?:-\w+)?|score|mean|median|sd|std)\b\s*(?:of\s+|[:=]\s*)?"
    r"|[=<>≤≥≈±]\s*)$")
_STAT_CHAIN = re.compile(r"^\s*\)?\s*(?:vs\.?|versus|to|and|or|[-–/,])\s*$", re.I)

def _version_noise(line: str, matches: list[re.Match]) -> set[int]:
    """Start offsets of version-number matches on `line` that are not version claims:
    inside a `[handle]{N}` citation; a document-structure locator; an arXiv ID or
    arXiv revision; a percentage; or a single-dot decimal statistic (after a
    statistic word/operator, or chained from one by vs/to/and). Matches are in
    line order; a statistic chain extends only from an excluded statistic."""
```

**Implementation notes**
- Called once per line inside the `version-number` branch (compute lazily on the
  first match, cache for the line); `continue` when `m.start()` is in the set.
  Runs **before** the URL/inline-code and anchor checks only in the sense that any
  exclusion short-circuits; order among exclusions is irrelevant.
- Citation-span mask: any `CITATION_RE` span containing `m.start()`.
- Percent: the text after the match starts with `%` or `\s*percent`.
- arXiv: fullmatch `_ARXIV_ID` on the digit core (leading `v` stripped); a dotless
  `vN` with `_ARXIV_REV_PRE` on the preceding 32 chars or `_ARXIV_REV_POST` after.
- Statistic: only single-dot, digit-leading tokens (`tok.count(".") == 1`); multi-dot
  tokens are never statistics. `_STAT_PRE` on the preceding 28 chars, or
  `_STAT_CHAIN` on the text between the previous excluded statistic's end and this
  match.
- `_VERSION_STRUCT_PRE` on the preceding 40 chars.

**Acceptance criteria**
- [ ] `§3.4`, `§B.3.2`, `Section 4.2`, `sections 1, 3.3-4.2` (both tokens), `Table 4.1`,
  `Appendix B.9` do not fire.
- [ ] `2306.05685`, `arXiv HTML v2`, `arXiv 2306.05685 v4`, `v4 of 2306.05685` do not fire.
- [ ] `36.7%`, `27.4% to 49.5%`, `12.5 percent` do not fire.
- [ ] `kappa 0.763 vs 0.627`, `Pearson 0.917 vs 0.817`, `p = 0.05`, `p < 0.01` do not fire.
- [ ] `Python 3.11 or 3.12` (both tokens) and `R 4.3` still fire.
- [ ] Still fire: `Python 3.1`, `numpy 1.26`, `Lattice 2.4.0`, `GPT-3.5`, `version 2.3.0`,
  `Lattice 2.4.0 was tested 3.5 times` (multi-dot unaffected; `3.5` without a
  statistic word still fires), and `Table 2 lists Lattice 2.6.0` (locator rule
  binds only the token right after the locator).

### Unit 2: Matcher recall

```python
"version-number": re.compile(
    r"\b[vV]?\d+(?:\.\d+)+\b"          # dotted: 2.4.0, v0.8.2, 3.12
    r"|(?i:\bversion\s+\d+\b)"         # version 3 / Version 3 / VERSION 3
    r"|(?<![\w-])[vV]\d+\b"            # standalone dotless: v2, V8
),
```

`_version_core` and `_attestation_has_token` already treat an undotted core as
`version N` or `vN`, case-insensitive — no change.

**Acceptance criteria**
- [ ] Uncited `Version 3`, `VERSION 3`, `v2`, `V8` fire.
- [ ] `Claude-v1`, `peeragent-v082-release` (bare text and inside a citation) do not fire.
- [ ] A cited `Version 3` / `v3` line is suppressed when the cited attestation carries
  `version 3` or `v3`; fires when it carries only `3.0`.

### Unit 3: Bibliography-entry anchoring

```python
# A bibliography / references entry line names its attestation by handle:
#   "12. **handle** — Title …"         (references.md, campaign source lists)
#   "| 12 / handle | Title … |"        (per-corpus BIBLIOGRAPHY tables)
#   "### 12. Title — `handle`"         (kernel templates/BIBLIOGRAPHY.md heading)
_BIB_ENTRY = re.compile(
    r"^\s*(?:\d+\.\s+\*\*(?P<a>[a-z0-9][a-z0-9-]*)\*\*"
    r"|\|\s*\d+\s*/\s*(?P<b>[a-z0-9][a-z0-9-]*)\s*\|"
    r"|#{2,6}\s+\d+\.\s.*—\s*`(?P<c>[a-z0-9][a-z0-9-]*)`\s*$)")

def _bib_entry_handle(line: str) -> str | None: ...
```

In `lint_file`'s `do_pattern` block, after the cited-line `anchored` map is built,
for each non-frontmatter, non-code line with a `_bib_entry_handle`, run
`check_citation(handle, attestation_dir, analysis_dir, True, False, handle_counts)`
(provenance treated as present, no URL fetch) and, when the status is in
`ANCHOR_STATUSES`, append that attestation's body to `anchored[lineno]`. The
version branch then anchors the line exactly as it does a cited line. Mask the
entry's own handle span (group `a`/`b`) from matching as for citation spans.

**Acceptance criteria**
- [ ] Each of the three entry shapes naming `version-anchor-src` with `2.4.0` is
  suppressed; with `2.6.0` (absent from the attestation) fires.
- [ ] An entry naming an acquisition-candidate or a missing attestation fires.
- [ ] A non-entry line (`Lattice 2.4.0 … **version-anchor-src**` mid-line) fires.
- [ ] No change to citation findings or `--stats` output for entry lines (anchoring
  is pattern-scan only).

### Unit 4: Conformance fixtures

- New `conformance/briefs/version-shape-brief.md` (`provenance: agent-synthesis`):
  one line per Unit 1/2 criterion, grouped under "must fire" / "must not fire"
  headings; cited lines cite `version-anchor-src`.
- New `conformance/briefs/version-bibliography.md`: the three entry shapes,
  anchored and unanchored, plus the candidate and missing-handle cases.
- Extend `version-anchor-src.md` only if a recall case needs a `v3` token; append
  below existing lines so current line numbers hold.
- Extend `expected.json` `version_anchor.suppressed` / `.flagged` and its
  `_comment`; update the check total and group breakdown in `conformance/README.md`
  and its "Version-number anchor rule" section (noise exclusions, bibliography
  anchoring, standalone `vN`).

### Unit 5: Prose roll-forward

- `lint-citations.py` suppression header (`:28-38`): replace the version bullet with
  the current rule — anchors (attestation tier, cited line, bibliography entry) and
  the noise exclusions in one short list. Keep the coincident-token known hole.
- `ard-core/CATALOGS.md:116`: the anchored definition adds "or a bibliography entry
  naming that attestation"; document-structure locators, arXiv IDs, percentages and
  statistics are not version identifiers.

## Implementation Order

1. Unit 1 with its fixture lines (trickiest; the statistic chain and locator ranges
   are where precision can overreach).
2. Unit 2 + fixture lines (depends on Unit 1's citation-span mask).
3. Unit 3 + bibliography fixture.
4. Unit 4 expected.json/README totals, then Unit 5 prose.
5. Corpus measurement: before/after version flag counts on `.research/` recorded in
   Implementation notes.

## Testing

- `python3 plugins/agentic-research/ard-core/kernel/conformance/run.py` — all
  existing 77 checks plus the new version-anchor lines pass.
- Negative control: run the suite with `--lint` against the pre-change kernel
  (`git show 457c5222:…/lint-citations.py` to scratch); the new fixture lines must
  fail there, showing the suite tells the variants apart.
- Existing shape tests: `plugins/agentic-research/scripts/tests/skill-metadata.test.sh`
  and `test_refresh_scan.py` (imports the kernel module) still pass.
- Corpus: version flag count on `.research/` before/after, with the residue sampled.

## Risks

- **Statistic chain overreach** — `vs`/`to` chaining could swallow a real version
  (`kappa 0.76 vs Lattice 2.4` is multi-dot, safe; `p = 0.05 to v1.2` — `v`-prefixed
  tokens are never statistics). — **Fallback**: drop chaining; keep keyword/operator
  only.
- **Locator rule hides a version after a locator word** (`Table 2.6.0`) — multi-dot
  after a locator is rare; accepted. — **Fallback**: limit the locator rule to tokens
  with at most one dot plus an optional letter prefix.
- **Bibliography lines in other deployments use other shapes** — unrecognized shapes
  simply keep today's behavior (flagged). No false suppression.
- **Fixture files under `briefs/` shift other check groups' totals** — run the whole
  suite; adjust only counts that change for the stated reason.
