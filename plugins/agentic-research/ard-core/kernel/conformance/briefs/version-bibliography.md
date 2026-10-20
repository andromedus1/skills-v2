# Version-bibliography conformance fixture

A bibliography entry names its attestation by handle; a version on the entry line
is anchored when that attestation carries the token.

## Anchored — version-number must NOT fire

1. **version-anchor-src** — Lattice 2.4.0 release notes. Source: https://example.com/lattice/releases.
| 1 / version-anchor-src | [Lattice 2.4.0 release notes](https://example.com/lattice/releases) | 2026-10-19 |
### 1. Lattice 2.4.0 release notes — `version-anchor-src`

## Unanchored — version-number must fire

1. **version-anchor-src** — Lattice 2.6.0 release notes. Source: https://example.com/lattice/releases.
| 1 / version-anchor-src | [Lattice 2.6.0 release notes](https://example.com/lattice/releases) | 2026-10-19 |
### 1. Lattice 2.6.0 release notes — `version-anchor-src`
4. **version-anchor-candidate-src** — Kestrel 8.0 changelog.
5. **no-such-bib-handle** — Orbit 5.1 release notes.
The Lattice 2.4.0 notes are listed as **version-anchor-src** above.
