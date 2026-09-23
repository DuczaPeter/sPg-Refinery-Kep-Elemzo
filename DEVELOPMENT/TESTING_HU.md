# Tesztelés és release gate — magyar

## Alapszabály

**Runtime PASS csak tényleges futás után mondható.**

Statikus elemzés, unit-szimuláció, logikai következtetés és célzott CLI OCR nem azonos a böngészős teljes runtime regresszióval.

## Statikus minimum

Minden módosítás után:

- `python tools/verify_release.py`;
- JavaScript parse;
- egyetlen root runtime HTML maradjon: `index.html`;
- ne legyen új kötelező helyi JS/CSS/runtime asset;
- ellenőrizd a módosítás scope-ját;
- dependency/endpoint változásnál forrás- és licencaudit.

## Targeted OCR

Az érintett branch kézzel ellenőrzött céljait futtasd először.

Manifest:
- [GROUND_TRUTH.csv](GROUND_TRUTH.csv)

Minőségi cél:
**false accepted row = 0**.

## Aktuális Freight gate — R23R6

109 képes privát Freight suite:

- expected imageCount: 109
- expected rowCount: 109
- expected reviewCount: 0
- expected totalScu: 82.239

Kritikus 9 target: lásd `VALIDATION_R23R6_HU.md`.

## Korábbi vegyes gate

90 képes suite:

- 56 Freight/Ore
- 34 Gemstone
- 90 sor
- 0 review
- 24/24 kritikus ground truth exact PASS
- Ore 48.745 SCU
- Gemstone 1504 db

Broad OCR release-nél a két suite szerepe eltér:
- 109 Freight: friss Freight regresszió;
- 90 mixed: Gemstone + Freight vegyes regressziós bizonyíték.

## Refinery Work Order

A jelenlegi R23R6 Freight suite nem teszteli. Refinery-kód módosításnál külön refinery fixture/gate szükséges.

## Export gate

Ellenőrizd:
- Ore A–Z → Gemstone A–Z;
- Q növekvő;
- max 3 tizedes;
- nincs binary float artifact;
- explicit demand `0` megmarad;
- missing/null nem válik 0-vá;
- DC copy nem módosítja UI sorokat.

## Scope gate

- Freight fix → Gemstone ne regresszáljon.
- Gemstone fix → Freight ne regresszáljon.
- Refinery fix → többi branch ne változzon bizonyítatlanul.
- UI/export fix → OCR output ne változzon indokolatlanul.

## Új SC patch/UI

Új patch, felbontás, UI-layout vagy font/rendering változás esetén új fixture és ground truth kell.
