"""Exact matrix and period checks for independently reviewed Paper II proofs.

These certificates verify the stated algebra. They do not replace the
geometric construction, properness, canonical-line, or source checks.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

OUT = Path(__file__).resolve().parents[2] / 'analysis'
I = s.eye(4)

def rows(M):
    return [[str(x) for x in row] for row in M.tolist()]

def smith(M):
    D = smith_normal_form(M, domain=s.ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape))]

B = [s.Matrix(x) for x in [
    [[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]],
    [[1,0,6,3],[0,1,2,1],[0,0,1,0],[0,0,0,1]],
    [[1,0,0,0],[0,2,1,0],[0,-1,0,0],[0,0,0,1]],
    [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
]]
assert B[0]*B[1]*B[2]*B[3] == I
assert B[0]**3 == I
BH = [b.inv().T for b in B]
BC = s.Matrix.vstack(*[b-I for b in B])
BW = s.Matrix.hstack(*[h-I for h in BH])
assert len(BC.nullspace()) == 1
assert smith(BW) == [1,1,1,0]

t,x,y,u = s.symbols('t x y u', real=True)
P = s.Matrix([[1,s.I,t,s.I*t],[-t,s.I*t,1,-s.I]])
Q = s.Matrix([[-s.I*t,-t,s.I,1],[-s.I,1,-s.I*t,t]])
assert Q*P.T == s.zeros(2)
qminors = [s.expand(Q[:,[a,b]].det()) for a in range(4) for b in range(a+1,4)]
assert s.gcd_list(qminors) == 1
Pinf = (u*P.subs(t,1/u)).applyfunc(s.simplify)
Qinf = (u*Q.subs(t,1/u)).applyfunc(s.simplify)
assert Pinf.subs(u,0).rank() == 2
assert Qinf.subs(u,0).rank() == 2
Pr = s.Matrix([[1,0,x,-y],[0,1,y,x],[-x,-y,1,0],[-y,x,0,-1]])
real_det = s.factor(Pr.det())
assert s.expand(real_det + (1+x*x+y*y)**2) == 0

T = [s.Matrix(z) for z in [
    [[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
    [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
    [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
    [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
]]
H = [q.inv().T for q in T]
assert T[0]*T[1]*T[2]*T[3] == I
assert T[0]**4 == I
for a in range(1,4):
    assert (T[a]-I)**2 == s.zeros(4)
assert [s.matrix2numpy(T[a]-I).shape for a in range(1,4)] == [(4,4)]*3
assert [(T[a]-I).rank() for a in range(1,4)] == [1,1,2]
Cvars = s.symbols('c:16')
C = s.Matrix(4,4,Cvars)
equations = s.Matrix.vstack(*[(C*h-h*C).reshape(16,1) for h in H])
A = equations.jacobian(Cvars)
E41 = s.zeros(4); E41[3,0] = 1
assert len(A.nullspace()) == 2
assert all(C0*h == h*C0 for C0 in [I,E41] for h in H)
ell = s.Matrix([1,-1,-1,0]); delta=s.Matrix([0,0,0,1])
norm = sum([H[0]**j for j in range(4)],s.zeros(4))
fixed = s.Matrix.hstack(ell,delta)
norm_coords = s.Matrix([[4,0,0,0],[0,2,-2,4]])
assert norm == fixed*norm_coords
assert (H[0]-I)*fixed == s.zeros(4,2)
assert (H[0]-I).rank() == 2
assert hermite_normal_form(norm_coords) == s.diag(4,2)

e = [I[:,j] for j in range(4)]
K = [s.Matrix.hstack(e[2]+e[3]),s.Matrix.hstack(e[1]),s.Matrix.hstack(e[2],e[3])]
fixed_reduced = [s.Matrix.hstack(e[0]-2*e[1],e[2],e[3]),
                 s.Matrix.hstack(e[0],e[1],e[3]),K[2]]
for j in range(3):
    assert hermite_normal_form(H[j+1]-I) == hermite_normal_form(K[j])
    assert smith(H[j+1]-I) == ([1]*(j//2+1) + [0]*(3-j//2))
    assert (H[j+1]-I)*fixed_reduced[j] == s.zeros(4,fixed_reduced[j].cols)
    assert fixed_reduced[j].rank() == 4-(H[j+1]-I).rank()
    assert all(z == 1 for z in smith(fixed_reduced[j]))

n=s.symbols('n',integer=True); h=2*n
bstar= -h*s.Rational(1,4)*(e[1]+e[2])
Lstar=-h*s.Rational(1,2)*e[1]
L1=s.zeros(4,1);L2=h*s.Rational(1,2)*e[1];L3=-h*s.Rational(1,2)*e[2]
assert (I-H[0])*bstar == h*s.Rational(1,4)*delta+Lstar
assert Lstar+H[0]*L1+H[0]*H[1]*L2+H[0]*H[1]*H[2]*L3 == s.zeros(4,1)

report = {
 'scope':'Exact algebra only; geometric construction and analytic descent are separately reviewed.',
 'D.1.6':{'cohomology_product_identity':True,'finite_order':3,
           'invariant_basis':[rows(v) for v in BC.nullspace()],
           'homology_coinvariant_smith':smith(BW)},
 'D.1.15':{'B_times_P_transpose_zero':True,'B_minors':[str(q) for q in qminors],
            'minor_gcd':'1','real_period_determinant':str(real_det),
            'P_infinity':rows(Pinf.subs(u,0)),'B_infinity':rows(Qinf.subs(u,0))},
 'E.5.2':{'homology_matrices':[rows(q) for q in H],
          'centralizer_basis':['I','E41'],'centralizer_dimension':2,
          'nilpotent_ranks':[1,1,2],'norm_matrix':rows(norm),
          'norm_coordinate_hnf':rows(hermite_normal_form(norm_coords)),
          'actual_integral_images':[rows(hermite_normal_form(hh-I)) for hh in H[1:]],
          'fixed_lattice_basis_matrices':[rows(q) for q in fixed_reduced]},
 'E.5.3':{'even_h_root_translation_identity':True,'full_sphere_cocycle_identity':True},
 'verdict':'PASS'
}
(OUT/'II_independent_batch2_exact.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
