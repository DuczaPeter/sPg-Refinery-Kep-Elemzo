# RELEASE CONTRACT — R23R6 GitHub package (V4.2)

STANDARD VERSION: V4.2  
STANDARD SHA-256: `f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2`  
CONTRACT DATE: 2026-09-23  
PREVIOUS PACKAGE: R23R6 GitHub package under V4.1 — HISTORICAL (release status was BLOCKED on licence)

PROJECT TYPE: single-file browser OCR / Star Citizen fan utility  
PRIMARY LANGUAGE: Hungarian  
SECONDARY LANGUAGE: English  
CANONICAL BASELINE: `index.html` — V1.40R23R6 Freight Material Evidence Adjudicator (SHA-256 `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`); repository baseline for this package: published `main` commit `a7c42bce981bc8c84621a6271ddfb6508665861e`  
MAIN ARTIFACT: `index.html`  
TARGET VERSION: documentation/repository release around unchanged R23R6 runtime artifact  
PUBLIC RELEASE: YES  
RUNTIME VALIDATION REQUIRED: YES — OCR/browser behavior is core functionality; satisfied by the existing R23R6 runtime evidence bound to the unchanged artifact SHA-256  
PACKAGE / ZIP REQUIRED: YES — explicitly requested  
REPOSITORY PUBLICATION: MANUAL BY USER  
LICENSE STATUS: **RESOLVED — MIT for original sPg code/documentation, selected by the owner on 2026-09-23**; third-party components keep their own licences/terms  
BASELINE BYTE PARITY REQUIRED: YES

## Scope of this package

- Licence gate resolved by the owner's explicit decision (MIT). The AI did not choose the licence.
- The V4.1 package was published without its dot-prefixed files (`.github/`, `.gitignore`, `.nojekyll`) although `CHECKSUMS.sha256` listed them. The files are recreated (originals unavailable; new files, new hashes).
- `.gitattributes` line-ending policy added; `DEVELOPMENT/GROUND_TRUTH.csv`, verbatim licence texts and test evidence protected with `-text`.
- HU/EN parity: the detailed Hungarian user documentation in `README_HU.md` gets an English equivalent in `README_EN.md`.
- `docs/RELEASE_STANDARD.md` replaced with the canonical V4.2 standard.
- Release gate extended (checksum existence parity, dot-prefixed files, line-ending policy, canonical standard SHA-256, licence, HU/EN section parity).

## Required gates

- Canonical baseline identified
- Main artifact identified
- Baseline byte parity
- Static validation
- Runtime validation (existing R23R6 evidence bound to unchanged SHA-256)
- Credential / secret cleanliness
- License status resolved
- Version consistency
- Regression evidence
- Documentation
- HU/EN parity (including detailed user documentation)
- Third-party legal/source status
- Package cleanliness
- Checksums
- Artifact consistency
- Visual documentation (Mermaid workflow/architecture)
- Inventory / checksum existence parity, including dot-prefixed files (V4.2 §69)
- Line-ending / `.gitattributes` policy (V4.2 §70–72)
- Canonical V4.2 standard byte identity
- Published repository parity (V4.2 §67) — MANUAL BY USER, therefore NOT VERIFIED + BLOCKED until the post-publish fresh-clone check

## Optional gates

- Actual GitHub social-preview repository setting — optional, a manual GitHub step.
- Fresh live UEX integration at package time — optional for this documentation-only packaging pass.
- Fresh full Gemstone + Refinery Work Order regression on 2026-09-23 — optional because runtime HTML is byte-identical; earlier mixed evidence remains documented.
- Real UI screenshot — optional. Not captured in this packaging environment: the app's remote fonts/OCR runtime cannot load here, so a representative screenshot is not possible. OPTIONAL BLOCKED, not N/A and not runtime evidence.

## Visuals

- Mermaid workflow in `README.md` and `README_EN.md`.
- Mermaid architecture/data-flow in `docs/ARCHITECTURE_OVERVIEW.md`.

## Deviations

- Private Star Citizen screenshots/raw runtime logs are excluded from the public package. Derived validation summaries are public; raw fixture evidence remains private.
