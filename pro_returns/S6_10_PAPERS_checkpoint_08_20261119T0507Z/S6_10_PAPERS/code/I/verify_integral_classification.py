"""Exact integer and rational checks used by Paper I's classification proofs."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
I=s.eye(4)
d=s.Matrix([0,0,0,1]); gamma=s.Matrix([[1,0,0,0]])
E=d*gamma
eps=s.Matrix([1,2,-4,0]); eps2=s.Matrix([1,3,-3,0])
assert A1**3==I and A2**4==I
assert A1*E==E*A1==E and A2*E==E*A2==E
N1=sum([A1**i for i in range(3)],s.zeros(4))
N2=sum([A2**i for i in range(4)],s.zeros(4))
assert N1==s.Matrix([[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]])
assert N2==s.Matrix([[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]])
X=s.Matrix(4,4,s.symbols('x0:16'))
eq=list(X*A1-A1*X)+list(X*A2-A2*X)
matrix,_=s.linear_eq_to_matrix(eq,list(X))
assert len(matrix.nullspace())==2
assert matrix*s.Matrix(list(I))==s.zeros(32,1)
assert matrix*s.Matrix(list(E))==s.zeros(32,1)

N1c=s.Matrix([[3,0,0,0],[0,2,1,3]])
N2c=s.Matrix([[4,0,0,0],[0,2,2,4]])
assert s.Matrix.hstack(eps,d)*N1c==N1
assert s.Matrix.hstack(eps2,d)*N2c==N2
assert smith_normal_form(N1c,domain=s.ZZ)[:,:2]==s.diag(1,3)
assert smith_normal_form(N2c,domain=s.ZZ)[:,:2]==s.diag(2,4)

n=s.symbols('n',integer=True)
u=s.Matrix([0,1,0,0]); w=s.Matrix([0,0,1,0])
r1=-n*(u+w)/3; r2=n*(u+w)/4
ell1=-n*w; ell2=n*u/2
assert (I-A1)*r1==n*d/3+ell1
assert (I-A2)*r2==-n*d/4+ell2
A0=(A1*A2).inv()
ell0=-A0*(ell1+A1*ell2)
assert ell0==3*n*w/2-n*d/2

H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
assert H**2==I
assert H*A2*H==A2.inv()
assert H*A1*H==A2.inv()*A1.inv()*A2
assert -A2*H*eps==-eps+d
assert H*eps2==eps2-3*d
tau,mu,beta,c=s.symbols('tau mu beta c')
Pi=s.Matrix([[6*mu,tau,1,0],[beta+c,mu,0,1]])
Piref=s.Matrix([[6*(1-mu),-tau,1,0],[-beta-c,1-mu,0,1]])
assert Piref*H==-Pi
assert Pi.subs(c,c+n)==Pi*(I+n*E)

output={'status':'PASS','scope':['finite orders','rational centralizer dimension and generators','norm images and Smith forms','even-shift rational solutions and cusp cocycle','integral reflection and full period matrix comparison'],
 'norm1':str(N1),'norm2':str(N2),'cusp_cocycle':str(ell0),
 'proof_boundary':'Exact finite algebra only; analytic extension and descent are checked in the written proof.'}
target=Path(__file__).with_suffix('.output.json')
target.write_text(json.dumps(output,indent=2))
print(json.dumps(output,indent=2))
