# R23R6 release notes — magyar

## Fő javítás

Freight material evidence adjudication.

A korábbi hibás esetben az OCR a teljes bal blokkban helyesen `Iron`-t olvasott, de egy szűk crop fuzzy `Construction Materials` találata érkezett előbb. R23R6-ban a crop-források találatai közös erősségi döntésbe kerülnek, ezért az exact canonical material felülírhatja a gyengébb fuzzy találatot.

## Megőrzött javítások

Az R23R4 hét kritikus Q/SCU javítása változatlanul megmaradt.

## Runtime bizonyíték

2026-09-13:
- 109 Freight screenshot;
- 109 sor;
- review 0;
- 82.239 SCU;
- kritikus 9 target helyes.

## Nincs új runtime dependency

A release továbbra is egyetlen `index.html`.
