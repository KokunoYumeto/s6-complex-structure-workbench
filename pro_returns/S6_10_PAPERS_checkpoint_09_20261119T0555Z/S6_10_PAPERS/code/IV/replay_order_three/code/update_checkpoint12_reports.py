"""Add the audited K40 and K41 proofs to the live checkpoint12 report."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text()
s=s.replace('P3F.1–P3F.2, P3F.16–P3F.56, P3K.6–P3K.38','P3F.1–P3F.2, P3F.16–P3F.56, P3K.6–P3K.38, P3K.40–P3K.41')
old='The actual source-suspension transport across its component flop is still under proof, as are general remaining source/cap-data loops and the other-fan transports of the new source loop; no uncomputed loop is assigned a class.'
new=('P3K.40 computes the actual first fixed-edge flop of the selected-cusp source loop as class23 modulo28. '
     'Its proof retains the sixth Tate winding and an unrestricted four-weight Cox action, verifies the exact quaternionic common-boundary arrow, and uses the actual Hopf quotient to obtain the relative coefficient n=-6 without assigning the still unevaluated other coefficient. '
     'P3K.41 proves that, for the stated fixed-source marked affine cap-data scope, fixed-scalar loops have zero return and every varying-scalar loop has winding divisible by M/b, with return equal to the corresponding integer power of the shortest scalar return of K35 on the same fan. '
     'The proof constructs the actual root Lie sheaf, the full orbifold-groupoid Cech comparison, local line-cover lifts through the reduced fibres, the global rational valuation equation and the inverse physical closing arrow; finite torsion kernels remain present until the global calculation removes them. '
     'The actual source-suspension transport across the v=0 component flop is still under proof. Its exact residual contraction prevents identifying omitted-origin labels with ordinary CP3 links without the full periodic quotient. '
     'The two relative source-loop characteristic integers, later fan transports, moving source/logarithmic sites, component-supported OS49 cap loops and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class.')
assert s.count(old)==2
s=s.replace(old,new)
p.write_text(s)
print('Updated both current-state passages and the exact K40–K41 statement list.')
