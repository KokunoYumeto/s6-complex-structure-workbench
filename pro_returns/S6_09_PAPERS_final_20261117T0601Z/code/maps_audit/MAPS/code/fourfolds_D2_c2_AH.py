"""Exact auxiliary-line and toric parity certificates for all minimal c=2 rows.

Scope: the15 actual additive-filling patterns in root's remaining smooth
catalogue, on13 distinct marked initial monodromy rows, with no additional
regular logarithms.  The script checks every actual local monodromy on
all16 lattice vectors modulo2; it does not replace a global extension
proof by this finite calculation.
"""
from pathlib import Path
from itertools import product
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

root=Path(__file__).resolve().parents[1]
patterns=[r for r in json.loads((root/'records/root_remaining_smooth_profiles.json').read_text())
          ['nontrivial_c_patterns'] if r['c']==2]
monos=json.loads((root/'records/manifolds_sphere_monodromies.json').read_text())['rows']
tate=json.loads((root/'records/manifolds_c2_tate_markings.json').read_text())
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
monodromy={key(r):r for r in monos};tates={tuple(r['key']):r for r in tate}

# Multiplicative factors are checked on logarithms, modulo integral shifts
# of the auxiliary logarithmic coordinate.  J is normalized at the origin.
a,d,tau,xi,beta=S.symbols('a d tau xi beta',integer=True)
b=2*d
h=S.Matrix([[1,0,0,tau],[0,1,0,a*xi],[-a,0,1,a/2],[0,0,0,1]])
F=S.Matrix([[1,0,0,-b*xi],[0,1,0,beta],[0,b,1,-a*b*xi/2+b*beta/2],[0,0,0,1]])
J=S.Matrix([[-1,0,0,0],[0,-1,0,0],[-a,0,1,0],[0,0,0,1]])
assert S.simplify(h*F-F*h)==S.zeros(4)
assert J*J==S.eye(4)
diff=S.simplify(J*h*J-h.inv());expected=S.zeros(4);expected[2,3]=a
assert diff==expected and S.simplify(J*F*J-F.inv())==S.zeros(4)
print('SYMBOLIC AH COMMUTATION AND NORMALIZED INVERSION IDENTITIES PASSED',flush=True)

x,y,z=S.symbols('x y z',integer=True)
records=[];checks=0
for K in sorted(set(key(r) for r in patterns)):
    row=monodromy[K];aa,bb=row['a'],row['b']
    assert aa%2==1 and bb in (2,6)
    Omega=S.diag(aa*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-bb],[bb,0]]))
    q=lambda v:int(aa*(v[0]+v[1]+v[0]*v[1]))%2
    for local in row['local']:
        M=S.Matrix(local['matrix']);assert M.T*Omega*M==Omega
        for v in product((0,1),repeat=4):
            assert q(M*S.Matrix(v))==q(v);checks+=1
    angular=S.Matrix.hstack(*(S.Matrix(t['toric_vanishing_basis']) for t in row['local']
                              if 'toric_vanishing_basis' in t))
    angular_hnf=hermite_normal_form(angular)
    assert angular_hnf==S.eye(4)[:,:3]
    global_images=S.Matrix.hstack(*(S.Matrix(t['matrix'])-S.eye(4) for t in row['local']))
    assert hermite_normal_form(global_images)==S.eye(4)[:,:3]
    rec={'key':list(K),'angular_hnf':angular_hnf.tolist(),'local':[]};elliptic_fixed=0
    for local in tates[K]['local']:
        n,j,rho=local['valuations'];P=S.Matrix(local['period_matrix'])
        assert P==S.Matrix([[n,-bb*j],[aa*j,rho]])
        C=S.Matrix(local['basis']);A=S.Matrix(row['local'][local['site']]['matrix'])
        adapted=S.eye(4);adapted[0,1]=n;adapted[2,1]=aa*j
        adapted[0,3]=-bb*j;adapted[2,3]=rho
        assert C.det()==1 and C.inv()*A*C==adapted
        entry={'site':local['site'],'type':local['type'],'zero':local['zero'],
               'valuations':[n,j,rho],'period_matrix':P.tolist()}
        if local['zero']:
            assert P.det()==1 and n%2 and rho%2
            phi=S.expand((-aa*rho*x*x-2*aa*bb*j*x*y+bb*n*y*y+aa*x)/2)
            assert S.expand(phi.subs({x:x+n,y:y+aa*j},simultaneous=True)-phi)==-aa*x
            expected=bb*y+S.Rational(bb*rho-aa*bb*j,2)
            assert S.expand(phi.subs({x:x-bb*j,y:y+rho},simultaneous=True)-phi-expected)==0
            dy=S.Poly(S.expand(phi.subs(y,y+1)-phi),x,y)
            assert int(dy.coeff_monomial(x))%2==0 and int(dy.coeff_monomial(y))%2==0
            assert int(dy.coeff_monomial(1))%2==1
            value=lambda u,v:phi.subs({x:u,y:v})
            degree=value(1,0)+value(-1,1)-value(0,0)-value(0,1)
            assert S.denom(degree)==1 and int(degree)%2==1
            for xx,yy in product((0,1),repeat=2):assert S.denom(value(xx,yy))==1
            entry.update(support=str(phi),vertical_character=1,fixed_curve_degree=int(degree))
        else:
            assert P.det()==0
            V=hermite_normal_form(P);assert V.shape==(2,1)
            assert S.gcd(V[0,0],V[1,0])==1
            if V[0,0]<0:V=-V
            u1,u2=map(int,V[:,0]);al=S.Rational(n,u1);be=S.Rational(-bb*j,u1)
            assert al.q==be.q==1 and S.gcd(al,be)==1
            assert al*u2==aa*j and be*u2==rho
            coeff=S.Rational(aa*u1,al);assert coeff.q==1
            rankone=S.expand(-coeff*z*(z-al)/2)
            assert S.expand(rankone.subs(z,z+al)-rankone)==-aa*u1*z
            assert S.expand(rankone.subs(z,z+be)-rankone)==bb*u2*z+S.Rational(bb*rho-aa*bb*j,2)
            assert al%2 or coeff%2==0
            isotropy=abs(int(V[0,0]))
            entry['scalar_isotropy_on_double_curve']=isotropy
            entry['primitive_valuation']=V.tolist()
            entry['period_coefficients']=[int(al),int(be)]
            entry['exact_rankone_support']=str(rankone)
            if isotropy%2==0:
                elliptic_fixed+=1
                assert n==2 and j%2 and rho==-aa*bb*j*j//2
                u=(1-aa*j)//2
                coordinate=S.Matrix([[u,1],[-aa*j,2]])
                assert coordinate.det()==1
                assert coordinate*S.Matrix([2,aa*j])==S.Matrix([1,0])
                # z=x^2 y^-1, v=x^(a*j) y^u.  The h multiplier has
                # x exponent -2a; F*h^(b*j/2) has x exponent0, y exponentb/2.
                r=bb*j//2
                assert -2*aa*r+aa*j*bb==0 and aa*r+u*bb==bb//2
                support=-aa*z*(z-1)
                assert S.expand(support.subs(z,z+1)-support)==-2*aa*z
                entry.update(coordinates=coordinate.tolist(),support=str(support),
                             involution_character=0,corrected_F_y_exponent=bb//2)
        rec['local'].append(entry)
    assert elliptic_fixed==1
    records.append(rec)
    print('ROW',K,'all semicharacters; cusp odd character/degree; unique I2 even character PASSED',flush=True)
assert len(patterns)==15 and len(records)==13
vertical_index={'II':1,'III':2,'IV':3,'III*':2,'IV*':3}
for p in patterns:
    assert len(p['finite_types'])<=1
    for typ in p['finite_types']:
        qi=vertical_index[typ]
        assert p['b']//qi==2 and p['b']%qi==0
result={'patterns':patterns,'initial_rows':records,'semicharacter_tests':checks,
        'scope':'Local AH parity, full angular and global coinvariant lattices, and all finite normal-column parities for Theorem D.2.35; the global proof is in the accompanying TeX'}
(root/'records/fourfolds_D2_c2_AH.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('ALL15 PATTERNS /13 INITIAL ROWS;',checks,'EXACT SEMICHARACTER TESTS;13 ANGULAR/COINVARIANT HNF CHECKS; ALL FINITE NORMAL PARITIES PASSED',flush=True)
