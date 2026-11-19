"""Exact Chern/blowup identity for P4.36."""
from pathlib import Path
import json
import sympy as sp
c,d,a,b=sp.symbols('c d a b',integer=True)
checks=[]
for e in (0,1):
 delta=-c*c+(1+e)*c+c*d+(1-2*e)*d-d*d
 transformed=sp.expand(delta.subs({c:a+1,d:b+1-e}))
 assert sp.expand(transformed-(1-a*a-b*b+a*b))==0
 equal=[]
 maximum=-10000
 for ci in range(-30,31):
  for di in range(-30,31):
   val=int(delta.subs({c:ci,d:di}))
   maximum=max(maximum,val)
   if val==1:equal.append([ci,di])
 assert maximum==1 and equal==[[1,1-e]]
 checks.append({'epsilon':e,'increment':str(delta),'translated_increment':str(transformed),
                'executed_integer_box':[-30,30],'maximum':maximum,'equality_pairs':equal})
result={'proof':'P4.36','checks':checks,'unrestricted_proof':'1-(a²+b²-ab), positive definite; equality iff a=b=0','all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('P4.36 exact blowup identities: PASS')
for row in checks:
 print('epsilon',row['epsilon'],'increment =',row['translated_increment'],'unique equality (c,d)=',row['equality_pairs'][0])
print('The exact positive quadratic identity proves the unrestricted integer bound.')
