# Release checklist — magyar

## Runtime artifact
- [ ] `index.html` az egyetlen root runtime HTML.
- [ ] APP_VERSION és OCR revision helyes.
- [ ] nincs kötelező helyi JS/CSS.
- [ ] `python tools/verify_release.py` PASS.

## OCR
- [ ] targeted ground truth PASS az érintett branchre.
- [ ] széles OCR módosításnál megfelelő regression suite.
- [ ] false accepted target nincs.
- [ ] review nem lett elrejtve hardcode-dal.

## Scope
- [ ] Freight/Gemstone/Refinery ágak nem regresszáltak.
- [ ] UI/export változás nem írta át OCR logikát indokolatlanul.

## Export
- [ ] rendezés helyes.
- [ ] max 3 tizedes.
- [ ] explicit 0 megmarad.
- [ ] DC copy nem mutál UI sort.

## Dokumentáció
- [ ] STATUS friss.
- [ ] Change history friss.
- [ ] Ground truth friss, ha új target van.
- [ ] Sources/licencek frissítve dependency/endpoint változásnál.
- [ ] README linkek élnek.

## Privacy/legal
- [ ] nincs screenshot/raw log/secrets/personal path.
- [ ] non-affiliation disclaimer megmaradt.
- [ ] harmadik fél attribution megmaradt.
