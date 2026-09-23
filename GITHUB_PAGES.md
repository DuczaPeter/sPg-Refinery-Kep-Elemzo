# GitHub feltöltés és GitHub Pages / Upload and GitHub Pages

## Magyar

A csomag úgy készült, hogy a repo gyökerében az `index.html` legyen a GitHub Pages belépési pont.

### Tiszta új repo

1. Csomagold ki ezt a release ZIP-et.
2. A **csomag tartalmát** töltsd fel a repository gyökerébe.
3. GitHub → Settings → Pages.
4. Source: **Deploy from a branch**.
5. Branch: `main`.
6. Folder: `/ (root)`.
7. Mentsd.

A `.nojekyll` fájl szándékosan része a csomagnak.

**Fontos:** a GitHub webes feltöltője kihagyja a ponttal kezdődő fájlokat (`.github/`, `.gitignore`, `.gitattributes`, `.nojekyll`). Git-tel vagy GitHub Desktoppal töltsd fel, utána futtasd a gate-et a publikált repository friss klónján.

### A meglévő `DuczaPeter/sPg-Refinery-Kep-Elemzo` repo frissítése

A mostani repository régebbi R18 dokumentációt és néhány duplikált/árva fájlt is tartalmaz. A tiszta R23R6 struktúrához az új csomag fájljait felül kell írni, és a régi, már nem használt fájlokat törölni kell.

A jelenlegi repóból törlendő, ha még léteznek:

- `README (1).md`
- `README (2).md`
- `download`
- `download (3)`
- gyökérben maradt régi: `AI_HANDOFF_HU.md`, `AI_HANDOFF_EN.md`
- `ARCHITECTURE_HU.md`, `ARCHITECTURE_EN.md`
- `CHANGE_HISTORY_HU.md`, `CHANGE_HISTORY_EN.md`
- `CONTRIBUTING_HU.md`, `CONTRIBUTING_EN.md`
- `DEVELOPMENT_NOTES_HU.md`, `DEVELOPMENT_NOTES_EN.md`
- `TESTING_HU.md`, `TESTING_EN.md`
- `GROUND_TRUTH.csv`
- `RELEASE_CHECKLIST.md`
- `verify_release.py`
- gyökérben lévő `Apache-2.0.txt`, `MIT.txt`, `OFL-1.1.txt`

Az új helyük a `DEVELOPMENT/`, `tools/` és `LICENSES/` könyvtár.

### Biztonságos frissítés Git használatával

Ajánlott:
- clone;
- külön branch;
- régi fájlok törlése;
- új csomag bemásolása;
- `python tools/verify_release.py`;
- commit;
- Pages ellenőrzés;
- merge.

A csomag létrehozása **nem módosította automatikusan a GitHub repót**.

## English

The package is laid out so `index.html` at repository root is the GitHub Pages entry point.

For the existing repository, replace files with this package and remove the obsolete R18-era duplicate/root files listed above. The new canonical locations are `DEVELOPMENT/`, `tools/`, and `LICENSES/`.

Recommended workflow: clone → branch → replace/clean → run `python tools/verify_release.py` → commit → test Pages → merge.

**Important:** the GitHub web uploader omits dot-prefixed files (`.github/`, `.gitignore`, `.gitattributes`, `.nojekyll`). Publish with git or GitHub Desktop, then run the gate on a fresh clone of the published repository.
