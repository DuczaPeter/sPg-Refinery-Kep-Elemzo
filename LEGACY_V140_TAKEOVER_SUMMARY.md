# Legacy V1.40 takeover summary

This is a sanitized historical summary of the original V1.40 repair handoff. It is **not** the current resume file; current developers should start with root `STATUS.md` and `AGENTS.md`.

Original repair scope focused only on Gemstone count/Q evidence and conflict handling.

Key lessons that remain valid:
- selected-card geometry is the item association baseline;
- selected Q and count must belong to the same card;
- repeated OCR passes from the same crop are correlated;
- missing `X` is not automatically fatal if badge geometry is strong;
- Q-source conflicts must not be resolved by blind priority;
- no global `/10` OCR hack;
- false accepted row = 0 is the first quality gate;
- runtime PASS requires an actual runtime test.

The original private screenshot fixtures and runtime logs are not redistributed here. Their expected outputs are preserved in `DEVELOPMENT/GROUND_TRUTH.csv`.
