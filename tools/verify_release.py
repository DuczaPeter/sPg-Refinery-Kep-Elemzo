#!/usr/bin/env python3
"""Static release verifier for sPg Refinery Kép Elemző.

No external Python packages required.
This is NOT a replacement for browser/OCR runtime testing.
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
EXPECTED_VERSION = "V1.40R23R6 Freight Material Evidence Adjudicator"
EXPECTED_REV = "v140r23r6-freight-material-evidence-adjudicator"
EXPECTED_SHA = "a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128"

def fail(msg: str) -> None:
    print("FAIL:", msg)
    raise SystemExit(1)

def ok(msg: str) -> None:
    print("PASS:", msg)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    if not HTML.exists():
        fail("index.html missing")
    text = HTML.read_text(encoding="utf-8")

    roots = sorted(ROOT.glob("*.html"))
    if [p.name for p in roots] != ["index.html"]:
        fail(f"root runtime HTML set is not exactly index.html: {[p.name for p in roots]}")
    ok("single root runtime HTML")

    if EXPECTED_VERSION not in text:
        fail("APP_VERSION marker missing/wrong")
    if EXPECTED_REV not in text:
        fail("OCR_ALGORITHM_REVISION marker missing/wrong")
    ok("R23R6 version markers")

    if sha256(HTML) != EXPECTED_SHA:
        fail("index.html differs from validated R23R6 artifact")
    ok("validated index.html SHA-256")

    local_script = re.findall(r'<script[^>]+src=["\'](?!https?://|//|data:)([^"\']+)', text, re.I)
    local_css = re.findall(r'<link[^>]+href=["\'](?!https?://|//|data:)([^"\']+\.css(?:\?[^"\']*)?)["\']', text, re.I)
    if local_script or local_css:
        fail(f"mandatory local runtime dependency found: scripts={local_script}, css={local_css}")
    ok("no mandatory local JS/CSS dependency")

    markers = [
        "chooseFreightMaterialMatch",
        "freightMaterialMatchRank",
        "chooseFreightQualityConsensus",
        "chooseFreightAmountConsensus",
        "analyzeFreightAmountSixEightTopology",
        "analyzeGemstoneBadgeDigitMorphology",
        "compareMaterialNamesGrouped",
        "buildDiscordInventoryText",
        "https://api.uexcorp.uk/2.0",
        "tesseract.js@5.1.1",
    ]
    for marker in markers:
        if marker not in text:
            fail(f"required marker missing: {marker}")
    ok("core R23R6 markers present")

    # No known private fixture filenames may be hardcoded into runtime.
    if "ScreenShot-2026-09-13" in text or "ScreenShot-2026-09-04" in text:
        fail("private fixture filename hardcoded in index.html")
    ok("no known private fixture filename hardcode")

    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.I | re.S)
    inline = [s for s in scripts if s.strip()]
    if not inline:
        fail("no inline JavaScript")
    node = shutil.which("node")
    if node:
        for i, js in enumerate(inline, 1):
            tmp = ROOT / f".verify_release_inline_{i}.js"
            try:
                tmp.write_text(js, encoding="utf-8")
                p = subprocess.run([node, "--check", str(tmp)], capture_output=True, text=True)
                if p.returncode:
                    print(p.stdout)
                    print(p.stderr, file=sys.stderr)
                    fail(f"node --check failed for inline script {i}")
            finally:
                tmp.unlink(missing_ok=True)
        ok(f"JavaScript syntax via node --check ({len(inline)} inline blocks)")
    else:
        print("SKIP: node not installed")

    forbidden = list(ROOT.rglob("ScreenShot-*.jpg")) + list(ROOT.rglob("ScreenShot-*.png"))
    forbidden += list(ROOT.rglob("*.txt-be"))
    if forbidden:
        fail(f"private fixture/log files found: {[str(p.relative_to(ROOT)) for p in forbidden]}")
    ok("no private screenshot/raw-log artifacts")

    print("SHA256 index.html:", sha256(HTML))
    print("NOTE: browser/OCR runtime acceptance is still required after behavioral changes.")

if __name__ == "__main__":
    main()
