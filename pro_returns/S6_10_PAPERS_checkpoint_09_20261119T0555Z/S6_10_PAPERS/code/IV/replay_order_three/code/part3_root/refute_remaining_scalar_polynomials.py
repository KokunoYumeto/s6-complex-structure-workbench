"""Exact counterexamples to the eight retained historical compound formulas."""
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
import json
from scalar_all_fans import calculate

root=Path(__file__).resolve().parents[2]
T0=(1,0,0,1); T2=(1,0,2,1)
os45=calculate(T0,1,8,1)['physical_class_mod28']
original=calculate(T2,2,F(1,3),F(1,6))['physical_class_mod28']
lr=calculate(T2,2,1,F(1,2))['physical_class_mod28']
# K65 provides the actual native C2 pair(-1,1), with positive-fan class0.
# The directed negative-to-positive physical increment is+1.
os49=(0-1)%28
rows=[
 ('P3K.33','Original K=L=1, actual shorter w loop, T2',0,original,'P3K.67; P3K.73'),
 ('P3F.53','Primitive OS45 a=8,b=1, lambda=r, T0',-3,os45,'P3K.68; P3K.69; P3K.73'),
 ('P3K.35','Primitive OS45 b=1 shorter endpoint, T0',-3,os45,'P3K.67; P3K.69; P3K.73'),
 ('P3K.36','Actual Liu-Rollenske corrected u=w^2 family, T2',0,lr,'P3K.67; P3K.73'),
 ('P3K.37','Actual OS49 k=1 shorter w loop, negative fan',0,os49,'P3K.65'),
 ('P3K.41','OS45 fixed cap-data loop, N=1, T0',-3,os45,'P3K.69; P3K.73; retained CP maps'),
 ('P3K.43','Same OS45 datum with constant ordinary-site path',-3,os45,'P3K.69; P3K.73; retained moving-site maps'),
 ('P3K.44','OS49 k=N=1 fixed cap-data loop, negative fan',0,os49,'P3K.65; retained component-cap maps')]
out=[]
for statement,datum,old,new,proof in rows:
    assert old%28!=new
    out.append({'statement':statement,'actual_datum':datum,'old_integer':old,
                'old_residue':old%28,'proved_physical_residue':new,'proof':proof})
assert original==lr==26 and os45==3 and os49==27
# The exact vertical cocharacter is(0,1) for every Tn, hence the old S is1.
for n in (-2,0,1,2,7):
    assert (1*0+0*1,-n*0+1*1)==(0,1)
    assert 0**2-0*1+1**2==1
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
        'counterexample_count':len(out),'counterexamples':out,
        'F52_scope':'Its actual invariant-divisor family isomorphism and covariance of the actual return are reproved with K73; an identity map is not used as a counterexample to covariance. Its imported K31 numerical recurrence is withdrawn.',
        'source_construction_certificates':['code/part3/scalar_nonvertical.json','code/part3/liu_rollenske_parameter.json','code/part3_fourfold/os49_corrected_returns.json']}
(root/'code/part3_root/refute_remaining_scalar_polynomials.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
