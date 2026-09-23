# Release process

Canonical baseline: `index.html`  
Version: **V1.40R23R6 Freight Material Evidence Adjudicator**  
SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

For documentation/repository-only release work, `index.html` must remain byte-identical. NO MATCH = FAIL.

Run static gate with `python tools/check-release.py`. This is static validation only and never substitutes for browser/runtime evidence.

Runtime evidence is documented in `DEVELOPMENT/VALIDATION_R23R6_HU.md`, `DEVELOPMENT/VALIDATION_R23R6_EN.md` and `test-artifacts/R23R6/validation-summary.json`.

Final checksums are stored in `CHECKSUMS.sha256`.

Project licence: **MIT** for original sPg code/documentation, selected by the owner on 2026-09-23 (Standard V4.2 §38: the AI does not choose licences).

Checksums and manifest are regenerated with `python tools/build-manifest.py` before the gate runs; gate outputs are written with `WRITE_GATE_SUMMARY=1 python tools/check-release.py`.

Publish with git or GitHub Desktop (the web uploader omits dot-prefixed files), then run the gate again on a fresh clone of the published repository. REPOSITORY PUBLICATION = MANUAL BY USER, so the PUBLISHED RELEASE STATUS stays BLOCKED until that check passes.
