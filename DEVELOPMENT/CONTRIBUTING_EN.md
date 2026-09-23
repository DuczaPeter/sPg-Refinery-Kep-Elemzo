# Contributing — English

## Before editing

Read:
- `../AGENTS.md`
- `../STATUS.md`
- `ARCHITECTURE_EN.md`
- `TESTING_EN.md`

## Branch and scope

Keep each change as narrow as possible.

Examples:
- Freight material fix;
- Freight Q fix;
- Gemstone badge fix;
- Refinery Work Order fix;
- UI/export fix;
- documentation/dependency fix.

Do not reopen previously settled OCR logic without new evidence.

## OCR-fix requirements

Forbidden:
- screenshot filename hardcode;
- `if material == Iron then...` style special case;
- embedding a known expected Q/SCU answer;
- treating preprocessing variants of the same crop as independent proof.

Required:
- reproducible failure;
- raw OCR/evidence;
- general rule;
- control case;
- targeted runtime test.

## PR content

Document:
- symptom;
- root cause;
- what changed;
- what did not change;
- tests actually run;
- what remains UNVERIFIED.

## Private fixtures

Screenshots and raw logs do not belong in the public repository. `PRIVATE_FIXTURES/` is local-only development storage.
