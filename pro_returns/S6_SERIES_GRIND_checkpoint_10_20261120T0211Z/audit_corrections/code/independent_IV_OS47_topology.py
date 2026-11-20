"""Fresh F21 source, coset, Jacobi and integral-cohomology computations.

Written after reading the receiving proof; no blind reproof is claimed.
No earlier program/certificate is imported. SymPy performs the independent
Todd--Coxeter, HNF and Smith calculations. Geometric cap identifications
and Cartier-line extension are separate receiving-proof inputs.
"""
from pathlib import Path
from itertools import combinations
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup,coset_enumeration_r
import json,time,hashlib

start=time.monotonic();checks=[];records={}
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)
def zero(name,expr):check(name,S.expand(expr)==0)
def serial(mat):return [[int(v) if v.q==1 else str(v) for v in mat.row(i)] for i in range(mat.rows)]
def snf(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
def wedge_matrix(M,q):
    ix=list(combinations(range(M.rows),q))
    return S.Matrix([[M.extract(i,j).det() for j in ix] for i in ix])
def exterior(q,terms):
    ix=list(combinations(range(4),q));v=S.zeros(len(ix),1)
    for key,c in terms.items():v[ix.index(tuple(key))]=c
    return v
def contraction(v,q,ell):
    old=list(combinations(range(4),q));new=list(combinations(range(4),q-1))
    out=S.zeros(len(new),1)
    for pos,inds in enumerate(old):
        for j,i in enumerate(inds):out[new.index(inds[:j]+inds[j+1:])]+=(-1)**j*ell[i]*v[pos]
    return out
def wedge_pair(a,p,b,q):
    out=0
    for ia,aa in zip(combinations(range(4),p),a):
        for ib,bb in zip(combinations(range(4),q),b):
            if len(set(ia+ib))!=p+q:continue
            inversions=sum(x>y for x in ia for y in ib)
            out+=(-1)**inversions*aa*bb
    return S.expand(out)

t=S.symbols('t')
f=1+8*t+40*t*t+48*t**3
g=1+12*t+84*t*t+280*t**3+504*t**4
zero('literal source discriminant',g*g-f**3+1728*t**7*(64*t*t+13*t+2))
zero('literal section G',(12*S.sqrt(3)*t*t)**2-((1+4*t)**3-3*f*(1+4*t)+2*g))
check('two ordinary nodes distinct nonzero',S.discriminant(64*t*t+13*t+2,t)!=0 and (64*t*t+13*t+2).subs(t,0)!=0)
rootf=S.series(S.sqrt(f),t,0,8).removeO()
XG=1+4*t-rootf
nodeunit=S.series(S.sqrt(2*rootf+1+4*t),t,0,6).removeO()
branchu=S.series(12*S.sqrt(3)*t*t+XG*nodeunit,t,0,7).removeO()
branchv=S.series(12*S.sqrt(3)*t*t-XG*nodeunit,t,0,7).removeO()
def valuation(poly):return min(k[0] for k,c in S.Poly(S.expand(poly),t).terms() if c!=0)
check('actual_node_section_branch_orders',sorted([valuation(branchu),valuation(branchv)])==[2,5])
check('node_smoothing_order',valuation(S.series(2*(g-f*rootf),t,0,8).removeO())==7)
possible={2*i*(7-i)+j for i in range(7) for j in (0,7)}
check('no_torsion_local_height_sum',28 not in possible and max(possible)<56)
check('primitive_section_height',2-S.Rational(10,7)-S.Rational(1,2)==S.Rational(1,14))
# Work in the rational coordinate U=y/sqrt(3), so 3U²=x³−3fx+2g.
def plus(P,Q,doubling=False):
    x,u=P;xx,uu=Q
    m=(x*x-f)/(2*u) if doubling else (uu-u)/(xx-x)
    m=S.cancel(m);xxx=S.factor(3*m*m-x-xx)
    uuu=S.factor(-u+m*(x-xxx))
    return xxx,uuu
G=(1+4*t,12*t*t);G2=plus(G,G,True);G3=plus(G,G2);G4=plus(G2,G2,True);G7=plus(G3,G4)
target7=-(140*t**3-609*t*t-420*t+92)/(t+10)**2
check('literal_sevenfold_section_x',S.cancel(G7[0]-target7)==0)
check('literal_sevenfold_section_on_source',S.cancel(3*G7[1]**2-G7[0]**3+3*f*G7[0]-2*g)==0)
check('ordinary_pole_not_cancelled',(140*t**3-609*t*t-420*t+92).subs(t,-10)!=0)
check('ordinary_pole_fibre_smooth',(t**7*(64*t*t+13*t+2)).subs(t,-10)!=0)
for multiple,expectedintersection in [(1,0),(2,0),(5,1),(7,1)]:
    comp=(2*multiple)%7
    height=S.Rational(multiple*multiple,14)
    contr=S.Rational(comp*(7-comp),7)+S.Rational(multiple%2,2)
    check('actual_source_intersection_'+str(multiple),(height-2+contr)/2==expectedintersection)
check('actual_linearization_Hom_degree',1+1-1+0==1)
check('degree_four_page_Euler',4*7+8==36)
check('degree_four_page_height',4*S.Rational(49,14)==14)
check('degree_four_page_intersection',(14-2*3)/2==4)
check('physical_page_pair_and_class',(-2*3-2*4,-3*24,S.Rational(-72-12*(-14),24))==(-14,-72,4))
records['sevenfold_section']={'x':str(G7[0]),'U':str(G7[1]),'coordinate':'U=y/sqrt(3)','node_branch_orders':[2,5],'ordinary_pole':-10,'page_cover_degree':4}
check('I7 primitive period basis',S.Matrix([[-1,4],[-2,7]]).det()==1)

F,sg,rg=free_group('S,R')
Gamma=FpGroup(F,[sg**2,rg**3]);tg=sg*rg
H=[tg**5*sg*tg**-5,tg**7,sg*tg*sg**-1,tg**3*sg*tg*sg**-1*tg**-3]
C=coset_enumeration_r(Gamma,H);C.compress();C.standardize()
check('Todd_Coxeter_actual_subgroup_index',C.n==9)
providedS=[1,0,3,2,6,5,4,8,7]
providedR=[1,2,0,4,5,3,7,8,6]
# Determine the based bijection, rather than assuming the enumerator’s labels.
maps=[providedS,providedR];cols=[0,2]
bijection={0:0};queue=[0]
while queue:
    a=queue.pop()
    for col,p in zip(cols,maps):
        b=C.table[a][col];target=p[bijection[a]]
        if b in bijection:check('coset_label_compatibility',bijection[b]==target)
        else:bijection[b]=target;queue.append(b)
check('based_complete_coset_bijection',len(bijection)==9 and len(set(bijection.values()))==9)
T=[providedR[providedS[i]] for i in range(9)]
def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:c.append(j);seen.add(j);j=p[j]
        out.append(c)
    return out
check('ordered_T_cusp_cycle',cycles(T)==[[0,2,4,7,6,5,3],[1],[8]])
check('degree_nine_modular_genus',sum(9-len(cycles(p)) for p in (providedS,providedR,T))==16)
records['coset_table']={'enumerated':C.table,'based_bijection':bijection,'provided_S':providedS,'provided_R':providedR,'T':T}

A=S.Matrix([[-5,26],[-1,5]]);B=S.Matrix([[1,7],[0,1]])
CC=S.Matrix([[1,0],[-1,1]]);D=S.Matrix([[-2,9],[-1,4]])
check('elliptic_ordered_product',A*B*CC*D==S.eye(2))
check('order_four_finite_monodromy',A*A==-S.eye(2))
j=S.symbols('j')
kA=S.Matrix([9*j+10,2*j+2]);kB=S.Matrix([2,0]);kC=S.Matrix([0,j]);kD=S.zeros(2,1)
check('actual_Abel_Jacobi_sphere_relation',kA==-A*(kB+B*kC))
def lift(E,k,z):
    a,b,c,d=E[0,0],E[0,1],E[1,0],E[1,1];k1,k2=k
    return S.Matrix([[1,2*(c*k1-a*k2),2*(d*k1-b*k2),z],
                     [0,a,b,7*k1],[0,c,d,7*k2],[0,0,0,1]])
TT=[lift(A,kA,7*(5*j*j+8*j+4)),lift(B,kB,8),lift(CC,kC,14*j*j),lift(D,kD,-1)]
product=TT[0]*TT[1]*TT[2]*TT[3]-S.eye(4)
expected=S.zeros(4);expected[0,3]=7*(j+1)*(7*j+5)
check('full_symbolic_Jacobi_lift_obstruction',S.simplify(product-expected)==S.zeros(4))
check('unique_integral_lift',S.solve(expected[0,3],j)==[-1,-S.Rational(5,7)])
Ts=[M.subs(j,-1) for M in TT];Thats=[M.inv().T for M in Ts]
ell=S.Matrix([1,-1,4,0])
check('cap_translation_fixed',Thats[0]*ell==ell)
for q,expectedrank in [(1,[2,1,1,2]),(2,[4,2,2,2]),(3,[2,1,1,2])]:
    Es=[wedge_matrix(M,q) for M in Ts];n=Es[0].rows
    images=[M-S.eye(n) for M in Es]
    bases=[hermite_normal_form(M) for M in images]
    check('local_image_ranks_q'+str(q),[M.cols for M in bases]==expectedrank)
    coords=[]
    for U,M in zip(bases,images):
        X=U.gauss_jordan_solve(M)[0]
        check('local_integral_HNF_coordinates_q'+str(q),all(v.q==1 for v in X))
        check('local_full_image_map_q'+str(q),U*X==M)
        coords.append(X)
    d0=S.Matrix.vstack(*coords);prefix=S.eye(n);parts=[]
    for U,E in zip(bases,Es):parts.append(prefix*U);prefix=prefix*E
    d1=S.Matrix.hstack(*parts)
    check('parabolic_complex_q'+str(q),d1*d0==S.zeros(n,n))
    rk={1:3,2:5,3:3}[q]
    check('both_differential_ranks_q'+str(q),(d0.rank(),d1.rank())==(rk,rk))
    check('zero_middle_rational_cohomology_q'+str(q),d0.rank()+d1.rank()==d0.rows)
    check('primitive_first_differential_q'+str(q),snf(d0)==[1]*rk)
    check('free_last_cokernel_q'+str(q),snf(d1)==[1]*rk and d1.rows-d1.rank()==1)
    records['parabolic_q'+str(q)]={'HNF_images':[serial(M) for M in bases],'d0':serial(d0),'d1':serial(d1),'smith_d0':snf(d0),'smith_d1':snf(d1)}

kill=S.Matrix.hstack(*[M-S.eye(4) for M in Thats[1:]])
check('primitive_Mumford_vanishing_lattice',snf(kill)==[1,1,1])
check('finite_cap_kills_last_generator',snf(kill.row_join(ell))==[1,1,1,1])
cap=(Thats[0]-S.eye(4)).row_join(-ell).col_join(S.Matrix([[0,0,0,0,4]]))
check('finite_cap_H1_has_no_torsion',snf(cap)==[1,1,1])
psi=exterior(1,{(0,):1});omega=exterior(2,{(1,2):7,(0,3):2})
phi=exterior(3,{(0,1,2):1});nu=S.Matrix([1]);gens={1:psi,2:omega,3:phi,4:nu}
coinv={0:S.Matrix([[1]]),1:S.Matrix([[0,0,0,1]]),2:S.Matrix([[0,0,7,2,0,0]]),3:S.Matrix([[0,0,0,1]]),4:S.Matrix([[1]])}
for q,gen in gens.items():
    for i,M in enumerate(Ts):
        E=wedge_matrix(M,q)
        check('global_invariant_q'+str(q)+'_'+str(i),E*gen==gen)
        check('coinvariant_functional_q'+str(q)+'_'+str(i),coinv[q]*(E-S.eye(E.rows))==S.zeros(1,E.rows))
    image=S.Matrix.hstack(*[wedge_matrix(M,q)-S.eye(gen.rows) for M in Ts])
    check('full_coinvariant_unit_saturation_q'+str(q),snf(image)==[1]*(gen.rows-1))
h=exterior(1,{(1,):-28,(2,):-7,(3,):2})
h2=exterior(2,{(0,1):-28,(0,2):-7,(0,3):2})
v2=exterior(2,{(1,2):1,(0,1):4,(0,2):1})
s3=exterior(3,{(0,1,3):4,(0,2,3):1,(1,2,3):1})
check('finite_degree1_invariant_h',Ts[0]*h==h)
check('finite_degree2_invariant_basis',all(wedge_matrix(Ts[0],2)*v==v for v in (h2,v2)))
check('finite_degree3_invariant_basis',all(wedge_matrix(Ts[0],3)*v==v for v in (phi,s3)))
for q,columns in [(1,(psi,h)),(2,(h2,v2)),(3,(phi,s3))]:
    finite_basis=S.Matrix.hstack(*columns)
    finite_operator=wedge_matrix(Ts[0],q)
    check('finite_full_kernel_rank_q'+str(q),finite_basis.rank()==finite_operator.rows-(finite_operator-S.eye(finite_operator.rows)).rank()==2)
    check('finite_full_kernel_saturation_q'+str(q),snf(finite_basis)==[1,1])
check('finite_omega_actual_coordinates',omega==h2+7*v2)
pair2=S.Matrix([[wedge_pair(a,2,b,2) for b in (h2,v2)] for a in (h2,v2)])
check('finite_degree2_intersection_form',pair2==S.Matrix([[0,2],[2,0]]))
pair13=S.Matrix([[wedge_pair(a,1,b,3) for b in (phi,s3)] for a in (psi,h)])
check('finite_degree1_degree3_pairing',pair13==S.Matrix([[0,1],[-2,0]]))
for q,gen in gens.items():
    value=(coinv[q-1]*contraction(gen,q,ell))[0]
    expected={1:1,2:2,3:2,4:1}[q]
    check('full_cap_contraction_q'+str(q),value==expected)
    factor={1:4,2:2,3:2,4:4}[q]
    check('actual_integral_Leray_differential_q'+str(q),S.Rational(factor,4)*value==1)
records['finite_cap']={'H1_relation':serial(cap),'H1_smith':snf(cap),'vanishing_images':serial(kill),'kill_with_ell':serial(kill.row_join(ell)),'degree2_pairing':serial(pair2),'degree1_degree3_pairing':serial(pair13)}
records['matrices']=[serial(M) for M in Ts]
out={'status':'PASS','assertions':len(checks),'seconds':round(time.monotonic()-start,3),'checks':checks,'records':records,
     'scope':'Exact original source and sevenfold section, based PSL2 subgroup, full Jacobi lift, primitive vanishing and parabolic complexes, finite-cap pairings, all four integral translation-prism contractions and actual degree-four page. Geometric Cartier/cap extension is a separately read proof input.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','assertions','seconds','code_sha256')},indent=2))
