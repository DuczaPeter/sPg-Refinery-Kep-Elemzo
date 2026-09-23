# Közreműködés — magyar

## Mielőtt hozzányúlsz

Olvasd:
- `../AGENTS.md`
- `../STATUS.md`
- `ARCHITECTURE_HU.md`
- `TESTING_HU.md`

## Branch és scope

Egy javítás legyen a lehető legszűkebb.

Példák:
- Freight material fix;
- Freight Q fix;
- Gemstone badge fix;
- Refinery Work Order fix;
- UI/export fix;
- dokumentáció/dependency fix.

Ne nyiss újra korábban lezárt OCR logikát bizonyíték nélkül.

## OCR-fix követelmény

Tilos:
- screenshot filename hardcode;
- `if material == Iron then...` jellegű egyedi javítás;
- konkrét várt Q/SCU szám beégetése;
- ugyanazon crop preprocessing passzainak független proofként kezelése.

Kell:
- reprodukálható hiba;
- raw OCR/evidence;
- általános szabály;
- kontroll eset;
- targeted runtime teszt.

## PR tartalom

Írd le:
- mi volt a hiba;
- mi a gyökérok;
- mi változott;
- mi nem változott;
- milyen teszt futott;
- mi maradt UNVERIFIED.

## Privát fixture

A screenshotok és logok nem kerülnek a publikus repóba. A `PRIVATE_FIXTURES/` csak helyi fejlesztési tároló.
