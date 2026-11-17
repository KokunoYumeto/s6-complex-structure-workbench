"""Exact arithmetic of the oriented nonzero Haefliger-normalization test.

The actual Kummer embedding and the generator morphisms are proved in
P3F.55 from the opened primary statements. This certificate checks their
integer and rational comparison; it does not stand in for those maps.
"""
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
import json

sigma = -16
normal_euler_square = 0
omega_L = Fraction(3 * sigma, 2)
whitehead_square_to_L = -4
omega_S2 = omega_L / whitehead_square_to_L
H_GT = omega_S2 / 3
H_Takase = Fraction(normal_euler_square - sigma, 8)
assert omega_L == -24
assert omega_S2 == 6
assert H_GT == H_Takase == 2
assert H_GT != 0

out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS",
    "actual_test": "Punctured Kummer embedding in S5, followed by S5 inclusion in S6; outward-normal-first boundary",
    "existence_sources": ["Takase2005 Remark4.2", "Haefliger1966 Theorem5.17 and its preceding compression proof"],
    "sigma": sigma,
    "normal_euler_square": normal_euler_square,
    "Nemethi_Pinter_Theorem9_1_6_Omega_L": str(omega_L),
    "literal_Whitehead_square_to_L": whitehead_square_to_L,
    "Omega_S2": str(omega_S2),
    "Gauniyal_Turchin_H": str(H_GT),
    "Takase_H": str(H_Takase),
    "group_morphism": "The two integer-valued group isomorphisms agree on a nonzero class and hence on the whole infinite cyclic group.",
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
