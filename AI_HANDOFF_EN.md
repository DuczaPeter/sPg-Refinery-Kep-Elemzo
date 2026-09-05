# AI / coding-agent handoff — English

Use this handoff for a new coding assistant or Codex-like agent.

## Resume order

1. `STATUS.md`
2. `AGENTS.md`
3. git branch / HEAD / dirty state
4. `DEVELOPMENT/ARCHITECTURE_EN.md`
5. only the functions/diff relevant to the current task
6. `DEVELOPMENT/GROUND_TRUTH.csv` when OCR is in scope

## Required behavior

- `index.html` is the baseline; do not regenerate it.
- Preserve the single-file release requirement.
- Do not discard existing dirty work automatically.
- On branch/HEAD/baseline mismatch, do not blindly reset; report it.
- Identify root cause before changing code.
- Prefer the smallest safe fix.
- Do not hardcode material names, fixture filenames or expected ground-truth numbers.
- If OCR is uncertain, review is better than guessing.
- Multiple OCR passes from the same crop are correlated evidence.
- Claim runtime PASS only after a real browser run.
- Do not change out-of-scope UI/OCR/export behavior.

## Gemstone scope

Start with selected-card, badge, Q and count association functions. Quantity must come from the selected card's own `Xnn` badge.

Known failure classes include:
- X11→X1;
- X19→X18;
- X99→X98/X89/X95;
- 6/9 topology;
- tooltip-Q vs selected-card-Q conflicts;
- false consensus from repeated passes of the same crop.

## Freight/Ore scope

Start with structured fields, legacy/tooltip crosschecks, amount consensus and Capacity guards.

A rescue may select only from values already present in OCR evidence. It must not manufacture a new Q or SCU value.

## Export/UI scope

Leave OCR unchanged. Required order:

**Ore A–Z → Gemstone A–Z → Quality ascending.**

DC format:
- `**Material**`
- `Qxxx — x,xxx SCU`
- Gemstone: `Qxxx — n db`

## Final report

Return:
- starting baseline / branch / HEAD;
- modified files;
- short root cause;
- implementation summary;
- targeted test PASS/FAIL;
- runtime test only if actually executed;
- git status;
- blockers;
- never claim an unexecuted test as passed.
