#!/usr/bin/env python3
"""Exact actual I8+4I1 source and weighted sphere tuple, proved in P3K.10."""
from pathlib import Path
from itertools import combinations
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r

out=Path(__file__).resolve().parent
def data(m): return [[int(v) for v in m.row(i)] for i in range(m.rows)]
def snf(m):
    D=smith_normal_form(m,domain=s.ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def exterior(m,q):
    ix=list(combinations(range(m.rows),q))
    return s.Matrix([[m.extract(i,j).det() for j in ix] for i in ix])
def contraction(ell,q):
    src=list(combinations(range(4),q));dst=list(combinations(range(4),q-1))
    C=s.zeros(len(dst),len(src))
    for j,v in enumerate(src):
        for k,i in enumerate(v):
            C[dst.index(v[:k]+v[k+1:]),j]+=(-1)**k*ell[i]
    return C
def trans(v):
    p,q=v
    return s.Matrix([[1-p*q,p*p],[-q*q,1+p*q]])
def lift(E,k,z):
    p,q,r,t=list(E);j,h=list(k)
    return s.Matrix([[1,r*j-p*h,t*j-q*h,z],
                     [0,p,q,8*j],[0,r,t,8*h],[0,0,0,1]])

t,b,parameter=s.symbols('t b parameter')
R=t*t+parameter
f=R*R+b*t
g=R**3+s.Rational(3,2)*b*t*R+s.Rational(3,8)*b*b
disc=s.factor(g*g-f**3)
expected=s.Rational(3,4)*b*b*parameter*R*R+s.Rational(1,8)*b**3*t**3+s.Rational(9,8)*b**3*parameter*t+s.Rational(9,64)*b**4
assert s.expand(disc-expected)==0
assert s.expand(3*(b/2)**2-R**3+3*f*R-2*g)==0
f1=s.expand(f.subs({b:1,parameter:1}))
g1=s.expand(g.subs({b:1,parameter:1}))
disc1=s.factor(disc.subs({b:1,parameter:1}))
disc_poly=s.together(disc1).as_numer_denom()[0]
assert s.degree(disc_poly,t)==4
assert s.gcd(disc_poly,s.diff(disc_poly,t))==1
assert s.gcd(disc_poly,f1)==1
assert s.degree(s.together(disc.subs(parameter,0)).as_numer_denom()[0],t)==3
u,y=s.symbols('u y')
shifted=s.expand((R+u)**3-3*f*(R+u)+2*g)
assert s.expand(shifted-3*(u*t-b/2)**2-u*u*(u+3*parameter))==0

# Rational group law using y=sqrt(3)*Y.
def double(P):
    x,Y=P
    slope=s.cancel((x*x-f1)/(2*Y))
    xx=s.factor(3*slope*slope-2*x)
    YY=s.factor(-Y+slope*(x-xx))
    return xx,YY
point=(t*t+1,s.Rational(1,2))
points={'G':[str(v) for v in point]}
for n in (2,4,8):
    point=double(point)
    points[str(n)+'G']=[str(v) for v in point]
x8den=s.denom(s.cancel(point[0]))
assert s.gcd(x8den,disc_poly)==1

v=[s.Matrix(v) for v in [(1,0),(1,0),(-3,1),(0,1),(3,1)]]
E=[trans((1,0))**8]+[trans(tuple(w)) for w in v[1:]]
prod=s.eye(2)
for e in E: prod=prod*e
assert prod==s.eye(2)
# The I9 specialization has a unique trivalent modular dessin: three
# monogon loops attached to the three leaves of a three-star.
FF,SS,RR=free_group('S,R');TT=SS*RR
modular=FpGroup(FF,[SS**2,RR**3])
subgroup=[TT**9,TT**-3*SS*TT*SS**-1*TT**3,
          SS*TT*SS**-1,TT**3*SS*TT*SS**-1*TT**-3]
cosets=coset_enumeration_r(modular,subgroup,max_cosets=100)
cosets.compress();cosets.standardize()
assert cosets.n==12
permS=[row[0] for row in cosets.table]
permR=[row[2] for row in cosets.table]
permT=[permR[permS[i]] for i in range(12)]
def cycles(p):
    todo=set(range(len(p)));ans=[]
    while todo:
        i=min(todo);cy=[]
        while i in todo:todo.remove(i);cy.append(i+1);i=p[i]
        ans.append(cy)
    return ans
assert sorted(map(len,cycles(permS)))==[2]*6
assert sorted(map(len,cycles(permR)))==[3]*4
assert sorted(map(len,cycles(permT)))==[1,1,1,9]
f0=s.expand(f.subs({b:1,parameter:0}))
g0=s.expand(g.subs({b:1,parameter:0}))
discriminant0=s.factor(g0*g0-f0**3)
assert s.degree(f0,t)==4 and s.gcd(f0,s.diff(f0,t))==1
assert s.degree(g0,t)==6 and s.gcd(g0,s.diff(g0,t))==1
assert s.gcd(f0,g0)==s.gcd(f0,s.together(discriminant0).as_numer_denom()[0])==1
r,j,h=s.symbols('r j h',integer=True)
ks=[s.Matrix([3,0]),r*v[1],j*v[2],h*v[3],s.zeros(2,1)]
zs=[9,8*r*r,8*j*j,8*h*h,-1]
matrices=[lift(e,k,z) for e,k,z in zip(E,ks,zs)]
prod=s.eye(4)
for m in matrices:prod=prod*m
linear=s.solve([prod[1,3],prod[2,3]],[r,j],dict=True)
assert len(linear)==1
eq=s.factor(prod[0,3].subs(linear[0]))
solutions=s.Poly(eq,h).all_roots()
integer=[sol for sol in solutions if sol.is_integer]
assert len(integer)==1
sub={h:integer[0]}
sub.update({var:s.simplify(value.subs(sub)) for var,value in linear[0].items()})
T=[m.subs(sub) for m in matrices]
assert all(z.is_integer for m in T for z in m)
prod=s.eye(4)
for m in T:prod=prod*m
assert prod==s.eye(4)
local_ranks=[(m-s.eye(4)).rank() for m in T]
assert local_ranks==[1,1,1,1,2]
local_smith=[snf(m-s.eye(4)) for m in T]
assert local_smith==[[1],[1],[1],[1],[1,1]]

H=[m.inv().T for m in T]
relations=s.Matrix.hstack(*[m-s.eye(4) for m in H])
ell=s.Matrix([1,0,0,0])
assert snf(relations)==[1,1,1]
assert snf(s.Matrix.hstack(relations,ell))==[1,1,1,1]
invariants={0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),
            2:s.Matrix([0,0,1,8,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinvariants={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),
              2:s.Matrix([[0,0,8,1,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
complexes={}
for q in range(5):
    W=[exterior(m,q) for m in T];n=W[0].rows
    dif=[m-s.eye(n) for m in W]
    local=[hermite_normal_form(m) for m in dif]
    d0=s.Matrix.vstack(*[basis.gauss_jordan_solve(mat)[0] if basis.cols else s.zeros(0,n)
                        for mat,basis in zip(dif,local)])
    acc=s.eye(n);blocks=[]
    for mat,basis in zip(W,local):blocks.append(acc*basis);acc=acc*mat
    d1=s.Matrix.hstack(*blocks)
    assert d1*d0==s.zeros(n,n)
    assert sum(basis.cols for basis in local)==d0.rank()+d1.rank()
    ambient=s.Matrix.vstack(*dif);rel=s.Matrix.hstack(*dif)
    assert snf(ambient)==[1]*(n-1)
    assert snf(rel)==[1]*(n-1)
    assert ambient*invariants[q]==s.zeros(len(T)*n,1)
    assert coinvariants[q]*rel==s.zeros(1,len(T)*n)
    record={'exterior_matrices':[data(m) for m in W],
            'local_image_bases':[data(m) for m in local],
            'd0':data(d0),'d1':data(d1),
            'ranks_d0_d1':[d0.rank(),d1.rank()],
            'ambient_invariant_smith':snf(ambient),
            'coinvariant_smith':snf(rel),
            'invariant_generator':data(invariants[q]),
            'coinvariant_projection':data(coinvariants[q])}
    if q:
        C=contraction(list(ell),q)
        val=(coinvariants[q-1]*C*invariants[q])[0]
        assert val==1
        record['contraction']=data(C);record['d2']=int(val)
        any_clutch=s.symbols('ell_gamma ell_u ell_w ell_delta')
        symbolic=(coinvariants[q-1]*contraction(any_clutch,q)*invariants[q])[0]
        assert s.expand(symbolic-any_clutch[0])==0
        record['all_affine_origin_corrections']='The contraction is exactly ell_gamma; source and delta components make no contribution.'
    complexes[q]=record

all_zero_sites=[]
without_zero=[m.copy() for m in T]
without_zero[4][0,3]+=1
for site in range(1,5):
    case=[m.copy() for m in without_zero]
    case[site][0,3]-=1
    product=s.eye(4)
    for m in case:product=product*m
    assert product==s.eye(4)
    hom=[m.inv().T for m in case]
    rel=s.Matrix.hstack(*[m-s.eye(4) for m in hom])
    assert snf(rel)==[1,1,1]
    assert snf(s.Matrix.hstack(rel,ell))==[1,1,1,1]
    rows=[]
    for q in range(5):
        W=[exterior(m,q) for m in case];n=W[0].rows
        dif=[m-s.eye(n) for m in W]
        local=[hermite_normal_form(m) for m in dif]
        d0=s.Matrix.vstack(*[basis.gauss_jordan_solve(mat)[0] if basis.cols else s.zeros(0,n)
                            for mat,basis in zip(dif,local)])
        acc=s.eye(n);blocks=[]
        for mat,basis in zip(W,local):blocks.append(acc*basis);acc=acc*mat
        d1=s.Matrix.hstack(*blocks)
        assert d1*d0==s.zeros(n,n)
        assert sum(basis.cols for basis in local)==d0.rank()+d1.rank()
        assert snf(s.Matrix.vstack(*dif))==[1]*(n-1)
        assert snf(s.Matrix.hstack(*dif))==[1]*(n-1)
        assert snf(d0)==snf(d1)==[1]*(n-1)
        rows.append({'q':q,'ranks':[d0.rank(),d1.rank()],
                     'd0_smith':snf(d0),'d1_smith':snf(d1)})
    all_zero_sites.append({'zero_site_index':site,'jacobi_tuple':[data(m) for m in case],
                          'parabolic_checks':rows,'homology':['Z',0,0,0,0,0,'Z']})

report={
 'status':'Proved actual source marking, holomorphic sphere family and signed return in notes/part3_os45.md P3K.10.',
 'source_f':str(f1),'source_g':str(g1),'discriminant':str(disc1),
 'rationality_identity':'y^2=3*(u*t-b/2)^2+u^2*(u+3*s), u=x-(t^2+s)',
 'rational_parameters':'A=(y-sqrt(3)*(u*t-b/2))/u, B=(y+sqrt(3)*(u*t-b/2))/u; AB=u+3*s',
 'deformation_discriminant':str(disc),'section_multiples_in_y_over_sqrt3':points,
 'x8_denominator':str(s.factor(x8den)),'gcd_x8den_discriminant':1,
 'elliptic_tuple':[data(m) for m in E],
 'I9_specialization_f':str(f0),'I9_specialization_g':str(g0),
 'I9_specialization_discriminant':str(discriminant0),
 'modular_coset_table':cosets.table,
 'modular_cycles':{'order2':cycles(permS),'order3':cycles(permR),'cusp':cycles(permT)},
 'cocycle_linear_solution':{str(var):str(value) for var,value in linear[0].items()},
 'central_equation':str(eq),'all_roots':[str(sol) for sol in solutions],
 'unique_integer_root':int(integer[0]),
 'normal_function_cocycles':[data(k.subs(sub)) for k in ks],
 'jacobi_tuple':[data(m) for m in T],
 'local_ranks':local_ranks,'local_smith':local_smith,
 'smooth_order_one_log_clutch':data(ell),
 'homology_action_relations':data(relations),
 'homology_action_smith':snf(relations),
 'all_relations_smith':snf(s.Matrix.hstack(relations,ell)),
 'complexes':complexes,
 'all_four_I1_zero_sites':all_zero_sites,
 'integral_homology':['Z',0,0,0,0,0,'Z'],
 'actual_page':{'degree':1,'chi':1,'signature':-8,'line_height':8,
                   'line_section_intersection':3,'M_square':-8,
                   'actual_positive_return_index':-3}}
(out/'os45_tuple.json').write_text(json.dumps(report,indent=2)+'\n')
print('Weierstrass source, G, 2G, 4G, 8G and ordinary coincidence fibres verified.')
print('Cocycle solution',linear,'central equation',eq,'unique integer root',integer)
print('Tuple',report['jacobi_tuple'])
print('Local ranks and Smith forms',local_ranks,local_smith)
print('Fundamental-group relation Smith forms',snf(relations),snf(s.Matrix.hstack(relations,ell)))
for q,c in complexes.items():print('Exterior degree',q,'ranks',c['ranks_d0_d1'],'d2',c.get('d2'))
print('Integral homology',report['integral_homology'])
print('Geometric marking, every local comparison, actual positive return -3 and class25 are proved in P3K.10.')
