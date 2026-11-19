"""Exact local data for all14 minimal residual6,15,30 smooth patterns.

This verifies the geometric hypotheses for the full3-primary operation
and the2/5-primary calculations. The complete prime-splitting proof is
separate; no finite multiplicity/twist cutoff is used.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parent
key=lambda x:(x['entry'],x['profile'],x['a'],x['b'],x['zero_index'])
patterns=json.loads((ROOT/'root_remaining_smooth_profiles.json').read_text())['nontrivial_c_patterns']
rows={key(x):x for x in json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']}
finite_rows={key(x):x for x in json.loads((ROOT/'manifolds_all_finite_logs.json').read_text())['rows']}
x,y,j=S.symbols('x y j',integer=True)
records=[];semi=0;normal_checks=[];matrix_checks=0
for c in (6,15,30):
    primes=list(S.factorint(c)); selected=[p for p in patterns if p['c']==c]
    tates=json.loads((ROOT/f'manifolds_c{c}_tate_markings.json').read_text())
    assert {tuple(t['key']) for t in tates}==set(map(key,selected))
    for pattern in selected:
        frow=finite_rows[key(pattern)]
        for site in pattern['finite_indices']:
            loc=frow['local'][site]
            assert loc['gamma_index']==1
            assert frow['b']//loc['q']==loc['normal_fibre_coefficient']
            assert frow['b']%c==loc['normal_fibre_coefficient']%c==0
            normal_checks.append(dict(key=list(key(pattern)),site=site,q=loc['q'],
                                      fibre_coefficient=loc['normal_fibre_coefficient']))
        for site,choice in pattern['additive_choices']:
            if choice=='original':assert frow['local'][site]['original_minimal']
    for tr in tates:
        K=tuple(tr['key']);row=rows[K];a,b=row['a'],row['b']
        assert gcd(a,b)==1 and b%c==0
        omega=S.diag(a*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-b],[b,0]]))
        q=lambda v:int(a*(v[0]+v[1]+v[0]*v[1]))%2
        for loc in row['local']:
            A=S.Matrix(loc['matrix']);assert A.T*omega*A==omega
            if c%2==0:
                assert a%2 and b%4==2
                for v in product((0,1),repeat=4):
                    assert q(A*S.Matrix(v))==q(v);semi+=1
        angular=S.Matrix.hstack(*(S.Matrix(loc['toric_vanishing_basis']) for loc in row['local'] if 'toric_vanishing_basis' in loc))
        globalimages=S.Matrix.hstack(*(S.Matrix(loc['matrix'])-S.eye(4) for loc in row['local']))
        assert hermite_normal_form(angular)==S.eye(4)[:,:3]
        assert hermite_normal_form(globalimages)==S.eye(4)[:,:3]
        rec=dict(residual=c,key=list(K),local=[],primary={})
        fixed={p:[] for p in primes}
        for loc in tr['local']:
            n,r,rho=loc['valuations'];P=S.Matrix(loc['period_matrix'])
            assert P==S.Matrix([[n,-b*r],[a*r,rho]])
            C=S.Matrix(loc['basis']);A=S.Matrix(row['local'][loc['site']]['matrix'])
            adapted=S.eye(4);adapted[0,1]=n;adapted[2,1]=a*r
            adapted[0,3]=-b*r;adapted[2,3]=rho
            assert C.det()==1 and C.inv()*A*C==adapted
            assert adapted==S.Matrix(loc['adapted_monodromy'])
            matrix_checks+=1
            ent=dict(site=loc['site'],type=loc['type'],zero=loc['zero'],valuations=[n,r,rho])
            if loc['zero']:
                assert P.det()==1
                psi=S.expand(-a*rho*x*x-2*a*b*r*x*y+b*n*y*y+a*x)
                assert S.expand(psi.subs({x:x+n,y:y+a*r},simultaneous=True)-psi)==-2*a*x
                assert S.expand(psi.subs({x:x-b*r,y:y+rho},simultaneous=True)-psi)==2*b*y+b*rho-a*b*r
                slope=S.Poly(S.expand(psi.subs(y,y+1)-psi),x,y)
                for p in primes:
                    if p==2:
                        assert n%2 and rho%2
                        half=psi/2
                        for xx,yy in product((0,1),repeat=2):assert S.denom(half.subs({x:xx,y:yy}))==1
                        assert b*n//2%2==1
                    else:
                        assert all(int(v)%p==0 for v in slope.coeffs())
                        assert a*(rho-b*r)%p!=0
                ent['doubled_support']=str(psi)
            else:
                assert P.det()==0
                U=hermite_normal_form(P);assert U.shape==(2,1)
                u1,u2=map(int,U);assert gcd(u1,u2)==1
                if u1<0:u1,u2=-u1,-u2
                alpha=n//u1;beta=-b*r//u1
                assert P==S.Matrix([[alpha*u1,beta*u1],[alpha*u2,beta*u2]])
                assert gcd(alpha,beta)==1 and a*u1%alpha==0
                psi=-S.Rational(a*u1,alpha)*j*(j-alpha)
                assert S.expand(psi.subs(j,j+alpha)-psi)==-2*a*u1*j
                assert S.expand(psi.subs(j,j+beta)-psi)==2*b*u2*j+b*rho-a*b*r
                ent.update(primitive_period=[u1,u2],period_coefficients=[alpha,beta],doubled_support=str(psi))
                if c%2==0:
                    assert alpha%2 or (a*u1//alpha)%2==0
                    for jj in range(4):assert S.denom((psi/2).subs(j,jj))==1
                for p in primes:
                    if u1%p:continue
                    assert n==p and alpha==1 and gcd(a*r,p)==1
                    assert S.expand(psi+a*p*j*(j-1))==0
                    fixed[p].append(loc['site'])
                    w=pow(a*r,-1,p)
                    if p==2:rec['primary'][str(p)]={'mod2_cube':1,'bordism_orbit':1}
                    else:
                        refined=(w*w-1)*pow(2,-1,p)%p
                        if p==3:assert refined==0
                        rec['primary'][str(p)]={'normal_weight':w,'refined_p':refined,
                                              'refined_p_orbit':int(refined!=0),
                                              'mu':0,'mu_justification':'fullS1 Pontryagin cube for3; ordinary cube detects fulltarget for5'}
        assert all(len(v)==1 for v in fixed.values())
        rec['fixed_elliptic_sites']={str(p):v[0] for p,v in fixed.items()}
        records.append(rec)
        print('ROW',K,'c',c,'PRIMARY',rec['primary'],'PASS')
assert len(records)==12
assert sum(p['c'] in (6,15,30) for p in patterns)==14
out={'scope':__doc__,'rows':records,'patterns':[p for p in patterns if p['c'] in (6,15,30)],
     'semicharacter_checks':semi,'adapted_matrix_checks':matrix_checks,'finite_normal_checks':normal_checks,
     'status':'Exact local hypotheses verified; global smooth proof draft separately audited'}
(ROOT/'manifolds_three_mixed_AH.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('ALL14 PATTERNS/12 ROWS;',semi,'SEMICHARACTER CHECKS;',len(normal_checks),'FINITE NORMAL CHECKS: PASS')
print('DIRECT ADAPTED-MATRIX RECHECKS:',matrix_checks,'PASS')
