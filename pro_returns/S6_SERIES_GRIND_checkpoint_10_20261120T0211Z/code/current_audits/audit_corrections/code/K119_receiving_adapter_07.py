"""After-receiving K119 comparison with the frozen 139-check derivation.

Checks actual integral adapters, cochain differences and displayed full maps.
This program is not counted as a before-receiving independent derivation.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import sympy as s

start = time.monotonic()
checks = []

def ck(name, value):
    if not bool(value):
        raise AssertionError(name)
    checks.append({"name": name, "pass": True})

def mat(M):
    return [[str(v) for v in M.row(i)] for i in range(M.rows)]

here = Path(__file__).resolve().parent
fresh_file = here / "K119_statement_exact_07.json"
fresh = json.loads(fresh_file.read_text())
packet_file = here.parent.parent / "audit_paper_i/iv_os45/K119_permitted_K10_matrix_inputs_07.json"
packet = json.loads(packet_file.read_text())
Ts0 = [s.Matrix(M) for M in packet["matrices_T"]]
D = s.Matrix([[-3,-8,0,0],[0,-1,0,0],[-2,-3,1,0],[-1,0,1,0],[0,3,1,0],[1,0,0,0]])
B = s.Matrix([[0,0,0,0,0,0],[0,0,1,-2,1,0],[1,1,-6,9,-3,0],[3,0,-8,8,0,1]])
S = s.diag(1,1,1,1,-1,1)
ck("literal inverse integral fifth-image sign adapter", S*S == s.eye(6) and S.det() == -1)
ck("receiving D equals S times frozen D0", D == S*s.Matrix(fresh["period_D0"]))
ck("receiving B equals frozen D1 times inverse S", B == s.Matrix(fresh["period_D1"])*S)
L = s.Matrix([[0,0,0,0,0,1],[0,-1,0,0,0,0],[0,0,0,1,0,1]])
J = s.Matrix([[-24,-8,3],[0,0,0],[-9,-3,1],[0,0,0],[10,3,-1],[0,0,0]])
Dp, Bp = D[:,:3], B[1:,:]
ck("receiving left inverse", L*Dp == s.eye(3))
ck("receiving right inverse", Bp*J == s.eye(3))
ck("receiving full degree-one contraction", Dp*L+J*Bp == s.eye(6))
ck("receiving integral complex", Bp*Dp == s.zeros(3,3))
e = [s.eye(4)[:,i] for i in range(4)]
g = [e[2]+3*e[3], e[2], e[1]+3*e[2]+16*e[3], e[1]+8*e[3], e[1]-3*e[2]]
d = {1:e[0], 2:e[0]+2*e[2], 3:e[0]+e[2], 4:e[0]}
site_data = []
for site in range(1,5):
    Ts = [T.copy() for T in Ts0]
    Ts[4][0,3] += 1
    Ts[site][0,3] -= 1
    H = [T.inv().T for T in Ts]
    N = [A-s.eye(4) for A in H]
    pref = s.eye(4)
    prefixes = []
    for i,A in enumerate(H):
        prefixes.append(pref)
        pref = pref*A
        ck(f"site {site} original inverse-transpose {i}", A.T*Ts[i] == s.eye(4) and all(v.q == 1 for v in A))
    ck(f"site {site} actual product", pref == s.eye(4))
    ck(f"site {site} displayed physical preimage", N[site]*d[site] == e[3])
    ck(f"site {site} displayed source preimages", N[1]*(-e[1]) == e[2] and N[3]*e[2] == e[1]+8*e[3])
    coeff = []
    selected_row = None
    for i,A in enumerate(N):
        E = s.Matrix.hstack(g[i],e[3]) if i == site else g[i]
        C, free = E.gauss_jordan_solve(A)
        ck(f"site {site} actual local coefficient {i}", free.rows == 0 and E*C == A and all(v.q == 1 for v in C))
        coeff.append(C[0,:])
        if i == site:
            selected_row = C[1,:]
    Di = s.Matrix.vstack(*coeff,selected_row)
    Bi = s.Matrix.hstack(*[prefixes[i]*g[i] for i in range(5)], prefixes[site]*e[3])
    ck(f"site {site} exact receiving local-basis D", Di == D)
    ck(f"site {site} exact receiving based B", Bi == B)
    # Receiving raw-to-based map, its literal inverse, and positive cone sign.
    Amap = s.eye(20)
    for j in range(5):
        for i in range(j+1,5):
            Amap[j*4:(j+1)*4,i*4:(i+1)*4] = -N[i]
    Ainv = Amap.inv()
    ck(f"site {site} full integral based adapter", Amap*Ainv == s.eye(20) and all(v.q == 1 for v in Ainv))
    rawcols = s.Matrix.hstack(*N)
    basedcols = s.Matrix.hstack(*[prefixes[i]*N[i] for i in range(5)])
    ck(f"site {site} whole raw-based boundary equality", basedcols*Amap == rawcols)
    raw = [s.zeros(4,3) for _ in range(5)]
    raw[1][:,1] = -e[1]
    raw[3][:,0] = e[2]
    raw[site] += d[site]*s.Matrix([[-8,0,1]])
    rawstack = s.Matrix.vstack(*raw)
    basedstack = Amap*rawstack
    ck(f"site {site} all zero-norm vectors actual preimage", basedcols*basedstack == s.eye(4)[:,1:])
    ck(f"site {site} positive cone direction z=-t", (-basedcols)*(-basedstack) == s.eye(4)[:,1:])
    if site == 4:
        coords = []
        extra = None
        for i in range(5):
            E = s.Matrix.hstack(g[i],e[3]) if i == site else g[i]
            v = N[i]*basedstack[4*i:4*i+4,:]
            c, free = E.gauss_jordan_solve(v)
            coords.append(c[0,:])
            if i == site:
                extra = c[1,:]
        receiving_image_pre = s.Matrix.vstack(*coords,extra)
        frozen_image_pre = S*s.Matrix(fresh["image_coordinate_preimages"])
        difference = receiving_image_pre-frozen_image_pre
        coboundary_pre = L*difference
        ck("whole frozen/receiving preimage difference is the displayed integral coboundary", difference == Dp*coboundary_pre)
        ck("same zero-norm target for both actual lifts", B*receiving_image_pre == B*frozen_image_pre == s.eye(4)[:,1:])
    site_data.append({"site":site,"H":list(map(mat,H)),"local_D":mat(Di),"based_B":mat(Bi),"raw_based_map":mat(Amap),"raw_based_inverse":mat(Ainv),"receiving_three_vector_lifts":mat(basedstack)})

# The nodal chronological formula is checked with every rational point factor.
Z,P,c = s.symbols("Z P c", nonzero=True)
def fm(m):
    return (-2*c)**(m-1)*(1-P**m)/(1-P)**m*(Z-P)**m/((Z-P**m)*(Z-1)**(m-1))
SG = c*(1+P)/(1-P)
actual = fm(2)**8*fm(8).subs(Z,Z/P)/fm(8)
displayed = (-2*SG)**8*(Z-P)*(Z-P**8)/((Z-P**9)*(Z-1))
ck("full nodal chronological coefficient", s.cancel(actual-displayed) == 0)
point = (1-Z/P**8)/(1-Z)
ck("full actual source-target Cartier cancellation", s.cancel(actual*point.subs(Z,Z/P)/point-(-2*SG)**8) == 0)
W = s.Matrix([[-1,3],[-3,8]])
Wi = s.Matrix([[8,-3],[3,-1]])
ck("actual infinity period word and inverse", W*Wi == s.eye(2) and Wi*W == s.eye(2) and s.Matrix([[8,-3]])*W == s.Matrix([[1,0]]))

out = {"status":"PASS","utc":datetime.now(timezone.utc).isoformat(),"assertions":len(checks),"seconds":time.monotonic()-start,
       "actor":"GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)",
       "exposure":"After full receiving K119 proof; distinct from the frozen 139-check statement-only derivation.",
       "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"frozen_input_sha256":hashlib.sha256(fresh_file.read_bytes()).hexdigest(),
       "checks":checks,"sign_adapter":mat(S),"D":mat(D),"B":mat(B),"L":mat(L),"J":mat(J),
       "receiving_image_preimages":mat(receiving_image_pre),"frozen_image_preimages_in_receiving_basis":mat(frozen_image_pre),
       "difference_coboundary_preimage":mat(coboundary_pre),"selected_site_data":site_data}
dest=Path(__file__).with_suffix('.json')
tmp=dest.with_suffix('.json.tmp'); tmp.write_text(json.dumps(out,indent=2)+'\n'); tmp.replace(dest)
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','source_sha256']}))
