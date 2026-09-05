# Technikai architektúra — magyar

## 1. Kiadási modell

A teljes alkalmazás egyetlen `index.html`. A CSS és JavaScript inline. Nincs build-lépés és nincs backend.

Távoli runtime függőségek jelenleg:
- Tesseract.js / OCR runtime;
- Tesseract English trained data;
- Google Fonts;
- UEX API 2.0.

A pontos linkek és licencek: [`../SOURCES_HU.md`](../SOURCES_HU.md) és [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

## 2. Fő adatfolyam

1. Felhasználó képeket ad hozzá.
2. A böngésző helyben betölti a képet.
3. A detector megpróbálja azonosítani a Gemstone vagy Freight/Ore UI-t.
4. A megfelelő OCR pipeline célzott cropokat készít.
5. Több OCR/evidence family eredménye kerül adjudikációra.
6. A sor objektumba kerül: material, Quality, mennyiség, típus, confidence és diagnosztikai raw mezők.
7. A UI közös comparatorral rendez.
8. Opcionális összevonás Material+Q szerint.
9. Opcionális UEX lekérés.
10. CSV, JSON vagy DC/Discord export.

## 3. Fontos függvénycsoportok

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

A selected card saját Q-ja és saját `Xnn` badge-e együtt értelmezendő.

### Freight / Ore

- `detectFreightTooltipRegionFromAmountCell`
- `parseFreightTooltipText`
- `recognizeFreightStructuredFields`
- `selectFreightConsensus`
- `tryFreightPrimaryRowCrosscheck`
- `selectFreightSingleLegacyStructuredRescue`
- `selectFreightStructuredQCrosssourceRescue`
- `recognizeFreightTooltip`

A Capacity validációs guard lehet, de nem automatikusan a készletmennyiség.

### Közös OCR orchestration

- `recognizeCanvasDetailed`
- `recognizeImage`
- `recognizeAll`

### Rendezés / export

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

## 4. Sor-modell

A felismerési sorok fő mezői a pipeline-tól függően többek között:

- `material`
- `quality`
- `screenType`
- `amountKind`
- `count` Gemstone esetén
- `scu` / `cscu` Ore/Freight esetén
- `freightActualScu`
- `freightCapacityScu`
- `confidence`
- `source`
- `raw`

Ne változtasd meg a mezők jelentését migrációs terv nélkül.

## 5. Gemstone bizonyítási modell

A fontos tanulság: az OCR-passz és a bizonyíték nem ugyanaz.

Két Tesseract futás ugyanarról a crop-ról ugyanazt a hibát ismételheti. Az evidence familykat ezért geometria, crop-forrás és preprocessing alapján kell értelmezni.

A pixel-topológiai adjudikáció csak szűk conflict resolver. A 6/9 esetnél a belső hurok függőleges pozíciója külön guard.

## 6. Freight bizonyítási modell

A structured OCR, legacy/tooltip OCR, amount evidence és Capacity guard együtt adhat cross-source megerősítést. Rescue csak már meglévő OCR jelöltek között választhat; új értéket nem generálhat.

## 7. Rendezési modell

Egyetlen közös logikai szabály:

**Ore A–Z → Gemstone A–Z → Q növekvő.**

Ha új listát készítesz, ezt a közös comparatorra építsd, ne írj külön lokális rendezést.

## 8. DC export

A DC gomb a felismert készletből Markdownot készít és vágólapra másolja.

Formátum:

`**Material**`

`Qxxx — 0,403 SCU`

vagy Gemstone esetén:

`Qxxx — 16 db`

Azonos Material+Q a DC szövegben összegezhető, de ez nem módosíthatja a képernyőn lévő eredeti sorokat.
