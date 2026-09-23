# Változástörténet — magyar

Ez a fontos OCR/release mérföldkövek összefoglalója, nem teljes Git commit log.

## R18 — GitHub Developer Release

Korábbi publikus repository baseline. Dokumentációs/handoff csomag, a repo jelenlegi frissítése előtt.

## R22 — Freight Batch Quality Template Rescue

Freight batch rescue mechanika és korábbi stabil regressziós alap.

## R23 / R23R1 / R23R2

Refinery Work Order felismerési ág és további Freight/Refinery finomítások.

## R23R3 — Freight Alternate Tooltip Evidence Repair

Alternatív tooltip/evidence rescue az unresolved Freight esetekhez.

## R23R4 — Freight Consensus Cross-Crop Repair

A 2026-09-13-i Freight készletben talált 7 magabiztosan hibás Q/SCU eset általános javítása.

Fő elemek:
- Q cross-crop konfliktus adjudikáció;
- constrained digit-position guard;
- amount 6/8 pixel-topology guard.

## R23R5 — Freight Material Canonical Guard

UEX cross-canonical alias ownership guard.

Eredmény:
- alias katalógus konfliktus csökkent;
- az Iron → Construction Materials hiba még megmaradt, mert a probléma a cropok közötti first-match material döntésben is jelen volt.

## R23R6 — Freight Material Evidence Adjudicator

A valódi Iron gyökérok javítása:
- több material crop közös evidence adjudikáció;
- exact canonical > gyengébb fuzzy;
- nincs Iron- vagy filename-hardcode.

Fresh runtime:
- 109/109 sor;
- review 0;
- 82.239 SCU;
- Iron Q500 / 0.180 helyes;
- a korábbi 7 Q/SCU fix helyes maradt.

Ez a GitHub package current baseline-ja.
