# Release manifest

Release: **V1.40R23R6 Freight Material Evidence Adjudicator**  
Standard: **V4.2**  
Package date: **2026-09-23**

## Main artifact

- `index.html`
- SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`
- bytes: 550540
- baseline byte parity: **PASS**

## Evidence

- Source: **SOURCE VERIFIED**
- Static: **STATIC VERIFIED**
- Runtime: **RUNTIME VERIFIED**
- Integration: **NOT VERIFIED** for a fresh live UEX packaging-time run

## Runtime validation

- R23R6 Freight: 109 images / 109 rows / review 0 / 82.239 SCU / 9 critical targets
- Earlier mixed: 90 images / 56 Freight / 34 Gemstone / 24/24 critical targets

## Release status

- **PACKAGE STATUS:** **READY WITH LIMITATIONS**
- **PUBLISHED RELEASE STATUS:** **BLOCKED** — post-publish fresh-clone verification pending (REPOSITORY PUBLICATION = MANUAL BY USER)

Licence: **MIT** for original sPg code/documentation (owner decision, 2026-09-23).

`CHECKSUMS.sha256` covers every package file except itself and the two gate outputs written after the gate run (`test-artifacts/R23R6/static-release-check.txt`, `test-artifacts/R23R6/release-gate-summary.json`).

## Public package excludes

- private Star Citizen screenshots
- raw runtime logs
- secrets/tokens/API keys
- local personal paths
- bundled Tesseract/font binaries

See `docs/RELEASE_CONTRACT.md`, `docs/RELEASE_GATE_SUMMARY.md`, `PACKAGE-MANIFEST.json` and `CHECKSUMS.sha256`.
