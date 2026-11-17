"""Register the independently audited OS49 cap-data theorem."""
from pathlib import Path
import ast

root = Path(__file__).resolve().parents[1]
p = root / "code/update_report.py"
s = p.read_text().replace("P3K.40–P3K.43", "P3K.40–P3K.44")
old = "The later source-loop fan transports, remaining source-moduli loops, component-supported OS49 cap loops and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class."
new = (
    "P3K.44 proves the corresponding marked fixed-source cap-data theorem for the component-supported OS49 cusp. "
    "Its actual periods (2,1) and (-3,-1), the rational norm divisor +C0+C1, and the forward root square yield the global physical C* endpoint group and the necessary scalar winding ell=N*k. "
    "The endpoint constructed in K37 realizes every such winding, so the return is exactly N*k*(S-1)*(S-3)/4 modulo28 on the same transported fan, and is zero at fixed scalar. "
    "The proof retains the central order-three kernel and finite line character and does not import the whole-zero I1 calculation. "
    "The later source-loop fan transports, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class."
)
assert s.count(old) == 2
s = s.replace(old, new)
ast.parse(s)
p.write_text(s)
print("Registered K44 in both current-state passages and the statement range.")
