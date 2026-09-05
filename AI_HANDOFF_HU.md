# AI / coding-agent handoff — magyar

Ezt add át egy új fejlesztő AI-nak vagy Codex-szerű kódoló agentnek.

## Resume sorrend

1. `STATUS.md`
2. `AGENTS.md`
3. git branch / HEAD / dirty state
4. `DEVELOPMENT/ARCHITECTURE_HU.md`
5. csak az aktuális feladathoz szükséges diff/funkciók
6. `DEVELOPMENT/GROUND_TRUTH.csv`, ha OCR a scope

## Kötelező viselkedés

- A `index.html` a baseline; ne generáld újra.
- A single-file release követelmény marad.
- A meglévő dirty munkát ne dobd el automatikusan.
- Branch/HEAD/baseline eltérésnél ne resetelj vakon; jelezd.
- Előbb root cause, utána kód.
- A legkisebb működő változtatást keresd.
- Ne hardcode-olj materialt, fixture fájlnevet vagy ground-truth számot.
- Ha OCR bizonytalan: review, nem találgatás.
- Ugyanazon crop több OCR-passza korrelált evidence.
- Runtime PASS csak tényleges browser futás után.
- Out-of-scope UI/OCR/export ne változzon.

## Ha Gemstone a scope

Elsőként vizsgáld azokat a függvényeket, amelyek a selected card, badge, Q és count asszociációját kezelik. A darabszám kizárólag a selected card saját `Xnn` badge-e.

Külön figyelj:
- X11→X1;
- X19→X18;
- X99→X98/X89/X95;
- 6/9 topology;
- tooltip Q és selected-card Q konfliktus;
- ugyanazon crop hamis OCR-konszenzusa.

## Ha Freight/Ore a scope

Elsőként a structured field, legacy/tooltip crosscheck, amount consensus és Capacity guard útvonalakat vizsgáld.

Rescue csak már létező evidence-jelöltből választhat. Nem gyárthat új Q/SCU értéket.

## Ha export/UI a scope

Az OCR-t hagyd érintetlenül. Kötelező sorrend:

**Ore A–Z → Gemstone A–Z → Q növekvő.**

DC formátum:
- `**Material**`
- `Qxxx — x,xxx SCU`
- Gemstone: `Qxxx — n db`

## Mit adj vissza a végén

- induló baseline / branch / HEAD;
- módosított fájlok;
- rövid root cause;
- implementáció röviden;
- targeted tesztek PASS/FAIL;
- runtime teszt, ha ténylegesen futott;
- git status;
- blocker, ha van;
- ne állíts olyat, amit nem tudtál lefuttatni.
