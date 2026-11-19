#!/usr/bin/env python3
"""Inspect the actual pinned scheduling proof source, separately from comparator.
This is a source scan, never a substitute for Lean type-checking.
"""
import concurrent.futures,hashlib,json,re,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PIN='4eaee87548250b2682affda7d05d947c05554bae'
directory='lean/OAI/Computability/Scheduling'
url=f'https://api.github.com/repos/openai/math/contents/{directory}?ref={PIN}'
def fetch(u):
 with urllib.request.urlopen(u,timeout=40) as r:return r.read()
listing=json.loads(fetch(url));cache=ROOT/'retrieved_sources/openai_actual'
def read_file(x):
 u=f'https://raw.githubusercontent.com/openai/math/{PIN}/'+x['path']
 b=fetch(u);p=cache/x['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 lines=b.decode().splitlines()
 return {'file':x['path'],'url':u,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
 'placeholder_or_axiom_lines':[i+1 for i,l in enumerate(lines) if re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b',l)],
 'release_declaration_lines':[i+1 for i,l in enumerate(lines) if 'def ReleaseTheorem' in l],
 'main_theorem_lines':[i+1 for i,l in enumerate(lines) if 'theorem main_theorem' in l]}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:rows=list(e.map(read_file,[x for x in listing if x['type']=='file' and x['name'].endswith('.lean')]))
report={'date':'2026-11-15','timezone':'Europe/Berlin','commit':PIN,'directory_api':url,'files':rows,'build_replayed':False,'interpretation':'Actual Main.lean proof body is distinct from the comparator sorry. Text scan is not Lean verification.','earlier_attempt':'Repository-wide recursive tree was truncated before this directory; contents API recovered the actual listed directory.'}
comparator=ROOT/'retrieved_sources/openai/ThreeMachine.lean'
model=cache/directory/'Model.lean'
if comparator.exists():
 target=b'theorem main_theorem : ReleaseTheorem := by\n  sorry\n\n'
 report['comparator_definitions_equal_model_after_deleting_target_placeholder']=comparator.read_bytes().replace(target,b'')==model.read_bytes()
(ROOT/'Q03_DEPOSIT/code/C_openai_formal_sources_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'{len(rows)} actual scheduling Lean files opened')
print('placeholder/axiom text matches',[(r['file'],r['placeholder_or_axiom_lines']) for r in rows if r['placeholder_or_axiom_lines']])
for r in rows:
 if r['main_theorem_lines'] or r['release_declaration_lines']:print(r)
