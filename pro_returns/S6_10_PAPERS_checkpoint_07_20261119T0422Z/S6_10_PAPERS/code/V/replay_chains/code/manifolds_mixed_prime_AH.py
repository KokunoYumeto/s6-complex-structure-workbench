"""Exact local certificates for residual c=10,14 (proof draft D.2.38).

Checks all12 filling patterns on10 actual initial rows, without any
bound on allowed finite multiplicities.  The global smooth conclusion
still requires the separately audited prime-splitting proof.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form
ROOT=Path(__file__).resolve().parents[1]
key=lambda x:(x['entry'],x['profile'],x['a'],x['b'],x['zero_index'])
patterns=json.loads((ROOT/'records/root_remaining_smooth_profiles.json').read_text())['nontrivial_c_patterns']
rows={key(x):x for x in json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']}
finite_rows={key(x):x for x in json.loads((ROOT/'records/manifolds_all_finite_logs.json').read_text())['rows']}
x,y,j=S.symbols('x y j',integer=True)
records=[];semi=0;cap_checks=[]
for c,prime in [(10,5),(14,7)]:
    selected=[p for p in patterns if p['c']==c]
    for pattern in selected:
        frow=finite_rows[key(pattern)]
        for site in pattern['finite_indices']:
            loc=frow['local'][site]
            assert loc['gamma_index']==1
            assert frow['b']%loc['q']==0
            assert frow['b']//loc['q']==loc['normal_fibre_coefficient']
            assert loc['normal_fibre_coefficient']%c==0 and frow['b']%c==0
            cap_checks.append(dict(key=list(key(pattern)),site=site,
                                  normal_fibre_coefficient=loc['normal_fibre_coefficient'],
                                  gamma_index=loc['gamma_index'],q=loc['q']))
        for site,choice in pattern['additive_choices']:
            if choice=='original':assert frow['local'][site]['original_minimal']
    tates=json.loads((ROOT/f'records/manifolds_c{c}_tate_markings.json').read_text())
    assert set(map(lambda t:tuple(t['key']),tates))==set(map(key,selected))
    for tr in tates:
        K=tuple(tr['key']);row=rows[K];a,b=row['a'],row['b']
        assert a%2 and b%4==2 and b%prime==0 and gcd(a,b)==1
        omega=S.diag(a*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-b],[b,0]]))
        q=lambda v:int(a*(v[0]+v[1]+v[0]*v[1]))%2
        for loc in row['local']:
            A=S.Matrix(loc['matrix']);assert A.T*omega*A==omega
            for v in product((0,1),repeat=4):
                assert q(A*S.Matrix(v))==q(v);semi+=1
        angular=S.Matrix.hstack(*(S.Matrix(loc['toric_vanishing_basis']) for loc in row['local'] if 'toric_vanishing_basis' in loc))
        globalimages=S.Matrix.hstack(*(S.Matrix(loc['matrix'])-S.eye(4) for loc in row['local']))
        assert hermite_normal_form(angular)==S.eye(4)[:,:3]
        assert hermite_normal_form(globalimages)==S.eye(4)[:,:3]
        rec={'residual':c,'odd_prime':prime,'key':list(K),'local':[]}
        fixed2=[];fixedodd=[]
        for loc in tr['local']:
            n,r,rho=loc['valuations'];P=S.Matrix(loc['period_matrix'])
            assert P==S.Matrix([[n,-b*r],[a*r,rho]])
            ent={'site':loc['site'],'type':loc['type'],'zero':loc['zero'],'valuations':[n,r,rho]}
            if loc['zero']:
                assert P.det()==1 and n%2 and rho%2
                psi=S.expand((-a*rho*x*x-2*a*b*r*x*y+b*n*y*y+a*x)/2)
                assert S.expand(psi.subs({x:x+n,y:y+a*r},simultaneous=True)-psi)==-a*x
                assert S.expand(psi.subs({x:x-b*r,y:y+rho},simultaneous=True)-psi)==b*y+S.Rational(b*rho-a*b*r,2)
                assert a*rho%2
                for xx,yy in product((0,1),repeat=2):assert S.denom(psi.subs({x:xx,y:yy}))==1
                slope=S.Poly(S.expand(psi.subs(y,y+1)-psi),x,y)
                assert int(slope.coeff_monomial(1))%2==1
                assert all(int(z)%prime==0 for z in slope.coeffs())
                ent.update(support=str(psi),involution_character=1,odd_prime_character=0,
                           degree_mod2=1,degree_mod_p_nonzero=True)
            else:
                assert P.det()==0
                U=hermite_normal_form(P);assert U.shape==(2,1)
                u1,u2=map(int,U);assert gcd(u1,u2)==1
                if u1<0:u1,u2=-u1,-u2
                alpha=n//u1;beta=-b*r//u1
                assert P==S.Matrix([[alpha*u1,beta*u1],[alpha*u2,beta*u2]])
                assert gcd(alpha,beta)==1 and a*u1%alpha==0
                psi=-S.Rational(a*u1,2*alpha)*j*(j-alpha)
                assert S.expand(psi.subs(j,j+alpha)-psi)==-a*u1*j
                assert S.expand(psi.subs(j,j+beta)-psi)==b*u2*j+S.Rational(b*rho-a*b*r,2), (K,loc,alpha,beta,psi,S.expand(psi.subs(j,j+beta)-psi), b*u2*j+S.Rational(b*rho-a*b*r,2))
                assert alpha%2==1 or (a*u1//alpha)%2==0
                for jj in range(4):assert S.denom(psi.subs(j,jj))==1
                ent.update(primitive_period=[u1,u2],period_coefficients=[alpha,beta],support=str(psi))
                if u1%2==0:
                    assert n==2 and alpha==1 and a*r%2
                    assert S.expand(psi+a*j*(j-1))==0
                    fixed2.append(loc['site']);ent['involution_character']=0
                if u1%prime==0:
                    assert n==prime and alpha==1 and gcd(a*r,prime)==1
                    w=pow(a*r,-1,prime)
                    assert S.expand(2*psi+a*prime*j*(j-1))==0
                    fixedodd.append(loc['site'])
                    ent.update(odd_prime_character=0,normal_weight=w)
                    rec['odd_refined_p']=(w*w-1)*pow(2,-1,prime)%prime
                    rec['odd_smooth_orbit']=int(rec['odd_refined_p']!=0)
            rec['local'].append(ent)
        assert len(fixed2)==len(fixedodd)==1
        rec.update(mod2_cube=1,odd_mu=0,fixed_elliptic_mod2=fixed2[0],fixed_elliptic_modp=fixedodd[0])
        records.append(rec)
        print('ROW',K,'c',c,'mod2 cube1; odd orbit',rec['odd_smooth_orbit'],'PASS')
assert len(records)==10
(ROOT/'records/manifolds_mixed_prime_AH.json').write_text(json.dumps({
    'scope':__doc__,'rows':records,'patterns':[p for p in patterns if p['c'] in (10,14)],
    'semicharacter_checks':semi,'finite_normal_checks':cap_checks,
    'status':'Exact local certificates; full global prime-splitting proof awaiting independent audit'},indent=2,default=int)+'\n')
assert len(cap_checks)==3
print('ALL12 PATTERNS/10 ROWS;',semi,'SEMICHARACTER CHECKS: PASS')
print('ALL3 finite normal-coefficient checks and all original additive choices: PASS')
