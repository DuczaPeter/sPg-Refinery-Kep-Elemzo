# RELEASE CONTRACT — R23R6 GitHub package

STANDARD VERSION: V4.1  
STANDARD UPDATED: 2026-09-23  
CONTRACT DATE: 2026-09-23

PROJECT TYPE: single-file browser OCR / Star Citizen fan utility  
PRIMARY LANGUAGE: Hungarian  
SECONDARY LANGUAGE: English  
CANONICAL BASELINE: `index.html` — V1.40R23R6 Freight Material Evidence Adjudicator  
MAIN ARTIFACT: `index.html`  
TARGET VERSION: documentation/repository release around unchanged R23R6 runtime artifact  
PUBLIC RELEASE: YES  
RUNTIME VALIDATION REQUIRED: YES — OCR/browser behavior is core functionality  
PACKAGE / ZIP REQUIRED: YES — explicitly requested  
LICENSE STATUS: **UNDECIDED FOR ORIGINAL sPg CODE/DOCS — REQUIRED GATE BLOCKED**  
BASELINE BYTE PARITY REQUIRED: YES

## Required gates

- Canonical baseline identified
- Main artifact identified
- Baseline byte parity
- Static validation
- Runtime validation
- Credential / secret cleanliness
- License status resolved
- Version consistency
- Regression evidence
- Documentation
- HU/EN parity
- Third-party legal/source status
- Package cleanliness
- Checksums
- Artifact consistency
- Visual documentation

## Optional gates

- Actual GitHub social-preview repository setting — optional, cannot be proven from a ZIP alone.
- Fresh live UEX integration at package time — optional for this documentation-only packaging pass.
- Fresh full Gemstone + Refinery Work Order regression on 2026-09-23 — optional because runtime HTML is byte-identical; earlier mixed evidence remains documented.

## Visuals

- Mermaid workflow in `README.md`.
- Mermaid architecture/data-flow in `docs/ARCHITECTURE_OVERVIEW.md`.

## Deviations

- The AI did not select a project license. Standard V4.1 requires the owner to decide it.
- Private Star Citizen screenshots/raw runtime logs are excluded from the public package. Derived validation summaries are public; raw fixture evidence remains private.
