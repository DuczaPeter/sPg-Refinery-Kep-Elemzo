# CHATGPT → CODEX handoff and credit-efficient workflow
## sPg Refinery Image Analyzer — project-specific edition

This file supplements the global **CHATGPT → CODEX HANDOFF AND CREDIT-EFFICIENT WORKFLOW**.

The global workflow remains the base rule. This document defines how to apply it specifically to the **sPg Refinery Image Analyzer** repository.

## 1. Mandatory baseline

Canonical runtime baseline:

- `index.html`
- APP_VERSION: `V1.40R23R6 Freight Material Evidence Adjudicator`
- OCR revision: `v140r23r6-freight-material-evidence-adjudicator`

Codex must not regenerate the application from scratch.

Before any work:

1. read `AGENTS.md`;
2. read `STATUS.md`;
3. read only the relevant `DEVELOPMENT/` docs;
4. inspect Git/repository state;
5. then edit.

## 2. Skill routing

Default for existing-project continuation:

`$credit-efficient-project-runner`

Use only when needed:

- `$three-model-consensus` — consequential, uncertain engineering decisions with broad regression risk;
- `$github-auth-duczapeter` — actual GitHub read/write work;
- `$ui-component-library` — reusable or significant UI component work.

`$uj-projekt` is forbidden for routine resume. Use it only for a genuinely new project or an explicitly requested new scaffold/control layer.

## 3. Handoff format

Every ChatGPT → Codex handoff should have two sections:

### NEKEM SZÓL

Short human-facing summary:
- what Codex will do;
- baseline;
- forbidden scope;
- acceptance test;
- anything the user must provide.

### CODEXNEK SZÓL

The actual concise Codex prompt.

Never pass the entire ChatGPT conversation.

## 4. Mandatory Codex prompt fields

Every handoff must define:

- baseline;
- explicit skill;
- exact scope;
- forbidden scope;
- evidence;
- acceptance fixture;
- tests;
- stop condition.

Acceptance fixtures may be used for testing but must never be hardcoded into runtime logic.

## 5. Credit efficiency

Normal resume context:
- `AGENTS.md`;
- `STATUS.md`;
- one or two relevant development docs;
- relevant `index.html` section;
- relevant ground-truth rows.

Do not reread the entire repository by default.

Do not run full regression routinely. Reserve it for broad OCR/shared logic, dependency/runtime changes, or release gates.

## 6. Dirty/WIP rule

Preserve existing work.

Forbidden:
- `git reset --hard`;
- deleting branches/worktrees;
- overwriting user WIP;
- clean-slate regeneration.

Inspect dirty state, understand it, and make only the scoped change.

## 7. R23R6 project invariants

Freight material:
**exact canonical > exact manual alias > exact alias/compact > clipped/edge > partial > ngram > fuzzy**

Do not restore first-match-wins.

Preserve R23R4 Freight Q/SCU conflict logic.

Gemstone quantity is the selected card's `Xnn`, not `0.001 SCU`.

Global ordering:
**Ore A–Z → Gemstone A–Z → ascending Q**

Export:
maximum 3 decimals; explicit zero is not missing/null.

Runtime:
one standalone `index.html`.

## 8. Validation authority

Fresh R23R6 Freight suite:
- 109 images;
- 109 rows;
- review 0;
- 82.239 SCU;
- 9 critical targets correct.

Earlier mixed suite:
- 90 images;
- 56 Freight;
- 34 Gemstone;
- review 0;
- 24/24 critical targets PASS.

The suites complement each other.

## 9. Codex response format

Keep it short and evidence-based.

Required:
- **CHANGED**
- **TESTED**
- **UNVERIFIED**
- **FILES**
- **STOP CONDITION / NEXT SAFE STEP**

Never claim PASS for a test that was not actually run.

## 10. Checkpoint commit

Allowed only when:
- task is clearly PASS;
- targeted tests completed;
- no known regression;
- scope is contained;
- dirty/WIP state is preserved.

## 11. GitHub

Use GitHub operations only when explicitly requested.

When required:
`$github-auth-duczapeter`

Inspect repository/branch/status before push, PR or release. Never overwrite `main` by assumption.

## 12. Minimal Codex prompt template

Use `$credit-efficient-project-runner`.

Baseline: current repository `index.html`, APP_VERSION `V1.40R23R6 Freight Material Evidence Adjudicator`.

Task: fix only the reproduced issue below.

Scope:
- affected branch/function only.

Forbidden:
- unrelated OCR branches;
- UEX/export/UI unless explicitly in scope;
- framework/build changes;
- regenerating `index.html`.

Evidence:
- use supplied screenshot/log/ground truth;
- prove root cause before editing.

Acceptance:
- target fixture correct;
- control remains correct;
- no filename/material/value hardcode.

Tests:
- static verifier;
- target;
- control;
- browser runtime if behavior changed.

Preserve dirty/WIP state. No reset/overwrite.

Output:
- CHANGED
- TESTED
- UNVERIFIED
- FILES
- NEXT SAFE STEP

Stop if a generic evidence-based fix cannot be justified.

## 13. Relationship to the global workflow

This document does not replace the global CHATGPT → CODEX workflow.

Priority:
1. global ChatGPT → Codex workflow;
2. repository `AGENTS.md`;
3. repository `STATUS.md`;
4. this project-specific workflow;
5. current task handoff.

Use the narrower, newer, explicit rule unless it would violate baseline safety invariants.
