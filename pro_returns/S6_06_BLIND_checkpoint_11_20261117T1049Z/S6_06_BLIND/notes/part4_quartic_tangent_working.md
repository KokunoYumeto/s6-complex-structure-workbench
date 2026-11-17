# Unrestricted quartic tangent obstruction

## P4.52 candidate — proof awaiting independent audit

In the remaining positive ruled support of Part4.2, the image of a contracted horizontal pole section has ambient multiplicity exactly three. No generic-transverse-type hypothesis is imposed.

### 1. The local form comparison

P4.51 proves that every local Milnor fibre of the actual support has zero rational intersection form. Let g=g_d+g_(d+1)+... be the reduced local equation, with homogeneous leading polynomial g_d. Suppose g_d is reduced. Every finite set of cycles in the smooth affine surface M_d={g_d=1} transports, together with their intersections, into a local Milnor fibre of g.

Indeed choose compact smooth cycle representatives and a compact neighbourhood K of their union in M_d. The gradient of g_d has no zero on M_d: Euler's identity gives sum x_i (g_d)_(x_i)=d there. For positive real epsilon set G_epsilon(x)=epsilon^(-d)g(epsilon x). These functions converge with every derivative to g_d on a neighbourhood of K. A compactly supported horizontal vector field for the family G_epsilon=1 transports a neighbourhood of K into G_epsilon=1 for all sufficiently small epsilon. Explicitly on that neighbourhood we solve dG_epsilon(V_epsilon)=-partial_epsilon G_epsilon using the Hermitian gradient divided by its squared norm, and multiply by a cutoff equal to one along the compact trajectories; integrate for small epsilon. Multiplication x↦epsilon x then gives an orientation-preserving embedding into g=epsilon^d inside the fixed original ball. Compact cycles and transverse intersections remain there. Thus the pairing of M_d must also vanish. This argument compares smooth nonzero level sets on a compact neighbourhood; it makes no equisingularity assertion about the zero set or its boundary.

For a homogeneous reduced polynomial, its global fibre M_d and a sufficiently large compact Milnor fibre have the same relevant finite-dimensional homology and monodromy. A direct justification is as follows. The affine fibre is semialgebraic, so the squared radius has finitely many critical values; above the largest value, its proper gradient flow gives a product end. Intersect with a large invariant ball and rescale to a small Milnor ball. The scalar monodromy x↦exp(2pi i/d)x preserves this compact core. The usual local Milnor-fibre CW dimension bound gives H_j=0 for j>2; the reduced polynomial makes the fibre connected.

### 2. The exact variation-map inequality

For a reduced homogeneous polynomial whose projective plane curve has isolated singular points, put M=sum mu_i for their transverse plane-curve Milnor numbers. Write F for its compact Milnor fibre, ∂_2F for the part over the singular-link circles, T for the monodromy on H2(F;Q), j:H2(F;Q)→H2(F,∂F;Q), and j2:H2(F;Q)→H2(F,∂_2F;Q).

The source used here is Dirk Siersma, *Variation mappings on singularities with a1-dimensional critical locus*, Topology30(1991),445–469, §§3.6 (printed pp451–452),5.3,6.3 and7.1 (printed p462), primary scan https://webhomes.maths.ed.ac.uk/~v1ranick/papers/siersma.pdf . The exact identity is

j2 (T-I)=VAR'' j.

It is the chain-level variation identity and requires no assertion that VAR'' is an isomorphism in dimension two. The n=2 modification discussed in §6 changes that isomorphism assertion, not the displayed identity. Poincaré–Lefschetz duality identifies j with the intersection pairing. When that pairing is zero, Im(T-I) lies in ker j2. The exact homology sequence of (F,∂_2F) identifies ker j2 with the image of H2(∂_2F). Each component of ∂_2F is the mapping torus of the transverse plane-curve Milnor fibre; its Wang sequence gives H2=ker(A_i-I) in H1(F_i). Consequently

rank(T-I) <= sum dim ker(A_i-I) <= M.                 (52.1)

All spaces here are compact manifolds with their specified boundary parts. The same argument with an empty ∂_2F gives rank(T-I)=0 for an isolated singularity with zero form.

### 3. The quartic numerical contradiction

Suppose the reduced projective quartic curve D={g4=0} has a normalization component of positive genus. Its possibilities by degree are an irreducible quartic of normalization genus g>=1, or a smooth elliptic cubic plus a line. In the first case sum delta=3-g<=2 and hence M=sum(2delta_i-r_i+1)<=4. In the second case the cubic and line meet by Bezout, their total intersection length is three, and their singularities have sum delta=3 and sum(r_i-1)>=1; thus M<=5. In both cases M<=5.

The quotient map {g4=1}→P2\D is an unramified fourfold cover. Normalization and the plane-curve genus formula give

chi(F)=4 chi(P2\D)=4(7-M).

Let ζ=i. The maps x↦ζ^k x, k=1,2,3, act freely on F. Their Lefschetz numbers vanish. Equivalently the virtual μ4-representation H0(F)-H1(F)+H2(F) equals (7-M) times the regular representation: its character is chi(F) at the identity and zero at the other three elements. For each nontrivial character χ this gives

dim H2(F)_χ=dim H1(F)_χ+(7-M).

The monodromy has finite order and is semisimple over C, so

rank(T-I) >= 3(7-M) >= 6 > M.

This contradicts(52.1). Thus a quartic tangent polynomial with a positive-genus reduced component cannot occur in the actual remaining support.

### 4. The pole comparison and the multiplicity conclusion

Blow up the ambient origin and use exactly the comparison map of P4.39: the minimal resolution T1 of the normalized strict transform dominates the minimal normalization resolution of the original germ. A positive-genus exceptional curve H persists under the intervening point blowups with pole coefficient two. Let E be the ambient exceptional divisor, n=ord_H(E)>0, and a>=0 the coefficient in the total pole divisor D1 relative to the strict-transform dualizing sheaf. Adjunction gives

2=(d-2)n+a.

Effectiveness follows from the negative-definite exceptional matrix as in P4R.6; every exceptional positive-genus curve has strictly positive coefficient in D1. Therefore d>=5 is impossible. If d=4 then n=1,a=0, so H is not exceptional over the normalized strict transform and is not over its conductor. The normalization is an isomorphism at its generic point. Since n=1, its image is a multiplicity-one component of the quartic exceptional curve; the map of H to the normalization of that component is birational. Thus that component has positive genus. A degree-three positive-genus component leaves at most one linear factor, and a degree-four component leaves none; the entire quartic polynomial is therefore reduced. Section3 supplies the contradiction.

If d=2, P4R.15 identifies the actual local equation with a product X²+Y^m. Each analytic branch has smooth normalization (for odd m its normalization is the explicit parametrization (Y,X,Z)=(u²,u^m,Z), up to a nonzero constant; for even m the two smooth branches are X=±iY^(m/2)). A positive-genus exceptional curve cannot lie over such a germ. A smooth point d=1 likewise has smooth normalization. The only remaining ambient multiplicity is d=3.

Code/part4/quartic_tangent.py verifies the finite character inversion and every integer bound for 0<=M<=5; the proof uses no numerical approximation and does not replace the unresolved cubic case by a completion.
