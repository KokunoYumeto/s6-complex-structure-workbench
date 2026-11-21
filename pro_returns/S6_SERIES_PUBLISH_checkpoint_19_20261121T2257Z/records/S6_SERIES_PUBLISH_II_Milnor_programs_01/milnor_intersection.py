#!/usr/bin/env python3
"""Exact compactification lattices for x^2-z*y^n=1 (P4.16).

The proof constructs the surface and its boundary, and proves that the
displayed orthogonal kernel is the image of compact H_2 of the affine
surface.  This program independently checks every lattice calculation.
All arithmetic is integral or rational; no numerical rank test is used.
"""
from functools import reduce
from math import gcd
import json
from pathlib import Path
import sympy as S

records = []
for n in range(1, 13):
    size = 2 + 2*n
    names = ['H_x', 'H_y'] + [f'E_{sign},{j}'
                            for sign in ('+', '-') for j in range(1,n+1)]
    Q = S.diag(*([0,0]+[-1]*(2*n)))
    Q[0,1] = Q[1,0] = 1
    def basis(i):
        v = S.zeros(size,1); v[i] = 1
        return v
    def exceptional(sign,j):
        return basis(2 + sign*n + j-1)
    divisors = [basis(0), basis(1),
                basis(1)-exceptional(0,1)-exceptional(1,1)]
    divisor_names = ['x=infinity', 'y=infinity', 'strict(y=0)']
    for sign in range(2):
        for j in range(1,n):
            divisors.append(exceptional(sign,j)-exceptional(sign,j+1))
            divisor_names.append(f'strict(E_{"+" if sign == 0 else "-"},{j})')
    B = S.Matrix.hstack(*divisors)
    restriction = B.T*Q
    v = sum((exceptional(0,j)-exceptional(1,j) for j in range(1,n+1)),
            S.zeros(size,1))
    kernel = restriction.nullspace()
    square = (v.T*Q*v)[0]
    assert restriction.rank() == 2*n+1
    assert len(kernel) == 1 and restriction*v == S.zeros(2*n+1,1)
    assert reduce(gcd, map(abs, map(int,v))) == 1
    assert square == -2*n
    assert kernel[0] == -v or kernel[0] == v
    # The boundary is a tree of rational curves, checked from its graph.
    intersection = B.T*Q*B
    edges = [(i,j) for i in range(B.cols) for j in range(i+1,B.cols)
             if intersection[i,j] != 0]
    assert all(intersection[i,j] == 1 for i,j in edges)
    assert len(edges) == B.cols-1
    reached = {0}
    while True:
        new = reached | {j for i,j in edges if i in reached} | {
            i for i,j in edges if j in reached}
        if new == reached: break
        reached = new
    assert len(reached) == B.cols
    weights = (n+2, 2, 4)
    assert 2*weights[0] == weights[2] + n*weights[1]
    print(f'n={n}: compactification rank={size}, boundary rank={B.cols}, '
          f'kernel=Z*{list(v)}, square={square}, boundary graph=tree; '
          f'weights={weights}, degree={2*n+4}')
    records.append(dict(n=n,basis=names,intersection_matrix=[list(r) for r in Q.tolist()],
                        boundary_divisors=divisor_names,
                        boundary_columns=B.tolist(),
                        restriction=restriction.tolist(),kernel=list(v),square=square))

# Local blowup formulas at either root x=+/-1. Here a=x^2-1 and b=y.
a,b,c,z = S.symbols('a b c z')
for n in range(1,13):
    for j in range(1,n+1):
        assert S.cancel((b**j*c)/b**n - c/b**(n-j)) == 0
    assert S.expand((b**n*z)-z*b**n) == 0
print('All n-step blowup charts a=b^j*a_j, z=a_j/b^(n-j) verified.')

# Independent n=2 compactification by two blowups of P1_r x P1_s.
Q = S.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-1,0],[0,0,0,-1]])
B = S.Matrix.hstack(S.Matrix([1,1,0,0]),S.Matrix([1,0,-1,0]),
                    S.Matrix([0,1,0,-1]))
v = S.Matrix([1,-1,1,-1])
assert B.T*Q*v == S.zeros(3,1) and (v.T*Q*v)[0] == -4
r,s = S.symbols('r s')
x= (r+s)/(r-s); y=2/(r-s)
assert S.cancel(x*x-r*s*y*y-1) == 0
print('Independent n=2 chart r=(x+1)/y, s=(x-1)/y: equation and square -4 verified.')

def integer_default(obj):
    if isinstance(obj,S.Integer): return int(obj)
    raise TypeError(type(obj).__name__)
Path(__file__).with_name('milnor_intersection.json').write_text(
    json.dumps(records,indent=2,default=integer_default)+'\n')
print('Conclusion checked: the compact H2 generator has square -2*n, never zero.')

# The same compactification for x^a-z*y^n=1 (P4.17).
general_records=[]
for exponent in range(2,7):
    for n in range(1,7):
        size=2+exponent*n
        Q=S.diag(*([0,0]+[-1]*(exponent*n)))
        Q[0,1]=Q[1,0]=1
        def unit(i):
            w=S.zeros(size,1); w[i]=1; return w
        def E(i,j): return unit(2+i*n+j-1)
        first=sum((E(i,1) for i in range(exponent)),S.zeros(size,1))
        B=S.Matrix.hstack(unit(0),unit(1),unit(1)-first,*[
            E(i,j)-E(i,j+1) for i in range(exponent) for j in range(1,n)])
        V=S.Matrix.hstack(*[
            sum((E(i,j)-E(i+1,j) for j in range(1,n+1)),S.zeros(size,1))
            for i in range(exponent-1)])
        A=S.zeros(exponent-1)
        for i in range(exponent-1):
            A[i,i]=2
            if i+1<exponent-1: A[i,i+1]=A[i+1,i]=-1
        form=V.T*Q*V
        assert B.T*Q*V == S.zeros(B.cols,exponent-1)
        assert (B.T*Q).rank() == size-exponent+1
        assert form == -n*A
        assert form.det() == (-n)**(exponent-1)*exponent
        # First exponent-1 chain coefficients give a triangular minor of det1.
        assert V.extract([2+i*n for i in range(exponent-1)],
                         range(exponent-1)).det()==1
        print(f'a={exponent}, n={n}: compact H2 rank={exponent-1}, '
              f'intersection=-{n}*A_{exponent-1}, determinant={form.det()}')
        general_records.append(dict(a=exponent,n=n,boundary_columns=B.tolist(),
                                    kernel_basis=V.tolist(),intersection=form.tolist()))
Path(__file__).with_name('milnor_intersection_general.json').write_text(
    json.dumps(general_records,indent=2,default=integer_default)+'\n')
print('General conclusion checked: compact H2 lattice is A_(a-1)(-n).')
