"""Fresh symbolic checks for the actual C.7.3/C.7.4 period identities.

This program was written from the statements, before opening the old
computation scripts. It proves the displayed rational identities; it
does not certify a period conjecture or a motivic comparison theorem.
"""
import sympy as S
import json
from pathlib import Path

J=S.Matrix([[0,1],[-1,0]])
a,b,c,d=S.symbols('a b c d')
M=S.Matrix([[a,b],[c,d]])
assert M.T*J*M==M.det()*J
x,y,u,v=S.symbols('x y u v')
h=S.Matrix([x,y]); k=S.Matrix([u,v])
def lie(q):
    A=S.zeros(4)
    A[1:3,0]=q
    A[3,1:3]=q.T*J
    return A
comm=lie(h)*lie(k)-lie(k)*lie(h)
expected=S.zeros(4);expected[3,0]=2*(h.T*J*k)[0]
assert comm==expected
r,s,D=S.symbols('r s D',real=True)
cm=S.Matrix([[r,-D*s],[s,r]])
assert cm.T*J*cm==(r*r+D*s*s)*J
w1,w2,e1,e2,q1,q2=S.symbols('w1 w2 e1 e2 q1 q2')
coef=S.Matrix([[w1,-e1],[w2,-e2]])
sol=coef.inv()*S.Matrix([q1,q2])
assert all(S.simplify(z)==0 for z in coef*sol-S.Matrix([q1,q2]))
wb1,wb2,z,zb=S.symbols('wb1 wb2 z zb')
realcoef=S.Matrix([[w1,w2],[wb1,wb2]])
ab=realcoef.inv()*S.Matrix([z,zb])
eta=(e1*(z*wb2-zb*w2)+e2*(zb*w1-z*wb1))/(w1*wb2-wb1*w2)
assert S.simplify((S.Matrix([[e1,e2]])*ab)[0]-eta)==0
out={'method':'SymPy polynomial and rational-function matrix identities; new implementation',
     'checks':{'isogeny_polarization_identity':True,'heisenberg_commutator':True,
               'CM_Rosati_pairing_scale':True,'Legendre_system_inversion':True,'real_linear_eta_formula':True},
     'commutator':str(comm[3,0]),'determinant':str(S.factor(coef.det())),
     'CM_scale':str(r*r+D*s*s),
     'scope':'Exact algebra only. Period/motivic source applications are checked separately.'}
dest=Path(__file__).with_suffix('.output.json');dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
