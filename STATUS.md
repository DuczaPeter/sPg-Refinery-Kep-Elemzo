# STATUS — sPg Refinery Kép Elemző

Last updated: **2026-09-13**

## Current baseline

- Runtime artifact: `index.html`
- APP_VERSION: **V1.40R23R6 Freight Material Evidence Adjudicator**
- OCR revision: `v140r23r6-freight-material-evidence-adjudicator`
- Architecture: one standalone HTML; embedded CSS + JavaScript
- `index.html` SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`
- `index.html` size: `550540` bytes

## Fresh browser/runtime validation — Freight suite

Source: user-run R23R6 browser log, 2026-09-13.

- imageCount: **109**
- rowCount: **109**
- reviewCount: **0**
- finalRowCount: **109**
- gemstoneRowCount: **0**
- totalScu: **82.239**
- protocol: `file:`
- browser: Chrome 153 on Windows

Critical repaired targets verified in that run:

1. `ScreenShot-2026-09-13_12-16-04-47E.jpg` — Tungsten Q662 — 0.449 SCU
2. `ScreenShot-2026-09-13_12-16-32-105.jpg` — Titanium Q622 — 0.757 SCU
3. `ScreenShot-2026-09-13_12-16-43-C48.jpg` — Savrilium Q905 — 0.140 SCU
4. `ScreenShot-2026-09-13_12-16-56-E3F.jpg` — Agricium Q588 — 0.226 SCU
5. `ScreenShot-2026-09-13_12-17-11-896.jpg` — Beryl Q860 — 0.617 SCU
6. `ScreenShot-2026-09-13_12-17-13-1D2.jpg` — Bexalite Q597 — 1.000 SCU
7. `ScreenShot-2026-09-13_12-17-23-B1B.jpg` — Aslarite Q575 — 0.142 SCU
8. `ScreenShot-2026-09-13_12-16-15-F6E.jpg` — Iron Q500 — 0.180 SCU
9. Control: `ScreenShot-2026-09-13_12-17-11-AA8.jpg` — Borase Q903 — 0.636 SCU

The Iron case specifically confirms the R23R6 material-evidence adjudicator: exact canonical `Iron` evidence correctly beats the noisy fuzzy material-row candidate.

## Earlier mixed regression evidence

A previously documented mixed suite remains important because the new 109-image run is Freight-only:

- 90 screenshots
- 56 Freight/Ore
- 34 Gemstone
- 90 recognized rows
- 0 review rows
- 24/24 hand-verified critical ground-truth targets exact PASS
- Ore total: 48.745 SCU
- Gemstone total: 1504 pieces

## What the latest run does NOT prove

Do not claim the 109-image Freight suite as a fresh full regression of:

- Gemstone badge/Q logic;
- Refinery Work Order recognition;
- every UEX endpoint;
- every browser/resolution;
- future Star Citizen UI builds.

A new Star Citizen patch, different resolution, UI redesign, browser/runtime dependency update or UEX schema change requires targeted re-validation.

## Release classification

R23R6 is the **current validated Freight baseline** and the correct source for this GitHub package. The public package preserves the exact validated runtime HTML and adds documentation only.
