# Paper V: derivations recorded before reading the printed proofs

Recorded UTC: 2026-11-20T22:46:08.955337+00:00
Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode; separate topology-check agent in S6_SERIES_PUBLISH. The runtime does not expose a numerical effort selector to this agent.

## Scope and sequencing

At this point the main statements and their proof outlines have been read, and the body theorem statements have been extracted without their proofs. The following derivations precede reading the corresponding body proof. They are checks of the precise claims described below, not a certification of the whole dependency chain.

## Genus-two pencil (night:P1.4; maps:src:F.3.5, Hodge part)

For f=x^5+a x+b, a multiple root r satisfies 5r^4+a=0 and f(r)=0. Eliminating a gives b=4r^5; the resultant is 256a^5+3125b^4. With a=lambda^3 and b=lambda^4, this becomes lambda^15(256+3125lambda). Thus the only singular fibre away from 0 and infinity is lambda_*=-256/3125. At that root, r=5lambda_*/4=-64/625. Here r is nonzero, f''(r)=20r^3 is nonzero, and the discriminant zero in lambda is simple. The fibre has one ordinary double point.

At zero set lambda=u^8, x=u^6X, y=u^15Y. The equation becomes Y^2=X^5+X+u^2. Its fibre at u=0 is smooth because X^5+X has no repeated root. The relative differentials satisfy dx/y=u^(-9)dX/Y and x dx/y=u^(-3)X dX/Y. At infinity set lambda=v^(-5), x=v^(-4)X, y=v^(-10)Y. The equation becomes Y^2=X^5+vX+1, whose fibre at v=0 is smooth, and the relative differentials become v^6dX/Y and v^2X dX/Y. The extension lines therefore have divisors (6/5)[infinity]-(9/8)[0] and (2/5)[infinity]-(3/8)[0], respectively. They are T^3 and T, with degree(T)=2/5-3/8=1/40.

The order-eight deck action on the first root chart acts on (X,Y) as (zeta_8^2X,zeta_8Y); hence its differential eigencharacters are zeta_8 and zeta_8^3. It has exact order eight on H^1. At infinity the order-five action has eigencharacters zeta_5^4 and zeta_5^3 on the two holomorphic differentials, hence exact order five. Its central -I at order eight acts trivially on the exterior square, explaining the effective order-four image there by an explicit representation morphism.

## Wedge-plane rank (night:P1.5)

Let H have dimension four, let ell=<u> be a line, and let omega in wedge^2 H be nondegenerate. The map H/ell -> wedge^2 H, [v] -> u wedge v, is injective: u wedge v=0 forces v in ell after extending u to a basis. Its image has dimension three. Every element in that image has exterior square zero. Nondegeneracy gives omega wedge omega nonzero, so no nonzero multiple of omega lies in this image. Projection modulo C omega is therefore injective on that image. This proves the rank-three bundle claim fibrewise; in holomorphic frames the constant rank gives a subbundle.

## Characteristic numbers (night:P1.13)

The integral homology statement night:P1.12 gives H^2=H^6=0, H^4=Z^4, Euler number 6 and signature between -4 and 4. For its almost complex tangent bundle, c1=c3=0 and integral c4=6. Write x=integral c2^2. The Todd index is (3x-6)/720=(x-2)/240, an integer k. Thus x=2+240k. Realification gives integral p1^2=4x and integral p2=x+12. Hirzebruch's signature polynomial yields sigma=(7(x+12)-4x)/45=(x+28)/15=2+16k. The signature bound forces k=0, so x=2, p1^2=8, p2=14 and sigma=2. The middle form is unimodular by integral Poincare duality. Its rank and signature are (4,2), so it has positive and negative indices (3,1). It cannot be even because an even unimodular form has signature divisible by eight. The classification of odd indefinite unimodular forms gives I_(3,1). The hypotheses and exact printed source locator will be checked against the cited source before recording a completed check.

Because H^2(M;Z/2)=0, w2=0. The spin class q1=p1/2 is characteristic: its mod-two reduction is w4, which equals the fourth Wu class as w2=w1=0. Its norm is p1^2/4=2. Characteristic vectors in I_(3,1) have all coordinates odd.

## Explicit characteristic-vector descent (maps:src:F.4.1)

Take a characteristic vector v=(a,b,c,d) of norm a^2+b^2+c^2-d^2=2. Coordinate sign changes are integral isometries, so take a,b,c,d positive odd. Let S=a+b+c and w=(1,1,1,1), with w^2=2. The integral reflection r_w(v)=v-(v,w)w has coordinates (d-b-c,d-a-c,d-a-b,2d-S); it preserves the form and the characteristic class.

For d>1, S>d since S^2=(d^2+2)+2(ab+ac+bc)>d^2. Also Cauchy gives S^2<=3(d^2+2)<9d^2 for d>1, hence S<3d. Therefore -d<2d-S<d. The reflected last coordinate is odd and nonzero; replacing all coordinates by absolute values preserves the norm and yields a smaller positive odd d. This strictly decreasing process reaches d=1. Then a^2+b^2+c^2=3 forces a=b=c=1. This proves the claimed lattice isometry constructively without an enumeration bound.

## Normal invariant and homotopy-sphere absorption (maps:src:F.4.1)

For oriented rank-four real bundles over S^4, pi3(SO4)=Z+Z. In the specified left/right quaternionic clutching conventions the characteristic map is (a,b)->(e,p1/2)=(a-b,a+b). The image consists of pairs of the same parity, and the inverse is ((e+p1/2)/2,(p1/2-e)/2). Thus equality of Euler and half-Pontryagin data determines the unstable normal class. For an embedded middle sphere, the Euler number is its self-intersection, so an isometry carrying q1 carries the full normal invariant. Integral Poincare duality converts the cohomological q1 to the homomorphism required in Wall's extended-form formulation. This needs direct checking against the cited classification's convention, not just its abstract.

The quaternionic projective plane has positive form <1> and p1=2u in its standard orientation. Changing its manifold orientation changes the pairing's sign while preserving the underlying class p1. The oriented connected sum of three positive and one negative copy therefore gives (I_(3,1),q1=(1,1,1,1)). Wall's classification then identifies the fourfold with this sum up to a homotopy eight-sphere. The precise Kramer--Stolz theorem must be opened to verify absorption by HP^2. An absorption diffeomorphism has degree +1: pullback takes the primitive middle generator to +/- the generator, whose square evaluates to +1, so naturality of top-dimensional evaluation forces degree +1. It then extends across the other oriented connected-sum factors.

## Integral topology: gates not yet checked

The printed monodromy matrices, integral finite-cap comparison maps, cusp collapse complex and Leray torsion transgressions have not yet been read. The claims of free homology and three-connectivity require these integral maps, beyond rational rank computations. No completion is recorded for those claims at this stage.
