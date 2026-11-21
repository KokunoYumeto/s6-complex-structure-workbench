# Paper I, inv:A2.3: preread derivation

The target statement was extracted without its proof. Inputs already read are the rational-section result fam:B1.3 and the visible section calculation fam:B1.1, the stated local branch and mu derivative at the order-four point, and the CM value mu=(2-rho)/3. These inputs are not claimed as newly re-proved here. The supplied Duke–Imamoğlu paper pp.1–5 was read in extracted text; its page 2 image has now also actually been read. Theorem 1, equation (5), gives z0=(1+tau)/2-i sqrt(6)/(3 pi) times the displayed hypergeometric quotient. Equation (2) is x=1-1728/j.

## Identification of the section

On the specified Weierstrass family j=1728t. The input section-group calculation gives the generator as one of the two sections P*=(0,sqrt(2)t^2(t-1)) and -P*. Uniformization by dX/(2Y) carries its x coordinate zero to wp(mu,tau)=0. The two choices are interchanged by negation on the elliptic curve. This is the exact map being used, not an identification of unmarked coordinates.

## Hypergeometric branch

Set mu=1-z0. The identities wp(1-z0,tau)=wp(-z0,tau)=wp(z0,tau) prove that this is a zero. Applying this affine change to the primary formula yields exactly the target expression. For t=1+s^4, x0=s^4/(1+s^4), so x0^(1/4)=s+O(s^5) on the stated branch. The numerator hypergeometric series equals 1+O(s^4). The denominator at s=0 equals E4(i)^(1/4), by the primary modular formula (10) on p.4 and the positive branch. Since tau=i+O(s^2), the derivative is i sqrt(6)/(3 pi E4(i)^(1/4))=i sqrt(2/3)/(pi E4(i)^(1/4)), exactly the supplied derivative. The initial value is (1-i)/2. These identify the prescribed local branch; analytic continuation gives the same lifted branch wherever it is defined.

## Exact order at the order-three point, by the group law

Use t=r^3 and the explicit coordinate map x=r^4 X, y=r^6 Y. The smooth model is Y^2=X^3+a(r)X+b(r), where a=-3r(r^3-1), b=2(r^3-1)^2. The visible section is P=(0,sqrt(2)(r^3-1)). At r=0 its tangent is horizontal and it is a nonzero point of order three. Compute 2P and 3P by the chord-and-tangent law. The local parameter u=-X/Y of 3P satisfies u=(9 sqrt(2)/32)r^2+O(r^5), with nonzero leading coefficient. The attached new exact symbolic program verifies both resulting points on the cubic and the displayed coefficient.

Let omega_1(r) be the nonzero holomorphic first period of dX/(2Y) on this smooth family. Its normalized Abel coordinate v/omega_1 identifies X=omega_1^(-2)wp(v/omega_1,tau) and Y=omega_1^(-3)wp'(v/omega_1,tau)/2. Near the identity u=v+O(v^5). The supplied branch at r=0 has mu=(2-tau)/3 there. Consequently the Abel coordinate of 3P near the identity is 3 omega_1(r)(mu-(2-tau)/3). The nonzero factor 3 omega_1(0) transports the computed order two exactly to the claimed order two. Choosing -P changes the formal coordinate sign and preserves that order.

## Exposure record

All three derivations above were formed before opening the target proof. A subsequent rg search for the primary citation and two input equation labels exposed three target-proof lines saying that Duke–Imamoğlu gives the formula by taking one minus their branch. Those lines were seen after the same affine map had already been derived from the primary source. No other target proof step has yet been opened. This limited exposure is recorded rather than described as an entirely unseen text. The computational derivation above is frozen before the target proof is extracted.
