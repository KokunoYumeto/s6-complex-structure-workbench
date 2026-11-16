"""Exact conjugacy invariant for the previously proved integral family."""
from pathlib import Path
import sympy as S
v=S.Symbol('v');I=S.eye(5);A=S.zeros(5)
for j in range(5):A[(j+1)%5,j]=1
q=v*v-v+1
X=I[:,0].row_join(I[:,2]+v*I[:,4])
Y=S.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
B=A.inv()*(I-X*Y)
f=S.factor(1+S.trace(A*B**3))
assert S.Poly(f,v).degree()>0
print('trace(M1*M2^3) =',f)
print('degree =',S.Poly(f,v).degree())
print('values0,1,2 =',[f.subs(v,j) for j in range(3)])
(Path(__file__).resolve().parents[1]/'records/fourfolds_unbounded_trace.json').write_text(
    __import__('json').dumps({'polynomial':str(f),'degree':S.Poly(f,v).degree(),
                            'values':[int(f.subs(v,j)) for j in range(3)]},indent=2)+'\n')
