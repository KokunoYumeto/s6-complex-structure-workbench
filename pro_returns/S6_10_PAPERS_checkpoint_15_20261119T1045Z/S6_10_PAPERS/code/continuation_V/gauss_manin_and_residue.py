"""New algebraic de Rham reduction and quotient/residue calculations.

The reduction is solved as a polynomial exact-differential identity, independently
of the earlier source programs. The displayed connection is an expected result,
not an imported computational implementation. All arithmetic is exact.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

x,l,z=s.symbols('x lambda z');a=-s.Rational(256,3125)
f=x**5+l**3*x+l**4
fprime=s.diff(f,x);fl=s.diff(f,l)
gamma=s.zeros(4);exact_primitives=[]
u=s.symbols('u0:4');v=s.symbols('v0:5')
for k in range(4):
    primitive=sum(v[j]*x**j for j in range(5))
    combination=sum(u[j]*x**j for j in range(4))
    identity=s.Poly(-x**k*fl/2-combination*f-s.diff(primitive,x)*f+primitive*fprime/2,x)
    equations=identity.all_coeffs()
    A,b=s.linear_eq_to_matrix(equations,(*u,*v))
    solution=A.inv()*b
    solution=[s.factor(r) for r in solution]
    for j in range(4):gamma[j,k]=solution[j]
    exact_primitives.append(s.factor(sum(solution[4+j]*x**j for j in range(5))))
    check=-x**k*fl/2-sum(gamma[j,k]*x**j for j in range(4))*f-s.diff(exact_primitives[-1],x)*f+exact_primitives[-1]*fprime/2
    assert s.factor(check)==0

pairs=list(combinations(range(4),2));pos={p:i for i,p in enumerate(pairs)}
G2=s.zeros(6)
def add_term(rowpair,col,coeff):
    i,j=rowpair
    if i==j:return
    sign=1 if i<j else -1
    G2[pos[tuple(sorted((i,j)))],col]+=sign*coeff
for col,(i,j) in enumerate(pairs):
    for k in range(4):
        add_term((k,j),col,gamma[k,i]);add_term((i,k),col,gamma[k,j])
symplectic=s.Matrix([0,0,3,1,0,0])
assert all(s.factor(x)==0 for x in G2*symplectic)
Q=s.zeros(5,6);keep=[0,1,2,4,5]
for i,j in enumerate(keep):Q[i,j]=1
Q[2,3]=-3
J=s.zeros(6,5)
for i,j in enumerate(keep):J[j,i]=1
W=(Q*G2*J).applyfunc(s.factor)
expected=s.Matrix([
[-8*(625*l+48)/l,-8,10*l,s.Rational(75,2)*l*l,0],
[-s.Rational(125,2)/l,-4*(625*l+48)/l,8,0,s.Rational(75,2)*l*l],
[300/l**2,-375/l,0,-48,60*l],
[120/l**3,0,s.Rational(125,2)/l,4*(625*l+48)/l,-8],
[0,120/l**3,50/l**2,-s.Rational(125,2)/l,8*(625*l+48)/l]])/(3125*l+256)
assert all(s.factor(x)==0 for x in W-expected)

b=s.Matrix([[-s.Rational(25,6)/l**2,-s.Rational(125,48)/l,0,1,0]])/(l-a)
G6=s.zeros(6);G6[0,1:]=b;G6[1:,1:]=W
res=G6.applyfunc(lambda q:s.cancel((l-a)*q).subs(l,a))
# Frame (e,w2,w1,w0,w-1,w-2), F=(w0+4z e/3,w1,w2), G=(e,w-1,w-2).
F=s.zeros(6,3);F[0,0]=s.Rational(4,3)*z;F[3,0]=1;F[2,1]=1;F[1,2]=1
projection=s.zeros(3,6);projection[0,0]=1;projection[0,3]=-s.Rational(4,3)*z;projection[1,4]=1;projection[2,5]=1
R=(projection*res*F).applyfunc(s.factor)
AA=-125*(192*z-3125)/12288
BB=-s.Rational(78125,393216)*(96*z+3125)
CC=-s.Rational(125,512);EE=s.Rational(78125,32768);DD=-s.Rational(146484375,2097152)
assert all(s.factor(q)==0 for q in R-s.Matrix([[0,AA,BB],[CC,0,DD],[EE,DD,0]]))
C1=s.Matrix([[-CC,AA,0],[-EE,0,BB],[0,-DD,DD]])
C2=s.Matrix([[-DD,DD,0],[EE,0,-BB],[0,-CC,AA]])
det1=s.factor(C1.det());det2=s.factor(C2.det())
assert s.factor(det1-s.Rational(476837158203125,281474976710656)*(384*z+3125))==0
assert det2==-det1
root=s.solve(det1,z)[0]
assert root==-s.Rational(3125,384)
assert s.factor(-s.Rational(128,625)*root)==s.Rational(5,3)

def mat(A):return [[str(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
out={'method':'polynomial exact-differential linear solve; induced exterior-square derivative; explicit primitive quotient; exact cusp residue',
 'Gamma_H':mat(gamma),'exact_primitives':[str(v) for v in exact_primitives],
 'Gamma_wedge2':mat(G2),'primitive_quotient_map':mat(Q),'Gamma_W':mat(W),
 'displayed_Gamma_W_matches':True,'cusp_residue':mat(res),'R':mat(R),'C1':mat(C1),'C2':mat(C2),
 'det_C1':str(det1),'det_C2':str(det2),'exceptional_z':str(root),
 'exceptional_real_c':'5/(3*pi)',
 'scope':'The extension row b was taken from the stated model. Its identification with integral monodromy and the numerical transversality exclusion are separate proof/certificate obligations.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'Gamma_W':'exact match','det_C1':str(det1),'det_C2':str(det2),'exceptional_z':str(root),'scope':out['scope']},indent=2))
