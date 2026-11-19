"""Exact line/localization inputs for all eighteen minimal c=4,8,20 patterns.

This extends, and does not overwrite, the earlier c4/c8 obstruction record.
The target coefficients are Z/4, Z/8 and (for c20) separately Z/4 and Z/5.
Every allowed arbitrary finite-II twist is checked symbolically through its
full normal-column coefficients.  No bound on its multiplicity is used.
The refined invariant itself is supplied by the relative-frame/link proof.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parent
key = lambda r: (r['entry'], r['profile'], r['a'], r['b'], r['zero_index'])
patterns = [r for r in json.loads((ROOT/'root_remaining_smooth_profiles.json').read_text())['nontrivial_c_patterns'] if r['c'] in (4,8,20)]
monos = {key(r):r for r in json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']}
finite = {key(r):r for r in json.loads((ROOT/'manifolds_all_finite_logs.json').read_text())['rows']}
x,y,t = S.symbols('x y t', integer=True)
records=[]
checks=matrices=normal=original=0
for pattern in patterns:
    row=finite[key(pattern)]
    for site in pattern['finite_indices']:
        loc=row['local'][site]
        assert loc['type']=='II' and loc['q']==loc['gamma_index']==1
        assert loc['normal_fibre_coefficient']==row['b']==pattern['c']
        # Full coefficients are b*n and -b*r, not just a selected power.
        r,n=S.symbols('r n',integer=True)
        assert S.expand(row['b']*n).coeff(n)%pattern['c']==0
        assert S.expand(-row['b']*r).coeff(r)%pattern['c']==0
        normal+=1
    for site,choice in pattern['additive_choices']:
        if choice=='original':
            assert row['local'][site]['type']=='II'
            assert row['local'][site]['original_minimal']
            original+=1

for c in (4,8,20):
    targets=(4,5) if c==20 else (c,)
    rows=json.loads((ROOT/f'manifolds_c{c}_tate_markings.json').read_text())
    assert {tuple(r['key']) for r in rows}=={key(r) for r in patterns if r['c']==c}
    for rr in rows:
        K=tuple(rr['key']);row=monos[K];a,b=row['a'],row['b']
        assert a%2 and b==c and gcd(a,c)==1
        Om=S.diag(a*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-b],[b,0]]))
        q=lambda z:int(a*(z[0]+z[1]+z[0]*z[1]))%2
        for loc in row['local']:
            M=S.Matrix(loc['matrix']);assert M.T*Om*M==Om
            for v in product((0,1),repeat=4):
                assert q(M*S.Matrix(v))==q(v);checks+=1
        angular=S.Matrix.hstack(*(S.Matrix(loc['toric_vanishing_basis']) for loc in row['local'] if 'toric_vanishing_basis' in loc))
        images=S.Matrix.hstack(*(S.Matrix(loc['matrix'])-S.eye(4) for loc in row['local']))
        assert hermite_normal_form(angular)==hermite_normal_form(images)==S.eye(4)[:,:3]
        record=dict(c=c,key=K,local=[],primary={})
        fixed={p:[] for p in targets}
        cusp_char={}
        for loc in rr['local']:
            n,j,rho=loc['valuations'];P=S.Matrix(loc['period_matrix'])
            C=S.Matrix(loc['basis']);M=S.Matrix(row['local'][loc['site']]['matrix'])
            adapted=S.eye(4);adapted[0,1]=n;adapted[0,3]=-b*j
            adapted[2,1]=a*j;adapted[2,3]=rho
            assert C.det()==1 and C.inv()*M*C==adapted
            assert P==S.Matrix([[n,-b*j],[a*j,rho]])
            matrices+=1
            item=dict(site=loc['site'],type=loc['type'],zero=loc['zero'],valuations=[n,j,rho])
            if loc['zero']:
                assert P.det()==1 and n%2 and rho%2
                phi=S.expand((-a*rho*x*x-2*a*b*j*x*y+b*n*y*y+a*x)/2)
                assert S.expand(phi.subs({x:x+n,y:y+a*j},simultaneous=True)-phi)==-a*x
                assert S.expand(phi.subs({x:x-b*j,y:y+rho},simultaneous=True)-phi)==b*y+S.Rational(b*rho-a*b*j,2)
                for xx,yy in product((0,1),repeat=2):
                    assert phi.subs({x:xx,y:yy}).q==1
                vertical=S.Poly(S.expand(phi.subs(y,y+1)-phi),x,y)
                val=lambda xx,yy:phi.subs({x:xx,y:yy})
                wall=int(val(1,0)+val(-1,1)-val(0,0)-val(0,1))
                assert gcd(wall,c)==1
                for p in targets:
                    assert all(int(vertical.coeff_monomial(v))%p==0 for v in (x,y))
                    cusp_char[p]=int(vertical.coeff_monomial(1))%p
                    assert cusp_char[p]==(0 if p==5 else p//2)
                item.update(support=str(phi),signed_wall=wall,characters=cusp_char)
            else:
                assert P.det()==0
                nu=hermite_normal_form(P)
                if nu[0,0]<0:nu=-nu
                u1,u2=map(int,nu);assert gcd(u1,u2)==1
                al=S.Rational(n,u1);be=S.Rational(-b*j,u1)
                assert al.q==be.q==1 and gcd(int(al),int(be))==1
                assert al*u2==a*j and be*u2==rho
                coeff=S.Rational(a*u1,al);assert coeff.q==1
                phi1=S.expand(-coeff*t*(t-al)/2)
                assert S.expand(phi1.subs(t,t+al)-phi1)==-a*u1*t
                assert S.expand(phi1.subs(t,t+be)-phi1)==b*u2*t+S.Rational(b*rho-a*b*j,2)
                assert int(al)%2 or int(coeff)%2==0
                item.update(primitive=list(nu),support=str(phi1),fixed={})
                for p in targets:
                    stabilizer=gcd(abs(u1),p)
                    assert stabilizer in (1,p)
                    if stabilizer!=p:continue
                    assert n==p and gcd(a*j,p)==1 and al==1
                    w=pow(a*j,-1,p)
                    slope=S.Poly(S.expand(phi1.subs(t,t+1)-phi1),t)
                    assert all(int(v)%p==0 for v in slope.coeffs())
                    if p!=5:assert w*w%p==1
                    fixed[p].append((loc['site'],w))
                    item['fixed'][p]=dict(normal_weight=w,character=0)
            record['local'].append(item)
        for p in targets:
            assert len(fixed[p])==1
            site,w=fixed[p][0]
            cube=-3*cusp_char[p]**2%p
            lam=-(1-w*w)%p
            assert cube==0
            if p!=5:assert lam==0
            record['primary'][p]=dict(fixed_elliptic_site=site,normal_weight=w,
                                     cube=cube,curve_normalized_lambda=lam)
        records.append(record)
        print('ROW',K,'PRIMARY',record['primary'],'PASS',flush=True)

assert len(patterns)==18 and len(records)==14
record=dict(scope=__doc__,patterns=patterns,rows=records,
            semicharacter_checks=checks,adapted_matrices=matrices,
            arbitrary_finite_normal_rows=normal,original_II_rows=original)
(ROOT/'fourfolds_D2_remaining_AH.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
print('PASS:',len(patterns),'patterns;',len(records),'rows;',checks,
      'semicharacters;',matrices,'adapted matrices;',normal,
      'symbolic finite rows;',original,'original II rows')
