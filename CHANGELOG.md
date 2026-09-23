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

### Documentation — 2026-09-23
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
