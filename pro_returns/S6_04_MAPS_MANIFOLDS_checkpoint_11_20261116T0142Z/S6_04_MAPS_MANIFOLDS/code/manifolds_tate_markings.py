"""Extract actual Tate valuations and unimodular markings from the monodromy.

Source: records/manifolds_sphere_monodromies.json, whose matrices are
independently generated from the supplied Oguiso--Shioda/Explorer marking
by manifolds_sphere_gluing.py.  No component representative is substituted.

Choose a genuine SL2 basis (u1,u2) with det=1 and
B u2=u2+n*u1.  In the torus basis (u1,u2,delta,gamma), the actual matrix
then has A u2=u2+n*u1+a*H*delta and
A gamma=gamma-b*H*u1+R*delta.
Thus ord(h1,hG,R_multiplier)=(n,H,R).  The actual two valuation periods
are the columns (n,aH),(-bH,R), whose determinant is nR+abH^2.
For a sphere-candidate row it is one at the chosen zero and zero at
every other multiplicative site.  This also gives the full cusp marking,
not merely the component of G modulo n.
"""
from pathlib import Path
import argparse
import json
import sympy as s
from manifolds_rankone_families import decomp,bezout

ROOT=Path(__file__).resolve().parents[1]
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])

def extract(residual):
    data=json.loads((ROOT/'records/manifolds_nonstar_sphere_patterns.json').read_text())['all_patterns']
    patterns=[r for r in data if r['residual_c']==residual and not r['orbifold_obstruction']]
    monodromy={key(r):r for r in json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']}
    result=[]
    for kk in sorted({key(p) for p in patterns}):
        row=monodromy[kk];locs=[]
        for j,loc in enumerate(row['local']):
            if not(loc['type'].startswith('I') and loc['type'][1:].isdigit()):continue
            A=s.Matrix(loc['matrix'])
            D,U,V,rank=decomp(A[:2,:2]-s.eye(2))
            assert rank==1
            u=U.inv()[:,0];be,g=bezout(list(u))
            assert g==1
            v=s.Matrix([-be[1],be[0]])
            C=s.eye(4);C[:2,:2]=s.Matrix.hstack(u,v)
            assert C.det()==1
            Ac=C.inv()*A*C
            n=Ac[0,1];H=Ac[2,1]/row['a'];R=Ac[2,3]
            assert n==int(loc['type'][1:]) and H.q==1 and Ac[0,3]==-row['b']*H
            expected=s.eye(4);expected[0,1]=n;expected[2,1]=row['a']*H
            expected[0,3]=-row['b']*H;expected[2,3]=R
            assert Ac==expected
            period=s.Matrix([[n,-row['b']*H],[row['a']*H,R]])
            assert period.det()==(1 if j==row['zero_index'] else 0)
            locs.append(dict(site=j,type=loc['type'],zero=j==row['zero_index'],
                             basis=C.tolist(),valuations=[int(n),int(H),int(R)],
                             period_matrix=period.tolist(),adapted_monodromy=Ac.tolist()))
        result.append(dict(key=kk,local=locs))
    path=ROOT/f'records/manifolds_c{residual}_tate_markings.json'
    path.write_text(json.dumps(result,indent=2,default=int)+'\n')
    print('Residual',residual,':',len(patterns),'patterns,',len(result),'initial rows;',path.name)
    for row in result:
        print(row['key'],[(v['type'],v['zero'],v['valuations']) for v in row['local']])
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--residual',type=int,nargs='+',default=[2,5,7])
    args=parser.parse_args()
    for c in args.residual:extract(c)
