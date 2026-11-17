#!/usr/bin/env python3
"""Three explicit sector polarizations after the source/scalar rescaling.

The forms differ by sector. No global common positive form is asserted.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json
ROOT=Path(__file__).resolve().parents[2]
N,r,s=S.symbols('N r s',integer=True,positive=True)
records=[]
for a,b in [(1,2),(2,1)]:
    I=S.eye(2); W=S.Matrix([[1,b],[-a,-2]])
    E=S.Matrix([[0,0],[0,N]])
    H=I+W+E
    QI=S.Matrix([[a,-S.Rational(4)/(N-3)],[-S.Rational(4)/(N-3),b]])
    QW=S.Matrix([[N+3,2*b],[2*b*(N+1),S.Rational(b,a)*(N+3)]])/(N-1)
    QE=S.Matrix([[1,0],[S.Rational(a+b,2),1]])
    forms={'selected':(QI,I),'other_node':(QW,W),'scalar':(QE,E)}
    out={}
    for name,(Q,J) in forms.items():
        P=S.simplify(Q*H); R=S.simplify(Q*J)
        assert P==P.T and R==R.T
        assert S.factor((r*J+s*H).det()) in [
          r*r+(N+1)*r*s+2*N*s*s,
          (N-1)*r*s+2*N*s*s,
          2*N*r*s+2*N*s*s,
        ] or S.factor((r*J+s*H).det()-
            {'selected':r*r+(N+1)*r*s+2*N*s*s,
             'other_node':(N-1)*r*s+2*N*s*s,
             'scalar':2*N*r*s+2*N*s*s}[name])==0
        for nv in range(6,129):
            PP=P.subs(N,nv); RR=R.subs(N,nv)
            assert PP[0,0]>0 and PP.det()>0
            assert RR[0,0]>=0 and RR[1,1]>=0 and RR.det()>=0
        out[name]={
          'Q':[[str(S.factor(e)) for e in Q.row(i)] for i in range(2)],
          'QH':[[str(S.factor(e)) for e in P.row(i)] for i in range(2)],
          'Qboundary':[[str(S.factor(e)) for e in R.row(i)] for i in range(2)],
          'det_QH':str(S.factor(P.det())),
          'leading_QH_minor':str(S.factor(P[0,0])),
          'cone_det':str(S.factor((r*J+s*H).det()))
        }
    # The global simultaneous condition is separately retained.
    x,y,z=S.symbols('x y z')
    Qglobal=S.Matrix([[x,y],[y,z]])
    assert (Qglobal*E-(Qglobal*E).T)[0,1]==N*y
    assert (Qglobal*W-(Qglobal*W).T)[0,1]==b*x-3*y+a*z
    records.append({'a':a,'b':b,'sectors':out,'global_obstruction':'Q symmetric, QE symmetric implies y=0; QW symmetric then z=-(b/a)x, hence Q indefinite unless zero.'})
data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: exact sector-form identities and738 positive-definiteness evaluations',
 'range':'N>=6; choose N a sufficiently large multiple of the actual one-gamma exponent M',
 'records':records,
 'scope':'Each base sector has its own rational form Q with QH positive definite and Qboundary positive semidefinite. A common global positive form does not exist. Actual fans, subdivisions and gluing remain to be constructed.'
}
(ROOT/'code/part3_fourfold/source_zero_sector_forms.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+data['utc']+' — Executed own source_zero_sector_forms.py. Material: explicit distinct sector forms for the rescaled source collision, exact symmetry/determinant formulas,738 positive evaluations, and the retained global-polarization obstruction. No fan or return claim inferred.\n')
print(json.dumps(data,indent=2))
