# K111: exact review of the revised auxiliary filling and its inherited inputs

## Scoped conclusion

The revised sections C and F of `audit_sign/K111_new_auxiliary_proof.tex` close their mathematical boundary-comparison gate. The new regular toric atlas is a filling with its own tangent bundle and physical circle action. Its exterior is identified with the original marked source and point line on the full localized charts. Its moving cap is attached by the actual outer normal derivative, with its new interior normal divisors retained. The twelve lower bodies are identified by their 36 complete resolved-source charts. The resulting Stokes comparison uses those data and the finite covering factors already specified in CFL/ASI2.

I found no additional mathematical gap in that argument. A map from every new interior cone to the older resolved point graph is not a term in this characteristic-number comparison. The recorded failures of that stronger map remain visible and are not removed: **8,723 / 229 / 184** full graph crossings at zero/one/infinity, including **26 of the 31 moving charts**. The construction does not resolve a further graph inside the atlas whose characteristic data were counted.

This review verifies the precise C/F, moving-normal, lower-body and inherited-statement comparisons. The separate construction of the full regular fans and the full compact-owner calculation are the sign agent's supplied certificates and the parent's independent owner recomputation. I do not recast those computations as work performed by this branch.

## Exposure and actual fresh work

Before opening the new proof, I read its isolated theorem statement and the sign agent's stated target. `K111_auxiliary_boundary_before_reading_05.md` records my derivation of the boundary Stokes mechanism and the geometric checks to perform. It is a before-reading mechanism derivation, not a claimed independent reconstruction of the enormous new fan.

I then read all revised sections A–G; the final scope sections of `K111_auxiliary_resolution_comparison.md`; the original I2P.1–9; original NC.1–20; NS.2–5 and NS.18–23b; IL.20–35 at the exact source/line/flow scopes used; CFL.27–31; and the relevant ASI2 attachment, localization, path and reference paragraphs. I read F41 and F46's actual source/root/topology proofs and K96's complete 600-line proof. For K94 I read the actual shared source/translation charts EU.0 and the annular/fan/quotient portions EU.4–5; its entire separate M6 theorem is not newly independently re-proved here.

Three fresh programs were written without importing any producing implementation:

| Program and output, both under `code/` | Actual result | Scope |
|---|---:|---|
| `independent_K111_boundary_normals_05.py` / `.json` | **137,749** exact assertions, **5.588627 s** | Complete source rows, all **6,677** exterior faces, all **36** lower charts, full point/O unit action, all **31** moving derivatives, **29** chronological blowdowns, intersections, NC matrices/ball inverse and directed arithmetic. |
| `independent_K111_period_actions_05.py` / `.json` | **2,464** exact assertions, **4.770790 s** | All **352** full period pairs and their inverse maps preserve both native cocharacters and both base parameters; matrix inverses checked. |
| `independent_K111_inherited_scope_05.py` / `.json` | **18** exact identities, **0.234916 s** | Source discriminant/selected path, SI2 parameter and meridian, doubled section, cubic root and all six Miller weights, and exact F41/F46 specialization. |

Their SHA256 values are, respectively,

* `1cc33ae9b10925bde2fb77f1efe06bdd88066feb4b3304ca822656afd16b9d3c`;
* `f4d92a19759e9e9d0e7b49c9c7bc95991d41a89166a88ee717ae16dce754679c`;
* `89fc8816a4150d8a158af460d676a9148e6c63b5f8d199e9ac9a0d91cbda2b51`.

The period reader's first execution stopped on a schema assumption: zero has a named native `lattice_matrix`, whereas one/infinity store local chart matrices. The original program and failure description are preserved as `independent_K111_period_actions_05_attempt01.py/.txt`. The corrected reader reconstructs the actual native map as `B_target * local_matrix * B_source^{-1}` and its reciprocal in the reverse order. No mathematical assertion failed in that attempt. These three runs are post-reading computations and are not counted as blind whole-proof reconstructions.

## 1. Exact exterior and point-line maps

The original I2P common band is retained:

\[
x=pP^3Z_c,\quad y=Z_c^{-1},\quad xy=P^2R,\qquad
v_2=\eta P^2X_cZ_c/f_{P^2}(x).
\]

On each original source band the corresponding `Q^j` and `P^(2j)` factors remain. The point graph is exactly

\[
x=P^2a,\ ay=R;\qquad xc=P^2,\ y=Rc,
\]

with the two source resolutions

\[
(P,x,c,y)=(uw,u,uw^2,Ruw^2),\qquad
(P,x,c,y)=(uw,u^2w,w,Rw).
\]

The fresh program derives the original valuation rows directly from the printed endpoint formulas, rather than accepting the saved graph-route classifications. For zero they are `x=y_native+3j r+j z`, `y=−y_native+3(1−j)r+(1−j)z`, `P=r`, `R=r+z`; for one they are `x=3r−x_native`, `y=x_native`, `P=R=r`; for infinity they are `x=y_native+3r+2z`, `y=−y_native`, `P=r+z`, `R=r`. It checks the full source equation on every saved cone, and then every actual nonempty localized exterior face.

On those faces the three actual regular maps are `a=x/P²`, `(u,w)=(x,P/x)`, and `(u,w)=(x/P,P²/x)`. Every required row is nonnegative. The returned maps into the source satisfy the displayed equations identically. At infinity, the full lower cone uses

\[
u=R^2u_{\rm base}Z_c,\qquad w=R^{-1}Z_c^{-1},\qquad P=Ru_{\rm base};
\]

substitution gives `x=u²w=R³u_base²Z_c`, `y=Rw=Z_c^{-1}` exactly. The period maps, inverse character maps and the identical localized lower fans identify the whole exterior, not just its valuation support.

The actual point/O line is checked at its original Cartier generators. I2P gives

\[
b f_b(x)=(b-x)E,quad b=P^2,qquad
v_2=(a-1)^{-1}A=(c-1)^{-1}C,\quad C=-cA.
\]

Under `(Xc,Zc)->(xi Xc,zeta Zc)`, the complete genuine coefficient is

\[
v_2'=\xi\zeta\frac{f_b(x)}{f_b(\zeta x)}v_2.
\]

Substitution yields exactly

\[
a'=\zeta a,\quad A'=\xi\zeta(E/E')A;qquad
c'=\zeta^{-1}c,\quad C'=\xi(E/E')C.
\]

At O, I2P.7 has `v2=(x−1)C_O` and
`f_b=(x−b)E_O/[b(x−1)]`, so the exact map is

\[
C_O'=\xi\zeta\frac{x-b}{\zeta x-b}\frac{E_O}{E_O'}C_O.
\]

This retains the original `b=P²` denominator and the extra `P^(−2)` in the original O-to-regular map. The fresh algebra verifies all these maps, their compatibility and their complete composition law with the E factors as independent symbols. The middle E factor cancels on composition; it is not replaced by its central value.

The required analytic domains also work. A small node polydisc is invariant under `|zeta|=1`, and every factor in the normally convergent I2P.3 product and reciprocal remains a unit there. On the O annulus `1/2<|x|<2`, with `|P²|<1/4`, both `x−P²` and `zeta x−P²` stay nonzero; the full I2P O products remain units after a uniform source-radius restriction. Thus the formulas extend through the actual point and O sections. Setting zeta=1 gives precisely `v2'=xi v2`, identifying the original physical nonzero-vector line.

The independent period check reconstructs or reads each native period matrix and its inverse, checks their product, and verifies that both cocharacters and both base coordinates are fixed. There are 302 zero pairs, 25 one pairs and 25 infinity pairs. All full analytic unit arguments are therefore invariant under the two compact circles. This establishes the global torus action on the new atlas at the exact C/F scope.

## 2. Moving normal bundle and the NC cap

For every one of the 31 new moving charts the program verifies membership in the actual endpoint atlas, then applies the literal NS.5 alignment

\[
(X,Y,P,p)\mapsto(P^8pf_0X,P^6pY,P,p).
\]

Its lattice matrix, the complete `f0` factor and its reciprocal are retained. In the aligned zero frame the normal characters are
`(1,−2,1,1)` and `(−1,1,0,0)`; the infinity frame adds `(0,1,0,0)` to both. The full unit pairs are exactly `(c_q f0/eta,eta/f0)` after T0 and `(c_q/eta,eta)` on the first face.

Evaluation on the two actual normal rays gives the standard basis `(1,0),(0,1)` in physical order `(-1,+1)`. Both P and the native fixed-curve coordinate have zero normal order, and p contains the product of the two normal coordinates. Therefore the first normal derivatives of every full base unit vanish on the fixed surface, exactly as asserted in the original NS.23 proof. This calculation remains valid on the new 31 charts: the outer normal map is

\[
N_\theta^+=G_0(Z)\operatorname{diag}(\overline{e_-},e_+),\qquad
G_0(Z)=\begin{pmatrix}1&-Z\\\bar Z&1\end{pmatrix}.
\]

The program verifies the other-chart identity
`G1(1/Z) diag(bar Z,Z)=G0(Z)`, the full normal inverse, the right-coefficient Cox overlap, the whole collar product and the positive-Hermitian-ball inverse. The determinant is `(1+|Z|²) bar(e_-) e_+`, nonzero on the actual outer collar. The transported Hermitian normalization therefore gives inverse sphere maps in both directions.

The original NS.23a and NC.17–19 explicitly use this as an invertible boundary map where P is nonzero. They retain its tangent monomials' actual central divisors in the interior. Thus the new 26 ambient point-graph crossings do not change the definition of this cap map. The normal bundles over the interior are computed on the new surface itself.

The fresh program reconstructs its entire ordered source fan, its 30-by-30 divisor intersection matrix, and all 29 chronological sum-of-neighbor blowdowns. Each blowdown has the actual maps `(u,w)->(u,uw)` and `(u,w)->(uw,w)` and reciprocal localization. It obtains

\[
D_-^2=-309,\quad D_-D_+=293,\quad D_+^2=-305,\qquad
hD_-=-4,\quad hD_+=5.
\]

The chronological exceptional-coefficient computation independently gives the same three products and ends at the actual native sphere times the original P disc. The NC.19 equality `C_hat B=N`, with `B=C^{-1}N`, gives the cap-completed bundle, including all constants and units. The rounded `D³×D²` bordism in NC.20 extends this exact bundle to the closed replacement. Its ordered positive lines are `x=h+D_-`, `y=−h−D_+`, giving

\[
(x^2,xy,y^2)=(-317,-294,-295),\quad
(c_1^2,c_2,p_1)=(-1200,-294,-87).
\]

Using the actual physical negative-line conjugation in ASI2.41 gives `(-906,-111)`. The reference retains its own cap with all three characteristic numbers zero. This comparison is made by the explicit NC bundle bordism, not by assigning the old cap's characteristic numbers to a different interior.

## 3. The twelve lower bodies

Every one of the twelve owners has exactly three complete charts, and all 36 are checked against the current endpoint cones and the original graph/resolution equations. This is a full local source isomorphism at the charts on which the IL comparison is used.

The source and line arrows are the original IL.20–31. In particular the full normal factors satisfy

\[
H_{+,l}=\eta_2u_s^lP^{-l}X^{-1},\quad
H_{-,l}=\eta_2^{-1}XP^{l+1}u_s^{-l-1},\quad
H_{+,l}H_{-,l}=P/u_s.
\]

Their source-period factors `P^(−2),P²` and entire
`gamma=p u_s^12 c12=P² lambda0 q eta2^6/t³` agree with the original source-cell reindex, including every `gamma^j`. The IL source horizontal field, its backward flow, the original-frame linear ODE and the reciprocal ODE supply the complete map to the fixed reference. The inverse first recovers the source point and then uses reciprocal normal coefficients. The prescribed good cubic cap square is retained on its protected annulus.

The source is the actual minimal I3 chain with the original marked point/O degree vectors. The cube frame and its reciprocal are the original IL.33–37 ones. Accordingly the collision pairings `(-2/3,−1/3,−2/3)` and the reference pairings `(-2/3,+2/3,−2/3)` glue with the exact torsion identity `I(-1,-1)^t=(1,1)^t` to `(0,−1,0)`, tangent p1 zero. Each double contributes `(1,−2)`, and all twelve contribute `(12,−24)`.

## 4. Boundary localization, finite stabilizers and orientations

The before-reading note first wrote the free-circle quotient version of Stokes. The actual CFL/ASI2 argument uses finite covering slices where stabilizers are nontrivial. This is sufficient: away from a fixed point the closed stabilizer subgroup of S1 is finite, so the quotient has these local finite slices. Average the tangent and physical-line connections over the compact circle and each finite group; integrate their descended characteristic forms with the explicit reciprocal covering degree. On common slice refinements the degrees and pullbacks agree. Ordinary Stokes on the covers, followed by that weighting, gives the same boundary formula. Global freeness on the new interior is not an extra required hypothesis.

The actual outer source/point-line maps and the NC/IL derivative maps transport the connections. Identical interpolations on opposite collars are taken in reverse interval directions, so their full Chern–Simons transgressions cancel pointwise. The stable tangent restriction to an oriented boundary is its tangent bundle plus the trivial outward line. Consequently the relevant integrals are exactly the physical e³ and p1 e boundary pair, with the original circle-first orientation and all finite Euler factors of CFL.27–31.

With the complete compact-owner result supplied by the producing and parent certificates, the same-atlas sum is

\[
O_c-O_{r,1}=(895,139)+(12,-24)+(-906,-111)=(1,4).
\]

The new interior is used for every collision-side term. The fixed-source reference and its own caps remain the original ones. The full RFB reference transport then gives `(72,0)`, and the explicit parameter reversal `[y,t]->[y,1−t]`, with its physical-line lift, gives `(71,−4)` in the Jin direction. The held-product formulas give `(-1,72)` and the physical inverse clutch gives 12. My fresh arithmetic checks these directed equalities; the full compact-owner ledger is credited to its separate checked construction.

## 5. Exact inherited statements and their maps to this target

| Input | Exact used specialization and map | Scope retained |
|---|---|---|
| F41 | Its E6-B source is literally `y²=x³+tx+t²`, `G=(0,t)`, the r_src=0 fibre of K111. Choose `(a,b,m,n)=(2,3,3,1)` and the same prescribed cubic character/reference. Instantiate its selected Hom section by the actual EX.2 coefficient `B_sel=(t+4/27)B_2,3/t³`. Its sphere and primitive source/Hopf attaching maps give the initial oriented S6. | The original line, three-step source translation, scalar root and meridian `3q+gamma_out` are retained. The scalar is the one in the actual EX.2 section, so no unidentified rescaling is needed. |
| F46 | The same initial object has `(m6,n6;m2,n2)=(3,1;1,0)`, hence `D=1`. At the III site `k=0` in F46.5 gives `(z,X,Y)=(t,x,y)`; the order-one deck and norm-zero map are the identity, and F46.9 gives `H2=B_lambda`. Thus this is the original ordinary III piece. At infinity it is the identical cubic map F46.4. | Its full integer maps provide the same sphere criterion. No parameter-return conclusion is taken from F46. The fresh code checks the b=3 degree-two determinant with both arbitrary collar integers and the exact degree-one specialization. |
| K96 | Use the `(a,b,m,n)=(2,3,3,1)` row at r_src=0 and its full local source/Cartier/good-root family. EX.1 is exactly K111's six-factor chronological Miller section; EX.2 is exactly its selected scalar coefficient. EX.3–4 with l=1 give `q_infty=z³`, `x=z^(−2)X`, `y=z^(−3)Y`, `t=z^(−3)` and `B_sel=(1−t_c z³)B'_2,3`. EX.14–19 retain the marked point/O correction, prescribed finite character and whole reference cochain. | The local disc theorem is used at the initial unselected III value. The actual parameter path described below transports that initial sphere to K111's positive s_* fibre. K96's zero-return assertion about a small loop at r_src=0 is not used as a statement about the loop at r_src=1/4. |
| K94 | K96 imports the identical source coordinates `(x,y,t,r)` and the parameter-preserving A1 resolution/translation maps in EU.0, plus the explicitly written reference-zero Cauchy operator EU.11e and the selected-fan/compactness construction EU.5. The K96 M2 line maps themselves are EX.1–2, EX.14 and EX.16–19. | These shared source and analytic-operator inputs are exact. No identification of K94's M6 line or quadratic cap with K111's M2 line or cubic cap is made. |

Here is the explicit path and its range. Put

\[
r_{\rm src}\in[0,1/4-s_*],\quad \rho=-\sqrt{1-3r_{\rm src}},\quad
t_c=\frac{(\rho-1)^2(2\rho+1)}{27},\quad
t_o=\frac{(\rho+1)^2(1-2\rho)}{27}.
\]

For `0<s_*<1/12`, rho runs from −1 to a value strictly below −1/2. The selected tc stays negative, the other branch is positive after the initial endpoint, and their difference is `4rho³/27`, which never vanishes. The only source collision on this closed path is the initial unselected III value handled by K96. The selected height stays `q=t−t_c` throughout. The fresh program verifies the full discriminant, these factorizations, the SI2 marked-cover formula `t_c=v/(v−2)³`, and its positive meridian derivative.

The actual doubled section is `(s,−t−s/2)`, with `s=1/4−r_src>0`. At the cubic root the full factor is

\[
f_{2,\rm old}=z^{-1}\frac{Y-1-zX/2}{X-sz^2}.
\]

All six factors have weight z^(−6), while the selected-height factor is `z^6(1−t_c z³)`; their product is precisely EX.4 with the scalar unchanged. These identities are also freshly checked.

The fixed scalar fits the complete path. Choose a small fixed delta inside the selected-collision chart range. On the compact initial portion `r_src∈[0,1/4−delta]`, K96 at the initial endpoint and the regular source/cap charts elsewhere supply a uniform scalar bound epsilon. Choose s_* sufficiently small that `|lambda0| s_*^12<epsilon`, as allowed by the target. On the remaining portion set `sigma=1/4−r_src>=s_*`; then

\[
|\lambda_{\rm base}|/\sigma^{12}
=|\lambda_0|(s_*/\sigma)^{12}\le|\lambda_0|.
\]

The ASI2.8–11 determinant/contraction bounds become at least as strong as those already proved for the coupled scalar `lambda0*sigma^12`, since decreasing the scalar increases D_B. The chosen cubic root is the constant `r0*s_*^4` along this path. The original finite character and annular integer cochain remain unchanged.

Use the actual local parameter lifts in these source/cap charts, a relative partition matching the prescribed derivative on protected collars, and circle/finite-deck averaging. Their source flow gives the fibre map; the actual Cartier transition functions give the line transport by the IL.29 rule `a_i=−sum chi_k X(g_ik)/g_ik`, `dot w_i=−a_i w_i`. The backward source flow followed by the inverse linear ODE is its inverse. This specifies the source, physical line, root and cap map through the whole path. The transported primitive Hopf and F35 source-boundary maps preserve the original orientation and the chosen fan. A guarded expansion of the current ASI2.7 paragraph is supplied in `K111_inherited_scope_patch_05.json`.

## Remaining responsibility

The C/F boundary comparison and the inherited statement-to-target morphisms are closed at the scopes above. This branch does not claim to have newly reconstructed the full F41/F46 lattice certificates, the unused portions of K94, or the full compact-owner implementation. Their retained evidence and the separate current owner checks remain credited at their actual scopes. The parent and sign agent own the whole-row conclusion, integration of the new auxiliary proof, source-reference disposition and final layout. This report gives no new PDF-layout or canonical completion claim.
