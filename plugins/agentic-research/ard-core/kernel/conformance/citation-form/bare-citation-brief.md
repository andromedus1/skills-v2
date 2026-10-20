---
provenance: agent-synthesis
---

# Citation-form fixture

Bare numeric citations (no handle) — each must fire `bare-citation`:
HippoRAG improves multi-hop recall {1}.
Two bare numbers on one line {2} and {13}.

Well-formed and non-citation braces — none may fire:
A well-formed citation [resolved-src]{1}.
A shell placeholder ${1} and a subscript x_{2} and an identifier f{3}.
Inline code `{4}` and a URL https://example.com/a{5} stay quiet.

```
A fenced block {6} stays quiet.
```
