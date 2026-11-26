#!/usr/bin/env python3
"""New KS raw-period/fan/divisor calculation; no original or old KS output."""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation6_iii_carriers"
RAW = OWN / "S6_SERIES_PUBLISH_III_02KS_raw_definitions.json"
raw_bytes = RAW.read_bytes()
assert hashlib.sha256(raw_bytes).hexdigest() == (
    "c4b9eb95a152dd12492ebf5b2aa2ae5f63619a652d308002caa0702431e09be4"
)
raw = json.loads(raw_bytes)
row = raw["rows"][0]
A = [s.Matrix(x) for x in row["elliptic_matrices"]]
g = [s.Matrix(x) for x in row["generator_section_cocycle"]]
J = s.Matrix([[0, 1], [-1, 0]])
p = 12
I4 = s.eye(4)
u, r = s.Matrix([-2, 1]), s.Matrix([-1, 0])
M = s.Matrix.hstack(u, r)
assert M.det() == 1
assert A[1] == s.eye(2) + 3*u*u.T*J and g[1] == 4*u
z = [(A[0]-s.eye(2)).inv()*g[0], s.Rational(4,3)*r,
     (A[2]-s.eye(2)).inv()*g[2]]
T, conjugacies = [], []

def mat_data(M):
    return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def emit(label, value):
    print(label + " = " + str(value))

for i in range(3):
    assert (A[i]-s.eye(2))*z[i] == g[i]
    b = -p*z[i].T*J
    beta = -p*g[i].T*J*A[i]
    Ti = s.eye(4)
    Ti[:2,:2], Ti[:2,3] = A[i], g[i]
    Ti[2,:2], Ti[2,3] = beta, (beta*z[i])[0] + raw["weights"][i]
    Si = s.eye(4)
    Si[:2,3], Si[2,:2], Si[2,3] = z[i], b, (b*z[i])[0]
    Si_inv = s.eye(4)
    Si_inv[:2,3], Si_inv[2,:2] = -z[i], -b
    assert Si*Si_inv == I4 and Si_inv*Si == I4
    Di = s.diag(A[i], s.eye(2))
    Di[2,3] = raw["weights"][i]
    assert Ti == Si_inv*Di*Si
    assert all(x.q == 1 for x in Ti)
    T.append(Ti)
    conjugacies.append((Si, Si_inv))
    emit("z,b,beta,T at " + row["fibers"][i],
         (mat_data(z[i]), mat_data(b), mat_data(beta), mat_data(Ti)))
    emit("S and inverse at " + row["fibers"][i],
         (mat_data(Si), mat_data(Si_inv)))

assert A[0]*A[1]*A[2] == s.eye(2)
assert g[0] + A[0]*g[1] + A[0]*A[1]*g[2] == s.zeros(2,1)
assert T[0]*T[1]*T[2] == I4
Omega = s.zeros(4)
Omega[0,1], Omega[1,0], Omega[2,3], Omega[3,2] = p, -p, -1, 1
for Ti in T:
    assert Ti.T*Omega*Ti == Omega and Ti[:,2] == I4[:,2]
emit("elliptic product, cocycle sum, period product", "I, 0, I")
emit("preserved alternating form", mat_data(Omega))

# Exact local component homomorphisms, without previous engine outputs.
phi_star = s.Matrix([[1,3]])
assert all(int(x) % 4 == 0 for x in phi_star*(A[2]-s.eye(2)))
assert int((phi_star*g[2])[0]) % 4 == 3
assert (A[2]-s.eye(2)).det() == 4
assert (A[0]-s.eye(2)).det() == 1
assert M.inv()*(A[1]-s.eye(2))*M == s.Matrix([[0,3],[0,0]])
emit("component maps", {
    "II": "zero; A-I unimodular",
    "I3": "(x,y)->y mod3, inverse residue k->k*(-2,1); free coordinate r retained",
    "I1star": "(x,y)->x+3y mod4, inverse residue k->(k,0)",
    "G residues": [0,1,3], "12G residues": [0,0,0]
})

# Exact transport to the admitted original OS50 odd-star construction.
C = s.Matrix([[1,1],[-1,0]])
Pstar = s.diag(C,s.eye(2))
Tstar_admitted = s.Matrix([[-1,-1,0,-1],[0,-1,0,1],
                           [-12,-24,1,3],[0,0,0,1]])
assert Pstar.det() == 1
assert Pstar.inv()*T[2]*Pstar == Tstar_admitted
assert s.Matrix([[-9,-3]])*C == s.Matrix([[-6,-9]])
kill = s.Matrix([[1,0,0],[0,1,0],[9,3,1]])
assert kill.det() == 1 and kill.inv()*kill == s.eye(3)
emit("star transport and inverse", (mat_data(Pstar),mat_data(Pstar.inv())))
emit("star plus delta killed lattice and inverse", (mat_data(kill),mat_data(kill.inv())))
emit("actual log parameters", "m=1, v=(0,0,0,1); primitive relation -gamma+x_regular")
emit("central log lattice map and inverse", "[(z,k)] -> z+k*gamma; z -> [(z,0)]")

# Preserve the literal angular cocharacters and the literal long periods.
lam = s.Matrix([-2,1,-16,0])
rr = s.Matrix([-1,0,0,0])
H = s.Matrix.hstack(lam,rr,I4[:,2],I4[:,3])
Hi = H.inv()
N = Hi*T[1]*H-I4
expected_N = s.zeros(4)
expected_N[0,1],expected_N[0,3],expected_N[2,3] = 3,4,1
assert H.det() == 1 and N == expected_N
assert H*Hi == I4 and Hi*H == I4
Gamma = s.Matrix([[3,4],[0,1]])
change = s.Matrix([[1,-1],[0,1]])
assert Gamma*change == s.Matrix([[3,1],[0,1]])
assert Gamma.det() == 3
emit("H, inverse H, N", (mat_data(H),mat_data(Hi),mat_data(N)))
emit("Gamma and reduced basis", (mat_data(Gamma),mat_data(Gamma*change)))
emit("Gamma quotient and inverse", "rho(x,y)=x-y mod3; k -> (k,0)+Gamma")
emit("Gamma-kernel inverse", "(x,y) -> ((x-4y)/3,y)")

# The admitted KO fan, in its primal valuation coordinates.
e1,e2 = s.Matrix([1,0]),s.Matrix([0,1])
rays = [e1,e2,e2-e1,-e1,-e2,e1-e2]
rho = lambda v: int(v[0]-v[1]) % 3
ray_colors = [rho(v) for v in rays]
assert ray_colors == [1,2,1,2,1,2]
assert all(k != 0 for k in ray_colors)
triangle_types = [[s.zeros(2,1),e1,e2],[e1+e2,e2,e1]]
for tri in triangle_types:
    R = s.Matrix.hstack(*[s.Matrix([v[0],v[1],1]) for v in tri])
    assert R.det() == 1
    assert sorted(rho(v) for v in tri) == [0,1,2]
    emit("triangle rays and circle weights", (mat_data(R),mat_data(R.inv()*s.Matrix([0,1,0]))))
emit("six neighbor residues", ray_colors)
emit("quotient cells", "3 vertices, 9 edges, 6 triangles; each triangle has all three colors")

# Intersection matrix derived from the oriented fan, rather than copied.
B = s.zeros(6)
for i in range(6):
    prev,cur,nxt = rays[(i-1)%6],rays[i],rays[(i+1)%6]
    assert s.Matrix.hstack(prev,cur).det() == 1
    assert s.Matrix.hstack(cur,nxt).det() == 1
    self_int = -s.Matrix.hstack(prev,nxt).det()
    assert prev+nxt == cur and self_int == -1
    B[i,i] = self_int
    B[i,(i-1)%6] = B[i,(i+1)%6] = 1
normal = -s.ones(6,1)
normal_square = (normal.T*B*normal)[0]
assert normal_square == 6
emit("boundary curve intersection matrix", mat_data(B))
emit("normal divisor coefficients and square", (list(normal),normal_square))

d = s.symbols("d0:3")
restrictions, squares = [], []
for i in range(3):
    coeff = s.Matrix([d[(i+k)%3]-d[i] for k in ray_colors])
    restrictions.append(coeff)
    squares.append(s.expand((coeff.T*B*coeff)[0]))
assert s.expand(sum(squares)) == 0
cubic = s.expand(sum(d[i]*squares[i] for i in range(3)))
factored = 3*(2*d[0]-d[1]-d[2])*(2*d[1]-d[0]-d[2])*(2*d[2]-d[0]-d[1])
assert s.expand(cubic-factored) == 0
for i in range(3):
    assert cubic.subs({d[j]:int(i==j) for j in range(3)}) == 6
emit("component restriction coefficient columns", [mat_data(v) for v in restrictions])
emit("restriction squares", squares)
emit("component divisor cubic", s.factor(cubic))
emit("all component intersection numbers", "Di^3=6; Di^2 Dj=-3 (i!=j); D0 D1 D2=6")
fixed_pairings = s.zeros(3)
for i in range(3):
    # The fixed e2 edge based at color i is boundary ray number 1 in Di.
    linear = s.expand((s.eye(6)[:,1].T*B*restrictions[i])[0])
    for j in range(3):
        fixed_pairings[j,i] = linear.coeff(d[j])
assert fixed_pairings == s.Matrix([[-1,-1,2],[2,-1,-1],[-1,2,-1]])
emit("divisor pairings with the three fixed curves", mat_data(fixed_pairings))

# Integral semisimplicial incidence maps for the actual three-colored cusp.
# dP6 curve classes in the basis L,E1,E2,E3, in cyclic fan order.
curves = s.Matrix([[0,1,0,1,0,1],
                   [1,-1,0,0,0,-1],
                   [0,-1,1,-1,0,0],
                   [0,0,0,-1,1,-1]])
intersection = s.diag(1,-1,-1,-1)
assert curves.T*intersection*curves == B
positive = [e1,e2,e2-e1]
edge_map = s.zeros(12,9)
dual_d1 = s.zeros(3,9)
dual_d2 = s.zeros(9,6)
for color in range(3):
    for direction,step in enumerate(positive):
        col = 3*color+direction
        end = (color+rho(step))%3
        edge_map[4*color:4*color+4,col] += curves[:,direction]
        edge_map[4*end:4*end+4,col] -= curves[:,direction+3]
        dual_d1[end,col] += 1
        dual_d1[color,col] -= 1
    # Plus triangle: e1 at color, -e2 at color, +e3 at color+1.
    dual_d2[3*color,2*color] += 1
    dual_d2[3*color+1,2*color] -= 1
    dual_d2[3*((color+1)%3)+2,2*color] += 1
    # Minus triangle: -e3 at color+1, +e2 at color+1, -e1 at color+2.
    dual_d2[3*((color+1)%3)+2,2*color+1] -= 1
    dual_d2[3*((color+1)%3)+1,2*color+1] += 1
    dual_d2[3*((color+2)%3),2*color+1] -= 1
assert dual_d1*dual_d2 == s.zeros(3,6)
def nonzero_smith(M):
    D = smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert nonzero_smith(edge_map) == [1]*7
assert nonzero_smith(dual_d1) == [1]*2
assert nonzero_smith(dual_d2) == [1]*5
emit("normalization H2 edge-incidence map", mat_data(edge_map))
emit("dual d1", mat_data(dual_d1))
emit("dual d2", mat_data(dual_d2))
emit("incidence Smith factors", {
    "H2 edge":nonzero_smith(edge_map),
    "dual d1":nonzero_smith(dual_d1),
    "dual d2":nonzero_smith(dual_d2)
})
emit("status", "All exact assertions passed; no original KS proof or historical KS calculation opened")

maps = {
    "scope":"Fresh raw/fan/component calculation, no target proof read",
    "T":[mat_data(x) for x in T],"H":mat_data(H),"H_inverse":mat_data(Hi),
    "N":mat_data(N),"Gamma":mat_data(Gamma),"ray_residues":ray_colors,
    "boundary_intersection":mat_data(B),"component_cubic":str(s.factor(cubic)),
    "fixed_curve_pairings":mat_data(fixed_pairings),
    "normalization_H2_edge_map":mat_data(edge_map),
    "dual_d1":mat_data(dual_d1),"dual_d2":mat_data(dual_d2)
}
(OWN / "S6_SERIES_PUBLISH_III_02KS_fresh_maps.json").write_text(
    json.dumps(maps,indent=2)+"\n",encoding="utf-8",newline="\n"
)
