#!/usr/bin/env python3
"""Run every mathematical computation and validate the statement ledger.

With --sources also verify the attached archive extracted as ../background/.
That source archive is not duplicated in this deliverable.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--sources',action='store_true')
args=parser.parse_args()
jobs=['a_calculations.py','b_dictionary.py','b_families.py','b_topology.py',
      'c_double_complex.py','c_sign_and_fibre.py','d_exact.py',
      'd_koszul.py','d_division_polynomials.py','d_comb.py',
      'a_metadata.py','b_metadata.py','c_metadata.py','assemble.py']
if args.sources: jobs.insert(0,'00_sources.py')
record=[]
for name in jobs:
    start=time.monotonic()
    result=subprocess.run([sys.executable,str(ROOT/'code'/name)],cwd=ROOT,capture_output=True,text=True)
    target=ROOT/'outputs'/('reproduce_'+Path(name).stem+'.txt')
    target.write_text(result.stdout+result.stderr)
    entry={'program':'code/'+name,'returncode':result.returncode,'seconds':round(time.monotonic()-start,3),
           'output':str(target.relative_to(ROOT))}
    record.append(entry)
    print(f'{name}: exit {result.returncode}',flush=True)
    if result.returncode:
        print(result.stdout[-2000:]+result.stderr[-2000:])
        break
(ROOT/'outputs/reproduction.json').write_text(json.dumps(record,indent=2)+'\n')
assert len(record)==len(jobs) and all(x['returncode']==0 for x in record)
print(f'All {len(jobs)} programs succeeded.')
