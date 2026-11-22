"""New post-reset certificate, written after target proof exposure.

This is a newly executed replacement for a lost postrelease supplement; it is
not represented as the lost program or as a prerelease independent program.
The durable prerelease discriminant proof is a separate input.
"""
from fractions import Fraction
import json

N = 4
def const(c):
    return {} if c == 0 else {(0,)*N: Fraction(c)}
def var(i):
    e = [0]*N; e[i] = 1
    return {tuple(e): Fraction(1)}
def add(*terms):
    out = {}
    for p in terms:
        for e,c in p.items(): out[e] = out.get(e,Fraction(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c): return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out = {}
    for e,c in p.items():
        for f,d in q.items():
            k=tuple(a+b for a,b in zip(e,f))
            out[k]=out.get(k,Fraction(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def coefficient(p,i,n):
    out={}
    for e,c in p.items():
        if e[i]==n:
            f=list(e);f[i]=0;out[tuple(f)]=c
    return out
def serial(p): return {','.join(map(str,e)):str(c) for e,c in sorted(p.items())}

r,da,db,eps=map(var,range(4))
a=scale(power(r,2),-3); b=scale(power(r,3),2)
variation=add(scale(power(add(a,mul(eps,da)),3),4),
              scale(power(add(b,mul(eps,db)),2),27))
dD=coefficient(variation,3,1)
expected=scale(mul(power(r,3),add(mul(r,da),db)),108)
assert dD==expected
Ft=scale(add(mul(r,da),db),-1)
assert not add(dD,scale(mul(power(r,3),Ft),108))
assert not coefficient(variation,3,0)

# A polynomial of degree at most six is zero when it vanishes at these seven
# distinct rational points. This is exact interpolation, not a singularity
# ideal/Groebner computation. The degree bound follows from P=(0,t^3,1).
finite_values=[]
for t in range(7):
    x,y,z=0,t**3,1
    value=y*y*z-x**3-(t**4+1)*x*z*z-t**6*z**3
    finite_values.append([t,value]);assert value==0

# Laurent monomial exponent transport for s=1/t, x=t^2 X, y=t^3 Y.
# Multiplication by s^6 gives the entire infinity-chart cubic, coefficientwise.
finite_cubic={(0,0,2,1):1,(0,3,0,0):-1,(4,1,0,2):-1,
              (0,1,0,2):-1,(6,0,0,3):-1}
infinity={}
for (t,x,y,z),c in finite_cubic.items():
    e=(6-t-2*x-3*y,x,y,z)
    assert e[0]>=0
    infinity[e]=infinity.get(e,0)+c
expected_infinity={(0,0,2,1):1,(0,3,0,0):-1,(0,1,0,2):-1,
                   (4,1,0,2):-1,(0,0,0,3):-1}
assert infinity==expected_infinity
infinity_section_residual=sum(c for (s,x,y,z),c in infinity.items() if x==0)
assert infinity_section_residual==0
# The section coordinates transport to (X,Y,z)=(0,1,1); the two homogeneous
# section divisors are disjoint since O has z=0 and P has z=1 on both charts.
zero_section_Fz=sum(c for (t,x,y,z),c in finite_cubic.items()
                    if t==0 and x==0 and z==1)
assert zero_section_Fz==1

print(json.dumps({
    'timing':'new post-reset, post-target-release replacement certificate',
    'new_independent_event_count':0,
    'node_first_variation_coefficients':serial(dD),
    'node_identity':'Dprime=108*r^3*(r*aprime+bprime)=-108*r^3*Ft',
    'node_nondegeneracy_scope':'r is nonzero; durable squarefreeness proof gives Dprime nonzero',
    'finite_P_interpolation_degree_bound':6,
    'finite_P_interpolation_values':finite_values,
    'infinity_cubic_coefficients':{','.join(map(str,e)):c for e,c in sorted(infinity.items())},
    'infinity_P_coordinates':[0,1,1],
    'infinity_P_residual':infinity_section_residual,
    'zero_section_Fz':zero_section_Fz,
    'all_assertions_passed':True
},indent=2,sort_keys=True))
