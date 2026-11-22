"""Postrelease comparison of the printed 02WS product-Hessian construction.

The target had already frozen and its full proof was read.  This file gives
no additional prereading credit.  Derivatives are reconstructed by exact
Lagrange interpolation of product values, independently of the printed
logarithmic-Hessian formula and of the prerelease two-jet implementation.
No associated historical target program was supplied or executed.
"""

from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path


def multiply_linear(poly, constant):
    out = [F(0)] * (len(poly) + 1)
    for k, c in enumerate(poly):
        out[k] += constant*c
        out[k+1] += c
    return out


def derivative_weights(degree):
    first, second = [], []
    for j in range(degree+1):
        poly, den = [F(1)], F(1)
        for k in range(degree+1):
            if k != j:
                poly = multiply_linear(poly, -k)
                den *= j-k
        first.append(poly[1]/den)
        second.append(2*poly[2]/den)
    return first, second


def determinant(m):
    result = F(0)
    for p in permutations(range(3)):
        sign = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        term = F(sign)
        for i in range(3):
            term *= m[i][p[i]]
        result += term
    return result


vectors = [(1,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,1),(2,-1,3)]
rows=[]
for r in range(2,7):
    v=[list(map(F,t)) for t in vectors[:r]]
    # Relation c=(1,-1,0,...,0).  The complementary indices illustrate the
    # printed epsilon/eta gradient correction as well as full-support r=2.
    eps, eta = F(1,10000), F(1,100)
    a=[eps,-eps]+[eta]*(r-2)
    correction=[-a[0]*sum(v[j][k]/a[j] for j in range(2,r)) for k in range(3)]
    w=[v[0][k]+correction[k] for k in range(3)]
    v[0]=w
    assert all(sum(v[i][k]/a[i] for i in range(r))==0 for k in range(3))
    assert all(any(c for c in t) for t in v)
    degree=2*r
    d1,d2=derivative_weights(degree)
    for choice in range(1,5):
        lam=F(1,100000*choice)
        def product_value(point):
            result=F(1)
            for i in range(r):
                term=a[i]+sum(v[i][k]*point[k] for k in range(3))
                if i==0:
                    term+=lam*sum(x*x for x in point)/2
                result*=term
            return result
        value=product_value([F(0)]*3)
        gradient=[];hessian=[[F(0)]*3 for _ in range(3)]
        for k in range(3):
            samples=[]
            for n in range(degree+1):
                point=[F(0)]*3;point[k]=F(n);samples.append(product_value(point))
            gradient.append(sum(c*y for c,y in zip(d1,samples)))
            hessian[k][k]=sum(c*y for c,y in zip(d2,samples))
        for i in range(3):
            for j in range(i+1,3):
                mixed=F(0)
                for n in range(degree+1):
                    for m in range(degree+1):
                        point=[F(0)]*3;point[i]=F(n);point[j]=F(m)
                        mixed+=d1[n]*d1[m]*product_value(point)
                hessian[i][j]=hessian[j][i]=mixed
        assert gradient==[0,0,0]
        predicted=[[((lam/a[0]) if j==k else 0)-sum(v[i][j]*v[i][k]/a[i]**2 for i in range(r))
                    for k in range(3)] for j in range(3)]
        assert all(hessian[j][k]/value==predicted[j][k] for j in range(3) for k in range(3))
        det=determinant(hessian)
        if det:
            rows.append(dict(branch_count=r,epsilon=str(eps),eta=str(eta),
              quadratic_coefficient=str(lam),gradient_correction=list(map(str,correction)),
              critical_value=str(value),hessian_determinant=str(det),
              method='Lagrange differentiation of exact product values',degree_bound=degree))
            break
    else:
        raise AssertionError('A degree-three determinant cannot vanish at all four choices: leading coefficient is nonzero.')
    print(f'{r} branches: exact interpolation recovers zero gradient and all nine printed Hessian entries; nonzero critical value and Hessian determinant.')

print('The all-branch formula and arbitrary-smallness argument are proved in the comparison record; these exact cases verify the independently implemented calculation.')
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
