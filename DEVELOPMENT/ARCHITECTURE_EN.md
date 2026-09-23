# Technical architecture — English

## Release model

Runtime is one `index.html` with inline CSS and JavaScript. No build system and no project-owned backend.

Remote runtime dependencies:
- Tesseract.js 5.1.1;
- Tesseract core/English OCR assets resolved by upstream runtime;
- Google Fonts;
- UEX API 2.0.

## Main flow

1. Load image.
2. Decode locally in browser.
3. UI-type detection gate.
4. Targeted crops.
5. Multiple OCR/evidence sources.
6. Branch-specific adjudication.
7. Structured row.
8. Common ordering.
9. Optional Material+Q merge.
10. Optional UEX lookup.
11. CSV/JSON/DC export.

## OCR workers

`Tesseract.createWorker('eng', 1, ...)`.

Target worker count is 3 when `navigator.hardwareConcurrency >= 8`, otherwise 2.

OCR cache keys include the algorithm revision, so cache evidence is revision-sensitive.

## Material catalog

Key functions:
- `refreshMaterialCatalog`
- `rebuildMaterialCatalog`
- `addMaterialAlias`
- `bestMaterialMatch`
- `freightMaterialMatchRank`
- `chooseFreightMaterialMatch`

UEX augments the built-in fallback material set.

### R23R5 ownership guard

A UEX parent/root group cannot claim another canonical material's exact name as an alias.

### R23R6 evidence adjudicator

Freight material selection now compares evidence across crop sources instead of using first-match-wins logic.

Conceptual strength:
1. exact canonical;
2. exact manual alias;
3. exact alias / compact;
4. clipped/edge;
5. partial;
6. ngram;
7. fuzzy.

This resolves cases where a narrow crop reads noisy `won S00` while the full left block clearly reads `Iron S00`.

## Freight/Ore pipeline

Important functions:
- `detectFreightTooltipRegion`
- `detectFreightTooltipRegionFromAmountCell`
- `parseFreightTooltipText`
- `recognizeFreightStructuredFields`
- `chooseFreightQualityConsensus`
- `chooseFreightAmountConsensus`
- `analyzeFreightAmountSixEightTopology`
- `tryFreightPrimaryRowCrosscheck`
- `selectFreightSingleLegacyStructuredRescue`
- `selectFreightStructuredQCrosssourceRescue`
- `selectFreightR23R3EvidenceRescue`
- `recognizeFreightTooltip`

R23R4 introduced/retained:
- cross-crop Q conflict adjudication;
- constrained 6/8 amount pixel-topology resolver;
- awareness that preprocessing variants of the same crop are correlated evidence.

## Gemstone pipeline

Key functions:
- `detectSelectedGemstoneCard`
- `detectSelectedGemstoneCountBadgeByBackground`
- `recognizeSelectedCardQuality`
- `analyzeGemstoneBadgeDigitSlots`
- `analyzeGemstoneBadgeDigitMorphology`
- `adjudicateGemstoneCountWithDigitMorphology`
- `recognizeGemstoneBadgeCandidate`
- `recognizeGemstoneStackCount`
- `recognizeGemstoneFreightRow`
- `recognizeGemstoneTooltipDirect`

Inventory quantity is the `Xnn` count. `0.001 SCU` is unit size only.

## Refinery Work Order pipeline

Main elements:
- `detectRefineryWorkOrderGrid`
- `recognizeRefineryScreenMetadata`
- `parseRefineryHeaderMetadata`
- `buildRefineryJobSignature`
- `applyRefineryWorkOrderSnapshotDedupe`

The current 109-image R23R6 Freight-only regression is not a fresh Refinery regression.

## Row model

Typical fields:
- `source`
- `material`
- `quality`
- `screenType`
- `amountKind`
- `count`
- `scu` / `cscu`
- `freightActualScu`
- `freightCapacityScu`
- refinery metadata
- `confidence`
- `raw`

## Ordering

Key functions:
- `rowMaterialCategoryRank`
- `compareMaterialNamesGrouped`
- `sortRowsAlphabetically`

Required global rule:

**Ore A–Z → Gemstone A–Z → ascending Q.**

## Export

- `mergeRows`
- `buildDiscordInventoryRows`
- `buildDiscordInventoryText`
- `copyDiscordInventory`
- `exportCsv`
- `exportJson`

DC copy may merge rows in copied output, but must not mutate source UI rows.

## UEX

- `fetchJson`
- `fetchCommodityPrices`
- `refreshSystems`
- `fetchAllPrices`

API base: `https://api.uexcorp.uk/2.0`.

## Diagnostics

Detailed OCR timing and debug logs are evidence for troubleshooting. Raw logs are not included in the public release.
