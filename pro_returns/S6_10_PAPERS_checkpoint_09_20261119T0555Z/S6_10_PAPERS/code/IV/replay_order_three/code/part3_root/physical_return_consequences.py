"""Exact arithmetic after the explicitly proved physical/dual line morphism."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,p):
 assert p,name
 checks.append(name)
primitive=[]
for d in (8,14,20,30):
 a=d//2-1;m=6;n=3*d-6
 ck(f'primitive {d} dual and physical pairs',(-m-n,-4*m)==(-3*d,-24) and n==6*a)
 primitive.append({'d':d,'A_U':-a,'A_M':a,'native':[m,n,a%28],'fixed_flop':(a+n)%28})
vertical=[{'n':n,'physical_class':(-1-3*n*(n-1))%28} for n in range(-84,85)]
for n in range(-84,84):
 ck(f'vertical directed recurrence {n}',(-1-3*(n+1)*n)-(-1-3*n*(n-1))==-6*n)
ck('vertical exact image',sorted({x['physical_class'] for x in vertical})==[5,7,9,13,19,21,23,27])
mutations=[{'j':j,'P':(-1-3*j*(j+1))%28,'R':(-7-24*j*(j+1))%28} for j in range(28)]
ck('R image',sorted({x['R'] for x in mutations})==[1,13,17,21])
ck('R period7',all(mutations[j]['R']==mutations[j+7]['R'] for j in range(21)))
ck('R no period1to6',all(any(mutations[j]['R']!=mutations[j+t]['R'] for j in range(7)) for t in range(1,7)))
rows=[]
for a in (1,2):
 for p in range(1,9):
  for k in range(1,9):
   scalar=0 if a==1 else 3*p-1;fixed=0 if a==1 else -1
   inf=fixed-2*k*scalar;total=a+2*k*scalar
   ck(f'groupoid {a} {p} {k}',total-1+inf==0)
   actual=[]
   for e in (0,1):
    z=(k*scalar+14*e)%28;zj=(a+k*scalar+14*e)%28
    ck(f'paired congruences {a} {p} {k} {e}',(z+zj-total)%28==0 and (zj-z-a)%28==0)
    actual.append([z,zj])
   allsolutions=[[z,(z+a)%28] for z in range(28) if (2*z+a-total)%28==0]
   ck(f'exhaustive order-two choices {a} {p} {k}',sorted(actual)==sorted(allsolutions))
   rows.append({'a':a,'p':p,'k':k,'scalar':scalar,'infinity':inf,'paired_sum':total,'possibilities':actual})
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof':'P3K.68--69','checks':len(checks),'checks_detail':checks,'primitive_rows':primitive,'vertical_rows':vertical,'mutation_rows':mutations,'paired_rows':rows,'scope':'Arithmetic consequences of the written physical line/cap/gluing morphisms. No source-zero order-two choice assigned.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'primitive':primitive,'source_vertical_image':sorted({x['physical_class'] for x in vertical}),'R_image':sorted({x['R'] for x in mutations})}))
