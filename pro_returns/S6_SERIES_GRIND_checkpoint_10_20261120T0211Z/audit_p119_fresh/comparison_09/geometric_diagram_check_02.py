"""Post-reading exact checks for the geometric P1.19 diagram comparison.

The geometric morphisms are specified in GEOMETRIC_COMPARISON_02.md.  This
program checks their literal finite-cap transports, all-degree free-word
homotopy identity, and the coefficient-two top homotopy.  It does not import
or execute a historical receiving producer or overwrite the first progress
certificate.  The triangle/product specifications below are exact integral
polyhedral chains, not sampled floating-point approximations.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import sys, json, hashlib
import sympy as s

HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent))
import derive_chain as f

prior=json.loads((HERE/'top_chain_adapter.json').read_text())
Q={i:s.Matrix(prior['Q'][str(i)]) for i in (1,2)}
RR={i:Q[i].inv()*f.M[i]*Q[i] for i in (1,2)}
KK={i:(f.P[i].inv()*Q[i])[1:,1:] for i in (1,2)}
J=s.Matrix(prior['orientation_J'])
h={i:s.Matrix(prior['h'][str(i)]) for i in (1,2)}
checks=[]
def ck(label,condition):
    assert condition,label
    checks.append(label)

def signed_b(i,k):
    R=RR[i][1:,1:]
    z=s.zeros(f.ed(k),f.bd(k))
    ff=list(combinations(range(6),k))
    ss=list(combinations(range(6),k-1)) if k else []
    kr=list(combinations(range(1,6),k))
    ks=list(combinations(range(1,6),k-1)) if k else []
    for j,c in enumerate(ff):
        if 0 not in c:
            z[kr.index(c),j]=1
        else:
            W=f.ext(R,k-1)
            N=sum((W**a for a in range(f.mult[i])),s.zeros(*W.shape))
            z[f.n(5,k):,j]=f.eps[i]*N[:,ks.index(c[1:])]
    for j,c in enumerate(ss):
        if 0 not in c:z[f.n(5,k)+ks.index(c),f.n(6,k)+j]=1
    return z

def signed_db(i,k):
    z=s.zeros(f.bd(k-1),f.bd(k))
    z[:f.n(6,k-1),f.n(6,k):]=f.ext(RR[i],k-1)-s.eye(f.n(6,k-1))
    return z

def signed_de(i,k):
    z=s.zeros(f.ed(k-1),f.ed(k))
    z[:f.n(5,k-1),f.n(5,k):]=f.ext(RR[i][1:,1:],k-1)-s.eye(f.n(5,k-1))
    return z

cap_adapters={}
for i in (1,2):
    BB={k:s.diag(f.ext(Q[i],k),f.ext(Q[i],k-1)) for k in range(9)}
    EE={k:s.diag(f.ext(KK[i],k),f.ext(KK[i],k-1)) for k in range(9)}
    for k in range(9):
        ck(f'literal finite-cap conjugacy {i},{k}',f.je(i,k)*BB[k]==EE[k]*signed_b(i,k))
        ck(f'boundary adapter inverse {i},{k}',BB[k].det() in (-1,1))
        ck(f'cap adapter inverse {i},{k}',EE[k].det() in (-1,1))
    for k in range(1,9):
        ck(f'boundary cellular transport {i},{k}',f.db(i,k)*BB[k]==BB[k-1]*signed_db(i,k))
        ck(f'cap cellular transport {i},{k}',f.de(i,k)*EE[k]==EE[k-1]*signed_de(i,k))
        ck(f'signed cap chain map {i},{k}',signed_de(i,k)*signed_b(i,k)==signed_b(i,k-1)*signed_db(i,k))
    mer=s.zeros(f.bd(1),1);mer[6]=1
    capmer=s.zeros(f.ed(1),1);capmer[5]=1
    ck(f'actual based affine meridian {i}',f.je(i,1)*mer==capmer)
    vv=s.zeros(f.bd(1),1);vv[:6,:]=f.eps[i]*f.v[i]
    ck(f'actual signed fibre-circle degree {i}',f.je(i,1)*vv==f.eps[i]*f.mult[i]*capmer)
    signed_h=s.zeros(1,6)
    if i==2:signed_h[0,0]=1
    transported_h=int(Q[i].det())*signed_h*f.ext(Q[i].inv(),5)
    ck(f'geometric D_R transport equals h {i}',transported_h==h[i])
    Hsigned=2*signed_h if i==2 else s.zeros(1,6)
    Hraw=int(KK[i].det())*Hsigned*f.ext(Q[i].inv(),5)
    ck(f'geometric coefficient-two transport {i}',Hraw==s.Matrix(prior['cap_homotopy_rows'][str(i)]))
    ck(f'cap top-cell degree {i}',f.je(i,6)[0,0]==f.eps[i]*f.mult[i])
    cap_adapters[i]={'Q':Q[i].tolist(),'K':KK[i].tolist(),'signed_monodromy':RR[i].tolist(),
                     'signed_polyhedral_top_row':signed_h.tolist(),'transported_top_row':transported_h.tolist(),
                     'transported_cap_homotopy':Hraw.tolist()}

# Exact noncommutative telescoping formula underlying H_Q in every degree.
# Words retain factor order; the boundary of the degree-two A factor has the
# signs that cancel the (-1)^(r-1) in the displayed chain homotopy.
for k in range(1,7):
    expr={}
    for r in range(k):
        plus=tuple(['C']*(r+1)+['L']*(k-r-1))
        minus=tuple(['C']*r+['L']*(k-r))
        expr[plus]=expr.get(plus,0)+1
        expr[minus]=expr.get(minus,0)-1
    expr={w:a for w,a in expr.items() if a}
    ck(f'exact Pontryagin telescoping boundary degree {k}',expr=={tuple(['C']*k):1,tuple(['L']*k):-1})

def reduceword(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)

def wordW(w,k):
    a=s.eye(f.n(6,k))
    for g in w:a=a*(f.W[abs(g),k] if g>0 else f.W[abs(g),k].inv())
    return a

def addexpr(dst,src,scale=1,left=()):
    for (w,i),a in src.items():
        key=(reduceword(left+w),i)
        dst[key]=dst.get(key,s.zeros(*a.shape))+scale*a
    return {key:a for key,a in dst.items() if a!=s.zeros(*a.shape)}

def Kword(w,k):
    out={}
    for pos,g in enumerate(w):
        pref=reduceword(w[:pos]);suff=wordW(w[pos+1:],k)
        if g>0:key=(pref,g);a=suff
        else:key=(reduceword(pref+(g,)),-g);a=-f.W[-g,k].inv()*suff
        out=addexpr(out,{key:a})
    return out

g0=(-2,-1);t1=(-1,);t2=g0
word_records={}
for k in range(7):
    n=f.n(6,k)
    W0=wordW(g0,k)
    ck(f'actual inverse word source {k}',W0==f.W[0,k])
    # Delta_fibre = -K1 W_(g1^-1) - K2 W_g0 - K_g0.
    lhs={((),1):-wordW(t1,k),((),2):-W0}
    lhs=addexpr(lhs,Kword(g0,k),-1)
    # d R_fibre = (M1-I)K_(g1^-1)+(M2-I)K_g0.
    rhs={}
    rhs=addexpr(rhs,Kword(t1,k),left=(1,))
    rhs=addexpr(rhs,Kword(t1,k),-1)
    rhs=addexpr(rhs,Kword(t2,k),left=(2,))
    rhs=addexpr(rhs,Kword(t2,k),-1)
    ck(f'exact free-word cusp homotopy fibre identity {k}',addexpr(lhs,rhs,-1)=={})
    ck(f'actual inverse word boundary identity {k}',-(f.W[1,k]-s.eye(n))*f.W[2,k]*W0-(f.W[2,k]-s.eye(n))*W0==W0-s.eye(n))
    word_records[k]={'K_g0':[{'left_word':list(w),'generator':i,'right_matrix':a.tolist()} for (w,i),a in Kword(g0,k).items()]}

# Exact integral triangle data for every column used in the all-degree H_Q.
triangle_data={}
for i in (1,2):
    columns=[]
    for col in range(6):
        v=Q[i][:,col];p=s.zeros(6,1);tri=[]
        for j in range(6):
            q=p.copy();q[j]+=v[j]
            if s.Matrix.hstack(p,q).rank()==2:
                tri.append([[0]*6,list(p),list(q)])
            p=q
        ck(f'triangle lattice path endpoint {i},{col}',p==v)
        columns.append({'column_0based':col,'v':list(v),'A_v_oriented_triangles':tri})
    triangle_data[i]={'columns':columns,'degree_5_override':{'delta':int(Q[i].det()),'Q_inverse':Q[i].inv().tolist(),'J':J.tolist()},
                     'all_degree_rule':'H_Q(e_I)=sum_r (-1)^(r-1) C(q_i1)*...*C(q_i(r-1))*A_qir*l_qi(r+1)*...*l_qik; degree5 replaced by delta*(J e_I)^t floor(Q^-1 x); degrees0,6 are zero.'}

X=f.ext(f.S,5)[:,[2,1,0]]
cov=J*X
ck('actual three cusp primitive covectors',all(s.gcd_list(list(cov[:,j]))==1 for j in range(3)))
ck('actual three cusp invariant covectors',f.M[0].inv().T*cov==cov)
ck('actual six-dimensional fibre orientation',f.M[0].det()==f.M[1].det()==f.M[2].det()==1)

report={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'scope':'Post-reading exact finite-cap transports, explicit integral triangle data, all-degree free-word homotopy equations, and cusp invariant covectors. The geometric chain proof is GEOMETRIC_COMPARISON_02.md.',
 'checks_count':len(checks),'checks':checks,'finite_cap_adapters':cap_adapters,
 'triangle_chain_data':triangle_data,'free_word_homotopy_data':word_records,
 'actual_cusp_fivevectors':X.tolist(),'actual_cusp_covectors':cov.tolist(),
 'source_hashes':{str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE.parent/'derive_chain.py',HERE/'top_chain_adapter.json']}}
(HERE/'geometric_diagram_check_02.json').write_text(json.dumps(report,indent=2,default=int)+'\n')
print(json.dumps({'utc':report['utc'],'status':report['status'],'checks_count':len(checks),'scope':report['scope']},indent=2))
