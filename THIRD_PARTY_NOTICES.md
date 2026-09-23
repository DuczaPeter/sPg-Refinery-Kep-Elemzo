# Third-party notices / Harmadik fél értesítések

Verification date / Ellenőrzés dátuma: **2026-09-13**

The application does not bundle Tesseract.js source, OCR traineddata, or font binaries. These are loaded remotely at runtime. License copies are included for transparency in `LICENSES/`.

| Component / service | Project use | License / terms | Runtime/bundled |
|---|---|---|---|
| Tesseract.js 5.1.1 | Browser OCR wrapper | Apache-2.0 | remote runtime |
| tesseract.js-core | OCR/WASM core used by Tesseract.js | Apache-2.0 | resolved by upstream runtime |
| `@tesseract.js-data/eng` | English OCR language data distribution | MIT package metadata | resolved by Tesseract.js defaults |
| jsDelivr | CDN for Tesseract.js script/runtime assets | service terms + upstream package license | remote service |
| Orbitron | UI font | SIL Open Font License 1.1 | Google Fonts remote delivery |
| Roboto | UI font | Apache-2.0 | Google Fonts remote delivery |
| Google Fonts API | Web-font delivery | service terms + individual font licenses | remote service |
| UEX API 2.0 | community market/material/system data | UEX Terms of Use + API Terms | remote API |
| Star Citizen / CIG / RSI | fan-project context and in-game terminology | RSI ToS + fan-content guidance | external IP/context |

## Exact explicit runtime URLs in R23R6

- `https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js`
- `https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&family=Roboto:wght@300;400;500;700;900&display=swap`
- `https://api.uexcorp.uk/2.0`

Tesseract.js may resolve additional core/worker/language assets through its own defaults. The application does not hardcode every transitive asset URL.

## Included license copies

- `LICENSES/Apache-2.0.txt`
- `LICENSES/MIT.txt`
- `LICENSES/OFL-1.1.txt`

These copies are included as references for third-party components. They do not license the original sPg project code.

## Star Citizen fan-project notice

Unofficial, non-commercial fan project. Not affiliated with, endorsed by, or approved by Cloud Imperium Games / Roberts Space Industries.

The current RSI fan guidance requires fan activities/sites to clearly avoid presenting themselves as official or endorsed. The public project therefore keeps an explicit non-affiliation notice.

## UEX notice

UEX is community-driven. Its current terms state that data are informational, may be inaccurate/incomplete, and the API is a work in progress that can change or remove resources. The project is intended for personal/non-commercial fan use consistent with the current terms.

## No bundled development screenshots

The public package intentionally excludes the private Star Citizen screenshots and raw runtime logs used as OCR fixtures. Only filename-based ground-truth manifests and derived test expectations are documented.
