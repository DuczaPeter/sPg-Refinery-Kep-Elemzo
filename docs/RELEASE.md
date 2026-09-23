# Release process

Canonical baseline: `index.html`  
Version: **V1.40R23R6 Freight Material Evidence Adjudicator**  
SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

For documentation/repository-only release work, `index.html` must remain byte-identical. NO MATCH = FAIL.

Run static gate with `python tools/check-release.py`. This is static validation only and never substitutes for browser/runtime evidence.

Runtime evidence is documented in `DEVELOPMENT/VALIDATION_R23R6_HU.md`, `DEVELOPMENT/VALIDATION_R23R6_EN.md` and `test-artifacts/R23R6/validation-summary.json`.

Final checksums are stored in `CHECKSUMS.sha256`.

The project license is not yet explicitly selected by the owner. Per Standard V4.1, the AI does not choose it. Current public-release status remains **BLOCKED** until that gate is resolved.
