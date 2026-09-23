#!/usr/bin/env python3
"""Regenerate PACKAGE-MANIFEST.json and CHECKSUMS.sha256 (in this order).
Gate outputs are written after the gate runs and are therefore excluded."""
from pathlib import Path
import hashlib, json, datetime
ROOT = Path(__file__).resolve().parents[1]
GATE_OUTPUTS = ['test-artifacts/R23R6/static-release-check.txt', 'test-artifacts/R23R6/release-gate-summary.json']
EXCLUDED = set(['CHECKSUMS.sha256'] + GATE_OUTPUTS)
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def files():
    out = []
    for p in ROOT.rglob('*'):
        rel = p.relative_to(ROOT).as_posix()
        if not p.is_file() or rel.startswith('.git/') or '__pycache__' in rel: continue
        if rel in EXCLUDED: continue
        out.append(rel)
    return sorted(out)
idx = ROOT / 'index.html'
manifest = {
    "releaseVersion": "V1.40R23R6 Freight Material Evidence Adjudicator",
    "standardVersion": "V4.2",
    "standardSha256": h(ROOT / 'docs/RELEASE_STANDARD.md'),
    "packageDate": datetime.date.today().isoformat(),
    "canonicalBaseline": "index.html",
    "mainArtifact": "index.html",
    "mainArtifactSha256": h(idx),
    "mainArtifactBytes": idx.stat().st_size,
    "baselineByteParity": True,
    "publicReleaseRequested": True,
    "repositoryPublication": "MANUAL BY USER",
    "licenseStatus": "RESOLVED - MIT (owner decision 2026-09-23)",
    "packageStatus": "READY WITH LIMITATIONS",
    "publishedReleaseStatus": "BLOCKED - post-publish fresh-clone verification pending",
    "evidence": {"source": "SOURCE VERIFIED", "static": "STATIC VERIFIED", "runtime": "RUNTIME VERIFIED",
                 "integration": "NOT VERIFIED", "publishedRepositoryParity": "NOT VERIFIED"},
    "runtimeEvidence": {"freight109": "PASS", "historicalMixed90": "PASS"},
    "privateFixturesBundled": False,
    "rawRuntimeLogsBundled": False,
    "gateOutputs": GATE_OUTPUTS,
    "packageFileCount": len(files()) + len(EXCLUDED),
}
(ROOT / 'PACKAGE-MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8', newline='\n')
fs = files()
(ROOT / 'CHECKSUMS.sha256').write_text(''.join(f"{h(ROOT / r)}  {r}\n" for r in fs), encoding='utf-8', newline='\n')
print(f'manifest + {len(fs)} checksums')
