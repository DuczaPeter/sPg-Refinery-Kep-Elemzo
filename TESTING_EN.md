# Testing and release gates — English

## Core rule

**Never claim runtime PASS for a run that was not actually executed.**

## 1. Static minimum

After every code change:
- JavaScript syntax/parse check;
- `index.html` must remain the single-file release artifact;
- no new required local `.js`, `.css`, image or data dependency;
- verify the change did not leak outside its intended scope.

Helper:

`python tools/verify_release.py`

## 2. Targeted OCR testing

For OCR changes, first run only the relevant hand-verified ground-truth images. The public repository does not distribute the screenshots; it contains only the manifest:

[`GROUND_TRUTH.csv`](GROUND_TRUTH.csv)

Primary quality target:

**false accepted row = 0**

If a value cannot be proven, review is better than a wrong automatic row.

## 3. Known ground truth

24 hand-verified target examples are documented:
- 19 Gemstone;
- 5 Freight/Ore.

The manifest records expected material, Quality and amount.

## 4. Combined regression

Before broad OCR releases, when private fixtures are available:
- 90 images;
- 56 Freight/Ore;
- 34 Gemstone;
- expected recognized rows: 90;
- expected review rows: 0;
- expected hand-verified targets: 24/24 exact PASS;
- expected Ore total: 48.745 SCU;
- expected Gemstone total: 1504 pieces.

This validates the specific Star Citizen UI/version and screenshot set, not every future patch.

## 5. Export regression

Verify:
- Ore A–Z → Gemstone A–Z;
- Quality ascending within the same material;
- SCU/cSCU max 3 decimals;
- no binary floating-point artifacts;
- UEX demand numeric `0` stays `0`;
- missing demand remains missing;
- category Ore/Gemstone correct;
- clear status for rows without UEX sale data;
- DC output format correct and UI rows remain unchanged.

## 6. Scope regression

A Gemstone fix must not alter Freight/Ore.
A Freight/Ore fix must not alter Gemstone.
A UI/export fix must not change OCR recognition.

## 7. New Star Citizen patch/UI

A new patch, resolution or UI layout requires new screenshot ground truth. Old PASS results are not sufficient.
