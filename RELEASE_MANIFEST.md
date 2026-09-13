# Release manifest

Release: **V1.40R23R6 Freight Material Evidence Adjudicator**

Date: **2026-09-13**

## Runtime artifact

- `index.html`
- bytes: `550540`
- SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`
- source build filename before packaging: `sPg_Refinery_Kep_Elemzo_V1_40R23R6_Freight_Material_Evidence_Adjudicator.html`
- runtime content is unchanged during packaging

## Validation state

Fresh Freight runtime:
- 109 images
- 109 rows
- 0 review
- 82.239 SCU
- 9 documented critical targets correct

Earlier mixed regression:
- 90 images
- 56 Freight/Ore
- 34 Gemstone
- 24/24 documented critical targets exact PASS

See `STATUS.md` and `DEVELOPMENT/VALIDATION_R23R6_HU.md` / `_EN.md`.

## Repository structure

- root: runtime, primary README/legal/status/source documents
- `DEVELOPMENT/`: architecture, testing, handoff, ground truth, release notes
- `LICENSES/`: reference license texts for third-party components
- `tools/`: static verification helper
- `.github/`: issue and PR templates

## Excluded on purpose

- Star Citizen development screenshots
- raw OCR logs
- private fixture archives
- API keys/tokens
- font binaries
- Tesseract.js distribution files/traineddata binaries

Those exclusions are intentional for privacy, repository size and third-party/IP hygiene.
