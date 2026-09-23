#!/usr/bin/env python3
"""STATIC release gate (Release Standard V4.2). Not a runtime/browser/integration test.
Set WRITE_GATE_SUMMARY=1 to write test-artifacts/R23R6/static-release-check.txt."""
from pathlib import Path
import hashlib, os, re, sys
ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'index.html'
EXPECTED_SHA = 'a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128'
EXPECTED_VERSION = 'V1.40R23R6 Freight Material Evidence Adjudicator'
CANON_STANDARD_SHA = 'f3b1358844a9f04da5ea8bfd6fe87b3051bd052e753bd8451991b39f894972b2'
GATE_OUTPUTS = {'test-artifacts/R23R6/static-release-check.txt', 'test-artifacts/R23R6/release-gate-summary.json'}
REQUIRED = ['README.md', 'README_EN.md', 'README_HU.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'SECURITY.md', 'PRIVACY.md',
            'LICENSE', 'LICENSE.md', 'NOTICE.md', 'THIRD_PARTY_NOTICES.md', 'AGENTS.md', 'STATUS.md', 'CHECKSUMS.sha256',
            'PACKAGE-MANIFEST.json', 'docs/RELEASE_STANDARD.md', 'docs/RELEASE_CONTRACT.md', 'docs/RELEASE_GATE_SUMMARY.md',
            'docs/RELEASE.md', 'docs/ARCHITECTURE_OVERVIEW.md', 'DEVELOPMENT/CODEX_WORKFLOW_HU.md',
            'DEVELOPMENT/CODEX_WORKFLOW_EN.md', 'test-artifacts/R23R6/validation-summary.json', 'tools/build-manifest.py',
            '.gitattributes', '.gitignore', '.nojekyll', '.github/workflows/release-static-check.yml',
            '.github/ISSUE_TEMPLATE/bug_report.md', '.github/ISSUE_TEMPLATE/feature_request.md', '.github/pull_request_template.md']
BYTE_EXACT = ['index.html', 'DEVELOPMENT/GROUND_TRUTH.csv', 'LICENSES/*.txt', 'test-artifacts/**']
SECRET_PATTERNS = [re.compile(r'(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
                   re.compile(r'(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*[\"\'][A-Za-z0-9_\-]{16,}'),
                   re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}')]
lines = []; failed = 0
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def check(name, cond, detail=''):
    global failed
    lines.append(f"{'PASS' if cond else 'FAIL'}: {name}" + (f' — {detail}' if detail and not cond else ''))
    if not cond: failed += 1
def repo_files():
    for p in ROOT.rglob('*'):
        rel = p.relative_to(ROOT).as_posix()
        if p.is_file() and not rel.startswith('.git/') and '__pycache__' not in rel:
            yield p, rel

check('index.html present', HTML.exists())
check('baseline byte parity', HTML.exists() and h(HTML) == EXPECTED_SHA)
htmls = sorted(p.name for p in ROOT.glob('*.html'))
check('single root runtime HTML', htmls == ['index.html'], repr(htmls))
t = HTML.read_text(encoding='utf-8', errors='replace') if HTML.exists() else ''
check('version consistency', EXPECTED_VERSION in t and EXPECTED_VERSION in (ROOT / 'VERSION.txt').read_text(encoding='utf-8'))
missing = [r for r in REQUIRED if not (ROOT / r).exists()]
check('required release documentation/files (dot-prefixed included)', not missing, ', '.join(missing))

std = ROOT / 'docs/RELEASE_STANDARD.md'
check('release standard V4.2 marker', std.exists() and re.search(r'^Standard version: V4\.2$', std.read_text(encoding='utf-8'), re.M) is not None)
check('release standard canonical V4.2 SHA-256', std.exists() and h(std) == CANON_STANDARD_SHA)

lic = ROOT / 'LICENSE'
check('license status resolved (MIT)', lic.exists() and lic.read_text(encoding='utf-8').startswith('MIT License')
      and 'LICENSE STATUS: RESOLVED — MIT' in (ROOT / 'LICENSE.md').read_text(encoding='utf-8'))

bad = []
for p, rel in repo_files():
    if rel in ('CHECKSUMS.sha256',): continue
    if p.suffix.lower() in ('.jpg', '.jpeg', '.png') and p.name.startswith('ScreenShot-'): bad.append(rel); continue
    try: txt = p.read_text(encoding='utf-8', errors='ignore')
    except Exception: continue
    for pat in SECRET_PATTERNS:
        if pat.search(txt): bad.append(rel + ' [secret-pattern]'); break
check('credential / secret / private-fixture cleanliness', not bad, ', '.join(bad))

errs = []
for p in ROOT.rglob('*.md'):
    if p.relative_to(ROOT).as_posix().startswith('.git/'): continue
    txt = p.read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', txt):
        target = m.group(1).strip()
        if target.startswith(('http://', 'https://', '#', 'mailto:')): continue
        target = target.split('#', 1)[0]
        if not target: continue
        q = (p.parent / target).resolve()
        try: q.relative_to(ROOT.resolve())
        except ValueError: continue
        if not q.exists(): errs.append(f'{p.relative_to(ROOT)} -> {target}')
check('local markdown links', not errs, '; '.join(errs[:25]))

# V4.2 section 69: every checksummed file exists and matches; every package file is covered.
cs_bad = []; listed = set()
for line in (ROOT / 'CHECKSUMS.sha256').read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    m = re.match(r'^([a-f0-9]{64})  (.+)$', line)
    if not m: cs_bad.append('format:' + line); continue
    listed.add(m.group(2)); f = ROOT / m.group(2)
    if not f.exists() or h(f) != m.group(1): cs_bad.append(m.group(2))
check('checksum existence parity', not cs_bad, ', '.join(cs_bad[:15]))
uncovered = [rel for _, rel in repo_files() if rel not in listed and rel not in GATE_OUTPUTS and rel != 'CHECKSUMS.sha256']
check('every package file covered by CHECKSUMS', not uncovered, ', '.join(uncovered[:15]))

# V4.2 sections 70-72: deterministic line endings; hash-bound files protected with -text.
attrs = (ROOT / '.gitattributes').read_text(encoding='utf-8').splitlines() if (ROOT / '.gitattributes').exists() else []
need = ['* text=auto eol=lf'] + [f'{p} -text' for p in BYTE_EXACT]
check('line-ending policy', all(l in attrs for l in need), ', '.join(l for l in need if l not in attrs))
def byte_exact(rel):
    return rel == 'index.html' or rel == 'DEVELOPMENT/GROUND_TRUTH.csv' or (rel.startswith('LICENSES/') and rel.endswith('.txt')) or rel.startswith('test-artifacts/')
crlf = []
for p, rel in repo_files():
    if byte_exact(rel): continue
    b = p.read_bytes()
    if b'\0' not in b and b'\r' in b: crlf.append(rel)
check('no CRLF in normalizable text files', not crlf, ', '.join(crlf[:15]))

# HU/EN parity of the detailed user documentation.
hu = (ROOT / 'README_HU.md').read_text(encoding='utf-8'); en = (ROOT / 'README_EN.md').read_text(encoding='utf-8')
pairs = [('## Miért készült?', '## Why was it made?'), ('### 2. OCR-beállítások', '### 2. OCR settings'),
         ('### 4. UEX eladóhely-keresés', '### 4. UEX sell-location lookup'), ('### 5. Export', '### 5. Export'),
         ('## Internetkapcsolat', '## Internet connection'), ('## Jogi és licencállapot', '## License and legal status'),
         ('## Hibajelentés', '## Bug reporting')]
gap = [e for hs, e in pairs if hs in hu and e not in en]
check('HU/EN detailed documentation parity', not gap, ', '.join(gap))

lines.append(f"STATIC RELEASE GATE: {'PASS' if failed == 0 else 'FAIL'}")
lines.append('NOTE: this is not a runtime/browser/integration test.')
out = '\n'.join(lines) + '\n'
sys.stdout.write(out)
if os.environ.get('WRITE_GATE_SUMMARY') == '1':
    (ROOT / 'test-artifacts/R23R6/static-release-check.txt').write_text(out, encoding='utf-8', newline='\n')
sys.exit(0 if failed == 0 else 1)
