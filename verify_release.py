#!/usr/bin/env python3
"""Lightweight repository/release checks for sPg Refinery Kép Elemző.

No external Python packages are required.
This does not replace browser/OCR runtime testing.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"PASS: {msg}")


def main() -> None:
    if not HTML.exists():
        fail("index.html missing")
    text = HTML.read_text(encoding="utf-8")

    html_files = sorted(ROOT.glob("*.html"))
    if len(html_files) != 1 or html_files[0].name != "index.html":
        fail(f"release root should contain one runtime HTML (index.html), found: {[p.name for p in html_files]}")
    ok("single runtime HTML at repository root")

    # Local required JS/CSS references would break the standalone artifact.
    local_script = re.findall(r'<script[^>]+src=["\'](?!https?://|//|data:)([^"\']+)', text, flags=re.I)
    local_css = re.findall(r'<link[^>]+href=["\'](?!https?://|//|data:)([^"\']+\.css(?:\?[^"\']*)?)["\']', text, flags=re.I)
    if local_script or local_css:
        fail(f"local runtime dependency found: scripts={local_script}, css={local_css}")
    ok("no required local JS/CSS runtime dependency")

    required_markers = [
        "Ore A–Z → Gemstone A–Z",
        "dcCopyButton",
        "buildDiscordInventoryText",
        "compareMaterialNamesGrouped",
        "selectFreightStructuredQCrosssourceRescue",
        "analyzeGemstoneBadgeDigitMorphology",
    ]
    for marker in required_markers:
        if marker not in text:
            fail(f"expected invariant/function marker missing: {marker}")
    ok("core invariant/function markers present")

    # Extract inline JS and run node --check when Node is available.
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, flags=re.I | re.S)
    inline = "\n".join(s for s in scripts if s.strip())
    if not inline.strip():
        fail("no inline JavaScript found")
    node = shutil.which("node")
    if node:
        tmp = ROOT / ".verify_release_inline_tmp.js"
        try:
            tmp.write_text(inline, encoding="utf-8")
            proc = subprocess.run([node, "--check", str(tmp)], capture_output=True, text=True)
            if proc.returncode != 0:
                print(proc.stdout)
                print(proc.stderr, file=sys.stderr)
                fail("node --check failed")
            ok("JavaScript syntax via node --check")
        finally:
            tmp.unlink(missing_ok=True)
    else:
        print("SKIP: node not installed; JavaScript syntax not checked by this helper")

    print(f"SHA256 index.html: {sha256(HTML)}")
    print("NOTE: browser/OCR runtime acceptance is still required for OCR/UI behavior changes.")


if __name__ == "__main__":
    main()
