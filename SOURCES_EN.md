# Sources and licenses – English

Checked: **2026-09-05**. Third-party terms can change; re-check the linked pages before a new public release.

## 1. Star Citizen / Cloud Imperium Games / Roberts Space Industries

The utility is a fan-made helper designed around Star Citizen in-game UI screenshots. Development screenshots are **not redistributed** in the public package.

- Official site: https://robertsspaceindustries.com/
- Star Citizen Fankit and Fandom FAQ: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- Terms of Service: https://robertsspaceindustries.com/en/tos/1

The public page includes a visible fan-project disclaimer and an official-site link. The repository/domain should not be presented as an official CIG/RSI property.

## 2. UEX API 2.0

Live market/material/system information is queried from UEX.

- UEX: https://uexcorp.space/
- API 2.0 documentation: https://uexcorp.space/api/documentation/id/home?is_kiosk=1
- Terms of Use and Privacy / API Terms: https://uexcorp.space/about/terms?is_kiosk=1&set_lang=en_US
- `GET /commodities`: https://uexcorp.space/api/documentation/id/get_commodities/
- `GET /commodities_prices`: https://uexcorp.space/api/documentation/id/get_commodities_prices/
- `GET /star_systems`: https://uexcorp.space/api/documentation/id/get_star_systems/
- Runtime API base: https://api.uexcorp.uk/2.0

UEX describes its API data as community-maintained and subject to errors and API changes. This project must not represent UEX data as official or guaranteed live-server truth.

Current UEX terms describe personal/non-commercial platform use and include a dedicated API Terms section. The current terms always take precedence over this documentation.

## 3. Tesseract.js

- Project: https://github.com/naptha/tesseract.js
- NPM: https://www.npmjs.com/package/tesseract.js
- Runtime version in this release: `5.1.1`
- Runtime CDN: https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js
- jsDelivr package page: https://www.jsdelivr.com/package/npm/tesseract.js
- License: Apache License 2.0
- License text: https://www.apache.org/licenses/LICENSE-2.0

The repository does not bundle Tesseract.js source; the browser loads the runtime from the CDN.

## 4. Tesseract English trained data

`Tesseract.createWorker('eng', 1, ...)` uses the default English recognition data path supplied by the Tesseract.js ecosystem.

- Package: https://www.npmjs.com/package/@tesseract.js-data/eng
- Repository: https://github.com/naptha/tessdata
- Package license metadata: MIT
- MIT license: https://opensource.org/license/mit

The public repository does not bundle the traineddata file; it is fetched at runtime by Tesseract.js.

## 5. Google Fonts API

The page requests two remote webfonts:

- Google Fonts API documentation: https://developers.google.com/fonts/docs/getting_started
- Runtime stylesheet request: https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&family=Roboto:wght@300;400;500;700;900&display=swap

### Orbitron

- Upstream: https://github.com/googlefonts/orbitron-vf
- Original project: https://github.com/theleagueof/orbitron
- License: SIL Open Font License 1.1
- Official OFL 1.1 text: https://openfontlicense.org/open-font-license-official-text/

### Roboto

- Upstream: https://github.com/googlefonts/roboto-2
- License: Apache License 2.0
- License file: https://github.com/googlefonts/roboto-2/blob/main/LICENSE

The repository does not redistribute font binaries; browsers fetch them through Google Fonts.

## 6. User-supplied development fixtures

Star Citizen screenshots and runtime logs supplied by the user were used as OCR fixtures and manual ground truth during development. They are intentionally omitted from the public GitHub release package.

## 7. Original project code

The `index.html` application logic and repository documentation are original project material, not copied Tesseract.js, Google Fonts or UEX source code. External services are referenced through script/font URLs or API requests.

No separate OSI-approved open-source license has been selected for the original project code in this package. See `LICENSE.md`.
