#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Reference implementation — ARD citation-chain lint.
#
# A zero-dependency reference implementation of the full lintable catalogue:
# the citation-chain enforcement (ARD SPEC §4.2), the lint pattern catalog
# (ARD CATALOGS §3), and the GR.5 thin-attestation structural check (ARD CATALOGS
# §1, §4 job h). It is one instantiation, not the framework: it assumes only the
# two invariants — the `[handle]{N}` citation wire-form and the normative-minimum
# attestation frontmatter — so it ports to any deployment that follows them.
#
# Covers, per the catalogue:
#   - 6 surface-signature pattern categories (warn; flag for human spot-check)
#   - canonical-handle fence (ASCII-lowercase; uppercase/homoglyph -> non-canonical-handle)
#   - citation-chain integrity, statuses:
#       resolved / unresolved-handle / mismatched-source-handle / colliding-handle /
#       unreachable-source / missing-provenance / duplicate-frontmatter-key (split-brain)
#     plus the non-broken statuses:
#       intra-program-resolved        (handle resolves to an analytical-tier artifact)
#       reduced-substrate-attestation (attestation marked search-summary/snippet-thin/unspecified)
#       acquisition-candidate         (intentionally-unfetched escape-hatch source, SPEC §4.1)
#   - GR.5 thin-attestation structural check (resolved attestation with no
#       section anchors and no key-passage blockquotes)
#   - substrate_confidence-omission grace-period deprecation: a resolved attestation
#       that omits substrate_confidence still reads source-direct but is flagged
#       (a future MAJOR flips the default fail-closed: omission -> unspecified -> gap)
#
# Suppression contexts (reduce false-positives in pattern scanning):
#   - YAML frontmatter block and fenced code blocks are fully masked.
#   - Per-category: version-number skipped in URLs and inline code; count and
#     decimal-with-attribution skipped in attestation files; composed-effort-estimate
#     and comparative-superlative skipped in blockquotes.
#   - version-number flags a version "without an in-corpus anchor" (CATALOGS §3).
#     Anchors: a source-direct attestation (the anchor tier); a line citing, or a
#     bibliography entry naming, a resolved / reduced-substrate-attestation whose
#     body contains the same version token. Not versions: tokens inside a citation,
#     document locators (§3.1, Section 4.2, Table 2.1), arXiv IDs and revisions,
#     percentages, and decimal statistics (kappa 0.76, p = 0.05). Known hole: a
#     coincident token elsewhere in the cited attestation's body also anchors.
#
# Usage:
#   python3 lint-citations.py <brief-or-dir>
#       [--attestation-dir DIR] [--analysis-dir DIR]
#       [--format markdown|json] [--exit-code-on high|medium|low|none]
#       [--no-citation-check] [--no-pattern-check] [--no-thin-check] [--no-url-check]
#       [--stats]
"""ARD citation-chain + pattern + thin-attestation lint (reference implementation)."""

import argparse
import glob
import ipaddress
import json
import os
import re
import socket
import sys
import urllib.request
from urllib.parse import urlparse

# The citation wire-form grammar (ARD SPEC §4.2): handle = [\w-]+, N = \d+.
# N is captured for reporting only — the kernel resolves by HANDLE, never by N.
# {N}<->bibliography correspondence (CATALOGS §3 check 7) needs the deployment's bibliography
# structure (not an ARD invariant), so it is deployment-mapped, not validated here.
CITATION_RE = re.compile(r"\[([\w-]+)\]\{(\d+)\}")
# Citation-form fence (CATALOGS §3 `bare-citation`): a `{N}` with no `[handle]` cannot
# enter the chain. Excludes `]{N}` (a well-formed citation), `x{N}`/`_{N}` (identifiers,
# LaTeX subscripts) and `${N}` (shell/template placeholders).
BARE_CITATION_RE = re.compile(r"(?<![\]\w$])\{(\d+)\}")
# The fence covers claim-bearing artifacts only (or ones declaring no provenance): source-direct
# attestations quote their sources' own notation, and verification records refer to the
# synthesis's numbering rather than making sourced claims.
BARE_CITATION_PROVENANCE = {"agent-synthesis", "agent-authored-from-raw"}

# Reference regex matchers, keyed by the lint pattern-category id (ARD CATALOGS §3).
# The *categories* are the invariant diagnostic targets and are sourced from the
# generated catalog data (kernel/catalogs.json) at runtime — so a MINOR inventory
# bump to the category set is a data change this lint consumes, no code edit. The
# *matchers* below are deployment latitude (reference heuristics flagging a span for
# human spot-check). If catalogs.json is absent, the lint falls back to these six.
REFERENCE_MATCHERS = {
    "decimal-with-attribution": re.compile(
        r"\b\d+(?:\.\d+)?%?\b(?=[^\n]{0,40}(?:arXiv|et al\.|[A-Z][a-z]+ et al|paper|\bpp?\.\s*\d))"
        r"|(?:arXiv|et al\.|paper)[^\n]{0,40}\b\d+(?:\.\d+)?%?\b"
    ),
    "version-number": re.compile(
        r"\b[vV]?\d+(?:\.\d+)+\b"          # dotted: 2.4.0, v0.8.2, 3.12
        r"|(?i:\bversion\s+\d+\b)"         # version 3 / Version 3
        r"|(?<![\w-])[vV]\d+\b"             # standalone dotless: v2 (not Claude-v1)
    ),
    "count-without-unit-citation": re.compile(
        r"\b[\d,]+\s+(?:lines|pages|words|files|tokens|developers?)\b|~\s*[\d,]+\s+(?:lines|loc)\b",
        re.IGNORECASE,
    ),
    "comparative-superlative": re.compile(
        r"\bthe (?:only|strongest|weakest|best|worst|most|least|largest|smallest|fastest|slowest|"
        r"highest|lowest)\b|\blowest effort\b|\bonly \w+ (?:that|with|to)\b"
        # Closed-world census phrased as a bounded count ("each has exactly two attested
        # implementations") — the same anchor-and-drift shape one altitude up.
        r"|\bexactly (?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b",
        re.IGNORECASE,
    ),
    "named-feature-claim": re.compile(
        r"\b[A-Z][A-Za-z0-9.\-]+\s+(?:supports|includes|implements|provides|offers|features|ships with)\b"
    ),
    "composed-effort-estimate": re.compile(
        r"\b\d+\s*[-–—]\s*\d+\s*(?:developer-days|dev-days|days|weeks|months|hours)\b"
        r"|~\s*\d+\s*(?:lines of|loc\b)",
        re.IGNORECASE,
    ),
}

# Fallback non-broken citation statuses (used only when catalogs.json is absent).
# Keep in sync with the non-broken statuses in CATALOGS §3 — a status the lint emits
# but omits here would be miscounted as broken on the no-data-file backward-compat path.
DEFAULT_NON_BROKEN = {"resolved", "intra-program-resolved",
                      "reduced-substrate-attestation", "acquisition-candidate"}
SEVERITY_RANK = {"high": 3, "medium": 2, "low": 1, "none": 0}


def load_catalog_config(catalogs_path):
    """Source the pattern-category set + non-broken-status set from the generated
    catalog data. Returns (matchers, non_broken). Falls back to the hardcoded
    reference set when catalogs.json is missing/unreadable — so the lint keeps
    working without the data file (backward compatible)."""
    try:
        with open(catalogs_path, encoding="utf-8") as fh:
            data = json.load(fh)
        lint = data["lint"]
        cat_ids = [c["id"] for c in lint["pattern_categories"]]
        non_broken = {s["id"] for s in lint["citation_chain_statuses"] if not s["broken"]}
    except (OSError, KeyError, ValueError):
        return dict(REFERENCE_MATCHERS), set(DEFAULT_NON_BROKEN)
    # Activate a matcher for each declared category; note any the impl can't match yet.
    matchers = {cid: REFERENCE_MATCHERS[cid] for cid in cat_ids if cid in REFERENCE_MATCHERS}
    missing = [cid for cid in cat_ids if cid not in REFERENCE_MATCHERS]
    if missing:
        print(f"[note] catalogs.json declares {len(missing)} pattern categor(ies) with no "
              f"matcher in this lint: {', '.join(missing)} — add a matcher to cover them.",
              file=sys.stderr)
    return matchers, (non_broken or set(DEFAULT_NON_BROKEN))


def parse_frontmatter(text):
    """Minimal frontmatter scan (no YAML dependency) — the fields the lint needs.
    Reads the LAST occurrence of each key (YAML loaders are last-wins); duplicate
    resolution-critical keys are caught separately by frontmatter_duplicate_keys."""
    fields = {}
    if not text.startswith("---"):
        return fields
    end = text.find("\n---", 3)
    if end == -1:
        return fields
    block = text[3:end]
    for key in ("source_handle", "source_url", "source_path", "provenance",
                "substrate_confidence", "acquisition_status"):
        matches = re.findall(rf"^{key}:\s*(.+?)\s*$", block, re.MULTILINE)
        if matches:
            fields[key] = matches[-1].strip().strip("\"'")
    return fields


def frontmatter_duplicate_keys(text):
    """Set of resolution-critical keys appearing 2+ times in the frontmatter block.
    A duplicated key is split-brain: this lint reads last-wins (matching YAML), but a
    tool reading first-wins sees a different value — the attestation's identity forks."""
    if not text.startswith("---"):
        return set()
    end = text.find("\n---", 3)
    if end == -1:
        return set()
    block = text[3:end]
    return {key for key in ("source_handle", "source_url", "source_path", "provenance")
            if len(re.findall(rf"(?m)^{key}:\s*.+$", block)) > 1}


def body_after_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def is_thin_attestation(body):
    """GR.5 structural check: thin iff body has no `##` section anchor AND no `>` blockquote."""
    has_section = re.search(r"^##\s", body, re.MULTILINE) is not None
    has_quote = re.search(r"^>\s", body, re.MULTILINE) is not None
    return not (has_section or has_quote)


# --- source_url liveness: SSRF-hardened HEAD probe -------------------------
# Check 4 (below) HEAD-probes whatever source_url an attestation declares.
# Attestations are vendored substrate a compromised or hostile source could
# seed, so the probe is fenced to only ever touch *public web* addresses:
#   - the scheme is allow-listed to http(s) (refuses file://, gopher://, ...);
#   - the resolved host must be a public IP — loopback / link-local / private
#     (RFC1918) / reserved / multicast / unspecified are refused, which closes
#     the cloud-metadata endpoint (169.254.169.254) and internal-range probes;
#   - every redirect hop is re-validated against the same two rules, so a 30x
#     can't bounce an allowed external probe inward.
# Best-effort by design: a DNS rebind between this resolution and urllib's own
# is not defended (would need pinning the connection to the checked IP) —
# proportionate for an operator-run, HEAD-only, body-ignored lint. A refused
# URL reports as not-alive (the existing low-severity unreachable-source warn).
_ALLOWED_URL_SCHEMES = ("http", "https")


def _host_is_public(host):
    """True iff `host` (an IP literal or DNS name) maps only to public addresses.
    A name that resolves to *any* non-public address is refused; an unresolvable
    or unparseable host is refused (safe default)."""
    if not host:
        return False
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False
    for *_, sockaddr in infos:
        try:
            ip = ipaddress.ip_address(sockaddr[0])
        except ValueError:
            return False
        if (ip.is_loopback or ip.is_link_local or ip.is_private
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            return False
    return True


def _url_allowed(url):
    parsed = urlparse(url)
    return parsed.scheme in _ALLOWED_URL_SCHEMES and _host_is_public(parsed.hostname)


class _PublicHTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Re-validate scheme + host on every redirect hop. Returning None refuses
    the hop, which makes urllib raise HTTPError -> url_alive() reports not-alive."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not _url_allowed(newurl):
            return None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_URL_OPENER = urllib.request.build_opener(_PublicHTTPRedirectHandler)


def url_alive(url, timeout=5):
    if not _url_allowed(url):
        return False
    try:
        # Send a User-Agent: Cloudflare and other bot-fight frontends return
        # HTTP 403 to a headerless urllib request, which would falsely flag a
        # live, properly-attested source as unreachable-source. A descriptive
        # UA identifies the probe as a lint, not a bot — the SSRF fence in
        # _url_allowed/_host_is_public is the security boundary, not UA
        # absence.
        req = urllib.request.Request(
            url, method="HEAD", headers={"User-Agent": "ard-lint/1.0 (+source liveness probe)"}
        )
        with _URL_OPENER.open(req, timeout=timeout) as resp:
            return 200 <= getattr(resp, "status", 200) < 400
    except Exception:
        return False


def source_handle_counts(attestation_dir):
    """Map source_handle -> count across the attestation tier, for the uniqueness check.
    A source_handle declared by 2+ attestations makes that handle resolve ambiguously."""
    counts = {}
    if not os.path.isdir(attestation_dir):
        return counts
    for r, _, fs in os.walk(attestation_dir):
        for f in fs:
            if not f.endswith(".md"):
                continue
            try:
                with open(os.path.join(r, f), encoding="utf-8") as fh:
                    sh = parse_frontmatter(fh.read()).get("source_handle")
            except OSError:
                continue
            if sh:
                counts[sh] = counts.get(sh, 0) + 1
    return counts


def intra_program_resolves(handle, analysis_dir):
    """Non-attestation resolution to an analytical-tier artifact (intra-program reference).

    Returns a resolution KIND, or None if unresolved:
      - "bound"            — a position artifact at positions/<handle>.md (fully bound).
      - "campaign-unbound" — a campaign specialist/parent reference whose slug (or
                             existence) resolves, but whose campaign NUMBER `cN` the kernel
                             cannot bind to a campaign directory. Reported in the output's
                             `campaign_unbound` list (not silently clean), so a fabricated
                             or cross-campaign `cN` is visible.
    """
    if os.path.isfile(os.path.join(analysis_dir, "positions", f"{handle}.md")):
        return "bound"
    # Campaign specialist brief: cN-fM-<slug> must name an ACTUAL specialist file
    # fM-<slug>.md (slug-bound) — not merely any fM-*.md, which laundered any fabricated
    # cN-fM-<anything> handle in (the campaign-namespace evasion, closed in v0.6.0).
    #
    # RESIDUAL (deployment-tier): the slug is bound, but the campaign NUMBER `cN` and the
    # campaign DIRECTORY are not — a real fM-<slug>.md in an UNRELATED campaign still
    # resolves a cN handle nominally for another campaign (cross-campaign reuse), and the
    # parent path below binds nothing but existence. Fully binding `cN` needs a
    # cN -> campaign-directory map, a deployment naming convention (dirs are slugs, not
    # numbers), not an ARD invariant — so it is deployment-mapped, like the {N}<->bibliography
    # check (CATALOGS §3 check 7). The kernel does NOT silently bless it: a cN resolution
    # is reported "campaign-unbound" (surfaced), so a fabricated cross-campaign handle is
    # visible. A deployment binds `cN` by making the handle convention data-driven.
    m = re.match(r"^c\d+-(f\d+-.+)$", handle)
    if m and glob.glob(os.path.join(analysis_dir, "campaigns", "*", "specialists", f"{m.group(1)}.md")):
        return "campaign-unbound"
    # Campaign parent (existence-bound only; cN unbound). NOTE: `position` is NOT resolved
    # here — a position artifact resolves above via positions/<handle>.md; globbing parent.md
    # for a cN-position-* handle was a latent bug (a position handle resolving on parent
    # existence), now removed.
    if re.match(r"^c\d+-parent", handle):
        if glob.glob(os.path.join(analysis_dir, "campaigns", "*", "parent.md")):
            return "campaign-unbound"
    return None


def project_root_for(attestation_dir):
    """The project root a relative `source_path` resolves against: the parent of the
    nearest `.research` ancestor of the attestation dir (None if there is none)."""
    d = os.path.abspath(attestation_dir)
    while True:
        if os.path.basename(d) == ".research":
            return os.path.dirname(d)
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def source_path_exists(source_path, project_root):
    """`source_path` is project-root-relative (attestation contract); resolve it there
    first, then against the working directory for backward compatibility, so the lint's
    verdict no longer depends on where it is run from."""
    if os.path.isabs(source_path):
        return os.path.exists(source_path)
    if project_root and os.path.exists(os.path.join(project_root, source_path)):
        return True
    return os.path.exists(source_path)


def check_citation(handle, attestation_dir, analysis_dir, calling_prov, check_urls, handle_counts,
                   project_root=None):
    """Canonical-handle fence + six-check sequence + non-broken statuses + thin flag.
    Returns a finding dict."""
    # Canonical-handle fence (homoglyph / case): the wire-form captures [\w-]+
    # permissively (Python \w is Unicode) so malformed handles surface here rather than
    # silently matching; a *canonical* handle is ASCII-lowercase. A Cyrillic-lookalike or
    # uppercase handle is non-canonical and must not resolve silently beside the real one.
    if not re.fullmatch(r"[a-z0-9-]+", handle):
        return {"status": "non-canonical-handle", "severity": "high", "thin": False}
    path = os.path.join(attestation_dir, f"{handle}.md")
    # Check 1 — handle resolution. If not an attestation, try the analytical tier.
    if not os.path.isfile(path):
        kind = intra_program_resolves(handle, analysis_dir)
        if kind:
            f = {"status": "intra-program-resolved", "severity": "none", "thin": False}
            if kind == "campaign-unbound":
                f["campaign_unbound"] = True
            return f
        return {"status": "unresolved-handle", "severity": "high", "thin": False}
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fm = parse_frontmatter(text)
    # Frontmatter split-brain fence: a duplicated resolution-critical key (any of
    # source_handle / source_url / source_path / provenance) means this lint
    # (last-wins) and a first-wins reader disagree on the attestation's identity or
    # the source/provenance it resolves to.
    if frontmatter_duplicate_keys(text):
        return {"status": "duplicate-frontmatter-key", "severity": "high", "thin": False}
    # Check 2 — source-handle match.
    if fm.get("source_handle") != handle:
        return {"status": "mismatched-source-handle", "severity": "high", "thin": False}
    # Check 3 — handle uniqueness: the source_handle must be declared by exactly one attestation.
    if handle_counts.get(handle, 0) > 1:
        return {"status": "colliding-handle", "severity": "high", "thin": False}
    # Acquisition candidate: an intentionally-unfetched source (the acquisition-pending
    # escape hatch, SPEC §4.1) marked in frontmatter — a benign non-broken status, NOT
    # unreachable-source. Distinguishes deliberate not-yet-fetched from fabrication.
    if fm.get("acquisition_status") == "candidate":
        return {"status": "acquisition-candidate", "severity": "none", "thin": False}
    # Check 4 — source resolution. Path failures are errors; URL failures warn.
    if "source_path" in fm:
        if not source_path_exists(fm["source_path"], project_root):
            return {"status": "unreachable-source", "severity": "medium", "thin": False}
    elif "source_url" in fm:
        if check_urls and not url_alive(fm["source_url"]):
            return {"status": "unreachable-source", "severity": "low", "thin": False}  # URL=warn
    else:
        return {"status": "unreachable-source", "severity": "medium", "thin": False}
    # Check 5 — provenance present on attestation AND calling brief.
    if "provenance" not in fm or not calling_prov:
        return {"status": "missing-provenance", "severity": "low", "thin": False}
    # Resolved. Mark reduced-substrate-depth (non-broken), the GR.5 thin flag, and
    # the substrate_confidence-omission grace-period deprecation (see main()).
    thin = is_thin_attestation(body_after_frontmatter(text))
    sc = fm.get("substrate_confidence")
    # `unspecified` is the future fail-closed default — an explicit substrate gap now.
    if sc in ("search-summary", "snippet", "snippet-thin", "unspecified"):
        return {"status": "reduced-substrate-attestation", "severity": "none", "thin": thin}
    # Omission still reads source-direct (grace period) but is flagged deprecated:
    # a future MAJOR flips the default to fail-closed (omission -> unspecified -> gap).
    return {"status": "resolved", "severity": "none", "thin": thin, "sc_omitted": sc is None}


# --- Pattern-scan suppression helpers --------------------------------------
# These reduce false-positives in contexts that *usually* carry quoted or
# source-attested content (code spans, URLs, blockquotes, source-direct
# attestations). A deliberate precision-for-recall trade: an agent-authored
# claim placed in one of these contexts is no longer flagged — acceptable
# because pattern output is a warn-only spot-check aid, not a verification
# gate.

def _frontmatter_line_count(lines):
    """Return the number of lines occupied by the YAML frontmatter block (0 if absent).
    The opening and closing `---` fence lines are included in the count."""
    if not lines or lines[0].rstrip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return i + 1
    return 0


def _code_block_mask(lines):
    """Return per-line bool mask: True means the line is inside (or is) a fenced code
    block and should be fully skipped by the pattern scanner."""
    mask = [False] * len(lines)
    fence = None   # (char, length) of the open fence, or None
    for i, line in enumerate(lines):
        m = re.match(r"\s{0,3}(`{3,}|~{3,})", line)
        if fence is None:
            if m:
                fence = (m.group(1)[0], len(m.group(1)))
                mask[i] = True  # the fence line itself is also masked
        else:
            mask[i] = True
            # CommonMark: closed by a fence of the same char, at least as long, with nothing after.
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] \
                    and not line[m.end():].strip():
                fence = None
    return mask


def _is_blockquote(line):
    """True iff the line's lstrip starts with `>` (Markdown blockquote)."""
    return line.lstrip().startswith(">")


def _is_in_url(line, pos):
    """True iff character position `pos` in `line` falls inside an https?:// URL."""
    for m in re.finditer(r"https?://\S+", line):
        if m.start() <= pos < m.end():
            return True
    return False


def _is_in_inline_code(line, pos):
    """True iff character position `pos` in `line` falls inside backtick-delimited
    inline code. A span opened by a run of N backticks closes at the next run of exactly N
    (CommonMark), so double-backtick spans containing a single backtick are handled."""
    i = 0
    while i < len(line):
        if line[i] != "`":
            i += 1
            continue
        j = i
        while j < len(line) and line[j] == "`":
            j += 1
        run = j - i
        k = j
        close = None
        while k < len(line):
            if line[k] == "`":
                e = k
                while e < len(line) and line[e] == "`":
                    e += 1
                if e - k == run:
                    close = (k, e)
                    break
                k = e
            else:
                k += 1
        if close is None:
            return False   # an unmatched run opens no span
        if i <= pos < close[1]:
            return True
        i = close[1]
    return False


def _inline_code_spans(lines, skip):
    """Per-line (start, end) column ranges covered by inline code spans. CommonMark spans
    may cross line breaks within a paragraph (not blank lines), so spans are matched over
    each paragraph's joined text: a run of N backticks closes at the next run of exactly N.
    `skip` marks lines (frontmatter, fenced code) that break paragraphs and are ignored."""
    spans = {i: [] for i in range(len(lines))}
    para = []
    def flush():
        if not para:
            return
        text = "\n".join(lines[i] for i in para)
        starts, pos = [], 0
        for i in para:                       # offset of each line in the joined text
            starts.append(pos)
            pos += len(lines[i]) + 1
        k = 0
        while k < len(text):
            if text[k] != "`":
                k += 1
                continue
            e = k
            while e < len(text) and text[e] == "`":
                e += 1
            run, close, q = e - k, None, e
            while q < len(text):
                if text[q] == "`":
                    r = q
                    while r < len(text) and text[r] == "`":
                        r += 1
                    if r - q == run:
                        close = r
                        break
                    q = r
                else:
                    q += 1
            if close is None:
                k = e                        # unmatched run opens no span
                continue
            for idx, i in enumerate(para):   # project [k, close) onto each line
                a, b = starts[idx], starts[idx] + len(lines[i])
                lo, hi = max(k, a), min(close, b)
                if lo < hi:
                    spans[i].append((lo - a, hi - a))
            k = close
        para.clear()
    for i, line in enumerate(lines):
        if skip[i] or not line.strip():
            flush()
        else:
            para.append(i)
    flush()
    return spans


# Citation statuses whose attestation body can anchor a version token on the citing
# line. Not intra-program (analytical tier) or acquisition-candidate (unfetched).
ANCHOR_STATUSES = {"resolved", "reduced-substrate-attestation"}
_NUM_RUN = re.compile(r"\d+(?:\.\d+)*")


def _version_core(line, m):
    """Maximal digit/dot run overlapping the version-number match (re-joins a
    `version 1` match with the `.9.0` that follows it)."""
    for r in _NUM_RUN.finditer(line):
        if r.start() < m.end() and m.start() < r.end():
            return r.group(0)
    return None


def _attestation_has_token(core, att_body):
    """Does the attestation body carry this version token? A dotted core must appear
    as a whole number (3.1 does not match 3.12 or 13.1); an undotted core (from a
    `version N` match) must appear as `version N` or `vN`, case-insensitive."""
    if "." in core:
        return re.search(rf"(?<![\d.]){re.escape(core)}(?!\d|\.\d)", att_body) is not None
    return re.search(rf"(?i)\b(?:version|v)\s*{re.escape(core)}(?!\d|\.\d)", att_body) is not None


def _attestation_body(handle, attestation_dir, cache):
    """Attestation body (after frontmatter), read once per run via `cache`."""
    path = os.path.join(attestation_dir, f"{handle}.md")
    if path not in cache:
        with open(path, encoding="utf-8") as fh:
            cache[path] = body_after_frontmatter(fh.read())
    return cache[path]


# Version-shaped tokens that are not version claims (see _version_noise).
# Document locators: §3.1, §B.3.2, Section 3.7, sections 1, 3.3-4.2, Table 4.1, Appendix B.9.
_LOCATOR_PRE = re.compile(
    r"(?i)(?:§+\s*|\b(?:sections?|secs?\.|tables?|tabs?\.|figures?|figs?\.|"
    r"appendix|appendices|app\.|chapters?|ch\.|eqs?\.|equations?)\s+)"
    r"(?:[A-Z]?[\d.]+\s*(?:[-–,/]|and|&)\s*)*[A-Z]?\.?$")
_ARXIV_ID = re.compile(r"\d{4}\.\d{4,5}")
# "arXiv v2", "arXiv HTML v2", "arXiv 2306.05685 v4"
_ARXIV_REV_PRE = re.compile(r"(?i)\barxiv[:\s]+(?:(?:html|pdf|abs)\s+)?(?:\d{4}\.\d{4,5}\s*)?$")
_ARXIV_REV_POST = re.compile(r"(?i)\s+of\s+(?:arxiv:?\s*)?\d{4}\.\d{4,5}")  # "v4 of 2306.05685"
# Statistic words stand alone; short symbols (p, r) count only with an operator,
# so "Python 3.11 or 3.12" and "R 4.3" still fire.
_STAT_PRE = re.compile(
    r"(?i)(?:\b(?:kappa|κ|pearson|spearman|kendall|correlation|accuracy|precision|"
    r"recall|f1|auc|bleu|rouge(?:-\w+)?|score|mean|median|sd|std)\b\s*(?:of\s+|[:=]\s*)?"
    r"|[=<>≤≥≈±]\s*)$")
_STAT_CHAIN = re.compile(r"(?i)^\s*(?:\)\s*)?(?:vs\.?|versus|to|and|or|[-–/,])\s*$")
# A bibliography / references entry line names its attestation by handle:
#   "12. **handle** — Title"   "| 12 / handle | Title |"   "### 12. Title — `handle`"
_BIB_ENTRY = re.compile(
    r"^\s*(?:\d+\.\s+\*\*(?P<a>[a-z0-9][a-z0-9-]*)\*\*"
    r"|\|\s*\d+\s*/\s*(?P<b>[a-z0-9][a-z0-9-]*)\s*\|"
    r"|#{2,6}\s+\d+\.\s.*—\s*`(?P<c>[a-z0-9][a-z0-9-]*)`\s*$)")


def _bib_entry(line):
    """The bibliography-entry match on `line`, or None."""
    return _BIB_ENTRY.match(line)


def _version_noise(line, matches):
    """Start offsets of version-number matches on `line` that are not version claims:
    inside a citation or a bibliography entry's own handle; a document locator; an
    arXiv ID or revision; a percentage; or a single-dot decimal statistic (after a
    statistic word/operator, or chained from one by vs/to/and). `matches` are in
    line order; a statistic chain extends only from an excluded statistic."""
    masked = [c.span() for c in CITATION_RE.finditer(line)]
    bib = _bib_entry(line)
    if bib:
        g = next(k for k in "abc" if bib.group(k))
        masked.append(bib.span(g))
    noise, stat_end = set(), None
    for m in matches:
        tok, pre, post = m.group(0), line[:m.start()], line[m.end():]
        core = tok.lstrip("vV")
        is_stat = tok[0].isdigit() and tok.count(".") == 1 and (
            _STAT_PRE.search(pre[-28:]) is not None
            or (stat_end is not None and _STAT_CHAIN.match(line[stat_end:m.start()]) is not None))
        if is_stat:
            stat_end = m.end()
        if (is_stat
                or any(s <= m.start() < e for s, e in masked)
                or _LOCATOR_PRE.search(pre[-40:])
                or _ARXIV_ID.fullmatch(core)
                or ("." not in tok and tok[0] in "vV"
                    and (_ARXIV_REV_PRE.search(pre[-32:]) or _ARXIV_REV_POST.match(post)))
                or re.match(r"%|\s*percent\b", post)):
            noise.add(m.start())
    return noise


def lint_file(path, attestation_dir, analysis_dir, matchers, handle_counts, do_citation, do_pattern, do_thin,
              check_urls, body_cache=None, project_root=None):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fm = parse_frontmatter(text)
    calling_prov = "provenance" in fm
    # Attestation files have source-direct provenance; counts/decimals there are
    # source-attested by design, not composed claims.
    is_attestation = fm.get("provenance") == "source-direct"
    citations, patterns, thin, sc_omitted, campaign_unbound = [], [], [], set(), set()
    if do_citation:
        for m in CITATION_RE.finditer(text):
            f = check_citation(m.group(1), attestation_dir, analysis_dir, calling_prov, check_urls, handle_counts,
                               project_root)
            line = text.count("\n", 0, m.start()) + 1
            f.update({"handle": m.group(1), "n": int(m.group(2)), "line": line})
            citations.append(f)
            # Grace-period deprecation (dedup per handle): a resolved attestation that
            # omits substrate_confidence still reads source-direct but is flagged.
            if f.pop("sc_omitted", False):
                sc_omitted.add(m.group(1))
            if f.pop("campaign_unbound", False):
                campaign_unbound.add(m.group(1))
            if do_thin and f.pop("thin", False):
                thin.append({"handle": m.group(1), "line": line})
        # Citation-form fence: bare `{N}` outside frontmatter, fenced code, inline code and URLs.
        bare_scope = fm.get("provenance") in BARE_CITATION_PROVENANCE or "provenance" not in fm
        lines = text.splitlines() if bare_scope else []
        fm_skip = _frontmatter_line_count(lines)
        code_mask = _code_block_mask(lines)
        skip = [i < fm_skip or code_mask[i] for i in range(len(lines))]
        code_spans = _inline_code_spans(lines, skip)
        for lineno, line in enumerate(lines, 1):
            if skip[lineno - 1]:
                continue
            for m in BARE_CITATION_RE.finditer(line):
                if any(lo <= m.start() < hi for lo, hi in code_spans[lineno - 1]) \
                        or _is_in_url(line, m.start()):
                    continue
                citations.append({"status": "bare-citation", "severity": "high", "handle": None,
                                  "n": int(m.group(1)), "line": lineno})
    if do_pattern:
        # line -> bodies of cited attestations that can anchor a version token there.
        body_cache = {} if body_cache is None else body_cache
        anchored = {}
        for c in citations:
            if c["status"] in ANCHOR_STATUSES:
                anchored.setdefault(c["line"], []).append(
                    _attestation_body(c["handle"], attestation_dir, body_cache))
        lines = text.splitlines()
        fm_skip = _frontmatter_line_count(lines)   # number of leading lines to skip
        code_mask = _code_block_mask(lines)
        # A bibliography entry anchors its own line by the attestation it names.
        for lineno, line in enumerate(lines, 1):
            bib = None if lineno <= fm_skip or code_mask[lineno - 1] else _bib_entry(line)
            if bib:
                handle = bib.group("a") or bib.group("b") or bib.group("c")
                f = check_citation(handle, attestation_dir, analysis_dir, True, False, handle_counts,
                                   project_root)
                if f["status"] in ANCHOR_STATUSES:
                    anchored.setdefault(lineno, []).append(
                        _attestation_body(handle, attestation_dir, body_cache))
        for lineno, line in enumerate(lines, 1):
            # Skip YAML frontmatter and fenced code blocks entirely.
            if lineno <= fm_skip:
                continue
            if code_mask[lineno - 1]:
                continue
            has_cite = bool(CITATION_RE.search(line))
            in_bq = _is_blockquote(line)
            for cat, rx in matchers.items():
                noise = None
                for m in rx.finditer(line):
                    pos = m.start()
                    # Per-category suppression rules (on top of the context masks above):
                    if cat == "version-number":
                        # Version strings inside URLs or inline code are structural, not claims.
                        if _is_in_url(line, pos) or _is_in_inline_code(line, pos):
                            continue
                        if noise is None:
                            noise = _version_noise(line, list(rx.finditer(line)))
                        if pos in noise:
                            continue
                        # Anchored: the attestation tier, or a cited attestation carrying the token.
                        if is_attestation:
                            continue
                        if lineno in anchored:
                            core = _version_core(line, m)
                            if core and any(_attestation_has_token(core, b) for b in anchored[lineno]):
                                continue
                    elif cat == "count-without-unit-citation":
                        # Attestation counts are source-attested; inline-code counts are examples.
                        if is_attestation or _is_in_inline_code(line, pos):
                            continue
                        # Keep the existing same-line-citation suppression.
                        if has_cite:
                            continue
                    elif cat == "composed-effort-estimate":
                        # Quoted estimates and attestation-body content are source-direct.
                        if in_bq or is_attestation:
                            continue
                    elif cat == "decimal-with-attribution":
                        # Attestations quote decimals from source; that's the discipline working.
                        if is_attestation:
                            continue
                    elif cat == "comparative-superlative":
                        # Superlatives inside blockquotes are quoted from source.
                        if in_bq:
                            continue
                    patterns.append({"category": cat, "line": lineno, "text": line.strip()[:120]})
                    break  # one finding per category per line is enough
    return {"file": path, "citations": citations, "patterns": patterns, "thin": thin,
            "sc_omitted": sorted(sc_omitted), "campaign_unbound": sorted(campaign_unbound)}


def collect(target):
    if os.path.isfile(target):
        return [target]
    return sorted(os.path.join(r, f) for r, _, fs in os.walk(target)
                  for f in fs if f.endswith(".md"))


def _build_stats(results, attestation_dir):
    """Compute the three-part stats/audit section for --stats mode."""
    # Part 1: by-handle citation counts across all linted files.
    handle_files = {}   # handle -> list of files citing it
    for r in results:
        for c in r["citations"]:
            h = c["handle"]
            if h is None:   # bare-citation: no handle to count
                continue
            if h not in handle_files:
                handle_files[h] = []
            if r["file"] not in handle_files[h]:
                handle_files[h].append(r["file"])
    by_handle = {h: {"count": sum(1 for r in results for c in r["citations"] if c["handle"] == h),
                     "files": sorted(handle_files[h])}
                 for h in sorted(handle_files)}

    # Part 2: by-file citation counts (per-handle counts within each linted file).
    by_file = {}
    for r in results:
        counts = {}
        for c in r["citations"]:
            if c["handle"] is not None:
                counts[c["handle"]] = counts.get(c["handle"], 0) + 1
        by_file[r["file"]] = counts

    # Part 3: attestation-tier audit (walk attestation_dir independent of lint targets).
    audit_findings = []
    if os.path.isdir(attestation_dir):
        # Collision: source_handle declared by 2+ attestation files.
        sh_counts = source_handle_counts(attestation_dir)
        for sh, cnt in sorted(sh_counts.items()):
            if cnt > 1:
                audit_findings.append({"kind": "colliding-handle", "handle": sh, "count": cnt})
        # Filename-mismatch: attestation file whose stem != its source_handle frontmatter.
        # The default citation-chain check (check 2) only catches mismatches for *cited*
        # handles; an uncited drifted attestation is invisible to that check.
        for root_dir, _, fnames in os.walk(attestation_dir):
            for fname in sorted(fnames):
                if not fname.endswith(".md"):
                    continue
                stem = fname[:-3]
                fpath = os.path.join(root_dir, fname)
                try:
                    with open(fpath, encoding="utf-8") as fh:
                        sh = parse_frontmatter(fh.read()).get("source_handle")
                except OSError:
                    continue
                if sh and sh != stem:
                    audit_findings.append({"kind": "filename-mismatch", "file": fpath,
                                           "stem": stem, "source_handle": sh})

    return {"by_handle": by_handle, "by_file": by_file, "audit": audit_findings}


def main():
    ap = argparse.ArgumentParser(description="ARD citation-chain + pattern + thin lint (reference impl).")
    ap.add_argument("target", help="markdown file or directory to lint")
    ap.add_argument("--attestation-dir", default=".research/attestation")
    ap.add_argument("--analysis-dir", default=".research/analysis")
    ap.add_argument("--project-root", default=None,
                    help="root that relative attestation source_path values resolve against "
                         "(default: parent of the attestation dir's .research ancestor, else cwd)")
    ap.add_argument("--format", choices=("markdown", "json"), default="markdown")
    ap.add_argument("--exit-code-on", choices=("high", "medium", "low", "none"), default="none")
    ap.add_argument("--no-citation-check", action="store_true")
    ap.add_argument("--no-pattern-check", action="store_true")
    ap.add_argument("--no-thin-check", action="store_true")
    ap.add_argument("--no-url-check", action="store_true", help="skip the HEAD liveness check on source_url")
    ap.add_argument("--stats", action="store_true",
                    help="emit citation deployment counts + attestation-tier audit after normal lint output")
    ap.add_argument("--catalogs", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalogs.json"),
                    help="generated catalog data (pattern categories + chain statuses); falls back to built-ins if absent")
    args = ap.parse_args()

    matchers, non_broken = load_catalog_config(args.catalogs)
    handle_counts = source_handle_counts(args.attestation_dir)
    project_root = args.project_root or project_root_for(args.attestation_dir)
    body_cache = {}   # attestation path -> body, shared across files (one read per run)

    results = [lint_file(p, args.attestation_dir, args.analysis_dir, matchers, handle_counts,
                         not args.no_citation_check, not args.no_pattern_check,
                         not args.no_thin_check, not args.no_url_check, body_cache, project_root)
               for p in collect(args.target)]

    broken = [c for r in results for c in r["citations"] if c["status"] not in non_broken]
    thin_all = [(r["file"], t) for r in results for t in r["thin"]]
    # Grace-period deprecation: resolved attestations omitting substrate_confidence
    # (deduped across files). Warn-only — does not contribute to exit-code severity.
    sc_omitted_all = sorted({h for r in results for h in r["sc_omitted"]})
    # cN- campaign handles whose campaign number the kernel cannot bind (deployment-mapped):
    # surfaced (not silently clean) so a fabricated / cross-campaign handle stays visible.
    # Warn-only — does not contribute to exit-code severity.
    campaign_unbound_all = sorted({h for r in results for h in r["campaign_unbound"]})
    worst = max([SEVERITY_RANK[c["severity"]] for c in broken]
                + [SEVERITY_RANK["low"]] * bool(thin_all), default=0)

    stats = _build_stats(results, args.attestation_dir) if args.stats else None
    # Stats audit findings (collision, filename-mismatch) count as high severity.
    if stats and stats["audit"]:
        worst = max(worst, SEVERITY_RANK["high"])

    if args.format == "json":
        payload = {"results": results, "broken_chains": broken, "thin_attestations": thin_all,
                   "substrate_confidence_omitted": sc_omitted_all,
                   "campaign_unbound": campaign_unbound_all}
        if stats is not None:
            payload["stats"] = stats
        print(json.dumps(payload, indent=2))
    else:
        for r in results:
            flags = [c for c in r["citations"] if c["status"] not in non_broken]
            notes = [c for c in r["citations"] if c["status"] in non_broken and c["status"] != "resolved"]
            if not (flags or notes or r["patterns"] or r["thin"]):
                continue
            print(f"\n## {r['file']}")
            for c in flags:
                cite = f"[{c['handle']}]{{{c['n']}}}" if c["handle"] else f"{{{c['n']}}}"
                print(f"  [{c['severity']}] L{c['line']} {cite} → {c['status']}")
            for c in notes:
                print(f"  [info] L{c['line']} [{c['handle']}]{{{c['n']}}} → {c['status']}")
            for t in r["thin"]:
                print(f"  [warn] L{t['line']} [{t['handle']}] → thin-attestation (GR.5)")
            for p in r["patterns"]:
                print(f"  [warn] L{p['line']} {p['category']}: {p['text']}")
        n_ok = sum(1 for r in results for c in r["citations"] if c["status"] in non_broken)
        print(f"\n{len(results)} file(s) · {n_ok} resolved/non-broken citation(s) · "
              f"{len(broken)} broken · {len(thin_all)} thin · "
              f"{sum(len(r['patterns']) for r in results)} pattern flag(s)")
        if sc_omitted_all:
            print(f"\n[deprecation] {len(sc_omitted_all)} cited attestation(s) omit "
                  f"substrate_confidence — omission defaults to source-direct (DEPRECATED; a "
                  f"future MAJOR makes it fail-closed: omission → unspecified → substrate gap). "
                  f"Declare it explicitly.")
            if args.stats:
                for h in sc_omitted_all:
                    print(f"  - {h}")
        if campaign_unbound_all:
            print(f"\n[note] {len(campaign_unbound_all)} intra-program handle(s) resolve by "
                  f"slug/existence but the kernel cannot bind the campaign number cN "
                  f"(deployment-mapped, like the 7th bibliography-correspondence check) — confirm each cN names the "
                  f"intended campaign:")
            for h in campaign_unbound_all:
                print(f"  - {h}")
        if stats is not None:
            print("\n### Citation deployment stats")
            print("\n#### By handle")
            for h, info in stats["by_handle"].items():
                print(f"  {h}: {info['count']} citation(s) in {len(info['files'])} file(s)")
            print("\n#### By file")
            for fpath in sorted(stats["by_file"]):
                counts = stats["by_file"][fpath]
                if counts:
                    parts = ", ".join(f"{h}×{n}" for h, n in sorted(counts.items()))
                    print(f"  {fpath}: {parts}")
            print("\n#### Attestation-tier audit")
            if stats["audit"]:
                for finding in stats["audit"]:
                    if finding["kind"] == "colliding-handle":
                        print(f"  [high] colliding-handle: [{finding['handle']}] declared by "
                              f"{finding['count']} attestation files")
                    elif finding["kind"] == "filename-mismatch":
                        print(f"  [high] filename-mismatch: {finding['file']} "
                              f"(stem={finding['stem']!r}, source_handle={finding['source_handle']!r})")
            else:
                print("  no audit findings")

    threshold = SEVERITY_RANK[args.exit_code_on]
    sys.exit(1 if threshold and worst >= threshold else 0)


if __name__ == "__main__":
    main()
