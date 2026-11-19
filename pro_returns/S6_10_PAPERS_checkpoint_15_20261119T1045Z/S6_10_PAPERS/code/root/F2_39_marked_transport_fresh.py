"""Fresh receiving-scope witnesses; no conjugacy-oracle or old chain code imported."""
from pathlib import Path
from itertools import product
from functools import reduce
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form

checks=[]
def ck(name,ok):
    ok=bool(ok);checks.append({'name':name,'pass':ok});assert ok,name
v=S.symbols('v');q=v*v-v+1
cyc=S.zeros(5)
for j in range(5):cyc[(j+1)%5,j]=1
I5=S.eye(5);X=I5[:,0].row_join(I5[:,2]+v*I5[:,4])
Y=S.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
B5=cyc.inv()*(I5-X*Y)
trace=S.expand(1+S.trace(cyc*(B5**3)))
ck('actual rank-six invariant trace polynomial',trace==-v**4+v**3-v**2+2)
for H in range(1,33):
    ck(f'trace exceeds height{H} word bound',abs(trace.subs(v,8*H))>6**4*H**4)

Aco=S.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
Bco=S.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M=[Aco.T,Bco.T];orders=[5,4]
vectors=[S.Matrix([1,3,-2,-1,2,0]),S.Matrix([-1,0,0,0,0,0])]
M0=(M[0]*M[1]).inv();N=M0-S.eye(6)
U=hermite_normal_form(N)
def integral_preimage(A,b):
    solution,params=A.gauss_jordan_solve(b)
    syms=list(params)
    coefficients=[x.subs({t:0 for t in syms}) for x in solution]
    coefficients += [S.diff(x,t) for x in solution for t in syms]
    den=int(S.ilcm(*[x.q for x in coefficients]))
    for values in product(range(den),repeat=len(syms)):
        z=solution.subs(dict(zip(syms,values)))
        if all(x.is_Integer for x in z):return z
    raise AssertionError('No actual integer preimage in the complete denominator-residue box')
V=S.Matrix.hstack(*(integral_preimage(N,U[:,j]) for j in range(3)))
P=U.row_join(V);std=S.zeros(6);std[:3,3:6]=S.eye(3)
ck('actual cusp N square zero rank3',N*N==S.zeros(6) and N.rank()==3)
ck('actual cusp marking integral unimodular',all(x.is_Integer for x in P) and abs(P.det())==1)
ck('actual cusp coordinate equation',N*P==P*std)
def powers(mats,nums):
    return [sum((m**j*u for j in range(d)),S.zeros(6,1))/d for m,u,d in zip(mats,nums,orders)]
def relation(mats,nums,kappa):
    ws=powers(mats,nums)
    top=S.Matrix.hstack(*(m-S.eye(6) for m in mats),*(-w for w in ws),kappa)
    bottom=S.zeros(2,15);bottom[0,12]=5;bottom[1,13]=4;bottom[:,14]=S.ones(2,1)
    return top.col_join(bottom)
def invariants(R):
    D=smith_normal_form(R,domain=S.ZZ);diag=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return {'free_rank':R.rows-len(diag),'torsion':[x for x in diag if x>1]}
results=[]
for twist in range(3):
    kap=twist*S.eye(6)[:,0];R=relation(M,vectors,kap);inv=invariants(R)
    ck(f'twist{twist} exact H1',inv=={'free_rank':0,'torsion':([] if twist==0 else [20*twist-1])})
    for a in range(6):
        for c in [-2,1]:
            Q=S.eye(6);Q[a,(a+1)%6]=c
            if c<0:Q[:,0]=-Q[:,0]
            Mi=[Q*m*Q.inv() for m in M];vi=[Q*x for x in vectors];kap2=Q*kap
            w2=powers(Mi,vi);w=powers(M,vectors)
            ck(f'twist{twist} Q{a},{c} actual powers',w2==[Q*x for x in w])
            R2=relation(Mi,vi,kap2);D=S.diag(Q,S.eye(2));E=S.diag(Q,Q,S.eye(3))
            ck(f'twist{twist} Q{a},{c} relation square',R2*E==D*R)
            ck(f'twist{twist} Q{a},{c} full H1',invariants(R2)==inv)
            P2=Q*P;N2=Q*N*Q.inv()
            ck(f'twist{twist} Q{a},{c} cusp map',N2*P2==P2*std and P2.inv()*Q*P==S.eye(6))
    results.append({'clutch_e0_multiple':twist,'H1':inv})
out={'status':'PASS','check_count':len(checks),'scope':'Trace invariant, explicit height witnesses, actual cusp marking and full marked H1 relation-square transport; no claim to rerun the full named conjugacy or chain algorithms','trace_polynomial':str(trace),'cusp_marking':[[str(x) for x in P.row(i)] for i in range(6)],'twist_results':results,'checks':checks}
Path('analysis/continuation_root/F2_39_marked_transport_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'check_count':len(checks),'twists':results},indent=2))
