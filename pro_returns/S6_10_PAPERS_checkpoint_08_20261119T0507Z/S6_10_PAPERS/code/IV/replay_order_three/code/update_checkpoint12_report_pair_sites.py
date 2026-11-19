"""Register the audited source characteristic pair and moving-site proof."""
from pathlib import Path
import ast

root = Path(__file__).resolve().parents[1]
p = root / "code/update_report.py"
s = p.read_text()
s = s.replace("P3K.40–P3K.41", "P3K.40–P3K.43")
old = "and uses the actual Hopf quotient to obtain the relative coefficient n=-6 without assigning the still unevaluated other coefficient."
new = "and uses the actual Hopf quotient to obtain the relative coefficient n=-6."
assert s.count(old) == 2
s = s.replace(old, new)
old = "The two relative source-loop characteristic integers, later fan transports, moving source/logarithmic sites, component-supported OS49 cap loops and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class."
new = (
    "P3K.42 computes the actual characteristic pair (k,ell)=(6,0) and relative coordinates (m,n,s)=(0,-6,1) for the selected-cusp source loop on its specified fan. "
    "The proof retains the determinant winding in the physical-q product collar, derives the actual normal covector directly from the source equation, and combines the framed local surgery with the signed SU2 clutch of the normalization trace. "
    "The earlier cotangent comparison that omitted the determinant factor is preserved with its correction and is not used. "
    "P3K.43 extends the fixed-source cap-data theorem to closed marked braids of ordinary order-one sites in the regular source locus: its exact moving logarithm gives the full period-valued Lie cocycle, and the actual global C* endpoint removes the braid discrepancy. "
    "Thus the same integer iterate of the shortest scalar return holds, with zero return at fixed scalar, in that stated moving-site scope. "
    "The later source-loop fan transports, remaining source-moduli loops, component-supported OS49 cap loops and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class."
)
assert s.count(old) == 2
s = s.replace(old, new)
ast.parse(s)
p.write_text(s)
print("Registered K42 and K43 in both current-state passages and the statement range.")
