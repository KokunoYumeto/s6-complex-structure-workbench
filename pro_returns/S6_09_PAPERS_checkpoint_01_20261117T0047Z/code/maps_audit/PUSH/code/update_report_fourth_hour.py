#!/usr/bin/env python3
"""Update the outcome table after the fourth-hour mathematical integrations."""
from pathlib import Path

path = Path(__file__).with_name('refresh_report.py')
text = path.read_text()
replacements = {
    'A.2': '| A.2 | A.2.1–A.2.5 | Literal normalization shape refuted; finite toroidal replacement proved | All proper invariant smooth refinements are parametrized by exact finite certificates. Normalized star charts, all strata and a terminating blow-up/down algorithm are explicit. A projective-three-space component refutes the universal blow-up-of-R shape. |',
    'A.4': '| A.4 | A.4.1–A.4.9 | Proved in the specified toroidal category | Euler number, fundamental group, all torsion-free integral homology groups and nearby monodromy are proved for every fan. Ambient and direct central normalization-stratification computations agree integrally. Classical Kähler Clemens–Schmid hypotheses fail; the algebraic monodromy filtration is specified. |',
    'B.2': '| B.2 | B.2.1–B.2.3; A.2.5; A.4.9 | Proved for the plain cusp fan | n+1 joint-flat reduced refinements after u=r^n, finite certificates for all proper smooth refinements, a uniform geometric algorithm and two integral central topology computations. The gluing obstruction of B.3 remains. |',
    'B.3': '| B.3 | B.3.1–B.3.8; B.4.1–B.4.6 | Stated gluing refuted; corrected construction open | Component rotations contradict the prescribed cusp. The nonsplit torsor and its normal line exist, but the resulting auxiliary family has Euler number24 and cusp multiplicity12, so it is not the six-sphere family. |',
    'B.4': '| B.4 | B.4.1–B.4.6 | Open, with necessary obstructions proved | Any semistable centre is simply connected, has h¹(O)≥1, and has a normalization component failing ddbar, even with self-crossings. The marked map extends meromorphically. A specified assembly with hyperbolic toric Kato caps is also excluded by its overlap maps. No actual global filling, descent resolution or least exponent is established. |',
    'B.5': '| B.5 | B.5.1; B.4.2–B.4.6 | Open globally | Necessary π₁ and coherent-cohomology constraints proved; no topology assigned to an unconstructed central fibre. |',
    'C.3': '| C.3 | C.3.1–C.3.19; C.5.1 | Partial; actual cap pairing advanced | Six turns reduce to a specified annular orbit translation with unique lift class. The actual linking inclusion is (12,0,1). A marked cusp circle extension, corrected Lefschetz comparison, twelve-node bounding four-manifold and actual spin-six-manifold cap are constructed. The affine frame defect is −24 in its stated orientation and the cap Pontryagin pairing has absolute value24. The signed cubic and characteristic integer remain open. |',
    'Lead 2': '| Lead 2 | A.1.1–A.2.5; A.4.1–A.4.9 | Minimal assertion proved; unrestricted replacement proved in the toroidal category | Global nodal plumbing, two minimal refinements, exhaustive fan certificates, explicit birational algorithm and two integral topology computations. |',
    'Lead 3': '| Lead 3 | A.2.1–A.2.5; A.3.1–A.3.3 | Refuted as worded | Exact-Q smoothing and unrestricted uniqueness are false. |',
    'Lead 7': '| Lead 7 | C.3.1–C.3.19; C.4.1–C.4.2; C.5.1 | Partial | Explicit closing maps, annular reduction, actual cap and absolute Pontryagin pairing; smooth class unresolved. |',
}
lines = text.splitlines()
found = set()
for index, line in enumerate(lines):
    if line.startswith('| '):
        key = line.split('|')[1].strip()
        if key in replacements:
            lines[index] = replacements[key]
            found.add(key)
assert found == set(replacements), found
text = '\n'.join(lines) + '\n'
text = text.replace('The third hourly checkpoint is being prepared at 15:38 UTC with the integrated 96-page paper.', 'The third hourly checkpoint was saved at approximately15:39 UTC with the clean96-page paper.')
text = text.replace('The next hourly deadline and progress assessment are 16:38:56 UTC.', 'The fourth-hour assessment and checkpoint are due at16:38:56 UTC. Work in the fourth hour completed the all-fan geometric algorithm and independent central homology calculation, proved a restricted non-Kähler cap obstruction, and advanced the actual monodromy to its cap Pontryagin pairing. These are advances on the main questions; the unrestricted analytic filling and actual monodromy class remain open.')
path.write_text(text)
print('Updated', len(found), 'outcome rows and the fourth-hour execution record.')
