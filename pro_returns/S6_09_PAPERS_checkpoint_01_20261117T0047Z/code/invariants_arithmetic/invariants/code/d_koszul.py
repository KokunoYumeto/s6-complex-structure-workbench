"""Exact tangent-twist Koszul calculations, by Smith forms and jet ranks.

The script checks finite algebra only. Its comparison with the analytic
relative Dolbeault complex is proved in statement D4.4 of the paper.
"""
from pathlib import Path
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'
s=S.symbols('s')

def complex_matrices(a,K):
    # C0 = (e1,e2,h); C1 = (e1g1,e1g2,e2g1,e2g2,hg1,hg2).
    # C2 = (e1g1g2,e2g1g2,hg1g2).
    a1,a2=a
    d0=S.zeros(6,3)
    d0[0,0]=a1; d0[1,0]=a2
    d0[2,1]=a1; d0[3,1]=a2
    d0[0,2]=K[0,0]; d0[1,2]=K[0,1]
    d0[2,2]=K[1,0]; d0[3,2]=K[1,1]
    d0[4,2]=a1; d0[5,2]=a2
    d1=S.zeros(3,6)
    d1[0,0]=-a2; d1[0,1]=a1
    d1[1,2]=-a2; d1[1,3]=a1
    d1[0,4]=-K[0,1]; d1[0,5]=K[0,0]
    d1[1,4]=-K[1,1]; d1[1,5]=K[1,0]
    d1[2,4]=-a2; d1[2,5]=a1
    assert d1*d0==S.zeros(3)
    return d0,d1

def jet_matrix(mat,N):
    out=S.zeros(mat.rows*N,mat.cols*N)
    for i in range(mat.rows):
        for j in range(mat.cols):
            for (k,),coef in S.Poly(mat[i,j],s).terms():
                for b in range(N-k):
                    out[i*N+b+k,j*N+b]=coef
    return out

def invariant_indices(weights,N,m):
    # A coefficient s^k in a frame of character w is invariant iff k=w mod m.
    return [j*N+k for j,w in enumerate(weights) for k in range(N) if (k-w)%m==0]

def jet_cohom(d0,d1,N,weights=None,m=1):
    D0,D1=jet_matrix(d0,N),jet_matrix(d1,N)
    dims=[3*N,6*N,3*N]
    if weights is not None:
        ids=[invariant_indices(w,N,m) for w in weights]
        D0=D0.extract(ids[1],ids[0]); D1=D1.extract(ids[2],ids[1])
        dims=[len(i) for i in ids]
    assert D1*D0==S.zeros(D1.rows,D0.cols)
    r0,r1=D0.rank(),D1.rank()
    return [dims[0]-r0,dims[1]-r0-r1,dims[2]-r1]

models={
 'regular':((S.Integer(0),s),S.Matrix([[0,1],[1,0]])),
 'order_three':((S.Integer(0),s**2),S.Matrix([[0,s],[s,1]])),
 'order_four':((S.Integer(0),s),S.Matrix([[0,1],[1,0]]))}
report={}
for name,(a,K) in models.items():
    d0,d1=complex_matrices(a,K)
    snf=smith_normal_form(d1,domain=S.QQ.poly_ring(s))
    factors=[str(S.factor(snf[j,j])) for j in range(3)]
    jets={str(N):jet_cohom(d0,d1,N) for N in [6,9]}
    report[name]={'d0':str(d0),'d1':str(d1),'H2_Smith_factors':factors,'jet_cohomology':jets}
    if name=='order_three':
        inv={}
        for n in range(3):
            c0=[n,n+2,n+1]
            c1=[n,n+2,n+2,n+4,n+1,n+3]
            c2=[n+2,n+4,n+3]
            got=jet_cohom(d0,d1,9,[c0,c1,c2],3)
            length=1+int(n%3!=0)
            assert got==[length,2*length,length],(n,got)
            inv[str(n)]=got
        report[name]['coarse_invariant_jet_cohomology']=inv
    if name=='order_four':
        inv={}
        for n in range(4):
            n0=3*n
            c0=[n0,n0+1,n0+1]
            c1=[n0,n0+1,n0+1,n0+2,n0+1,n0+2]
            c2=[n0+1,n0+2,n0+2]
            got=jet_cohom(d0,d1,8,[c0,c1,c2],4)
            length=int(n%4 in [1,2])
            assert got==[length,2*length,length],(n,got)
            inv[str(n)]=got
        report[name]['coarse_invariant_jet_cohomology']=inv

# Independent symbolic leading-coefficient calculation at t=s^3.
F=S.symbols('F',nonzero=True)
tau1=S.I*S.pi*F**2/2
nu2sq=9*F**2/S.Integer(512)
K2=3*F**2/S.Integer(4)
b3=S.simplify((24*nu2sq-K2)/(3*tau1))
transverse=S.simplify(3*(b3-12*nu2sq/tau1))
assert S.simplify(K2+12*nu2sq-123*F**2/128)==0
report['order_three_leading_coefficients']={
 'tau1':str(tau1),'nu2_squared':str(nu2sq),'K2':str(K2),
 'b3':str(b3),'transverse_coefficient_for_k1':str(transverse)}
(OUT/'d_koszul.json').write_text(json.dumps(report,indent=2)+'\n')
for k,v in report.items():
    if 'H2_Smith_factors' in v:
        print(k,'H2 Smith factors:',v['H2_Smith_factors'],'jet cohomology:',v['jet_cohomology'])
        if 'coarse_invariant_jet_cohomology' in v:
            print('  invariant checks:',v['coarse_invariant_jet_cohomology'])
print('Order-three coefficients:',report['order_three_leading_coefficients'])
print('Wrote outputs/d_koszul.json.')
