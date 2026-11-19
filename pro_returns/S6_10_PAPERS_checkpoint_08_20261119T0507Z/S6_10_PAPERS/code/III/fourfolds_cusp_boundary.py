"""Integral boundary torsion of the primitive rank-three Kuhn cusp.

Together with the proved cap groups, Poincare--Lefschetz duality shows
that the primitive kernel in cap H4 maps to the nonzero boundary Z/2.
This supplies the free-cusp d2 column in the universal homology test.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parent
M=s.eye(6)
for i in range(3):M[i,i+3]=1
records=[]
for q in range(1,6):
 basis=list(combinations(range(6),q))
 E=s.Matrix([[M.extract(I,J).det() for J in basis] for I in basis])
 C=E-s.eye(len(basis))
 D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(s.ZZ))
 D,U,V=[t.to_Matrix() for t in (D,U,V)]
 assert U*C*V==D and abs(U.det())==abs(V.det())==1
 diag=[int(D[i,i]) for i in range(D.rows) if D[i,i]]
 tors=[abs(x) for x in diag if abs(x)>1]
 assert tors==([2] if q==3 else [])
 rec={'degree':q,'smith_nonzero':[abs(x) for x in diag],
      'free_cokernel_rank':len(basis)-len(diag),'torsion':tors}
 if q==3:
  i=next(i for i in range(D.rows) if abs(D[i,i])==2)
  w=U.inv()[:,i]
  z=(s.Rational(2,D[i,i])*V[:,i]).applyfunc(s.simplify)
  assert all(x.q==1 for x in w) and all(x.q==1 for x in z)
  assert C*z==2*w and (U*w)[i]==1
  rec.update({'exterior_basis':basis,'torsion_generator':list(w),'twice_generator_preimage':list(z),
              'nonzero_certificate':'The Smith coordinate of the generator is1 modulo2.'})
 records.append(rec)
 print('exterior degree',q,'nonzero Smith',rec['smith_nonzero'],
       'free rank',rec['free_cokernel_rank'],'torsion',tors)
 if q==3:
  print('primitive order-two representative:',list(w))
  print('integer preimage of twice representative:',list(z))

out={'canonical_cusp':M.tolist(),'exterior_cokernels':records,
     'boundary_H4_torsion':'Z/2',
     'cap_input':'E.1.3: H3(cap)=Z9; H4(cap) is free and specializes onto invariant degree4 with primitive kernelZ.',
     'deduction':'The PL target H5(cap,boundary)=H3(cap) is free, so boundary torsion lifts. Its fibre restriction vanishes, hence its lift lies in the primitive kernelZ, whose generator therefore restricts to the nonzero order-two class.'}
(ROOT/'fourfolds_cusp_boundary.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('ALL INTEGRAL BOUNDARY CERTIFICATES PASSED')
