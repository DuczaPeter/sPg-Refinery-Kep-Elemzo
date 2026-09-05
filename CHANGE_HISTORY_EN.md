# Development history R1–R18 — English

## Baseline

The project started from a working V1.40 single-file HTML baseline. The repair strategy was to preserve the existing app and add narrowly justified guards/evidence handling for reproduced failures rather than rewrite the product.

## R1–R3

- Separated Gemstone Q/count evidence families.
- Multiple OCR passes from one crop stopped counting as automatically independent evidence.
- False-accept gate became the primary quality target.

## R4–R6

- Isolated selected gemstone card and its own upper-right `Xnn` badge.
- Improved thin-digit X11/X19 handling.
- Separated count source from name/Q OCR.

## R7–R10

- 8/9 and 6/9 digit-confusion handling.
- Multiscale and pixel-topology adjudication for X99→X98/X89/X95 classes.
- Fixed crosscheck status rendering.
- Added Feynmaline X99 noisy-family rescue.

## R11–R12

- Freight structured crosscheck.
- Capacity-unique amount guard.
- Near-jitter amount handling.
- Structured Q + independent legacy/tooltip identity cross-source rescue.

## R13

- Combined 90-image regression exposed an Aphorite X16→X19 regression.
- One interior loop no longer automatically means digit 9; vertical loop position became a 6/9 guard.

## R14

- Unified ordering everywhere: Ore A–Z → Gemstone A–Z → Quality ascending.
- Removed CSV binary floating-point artifacts.
- Preserved UEX demand numeric `0` separately from null/missing.
- Added category and UEX status export fields.

## R15

- Added DC button for one-click Discord Markdown copy.
- DC output may aggregate same Material+Q without mutating visible rows.

## R16

- Unified diagnostic ordering text.

## R17

- GitHub Pages release package.
- Hungarian/English README, source, third-party and license documentation.
- Pinned Tesseract.js runtime version.

## R18

- Full public developer handoff package.
- Added `AGENTS.md`, `STATUS.md`, contribution guides, architecture, testing, AI handoff, ground-truth manifest, release checklist and release verification helper.
- Private Star Citizen screenshot fixtures remain undistributed.
