# sPg Refinery Kép Elemző – Magyar dokumentáció

## Mi ez?

Az **sPg Refinery Kép Elemző** egy egyfájlos, böngészőben futó Star Citizen segédeszköz. A célja, hogy képernyőképekből OCR-rel felismerje a finomítói / Freight Manager készletadatokat, külön kezelje az Ore és Gemstone tételeket, majd opcionálisan UEX API-adatok alapján játékbeli eladóhelyet és becsült bevételt keressen.

A nyilvános GitHub-csomag futtatási belépési pontja az `index.html`. Nincs build-lépés, Node.js vagy külön backend.

## Miért készült?

A kézi készletfelírás sok Quality- és mennyiségi adatnál lassú és könnyű elgépelni. A fejlesztés fő célja nem az volt, hogy „mindenáron legyen OCR-találat”, hanem hogy a program:

- ne találjon ki hiányzó adatot;
- külön kezelje a Freight/Ore és Gemstone UI-t;
- a bizonytalan OCR-olvasatokat több, egymástól eltérő képkivágással és ellenőrzéssel vizsgálja;
- az ismert false accept eseteket kiszűrje;
- ugyanazt a rendezési szabályt használja a találati listán, UEX-listán, CSV/JSON exportban és Discord exportban;
- a felhasználói képeket ne küldje saját alkalmazásszerverre.

## Feldolgozási folyamat

### 1. Képek betöltése

A képek fájlválasztással / behúzással kerülnek a böngészőbe. A program helyi Object URL-ekkel dolgozik. A nyilvános csomag nem tartalmaz fejlesztési screenshotokat.

### 2. OCR

A program **Tesseract.js 5.1.1**-et használ angol OCR-modellel. Több worker fut párhuzamosan, ha a gép legalább 8 logikai CPU-szálat jelent.

A feldolgozás nem egyetlen teljes képes OCR eredményre támaszkodik. Több célzott crop, kontrasztos / szürke / binarizált variáns, PSM-beállítás és geometriai ellenőrzés kerül összevetésre.

### 3. Gemstone kezelés

Gemstone esetén a készlet mennyisége **darabszám**, nem a tooltipben látható `0,001 SCU`. A `0,001 SCU` az egy darab fizikai mérete.

A program a kiválasztott gemstone kártyához tartozó:

- anyagnevet;
- Quality értéket;
- jobb felső `Xnn` darabszám badge-et

kapcsolja össze. A fejlesztés során külön védelmek készültek az `X11 → X1`, `X19 → X18`, `X99 → X98/X89/X95`, valamint a 6/9 karaktertévesztések ellen. A pixel-topológiai ellenőrzés csak a gemstone badge ágon fut.

### 4. Freight Manager / Ore kezelés

Ore / ship-mineable képnél a tooltip tényleges SCU-mennyisége a releváns készletérték. A program külön olvassa az anyagnevet, Q-t, SCU-t és – ahol használható – a Capacity adatot. Több cross-source ellenőrzés védi az olyan eseteket, ahol egy OCR-passz például `0.493` helyett hibás számot ad.

### 5. Rendezés

Minden material-lista ugyanazt a szabályt használja:

**Ore A–Z → Gemstone A–Z → azonos anyagon belül Q növekvő.**

Ez vonatkozik:

- a felismert tételekre;
- az összevont tételekre;
- a UEX lekérés / eredmény sorrendjére;
- CSV exportra;
- JSON exportra;
- DC / Discord másolásra.

### 6. Összevonás

Az **„Azonos anyag és Q összevonása”** gomb azonos material + Quality tételeket összegez. Ore esetén SCU, gemstone esetén darabszám adódik össze.

### 7. UEX integráció

A program a **UEX API 2.0** nyilvános GET végpontjait használja:

- `/commodities` – material katalógus és névváltozatok;
- `/commodities_prices?commodity_name=...` – ár, Quality, helyszín, kereslet;
- `/star_systems` – élő rendszerlista.

A program a saját Q-értékhez legközelebbi riportált UEX Q-adatot értékeli a beállított toleranciával. Nem talál ki ismeretlen Quality-árképletet. Az UEX közösségi adatbázis, ezért az eredmény nem garantáltan azonos az aktuális live szerverrel.

### 8. Exportok

- **CSV:** Ore A–Z, majd Gemstone A–Z; normalizált SCU értékek, explicit `0` demand megőrzéssel.
- **JSON:** ugyanaz a rendezés és UEX-projekció géppel olvasható formában.
- **DC:** egy kattintással Discord Markdown kerül a vágólapra. Azonos material + Q automatikusan összeadódik a másolt szövegben, a képernyőn lévő eredeti sorok módosítása nélkül.

## DC gomb

A `2. Felismert tételek` panel jobb felső részén lévő **DC** gomb a készletet ilyen formában másolja:

**Agricium**  
Q568 — 0,403 SCU  
Q588 — 6,2 SCU

**Aphorite**  
Q500 — 16 db

A sorrend mindig Ore A–Z → Gemstone A–Z, anyagon belül Q növekvő.

## GitHub Pages telepítés

1. Hozz létre egy új GitHub repositoryt.
2. A csomag minden fájlját töltsd fel a repo gyökerébe.
3. Az `index.html` maradjon a gyökérben.
4. GitHub → **Settings → Pages**.
5. Source: **Deploy from a branch**.
6. Branch: `main`, folder: `/ (root)`.
7. Mentés után várd meg a GitHub Pages URL-t.

Az alkalmazás közvetlen `file://` megnyitással is működhet, de a böngésző CORS / vágólap / külső API szabályai miatt a GitHub Pages vagy más HTTPS tárhely megbízhatóbb.

## Adatvédelem

A program nem rendelkezik saját képfeltöltő backenddel. Az OCR a böngészőben fut. Internetkapcsolat szükséges a külső OCR-komponensek, a Google Fonts és a UEX API miatt. A debug log böngészőoldali állapotot használ.

## Fontos jogi megjegyzések

- Nem hivatalos, nem kereskedelmi Star Citizen rajongói projekt.
- Nem kapcsolódik a Cloud Imperium Games / Roberts Space Industries szervezeteihez.
- A Star Citizenhez tartozó nevek, megjelenések és játékbeli IP a megfelelő jogtulajdonosokhoz tartoznak.
- A nyilvános repo nem tartalmazza a fejlesztéshez használt Star Citizen screenshotokat.
- UEX használatnál tartsd be az aktuális UEX Terms of Use / API Terms szabályait és kvótáit.
- Harmadik fél komponenseinek licenceit a `THIRD_PARTY_NOTICES.md` és `LICENSES/` könyvtár dokumentálja.
- Az eredeti projektkódra a repository tulajdonosa külön open-source licencet nem adott meg ebben a csomagban; lásd `LICENSE.md`.

## Validációs állapot

A fejlesztés során történt egy 90 képes kombinált regressziós futás: 56 Freight/Ore és 34 Gemstone kép. A célzott, kézzel megadott ground-truth példák alapján a problémás OCR-eseteket iteratívan javítottuk. Ez tesztbizonyíték, nem általános garancia: új patch, UI-változás vagy eltérő felbontás új ellenőrzést igényelhet.
