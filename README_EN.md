# sPg Refinery Image Analyzer – English documentation

## What is it?

**sPg Refinery Image Analyzer** is a single-file, browser-based Star Citizen fan utility. It uses OCR to read refinery / Freight Manager screenshots, separates Ore and Gemstone inventory semantics, and can optionally query UEX API 2.0 for in-game sell locations and estimated revenue.

The public GitHub package runs from `index.html`. There is no build step, Node.js requirement, or custom backend.

## Why was it built?

Manually transcribing many Quality and quantity values is slow and error-prone. The project was intentionally optimized for **accuracy before acceptance** rather than “always return an OCR result”. The design goals are:

- do not invent missing data;
- keep Freight/Ore and Gemstone UI rules isolated;
- cross-check uncertain OCR with independent crops and preprocessing passes;
- prevent previously observed false-accepted rows;
- keep a single ordering rule across results, UEX output, CSV/JSON and Discord copy;
- process user screenshots locally in the browser instead of uploading them to a project-owned image server.

## Processing pipeline

### 1. Image input

Images are selected or dropped into the browser and represented with local Object URLs. Development screenshots are not included in the public repository package.

### 2. OCR

The app uses **Tesseract.js 5.1.1** with English recognition data. Multiple workers can be created in parallel on machines reporting at least 8 logical CPU threads.

Recognition does not trust one full-screen OCR pass. It combines targeted crops, grayscale / contrast / threshold variants, page segmentation modes and geometry checks.

### 3. Gemstones

For gemstones, inventory quantity is the **piece count**. The tooltip `0.001 SCU` value is the physical size of one piece, not the stock quantity.

The app associates the selected gemstone card's:

- material name;
- Quality value;
- top-right `Xnn` count badge.

Targeted guards were developed for real observed failures such as `X11 → X1`, `X19 → X18`, `X99 → X98/X89/X95`, and 6-vs-9 digit topology errors. Pixel-topology adjudication is restricted to the gemstone badge path.

### 4. Freight Manager / Ore

For Ore / ship-mineable inventory screenshots, the actual tooltip SCU amount is the relevant quantity. Material, Quality, amount and usable Capacity evidence are read separately. Cross-source rescue logic is used where a single OCR pass is noisy but independent evidence agrees on a safe result.

### 5. Ordering

All material-facing lists use the same rule:

**Ore A–Z → Gemstone A–Z → ascending Quality within each material.**

This applies to:

- recognized rows;
- merged rows;
- UEX request/result order;
- CSV export;
- JSON export;
- Discord copy.

### 6. Merge

The **Merge same material and Q** action combines identical material + Quality entries. Ore values are summed in SCU; gemstones are summed as pieces.

### 7. UEX integration

The app calls public GET endpoints from **UEX API 2.0**:

- `/commodities` – material catalog and aliases;
- `/commodities_prices?commodity_name=...` – price, Quality, location and demand data;
- `/star_systems` – available systems.

The app evaluates the reported UEX Quality closest to the recognized Quality within the selected tolerance. It does not invent an undocumented Quality-price formula. UEX is community-maintained, so results can be stale, incomplete or incorrect.

### 8. Exports

- **CSV:** grouped Ore A–Z, then Gemstone A–Z; normalized SCU values; explicit zero demand is preserved as `0`.
- **JSON:** the same ordered UEX projection in machine-readable form.
- **DC:** one-click Discord Markdown copy. Same material + Quality is merged in the copied text without modifying the source rows on screen.

## GitHub Pages deployment

1. Create a GitHub repository.
2. Upload all files from this package to the repository root.
3. Keep `index.html` in the root.
4. GitHub → **Settings → Pages**.
5. Select **Deploy from a branch**.
6. Branch: `main`, folder: `/ (root)`.
7. Save and open the generated GitHub Pages URL after deployment completes.

Hosting through HTTPS is recommended because browser clipboard, CORS and external API policies are more predictable than direct `file://` execution.

## Privacy

The project has no custom screenshot-upload backend. OCR processing runs in the user's browser. Internet access is still required for the external OCR runtime/data, Google Fonts and UEX API requests. Debug state is browser-side.

## Legal / licensing notes

- Unofficial, non-commercial Star Citizen fan project.
- Not affiliated with or endorsed by Cloud Imperium Games / Roberts Space Industries.
- Star Citizen names, visuals and game IP remain the property of their respective rights holders.
- Development screenshots are not redistributed in the public package.
- UEX use is subject to the current UEX Terms of Use / API Terms and rate limits.
- Third-party notices are documented in `THIRD_PARTY_NOTICES.md` and `LICENSES/`.
- No separate OSI-approved license has been selected for the original project code in this package; see `LICENSE.md`.

## Validation snapshot

Development included a combined 90-image regression run: 56 Freight/Ore images and 34 Gemstone images. Known, manually supplied ground-truth cases were used to drive targeted fixes. This is test evidence, not a universal guarantee; Star Citizen UI changes, different resolutions or future patches may require re-validation.

## Developer continuation package

The repository includes a full handoff so another human developer or coding agent can continue the project without reconstructing its design decisions:

- [`AGENTS.md`](AGENTS.md) — mandatory invariants and prohibitions
- [`STATUS.md`](STATUS.md) — current baseline and validation state
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution entry point
- [`DEVELOPMENT/CONTRIBUTING_EN.md`](DEVELOPMENT/CONTRIBUTING_EN.md) — detailed contribution guide
- [`DEVELOPMENT/ARCHITECTURE_EN.md`](DEVELOPMENT/ARCHITECTURE_EN.md) — architecture and key functions
- [`DEVELOPMENT/TESTING_EN.md`](DEVELOPMENT/TESTING_EN.md) — testing and release gates
- [`DEVELOPMENT/AI_HANDOFF_EN.md`](DEVELOPMENT/AI_HANDOFF_EN.md) — coding-agent handoff
- [`DEVELOPMENT/GROUND_TRUTH.csv`](DEVELOPMENT/GROUND_TRUTH.csv) — 24 hand-verified expected results
- [`DEVELOPMENT/RELEASE_CHECKLIST.md`](DEVELOPMENT/RELEASE_CHECKLIST.md) — release checklist
- [`tools/verify_release.py`](tools/verify_release.py) — lightweight static verifier

Development Star Citizen screenshots and raw runtime logs are intentionally excluded from the public repository for rights/privacy reasons. The ground-truth manifest preserves the expected outputs.
