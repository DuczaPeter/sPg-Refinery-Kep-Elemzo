# sPg Refinery Image Analyzer

**Star Citizen Freight / Gemstone / Refinery OCR + UEX helper**

[Magyar](README.md) · [Status](STATUS.md) · [Release Standard](docs/RELEASE_STANDARD.md)

> Unofficial, non-commercial Star Citizen fan project. Not affiliated with, endorsed by, or approved by Cloud Imperium Games / Roberts Space Industries.

## What is it?

A single-file browser utility that turns user-provided Star Citizen screenshots into structured material, Quality and quantity data using OCR.

**Main artifact:** `index.html`  
**Current baseline:** V1.40R23R6 Freight Material Evidence Adjudicator  
**SHA-256:** `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

CSS and JavaScript are embedded in `index.html`. There is no build system and no project-owned backend.

## Main features

- Freight Manager / Ore OCR;
- Gemstone OCR with `Xnn` inventory count;
- Refinery Work Order recognition infrastructure;
- Material + Q merge;
- optional UEX API 2.0 sell/price/demand lookup;
- CSV, JSON and Discord Markdown export;
- HU / EN interface;
- detailed OCR/debug logging.

## Quick use

1. Open `index.html` or the GitHub Pages deployment.
2. Add Star Citizen screenshots.
3. Run recognition.
4. Review material / Q / quantity rows.
5. Optionally merge identical Material + Q rows.
6. Optionally query UEX.
7. Export CSV, JSON or Discord Markdown.

## R23R6 Freight material rule

Material selection is not first-match-wins. Evidence strength follows:

**exact canonical > exact manual alias > exact alias/compact > clipped/edge > partial > ngram > fuzzy**

This fixed the real Iron → Construction Materials false classification without filename/material hardcoding.

## Validation

Fresh R23R6 Freight browser run: 109 images, 109 rows, review 0, 82.239 SCU, 9 critical targets verified.

Earlier mixed regression: 90 images, 56 Freight/Ore, 34 Gemstone, review 0, 24/24 critical targets PASS, 48.745 SCU Ore, 1504 Gemstone pieces.

The suites complement each other. The fresh 109-image suite is Freight-only.

## Data sources and licenses

Tesseract.js 5.1.1, tesseract.js-core, English OCR data, jsDelivr, Google Fonts, UEX API 2.0, and Star Citizen/CIG/RSI fan-project context are documented in [SOURCES_EN.md](SOURCES_EN.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Privacy and security

There is no project-owned screenshot-upload backend. Screenshot processing happens in the browser. External requests exist for runtime dependencies and optional UEX queries.

- [PRIVACY.md](PRIVACY.md)
- [SECURITY.md](SECURITY.md)

## Known limitations

Star Citizen UI/patch changes, resolution/scaling/HDR/compression and external API changes can affect behavior. UEX is community data, not guaranteed live truth. A fresh full Gemstone and Refinery Work Order regression is not documented for 2026-09-23.

## Development / Codex

For normal development read [AGENTS.md](AGENTS.md), [STATUS.md](STATUS.md) and [DEVELOPMENT/CODEX_WORKFLOW_EN.md](DEVELOPMENT/CODEX_WORKFLOW_EN.md).

For full GitHub release/package work use [docs/RELEASE_STANDARD.md](docs/RELEASE_STANDARD.md).

## Release status

Under Standard V4.1 the release is currently **BLOCKED** by one REQUIRED gate:

**LICENSE STATUS RESOLVED** — the owner has not explicitly selected a project license for the original sPg code/documentation.

The AI does not choose that license.

- [Release Contract](docs/RELEASE_CONTRACT.md)
- [Release Gate Summary](docs/RELEASE_GATE_SUMMARY.md)
- [Release Process](docs/RELEASE.md)
- [Architecture Overview](docs/ARCHITECTURE_OVERVIEW.md)
- [CHANGELOG](CHANGELOG.md)
