"""Exact residual c=4,8 fixed-curve and integral support certificates.

All13 additive patterns on10 actual initial rows are checked. The C_c
isotropy outside the two fixed curves is trivial, so localization with
Z/c coefficients is valid. This script verifies the local inputs and
symbolic fixed-curve evaluations only. It does not decide the remaining
order-two refined Pontryagin invariant.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parents[1]
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
patterns=[r for r in json.loads((ROOT/'records/root_remaining_smooth_profiles.json').read_text())['nontrivial_c_patterns'] if r['c'] in (4,8)]
monos={key(r):r for r in json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']}
x,y,t=S.symbols('x y t',integer=True)
records=[];checks=0
for c in (4,8):
 rows=json.loads((ROOT/f'records/manifolds_c{c}_tate_markings.json').read_text())
 assert {tuple(r['key']) for r in rows}=={key(r) for r in patterns if r['c']==c}
 for rr in rows:
  K=tuple(rr['key']);row=monos[K];a,b=row['a'],row['b']
  assert a%2 and b==c and gcd(a,c)==1
  Om=S.diag(a*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-b],[b,0]]))
  q=lambda z:int(a*(z[0]+z[1]+z[0]*z[1]))%2
  for loc in row['local']:
   M=S.Matrix(loc['matrix']);assert M.T*Om*M==Om
   for v in product((0,1),repeat=4):assert q(M*S.Matrix(v))==q(v);checks+=1
  angular=S.Matrix.hstack(*(S.Matrix(s['toric_vanishing_basis']) for s in row['local'] if 'toric_vanishing_basis' in s))
  assert hermite_normal_form(angular)==S.eye(4)[:,:3]
  images=S.Matrix.hstack(*(S.Matrix(s['matrix'])-S.eye(4) for s in row['local']))
  assert hermite_normal_form(images)==S.eye(4)[:,:3]
  record={'c':c,'key':K,'local':[]};fixed=[]
  for loc in rr['local']:
   n,j,rho=loc['valuations'];P=S.Matrix(loc['period_matrix'])
   C=S.Matrix(loc['basis']);M=S.Matrix(row['local'][loc['site']]['matrix'])
   adapted=S.eye(4);adapted[0,1]=n;adapted[0,3]=-b*j;adapted[2,1]=a*j;adapted[2,3]=rho
   assert C.det()==1 and C.inv()*M*C==adapted
   assert P==S.Matrix([[n,-b*j],[a*j,rho]])
   item=dict(site=loc['site'],type=loc['type'],zero=loc['zero'],valuations=[n,j,rho])
   if loc['zero']:
    assert P.det()==1
    phi=S.expand((-a*rho*x*x-2*a*b*j*x*y+b*n*y*y+a*x)/2)
    assert S.expand(phi.subs({x:x+n,y:y+a*j},simultaneous=True)-phi)==-a*x
    assert S.expand(phi.subs({x:x-b*j,y:y+rho},simultaneous=True)-phi)==b*y+S.Rational(b*rho-a*b*j,2)
    vertical=S.Poly(S.expand(phi.subs(y,y+1)-phi),x,y)
    assert all(int(vertical.coeff_monomial(v))%c==0 for v in (x,y))
    assert int(vertical.coeff_monomial(1))%c==c//2
    val=lambda xx,yy:phi.subs({x:xx,y:yy})
    signed_wall=val(1,0)+val(-1,1)-val(0,0)-val(0,1)
    assert gcd(int(signed_wall),c)==1
    item.update(support=str(phi),character=c//2,signed_wall=int(signed_wall),curve_normalized_alpha=1)
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
    stabilizer=gcd(abs(u1),c)
    assert stabilizer in (1,c)
    item.update(primitive=list(nu),support=str(phi1),cyclic_stabilizer=stabilizer)
    if stabilizer==c:
     assert n==c and gcd(a*j,c)==1 and al==1
     w=pow(a*j,-1,c)
     slope=S.expand(phi1.subs(t,t+1)-phi1)
     assert all(int(v)%c==0 for v in S.Poly(slope,t).coeffs())
     assert w*w%c==1
     item.update(normal_weight=w,character=0)
     fixed.append(item)
   record['local'].append(item)
  assert len(fixed)==1
  w=fixed[0]['normal_weight'];alpha_E=-w*w%c
  cube=3*(c//2)**2%c
  lam=-(1+alpha_E)%c
  assert cube==lam==0
  record.update(curve_normalized_elliptic_alpha=alpha_E,mu_mod_c=cube,
                spin_lambda=lam,remaining_refined_p=[0,c//2],
                full_smooth_type='Unresolved order-two refinement; no choice between the two candidates is asserted')
  records.append(record)
  print('ROW',K,'c',c,'normal weight',w,'cube0 spin-lambda0 PASS',flush=True)
assert len(patterns)==13 and len(records)==10
result={'scope':__doc__,'patterns':patterns,'rows':records,'semicharacter_tests':checks}
(ROOT/'records/fourfolds_D2_2power_AH.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('ALL13 PATTERNS /10 ROWS;',checks,'EXACT SEMICHARACTERS; FULL MOD-c CUBE AND SPIN-LAMBDA CERTIFICATES PASS',flush=True)
