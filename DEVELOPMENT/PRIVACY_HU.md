# Adatvédelem és hálózati működés — magyar

## Mi marad helyben?

A felhasználó által betöltött screenshotot a program böngészőoldalon dekódolja és OCR-ezi. A projektnek nincs saját screenshot-upload backendje.

## Milyen külső kérések vannak?

A jelenlegi `index.html` explicit külső szolgáltatásai:

- jsDelivr — Tesseract.js script;
- Tesseract runtime által feloldott OCR core/language assetek;
- Google Fonts — Orbitron és Roboto;
- UEX API — material/system/market lekérések.

A screenshot nem kerül UEX-re.

## Debug log

A debug log feldolgozás közben memóriában él, és a program a munkamenet végén helyi böngészőtárba is menthet. A **1 kattintásos log** funkcióval a felhasználó maga másolhatja ki.

A log fájlneveket, OCR-szöveget, böngésző/runtime információt tartalmazhat. Nyilvános issue előtt olvasd át.

## Publikus repo szabály

Ne commitolj:
- privát screenshotot;
- raw runtime logot;
- account adatot;
- API keyt vagy tokent;
- helyi személyes elérési utat.

## Külső szolgáltatók

Normál HTTP-kéréseknél a szolgáltató a kapcsolat működéséhez szükséges hálózati metaadatokat kezelheti. Az ő saját privacy/terms dokumentumaik érvényesek.
