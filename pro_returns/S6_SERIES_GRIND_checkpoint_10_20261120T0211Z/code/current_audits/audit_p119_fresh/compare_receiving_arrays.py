"""Post-freeze comparison to the named receiving saved outputs.

No receiving program is imported.  The reconstruction imported here is the
fresh program already frozen before the receiving proof was released.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
import derive_chain as f

P=Path(__file__).parent; ROOT=P.parent
paths={
 'fresh':P/'fresh_candidate_chain.json',
 'receiving':ROOT/'audit_corrections/code/reconstruct_V_global_06.json',
 'verifier':ROOT/'audit_corrections/code/verify_V_global_saved_07.json',
 'cusp':ROOT/'audit_corrections/code/reconstruct_V_cusp_06.json'}
raw={k:json.loads(v.read_text()) for k,v in paths.items()}
R=raw['receiving']; V=raw['verifier']; F=raw['fresh']; C=raw['cusp']
checks=[]
def check(name,claim):
    assert claim,name
    checks.append(name)
def mat(value,rows,cols):return s.Matrix(value) if rows and cols else s.zeros(rows,cols)

nr=F['candidate_global_chain_ranks'];yr=F['Y_chain_ranks'];cr=f.cusp_ranks
db={k:mat(R['boundary_differentials'][str(k)],f.bd(k-1),f.bd(k)) for k in range(9)}
dy={k:mat(R['Y_differentials'][str(k)],f.yd(k-1),f.yd(k)) for k in range(9)}
jy={k:mat(R['jY'][str(k)],f.yd(k),f.bd(k)) for k in range(9)}
kr={k:mat(R['kappa'][str(k)],cr[k],f.n(6,k)) for k in range(9)}
dr={k:mat(R['global_differentials'][str(k)],nr[k-1] if k else 0,nr[k]) for k in range(9)}
df={0:s.zeros(0,nr[0]),**{k:s.Matrix(F['candidate_differentials'][str(k)]) for k in range(1,9)}}
for k in range(9):
    check(f'Y differential {k} identical',dy[k]==f.Y[k])
    check(f'boundary differential {k} identical',db[k]==f.db(0,k))
    check(f'boundary-to-Y map {k} identical',jy[k]==f.j_y(k))
    if k<=6:
        kc=s.Matrix(C['collapse'][str(k)]['matrix'])
        check(f'cusp S marking {k}',kr[k]==kc*f.ext(f.S.inv(),k))

er=s.Matrix(R['e']);psi=s.Matrix(R['psi']);rr=s.Matrix(R['r']);tt=s.Matrix(R['t'])
check('psi annihilates degree-four collapse',psi*kr[4]==s.zeros(1,15))
check('psi evaluates to one on e',psi*er==s.ones(1,1))

AA={};AI={}
for k in range(9):
    if k<=6:
        dd,u,v=f.TS[k];rank=sum(dd[i,i]!=0 for i in range(dd.rows))
        q=u.inv()[:,rank:]
        aa=kr[k]*q
        if k==4:aa=s.Matrix.hstack(aa,er)
    else:aa=s.zeros(0,0)
    ai=aa.inv();AA[k]=aa;AI[k]=ai
    check(f'cap basis A{k} unimodular',abs(int(aa.det()))==1 and all(x.q==1 for x in ai))
    check(f'cap basis intertwines collapse {k}',aa*f.kap[k]==kr[k])

rf=s.Matrix.hstack(s.zeros(1,15),f.eta[4][-1,:])
delta=rr-rf
dd,u,v=f.TS[3]
slot=next(j for j in range(dd.rows) if abs(dd[j,j])==2)
in_smith=delta[:,15:]*v
coeff=s.zeros(1,20)
for j in range(20):
    if dd[j,j]:
        coeff[j]=in_smith[j]/dd[j,j]
        check(f'cocycle primitive coefficient {j} integral',coeff[j].q==1)
    else:check(f'cocycle free slot {j} zero',in_smith[j]==0)
h=s.Matrix.hstack(coeff*u,s.zeros(1,15))
check('cocycle difference exact over Z',h*db[4]==delta)
check('receiving cocycle represents odd Smith class',int((rr[:,15:]*v)[slot])%2==1)

Q={};QI={}
for k in range(9):
    q=s.eye(nr[k]);qi=s.eye(nr[k]);a=yr[k];b=a+cr[k]
    # The receiving arrays use +(kappa,h); the fresh cone uses its negative.
    q[a:b,a:b]=-AA[k];qi[a:b,a:b]=-AI[k]
    if k==4:
        q[a:b,b:]=-er*h
        qi[a:b,b:]=-AI[k]*er*h
    check(f'global inverse {k}',q*qi==s.eye(nr[k]) and qi*q==s.eye(nr[k]))
    Q[k]=q;QI[k]=qi
for k in range(1,9):
    check(f'full differential intertwining {k}',dr[k]*Q[k]==Q[k-1]*df[k])

bridge=V['homology_basis_bridges']['4']
HB=s.Matrix(bridge['HB_free']);HY=s.Matrix(bridge['HY_projection'])
j4=s.Matrix(bridge['j4']);U=s.Matrix(bridge['j4_left']);VV=s.Matrix(bridge['j4_right']);DD=s.Matrix(bridge['j4_smith'])
f0=s.Matrix.hstack(kr[4],s.zeros(10,20))
check('actual degree-four homology gluing',j4==s.Matrix.vstack(HY*jy[4]*HB,f0*HB))
check('degree-four boundary representatives are cycles',db[4]*HB==s.zeros(35,18))
check('degree-four Smith identity',U*j4*VV==DD)
check('degree-four Smith bases unimodular',abs(int(U.det()))==abs(int(VV.det()))==1)
check('degree-four image primitive rank18',sum(DD[i,i]!=0 for i in range(18))==18 and all(abs(DD[i,i])==1 for i in range(18)))
rawc=s.Matrix(bridge['raw_cokernel_projection']);adapter=s.Matrix(bridge['cokernel_adapter']);adapted=s.Matrix(bridge['adapted_cokernel_projection'])
check('cokernel projection from last four Smith rows',rawc==U[-4:,:])
swap=s.eye(4);swap.row_swap(0,3)
check('literal cokernel row-swap adapter',adapter==swap and adapted==adapter*rawc)
check('literal cap quotient coordinate',adapted[:,12:]==s.Matrix.vstack(s.zeros(3,10),psi))

std=bridge['standard_kernel_basis'];K=s.Matrix(std['K']);W=s.Matrix(std['W']);X=s.Matrix(std['X']);T=s.Matrix(std['T'])
Klit=s.Matrix.hstack(*[s.eye(10)[:,i]-psi[i]*er for i in range(10) if i!=3])
check('literal kernel basis K',K==Klit)
check('kernel splitting unimodular',abs(int(s.Matrix.hstack(er,K).det()))==1)
change=s.Matrix(std['from_smith_kernel'])
check('Smith kernel adapter unimodular',abs(int(change.det()))==1)
check('Smith kernel adapter maps literal columns',s.Matrix(R['K'])*change==K)
check('j4W=(0,K)',j4*W==s.Matrix.vstack(s.zeros(12,9),K))
check('boundary cycles from homology lifts',HB*W==X)
check('X actual cycles',db[4]*X==s.zeros(35,9))
check('dYT=jYX',dy[5]*T==jy[4]*X)
check('f0X=K',f0*X==K)
check('rX=0',rr*X==s.zeros(1,9))
check('r d5=0',rr*db[5]==s.zeros(1,21))
check('2r=t d4',2*rr==tt*db[4])
for j in range(9):
    eta=X[:,j]*rr
    hom=T[:,j]*rr
    check(f'boundary automorphism square zero {j}',eta*eta==s.zeros(35))
    check(f'boundary automorphism chain map {j}',db[4]*eta==s.zeros(35) and eta*db[5]==s.zeros(35,21))
    check(f'complement homotopy {j}',dy[5]*hom==jy[4]*eta and hom*db[5]==s.zeros(118,21))

report={'utc':datetime.now(timezone.utc).isoformat(),
        'status':'PASS','assertions':len(checks),'checks':checks,
        'inputs':{k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()},
        'cap_basis_A':{k:a.tolist() for k,a in AA.items()},
        'cap_basis_A_inverse':{k:a.tolist() for k,a in AI.items()},
        'cap_basis_determinants':{k:int(a.det()) for k,a in AA.items()},
        'fresh_secondary_row':rf.tolist(),'receiving_secondary_row':rr.tolist(),
        'secondary_difference_primitive_h':h.tolist(),
        'global_adapter_formula':'Identity on Y and shifted B; -A_k on C_k to match the receiving plus convention; in global degree 4 also -e*h from B_3 to C_4. Inverse has -A_k^-1 and -A_4^-1*e*h.',
        'intertwining':'D_receiving[k] Q[k] = Q[k-1] D_fresh[k], all k=1,...,8, checked by exact multiplication',
        'scope':'Receiving outputs read only after frozen fresh derivation and full printed-proof comparison. No receiving program imported.'}
(P/'receiving_chain_adapter.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
print(json.dumps({'status':report['status'],'assertions':len(checks),'cap_basis_determinants':report['cap_basis_determinants'],
                  'h_nonzero_1based':[(i+1,int(h[i])) for i in range(h.cols) if h[i]],
                  'path':str(P/'receiving_chain_adapter.json')},indent=2))
