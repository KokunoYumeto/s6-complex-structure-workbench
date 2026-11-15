#!/usr/bin/env python3
"""Update current outcomes after the actual monodromy and Hopf-model proofs."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'code'/'refresh_report.py'
s=p.read_text()
replacements={
'| B.4 |':'| B.4 | B.4.1–B.4.7 | Open, with necessary obstructions and a limiting example proved | Any semistable centre is simply connected, has h¹(O)≥1, and has a normalization component failing ddbar, even with self-crossings. The marked map extends meromorphically. A specified hyperbolic Kato assembly is excluded. An explicit Hopf semistable family shows that the remaining non-Kähler case and nonmeromorphic comparison cannot be dismissed. No actual global filling, descent resolution or least exponent is established. |',
'| C.1 |':'| C.1 | C.1.1–C.1.2; C.3.24; C.3.27 | Proved | The positive one-loop class is zero in Θ7=Z/28. The actual mapping torus is oriented-diffeomorphic to S1×S6. |',
'| C.2 |':'| C.2 | C.2.1–C.2.3; C.3.25; C.5.1 | Formula and a new actual smooth coboundary proved; specified analytic filling open | A product-framed four-handle on D(Lx) bounds the actual clutching sphere. Q=[[k,1],[1,0]], p1=(p+k,3), c²=(k,1), σ=0, and μ=(p−4k)/672. This smooth spin-c manifold is not identified with the analytic W of B.4; that W and its Chern data remain open. |',
'| C.3 |':'| C.3 | C.3.1–C.3.27 | Two independent invariant bridges give zero | The actual relative Pontryagin defect is −24 and the actual delta-line square is −2. The equivariant knot route and the explicit eight-dimensional spin-c index route both give zero for one loop, using integer additivity before reduction modulo28. They share the disclosed geometric p,k inputs; the second route uses no Wall, Davis or Haefliger conversion. |',
'| C.4 |':'| C.4 | C.4.1–C.4.2; C.3.24; C.3.27 | Proved | The class is zero for all twist data covered by the marked family comparison; the conjugation relation is therefore consistent with zero. |',
'| Lead 6 |':'| Lead 6 | C.2.1–C.2.3; C.3.25–C.3.27; C.5.1 | Formula proved and applied to an actual smooth coboundary | The spin-c formula and boundary hypotheses are verified. The analytic filling specified in B.4, and the request for its component-derived Chern numbers, remain open. |',
'| Lead 7 |':'| Lead 7 | C.3.1–C.3.27; C.4.1–C.4.2 | Actual equivariant twist computed | The exact integer is zero, hence the positive one-loop smooth class is zero. Equivariance alone had not determined it; the actual framing and circle-bundle square do. |',
}
lines=s.splitlines()
for i,line in enumerate(lines):
    for prefix,value in replacements.items():
        if line.startswith(prefix):
            lines[i]=value
s='\n'.join(lines)+'\n'
old='The fourth-hour assessment and checkpoint are due at16:38:56 UTC. Work in the fourth hour completed the all-fan geometric algorithm and independent central homology calculation, proved a restricted non-Kähler cap obstruction, and advanced the actual monodromy to its cap Pontryagin pairing. These are advances on the main questions; the unrestricted analytic filling and actual monodromy class remain open.'
new='The fourth checkpoint was saved at approximately16:39 UTC with the clean116-page draft15 paper,100 registered statements and75 bibliography entries. The fourth-hour assessment continued work because the all-fan algorithm, independent central homology computation, restricted non-Kähler cap obstruction and actual cap pairing advanced the main questions. During the fifth hour the actual monodromy was determined as zero, then independently checked by an explicit smooth eight-dimensional coboundary and a direct additive index. A proper Hopf degeneration isolated a genuine limitation of the remaining analytic-filling obstructions. The unrestricted S6 analytic filling remains open. The fifth hourly checkpoint and progress assessment are due at17:38:56 UTC.'
assert old in s or new in s
s=s.replace(old,new)
old_list='"root_fourth_hour_audit.md","retention_record.md"'
new_list='"root_fourth_hour_audit.md","root_C25_C26_B47_referee.md","root_fifth_hour_audit.md","retention_record.md"'
s=s.replace(old_list,new_list)
p.write_text(s)
print('Updated fifth-hour outcome rows and execution record; no old checkpoint changed.')
