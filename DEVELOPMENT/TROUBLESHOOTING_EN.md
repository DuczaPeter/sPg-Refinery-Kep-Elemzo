# Troubleshooting — English

## OCR does not start

- load at least one image;
- check internet access;
- check whether jsDelivr/Tesseract runtime is blocked;
- inspect browser console and the **1-click log**.

## UEX does not work

- UEX is an external service;
- endpoints, CORS, rate limits or uptime can change;
- the built-in fallback material catalog may still work;
- never invent price/location data when API data are unavailable.

## Clipboard / DC button

Browser clipboard rules can be stricter under `file://`. GitHub Pages / HTTPS is more predictable.

## Wrong OCR

Provide:
1. full filename;
2. screenshot;
3. expected material/Q/amount;
4. actual material/Q/amount;
5. 1-click log;
6. Star Citizen patch/build;
7. resolution;
8. browser.

A concrete screenshot + log is required to create a general fix instead of a hardcode.

## Review

A review result is not automatically a bug. The design intentionally prefers review over unsupported automatic acceptance.

## New Star Citizen patch

UI movement, font/rendering changes or new panels may require detector/crop re-validation.
