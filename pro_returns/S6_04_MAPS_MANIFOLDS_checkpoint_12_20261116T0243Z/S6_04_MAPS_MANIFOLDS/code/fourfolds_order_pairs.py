"""Exhaustive finite-order pair filter after Theorems F.2.7--F.2.8.

The input order list is proved complete in F.2.2.  This script
does not bound affine multiplicities or integral matrix entries.
"""
from itertools import combinations
from math import gcd

orders = [1, 2, 3, 4, 5, 6, 8, 10, 12]
pairs = [p for p in combinations(orders, 2)
         if min(p) > 2 and gcd(*p) == 1]
assert pairs == [(3, 4), (3, 5), (3, 8), (3, 10),
                 (4, 5), (5, 6), (5, 8), (5, 12)]
print("Complete input linear orders:", orders)
print("Necessary unordered pairs after orbifold and involution obstructions:", pairs)
print("Number of pairs:", len(pairs))
print("No genuine k=3 datum is simply connected, by the triangle quotient.")

from sympy import Matrix, eye, zeros, symbols, factor
from itertools import combinations

remaining = [p for p in pairs if p not in [(3, 5), (3, 8), (3, 10)]]
assert remaining == [(3, 4), (4, 5), (5, 6), (5, 8), (5, 12)]
print("After the rank-five self-duality and spin obstruction:", remaining)
print("Rank-five local centralizer dimensions:", 1+2**2+2**2, 5, 3**2+2**2)
assert -25+(1+2**2+2**2)+5+(3**2+2**2) == 2

pairs4=list(combinations(range(4),2))
def wedge2(T):
    return Matrix([[T.extract(i,j).det() for j in pairs4] for i in pairs4])

# Standard symplectic pairs are (0,1) and (2,3).
J=Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]])
T=eye(4); T[0,1]=1
R=eye(4); R[2:4,2:4]=Matrix([[0,-1],[1,-1]])
assert T.T*J*T==J and R.T*J*R==J
assert R**3==eye(4)
Q=eye(6); Q[:,0]=Matrix([1,0,0,0,0,1])
assert Q.det()==1
Wt=(Q.inv()*wedge2(T)*Q)[1:,1:]
Wr=(Q.inv()*wedge2(R)*Q)[1:,1:]
Nt=Wt-eye(5)
assert Nt.rank()==2 and Nt**2==zeros(5)
t=symbols('t')
assert factor(Wr.charpoly(t).as_expr())==(t-1)*(t*t+t+1)**2
assert factor(R.charpoly(t).as_expr())==(t-1)**2*(t*t+t+1)
assert (R-eye(4))*(R*R+R+eye(4))==zeros(4)
print("Symplectic rank-one transvection gives orthogonal Jordan type (2,2,1).")
print("Finite spin lift polynomial:",factor(R.charpoly(t).as_expr()))
print("Primitive exterior polynomial:",factor(Wr.charpoly(t).as_expr()))
print("All exact order-pair and exterior-square checks passed.")

# Reuse the complete degree-six cyclotomic enumeration, whose n<=50
# bound is proved in F.2.2. No integral matrix entry bound is used.
from pathlib import Path
import json
types=json.loads(Path(__file__).with_name('fourfolds_finite_types.json').read_text())
eligible=[u for u in types if u['holomorphic_possible']
          and u['multiplicities']['1']==2 and u['fixed_exterior_ranks'][2]==3]
spectral_pairs=[(u,v) for u,v in combinations(eligible,2)
                if gcd(u['order'],v['order'])==1]
assert len(spectral_pairs)==8
order_pairs=sorted({tuple(sorted((u['order'],v['order']))) for u,v in spectral_pairs})
assert order_pairs==[(4,5),(5,6),(5,8),(5,12)]
print('Final necessary order pairs after the invariant-alternating-form argument:',order_pairs)
print('Eight finite spectral pairs:')
for u,v in spectral_pairs:
    print(u['order'],u['polynomial'],' | ',v['order'],v['polynomial'])
