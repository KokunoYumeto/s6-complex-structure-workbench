#!/usr/bin/env python3
"""Post-release comparison of KD's printed matrices with the fixed derivation.

The old programs have not been read at creation of this file.  The matrices
called source below are the complete proof released at 16:37:31 UTC.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import sympy as S

d = S.symbols('d', integer=True, positive=True)
n1,n2 = S.symbols('n1 n2', integer=True)
I4 = S.eye(4)
A1 = S.Matrix([[1,0,0,0],[6*d,0,1,0],[-6*d,-1,-1,0],[-2*d,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6*d,1,0,0],[3*d,0,1,1]])
F = S.Matrix([[2,1,3,0,0,0],[0,0,6*d,1,0,0],
              [-2,-2,-4,0,0,0],[-1,-1,-2-6*d,-1,0,0]])
Src = S.Matrix([[2,1,3,0,0,0],[-4*d,-2*d,0,1,0,0],
                [-2,-2,-4,0,0,0],[3*d,3*d,0,-1,0,0]])
U1 = S.Matrix([[1,-2*d],[0,1]])
U2 = S.Matrix([[1,-(3*d+1)/2],[0,1]])
P = S.diag(U1.T,U2.T)
lam = S.Matrix([[0,2,-1,2]])
phi = S.Matrix([[4*d,2,3*d,2]])

def zero(M):
    assert all(S.simplify(v)==0 for v in M)

def show(label,M):
    print(label)
    print(M)

print('Post-release exact comparison; fixed fresh derivation is unchanged.')
zero(Src-P*F)
zero(phi-lam*P.inv())
assert P.det()==1
show('Source cohomology basis changes U1,U2 =',(U1,U2))
show('Homology coordinate morphism P =',P)
show('Its integral inverse for odd d =',P.inv())
show('Source minus P times fresh =',Src-P*F)
show('Source Phi minus fresh lambda times P inverse =',phi-lam*P.inv())

H = S.Matrix([[0,1],[1,0]])
G1 = S.Matrix([[0,1],[1,4*d]])
G2 = S.Matrix([[0,1],[1,1+3*d]])
zero(U1.T*G1*U1-H)
zero(U2.T*G2*U2-H)
J = S.diag(-1,1)
zero(J.T*(-H)*J-H)
show('Complex-oriented source Gram matrices =',(-H,-H))
show('Explicit isometry from negative hyperbolic plane to hyperbolic plane =',J)

for rows,cols,wanted in [((0,1,2),(0,1,3),2),
                         ((0,1,3),(1,2,3),3*d),
                         ((1,2,3),(1,2,3),4*d)]:
    got=S.expand(Src.extract(rows,cols).det())
    assert got==wanted
    print('Source minor: rows',tuple(r+1 for r in rows),
          'columns',tuple(c+1 for c in cols),'determinant',got)
assert Src.rank()==3

for j,(A,m) in enumerate([(A1,3),(A2,4)],1):
    norm=sum((A**i for i in range(m)),S.zeros(4))
    avg=norm/m
    R=sum((i*A**i for i in range(m)),S.zeros(4))/m
    zero((A-I4)*R-(I4-avg))
    show(f'Conjugating translation operator R{j}, with (A-I)R=I-average =',R)

pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def wedge(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs] for i,j in pairs])
A0=(A1*A2).inv()
W=wedge(A0)-S.eye(6)
R=S.Matrix([[0,0],[0,1],[0,0],[0,0],[0,d],[1,0]])
K=S.Matrix([[d,d,0,0,1,0],[1,0,0,0,0,0]])
B=S.Matrix([[0,1],[0,0],[0,0],[0,0],[1,-d],[0,0]])
zero(W-R*K)
zero(R-W*B)
projection=S.Matrix([[1,0,0,0,0,0],[0,0,1,0,0,0],
                     [0,0,0,1,0,0],[0,-d,0,0,1,0]])
inverse=S.Matrix([[1,0,0,0],[0,0,0,0],[0,1,0,0],
                  [0,0,1,0],[0,0,0,1],[0,0,0,0]])
residual=S.Matrix([[0,0,0,0,0,1],[0,1,0,0,0,0]])
zero(projection*inverse-S.eye(4))
zero(S.eye(6)-inverse*projection-R*residual)
show('Clockwise cusp exterior-square difference =',W)
show('Exact image generators (w-delta, g-w+d u-delta) =',R)
show('Their actual preimages under exterior-square difference =',B)
show('Integral cokernel map for the Wang sequence =',projection)
show('Its section =',inverse)

for e in [1,-1]:
    sa1=-e-3*n1
    sa2=e-4*n2
    sa0=-n1-n2
    assert S.expand(12*sa0-4*sa1-3*sa2)==e
    print('sign(p)=',e,'source transformed coefficients =',(sa0,sa1,sa2))
    print('Theta(positive q meridian)=',-e,
          '; Theta(clockwise inverse)=',e)
    print('Right circle-trace slant = d Theta; positive-q evaluation =',-e*d)

print('All comparison identities passed.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
print('Program SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
