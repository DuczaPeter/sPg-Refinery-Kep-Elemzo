# sPg Refinery Kép Elemző – EZT TÖLTSD FEL GITHUBRA

Ez a mappa már a teljes GitHub repository tartalma.
Nem kell kiválogatnod belőle semmit.

## Feltöltés nagyon röviden

1. Csomagold ki a ZIP-et.
2. GitHubon hozz létre egy új, üres repositoryt.
3. A repositoryban válaszd az **Add file → Upload files** lehetőséget.
4. A KICSOMAGOLT mappa TELJES TARTALMÁT húzd be egyszerre, a mappákkal együtt.
5. Kattints a **Commit changes** gombra.
6. GitHub Pageshez: **Settings → Pages → Deploy from a branch → main → / (root) → Save**.

Ennyi. Az oldal belépési fájlja az `index.html`.

## Amit ne csinálj

- Ne csak az `index.html` fájlt töltsd fel, ha a fejlesztési dokumentációt is meg akarod tartani.
- Ne tedd a teljes csomagot még egy plusz almappába a repositoryn belül.
- Ne töröld az `AGENTS.md`, `DEVELOPMENT`, `LICENSES`, `SOURCES_*` és `THIRD_PARTY_NOTICES.md` fájlokat, mert ezek kellenek a fejleszthetőséghez és a forrás/licenc dokumentációhoz.

## Mi van benne?

- `index.html` – a futó, egyfájlos alkalmazás.
- `README.md`, `README_HU.md`, `README_EN.md` – felhasználói dokumentáció.
- `DISCORD_HASZNALAT_HU.md` – rövid magyar Discord használati leírás.
- `AGENTS.md` – fejlesztési szabályok fejlesztőknek és Coding Agenteknek.
- `DEVELOPMENT/` – architektúra, tesztelés, ground truth, AI handoff, release checklist.
- `SOURCES_HU.md`, `SOURCES_EN.md` – források.
- `THIRD_PARTY_NOTICES.md`, `LICENSES/` – harmadik fél licencek és licencek szövegei.
- `GITHUB_PAGES.md` – részletes GitHub Pages útmutató.
- `tools/verify_release.py` – opcionális fejlesztői release ellenőrző.

Ha csak fel akarod tenni és használni, elég a fenti 6 lépést követni.
