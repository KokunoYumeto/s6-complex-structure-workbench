"""Exact targeted checks after reading P1.10/P1.12/P1.19 in full.

This is a fresh implementation of the displayed input maps, not an
execution of the absent historical finite_permutation_models.py.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

start = time.monotonic()
checks = []
def ck(name, value):
    if not bool(value):
        raise AssertionError(name)
    checks.append({"name": name, "pass": True})
def rows(M):
    return [[int(v) for v in M.row(i)] for i in range(M.rows)]

A = s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
              [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]]).T
B = s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
              [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]]).T
ell = s.Matrix([[1,0,0,0,0,0]])
v1 = s.Matrix([1,3,-2,-1,2,0])
v2 = s.Matrix([-1,0,0,0,0,0])
K1 = s.Matrix([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],
               [0,-1,-1,0,-1],[0,0,1,0,0]])
K2 = s.Matrix([[-1,0,-1,0,-1],[-1,1,0,1,-1],[0,1,-1,1,-1],
               [0,-1,0,-1,1],[1,-1,1,0,1]])
models = {}
for i, M, v, m, K in [(1,A,v1,5,K1),(2,B,v2,4,K2)]:
    eps = int((ell*v)[0])
    ck(f"finite {i}: prescribed primitive translation sign", eps == (1 if i == 1 else -1))
    ck(f"finite {i}: invariant ell and v", ell*M == ell and M*v == v)
    ck(f"finite {i}: exact order relation", M**m == s.eye(6))
    for j in range(1,m):
        ck(f"finite {i}: affine power {j} has nonintegral ell shift", s.Rational(j*eps,m).q > 1)
    P = s.Matrix.hstack(eps*v, s.eye(6)[:,1:])
    ck(f"finite {i}: unimodular actual lattice split", abs(P.det()) == 1)
    split = P.inv()*M*P
    R = split[1:,1:]
    ck(f"finite {i}: split is 1 plus R", split == s.diag(1,R))
    ck(f"finite {i}: displayed conjugator unimodular", abs(K.det()) == 1)
    C = K.inv()*R*K
    ck(f"finite {i}: exactly one signed unit in each row and column",
       all(sum(abs(C[a,b]) for b in range(5)) == 1 for a in range(5)) and
       all(sum(abs(C[a,b]) for a in range(5)) == 1 for b in range(5)))
    seen, cycles = set(), []
    for j in range(5):
        if j in seen: continue
        cycle, sign, k = [], 1, j
        while k not in seen:
            seen.add(k); cycle.append(k)
            dest = next(a for a in range(5) if C[a,k])
            sign *= int(C[dest,k]); k = dest
        ck(f"finite {i}: signed permutation cycle closes at its start {j}", k == j)
        cycles.append({"indices_zero_based":cycle,"sign_product":sign})
    ck(f"finite {i}: prescribed signed cycle type",
       sorted((len(x['indices_zero_based']),x['sign_product']) for x in cycles)
       == ([(5,1)] if i == 1 else [(1,-1),(4,1)]))
    models[str(i)] = {"P":rows(P),"R":rows(R),"K":rows(K),
                      "signed_permutation":rows(C),"cycles":cycles}

coinv = (A-s.eye(6)).row_join(B-s.eye(6))
D = smith_normal_form(coinv, domain=s.ZZ)
ck("common coinvariants are Z with no torsion", [abs(D[j,j]) for j in range(6)] == [1,1,1,1,1,0])
ck("ell is the actual primitive coinvariant quotient", ell*coinv == s.zeros(1,12) and ell[0,0] == 1)
presentation = s.Matrix([[5,0,-1],[0,4,1],[1,1,0]])
ck("van Kampen residual presentation determinant is minus one", presentation.det() == -1)
ck("van Kampen residual presentation has integral inverse", all(x.q == 1 for x in presentation.inv()))
S = s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],
              [-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
M0 = (A*B).inv()
expected = s.eye(6)
expected[:3,3:] = s.eye(3)
ck("cusp S is the actual unimodular (a,b) marking", abs(S.det()) == 1)
ck("cusp S transports the based word to b_j maps to b_j plus a_j", S.inv()*M0*S == expected)
N = M0-s.eye(6)
ck("cusp nilpotent primitive rank three", N**2 == s.zeros(6) and N.rank() == 3 and
   [abs(x) for x in smith_normal_form(N,domain=s.ZZ).diagonal()] == [1,1,1,0,0,0])

out = {"status":"PASS","actor":"GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)",
       "utc":datetime.now(timezone.utc).isoformat(),"assertions":len(checks),"checks":checks,
       "seconds":time.monotonic()-start,"finite_models":models,"coinvariant_smith":rows(D),
       "presentation":rows(presentation),"presentation_inverse":rows(presentation.inv()),"S":rows(S),
       "scope":"Post-receiving exact check of the actual P1.10 fundamental-group inputs and the P1.12 signed-permutation cellular models; full source proofs were read first. It does not alone construct the analytic family, prove the toric comparison, or replace a global cellular certificate.",
       "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
outpath = Path(__file__).with_suffix('.json')
tmp = outpath.with_suffix('.json.tmp')
tmp.write_text(json.dumps(out,indent=2)); tmp.replace(outpath)
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','source_sha256']}))
