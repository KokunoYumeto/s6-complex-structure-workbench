# Fourfold classification derivation frozen before reading the target proof

Frozen: 2026-11-19T18:43:37.769607+00:00

The statement of maps:src:F.4.1 and statements night:P1.12/P1.13 have been read. The proof of maps:src:F.4.1 has not yet been opened in this audit. The already-given three-connectivity, integral lattice I_{3,1}, and diagonal p1/2=(1,1,1,1) are inputs to this derivation; their construction is not re-proved here.

1. Let N=3 HP^2 # (-HP^2). Choose generators u_i of the four middle cohomology summands so that their square pairings are (1,1,1,-1), and p1(N)=2(u_1+u_2+u_3+u_4). The basis map u_i -> v_i, where v_i is the diagonal basis asserted for M_c, is an integral isometry and sends p1(N) to p1(M_c).
2. For an embedded oriented middle sphere v in a three-connected eight-manifold, the normal four-plane bundle has Euler number q(v,v) and p1 number <p1(TM),v>. The tangent bundle of S^4 is stably trivial, so subtracting its stable class changes no p1 number. The map pi_3(SO(4)) -> Z^2 given by (Euler number, p1 number) is injective: in the two Spin(4)=SU(2)xSU(2) coordinates the formulas have determinant of absolute value four. Thus the basis map in step 1 preserves the full normal invariant and hence the extended quadratic form. This is the necessary transport from the cohomology presentation to Wall's homology data.
3. Wall's classification of the extended form gives an orientation-preserving almost diffeomorphism M_c ≅ N # Sigma^8. The applicable exact theorem and hypotheses must be opened before this step is entered as a verified source check. The attached paper's own prior check remains historical evidence.
4. Kramer-Stolz Theorem A, p.178, opened at https://www.uni-muenster.de/AGKramer/linuspub/27.pdf on 2026-11-19, gives HP^2 # Sigma^8 ≅ HP^2. Both sides have signature +1. Any diffeomorphism supplied by this theorem therefore preserves orientation, since an orientation reversal would negate the signature. Taking connected sum with the three remaining summands and using oriented associativity gives N # Sigma^8 ≅ N. Therefore the homotopy-sphere ambiguity is absorbed.

This is an independent re-derivation of the classification implication, not an independent reconstruction of the fourfold or of its characteristic lattice. The archived night rows P1.6 and P1.14 report this same classification route; their omitted notes/part1.tex is not contained in the supplied night folder.

## Subsequent source check and comparison

After freezing the derivation, the complete printed F.4.1 proof was opened. Its explicit Spin(4) coordinates are (e,p1/2)=(a-b,a+b), agreeing with the injective characteristic transport above. Conway-Crowley-Powell-Sixt author v3 Definition 3.6 p12 and Theorem 3.7(1) pp13-14 were then opened and their three-connectivity, oriented dimension-eight and smooth extended-form hypotheses matched. The published source has the same statements at pp185-186. Kramer-Stolz Theorem A p178 was opened and its HP2 hypotheses matched. This closes the source gate for the classification implication.
