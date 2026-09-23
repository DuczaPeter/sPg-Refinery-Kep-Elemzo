# Technikai architektúra — magyar

## Kiadási modell

A runtime egyetlen `index.html`. CSS és JavaScript inline. Nincs build-rendszer és nincs saját backend.

Távoli runtime függőségek:
- Tesseract.js 5.1.1;
- Tesseract core/angol OCR assetek upstream feloldással;
- Google Fonts;
- UEX API 2.0.

## Fő adatfolyam

1. Kép betöltése.
2. Helyi böngészős dekódolás.
3. UI-típus felismerési gate.
4. Célzott cropok.
5. Több OCR/evidence source.
6. Branch-specifikus adjudikáció.
7. Strukturált sor.
8. Közös rendezés.
9. Opcionális Material+Q merge.
10. Opcionális UEX.
11. CSV/JSON/DC export.

## OCR worker modell

`Tesseract.createWorker('eng', 1, ...)`.

Ha `navigator.hardwareConcurrency >= 8`, cél 3 worker; gyengébb gépen 2.

Az OCR cache kulcsában szerepel az OCR algoritmus revision, ezért új algoritmusverziónál a korábbi cache nem tekintendő azonos bizonyítéknak.

## Material katalógus

Fő függvények:
- `refreshMaterialCatalog`
- `rebuildMaterialCatalog`
- `addMaterialAlias`
- `bestMaterialMatch`
- `freightMaterialMatchRank`
- `chooseFreightMaterialMatch`

A UEX katalógus kiegészíti a beépített fallback material-listát.

### R23R5 guard

Egy UEX parent/root csoport nem sajátíthatja ki egy másik canonical material pontos nevét.

### R23R6 adjudicator

A Freight material eredmény több OCR-crop bizonyítékából dönt. Nem first-match-wins.

Prioritási elv:
1. exact canonical;
2. exact manual alias;
3. exact alias / compact;
4. clipped/edge;
5. partial;
6. ngram;
7. fuzzy.

Ez oldja meg azt az esetet, amikor a szűk crop `won S00` zajt ad, miközben a teljes bal blokk `Iron S00`.

## Freight/Ore pipeline

Fontos függvények:
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

R23R4 fontos védelmek:
- cross-crop Q konfliktus adjudikáció;
- constrained 6/8 amount pixel-topology resolver;
- correlated preprocessing evidence nem automatikusan független proof.

## Gemstone pipeline

Fő függvények:
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

A készlet mennyisége `Xnn` darab, a `0.001 SCU` csak unit-size.

## Refinery Work Order pipeline

Fő elemek:
- `detectRefineryWorkOrderGrid`
- `recognizeRefineryScreenMetadata`
- `parseRefineryHeaderMetadata`
- `buildRefineryJobSignature`
- `applyRefineryWorkOrderSnapshotDedupe`

Az aktuális R23R6 Freight-only 109 képes regresszió nem minősül friss Refinery regressziónak.

## Sor-modell

Tipikus mezők:
- `source`
- `material`
- `quality`
- `screenType`
- `amountKind`
- `count`
- `scu` / `cscu`
- `freightActualScu`
- `freightCapacityScu`
- refinery meta mezők
- `confidence`
- `raw`

## Rendezés

Fő függvények:
- `rowMaterialCategoryRank`
- `compareMaterialNamesGrouped`
- `sortRowsAlphabetically`

Kötelező globális sorrend:

**Ore A–Z → Gemstone A–Z → Q növekvő.**

## Export

- `mergeRows`
- `buildDiscordInventoryRows`
- `buildDiscordInventoryText`
- `copyDiscordInventory`
- `exportCsv`
- `exportJson`

DC copy összevonhat az export-szövegben, de nem módosíthatja a UI eredeti sorait.

## UEX

- `fetchJson`
- `fetchCommodityPrices`
- `refreshSystems`
- `fetchAllPrices`

API base: `https://api.uexcorp.uk/2.0`.

## Diagnosztika

A részletes OCR timing és debug log a hibák bizonyítására szolgál. A raw log nem kerül a publikus release-be.
