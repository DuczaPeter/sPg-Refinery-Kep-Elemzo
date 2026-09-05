# Private OCR fixtures

The public repository intentionally does **not** redistribute the Star Citizen screenshots and raw runtime logs that were used during OCR development.

Reasons:
- they contain game imagery owned by the relevant rights holders;
- logs can contain local/browser/session diagnostic details;
- they are not required for normal users of the application.

For local development, place authorized/private screenshots here or in another local folder and keep them out of Git.

Expected values are recorded in `../GROUND_TRUTH.csv`.

If you create new fixtures:
1. keep the original filename;
2. record the user-verified material, Quality and amount;
3. do not infer ground truth from the OCR output itself;
4. add the expected result to `GROUND_TRUTH.csv` only after visual/manual verification;
5. never publish a screenshot if you do not have the right to redistribute it.
