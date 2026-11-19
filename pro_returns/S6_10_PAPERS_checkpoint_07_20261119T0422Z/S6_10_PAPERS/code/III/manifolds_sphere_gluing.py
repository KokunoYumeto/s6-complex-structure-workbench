"""All natural finite sphere initial rows: exact marked monodromies and vanishing normal closure.
No numerical cutoff in section data. Filling multiplicities are not yet classified here.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
from math import gcd
import sys,json
import sympy as s
from manifolds_rankone_families import decomp,ikernel,wedge
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'explorer'))
import os_monodromy as om
rows=json.loads((ROOT/'manifolds_sphere_natural.json').read_text())['candidates']

def saturation(M):
    D,U,V,r=decomp(M)
    return U.inv()[:,:r]

def image_basis(M):
    D,U,V,r=decomp(M)
    return U.inv()[:,:r]*D[:r,:r]

out=[]
for row in rows:
    en,pr,a,b,j0,n=[row[k] for k in ['entry','profile','a','b','zero_index','n']]
    model=om._model(en,pr);kinds=[v['type'] for v in model['fibers']]
    p=om.section_cocycle(model,(a,));q=om.section_cocycle(model,(b,))
    mats=[]
    for j,(v,pi,qi) in enumerate(zip(model['fibers'],p,q)):
        # Zero-free points are narrow for at least one section. At the one
        # component zero use the rational normalized weight; the global
        # relation independently verifies its actual integral lift.
        mat=s.Matrix(om.local_lift(v['A'],pi,qi,Fraction(1,n) if j==j0 else 0))
        assert all(x.q==1 for x in mat)
        mats.append(mat)
    total=s.eye(4)
    for A in mats:total=total*A
    assert total==s.eye(4)
    before=s.eye(4);after=s.eye(4)
    for A in mats[:j0]:before=before*A
    for A in mats[j0+1:]:after=after*A
    assert mats[j0]==before.inv()*after.inv()
    Om=s.diag(a*s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,-b],[b,0]]))
    assert all(A.T*Om*A==Om for A in mats)
    local=[];van=[]
    for k,A in zip(kinds,mats):
        N=A-s.eye(4);D,U,V,r=decomp(N)
        divs=[int(abs(D[i,i])) for i in range(r)]
        fixed=ikernel(N)
        gam=0
        for zz in fixed[3,:]:gam=gcd(gam,abs(int(zz)))
        rec=dict(type=k,matrix=A.tolist(),rank=r,smith=divs,fixed_gamma_index=gam)
        if k.startswith('I') and k[1:].isdigit():
            assert r in [1,2]
            B=saturation(N);van.append(B)
            rec['toric_vanishing_basis']=B.tolist()
        local.append(rec)
    L=image_basis(s.Matrix.hstack(*van))
    while True:
        N=image_basis(s.Matrix.hstack(L,*[A*L for A in mats]))
        if N.cols==L.cols:
            # index one in either coordinate basis gives exact equality.
            sol=L.gauss_jordan_solve(N)[0]
            if all(v.q==1 for v in sol) and abs(sol.det())==1:break
        L=N
    assert L.rank()==3 and all(x==0 for x in L[3,:])
    D,_,_,rank=decomp(L[:3,:]);tors=[int(abs(D[i,i])) for i in range(rank) if abs(D[i,i])>1]
    # The star semistable thimble is primitive on the descended regular fibre.
    Lstar=L
    for k,A in zip(kinds,mats):
        if k.startswith('I') and k.endswith('*') and k[1:-1].isdigit():
            Lstar=Lstar.row_join(saturation(A*A-s.eye(4)))
    Dstar,_,_,rs=decomp(Lstar[:3,:])
    assert rs==3 and all(abs(Dstar[i,i])==1 for i in range(rs))
    coin=s.Matrix.hstack(*[wedge(A)-s.eye(6) for A in mats])
    Dc,_,_,rc=decomp(coin)
    ct=[int(abs(Dc[i,i])) for i in range(rc) if abs(Dc[i,i])>1]
    assert rc==5
    out.append(dict(**row,local=local,vanishing_normal_lattice=L.tolist(),vertical_quotient=tors,
        vertical_quotient_after_star_thimble=[],degree_two_coinvariant_torsion=ct))
print('All integral monodromy tuples:',len(out))
print('Normal-closure vertical quotients:',Counter(tuple(x['vertical_quotient']) for x in out))
print('All172 have trivial vertical quotient after actual star thimble')
print('Degree-two coinvariant torsion:',Counter(tuple(x['degree_two_coinvariant_torsion']) for x in out))
for x in out:
    if x['vertical_quotient']:print(x['entry'],x['profile'],x['a'],x['b'],x['zero_type'],x['vertical_quotient'])
(ROOT/'manifolds_sphere_monodromies.json').write_text(json.dumps(dict(scope=__doc__,rows=out),indent=2,default=int)+'\n')

# Integral and rational block certificates for the all-order I3* obstruction.
star_count=0
for row in out:
    for v in row['local']:
        if v['type']!='I3*':continue
        A=s.Matrix(v['matrix']);N=A*A-s.eye(4)
        D,U,V,r=decomp(N)
        assert r==1 and abs(D[0,0])==3 and N*N==s.zeros(4)
        assert A*N==-N and N*A==-N
        K=ikernel(N)
        assert s.Matrix.hstack(N,(A-s.eye(4))*K).rank()==1
        assert 6-(wedge(A)-s.eye(6)).rank()==2
        k=s.symbols('k',integer=True,positive=True)
        # (I+N)^k=I+kN follows exactly from N^2=0.
        assert N*N==s.zeros(4)
        star_count+=1
assert star_count==8
print('I3* all-order block certificates:',star_count,'rows; width3k, transverse identity, dual-circle -1')
