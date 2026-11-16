# B6 research note: finite affine sheets in the moving-section parameters

This is a route record, not a computation of the remaining Theta7 class and not a claim of a global compactification at the origin of this parameter space.

Write the actual linearization section as

\[
\phi_{A,B}(t)=At+B.
\]

The smoothing region has `A B (A+B) != 0`; the three excluded lines correspond to its zero meeting infinity, zero, and one. In the D3 chart, `A=-u s`, `B=u`, and `u=w^2` for the original family. We work in a sufficiently small coefficient region so the contraction estimates hold on the compact elliptic surface.

## Exact local norm constraints

For multiplicities `m=3k`, `n=4l`, the sphere data have `n N0 + m N1 = ±1`. Therefore `N0` is invertible modulo `k` and `N1` is invertible modulo `2l`. The repeated finite norm images in K1 are

\[
N_m\Lambda=m\mathbb Z\varepsilon+k\mathbb Z\delta,
\qquad
N_n\Lambda=n\mathbb Z\varepsilon'+2l\mathbb Z\delta.
\]

If a parameter loop has winding numbers `b0=wind(B)` and `b1=wind(A+B)`, the local logarithms of the two nonzero linearizations change by `b0,b1`. A shift by `b_j` changes the invariant affine translation by `±b_j N_j delta`; the sign depends on the direction chosen for the period comparison and does not affect the norm condition. Returning to the original finite affine datum requires

\[
b_0\equiv0\pmod{k},\qquad b_1\equiv0\pmod{2l}.
\]

These are local necessary conditions, and the local finite norm calculation also supplies the corresponding root-chart comparison when they hold. We have not asserted that they alone prove every global parameter gluing or a filling at an excluded line.

The finite cover

\[
P^k=B,\qquad Q^{2l}=A+B,
\qquad A=Q^{2l}-P^k
\]

removes both local obstructions. It is unramified over the stated region and has degree `2kl`, with deck group `Z/k × Z/(2l)`, cyclic because `gcd(k,2l)=1`. Its coordinate description is

\[
\{(P,Q)\in\mathbb C^2:P Q(Q^{2l}-P^k)\ne0\}.
\]

Its weighted radial circle has weights `(2l,k)`: `P -> exp(2l i theta) P`, `Q -> exp(k i theta) Q`. Both `A` and `B` then scale by `exp(2kl i theta)`, so this circle has exactly the parameter-period multiplicity of K1.

## Original pair and the meridian relation

For `k=l=1`, put `G=Q`, so `G^2=A+B`. The cover is

\[
\{(A,G):A G(A-G^2)\ne0\}.
\]

On `G != 0`, the coordinates `(G,z=A/G^2)` identify it with

\[
\mathbb C^*\times(\mathbb C\setminus\{0,1\}).
\]

The positive `w` circle is the first-factor circle; in the D3 chart, `G=w sqrt(1-s)` with a fixed local square root. A small positive meridian of `G=0` at fixed `A != 0` winds `G` once and winds `z` twice negatively around infinity. With based peripheral paths and order fixed, it is therefore the central scale loop multiplied by the inverse square of the corresponding zero-position peripheral product. This is a relation in the parameter fundamental group; its use for smooth monodromy still needs the full family and the local collision lifts.

The saved algebraic pure-braid calculation `code/maps_moving_zero_braid.py` gives matrices of orders three, four, and a primitive unipotent for the middle parabolic local system. It does not identify their smooth lifts or assert that each unlifted meridian returns the same affine sheet.

## Remaining collision obstruction

The parameter-sheet cover does not remove the local root obstruction in the actual Tate coordinate. Near the finite fibre, the long-period affine translation multiplies that coordinate by a root of

\[
q=u(s_j^{m_j}-a).
\]

Even after `a=b^{m_j}`, the divisor of `s_j^{m_j}-b^{m_j}` is the sum of distinct lines with multiplicity one. Thus this holomorphic function is not an `m_j`th power on the two-variable chart. A root `Q_local^{m_j}=q` and the simultaneous permutation of the semistable components remain part of the geometry. Omitting them is precisely the gap in a naive product or simultaneous-resolution calculation.
