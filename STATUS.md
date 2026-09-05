# STATUS — GitHub Developer Release R18

## Current baseline

- Runtime artifact: `index.html`
- Package label: **V1.40R18 GitHub Developer Release**
- Functional baseline: R16/R17 behavior plus documentation/developer-package changes only.
- Runtime architecture: single-file HTML, embedded CSS + JavaScript.

## Last validated behavior before this developer-package release

- Combined regression: 90 images.
- Ore/Freight images: 56.
- Gemstone images: 34.
- Recognized rows: 90.
- Review rows: 0.
- Hand-verified ground-truth targets: 24/24 exact PASS.
- Ore total in validated combined set: 48.745 SCU.
- Gemstone total in validated combined set: 1504 pieces.
- Export/list order: Ore A–Z → Gemstone A–Z → Q ascending.
- CSV demand `0` preserved separately from missing/null.
- CSV/JSON numeric quantity normalization: max 3 decimals.
- DC button: one-click Discord Markdown copy.

## Important caution

R18 changes the public release/developer documentation and version label. It does not create a new OCR algorithm. Do not claim a fresh full runtime regression for R18 unless it is actually run.

## Next developer action

Before changing OCR logic, read `AGENTS.md`, then `DEVELOPMENT/AI_HANDOFF_HU.md` or `DEVELOPMENT/AI_HANDOFF_EN.md`, and use the smallest possible targeted scope.
