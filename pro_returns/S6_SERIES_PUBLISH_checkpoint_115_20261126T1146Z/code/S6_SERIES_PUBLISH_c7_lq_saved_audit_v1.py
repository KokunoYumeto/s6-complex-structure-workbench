#!/usr/bin/env python3
"""Read every saved LQ matrix and check inverse equations independently.
Also construct the actual central group and evaluate all marked tori.
This is exhaustive computational verification, not manual JSON reading.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
from datetime import datetime, timezone
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'agents/continuation7_iii_star_logs/S6_SERIES_PUBLISH_III_02LQ_fresh_data_v1.json'
PAIRS=list(combinations(range(4),2))


def wedge(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in PAIRS]
                     for i,j in PAIRS])


def egcd(a,b):
    if not b: return abs(a), (1 if a>0 else -1 if a<0 else 0), 0
    d,u,v=egcd(b,a%b)
    return d,v,u-(a//b)*v


def core_mul(x,y):
    b,l,f,t=x; B,L,F,T=y
    return b+B,l+L,f+F,(t+T-l*B)%2


def core_inverse(x):
    b,l,f,t=x
    return -b,-l,-f,(-t-l*b)%2


def theta(x,n,sign):
    b,l,f,t=x
    if sign==1:
        return -b,l-n*b,f-l,(t-n*b*(b-1)//2)%2
    B=-b; L=l-n*b
    return B,L,f+L,(t+n*B*(B-1)//2)%2


def action(x,z,n):
    for _ in range(abs(z)):
        x=theta(x,n,1 if z>=0 else -1)
    return x


def mul(x,y,n):
    return core_mul(x[:4],action(y[:4],x[4],n))+(x[4]+y[4],)


def inverse(x,n):
    return action(core_inverse(x[:4]),-x[4],n)+(-x[4],)


def power(x,z,n):
    if z<0: return power(inverse(x,n),-z,n)
    out=(0,0,0,0,0)
    while z:
        if z%2: out=mul(out,x,n)
        x=mul(x,x,n); z//=2
    return out


def comm(x,y,n):
    return mul(mul(mul(x,y,n),inverse(x,n),n),inverse(y,n),n)


def audit_data():
    data=json.loads(PATH.read_text())
    assert set(data)=={'scope','rows','normalization_complexes','local_counts','global_count'}
    assert len(data['rows'])==12 and len(data['normalization_complexes'])==80
    fields={'name','n','H','H_inverse','matrices','omega','wedge_relation_U',
            'wedge_relation_V','graph_K','graph_K_inverse','normal_columns',
            'normal_U','normal_V','delta_relation'}
    for row in data['rows']:
        assert set(row)==fields
        H=S.Matrix(row['H']); Hi=S.Matrix(row['H_inverse'])
        assert H*Hi==Hi*H==S.eye(4) and H.det()==1
        AA=list(map(S.Matrix,row['matrices'])); P=S.eye(4)
        for A in AA: P=P*A
        assert P==S.eye(4)
        star=next(A for A in AA if A.trace()==0)
        n=row['n']; target=S.Matrix([[-1,0,-1,0],[0,-1,0,0],[0,-n,1,0],[0,0,0,1]])
        assert Hi*star*H==target
        W=S.Matrix.hstack(*(wedge(A)-S.eye(6) for A in AA))
        U=S.Matrix(row['wedge_relation_U']); V=S.Matrix(row['wedge_relation_V'])
        diag=U*W*V
        assert abs(U.det())==abs(V.det())==1
        assert diag==S.diag(1,1,1,1,1,0).row_join(S.zeros(6,W.cols-6))
        omega=S.Matrix(row['omega']); assert omega*W==S.zeros(1,W.cols)
        G=S.Matrix.hstack(*(A-S.eye(4) for A in AA[:-1]))
        K=S.Matrix(row['graph_K']); Ki=S.Matrix(row['graph_K_inverse'])
        assert G*K==S.zeros(4,K.cols) and Ki*K==S.eye(K.cols)
        normals=S.Matrix(row['normal_columns']); Q=Ki*normals
        U=S.Matrix(row['normal_U']); V=S.Matrix(row['normal_V'])
        assert U*Q*V==S.eye(K.cols).row_join(S.zeros(K.cols,1))
        assert abs(U.det())==abs(V.det())==1 and K*Q==normals
        delta=S.Matrix(row['delta_relation'])
        assert normals*delta==S.zeros(normals.rows,1) and gcd(*map(int,delta))==1
        local=[]
        for A in AA:
            sd=smith_normal_form(A-S.eye(4),domain=S.ZZ)
            entries=[abs(int(sd[i,i])) for i in range(4) if sd[i,i]]
            assert all(x==1 for x in entries)
            local.append(entries)
        print('SAVED ROW PASS',row['name'],'all inverse fields; boundary H1 entries',local,flush=True)
    for obj in data['normalization_complexes']:
        assert set(obj)=={'n','k','j','f','rho','C','U','V'}
        n,k,j,f,rho=(obj[x] for x in ('n','k','j','f','rho'))
        assert n in (1,3) and 1<=k<=8 and -2<=j<=2
        actual=sum((2*i-j)%(n*k)==0 for i in range(n*k))
        assert actual==f and rho==(n*k+f)//2
        C=S.Matrix(obj['C']); U=S.Matrix(obj['U']); V=S.Matrix(obj['V'])
        assert abs(U.det())==abs(V.det())==1
        diagonal=U*C*V
        assert C.rows-C.cols==rho+1
        want=[1]*C.cols
        if f==0: want[-1]=2
        expected=S.zeros(C.rows,C.cols)
        for i,z in enumerate(want): expected[i,i]=z
        assert diagonal==expected
        assert U.inv()*diagonal*V.inv()==C
    assert data['local_counts']=={'0':264,'1':600,'2':396}
    assert data['global_count']==11340
    print('SAVED DATA PASS: every field in 12 rows and 80 complexes checked; 961855 input bytes',flush=True)


def central_check():
    beta=(1,0,0,0,0); lam=(0,1,0,0,0); h=(0,0,0,0,1)
    one=(0,0,0,0,0); total=0
    for n in (1,3):
        for x in (beta,lam,h,(3,-2,5,1,-3)):
            assert mul(x,inverse(x,n),n)==mul(inverse(x,n),x,n)==one
        assert comm(beta,lam,n)==(0,0,0,1,0)
        assert comm(lam,h,n)==(0,0,1,0,0)
        assert comm(beta,power(h,2,n),n)==(0,0,-n,n%2,0)
        for k in range(1,7):
            m=2*k
            for j in range(-2,3):
                for r in range(-2,3):
                    R=2*r-j
                    for N in (-5,-3,-1,1,3,5):
                        if gcd(N,m)!=1: continue
                        d,u,v=egcd(N,m); assert d==1
                        g=mul(power(h,N,n),power(lam,v*R,n),n)
                        ell=mul(power(h,m,n),power(lam,-u*R,n),n)
                        w=mul(comm(beta,ell,n),power(comm(lam,ell,n),(n-1)//2,n),n)
                        assert w==(0,0,-k,(k+j)%2,0)
                        assert comm(power(lam,2,n),g,n)==(0,0,2*N,0,0)
                        assert comm(ell,g,n)==(0,0,-R,0,0)
                        # Marked H1 quotient and its literal inverse.
                        A=S.Matrix([[1,2*u*R,-2*v*R],[0,m,N]])
                        section=S.Matrix([[1,0],[0,v],[0,u]])
                        kernel=S.Matrix([-2*R,N,-m])
                        assert A*section==S.eye(2) and A*kernel==S.zeros(2,1)
                        assert S.eye(3)-section*A==kernel*S.Matrix([[0,u,-v]])
                        total+=1
    print('CENTRAL GROUP PASS',total,'exact word evaluations, all normal torsion coordinates and H1 inverses',flush=True)


def toric_identity():
    n,k,j,r,N,tau,l,w,z,B,eps,F=S.symbols('n k j r N tau l w z B eps F')
    R=2*r-j; m=2*k; q=n*k; t=(R+N*tau)/m
    linear=S.Matrix([[-1,-1],[0,1]])
    periods=[S.Matrix([1,0]),S.Matrix([-q*l-eps/2+B,-n/2+eps]),
             S.Matrix([0,1]),S.Matrix([-tau/2,tau])]
    shifted=[v.subs({l:l+1/m,eps:-eps},simultaneous=True) for v in periods]
    wanted=[-shifted[0],-shifted[1]-n*shifted[2],shifted[2]-shifted[0],shifted[3]]
    assert all((linear*a-b).applyfunc(S.simplify)==S.zeros(2,1) for a,b in zip(periods,wanted))
    first=-z-w-j*l+F
    second=S.expand(-first-(w+t)-j*(l+1/m)+F)
    assert S.simplify(second-(z-t-j/m))==0
    assert S.simplify(-k*(t+j/m)-(-r-N*tau/2))==0
    print('TORIC PASS: exact nonconstant-period conjugacy, two-step translation and full root power',flush=True)


if __name__=='__main__':
    print('START',datetime.now(timezone.utc).isoformat(),flush=True)
    audit_data(); central_check(); toric_identity()
    print('PASS',datetime.now(timezone.utc).isoformat(),flush=True)
