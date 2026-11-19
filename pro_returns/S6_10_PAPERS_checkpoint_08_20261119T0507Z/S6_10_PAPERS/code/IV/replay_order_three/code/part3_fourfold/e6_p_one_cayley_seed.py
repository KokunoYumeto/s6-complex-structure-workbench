"""Exact native p-one Cayley cones; common-fan extension is separate."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as S
base=Path(__file__).resolve().parents[2]
cones=[]
for cell in range(3):
    I=lambda r:S.Matrix([cell+1,r,1,0])
    J=lambda r:S.Matrix([cell,r,1,0])
    E=lambda r:S.Matrix([0,r,0,1])
    raw=[('x',r,[I(r-1),I(r),J(0),E(0)]) for r in range(1,4)]
    raw += [('y',r,[J(r-1),J(r),I(3),E(0)]) for r in range(1,4)]
    raw += [('v',r,[E(r-1),E(r),I(3),J(3)]) for r in range(1,5)]
    for kind,r,rays in raw:
        N=S.Matrix.hstack(*rays);det=int(N.det());assert abs(det)==1
        perm=[0,1,2,3] if det==1 else [1,0,2,3]
        NN=N[:,perm];assert NN.det()==1
        physical=list(NN.inv()*S.Matrix([0,1,0,0]));assert sorted(physical)==[-1,0,0,1]
        cones.append({'source_cell':cell,'factor':kind,'factor_index':r,
                      'raw_rays':[list(map(int,x)) for x in rays],
                      'positive_order_permutation':perm,
                      'rays':[list(map(int,NN[:,j])) for j in range(4)],
                      'physical_weights':list(map(int,physical))})
source=base/'notes/part3_e6_p_one_cayley_working.md'
common=base/'code/part3_root/e6_common_period_fan.json'
out={'status':'PASS_NATIVE_CAYLEY_SEED','utc':datetime.now(timezone.utc).isoformat(),
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'common_input_sha256':hashlib.sha256(common.read_bytes()).hexdigest(),
     'cone_count':len(cones),'cones':cones,
     'native_lattice':['Z','W_C','P','v'],
     'h_valuation_map':[[1,0,3,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
     'B_valuation_map':[[1,0,-1,0],[0,1,3,4],[0,0,1,0],[0,0,0,1]],
     'full_units':{'h':['p','p^-2'],'B':['1','c'],'corner_relation':'b=v^-4 c^-1'},
     'pending':'The common510 upper-fan extension, full parent morphisms and shared/period facets.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','cone_count','source_sha256','common_input_sha256')},indent=2))
