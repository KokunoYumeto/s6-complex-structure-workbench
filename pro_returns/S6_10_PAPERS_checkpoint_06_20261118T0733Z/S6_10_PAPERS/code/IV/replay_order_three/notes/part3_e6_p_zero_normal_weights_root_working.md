# Exact normal weights on the p-zero binomial graph charts

Retain the actual corrected coordinates of the checks construction,
with equation UV=x^9 y^9 p and physical-circle weights
(x,y,U,V,p)=(-1,1,1,-1,0). The ordered graph factorization uses nine
x factors, nine y factors and p. For k=0,...,8 its x charts are

\[
 x=ab,\qquad U=x^k a,\qquad V=x^{8-k}y^9p b.
\]

The free coordinates (a,b,y,p) have exact weights
(k+1,-k-2,1,0). The y charts are

\[
 y=ab,\qquad U=x^9y^k a,\qquad V=y^{8-k}p b,
\]

whose free coordinates (x,a,b,p) have weights
(-1,10-k,k-9,0). The final chart is p=ab,
U=x^9y^9a,V=b, with free weights (-1,1,1,-1)
on (x,y,a,b). All four-weight sums are zero.

The complete source-chain overlap x'=1/y, y'=xy^2
has the literal lifted map from the x chart with index k to the
y chart with that same index

\[
 a'=y^{9-2k}a,\qquad b'=y^{2k-7}b.
\]

The inverse divides by those powers on this open set. Substitution
preserves U,V,p and every physical weight. The canonical residue
dx wedge dy wedge dp wedge dU/U has coefficients -1,+1,-1
in the displayed x, y and final free-coordinate orders. These
are the actual complex-volume coefficients, with their phases.

These computations supply the normal representations in each local
chart. The first eighteen charts contain a fixed p curve and the
last has an isolated fixed point. The global period identifications,
the point-graph refinement and the remaining end/cap overlaps are
needed before a global fixed-component count or characteristic
pair is assigned. The exact certificate is
code/part3_root/e6_p_zero_resolution_weights.py and its output.
