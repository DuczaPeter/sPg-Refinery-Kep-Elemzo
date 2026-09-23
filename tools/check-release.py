#!/usr/bin/env python3
from pathlib import Path
import hashlib, re, sys
ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'
EXPECTED_SHA='a408b5377f34bad89ac5ec189394ae10c7c6bbe1b8d700b7b3b286e5569f0128'
EXPECTED_VERSION='V1.40R23R6 Freight Material Evidence Adjudicator'
REQUIRED=['README.md','README_EN.md','CHANGELOG.md','CONTRIBUTING.md','SECURITY.md','PRIVACY.md','LICENSE.md','NOTICE.md','THIRD_PARTY_NOTICES.md','AGENTS.md','STATUS.md','docs/RELEASE_STANDARD.md','docs/RELEASE_CONTRACT.md','docs/RELEASE_GATE_SUMMARY.md','docs/RELEASE.md','docs/ARCHITECTURE_OVERVIEW.md','DEVELOPMENT/CODEX_WORKFLOW_HU.md','DEVELOPMENT/CODEX_WORKFLOW_EN.md','test-artifacts/R23R6/validation-summary.json','test-artifacts/R23R6/release-gate-summary.json']
SECRET_PATTERNS=[re.compile(r'(?i)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),re.compile(r'(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*[\"\'][A-Za-z0-9_\-]{16,}'),re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}')]
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def fail(m): print('FAIL:',m); raise SystemExit(1)
def ok(m): print('PASS:',m)
if not HTML.exists(): fail('index.html missing')
if h(HTML)!=EXPECTED_SHA: fail('baseline byte parity failed')
ok('baseline byte parity')
htmls=sorted(p.name for p in ROOT.glob('*.html'))
if htmls!=['index.html']: fail('single-file runtime violated: '+repr(htmls))
ok('single root runtime HTML')
t=HTML.read_text(encoding='utf-8',errors='replace')
if EXPECTED_VERSION not in t: fail('version consistency failed')
ok('version consistency')
for rel in REQUIRED:
 if not (ROOT/rel).exists(): fail('required release file missing: '+rel)
ok('required release documentation/files')
bad=[]
for p in ROOT.rglob('*'):
 if not p.is_file(): continue
 rel=p.relative_to(ROOT).as_posix()
 if rel in ('CHECKSUMS.sha256','SHA256SUMS.txt'): continue
 if p.suffix.lower() in ('.jpg','.jpeg','.png') and p.name.startswith('ScreenShot-'): bad.append(rel); continue
 try: txt=p.read_text(encoding='utf-8',errors='ignore')
 except Exception: continue
 for pat in SECRET_PATTERNS:
  if pat.search(txt): bad.append(rel+' [secret-pattern]'); break
if bad: fail('credential/private-fixture cleanliness: '+', '.join(bad))
ok('credential / secret / private-fixture cleanliness')
errs=[]
for p in ROOT.rglob('*.md'):
 txt=p.read_text(encoding='utf-8',errors='replace')
 for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',txt):
  target=m.group(1).strip()
  if target.startswith(('http://','https://','#','mailto:')): continue
  target=target.split('#',1)[0]
  if not target: continue
  q=(p.parent/target).resolve()
  try: q.relative_to(ROOT.resolve())
  except ValueError: continue
  if not q.exists(): errs.append(f'{p.relative_to(ROOT)} -> {target}')
if errs: fail('broken local markdown links: '+'; '.join(errs[:25]))
ok('local markdown links')
print('STATIC RELEASE GATE: PASS')
print('NOTE: this is not a runtime/browser/integration test.')
