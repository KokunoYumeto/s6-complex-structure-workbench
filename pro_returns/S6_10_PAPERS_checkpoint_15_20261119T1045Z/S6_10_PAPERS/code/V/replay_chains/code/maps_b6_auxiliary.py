"""Auxiliary exact algebra explored while seeking the B6 central residue.

These tests do not identify a smooth mapping-class lift.  In particular,
the invariant alternating form is indefinite relative to the cusp and
does not supply a polarization or a characteristic-number computation.
"""
from pathlib import Path
import json
import sympy as s

A=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
B=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
x=s.symbols('x:6')
J=s.zeros(4)
for (i,j),v in zip([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],x):
    J[i,j]=v;J[j,i]=-v
invariants=s.linsolve(list(A.T*J*A-J)+list(B.T*J*B-J),x)
J0=J.subs(dict(zip(x,[0,0,6,1,0,0])))
assert A.T*J0*A==J0 and B.T*J0*B==J0
R1=s.Matrix([[0,1],[-1,-1]])
R2=s.Matrix([[0,-1],[1,0]])
products={}
for name,M in [('R1_R2',R1*R2),('R1inv_R2',R1.inv()*R2),
               ('R1_R2inv',R1*R2.inv()),('R1inv_R2inv',R1.inv()*R2.inv())]:
    products[name]={'matrix':M.tolist(),'trace':s.trace(M)}
p,z,c1,c2,sig=s.symbols('p z c1 c2 sig')
phat=(p+z**2)/2
mu=s.expand(((phat**2-sig)/8-s.Rational(5,12)*z**2*phat+z**4/4)/28)
assert s.expand(mu-((p**2-4*sig)/896-p*z**2/192+z**4/384))==0
mucomplex=s.expand(mu.subs({p:c1**2-2*c2,z:c1}))
assert s.expand(28*mucomplex-(-c1**4+4*c1**2*c2+3*c2**2-3*sig)/24)==0
out={'common_alternating_forms':str(invariants),
     'primitive_form':J0.tolist(),'determinant':J0.det(),
     'elliptic_quotient_products':products,
     'spinc_Eells_Kuiper_normalized':str(mu),
     'almost_complex_Eells_Kuiper_normalized':str(mucomplex),
     'almost_complex_Theta7':str(s.expand(28*mucomplex)),
     'limitation':'No smooth lift or numerical Theta7 class follows from these matrices.'}
txt=json.dumps(out,indent=2,default=str)+'\n'
print(txt,end='')
Path(__file__).with_suffix('.out.json').write_text(txt)
