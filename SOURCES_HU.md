# Források, adatforrások és licencek — magyar

Ellenőrzés dátuma: **2026-09-13**

A külső licencek, API-k és szolgáltatási feltételek változhatnak. Új release előtt ezeket újra ellenőrizni kell.

## 1. Star Citizen / CIG / RSI

Felhasználás: fan-project kontextus, játékon belüli UI és materialnevek.

- Hivatalos oldal: https://robertsspaceindustries.com/
- Fan Content Guidance: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- Terms of Service: https://robertsspaceindustries.com/en/tos/1

A 2026-09-02-án frissített fan FAQ alapján a fan oldalaknak egyértelművé kell tenniük, hogy nem hivatalosak és nem CIG/RSI által támogatottak. A projekt ezt a disclaimert a UI-ban és a dokumentációban is megjeleníti.

A nyilvános repo nem terjeszti a fejlesztéshez használt Star Citizen screenshotokat.

## 2. UEX API 2.0

Felhasználás:
- material katalógus és aliasok;
- commodity price/sell-location/demand adatok;
- Star System lista.

Runtime base:
- https://api.uexcorp.uk/2.0

Dokumentáció:
- https://uexcorp.space/api/documentation/id/home?is_kiosk=1

Terms:
- https://uexcorp.space/about/terms?is_kiosk=1&set_lang=en_US

A 2026-07-02-i Terms szerint:
- a platform közösségi adatforrás;
- az adat nem garantáltan pontos vagy teljes;
- személyes, nem kereskedelmi használatra szól;
- az API work in progress;
- endpointok módosíthatók vagy eltávolíthatók.

A program kritikus adatnál ezért nem állít hivatalos/live garanciát.

## 3. Tesseract.js 5.1.1

Felhasználás: browser OCR.

- Projekt: https://github.com/naptha/tesseract.js
- Runtime script: https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js
- Licenc: Apache-2.0
- Upstream licence: https://github.com/naptha/tesseract.js/blob/master/LICENSE.md

A repo nem másolja be a Tesseract.js disztribúciót; a script futáskor CDN-ről érkezik.

## 4. tesseract.js-core

Felhasználás: Tesseract.js által használt OCR core/WASM.

- Projekt: https://github.com/naptha/tesseract.js-core
- Licenc: Apache-2.0
- Upstream licence: https://github.com/naptha/tesseract.js-core/blob/master/LICENSE

A core nincs a repositoryba beépítve.

## 5. Angol OCR-adat

A program `Tesseract.createWorker('eng', 1, ...)` hívással angol nyelvi modellt kér.

Kapcsolódó nyilvános csomag:
- `@tesseract.js-data/eng`
- https://www.npmjs.com/package/@tesseract.js-data/eng
- Package license metadata: MIT
- Repository: https://github.com/naptha/tessdata

Fontos: az alkalmazás nem állít explicit `langPath` URL-t; a pontos transitive language-asset feloldást a Tesseract.js runtime alapértelmezései végzik.

## 6. jsDelivr

Felhasználás: Tesseract.js runtime script és upstream asset delivery.

- https://www.jsdelivr.com/
- A CDN szolgáltatás saját feltételei érvényesek.
- A hosztolt package saját upstream licencétől nem válik jsDelivr-licencűvé.

## 7. Google Fonts

Explicit CSS kérés:
- https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&family=Roboto:wght@300;400;500;700;900&display=swap

### Orbitron
- https://github.com/googlefonts/orbitron-vf
- SIL Open Font License 1.1

### Roboto
- A projekt jelenlegi UI-linkje: https://github.com/googlefonts/roboto-2
- Licenc: Apache-2.0
- A `roboto-2` repository archivált, de a benne dokumentált licenc továbbra is Apache-2.0.

A repo nem tartalmaz font binárist.

## 8. Felhasználói tesztanyag

A projekt fejlesztéséhez felhasználó által készített Star Citizen screenshotok és runtime logok szolgáltak privát fixture-ként.

A publikus csomag:
- screenshotot nem tartalmaz;
- raw logot nem tartalmaz;
- csak ground-truth fájlneveket és elvárt, strukturált eredményeket dokumentál.

## 9. Saját sPg kód

Az `index.html` és a projekt saját dokumentációja nincs harmadik fél open-source licence alá helyezve. Lásd [LICENSE.md](LICENSE.md).
