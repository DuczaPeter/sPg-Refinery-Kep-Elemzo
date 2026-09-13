# Testing and release gates — English

## Core rule

**A runtime PASS requires an actual runtime run.**

Static analysis, unit simulation, logical reasoning, or targeted CLI OCR are not equivalent to a complete browser regression.

## Static minimum

After every change:

- run `python tools/verify_release.py`;
- parse JavaScript;
- keep exactly one root runtime HTML: `index.html`;
- do not add mandatory local JS/CSS/runtime assets;
- check scope;
- re-audit sources/licenses when dependencies/endpoints change.

## Targeted OCR

Run the hand-verified targets relevant to the changed branch first.

Manifest:
- [GROUND_TRUTH.csv](GROUND_TRUTH.csv)

Quality goal:
**false accepted row = 0**.

## Current Freight gate — R23R6

Private 109-image Freight suite:

- expected imageCount: 109
- expected rowCount: 109
- expected reviewCount: 0
- expected totalScu: 82.239

See `VALIDATION_R23R6_EN.md` for the nine critical targets.

## Earlier mixed gate

90-image suite:

- 56 Freight/Ore
- 34 Gemstone
- 90 rows
- 0 review
- 24/24 critical ground-truth targets exact PASS
- Ore: 48.745 SCU
- Gemstone: 1504 pieces

The suites have different purposes:
- 109 Freight: fresh Freight regression;
- 90 mixed: mixed Freight + Gemstone regression evidence.

## Refinery Work Order

The current R23R6 Freight suite does not test it. Refinery code changes require dedicated refinery fixtures and acceptance criteria.

## Export gate

Verify:
- Ore A–Z → Gemstone A–Z;
- ascending Q;
- maximum 3 decimal places;
- no binary float artifacts;
- explicit demand `0` remains `0`;
- missing/null remains missing;
- DC copy does not mutate UI rows.

## Scope gate

- Freight fix → no Gemstone regression.
- Gemstone fix → no Freight regression.
- Refinery fix → no unverified cross-branch behavior change.
- UI/export fix → OCR results should not change without reason.

## New SC patch/UI

A new Star Citizen patch, resolution, UI layout or rendering/font change requires new fixtures and ground truth.
