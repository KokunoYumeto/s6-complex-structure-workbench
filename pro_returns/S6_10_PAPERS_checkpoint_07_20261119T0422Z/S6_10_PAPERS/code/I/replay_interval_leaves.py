"""Recompute every archived norm leaf with directed interval arithmetic.

This program does not accept an archived numerical bound as evidence: it calls
certify on each rational leaf again. The separate exact partition verifier is
also retained and executed. A numerical pass concerns these leaves only; the
omitted local disc and cusp are covered by the analytic proofs in the paper.
"""
from pathlib import Path
from fractions import Fraction as F
from concurrent.futures import ProcessPoolExecutor
import json,time,sys
HERE=Path(__file__).resolve().parent
REPLAY=HERE/'replay_family'
sys.path.insert(0,str(REPLAY))
from f_interval_cert import certify

def verify(row):
 box=tuple(F(x) for x in row['box'])
 ok,details=certify(box)
 return {'box':row['box'],'current_pass':ok,'current_certificate':details}

def main():
 archive=json.loads((REPLAY/'f_interval_parallel_certificate.json').read_text())
 print('keys',list(archive),flush=True)
 rows=archive.get('certified',[])
 if not rows:raise ValueError('Expected nonempty certified leaves')
 start=time.monotonic();out=[]
 with ProcessPoolExecutor(max_workers=6) as pool:
  for index,row in enumerate(pool.map(verify,rows,chunksize=16),1):
   out.append(row)
   if index%1000==0:print('Recomputed',index,'of',len(rows),'elapsed',round(time.monotonic()-start,2),flush=True)
 result={'result':'PASS' if all(x['current_pass'] for x in out) else 'FAIL','norm_leaves_recomputed':len(out),'elapsed_seconds':time.monotonic()-start,'current_leaves':out}
 (HERE/'replay_interval_leaves.output.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='current_leaves'}),flush=True)
if __name__=='__main__':main()
