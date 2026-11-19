# Class VII conductor results: complete derivations before reading the proofs

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

The four target printed proofs VII.1–4 have not been read. Their metadata-stripped statements are in `018_statement_packet.json`; A.5.3, A.5.12 and the other requested inputs are in the accompanying 018 packets. The already reviewed INT.3 proof was revisited as a cited input, including its exact conductor-duality and point-blowup pushforward maps. The derivations below were written before any target proof exposure. They do not invoke an unrestricted class-VII classification conjecture.

## VII.1: the anticanonical support under the actual blowdown

Let σ:Z→Z0 be the successive point blowdowns to the minimal surface. Push D forward to D0. The Picard isomorphism under point blowup and the canonical formula give an actual torsion line L0 with K_Z0+D0=L0 and

D=σ*D0−K_{Z/Z0}.

D0 cannot vanish: otherwise the minimal class-VII canonical bundle would be torsion and have Kodaira dimension zero. Thus the proved numerically-anticanonical-divisor results apply on Z0. For positive b2, Dloussky's Theorem0.2 and the precise support alternatives in Corollary2.25/Propositions2.27,2.29/Theorem2.38 give a cycle with rational trees, two rational cycles, or the parabolic Inoue elliptic curve and rational cycle. The intermediate configuration is also stated in DOT2003 §1 pp.284–285; its rational-curve bound is stated on p.283. Each connected reduced support has arithmetic genus one, and its topological Euler number is its number of rational irreducible components. The minimal b2=0 case with an effective divisor is Hopf; its compact curves are disjoint smooth elliptic curves, as in the explicit Hopf normal-form comparisons already checked. The Inoue b2=0 surfaces have no such divisor.

For one reverse point blowup, if the current divisor has multiplicity k at the centre, the new exceptional coefficient is k−1. A centre outside the support would give a negative coefficient that persists on every later strict transform, contradicting the final effectivity. Thus every centre lies on the current support. At a smooth point of a coefficient-one branch, k=1 and the new exceptional is omitted from the reduced support; that support is unchanged. At any other permitted smooth point an attached rational leaf is added. At a node the exceptional coefficient is a+b−1>0 and the old edge is subdivided. These are the only operations, starting with the normal crossing configurations just listed. They preserve the arithmetic genus of each connected support component. Each included new rational curve increases both its rational-curve count and its Euler number by one. The formula e(R)=r(R) follows through the actual σ. Every point blowup adds exactly one rational curve to the total rational-curve count and one to b2, so r(Z)≤b2(Z) follows from the minimal bound. An elliptic curve together with a second elliptic curve, or a path joining two distinct points of one elliptic curve, has arithmetic genus at least two by the curve-normalization sequence; it cannot occur in one of these genus-one support components.

## VII.2: the full conductor and its reduced curve

Write L=ω_S and I for the conductor ideal on S, so Γ is defined by I. The empty-conductor case has both asserted inequalities immediately. Assume it is nonempty. Finite duality identifies η*ω_T with Hom_S(η*O_T,L)=I⊗L. It also gives

Hom_S(I,L)=η*(η*L).

For the last equality one may work on T: its canonical module is a reflexive rank-one module, and an endomorphism is multiplication by a meromorphic function with no codimension-one pole. Normality extends that function holomorphically. This identifies the endomorphism sheaf with O_T and gives the displayed isomorphism, including the natural map from L.

Because S is irreducible and compact, h0(O_S)=1. Serre duality and χ(O_S)=0 give h1(O_S)=1+h0(L). A torsion line on a connected reduced compact space has at most one section: a nonzero section raised to its torsion order is a nonzero constant, so it trivializes the line. Thus h0(L) and h0(η*L) are at most one. In the sequence 0→I→O_S→O_Γ→0, duality identifies the map H²(I)→H²(O_S) with the dual of the injective map H0(L)→H0(η*L). Consequently

h1(O_Γ)≤h1(O_S)+dim ker[H²(I)→H²(O_S)]
≤1+h0(η*L)≤2.

The map H¹(O_Γ)→H¹(O_C) is surjective because the nilpotent kernel has support of dimension at most one and therefore no H². Since h0(O_C)≥1, this proves χ(O_C)≥−1 without discarding the nonreduced conductor scheme.

Now let Z be class VII and R the reduced effective resolution conductor from A.5.3. Every normalized image component of C has genus zero or one, since it is dominated by a rational or elliptic component of R. Let n0 be the number with genus zero; let δ be the sum of local delta invariants; and let v=Σ_x(s_x−1). The exact normalization formulas give

χ(O_C)=n0−δ,   e(C)=2n0−v,   0≤v≤δ≤n0+1.

For n0≥1, e(C)≥n0−1≥0. It remains to exclude v=1 when n0=0. In that case δ≤1, so v=1 is exactly one ordinary node, with two local branches of elliptic normalization. Their finite maps from elliptic curves upstairs are unramified by Riemann–Hurwitz.

Here is the actual local lifting argument at that node q. If one point p of the normalization over q sees both branches, connectedness of π^{-1}(p) joins the two lifted branch germs in R. If every p sees only one branch, partition the local irreducible hypersurface branches according to that branch of C. Both parts are nonempty. Any hypersurface germ from one part meets any from the other in a positive-dimensional analytic curve through q (two equations in the smooth threefold). That intersection lies in the conductor and is one of its two local branches, which would then be incident to both normalization points, contradicting the partition. Thus some p sees both branches after all.

A zero-coefficient π-exceptional curve cannot interfere with this argument. Adjunction and minimality of π force such a curve to be a rational (−2)-curve disjoint from R: for a curve E with zero coefficient, 0=(K_Z+D).E=2p_a(E)−2−E²+D.E, and every term has the required nonnegative sign once E²≤−2. A connected exceptional fibre meeting the strict conductor therefore consists of positive-coefficient curves. Its connecting path in R joins either two distinct elliptic curves or two distinct points of the same elliptic curve. Each possibility contradicts the genus-one conclusion of VII.1. Hence v=0 when n0=0, and e(C)≥0 in every case.

## VII.3: exact exceptional-fibre Euler accounting

First, the canonical line of the irreducible support is torsion. On a small disc, the proper direct image of the relative canonical bundle is torsion-free of generic rank one, because the smooth fibres are tori. Choose its generator. Its evaluation is a holomorphic relative canonical form whose zero divisor is a multiple aS of the only irreducible support. Thus K_Y on the tube is O(aS), and adjunction gives ω_S=O((a+1)S)|_S. Since O(mS) is trivial there, ω_S is torsion. The Cartier-divisor Riemann–Roch calculation under b2(Y)=0 gives χ(O_S)=0. The conductor line K_Z+D=h*ω_S is torsion, so VII.1–2 apply.

Let r count rational curves in R. The zero-coefficient exceptional curves are disjoint (−2)-configurations as in VII.2. Negative definiteness excludes a cycle or repeated edge in a connected such configuration: the sum of the cycle classes would have nonnegative square. Thus each is a rational tree. Such fibres lie outside the conductor, since a connected fibre over the conductor meets a strict conductor curve. Let a count all their irreducible curves. Let b count the exceptional fibres lying wholly in R whose image lies outside the conductor. Removing R upstairs and the conductor downstairs gives the exact comparison

e(T\A_red)=e(Z)−e(R)−a+b=b2(Z)−r−a+b.

Indeed contracting a zero-coefficient rational tree with k vertices removes k from the Euler number, while a positive-conductor fibre removed upstairs is represented by one point downstairs and adds one. All other resolution changes occur within the removed conductor. The actual normalization is an isomorphism T\A_red→S\C. Therefore

e(S)=[b2(Z)−r−a]+b+e(C).

The r support curves and a disjoint exceptional curves are distinct rational curves, so r+a≤r(Z)≤b2(Z). Each of the three displayed terms is nonnegative. This proves the sign with all exceptional corrections retained.

## VII.4: both equality criteria

The exact preceding formula shows that equality is equivalent to b=0, b2=r+a and e(C)=0. The curve formulas then give v=2n0 and 2n0≤δ≤n0+1, hence n0≤1. For n0=0 one gets v=0 and δ≤1. For n0=1 one gets v=δ=2; since every local δ_x≥s_x−1, equality of their sums gives equality at every point. This is exactly the first displayed criterion, including its nonreduced-conductor provenance.

For the sharper assertion, assume the actual homomorphism Pic0(Y)→Pic0(Z) is nonconstant. Since Pic0(Z) is the one-dimensional complex Lie group C*, its image is open and hence all of Pic0(Z). Put L_Z=K_Z+D=h*ω_S, a torsion line. Choose a nontrivial unitary flat line N in that image such that L_Z⊗N^{-1} is also nontrivial. The unitary character circle is infinite, so only the two specified values are excluded. Choose an actual M∈Pic0(Y) pulling back to N, and let N_T be its pullback to T.

A nontrivial unitary flat line on a compact connected complex space has no holomorphic section: the pointwise norm has the maximum principle, and a nonzero section would be parallel and trivialize it. A Gauduchon metric on Z gives deg(K_Z)=−deg(D)<0. Thus the second cohomology of each of N and L_Z⊗N^{-1} vanishes by Serre duality and negativity of the canonical twist. Their Euler characteristic is χ(O_Z)=0, so their first cohomology vanishes as well.

The normalization dualizing sheaf is ω_T=I_A⊗η*ω_S. It embeds in η*ω_S, so H²(T,N_T), dual to H0(T,ω_T⊗N_T^{-1}), vanishes after pullback to the nontrivial unitary line L_Z⊗N^{-1}. The Leray sequence for π, together with H¹(Z,N)=0, therefore forces H0(R¹π_*O_Z⊗N_T)=0. This sheaf has finite support; hence R¹π_*O_Z=0 and T has rational singularities.

The exact divisor sequence

0→ω_Z⊗L_Z^{-1}⊗N→N→O_D⊗N→0

and Serre duality give H0(D,N)=0, since H0(Z,N)=0 and H¹(ω_Z⊗L_Z^{-1}⊗N) is dual to H¹(L_Z⊗N^{-1})=0. Proper duality for the now rational resolution gives Rπ_*ω_Z=ω_T. Comparing this divisor sequence with the finite-conductor ideal sequence gives the actual identification Rπ_*O_D=O_A, as in the already checked INT.3 calculation. Thus H0(A,N_T)=0. The conductor inclusion O_Γ→η*O_A yields H0(Γ,M)=0.

Here χ(O_T)=χ(O_Z)=0, so the normalization quotient Q=η*O_T/O_S has χ(Q)=0. Finite conductor duality Q=ω_Γ⊗ω_S^{-1}|_Γ gives χ(O_Γ)=0. Twisting by the ambient topologically trivial M preserves the Euler characteristic. Consequently H¹(Γ,M)=0, and restriction to C gives H¹(C,M)=0. In particular χ(O_C)=χ(M|_C)≥0. The exact curve formula

e(C)=χ(O_C)+n0+Σ_x[δ_x−(s_x−1)]

then shows that equality forces C to be a disjoint union of smooth elliptic curves.

Every rational curve in R must now be π-exceptional, because it cannot map nonconstantly to an elliptic curve. Together with b2=r+a this accounts for every rational curve on Z. A nonminimal Z has a last (−1)-curve, which would then be π-exceptional, contrary to minimality of the resolution. Hence Z is minimal. Positive b2 and the proved NAC classification would give a rational cycle; all its curves would be π-exceptional, contradicting rationality of the singularities (formal functions surject onto H¹ of that reduced cycle). Thus b2(Z)=0. The effective conductor excludes a curve-free Inoue surface, leaving a minimal Hopf surface. Its resolution map cannot contract a rational curve, and rationality of the singularities excludes contraction of an elliptic curve. Therefore T=Z is smooth minimal Hopf. The reduced inverse conductor consists of disjoint smooth elliptic curves, and its finite maps to C are unramified. Conversely, these actual normalization and conductor maps have Euler number zero on each of their spaces, and the normalization additivity formula gives e(S)=0.

No step of the sharper criterion uses the reducibility hypothesis of INT.3; the exact duality and twisting maps have been constructed above for this irreducible support.
