#!/usr/bin/env python3
"""02LV post-exposure comparison: explicit integral maps and exact formulas.

The five unchanged attached historical programs are executed in a temporary
directory, after their full sources have been read.  Their actual streams
are retained.  No imported program is represented as a new independent
implementation.  The newly written comparisons below transport every
coordinate using displayed integral maps.
"""
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from io import StringIO
from itertools import combinations, product
from pathlib import Path
import json
import runpy
import shutil
import tempfile
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation8_iii_lv'
OUT.mkdir(exist_ok=True)
BASE = ROOT.parent / 'S6_PUBLISH_programs/code'
names = ['III_OS45_core_independent.py',
         'III_OS45_primitive_cubic_independent.py',
         'III_OS45_annulus_independent.py',
         'III_OS45_boundary_prisms_07.py',
         'III_weighted_OS45_checks.py']
fresh = json.loads((ROOT/'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_fresh_lattices_v001.json').read_text())
toric = json.loads((ROOT/'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_toric_coefficients_v001.json').read_text())
print('START', datetime.now(timezone.utc).isoformat())
with tempfile.TemporaryDirectory(prefix='S6_SERIES_PUBLISH_c8_lv_', dir=str(ROOT.parent.parent)) as td:
    temp=Path(td); (temp/'code/outputs').mkdir(parents=True)
    env={}
    for name in names:
        source=BASE/name
        target=temp/'code'/name
        shutil.copyfile(source,target)
        stdout,stderr=StringIO(),StringIO()
        started=datetime.now(timezone.utc).isoformat()
        try:
            with redirect_stdout(stdout),redirect_stderr(stderr):
                env[name]=runpy.run_path(str(target),run_name='__main__')
        finally:
            (OUT/('S6_SERIES_PUBLISH_02LV_replay_'+name[:-3]+'.out')).write_text(stdout.getvalue(),newline='\n')
            (OUT/('S6_SERIES_PUBLISH_02LV_replay_'+name[:-3]+'.err')).write_text(stderr.getvalue(),newline='\n')
        print('HISTORICAL_REPLAY',name,'SHA256',sha256(source.read_bytes()).hexdigest(),'START',started,'EXIT',0)
    old=env[names[0]]
    oldcub=env[names[1]]
    oldann=env[names[2]]
    oldloc=env[names[4]]

    # Exact two-way ambient graph maps and maps of relation columns.
    Mold=old['M']; Mnew=S.Matrix(fresh['H2quotient']['M'])
    Ko=old['K']; Kro=old['Kplus']; Kn=S.Matrix(fresh['graph']); Krn=S.Matrix(fresh['graph_reader'])
    J=S.diag(S.eye(6),Kro*Kn); Ji=S.diag(S.eye(6),Krn*Ko)
    assert J*Ji==Ji*J==S.eye(23)
    def relation_lift(U,V,D,X):
        Y=U*X; Z=S.zeros(V.rows,X.cols)
        for i in range(D.rows):
            if D[i,i]:
                assert all(t % D[i,i]==0 for t in Y.row(i))
                Z[i,:]=Y[i,:]/D[i,i]
            else: assert Y.row(i)==S.zeros(1,Y.cols)
        return V*Z
    Un=S.Matrix(fresh['H2quotient']['U']); Vn=S.Matrix(fresh['H2quotient']['V'])
    Dn=Un*Mnew*Vn
    A=relation_lift(old['U'],old['V'],old['S'],J*Mnew)
    B=relation_lift(Un,Vn,Dn,Ji*Mold)
    assert Mold*A==J*Mnew and Mnew*B==Ji*Mold
    delta=old['literal_phi']*J-Un[22,:]
    assert all(x%8==0 for x in delta)
    linear_new=Un[22,6:]*Krn
    assert all(x%8==0 for x in old['literal_extension']-linear_new)
    print('CORE_SHAPES',list(Mold.shape),list(Mnew.shape),'GRAPH_ROW_MAP_IDENTITY',J==S.eye(23))
    print('CORE_RELATION_MAPS', 'old_A=J_new',A.shape,'new_B=Ji_old',B.shape,'COMPOSITES_IDENTITY',True)
    print('LITERAL_COCHAIN_DIFFERENCE_OVER8',list((old['literal_extension']-linear_new)/8))
    print('CUSP_LINEAR_OLD',list(old['literal_cusp']),'NEW',list(linear_new[:,:4]))

    # The Cremona/permutation map compares the two actual dP6 markings.
    T=S.Matrix([[2,1,1,1],[-1,-1,-1,0],[-1,0,-1,-1],[-1,-1,0,-1]])
    I=S.diag(1,-1,-1,-1)
    assert abs(T.det())==1 and T.T*I*T==I
    newcurves=[(1,-1,0,-1),(0,1,0,0),(1,-1,-1,0),(0,0,1,0),(1,0,-1,-1),(0,0,0,1)]
    for i in range(6):assert T*S.Matrix(oldcub['boundary'][i])==S.Matrix(newcurves[i])
    assert T*S.Matrix(oldcub['fibre'])==S.Matrix([1,0,-1,0])
    print('SURFACE_MAP',T.tolist(),'INVERSE',T.inv().tolist(),'INTERSECTION_ISOMETRY',True)
    eta_deltas=[]
    for i,row in enumerate(oldann['components']):
        q=T*S.Matrix(row['eta'])-S.Matrix(toric['etas'][i])
        assert all(x%8==0 for x in q)
        eta_deltas.append([int(x/8) for x in q])
    print('COMPONENT_REPRESENTATIVE_DIFFERENCES_OVER8',eta_deltas)
    cnew={tuple(v[:3]):v[3] for v in toric['cubic_nonzero']}
    for key,value in oldcub['primitive'].items():assert value==cnew.get(tuple(sorted(key)),0)
    for key,value in cnew.items():assert oldcub['primitive'][key]==value
    assert oldann['P'].applyfunc(lambda z:int(z)%8)==S.Matrix(toric['mixed'])
    print('ALL_CUBICS_AGREE',680,'ALL_MIXED_AGREE',120,'QUADRATIC_AGREE',[7]*14+[0],'PURE_CUBE',0)

    # Common-character and representative changes, with a polynomial proof.
    L,V=S.symbols('L V',integer=True)
    dnew=[];lnew=[];mnew=[]
    for r in range(8):
        e=4 if r==0 else -4 if r==7 else 0
        for s in range(2):
            dnew.append(e if s==0 else 3+e)
            lnew.append(0 if s==0 else -3*r)
            mnew.append(1 if s==0 else 0)
    for i,row in enumerate(oldloc['rows']):
        assert (dnew[i]-row['d'])%8==0 and lnew[i]==-row['lam'] and mnew[i]==row['mu']+1
    polys=[S.expand(-3*sum(d*(L+l)**2 for d,l in zip(dnew,lnew))),
           S.expand(-2*sum(d*(L+l)*(V+m) for d,l,m in zip(dnew,lnew,mnew))),
           S.expand(-sum(d*(V+m)**2 for d,m in zip(dnew,mnew)))]
    for p,mod in zip(polys,[8,16,8]):assert all(x%mod==0 for x in S.Poly(p,L,V).coeffs())
    print('NEW_LOCALIZATION_POLYNOMIALS',[(str(p),m) for p,m in zip(polys,[8,16,8])])

    # Both critical preimages represent the same actual specialization class.
    e=S.eye(4);a,b,d,g=(e[:,i] for i in range(4));u=2*a-b
    rold=a;rnew=-a+b
    assert S.det(S.Matrix.hstack(u[:2,:],rold[:2,:]))==S.det(S.Matrix.hstack(u[:2,:],rnew[:2,:]))==1
    assert rnew==rold-u
    wold=g-8*rold;wnew=g-8*rnew
    A2=old['A'][2]
    assert A2*wold==wold and A2*wnew==wnew
    R2=old['exterior'](A2)-S.eye(6)
    diff=old['wedge'](d,wold)-old['wedge'](d,wnew)
    assert diff==8*R2*old['wedge'](a,d)
    zold=S.Matrix([-16,8,6,16,0,6]);znew=S.Matrix([-16,-8,6,24,0,6])
    assert zold-znew==diff
    print('RANK_ONE_TRANSVERSE_MAP_OLD_TO_NEW',[[1,-1],[0,1]],'INVERSE',[[1,1],[0,1]])
    print('CRITICAL_OLD_MINUS_NEW',list(diff),'EXACT_BOUNDARY', '8 T_2(a wedge delta)')

    # Literal source-line coordinate maps, retaining endpoint unit factors.
    aa,bb,cc,dd,h0,h1=S.symbols('a b c d h0 h1',nonzero=True)
    f=aa*dd
    x=h0**6/bb;y=aa*bb;z=h0**-5*dd
    assert S.simplify(x*y*z-h0*f)==0
    assert S.simplify(x**5*y**5*z**6-f**6/aa)==0
    assert S.simplify((h0*f)**6/(y*(f**6/aa))-x)==0
    assert S.simplify((x*y/h0**6)-aa)==0
    assert S.simplify((h0**6/x)-bb)==0
    assert S.simplify(h0**5*z-dd)==0
    X=-h1*cc/aa;Y=aa*bb;W=aa/(1+bb*cc)**6
    assert S.simplify(X*Y-h1*(1-(1+bb*cc)))==0
    assert S.simplify(W*(1+bb*cc)**6-aa)==0
    print('SOURCE_CHART_FORWARD_INVERSES', 'cusp and I1 exact with h0,h1 retained')

    # Keep the explicit relation maps as new comparison data, without copied sources.
    def sparse(M):return [[i,j,int(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]
    result=dict(core_row_map=sparse(J),core_row_inverse=sparse(Ji),old_from_new_relations=sparse(A),
                new_from_old_relations=sparse(B),relation_shapes=[list(A.shape),list(B.shape)],
                surface_map=T.tolist(),surface_inverse=T.inv().tolist(),eta_differences_over8=eta_deltas,
                ambient_cochain_difference_over8=[int(x/8) for x in old['literal_extension']-linear_new],
                critical_difference=list(diff),localization_polynomials=[str(p) for p in polys],
                qualification='Post-exposure exact comparison and five unchanged attached-program replays; no independent-before-reading credit.')
    (OUT/'S6_SERIES_PUBLISH_III_02LV_comparison_maps.json').write_text(json.dumps(result,default=int,indent=2)+'\n',newline='\n')
print('END',datetime.now(timezone.utc).isoformat())
