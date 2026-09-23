# AGENTS.md — sPg Refinery Kép Elemző

Primary developer/coding-agent handoff.

## Product

A Star Citizen browser utility delivered as one self-contained `index.html`. It reads user-provided screenshots locally with OCR, separates Freight/Ore, Gemstone and Refinery Work Order flows, can query UEX data, and exports structured inventory data.

## Non-negotiable rules

1. `index.html` is the baseline. Never regenerate the application from scratch.
2. User-facing runtime stays a single standalone HTML with embedded CSS + JavaScript.
3. No framework, build system, backend, mandatory local runtime dependency or required asset unless explicitly requested.
4. Do not invent OCR values. Review/uncertain is preferable to false acceptance.
5. Runtime PASS may only be claimed after an actual browser/runtime run.
6. Never hardcode a screenshot filename, material name or expected numeric value as a recognition fix.
7. Multiple OCR passes from the same crop/evidence family are correlated; preprocessing variants are not automatically independent proof.
8. Preserve scope: Gemstone, Freight/Ore, Refinery and UI/export fixes must not silently cross-contaminate branches.
9. Preserve global order: **Ore A–Z → Gemstone A–Z → Q ascending within material.**
10. Preserve numeric zero separately from missing/null.
11. Normalize SCU/cSCU export values to at most 3 decimals.
12. DC copy must not mutate visible rows.
13. Preserve third-party attribution, source, fan-project and license notices.
14. Never commit private screenshots, raw user logs, account data, secrets, API keys or personal filesystem paths.

## R23R6 Freight material rule

Material evidence is adjudicated across multiple crop sources. Strong exact canonical evidence must be able to beat a weaker fuzzy result that arrived earlier.

Conceptual ranking:

**exact canonical > exact manual alias > exact alias/compact > clipped/edge recovery > partial > ngram > fuzzy**

Relevant functions include:
- `freightMaterialMatchRank`
- `chooseFreightMaterialMatch`
- `bestMaterialMatch`
- `rebuildMaterialCatalog`

Do not replace this with first-match-wins logic.

## Freight Q/SCU invariants

- actual SCU is inventory quantity;
- Capacity is a validity guard, not automatic quantity;
- cross-source rescue chooses among existing OCR evidence; it does not synthesize a missing value;
- R23R4 cross-crop Q conflict logic and constrained amount 6/8 pixel topology must stay scoped.

## Gemstone invariants

- inventory quantity is the selected card's `Xnn`, not `0.001 SCU`;
- material/Q/count must belong to the same card;
- selected-card geometry is primary association;
- pixel topology is a constrained conflict resolver only;
- a single interior loop does not automatically mean `9`; loop position matters for 6/9.

## Minimum verification

After code changes:
1. JavaScript parse/syntax.
2. Relevant ground-truth targets.
3. Real browser test for OCR/UI/browser behavior.
4. Combined regression for broad OCR changes when private fixtures are available.
5. Verify single-file runtime and no new mandatory local asset.
6. Re-check source/license docs if dependencies/endpoints changed.
7. Never report an unavailable test as passed.

## Current baseline

See [STATUS.md](STATUS.md).

## Developer docs

- `DEVELOPMENT/ARCHITECTURE_HU.md` / `ARCHITECTURE_EN.md`
- `DEVELOPMENT/TESTING_HU.md` / `TESTING_EN.md`
- `DEVELOPMENT/AI_HANDOFF_HU.md` / `AI_HANDOFF_EN.md`
- `DEVELOPMENT/GROUND_TRUTH.csv`
- `DEVELOPMENT/RELEASE_CHECKLIST_HU.md` / `RELEASE_CHECKLIST_EN.md`
- `DEVELOPMENT/CODEX_WORKFLOW_HU.md` / `CODEX_WORKFLOW_EN.md` — project-specific ChatGPT → Codex workflow

## Release workflow reference

For full GitHub release or release-package work, use:

`docs/RELEASE_STANDARD.md`

Do not load or apply the full release workflow during ordinary development tasks. The project-local release standard is authoritative unless explicitly overridden by the user's current instruction.
