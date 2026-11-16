"""Exact cyclic scalar-return cover and elliptic pullback certificates.

This computes the auxiliary degree-twelve cover, not a spin filling
or the unresolved Theta_7 monodromy. Every enumeration is explicit:
deck exponents 0..11 and one-dimensional eigensections of K_C tensor L.
All Fourier arithmetic is in Q[x]/Phi_12(x), with no floating point.
"""
from math import gcd, ceil, floor
from sympy import Poly, symbols, Rational

x=symbols('x')
phi=Poly(x**4-x**2+1,x)
degree=12
exponents=[4,-3,-1]
ramification=[degree//gcd(degree,a) for a in exponents]
points=[gcd(degree,a) for a in exponents]
assert gcd(degree,*exponents)==1
assert ramification==[3,4,12] and points==[4,3,1]
two_g_minus_two=-2*degree+sum(degree-d for d in points)
assert two_g_minus_two==4
genus=(two_g_minus_two+2)//2
print('cover degree',degree,'exponents',exponents)
print('ramification indices',ramification,'points above',points,'genus',genus)

# At t=0,1,p_s,infinity the pullback of the chosen rational
# two-form has respective orders 0,2,11,-1. For h^j*t^a*(t-1)^b
# *(t-p_s)^c times this form, use the least allowed integers.
holomorphic=[]
for j in range(degree):
    a=-floor(Rational(j,3))
    b=ceil(Rational(j-2,4))
    c=ceil(Rational(j-11,12))
    excess=-a-b-c-1
    dimension=max(0,excess+1)
    if dimension:
        holomorphic.append((j,a,b,c,dimension))
    print('form character',j,'minimal exponents',(a,b,c),'dimension',dimension)
assert holomorphic==[(6,-2,1,0,1),(9,-3,2,0,1),(10,-3,2,0,1)]
assert sum(row[-1] for row in holomorphic)==3

chi_O=1
b1=2*genus
euler=12
b2=euler-2+2*b1
pg=chi_O+genus-1
bplus=1+2*pg
bminus=b2-bplus
signature=bplus-bminus
assert (b1,b2,bplus,bminus,signature)==(6,22,7,15,-8)
print('elliptic pullback: chiO, pg, b1, b2, b+, b-, sigma',
      chi_O,pg,b1,b2,bplus,bminus,signature)
height=degree*Rational(1,6)
P_dot_O=(height-2*chi_O)/2
L_square=-2*chi_O-2*P_dot_O
assert height==2 and P_dot_O==0 and L_square==-2
print('section height',height,'P.O',P_dot_O,'(P-O)^2',L_square)

traces=[b2]
for j in range(1,degree):
    fixed_curve=1+4*(j%4==0)+3*(j%3==0)
    trace_H1=2-fixed_curve
    # The ramification point p_s carries a whole fixed elliptic
    # fibre, of Euler number zero. At the order-three points
    # there are three fixed elliptic points; at order-four
    # points there are two (or four for the involution).
    fixed_surface=12*(j%4==0)
    if j%3==0:
        fixed_surface+=12 if j==6 else 6
    trace_H2=fixed_surface-2+2*trace_H1
    traces.append(trace_H2)
assert traces==[22,0,0,0,4,0,6,0,4,0,0,0]
print('H2 traces for eta^j, j=0..11',traces)
multiplicities=[]
for k in range(degree):
    expr=sum(Rational(traces[j],degree)*x**((-j*k)%degree)
             for j in range(degree))
    remainder=Poly(expr,x).rem(phi).as_expr()
    assert remainder.is_Integer and remainder>=0
    multiplicities.append(int(remainder))
assert multiplicities==[3,1,2,2,2,1,3,1,2,2,2,1]
positive=[0]*degree
positive[0]=1
for j,_,_,_,dimension in holomorphic:
    positive[j]+=dimension
    positive[(-j)%degree]+=dimension
negative=[m-p for m,p in zip(multiplicities,positive)]
signed=[p-n for p,n in zip(positive,negative)]
assert all(n>=0 for n in negative)
assert sum(positive)==bplus and sum(negative)==bminus
assert sum(signed)==signature and (multiplicities[0],signed[0])==(3,-1)
print('H2 eigendimensions',multiplicities)
print('positive eigendimensions',positive)
print('negative eigendimensions',negative)
print('signed eigendimensions',signed)
print('invariant H2 rank/signature',multiplicities[0],signed[0])
print('No bounding manifold, Pontryagin square, or Theta7 value is inferred.')
