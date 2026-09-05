# Tesztelés és release gate — magyar

## Alapszabály

**Nem mondunk runtime PASS-t olyan futásra, amit nem futtattunk le.**

## 1. Statikus minimum

Minden kódmódosítás után:

- JavaScript syntax/parse check;
- `index.html` továbbra is egyfájlos release legyen;
- ne legyen új kötelező helyi `.js`, `.css`, kép vagy adatfájl;
- ellenőrizd, hogy a módosítás scope-ja nem érintett-e más ágat.

A repo tartalmaz egy segédet:

`python tools/verify_release.py`

## 2. Targeted OCR teszt

OCR változásnál először csak az érintett, kézzel ellenőrzött ground-truth képeket futtasd. A publikus repo a képeket nem tartalmazza, csak a manifestet:

[`GROUND_TRUTH.csv`](GROUND_TRUTH.csv)

Ha a fixture-k helyben rendelkezésre állnak, a fájlnevet és elvárt értéket pontosan tartsd meg.

Elsődleges minőségi cél:

**false accepted row = 0**

Ha valami nem bizonyítható, review jobb, mint egy hibás automatikus sor.

## 3. Ismert ground truth

24 kézzel ellenőrzött célpélda van dokumentálva:
- 19 Gemstone;
- 5 Freight/Ore.

A manifestben minden elvárt material/Q és amount szerepel.

## 4. Kombinált regresszió

Széles OCR-változás vagy release előtt, ha a private fixture-k elérhetők:

- 90 kép;
- 56 Freight/Ore;
- 34 Gemstone;
- elvárt felismerési sor: 90;
- elvárt review: 0;
- elvárt kézzel ellenőrzött célok: 24/24 exact PASS;
- elvárt Ore összeg: 48.745 SCU;
- elvárt Gemstone összeg: 1504 db.

Ez az adott Star Citizen UI/verzió és screenshot-készlet regressziója, nem örök garancia.

## 5. Export regresszió

Ellenőrizd:

- Ore A–Z → Gemstone A–Z;
- azonos materialon belül Q növekvő;
- SCU/cSCU max. 3 tizedes;
- nincs `0.402999999...` jellegű export;
- UEX demand `0` megmarad `0`-nak;
- valóban hiányzó demand marad hiányzó;
- `category` Ore/Gemstone helyes;
- UEX nélküli sor státusza egyértelmű;
- DC formátum helyes és nem módosítja a UI sorokat.

## 6. Scope regresszió

Gemstone fixnél külön ellenőrizd, hogy Freight/Ore nem változott.
Freight/Ore fixnél külön ellenőrizd, hogy Gemstone nem változott.
UI/export fixnél az OCR eredmény ne változzon.

## 7. Új Star Citizen patch/UI

Új patch, eltérő felbontás vagy UI-layout esetén a régi PASS nem elég. Új screenshot-ground-truth kell.
