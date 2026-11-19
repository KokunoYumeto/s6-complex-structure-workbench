"""Exact OS49 IV*+II+I2 component-supported construction checks.

The local filling and integral specialization maps are proved in
notes/part3_os49_component.md.  The output does not assign a return index:
the actual cusp circle is K=3u+2gamma, and its page comparison is separate.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form


def data(a):
    return [[int(v) for v in a.row(i)] for i in range(a.rows)]


def smith(a):
    d = smith_normal_form(a, domain=s.ZZ)
    return [abs(int(d[i, i])) for i in range(min(d.shape)) if d[i, i]]


def wedge(a, q):
    ix = list(combinations(range(a.rows), q))
    return s.Matrix([[a.extract(i, j).det() for j in ix] for i in ix])


def contraction(ell, q):
    src = list(combinations(range(4), q))
    dst = list(combinations(range(4), q - 1))
    a = s.zeros(len(dst), len(src))
    for j, ix in enumerate(src):
        for k, b in enumerate(ix):
            a[dst.index(ix[:k] + ix[k+1:]), j] += (-1)**k * ell[b]
    return a


def pair(u, v):
    return (u[0]*v[5]-u[1]*v[4]+u[2]*v[3]
            +u[3]*v[2]-u[4]*v[1]+u[5]*v[0])


t = s.symbols('t')
f = t**3*(t-1)
g = t**4*(t-1)*(t-s.Rational(1,2))
xG, yG = t**2, t**2
assert s.factor(f**3-g**2) == -t**8*(t-1)**2/4
assert s.factor(f**3/(f**3-g**2)) == -4*t*(t-1)
assert s.expand(yG**2-xG**3+3*f*xG-2*g) == 0

E = [s.Matrix(a) for a in [
    [[-2,-3],[1,1]], [[1,1],[-1,0]], [[1,2],[0,1]],
]]
assert E[0]*E[1]*E[2] == s.eye(2)
assert E[0]**3 == s.eye(2) and E[1]**3 == -s.eye(2)

r = s.symbols('r', integer=True)
def jacobi(e,k,z):
    a,b,c,d = list(e)
    u,w = list(k)
    return s.Matrix([[1,3*(c*u-a*w),3*(d*u-b*w),z],
                     [0,a,b,u],[0,c,d,w],[0,0,0,1]])
kC = s.Matrix([r,0])
kA = -E[0]*E[1]*kC
TA0 = jacobi(E[0],kA,0)
zA = s.factor(-(TA0**3)[0,3]/3)
# Norm(phi) has divisor C0+C1=F at I2.
zC = (3*r*r-1)/2
prod = jacobi(E[0],kA,zA)*jacobi(E[1],s.zeros(2,1),0)*jacobi(E[2],kC,zC)
equation = s.factor(prod[0,3])
assert s.expand(equation-(r*r-1)/2) == 0
assert s.solve(equation,r) == [-1,1]

T = [s.Matrix(a) for a in [
    [[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]],
    [[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]],
    [[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]],
]]
assert T[0]*T[1]*T[2] == s.eye(4)
assert T[0]**3 == s.eye(4)
ell = s.Matrix([1,-1,0,0])
assert T[0].inv().T*ell == ell

inv = {0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),
       2:s.Matrix([0,0,3,1,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinv = {0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),
         2:s.Matrix([[0,0,1,3,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
sp = {0:1,1:3,2:1,3:1,4:3}
complexes = {}
for q in range(5):
    W = [wedge(a,q) for a in T]
    n = W[0].rows
    D = [a-s.eye(n) for a in W]
    ambient = s.Matrix.vstack(*D)
    rel = s.Matrix.hstack(*D)
    images = [hermite_normal_form(a) for a in D]
    d0 = s.Matrix.vstack(*[
        b.gauss_jordan_solve(a)[0] if b.cols else s.zeros(0,n)
        for a,b in zip(D,images)])
    acc = s.eye(n)
    blocks = []
    for a,b in zip(W,images):
        blocks.append(acc*b)
        acc = acc*a
    d1 = s.Matrix.hstack(*blocks)
    assert d1*d0 == s.zeros(n,n)
    assert all(v.q == 1 for v in d0)
    assert sum(a.cols for a in images) == d0.rank()+d1.rank()
    assert smith(ambient) == [1]*(n-1)
    assert smith(rel) == [1]*(n-1)
    assert smith(d0) == [1]*(n-1)
    assert ambient*inv[q] == s.zeros(3*n,1)
    assert coinv[q]*rel == s.zeros(1,3*n)
    record = {'exterior_matrices':[data(a) for a in W],
              'local_image_bases':[data(a) for a in images],
              'd0':data(d0),'d1':data(d1),
              'ranks_d0_d1':[d0.rank(),d1.rank()],
              'ambient_smith':smith(ambient),'coinvariant_smith':smith(rel),
              'global_invariant':data(inv[q]),
              'coinvariant_projection':data(coinv[q]),
              'global_specialization_index':sp[q], 'parabolic_H1':0}
    if q:
        C = contraction(list(ell),q)
        num = (coinv[q-1]*C*(sp[q]*inv[q]))[0]
        assert num == 3
        record.update(contraction=data(C),clutch_numerator=int(num),d2=1)
    complexes[q] = record

H = [a.inv().T for a in T]
nonfinite = s.Matrix.hstack(*[a-s.eye(4) for a in H[1:]])
full = s.Matrix.hstack(nonfinite,ell)
assert smith(nonfinite) == [1,1,1]
assert smith(full) == [1,1,1,1]
finite = s.zeros(5,5)
finite[:4,:4] = H[0]-s.eye(4)
finite[:4,4] = -ell
finite[4,4] = 3
assert smith(finite) == [1,1,1]
u2 = s.Matrix([0,-1,3,0,0,0])
v2 = s.Matrix([0,1,0,1,0,0])
assert inv[2] == u2+v2
assert pair(u2,u2) == pair(v2,v2) == 0 and pair(u2,v2) == 3

valuations = s.Matrix([[2,-3],[1,-1]])
basis = s.Matrix([[-1,3],[-1,2]]) # columns H=-u-gamma, K=3u+2gamma
assert valuations*basis == s.eye(2)
assert basis.det() == 1
assert basis.inv() == s.Matrix([[2,-3],[1,-1]])

ss,v,theta,D1,D2=s.symbols('s v theta D1 D2')
D=s.Matrix([D1,D2]);delta=s.Matrix([0,1])
K=D+(ss+6*v)*delta
sigma=v*D+3*v*(v-1)*delta
origin=-ss*D/6-ss**2*delta/12-ss*v*delta
F=s.simplify(sigma-origin)
assert s.simplify(origin.subs(v,v+1)-origin+ss*delta) == s.zeros(2,1)
assert s.simplify(sigma.subs(v,v+1)-sigma+ss*delta-K) == s.zeros(2,1)
assert s.simplify(F.subs(v,v+theta)-F-theta*K-3*theta*(theta-1)*delta) == s.zeros(2,1)
assert s.simplify(F.subs(ss,ss+6)-F-K-3*delta) == s.zeros(2,1)
assert s.simplify((F.subs(v,v+theta)-F).subs(ss,ss+6)-(F.subs(v,v+theta)-F)-6*theta*delta) == s.zeros(2,1)

out = {'weierstrass_f':str(f),'weierstrass_g':str(g),
       'f_cubed_minus_g_squared':str(s.factor(f**3-g**2)),
       'j_over_1728':str(s.factor(f**3/(f**3-g**2))),
       'section_G':[str(xG),str(yG)],
       'elliptic_tuple':[data(a) for a in E],
       'jacobi_tuple':[data(a) for a in T],
       'normal_function_completeness_equation':str(equation),
       'logarithmic_twist':list(map(int,ell)),
       'cusp_valuation_matrix':data(valuations),
       'cusp_new_period_basis':data(basis),
       'cusp_new_period_inverse':data(basis.inv()),
       'positive_angular_clutch':'theta*K+3*theta*(theta-1)*delta',
       'sixth_root_line_clutch_winding':6,
       'finite_H2_invariant_basis':[list(map(int,u2)),list(map(int,v2))],
       'finite_H2_intersection':[[0,3],[3,0]],
       'nonfinite_pi1_relations':data(nonfinite),
       'full_pi1_relations':data(full),
       'finite_H1_relation_matrix':data(finite),
       'finite_H1_smith':smith(finite),
       'complexes':complexes,
       'homology':['Z',0,0,0,0,0,'Z'],
       'return_index_status':'Unassigned: actual K-circle page comparison required',
       'compact_source_pullback':{'degree':3,'fibres':{'II':3,'I2':3},
               'chi':1,'signature':-8,'height_G':'1/2',
               'sum_local_contributions':'3/2','section_intersection':0}}
dest = Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print('Weierstrass equation, section, discriminant and j-map checked exactly.')
print('Actual Jacobi normalization equation:',equation,'; roots -1,+1.')
print('Cusp valuation determinant:',valuations.det(),'; new basis:',data(basis))
print('Fundamental-group Smith forms:',smith(nonfinite),smith(full))
for q,a in complexes.items():
    print('Exterior degree',q,'ranks',a['ranks_d0_d1'],
          'primitive Smith',a['ambient_smith'],
          'specialization',sp[q],'d2',a.get('d2','--'))
print('Integral homology:',out['homology'])
print('Return index remains unassigned pending the actual mixed-circle comparison.')
print('Full exact matrices:',dest)
