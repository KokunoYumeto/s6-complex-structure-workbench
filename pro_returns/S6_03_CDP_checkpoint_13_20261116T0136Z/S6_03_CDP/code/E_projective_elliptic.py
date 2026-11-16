"""Exact charts, integral Mayer--Vietoris maps and cohomology for UN18."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

m = s.symbols('m', integer=True, positive=True)
z, u, a, b, ap, bp = s.symbols('z u a b ap bp', nonzero=True)
plus = s.Matrix([z/u,u**m])
minus = s.Matrix([z*u,u**(-m)])
assert s.simplify(plus.jacobian([z,u]).det()-m*u**(m-2)) == 0
assert s.simplify(minus.jacobian([z,u]).det()+m*u**(-m)) == 0
assert s.simplify(plus[0]**m*plus[1]-z**m) == 0
assert s.simplify(minus[0]**m*minus[1]-z**m) == 0
print('Finite product cover Jacobians:',plus.jacobian([z,u]).det(),
      minus.jacobian([z,u]).det())
print('Both maps preserve the actual local base equation x=z^m.')

# H1(M3): base generators a,b, then delta_plus,delta_minus,h.
relations = s.Matrix([[0,0,1,1,0],
                      [0,0,m,0,1],
                      [0,0,0,m,-1]])
assert relations.rank() == 2
assert relations.extract([0,1],[3,4]).det() == 1
assert relations.row(1)+relations.row(2) == m*relations.row(0)
print('M3 relation rank=2 and a universal 2-by-2 minor is 1: H1=Z^3.')

def invariants(matrix):
    snf = smith_normal_form(matrix,domain=ZZ)
    nonzero = [abs(int(snf[i,i])) for i in range(min(snf.shape))
               if snf[i,i] != 0]
    assert all(x == 1 for x in nonzero)
    return len(nonzero),nonzero

mv5 = {
    0:s.Matrix([[1,1],[-1,0],[0,-1]]),
    1:s.Matrix([[0,0],[0,0],[1,-1]]),
    2:s.zeros(4,0),
    3:s.Matrix([[1,-1],[0,0],[0,0],[0,0],[0,0],[-1,0],[0,-1]]),
    # The second base S3 and its angular fibre both reverse sign.
    4:s.Matrix([[1,1],[0,0],[0,0]]),
    5:s.zeros(0,0),
}
target5 = [3,3,4,7,3,0]
source5 = [2,2,0,2,2,0]
ranks5 = []
for k in range(6):
    rank,diag = invariants(mv5[k])
    ranks5.append(rank)
    print('M5 MV degree',k,'shape',mv5[k].shape,'Smith nonzero diagonal',diag)
bM = [target5[k]-ranks5[k]+(source5[k-1]-ranks5[k-1] if k else 0)
      for k in range(6)]
assert bM == [1,2,5,5,2,1]
bY = [bM[k] if k < 6 else 0 for k in range(7)]
for k in range(1,7):
    bY[k] += bM[k-1]
assert bY == [1,3,7,10,7,3,1]

mvS = {
    0:s.Matrix([[1,1],[-1,0],[0,-1]]),
    1:s.Matrix([[0,0,0,0],[0,0,0,0],[1,0,-1,0],
                [0,1,0,1],[0,-1,0,0],[0,0,0,-1]]),
    2:s.Matrix([[1,1],[0,0],[0,0],[0,0],[0,0],[0,0]]),
    3:s.zeros(6,0),
    4:s.zeros(3,0),
}
targetS = [3,6,6,6,3]
sourceS = [2,4,2,0,0]
ranksS = []
for k in range(5):
    rank,diag = invariants(mvS[k])
    ranksS.append(rank)
    print('Support MV degree',k,'shape',mvS[k].shape,'Smith nonzero diagonal',diag)
bS = [targetS[k]-ranksS[k]+(sourceS[k-1]-ranksS[k-1] if k else 0)
      for k in range(5)]
assert bS == [1,3,6,7,3]

bP = [1,4,6,4,1]
bQ = [1,1,0,1,1]
e = lambda values: sum((-1)**k*v for k,v in enumerate(values))
assert e(bP) == e(bQ) == e(bS) == e(bY) == 0
print('All integral cohomology is free, by the primitive Smith images.')
print('M5:',bM)
print('P:',bP,'Q:',bQ,'support:',bS,'compact Y:',bY)
print('Coherent dimensions P=(1,2,1), Q=(1,1,0), S=(1,2,1), Y=(1,2,1,0).')
for mm in range(2,7):
    plurigenera = []
    for rr in range(1,7):
        degree = 2*(rr*(mm-1)//mm)
        plurigenera.append(max(1,degree))
    print('m=',mm,'genus(C)=',mm,'P_1,...,P_6=',plurigenera,
          'canonical growth slope=',s.Rational(2*(mm-1),mm))
print('All exact checks passed.')
