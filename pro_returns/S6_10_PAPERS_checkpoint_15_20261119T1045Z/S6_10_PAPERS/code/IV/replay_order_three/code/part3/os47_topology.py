"""Full exact topological calculation for M=7G-O, Q=2G on I7+III+2I1.

The proof of geometric realization, local charts, specialization lattices
and clutch sign is in notes/part3_os47.md.  This program independently
checks the rational elliptic input, modular cosets, all integer matrices,
primitive local images, parabolic complexes, and integral d2 maps.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r

def data(m):
    return [[int(v) for v in m.row(i)] for i in range(m.rows)]

def snf(m):
    d=smith_normal_form(m,domain=s.ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]

def exterior(m,q):
    ix=list(combinations(range(m.rows),q))
    return s.Matrix([[m.extract(i,j).det() for j in ix] for i in ix])

def contraction(ell,q):
    src=list(combinations(range(4),q));dst=list(combinations(range(4),q-1))
    out=s.zeros(len(dst),len(src))
    for j,v in enumerate(src):
        for k,i in enumerate(v):
            out[dst.index(v[:k]+v[k+1:]),j]+=(-1)**k*ell[i]
    return out

def pair(u,v):
    # Intersection of two two-forms in the lexicographic exterior basis.
    return u[0]*v[5]-u[1]*v[4]+u[2]*v[3]+u[3]*v[2]-u[4]*v[1]+u[5]*v[0]

t=s.symbols('t')
f=1+8*t+40*t*t+48*t**3
g=1+12*t+84*t*t+280*t**3+504*t**4
disc=s.factor(g*g-f**3)
assert disc==-1728*t**7*(64*t*t+13*t+2)
xG=1+4*t;yG=12*s.sqrt(3)*t*t
assert s.expand(yG*yG-xG**3+3*f*xG-2*g)==0

E=[s.Matrix(m) for m in [
    [[-5,26],[-1,5]], [[1,7],[0,1]],
    [[1,0],[-1,1]], [[-2,9],[-1,4]],
]]
assert E[0]*E[1]*E[2]*E[3]==s.eye(2)
assert E[0]**2==-s.eye(2)
FF,SS,RR=free_group('S,R');TT=SS*RR
modular=FpGroup(FF,[SS**2,RR**3])
subgroup=[TT**5*SS*TT**-5,TT**7,SS*TT*SS**-1,
          TT**3*SS*TT*SS**-1*TT**-3]
cosets=coset_enumeration_r(modular,subgroup,max_cosets=100)
cosets.compress();cosets.standardize()
assert cosets.n==9
permS=[row[0] for row in cosets.table]
permR=[row[2] for row in cosets.table]
permT=[permR[permS[i]] for i in range(9)]
def cycles(p):
    left=set(range(len(p)));out=[]
    while left:
        i=min(left);cy=[]
        while i in left:
            left.remove(i);cy.append(i+1);i=p[i]
        out.append(cy)
    return out
assert sorted(map(len,cycles(permS)))==[1,2,2,2,2]
assert sorted(map(len,cycles(permR)))==[3,3,3]
assert sorted(map(len,cycles(permT)))==[1,1,7]

T=[s.Matrix(m) for m in [
 [[1,-2,10,7],[0,-5,26,7],[0,-1,5,0],[0,0,0,1]],
 [[1,0,4,8],[0,1,7,14],[0,0,1,0],[0,0,0,1]],
 [[1,2,0,14],[0,1,0,0],[0,-1,1,-7],[0,0,0,1]],
 [[1,0,0,-1],[0,-2,9,0],[0,-1,4,0],[0,0,0,1]],
]]
assert T[0]*T[1]*T[2]*T[3]==s.eye(4)
assert T[0]**4==s.eye(4)
ell=s.Matrix([1,-1,4,0])
assert T[0].inv().T*ell==ell
assert ell[0]==1

# Symbolic completeness of the geometric lift, after normalizing k7=(2,0),
# kD=0 by a single change of Abel--Jacobi lift.
r=s.symbols('r',integer=True)
def jacobi(E,k,c):
    p,q,u,v=list(E);j,h=list(k)
    return s.Matrix([[1,2*(u*j-p*h),2*(v*j-q*h),c],
                     [0,p,q,7*j],[0,u,v,7*h],[0,0,0,1]])
kA=-E[0]*(s.Matrix([2,0])+E[1]*s.Matrix([0,r]))
TAzero=jacobi(E[0],kA,0)
cA=s.factor(-(TAzero**4)[0,3]/4)
actual_product=(jacobi(E[0],kA,cA)*T[1]*
                jacobi(E[2],s.Matrix([0,r]),14*r*r)*T[3])
central_equation=s.factor(actual_product[0,3])
assert s.expand(central_equation-7*(r+1)*(7*r+5))==0
assert [z for z in s.solve(central_equation,r) if z.is_integer]==[-1]

H=[u.inv().T for u in T]
nonfinite=s.Matrix.hstack(*[u-s.eye(4) for u in H[1:]])
assert snf(nonfinite)==[1,1,1]
assert s.Matrix([[1,0,0,0]])*nonfinite==s.zeros(1,12)
relations=s.Matrix.hstack(nonfinite,ell)
assert snf(relations)==[1,1,1,1]
finite_relation=s.zeros(5,5)
finite_relation[:4,:4]=H[0]-s.eye(4)
finite_relation[:4,4]=-ell;finite_relation[4,4]=4
assert snf(finite_relation)==[1,1,1]

inv={0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),
     2:s.Matrix([0,0,2,7,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinv={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),
       2:s.Matrix([[0,0,7,2,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
sp={0:1,1:4,2:2,3:2,4:4}
complexes={}
for q in range(5):
    W=[exterior(u,q) for u in T];n=W[0].rows
    d=[u-s.eye(n) for u in W]
    ambient=s.Matrix.vstack(*d);rel=s.Matrix.hstack(*d)
    local=[hermite_normal_form(u) for u in d]
    d0=s.Matrix.vstack(*[b.gauss_jordan_solve(a)[0] if b.cols else s.zeros(0,n)
                       for a,b in zip(d,local)])
    acc=s.eye(n);blocks=[]
    for u,b in zip(W,local): blocks.append(acc*b);acc=acc*u
    d1=s.Matrix.hstack(*blocks)
    assert d1*d0==s.zeros(n,n)
    assert sum(b.cols for b in local)==d0.rank()+d1.rank()
    assert snf(ambient)==[1]*(n-1)
    assert snf(rel)==[1]*(n-1)
    assert ambient*inv[q]==s.zeros(4*n,1)
    assert coinv[q]*rel==s.zeros(1,4*n)
    c={'exterior_matrices':[data(u) for u in W],
       'local_image_bases':[data(u) for u in local],
       'd0':data(d0),'d1':data(d1),
       'ranks_d0_d1':[d0.rank(),d1.rank()],
       'd0_ambient_smith':snf(ambient),'coinvariant_smith':snf(rel),
       'global_invariant':data(inv[q]),'coinvariant_projection':data(coinv[q]),
       'global_specialization_index':sp[q]}
    if q:
        C=contraction(list(ell),q)
        numerator=(coinv[q-1]*C*(sp[q]*inv[q]))[0]
        assert numerator==4
        c['contraction']=data(C);c['d2_numerator']=int(numerator);c['d2']=1
    complexes[q]=c

h=s.Matrix([0,-28,-7,2])
h2=s.Matrix([-28,-7,2,0,0,0])
v2=s.Matrix([4,1,0,1,0,0])
omega=inv[2]
assert omega==h2+7*v2
assert pair(h2,h2)==pair(v2,v2)==0 and pair(h2,v2)==2
assert (h.T*ell)[0]==0

out={'Weierstrass_f':str(f),'Weierstrass_g':str(g),'g_squared_minus_f_cubed':str(disc),
     'section_G':[str(xG),str(yG)],
     'elliptic_tuple':[data(u) for u in E],
     'modular_coset_table':cosets.table,'modular_cycles':{
         'order2':cycles(permS),'order3':cycles(permR),'cusp':cycles(permT)},
     'jacobi_tuple':[data(u) for u in T],
     'normal_function_cocycles':[[1,0],[2,0],[0,-1],[0,0]],
     'normalized_cA':str(cA),'completeness_equation':str(central_equation),
     'logarithmic_twist':list(map(int,ell)),
     'nonfinite_pi1_relations':data(nonfinite),'nonfinite_smith':snf(nonfinite),
     'all_fibre_pi1_relations':data(relations),'full_smith':snf(relations),
     'finite_fibre_H1_matrix':data(finite_relation),
     'finite_fibre_H1_smith':snf(finite_relation),
     'finite_H2_invariant_basis':[list(map(int,h2)),list(map(int,v2))],
     'finite_H2_intersection':[[0,2],[2,0]],
     'complexes':complexes,
     'cohomology':['Z',0,0,0,0,0,'Z'],
     'homology':['Z',0,0,0,0,0,'Z'],
     'page':{'degree':4,'genus':0,'fibres':{'I7':4,'I1':8},'chi':3,
             'signature':-24,'height_line_section':14,'section_intersection':4,
             'line_square':-14,'p_rel':-72,'page_index_expression':-4}}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print('The explicit Weierstrass equation and section are verified.')
print('Modular index and cycle types:',cosets.n,out['modular_cycles'])
print('Normalized section-lift completeness equation:',central_equation,'; unique integer solution r=-1.')
print('Jacobi product I, finite order4, primitive invariant logarithm verified.')
print('Nonfinite and full fundamental-group Smith forms:',snf(nonfinite),snf(relations))
for q,v in complexes.items():
    print('Exterior degree',q,'ranks',v['ranks_d0_d1'],
          'ambient Smith',v['d0_ambient_smith'],'specialization index',sp[q],
          'd2',v.get('d2','--'))
print('Integral homology:',out['homology'])
print('Page data:',out['page'])
print('Full integer data:',path)
