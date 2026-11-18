"""Exact diagnostic of native Cox mutation and GF uniqueness; no theorem export."""
from collections import deque
from datetime import datetime,timezone
from pathlib import Path
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
Q=[S.Matrix([[1,-1],[0,1]]),S.Matrix([[1,0],[-1,1]]),S.Matrix([[1,1],[0,1]])]
selected=[2,2,0]
e1=S.Matrix([1,0]);e2=S.Matrix([0,1])

def local(P):
    B=-6*P.inv()*e1*e1.T*P
    l=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
    xi,ups=P.inv()*e2
    w=[xi,ups,-xi-ups]
    d=[-xi-2*ups,-2*xi-ups,xi-ups]
    I=[-3*w[i]+d[i]*(l[i]+3) for i in range(3)]
    W=[-3*w[i]-d[i]*(l[i]+3) for i in range(3)]
    return B,l,w,d,I,W

def solve(P,i,a,b):
    B,l,w,d,I,W=local(P)
    zeros=[j for j in range(3) if w[j]==0]
    if not zeros:
        r=S.Matrix([1/x for x in w])
        c=w[i]**2*a-w[i]*I[i]
        eta=w[i]*b-W[i]
        V=S.diag(*[I[j]/w[j] for j in range(3)])+c*r*r.T
        delta=S.Matrix([(W[j]+eta)/w[j] for j in range(3)])
    elif zeros==[i]:
        V=S.zeros(3);delta=S.zeros(3,1)
        V[i,i]=a;delta[i]=b
        for j in range(3):
            if j==i:continue
            V[j,j]=I[j]/w[j]
            V[i,j]=V[j,i]=-I[i]/w[j]
            delta[j]=(W[j]-W[i])/w[j]
    else:
        return None
    for j in (1,2):
        h=S.zeros(3,1);h[j]=w[j];h[0]-=w[0]
        rhs=S.zeros(3,1);rhs[j]=I[j];rhs[0]-=I[0]
        assert all(S.simplify(x)==0 for x in V*h-rhs)
        assert S.simplify(w[j]*delta[j]-w[0]*delta[0]-W[j]+W[0])==0
    return V,delta

def pkey(P):return tuple(int(x) for x in P)
def fan_key(P):
    v,w=P[:,0],P[:,1]
    rays=[]
    for x in [v,w,w-v]:
        a,b=map(int,x)
        if a<0 or (a==0 and b<0):a,b=-a,-b
        rays.append((a,b))
    return tuple(sorted(rays))

initial_V=S.Matrix([[0,6,-6],[6,0,0],[-6,0,0]])
initial_delta=S.Matrix([-12,-12,0])
P0=S.eye(2)
P1=S.Matrix([[1,0],[1,1]])
V1,d1=solve(P1,0,S.Integer(0),S.Integer(-12))
queue=deque([(P0,initial_V,initial_delta,1,()),(P1,V1,d1,1,())])
visited={};fans={};conflicts=[];integrality_failures=[];skipped=[]
max_depth=7
while queue:
    P,V,delta,s,word=queue.popleft()
    key=pkey(P);fk=fan_key(P)
    if key in visited:
        old=visited[key]
        if old['V']!=V or old['delta']!=delta or old['s']!=s:
            conflicts.append({'type':'same_basis','P':list(key),'old_word':old['word'],'new_word':word,
                              'old_s':old['s'],'new_s':s,
                              'V_difference':[[str(x) for x in row] for row in (V-old['V']).tolist()],
                              'delta_difference':[str(x) for x in delta-old['delta']]})
        continue
    visited[key]={'V':V,'delta':delta,'s':s,'word':word}
    if fk in fans and fans[fk]['s']!=s:
        conflicts.append({'type':'same_fan','fan':fk,'old':fans[fk],
                          'new':{'P':list(key),'s':s,'word':word}})
    else:
        fans[fk]={'P':list(key),'s':s,'word':word}
    if len(word)>=max_depth:continue
    for i in range(3):
        Pn=P*Q[i]
        a=V[i,i];b=2*a-delta[i]
        out=solve(Pn,selected[i],a,b)
        if out is None:
            skipped.append({'P':list(key),'edge':i,'reason':'A separate fixed target edge leaves a transverse entry.'})
            continue
        Vn,dn=out
        right=(delta[i]-V[i,i])/2
        if any(x.q!=1 for x in list(Vn)+list(dn)+[right]):
            integrality_failures.append({'P':list(key),'edge':i,'word':word,
                                         'V':[str(x) for x in Vn],'delta':[str(x) for x in dn],'right':str(right)})
            continue
        sn=(s+int(right))%28
        queue.append((Pn,Vn,dn,sn,word+(i,)))

j=S.symbols('j',integer=True,positive=True)
Pj=S.Matrix([[1,-j],[0,1]])
Vj=S.Matrix([[0,6*(j+1),-6],[6*(j+1),18*j*(j+1),-6*j],[-6,-6*j,0]])
dj=S.Matrix([-12*(j+1),-24*j*(j+1)-12,12*j])
Vp,dp=solve(Pj*Q[0],2,Vj[0,0],2*Vj[0,0]-dj[0])
targetV=Vj.subs(j,j+1);targetd=dj.subs(j,j+1)
symbolic={
 'staircase_V_step':all(S.simplify(x)==0 for x in Vp-targetV),
 'staircase_delta_step':all(S.simplify(x)==0 for x in dp-targetd),
 'staircase_central_step':S.simplify((1-3*j*(j+1))+(dj[0]-Vj[0,0])/2-(1-3*(j+1)*(j+2)))==0,
 'second_branch_central':S.simplify((1-3*j*(j+1))+(dj[1]-Vj[1,1])/2-(-5-24*j*(j+1)))==0,
}
out={'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_DIAGNOSTIC' if not conflicts and not integrality_failures and all(symbolic.values()) else 'FAILED_DIAGNOSTIC',
 'basis_states':len(visited),'fan_states':len(fans),'depth':max_depth,
 'conflicts':conflicts,'integrality_failures':integrality_failures,
 'skipped_separate_fixed_targets':len(skipped),'symbolic':symbolic,
 'scope':'The exact Cox and native-framing maps require their written proof. No unproved matrix reset or full-fan return is assigned.'}
(root/'code/part3_root/source_cusp_mutation_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('conflicts','integrality_failures')},indent=2))
print('conflicts',len(conflicts),'integrality_failures',len(integrality_failures))
if conflicts:print(json.dumps(conflicts[:3],indent=2))
if integrality_failures:print(json.dumps(integrality_failures[:3],indent=2))
