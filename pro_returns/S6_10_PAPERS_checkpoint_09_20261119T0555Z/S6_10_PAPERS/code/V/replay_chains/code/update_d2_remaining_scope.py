"""Replace the historical open-item paragraph by its current exact scope."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'sections/manifolds.tex';s=p.read_text()
start=s.index(r'\paragraph{Remaining task D.2.4 ')
end=s.index(r'\paragraph{Theorem D.2.5 ',start)
old=s[start:end]
archive=root/'records/D2_4_superseded_at09.tex'
if not archive.exists():archive.write_text(old)
new=r'''\paragraph{Remaining task D.2.4 (Open: the full filling and smooth classification).}
The later theorems remove the finite-order and coprimality restrictions
of the public initial scan; its original limitations are retained in
\path{records/D2_4_superseded_at09.tex}. The current exact scope is as follows.
D.2.24--28 complete the natural section-line sphere question on all
$21$ profiles, with $59$ marked sphere patterns on $50$ initial rows.
D.2.29--30 compute every free finite affine twist in the stated
nonstar sector, retaining torsion in both the cap and its normal line.
D.2.31--33 add every original additive and multiplicative choice
on the finite natural initial catalogue, giving $495$ distinct
integral homology presentations on $172$ marked rows. Zero-degree
original/Mumford alternatives are individually recorded; equality
of their presentations does not assert relative diffeomorphism.
D.2.34 treats all positive initial weights on the original Engel
profile, including weights divisible by two and three and every
original/log additive choice.

The simply connected smooth statements now include D.2.8,
D.2.14, D.2.25--26, D.2.31 and D.2.35--36. In particular,
with the specified primitive multiplicative caps and no additional
regular logarithms, all fifteen residual-$c=2$ patterns have the
oriented conic-surgery type, while the twenty-four $c=5$ and twelve
$c=7$ patterns have respectively two and one oriented types with
their full Zhubr invariants computed. These statements allow all
finite orders and twists satisfying simple connectivity.

The remaining task includes logarithmic Mumford star caps beyond
the proved sphere obstruction, the general initial-weight and
vertically corrected sectors, and the nonsphere smooth invariants
not covered by those theorems. Even in the minimal nonstar sector
there are eight residual-$c=3$ patterns and five $c=4$ patterns
whose complete refined invariant is not yet computed.
For a concrete first instance take OS $56$/II, $(a,b)=(5,3)$,
zero at its position-zero $I_2$, a type-$II$ logarithm of order
$6$ with primitive gamma numerator one, zero delta twist, and
zero ordinary clutch. Its group is trivial and
$H_2=H_3=\mathbb Z/3$; its degree-six class in
$H_6(K(\mathbb Z/3,2);\mathbb Z)$ remains to be evaluated.
Additional
regular logarithms can introduce nontrivial torsion extensions;
the known homology presentations do not determine their smooth
types. Positive-weight Engel members with two- or three-primary
torsion likewise require their full smooth invariant beyond the
groups in D.2.34. These are active undecided cases, not exceptions
to the requested classification. The exact failed approaches,
certificates and next steps remain in the dated research records.

'''
p.write_text(s[:start]+new+s[end:])
print('Updated D.2.4; preserved its full historical paragraph.')
