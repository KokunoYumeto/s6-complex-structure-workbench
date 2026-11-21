# Preread derivation — push:src:D.2.3 [032F]

The target proof remains unopened. I read its statement and D.2.1, D.2.2 and D.3.1 statements. The following direct period construction does not use the D.3.1 classification or its converse. The cited exact dual equation was masked because it lies inside another proof; the dual functional below is derived independently before opening it.

Use the actual D.2.1 periods in coordinates(η,ξ):
p1=(1,1/2), p2=(τ,1/2+h), p3=(0,1), p4=(6h,a+B(h)),
where τ=i+O(h²), B=−3ih²+O(h⁴), and D(h)=−3|h|²+O(|h|⁴). Shrink the disc so D(h)<0 for h≠0. Write h=x+iy,T=Imτ. An integral period with coefficients(j,k,l,N) is
η=j+kτ+6Nh,
ξ=(j+k)/2+l+aN+kh+NB(h).

## Necessary condition and an exact separating morphism

The imaginary equations give
k=(Imη−6Ny)/T,
Imξ=(y/T)Imη+N D(h),
where D(h)=ImB−6y²/T exactly in this period basis.
Set R(h)=ReB−6xy/T and theta(h)=R(h)/D(h). Since ReB=6xy+O(|h|⁴) and T=1+O(h²), R=O(|h|⁴), so theta=O(|h|²). The real linear functional
chi_h(η,ξ)=Reξ−theta Imξ+((theta y−x)/T)Imη
therefore extends continuously at h=0 by chi_0=Reξ. Its value on every actual period is exactly
(j+k)/2+l+aN.
This is a specified morphism from the varying real vector spaces to R, with exact lattice images, not an asymptotic replacement of the period matrix.

For rational a the image G_a=(1/2)Z+aZ is discrete, so chi_h modulo G_a defines a continuous map from the entire quotient family to the Hausdorff circle R/G_a. It separates any two central representatives whose real ξ difference is not in G_a. Equivalently, for any convergent sequence of integral periods at h→0 the limit of its real ξ coordinate belongs to G_a. The exact functional proves this even when the integral coefficients diverge.

## Construct every claimed nonseparated pair using only p1,p3,p4

Fix a desired difference(η0,ξ0), with b=Imξ0 and r=Reξ0. Set the coefficient k=0, choose integers N and j, and put
h_N=(η0−j)/(6N).
Then the first coordinate of j p1+l p3+N p4 is exactly η0. Its second coordinate is
j/2+l+aN+N B(h_N).
When j=O(sqrt|N|), the expansion gives
N B(h_N)=−i j²/(12N)+o(1).
The omitted terms involving η0 are O(|j|/|N|)+O(1/|N|), and the holomorphic remainder N O(h_N⁴) is O(1/|N|), so this limit is uniform for the chosen bounded ratios.

For b≠0 take N→infinity with sign(N)=−sign(b), and choose j of a prescribed parity with j/sqrt|N|→sqrt(12|b|). Then N B(h_N)→ib. For b=0 choose j of the required parity with j→infinity but j=o(sqrt|N|), which gives the same conclusion and keeps h_N≠0 eventually. In both cases h_N→0 through noncentral fibres.

If a=m/n is rational and r∈G_a, choose integers p,q with r=p/2+a q. Choose N in the residue class q modn, tending in the required sign, and choose j≡p mod2 as above. Then l=r−j/2−aN is an integer exactly. The period sequence converges to(η0,ξ0).

If a is irrational, choose N tending in the required sign with aN modulo1 tending to r modulo1; density and recurrence of the irrational rotation supply such a sequence. Choose j even with the required size and l the nearest integer correcting r−j/2−aN. The real part error tends to0, and the same construction realizes every(η0,ξ0). The b=0 construction again uses j=o(sqrt|N|).

For any two central representatives differing by such a limit, take one fixed representative at h_N and translate it by the constructed period. The two representative sequences have the same quotient point and converge to the two central representatives. Every pair of their neighbourhoods therefore meets in the quotient. This is the exact nonseparation argument.

## The global Hausdorff reflection

Different base fibres are separated by the continuous map to the disc. At any nonzero base point, a smaller disc avoiding0 has uniformly invertible period matrix; its quotient is a Hausdorff torus bundle. Thus there are no further nonseparated pairs.

On the central fibre, the relation just proved is addition by C×(G_a+iR) in the rational case and by all C² in the irrational case. It is already an equivalence relation. Form the quotient of the total space by this relation only at h=0. It is Hausdorff: different bases are separated by base opens; distinct noncentral points are separated within the punctured torus bundle; distinct rational central classes are separated by the descended circle-valued chi. The quotient has the original tori away from0. Its central topology is exactly R/G_a: chi is a continuous map to that circle, and the continuous map r↦the class of(0,r) descends to its inverse. In the irrational case the central fibre is one point. Every continuous map from the original space to a Hausdorff space identifies nonseparated pairs, so it factors uniquely through this Hausdorff quotient. This proves the universal reflection property, not merely a set-theoretic description.

Finally, for a=m/n in lowest terms,
G_a=(gcd(n,2m)/(2n))Z=(gcd(n,2)/(2n))Z=lcm(2,n)^(-1)Z.
The arithmetic coefficient and exact chi-period identity will be recomputed with a fresh program. The density of irrational rotations is the elementary circle character fact; this proof does not require any result about all Chabauty limits.

Saved UTC: 2026-11-21T01:36:22.570205+00:00
