#!/usr/bin/env python3
"""Integrate reviewed eighth-hour outcomes without claiming an origin cap."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = root / 'code' / 'refresh_report.py'
s = p.read_text()
replacement = {
'| B.3 |': '| B.3 | B.3.1–B.3.8; B.4.1–B.4.20 | Stated gluing refuted; global partial filling proved; origin open | The actual family now extends properly over (P1 x Delta_r) minus {(infinity,0)}, with all finite and punctured-cusp overlap maps and their exact cocycle. The required clockwise cusp rotation is -1. A proper completion of the remaining origin is unconstructed. |',
'| B.4 |': '| B.4 | B.4.1–B.4.20 | Open, with actual partial filling and embedded Tate interface proved | The proper global partial family has smooth total space and reduced NC r-central divisor. An actual Tate divisor in a proper Kato family has the required degree-zero normal and 6P action, but its relative neighbourhood at the nodes is not the total normal line; fixed-base localized plumbing retains exceptional rational curves and cannot yield the prescribed ordinary tori. The origin cap, descent resolution and least exponent remain open. Necessary fundamental-group, coherent-cohomology and non-ddbar-normalization constraints, actual regular Hopf insertions, and the earlier exact obstructions remain proved. |',
'| E.2 |': '| E.2 | E.2.1–E.2.24 | Proved | Tangent cohomology is (1,1,1,0); the period family is locally miniversal with smooth reduced one-dimensional Kuranishi germ for every coprime pair. Actual smooth specialization, analytic cusp reconstruction and finite analytic propagation prove separation under arbitrary holomorphic deformation chains. Each fixed-pair locus is also clopen in the C-infinity space of integrable structures. Equal ordered pairs lie in the same connected unmarked period family; no count of marked components is asserted. |',
'| Lead 5 |': '| Lead 5 | B.3.1–B.5.1; B.4.19–B.4.20 | Proposed gluing false; global partial replacement proved; origin open | All actual finite and punctured-cusp overlaps now glue over the complement of the single base origin. An embedded Tate interface is constructed, but its normal-line agreement does not supply the missing neighbourhood or second-period comparison. The proper origin completion and compact global filling remain open. |',
}
lines = s.splitlines()
found = set()
for i, line in enumerate(lines):
    for start, value in replacement.items():
        if line.startswith(start):
            lines[i] = value
            found.add(start)
assert found == set(replacement), found
s = '\n'.join(lines) + '\n'
new_records = [
    'root_eighth_hour_audit.md', 'D_B4419_referee.md',
    'E_E220_referee.md', 'D_E2221_referee.md',
    'D_E2222_referee.md', 'D_E2223_referee.md',
    'D_E2224_referee.md', 'E_propagation_source_audit.md',
    'D_other_axis_interface_audit.md',
]
for name in new_records:
    if f'"{name}"' not in s:
        s = s.replace('"retention_record.md"]:', f'"{name}","retention_record.md"]:')
p.write_text(s)

p = root / 'sections' / 'root_eighth_hour_audit.md'
s = p.read_text()
s = s.replace(
'The separate interpretation involving continuous families in the C-infinity space of integrable complex structures is being checked against the original local Kuranishi completeness theorem. It is not silently included merely by changing the wording of the holomorphic-base theorem. No claim that a fixed pair has only one marked Teichmüller component is made.',
'E.2.24 resolves the separate interpretation involving continuous families in the C-infinity space of integrable complex structures. Root and boundary_d both opened Meersseman\'s original published paper, Section3.2 Theorem3.4 and Remark3.6, pp898--899, including the actual retraction (3.11). Its connected local Kuranishi domain retracts continuously to the connected analytic deformation base, and every structure in the domain is biholomorphic to its representative by a small diffeomorphism. E.2.23 therefore makes each fixed-pair saturated locus open and closed, including near an initially unconstructed structure. No global bounded-automorphism hypothesis or global analytic-stack theorem is used. No claim that a fixed pair has only one marked Teichmüller component is made.')
s += '''\n\n## Full-source review of the embedded Tate interface\n\n+B.4.20 was read in full by root, including its final fixed-base plumbing restriction. The proof uses holomorphic units kappa(s),a(s), as already allowed by B.4.10; no unproved smallness condition on kappa is introduced. The equation h=pi_n^*w-s transforms by exactly a(s), and every blow-up coefficient in its central divisor is one. Its smooth total divisor is the marked semistable Tate surface. In the stated total-coordinate convention W=exp(-2pi i zeta2), the normal factor a=exp(-2pi i mu) represents M^(-1)=O(O-P); the independent scaling a^(-6)=exp(12pi i mu) represents translation by6P. The final Picard-sign clarification was adopted before integration. These are distinct data and are correctly distinguished.\n\n+At a node the Kato neighbourhood has base map s=uv-h, while the total normal line has s=uv. Their relative critical loci differ. The proposed local plumbing r=f(uv-s) is smooth with NC r-centre, but changes the local s-fibration. In addition, the exceptional rational curves of the generic blown-up Hopf surface are disjoint from the other axis and survive any fixed-base plumbing confined to that axis. Such a plumbing cannot have ordinary two-tori as its nearby surface fibres. The full-source statement passes precisely at its embedded-interface and restricted-obstruction scope. It does not fill the origin.\n'''.replace('\n+', '\n')
p.write_text(s)
print('Updated reviewed outcomes B.4.19–20 and E.2.20–24; retained all global filling Open statuses.')
