# Changelog

## [V1.40R23R6] — 2026-09-13

### Fixed
- Freight material selection now uses cross-crop evidence adjudication.
- Exact canonical evidence can beat an earlier weaker fuzzy crop result.
- Fixed Iron → Construction Materials without filename/material hardcode.
- Preserved the seven R23R4 critical Q/SCU fixes.

### Validation
- 109 Freight screenshots.
- 109 rows.
- 0 review rows.
- 82.239 SCU.
- 9 critical Freight targets verified in runtime evidence.

### Documentation — 2026-09-23 (V4.2 package)
- Licence resolved: MIT for original sPg code/documentation (owner decision).
- The V4.1 package was published without its dot-prefixed files; `.github/`, `.gitignore`, `.nojekyll` recreated (new hashes) and `.gitattributes` added.
- `README_EN.md` now contains the English equivalent of the detailed Hungarian documentation (HU/EN parity).
- `docs/RELEASE_STANDARD.md` replaced by the canonical V4.2 standard.
- Release gate extended: checksum existence parity, dot-prefixed files, line-ending policy, canonical standard SHA-256, licence, HU/EN sections; new `tools/build-manifest.py`.
- Regression protection: a repeat of the dot-file omission now fails the static gate.
- Runtime `index.html` remains byte-identical to the validated R23R6 artifact.

### Documentation — 2026-09-23 (V4.1 package, HISTORICAL)
- Adopted project-local `docs/RELEASE_STANDARD.md` Standard V4.1.
- Added Release Contract and deterministic gate summary.
- Added SECURITY, PRIVACY, NOTICE and CHANGELOG.
- Added GitHub Actions static release gate.
- Added Mermaid architecture/workflow documentation.
- Added public derived test summaries under `test-artifacts/R23R6/`.
- Runtime `index.html` remains byte-identical to the validated R23R6 artifact.

## [V1.40R23R5]
- Added cross-canonical material alias ownership guard.
- Iron issue remained because crop-level material selection still used first-match behavior.

## [V1.40R23R4]
- Added cross-crop Freight Q conflict adjudication and constrained amount 6/8 topology resolution.
- Repaired seven critical Q/SCU regressions.

Earlier milestones: see `DEVELOPMENT/CHANGE_HISTORY_HU.md` and `DEVELOPMENT/CHANGE_HISTORY_EN.md`.
