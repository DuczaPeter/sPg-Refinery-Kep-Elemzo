# Fejlesztési történet R1–R18 — magyar

## Baseline

A projekt a működő V1.40 egyfájlos HTML baseline-ból indult. A javítási stratégia végig az volt, hogy a meglévő alkalmazást ne írjuk újra, hanem a reprodukált hibákhoz célzott guardokat és evidence-kezelést adjunk.

## R1–R3

- Gemstone Q/count evidence-familyk szétválasztása.
- Ugyanazon crop több OCR-passza nem automatikusan független bizonyíték.
- False-accept gate előtérbe került.

## R4–R6

- Selected gemstone card és saját jobb felső `Xnn` badge izolálása.
- X11/X19 vékony karakterproblémák kezelése.
- Count forrásának leválasztása a név/Q OCR-től.

## R7–R10

- 8/9 és 6/9 jellegű digit-tévesztések kezelése.
- X99→X98/X89/X95 típushibákhoz multiscale és pixel-topológiai adjudikáció.
- Q crosscheck státusz javítása.
- Feynmaline X99 noisy-family rescue.

## R11–R12

- Freight structured crosscheck.
- Capacity-unique amount guard.
- 0.001 SCU körüli OCR jitter kezelés.
- Structured Q + külön legacy/tooltip identity cross-source rescue.

## R13

- 90 képes kombinált regresszió közben talált Aphorite X16→X19 regresszió.
- Egy belső hurok nem elég a 9 felismeréséhez; a hurok függőleges pozíciója 6/9 guard lett.

## R14

- Minden material-lista egységes sorrendje: Ore A–Z → Gemstone A–Z → Q növekvő.
- CSV floating-point zaj megszüntetése.
- UEX demand `0` külön kezelése a null/hiányzó adattól.
- `category` és UEX státusz exportmezők.

## R15

- DC gomb: egy kattintással Discord Markdown a vágólapra.
- DC export összegezhet azonos Material+Q tételeket anélkül, hogy a látható sorokat módosítaná.

## R16

- Diagnosztikai rendezési szöveg egységesítése.

## R17

- GitHub Pages release csomag.
- Magyar/angol README, források, third-party notice, licencek.
- Tesseract.js runtime verzió pin.

## R18

- Teljes publikus fejlesztői handoff csomag.
- `AGENTS.md`, `STATUS.md`, contributing, architektúra, tesztelés, AI-handoff, ground-truth manifest, release checklist és release-ellenőrző script.
- A private Star Citizen screenshot fixture-k továbbra sincsenek terjesztve.
