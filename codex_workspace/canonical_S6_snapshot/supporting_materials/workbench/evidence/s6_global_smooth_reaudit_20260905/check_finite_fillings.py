"""Small exact certificates for the stated finite-filling audit, not global X."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RESEARCH = ROOT / "output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research"
T1 = S.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2 = S.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1 = S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1, v2 = S.Matrix([1,2,-4,0]), S.Matrix([-1,-3,3,0])
gamma = S.Matrix([[1,0,0,0]])
psi1, psi2 = S.Matrix([[0,2,1,3]]), S.Matrix([[0,1,1,2]])
checks = []
def check(name, condition, detail):
    assert condition, name
    checks.append({"name": name, "passed": True, "detail": detail})

for j, T, A, v, psi, m in [(1,T1,A1,v1,psi1,3),(2,T2,A2,v2,psi2,4)]:
    check(f"A{j} contragredient", A == T.inv().T, str(A.tolist()))
    check(f"A{j} order", A**m == S.eye(4) and all(A**k != S.eye(4) for k in range(1,m)), m)
    check(f"A{j} invariant translation", A*v == v, str(v.T.tolist()))
    check(f"A{j} invariant covectors", gamma*A == gamma and psi*A == psi,
          {"gamma_v": str((gamma*v)[0]), "psi_v": str((psi*v)[0])})
    for k in range(1,m):
        cov = (gamma*(S.Rational(k,m)*v))[0]
        check(f"A{j} power{k} fixed-point obstruction", cov.q != 1, str(cov))
        check(f"A{j} power{k} complete rational fixed space",
              (A**k-S.eye(4)).rank() == 2 and gamma*A**k == gamma and psi*A**k == psi,
              {"rank_Ak_minus_I": 2, "primitive_covector_minor": 1})
        # Each displayed invariant covector matrix has a 2x2 minor equal to 1.
        # Therefore its row lattice is primitive. Rank and primitivity together
        # exhaust the integral fixed covectors, not only a rational subspace.
        covectors = gamma.col_join(psi)
        minors = [abs(covectors[:,[a,b]].det()) for a in range(4) for b in range(a+1,4)]
        check(f"A{j} power{k} saturated invariant lattice", S.gcd_list(minors) == 1, [int(a) for a in minors])
    total = S.zeros(4,1)
    for k in range(m):
        total += A**k * (v/m)
    check(f"A{j} full affine orbit translation", total == v, str(total.T.tolist()))

# Public portable mode: run the same exact assertions without accessing the
# original audit workspace or the separately licensed primary-source scan.
import sys
if "--matrix-only" in sys.argv:
    print(json.dumps({"groups_passed": len(checks), "checks": checks}))
    raise SystemExit(0)

records = []
for rel in ["candidate_geometry.tex", "exact_algebra.tex", "integral_leray.tex"]:
    p = RESEARCH/rel
    data = p.read_bytes()
    records.append({"path": "supporting_materials/workbench/research/"+rel,
                    "bytes":len(data), "sha256":sha256(data).hexdigest()})
primary = ROOT / "literature_primary/Hodge_Cotangent_Sources/Cartan_1953-1954_Quotient_variete_analytique_SHC_Exp12.pdf"
data = primary.read_bytes()
records.append({"title":"Cartan, Expose 12 (1953-1954)",
                "url":"https://www.numdam.org/item/SHC_1953-1954__6__A12_0/",
                "pages_read":"printed 12-1 to 12-3", "bytes":len(data),
                "sha256":sha256(data).hexdigest()})
result = {"scope":"Finite printed matrices and translation obstructions only. Analytic proofs are in FINITE_FILLINGS_AUDIT.md; no global S6 certification.",
          "groups_passed":len(checks), "checks":checks, "inputs":records}
output = HERE/"FINITE_EXACT_RESULTS.json"
output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"passed":len(checks), "receipt":str(output)}))
