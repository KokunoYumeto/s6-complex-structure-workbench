#!/usr/bin/env python3
"""Independent exhaustive field/map comparison of the pinned LK JSON."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
import json
from math import gcd
from pathlib import Path

from sympy import Matrix, Rational, diag, eye, simplify, symbols, zeros
from S6_SERIES_PUBLISH_c7_lk_lattices_v1 import one_lattice, positive_smith, preimage
from S6_SERIES_PUBLISH_c7_lh_integral import exterior, integral, rows

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_general_cusp_receiving"
P = "S6_SERIES_PUBLISH_III_02LK_"
path = LANE/(P+"historical_manifolds_general_cusp.json")
assert sha256(path.read_bytes()).hexdigest() == "158174459afada4c5381235fc0bf64efa0a87e68267c360b9e3274fc2d5b84c6"
old = json.loads(path.read_text())
assert set(old) == {"symbolic", "cases"}
x, y = symbols("x y")
a0, b0 = x-1, y-1
B = Matrix([[-1/x,-1,-1/x,-1/x],[1,1,1,y],[-x*y,-x*y,-1,-x*y]])
U = Matrix([[-x,0,0],[x,1,0],[0,x*y,1]])
V = Matrix([[1,-x,-1,-1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
F = Matrix([[1-x,0],[0,x*y-1],[y-1,x*y*(y-1)]])
R = zeros(3,4)
R[0,0], R[1:,1:] = 1, F.T
T = Matrix([[0,0,-1/x],[-1/(x*y*y),1/(x*y),-1/(x*x*y)],[-1/y,0,0]])
S = Matrix([[y,x*y*y],[x,0]])
C = Matrix([[-b0,0],[a0,-b0],[0,a0]])
g = Matrix([[a0*a0,a0*b0,b0*b0]])

def clean(M):
    return M.applyfunc(simplify)

def bar(M):
    return clean(M.subs({x:1/x,y:1/y}, simultaneous=True))

def equal(A,B):
    assert A.shape == B.shape and clean(A-B) == zeros(*A.shape)

equal(U*B*V, R)
assert simplify(U.det()) == -x and V.det() == 1
equal(U*U.inv(), eye(3))
equal(V*V.inv(), eye(4))
equal(T.inv()*F, C*S)
old_generator = Matrix([[-(x*y-1)*(y-1),-x*y*(1-x)*(y-1),(1-x)*(x*y-1)]])
equal(old_generator*T, g)
expected_symbolic = dict(
    ring="Z[x^+-1,y^+-1]", opposite_weights=["x^-1","y","xy"],
    restriction=str(B), left=str(U), right=str(V), cancelled=str(R),
    target_change=str(T), source_change=str(S),
    hilbert_burch=str(C), ideal="(x-1,y-1)^2")
# The recorded cancellation keeps a polynomial expression equal to zero.
# Parse only integer Laurent expressions and Matrix(list), then prove equality.
def recorded_expression(text):
    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return Rational(node.value)
        if isinstance(node, ast.Name) and node.id in ("x","y"):
            return x if node.id == "x" else y
        if isinstance(node, (ast.List,ast.Tuple)):
            return [visit(value) for value in node.elts]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd,ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op,ast.UAdd) else -value
        if isinstance(node,ast.BinOp):
            left,right = visit(node.left),visit(node.right)
            if isinstance(node.op,ast.Add): return left+right
            if isinstance(node.op,ast.Sub): return left-right
            if isinstance(node.op,ast.Mult): return left*right
            if isinstance(node.op,ast.Div): return left/right
            if isinstance(node.op,ast.Pow):
                assert right.is_Integer
                return left**right
        if (isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
            and node.func.id == "Matrix" and len(node.args) == 1 and not node.keywords):
            return Matrix(visit(node.args[0]))
        raise AssertionError(ast.dump(node))
    return visit(ast.parse(text,mode="eval"))

assert set(old["symbolic"]) == set(expected_symbolic)
for key in ("ring","opposite_weights","ideal"):
    assert old["symbolic"][key] == expected_symbolic[key]
for key,expected in (("restriction",B),("left",U),("right",V),("cancelled",R),
                     ("target_change",T),("source_change",S),("hilbert_burch",C)):
    equal(recorded_expression(old["symbolic"][key]),expected)
print("PASS all 10 symbolic JSON fields and exact Laurent operations/inverses", flush=True)

# Chain maps from this historical cancellation, with the homology involution.
L4, R3 = bar(V.T), bar(U.T)
d = bar(B.T)
D0 = diag(x**-2,(x*y)**-1,y**-2)
E0 = diag(-1/(x*x*y),-1/(x*y*y))
p, inc = eye(4)[1:,:], eye(4)[:,1:]
Q = clean(D0*bar(T).inv()*p*L4)
section = clean(L4.inv()*inc*bar(T)*D0.inv())
source_forward = clean(E0*Matrix.hstack(zeros(2,1),bar(S))*R3.inv())
source_inverse = clean(R3*Matrix.vstack(zeros(1,2),bar(S).inv()*E0.inv()))
H = clean(R3[:,0]*L4[0,:])
equal(Q*section, eye(3))
equal(section*Q, eye(4)-d*H)
equal(Q*d, C*source_forward)
equal(section*C, d*source_inverse)
equal(source_forward*source_inverse, eye(2))
equal(source_inverse*source_forward+H*d, eye(3))
print("PASS historical bar-transpose -> I^2: both chain maps and both homotopies", flush=True)

parameters = [(a,b,c) for a in range(1,6) for c in range(1,6) for b in range(a)]
assert len(old["cases"]) == len(parameters) == 75
keys = {"lattice","index","smith","normalization_H2","cap_H2","boundary_H2",
        "regular_fibre_image","monodromy","full_fibre_kernel_generators","component_meridians"}
answers = []
for number, ((a,b,c), row) in enumerate(zip(parameters, old["cases"]), 1):
    assert set(row) == keys
    L = Matrix([[a,b],[0,c]])
    D, s = a*c, gcd(a,b,c)
    t = D//s
    fresh = one_lattice(a,b,c)
    assert row["lattice"] == fresh["L"] == rows(L)
    assert row["index"] == fresh["index"] == D
    assert row["smith"] == fresh["smith"] == [s,t]
    for old_key, fresh_key in (("normalization_H2","normalization_coker"),
                               ("cap_H2","cap_H2"),("boundary_H2","boundary_H2")):
        free,torsion = fresh[fresh_key]
        assert row[old_key] == {"free":free,"torsion":torsion}
    assert row["regular_fibre_image"] == {"free":4,"torsion":([s] if s>1 else [])}

    A = eye(4)
    A[:2,2:] = L
    assert row["monodromy"] == rows(A)
    W = exterior(A)-eye(6)
    angular = eye(6)[:,0]
    Kold = Matrix(row["full_fibre_kernel_generators"])
    assert Kold == Matrix.hstack(W,angular)
    Kfresh = Matrix(fresh["fibre_kernel"])
    basis = Matrix(fresh["period_basis"])
    basis_inverse = Matrix(fresh["period_basis_inverse"])
    quotient = Matrix(fresh["wedge_quotient_basis"])
    quotient_inverse = Matrix(fresh["wedge_quotient_inverse"])
    assert basis*basis_inverse == eye(4)
    assert quotient*quotient_inverse == eye(6)
    marked = quotient_inverse*exterior(basis_inverse)*Kold
    assert marked[2:,:] == zeros(4,7)
    forward = integral(diag(1,Rational(1,s))*marked[:2,:])
    assert Kfresh*forward == Kold
    backward = preimage(Kold,positive_smith(Kold),Kfresh)
    assert Kold*backward == Kfresh
    assert forward*backward == eye(2)
    assert Kold*(backward*forward-eye(7)) == zeros(6,7)

    old_values = [(i,j) for i in range(a) for j in range(c)]
    new_values = [tuple(v) for v in fresh["components"]]
    permutation = zeros(D)
    for j,v in enumerate(new_values):
        permutation[old_values.index(v),j] = 1
    assert permutation.T*permutation == eye(D)
    meridians = Matrix(row["component_meridians"])
    assert meridians == Matrix([[i for i,j in old_values],
                               [j for i,j in old_values],[1]*D])
    Us = basis_inverse.extract([0,2],[0,1])
    Vs = basis.extract([2,3],[1,3])
    assert Us*L*Vs == diag(s,t)
    target = zeros(3)
    target[0,2],target[1:,:2] = 1,Us
    target_inverse = integral(target.inv())
    assert target*target_inverse == eye(3)
    old_rel = Matrix.vstack(L,zeros(1,2))
    new_rel = Matrix([[0,0],[s,0],[0,t]])
    assert target*old_rel*Vs == new_rel
    transformed = target*meridians*permutation
    reduced = transformed.copy()
    for j in range(D):
        reduced[1,j] %= s
        reduced[2,j] %= t
    corrections = integral(diag(Rational(1,s),Rational(1,t))*(transformed-reduced)[1:,:])
    assert transformed == reduced+new_rel*corrections
    DK = Matrix(fresh["disc_basis"])
    DI = (Matrix([[Rational(v) for v in rr] for rr in fresh["disc_inverse"]])
          if D>1 else zeros(0,1))
    assert DI*DK == eye(D-1)
    old_kernel, old_inverse = permutation*DK, DI*permutation.T
    augmented = Matrix.hstack(meridians,-old_rel)
    adecomp = positive_smith(augmented)
    assert adecomp[-1] == 3
    projected = adecomp[2][:D,3:]
    coefficients = integral(old_inverse*projected)
    assert old_kernel*coefficients == projected
    assert old_inverse*old_kernel == eye(D-1)
    assert augmented*adecomp[2][:,3:] == zeros(3,D-1)
    answers.append(dict(lattice=rows(L),kernel_forward=rows(forward),
                        kernel_backward=rows(backward),
                        component_permutation=rows(permutation),
                        target_change=rows(target),target_inverse=rows(target_inverse),
                        period_source_change=rows(Vs),meridian_corrections=rows(corrections),
                        disc_kernel=rows(old_kernel),
                        disc_inverse=[[str(v) for v in rr] for rr in old_inverse.tolist()]))
    print(f"PASS {number:02d} L=({a},{b};0,{c}) D={D} s={s} all ten fields; kernel/disc inverse maps", flush=True)

output = LANE/(P+"historical_validation_data.json")
data = dict(scope="Post-exposure exhaustive computational verification; not manual matrix reading",
            cases=answers)
output.write_text(json.dumps(data,sort_keys=True,separators=(",",":"))+"\n")
assert json.loads(output.read_text()) == data
print("PASS all 75 cases, 750 finite fields, complete source/codomain changes and inverse equations", flush=True)
print("PASS noncyclic cases",sum(row["smith"][0]>1 for row in old["cases"]), flush=True)
print("PASS generated comparison maps reread and compared in full computationally", flush=True)
print("DATA_SHA256",sha256(output.read_bytes()).hexdigest(), flush=True)
print("COMPLETED_UTC",datetime.now(timezone.utc).isoformat(), flush=True)
