# ARD lint conformance

Golden fixtures + a runner that assert a citation-chain lint reproduces ARD's **canonical verdicts**. Run it against the reference lint, or against any re-implementation of it:

```
python3 run.py                  # validates ../lint-citations.py
python3 run.py --lint <path>    # validates an alternate implementation
```

It covers the full lintable contract (*ARD SPEC §4.2*, *ARD CATALOGS §3*): all citation-chain statuses (seven broken — `unresolved-handle`, `mismatched-source-handle`, `colliding-handle`, `unreachable-source`, `missing-provenance`, `non-canonical-handle`, `duplicate-frontmatter-key` — plus four non-broken: `resolved`, `intra-program-resolved`, `reduced-substrate-attestation`, `acquisition-candidate`), the GR.5 thin-attestation flag, the six lint pattern categories (incl. the closed-world "exactly N" census), the suppression contexts (fenced code blocks, inline code, URLs, blockquotes, attestation files — patterns that should NOT fire in these contexts), the `substrate_confidence`-omission deprecation, and the `--stats` audit mode (colliding-handle, filename-mismatch, by-handle citation counts), and the `campaign_unbound` surfacing (a `cN-` campaign handle whose slug/existence resolves but whose campaign number is deployment-mapped is surfaced, not silently clean — incl. the cross-campaign and `cN-position` cases), and the `version-number` anchor rule (below). Expected verdicts are in [expected.json](expected.json); fixtures live under `attestation/`, `analysis/`, and `briefs/`. Exit 0 = conformant, 1 = a divergence (printed per-check). 119 checks total: 27 baseline · 16 suppression · 4 stats · 2 substrate-confidence · 8 lint-hardening · 62 version-anchor.

## Version-number anchor rule

`version-number` flags a version token *without an in-corpus anchor* (*ARD CATALOGS §3*). The `version_anchor` block in `expected.json` lists, per fixture line, what must and must not fire:

- **Suppressed (negative):** every version token in a `provenance: source-direct` attestation (`version-anchor-src`, `version-anchor-reduced-src`, `version-anchor-candidate-src`) — the attestation is the anchor tier; and a cited analytical line whose `resolved` or `reduced-substrate-attestation` attestation contains the same token (`briefs/version-anchor-brief.md` L13–17: dotted tokens, case-insensitive `version N`, a reduced-substrate anchor, two tokens anchored by two different citations).
- **Flagged (positive):** an uncited version (L21); a cited line whose attestation lacks the token (L22 `2.6.0`, L23 `3.1` against an attested `3.12`, L24 `version 4`); a citation whose status cannot anchor (L25 intra-program, L26 acquisition candidate whose placeholder body names the token); and one unanchored token among anchored ones (L27).
- **Dotted `version N.M`:** the whole dotted token is the key — L31 `version 2.3.0` is anchored by the attested `2.3.0`; L32 `version 3.9` fires although the attestation contains `Version 3`.

The flagged cited lines make the suite fail a matcher that suppresses every cited line, as well as one that only suppresses the attestation tier.

- **Token shapes** (`briefs/version-shape-brief.md`): `Version N` in any case and a standalone `vN` are versions (L35–38); `Claude-v1` and a `[v2-notes]{N}` citation are not (L27, L31). Not versions: document locators (`§3.4`, `§B.3.2`, `Section 4.2`, `sections 1, 3.3-4.2`, `Table 4.1`), arXiv IDs and revisions, percentages, and decimal statistics after a statistic word or operator, chained by `vs`/`to` (L13–26). Still flagged: `numpy 1.26`, an unqualified `3.5`, `GPT-3.5`, a version after a locator's own number (`Table 2 lists Lattice 2.6.0`), `Python 3.12 or 3.11` with only 3.12 anchored, `R 4.3`, and a `vN` merely near the word arXiv (L39–46, L48). Cited `Version 3` / `v3` lines are anchored by the attestation's `Version 3` (L29–30); a cited `v4` is not (L47).
- **Bibliography entries** (`briefs/version-bibliography.md`): a `N. **handle**`, `| N / handle |` or `### N. Title — `handle`` line is anchored by the attestation it names, under the same token rule (L8–10). It fires when that attestation lacks the token (L14–16), when the handle is an acquisition candidate or does not resolve (L17–18), and on a non-entry line that only mentions the handle (L19).

**Known limitation:** the token check reads the whole attestation body, so a coincident token in an unrelated passage of the cited attestation (for example an unrelated `version 2` or `0.2.0`) anchors the line and hides a fabricated version. This is documented, not fixed; a stricter rule would restrict matching to the attestation's quoted passages.
