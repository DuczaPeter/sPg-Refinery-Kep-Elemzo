# Third-party notices

This file records third-party runtime services/components referenced by the public package. The repository does **not** redistribute Tesseract.js source code, OCR traineddata, or font binaries; they are loaded remotely at runtime.

| Component / service | Use in this project | Source | License / terms |
|---|---|---|---|
| Tesseract.js 5.1.1 | Browser OCR | https://github.com/naptha/tesseract.js | Apache-2.0 |
| tesseract.js-core | WebAssembly OCR core used through Tesseract.js | https://github.com/naptha/tesseract.js-core | Apache-2.0 |
| @tesseract.js-data/eng | English OCR trained data | https://www.npmjs.com/package/@tesseract.js-data/eng | MIT package metadata |
| jsDelivr | CDN delivery of Tesseract.js/runtime data | https://www.jsdelivr.com/ | Service terms apply; hosted package keeps its upstream license |
| Orbitron | Web font via Google Fonts | https://github.com/googlefonts/orbitron-vf | SIL Open Font License 1.1 |
| Roboto | Web font via Google Fonts | https://github.com/googlefonts/roboto-2 | Apache-2.0 |
| Google Fonts API | Webfont delivery | https://developers.google.com/fonts/docs/getting_started | Service terms + individual font licenses |
| UEX API 2.0 | Community market/material/system data | https://uexcorp.space/api/documentation/id/home?is_kiosk=1 | UEX Terms of Use / API Terms |
| Star Citizen / RSI / CIG | Fan-project context and in-game UI terminology | https://robertsspaceindustries.com/ | RSI Terms of Service + Fan Content guidance |

## License copies included

- `LICENSES/Apache-2.0.txt` – relevant to Tesseract.js / tesseract.js-core / Roboto.
- `LICENSES/OFL-1.1.txt` – relevant to Orbitron.
- `LICENSES/MIT.txt` – reference copy for the `@tesseract.js-data/eng` package license metadata.

## Star Citizen fan-project notice

This repository is an unofficial, non-commercial fan project. It is not affiliated with or endorsed by Cloud Imperium Games / Roberts Space Industries. Game-related names and other third-party content remain the property of their respective rights holders.

Official fan guidance: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ

## UEX notice

UEX data is community-maintained and can be incomplete, stale or wrong. UEX may change endpoints or access rules. The project should be used in accordance with the current UEX Terms and API Terms:

https://uexcorp.space/about/terms?is_kiosk=1&set_lang=en_US

## No bundled third-party binaries

The GitHub package deliberately does not contain:

- Star Citizen screenshots used during development;
- Tesseract.js distribution files;
- Tesseract traineddata files;
- Orbitron or Roboto font files.

This reduces redistribution obligations and keeps upstream license/attribution information tied to the original providers. The linked runtime dependencies are still documented above.
