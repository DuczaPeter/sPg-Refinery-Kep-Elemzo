# CHATGPT → CODEX átadási és credit-optimalizált munkaszabály
## sPg Refinery Kép Elemző — projekt-specifikus változat

Ez a fájl a globális **CHATGPT → CODEX ÁTADÁSI ÉS CREDIT-OPTIMALIZÁLT MUNKASZABÁLY** projekt-specifikus kiegészítése.

A globális szabály marad az alap. Ez a dokumentum azt mondja meg, hogy az **sPg Refinery Kép Elemző** projektnél pontosan hogyan kell alkalmazni.

---

## 1. Kötelező baseline

A jelenlegi canonical runtime baseline:

- `index.html`
- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- OCR revision: `v140r23r6-freight-material-evidence-adjudicator`

A Codex **nem generálhatja újra nulláról** az alkalmazást.

A meglévő `index.html` a forrás és a baseline.

Minden munka előtt:

1. olvasd el az `AGENTS.md` fájlt;
2. olvasd el a `STATUS.md` fájlt;
3. olvasd el a releváns `DEVELOPMENT/` dokumentumokat;
4. ellenőrizd a Git/GitHub állapotot;
5. csak ezután módosíts.

---

## 2. Alap skill routing

Meglévő projekt folytatásánál az alap skill:

`$credit-efficient-project-runner`

Ezt kell használni routine fejlesztéshez, hibajavításhoz, auditáláshoz és kis scope-ú módosításhoz.

### Csak szükség esetén

`$three-model-consensus`

Csak akkor használd, ha:
- az OCR evidence modellben következményes, bizonytalan döntés van;
- több lehetséges architekturális megoldás ütközik;
- egy döntés széles regressziós kockázatot hordoz.

`$github-auth-duczapeter`

Csak akkor használd, ha tényleges GitHub read/write művelet kell.

`$ui-component-library`

Csak újrahasználható UI komponens vagy nagyobb UI szerkezeti fejlesztés esetén.

`$uj-projekt`

**Tilos routine resume-ra.**

Csak akkor használható, ha:
- teljesen új projekt indul; vagy
- a repository tulajdonosa kifejezetten új scaffoldot/control layert kér.

---

## 3. ChatGPT → Codex átadás formátuma

Minden Codex handoff két részre legyen bontva:

### NEKEM SZÓL

Ide kerüljön röviden:

- mit fog Codex csinálni;
- mi a baseline;
- mihez nem nyúl;
- milyen teszt bizonyítja a kész állapotot;
- kell-e nekem valamit külön odaadnom.

### CODEXNEK SZÓL

Ide kerüljön a tényleges Codex prompt.

A Codex prompt legyen rövid, de teljes.

Ne add át a teljes ChatGPT-beszélgetést.

---

## 4. Kötelező Codex prompt tartalom

Minden handoff tartalmazza:

### Baseline

Példa:

`Baseline: current repository index.html, V1.40R23R6 Freight Material Evidence Adjudicator.`

### Kötelező skill

Példa:

`Use $credit-efficient-project-runner.`

### Scope

Pontosan meg kell mondani, mit módosíthat.

Példák:

- Freight material recognition only;
- Freight Q adjudication only;
- Gemstone badge OCR only;
- Refinery Work Order branch only;
- export/UI only;
- documentation only.

### Tiltott scope

Példa:

- do not rewrite unrelated OCR branches;
- do not regenerate `index.html`;
- do not add framework/build system/backend;
- do not change UEX integration unless explicitly in scope;
- do not modify Gemstone logic during a Freight-only fix.

### Bizonyíték

A Codex ne találjon ki hibát vagy javítást.

Használható bizonyíték:

- screenshot;
- raw OCR log;
- `GROUND_TRUTH.csv`;
- reprodukálható runtime failure;
- source inspection;
- existing regression evidence.

### Acceptance fixture

Minden OCR-javításnál legyen konkrét cél.

Példa:

- exact filename;
- expected material;
- expected Q;
- expected amount;
- control case.

A fixture csak tesztfeltétel lehet.

**Tilos a fixture értéket a runtime kódba hardcode-olni.**

### Teszt

Csak a szükséges tesztet futtasd.

Először:
1. static check;
2. targeted case;
3. relevant control;
4. broad regression csak indokolt esetben.

Browser/E2E teszt csak akkor kötelező, ha:
- OCR runtime;
- DOM;
- UI;
- browser API;
- interaction;
- clipboard;
- network integration változott.

### Stop condition

A Codex álljon meg, ha:

- csak filename/material/expected value hardcode-dal tudná megoldani;
- nincs elég bizonyíték a gyökérokra;
- a baseline nem egyezik;
- a repo dirty állapotát csak reset/overwrite árán tudná folytatni;
- a módosítás túlterjedne a megadott scope-on.

---

## 5. Credit-optimalizálás

### Ne töltsön be mindent

Normál resume-context:

- `AGENTS.md`
- `STATUS.md`
- releváns egy-két `DEVELOPMENT/*.md`
- érintett `index.html` kódrész
- releváns ground-truth sorok

Ne olvassa újra automatikusan az egész repositoryt minden körben.

### Ne fusson teljes regresszió rutinszerűen

Teljes regression csak akkor kell, ha:

- OCR core döntési logika változik;
- cross-branch shared function változik;
- release készül;
- dependency/runtime változik;
- egy fix regressziós kockázata széles.

### Célozott keresés

A Codex először keresse meg:

- releváns függvényt;
- hívási útvonalat;
- döntési pontot;
- evidence source-okat.

Ne kezdje az egész `index.html` újraértelmezésével.

---

## 6. Dirty/WIP szabály

Meglévő munkaállapotot meg kell őrizni.

Tilos:

- `git reset --hard`;
- branch törlés;
- worktree törlés;
- felhasználói WIP felülírás;
- automatikus „clean slate” újrakezdés.

Ha dirty állapot van:

1. olvasd ki;
2. értsd meg;
3. csak a kijelölt scope-ban módosíts;
4. ne töröld.

---

## 7. R23R6 projektspecifikus invariánsok

### Freight material

Az R23R6 material evidence adjudicator megmarad.

Erősségi modell:

**exact canonical > exact manual alias > exact alias/compact > clipped/edge > partial > ngram > fuzzy**

A first-match-wins működés visszaállítása tilos.

### Freight Q/SCU

Az R23R4 cross-crop Q és amount conflict kezelés megmarad.

A 6/8 amount pixel-topology csak szűk conflict resolver.

### Gemstone

A stock quantity az `Xnn` badge.

Nem a `0.001 SCU`.

### Rendezés

Mindenhol:

**Ore A–Z → Gemstone A–Z → Q növekvő**

### Export

Maximum 3 tizedes.

Explicit `0` nem válhat missing/null értékké.

### Runtime

A release maradjon:

**egy darab standalone `index.html`**

---

## 8. Validációs authority

### Friss Freight suite

R23R6:

- 109 kép;
- 109 sor;
- review 0;
- 82.239 SCU;
- 9 kritikus target helyes.

### Korábbi mixed suite

- 90 kép;
- 56 Freight;
- 34 Gemstone;
- 90 sor;
- review 0;
- 24/24 kritikus target PASS.

A két suite nem helyettesíti egymást.

---

## 9. Codex válaszformátum

A Codex válasz legyen rövid és bizonyíték-alapú.

Kötelező részek:

- **CHANGED**
- **TESTED**
- **UNVERIFIED**
- **FILES**
- **STOP CONDITION / NEXT SAFE STEP**

Ne írjon hosszú önmagyarázó esszét.

Ne állítsa, hogy valami PASS, ha nem futtatta.

---

## 10. Checkpoint commit

Checkpoint commit csak akkor engedhető, ha:

- a részfeladat egyértelműen PASS;
- targeted teszt kész;
- scope nem lóg túl;
- nincs ismert regresszió;
- dirty/WIP állapot nem sérül.

Commit előtt a Codex röviden írja le:

- mit változtat;
- miért;
- milyen teszt PASS.

---

## 11. GitHub szabály

GitHub művelet csak akkor, ha explicit kérés van rá.

Ha kell:

`$github-auth-duczapeter`

Először:

- repo/branch/status ellenőrzés;
- csak utána push/PR/release.

Ne írja felül automatikusan a `main` branchet.

---

## 12. Példa minimális Codex prompt

### CODEXNEK SZÓL

Use `$credit-efficient-project-runner`.

Baseline: current repository `index.html`, APP_VERSION `V1.40R23R6 Freight Material Evidence Adjudicator`.

Task: fix only the reproduced Freight OCR issue described below.

Scope:
- affected Freight recognition function/path only.

Forbidden scope:
- Gemstone logic;
- Refinery Work Order logic;
- UEX;
- export/UI;
- framework/build changes;
- rewriting `index.html` from scratch.

Evidence:
- use the supplied screenshot/log/ground-truth only;
- identify the root cause before editing.

Acceptance:
- target fixture must match expected material/Q/SCU;
- relevant control case must remain unchanged;
- no filename/material/value hardcode.

Tests:
- static verifier;
- targeted fixture;
- targeted control;
- browser runtime if behavior changed.

Preserve dirty/WIP state. No reset or overwrite.

Output only:
- CHANGED
- TESTED
- UNVERIFIED
- FILES
- NEXT SAFE STEP

Stop if the issue cannot be solved generically from available evidence.

---

## 13. Viszony a globális munkaszabályhoz

Ez a dokumentum **nem helyettesíti** a globális CHATGPT → CODEX munkaszabályt.

A hierarchia:

1. globális CHATGPT → CODEX credit-optimalizált munkaszabály;
2. repository `AGENTS.md`;
3. repository `STATUS.md`;
4. ez a projekt-specifikus Codex workflow;
5. aktuális task handoff.

Ütközésnél a szűkebb, frissebb és explicit projekt/task szabály az irányadó, kivéve ha az a baseline biztonsági invariánsait sértené.
