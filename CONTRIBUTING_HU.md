# Fejlesztői közreműködés — magyar

## Alapelv

A jelenlegi `index.html` működő baseline. **Ne generáld újra nulláról.** A projekt legfontosabb tulajdonsága, hogy a felhasználói kiadás egyetlen önálló HTML fájl.

## Ajánlott munkamenet

1. Olvasd el a gyökér `STATUS.md` és `AGENTS.md` fájlját.
2. Készíts külön branchet a módosításhoz.
3. Határozd meg a scope-ot egy mondatban: Gemstone, Freight/Ore, UEX/export, UI vagy dokumentáció.
4. Csak a szükséges függvényeket módosítsd.
5. Ne töröld vagy írd felül a működő baseline-t csak azért, mert más architektúrát preferálsz.
6. Futtasd a célzott teszteket.
7. OCR/runtime változásnál valódi böngészős futás szükséges.
8. Csak bizonyított PASS után készüljön release.

## Tiltott rövidítések

- Fájlnévhez kötött OCR-fix.
- Materialnévhez kötött OCR-fix.
- Egy konkrét Q/count/SCU érték hardcode-ja a felismerőbe.
- Ugyanabból a cropból származó több OCR-pass „független bizonyítékként” kezelése.
- Hiányzó adat kitalálása.
- `0` és null/hiányzó adat összemosása.
- Teljes alkalmazás újraírása célzott bugfix helyett.

## Pull requestben legyen

- rövid root cause;
- érintett függvények;
- mi maradt szándékosan változatlan;
- célzott teszt eredménye;
- runtime teszt eredménye, ha volt;
- új külső forrás/dependency esetén link + licenc/terms ellenőrzés;
- screenshot/log csak akkor, ha terjeszthető és nem tartalmaz személyes adatot.

## Rendezési invariáns

Minden material-lista:

**Ore A–Z → Gemstone A–Z → azonos anyagon belül Q növekvő.**

Ez vonatkozik UI-ra, UEX-re, CSV-re, JSON-ra és DC exportra is.

## Licenc és forrás

Módosítás előtt olvasd el:

- [`../SOURCES_HU.md`](../SOURCES_HU.md)
- [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md)
- [`../LICENSE.md`](../LICENSE.md)

Új külső komponenst csak dokumentált forrással és a licenc/terms tiszteletben tartásával adj hozzá.
