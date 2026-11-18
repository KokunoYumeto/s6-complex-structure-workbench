"""Exact local Cox/normalization identities; no global source-zero return."""
import json
import sympy as s
from pathlib import Path

x,y,k,l,z,v,r,B,D,sg,Fp,Fm,u,Q,a=s.symbols('x y k l z v r B D sg Fp Fm u Q a')
checks=[]
def check(name, expr, relations=()):
    num=s.together(expr).as_numer_denom()[0]
    if relations:
        num=s.reduced(s.expand(num), list(relations), sg,x,y,k,l,Fp,Fm,u,Q)[1]
    value=s.factor(num)
    assert value==0,(name,value)
    checks.append(name)

# x=s0, y=t1, k=s1-s0, l=t0+t1, sg^2=1+xy.
vv=x*y+(k*y-x*l)/2
qq=k*l-(x*l-y*k)**2/4
fp=((sg+1)*k-x*x*l/(sg+1))/2
fm=((sg+1)*l-y*y*k/(sg+1))/2
rel=[sg**2-1-x*y]
check('actual v from s1*t1-s0*t0',vv-((x+k)*y-x*(l-y))/2)
check('actual q factorization',fp*fm-qq,rel)
mat=s.Matrix([[s.diff(fp,k),s.diff(fp,l)],[s.diff(fm,k),s.diff(fm,l)]])
check('factor-coordinate determinant is sg',mat.det()-sg,rel)
ki=((sg+1)*Fp+x*x*Fm/(sg+1))/(2*sg)
li=(y*y*Fp/(sg+1)+(sg+1)*Fm)/(2*sg)
check('inverse k coordinate',ki.subs({Fp:fp,Fm:fm}, simultaneous=True)-k,rel)
check('inverse l coordinate',li.subs({Fp:fp,Fm:fm}, simultaneous=True)-l,rel)
check('v in factor coordinates',vv.subs({k:ki,l:li},simultaneous=True)-(x*y+(y*Fp-x*Fm)/(2*sg)),rel)
check('finite invariant chart v/q',
      (x*y+(y*Fp-x*Fm)/(2*sg)).subs({x:u*Fp,y:z*Fm},simultaneous=True)
      -Fp*Fm*(u*z+(z-u)/(2*sg)))
# The two physical weights of the factors are -1,+1.
t=s.symbols('t', nonzero=True)
check('Fplus weight -1',fp.subs({x:x/t,y:t*y,k:k/t,l:t*l},simultaneous=True)-fp/t)
check('Fminus weight +1',fm.subs({x:x/t,y:t*y,k:k/t,l:t*l},simultaneous=True)-t*fm)

# Blowing up (s+1,v) with x=s+1, v=x*r.
zz=1/(x-1-r)
BB=x*(x-2)*(x-1-r)
DD=s.factor((BB-2*x*r)/zz)
check('blowup selected normalization X',BB*zz-x*(x-2))
check('blowup selected normalization v',(BB-DD*zz)/2-x*r)
check('finite-chart immersion Jacobian',
      s.Matrix([[s.diff(zz,x),s.diff(zz,r)],[s.diff(BB,x),s.diff(BB,r)]]).det()
      +2*(x-1)/(x-1-r))
ww=x-1-r
CC=x*(x-2)
check('other-chart immersion Jacobian',
      s.Matrix([[s.diff(ww,x),s.diff(ww,r)],[s.diff(CC,x),s.diff(CC,r)]]).det()-(2*x-2))
check('trace index',( (1-2*a)**2-1)/8-a*(a-1)/2)
check('reversed trace index',((1+2*a)**2-1)/8-a*(a+1)/2)
check('trace difference',a*(a+1)/2-a*(a-1)/2-a)
cc=s.symbols('cc')
check('charged ruling mapping-torus index',
      (4*(-a**3*cc)-(-4*a*cc))/24+a*(a*a-1)*cc/6)
check('adjacent-charge wall crossing',
      a*(a*a-1)/6-(a-1)*((a-1)**2-1)/6-a*(a-1)/2)
aux=(1,1,-1,a-1,-a)
phys=(0,0,0,1,-1)
weights_V=[phys[i]-aux[i]/a for i in (0,1,2,3)]
weights_z=[phys[i]-aux[i]/(a-1) for i in (0,1,2,4)]
for i,target in enumerate((-1,-1,1,1)):
    check('V gauge physical weight '+str(i),weights_V[i]-target/a)
    check('z gauge physical weight '+str(i),weights_z[i]-target/(a-1))
KK=s.symbols('K',positive=True)
avec=(1,1,-1,1,-2);dvec=(0,0,0,1,-1)
assert [avec[i]*(avec[i]+KK*dvec[i]) for i in range(5)]==[1,1,1,1+KK,4+2*KK]
checks.append('reduced auxiliary orbit positive derivative')
A2,AD,D2=s.symbols('A2 AD D2')
check('projected physical moment derivative',
      D2-AD*(AD+KK*D2)/(A2+KK*AD)-(A2*D2-AD**2)/(A2+KK*AD))

# Specified fixed-S3 surgery of the reduced disk-bundle model only.
check('reduced disk bundle first Chern class',3-1-2)
check('reduced disk bundle Euler coefficient',(-1)*(-2)-2)
check('reduced disk bundle Pontryagin coefficient',3+(-1)**2+(-2)**2-8)
c1sq=-(1-2*a)**2
c2=-a*(a-1)
check('capped positive spinor adjoint Pontryagin',c1sq-4*c2+1)
k_B=-(c1sq-c2)
ell_B=-(-3+c1sq-4*c2)
check('capped fixed boundary physical Euler cube',k_B-(3*a*a-3*a+1))
check('capped fixed boundary physical Pontryagin pairing',ell_B-4)
check('capped fixed boundary physical index',(4*k_B-ell_B)/24-a*(a-1)/2)
k_Y=-1-k_B.subs(a,2)
ell_Y=-4-ell_B.subs(a,2)
check('specified reduced surgery quotient Euler cube',k_Y+8)
check('specified reduced surgery quotient Pontryagin pairing',ell_Y+8)
check('specified reduced surgery quotient index',(4*k_Y-ell_Y)/24+1)

out={'status':'PASS','scope':'exact local identities only; global attachment and return not assigned',
     'count':len(checks),'checks':checks,
     'local_trace_values':{'a1':[0,1],'a2':[1,3]},
     'specified_reduced_local_surgery':{'physical_k':int(k_Y),'physical_ell':int(ell_Y),'index':-1,'global_attachment':'not identified'},
     'unresolved':'actual global moment/quotient bordism, cap attachment, and physical normal framing'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
