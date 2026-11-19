from pathlib import Path
from itertools import product
import json,datetime
cases=[]
for n in range(3):
 for ds in product(range(1,3),repeat=n):
  if sum(ds)>2:continue
  for rs in product(range(1,4),repeat=n):
   if any(r-1>d for r,d in zip(rs,ds)):continue
   b=sum(r-1 for r in rs)
   if b>1:continue
   s=sum(rs);assert s==b+n and s<=1+sum(ds)
   if sum(ds)==0:assert s==0
   cases.append({'delta':ds,'branches':rs,'b1':b,'s':s})
r={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'passed','count':len(cases),'cases':cases,'scope':'Only the finite arithmetic totals; geometry is proved in the prereading note.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
