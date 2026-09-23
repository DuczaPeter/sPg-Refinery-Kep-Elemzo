# R23R6 validációs bizonyíték — magyar

Dátum: **2026-09-13**

## Futási összegzés

Böngészőből kimásolt R23R6 log alapján:

- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- képek: 109
- sorok: 109
- review: 0
- Freight total: 82.239 SCU
- Gemstone sor: 0
- runtime: Chrome 153 / Windows / `file:` protokoll

## Kritikus targetek

| Fájl | Elvárt |
|---|---|
| ScreenShot-2026-09-13_12-16-04-47E.jpg | Tungsten Q662 / 0.449 SCU |
| ScreenShot-2026-09-13_12-16-32-105.jpg | Titanium Q622 / 0.757 SCU |
| ScreenShot-2026-09-13_12-16-43-C48.jpg | Savrilium Q905 / 0.140 SCU |
| ScreenShot-2026-09-13_12-16-56-E3F.jpg | Agricium Q588 / 0.226 SCU |
| ScreenShot-2026-09-13_12-17-11-896.jpg | Beryl Q860 / 0.617 SCU |
| ScreenShot-2026-09-13_12-17-13-1D2.jpg | Bexalite Q597 / 1.000 SCU |
| ScreenShot-2026-09-13_12-17-23-B1B.jpg | Aslarite Q575 / 0.142 SCU |
| ScreenShot-2026-09-13_12-16-15-F6E.jpg | Iron Q500 / 0.180 SCU |
| ScreenShot-2026-09-13_12-17-11-AA8.jpg | Borase Q903 / 0.636 SCU — kontroll |

Mind a 9 a várt végső sorral szerepel a friss logban.

## Iron hiba lezárása

R23R5-ben:
- a teljes bal OCR blokk `Iron S00` volt;
- a szűk material-row crop `won S00` jellegű zajt adott;
- a first-match döntés a fuzzy `Construction Materials` eredményt tartotta meg.

R23R6:
- több crop material evidence közös adjudikációja;
- exact canonical `Iron` erősebb a fuzzy téves találatnál;
- nincs screenshotnév- vagy Iron-specifikus hardcode.

## Korlát

Ez a suite 109 Freight képet tartalmaz, ezért önmagában nem bizonyít friss Gemstone vagy Refinery Work Order regressziót.
