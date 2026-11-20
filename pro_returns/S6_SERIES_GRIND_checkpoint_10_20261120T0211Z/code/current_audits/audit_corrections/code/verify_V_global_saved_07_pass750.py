"""Saved-output verifier and explicit low-degree bridge for P1.12/P1.19.

The global homology verification does not run Smith reduction again: it
checks the saved integral inverse/cycle/incoming certificates, and proves
the outgoing ranks by exact finite-field lower bounds plus the displayed
integral kernels. Local boundary/complement Smith reductions construct
the otherwise missing bases for the homology maps.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import sympy as s, json, hashlib, time
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

start=time.monotonic(); checks=[]
def ck(name,val):
    if not bool(val): raise AssertionError(name)
    checks.append({'name':name,'pass':True})
def mat(M): return [[int(x) for x in M.row(i)] for i in range(M.rows)]
def readmat(x,r,c):
    ck('saved matrix dimensions '+str((r,c)),len(x)==r and all(len(row)==c for row in x))
    ck('saved entries are integers '+str((r,c)),all(type(v) is int for row in x for v in row))
    return s.Matrix(r,c,[v for row in x for v in row])
def unitinverse(M,name):
    I=M.inv(method='DM') if M.rows else s.zeros(0)
    ck(name+' integral inverse',all(x.q==1 for x in I))
    ck(name+' exact inverse products',M*I==s.eye(M.rows) and I*M==s.eye(M.rows))
    return I
def modrank(M,p):
    return DomainMatrix.from_Matrix(M).convert_to(s.GF(p)).rank()
def snf(M,name):
    if not M.rows or not M.cols: return s.zeros(*M.shape),s.eye(M.rows),s.eye(M.cols)
    D,U,V=[x.to_Matrix() for x in smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(s.ZZ))]
    ck(name+' exact Smith equality',D==U*M*V)
    unitinverse(U,name+' left');unitinverse(V,name+' right')
    return D,U,V
def nr(D): return sum(D[i,i]!=0 for i in range(min(D.shape)))
def localH(ds,k,name):
    Do=ds[k];Di=ds[k+1];D,U,V=snf(Do,name+' outgoing');r=nr(D);Vi=unitinverse(V,name+' cycles');coords=Vi*Di
    ck(name+' incoming top zero',coords[:r,:]==s.zeros(r,Di.cols))
    DB,UB,VB=snf(coords[r:,:],name+' incoming');rb=nr(DB);UBi=unitinverse(UB,name+' homology')
    C=V[:,r:];F=C*UBi[:,rb:];P=UB[rb:,:]*Vi[r:,:]
    tors=[(j,abs(int(DB[j,j]))) for j in range(rb) if abs(DB[j,j])>1]
    return {'free':F,'proj':P,'cycles':C,'incoming_left_inverse':UBi,'torsion':tors,'rank':F.cols}
def solve(M,T,name):
    D,U,V=snf(M,name);r=nr(D);Z=U*T;ck(name+' zero residual',Z[r:,:]==s.zeros(Z.rows-r,Z.cols));X=s.zeros(M.cols,T.cols)
    for i in range(r):
        for j in range(T.cols):
            q=s.Rational(Z[i,j],D[i,i]);ck(name+' integral division '+str((i,j)),q.q==1);X[i,j]=q
    X=V*X;ck(name+' actual solved equality',M*X==T);return X

root=Path(__file__).parent
source=root/'reconstruct_V_global_06.json'; data=json.loads(source.read_text())
gdim=[4,26,87,162,200,156,79,23,3]
ydim=[3,22,71,132,155,118,57,16,2]
bdim=[1,7,21,35,35,21,7,1,0]
cdim=[1,3,9,9,10,3,1,0,0]
gd=[readmat(data['global_differentials'][str(k)],gdim[k-1] if k else 0,gdim[k]) for k in range(9)]
yd=[readmat(data['Y_differentials'][str(k)],ydim[k-1] if k else 0,ydim[k]) for k in range(9)]
bd=[readmat(data['boundary_differentials'][str(k)],bdim[k-1] if k else 0,bdim[k]) for k in range(9)]
jy=[readmat(data['jY'][str(k)],ydim[k],bdim[k]) for k in range(9)]
kap=[readmat(data['kappa'][str(k)],cdim[k],len(list(combinations(range(6),k)))) for k in range(9)]
psi=readmat(data['psi'],1,10);e=readmat(data['e'],10,1);K=readmat(data['K'],10,9)
r=readmat(data['r'],1,35);t=readmat(data['t'],1,35);X=readmat(data['X'],35,9);T=readmat(data['T'],118,9)
ck('actual primitive psi and e',psi*kap[4]==s.zeros(1,15) and psi*e==s.ones(1))
ck('actual kernel basis psi K',psi*K==s.zeros(1,9));unitinverse(e.row_join(K),'actual [e,K]')
ck('torsion row relations',r*bd[5]==s.zeros(1,21) and 2*r==t*bd[4])
ck('torsion row is not an integral coboundary: mod2 obstruction',modrank(bd[4].T.row_join(r.T),2)>modrank(bd[4].T,2))
f0=[kap[k].row_join(s.zeros(cdim[k],bdim[k]-kap[k].cols)) for k in range(9)]
ck('actual secondary cycles and nullchains',bd[4]*X==s.zeros(35,9) and yd[5]*T==jy[4]*X and f0[4]*X==K and r*X==s.zeros(1,9))
fc=[m.copy() for m in f0];fc[4]+=e*r
for k in range(1,9):
    ck('saved global actual mapping cone '+str(k),
       gd[k]==s.BlockMatrix([[yd[k],s.zeros(ydim[k-1],cdim[k]),jy[k-1]],
                             [s.zeros(cdim[k-1],ydim[k]),s.zeros(cdim[k-1],cdim[k]),fc[k-1]],
                             [s.zeros(bdim[k-2] if k>=2 else 0,ydim[k]),s.zeros(bdim[k-2] if k>=2 else 0,cdim[k]),-bd[k-1]]]).as_explicit())

homology={}
for k,n in enumerate(gdim):
    h=data['global_certificates'][str(k)];out=h['outgoing_rank'];inc=h['incoming_rank'];nh=h['rank'];nxt=gdim[k+1] if k<8 else 0
    D=gd[k];Di=gd[k+1] if k<8 else s.zeros(n,0)
    V=readmat(h['outgoing_right'],n,n);Vi=readmat(h['outgoing_right_inverse'],n,n)
    ck('global saved inverse '+str(k),V*Vi==s.eye(n) and Vi*V==s.eye(n))
    DV=D*V
    ck('global exact integral kernel '+str(k),DV[:,out:]==s.zeros(D.rows,n-out))
    ck('global independent rank lower bound modulo 1009 '+str(k),modrank(DV[:,:out],1009)==out)
    C=readmat(h['cycles'],n,n-out);ck('global displayed cycle basis '+str(k),C==V[:,out:])
    incoming=Vi*Di
    ck('global incoming cycle equality '+str(k),incoming[:out,:]==s.zeros(out,nxt))
    B=readmat(h['incoming'],n-out,nxt);ck('global saved incoming coordinates '+str(k),B==incoming[out:,:])
    DB=readmat(h['incoming_smith'],n-out,nxt);U=readmat(h['incoming_left'],n-out,n-out);W=readmat(h['incoming_right'],nxt,nxt)
    Ui=unitinverse(U,'global incoming left '+str(k));unitinverse(W,'global incoming right '+str(k))
    ck('global incoming Smith equality '+str(k),DB==U*B*W)
    ck('global incoming unit factors and zero complement '+str(k),DB==s.Matrix(n-out,nxt,lambda i,j:(DB[i,i] if i==j and i<inc else 0)) and all(abs(DB[i,i])==1 for i in range(inc)))
    ck('global free rank formula '+str(k),nh==n-out-inc)
    F=readmat(h['free'],n,nh);P=readmat(h['proj'],nh,n)
    ck('global free lift and projection '+str(k),F==C*Ui[:,inc:] and P==U[inc:,:]*Vi[out:,:] and P*F==s.eye(nh))
    homology[str(k)]={'rank':nh,'torsion':[],'outgoing_rank':out,'incoming_rank':inc}
ck('all saved global homology groups',[homology[str(k)]['rank'] for k in range(9)]==[1,0,0,0,4,0,0,0,1])

bridges={}
for k in range(1,5):
    HB=localH(bd,k,'boundary H'+str(k));HY=localH(yd,k,'complement H'+str(k))
    JY=HY['proj']*jy[k]*HB['free'];JC=f0[k]*HB['free'];J=JY.col_join(JC)
    if k<=3:
        ck('combined actual homology map unimodular '+str(k),J.rows==J.cols and abs(J.det())==1)
        DJ,UY,VY=snf(JY,'surjection jY H'+str(k));ry=nr(DJ)
        ck('jY actual integral surjection '+str(k),ry==HY['rank'] and all(abs(DJ[i,i])==1 for i in range(ry)))
        item={'HB_free':mat(HB['free']),'HY_projection':mat(HY['proj']),'jY_homology':mat(JY),'jC_homology':mat(JC),'joint_homology':mat(J),'joint_det':int(J.det()),'boundary_torsion':HB['torsion']}
        if k in [2,3]:
            kernel=VY[:,ry:]
            fibre=s.eye(bdim[k])[:,:kap[k].cols]
            Q=solve(HB['proj']*fibre,kernel,'vertical kernel lift H'+str(k))
            Ck=kap[k]*Q
            ck('vertical kernel collapses unimodularly '+str(k),Ck.rows==9 and Ck.cols==9 and abs(Ck.det())==1)
            item.update({'kernel_free_coordinates':mat(kernel),'vertical_kernel_cycles':mat(Q),'kernel_collapse':mat(Ck),'kernel_collapse_det':int(Ck.det())})
        if k==3:
            ck('actual H3 boundary torsion Z2',HB['torsion'] and [v for _,v in HB['torsion']]==[2])
            j=HB['torsion'][0][0];tors=HB['cycles']*HB['incoming_left_inverse'][:,j]
            ck('torsion generator lies in fibre',tors[kap[k].cols:,:]==s.zeros(bdim[k]-kap[k].cols,1))
            ck('torsion generator collapses to zero',f0[k]*tors==s.zeros(cdim[k],1))
            item['torsion_cycle']=mat(tors)
        bridges[str(k)]=item
    else:
        old=readmat(data['j4'],22,18)
        ck('j4 basis reconstruction exact',J==old)
        W=readmat(data['W'],18,9)
        ck('j4 lifts and source cycle matrix exact',J*W==s.zeros(12,9).col_join(K) and HB['free']*W==X)
        DJ,UJ,VJ=snf(J,'degree4 homology gluing')
        ck('j4 primitive rank18',nr(DJ)==18 and all(abs(DJ[i,i])==1 for i in range(18)))
        # Record the exact actual cokernel coordinates; a further unimodular
        # row adapter sends its primitive image to the fourth coordinate.
        quotient=UJ[18:,:];Cmap=quotient[:,12:]
        ck('cusp-to-global quotient factors through actual psi',Cmap==Cmap*e*psi)
        v=Cmap*e;DV,UV,VV=snf(v,'cusp quotient primitive vector')
        ck('cusp quotient generator primitive',nr(DV)==1 and abs(DV[0,0])==1)
        P=s.eye(4);P.row_swap(0,3)
        adapter=P*UV
        sign=int((adapter*v)[3]);adapter[3,:]*=sign
        ck('actual cokernel adapter to fourth row psi',adapter*Cmap==s.zeros(3,10).col_join(psi))
        bridges['4']={'HB_free':mat(HB['free']),'HY_projection':mat(HY['proj']),'j4':mat(J),'j4_smith':mat(DJ),'j4_left':mat(UJ),'j4_right':mat(VJ),'raw_cokernel_projection':mat(quotient),'cokernel_adapter':mat(adapter),'adapted_cokernel_projection':mat(adapter*quotient)}

out={'status':'PASS','actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)',
     'utc':datetime.now(timezone.utc).isoformat(),'assertions':len(checks),'seconds':time.monotonic()-start,'checks':checks,
     'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'homology':homology,'homology_basis_bridges':bridges,
     'scope':'Saved global certificate checked using exact integral inverse/kernel/incoming products and modular rank witnesses, plus newly reconstructed actual P1.12 low-degree kernel cycles and degree-four j4/cokernel basis adapter. This is a different verification of saved matrices in the same model family, after reading the full receiving proofs; no blind or cross-model claim.'}
outpath=Path(__file__).with_suffix('.json');tmp=outpath.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2));tmp.replace(outpath)
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','source_sha256','input_sha256']}))
