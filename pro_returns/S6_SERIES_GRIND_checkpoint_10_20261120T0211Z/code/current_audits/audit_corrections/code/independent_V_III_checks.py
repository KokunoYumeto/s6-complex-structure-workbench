"""Fresh exact checks: P3F.34 determinantal divisors, and V source transports.

No earlier computational program is imported. The geometric pair sequence,
boundary basis and the normal-circle values are retained theorem inputs.
"""
from pathlib import Path
from math import gcd
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

out=Path(__file__).with_suffix('.json')
checks=0
def check(x):
    global checks
    assert x
    checks+=1

k,n,d=sp.symbols('k n d',integer=True)
A=sp.Matrix([[3*d,3*k],[-n,0],[0,n]])
normal=sp.Matrix([-n,-3*d,3*k])
check(normal.T*A==sp.zeros(1,2))
check(A[:,0].cross(A[:,1])==n*normal)
minors=[sp.factor(A.extract(rr,[0,1]).det()) for rr in [(0,1),(0,2),(1,2)]]
check(minors==[3*k*n,3*d*n,-n*n])

counts={'triples':0,'free':0,'noncoprime_free':0,'n_zero_free':0,'smith_forms':0}
witnesses={}
for kval in range(1,19):
 for nval in range(-12,13):
  for dval in range(-8,9):
   counts['triples']+=1
   m=3*kval
   free=gcd(gcd(kval,nval),dval)==1 and (nval%3!=0 or kval%3==0)
   # Direct test of every nonidentity affine power from its image/norm equation.
   fixed=False
   for j in range(1,m):
    if j%3==0:
     s=j//3
     has_fixed=(s*nval)%kval==0 and (s*dval)%kval==0
    else:
     has_fixed=(j*nval)%m==0 and (3*j*dval)%m==0
    fixed |= has_fixed
   check(free==(not fixed))
   if not free:continue
   counts['free']+=1
   g=gcd(gcd(m,nval),3*dval)
   check(g in (1,3))
   if nval:
    check(nval%g==0)
    delta1=gcd(gcd(3*dval,m),abs(nval))
    delta2=gcd(gcd(abs(m*nval),abs(3*dval*nval)),nval*nval)
    check((delta1,delta2//delta1)==(g,abs(nval)))
    if gcd(nval,m)==1:check(g==1)
    else:counts['noncoprime_free']+=1
    if counts['free']%11==0 or (kval,nval,dval)==(3,3,1):
     sm=smith_normal_form(A.subs({k:kval,n:nval,d:dval}),domain=sp.ZZ)
     check([abs(int(sm[i,i])) for i in range(2)]==[g,abs(nval)])
     counts['smith_forms']+=1
   else:
    counts['n_zero_free']+=1
    check(kval%3==0 and gcd(kval,dval)==1 and g==3)
    # In ker(0,-3d,3k), basis is e_psi and (0,k,d).
    check(gcd(m,3*dval)==3)
   if (kval,nval,dval) in [(3,3,1),(3,0,1),(1,1,0)]:
    witnesses[str((kval,nval,dval))]={'g':g,'transfer':str(A.subs({k:kval,n:nval,d:dval})),
                                    'predicted_H2':('Z/3 + Z/3' if nval==3 else 'Z^2 + Z/3' if nval==0 else '0')}

# Actual common-root divisor transport: T=4D1-D2, 15D1-4D2=div(t/(t-1)).
T=sp.Matrix([4,-1]); q3L=sp.Matrix([5,-1]);q5L=sp.Matrix([12,-3])
check(q5L==3*T)
check(5*T-q3L==sp.Matrix([15,-4]))

# Realification and index-polynomial compatibility for N=3HP2#(-HP2).
eps=[1,1,1,-1];a=[1,1,1,1];c2sq=sum(e*x*x for e,x in zip(eps,a))
euler=6;p1sq=4*c2sq;p2=c2sq+2*euler
check((c2sq,p1sq,p2)==(2,8,14))
check((p2-sum(e*x*(2*x-1) for e,x in zip(eps,a)))%4==0)
check(p2-c2sq==2*euler)
check(4*p2-p1sq==8*(4+2)) # Huijun Yang Theorem 2, n=4.
check((9*sum(eps))%2==0) # Huijun Yang Theorem 1, n=4.
sig=sp.Rational(7*p2-p1sq,45)
check(sig==2)
H=[[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]]
chi=[sum((-1)**q*row[q] for q in range(5)) for row in H]
idx=[sp.Rational(3*c2sq-euler,720),sp.Rational(3*c2sq-31*euler,180),sp.Rational(3*c2sq+79*euler,120)]
check(chi[:3]==idx)
check(chi==[0,-1,4,-1,0])
check(sum((-1)**p*chi[p] for p in range(5))==euler)

report={'checks':checks,'status':'passed','P3F34':counts,'symbolic_transfer_matrix':str(A),
        'two_by_two_minors':[str(x) for x in minors],
        'universal_result':'For n nonzero, determinantal divisors g and |n|g give invariant factors g,|n|. Saturation of ker(normal) makes this the same torsion quotient in the primitive rank-two kernel.',
        'sample_witnesses':witnesses,
        'V_realification':{'c2_squared':c2sq,'p1_squared':p1sq,'p2':p2,'c4':euler,'signature':str(sig),'chi_p':chi},
        'scope':'Arithmetic and source-convention checks only. The geometry of the actual boundary basis, pair sequence, smooth cap and tangent bundle remains the named proved input.'}
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
