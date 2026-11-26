#!/usr/bin/env python3
"""Distinct LQ construction from raw profiles and explicit chain relations.

No LQ original, old packet, historical target code or target output is read.
All source attempts and streams are retained. Finite checks supplement the
unbounded proof; they are not its parameter justification.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
from fractions import Fraction
from datetime import datetime, timezone
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'agents/continuation7_iii_star_logs'
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
PAIRS = list(combinations(range(4), 2))
I4 = S.eye(4)
J = S.Matrix([[0, 1], [-1, 0]])


def egcd(a, b):
    if not b:
        return abs(a), (1 if a > 0 else -1 if a < 0 else 0), 0
    g, u, v = egcd(b, a % b)
    return g, v, u-(a//b)*v


def smith(M):
    """Integer row/column Euclidean operations, with both inverse markings."""
    A = S.MutableDenseMatrix(M)
    U, V = S.eye(A.rows), S.eye(A.cols)
    def rowadd(i, j, c):
        for B in (A, U):
            old = list(B.row(j))
            for h in range(B.cols):
                B[i, h] += c*old[h]
    def coladd(i, j, c):
        for B in (A, V):
            old = list(B.col(j))
            for h in range(B.rows):
                B[h, i] += c*old[h]
    for k in range(min(A.shape)):
        entries = [(abs(int(A[i,j])), i, j)
                   for i in range(k,A.rows) for j in range(k,A.cols) if A[i,j]]
        if not entries:
            break
        _, i, j = min(entries)
        A.row_swap(k,i); U.row_swap(k,i)
        A.col_swap(k,j); V.col_swap(k,j)
        while True:
            ii = next((i for i in range(k+1,A.rows) if A[i,k]), None)
            if ii is not None:
                rowadd(ii,k,-int(A[ii,k]//A[k,k]))
                if A[ii,k]:
                    A.row_swap(ii,k); U.row_swap(ii,k)
                continue
            jj = next((j for j in range(k+1,A.cols) if A[k,j]), None)
            if jj is not None:
                coladd(jj,k,-int(A[k,jj]//A[k,k]))
                if A[k,jj]:
                    A.col_swap(jj,k); V.col_swap(jj,k)
                continue
            bad = next(((i,j) for i in range(k+1,A.rows)
                        for j in range(k+1,A.cols) if A[i,j] % A[k,k]), None)
            if bad is None:
                break
            rowadd(k,bad[0],1)
        if A[k,k] < 0:
            A.row_op(k,lambda v,j:-v); U.row_op(k,lambda v,j:-v)
    assert U*M*V == A and abs(U.det()) == abs(V.det()) == 1
    d = [int(A[i,i]) for i in range(min(A.shape)) if A[i,i]]
    assert all(d[i+1] % d[i] == 0 for i in range(len(d)-1))
    assert all(A[i,j] == 0 for i in range(A.rows) for j in range(A.cols) if i != j)
    return d, U, V


def wedge(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in PAIRS] for i,j in PAIRS])


def ivec(v):
    assert all(x.q == 1 for x in v)
    return [int(x) for x in v]


def mat(A):
    return [ivec(A.row(i)) for i in range(A.rows)]


def rebuild(raw, selected, a, b):
    out=[]
    for i, kind in enumerate(raw['fibers']):
        E=S.Matrix(raw['elliptic_matrices'][i])
        g=S.Matrix(raw['generator_section_cocycle'][i])
        row=-a*g.T*J*E
        if kind.startswith('I') and kind[1:].isdigit():
            nu=int(kind[1:]); N=E-S.eye(2)
            col=next(N.col(j) for j in range(2) if N.col(j) != S.zeros(2,1))
            h=gcd(*ivec(col)); u=col/h
            if next(x for x in u if x) < 0:
                u=-u
            kap=next(g[j]/u[j] for j in range(2) if u[j])
            assert E-S.eye(2) == nu*u*u.T*J and g == kap*u
            c=(-a*b*kap**2+int(i==selected))/nu
        else:
            c=(row*b*(E-S.eye(2)).inv()*g)[0]
        A=S.eye(4); A[:2,:2]=E; A[:2,3]=b*g; A[2,:2]=row; A[2,3]=c
        mat(A)
        out.append(A)
    P=S.eye(4)
    for A in out:
        P=P*A
    assert P == S.eye(4)
    return out


def natural(raw):
    d=Fraction(raw['height_of_generator']).denominator
    for selected, kind in enumerate(raw['fibers']):
        if not (kind.startswith('I') and kind[1:].isdigit()):
            continue
        nu=int(kind[1:]); ab=d//nu
        for a in range(1,ab+1):
            if ab % a:
                continue
            b=ab//a
            if gcd(a,b)!=1:
                continue
            okay=True
            for i, component in enumerate(raw['component_coordinates']):
                for mod, residue in zip(component['moduli'],component['rows']):
                    v=residue[0]
                    p,q=a*v % mod,b*v % mod
                    if i==selected:
                        okay &= gcd(q,mod)==1
                        okay &= all(int(j==p)-int(j==0)-int(j==(p-q)%mod)+int(j==(-q)%mod)
                                    == -2*int(j==0)+int(j==1%mod)+int(j==(-1)%mod)
                                    for j in range(mod))
                    else:
                        okay &= p==0 or q==0
            if okay:
                yield selected,a,b


def catalogue():
    result=[]
    for raw in json.loads(RAW.read_text())['rows']:
        if raw['OS'] not in (46,50):
            continue
        for selected,a,b in natural(raw):
            if b % 4:
                continue
            star=next(i for i,f in enumerate(raw['fibers']) if f in ('I1*','I3*'))
            n=int(raw['fibers'][star][1:-1]); matrices=rebuild(raw,selected,a,b)
            alpha=S.Matrix([2,0,a,0]); lam=S.Matrix([1,0,(a+1)//2,0])
            beta=S.Matrix([0,1,0,0])+(2*a-n*(a+1)//2)*lam
            ell=S.Matrix([0,b//2,0,1])+(-3*b//4 if n==1 else -b//4)*lam
            H=S.Matrix.hstack(alpha,beta,lam,ell)
            if raw['profile']=='II' and raw['OS']==50:
                C=S.eye(4); C[:2,:2]=S.Matrix([[1,1],[-1,0]])
                H=C*H
            target=S.Matrix([[-1,0,-1,0],[0,-1,0,0],[0,-n,1,0],[0,0,0,1]])
            assert H.det()==1 and H.inv()*matrices[star]*H==target
            assert H*S.Matrix([-1,0,2,0])==S.Matrix([0,0,1,0]) and H[3,3]==1
            omega=S.Matrix([[a,0,0,0,0,-b]])
            WH=wedge(H)
            w=S.Matrix([0,0,0,0,1,(n-1)//2])
            assert (omega*WH*S.Matrix([0,0,0,1,0,0]))[0]==-a
            assert (omega*WH*w)[0]==b//4
            relation=S.Matrix.hstack(*(wedge(A)-S.eye(6) for A in matrices))
            ds,Ur,Vr=smith(relation)
            assert ds==[1]*5 and omega*relation==S.zeros(1,relation.cols)
            G=S.Matrix.hstack(*(A-S.eye(4) for A in matrices[:-1]))
            dg,Ug,Vg=smith(G); assert dg==[1]*3
            K=Vg[:,3:]; Ki=Vg.inv()[3:,:]
            blocks=[]; offset=0; delta_relation=[]
            for i,A in enumerate(matrices):
                da,Ua,Va=smith(A-S.eye(4)); F=Va[:,len(da):]
                Fi=Va.inv()[len(da):,:]
                Ji=S.zeros(G.cols,4)
                if i<len(matrices)-1:
                    Ji[4*i:4*i+4,:]=S.eye(4)
                else:
                    suffix=S.eye(4)
                    for h in reversed(range(len(matrices)-1)):
                        Ji[4*h:4*h+4,:]=-suffix
                        suffix=matrices[h]*suffix
                assert G*Ji*F==S.zeros(4,F.cols)
                blocks.append(Ji*F)
                delta_relation+=ivec(Fi*S.Matrix([0,0,1,0]))
            normal=S.Matrix.hstack(*blocks)
            coords=Ki*normal
            dn,Un,Vn=smith(coords)
            assert dn==[1]*K.cols and normal*S.Matrix(delta_relation)==S.zeros(G.cols,1)
            assert normal.cols==K.cols+1 and gcd(*delta_relation)==1
            name=f"OS{raw['OS']}/{raw['profile']}:zero{selected+1}:({a},{b})"
            entry={'name':name,'n':n,'H':mat(H),'H_inverse':mat(H.inv()),
                   'matrices':[mat(A) for A in matrices], 'omega':mat(omega),
                   'wedge_relation_U':mat(Ur),'wedge_relation_V':mat(Vr),
                   'graph_K':mat(K),'graph_K_inverse':mat(Ki),
                   'normal_columns':mat(normal),'normal_U':mat(Un),'normal_V':mat(Vn),
                   'delta_relation':delta_relation}
            result.append(entry)
            print('ROW',name,'n',n,'H',mat(H),'inverse',mat(H.inv()),'graph_rank',K.cols,flush=True)
    assert len(result)==12 and sum(r['n']==1 for r in result)==8
    return result


def normalization(q,j):
    sig=lambda i:(j-i)%q
    orbits=[]; owner={}
    for i in range(q):
        if i not in owner:
            O=sorted({i,sig(i)}); z=len(orbits); orbits.append(O)
            for v in O: owner[v]=z
    fixed=[z for z,O in enumerate(orbits) if len(O)==1]
    f=len(fixed); rho=len(orbits)
    # Each component contributes F and sigma. Each edge orbit contributes D;
    # each half-edge orbit contributes its literal conductor column.
    edges=[]; edge_owner={}
    for i in range(q):
        if i not in edge_owner:
            O=sorted({i,(j-i-1)%q}); z=len(edges); edges.append(O)
            for v in O: edge_owner[v]=z
    half_orbits=[]; seen=set()
    for i in range(q):
        for sign in (-1,1):
            h=(i,sign)
            if h in seen: continue
            O={h,(sig(i),-sign)}; seen|=O; half_orbits.append(O)
    C=S.zeros(2*rho+len(edges),len(half_orbits))
    for col,O in enumerate(half_orbits):
        i,sign=min(O); v=owner[i]; edge=i if sign==1 else (i-1)%q
        z=edge_owner[edge]
        if len(orbits[v])==1:
            C[2*v,col]=-1; C[2*v+1,col]=2
        else:
            C[2*v+1,col]=1
        C[2*rho+z,col]=-2 if len(edges[z])==1 else -1
    d,U,V=smith(C)
    assert len(d)==C.cols and C.rows-len(d)==rho+1
    assert [x for x in d if x>1]==([2] if f==0 else [])
    return f,rho,mat(C),mat(U),mat(V)


def finite_checks():
    counts={0:0,1:0,2:0}; norms=[]; global_count=0
    for n in (1,3):
        for k in range(1,9):
            q=n*k
            for j in range(-2,3):
                f,rho,C,U,V=normalization(q,j)
                assert f==(1 if k%2 else 2 if j%2==0 else 0)
                norms.append({'n':n,'k':k,'j':j,'f':f,'rho':rho,'C':C,'U':U,'V':V})
                for r in (-2,0,3):
                    R=2*r-j
                    for N in (-5,-3,-1,1,3,5):
                        if gcd(N,2*k)!=1: continue
                        counts[f]+=1
                        # Exact local surjection and its explicit inverse columns.
                        if f in (1,2):
                            h=k if f==1 else k//2
                            dN=2*N if f==1 else N
                            dR=R if f==1 else R//2
                            g,p,t=egcd(h,dN); assert g==1
                            assert -h*(-p)+dN*t==1
                        else:
                            g,p,t=egcd(k,N); assert g==1
                            twice=S.Matrix([-2*p,t,0])
                            Y=-S.Matrix([0,0,1])+((1-R)//2)*twice
                            coeff=S.Matrix([[-k,2*N,-R]])
                            assert (coeff*twice)[0]==2 and (coeff*Y)[0]==1
                            assert int(Y[0])%2==0
                            tau=S.Matrix([1,0,0])+k*Y
                            assert (coeff*tau)[0]==0 and int(tau[0])%2==1
                        for e in (-2,0,3):
                            s=N-2*k*e
                            assert s%2 and s and gcd(s,2*k)==1
                            for B in (1,3,5):
                                if f==1:
                                    u=pow(k,-1,2*abs(s)); M=S.Matrix([[2*B*s,-B*u*R],[0,1]])
                                    want=[1,2*B*abs(s)]
                                elif f==2:
                                    mod=abs(s); u=pow(k//2,-1,mod) if mod>1 else 0
                                    M=S.Matrix([[B*s,-B*u*(R//2)],[0,1]])
                                    want=[1,B*abs(s)]
                                else:
                                    mod=abs(s); u=pow(k,-1,mod) if mod>1 else 0
                                    M=S.Matrix([[2*B*s,-2*B*u*R],[0,2]])
                                    want=[2,2*B*abs(s)]
                                d,_,_=smith(M); assert d==want
                                global_count+=1
    print('NORMALIZATION',len(norms),'exact conductor complexes with all Smith inverses checked',flush=True)
    print('LOCAL',counts,'surjections and torsion inverse columns checked',flush=True)
    print('GLOBAL',global_count,'Smith presentations, signed powers and clutches checked',flush=True)
    return norms,counts,global_count


if __name__=='__main__':
    print('START',datetime.now(timezone.utc).isoformat(),flush=True)
    rows=catalogue()
    norms,counts,total=finite_checks()
    data={'scope':'new finite checks supplementing all-parameter proof',
          'rows':rows,'normalization_complexes':norms,'local_counts':counts,'global_count':total}
    path=DEST/'S6_SERIES_PUBLISH_III_02LQ_fresh_data_v1.json'
    path.write_text(json.dumps(data,indent=2)+'\n')
    print('DATA',path.name,'bytes',path.stat().st_size,flush=True)
    print('PASS',datetime.now(timezone.utc).isoformat(),flush=True)
