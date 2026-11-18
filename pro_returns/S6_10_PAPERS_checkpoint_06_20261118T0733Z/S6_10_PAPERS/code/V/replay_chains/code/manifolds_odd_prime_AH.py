"""Exact local certificates for the minimal residual c=5 and c=7 cases.

The finite selection is all36 potentially simply connected filling patterns
on30 marked initial rows in root_remaining_smooth_profiles.json.  No cutoff
on finite logarithmic orders is used.  This program checks the doubled
Appell--Humbert cocycle, actual Tate markings, scalar fixed-curve weights,
primitive angular normal lattice and the resulting conditional localized
characteristic numbers in the basis normalized by evaluation one on the
complex-oriented rational fixed curve.  The global extension/localization
argument is proved separately in D.2.36; these integer checks alone are
not a substitute for that geometric proof.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

ROOT=Path(__file__).resolve().parents[1]
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
patterns=json.loads((ROOT/'records/root_remaining_smooth_profiles.json').read_text())['nontrivial_c_patterns']
monodromy={key(r):r for r in json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']}

# Coordinates are logarithms of (z,v,zeta,1).  All entries are exact.
a,b,tau,xi,beta=S.symbols('a b tau xi beta',integer=True)
h=S.Matrix([[1,0,0,tau],[0,1,0,a*xi],[-2*a,0,1,0],[0,0,0,1]])
F=S.Matrix([[1,0,0,-b*xi],[0,1,0,beta],[0,2*b,1,-a*b*xi+b*beta],[0,0,0,1]])
J=S.Matrix([[-1,0,0,0],[0,-1,0,0],[-2*a,0,1,0],[0,0,0,1]])
assert S.simplify(h*F-F*h)==S.zeros(4)
assert J*J==S.eye(4)
assert S.simplify(J*h*J-h.inv())==S.zeros(4)
assert S.simplify(J*F*J-F.inv())==S.zeros(4)
print('Doubled AH commutation and normalized inversion: PASS')

x,y,j=S.symbols('x y j',integer=True)
records=[]
for prime in (5,7):
    selected=[r for r in patterns if r['c']==prime]
    tates=json.loads((ROOT/f'records/manifolds_c{prime}_tate_markings.json').read_text())
    assert {tuple(r['key']) for r in tates}=={key(r) for r in selected}
    for tr in tates:
        K=tuple(tr['key']);row=monodromy[K];aa,bb=row['a'],row['b']
        assert bb%prime==0 and gcd(aa,prime)==1
        Omega=S.diag(aa*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-bb],[bb,0]]))
        for local in row['local']:
            M=S.Matrix(local['matrix'])
            assert M.T*Omega*M==Omega
        angular=[S.Matrix(loc['toric_vanishing_basis'])[:3,:]
                 for loc in row['local'] if 'toric_vanishing_basis' in loc]
        angular=S.Matrix.hstack(*angular)
        sn=smith_normal_form(angular,domain=S.ZZ)
        inv=[abs(int(sn[i,i])) for i in range(min(sn.shape)) if sn[i,i]]
        assert inv==[1,1,1]
        rec={'prime':prime,'key':list(K),'angular_smith':inv,'local':[]}
        fixed=[]
        for loc in tr['local']:
            n,r,rho=loc['valuations'];P=S.Matrix(loc['period_matrix'])
            assert P==S.Matrix([[n,-bb*r],[aa*r,rho]])
            item={'site':loc['site'],'type':loc['type'],'zero':loc['zero'],
                  'valuations':[n,r,rho]}
            if loc['zero']:
                assert P.det()==1
                psi=S.expand(-aa*rho*x*x-2*aa*bb*r*x*y+bb*n*y*y+aa*x)
                assert S.expand(psi.subs({x:x+n,y:y+aa*r},simultaneous=True)-psi)==-2*aa*x
                assert S.expand(psi.subs({x:x-bb*r,y:y+rho},simultaneous=True)-psi)==2*bb*y+bb*rho-aa*bb*r
                vertical=S.Poly(S.expand(psi.subs(y,y+1)-psi),x,y)
                assert all(int(v)%prime==0 for v in vertical.coeffs())
                value=lambda xx,yy:psi.subs({x:xx,y:yy})
                degree=S.expand(value(1,0)+value(-1,1)-value(0,0)-value(0,1))
                assert degree==-2*aa*(rho-bb*r)
                alpha=int(degree)*pow(2,-1,prime)%prime
                assert alpha==(-aa*pow(n,-1,prime))%prime and alpha
                rec['signed_wall_half_mod_p']=alpha
                rec['cusp_alpha']=1
                item.update(support=str(psi),scalar_character_mod_p=0,
                            doubled_curve_degree=int(degree),alpha_mod_p=alpha)
            else:
                assert P.det()==0
                primitive=hermite_normal_form(P)
                assert primitive.shape==(2,1)
                assert gcd(int(primitive[0,0]),int(primitive[1,0]))==1
                isotropy=abs(int(primitive[0,0]))
                item['scalar_isotropy']=isotropy
                u1,u2=map(int,primitive)
                alpha=n//u1;bet=-bb*r//u1
                assert P==S.Matrix([[alpha*u1,bet*u1],[alpha*u2,bet*u2]])
                assert gcd(alpha,bet)==1 and aa*u1%alpha==0
                rankone_support=-(aa*u1//alpha)*j*(j-alpha)
                assert S.expand(rankone_support.subs(j,j+alpha)-rankone_support)==-2*aa*u1*j
                assert S.expand(rankone_support.subs(j,j+bet)-rankone_support)==2*bb*u2*j+bb*rho-aa*bb*r
                item.update(primitive_period=[u1,u2],period_coefficients=[alpha,bet],
                            integral_support=str(rankone_support))
                if isotropy%prime==0:
                    assert n==prime and gcd(aa*r,n)==1
                    w=pow(aa*r,-1,prime)
                    support=-aa*n*j*(j-1)
                    assert S.expand(support.subs(j,j+1)-support)==-2*aa*n*j
                    item.update(normal_weight_mod_p=w,normal_weight_squared_mod_p=w*w%prime,
                                support=str(support),scalar_character_mod_p=0)
                    fixed.append(item)
            rec['local'].append(item)
        assert len(fixed)==1
        w=fixed[0]['normal_weight_mod_p'];alpha=rec['cusp_alpha']
        # Localization, using D.2.36's global lift and its curve normalization.
        alpha_elliptic=-w*w*alpha%prime
        p1=-2*(alpha+alpha_elliptic)%prime
        refined=p1*pow(4,-1,prime)%prime
        rec.update(elliptic_alpha=alpha_elliptic,normalized_p1=p1,
                   normalized_refined_p=refined,mu=0,
                   smooth_orbit=int(refined!=0))
        records.append(rec)
        print('ROW',K,'p',prime,'fixed weights',w,'curve-normalized refined p',refined,'PASS')

assert len(records)==30
result={'scope':__doc__,'rows':records,'patterns':[p for p in patterns if p['c'] in (5,7)],
        'global_status':'D.2.36 global comparison and classification independently audited; this is its exact local certificate'}
(ROOT/'records/manifolds_odd_prime_AH.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('ALL30 MARKED ROWS /36 FILLING PATTERNS: PASS')
