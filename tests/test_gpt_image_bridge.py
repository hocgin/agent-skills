"""Offline CLI regression tests; never invokes the real Codex service."""

import base64
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "skills/gpt-image-bridge/bin/gpt-image-2"
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII="
)


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="bridge-tests-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.tmp = self.root / "temporary files"
        self.tmp.mkdir()
        self.capture = self.root / "args.json"
        self.output = self.root / "output image.png"
        self.fixture = self.root / "fixture.png"
        self.fixture.write_bytes(PNG)
        self.env = dict(os.environ, PATH=f"{self.bin}:/usr/bin:/bin",
                        TMPDIR=str(self.tmp), BRIDGE_CAPTURE=str(self.capture),
                        BRIDGE_FIXTURE=str(self.fixture))
        fake = self.bin / "codex"
        fake.write_text(f"#!{sys.executable}\n" + '''
import json, os, pathlib, shutil, sys
args = sys.argv[1:]
pathlib.Path(os.environ["BRIDGE_CAPTURE"]).write_text(json.dumps(args))
if os.environ.get("BRIDGE_MODE") == "fail":
    print("simulated codex failure", file=sys.stderr)
    sys.exit(9)
if os.environ.get("BRIDGE_MODE") != "no-image":
    workdir = args[args.index("-C") + 1]
    if workdir.startswith("C:"):
        workdir = workdir[2:]
    name = "fallback.png" if os.environ.get("BRIDGE_MODE") == "fallback" else "out.png"
    shutil.copyfile(os.environ["BRIDGE_FIXTURE"], pathlib.Path(workdir) / name)
''')
        fake.chmod(0o755)

    def run_bridge(self, *options, mode="", output=None):
        return subprocess.run(
            ["/bin/bash", str(WRAPPER), "a balloon; literal $(text)",
             str(output or self.output), *options],
            cwd=self.root, env=dict(self.env, BRIDGE_MODE=mode),
            text=True, capture_output=True, timeout=10,
        )

    def args(self):
        return json.loads(self.capture.read_text())

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, f"{self.output}\n")
        self.assertEqual(self.output.read_bytes(), PNG)
        self.assertEqual(list(self.tmp.iterdir()), [])

    def test_text_only_and_cleanup(self):
        self.assert_success(self.run_bridge())
        args = self.args()
        self.assertEqual(args[:4], ["exec", "--skip-git-repo-check", "-s", "workspace-write"])
        self.assertFalse(any(arg.startswith("--image=") for arg in args))
        self.assertNotIn("REFERENCE IMAGES:", args[-1])
        self.assertIn("PROMPT: a balloon; literal $(text)", args[-1])
        self.assertNotIn(str(self.output), args[-1])

    def test_multiple_references_preserve_order_and_spaces(self):
        relative = self.root / "references with spaces" / "first image.png"
        relative.parent.mkdir()
        relative.write_bytes(PNG)
        self.assert_success(self.run_bridge(
            "--ref", "references with spaces/first image.png",
            "--size", "1024x1536", "--ref", str(self.fixture)))
        args = self.args()
        self.assertEqual([a for a in args if a.startswith("--image=")],
                         [f"--image={relative}", f"--image={self.fixture}"])
        self.assertIn("REFERENCE IMAGES: 2", args[-1])
        self.assertIn("SIZE: 1024x1536", args[-1])

    def test_relative_output_is_reported_as_absolute(self):
        self.assert_success(self.run_bridge(output="output image.png"))

    def test_missing_reference_does_not_start_codex_or_replace_output(self):
        self.output.write_bytes(b"existing output")
        result = self.run_bridge("--ref", "missing image.png")
        self.assertEqual(result.returncode, 2)
        self.assertIn("reference image not found", result.stderr)
        self.assertFalse(self.capture.exists())
        self.assertEqual(self.output.read_bytes(), b"existing output")
        self.assertEqual(list(self.tmp.iterdir()), [])

    def test_missing_option_values_are_usage_errors(self):
        for option in ("--ref", "--size"):
            for suffix in ([], [""], ["--ref", str(self.fixture)]):
                with self.subTest(option=option, suffix=suffix):
                    result = self.run_bridge(option, *suffix)
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(f"{option} requires a value", result.stderr)
                    self.assertFalse(self.capture.exists())

    def test_unknown_option(self):
        result = self.run_bridge("--invalid")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown arg", result.stderr)
        self.assertFalse(self.capture.exists())

    def test_missing_output_directory(self):
        result = self.run_bridge(output=self.root / "missing" / "out.png")
        self.assertEqual(result.returncode, 2)
        self.assertIn("output dir does not exist", result.stderr)
        self.assertFalse(self.capture.exists())

    def test_missing_codex(self):
        (self.bin / "codex").unlink()
        result = self.run_bridge()
        self.assertEqual(result.returncode, 127)
        self.assertIn("codex CLI not found", result.stderr)

    def test_no_arguments(self):
        result = subprocess.run(["/bin/bash", str(WRAPPER)], env=self.env,
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage:", result.stderr)

    def test_failures_preserve_existing_output_and_log(self):
        for mode, message in (("fail", "codex exec failed"),
                              ("no-image", "produced no PNG")):
            with self.subTest(mode=mode):
                self.output.write_bytes(b"existing output")
                result = self.run_bridge(mode=mode)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)
                self.assertIn("full log:", result.stderr)
                self.assertEqual(self.output.read_bytes(), b"existing output")
                args = self.args()
                workdir = Path(args[args.index("-C") + 1])
                self.assertTrue(workdir.is_dir())
                self.assertTrue(Path(f"{workdir}.log").is_file())

    def test_fallback_filename(self):
        self.assert_success(self.run_bridge(mode="fallback"))

    def test_cygpath_converts_reference_and_workdir(self):
        cygpath = self.bin / "cygpath"
        cygpath.write_text('#!/bin/bash\nprintf "C:%s\\n" "$2"\n')
        cygpath.chmod(0o755)
        self.assert_success(self.run_bridge("--ref", str(self.fixture)))
        args = self.args()
        self.assertIn(f"--image=C:{self.fixture}", args)
        self.assertTrue(args[args.index("-C") + 1].startswith("C:"))


if __name__ == "__main__":
    unittest.main()
