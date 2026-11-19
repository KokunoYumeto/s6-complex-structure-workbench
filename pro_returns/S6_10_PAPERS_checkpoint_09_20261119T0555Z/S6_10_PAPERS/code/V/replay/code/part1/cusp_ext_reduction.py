"""Integral chain automorphisms and homotopies reducing all cusp corrections.
The displayed plus-sign MV convention is obtained from the whole-diagram
convention by multiplication by -1 on the cusp chain summand.
"""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('complement_check.py').read_text().split('out={}')[0])

cases=json.loads(Path(__file__).with_name('global_ext_cases.json').read_text())
r=s.Matrix(cases['torsion_cocycle'])
psi=s.Matrix([[0,0,0,1,-1,1,1,-1,-1,1]])
e=s.eye(10)[:,3]
K=s.Matrix.hstack(*[s.eye(10)[:,i]-psi[i]*e for i in range(10) if i!=3])
assert psi*K==s.zeros(1,9) and abs(e.row_join(K).det())==1

def integral_solve(A,B):
 d,u,v=snf(A);rank=A.rank();T=u*B
 assert T[rank:,:]==s.zeros(A.rows-rank,B.cols)
 C=s.zeros(A.cols,B.cols)
 for i in range(rank):
  for j in range(B.cols):
   assert T[i,j]%d[i,i]==0
   C[i,j]=T[i,j]/d[i,i]
 out=v*C;assert A*out==B;return out

k=4
yz,yp,yr=hpresentation(yd(k),yd(k+1));bz,bp,br=hpresentation(dbdry(0,k),dbdry(0,k+1))
j=(yp*yj(k)*bz).col_join(fcusp(k)*bz)
want=s.zeros(yz.cols,9).col_join(K)
Wlift=integral_solve(j,want);Xcycles=bz*Wlift
assert r*Xcycles==s.zeros(1,9)
Ybound=yj(4)*Xcycles
T=integral_solve(yd(5),Ybound)
assert fcusp(4)*Xcycles==K
# Twice the torsion cocycle is the integral coboundary of t.
trow=integral_solve(dbdry(0,4).T,2*r.T).T
assert trow*dbdry(0,4)==2*r
for i in range(9):
 Eta=Xcycles[:,i]*r
 assert Eta*Eta==s.zeros(*Eta.shape)
 assert dbdry(0,4)*Eta==s.zeros(dbdry(0,4).rows,Eta.cols)
 assert Eta*dbdry(0,5)==s.zeros(Eta.rows,dbdry(0,5).cols)
 assert abs((s.eye(Eta.rows)+Eta).det())==1
 print('kernel generator',i,'chain automorphism certified',flush=True)
print('torsion cocycle',r,flush=True)
print('psi',psi,'psi e',psi*e,flush=True)
print('nine integral boundary-cycle lifts and their Y bounding chains verified',flush=True)
out={'psi':psi.tolist(),'canonical_odd_vector':e.tolist(),'kernel_basis':K.tolist(),
     'boundary_H4_lifts':Wlift.tolist(),'boundary_chain_lifts':Xcycles.tolist(),
     'Y_bounding_chains':T.tolist(),'torsion_cocycle':r.tolist(),'twice_cocycle_primitive':trow.tolist(),
     'automorphism_formula':'Id + (boundary_chain_lifts * v) * torsion_cocycle; its square-zero correction has integral inverse Id minus that correction.',
     'homotopy_formula':'Y_bounding_chains * v * torsion_cocycle; even multiples of the canonical odd vector use canonical_odd_vector * twice_cocycle_primitive.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
