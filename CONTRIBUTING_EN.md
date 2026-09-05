# Developer contribution guide — English

## Core principle

The current `index.html` is a working baseline. **Do not regenerate the application from scratch.** The user-facing release must remain a single standalone HTML file unless the repository owner explicitly changes that requirement.

## Recommended workflow

1. Read root `STATUS.md` and `AGENTS.md`.
2. Work on a dedicated branch.
3. State the scope in one sentence: Gemstone, Freight/Ore, UEX/export, UI, or documentation.
4. Modify only the functions needed for that scope.
5. Do not replace the baseline with a preferred architecture during a targeted bugfix.
6. Run targeted tests.
7. OCR/runtime changes require a real browser run.
8. Create a release only after verified acceptance.

## Do not

- Hardcode screenshot filenames.
- Hardcode material names as recognition fixes.
- Hardcode a specific expected Q/count/SCU result into OCR logic.
- Treat multiple passes from the same crop as independent evidence by default.
- Invent missing data.
- Collapse numeric zero into null/missing.
- Rewrite the entire app for a small repair.

## A pull request should include

- short root cause;
- affected functions;
- intentionally unchanged areas;
- targeted test results;
- runtime test result when applicable;
- source + license/terms check for any new dependency/service;
- screenshots/logs only when redistribution is appropriate and no personal data is exposed.

## Ordering invariant

Every material list uses:

**Ore A–Z → Gemstone A–Z → Quality ascending inside the same material.**

The same rule applies to UI, UEX, CSV, JSON and DC/Discord export.

## Licensing and sources

Read before adding dependencies:

- [`../SOURCES_EN.md`](../SOURCES_EN.md)
- [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md)
- [`../LICENSE.md`](../LICENSE.md)
