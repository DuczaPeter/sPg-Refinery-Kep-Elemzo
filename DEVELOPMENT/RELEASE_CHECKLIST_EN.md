# Release checklist — English

## Runtime artifact
- [ ] `index.html` is the only root runtime HTML.
- [ ] APP_VERSION and OCR revision are correct.
- [ ] no mandatory local JS/CSS.
- [ ] `python tools/verify_release.py` PASS.

## OCR
- [ ] targeted ground truth PASS for changed branch.
- [ ] appropriate regression suite for broad OCR changes.
- [ ] no known false-accepted target.
- [ ] review behavior was not hidden by hardcode.

## Scope
- [ ] Freight/Gemstone/Refinery branches did not regress.
- [ ] UI/export work did not rewrite OCR logic without reason.

## Export
- [ ] ordering correct.
- [ ] maximum 3 decimals.
- [ ] explicit zero preserved.
- [ ] DC copy does not mutate UI rows.

## Documentation
- [ ] STATUS current.
- [ ] change history current.
- [ ] ground truth updated for new targets.
- [ ] sources/licenses updated after dependency/endpoint changes.
- [ ] README links valid.

## Privacy/legal
- [ ] no screenshots/raw logs/secrets/personal paths.
- [ ] non-affiliation disclaimer preserved.
- [ ] third-party attribution preserved.
