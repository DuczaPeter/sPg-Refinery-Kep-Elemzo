# AI / coding agent handoff — magyar

## Baseline

- `index.html`
- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- OCR revision: `v140r23r6-freight-material-evidence-adjudicator`
- SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

Ez a 2026-09-13-i 109 képes Freight runtime tesztből származó validált artifact. Ne generáld újra nulláról.

## Először olvasd

1. `../AGENTS.md`
2. `../STATUS.md`
3. `ARCHITECTURE_HU.md`
4. `TESTING_HU.md`
5. `GROUND_TRUTH.csv`

## R23R6 kulcsdöntés

A Freight material felismerés több crop evidence közül dönt. Exact canonical material erősebb a fuzzy találatnál, még akkor is, ha a fuzzy crop érkezett előbb.

Ne állítsd vissza first-match-wins működésre.

## Stabilitás

A R23R4 Q/SCU konfliktuskezelés és az R23R6 material adjudikátor együtt alkotja a jelenlegi Freight baseline-t.

## Tesztállapot

- friss Freight: 109/109, review 0, 82.239 SCU;
- kritikus R23R6 targetek: 9/9 a log szerint;
- korábbi mixed suite: 90/90, review 0, 24/24 critical target;
- új 109 suite nem Gemstone/Refinery regresszió.

## Stop condition

Ha egy javasolt javítás csak konkrét filename/material/expected value hardcode-dal oldható meg, állj meg. Előbb általános evidence-szabály kell.
