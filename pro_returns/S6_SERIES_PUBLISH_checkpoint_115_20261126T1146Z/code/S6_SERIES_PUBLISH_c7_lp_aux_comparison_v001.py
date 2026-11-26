#!/usr/bin/env python3
"""Post-exposure LP auxiliary arithmetic and isolated historical rerun."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import subprocess
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
TMP = Path("/tmp/S6_SERIES_PUBLISH_c7_LP_aux")
LANE = ROOT / "agents/continuation7_iii_primary_powers"
historical = TMP / "S6_SERIES_PUBLISH_lp_historical_thomas.py"
source = historical.read_bytes()
assert sha256(source).hexdigest() == "8e080c4fb00575274b8032e38037dbf8c13bd2d56394e4ef9117f8f9fd46ec2f"
saved = ROOT / "code/S6_SERIES_PUBLISH_c7_lp_historical_thomas.py"
assert not saved.exists()
saved.write_bytes(source)
out = ROOT / "code/S6_SERIES_PUBLISH_c7_lp_historical_thomas_new_run.out"
err = ROOT / "code/S6_SERIES_PUBLISH_c7_lp_historical_thomas_new_run.err"
assert not out.exists() and not err.exists()
assert not (TMP / "fourfolds_D48_thomas.json").exists()
print("Post-exposure comparison UTC", datetime.now(timezone.utc).isoformat(), flush=True)
print("Historical source fully inspected: imports pathlib,json,sympy only; sole data write is adjacent fourfolds_D48_thomas.json.", flush=True)
print("Execute exact source in /tmp; no target or canonical import/write.", flush=True)
with out.open("xb") as stdout, err.open("xb") as stderr:
    run = subprocess.run([sys.executable, str(historical)], cwd=TMP, stdout=stdout, stderr=stderr, check=False)
print("Historical new run exit", run.returncode, flush=True)
assert run.returncode == 0
data = (TMP / "fourfolds_D48_thomas.json").read_bytes()
new_data = LANE / "S6_SERIES_PUBLISH_III_02LP_historical_thomas_new_run.json"
assert not new_data.exists()
new_data.write_bytes(data)
for path in (saved, out, err, new_data):
    print("RETAINED", path.relative_to(ROOT), len(path.read_bytes()), sha256(path.read_bytes()).hexdigest(), flush=True)

print("NEW FOCUSED EXACT IDENTITIES", flush=True)
d,k,ell,n0,n1,P = S.symbols("d k ell n0 n1 P", integer=True)
C0 = S.Matrix([-2*d*n0,-k,0,0])
C1 = S.Matrix([-3*d*n1,2*ell,0,0])
combination = -P*(2*ell*C0+k*C1)
assert combination == S.Matrix([d*P*(4*ell*n0+3*k*n1),0,0,0])
print("Thom combination", combination.T, "= d P^2 s = d s for P=+/-1", flush=True)
print("Critical preimage xi-values: d*1+d*0+(-6*d) =", S.expand(d-6*d), flush=True)
print("Chosen Thom chain coefficient in cap1 = -k*P; C=-5d*s gives link = 5*k*P", flush=True)

A = S.Matrix([[0,1],[-1,0]])
for matrix,U,V in [
    (A, S.Matrix([[-1,0],[1,-1]]), S.Matrix([[1,1],[0,1]])),
    (A.inv(), S.Matrix([[-1,0],[-1,-1]]), S.Matrix([[1,-1],[0,1]])),
]:
    assert U.det() == V.det() == 1
    assert U*(matrix-S.eye(2))*V == S.diag(1,2)
    print("Order4 matrix",matrix.tolist(),"U",U.tolist(),"Uinv",U.inv().tolist(),
          "V",V.tolist(),"Vinv",V.inv().tolist(),"diagonal",S.diag(1,2).tolist(),flush=True)

x,y,j,h = S.symbols("x y j h", integer=True)
phi = -x*(x-1)/S.Integer(2)+3*y*y
psi = -x*(x-1)/S.Integer(2)+3*y*(y-1)
assert S.expand(psi-phi) == -3*y
assert S.expand(phi.subs(y,y+d)-phi) == 6*d*y+3*d*d
assert S.expand(psi.subs(y,y+d)-psi) == 6*d*y+3*d*d-3*d
print("Support difference",S.expand(psi-phi),"; forward monomial z2^-3, inverse z2^3",flush=True)
print("Gamma factor ratio q^(-3d)*unit_gamma^(-3); all other period ratios use the same monomial.",flush=True)

for sign in (-1,1):
    total = S.expand(S.summation((h+sign*6*j)**2,(j,0,d-1)))
    quotient = h*h+sign*6*h*(d-1)+6*(d-1)*(2*d-1)
    assert S.expand(total-d*quotient) == 0
    print("Independent pure-cube identity sign",sign,"sum/d",S.expand(quotient),flush=True)
print("All checks are post-exposure auxiliary comparisons; no fresh whole-LP credit.",flush=True)
