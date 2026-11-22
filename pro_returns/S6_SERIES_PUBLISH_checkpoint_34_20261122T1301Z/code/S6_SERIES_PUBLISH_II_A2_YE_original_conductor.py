#!/usr/bin/env python3
"""Postrelease exact checks of the retained R20 conductor-vector route."""
import json
from itertools import product
import sympy as sp


def main():
    b,t=sp.symbols('b t',integer=True)
    def inter(v,w):return sp.expand(2*v[0]*w[0]+v[0]*w[1]+v[1]*w[0])
    GH=(2,t-b);GR=(1,-t);K=(-2,0)
    paH=sp.expand(1+inter(GH,(GH[0]+K[0],GH[1]+K[1]))/2)
    cross=inter(GH,GR)
    assert paH==1+t-b and cross==4-t-b
    assert sp.expand(paH+cross)==5-2*b
    allowed=[]
    for bc in range(9):
        for e in range(bc+1):
            for rb in range(3,10):
                if e<rb-1:continue
                for g in range(1,6):
                    for delta in range(6):
                        n=5-2*bc-g-delta
                        if n>=0:allowed.append((bc,e,rb,g,delta,n))
    assert allowed==[(2,2,3,1,0,0)]
    degree_rows=[]
    for c in range(2,6):
        for ds in product(range(1,4),repeat=c):
            if sum(ds)==3 and ds[0]==ds[-1]==1:degree_rows.append(ds)
    assert degree_rows==[(1,1,1)]
    exponent_rows=[(x,y) for x in range(1,3) for y in range(1,3) if x+y==2]
    assert exponent_rows==[(1,1)]
    u,v,w,z,g=sp.symbols('u v w z g')
    residual=sp.expand((v**2+u**2*g).subs(v,u*w))
    assert residual==u**2*w**2+u**2*g
    # A smooth ramified spectral chart has z=-w^2-lambda*u.
    lam=sp.symbols('lambda')
    assert sp.expand((w**2+z+lam*u).subs(z,-w**2-lam*u))==0
    assert sp.Poly((-w**2-lam*u).subs(u,0),w).degree()==2
    pplus,pminus=sp.symbols('p_plus p_minus',positive=True,integer=True)
    plus=(4,2+pplus,2+pplus);minus=(1+pminus,1+pminus,2)
    third_difference=sp.expand(plus[2]-minus[2])
    assert third_difference==pplus
    for pp in range(1,33):assert plus[2].subs(pplus,pp)>=3
    # The individual degrees follow from ord(u|W1)=d1*ord(u|B+)=1.
    unit_order_solutions=[(d,k) for d in range(1,33) for k in range(1,33) if d*k==1]
    assert unit_order_solutions==[(1,1)]
    print(json.dumps({
        'check':'02YE retained spectral equality, exponent budget and conductor mismatch',
        'spectral_genus_H':str(paH),'spectral_intersection':str(cross),
        'spectral_sum':str(sp.expand(paH+cross)),
        'budget_variables':['b','e','r_B','g','delta_H','n'],
        'budget_solutions':allowed,
        'positive_degree_vectors_with_endpoints_one_and_sum_three':degree_rows,
        'internal_factor_exponents':exponent_rows,
        'normalization_residual':str(residual),
        'smooth_ramified_chart':'z=-w^2-lambda*u; v=u*w',
        'degree_valuation_solutions':unit_order_solutions,
        'marked_components':['W1','W2','W3'],
        'plus_vector':[str(x) for x in plus],
        'minus_vector':[str(x) for x in minus],
        'W3_difference':str(third_difference),
        'scope':'Exact symbolic intersection/vector/substitution identities and finite supplementary positive-integer checks. The arbitrary inequalities, actual conductor residue formula, smoothness and cover maps are verified in the comparison, not inferred from the enumerations.',
        'status':'PASS'},indent=2))


if __name__=='__main__':main()
