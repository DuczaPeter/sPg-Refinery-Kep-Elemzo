# R23R6 validation evidence — English

Date: **2026-09-13**

## Runtime summary

From the user-run R23R6 browser log:

- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- images: 109
- rows: 109
- review: 0
- Freight total: 82.239 SCU
- Gemstone rows: 0
- runtime: Chrome 153 / Windows / `file:` protocol

## Critical targets

| File | Expected |
|---|---|
| ScreenShot-2026-09-13_12-16-04-47E.jpg | Tungsten Q662 / 0.449 SCU |
| ScreenShot-2026-09-13_12-16-32-105.jpg | Titanium Q622 / 0.757 SCU |
| ScreenShot-2026-09-13_12-16-43-C48.jpg | Savrilium Q905 / 0.140 SCU |
| ScreenShot-2026-09-13_12-16-56-E3F.jpg | Agricium Q588 / 0.226 SCU |
| ScreenShot-2026-09-13_12-17-11-896.jpg | Beryl Q860 / 0.617 SCU |
| ScreenShot-2026-09-13_12-17-13-1D2.jpg | Bexalite Q597 / 1.000 SCU |
| ScreenShot-2026-09-13_12-17-23-B1B.jpg | Aslarite Q575 / 0.142 SCU |
| ScreenShot-2026-09-13_12-16-15-F6E.jpg | Iron Q500 / 0.180 SCU |
| ScreenShot-2026-09-13_12-17-11-AA8.jpg | Borase Q903 / 0.636 SCU — control |

All nine appear with the expected final row in the fresh log.

## Iron bug closure

R23R5:
- full-left OCR contained `Iron S00`;
- narrow material-row crop produced noisy `won S00`;
- first-match behavior retained a fuzzy `Construction Materials` result.

R23R6:
- compares material evidence across crop sources;
- exact canonical `Iron` beats the weaker fuzzy error;
- no screenshot-name or Iron-specific hardcode.

## Limitation

This suite contains 109 Freight screenshots, so it does not by itself prove a fresh Gemstone or Refinery Work Order regression.
