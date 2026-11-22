# 01FM / cdp:st:C4c: derivation before target-proof release

Status: complete finite-test argument on the smooth total-space domain of its inputs; ambient wording remains a separate gate. Target proof closed. Common analytic arguments are in S6_SERIES_PUBLISH_II_C4_prereading_common_arguments_v1.md.

1. There are finitely many critical values Sigma. On a Picard component P the universal line family and proper cohomology semicontinuity make each stated Z_c a closed analytic set. The exact full-fibre duality in the common argument identifies Z_c with the locus of nonzero H2(F_c,(T_Y L)|F_c).

2. Suppose every Z_c is proper. Their finite union has dense open complement in the connected irreducible complex-vector-space torsor P. Intersect that complement with the dense G_delta set supplied by D.1.11, and choose L there. On every singular full fibre, its H2 group is zero by the definition of Z_c. On every regular torus fibre, L restricts to a nontrivial degree-zero line and the tangent extension 0->O^2->T_Y|F->O->0 makes all twisted cohomology zero. Thus all full-fibre H2 groups vanish. The common positive-base-twist and semicontinuity argument proves generic global H2 vanishing in P.

3. Conversely suppose H2(Y,T_Y L)=0 on a dense open subset of P. Choose L in that subset and in the D.1.11 dense G_delta set. The sheaf R2f_*(T_Y L) has generic rank zero because the regular torus fibres are acyclic; it is a torsion sheaf. If some Z_c equalled P, top-degree base change at c would make this torsion sheaf nonzero. Its nonzero H0 is a quotient of H2(Y,T_Y L) by the two-column Leray sequence, contradicting the chosen global vanishing. Therefore every Z_c is proper. This establishes both directions without imposing local freeness on a possibly torsion direct image.

4. Intersect the resulting dense open H2 vanishing locus with the primary generic H0/H3 vanishing loci. There only H1 may survive, so chi=-h1<=0 and c3=2chi<=0.

5. The reduced-fibre computational test is exactly the two conormal sequences of current A.1.1. For V=Omega_Y|S, Q its torsion-free quotient, K=ker(V->Q), the long exact sequence gives H0(V A)=0 precisely when H0(K A)=0 and the connecting map H0(Q A)->H1(K A) is injective. The first sequence 0->N*->K->T->0 computes H0(K A), including its connecting map; vanishing on a torsion-free quotient alone does not suffice. For F=mS, the ideal-power quotient I^{j}/I^{j+1}=(N*)^j gives the exact current A.3.1 filtration. At every stage the long exact sequence yields 0->H0(G_j)->H0(E_{j+1})->ker epsilon_{j+1}->0. This preserves all extension maps through the full fibre.

6. For b3=0 the tangent index is one. The consequence in step4 would make it nonpositive. Hence at least one of the finitely many Z_c is all of P. Current A.3.5 gives a proper closed analytic exceptional locus for every reducible full fibre, in every Picard component; apply it after the isomorphism L -> K_Y L^-1. Therefore this fixed fibre has irreducible support. When H2(Y,Z)=0, the exponential sequence gives a single Picard component, so the same fixed fibre works for every L in Pic(Y).

The argument checks the whole finite-test statement on its identified smooth domain. It neither supplies a singular counterexample nor certifies a broader singular reading.
