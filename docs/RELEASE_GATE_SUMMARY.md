# Release gate summary

STANDARD VERSION: V4.2  
RELEASE VERSION: V1.40R23R6  
DATE: 2026-09-23  
REPOSITORY PUBLICATION: MANUAL BY USER

## Evidence

- Source: **SOURCE VERIFIED**
- Static: **STATIC VERIFIED** — `python tools/check-release.py`
- Runtime: **RUNTIME VERIFIED** (R23R6 evidence bound to the unchanged SHA-256)
- Integration: **NOT VERIFIED** for a fresh live UEX packaging-time run
- Published repository parity: **NOT VERIFIED** — post-publish check pending

## Test result summary

- Baseline byte parity: **PASS**
- Static release gate: **PASS**
- Credential/secret cleanliness: **PASS**
- Checksum existence parity (dot-prefixed files included): **PASS**
- Line-ending policy (checked on a `core.autocrlf=true` clone): **PASS**
- R23R6 Freight 109-image runtime: **PASS**
- Historical mixed regression: **PASS**
- Fresh live UEX integration at packaging time: **UNKNOWN**

## Gates

| Gate | Required | Status | Note |
|---|---:|---|---|
| Canonical baseline | YES | **DONE** | index.html |
| Main artifact | YES | **DONE** | index.html |
| Baseline byte parity | YES | **DONE** | hash match |
| Static validation | YES | **DONE** | static gate |
| Runtime validation | YES | **DONE** | R23R6 evidence, unchanged artifact |
| Credential / secret cleanliness | YES | **DONE** | static scan |
| License status resolved | YES | **DONE** | MIT, owner decision 2026-09-23 |
| Version consistency | YES | **DONE** | index / VERSION / docs |
| Regression evidence | YES | **DONE** | 109 Freight + historical mixed 90 |
| Documentation | YES | **DONE** | README, docs, DEVELOPMENT |
| HU/EN parity | YES | **DONE** | detailed usage now also in README_EN.md |
| Third-party legal/source status | YES | **DONE** | THIRD_PARTY_NOTICES, SOURCES |
| Package cleanliness | YES | **DONE** | no private fixtures / raw logs |
| Checksums | YES | **DONE** | CHECKSUMS.sha256 |
| Artifact consistency | YES | **DONE** | manifest / checksums |
| Visual documentation | YES | **DONE** | Mermaid workflow + architecture |
| Inventory / checksum existence parity | YES | **DONE** | every listed file exists |
| Line-ending / .gitattributes policy | YES | **DONE** | LF default, `-text` for hash-bound files |
| Canonical V4.2 standard identity | YES | **DONE** | SHA-256 `f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2` |
| Published repository parity | YES | **BLOCKED** | MANUAL BY USER — post-publish check pending |
| Fresh live UEX integration at package time | NO | **BLOCKED** | not rerun |
| Fresh full Gemstone + Refinery WO regression | NO | **BLOCKED** | not rerun; artifact unchanged |
| Real UI screenshot | NO | **BLOCKED** | remote fonts/OCR runtime unavailable in packaging environment |
| Actual GitHub social-preview setting | NO | **BLOCKED** | manual GitHub step |

## Release status

- **PACKAGE STATUS:** **READY WITH LIMITATIONS** — all REQUIRED gates except published repository parity are DONE; optional limitations remain documented.
- **PUBLISHED RELEASE STATUS:** **BLOCKED** — manual publication and post-publish verification pending.

## Post-publish check

```
git clone https://github.com/DuczaPeter/sPg-Refinery-Kep-Elemzo.git refinery-post-publish-check
cd refinery-post-publish-check
python tools/check-release.py
```
