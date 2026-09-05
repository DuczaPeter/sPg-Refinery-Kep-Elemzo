# AGENTS.md — sPg Refinery Kép Elemző

This file is the primary handoff for human developers and coding agents.

## Product

**sPg Refinery Kép Elemző** is a Star Citizen browser utility delivered as a **single self-contained `index.html`**. It reads user-provided screenshots locally with OCR, separates Ore/Freight and Gemstone flows, can query UEX market data, and exports ordered inventory data to CSV, JSON and Discord Markdown.

## Non-negotiable project rules

1. **The current `index.html` is the baseline. Do not regenerate the application from scratch.**
2. User-facing release stays a **single standalone HTML file**. CSS and JavaScript stay embedded in `index.html`.
3. Do not add a build system, framework, backend, local runtime dependency, or extra required asset unless the repository owner explicitly requests it.
4. Do not invent OCR values. Unresolved data must remain review/uncertain rather than becoming a false accepted row.
5. A runtime PASS may only be claimed after an actual browser/runtime test. Static reasoning is not a runtime PASS.
6. Do not hardcode a screenshot filename, a material name, or a specific expected numeric answer as a recognition fix. Fix the general UI/evidence rule.
7. Different OCR passes made from the **same crop/evidence family are correlated**. They are not automatically independent proof.
8. Preserve scope. A Gemstone fix must not silently modify Ore/Freight/Refinery behavior, and vice versa.
9. Preserve the global material order everywhere:
   **Ore A–Z → Gemstone A–Z → Quality ascending inside the same material.**
10. Preserve explicit zero values. In UEX/export data, numeric `0` is not the same as missing/null.
11. SCU/cSCU exports must be normalized to at most 3 decimals. Do not export binary floating-point artifacts.
12. The **DC** button copies Discord Markdown in the same Ore→Gemstone ordering. It must not mutate the visible rows.
13. Keep source, attribution, fan-project and third-party license notices intact.
14. Do not commit development screenshots, raw user logs, account data, API keys, secrets, or personal paths to the public repository.

## Gemstone invariants

- Gemstone stock quantity is the inventory `Xnn` badge count, not the `0.001 SCU` tooltip unit size.
- The `0.001 SCU` cell is an anchor/unit indicator.
- Material name, Quality and count must belong to the **same selected/hovered inventory card**.
- Selected-card geometry is the primary association mechanism.
- Count comes from the selected card's own upper-right `Xnn` badge.
- A missing OCR `X` may be recoverable only when badge geometry is strong and the numeric evidence is otherwise safe.
- Q conflicts must not be resolved by blind source priority.
- Pixel topology/morphology is a constrained adjudicator, not a license to rewrite arbitrary digits.
- The 6/9 distinction must use loop position; one interior loop alone does not imply `9`.

## Ore / Freight invariants

- Ore/Freight quantity is the actual SCU amount shown by the relevant UI, not the setup/capacity field.
- Capacity can be used as a physical validity guard, but not as the stock amount unless the UI explicitly says so.
- Cross-source rescue is allowed only when material/Q/amount already exist in OCR evidence and satisfy the documented confidence gates.
- Do not synthesize a missing Q or SCU value.

## Current accepted ordering/export behavior

- UI lists: Ore A–Z, then Gemstone A–Z, then Q ascending.
- UEX request/result ordering: same comparator.
- CSV/JSON: same comparator.
- DC/Discord: same comparator.
- Same Material+Q may be merged only by the explicit merge action, or for the DC copied text without mutating on-screen rows.

## Minimum verification after code changes

1. Check JavaScript syntax/parse.
2. Run the targeted ground-truth cases relevant to the changed branch.
3. If OCR, UI or browser runtime behavior changed, run a real browser test.
4. For broad OCR changes, run the combined regression suite when local private fixtures are available.
5. Verify no new local runtime dependency was introduced.
6. Verify source/license documentation if a third-party dependency or endpoint changed.
7. Never claim an unavailable test as passed.

## Known stable regression evidence

The last validated combined suite used 90 screenshots:
- 56 Ore/Freight
- 34 Gemstone
- 90 recognized rows
- 0 review rows
- 24 hand-verified ground-truth targets exact PASS
- Ore total: 48.745 SCU
- Gemstone total: 1504 pieces

The private screenshots are intentionally **not distributed** in the public repository. See `DEVELOPMENT/GROUND_TRUTH.csv` and `DEVELOPMENT/PRIVATE_FIXTURES/README.md`.

## Important files

- `index.html` — current application baseline and release artifact.
- `STATUS.md` — current project state.
- `CONTRIBUTING.md` — contribution entry point.
- `DEVELOPMENT/ARCHITECTURE_HU.md` / `ARCHITECTURE_EN.md` — technical architecture.
- `DEVELOPMENT/TESTING_HU.md` / `TESTING_EN.md` — test strategy and release gates.
- `DEVELOPMENT/GROUND_TRUTH.csv` — hand-verified target manifest without copyrighted screenshots.
- `DEVELOPMENT/AI_HANDOFF_HU.md` / `AI_HANDOFF_EN.md` — continuation instructions for another coding assistant.
- `SOURCES_HU.md`, `SOURCES_EN.md`, `THIRD_PARTY_NOTICES.md` — sources, terms and licenses.
