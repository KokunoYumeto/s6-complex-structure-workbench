"""Exact current-run checks of the printed fourfold linear and residue data.

Inputs are transcribed from MAPS F.2.5, night P1.1--5, P1.17 and P1A.2.
This program certifies the stated arithmetic; the manuscript separately
supplies the geometric maps identifying those matrices with the construction.
"""
from pathlib import Path
from itertools import combinations, product
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

OUT = Path(__file__).with_suffix('.json')
A = s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
              [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B = s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
              [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M1, M2 = A.T, B.T
M0 = (M1*M2).inv()
I = s.eye(6)
N = M0-I
v1, v2 = s.Matrix([1,3,-2,-1,2,0]), s.Matrix([-1,0,0,0,0,0])
ell = s.Matrix([[1,0,0,0,0,0]])
S = s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],
              [-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])

def invariant_factors(M):
    D = smith_normal_form(M, domain=ZZ)
    return [int(abs(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

assert M1**5==I and M2**4==I
assert all(M1**j!=I for j in range(1,5))
assert all(M2**j!=I for j in range(1,4))
assert N*N==s.zeros(6) and N.rank()==3
assert invariant_factors(N)==[1,1,1]
assert abs(S.det())==1
assert S.inv()*M0*S==s.BlockMatrix([[s.eye(3),s.eye(3)],[s.zeros(3),s.eye(3)]]).as_explicit()
assert (M1-I).col_join(M2-I).rank()==6
assert hermite_normal_form((M1-I).row_join(M2-I))==s.eye(6)[:,1:]
assert invariant_factors((A-I).row_join(B-I))==[1,1,1,1,1,2]
caps=[]
for M,v,m in [(M1,v1,5),(M2,v2,4)]:
    assert M*v==v and ell*M==ell
    assert abs((ell*v)[0])==1
    assert all((s.Rational(j,m)*(ell*v)[0]).q>1 for j in range(1,m))
    R=s.zeros(7);R[:6,:6]=M-I;R[:6,6]=-v;R[6,6]=m
    caps.append({'order':m,'free_rank':7-R.rank(),'torsion':[d for d in invariant_factors(R) if d>1]})
assert caps==[{'order':5,'free_rank':2,'torsion':[]},{'order':4,'free_rank':2,'torsion':[2]}]
assert abs(s.Matrix([[5,0,-1],[0,4,1],[1,1,0]]).det())==1

Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
Q=s.eye(6);Q[:,0]=s.ones(6,1)
inds=list(combinations(range(4),2))
def wedge(M):return s.Matrix([[M.extract(i,j).det() for j in inds] for i in inds])
assert (Q.inv()*wedge(Cf.inv())*Q)[1:,1:]==A[1:,1:]
assert (Q.inv()*wedge(Cg)*Q)[1:,1:]==B[1:,1:]
G=s.zeros(6)
for i,j,e in [(0,5,1),(1,4,-1),(2,3,1)]:G[i,j]=G[j,i]=e
omega=s.ones(6,1)
contraction=omega.T*G
P=s.Matrix.vstack(-contraction[:,1:],s.eye(5))
j=(Q.inv()*P)[1:,:]
assert invariant_factors(j)==[1,1,1,1,2]
Gp=P.T*G*P
Gb=Q.T*G*Q
Gq=2*(Gb[1:,1:]-Gb[1:,:1]*Gb[:1,1:]/2)
assert Gp.det()==-2 and Gq.det()==-16
assert j.T*Gq*j==2*Gp
for E,F in [((wedge(Cf.inv())*P)[1:,:],(wedge(Cg)*P)[1:,:]),(A[1:,1:],B[1:,1:])]:
    X=s.Matrix(5,5,s.symbols('x:25'))
    L=s.linear_eq_to_matrix(list(E.T*X*E-X)+list(F.T*X*F-X),list(X))[0]
    assert 25-L.rank()==1

X=s.Matrix(6,6,s.symbols('z:36'))
L=s.linear_eq_to_matrix(list(X*M1-M1*X)+list(X*M2-M2*X),list(X))[0]
assert len(L.nullspace())==1 and s.Matrix(6,6,L.nullspace()[0])==I
R=s.Matrix([[1,0,0,0,0,0],[2,0,0,0,-1,0],[-1,0,-1,0,0,0],
            [-1,0,0,-1,0,0],[2,-1,0,0,0,0],[-1,1,1,1,1,1]])
Lr=s.linear_eq_to_matrix(list(X*M1-M1.inv()*X)+list(X*M2-M2.inv()*X),list(X))[0]
assert 36-Lr.rank()==1 and abs(R.det())==1 and R*R==I
assert all(R*M==M.inv()*R for M in [M1,M2])
H=M2.inv()*(-R)
assert H*M0*H.inv()==M0.inv()
Hs=S.inv()*H*S
Pr=s.Matrix([[1,0,0],[0,1,0],[1,-1,-1]])
assert Hs[:3,:3]==Pr and Hs[3:,3:]==-Pr and Hs[3:,:3]==s.zeros(3)
rays={tuple(sign*v for v in vector) for vector in product((0,1),repeat=3) if any(vector) for sign in (-1,1)}
bad=tuple(-Pr*s.Matrix([0,1,0]))
assert bad==(0,-1,1) and bad not in rays
tau=s.Matrix([0,1,1,1,1,1])/2
assert all(v.q==1 for M in [M1,M2,M0] for v in (M-I)*tau)

x,lam=s.symbols('x lam')
f=x**5+lam**3*x+lam**4
assert s.factor(s.discriminant(f,x))==lam**15*(3125*lam+256)
root={x:s.Rational(64,625),lam:-s.Rational(256,3125)}
assert f.subs(root)==0 and s.diff(f,x).subs(root)==0
assert s.diff(f,x,2).subs(root)!=0 and s.diff(f,lam).subs(root)!=0

def degree(k):return (4*k)//5+(-3*k)//4
def bundle_cohom(weights):
    ans=[0]*5
    for q in range(4):
        for inds in combinations(range(3),q):
            for weight in weights:
                d=degree(weight+sum([0,-1,-2][i] for i in inds))
                ans[q]+=max(d+1,0);ans[q+1]+=max(-d-1,0)
    return ans
expected={'O':([0],[1,1,0,0,0]),'E':([0,-1,-2],[1,1,0,0,0]),
          'F':([0,1,2],[1,3,2,0,0]),'L11':([11],[0,2,3,1,0]),
          'wedge2F':([1,2,3],[0,2,3,1,0]),'L11F':([11,12,13],[2,6,7,3,0]),
          'L9':([9],[1,2,1,0,0])}
for name,(weights,h) in expected.items():assert bundle_cohom(weights)==h
z=s.Symbol('z')
aa=-s.Rational(125,12288)*(192*z-3125)
bb=-s.Rational(78125,393216)*(96*z+3125)
cc=-s.Rational(125,512)
ee=s.Rational(78125,32768)
dd=-s.Rational(146484375,2097152)
C1=s.Matrix([[-cc,aa,0],[-ee,0,bb],[0,-dd,dd]])
C2=s.Matrix([[-dd,dd,0],[ee,0,-bb],[0,-cc,aa]])
det=s.factor(C1.det())
print('determinant_expanded_difference',s.factor(det-s.Rational(476837158203125,281474976710656)*(384*z+3125)))
assert s.factor(det-s.Rational(476837158203125,281474976710656)*(384*z+3125))==0
assert s.factor(C2.det())==-det
hodges=[[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]]
assert all(hodges[p][q]==hodges[4-p][4-q] for p in range(5) for q in range(5))
assert [sum((-1)**q*hodges[p][q] for q in range(5)) for p in range(5)]==[0,-1,4,-1,0]
assert sum((-1)**(p+q)*hodges[p][q] for p in range(5) for q in range(5))==6

record={'status':'PASS','model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',
 'date':'2026-11-18','scope':'exact printed linear, lattice, cusp-fan and cohomology-residue arithmetic; no geometric completeness inferred from these calculations',
 'finite_caps':caps,'primitive_to_quotient_smith':invariant_factors(j),
 'primitive_and_quotient_form_determinants':[int(Gp.det()),int(Gq.det())],
 'centralizer_dimension':1,'reflection_intertwiner_dimension':1,'anti_fan_obstruction':bad,
 'orbifold_bundle_cohomology':{k:v[1] for k,v in expected.items()},
 'rank_jump_polynomial':str(det),'hodge_table':hodges}
OUT.write_text(json.dumps(record,indent=2,default=int)+'\n')
print(json.dumps(record,indent=2,default=int))
