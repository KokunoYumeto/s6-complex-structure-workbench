from pathlib import Path
import datetime,json,sympy as S
r=Path(__file__).resolve().parents[1]
a=S.symbols('a',nonzero=True)
I=S.eye(3)
Ug=I.copy();Ug[1,2]=-1
Uu=I.copy();Uu[0,2]=1
A=a*Ug-I;B=Uu-I
assert Ug*Uu==Uu*Ug
assert S.factor(A.det())==(a-1)**3
Ai=S.simplify(A.inv())
d0=A.col_join(B)
d1=B.row_join(-A)
h1=Ai.row_join(S.zeros(3))
h2=S.zeros(3).col_join(-Ai)
assert d1*d0==S.zeros(3)
assert S.simplify(h1*d0)==I
assert S.simplify(d0*h1+h2*d1)==S.eye(6)
assert S.simplify(d1*h2)==I
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'Explicit symbolic contracting homotopy for the twisted torus local-system Koszul complex.',
 'parameter':'a=exp(2*pi*i*z), a != 1',
 'monodromy_gamma':str(Ug),'monodromy_u':str(Uu),'det_A':str(S.factor(A.det())),
 'inverse_A':str(Ai),'d0':str(d0),'d1':str(d1),'h1':str(h1),'h2':str(h2),
 'verified':['d1*d0=0','h1*d0=I3','d0*h1+h2*d1=I6','d1*h2=I3'],
 'scope':'Exact vanishing of the logarithmic tangent complex on the central fibre for every z outside Z. The normal quotient and its length-one direct image are proved in prose.'}
(r/'records/S6_SERIES_PUBLISH_I_D42_preread_computation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
