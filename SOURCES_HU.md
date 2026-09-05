# Források és licencek – magyar

Ellenőrzés dátuma: **2026-09-05**. A külső feltételek változhatnak; kiadás előtt érdemes újra megnyitni a linkeket.

## 1. Star Citizen / Cloud Imperium Games / Roberts Space Industries

A program Star Citizen játékbeli UI-képernyőképekhez készült rajongói segédeszköz. A nyilvános csomag **nem tartalmazza** a fejlesztési screenshotokat.

- Hivatalos oldal: https://robertsspaceindustries.com/
- Star Citizen Fankit and Fandom FAQ: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- Terms of Service: https://robertsspaceindustries.com/en/tos/1

A projektoldalon látható disclaimer szándékosan jelzi, hogy ez nem hivatalos és nem CIG/RSI által támogatott projekt. A repo neve / GitHub Pages domainje ne próbáljon hivatalos RSI/CIG oldalt utánozni.

## 2. UEX API 2.0

A program élő market/material/system adataihoz UEX API-t használ.

- UEX: https://uexcorp.space/
- API 2.0 dokumentáció: https://uexcorp.space/api/documentation/id/home?is_kiosk=1
- Terms of Use and Privacy / API Terms: https://uexcorp.space/about/terms?is_kiosk=1&set_lang=en_US
- `GET /commodities`: https://uexcorp.space/api/documentation/id/get_commodities/
- `GET /commodities_prices`: https://uexcorp.space/api/documentation/id/get_commodities_prices/
- `GET /star_systems`: https://uexcorp.space/api/documentation/id/get_star_systems/
- Futási API base: https://api.uexcorp.uk/2.0

A UEX dokumentáció szerint az adat közösségi jelentésekből származik, hibás vagy késleltetett lehet, és az API változhat. A projektet ezért nem szabad hivatalos vagy garantált live adatforrásként bemutatni.

A jelenlegi UEX feltételek személyes / nem kereskedelmi használatot írnak le a platformra, és külön API Terms részt tartalmaznak. Nyilvános újrafelhasználás előtt mindig az aktuális feltételek az irányadók.

## 3. Tesseract.js

- Projekt: https://github.com/naptha/tesseract.js
- NPM: https://www.npmjs.com/package/tesseract.js
- Runtime verzió a release-ben: `5.1.1`
- Runtime CDN: https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js
- CDN szolgáltató / package oldal: https://www.jsdelivr.com/package/npm/tesseract.js
- Licenc: Apache License 2.0
- Licenc: https://www.apache.org/licenses/LICENSE-2.0

A Tesseract.js böngészőben futó OCR wrapper. A release nem másolja be a teljes könyvtárat, hanem CDN-ről tölti be.

## 4. Tesseract English trained data

A `Tesseract.createWorker('eng', 1, ...)` alapértelmezett angol trained data használatával fut.

- Package: https://www.npmjs.com/package/@tesseract.js-data/eng
- Repository: https://github.com/naptha/tessdata
- Alapértelmezett jsDelivr adatforrás dokumentációja: https://github.com/naptha/tessdata
- Package licenc: MIT
- MIT licenc: https://opensource.org/license/mit

Megjegyzés: a traineddata upstream tartalma Tesseract adatforrásokra épülhet; a `@tesseract.js-data/eng` NPM-csomag metadata szerint MIT licencű. A repo nem terjeszt traineddata fájlt, azt futáskor a Tesseract.js tölti be.

## 5. Google Fonts API

Az oldal két távoli webfontot használ:

- CSS API dokumentáció: https://developers.google.com/fonts/docs/getting_started
- Futási CSS kérés: https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&family=Roboto:wght@300;400;500;700;900&display=swap

### Orbitron

- Upstream: https://github.com/googlefonts/orbitron-vf
- Eredeti projekt: https://github.com/theleagueof/orbitron
- Licenc: SIL Open Font License 1.1
- Hivatalos OFL 1.1: https://openfontlicense.org/open-font-license-official-text/

### Roboto

- Upstream: https://github.com/googlefonts/roboto-2
- Licenc: Apache License 2.0
- Licencfájl: https://github.com/googlefonts/roboto-2/blob/main/LICENSE

A repo nem tartalmaz fontfájlokat; a böngésző a Google Fonts szolgáltatásból tölti őket.

## 6. Felhasználói tesztanyagok

A fejlesztéshez a felhasználó által készített Star Citizen screenshotok és runtime logok szolgáltak OCR fixture-ként és ground-truth ellenőrzésként. Ezeket a GitHub release csomag nem tartalmazza.

## 7. Saját projektkód

A `index.html` eredeti alkalmazáslogikája és a projekt dokumentációja nem Tesseract.js-, Google Fonts- vagy UEX-forráskód másolata. A külső szolgáltatásokhoz URL/API hívásokkal kapcsolódik.

A saját kódhoz ebben a csomagban nincs külön OSI open-source licenc hozzárendelve. Lásd `LICENSE.md`.
