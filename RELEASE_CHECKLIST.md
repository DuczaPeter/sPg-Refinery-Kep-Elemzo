# Release checklist

## Runtime artifact

- [ ] `index.html` is the user-facing application.
- [ ] No required local `.js`, `.css`, image, font or data file.
- [ ] JavaScript syntax/parse passes.
- [ ] No accidental debug-only local path is required.

## OCR acceptance

- [ ] Relevant targeted private fixtures PASS.
- [ ] Known false accepted row count = 0.
- [ ] If OCR logic changed broadly, combined regression was actually run.
- [ ] Runtime PASS is not claimed from static reasoning alone.

## Ordering and exports

- [ ] Ore A–Z → Gemstone A–Z → Q ascending everywhere.
- [ ] CSV/JSON SCU values max 3 decimals.
- [ ] Numeric demand `0` is preserved.
- [ ] Missing demand is not converted to zero.
- [ ] DC output matches Discord Markdown format.
- [ ] DC copy does not mutate visible rows.

## UEX

- [ ] API endpoint assumptions still valid.
- [ ] No secret/token is committed.
- [ ] UEX terms/source links are current enough for release.

## Sources and licenses

- [ ] `SOURCES_HU.md` and `SOURCES_EN.md` updated if dependencies changed.
- [ ] `THIRD_PARTY_NOTICES.md` updated if needed.
- [ ] Upstream license copy/reference retained.
- [ ] No font binaries are committed.
- [ ] No Star Citizen private development screenshots are committed without an explicit redistribution decision.

## Documentation

- [ ] README HU/EN matches current behavior.
- [ ] `STATUS.md` updated.
- [ ] Developer handoff updated if architecture/invariants changed.
- [ ] `RELEASE_MANIFEST.md` and `SHA256SUMS.txt` regenerated.
