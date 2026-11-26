#!/usr/bin/env python3
"""LM post-exposure comparison: actual maps, old stored arithmetic, all parameters.

No historical program is executed/imported.  Frozen fresh files are read only.
The historical full Smith matrices are not present in their output; their
stored vectors are inspected through every available literal pairing map.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, product
from math import gcd
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_residual_twenty_receiving'
LANE.mkdir(exist_ok=True)
OLD=Path('/tmp/S6_SERIES_PUBLISH_c7_LM_historical')
FRESH=ROOT/'agents/continuation7_iii_residual_twenty_root'
raw=json.loads((ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())
new=json.loads((FRESH/'S6_SERIES_PUBLISH_III_02LM_fresh_geometry_v003.json').read_text())['rows']
def old(name):return json.loads((OLD/('S6_SERIES_PUBLISH_'+name+'.json')).read_text())
ah=old('fourfolds_D2_remaining_AH')
critical=old('manifolds_extended_critical_cycles')
symbolic=old('manifolds_extended_critical_symbolic')
frame=old('maps_D2_II_frame_checks')
key=lambda r:(r['OS'],r['profile'],r['a'],r['b'],r['zero'])
new_by={key(r):r for r in new}
E=S.eye(4);J=S.Matrix([[0,1],[-1,0]])
PAIRS=list(combinations(range(4),2))
def biv(u,v):return S.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in PAIRS])
def wedge(T):return S.Matrix.hstack(*(biv(T[:,i],T[:,j]) for i,j in PAIRS))
def ivec(v):return [int(x) for x in v]
def imat(M):return [[int(x) for x in r] for r in M.tolist()]

# Direct original-II polynomial and matrix identities, including generation data.
x,y,xb,yb=S.symbols('x y xb yb')
df=S.Matrix([[-3*x*x,2*y,0]])
kernel=S.Matrix([[2*y,0],[3*x*x,0],[0,1]])
bott=S.Matrix([[2*y,-3*xb*xb],[3*x*x,2*yb]])
star=S.Matrix([[2*yb,3*xb*xb],[-3*x*x,2*y]])
norm=4*y*yb+9*x*x*xb*xb
assert df*kernel==S.zeros(1,2)
assert star*bott==norm*S.eye(2) and bott.det()==norm
assert S.Matrix([[-3*x*x,2*y]])*bott==S.Matrix([[0,norm]])
assert frame['critical_multiplicity']==frame['bott_degree']==2
assert frame['type_II_jacobian_standard_monomials']==['1','x']
assert frame['good_log_corrected_critical_cycle']==0
print('II differential: kernel annihilation, full Bott identity, Jacobian basis 1,x; degree and generation proved in receiving text')
print('HISTORICAL_FRAME_OUTPUT',json.dumps(frame,sort_keys=True))

# Reconstruct all fourteen historical AH inputs from permitted raw fixtures.
semicount=adapted=0
for rr in ah['rows']:
    os,name,a,b,zero=rr['key']
    profile=next(r for r in raw['rows'] if r['OS']==os and r['profile']==name)
    alt=S.diag(a*J,S.Matrix([[0,-b],[b,0]]))
    Ts=[]
    for i,(kind,bb,gg) in enumerate(zip(profile['fibers'],profile['elliptic_matrices'],profile['generator_section_cocycle'])):
        B,G=S.Matrix(bb),S.Matrix(gg);beta=-G.T*J*B
        T=S.eye(4);T[:2,:2]=B;T[:2,3]=b*G;T[2,:2]=a*beta
        if kind=='II':T[2,3]=a*b*(beta*(B-S.eye(2)).inv()*G)[0]
        else:
            D=B-S.eye(2)
            u=next(D[:,j] for j in range(2) if D[:,j]!=S.zeros(2,1))
            u/=gcd(int(u[0]),int(u[1]))
            if next(z for z in u if z)<0:u=-u
            nu=next(D[i,j]/(u*u.T*J)[i,j] for i in range(2) for j in range(2) if (u*u.T*J)[i,j])
            kap=next(G[j]/u[j] for j in range(2) if u[j])
            T[2,3]=S.Rational(int(i==zero)-a*b*kap*kap,nu)
        assert all(z.is_Integer for z in T) and T.T*alt*T==alt
        for vv in product((0,1),repeat=4):
            v=S.Matrix(vv);w=T*v
            assert int(a*(v[0]*v[1]+v[0]+v[1])-a*(w[0]*w[1]+w[0]+w[1]))%2==0
            semicount+=1
        Ts.append(T)
    for loc in rr['local']:
        i=loc['site'];nu,j,rho=loc['valuations']
        T=Ts[i]
        # The stored AH result omits the input basis.  Its physical valuation
        # matrix is checked against the defining raw rank-one nilpotent map.
        B=T[:2,:2];D=B-S.eye(2)
        u=next(D[:,k] for k in range(2) if D[:,k]!=S.zeros(2,1))
        u/=gcd(int(u[0]),int(u[1]))
        if next(z for z in u if z)<0:u=-u
        kap=next(S.Matrix(profile['generator_section_cocycle'][i])[k]/u[k] for k in range(2) if u[k])
        assert abs(j)==abs(kap) and int(nu)==int(profile['fibers'][i][1:])
        assert rho==T[2,3]
        adapted+=1
    print('AH_RAW_ROW',rr['key'],'semicharacters',16*len(Ts),'physical_period_rows',len(rr['local']),
          'stored_primary',json.dumps(rr['primary'],sort_keys=True))
assert len(ah['patterns'])==18 and len(ah['rows'])==14
assert semicount==ah['semicharacter_checks']==1056
assert adapted==ah['adapted_matrices']==62
assert ah['arbitrary_finite_normal_rows']==ah['original_II_rows']==4
print('AH_COUNTS 18 patterns / 14 rows / 1056 actual quadratic-refinement checks / 62 raw physical valuation rows / 4 finite and 4 original II')

# Read and verify every retained fresh integral inverse/chain matrix.
for rr in new:
    a,b=rr['a'],rr['b'];Om=S.Matrix([[a,0,0,0,0,-b]])
    F,Fi=S.Matrix(rr['fibre_basis']),S.Matrix(rr['fibre_inverse'])
    R,Q=S.Matrix(rr['relation_matrix']),S.Matrix(rr['relation_section'])
    U,V=S.Matrix(rr['euclid_left']),S.Matrix(rr['euclid_right'])
    M=(Fi*R)[1:,:]
    assert F*Fi==Fi*F==S.eye(6) and Fi[0,:]==Om
    assert U*M*V==S.eye(5).row_join(S.zeros(5,M.cols-5))
    assert abs(U.det())==abs(V.det())==1 and M*Q==S.eye(5)
    assert U.inv()*U==S.eye(5) and V.inv()*V==S.eye(V.rows)
    ang,sec=S.Matrix(rr['angular_matrix']),S.Matrix(rr['angular_section'])
    assert ang*sec==E[:,:3]
    for loc in rr['local']:
        H,Hi=S.Matrix(loc['H']),S.Matrix(loc['H_inverse'])
        assert H*Hi==Hi*H==E and H.det()==1
    for vv in rr['variants']:
        c=S.Matrix(vv['total']);chain=S.Matrix(vv['exterior_chain'])
        assert R*chain==c-vv['q']*F[:,0]
    print('FRESH_MAPS',list(key(rr)),'all local inverses, angular section, full Euclid inverse matrices and every critical chain PASS')

# Every stored critical replay: all coefficients available in its output.
assert len(critical['rows'])==158
old_by_pattern={}
for index,rec in enumerate(critical['rows']):
    kk=tuple(rec['key']);rr=new_by[kk];a,b=rr['a'],rr['b'];Om=S.Matrix([[a,0,0,0,0,-b]])
    old_by_pattern.setdefault(rec['pattern'],rec)
    total=S.zeros(6,1)
    for loc in rec['local_critical_lifts']:
        if loc['type']=='II':
            v=loc['multiplicity']*S.Matrix(loc['reduced_curve_lift'])
            assert v==loc['multiplicity']*biv(E[:,2],S.Matrix(loc['fixed_long']))
            assert S.Matrix(rr['monodromies'][loc['site']])*S.Matrix(loc['fixed_long'])==S.Matrix(loc['fixed_long'])
        else:
            v=S.Matrix(loc['curve_lift'])
            C=S.Matrix(loc['basis']);P=S.Matrix(loc['period'])
            T=S.Matrix(rr['monodromies'][loc['site']])
            assert C.det()==1 and (C.inv()*T*C).extract([0,2],[1,3])==P
            if P.det():
                assert P.det()==1
                Sh=C[:,[0,2]];Lo=C[:,[1,3]];Lold=Lo*P.inv()
                stated=biv(Sh[:,0],Lold[:,0])+biv(Lold[:,0],Sh[:,1])+biv(Sh[:,1],Lold[:,1])
                assert v==stated
            else:
                assert (Om*v)[0]==rr['local'][loc['site']]['degree']
        total+=v
    assert ivec(total)==rec['critical_cycle']
    kval=int((Om*total)[0]);assert rec['critical_cycle_order']==b//gcd(b,kval)
    offset=6*(len(rec['local_critical_lifts'])+1)
    def clutch(c):return S.Matrix(c[offset:offset+4])+S.Matrix([0,0,0,-rec['e']])*c[offset+4]
    assert ivec(clutch(rec['torsion_bounding_coefficients']))==rec['torsion_linking_loop']
    assert ivec(clutch(rec['critical_bounding_coefficients']))==rec['critical_linking_loop']
    assert rec['critical_linking']==rec['critical_linking_loop'][2]
    fc=rec['finite_core']
    if fc:
        chi=S.Matrix([fc['character']]);off=fc['column_offset']
        def pair(c):return int((chi*S.Matrix(c[off:off+4]))[0]+fc['root_character']*c[off+4])
        assert pair(rec['torsion_bounding_coefficients'])==fc['torsion_linking']
        assert pair(rec['critical_bounding_coefficients'])==fc['critical_linking']
        assert gcd(fc['torsion_linking'],b)==1
        assert fc['n']-fc['m']*rec['e'] in (-1,1)
        assert fc['root_character']==-(fc['n']-fc['m']*rec['e'])*fc['r']*rec['e']
        assert fc['critical_scalar']==kval
        assert fc['critical_linking']==(fc['n']-fc['m']*rec['e'])*rec['critical_cycle_order']*kval//b
    original=rr['profile']=='II' and not rec['finite']
    corrected=next(v for v in rr['variants'] if v['original_II']==original)
    print('OLD_REPLAY',index,'pattern',rec['pattern'],'key',rec['key'],'e',rec['e'],
          'finite_parameters',rec.get('canonical_parameters'),
          'K_old',kval,'K_actual',corrected['q'],'P_old',(-kval//2)%b,
          'P_actual',corrected['P'],'regular_link',rec['critical_linking'],
          'core_link',fc['critical_linking'] if fc else None,
          'root_character',fc['root_character'] if fc else None)

# Replay every old constant certificate and give the exact corrected replacement.
assert len(symbolic['rows'])==11
certificates=[];changed=0
for rec in symbolic['rows']:
    rr=new_by[tuple(rec['key'])];a,b=rr['a'],rr['b'];Om=S.Matrix([[a,0,0,0,0,-b]])
    R=S.Matrix(rec['fibre_relation_matrix']);s=S.Matrix(rec['standard_fibre_generator'])
    Rnew=S.Matrix(rr['relation_matrix']);assert R==S.zeros(6).row_join(Rnew)
    assert (Om*s)[0]==1
    oldcrit=S.Matrix(old_by_pattern[rec['pattern']]['critical_cycle'])
    assert R*S.Matrix(rec['critical_difference_coefficients'])==oldcrit-rec['critical_scalar']*s
    assert R*S.Matrix(rec['ordinary_difference_coefficients'])==biv(E[:,2],E[:,3])+b*s
    assert rec['delta_bar_corrections_zero'] and rec['peripheral_delta_sweeps_sum_zero']
    if rec['finite']:
        ell=S.Matrix(rec['fixed_long'])
        assert R*S.Matrix(rec['finite_difference_coefficients'])==-biv(E[:,2],ell)-b*s
    original=rr['profile']=='II' and not rec['finite']
    actual=next(v for v in rr['variants'] if v['original_II']==original)
    difference=S.Matrix(actual['total'])-actual['q']*s
    Fi=S.Matrix(rr['fibre_inverse']);Q=S.Matrix(rr['relation_section'])
    cnew=S.zeros(6,1).col_join(Q*(Fi*difference)[1:,0])
    assert R*cnew==difference
    pold=(-rec['critical_scalar']//2)%b
    changed+=int(pold!=actual['P'])
    cert=dict(pattern=rec['pattern'],key=rec['key'],finite=rec['finite'],
              old_K=rec['critical_scalar'],new_K=actual['q'],old_P=pold,new_P=actual['P'],
              generator=ivec(s),old_critical=ivec(oldcrit),new_critical=actual['total'],
              new_critical_difference=ivec(cnew))
    certificates.append(cert)
    print('CONSTANT_CERTIFICATE',json.dumps(cert,sort_keys=True))
assert changed==8

# The complete integer Thom relation maps; both signs, no parameter bound.
m,e,r,b=S.symbols('m e r b',integer=True)
for sigma in (-1,1):
    n=m*e+sigma
    C1,C2,C3,Ge=S.Matrix([b*n,m,0]),S.Matrix([-b*r,0,m]),S.Matrix([0,r,n]),S.Matrix([b*e,1,0])
    E1,E2,E3=sigma*(C1-m*Ge),Ge,sigma*(C3-r*Ge-e*C2)
    assert S.simplify(E1-S.Matrix([b,0,0]))==S.zeros(3,1)
    assert S.simplify(E3-S.Matrix([0,0,1]))==S.zeros(3,1)
    for lhs,rhs in ((C1,sigma*E1+m*E2),(C2,-r*E1+m*E3),(C3,-e*r*E1+r*E2+n*E3)):
        assert S.simplify(lhs-rhs)==S.zeros(3,1)
    chi_ell,chi_g=-sigma*r,-sigma*r*e
    assert S.expand(m*chi_g-r-n*chi_ell)==0
    assert S.expand((-sigma*e)*m+sigma*n)==1
    print('ALL_INTEGER_CORE_MAPS sigma',sigma,'chi=(1,-sigma*r,-sigma*r*e), t=sigma*(g-e*ell), inverse ell=-sigma*r*delta+m*t; g=-sigma*r*e*delta+n*t PASS')
for bb in (4,8,20):
    odd=bb
    while odd%2==0:odd//=2
    for k in range(24):assert (odd*k)%2==k%2
    assert bb//gcd(bb,odd) in (4,8)
    print('ADMISSIBILITY_COEFFICIENT_MAP b',bb,'odd_multiple',odd,'parity inverse is identity mod2; geometry proved in post-exposure note')
for xx in range(20):
    assert (5*(xx%4)+16*(xx%5))%20==xx
    assert (5*(xx%4)+4*((4*xx)%5))%20==xx
print('BOTH_CRT_MAPS coefficient inverse (x4,x5)->5*x4+16*x5; model marking inverse x->(x mod4,4*x mod5) PASS')
out=LANE/'S6_SERIES_PUBLISH_III_02LM_post_exposure_data_v001.json'
with out.open('x') as f:json.dump(dict(scope='post-exposure arithmetic and exact maps',certificates=certificates,changed_patterns=changed),f,indent=2);f.write('\n')
print('CHANGED_PATTERN_COUNT',changed,'OF',len(certificates))
print('OUTPUT_SHA256',sha256(out.read_bytes()).hexdigest())
print('LIMIT: historical full global Smith matrices were neither reconstructed nor executed; stored pairing coordinates and all eleven constant R-preimages were checked. The receiving proof supplies the actual geometric chains and unbounded maps.')
