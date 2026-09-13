# sPg Refinery Image Analyzer — full English documentation

## What is it?

**sPg Refinery Image Analyzer** is a single-file browser utility for Star Citizen. It processes user-provided screenshots locally with OCR and converts them into structured material, Quality and quantity data.

Main branches:

- **Freight Manager / Ore** recognition;
- **Gemstone** recognition, where inventory quantity is the selected card's `Xnn` count;
- **Refinery Work Order** recognition infrastructure;
- **UEX API 2.0** material/system/price/sell-location integration;
- Material + Q merge;
- CSV, JSON and Discord Markdown export;
- Hungarian and English UI;
- detailed diagnostic logging.

The runtime entry point is `index.html`. There is no build step, Node.js requirement, or project-owned backend.

## Current release

**V1.40R23R6 Freight Material Evidence Adjudicator**

`index.html` is byte-for-byte the R23R6 runtime artifact used in the successful 109-Freight-image run on 2026-09-13. Adding this GitHub documentation package does not modify the OCR code.

See [STATUS.md](STATUS.md).

## Why does it exist?

Manually transcribing many Star Citizen mining/refinery rows is slow and makes Quality and decimal SCU mistakes easy. The project therefore prioritizes evidence-backed recognition over “always return a result”.

Core principles:

- do not invent missing values;
- OCR passes are not automatically independent evidence;
- review is better than a confidently wrong row;
- material, Q and quantity must belong to the same relevant UI element;
- never hardcode a screenshot filename/material/expected number as an OCR fix;
- user screenshots are not uploaded to a project-owned server.

## Quick usage

### 1. Images

The **Images** panel provides:

- file selection / drag and drop;
- **Paste from clipboard**;
- **Recognize images**;
- **Clear all**;
- **1-click log**;
- **Refresh UEX material list**;
- **Load demo data** — UI/export demo, not an OCR test.

### 2. OCR settings

**Crop mode**
- Automatic refinery-panel crop — default.
- Full image — diagnostics/fallback.

**Preprocess**
- Contrast/inverted — default.
- Grayscale.
- Original image.

**Full-image fallback**
- permits broader fallback recognition when needed.

### 3. Recognized items

**Freight/Ore**
- quantity is the actual SCU amount;
- Capacity can be a validity guard, not an automatic stock amount.

**Gemstone**
- quantity is the selected card's `Xnn` badge count;
- tooltip `0.001 SCU` is the physical size of one piece, not total inventory.

Actions:
- **Add row**;
- **Merge same material and Q**;
- **DC** — copy Discord Markdown.

Global order:

**Ore A–Z → Gemstone A–Z → ascending Q inside the same material.**

### 4. UEX sell-location lookup

The app uses public UEX API 2.0 GET resources for:

- system discovery;
- material catalog/aliases;
- sell prices, demand and locations;
- Quality tolerance;
- optional distant-Q fallback.

It does not invent an undocumented Quality pricing formula. UEX is community-maintained and may differ from the live game.

### 5. Export

- **CSV**
- **JSON**
- **DC / Discord Markdown**

SCU/cSCU values are normalized to at most three decimals so binary floating-point noise is not exported.

## HU / EN interface

The **HU / EN** buttons switch the UI language. OCR continues to use English Tesseract data because Star Citizen UI/material names are English.

## Internet requirement

OCR processing happens in the browser, but this release uses remote runtime services:

- Tesseract.js 5.1.1 from jsDelivr;
- Tesseract English OCR/runtime assets resolved through Tesseract.js defaults;
- Google Fonts for Orbitron and Roboto;
- UEX API 2.0.

Therefore the app is not fully offline.

## Privacy

There is no project-owned screenshot upload backend. Screenshots are processed locally.

External requests still occur to the runtime services above. Those providers can receive the normal network metadata required to serve HTTP requests, such as IP address and browser information.

UEX receives material/market API requests, not screenshots.

See [DEVELOPMENT/PRIVACY_EN.md](DEVELOPMENT/PRIVACY_EN.md).

## Legal and licensing status

The original sPg application code and project documentation currently have **no separately selected OSI open-source license**. A public GitHub repository does not itself grant reuse rights. See [LICENSE.md](LICENSE.md).

Third parties:
- Tesseract.js — Apache-2.0;
- tesseract.js-core — Apache-2.0;
- `@tesseract.js-data/eng` — MIT package metadata;
- Orbitron — SIL OFL 1.1;
- Roboto — Apache-2.0;
- UEX — service/API terms;
- Star Citizen/CIG/RSI — their own ToS and fan-content rules.

See [SOURCES_EN.md](SOURCES_EN.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Validation

### Fresh R23R6 Freight run — 2026-09-13

- 109 images;
- 109 result rows;
- 0 review rows;
- 82.239 SCU;
- 0 Gemstone rows in this specific suite.

The Iron → Construction Materials false classification is fixed and the seven previously repaired Q/SCU critical cases remain correct.

### Earlier mixed regression

Previously documented combined suite:

- 90 images;
- 56 Freight/Ore;
- 34 Gemstone;
- 90 rows;
- 0 review;
- 24/24 hand-verified critical targets PASS;
- 48.745 SCU Ore;
- 1504 Gemstone pieces.

The suites complement each other. The 109-image Freight run does not replace Gemstone regression coverage.

## Bug reports

Include:

- full screenshot filename;
- Star Citizen patch/build;
- browser;
- APP_VERSION;
- expected result;
- actual result;
- **1-click log** output.

Only attach screenshots to a public GitHub issue if you actually want those images to become public.

See [DEVELOPMENT/TROUBLESHOOTING_EN.md](DEVELOPMENT/TROUBLESHOOTING_EN.md).
