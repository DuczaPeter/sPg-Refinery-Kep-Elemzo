# Release manifest

Release: **V1.40R23R6 Freight Material Evidence Adjudicator**  
Standard: **V4.1**  
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

**BLOCKED**

Required `LICENSE STATUS RESOLVED` gate is blocked until the owner explicitly decides the original sPg project license.

## Public package excludes

- private Star Citizen screenshots
- raw runtime logs
- secrets/tokens/API keys
- local personal paths
- bundled Tesseract/font binaries

See `docs/RELEASE_CONTRACT.md`, `docs/RELEASE_GATE_SUMMARY.md`, `PACKAGE-MANIFEST.json` and `CHECKSUMS.sha256`.
