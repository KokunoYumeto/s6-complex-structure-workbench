# Independent derivation: cdp:st:D.1.2 (tag01G0)

The target proof has not been opened. Inputs read: the exact statement packet and its supplement (the S6_09 semidirect-product abelianization statement), plus the primary topology readings listed in `S6_SERIES_PUBLISH_II_A_primary_readings.md`. This argument retains rational and integral coefficient groups separately throughout.

1. Put B=C minus Delta and U=f^{-1}(B)=Y minus D. Properness is preserved by this base change. At every point of U the differential of f has rank one over C. Ehresmann's proposition therefore gives a smooth fibre bundle U→B with connected fibre F. The nonempty puncture set makes B homotopy equivalent to a graph with n=2g+s−1 loops. One obtains this graph by deleting s disjoint discs from a genus-g surface and retracting its standard polygon onto a spine. In particular pi_2(B)=0 and pi_1(B) is free of rank n.

2. The fibre-bundle homotopy sequence is 1→pi_1(F)→pi_1(U)→pi_1(B)→1. Choose a lift of each free generator of pi_1(B). Their universal property gives a section of this extension. Write K=pi_1(F), Q=pi_1(B). The explicit homomorphism (k,q)↦([q],[k]) identifies the abelianization of K semidirect Q with Q^ab direct-sum the Q-coinvariants of K^ab: multiplication changes the second coordinate by rho(q)k'−k', exactly the defining coinvariant relation; the two inclusions provide the inverse. Consequently

   H_1(U;Z) ≅ Z^n ⊕ H_1(F;Z)_Q.

   The splitting depends on the chosen lifted generators; the injection and quotient in the corresponding short exact sequence are intrinsic.

3. The complex orientation on Y and the positive complex normal orientation at the regular points of D identify H_2(Y,U;Z) with the free meridian lattice Z^r. Here is the low-degree justification at singular points: D has pure real dimension4, its singular locus and intersections of distinct components have dimension at most2, and a triangulation compatible with these analytic strata has no singular3-faces. Such a triangulation is supplied by Łojasiewicz, §3 Theorem2, pp.463–464, opened before this derivation was frozen. The top cochain group modulo coboundaries identifies adjacent oriented4-simplices, one generator per connected regular irreducible component. It is therefore Z^r, with the generator paired with a positive transverse disc. H^5(D;Z)=0 by dimension. Hatcher3.44 gives H_2(Y,U;Z)=H^4(D;Z)=Z^r and H_1(Y,U;Z)=H^5(D;Z)=0. Equivalently these are the transverse-disc and meridian boundary classes. The boundary map sends the i-th positive normal disc to the i-th positive meridian.

4. The exact sequence of (Y,U) with Q coefficients now reads

   H_2(Y;Q)→Q^r→H_1(U;Q)→H_1(Y;Q)→0.

   Its left term vanishes by b_2(Y)=0. Thus dim H_1(U;Q)=r+b_1(Y). Step2 gives dim H_1(U;Q)=n+t'. Subtraction proves exactly r=2g+s−1+t'−b_1(Y).

5. The equality defining t' is also justified by an explicit dual map. A functional phi on H_1(F;Q) descends to coinvariants precisely when phi(rho(q)v−v)=0 for every q,v. This is precisely the invariance condition on the dual representation. The dual of the quotient is therefore the invariant subspace of H^1(F;Q); finite dimensionality equates their dimensions.

6. For the integral assertion, all homology groups of the compact smooth manifold Y are finitely generated. H^1(Y;Z)=Hom(H_1(Y;Z),Z)=0 makes H_1(Y;Z) finite. The universal coefficient injection Ext(H_1(Y;Z),Z)→H^2(Y;Z)=0 kills this finite group, since Ext(Z/d,Z)=Z/d. Hence H_1(Y;Z)=0. The remaining quotient Hom(H_2(Y;Z),Z)=0 makes H_2(Y;Z) finite. Every homomorphism from this finite group to the free group Z^r is zero. The integral pair sequence consequently identifies its meridian boundary map Z^r→H_1(U;Z) as an isomorphism.

7. Step2 injects H_1(F;Z)_Q into that free finitely generated group. A subgroup of a finite-rank free abelian group is free, so the indicated coinvariant quotient is free. No conclusion about torsion in the source H_1(F;Z) enters this inference: the quotient map H_1(F;Z)→H_1(F;Z)_Q has its explicitly stated relation subgroup.

8. Finally f_*:pi_1(Y)→pi_1(C) is surjective. Represent a base loop outside Delta, lift it in U from a chosen point, and join its endpoint to its start by a path in the connected fibre. Projection of the added path is constant. This produces the base-loop class from a loop in Y, also after passing from B to C. Therefore H_1(Y;Z)=0 surjects onto H_1(C;Z)=Z^{2g}; g=0. The genus-zero compact Riemann surface is P^1. Substitution in step4 yields r=s−1+t'.

There is no finite enumeration, approximate numerical calculation, or stored matrix in this derivation. The only arithmetic is the exact rank identity established by two explicit short exact sequences. All statements above are proved for the hypotheses of the target; no additional geometric assumptions have been inserted.
