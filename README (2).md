# Developer tools

`verify_release.py` performs lightweight repository checks without third-party Python packages.

Run from the repository root:

```bash
python tools/verify_release.py
```

It checks:
- single runtime `index.html` at repo root;
- no required local JS/CSS runtime dependency;
- important ordering/DC/OCR function markers;
- JavaScript syntax with `node --check` when Node is installed;
- SHA256 of `index.html`.

It **does not** replace real browser/OCR regression testing.
