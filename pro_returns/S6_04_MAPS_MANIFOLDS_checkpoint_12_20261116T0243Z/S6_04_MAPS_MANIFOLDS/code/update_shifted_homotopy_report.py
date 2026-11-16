"""Record the audited E2 peripheral and second-homotopy advances."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'S6_04_MAPS_MANIFOLDS_report.md'
s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| E.2 |'):
  lines[i]='| E.2 | E.2.1–E.2.11 | Undecided in full smooth classification: complex invariants, χ, π1, full integral homology, stable framing and framed null-bordism overBG are proved. The exact second-homotopy coinvariants are Z²⊕(Z/12)^6, excluding a projective ZG-module and sphere-product connected-sum models; the actual regular-fibre embedding is not an ordinary closed spin |'
s='\n'.join(lines)+'\n'
heading='## The shifted product: peripheral topology and second homotopy'
if heading not in s:
 s+='''\n\n## The shifted product: peripheral topology and second homotopy

E.2.10 identifies the actual regular-fibre complement group as the(3,4) torus-knot group, including its peripheral map: the original invariant fibre loop maps to the central Seifert fibre h, with linking number12. The unique zero-linking framing changes it to the longitude hμ^(−12). Nevertheless the embedded four-torus is not an ordinary closed spin, even one spin of an arbitrary three-torus in a five-sphere. Its preferred degree-two restriction forms force any possible spin direction to lie in the delta line, while its nonzero degree-three restriction class2gamma*u*w is annihilated by that direction. An ordinary spin would require contraction in the spin direction to be injective on the degree-three restriction image. This excludes that precise comparison construction, including the ordinary threefold spin of the classical torus knot.

E.2.11 computes (pi2(P))_G=Z²⊕(Z/12)^6 for the actual classifying map c:P→N. Its H3 pushforward is zero, but the H3 cohomology pullback of the target generator has exact order12. The latter distinction detects the integral extension missed by rational homology: relative Hurewicz and the cohomology exact sequence force a primitive Ext vector, whose Smith factors are1 followed by six12s. Thus the full second-homotopy ZG-module is not projective. In particular P is not homotopy equivalent to N×S6 connected-summed with any finite collection of sphere products S^r×S^(10−r),2≤r≤8, or a homotopy ten-sphere.

Root independently checked both arguments and reran the exact16-sign boundary calculation. Winter's primary spinning definition and peripheral theorem were opened directly and are recorded in records/root_sixth_hour_reading.md. These results narrow the possible smooth type, but do not identify the full ZG-module, its higher attaching data or the smooth surgery class. E.2 therefore remains explicitly incomplete.
'''
p.write_text(s)
print('Updated E.2 through the exact pi2 coinvariants and spinning obstruction.')
