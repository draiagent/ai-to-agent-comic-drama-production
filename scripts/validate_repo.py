#!/usr/bin/env python3
"""Offline structural checks; no generation, licensing or visual claims."""
from pathlib import Path
import json, hashlib, re, sys, csv
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok: errors.append(msg)
required=['README.md','LICENSE','COPYRIGHT.md','CHANGELOG.md','CONTRIBUTING.md','project.json','VERSION','validation-report.md','assets/manifest.json']
for p in required:check((ROOT/p).is_file(),'missing: '+p)
for p in ROOT.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception:errors.append('invalid JSON: '+str(p.relative_to(ROOT)))
for p in ROOT.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if '://' in target or target.startswith('#'):continue
  check((p.parent/target.split('#')[0]).exists(),f'broken link: {p.name} -> {target}')
manifest=json.loads((ROOT/'assets/manifest.json').read_text(encoding='utf-8'))
check([x['page'] for x in manifest]==[1,2,3,4],'page sequence')
for item in manifest:
 p=ROOT/item['path']
 check(p.exists(),'missing image: '+str(p))
 if p.exists():
  check(p.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'),'PNG signature: '+p.name)
  check(hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],'image hash: '+p.name)
for p in ROOT.glob('templates/*.csv'):
 with p.open() as f: rows=list(csv.reader(f))
 check(len(rows)==1 and len(rows[0])>=8,'CSV header: '+p.name)
for p in ROOT.glob('docs/0[1-4]-usage.md'):
 body=p.read_text(encoding='utf-8').split('\n\n',2)[2].split('\n---')[0]
 count=len(re.findall(r'[\u4e00-\u9fff]',body))
 check(480<=count<=550,'intro length: '+p.name)
 print(p.name, 'CJK characters:',count)
meta=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
check(meta['version']=='0.1.0','version')
check((ROOT/'VERSION').read_text(encoding='utf-8').strip()==meta['version'],'VERSION differs from project.json')
for p in ['README.md','CHANGELOG.md','RELEASE_NOTES.md']:check(meta['version'] in (ROOT/p).read_text(encoding='utf-8'),'version missing: '+p)
for p in ROOT.rglob('*'):
 if p.is_file():check(p.stat().st_size>0,'empty file: '+str(p))
example=json.loads((ROOT/'examples/palace-shot-vac.json').read_text(encoding='utf-8'))
check(example['review']['status']=='draft' and not example['review']['human_approved'],'example must not claim approval')
check(example['limits']['max_retries']==2,'example retry consistency')
print('STRUCTURAL CHECK:', 'FAIL' if errors else 'PASS')
for e in errors:print(e)
print('LICENSE:',meta['license_status'],'- structural PASS is not legal review.')
sys.exit(bool(errors))
