#!/usr/bin/env python3
"""Fresh LS OS45 computation: raw periods, actual cap maps, full integral bar.

The only mathematical input file is the authorized raw defining fixture.
No LS original, old packet, historical target program, or old output is read.
The generic tracked Euclidean Smith helper is reused from this lane's
new LJ program; the OS45 vertical and full bar computation is new.
"""
from pathlib import Path
from datetime import datetime, timezone
from functools import reduce
from math import gcd
import hashlib
import json
import sympy as S

W = Path(__file__).resolve().parents[1]
LANE = W / "agents/continuation7_iii_vertical_correction"
LANE.mkdir(exist_ok=True)
RAW = W / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
data = json.loads(RAW.read_text())
row = next(r for r in data["rows"] if r["OS"] == 45 and r["profile"] == "default")
PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
I4, I6 = S.eye(4), S.eye(6)
J = S.Matrix([[0,1],[-1,0]])

def ints(M):
    assert all(S.denom(x) == 1 for x in M)
    return M

def sparse(M):
    ints(M)
    return {"shape": list(M.shape),
            "entries": [[i,j,int(M[i,j])] for i in range(M.rows)
                        for j in range(M.cols) if M[i,j]]}

def emit(label, value):
    print(label+"="+json.dumps(value, sort_keys=True, separators=(",",":")), flush=True)

def bezout(a,b):
    r0,r1,x0,x1,y0,y1 = a,b,1,0,0,1
    while r1:
        q = r0//r1
        r0,r1,x0,x1,y0,y1 = r1,r0-q*r1,x1,x0-q*x1,y1,y0-q*y1
    sign = 1 if r0 >= 0 else -1
    return sign*r0,sign*x0,sign*y0

def smith(A):
    M,U,V = S.Matrix(A), S.eye(A.rows), S.eye(A.cols)
    for k in range(min(A.shape)):
        nonzero = [(abs(M[i,j]),i,j) for i in range(k,M.rows)
                   for j in range(k,M.cols) if M[i,j]]
        if not nonzero:
            break
        _,i,j = min(nonzero)
        M.row_swap(k,i); U.row_swap(k,i)
        M.col_swap(k,j); V.col_swap(k,j)
        while True:
            for i in range(k+1,M.rows):
                if M[i,k]:
                    q = M[i,k]//M[k,k]
                    M[i,:] -= q*M[k,:]; U[i,:] -= q*U[k,:]
                    if M[i,k]:
                        M.row_swap(k,i); U.row_swap(k,i)
                    break
            else:
                for j in range(k+1,M.cols):
                    if M[k,j]:
                        q = M[k,j]//M[k,k]
                        M[:,j] -= q*M[:,k]; V[:,j] -= q*V[:,k]
                        if M[k,j]:
                            M.col_swap(k,j); V.col_swap(k,j)
                        break
                else:
                    bad = next(((i,j) for i in range(k+1,M.rows)
                                for j in range(k+1,M.cols)
                                if M[i,j] % M[k,k]), None)
                    if bad is None:
                        break
                    M[k,:] += M[bad[0],:]; U[k,:] += U[bad[0],:]
        if M[k,k] < 0:
            M[k,:] = -M[k,:]; U[k,:] = -U[k,:]
    assert U*A*V == M
    assert abs(U.det()) == abs(V.det()) == 1
    Ui,Vi = ints(U.inv()),ints(V.inv())
    assert all(not M[i,j] for i in range(M.rows)
               for j in range(M.cols) if i != j)
    ds = [int(M[i,i]) for i in range(min(M.shape)) if M[i,i]]
    assert all(y % x == 0 for x,y in zip(ds,ds[1:]))
    return M,U,V,Ui,Vi,ds

def factor_record(result):
    D,U,V,Ui,Vi,ds = result
    return {"D":sparse(D),"U":sparse(U),"V":sparse(V),
            "U_inverse":sparse(Ui),"V_inverse":sparse(Vi),
            "nonzero_diagonal":ds}

def solve_from_factor(A,B,result):
    D,U,V,Ui,Vi,ds = result
    UB=U*B
    X0=S.zeros(A.cols,B.cols)
    for i in range(A.rows):
        d=D[i,i] if i<A.cols else 0
        if d:
            for j in range(B.cols):
                assert UB[i,j] % d == 0
                X0[i,j]=UB[i,j]//d
        else:
            assert UB[i,:] == S.zeros(1,B.cols)
    X=V*X0
    assert A*X==B
    return X

def wedge(u,v):
    return S.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in PAIRS])

def exterior(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in PAIRS] for i,j in PAIRS])

def p(u,v):
    return S.Matrix([u[i]*v[j] for i,j in PAIRS])

def multiply(g,h):
    x,z=g; y,w=h
    return x+y,z+w+p(x,y)

def inverse(g):
    x,z=g
    return -x,-z+p(x,x)

def power(g,n):
    if n < 0:
        g=inverse(g); n=-n
    ans=(S.zeros(4,1),S.zeros(6,1))
    while n:
        if n & 1:
            ans=multiply(ans,g)
        g=multiply(g,g); n//=2
    return ans

def f_word(A,x):
    """Lift ordered signed basis-generator words in the actual central group."""
    out=(S.zeros(4,1),S.zeros(6,1))
    for i in range(4):
        out=multiply(out,power((A[:,i],S.zeros(6,1)),int(x[i])))
    assert out[0]==A*x
    canonical=sum((x[i]*x[j]*I6[:,k] for k,(i,j) in enumerate(PAIRS)),
                  S.zeros(6,1))
    return exterior(A)*canonical-out[1]

def f_poly(A,x):
    B=exterior(A)
    def DA(i,j):
        return p(A[:,i],A[:,j])-B*p(I4[:,i],I4[:,j])
    out=S.zeros(6,1)
    for i in range(4):
        out-=x[i]*(x[i]-1)//2*DA(i,i)
        for j in range(i+1,4):
            assert DA(i,j)==DA(j,i)
            out-=x[i]*x[j]*DA(i,j)
    assert out==f_word(A,x)
    return out

def local_raw(A,g):
    N=A-S.eye(2)
    nu=reduce(gcd,(abs(int(x)) for x in N),0)
    col=next(N[:,j] for j in range(2) if N[:,j]!=S.zeros(2,1))
    u=col/reduce(gcd,(abs(int(x)) for x in col),0)
    if next(x for x in u if x)<0:
        u=-u
    assert N==nu*u*(u.T*J)
    one,x,y=bezout(int(u[0]),int(u[1])); assert one==1
    v=S.Matrix([-y,x])
    kap=next(g[i]/u[i] for i in range(2) if u[i])
    assert S.denom(kap)==1 and g==kap*u
    return nu,u,v,int(kap)

def lift(u):
    return S.Matrix([u[0],u[1],0,0])

def vertical(n,p0,q0):
    p0%=n; q0%=n
    C=S.zeros(n,n)
    for i in range(n):
        C[i,i]-=2; C[i,(i-1)%n]+=1; C[i,(i+1)%n]+=1
    perm=[(i+q0)%n for i in range(n)]
    Sm=S.Matrix([[int(j==perm[i]) for j in range(n)] for i in range(n)])
    mp=S.eye(n)[:,p0]-S.eye(n)[:,0]
    if not p0 or not q0:
        d=S.zeros(n,1); m=mp
    else:
        g=gcd(n,q0); ell=n//g
        assert p0 % ell==0 and g>1
        m=S.Matrix([(p0//ell)*(int(i%g==1)-int(i%g==0)) for i in range(n)])
        h=m-mp
        assert sum(h)==0 and sum(i*h[i] for i in range(n))%n==0
        r0=-sum((n-1-i)*h[i] for i in range(n))/n
        ints(S.Matrix([r0]))
        r=[r0+sum(h[j] for j in range(i)) for i in range(n)]
        d=S.Matrix([sum(r[k] for k in range(1,i+1)) for i in range(n)])
    assert C*d==m-mp and Sm*m==m and C*Sm==Sm*C
    fq=S.zeros(n,1)
    fq[1:,0]=C[1:,1:].inv()*(S.eye(n)[:,q0]-S.eye(n)[:,0])[1:,0]
    assert C*fq==S.eye(n)[:,q0]-S.eye(n)[:,0]
    assert (m.T*fq)[0]==0 and d[q0]-d[0]==-fq[p0]
    return {"physical_P":p0,"physical_Q":q0,"pullback_permutation":perm,
            "C":sparse(C),"S":sparse(Sm),"d":[int(x) for x in d],
            "multidegree":[int(x) for x in m],
            "raw_d":[int(d[(-j)%n]) for j in range(n)],
            "height_inverse":[str(x) for x in fq],
            "mixed_correction":str(-fq[p0])}

print("START",datetime.now(timezone.utc).isoformat(),flush=True)
print("RAW_SHA256",hashlib.sha256(RAW.read_bytes()).hexdigest(),flush=True)
emit("RAW_OS45",row)
ALL=[]
for a,b in [(2,4),(4,2)]:
    vr=vertical(8,-3*a,-3*b); emit("VERTICAL",{"a":a,"b":b,**vr})
    for zero in range(1,5):
        print("\nGEOMETRY",a,b,zero,flush=True)
        Ts=[]; locals_=[]; vanishing=[]
        for i,(aa,gg) in enumerate(zip(row["elliptic_matrices"],row["generator_section_cocycle"])):
            A,g=S.Matrix(aa),S.Matrix(gg)
            nu,u,v,kap=local_raw(A,g)
            beta=-a*g.T*J*A
            x=S.Rational(b*kap,nu)*v
            c=(beta*x)[0]+int(i==zero)
            T=S.zeros(4,4); T[:2,:2]=A; T[:2,3]=b*g
            T[2,:2]=beta; T[2,2]=1; T[2,3]=c; T[3,3]=1
            ints(T); assert T.det()==1
            Ti=ints(T.inv()); assert T*Ti==I4
            short=lift(u).row_join(I4[:,2]); long=lift(v).row_join(I4[:,3])
            if i==zero:
                C=S.Matrix([[nu,b*kap],[-a*kap,c]])
                assert C.det()==1
                H=S.Matrix.hstack(short*C[:,0],long[:,0],short*C[:,1],long[:,1])
                model=I4.copy(); model[0,1]=1; model[2,3]=1
                Q1=S.Matrix([[0,1,0,0],[0,0,0,1]])
                Q2=S.Matrix([[1,0,0,0,0,0],[0,0,1,-1,0,0],
                             [0,0,0,0,1,0],[0,0,0,0,0,1]])
                Eker=S.Matrix.hstack(I6[:,1],I6[:,2]+I6[:,3])
                pre=S.Matrix.hstack(I6[:,3],I6[:,4]-I6[:,3])
                fixed=H[:,[0,2]]
                vanishing.extend([H[:,0],H[:,2]])
                extra={"kind":"primitive_cusp","C":sparse(C),"C_inverse":sparse(C.inv())}
            else:
                d0=gcd(nu,a*kap); n0=nu//d0; A0=a*kap//d0
                one,theta,sigma=bezout(n0,A0); assert one==1
                B0=S.Rational(b*kap,n0); assert S.denom(B0)==1
                one,xx,yy=bezout(d0,int(B0)); assert one==1
                CS=S.Matrix([[n0,sigma],[-A0,theta]])
                CL=S.Matrix([[xx,-B0],[yy,d0]])
                assert CS.det()==CL.det()==1
                H=S.Matrix.hstack(short*CS[:,0],long*CL[:,0],
                                  short*CS[:,1],long*CL[:,1])
                model=I4.copy(); model[0,1]=1
                Q1=S.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1]])
                Q2=I6[[0,3,4,5],:]
                Eker=S.Matrix.hstack(I6[:,1],I6[:,2])
                pre=S.Matrix.hstack(I6[:,3],I6[:,4])
                fixed=H[:,[0,2,3]]
                vanishing.append(H[:,0])
                extra={"kind":"primitive_rank_one","d0":d0,"n0":n0,
                       "CS":sparse(CS),"CS_inverse":sparse(CS.inv()),
                       "CL":sparse(CL),"CL_inverse":sparse(CL.inv())}
            Hi=ints(H.inv()); assert H.det()==1 and Hi*T*H==model
            WH=exterior(H); f1=Q1*Hi; f2=Q2*exterior(Hi)
            sec1=H*Q1.T
            sec2=WH*S.Matrix.hstack(I6[:,0],I6[:,2] if i==zero else I6[:,3],
                                   I6[:,4],I6[:,5])
            ker=WH*Eker
            assert f1*sec1==S.eye(f1.rows) and f2*sec2==S.eye(4)
            assert f2*ker==S.zeros(4,2)
            assert (exterior(T)-I6)*WH*pre==ker
            assert (T-I4)*fixed==S.zeros(4,fixed.cols)
            local={"site":i,"nu":nu,"kappa":kap,"u":list(map(int,u)),
                   "v":list(map(int,v)),"T":sparse(T),"T_inverse":sparse(Ti),
                   "H":sparse(H),"H_inverse":sparse(Hi),
                   "f1":sparse(f1),"f1_section":sparse(sec1),
                   "f2":sparse(f2),"f2_section":sparse(sec2),
                   "fibre_kernel":sparse(ker),"kernel_preimage":sparse(WH*pre),
                   "fixed_basis":sparse(fixed),**extra}
            locals_.append((local,ker,fixed)); Ts.append(T); emit("LOCAL",local)
        prod=I4.copy()
        for T in Ts: prod=prod*T
        assert prod==I4
        R=S.Matrix.hstack(*[exterior(T)-I6 for T in Ts])
        Rfact=smith(R)
        DG=S.Matrix.hstack(*[T-I4 for T in Ts]); Gfact=smith(DG)
        _,_,GV,_,GVi,Gds=Gfact
        K=GV[:,len(Gds):]; Kinv=GVi[len(Gds):,:]
        assert DG*K==S.zeros(4,K.cols) and Kinv*K==S.eye(K.cols)
        suffix=[I4.copy() for _ in Ts]
        acc=I4.copy()
        for i in reversed(range(len(Ts))):
            suffix[i]=acc; acc=Ts[i]*acc
        Jlast=S.Matrix.vstack(*[-M for M in suffix])
        assert DG*Jlast==S.zeros(4,4)
        def c_last(x):
            return -sum((f_poly(Ts[i],suffix[i]*x) for i in range(5)),S.zeros(6,1))
        def c_last_actual(x):
            xx,zz=x,S.zeros(6,1)
            for T in Ts:
                xx=T.inv()*xx
                zz=exterior(T.inv())*(zz+f_word(T,xx))
            assert xx==x
            return -zz
        diff=S.Matrix.hstack(*[c_last_actual(I4[:,i])-c_last(I4[:,i]) for i in range(4)])
        diff_pre=solve_from_factor(R,diff,Rfact)
        zcols=[]
        for j in range(K.cols):
            k=K[:,j]; cur=S.zeros(4,1); z=S.zeros(6,1)
            for i,T in enumerate(Ts):
                u=k[4*i:4*i+4,0]; z+=f_poly(T,u)+p(u,-u)
                for vv in [T*u,-u]:
                    z-=p(cur,vv); cur+=vv
            assert cur==S.zeros(4,1); zcols.append(z)
        ZK=S.Matrix.hstack(*zcols)
        vanish=S.Matrix.hstack(*vanishing)[:3,:]
        vf=smith(vanish)
        van_inverse=solve_from_factor(vanish,S.eye(3),vf)
        global_data={"R":sparse(R),"R_smith":factor_record(Rfact),
                     "graph_D":sparse(DG),"graph_smith":factor_record(Gfact),
                     "K":sparse(K),"K_inverse":sparse(Kinv),
                     "bar_section_z":sparse(ZK),"J_last":sparse(Jlast),
                     "last_word_difference":sparse(diff),"difference_preimage":sparse(diff_pre),
                     "vanishing_nongamma":sparse(vanish),"vanishing_right_inverse":sparse(van_inverse)}
        emit("EXTERIOR",global_data)
        for e in [-1,1]:
            columns=[]; labels=[]
            for j in range(R.cols):
                columns.append(R[:,j].col_join(S.zeros(K.cols,1))); labels.append(["fibre_relation",j])
            normal=[]
            for i,(_,ker,fixed) in enumerate(locals_):
                for j in range(ker.cols):
                    columns.append(ker[:,j].col_join(S.zeros(K.cols,1))); labels.append(["cap_fibre",i,j])
                for j in range(fixed.cols):
                    u=fixed[:,j]; gg=S.zeros(20,1); gg[4*i:4*i+4,0]=u
                    kk=Kinv*gg; assert K*kk==gg
                    ff=f_poly(Ts[i],u)
                    col=ff.col_join(kk); columns.append(col); labels.append(["fixed_normal",i,j])
                    normal.append({"site":i,"u":list(map(int,u)),"f":list(map(int,ff)),"K":list(map(int,kk))})
            power_v=-e*I4[:,3]
            for j in range(4):
                u=I4[:,j]; gg=Jlast*u; kk=Kinv*gg; assert K*kk==gg
                ff=c_last(u)-wedge(u,power_v)
                columns.append(ff.col_join(kk)); labels.append(["ordinary_normal",j])
                normal.append({"site":"ordinary","u":list(map(int,u)),"f":list(map(int,ff)),"K":list(map(int,kk))})
            gg=Jlast*power_v
            columns.append(c_last(power_v).col_join(Kinv*gg)); labels.append(["ordinary_root"])
            B=S.Matrix.hstack(*columns); bf=smith(B)
            DD,UU,VV,UUi,VVi,ds=bf
            tors=[d for d in ds if d>1]
            free=B.rows-len(ds)
            # Five component discs after the ordinary filling:
            # quotient H1 has gamma and five base loops / (sum base + e gamma).
            disc=S.eye(6)[:,1:]
            ordinary=S.Matrix([e,1,1,1,1,1])
            disc_full=ordinary.row_join(disc)
            assert abs(disc_full.det())==1
            cert={"a":a,"b":b,"zero":zero,"e":e,"normal_columns":normal,
                  "column_labels":labels,"B":sparse(B),"B_smith":factor_record(bf),
                  "cokernel_free_rank":free,"torsion":tors,
                  "component_disc_matrix":sparse(disc_full),
                  "component_disc_inverse":sparse(disc_full.inv()),
                  "pi1_gamma_relation":e}
            emit("FULL_RESULT",cert)
            assert free==0 and tors==[b]
            ALL.append({"a":a,"b":b,"zero":zero,"e":e,"torsion":tors,
                        "H2_free":free,"H3_free":0,"pi1":"trivial",
                        "vertical":vr,"local_maps":[x[0] for x in locals_],
                        "exterior":global_data,"full":cert})
out=LANE/"S6_SERIES_PUBLISH_III_02LS_fresh_os45_data_v001.json"
out.write_text(json.dumps(ALL,indent=2,sort_keys=True)+"\n")
assert len(ALL)==16
emit("SUMMARY",[{"a":x["a"],"b":x["b"],"zero":x["zero"],"e":x["e"],
                 "H2":x["torsion"],"H2_free":x["H2_free"],
                 "H3_free":x["H3_free"],"pi1":x["pi1"]} for x in ALL])
print("DATA_SHA256",hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
print("COMPLETE",datetime.now(timezone.utc).isoformat(),flush=True)
