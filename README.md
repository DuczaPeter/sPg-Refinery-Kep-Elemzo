# sPg Refinery Kép Elemző

**GitHub Pages-ready, single-file Star Citizen fan tool for OCR-assisted refinery / Freight Manager inventory reading and UEX-based sell-location lookup.**

- 🇭🇺 [Magyar részletes leírás](README_HU.md)
- 🇬🇧 [English detailed documentation](README_EN.md)
- 📚 [Források magyarul](SOURCES_HU.md)
- 📚 [Sources in English](SOURCES_EN.md)
- ⚖️ [Third-party notices and licenses](THIRD_PARTY_NOTICES.md)
- 💬 [Rövid magyar Discord használati leírás](DISCORD_HASZNALAT_HU.md)
- 🧪 [Fejlesztési és validációs jegyzetek](DEVELOPMENT_NOTES_HU.md)

## Gyors indítás / Quick start

1. Upload the contents of this folder to a GitHub repository.
2. Keep `index.html` in the repository root.
3. GitHub → **Settings → Pages** → Deploy from branch → `main` / root.
4. Open the generated GitHub Pages URL in Chrome/Edge.

A projekt nem hivatalos Star Citizen rajongói projekt, és nem áll kapcsolatban a Cloud Imperium Games / Roberts Space Industries szervezeteivel. UEX-adatok közösségi jelentésekből származnak, ezért ellenőrzést igényelhetnek.

This is an unofficial Star Citizen fan project and is not affiliated with or endorsed by Cloud Imperium Games / Roberts Space Industries. UEX data is community-maintained and can be incomplete or inaccurate.

## Runtime külső függőségek / Runtime external dependencies

The app is one local `index.html`, but it needs internet access for:

- Tesseract.js OCR runtime and English trained data;
- Google Fonts (Orbitron, Roboto);
- UEX API 2.0 live data.

The user's screenshots are processed locally in the browser by the app logic; the repository does not include the development screenshots.

## Developer package

This repository also contains a complete continuation/handoff package for future developers and coding agents:

- [`AGENTS.md`](AGENTS.md) — non-negotiable project rules
- [`STATUS.md`](STATUS.md) — current baseline/status
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution entry point
- [`DEVELOPMENT/ARCHITECTURE_EN.md`](DEVELOPMENT/ARCHITECTURE_EN.md) — architecture
- [`DEVELOPMENT/TESTING_EN.md`](DEVELOPMENT/TESTING_EN.md) — testing and release gates
- [`DEVELOPMENT/AI_HANDOFF_EN.md`](DEVELOPMENT/AI_HANDOFF_EN.md) — coding-agent handoff
- [`DEVELOPMENT/GROUND_TRUTH.csv`](DEVELOPMENT/GROUND_TRUTH.csv) — 24 hand-verified expected results (screenshots not redistributed)
- [`DEVELOPMENT/RELEASE_CHECKLIST.md`](DEVELOPMENT/RELEASE_CHECKLIST.md) — release checklist
- [`tools/verify_release.py`](tools/verify_release.py) — lightweight static release checks

Private Star Citizen screenshot fixtures and raw runtime logs are intentionally excluded from the public repository. See [`DEVELOPMENT/PRIVATE_FIXTURES/README.md`](DEVELOPMENT/PRIVATE_FIXTURES/README.md).
