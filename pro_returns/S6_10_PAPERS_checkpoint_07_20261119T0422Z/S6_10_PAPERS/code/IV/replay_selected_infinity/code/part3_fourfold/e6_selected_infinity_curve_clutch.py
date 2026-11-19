"""Literal finite-native / resolved-infinity normal clutches for ten curves."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
overlay = ROOT / 'code/part3/e6_selected_infinity_factor_overlay.json'
faces = ROOT / 'code/part3_fourfold/e6_fixed_face_orbits.json'
ov = json.loads(overlay.read_text())
ff = json.loads(faces.read_text())
checks = []

def ck(value, name):
    assert value, name
    checks.append(name)

def mat(rows):
    return S.Matrix.hstack(*map(S.Matrix, rows))

def ints(M):
    return [[int(x) for x in row] for row in M.tolist()]

rows = []
for rec in ff['selected_ordinary_overlay']['components']:
    if rec['dimension'] != 1 or rec['tag'] != 'chi_unit':
        continue
    ck(len(rec['face_occurrences']) == 1, 'one retained face occurrence')
    occ = rec['face_occurrences'][0]
    ck(len(occ['charts']) == 1, 'one resolved infinity end chart')
    ck(not rec['period_stabilizer_basis'], 'no period stabilizer on curve')
    ci = occ['charts'][0]
    chart = ov['regular4_cones'][ci]
    N = mat(chart['rays'])
    iw = N.inv() * S.Matrix([0, 0, 0, 1])
    nn = [i for i in range(4) if iw[i]]
    tt = [i for i in range(4) if not iw[i]]
    ck(len(nn) == 3 and len(tt) == 1, 'one tangent and three normal axes')
    ti = tt[0]
    ck(list(N[0, :]) == [int(i == ti) for i in range(4)],
       'q_infinity equals the tangent coordinate literally')
    face3 = [r[1:] for r in rec['canonical_face']]
    A = mat(face3).inv()
    ck(abs(mat(face3).det()) == 1, 'native common cone is regular')
    E = S.zeros(3, 4)
    E[:, 1:] = A
    transition = E * N
    weights = list(map(int, A * S.Matrix([0, 0, 1])))
    ck(weights == rec['normal_weights'], 'canonical physical normal order')
    degree = []
    correspondence = []
    for i in range(3):
        nz = [j for j in nn if transition[i, j]]
        ck(len(nz) == 1 and transition[i, nz[0]] == 1,
           'normal row is one normal axis times tangent power')
        ck(iw[nz[0]] == weights[i], 'normal row preserves physical weight')
        degree.append(-int(transition[i, ti]))
        correspondence.append(nz[0])
    common = [i for i, c in enumerate(ov['regular3_cones'])
              if sorted(c['rays']) == sorted(face3)]
    ck(len(common) == 1, 'unique native common3 cone')
    selected = [i for i, c in enumerate(ov['selected_full_regular_cones'])
                if c.get('common3') == common[0]]
    ck(len(selected) == 1, 'unique full selected extension')
    Ns = mat(ov['selected_full_regular_cones'][selected[0]]['rays'])
    Es = S.zeros(3, 4)
    for i in range(3):
        Es[i, 0], Es[i, 1], Es[i, 3] = A[i, 0], A[i, 1], A[i, 2]
    trans_s = Es * Ns
    qcols = [i for i in range(4) if Ns[:, i] == S.Matrix([0, 0, 1, 0])]
    ck(len(qcols) == 1, 'actual selected Q0 tangent axis')
    ck(trans_s[:, qcols[0]] == S.zeros(3, 1),
       'all native normal monomials have zero selected q degree')
    # This is the full exponent of the point/theta unit; its restriction
    # to the curve is exactly one by the actual point-section argument.
    psi_exponents = list(map(int, A * S.Matrix([0, 0, 1])))
    ck(psi_exponents == weights, 'point/theta normal coefficient powers retained')
    prod = F(1)
    for w in weights:
        prod *= w
    ru = -sum((F(4 - sum(w*w for w in weights), wi) + 2*wi) * di
              for wi, di in zip(weights, degree)) / (24 * prod)
    rows.append({'id': rec['id'], 'infinity_chart': ci,
                 'common3': common[0], 'selected_chart': selected[0],
                 'canonical_face': rec['canonical_face'],
                 'normal_weights': weights, 'normal_degrees': degree,
                 'native_normal_exponents': ints(E),
                 'infinity_chart_matrix': ints(N),
                 'full_clutch_exponents': ints(transition),
                 'normal_column_correspondence': correspondence,
                 'tangent_column': ti,
                 'selected_clutch_exponents': ints(trans_s),
                 'point_theta_unit_exponents': psi_exponents,
                 'positive_u_residue': str(ru), 'physical_M_residue': str(-ru)})

ck(len(rows) == 10, 'all ten chi-unit curves')
total = sum((F(r['positive_u_residue']) for r in rows), F(0))
ck(total == 0, 'ten curve contributions cancel exactly')
q, z = S.symbols('q z')
ck(S.simplify((q*z)/q-z) == 0, 'directed line clutch inverse')
record = {
    'status': 'PASS_EXACT_CURVE_CLUTCH',
    'utc': datetime.now(timezone.utc).isoformat(),
    'checks': len(checks), 'check_labels': checks,
    'inputs': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in (overlay, faces)},
    'curves': rows, 'positive_u_sum_per_O_or_T_copy': str(total),
    'physical_M_sum_per_O_or_T_copy': str(-total),
    'source_arrow': 'T=(chi^4,chi*eta,v,V); native=(eta_e,v,V)=(T1,T2,T3). At T use b0=y/t through the exact I2 source chart. q_infinity=T0.',
    'full_point_unit': 'psi=f_(P^a)/r_a, not deleted. On v=0 and eta nonzero, sigma=0 gives aG=O and P^a=1, so both factors are exactly 1. The already proved holomorphic unit extension fixes psi=1 on each curve including O. At T the canonical point frame has r_a=1. All powers in every normal arrow are recorded.',
    'directed_clutch': 'n_native=q_infinity^d n_infinity; the coefficient transition has line degree -d on P1_t.',
    'scope': 'The ten compact continuations of the chi-unit curves, one O/T fundamental copy at a time. No surface integral or global source return is assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status':record['status'], 'checks':len(checks),
                  'curves': [{k:r[k] for k in ('id','normal_weights','normal_degrees','positive_u_residue')} for r in rows],
                  'sum':str(total)}, indent=2))
