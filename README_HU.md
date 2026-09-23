# sPg Refinery Kép Elemző — teljes magyar dokumentáció

## Mi ez?

Az **sPg Refinery Kép Elemző** egy böngészőben futó, egyfájlos Star Citizen segédeszköz. A felhasználó által megadott képernyőképeket helyben elemzi OCR-rel, majd strukturált material-, Quality- és mennyiségi adatokat készít belőlük.

A program fő ágai:

- **Freight Manager / Ore** felismerés;
- **Gemstone** felismerés, ahol a készlet a kártya `Xnn` darabszáma;
- **Refinery Work Order** felismerési infrastruktúra;
- **UEX API 2.0** alapú material-, rendszer-, ár- és eladóhely-adatok;
- Material + Q összevonás;
- CSV, JSON és Discord Markdown export;
- magyar és angol felület;
- részletes diagnosztikai log.

A futtatási belépési pont az `index.html`. Nincs build-lépés, Node.js-követelmény vagy saját backend.

## Aktuális verzió

**V1.40R23R6 Freight Material Evidence Adjudicator**

Az `index.html` byte-ra pontosan a 2026-09-13-án 109 Freight képpel sikeresen lefuttatott R23R6 runtime artifact. A GitHub-dokumentáció hozzáadása nem módosítja az OCR-kódot.

Részletes állapot: [STATUS.md](STATUS.md).

## Miért készült?

A Star Citizen bányászati/refinery készlet kézi felírása sok tételnél lassú, és különösen könnyű elrontani a Quality vagy a tizedes SCU értéket. A projekt ezért nem „mindenáron találatot” akar, hanem bizonyíték-alapú felismerést.

Fő alapelvek:

- hiányzó adatot nem találunk ki;
- az OCR-passzok nem automatikusan független bizonyítékok;
- bizonytalan esetben review jobb, mint egy magabiztosan hibás sor;
- material, Q és mennyiség ugyanahhoz a UI-elemhez tartozzon;
- fix fájlnév/material/szám hardcode nem lehet OCR-javítás;
- a felhasználói screenshotok nem kerülnek a projekt saját szerverére.

## Gyors használat

### 1. Képek

A **Képek** panelen:

- fájlválasztással vagy drag-and-drop módszerrel tölthetsz be képeket;
- **Beillesztés vágólapról**: támogatott böngészőben közvetlenül is beilleszthető kép;
- **Képek felismerése**: elindítja az OCR-t;
- **Mindent töröl**: üríti az aktuális munkamenet képeit és sorait;
- **1 kattintásos log**: kimásolja a hibakeresési logot;
- **UEX anyaglista frissítése**: újratölti a material katalógust;
- **Mintaadat betöltése**: UI/export próba, nem OCR-teszt.

### 2. OCR-beállítások

**Crop mód**
- Automatikus finomítópanel-vágás — alapértelmezett.
- Teljes kép — hibakereséshez/fallbackhez.

**Preprocess**
- Kontrasztos, invertált — alapértelmezett.
- Szürkeárnyalatos.
- Eredeti kép.

**Fallback full**
- ha aktív, a pipeline szükség esetén teljes képes fallbacket is enged.

### 3. Felismert tételek

A sorokban a program a képtípustól függően materialt, Q-t és mennyiséget tárol.

**Freight/Ore**
- mennyiség: tényleges SCU;
- Capacity ellenőrző guard lehet, nem automatikus készletmennyiség.

**Gemstone**
- mennyiség: a kiválasztott kártya `Xnn` badge-e;
- a tooltip `0.001 SCU` értéke egy darab fizikai mérete, nem a teljes készlet.

Gombok:
- **Új sor** — kézi sor;
- **Azonos anyag és Q összevonása** — azonos Material + Q összegzése;
- **DC** — Discord Markdown másolása.

Globális sorrend:

**Ore A–Z → Gemstone A–Z → azonos materialon belül Q növekvő.**

### 4. UEX eladóhely-keresés

A program a UEX API 2.0 nyilvános GET erőforrásait használja.

Fő funkciók:
- rendszerlista frissítése;
- material katalógus és aliasok;
- eladóhely/ár/kereslet lekérés;
- Quality tolerancia;
- távolabbi Q fallback engedélyezése.

A program nem talál ki nem dokumentált Q-árképletet. A UEX közösségi adatbázis, ezért az adat eltérhet az aktuális live szervertől.

### 5. Export

- **CSV** — táblázatos export;
- **JSON** — géppel feldolgozható export;
- **DC** — Discord Markdown.

SCU/cSCU kimenetnél a program legfeljebb 3 tizedesre normalizál, így nem kerülhet ki `0.402999999...` jellegű lebegőpontos zaj.

## Magyar / angol felület

A jobb felső **HU / EN** gombokkal váltható a felület. Az OCR továbbra is angol Tesseract modellt használ, mert a Star Citizen UI és a materialnevek angolok.

## Internetkapcsolat

Az OCR maga a böngészőben fut, de a jelenlegi release távoli runtime szolgáltatásokat használ:

- Tesseract.js 5.1.1 — jsDelivr;
- Tesseract angol OCR-adat/runtime elemek — Tesseract.js alapértelmezett feloldása;
- Google Fonts — Orbitron és Roboto;
- UEX API 2.0.

Ezért az alkalmazás nem teljesen offline.

## Adatvédelem

A projektnek nincs saját képfeltöltő backendje. A screenshotot az alkalmazás helyben dolgozza fel.

Külső hálózati kapcsolatok ettől még vannak a fent felsorolt runtime szolgáltatások felé. Normál webes működésként ezek a szolgáltatások láthatják a hálózati kéréshez szükséges adatokat, például IP-címet és böngésző-információt.

A UEX felé material/market API-kérések mennek, screenshot nem.

Részletek: [DEVELOPMENT/PRIVACY_HU.md](DEVELOPMENT/PRIVACY_HU.md).

## Jogi és licencállapot

A saját sPg alkalmazáskód és projekt-dokumentáció licence **MIT** ([LICENSE](LICENSE), állapot: [LICENSE.md](LICENSE.md)). Ez csak a projekt saját részére vonatkozik, a harmadik felek komponenseit és szolgáltatásait nem licenceli újra.

Harmadik felek:
- Tesseract.js — Apache-2.0;
- tesseract.js-core — Apache-2.0;
- `@tesseract.js-data/eng` — MIT package metadata;
- Orbitron — SIL OFL 1.1;
- Roboto — Apache-2.0;
- UEX — szolgáltatási/API feltételek;
- Star Citizen/CIG/RSI — saját ToS és fan-content szabályok.

Részletek: [SOURCES_HU.md](SOURCES_HU.md), [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Validáció

### Friss R23R6 Freight futás — 2026-09-13

- 109 kép;
- 109 eredménysor;
- 0 review;
- 82.239 SCU;
- 0 Gemstone sor ebben a tesztben.

Az Iron → Construction Materials hiba kijavítva, és a hét korábbi kritikus Q/SCU regressziós eset is helyes maradt.

### Korábbi vegyes regresszió

A korábbi dokumentált kombinált suite:

- 90 kép;
- 56 Freight/Ore;
- 34 Gemstone;
- 90 sor;
- 0 review;
- 24/24 kézzel ellenőrzött kritikus target PASS;
- 48.745 SCU Ore;
- 1504 Gemstone darab.

Ez a két teszt egymást kiegészíti. A 109 képes Freight futás nem helyettesíti a Gemstone regressziót.

## Hibajelentés

Hibánál add meg:

- a teljes screenshot fájlnevet;
- Star Citizen patch/build információt;
- böngészőt;
- program APP_VERSION értékét;
- elvárt eredményt;
- tényleges eredményt;
- az **1 kattintásos log** tartalmát.

Ha képet osztasz meg, csak akkor tedd publikus GitHub issue-ba, ha annak tartalmát valóban nyilvánossá akarod tenni.

Részletes útmutató: [DEVELOPMENT/TROUBLESHOOTING_HU.md](DEVELOPMENT/TROUBLESHOOTING_HU.md).
