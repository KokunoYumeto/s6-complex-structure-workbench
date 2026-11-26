#!/usr/bin/env python3
"""LC auxiliary comparison after individual original exposure.

Reads only the frozen new LC data.  It never executes a historical target
program and does not regenerate or modify any fresh evidence or global file.
"""
from pathlib import Path
from math import gcd
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'agents/continuation7_iii_odd_cubic/S6_SERIES_PUBLISH_III_02LC_fresh_data.json'
EXPECTED = '8503ee12fd4374c45fe42cfa6d2e571a1b7e874b6ff50de7f0ebe129f8a31795'
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == EXPECTED
data = json.loads(DATA.read_text())
print('Post-exposure LC auxiliary check:', datetime.now(timezone.utc).isoformat())
print('Frozen data SHA256:', EXPECTED)

z, v, ell, H, G, R = S.symbols('z v ell H G R')
a, b = S.symbols('a b', positive=True, integer=True)
state = S.Matrix([z, v, ell])
h = S.Matrix([z+H, v+a*G, ell-2*a*z])
f = S.Matrix([z-b*G, v+R, ell-a*b*G+b*R+2*b*v])
j = S.Matrix([-z, -v, ell-2*a*z])
hi = S.Matrix([z-H, v-a*G, ell+2*a*(z-H)])
fi = S.Matrix([z+b*G, v-R, ell+a*b*G+b*R-2*b*v])
h0 = S.Matrix([z+H, v+a*G, ell-a*H-2*a*z])
f0 = S.Matrix([z-b*G, v+R, ell+b*R+2*b*v])
j0 = S.Matrix([-z, -v, ell])
gauge = S.Matrix([z, v, ell+a*z])
gauge_i = S.Matrix([z, v, ell-a*z])

def compose(x, y):
    return x.subs(dict(zip(state, y)), simultaneous=True).applyfunc(S.expand)

def same(name, x, y):
    assert (x-y).applyfunc(S.simplify) == S.zeros(*x.shape), name
    print(name, 'PASS', list(y))

same('hF=Fh', compose(h, f), compose(f, h))
same('J^2=id', compose(j, j), state)
same('JhJ=h^-1', compose(j, compose(h, j)), hi)
same('JFJ=F^-1', compose(j, compose(f, j)), fi)
for name, x, y in [('h', h, hi), ('F', f, fi), ('gauge', gauge, gauge_i)]:
    same(name+' inverse forward', compose(x, y), state)
    same(name+' inverse backward', compose(y, x), state)
for name, x0, x in [('h', h0, h), ('F', f0, f), ('J', j0, j)]:
    same('z^a gauge '+name, compose(gauge, compose(x0, gauge_i)), x)

n, r, x, y, u, vv = S.symbols('n r x y u vv', nonzero=True)
rho = (1-a*b*r*r)/n
C = S.Matrix([[n, -b*r], [a*r, rho]])
Ci = S.Matrix([[rho, b*r], [-a*r, n]])
K0 = S.diag(a, -b)
K = (C.T*K0).applyfunc(S.simplify)
assert C.det() == 1 and (C*Ci).applyfunc(S.simplify) == S.eye(2)
psi = -a*rho*x*x-2*a*b*r*x*y+b*n*y*y+a*x

def at(X, Y):
    return psi.subs({x:X,y:Y}, simultaneous=True)

assert S.simplify(at(x+n,y+a*r)-psi+2*a*x) == 0
assert S.simplify(at(x-b*r,y+rho)-psi-(2*b*y+b*rho-a*b*r)) == 0
Z = C*S.Matrix([u,vv])
pulled = S.expand(at(*Z))
canonical = (S.Matrix([u,vv]).T*K*S.Matrix([u,vv]))[0]
assert S.simplify(pulled+canonical-a*(n*u-b*r*vv)) == 0
old_wall = S.simplify(at(1,0)+at(-1,1)-at(0,0)-at(0,1))
actual_wall = S.simplify(pulled.subs({u:1,vv:0})+
                        pulled.subs({u:-1,vv:1})-
                        pulled.subs({u:0,vv:0})-
                        pulled.subs({u:0,vv:1}))
assert S.simplify(old_wall+2*a*(rho-b*r)) == 0
assert S.simplify(actual_wall+2*a*(n+b*r)) == 0
delta = Ci*S.Matrix([0,1])
assert delta == S.Matrix([b*r,n])
assert S.simplify(a*(n*delta[0]-b*r*delta[1])) == 0
print('Cusp physical support differences PASS')
print('Cusp pullback psi(Cv)=-v^tKv+a(n v1-br v2) PASS')
print('Physical-wall expression:', old_wall)
print('Prescribed-fan wall expression:', S.factor(actual_wall))
print('Prescribed-fan complex line degree:', S.factor(-actual_wall))
print('Scalar vector:', list(delta), '; linear gauge is scalar invariant PASS')

alpha, beta, u1, u2, jj = S.symbols('alpha beta u1 u2 jj', nonzero=True)
psi1 = -a*u1/alpha*jj*(jj-alpha)
assert S.expand(psi1.subs(jj,jj+alpha)-psi1+2*a*u1*jj) == 0
residual = S.factor(psi1.subs(jj,jj+beta)-psi1-
                    (2*b*u2*jj+b*beta*u2-b*alpha*u2))
assert S.simplify(residual.subs(u2,-a*beta*u1/(b*alpha))) == 0
print('Rank-one F difference residual:', residual)
print('It vanishes by a beta u1+b alpha u2=0 PASS')

rank_one_count = 0
nonprimitive_h = []
changed = []
print('COMPLETE RANK-ONE SUPPORT/PERIOD CHECK')
for row in data['patterns']:
    aa, bb, p = row['a'], row['b'], row['p']
    nu, kap = row['selected_nu'], row['selected_kappa']
    CC, KK = S.Matrix(row['C']), S.Matrix(row['cusp_K'])
    rr = -kap
    rrho = S.Rational(1-aa*bb*rr*rr,nu)
    pp = psi.subs({a:aa,b:bb,n:nu,r:rr})
    XX = CC*S.Matrix([u,vv])
    lhs = S.expand(pp.subs({x:XX[0],y:XX[1]},simultaneous=True))
    rhs = -(S.Matrix([u,vv]).T*KK*S.Matrix([u,vv]))[0]+aa*(nu*u-bb*rr*vv)
    assert S.simplify(lhs-rhs) == 0
    assert row['cusp_degree_xi'] == aa*(nu+bb*rr)
    for node in row['rank_one']:
        nn, kk = node['nu'], node['kappa']
        dd = gcd(nn,aa*kk)
        ss, tt = nn//dd, -aa*kk//dd
        be = S.Rational(bb*kk,ss)
        assert be.q == 1 and gcd(dd,int(be)) == 1
        be = int(be)
        assert S.Matrix([nn,-aa*kk]) == dd*S.Matrix([ss,tt])
        assert S.Matrix([bb*kk,-S.Rational(aa*bb*kk*kk,nn)]) == be*S.Matrix([ss,tt])
        N = S.Rational(aa*nn,dd*dd)
        assert N.q == 1 and node['K'][0][0] == N
        assert aa*be*ss+bb*dd*tt == 0
        q = -N*jj*(jj-dd)
        assert S.expand(q.subs(jj,jj+dd)-q+2*aa*ss*jj) == 0
        assert S.expand(q.subs(jj,jj+be)-q-
                        (2*bb*tt*jj+bb*be*tt-bb*dd*tt)) == 0
        assert N*dd == aa*ss
        rank_one_count += 1
        if dd > 1:
            nonprimitive_h.append((row['number'],node['site'],dd,be))
        print(row['number'], node['site'], node['kind'],
              'alpha,beta=',dd,be,'u=',[ss,tt], 'N=',N,'PASS')
    ww = row['elliptic']['w']
    qf = bb//p
    aaC = aa*nu % p
    aaE = -qf % p
    assert (aaC*pow(nu*nu,-1,p)+aaE*pow(ww*ww,-1,p)) % p == 0
    relw = ww*pow(nu,-1,p) % p
    subgroup = pow(nu,-1,p)
    assert subgroup*nu % p == 1
    normE = aaE*pow(aaC,-1,p) % p
    assert normE == -relw*relw % p
    P_C = (relw*relw-1)*pow(2,-1,p) % p
    assert P_C == row['refined_coefficient']*pow(aaC,-1,p) % p
    if row['claimed_zero'] != row['actual_zero']:
        changed.append(row['number'])
print('Rank-one occurrences:', rank_one_count)
print('COMPLETE NONPRIMITIVE H OCCURRENCES', nonprimitive_h)
print('COMPLETE CORRECTED WEIGHT/GENERATOR CHECK')
for row in data['patterns']:
    p, aa, bb, nu = row['p'],row['a'],row['b'],row['selected_nu']
    ww = row['elliptic']['w']
    relw = ww*pow(nu,-1,p) % p
    P_C = row['refined_coefficient']*pow(aa*nu,-1,p) % p
    print(row['number'],'p=',p,'nu=',nu,'Tate w=',ww,'normalized w=',relw,
          'subgroup map/inverse=',pow(nu,-1,p),nu % p,
          'P_s=',row['refined_coefficient'],'P_C=',P_C,'PASS')
assert changed == [21,22,25,26,27,28,29,30,33,34]
print('Ten changed assignments:', changed)
print('All post-exposure auxiliary identities PASS; no fresh/global file modified.')
