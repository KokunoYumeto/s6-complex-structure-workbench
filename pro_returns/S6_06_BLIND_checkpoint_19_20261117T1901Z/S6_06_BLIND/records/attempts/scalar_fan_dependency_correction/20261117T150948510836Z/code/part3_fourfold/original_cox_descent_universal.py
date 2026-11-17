#!/usr/bin/env python3
"""Universal, cusp-zero integral descent for both K11 sphere signs.

This certificate gives the actual one-period cochain, its comparison with
the sixfold logarithmic primitives, and the simultaneous closed Cox origin.
It does not divide a homotopy-sphere class.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
I = S.eye(4)
zero = S.zeros(4, 1)
T1 = S.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2 = S.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1, A2 = T1.inv().T, T2.inv().T
A0 = (A1*A2).inv()
N1, N2 = I+A1+A1**2, I+A2+A2**2+A2**3
J = S.Matrix([[0,0],[0,0],[1,0],[0,1]])
e1,e2,e3,delta = [I[:,i] for i in range(4)]
K,L,P,Q,eps = S.symbols('K L P Q eps', integer=True)
d, b = 12*K*L, 2*K*L

def stack(parts):
    return S.Matrix.vstack(*parts)

def serial(M):
    return [[str(S.simplify(x)) for x in M.row(i)] for i in range(M.rows)]

def ints(M):
    return [int(x) for x in M]

d0 = S.zeros(28,14)
d0[0:4,0:4], d0[4:8,0:4] = A1-I, A2-I
d0[8:12,4:8], d0[12:16,8:12] = A1-I, A2-I
for i in range(3):
    d0[16+4*i:20+4*i,0:4] = I
d0[16:20,4:8] = -I
d0[20:24,8:12] = -I
d0[24:28,12:14] = -J
d1 = S.zeros(20,28)
d1[0:4,8:12], d1[4:8,12:16] = K*N1, L*N2
d1[8:12,0:4], d1[8:12,8:12] = I, -I
d1[12:16,4:8], d1[12:16,12:16] = I, -I
d1[16:20,0:4], d1[16:20,4:8] = -A0, -A0*A1
for i,A in enumerate((A1,A2,A0)):
    d1[8+4*i:12+4*i,16+4*i:20+4*i] = -(A-I)
assert d1*d0 == S.zeros(20,14)

p = (P*delta-eps*(A1-I)*e1)/6
q = (Q*delta-eps*(A2-I)*e1)/6
x = stack([p,q,p,q,zero,zero,zero])
cover = stack([P*delta,Q*delta,P*delta,Q*delta,zero,zero,eps*e1])
y = stack([eps*e1,eps*e1,eps*e1,S.zeros(2,1)])
assert cover-6*x == d0*y
assert S.simplify((p+A1*q).subs(Q,eps-P)) == zero
target = stack([K*P*delta/2,2*L*Q*delta/3,zero,zero,zero])
assert S.simplify((d1*x-target).subs(Q,eps-P)) == S.zeros(20,1)
assert S.simplify((d1*cover-6*target).subs(Q,eps-P)) == S.zeros(20,1)
shear = I.copy()
shear[3,0] = b
for block in range(7):
    assert shear*x[4*block:4*block+4,:] == x[4*block:4*block+4,:]
assert (A0-I)*e1 == -delta
assert (A1*A2-I)*e1 == delta

v,C,U,Gamma = S.symbols('v C U Gamma')
tau = S.Matrix([eps*Gamma/6,(eps*C+U-eps*d*v)/6])
sigma = S.Matrix([eps*Gamma*v,v*(eps*C+U)-eps*d*v**2/2+eps*d*v/2])
sigma_desc = sigma + S.Matrix([0,eps*K*L*v])
step = S.Rational(1,6)
norm = sum((tau.subs(v,v+j*step) for j in range(6)),S.zeros(2,1))
assert S.simplify(norm-6*tau) == S.Matrix([0,-5*eps*K*L])
assert S.simplify(sigma.subs(v,v+step)-sigma-tau) == S.Matrix([0,5*eps*K*L/6])
assert S.simplify(sigma_desc.subs(v,v+step)-sigma_desc-tau) == S.Matrix([0,eps*K*L])
assert S.simplify(sigma_desc.subs(v,v+1)-sigma_desc-
                  (sigma.subs(v,v+1)-sigma)) == S.Matrix([0,eps*K*L])

samples = []
for kval,lval in [(1,1),(1,2),(1,5),(3,1),(5,1),(5,2),(7,5),(13,7)]:
    assert gcd(3*kval,4*lval)==1
    n0 = pow(4*lval,-1,3*kval)
    n1 = (1-4*lval*n0)//(3*kval)
    for epsval in (1,-1):
        n0signed,n1signed = epsval*n0,epsval*n1
        pval,qval = 4*lval*n0signed,3*kval*n1signed
        subs = {K:kval,L:lval,P:pval,Q:qval,eps:epsval}
        xi = x.subs(subs)
        assert all(z.is_Integer for z in xi)
        assert (pval+2*epsval)%6==0 and (qval-3*epsval)%6==0
        ti = stack([2*kval*lval*n0signed*delta,2*kval*lval*n1signed*delta,zero,zero,zero])
        assert d1.subs(subs)*xi==ti
        samples.append(dict(K=kval,L=lval,eps=epsval,n0=n0signed,n1=n1signed,P=pval,Q=qval,
                            primitive=ints(xi),target=ints(ti)))

Sval = S.symbols('S', integer=True)
kval,ellval = -K*L,-4*K*L
class_value = S.factor(ellval*(Sval-1)/8-kval*(Sval**2-1)/8)
assert class_value == K*L*(Sval-3)*(Sval-1)/8
residue_range = sorted({int(((s-1)*(s-3)//8)%28) for s in range(1,113,2)})
checks = ['d1 d0=0','universal cusp-zero integral primitive',
          'p+A1 q=0 under P+Q=eps','exact finite cyclic norms',
          'S_b x=x','cover-6x=d0(eps e1,eps e1,eps e1,0)',
          'sixfold norm differs by the integer period -5 eps KL delta',
          'sigma_desc step differs from actual translation by eps KL delta',
          'cover framing adjustment is the global eps KL delta loop',
          'all sixteen signed marked integral sample tuples pass']
data = dict(status='PASS: exact integral and cusp-origin identities; geometric comparison recorded separately',
            utc=datetime.now(timezone.utc).isoformat(),
            scope='eps=4Ln0+3Kn1=+1 or -1; gcd(3K,4L)=1',
            T1=serial(T1),T2=serial(T2),A1=serial(A1),A2=serial(A2),A0=serial(A0),
            d0=serial(d0),d1=serial(d1),
            one_step_blocks={name:serial(x[4*i:4*i+4,:]) for i,name in
                             enumerate(['p','q','r','s','u','v','w'])},
            sixfold_blocks={name:serial(cover[4*i:4*i+4,:]) for i,name in
                            enumerate(['p','q','r','s','u','v','w'])},
            comparison_gauge=serial(y),cusp_tau=serial(tau),sigma=serial(sigma),
            closed_original_sigma=serial(sigma_desc),samples=samples,
            original_fan_formula=str(class_value),original_KL1_range=residue_range,
            checks=checks)
(ROOT/'code/part3_fourfold/original_cox_descent_universal.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+data['utc']+' — Executed own code/part3_fourfold/original_cox_descent_universal.py. '
              'Reason: actual one-period simultaneous Cox descent. Material: full symbolic integer complex, '
              'universal cusp-zero primitive, exact sixfold coboundary, literal bounded cusp translation '
              'and closed original-loop origin; no homotopy-sphere class is divided.\n')
print('p =',p.T,'; q =',q.T)
print('tau =',tau.T)
print('sigma_desc =',sigma_desc.T)
print('Original positive-sphere fan expression:',class_value)
print('KL=1 exact fan residues:',residue_range)
print('PASS:', '; '.join(checks))
