# Sources, data providers and licenses — English

Verification date: **2026-09-13**

External licenses, APIs and service terms can change. Re-check them before future releases.

## 1. Star Citizen / CIG / RSI

Use: fan-project context, in-game UI and material terminology.

- Official site: https://robertsspaceindustries.com/
- Fan Content Guidance: https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793-Star-Citizen-Fankit-and-Fandom-FAQ
- Terms of Service: https://robertsspaceindustries.com/en/tos/1

The fan FAQ updated on 2026-09-02 says fan sites/activities must clearly avoid presenting themselves as official or endorsed by CIG/RSI. This project therefore carries an explicit non-affiliation notice in both the UI and documentation.

Development Star Citizen screenshots are not redistributed in the public repository.

## 2. UEX API 2.0

Use:
- material catalog and aliases;
- commodity price/sell-location/demand data;
- Star System list.

Runtime base:
- https://api.uexcorp.uk/2.0

Documentation:
- https://uexcorp.space/api/documentation/id/home?is_kiosk=1

Terms:
- https://uexcorp.space/about/terms?is_kiosk=1&set_lang=en_US

The Terms updated 2026-07-02 state that:
- UEX is community-driven;
- data are not guaranteed accurate or complete;
- use is personal/non-commercial;
- the API is a work in progress;
- resources/endpoints can change or be removed.

The app therefore does not present UEX as an official or guaranteed-live data source.

## 3. Tesseract.js 5.1.1

Use: browser OCR.

- Project: https://github.com/naptha/tesseract.js
- Runtime script: https://cdn.jsdelivr.net/npm/tesseract.js@5.1.1/dist/tesseract.min.js
- License: Apache-2.0
- Upstream license: https://github.com/naptha/tesseract.js/blob/master/LICENSE.md

The repository does not bundle the Tesseract.js distribution; the script is loaded remotely at runtime.

## 4. tesseract.js-core

Use: OCR core/WASM consumed by Tesseract.js.

- Project: https://github.com/naptha/tesseract.js-core
- License: Apache-2.0
- Upstream license: https://github.com/naptha/tesseract.js-core/blob/master/LICENSE

The core is not bundled in this repository.

## 5. English OCR data

The application requests English recognition data through `Tesseract.createWorker('eng', 1, ...)`.

Related public data package:
- `@tesseract.js-data/eng`
- https://www.npmjs.com/package/@tesseract.js-data/eng
- package license metadata: MIT
- repository: https://github.com/naptha/tessdata

Important: the app does not set an explicit `langPath`; exact transitive language-asset resolution is controlled by Tesseract.js runtime defaults.

## 6. jsDelivr

Use: delivery of the Tesseract.js runtime script and upstream assets.

- https://www.jsdelivr.com/
- jsDelivr service terms apply.
- Hosting a package does not replace the package's upstream software license.

## 7. Google Fonts

Explicit CSS request:
- https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800&family=Roboto:wght@300;400;500;700;900&display=swap

### Orbitron
- https://github.com/googlefonts/orbitron-vf
- SIL Open Font License 1.1

### Roboto
- Current UI link: https://github.com/googlefonts/roboto-2
- License: Apache-2.0
- The `roboto-2` repository is archived, but its documented license remains Apache-2.0.

No font binaries are bundled in the public repository.

## 8. User-provided test fixtures

User-created Star Citizen screenshots and runtime logs were used privately during development.

The public package:
- contains no screenshots;
- contains no raw runtime logs;
- documents only ground-truth filenames and derived structured expectations.

## 9. Original sPg code

`index.html` and project-authored documentation are not placed under any third-party open-source license. See [LICENSE.md](LICENSE.md).
