#!/usr/bin/env python3
"""Persist exact comparator/repository and source-availability audit metadata.
Research full text remains outside Q03_DEPOSIT. No Lean build is performed.
"""
import hashlib,json,re,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CACHE=ROOT/'retrieved_sources';OUT=ROOT/'Q03_DEPOSIT/code'
PIN='4eaee87548250b2682affda7d05d947c05554bae'
url=f'https://raw.githubusercontent.com/openai/math/{PIN}/lean/ComparatorChallenges/ThreeMachine.lean'
p=CACHE/'openai/ThreeMachine.lean';p.parent.mkdir(parents=True,exist_ok=True)
if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=40).read())
b=p.read_bytes();s=b.decode();lines=s.splitlines()
report={'date':'2026-11-15','timezone':'Europe/Berlin','comparator':{
 'url':url,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
 'capacity_three_line':next(i+1 for i,l in enumerate(lines) if 'card ≤ 3' in l),
 'release_declaration_line':next(i+1 for i,l in enumerate(lines) if 'def ReleaseTheorem' in l),
 'exponent_150020_line':next(i+1 for i,l in enumerate(lines) if '^ 150020' in l),
 'sorry_lines':[i+1 for i,l in enumerate(lines) if re.search(r'\bsorry\b',l)],
 'interpretation':'Comparator target declaration contains sorry; it is not a completed proof. No Lean build or theorem verification is claimed.'}}
base=CACHE/'drbh/scheduling-proof-exploration-bbd30137258b15d8c5caedd035d72e8e8a875dbd/OAI/Computability/Scheduling'
files=sorted(base.glob('*.lean'))
hits=[]
for f in files:
 for i,l in enumerate(f.read_text().splitlines(),1):
  if re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b',l):hits.append({'file':f.name,'line':i})
report['drbh']={'commit':'bbd30137258b15d8c5caedd035d72e8e8a875dbd','lean_files_scanned':len(files),'placeholder_or_axiom_hits':hits,'build_replayed':False,'scope':'Model.lean ReleaseTheorem; Main.lean main_theorem; source statements inspected.'}
baseurl='https://kokunoyumeto.github.io/open-math-courses-public/courses/three-machine-unit-job-scheduling/'
report['course_extra_metadata']=[]
for name in ['course.json','providers.json','provenance.json']:
 p=CACHE/'course'/name
 row={'url':baseurl+name}
 if p.exists():
  b=p.read_bytes();row.update(status='opened',bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 else:
  try:
   with urllib.request.urlopen(baseurl+name,timeout=25) as r:b=r.read()
   p.write_bytes(b);row.update(status='opened',bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  except Exception as e:row.update(status='unavailable',error=str(e))
 report['course_extra_metadata'].append(row)
(OUT/'C_followup_source_checks_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
