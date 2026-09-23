# R23R6 release notes — English

## Main fix

Freight material evidence adjudication.

In the failing case, full-left OCR correctly read `Iron`, but a narrow crop produced an earlier fuzzy `Construction Materials` match. R23R6 ranks evidence across crop sources, allowing exact canonical material evidence to override weaker fuzzy evidence.

## Preserved repairs

The seven critical R23R4 Q/SCU repairs remain intact.

## Runtime evidence

2026-09-13:
- 109 Freight screenshots;
- 109 rows;
- review 0;
- 82.239 SCU;
- nine critical targets correct.

## No new runtime dependency

Release remains a single `index.html`.

## 2026-09-23 — V4.2 package

`index.html` is unchanged. The project's own code is licensed under MIT (owner decision). The package restores the dot-prefixed files missing from the published repository, adds a `.gitattributes` line-ending policy, extends the English documentation with the detailed usage guide and replaces the project-local standard with the canonical V4.2.
