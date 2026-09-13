# sPg Refinery Kép Elemző / sPg Refinery Image Analyzer

**Star Citizen OCR + UEX helper — unofficial, non-commercial fan project**

- Magyar dokumentáció: [README_HU.md](README_HU.md)
- English documentation: [README_EN.md](README_EN.md)
- Gyors kezdés / Quick start: [00_START_HERE_HU.md](00_START_HERE_HU.md) · [00_START_HERE_EN.md](00_START_HERE_EN.md)
- GitHub Pages: https://duczapeter.github.io/sPg-Refinery-Kep-Elemzo/

## Current release

**V1.40R23R6 Freight Material Evidence Adjudicator**

The runtime application is the single standalone file `index.html`. CSS and JavaScript are embedded. There is no build step and no project-owned backend.

Latest verified Freight regression, 2026-09-13:

- 109 screenshots processed
- 109 result rows
- 0 review rows
- 82.239 SCU total
- the Iron → Construction Materials false classification is fixed
- the previously repaired seven Q/SCU cases remain correct

Important: that 109-image run contained Freight images only. Gemstone and Refinery Work Order validation are documented separately; the project does not present the Freight-only run as a full regression of every recognition branch.

## Documentation map

- [README_HU.md](README_HU.md) / [README_EN.md](README_EN.md) — full product overview
- [SOURCES_HU.md](SOURCES_HU.md) / [SOURCES_EN.md](SOURCES_EN.md) — data sources, runtime services, licenses
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — third-party notices
- [LICENSE.md](LICENSE.md) — license status of original project code/documentation
- [STATUS.md](STATUS.md) — current validated baseline
- [AGENTS.md](AGENTS.md) — mandatory rules for developers and coding agents
- [GITHUB_PAGES.md](GITHUB_PAGES.md) — deployment and replacement guide
- [DEVELOPMENT/](DEVELOPMENT/) — architecture, tests, handoff, change history and ground truth
- [tools/verify_release.py](tools/verify_release.py) — static release verifier

## Legal notice

Star Citizen, Cloud Imperium Games, Roberts Space Industries and related names/assets belong to their respective rights holders. This project is not affiliated with, endorsed by, or approved by CIG/RSI.

UEX is an independent community service. UEX data can be delayed, incomplete or wrong; critical values should be verified in game.
