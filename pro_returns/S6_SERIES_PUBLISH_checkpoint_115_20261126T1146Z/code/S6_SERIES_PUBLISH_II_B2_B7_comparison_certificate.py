#!/usr/bin/env python3
"""B7: exact second-jet arithmetic using only rational sparse polynomials.

The source uses the chain rule for the power Hessian. This independent check
uses the multiplicative law for truncated binomial jets, established as a
polynomial identity in two formal exponents. No finite exponent sampling is
used, and no computer algebra library is required.
"""
from fractions import Fraction as F
import json

names = 'B C c l1 l2 h11 h12 h22 u0 u1 u2 y z i'.split()
positions={v:i for i,v in enumerate(names)}
zero=(0,)*len(names)
iy,iz=positions['y'],positions['z']
ii=positions['i']


def const(v):
    return {zero:F(v)} if v else {}


def var(name,power=1):
    e=list(zero);e[positions[name]]=power
    return {tuple(e):F(1)}


def add(*polys):
    out={}
    for p in polys:
        for e,a in p.items():out[e]=out.get(e,F(0))+a
    return {e:a for e,a in out.items() if a}


def scale(p,a):
    return {e:v*F(a) for e,v in p.items() if v*F(a)}


def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            k=list(x+y for x,y in zip(e,f))
            if k[iy]+k[iz]>2:continue
            sign=(-1)**(k[ii]//2);k[ii]%=2;k=tuple(k)
            out[k]=out.get(k,F(0))+sign*a*b
    return {e:a for e,a in out.items() if a}


def derivative(p,name):
    i=positions[name];out={}
    for e,a in p.items():
        if e[i]:
            k=list(e);k[i]-=1
            out[tuple(k)]=a*e[i]
    return out


def origin(p):
    return {e:a for e,a in p.items() if e[iy]==e[iz]==0}


def hessian(p):
    return [[origin(derivative(derivative(p,i),j))
             for j in ('y','z')] for i in ('y','z')]


checks=[]


def equal(name,p,q):
    residue=add(p,scale(q,-1))
    if residue:raise AssertionError((name,residue))
    checks.append(name)


one=const(1)
B,C=var('B'),var('C')
cinv=var('c',-1)
y,z=var('y'),var('z')
linear=add(mul(var('l1'),y),mul(var('l2'),z))
quadratic=add(scale(mul(var('h11'),mul(y,y)),F(1,2)),
              mul(var('h12'),mul(y,z)),
              scale(mul(var('h22'),mul(z,z)),F(1,2)))
A=mul(cinv,add(linear,quadratic))


def power_jet(exponent,increment):
    second=scale(mul(exponent,add(exponent,const(-1))),F(1,2))
    return add(one,mul(exponent,increment),mul(second,mul(increment,increment)))


equal('binomial jet exponent addition',
      mul(power_jet(B,A),power_jet(C,A)),power_jet(add(B,C),A))
equal('binomial jet exponent zero',power_jet({},A),one)
equal('binomial jet exponent one',power_jet(one,A),add(one,A))
HH=[[var('h11'),var('h12')],[var('h12'),var('h22')]]
ell=[var('l1'),var('l2')]
JH=hessian(power_jet(B,A))
for i in range(2):
    for j in range(2):
        expected=add(mul(mul(B,cinv),HH[i][j]),
          mul(mul(mul(B,add(B,const(-1))),mul(cinv,cinv)),mul(ell[i],ell[j])))
        equal(f'power Hessian full jet {i}{j}',JH[i][j],expected)
crit_hessian=hessian(power_jet(B,mul(cinv,quadratic)))
for i in range(2):
    for j in range(2):
        equal(f'power Hessian critical jet {i}{j}',
              crit_hessian[i][j],mul(mul(B,cinv),HH[i][j]))
det_new=add(mul(crit_hessian[0][0],crit_hessian[1][1]),
            scale(mul(crit_hessian[0][1],crit_hessian[1][0]),-1))
det_old=add(mul(HH[0][0],HH[1][1]),scale(mul(HH[0][1],HH[1][0]),-1))
equal('nondegenerate power Hessian determinant',det_new,
      mul(mul(mul(B,B),mul(cinv,cinv)),det_old))
unit=add(var('u0'),mul(var('u1'),y),mul(var('u2'),z))
unit_hessian=hessian(mul(unit,quadratic))
for i in range(2):
    for j in range(2):
        equal(f'unit multiple Hessian at critical point {i}{j}',
              unit_hessian[i][j],mul(var('u0'),HH[i][j]))

# Both linear maps used in the source comparison, including the sign of the
# quadratic form. Gaussian rationals are represented by i^2=-1 in mul().
imag=var('i')
for sign in (1,-1):
    UU=add(y,mul(imag,z))
    VV=add(scale(y,sign),scale(mul(imag,z),-sign))
    equal(f'quadratic linear map product sign {sign}',mul(UU,VV),
          scale(add(mul(y,y),mul(z,z)),sign))
    equal(f'quadratic inverse y sign {sign}',scale(add(UU,scale(VV,sign)),F(1,2)),y)
    equal(f'quadratic inverse z sign {sign}',
          scale(mul(imag,add(UU,scale(VV,-sign))),F(-1,2)),z)
    jac=add(mul(derivative(UU,'y'),derivative(VV,'z')),
            scale(mul(derivative(UU,'z'),derivative(VV,'y')),-1))
    equal(f'quadratic coordinate Jacobian sign {sign}',jac,scale(imag,-2*sign))

# Exact radii in the original proof, normalized by rho^a.
for name,a,b in [
 ('boundary lower bound exceeds critical bound',F(1,4),F(3,4)),
 ('boundary upper bound below chosen eta0',F(5,4),F(2)),
 ('target transport disk inside unit x radius',F(1,4),F(1))]:
    assert a<b,name
    checks.append(name)

print(json.dumps({'tag':'01B7','phase':'complete original proof comparison',
 'method':'standard-library rational sparse second jets and exponent-addition identities',
 'checks':len(checks),'passed':checks,
 'universal_scope':'The exponent-addition identity plus exponent zero/one proves the truncated formula for every nonnegative integer exponent by induction. Multiply the normalized Hessian by c^b to obtain b*c^(b-1)*H at a critical point.',
 'analytic_scope':'Analytic regularity, properness, path transport and the coordinate inverses are proved in the mathematical records, not inferred from this computation.'},indent=2))
