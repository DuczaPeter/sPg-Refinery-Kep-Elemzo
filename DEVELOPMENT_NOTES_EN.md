# Development and validation notes – English

## Baseline principle

Development started from the V1.40 baseline. Throughout the repair cycles, a release gate protected already-working Ore / Freight / Refinery / UI behavior from gemstone-only fixes, and vice versa.

## Main repair cycles

| Cycle | Change | Reason |
|---|---|---|
| R1–R3 | Split gemstone Q/count evidence families, multiscale OCR, false-accept gate | multiple OCR passes of one crop must not masquerade as independent evidence |
| R4–R6 | Isolated selected gemstone count badge; thin X11/X19 digit handling | count must come from the selected card's top-right badge |
| R7–R10 | 8/9 and 6/9 digit topology, X99 rescue, crosscheck status | real screenshots produced X99→X98/X89/X95 and X19→X18 failures |
| R11–R12 | Freight structured crosscheck and Q cross-source rescue | correct Taranite/Copper/Riccite/Savrilium/Titanium rows should not remain unnecessary warn/review results |
| R13 | combined 90-image regression and 6/9 topology guard | an X16→X19 gemstone regression was exposed only in the combined run |
| R14 | unified Ore→Gemstone ordering; CSV floating-point and demand=0 fixes | every list/export should use the same structure |
| R15 | DC button | one-click Discord-ready inventory text |
| R16 | diagnostic order-label cleanup | log description matches actual ordering |
| R17 | GitHub release package, source/license panel, Tesseract 5.1.1 pin | more reproducible public release and clear source/legal attribution |

## Ground-truth method

The repairs were not based on filename or material-name hardcoding. The user supplied the correct material / Quality / SCU or count for selected Star Citizen screenshots, and runtime logs were compared against those values.

The priority was:

1. zero false-accepted rows on known fixtures;
2. then increase exact-pass coverage;
3. prefer review over guessing when evidence remains contradictory;
4. protect unrelated code/UI scope during targeted fixes.

## Combined regression snapshot

A 90-image mixed regression run was used during stabilization:

- 56 Freight/Ore images;
- 34 Gemstone images;
- known manually checked target cases passed after the fixes;
- Ore total: 48.745 SCU;
- Gemstone total: 1504 pieces.

This validation applies to the available screenshot set and is not a guarantee for future Star Citizen patches or UI changes.

## Ordering invariant

All material-facing lists share one comparator:

**Ore A–Z → Gemstone A–Z → ascending Quality within each material.**

## Public-release principle

The public GitHub package intentionally excludes Star Citizen screenshot fixtures and runtime logs. It distributes the application and documentation, not game imagery or user test data.

## R18 – developer handoff package

The public repository now includes a complete continuation package alongside the working application: `AGENTS.md`, `STATUS.md`, contribution guides, architecture, testing/release gates, AI handoff, a 24-target ground-truth manifest and a lightweight static release verifier. Private screenshot fixtures remain undistributed.
