"""Current independent reconstruction of P4.4's actual homology maps.

The inputs are the three holomorphic markings and the stated logarithmic
clutch.  No archived matrix or archived execution output is imported.
This checks the displayed integral maps, not the analytic construction.
"""
from itertools import combinations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
pairs = list(combinations(range(4), 2))
I = s.eye(4)

def wedge(x, y):
    return s.Matrix([x[a]*y[b] - x[b]*y[a] for a, b in pairs])

def exterior_square(M):
    return s.Matrix.hstack(*(wedge(M[:, a], M[:, b]) for a, b in pairs))

# Columns are the images of (a,c,b,d), obtained directly from
# (z,w)->(w,z), (iz,iz+w), and (z,iz+w), respectively.
S = [s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]),
     s.Matrix([[0,-1,0,0],[1,0,0,0],[0,-1,1,0],[1,0,0,1]]),
     s.Matrix([[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]])]
g = [I[:,0], s.zeros(4,1), s.zeros(4,1)]
v = [s.Matrix([1,0]), s.Matrix([0,1]), s.Matrix([-1,-1])]
F1, F2 = s.zeros(15,15), s.zeros(29,30)
local = []
for i, Si in enumerate(S):
    assert Si.det() == 1
    Qi = Si.inv()
    R1 = Qi[1:4,:]
    R2 = exterior_square(Qi)[1:6,:]
    assert R1*Si[:,0] == s.zeros(3,1)
    assert R2*wedge(Si[:,0],Si[:,1]) == s.zeros(5,1)
    F1[0:4,5*i:5*i+4] = I
    F1[0:4,5*i+4:5*i+5] = g[i]
    F1[4:6,5*i+4:5*i+5] = v[i]
    F1[6+3*i:9+3*i,5*i:5*i+4] = -R1
    F2[0:6,10*i:10*i+6] = s.eye(6)
    F2[0:6,10*i+6:10*i+10] = s.Matrix.hstack(*(wedge(I[:,j],g[i]) for j in range(4)))
    for b in range(2):
        F2[6+4*b:10+4*b,10*i+6:10*i+10] = v[i][b]*I
    F2[14+5*i:19+5*i,10*i:10*i+6] = -R2
    local.append({'S':Si.tolist(),'inverse':Qi.tolist(),'R1':R1.tolist(),'R2':R2.tolist()})
F0 = s.Matrix([[1,1,1],[-1,0,0],[0,-1,0],[0,0,-1]])
RH1 = s.Matrix([[1,0,0,1],[0,0,1,0],[0,1,0,0],[0,0,1,1]])
RH2 = s.Matrix([[1,0,0,0,1,1],[0,1,0,0,0,-1],[0,0,1,0,1,0],
                [0,0,0,0,-1,0],[0,0,0,0,0,-1],[0,0,0,1,1,1]])
D1, D2 = smith_normal_form(F1,domain=ZZ), smith_normal_form(F2,domain=ZZ)
invariants1 = [abs(int(D1[j,j])) for j in range(15)]
invariants2 = [abs(int(D2[j,j])) for j in range(29)]
assert invariants1 == [1]*15
assert invariants2 == [1]*29
assert F1.det() == -1
assert F0.rank() == 3
assert RH1.det() == -1 and RH2.det() == 1
out = {'timestamp_utc':datetime.now(timezone.utc).isoformat(),
       'label':'night:P4.4','scope':'Current independently reconstructed integral homology matrices and primitive surjectivity only; analytic and topological maps require the displayed proof.',
       'source_block_sha256':hashlib.sha256((ROOT/'analysis/sign_remaining_night_P4.4.tex').read_bytes()).hexdigest(),
       'markings':local,'F0':F0.tolist(),'F1':F1.tolist(),'F2':F2.tolist(),
       'F0_rank':int(F0.rank()),'F1_determinant':int(F1.det()),
       'F1_smith_factors':invariants1,'F2_smith_factors':invariants2,
       'H1_reduced_determinant':int(RH1.det()),'H2_reduced_determinant':int(RH2.det()),
       'all_assertions_passed':True}
(ROOT/'analysis/sign_P44_integral_replay.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps({k:out[k] for k in ['timestamp_utc','F0_rank','F1_determinant','F1_smith_factors','F2_smith_factors','H1_reduced_determinant','H2_reduced_determinant','all_assertions_passed']}))
