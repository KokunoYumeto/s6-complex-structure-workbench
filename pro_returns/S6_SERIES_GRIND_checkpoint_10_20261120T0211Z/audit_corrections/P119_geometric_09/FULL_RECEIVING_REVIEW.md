# P1.19: complete receiving review of the integral geometric diagram

## Verdict and scope

PASS for the all-degree integral geometric comparison in `audit_p119_fresh/comparison_09/GEOMETRIC_COMPARISON_02.md`, SHA c5b7d4b21f94d941231013edf9eab19bc20d8569f91bd6049dcf81040c6b3f67. The displayed maps close the previously identified geometric common-fibre/finite-cap/cusp-marking gap. The geometry supplies the comparison with the already retained global integral complex; agreement of ranks or the old flat-volume assertion is not used to identify the required marking.

This is a complete receiving review of that new construction, including its actual q_i realization, free-chain equivalences, cone signs, integral cap correction, cusp inverse word, prescribed invariant tori and final local-duality/F_k reduction. It is not a fresh whole-before-reading derivation of P1.19. The exact chronology is separately preserved in `receiving_sign_reconstruction.md` and `sign_reconstruction_exposure.json`. The target formula had already been supplied when the cusp identity was independently recalculated; its new proof sections were opened only afterward. During the checkpoint filesystem hold the calculation was committed in a collaboration message, and the file was saved after the hold. No file is backdated.

Reviewer: GPT-6 Astra, ChatGPT Pro mode; inherited reasoning effort not separately exposed. Full target proof, full `geometric_diagram_check_02.py`, full `top_chain_adapter.py` and full `derive_chain.py` have been read. The complete retained BEFORE_READING sections3–6 were reopened for the integral reduction, and the actual finite geometric input was reopened at P1.12 proof Steps1–5, especially equations(1.12.4)–(1.12.5) and source-packet lines400–458,488–555.

## 1. The literal finite maps and all four cell rows

The input's evaluation map E_c has the displayed inverse formed from the real and imaginary parts of the period matrix. Its transport square preserves the specified lattice and zero section. The attaching correction h_c=LJ_c(u)v obeys the actual monodromy law. Translation by -s chi h_c is an equivariant isotopy, with inverse translation and with the outer collar fixed. Thus the ensuing finite map concerns the actual gluing, including its original marking.

In the literal split lattice basis P_i=(epsilon_i v_i,e_1,...,e_5), write t for the first circle, y for the transverse five-torus, and theta for the boundary mapping-torus coordinate. The map is exactly

  q_i(t,y,theta)=[y,theta+mu_i t],  mu_1=5, mu_2=-4.

The changes Q_i=P_i diag(1,K_i) and K_i are actual torus automorphisms. Both Q_i and K_i have determinant -1, while both P_i have determinant +1; the two orientation signs therefore cancel in the raw top-cell degree. The new certificate checks the literal transports, and the independent receiving calculation below recomputes their map from backwards sweeps when mu_i is negative.

There are four kinds of source product cell, with the indicated exact images:

| Source cell | Image and geometric reason |
|---|---|
| A transverse y-cell | The same cap fibre cell: t=theta=0. |
| t times a transverse cell | Subdivide the base interval into abs(mu_i) strips. Each positive strip transports the transverse cell by the corresponding power of R_i. For mu_i negative the oriented sum is -sum_(j=1)^m R_i^(-j). Since R_i^m=I this equals -sum_(j=0)^(m-1) R_i^j, with the negative orientation retained. |
| theta times a transverse cell | One positive cap-base strip, with the actual transverse cell. |
| theta times t times a transverse cell | Zero pushforward in that dimension. On every affine subdivision chamber dq(partial_t)=mu_i dq(partial_theta); the two base derivatives are dependent. The transverse derivative does not restore the missing dimension. The projected polyhedral chain is therefore dimension-dropping on every piece. |

The boundary faces of adjacent subdivision chambers cancel with their induced orientations, so the last row has no extra interface chain. The map is continuous through the mapping-torus identifications because R_i has the stated finite order. At t=y=0 it sends theta to the literal positive based cap meridian; it is not identified only by its image in an abelianized group. The norm and affine-meridian maps in (1.12.5) are therefore exactly the ones used in the new diagram.

## 2. Integral geometric chains and the actual equivalences

The polyhedral complex P_*(T^6) uses finite integral chains with rational affine simplices, cut at the integer translates of the coordinate faces, modulo oriented subdivision. A finite collection of such projected chains has a common rational triangulation. Refinement maps are induced by the identity of the underlying torus, with the ordinary subdivision prism giving their chain homotopies. In a countable cofinal nested refinement, each chain-group inclusion splits over Z by reading one chosen subdividing coefficient for each old open simplex. The successive complements are free subgroups of free abelian groups. Thus the direct-limit chain groups are free and their homology is the integral torus homology.

The map C sends each exterior basis element to the actual oriented product of its coordinate circles. Those cycles are the usual product-cell homology basis, so C induces the integral homology isomorphism with its specified basis. Addition defines the Pontryagin product on these polyhedral chains. Triangulated products give the exact signed Leibniz identity, and the interchange of factors has the graded orientation sign. The triangle chains A_v have the actual boundary C_1(v)-ell_v, including negative and repeated coordinate windings. The stated ordered telescoping product consequently has boundary C wedge Q-Q_*C before any reordering is invoked.

The degree-five replacement D_Q has the same required boundary. The source complex L has zero differential; therefore there is no adjacent-degree compatibility term concealed by replacing that component. Degree six has zero homotopy component because both maps send the fundamental chain to det(Q) times the same chain. These are equal geometric top chains after common subdivision, not merely equal homology classes. The floor composition identity retains the determinant sign of the pushforward and the integer changes of fundamental cube.

For a monodromy M, the geometric cylinder model has differential

  d(a,x)=(partial a+(M_*-I)x,-partial x).

The map to the actual mapping torus is the fibre inclusion plus the oriented interval-first prism. Its boundary is (M_*-I)x minus the prism of partial x, which fixes the sign. The relative quotient by the fibre is the suspension of that fibre. On the relative homology sequence this prism map is the indicated identity on the shifted torus homology; on the fibre it is the identity. The long exact sequence therefore proves an integral homology isomorphism. Two actual edge cylinders give the same argument for the graph. For the finite caps, signed coordinate permutations preserve the product circle cells, and their action on the actual oriented cells is the exterior power. The e_i maps are therefore actual cellular/prism equivalences to the geometric cap cores.

The complement is the homotopy pushout of its graph part and actual finite caps along the collars. Their deformation retractions and collar prisms give the geometric cone. The maps Phi_G, Phi_i and e_i induce homology isomorphisms on its unshifted and shifted pieces, so its cone relative sequence gives the integral equivalence Psi_Y. All these complexes are free. The cone of each quasi-isomorphism is acyclic and free; its boundary subgroups are free, so choosing integral sections gives an actual contraction. This yields chain-homotopy equivalences without assuming that the finite-cap homology itself is free. The separate free-homology decomposition is used for the torus fibre and the cusp cap, where that hypothesis is supplied and checked.

## 3. Common fibre, finite-square signs and the top correction

The underlying equality is partial H_i=C-Ctilde_i. Substitution into Hcal_i(f,x)=(H_i f,-H_i x) gives

  d Hcal_i+Hcal_i d=((C-Ctilde_i)f+(H_i W_i-M_i* H_i)x,(C-Ctilde_i)x).

This is precisely Phi_i^Q-PhiTilde_i. Applying the actual q_i produces the all-degree finite homotopy Z_i. Its source degree-five component is the specified floor chain; its lower components are the explicit triangle products. Thus there is no remaining extension problem for a top-degree homotopy specified without its lower components.

For the negative coordinate of the order-four signed cap, the floor comparison adds one fibre top cell to the specified suspension sigma. In these conventions d sigma=-2z and q_2[T^6]=-4[E_2]. Consequently Hcap_2(z)=2[E_2] has the required boundary-homotopy effect -4[E_2]. The determinant signs of the literal Q_2 and K_2 transport this to the raw row 2h_2, with h_2=(1,-1,-1,1,-1,0). This uses an integral top chain. The rational auxiliary beta row is not asserted to be an integral chain automorphism.

Since U_i-I is nonzero only on B_i degree6 and its image is in the fibre L_6, while H_(i,6)=0, one has Hcal_i(U_i-I)=0. Therefore Z_i U_i=Z_i and the full finite homotopy is exactly Z_i+e_i Hcap_i, with no omitted cross-term. For F=(j_G,-b_1,-b_2) and its geometric counterpart, the diagram defect Phi_D F-Fgeom Phi_B is +dZ+Zd on the cap components. The cone map consequently adds +Z on the shifted boundary component. This fixes the sign used by Psi_Y and S_Y.

## 4. Cusp inverse word and the actual invariant-torus cycles

The based inverse-word prism map is J0(a,x)=(a,-M_2*M_0*x,-M_0*x), with its actual zero clutch translation. The two strip coefficients give dJ0=J0d by the identity

  -(M_1-I)M_2M_0-(M_2-I)M_0=M_0-I.

Extending K by K_gh=K_g W_h+M_g* K_h and K_ginv=-M_ginv* K_g W_ginv gives the required boundary identity in every degree. Expanding those formulas gives the displayed R(f,x)=(0,K_g1inv x,K_g0 x). Its two edge boundaries carry the minus sign in the cylinder differential, and its fibre boundary is exactly -K_1 W_2 W_0-K_2 W_0-K_g0. Also R d_B=0 since R vanishes on the fibre summand. The new code keeps the left target actions as formal reduced words, so its verification does not replace geometric actions by homology matrices.

For each actual invariant five-vector x_j, its covector l_j is primitive and fixed by M_0^-t. The floor-density calculation committed before opening Section7 gives exactly

  Phi0(0,x_j)-(0,H_lj)=partial(0,-D_lj).

This uses the specified integral seven-chain and retains its minus sign. The nonzero h_0 X=(0,-2,-2) is explicitly recorded; the new construction does not hide that old-to-new marking change. The simultaneous comparison uses both this boundary and the R homotopy, so the same invariant torus is tracked into the complement.

Under the actual toric cusp retraction its base satisfies b_j=0 and has dimension at most2, while the angular fibre has dimension at most3. Subdivision by its finite moment-cell stratification gives image dimension at most5, so the six-dimensional mapping-torus fundamental cycle maps to zero. The previously received P1.11 bounded-unit deformation transports the whole marked boundary retraction, retaining this homology value. The meridian is separately exact because K_(g,0)=0: (0,1) is the actual zero-section meridian and bounds its specified cusp disc.

## 5. Final gluing and the saved integral reduction

Here is an explicit sign version of the final comparison. Transfer the geometric cusp cap to its free homology by the fixed contraction p_C, and define j_C^act=p_C q0 Phi0. The cusp-to-complement defect is

  Psi_Y jY-jY_geom Phi0=dR+Rd.

The full gluing map, with attaching column(jY,-j_C^act), is consequently

  (y,c,b) -> (Psi_Y y+R b,c,Phi0 b).

This is the +R case of the cone formula in Section5. The separate generic formula Cone(F)->Cone(F') for F'-F=dT+Td is (a,b)->(a-Tb,b); its direction agrees with this actual formula when the defect is assigned consistently.

On the common fibre, Psi_Y sends its literal numerical inclusion to C exactly: all edge coordinates and shifted boundary coordinates are zero. Hence each saved identity d_Y F_k=J_k becomes an actual geometric filling of that common fibre under Psi_Y. No new top-cell marking is silently imposed on those fillers. The four identities for k=2,3,4,5 were freshly multiplied in the receiving check below.

The supplied cusp collapse has primitive image and the stated kernel. The old integral Smith maps identify that actual quotient with the fibre generators in the reduced boundary model. The cusp cap has free homology, so the displayed integral contraction onto its homology applies. Its actual transferred boundary map may still have suspension values; they are not assumed zero.

Local Poincare–Lefschetz duality applies to the actual compact oriented smooth eight-dimensional cap W with boundary B. Since the absolute cap homology is free, its relative groups are free. The cap-pair sequence, together with surjectivity of the degree-five fibre collapse, makes the degree-four boundary image rank9. It contains the primitive rank-nine collapse image, hence equals that image. In degrees2,3,5 the collapse is onto. Thus every free suspension value in degrees2–5 lies in the prescribed collapse image.

The source shear s -> s-iota h(s), fixing every fibre generator, removes those values. Its inverse is s -> s+iota h(s). Its change in the complement map is -J_k iota h, filled by the actual -F_k iota h. This homotopy is zero on the fibre generators, so its composition with the residual boundary differential is zero. The analogous shear t -> t-iota w retains d t=2z. These are the explicit source and target maps required for the reduction.

The remaining local relative cone column is(a,-2)^t. Its torsion would have order gcd(a,2); the actual local duality group is free, so a is odd. Put k=(a-1)/2. On the relative column, the unimodular matrix[[1,k],[0,1]] sends(a,-2) to(1,-2). For the global cap sign, [[1,-k],[0,1]] sends(-a,-2) to(-1,-2). These are the precise cone shears associated to the cap homotopy on z. They identify the actual secondary term, without invoking duality or the homology answer of the closed manifold.

The retained full global complex and its literal receiving-array adapter therefore apply. The mathematical geometric-comparison gap is closed at this scope. Original computation and source records retain their actual reading/verification chronology.

## 6. Fresh finite evidence and preserved limits

`exact_receiving_checks.py` was written and executed after the complete receiving proof/code reading. It passed50 assertions. It reconstructs the four finite rows from actual forward/backward interval sweeps and compares their Q/K transports in degrees0–7; verifies both raw orientations and top degrees; multiplies all four saved integral F_k against the literal complement differential; and verifies the relative/global odd-secondary shear signs. The filler sizes are132x15,155x20,118x15,57x6. The exact code, JSON output and stdout are retained here.

The new author's154 and113 checks were read with their code. They are not counted as executions by this reviewer. Earlier actual cusp186, global989 and saved-global914 checks remain in `V_P111_receiving_receipt_06.json` and `V_topology_receiving_receipt_07.json`; these receipts were reopened, and those old programs were not rerun here. Their global numerical agreement alone was never used to close the geometric gate.

The precise local-duality primary source is the retained opening of Hatcher, Theorem3.43, printedp254, documented in `primary_sources/Hatcher2002_author_07.metadata.json`. No new primary-PDF opening is claimed in this receiving review. The actual collar maps and cusp collapse are the received P1.12/P1.11 inputs at the exact scope above.

No shared source, canonical row or whole-row completion was changed here. Root's integration of the complete proposed proof, reconciliation with the retained whole-row exposure/credit evidence, and current PDF review remain publication tasks. This report supplies a receiving PASS for the new mathematical geometric-diagram construction.
