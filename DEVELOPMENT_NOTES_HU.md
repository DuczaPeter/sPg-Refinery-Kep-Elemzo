# Fejlesztési és validációs jegyzetek – magyar

## Kiindulási elv

A projekt V1.40 baseline-ból indult. A javításoknál végig release-gate volt, hogy a már működő Ore / Freight / Refinery / UI ág ne romoljon el egy gemstone-specifikus javítás miatt, és fordítva.

## Fő javítási ciklusok

| Ciklus | Mi változott | Miért |
|---|---|---|
| R1–R3 | Gemstone Q/count evidence-familyk szétválasztása, multiscale OCR, false accept gate | ugyanazon crop több OCR-passza ne számítson hamis független konszenzusnak |
| R4–R6 | Selected gemstone badge izolálása, X11/X19 vékony számjegyek kezelése | darabszám kizárólag a kiválasztott kártya jobb felső badge-éből jöjjön |
| R7–R10 | 8/9 és 6/9 digit topológia, X99 rescue, crosscheck státusz | valós képeken X99→X98/X89/X95 és X19→X18 típushibák jelentek meg |
| R11–R12 | Freight structured crosscheck és Q cross-source rescue | Taranite/Copper/Riccite/Savrilium/Titanium eseteknél jó adat ne maradjon indokolatlan warn/review állapotban |
| R13 | kombinált 90 képes regresszió, 6/9 topology guard | egy gemstone regresszió X16→X19 formában csak kombinált futásban látszott |
| R14 | egységes Ore→Gemstone rendezés, CSV floating-point és demand=0 javítás | minden lista és export ugyanazt a struktúrát adja |
| R15 | DC gomb | egy kattintással Discord-kompatibilis készletlista |
| R16 | logszöveg takarítás | a diagnosztikai leírás is ugyanazt a rendezési szabályt jelezze |
| R17 | GitHub release csomag, forrás/licenc panel, Tesseract 5.1.1 pin | reprodukálhatóbb nyilvános kiadás és egyértelmű jogi/forrásmegjelölés |

## Ground-truth módszer

A javítások nem anyagnév- vagy fájlnév-hardcode alapján készültek. A felhasználó Star Citizen képernyőképeken kézzel megadta a helyes material / Q / SCU vagy darabszám értéket; a runtime logokat ehhez hasonlítottuk.

A cél minden körben:

1. false accepted row = 0 az ismert fixture-ökön;
2. csak utána exact PASS arány növelése;
3. bizonytalanság esetén review előnyben részesítése a találgatással szemben;
4. scope-hash / UI ellenőrzés a nem célzott részek védelmére.

## Kombinált regresszió

A stabilizálási szakaszban 90 képes közös futás történt:

- 56 Freight / Ore kép;
- 34 Gemstone kép;
- a kézzel ellenőrzött célpéldák alapján a korábbi hibák lezárásra kerültek;
- Ore összesítés: 48,745 SCU;
- Gemstone összesítés: 1504 db.

Ez a teszt a rendelkezésre álló screenshot-készletre vonatkozik, és nem helyettesíti az új Star Citizen patch/UI verziók regressziós tesztjét.

## Rendezési invariáns

Minden material-listán egyetlen közös comparator érvényes:

**Ore A–Z → Gemstone A–Z → azonos anyagon belül Q növekvő.**

## Nyilvános release elv

A nyilvános GitHub-csomag szándékosan nem tartalmazza a Star Citizen screenshot fixture-öket és runtime logokat. Így a repo a működő alkalmazást és dokumentációt terjeszti, nem a játék képi anyagait vagy felhasználói tesztadatokat.
