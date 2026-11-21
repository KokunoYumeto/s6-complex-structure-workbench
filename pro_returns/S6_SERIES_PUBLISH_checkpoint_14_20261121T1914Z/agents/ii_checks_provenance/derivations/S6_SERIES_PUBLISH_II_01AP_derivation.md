# Derivation before target proof: 01AP

Owner `cdp:st:A.3.5`; checker `i_provenance`. The exact target packet and its
empty supplement have been read. No II target proof or earlier check file
has been opened. Related Paper I mathematics is prior exposure. During the
primary-source check for 01AR the browser also displayed CDP20 Proposition
7.5, including its suggestion to twist by a meeting component. This is
disclosed as a cited-literature exposure before this freeze. The argument
below supplies the actual full-divisor filtration and every Picard component.

Write F as an ordered sum of irreducible components, repeating S_i exactly
m_i times. Each S_i is a Cartier divisor because Y is smooth. Starting with
G=0 and adding one component S_i, the ideal quotient gives the exact sequence
0 -> O_(S_i)(-G) -> O_(G+S_i) -> O_G ->0. Tensor this sequence by the locally
free Omega_Y^1 tensor L. Its first term is V_i,G tensor L|_(S_i), where
V_i,G=(Omega_Y^1 tensor O_Y(-G))|_(S_i). There are only finitely many such
terms. Their H0 vanishings imply the H0 vanishing on F by this exact sequence.

Fix one such component and one Picard component, represented by L_0. Because
the reduced support is connected and reducible, the intersection graph of
its irreducible components is connected and S_i meets some S_j with j!=i.
The restriction D_ij=S_j|_(S_i) is a nonzero effective Cartier divisor on the
reduced irreducible S_i: a local equation of S_j is a nonzero element of its
local domain. For V=V_i,G tensor L_0|_(S_i), the spaces H0(S_i,V(-kD_ij))
form a descending chain of subspaces of the finite-dimensional H0(S_i,V).
Their intersection is zero. A section in the intersection vanishes to every
order at a point of D_ij; Krull intersection in the Noetherian local domain,
and then analytic continuation on the irreducible space, give zero. The
chain therefore becomes zero for all sufficiently large integers k.

Since H2(Y,Q)=0, c1(O_Y(S_j)) is torsion in the finitely generated H2(Y,Z).
Choose n killing it. Exactness of the exponential sequence places O_Y(nS_j)
in Pic^0(Y). Thus L_0 tensor O_Y(-knS_j) belongs to the chosen Picard
component for every k, and the preceding argument provides an actual line
in that component for which this one layer has zero sections.

Local holomorphic families on Pic(Y), constructed by exponentiating Cech
representatives of H1(Y,O_Y), realize the fixed restrictions as a flat family
of locally free sheaves on the compact S_i. Proper cohomology and upper
semicontinuity make its nonzero-H0 locus a closed analytic subset. It is
proper because of the actual vanishing line just constructed. A connected
complex Lie group component is irreducible; a finite union of proper analytic
subsets is proper. Intersect the finitely many open complements for all
layers. The filtration now gives the asserted dense open set on the full
Cartier divisor, with all multiplicities and layer twists retained.

For a proper map from smooth Y to a smooth compact curve, generic smoothness
and properness make the critical-value set finite. A smooth connected fibre
is irreducible. Hence only finitely many full fibres have reducible support.
Intersect their finite collections of open sets inside any Picard component.
The last assertion follows by applying the resulting actual vanishing twist
to any full fibre whose ambient group is nonzero for every twist.

No numerical calculation is used. The morphisms are the ideal-quotient
injections, restriction of the ambient twist, and the exponential-sequence
map to Pic^0. The proof comparison remains embargoed until this file freezes.
