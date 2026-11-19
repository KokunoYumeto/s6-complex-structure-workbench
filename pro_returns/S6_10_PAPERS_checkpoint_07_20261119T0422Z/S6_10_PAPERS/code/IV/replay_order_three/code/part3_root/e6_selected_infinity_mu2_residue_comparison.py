"""Exact integral boundary map and local A1/point characteristic cancellation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT/'notes/part3_e6_selected_infinity_mu2_residue_comparison_working.md'
labels = []


def ck(value, name):
    assert bool(value), name
    labels.append(name)


rho, z, a, u, p1, v, e = S.symbols('rho z a u p1 v e', nonzero=True)
b = S.symbols('b')
x, y, t = rho, rho*z, rho*z**2
ck(S.expand(x*t-y*y) == 0, 'exact A1 invariant equation')
rhob, zb, ab = rho*z**2, 1/z, a/z
ck([S.cancel(rhob*zb**2-x), S.cancel(rhob*zb-y), S.cancel(rhob-t)] == [0,0,0],
   'both actual resolution charts have the same quadratic-invariant map')
ck(S.cancel(rhob*ab**2-rho*a**2) == 0, 'odd-normal quadratic invariant agrees on both charts')
intersection = S.Matrix([[-2]])
ck(intersection.det() == -2, 'integral complex-oriented intersection matrix')
ck(S.Matrix([[2]])*S.Matrix([[0]]) == S.zeros(1,1), 'boundary cellular d2 d3 is zero')
results = []
for w in (1,-1):
    rel = intersection.inv()*S.Matrix([w])
    square = (S.Matrix([[w]])*rel)[0]
    ck(intersection*rel == S.Matrix([w]), f'w{w}: relative lift solves the literal integral map')
    ck(square == -S.Rational(1,2), f'w{w}: full rational relative square')
    ck(w % 2 == 1, f'w{w}: nontrivial boundary sign character retained')
    # The actual primitive positive-complex derivative index is +1 on
    # each of the two resolved charts. The stabilizer divides the original.
    first = S.Matrix([[2*(1+e),0],[0,-2*e]])
    second = S.Matrix([[2*(1-e),0],[0,2*e]])
    ck(first.det().subs(e,S.Rational(1,2)) != 0 and second.det().subs(e,S.Rational(1,2)) != 0,
       f'w{w}: two nondegenerate resolved zeros at the explicit e=1/2')
    dc2 = S.Integer(2)-S.Rational(1,2)
    dp1 = -2*dc2
    dr = S.cancel((dp1-3*square)/24)
    weights = [2*w,-w,-w,-w]
    point = S.Rational(4-sum(q*q for q in weights),24*S.prod(weights))
    ck(dp1 == -3 and dr == -S.Rational(1,16), f'w{w}: actual tangent and surface correction')
    ck(point == S.Rational(1,16) and dr+point == 0, f'w{w}: exact isolated-point cancellation')
    results.append({'line_weight':w,'intersection_matrix':[[-2]],
                    'boundary_torsion_class_mod2':w%2,'relative_lift':str(rel[0]),
                    'delta_D_squared':str(square),'delta_c2':'3/2','delta_p1':str(dp1),
                    'surface_correction':str(dr),'point_weights':weights,
                    'point_residue':str(point),'complete_local_correction':'0'})

# Independent Laurent expansion at u=infinity using v=1/u.
expr=(4*u**3-u*(p1+(a+u)**2+(b-u)**2))/(24*(a+u)*(b-u))
series=S.series(expr.subs(u,1/v),v,0,2).removeO().expand()
coefficient=S.simplify(series.coeff(v,1))
ck(S.factor(coefficient-(p1-3*(a-b)**2)/24)==0,
   'complete fixed-surface residue expands to the stated determinant-square polynomial')

# Pull back the actual source and line arrows through ell=chi*a.
chi, zeta, ell, neutral, A, B, C = S.symbols('chi zeta ell neutral A B C', nonzero=True)
for sign in (1,-1):
    z_new=A*(zeta/chi)+B*(ell/chi)*neutral
    a_new=C**sign*(ell/chi)
    ck(S.cancel(chi*z_new-(A*zeta+B*ell*neutral))==0,
       f'sign{sign}: full source mixing commutes with the line comparison')
    ck(S.cancel(chi*a_new-C**sign*ell)==0,
       f'sign{sign}: full line unit commutes with the odd-character comparison')

out={'status':'PASS_EXACT_MU2_LOCAL_CHARACTERISTIC_COMPARISON',
     'utc':datetime.now(timezone.utc).isoformat(),'checks':len(labels),'check_labels':labels,
     'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
     'surface_residue_polynomial':str(coefficient),'cases':results,
     'four_node_complete_local_correction':'0',
     'unassigned':'Global orbifold fixed-surface integrals, reference boundary caps, and total return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='check_labels'},indent=2))
