# 00 — Start here

## If you only want to use the app

1. Open `index.html`, or use the GitHub Pages deployment.
2. Add Star Citizen screenshots.
3. Click **Recognize images**.
4. Review the recognized material, Quality and quantity values.
5. Merge identical Material + Q rows when appropriate.
6. Optionally fetch UEX sell/pricing data.
7. Export CSV/JSON, or use **DC** for Discord Markdown.

## If you are publishing it on GitHub

Keep `index.html` in the repository root. Upload the full package together because the documentation contains relative links.

For replacing the existing repository layout, read [GITHUB_PAGES.md](GITHUB_PAGES.md).

## If you are developing it

Read, in this order:

1. [AGENTS.md](AGENTS.md)
2. [STATUS.md](STATUS.md)
3. [DEVELOPMENT/ARCHITECTURE_EN.md](DEVELOPMENT/ARCHITECTURE_EN.md)
4. [DEVELOPMENT/TESTING_EN.md](DEVELOPMENT/TESTING_EN.md)
5. [DEVELOPMENT/AI_HANDOFF_EN.md](DEVELOPMENT/AI_HANDOFF_EN.md)

Core rule: never “fix” OCR by hardcoding a particular screenshot filename or an expected numeric answer.
