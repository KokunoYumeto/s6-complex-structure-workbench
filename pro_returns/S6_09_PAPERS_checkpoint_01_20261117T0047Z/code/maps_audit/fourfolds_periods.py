"""Exact certificates for the geometric period construction in F.3.5--7.

No numerical continuation or positivity sampling is used.  The analytic
height estimate is proved in the text.  This script checks the algebraic
curve, root exponents, line-bundle cohomology inputs, and the exact
primitive-exterior quotient representation.
"""
from sympy import Matrix, eye, zeros, ones, symbols, factor, discriminant, Rational, floor
from itertools import combinations

x,lam,s,X,Y=symbols('x lam s X Y')
f=x**5+lam**3*x+lam**4
disc=factor(discriminant(f,x))
assert disc == lam**15*(3125*lam+256)
print("discriminant",disc)
node=Rational(-256,3125)
r=Rational(64,625)
assert f.subs({lam:node,x:r})==0
assert f.diff(x).subs({lam:node,x:r})==0
assert f.diff(x,2).subs({lam:node,x:r})!=0
print("node parameter",node,"double branch root",r,
      "nonzero quadratic coefficient",f.diff(x,2).subs({lam:node,x:r})/2)
assert factor(f.subs({lam:s**8,x:s**6*X})/s**30)==X**5+X+s**2
assert factor(f.subs({lam:s**-5,x:s**-4*X})*s**20)==X**5+s*X+1
print("root models at zero/infinity: Y²=X⁵+X+s²; Y²=X⁵+sX+1")
print("Hodge line degrees",
      Rational(6,5)-Rational(9,8),Rational(2,5)-Rational(3,8))
assert Rational(6,5)-Rational(9,8)==Rational(3,40)
assert Rational(2,5)-Rational(3,8)==Rational(1,40)
coarse={k:int(floor(Rational(2*k,5))+floor(Rational(-3*k,8)))
        for k in [0,-2,-4,2,4,6]}
assert all(v>=-1 for v in coarse.values())
print("coarse degrees of T^k",coarse)

Cf=Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert Cf**5==eye(4) and Cg**8==eye(4)
assert (Cf.inv()*Cg-eye(4)).rank()==1
assert (Cf.inv()*Cg-eye(4))**2==zeros(4)
pairs=list(combinations(range(4),2))
def wedge2(T):
    return Matrix([[T.extract(i,j).det() for j in pairs] for i in pairs])
Q=eye(6);Q[:,0]=ones(6,1)
assert Q.det()==1
W1=Q.inv()*wedge2(Cf.inv())*Q
W2=Q.inv()*wedge2(Cg)*Q
assert W1[:,0]==eye(6)[:,0] and W2[:,0]==eye(6)[:,0]
A=Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],
          [0,1,0,-1,0,0],[0,2,-1,-1,0,1],
          [0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],
          [0,0,-1,0,0,1],[0,0,-1,0,0,0],
          [0,1,-1,0,0,0],[0,0,-1,1,0,0]])
assert W1[1:,1:]==A[1:,1:] and W2[1:,1:]==B[1:,1:]
assert (A*B-eye(6))**2==zeros(6)
assert (A*B-eye(6)).rank()==3
assert (A[1:,1:]*B[1:,1:]-eye(5)).rank()==2
print("rank-four companion pair",Cf.inv(),Cg)
print("primitive quotient certificate Q",Q)
print("quotient matrices agree exactly with the candidate lower five blocks")
print("cusp ranks: rank-four source 1; rank-five quotient 2; rank-six extension 3")
print("All exact checks passed; global height and gluing are proved analytically.")
