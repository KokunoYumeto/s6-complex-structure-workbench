# Exact exceptional-curve nonclosure in the repaired degree-one Kato model

Owner: boundary_d. Working proof, 2026-11-15. This does not exclude an
arbitrary origin cap which changes the complementary region.

## Marked intersection section

In the n=1 family of B.4.10, at a parameter q not zero the unique
exceptional rational curve of the generic Hopf blow-up meets the
persistent elliptic axis transversely at [v=-q] in
E_{a(q)}=C*/a(q)^Z. This is the ordinary blow-up intersection, expressed
in the exact v=w-q marking used in that construction. After q=s^12
the section is p(s)=[-s^12]. The seventy-eight modifications of B.4.21
are all disjoint from the persistent axis, so they leave this entire
intersection germ unchanged.

Choose a holomorphic logarithm tau(s)=(2 pi i)^(-1) log a(s^12) on the
full small disc. The elliptic family is C/(Z+tau(s) Z). On a lifted
punctured disc the section has logarithm
z(s)=(2 pi i)^(-1) log(-s^12). Its continuation around a positive
s-loop changes z by 12, whereas tau returns unchanged. Therefore its
loop has class 12 times the primitive C* winding cycle in the integral
first homology of the smoothly trivial elliptic family. It cannot be
the boundary of a continuous section over the disc. In particular p
has no holomorphic or meromorphic extension. A finite base change of
degree d replaces 12 by 12d and does not remove this obstruction.

## No analytic divisor closure of the exceptional family

Suppose the union of generic exceptional P1s had a proper analytic
divisor closure Z in the repaired threefold. Take the irreducible
component which dominates the parameter disc. It cannot contain the
persistent axis family, since on every nonzero fibre their intersection
is exactly the one point p(s). Intersecting the two Cartier divisors
gives an analytic curve, proper over the disc. Its horizontal reduced
part has generic degree one. A proper irreducible analytic curve with
nonconstant map to a disc has finite fibres; after normalization its
degree-one map is a biholomorphism. Vertical components do not alter
this horizontal component. Thus the intersection extends p(s),
contradicting its nonzero homology winding. Hence no such analytic
divisor closure exists. The same reasoning applies to any further
finite proper modification if a putative closure is pushed forward
properly to the repaired model.

A relative proper holomorphic modification contracting the generic
exceptional P1s would supply precisely such a horizontal exceptional
divisor. A relative proper meromorphic contraction, interpreted via
an analytic graph and a proper resolution of that graph, would do the
same after proper pushforward. Thus these contractions cannot extend
through s=0 while retaining the given complementary Kato family. This
does not rule out a cap obtained by a new deformation or a replacement
which is not such a relative meromorphic comparison.

## Primary context and source access

Dloussky and Teleman explicitly study the known failure of properness
for exceptional curves in deformations of minimal GSS surfaces to
blown-up Hopf surfaces. Their Section 1.2 explains that the exceptional
classes have no compact effective limiting cycle; later sections study
limits on universal covers. The marked-intersection proof above is
self-contained and makes no novelty claim.

APA metadata independently checked on the publisher site:
Dloussky, G., & Teleman, A. (2012). Infinite bubbling in non-Kählerian
geometry. *Mathematische Annalen, 353*, 1283–1314.
https://doi.org/10.1007/s00208-011-0713-9

Opened original author preprint: https://arxiv.org/pdf/1012.5247
(version 2, 5 October 2011), Section 1.2, printed pp.3–4.
Opened publisher metadata: https://link.springer.com/article/10.1007/s00208-011-0713-9 .
Search query: Dloussky Teleman infinite bubbling non Kahler exceptional
curves Hopf Enoki deformation. Retrieval: turn557academia22, then
turn558view0 (full primary preprint) and turn558view1 (publisher).
The subscription published full text was not obtained; no claim of
reading it is made. No new manuscript input or results CSV yet.


## Post-checkpoint full-source version

The complete marked nonclosure and general semistable persistence
proof is now in `B_exceptional_curve_obstruction.tex`, reserved B.4.23.
For the latter, the exact sequence
0 -> O(-1) -> N_{C/Y} -> O^2 -> 0 splits, H1(N)=0, and the induced
map on H0 to the two base directions is an isomorphism. Kodaira's
local embedded-deformation space consequently maps locally
biholomorphically to (Q,r), forcing a rational curve in each nearby
ordinary torus fibre. The conductor-disjointness assumption is
explicit and essential.

Kodaira1962 original DOI/publisher metadata were Opened; its full
JSTOR scan was inaccessible (turn567view1). The exact theorem was
independently Opened in the first paragraph of Merkulov's original
research-article publisher extract, turn570view0, lines451–454:
Merkulov, S. A. (1995). Moduli spaces of compact complex submanifolds
of complex fibered manifolds. Mathematical Proceedings of the
Cambridge Philosophical Society, 118(1), 71–91.
https://doi.org/10.1017/S0305004100073473 .
Original Kodaira metadata: Annals of Mathematics, 75(1) (1962),
146–162; DOI10.2307/1970424 (turn565search0, turn568search0).
No full-original reading claim is made.


Root then independently opened Dloussky–Teleman Proposition 2.3 and
its full proof (preprint pp.6–7), giving the exact relative local
Douady conclusion without properness. I independently opened it too
(turn582view0 and turn583view0). B.4.23 now cites that direct original
primary result; the earlier Kodaira metadata and Merkulov extract are
retained accurately as historical verification. Root and limits_ab
passed the full source; input and registry were integrated after
B.4.22.
