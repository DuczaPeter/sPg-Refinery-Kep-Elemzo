# STATUS

CURRENT VERSION: **V1.40R23R6 Freight Material Evidence Adjudicator**  
CANONICAL BASELINE: `index.html`  
LATEST VALIDATED ARTIFACT: `index.html`  
SHA-256: `a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128`

## Latest validation

R23R6 Freight runtime, 2026-09-13: 109 images, 109 rows, review 0, 82.239 SCU, 9 critical targets verified.

Earlier mixed evidence: 90 images, 56 Freight / 34 Gemstone, 90 rows, review 0, 24/24 critical targets PASS.

## Current release status

Standard: **V4.2** (`docs/RELEASE_STANDARD.md`, SHA-256 `f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2`)  
Repository publication: **MANUAL BY USER**

- **PACKAGE STATUS:** **READY WITH LIMITATIONS**
- **PUBLISHED RELEASE STATUS:** **BLOCKED** — post-publish fresh-clone verification pending

Licence: **RESOLVED — MIT**, selected by the owner on 2026-09-23.

## Attention

- Fresh 109-image suite is Freight-only.
- Fresh live UEX integration was not rerun for this documentation-only packaging pass.
- Actual GitHub social-preview repository setting is not part of the ZIP.

## Unknown / not verified

- Fresh full Gemstone regression on 2026-09-23.
- Fresh full Refinery Work Order regression on 2026-09-23.
- Fresh live UEX integration during package creation.

## Published repository parity

Upload with git or GitHub Desktop so dot-prefixed files (`.github/`, `.gitignore`, `.gitattributes`, `.nojekyll`) are included; the V4.1 web upload silently omitted them. Then run on a fresh clone:

```
git clone https://github.com/DuczaPeter/sPg-Refinery-Kep-Elemzo.git refinery-post-publish-check
cd refinery-post-publish-check
python tools/check-release.py
```

## Next task

Post-publish fresh-clone check of the published repository.

## Not started / separate approval

- OCR/runtime code change.
- New UI feature.
- New dependency.
- New application release version.

Full release/package work uses `docs/RELEASE_STANDARD.md`.
