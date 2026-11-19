"""Fresh exact checks written for S6_SERIES_GRIND, 2026-11-19.

The earlier physical_line_orientation.py and p3f22_normalization.py were
not read or imported. This program derives the quaternion maps by their
multiplication table, exterior products by permutation parity, and the
spin-c characteristic polynomial by formal degree extraction.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as S

checks = []
def check(name, value, expected):
    assert value == expected, (name, value, expected)
    checks.append({'name':name, 'value':str(value), 'expected':str(expected)})

# Quaternion products in (1,i,j,k), as a full bilinear operation.
mul = [
 [(1,0),(1,1),(1,2),(1,3)],
 [(1,1),(-1,0),(1,3),(-1,2)],
 [(1,2),(-1,3),(-1,0),(1,1)],
 [(1,3),(1,2),(-1,1),(-1,0)],
]
def qm(a,b):
 out=[0]*4
 for i,ai in enumerate(a):
  for j,bj in enumerate(b):
   sign,k=mul[i][j];out[k]+=sign*ai*bj
 return S.Matrix(out)
e=[S.eye(4)[:,i] for i in range(4)]
hopf=lambda v:qm(v,e[1])-qm(e[1],v)
check('Hopf derivative on j',hopf(e[2]),S.Matrix([0,0,0,-2]))
check('Hopf derivative on k',hopf(e[3]),S.Matrix([0,0,2,0]))
check('Cox real chart determinant',S.det(S.Matrix.hstack(e[0],e[1],e[2],-qm(e[2],e[1]))),1)
check('physical circle-first orientation',S.det(S.Matrix.hstack(-e[1][1:4,0],e[2][1:4,0],e[3][1:4,0])),-1)
check('right projective chart orientation',S.det(S.Matrix.hstack(hopf(e[2])[2:4,0],hopf(-e[3])[2:4,0])),-4)
check('positive-spinor projective chart orientation',S.det(S.Matrix.hstack(hopf(e[2])[2:4,0],hopf(e[3])[2:4,0])),4)

# Exterior algebra in the ordered basis (dalpha,du,dv,dgamma,dtheta).
def wedge(a,b):
 out={}
 for ia,ca in a.items():
  for ib,cb in b.items():
   word=ia+ib
   if len(set(word))!=len(word):continue
   inv=sum(word[i]>word[j] for i in range(len(word)) for j in range(i+1,len(word)))
   key=tuple(sorted(word));out[key]=S.expand(out.get(key,0)+(-1)**inv*ca*cb)
 return {k:v for k,v in out.items() if v!=0}
n,alpha,theta,s=S.symbols('n alpha theta s')
beta={(1,):-n,(2,):-n*alpha+6*n*theta}
curv={(0,3):1,(0,2):n}
db={(0,2):-n,(4,2):6*n}
check('F squared',wedge(curv,curv),{})
check('d beta squared',wedge(db,db),{})
check('beta F d beta',wedge(wedge(beta,curv),db),{(0,1,2,3,4):6*n*n})
check('outward decreasing-cutoff transgression',-3*S.integrate(2*s*6*n*n,(s,0,1)),-18*n*n)

# Obtain the degree-eight spin-c index from exp(z/2) A-hat.
t,z,p1,p2,sigma=S.symbols('t z p1 p2 sigma')
Ahat=1-p1*t**2/24+(7*p1**2-4*p2)*t**4/5760
index=S.expand(S.series(S.exp(z*t/2),t,0,5).removeO()*Ahat).coeff(t,4)
check('degree-eight index polynomial',index,z**4/384-z*z*p1/192+(7*p1*p1-4*p2)/5760)
with_signature=S.expand(index.subs(p2,(45*sigma+p1*p1)/7))
check('spin-c Eells-Kuiper polynomial',with_signature,(p1*p1-4*sigma)/896-z*z*p1/192+z**4/384)

# Compute characteristic pairings from inverse intersection form, without
# reducing k to zero and without using the homomorphism property.
k,ell=S.symbols('k ell',integer=True)
Q=S.Matrix([[0,1],[1,k]])
pp=S.Matrix([3,ell+k]);zz=S.Matrix([1,k])
check('intersection determinant',Q.det(),-1)
pp2=S.expand((pp.T*Q.inv()*pp)[0]);zzpp=S.expand((zz.T*Q.inv()*pp)[0]);zz2=S.expand((zz.T*Q.inv()*zz)[0])
check('p1 squared',pp2,6*ell-3*k)
check('z squared p1',zzpp,ell+k)
check('z fourth',zz2,k)
boundary_mu=S.expand(pp2/S.Integer(896)-zzpp/S.Integer(192)+zz2/S.Integer(384))
check('bounding manifold invariant',boundary_mu,(ell-4*k)/672)
check('oriented Hopf gluing invariant',-boundary_mu,(4*k-ell)/672)
check('lambda a',(-boundary_mu).subs({k:1,ell:4}),0)
check('lambda b',(-boundary_mu).subs({k:8,ell:8}),S.Rational(1,28))
check('Milnor sphere check',S.Rational(36-4,896),S.Rational(1,28))
check('dual-line index transport',S.expand((4*(-k)-(-ell))/24),-(4*k-ell)/24)

# Additional sweep arithmetic, with every scope retained in the report.
import math
gcd_cases=0
for n0 in range(-60,61):
 for k0 in range(1,25):
  if math.gcd(n0,3*k0)==1:
   for d0 in range(-12,13):
    assert math.gcd(3*k0,n0,3*d0)==1
    gcd_cases+=1
check('OS49 excluded noncoprime cap gcd',math.gcd(3,3),3)
check('OS49 extra torsion index example',math.gcd(3,3,3),3)
for m in [12,13,20,100]:
 check(f'comb tangent Euler characteristic m={m}',(2*m+1)-(8*m+1)+(6*m+1),1)
check('m12 comb Kuranishi dimension',8*12+1,97)

result={'checks':checks,'total_exact_checks':len(checks),'finite_gcd_examples':gcd_cases,
 'scope':'Quaternion, form and characteristic-number arithmetic. Geometric realization and cited coordinates remain theorem inputs; source matching is recorded separately.'}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
