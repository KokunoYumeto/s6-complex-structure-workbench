"""Independent auxiliary-circle audit of all 117 compact fixed surfaces.

Recomputes all three normal intersections and p1 by localization on the
two actual P1 sections and the extra isolated point in each of the four
blown-up surfaces. It does not use the intersection-matrix inversion
used by the original surface certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
SURFACES = ROOT/'code/part3/e6_order_three_fixed_surfaces.json'
GENERIC = ROOT/'code/part3_root/e6_common_period_fan.json'
ENDS = ROOT/'code/part3/e6_common_corner_lift.json'
surface = json.loads(SURFACES.read_text())
generic = json.loads(GENERIC.read_text())['cones']
infinity = json.loads(ENDS.read_text())['ends']['infinity']['cones']
labels = []


def ck(value, label):
    assert bool(value), label
    labels.append(label)


def matrix(rays):
    return S.Matrix.hstack(*(S.Matrix(r) for r in rays))


def ordered_indices(physical):
    normal = sorted([i for i, w in enumerate(physical) if w != 0], key=lambda i: physical[i])
    tangent = [i for i, w in enumerate(physical) if w == 0]
    return normal, tangent


rows = []
for row in surface['surfaces']:
    identifier = row['common_component']
    integrals = [Q(0), Q(0), Q(0)]
    p1 = Q(0)
    section_rows = []
    for number, ci in enumerate(row['generic_section_cones']):
        n = matrix(generic[ci]['rays'])
        physical = n.inv()*S.Matrix([1, 0, 0])
        auxiliary = n.inv()*S.Matrix([0, 1, 0])
        normal, tangent = ordered_indices(physical)
        ck(len(normal) == 2 and len(tangent) == 1, f'{identifier}/{number}: section inside actual fixed surface')
        ck([int(physical[i]) for i in normal] == row['physical_normal_weights'],
           f'{identifier}/{number}: actual normal eigenlines')
        k = int(auxiliary[tangent[0]])
        ck(k != 0, f'{identifier}/{number}: auxiliary action fixes exactly the section')
        m = [int(auxiliary[i]) for i in normal]
        degree = row['normal_degrees_on_sections'][number]
        self_degree = row['section_self_intersections'][number]
        integrals[0] += Q(2*m[0]*degree[0], k)-Q(m[0]*m[0]*self_degree, k*k)
        integrals[1] += Q(m[0]*degree[1]+m[1]*degree[0], k)-Q(m[0]*m[1]*self_degree, k*k)
        integrals[2] += Q(2*m[1]*degree[1], k)-Q(m[1]*m[1]*self_degree, k*k)
        p1 += self_degree
        section_rows.append({'common_cone': ci, 'tangent_weight': k,
                             'normal_auxiliary_weights': m,
                             'normal_line_degrees': degree,
                             'section_self_intersection': self_degree})
    ck(section_rows[0]['tangent_weight'] == -section_rows[1]['tangent_weight'],
       f'{identifier}: actual opposite fibre weights')

    isolated = []
    for ci in row['end_surface_stars']['infinity']['charts']:
        n = matrix(infinity[ci]['rays'])
        physical = n.inv()*S.Matrix([1, 0, 0, 0])
        auxiliary = n.inv()*S.Matrix([0, 1, 0, 0])
        normal, tangent = ordered_indices(physical)
        ck(len(normal) == 2 and len(tangent) == 2, f'{identifier}/{ci}: true surface chart')
        k = [int(auxiliary[i]) for i in tangent]
        if all(k):
            m = [int(auxiliary[i]) for i in normal]
            den = k[0]*k[1]
            integrals[0] += Q(m[0]**2, den)
            integrals[1] += Q(m[0]*m[1], den)
            integrals[2] += Q(m[1]**2, den)
            p1 += Q(k[0]**2+k[1]**2, den)
            isolated.append({'infinity_cone': ci, 'tangent_weights': k,
                             'normal_auxiliary_weights': m})
    ck(len(isolated) == int(row['exceptional_curve'] is not None),
       f'{identifier}: exactly the actual additional isolated auxiliary point')
    expected = [Q(v) for v in row['normal_intersections']]
    ck(integrals == expected, f'{identifier}: independent localization gives all three normal intersections')
    ck(p1 == row['p1_surface'], f'{identifier}: independent tangent localization gives p1')
    ck(all(q.denominator == 1 for q in integrals), f'{identifier}: actual integral normal intersections')

    # Recompute the physical pair from the independently obtained intersections.
    w1, w2 = row['physical_normal_weights']
    x, y, z = integrals
    qform = x/Q(w1*w1)+y/Q(w1*w2)+z/Q(w2*w2)
    ku = qform/Q(w1*w2)
    lu = (p1-x-z-2*(Q(w1,w2)+Q(w2,w1))*y+(w1*w1+w2*w2)*qform)/Q(w1*w2)
    ck([str(-ku), str(-lu)] == row['physical_M_inner_pair'],
       f'{identifier}: physical pair from independent intersections')
    rows.append({'common_component': identifier, 'sections': section_rows,
                 'auxiliary_isolated_points': isolated,
                 'independent_normal_intersections': list(map(str, integrals)),
                 'independent_p1': str(p1), 'physical_M_inner_pair': [str(-ku), str(-lu)]})

total = [sum((Q(r['physical_M_inner_pair'][i]) for r in rows), Q(0)) for i in (0,1)]
ck(list(map(str, total)) == surface['sum_physical_M_inner_pair'], 'complete independently recomputed physical surface sum')
ck(len(rows) == 117 and sum(len(r['auxiliary_isolated_points']) for r in rows) == 4,
   '117 complete surfaces with exactly four auxiliary isolated blowup points')
out = {'status': 'PASS_INDEPENDENT_AUXILIARY_SURFACE_LOCALIZATION',
       'utc': datetime.now(timezone.utc).isoformat(), 'checks': len(labels), 'check_labels': labels,
       'inputs': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (SURFACES, GENERIC, ENDS)},
       'surface_count': len(rows), 'surfaces': rows,
       'physical_M_inner_surface_pair': list(map(str, total)),
       'physical_M_inner_surface_residue': str((4*total[0]-total[1])/24),
       'scope': 'Two actual auxiliary-fixed sections per surface, plus the four actual isolated blowup points, independently recover all normal intersections and tangent p1.',
       'unassigned': 'Four p1 lower surfaces, exterior reference doubles, outer-boundary generator/orientation transfer, and total return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('check_labels','surfaces')}, indent=2))
