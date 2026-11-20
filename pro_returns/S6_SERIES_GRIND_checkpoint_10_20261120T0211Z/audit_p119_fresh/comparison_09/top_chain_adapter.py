"""Post-reading exact top-chain adapters for the literal finite-cap diagram.

This checks the candidate integral diagram adapter.  Its geometric origin is
kept as a separate proof obligation until explicitly established.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import sympy as s
HERE=Path(__file__).parent;P=HERE.parent
sys.path.insert(0,str(P))
import derive_chain as f

K={
1:s.Matrix([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],[0,-1,-1,0,-1],[0,0,1,0,0]]),
2:s.Matrix([[-1,0,-1,0,-1],[-1,1,0,1,-1],[0,1,-1,1,-1],[0,-1,0,-1,1],[1,-1,1,0,1]])}
J=s.zeros(6)
for col in range(6):J[5-col,col]=(-1)**(5-col)
checks=[]
def check(label,condition):
    assert condition,label;checks.append(label)

Q={};RR={};beta={};h={};Hrow={};Halternative={}
for i in (1,2):
    Q[i]=f.P[i]*s.diag(1,K[i])
    RR[i]=Q[i].inv()*f.M[i]*Q[i]
    beta[i]=s.ones(1,6)*Q[i].T*J/2
    h[i]=beta[i]*(f.W[i,5]-s.eye(6))
    check(f'Q{i} unimodular',abs(int(Q[i].det()))==1)
    check(f'h{i} integral',all(a.q==1 for a in h[i]))
    check(f'actual order {i}',f.M[i]**f.mult[i]==s.eye(6))
    Halternative[i]=s.zeros(1,6) if i==1 else f.eps[i]*f.mult[i]*beta[i]
    Hrow[i]=s.zeros(1,6) if i==1 else 2*h[i]
    check(f'cap homotopy {i} integral',all(a.q==1 for a in Hrow[i]))
    check(f'cap homotopy {i} differential',Hrow[i]*(f.W[i,5]-s.eye(6))==f.eps[i]*f.mult[i]*h[i])
    check(f'alternative cap homotopy {i}',(Halternative[i]-Hrow[i])*(f.W[i,5]-s.eye(6))==s.zeros(1,6))
check('order5 h1 zero',h[1]==s.zeros(1,6))
check('order4 h2 literal',h[2]==s.Matrix([[1,-1,-1,1,-1,0]]))
check('order4 cap homotopy literal',Hrow[2]==s.Matrix([[2,-2,-2,2,-2,0]]))

UG={k:s.eye(f.gd(k)) for k in range(9)}
UG[6][0,1:7]=h[1];UG[6][0,7:13]=h[2]
UB={i:{k:s.eye(f.bd(k)) for k in range(9)} for i in (1,2)}
for i in (1,2):UB[i][6][0,1:]=h[i]
for i in (1,2):
    for k in range(1,9):
        check(f'boundary source chain map {i},{k}',f.db(i,k)*UB[i][k]==UB[i][k-1]*f.db(i,k))
    for k in range(9):
        check(f'finite boundary graph square {i},{k}',UG[k]*f.jg(i,k)==f.jg(i,k)*UB[i][k])
    HH=s.Matrix.hstack(Hrow[i],s.zeros(1,f.n(6,4)))
    check(f'finite cap actual row {i}',f.je(i,6)*(UB[i][6]-s.eye(7))==HH*f.db(i,6))

SY={k:s.eye(f.yd(k)) for k in range(9)}
SY[6][:f.gd(6),:f.gd(6)]=UG[6]
for i in (1,2):
    erow=f.gd(6)+(i-1)*f.ed(6)
    bcol=f.gd(6)+2*f.ed(6)+(i-1)*f.bd(5)
    SY[6][erow,bcol:bcol+6]=Hrow[i]
    start=f.gd(7)+2*f.ed(7)+(i-1)*f.bd(6)
    SY[7][start:start+7,start:start+7]=UB[i][6]
SI={}
for k in range(9):
    NN=SY[k]-s.eye(f.yd(k));check(f'Y nilpotence {k}',NN*NN==s.zeros(f.yd(k)))
    SI[k]=s.eye(f.yd(k))-NN
    check(f'Y inverse {k}',SY[k]*SI[k]==s.eye(f.yd(k)) and SI[k]*SY[k]==s.eye(f.yd(k)))
for k in range(1,9):check(f'Y full differential {k}',f.Y[k]*SY[k]==SY[k-1]*f.Y[k])

h0=-h[1]*f.W[2,5]*f.W[0,5]-h[2]*f.W[0,5]
check('h0 literal',h0==s.Matrix([[-1,1,1,-3,-1,0]]))
U0={k:s.eye(f.bd(k)) for k in range(9)};U0[6][0,1:]=h0
for k in range(1,9):check(f'cusp source chain map {k}',f.db(0,k)*U0[k]==U0[k-1]*f.db(0,k))
for k in range(9):check(f'exact jY square {k}',SY[k]*f.j_y(k)==f.j_y(k)*U0[k])
X=f.ext(f.S,5)[:,[2,1,0]]
check('actual source correction values',h0*X==s.Matrix([[0,-2,-2]]))

D=f.global_complex();DS={k:a.copy() for k,a in D.items()}
# Change j_C,6 from (kappa,0) to j_C,6 U0,6^-1.
DS[7][f.yd(6),f.yd(7)+1:]=h0
PP={};PI={}
for k in range(9):
    uk=U0[k-1] if k else s.eye(0)
    PP[k]=s.diag(SY[k],s.eye(f.cusp_ranks[k]),uk)
    PI[k]=s.diag(SI[k],s.eye(f.cusp_ranks[k]),2*s.eye(uk.rows)-uk)
    check(f'global inverse {k}',PP[k]*PI[k]==s.eye(PP[k].rows) and PI[k]*PP[k]==s.eye(PP[k].rows))
for k in range(1,9):check(f'global top correction intertwining {k}',DS[k]*PP[k]==PP[k-1]*D[k])

def sparse(a):return {'shape':list(a.shape),'entries_0based':[[i,j,int(a[i,j])] for i in range(a.rows) for j in range(a.cols) if a[i,j]]}
report={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS for exact integral diagram identities; geometric realization proof separate','assertions':len(checks),'checks':checks,
        'orientation_J':J.tolist(),'Q':{i:a.tolist() for i,a in Q.items()},'signed_permutations':{i:a.tolist() for i,a in RR.items()},
        'beta':{i:[[str(a) for a in b]] for i,b in beta.items()},'h':{i:a.tolist() for i,a in h.items()},'cap_homotopy_rows':{i:a.tolist() for i,a in Hrow.items()},'alternative_cap_homotopy_rows':{i:a.tolist() for i,a in Halternative.items()},
        'h0':h0.tolist(),'h0_actual_xj':(h0*X).tolist(),
        'Y_automorphisms_sparse':{k:sparse(SY[k]-s.eye(f.yd(k))) for k in (6,7)},
        'cusp_source_automorphism_sparse':sparse(U0[6]-s.eye(7)),
        'global_adapter':'P_k=diag(SY_k,I_Ck,U0_(k-1)); DS_k P_k=P_(k-1)D_k; DS has j_C,6=(kappa,-kappa*h0). Inverses are I minus the square-zero corrections.',
        'scope':'Post-reading exact source/target/cap-homotopy candidate. This does not by itself identify the candidate with the geometric polyhedral-to-product-cell comparison.'}
(HERE/'top_chain_adapter.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
print(json.dumps({'utc':report['utc'],'status':report['status'],'assertions':len(checks),'h0':report['h0'],'cap_homotopy_rows':report['cap_homotopy_rows']},indent=2,default=int))
