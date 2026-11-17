"""Full integer Smith certificate for the corrected actual global cell model.
Case one is selected by local Poincare--Lefschetz duality of the cusp cap;
cusp_ext_reduction exports the chain automorphisms reducing every allowed
secondary map to this case. Global Poincare duality is not used here.
"""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('cusp_complex.py').read_text().split('result=')[0])
p=Path(__file__).parent
j=json.loads((p/'global_ext_cases.json').read_text())['cases']['1']
Ds={int(k):s.Matrix(v) for k,v in j['differentials'].items()}
ranks=[4,26,87,162,200,156,79,23,3]
out={'method':__doc__,'chain_ranks':ranks,'degrees':{}}
for k in range(9):
 A=Ds[k] if k else s.zeros(0,ranks[k]);B=Ds[k+1]
 if not A.rows:
  DA=A;U=s.eye(0);V=s.eye(A.cols);rk=0
 else:
  DA,U,V=snf(A);rk=A.rank();assert U*A*V==DA
 K=V[:,rk:];Vin=V.inv();Q=(Vin*B)[rk:,:]
 assert (Vin*B)[:rk,:]==s.zeros(rk,B.cols)
 DQ,UQ,VQ=snf(Q);rr=Q.rank();assert UQ*Q*VQ==DQ
 tors=[abs(int(DQ[i,i])) for i in range(rr) if abs(DQ[i,i])>1]
 free=K.cols-rr
 print('degree',k,'chain_rank',ranks[k],'outgoing_rank',rk,'incoming_rank',rr,'free',free,'torsion',tors,flush=True)
 out['degrees'][str(k)]={'differential':A.tolist(),'smith_D':DA.tolist(),'smith_U':U.tolist(),'smith_V':V.tolist(),
     'kernel_basis':K.tolist(),'incoming_in_kernel':Q.tolist(),'incoming_smith_D':DQ.tolist(),
     'incoming_smith_U':UQ.tolist(),'incoming_smith_V':VQ.tolist(),'free':free,'torsion':tors}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
assert [out['degrees'][str(k)]['free'] for k in range(9)]==[1,0,0,0,4,0,0,0,1]
assert not any(out['degrees'][str(k)]['torsion'] for k in range(9))
print('COMPLETE exact global cellular certificate',flush=True)
