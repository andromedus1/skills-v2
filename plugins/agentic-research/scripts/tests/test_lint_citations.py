#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Deployment tests for the kernel citation lint's project-root `source_path` resolution.

An attestation's `source_path` is project-root-relative. The lint used to resolve it
against the working directory, so running it from inside `.research/` reported false
`unreachable-source` findings. Builds a temp project and runs the real lint as a
subprocess from several working directories. Fully offline; run with `python3`.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
LINT = os.path.normpath(os.path.join(HERE, os.pardir, os.pardir, "ard-core", "kernel",
                                     "lint-citations.py"))


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def attestation(handle, source_path):
    return (f"---\nsource_handle: {handle}\nfetched: 2026-10-20\nsource_path: {source_path}\n"
            f"provenance: source-direct\nsubstrate_confidence: source-direct\n---\n\n"
            f"Summary of the source.\n\n> A key passage (§1).\n")


class ProjectRootSourcePath(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.realpath(self.tmp.name)
        research = os.path.join(self.root, ".research")
        write(os.path.join(self.root, "data", "source.txt"), "source\n")
        write(os.path.join(research, "attestation", "present-src.md"),
              attestation("present-src", "data/source.txt"))
        write(os.path.join(research, "attestation", "missing-src.md"),
              attestation("missing-src", "data/absent.txt"))
        write(os.path.join(research, "attestation", "absolute-src.md"),
              attestation("absolute-src", os.path.join(self.root, "data", "source.txt")))
        write(os.path.join(research, "analysis", "briefs", "b.md"),
              "---\nprovenance: agent-synthesis\n---\n\n"
              "Claim [present-src]{1}. Claim [missing-src]{2}. Claim [absolute-src]{3}.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def lint(self, cwd, attestation_dir, target, *extra):
        proc = subprocess.run(
            [sys.executable, LINT, target, "--attestation-dir", attestation_dir,
             "--no-url-check", "--format", "json", *extra],
            cwd=cwd, capture_output=True, text=True)
        self.assertIn(proc.returncode, (0, 1), proc.stderr)
        out = json.loads(proc.stdout)
        return {c["handle"]: c["status"] for r in out["results"] for c in r["citations"]}

    def assert_verdicts(self, got):
        self.assertEqual(got["present-src"], "resolved")
        self.assertEqual(got["absolute-src"], "resolved")
        self.assertEqual(got["missing-src"], "unreachable-source")

    def test_from_project_root(self):
        self.assert_verdicts(self.lint(self.root, ".research/attestation",
                                       ".research/analysis/briefs/b.md"))

    def test_from_inside_research_dir(self):
        research = os.path.join(self.root, ".research")
        self.assert_verdicts(self.lint(research, "attestation", "analysis/briefs/b.md"))

    def test_from_unrelated_cwd_with_absolute_dirs(self):
        with tempfile.TemporaryDirectory() as elsewhere:
            self.assert_verdicts(self.lint(
                elsewhere, os.path.join(self.root, ".research", "attestation"),
                os.path.join(self.root, ".research", "analysis", "briefs", "b.md")))

    def test_explicit_project_root_without_research_ancestor(self):
        # An attestation dir outside any `.research/` resolves via --project-root.
        moved = os.path.join(self.root, "att")
        os.rename(os.path.join(self.root, ".research", "attestation"), moved)
        with tempfile.TemporaryDirectory() as elsewhere:
            target = os.path.join(self.root, ".research", "analysis", "briefs", "b.md")
            got = self.lint(elsewhere, moved, target)
            self.assertEqual(got["present-src"], "unreachable-source")
            self.assert_verdicts(self.lint(elsewhere, moved, target, "--project-root", self.root))


if __name__ == "__main__":
    unittest.main()
