# Independent derivation: cdp:st:D.1.9 (tag01G7)

The target proof has not been opened. I read the statement/input packet, including only the statements of D.1.7 and D.1.8, and the empty supplement. Separate independent derivations of those two inputs have now been written and remain unreleased. The general-manifold local proof in my D.1.8 derivation supplies the dimension scope required here.

Since Y is compact smooth, its integral cohomology groups are finitely generated. b_1(Y)=0 gives H^1(Y;Z)=0, and b_2(Y)=0 makes H^2(Y;Z) finite. Connected fibres and properness identify f_*Z_Y with Z_{P^1}. The degree≤2 portion of the topological Leray spectral sequence is

0→H^1(P^1;Z)→H^1(Y;Z)→H^0(P^1,R^1f_*Z) --d_2→ H^2(P^1;Z)→H^2(Y;Z).

The first two terms vanish. The last map has finite image because its target is finite. Its kernel is dZ for a positive integer d. Exactness therefore identifies H^0(R^1f_*Z) with this nonzero infinite cyclic subgroup. Choose its generator alpha. By D.1.8, evaluated via proper base change, every alpha_c∈H^1(f^{-1}(c);Z) is nonzero.

The coefficient inclusion Z_Y→O_Y sends alpha to a section s of R^1f_*O_Y. The coherent Leray sequence, f_*O_Y=O_{P^1}, and H^1(P^1,O)=H^2(P^1,O)=0 identify H^1(Y,O_Y) with H^0(R^1f_*O_Y). Let beta be the unique class corresponding to s. The natural evaluation and base-change map sends s(c) to the restriction beta_c in H^1(F_c,O_{F_c}), and naturality of coefficient inclusion identifies beta_c with iota_c(alpha_c). Here F_c is the full scheme-theoretic fibre. Constant-sheaf cohomology uses its underlying topological space; iota_c is the inclusion into its full structure sheaf.

Use the exponential homomorphism exp(2pi i·):O→O^*. For an irrational real r, suppose a positive power n of L_r|F_c is trivial. Exactness of the exponential sequence then supplies gamma_c∈H^1(F_c;Z) with n r beta_c=iota_c(gamma_c). The coefficient map from H^1(F_c;R) is injective by D.1.7, including nilpotents. Hence n r alpha_c=gamma_c in H^1(F_c;R). H^1(F_c;Z) is a finitely generated free abelian group: it is Hom(H_1(F_c;Z),Z). In an integral basis choose a nonzero integer coordinate a of alpha_c; the same coordinate of gamma_c is an integer b. The equality gives r=b/(na), contradicting irrationality. Thus L_r has infinite order on every full fibre simultaneously.

To treat a component of Pic(Y), choose a representative M. Its Chern class in H^2(Y;Z) is torsion, so m c_1(M)=0 for some positive m. The exponential sequence identifies the Chern-class-zero subgroup with H^1(Y,O_Y), since H^1(Y;Z)=0. Choose gamma with exp(2pi i gamma)=M^m. Define T=M tensor exp(−2pi i gamma/m). Then T^m is trivial, and T lies in the same Picard component as M, because the exponential factor is connected to1 along its vector-space line. The family T tensor L_r stays in that component. Torsion of its restriction would make a positive power of L_r|F_c trivial after also taking the m-th power. The previous paragraph excludes this for every irrational r and every c.

All uses of evaluation are the natural morphisms supplied by Leray and the exponential sequence. Neither their construction nor the argument required an isomorphism E⊗C(c)→H^1(F_c,O_{F_c}). No enumeration, numerical calculation, or stored code is used.
