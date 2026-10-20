---
provenance: agent-synthesis
---

# Version-shape conformance brief

Exercises the version-number token shapes (CATALOGS §3 item 2): which forms are
version identifiers, and which version-shaped tokens are locators, arXiv IDs,
percentages or statistics.

## Not a version — version-number must NOT fire

The streaming design is in §3.4 and the retry rules in §B.3.2.
Section 4.2 covers batching.
The engagement read main text sections 1, 3.3-4.2.
Table 4.1 lists the defaults; Appendix B.9 has the proofs.
The benchmark paper is arXiv 2306.05685.
It was re-read from arXiv HTML v2.
The judge study was checked against arXiv 2306.05685 v4.
The table was re-fetched from v4 of 2306.05685.
A median 36.7% of alerts were fixed.
Between 27.4% to 49.5% of alerts were acted on.
Override rates rose 12.5 percent.
Agreement reached kappa 0.763 vs 0.627 on NQ.
Ranking correlation was Pearson 0.917 vs 0.817.
The effect held at p = 0.05 and at p < 0.01.
The Claude-v1 judge was excluded.
Lattice 2.4.0 adds streaming responses. [version-anchor-src]{1}
The Lattice wire protocol is Version 3. [version-anchor-src]{1}
The Lattice wire protocol is v3. [version-anchor-src]{1}
Release notes are tracked in [v2-notes]{9}.

## A version — version-number must fire

The Orbit wire protocol is Version 7.
ORBIT VERSION 7 is the current protocol.
Orbit v2 dropped the legacy codec.
Embedders still pin V8 for the sandbox.
Python 3.1 support was dropped early.
The pipeline requires numpy 1.26 at minimum.
The load test ran 3.5 times longer.
Pinned to GPT-3.5 for the judge.
Lattice version 2.3.0 remains a supported line.
Table 2 lists Lattice 2.6.0 as current.
Builds target Python 3.12 or 3.11. [version-anchor-src]{1}
Statistics ran on R 4.3.
The Orbit client moved to v4. [version-anchor-src]{1}
The arXiv paper and Lattice v2 differ.
