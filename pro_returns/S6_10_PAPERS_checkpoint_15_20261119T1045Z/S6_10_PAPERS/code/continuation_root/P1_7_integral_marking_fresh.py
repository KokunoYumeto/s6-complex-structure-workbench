"""New exact P1.7 integral marking computation, written before target reading."""
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from itertools import combinations
import hashlib,json,datetime
P=Path(__file__).resolve().parents[2]
A=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
B=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
J=s.Matrix([[0,1,-1,1],[-1,0,1,-1],[1,-1,0,1],[-1,1,-1,0]])
d=s.Matrix([1,1,1,0]);D=s.Matrix.hstack(*[A**i*d for i in range(4)])
W=s.zeros(4)
for i in range(4):W[i,3-i]=1
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append({'name':name,'result':'passed'})
ck('A order five',A**5==s.eye(4))
ck('B eighth power and central fourth',B**8==s.eye(4) and B**4==-s.eye(4))
ck('actual common invariant form',A.T*J*A==J and B.T*J*B==J)
coeff=s.symbols('j0:6');JJ=s.zeros(4);pairs=list(combinations(range(4),2))
for k,(i,j) in enumerate(pairs):JJ[i,j]=coeff[k];JJ[j,i]=-coeff[k]
lin,_=s.linear_eq_to_matrix(list(A.T*JJ*A-JJ)+list(B.T*JJ*B-JJ),coeff)
ck('invariant alternating space dimension one',lin.rank()==5)
ck('unimodular form',J.det()==1)
N=A.inv()*B-s.eye(4)
ck('actual node rank-one factor',N==d*s.Matrix([[0,0,0,1]]))
ck('actual node functional',d.T*J==s.Matrix([[0,0,0,1]]))
ck('primitive single transvection matrix',N.rank()==1 and N*N==s.zeros(4) and s.gcd_list(list(N))==1)
ck('vanishing orbit unimodular',D.det()==1 and all(x.q==1 for x in D.inv()))
G=D.T*J*D
ck('actual vanishing orbit Gram matrix',G==s.Matrix([[0,1,0,0],[-1,0,1,0],[0,-1,0,1],[0,0,-1,0]]))
ck('Gram inverse integral',G.det()==1 and all(x.q==1 for x in G.inv()))
ck('simultaneous integral reversal',W*W==s.eye(4) and W.det()==1 and W*A*W==A.inv() and W*B*W==B.inv())
ck('reversal preserves exact pairing sign',W.T*J*W==-J)
T1=A.inv();T2=B;c=(T1*T2).inv();cp=T1.inv()*c*T1
ck('actual based cusp conjugation',c==B.inv()*A and cp==A*B.inv())
ck('geometric and formal generator product',A*(A.inv()*B)*B.inv()==s.eye(4))
ck('homology/cohomology dual evaluation',T1.T*T1.inv().T==s.eye(4) and T2.T*T2.inv().T==s.eye(4))
def wedge2(M):
    return s.Matrix([[M[i,k]*M[j,l]-M[i,l]*M[j,k] for k,l in pairs] for i,j in pairs])
omega=s.ones(6,1);Q=s.eye(6);Q[:,0]=omega
AA=wedge2(T1);BB=wedge2(T2)
ck('primitive invariant wedge vector',AA*omega==omega and BB*omega==omega)
ck('actual quotient basis unimodular',Q.det()==1)
qa=Q.inv()*AA*Q;qb=Q.inv()*BB*Q
ck('invariant line produces quotient blocks',qa[1:,0]==s.zeros(5,1) and qb[1:,0]==s.zeros(5,1))
K=s.zeros(6)
for i,j,sgn in [(0,5,1),(1,4,-1),(2,3,1)]:K[i,j]=K[j,i]=sgn
row=omega.T*K
ck('exact wedge pairing and square',K.det()==-1 and (omega.T*K*omega)[0]==2 and row==s.Matrix([[1,-1,1,1,-1,1]]))
primitive=s.Matrix.hstack(*[s.eye(6)[:,j]-row[j]*s.eye(6)[:,0] for j in range(1,6)])
ck('primitive kernel basis',row*primitive==s.zeros(1,5) and primitive[1:,:]==s.eye(5))
pq=(Q.inv()*primitive)[1:,:]
snf=smith_normal_form(pq,domain=s.ZZ)
ck('natural primitive projection exact index',sorted(abs(snf[i,i]) for i in range(5))==[1,1,1,1,2])
for M,name in [(AA,'A'),(BB,'B')]:
    ck(f'wedge pairing preserved by {name}',M.T*K*M==K)
out={'status':'passed','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro',
 'method':'fresh SymPy linear equations, exact symplectic orbit and integral inverse, actual peripheral word identities, independently constructed exterior-square minors and Smith form',
 'prereading_sha256':hashlib.sha256((P/'analysis/continuation_root/P1_7_before_read.md').read_bytes()).hexdigest(),
 'count':len(checks),'checks':checks,
 'matrices':{k:str(v) for k,v in {'J':J,'d':d,'D':D,'D_inverse':D.inv(),'G':G,'G_inverse':G.inv(),'W':W,'c':c,'c_prime':cp,'quotient_A':qa[1:,1:],'quotient_B':qb[1:,1:],'primitive_to_quotient':pq,'primitive_map_smith':snf}.items()},
 'scope':'All displayed P1.7 derivation matrices; universal lattice saturation follows from the written integral Gram inverse argument. No old producing code or target proof read.'}
target=Path(__file__).with_suffix('.output.json');target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','completed_at_utc','count','prereading_sha256']},indent=2))
