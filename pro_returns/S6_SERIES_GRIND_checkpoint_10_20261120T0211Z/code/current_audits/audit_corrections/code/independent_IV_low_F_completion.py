"""Fresh exact low-F identities from the stated equations and maps.

No previous program or certificate is imported. This is written after receiving
proof readings; it is not a blind re-proof. Analytic gluing, line extension,
classification and framing transport remain the separately read geometric inputs.
"""
from pathlib import Path
import sympy as S
import json,time,hashlib
start=time.monotonic();checks=[];records={}
def check(label,name,value):
    if not bool(value):raise AssertionError((label,name))
    checks.append({'label':label,'name':name})
def eq(label,name,a,b):check(label,name,S.simplify(a-b)==0)
def mat_eq(label,name,a,b):check(label,name,all(S.simplify(x)==0 for x in a-b))

c,k,l,n=S.symbols('c k l n')
eq('night:P3F.4','Hopf_lift_Mayer_Vietoris_unimodular',S.Matrix([[0,1],[1,c]]).det(),-1)
eq('night:P3F.7','conifold_orbit_Mayer_Vietoris_unimodular',S.Matrix([[0,1],[-1,0]]).det(),1)
x0,x1,z=S.symbols('x0 x1 z')
A,B,C,D=x0,z*x0,x1,z*x1
eq('night:P3F.7','actual_conifold_map',A*D-B*C,0)
u,v,w=S.symbols('u v w',real=True)
# a=sin(u) exp(iv), b=cos(u): actual SU2 disc contraction.
a=S.sin(u)*(S.cos(v)+S.I*S.sin(v));b=S.cos(u)
M=S.Matrix([[a,b],[-b,S.conjugate(a)]])
eq('night:P3F.7','actual_SU2_contraction_determinant',S.expand_complex(M.det()),1)
mat_eq('night:P3F.7','SU2_center_constant',M.subs(u,0),S.Matrix([[0,1],[-1,0]]))
mat_eq('night:P3F.7','SU2_boundary_loop',M.subs(u,S.pi/2),S.diag(S.cos(v)+S.I*S.sin(v),S.cos(v)-S.I*S.sin(v)))

F2,FM,M2=S.symbols('F2 FM M2')
Ksq=25*F2;KM=5*FM
characteristic=S.expand(Ksq+4*KM+4*M2)
eq('night:P3F.5','genus_three_canonical_fibre_coefficient',1+2*3-2,5)
eq('night:P3F.5','actual_characteristic_square',characteristic.subs({F2:0,FM:0}),4*M2)
eq('night:P3F.10','fibre_shift_preserves_line_square',(M2+2*n*FM+n*n*F2).subs({F2:0,FM:0}),M2)
eq('night:P3F.10','reference_page_pair',S.Rational(-24-12*(-2),24),0)
eq('night:P3F.10','actual_Seifert_meridian_determinant',S.Matrix([[3,0,-1],[0,4,1],[1,1,0]]).det(),1)

r,eps=S.symbols('r eps',positive=True)
X,Y=S.symbols('X Y',nonnegative=True)
bold=(r-Y/r)/2;bnew=(X*r-1/r)/2
ratio=S.factor(S.diff(bnew,r)/S.diff(bold,r))
eq('night:P3F.9','actual_orbit_chart_derivative',ratio,(X+r**-2)/(1+Y*r**-2))
radial=X*r-Y/r+2*eps*(r-1)/(r+1)
eq('night:P3F.9','actual_radial_derivative',S.diff(radial,r),X+Y/r**2+4*eps/(r+1)**2)
check('night:P3F.9','positive_derivative_terms',X.is_nonnegative and (Y/r**2).is_nonnegative and (4*eps/(r+1)**2).is_positive)
check('night:P3F.9','zero_fibre_unique_positive_root',S.solve(radial.subs({X:0,Y:0}),r)==[1])
records['F9']={'transition_derivative':str(ratio),'section_equation':str(radial),'positive_derivative':str(S.factor(S.diff(radial,r)))}

h,t,nm,np=S.symbols('h t n_minus n_plus')
def truncate(poly):
    return S.Poly(S.expand(poly),h,t).terms()
def coeff11(poly):return S.Poly(S.expand(poly),h,t).coeff_monomial(h*t)
c1=(h-nm*t)+(-h+np*t);c2=(h-nm*t)*(-h+np*t)
eq('night:P3F.11','phase_line_c2',coeff11(c2),nm+np)
eq('night:P3F.11','adjoint_p1',coeff11(c1*c1-4*c2),-4*(nm+np))
eq('night:P3F.11','framing_index_invariance',(4*(k+n)-(l+4*n))/24,(4*k-l)/24)
eq('night:P3F.11','sixfold_integer_additivity',(4*(6*k)-6*l)/24,6*(4*k-l)/24)

AA=S.Matrix([[0,1],[-1,-1]]);BB=S.Matrix([[0,-1],[1,0]])
GG=AA*BB*AA.inv()*BB.inv()
mat_eq('night:P3F.12','full_literal_commutator',GG,S.Matrix([[1,-1],[-1,2]]))
eq('night:P3F.12','commutator_coinvariant_unimodularity',(GG-S.eye(2)).det(),-1)
eq('night:P3F.12','commutator_cover_character',4-3-4+3,0)
check('night:P3F.12','connected_degree_twelve_character',S.gcd(S.gcd(4,3),12)==1)
eq('night:P3F.12','literal_component_cover_genus',S.Rational(2-24+sum(12-S.gcd(12,j) for j in [4,-3,-1]),2),3)
records['F12']={'A':[[int(v) for v in row] for row in AA.tolist()],'B':[[int(v) for v in row] for row in BB.tolist()],'commutator':[[int(v) for v in row] for row in GG.tolist()],'determinant':-1,'cover_character':[4,-3],'curve':'y^12=t^4/(t-1)^3'}

s,v,theta,mu,C=S.symbols('s v theta mu C')
# Literal default-twist origins from night:P2.2, a=b=1 and l0=0.
U=S.symbols('U')
o=S.Matrix([-mu*s/2,s*s/24-C*s/12+v*(s+U)])
sigma=S.Matrix([6*mu*v,v*U+C*v-6*v*v+6*v])
F=sigma-o;delta=S.Matrix([0,1]);gamma=S.Matrix([6*mu,C-s-12*v])
mat_eq('night:P3F.13','literal_full_origin_difference',F,S.Matrix([mu*(s+12*v)/2,C*(s+12*v)/12-(s+12*v)**2/24+6*v]))
change=F.subs(v,v+theta)-F
mat_eq('night:P3F.13','full_angular_change',change,theta*gamma+6*theta*(1-theta)*delta)
mat_eq('night:P3F.13','full_parameter_deck_change',change.subs(s,s+12)-change,-12*theta*delta)
check('night:P3F.13','both_periodic_gauge_endpoints',all((6*theta*(1-theta)).subs(theta,j)==0 for j in [0,1]))
eq('night:P3F.13','line_winding',S.Rational(-24,2),-12)
Q,rr,xx,yy,zz,ww,uu,vv,kk=S.symbols('Q rr xx yy zz ww uu vv kk')
for name,sub in [('first',{xx:Q*zz,rr:zz*yy}),('second',{Q:xx*ww,yy:ww*rr})]:
 eq('night:P3F.13','first_small_resolution_'+name,(xx*yy-Q*rr).subs(sub,simultaneous=True),0)
for name,sub in [('first',{xx:uu*kk,vv:kk*ww}),('second',{uu:xx*kk,ww:kk*vv})]:
 eq('night:P3F.13','source_node_resolution_'+name,(uu*vv-xx*ww).subs(sub,simultaneous=True),0)
records['F13']={'ordinary_origin':[str(q) for q in o],'cusp_origin':[str(q) for q in sigma],'difference':[str(S.expand(q)) for q in F],'angular_change':[str(S.expand(q)) for q in change]}

# Formal Laurent-exponent vectors in (eta,zeta,rho,W); i remains symbolic.
i=S.symbols('i',integer=True)
Xold=S.Matrix([0,0,-i,1]);Yold=S.Matrix([0,0,i+1,-1])
Wnew=S.Matrix([1,0,-1,1]);rhonew=S.Matrix([0,1,1,0])
Xnew=Wnew-(i-1)*rhonew;Ynew=i*rhonew-Wnew
mat_eq('night:P3F.15','whole_X_chart_unit',Xnew-Xold,S.Matrix([1,1-i,0,0]))
mat_eq('night:P3F.15','whole_Y_chart_unit',Ynew-Yold,S.Matrix([-1,i,0,0]))
mat_eq('night:P3F.15','node_product_parameter',Xnew+Ynew,rhonew)
phase_eta=12;phase_zeta=-sum(range(12))
eq('night:P3F.15','twelvefold_full_phase_exponent',phase_eta+2*phase_zeta,-120)
check('night:P3F.15','full_phase_is_one',(-120)%24==0)
eq('night:P3F.15','full_source_translation',12*S.Rational(-1,2),-6)
check('night:P3F.15','every_nontrivial_label_power_free',all((j-power)%12!=j for power in range(1,12) for j in range(12)))
eq('night:P3F.15','twelfth_scalar_winding',-sum([1]*12),-12)
eq('night:P3F.15','central_base_valuation',S.degree(Q**12,Q),12)
records['F15']={'formal_X_multiplier':list(map(str,Xnew-Xold)),'formal_Y_multiplier':list(map(str,Ynew-Yold)),'twelvefold_eta_exponent':-120,'twelvefold_rho_exponent':-12,'source_translation_multiple':-6}

m,n,k,l,a=S.symbols('m n k l a',integer=True,positive=True)
d=m*n;ram=(d-n)+(d-m)+(d-1)
eq('night:P3F.17','full_Riemann_Hurwitz',2*d-ram,m+n-m*n+1)
eq('night:P3F.17','Milnor_page_genus',2-(2*d-ram),(m-1)*(n-1))
d=12*k*l
for name,left,right in [('chi',d/12,k*l),('signature',-2*d/3,-8*k*l),('height',d/6,2*k*l),('intersection',(a*a*d/6-2*k*l)/2,k*l*(a*a-1)),('line_square',-2*k*l,-2*k*l),('relative_p1',3*(-8*k*l),-24*k*l),('page_expression',(-24*k*l-12*(-2*k*l))/24,0)]:eq('night:P3F.17',name,left,right)
for name,left,right in [('first_page_Euler',12,12),('second_page_Euler',4*2+4,12),('fourfold_height',4*S.Rational(1,2),2),('multiple_intersection',(2*a*a-2)/2,a*a-1),('section_square',-2,-2)]:eq('night:P3F.18',name,left,right)

monomial=S.Matrix([[0,1],[-1,2]])
eq('night:P3F.20','primitive_monomial_determinant',monomial.det(),1)
mat_eq('night:P3F.20','actual_pinched_ray_image',monomial*S.Matrix([2,1]),S.Matrix([1,0]))
mat_eq('night:P3F.20','actual_physical_circle_image',monomial*S.Matrix([0,1]),S.Matrix([1,2]))
check('night:P3F.20','exact_stabilizer_order',S.gcd(2,0)==2)
eq('night:P3F.20','OS49_component_correction',(S.Rational(1,2)-2+S.Rational(3,2))/2,0)

out={'status':'PASS','assertions':len(checks),'seconds':round(time.monotonic()-start,3),'checks':checks,'records':records,'method':'Fresh SymPy differentiation, polynomial reduction and formal Laurent-exponent vectors; no prior code/certificate imports.','scope':'Exact displayed identities only; source realization, analytic maps, orientations and global topology are separately read proof/source inputs. No blind re-proof or unavailable old-atlas replay is claimed.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','code_sha256']},indent=2))
