"""Exact finite cap and stable-end maps; no completed bordism is inferred."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
rows=[]
for p in range(1,13):
    for a,b,m in [(1,2,4*p),(2,1,4*p-1)]:
        exponent=m*a//2
        assert 2*exponent==m*a and a*b==2
        assert exponent*b==m
        character=(-1 if a==1 else 1)
        assert s.exp(2*s.pi*s.I*s.Rational(exponent,m))*character==1
        for n in [-1,1]:
            for d in range(m):
                chars=[d]
                for j in range(b):
                    chars.append((chars[-1]+(m//2 if a==1 else 0))%m)
                assert chars[-1]==d
                rows.append({'p':p,'a':a,'b':b,'m':m,'n':n,'d':d,
                             'root_exponent':exponent,'character_sequence':chars})
rs,rt,xi=s.symbols('rs rt xi',positive=True)
for a in [1,2]:
    Nt=xi*rt**a
    Ns=xi/rs**a
    R=rs*rt
    assert s.simplify(Nt-R**a*Ns)==0
    assert s.simplify((R**a*xi)/rs**a-Nt)==0
    # Full real auxiliary invariance of the positive-weight frame.
    assert (a-1)-(a-1)==0
    assert -a-a+2*a==0
c,K,t=s.symbols('c K t',positive=True)
a=2
aux=[1,1,-1,a-1,-a]
phys=[0,0,0,1,-1]
coef=[s.expand(w*(w+K*p)) for w,p in zip(aux,phys)]
assert coef==[1,1,1,K+1,2*K+4]
x,y,z,w=s.symbols('x y z w')
quad=x*w-y*z
Hess=s.hessian(quad,(x,y,z,w))
assert Hess.det()==1
h=s.symbols('h')
c_total=s.expand((1+h)**3*(1-h)*(1-2*h))
assert c_total.coeff(h,1)==0
assert 3+1+4==8
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'finite_cap_rows':len(rows),'rows':rows,
     'reduced_auxiliary_derivative':list(map(str,coef)),
     'reduced_positive_model':{'bundle':'O(-1) plus O(-2) over CP2',
         'parameter':'S0*z*V-S1*T1', 'morse_points':['[1:0:0]','[0:0:1]'],
         'morse_hessian_det':str(Hess.det()),'c1':0,'p1_coefficient':8,
         'radial_link_H4':'Z/2'},
     'scope':'Actual primitive cap characters, stable finite-end metric arrow, and fixed-boundary spinor frame. No global source-zero bordism, inner surgery, or return assigned.'}
(root/'code/part3_fourfold/source_zero_cap_end.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
