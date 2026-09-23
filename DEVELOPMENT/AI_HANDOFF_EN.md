# AI / coding-agent handoff — English

## Baseline

- `index.html`
- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- OCR revision: `v140r23r6-freight-material-evidence-adjudicator`
- SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

This is the validated runtime artifact from the 2026-09-13 109-image Freight run. Do not regenerate it from scratch.

## Read first

1. `../AGENTS.md`
2. `../STATUS.md`
3. `ARCHITECTURE_EN.md`
4. `TESTING_EN.md`
5. `GROUND_TRUTH.csv`

## R23R6 key decision

Freight material recognition adjudicates evidence across crop sources. Exact canonical material evidence beats a weaker fuzzy match even if the fuzzy crop arrived first.

Do not restore first-match-wins behavior.

## Stability

R23R4 Q/SCU conflict handling plus the R23R6 material adjudicator form the current Freight baseline.

## Test state

- fresh Freight: 109/109, review 0, 82.239 SCU;
- R23R6 critical targets: 9/9 according to the runtime log;
- earlier mixed suite: 90/90, review 0, 24/24 critical targets;
- the new 109-image suite is not a Gemstone/Refinery regression.

## Stop condition

If a proposed fix only works by hardcoding a specific filename/material/expected value, stop. Find a general evidence rule first.
