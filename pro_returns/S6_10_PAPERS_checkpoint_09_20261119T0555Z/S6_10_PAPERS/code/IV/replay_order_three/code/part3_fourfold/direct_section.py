"""Coordinate verification for the independent analytic index in P3K.8."""
import json
from pathlib import Path
import sympy as s

t,z,q,X,Y=s.symbols('t z q X Y')
F=lambda tt,xx,yy: yy**2-xx**3+3*tt**3*(tt-1)*xx-2*tt**4*(tt-1)**2
px=0
py=s.sqrt(2)*t**2*(t-1)
assert s.expand(F(t,px,py)) == 0
iv=s.expand(F(z**3,z**4*X,z**6*Y)/z**12)
iii=s.expand(F(1+z**4,z**2*X,z**3*Y)/z**6)
inf=s.expand(q**6*F(1/q,X/q**2,Y/q**3))
piv=s.simplify(py.subs(t,z**3)/z**6)
piii=s.simplify(py.subs(t,1+z**4)/z**3)
pinf=s.simplify(q**3*py.subs(t,1/q))
assert s.simplify(iv.subs({X:0,Y:piv})) == 0
assert s.simplify(iii.subs({X:0,Y:piii})) == 0
assert s.simplify(inf.subs({X:0,Y:pinf})) == 0
assert piv.subs(z,0) == -s.sqrt(2)
assert piii.subs(z,0) == 0
assert pinf.subs(q,0) == s.sqrt(2)
assert s.diff(inf,Y).subs({X:0,Y:s.sqrt(2),q:0}) != 0
result={
 'status':'PASS',
 'source_section':['0',str(py)],
 'IVstar_base_change':{'map':'t=z^3; x=z^4 X; y=z^6 Y',
                     'equation':str(iv),'section':['0',str(piv)],
                     'limit':['0',str(piv.subs(z,0))]},
 'III_base_change':{'map':'t=1+z^4; x=z^2 X; y=z^3 Y',
                  'equation':str(iii),'section':['0',str(piii)],
                  'limit':['0','0']},
 'I1_chart':{'map':'q=1/t; X=q^2 x; Y=q^3 y',
            'equation':str(inf),'section':['0',str(pinf)],
            'smooth_limit':['0',str(pinf.subs(q,0))]},
 'scope':'Finite section coordinates give direct nonidentity specialization; no height, signature, line square or Pontryagin evaluation is used in this computation.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
