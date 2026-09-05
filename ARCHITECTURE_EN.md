# Technical architecture — English

## 1. Release model

The entire application is shipped as a single `index.html` with embedded CSS and JavaScript. There is no build step and no backend.

Current remote runtime dependencies/services:
- Tesseract.js OCR runtime;
- Tesseract English trained data;
- Google Fonts;
- UEX API 2.0.

See [`../SOURCES_EN.md`](../SOURCES_EN.md) and [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

## 2. Main data flow

1. User adds screenshots.
2. Browser loads images locally.
3. Detection identifies Gemstone or Freight/Ore UI.
4. The relevant OCR pipeline creates targeted crops.
5. Multiple OCR/evidence families are adjudicated.
6. A row object is produced with material, Quality, amount, type, confidence and diagnostic fields.
7. UI applies the common material comparator.
8. Optional Material+Q merge.
9. Optional UEX lookup.
10. CSV, JSON or DC/Discord export.

## 3. Important function groups

### Gemstone

- `detectSelectedGemstoneCard`
- `selectedCardBadgeCandidates`
- `detectSelectedGemstoneCountBadgeByBackground`
- `recognizeSelectedCardQuality`
- `analyzeGemstoneBadgeDigitSlots`
- `analyzeGemstoneBadgeDigitMorphology`
- `adjudicateGemstoneCountWithDigitMorphology`
- `recognizeGemstoneBadgeCandidate`
- `recognizeGemstoneStackCount`
- `recognizeGemstoneFreightRow`
- `recognizeGemstoneTooltipDirect`

Selected-card Q and its own upper-right `Xnn` badge must refer to the same card.

### Freight / Ore

- `detectFreightTooltipRegionFromAmountCell`
- `parseFreightTooltipText`
- `recognizeFreightStructuredFields`
- `selectFreightConsensus`
- `tryFreightPrimaryRowCrosscheck`
- `selectFreightSingleLegacyStructuredRescue`
- `selectFreightStructuredQCrosssourceRescue`
- `recognizeFreightTooltip`

Capacity may validate physical plausibility but is not automatically the stock amount.

### OCR orchestration

- `recognizeCanvasDetailed`
- `recognizeImage`
- `recognizeAll`

### Ordering / export

- `rowMaterialCategoryRank`
- `rowMaterialCategoryLabel`
- `compareMaterialNamesGrouped`
- `sortRowsAlphabetically`
- `mergeRows`
- `buildDiscordInventoryRows`
- `buildDiscordInventoryText`
- `copyDiscordInventory`
- `exportCsv`
- `exportJson`

### UEX

- `fetchJson`
- `fetchCommodityPrices`
- `refreshSystems`
- `fetchAllPrices`

## 4. Row model

Recognition rows may contain:
- `material`
- `quality`
- `screenType`
- `amountKind`
- `count` for Gemstone
- `scu` / `cscu` for Ore/Freight
- `freightActualScu`
- `freightCapacityScu`
- `confidence`
- `source`
- `raw`

Do not silently change field semantics without a migration plan.

## 5. Gemstone evidence model

An OCR pass is not the same thing as independent evidence. Multiple Tesseract passes from the same crop can repeat the same error. Evidence families must be interpreted by geometry, crop source and preprocessing.

Pixel topology is a constrained conflict resolver. The 6/9 guard uses vertical position of the interior loop; one loop alone does not imply digit 9.

## 6. Freight evidence model

Structured OCR, legacy/tooltip OCR, amount evidence and Capacity guards can cross-validate a row. Rescue paths may choose between values already present in OCR evidence, but must not synthesize a missing value.

## 7. Ordering model

One global rule:

**Ore A–Z → Gemstone A–Z → Quality ascending.**

New lists should reuse the common comparator instead of implementing a local sort.

## 8. DC export

The DC button produces Markdown and copies it to clipboard.

Format:
- `**Material**`
- `Qxxx — 0,403 SCU`
- or `Qxxx — 16 db` for Gemstone.

Same Material+Q may be aggregated in the copied text without mutating the original UI rows.
