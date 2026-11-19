"""Actual two-torsion-pair mu2 quotient charts and fixed-stratum blowup."""
from pathlib import Path
from itertools import product,combinations
import sympy as s
import json
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def integers(M):
 check('integral matrix',all(q.q==1 for q in M))
 return [[int(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
rows=[]
Id=s.eye(4)
physical=s.Matrix([0,0,1,-1])
original=s.Matrix([[1,1,4,4]])
for j in range(4):
 gamma=[1,-1,j,-j-1];parity=[q%2 for q in gamma]
 odd=[i for i,q in enumerate(parity) if q];neutral=[i for i,q in enumerate(parity) if not q]
 check('three odd and one neutral',len(odd)==3 and len(neutral)==1)
 neutral=neutral[0]
 basis=s.Matrix.hstack(s.Matrix(parity)/2,Id[:,1],Id[:,2],Id[:,3])
 check('actual quotient lattice index2',basis.det()==s.Rational(1,2))
 parent=basis.inv();check('parent quotient cone determinant2',parent.det()==2)
 new=s.Matrix([1,0,0,0])
 invariant=[a for a in product(range(3),repeat=4) if 1<=sum(a)<=2 and sum(a[i]*parity[i] for i in range(4))%2==0]
 for pivot in odd:
  C=parent.copy();C[:,pivot]=new
  order=list(range(4))
  if C.det()<0:C.col_swap(2,3);order[2],order[3]=order[3],order[2]
  check('smooth child cone',C.det()==1)
  cover=basis*C
  invariant_rows=[]
  for a in invariant:
   out=s.Matrix([a])*cover
   check('nonnegative invariant generator',all(q.q==1 and q>=0 for q in out))
   invariant_rows.append([int(q) for q in out])
  others=[i for i in odd if i!=pivot]
  chars=[]
  rho=[0]*4;rho[pivot]=2;chars.append(rho)
  for i in others:
   a=[0]*4;a[i]=1;a[pivot]=-1;chars.append(a)
  a=[0]*4;a[neutral]=1;chars.append(a)
  explicit=s.Matrix(chars)*cover
  check('explicit quotient blowup chart is a coordinate permutation',
        all(q in (0,1) for q in explicit) and all(sum(explicit.row(i))==1 for i in range(4)) and all(sum(explicit.col(i))==1 for i in range(4)))
  w=C.inv()*physical
  check('physical weights integral',all(q.q==1 for q in w))
  expected=s.Matrix(chars)*physical
  check('physical action in explicit rho chart',explicit*w==expected)
  phases=s.Matrix(chars)*s.Matrix(gamma)
  check('square deck identified in mu2 quotient',all(int(q)%2==0 for q in phases))
  orders=original*cover-s.ones(1,4)
  check('original marked volume has integral nonnegative orders',all(q.q==1 and q>=0 for q in orders))
  new_index=next(i for i in range(4) if C[:,i]==new)
  check('exceptional original volume order2',orders[new_index]==2)
  eps=s.Matrix([[1,0,1,1]])*cover
  qnew=s.Matrix([[4,0,0,0]])*cover
  sig4=s.Matrix([[0,0,4,4]])*cover
  check('all base arrows integral and nonnegative',all(q.q==1 and q>=0 for q in list(eps)+list(qnew)+list(sig4)))
  check('exact base graph equation',qnew+sig4==4*eps)
  rows.append({'j':j,'mu4_cover_weights':gamma,'mu2_cover_weights':parity,'pivot_cover_coordinate':pivot,'neutral_cover_coordinate':neutral,'other_odd_coordinates':others,'rays_as_columns':integers(C),'cover_column_permutation':order,'invariant_generators':invariant,'invariant_monomial_matrix':invariant_rows,'explicit_coordinates':['rho','z_b','z_c','neutral'],'explicit_coordinate_character_rows_in_cover':chars,'explicit_coordinate_matrix':integers(explicit),'explicit_mu4_phase_powers':[int(q) for q in phases],'explicit_physical_weights':[int(q) for q in expected],'chart_physical_weights':[int(q) for q in w],'original_volume_orders':[int(q) for q in orders],'epsilon_exponents':[int(q) for q in eps],'q_new_exponents':[int(q) for q in qnew],'sigma_fourth_exponents':[int(q) for q in sig4]})
# The full translated source chart mixes its tangent coordinate with sigma.
A,B,C,X=s.symbols('A B C X',nonzero=True)
ideal_arrow=s.Matrix([[1,0,0],[0,A,B*X],[0,0,1/C]])
check('full fixed-ideal arrow invertible',s.factor(ideal_arrow.det()-A/C)==0)
t,z1,z2,rho=s.symbols('t z1 z2 rho')
vec=s.Matrix([t,t*z1,t*z2])
L=ideal_arrow*s.Matrix([1,z1,z2])
check('homogeneous fixed-ideal lift',(ideal_arrow*vec-t*L).applyfunc(s.expand)==s.zeros(3,1))
sx,sy,ss,aa,dd=s.symbols('source_X source_Y sigma a2 d')
curve=sy**2-sx**3-aa*sx**2-dd*sx-ss**2
xp=dd/sx+2*ss*(sy+ss)/sx**2
yp=ss-(sy+ss)*xp/sx
def oncurve_zero(expr):
 numerator=s.together(expr).as_numer_denom()[0]
 return s.rem(numerator,curve,sy)==0
check('full chord preserves the exact source cubic',oncurve_zero(yp**2-xp**3-aa*xp**2-dd*xp-ss**2))
Ds=3*sx**2+2*aa*sx+dd
Dt=3*xp**2+2*aa*xp+dd
J=s.diff(yp,sy)+s.diff(yp,sx)*2*sy/Ds
check('full invariant-differential Jacobian',oncurve_zero(J-Dt/Ds))
Achord=-xp/sx;Bchord=1-xp/sx
check('complete affine source tangent map',s.factor(yp-Achord*sy-Bchord*ss)==0)
quarter={sx:-sx,sy:-s.I*sy,ss:-s.I*ss,aa:-aa}
check('full quarter deck commutes with source X chord',s.simplify(xp.subs(quarter,simultaneous=True)+xp)==0)
check('full quarter deck commutes with source Y chord',s.simplify(yp.subs(quarter,simultaneous=True)+s.I*yp)==0)
for sign in (1,-1):
 at={sx:sign*s.I,sy:0,ss:0,aa:0,dd:1}
 check('exact two-torsion source-unit value',s.simplify(Achord.subs(at))==1 and s.simplify(Bchord.subs(at))==2)
 check('actual invariant-differential central unit',s.simplify((1/Ds).subs(at))==-s.Rational(1,2))
out={'status':'PASS','checks':len(checks),'checked_assertions':checks,'scope':'Both non-O/T two-torsion points, exchanged by the actual mu4 action, with their mu2 stabilizer. All twelve three-chart quotient blowups for j modulo4, full invariant polynomial maps, deck/physical weights, source base graph and original marked-volume orders. The actual source-mixing map is lifted by its preserved fixed-stratum ideal; no return is assigned.',
 'source_sections':'Xbar^2+a2 Xbar+d=0, Ybar=sigma=0; at chi=0 they are Xbar=+i and -i.',
 'full_source_ideal_map':'zeta_target=A*zeta_source+B*sigma, A a full holomorphic unit; sigma=X_line*Y_line. Even j has fixed ideal(chi,zeta,Y_line), odd j has(chi,zeta,X_line). Entire coefficients and inverse source map are retained.',
 'coarse_blowup':'The ideal is generated by all six quadratic products of the three odd coordinates. The cover blowup modulo mu2 has charts rho=t_pivot^2,z_b=t_b/t_pivot,z_c=t_c/t_pivot,neutral.',
 'full_ideal_chart_lift':'For odd column w=t*z and preserved-ideal matrix M, L=M*z. On target pivot beta: rho_target=rho*L_beta^2; z_target_gamma=L_gamma/L_beta. Full neutral-line multiplier retained.',
 'original_volume':'-8*(X_line*Y_line)^3*d(epsilon)^(-2)*u*dchi wedge dzeta wedge dX_line wedge dY_line; oriented quotient child unit is -4*d^-2*u.',
 'original_cover_log_character':[1,1,4,4],'rows':rows}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('checked_assertions','rows')},indent=2))
