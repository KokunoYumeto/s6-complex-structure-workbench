# Independent derivation: cdp:st:D.1.7 (tag01G5)

The target proof has not been opened. The exact statement and its empty cited-input supplement were read. The argument uses the coefficient inclusion R_S→O_S and the reduction morphism O_S→O_{S_red}; both maps are specified here.

First treat a reduced connected compact complex space. Let P denote the image sheaf of Im:O_S→C^0(S,R). A section of P is a real function locally equal to the imaginary part of a holomorphic function. The kernel of Im consists of real-valued holomorphic functions; on every connected analytic branch these are constant by the one-variable open mapping principle along analytic discs. They glue to the locally constant real sheaf. Thus 0→R_S→O_S→P→0 is exact.

A global section u of P is constant. Indeed u attains a maximum on compact S. On an irreducible component containing a maximum point the local maximum principle for the imaginary part of a holomorphic function forces the value to be constant, by analytic continuation along its regular locus and continuity to its singular locus. Each irreducible component is compact; the same argument applies at its own maximum, so u is constant separately on every irreducible component. Constants agree on intersections. The intersection graph of the irreducible components is connected because S is connected, and hence u is globally constant. The same conclusion follows after pulling u back to a smooth compact resolution of each irreducible component, where it is pluriharmonic and the ordinary maximum principle applies; the pullback is surjective on points, so its constant value descends.

Every real constant u is the imaginary part of the global holomorphic constant i u. The homomorphism H^0(O_S)→H^0(P) is therefore onto. The connecting homomorphism H^0(P)→H^1(S;R) is zero, and exactness gives injectivity of H^1(S;R)→H^1(S,O_S).

For completeness, this is also a direct cocycle argument. A real Čech1-cocycle that becomes a holomorphic coboundary has the form a_ij=g_i−g_j. The functions Im(g_i) agree and define the above global u. Subtract i u from every g_i. The resulting holomorphic functions are real-valued and locally constant, so the original real cocycle is already a coboundary in R_S. This establishes the exact kernel assertion without changing coefficients.

Now let S carry nilpotents. The reduction inclusion i:S_red→S is the identity on the underlying topological space. Its morphism of structure sheaves O_S→i_*O_{S_red} composes with R_S→O_S to give precisely R_{S_red}→O_{S_red}. Accordingly the composite

H^1(S;R)→H^1(S,O_S)→H^1(S_red,O_{S_red})

is the injective coefficient map just proved for S_red. Its first factor is injective. All maps are R-linear, proving the statement at the claimed real-vector-space scope for nonreduced spaces too. No numerical or symbolic computation is needed.
