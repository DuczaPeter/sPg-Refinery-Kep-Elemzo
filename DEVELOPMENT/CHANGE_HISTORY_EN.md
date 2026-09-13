# Change history — English

This is a selected OCR/release milestone history, not a complete Git commit log.

## R18 — GitHub Developer Release

Previous public repository baseline before this refresh.

## R22 — Freight Batch Quality Template Rescue

Freight batch-rescue mechanics and an earlier stable regression baseline.

## R23 / R23R1 / R23R2

Refinery Work Order recognition branch and additional Freight/Refinery refinement.

## R23R3 — Freight Alternate Tooltip Evidence Repair

Alternative tooltip/evidence rescue for unresolved Freight cases.

## R23R4 — Freight Consensus Cross-Crop Repair

General repairs for seven confidently wrong Q/SCU outputs identified in the 2026-09-13 Freight set.

Key elements:
- cross-crop Q conflict adjudication;
- constrained digit-position guard;
- amount 6/8 pixel-topology guard.

## R23R5 — Freight Material Canonical Guard

UEX cross-canonical alias ownership guard.

Result:
- reduced alias-catalog collisions;
- Iron → Construction Materials still remained because crop-level material selection also used first-match behavior.

## R23R6 — Freight Material Evidence Adjudicator

Fixes the actual Iron root cause:
- adjudicates material evidence across multiple crops;
- exact canonical beats weaker fuzzy;
- no Iron/filename hardcode.

Fresh runtime:
- 109/109 rows;
- review 0;
- 82.239 SCU;
- Iron Q500 / 0.180 correct;
- the previous seven Q/SCU repairs remain correct.

This is the current baseline for this GitHub package.
