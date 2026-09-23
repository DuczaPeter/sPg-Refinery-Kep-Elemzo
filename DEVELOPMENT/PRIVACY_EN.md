# Privacy and network behavior — English

## What stays local?

User-provided screenshots are decoded and OCR-processed in the browser. The project has no screenshot-upload backend of its own.

## External requests

Explicit external services in the current `index.html`:

- jsDelivr — Tesseract.js script;
- OCR core/language assets resolved by the Tesseract runtime;
- Google Fonts — Orbitron and Roboto;
- UEX API — material/system/market requests.

Screenshots are not sent to UEX.

## Debug log

The debug log lives in memory during processing and may be persisted to browser-local storage at session end. The **1-click log** action lets the user copy it.

Logs can contain filenames, OCR text and browser/runtime details. Review them before posting publicly.

## Public repository rule

Do not commit:
- private screenshots;
- raw runtime logs;
- account data;
- API keys/tokens;
- personal filesystem paths.

## External providers

Normal HTTP requests expose the network metadata required for those services to respond. Their own privacy policies/terms apply.
