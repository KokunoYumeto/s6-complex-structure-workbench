# Paper IV, night:P3K.119: complete scoped audit

**Conclusion: mathematically proved at the stated fixed-family scope; high confidence.** The original prescribed-reference gate is closed. All twenty-four ordinary-cap collision meridians on the ordered OS45 cover, and their reciprocals, have zero return class for the original order-one positive-norm cap, its full source/physical period reference, every prescribed integral lattice-basis selected fan, and the original admitted fixed scalar. The family is the fixed nonzero Hom normalization \(C_*\) continuation of K116. The proposed statement insertion makes that identification literal.

Attribution: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. The supplied same-family supporting proofs are not described as a different-family review.

## 1. Chronology and executable evidence

The K116/K117/K119 statements were read before their arguments. PREREADING.md, prereading_freeze.json, and code/prereading_exact.py preserve that first route: original source equation, marked selected-node map, collision polynomial and disjointness, nodal coefficient, and parameter winding. Its 50 named checks include K119 source algebra but do not prove the global cap comparison. The bounded fan tests in that same program concern K117.

I subsequently read all four K119 supporting proofs in cp15: OC45.1–11, OCP.1–6, OCGC.1–4, and ORC.1–10, original lines 116303–118697. The used invariant-stalk argument at K78/OCS.1 was also read. K10's literal source and topology and the F35/O45P.6 prescribed-fan input had already been read for K116; see K116_REVIEW.md and its 249-check program. The explicit common-blowup/ruling morphisms transport that input to the prescribed fan.

After reading all four K119 arguments I wrote code/k119_afterreading_exact.py without importing a historical or earlier audit checker. The run passed **175 named exact checks**. It reconstructs all four actual selected-zero choices and all twenty original inverse-transpose matrices; the complete 20-by-20 raw/based maps and their integral inverses; 20-by-36 mapping-cone boundaries; primitive image coordinates; and the full degree-one contraction. Output: output/k119_afterreading_exact.json; SHA256 ed38ca56e8acb546c2742ef698b0ef201a53f2cfb7df6992d640f4e2b4e2e4c2. Stdout records Python 3.12.14, SymPy 1.14.0 and 31.20 seconds.

The first run stopped on structural equality between an expanded polynomial and a factored expression. The saved attempt is output/attempts/k119_01_structural_polynomial_comparison.stdout.txt; the rerun tests their exact rational difference. No mathematical formula changed. These are fresh post-reading computations, not a blind proof or a replay of absent historical programs.

The symbolic checks do not establish analytic convergence, Cartier-module extension, properness or isotopy by finite testing. Those points are checked by the actual maps below.

## 2. Exact family, collision count, and coordinate inverses

The original family retains
\[
R=t^2+a,\quad f=R^2+t,\quad g=R^3+\tfrac32tR+\tfrac38,
\qquad y^2=x^3-3fx+2g,
\]
with \(G=(R,\sqrt3/2)\), \(\mathcal M=\mathcal O([8G]-[O])\), translation by \(-G\), and
\[
B_\lambda(p,v_M)=(p-G,\lambda C_*(t-t_c)B_{8,1}(p)v_M),
\quad B_{8,1}=f_2^8(f_8\circ t_{-G})/f_8.
\]
The chronological tangent normalization and \(C_*\) are fixed by the initial source and Cartier frames. An independently varying coefficient \(c(a)\) instead induces the exact scalar path \(\lambda_{\rm eff}=\lambda c(a)/C_*\); its extension is not inferred from an initial value. ORC.12 already retains this fixed \(C_*\), and the proposed statement clarifies it.

For the original marked cover \(a=-u/3-u^4/9\), \(t_c=(2u)^{-1}-u^2/3\), \(v^2=4u^3+3\), the exact pullback is
\[
729(16a(u)^3+3)=2187-16u^3(u^3+3)^3
=-(2u^3-3)(8u^9+84u^6+342u^3+729).
\]
The degree-twelve polynomial is square-free. Saved Bezout witnesses prove its disjointness from \(u\), \(u^3+3\), \(4u^3+3\), and \(16u^6+120u^3+243\). Each root therefore has two ordered \(v\)-values. The first factor gives six points with \(t_c=0\); the degree-nine factor gives eighteen with \(t_c\ne0\). There is no lost branch multiplicity.

The actual discriminant factor is \(D=64(g^2-f^3)=48a(t^2+a)^2+8t^3+72at+9\). At \(a_*^3=-3/16\), \(D_t=72a_*\), \(D_a=144a_*^2\), so \(ds/da=-2a_*\ne0\). Also \(da/du=-(4u^3+3)/9\ne0\). These original local maps have implicit inverses, and a positive ordered meridian is exactly one positive \(s\)-turn. The other finite critical values stay simple since \(\operatorname{disc}_tD=331776(256a^3-3)^3\).

The cubic at the cap node is \(y^2=(x+a_*)^2(x-2a_*)\). Put \(q=t-s\), choose the actual branch \(\xi(q,s)=\sqrt{f(s+q,a(s))}\) with \(\xi(0,0)=-a_*\), and retain \(h=2(g-\xi^3)/q\). The numerator vanishes on the entire moving nodal locus. Since \(\xi_t=-1/(2a_*)\) and \(g_t=3a_*/2\), \(h(0,0)=6a_*\ne0\). The maps
\[
X=y-(x-\xi)\sqrt{x+2\xi},\quad
Y=h^{-1}(y+(x-\xi)\sqrt{x+2\xi}),\quad XY=q
\]
have inverse \(q=XY,t=s+XY,y=(X+hY)/2\), with \(x\) solved by \(2(x-\xi)\sqrt{x+2\xi}=hY-X\). Its derivative is \(2\sqrt{3\xi}\ne0\). Thus \((X,Y,s)\) are smooth total-space coordinates. The \(q\)-dependent square root is retained.

## 3. Original chronological Miller map and full point module

The normalization is \(x=S^2+2a_*, y=S(S^2+3a_*)\), \(c^2=-3a_*\), \(S_G=\sqrt3/(4a_*)\), \(S_G^2=-a_*\). Under \(Z=(S-c)/(S+c)\), \(P_*=-2\pm\sqrt3\). These reciprocal real values have absolute value unequal to one, so no relevant power is the identity.

The fresh program first derives the tangent quotient. For a general node, \(S_{2j}=(S_j^2+c^2)/(2S_j)\), and the tangent quotient equals \((S-S_j)^2/(S-S_{2j})\). Three chronological doublings give \(f_m=(S-S_G)^m/(S-S_m)\), where \(S_m=c(1+P^m)/(1-P^m)\), for \(m=2,4,8\). Substitution by the exact inverse \(S=c(1+Z)/(1-Z)\) gives OC45.14 including the constant and equal values at the two node branches.

For translation by \(-G\),
\[
T(S)=(S_GS-c^2)/(S_G-S),\quad Z(T)=Z/P,\quad
f_2(S)(T(S)-S_G)/(S-S_G)=-2S_G.
\]
The last identity derives the full chronological coefficient, before the actual point-function cancellation:
\[
B_{8,1}(Z)\frac{f_{P^8}(Z/P)}{f_{P^8}(Z)}
=(-2S_G)^8=9/a_*^2,\qquad f_b(Z)=(1-Z/b)/(1-Z).
\]
The four factors are the original source and target Cartier generators. Their quotient is a module isomorphism through the point and zero-section graphs; the inverse evaluates the reciprocal at the inverse source point.

The inverse-j expansion in the original \(q=t-s\) gives \(\kappa(0,0)=1/(288a_*^2)\), equal to \(-h/(1728\xi^3)\). The full functions are \(Q=q\kappa(q,s)\), \(P(q,s)\), and \(\beta(q,s)\), with \(\beta(0,0)=C_*9/a_*^2\). All higher coefficients remain in the actual period arrows.

## 4. Extending exponential and Lie sheaf

The full map is \(\mathcal T_{A,D}(Z,V)=(e^AZ,e^DV)\), with inverse \(\mathcal T_{-A,-D}\), and its point-module coefficient is \(e^D f_{P^8}(Z;Q)/f_{P^8}(e^AZ;Q)\). Composition cancels the actual intermediate function. On a Tate chain the source factors are reciprocal, preserving \(X_iY_i=Q\) and the original height. On any chosen cone a character \(Z^rV^d q^e\) receives the analytic unit \(e^{rA+dD}\). Its inverse and every character relation persist on the same prescribed fan.

At infinity the complete identity is \(f_{Q^3b_0}=(-Z/b_0)^3Q^{-6}f_{b_0}\). In \(V_0=f_{b_0}v_M\), the action is \(e^{D-3A}\). The full base factors cancel because the base is fixed. The integer period matrix and its inverse are
\[
W=\begin{pmatrix}-1&3\\-3&8\end{pmatrix},\qquad
W^{-1}=\begin{pmatrix}8&-3\\3&-1\end{pmatrix};
\quad (8,-3)W=(1,0).
\]
They give \(H=h^{-1}B^{-3},K=h^3B^8\) and \(h=H^8K^3,B=H^{-3}K^{-1}\). A source component order \(n\) is removed by the actual word \(H^{-n}\), with all units. At a selected filling the two valuations are the exact basis \((1,0),(0,1)\); at an unselected node the source period removes its single order. The remaining analytic units have logarithms. This supplies local exponential surjectivity and kernel \(j_*\Lambda\), the periods of zero radial order.

The local disc/annulus mapping cone retains \(\ker(H_i-I)\) and cancels the same annular coinvariant term by its identity map with the opposite boundary. It is an integral cancellation. The relative differential equality \(dx/(2y)=z\,dX/(2Y)\) gives the source Lie line \(\mathcal O(-1)\); the physical vector is global. Thus the full transition is
\[
\mathcal L(t,s)=\begin{pmatrix}t^{-1}&0\\a(t,s)&1\end{pmatrix},
\]
where \(a(t,s)\) remains the derivative of the entire original point-module transition.

## 5. Complete integral comparison and signs

The new code independently inverts the five original K10 matrices for each selected site. It obtains \(H_i=T_i^{-t}\), \(N_i=H_i-I\), \(P_i=H_0\cdots H_{i-1}\), and \(M_i=P_iN_i=P_{i+1}-P_i\). It verifies the primitive image bases over the integers. They are \(e_w+3e_\delta,e_w,e_u+3e_w+16e_\delta,e_u+8e_\delta,e_u-3e_w\), with the additional \(e_\delta\) at the selected site.

For the entire difference \(v=Ae_u+Be_w+Ce_\delta\), use \(r_1=-Be_u,r_3=Ae_w,r_\sigma\mathrel{+}=(C-8A)d_\sigma\), adding terms at repeated indices. The transported preimage is \(t_j=r_j-\sum_{i>j}N_ir_i\), with integral inverse \(r_j=t_j+\sum_{i>j}N_ir_i\) in descending order. Both complete 20-by-20 matrices are saved, their product is the identity, and the transported boundary composed with that map equals the raw boundary.

The actual cone is \(b_i=p_i-N_iz_i\) for \(i<4\), \(b_4=-H_4\sum_{i<4}P_ip_i-N_4z_4\). The full coordinate \(v_*=\sum P_ib_i\) cancels all exterior terms and equals \(-\sum M_iz_i\). Consequently the positive difference uses **\(z_i=-t_i\)**. The whole 20-by-36 cone, including this sign, is checked.

The derived primitive matrices are precisely OCP.17/ORC.28 at all four sites. With the printed \(L,J\), \(LD'=I_3\), \(B'J=I_3\), \(D'L+JB'=I_6\), \(B'D'=0\) hold integrally. Therefore
\[
H^0(\mathscr H)=\mathbb Z\delta,\quad H^1(\mathscr H)=0,\quad
H^2(\mathscr H)\xrightarrow{\psi}\mathbb Z
\]
with section \(1\mapsto[e_\psi]\), including all torsion information. The two norm-one caps have the same degree-two class, and every retained source, physical and suspension component is inserted by the explicit total cochain before exponentiation.

## 6. Full analytic comparison and actual endpoint

After that integral correction the Lie cocycle is single valued. The Laurent solve retains
\[
u_0=-\sum_{j\ge0}f_jt^j,\quad u_\infty=\sum_{j<0}f_jt^{j+1},
\quad G=g-a(t,s)u_\infty,
\]
then \(v_0=-\sum_{j\ge0}G_jt^j\), \(v_\infty=\sum_{j<0}G_jt^j\). Direct substitution gives \(\mathcal L(u_\infty,v_\infty)^t-(u_0,v_0)^t=(f,g)^t\), retaining the full off-diagonal term and the allowed constant \(j=-1\) in \(u_\infty\). Fixed protected contours give convergence and holomorphic parameter dependence on smaller annuli. On the many-disc cover the partition cochain, affine Cauchy primitives and this Laurent solve give the actual holomorphic cochains. Hence \(H^1(\mathscr E)=0\) with the full transition.

The actual maps are \(F_i=\operatorname{Exp}(-s_i)\), inverse \(\operatorname{Exp}(s_i)\), and \(F_i g^X_{ij}=g^Y_{ij}F_j\). The preceding complete charts extend them on every filling. Both original cap logarithms, \(\log t\) and \(\log(t-d)\), remain.

At the original cap \(q=-s\),
\[
\gamma_{\rm ref}=(-\log P,\log C)/(2\pi i)
+k(\log Q,8\log P)/(2\pi i)+r\alpha+d_\delta\delta.
\]
The positive turn gives \(k\alpha\) at eighteen points and **\(k\alpha+\delta\)** at six points, because there \(C(0,s)=-\lambda s\beta(-s,s)\). The complete transported jumps enter the same preimage calculation. This closes the original-reference gate beyond the particular eighteen-point enlargement.

A global source Lie section vanishes by \(u_0=t^{-1}u_\infty\) and regular Laurent powers. The remaining section is a constant physical vector. The proved integral \(H^1(\mathscr H)=0\) gives the exact comparison group
\[
\mathbb C\delta/\mathbb Z\delta\longrightarrow\mathbb C^*,
\quad [z\delta]\longmapsto(v_M\mapsto e^{2\pi iz}v_M),
\]
with local inverse \((2\pi i)^{-1}\log\). Comparison ratios are therefore literal physical scalars.

The parameter-annulus construction retains the scalar holonomy, flattens it by its explicit exponential, solves the radial connection equation with the negative sign dictated by its transition, then removes its common antiholomorphic derivative by the Cauchy kernel. On a cut the typed endpoint equation is
\[
C=F_1E_XF_0^{-1}E_Y^{-1},\quad
F_0E_X^{-1}F_1^{-1}=E_Y^{-1}C^{-1}.
\]
Here \(C\) acts on \(Y_1\). For \(P_Y:Y_0\to Y_1\),
\[
F_0(E_X^{-1}F_1^{-1}P_YF_0)F_0^{-1}=E_Y^{-1}C^{-1}P_Y.
\]
The fresh free-group check verifies this order without commuting endpoint or transport maps. The physical scalar has the actual global isotopy \(e^{\theta\log C}\) and reciprocal on every cap and cone.

## 7. Proper protected-cap family and return

Choose a fixed protected \(d\ne0\) and cap disc of radius below \(|d|/4\), then shrink the parameter disc to avoid all moving critical values. The full nonzero \(Q,P,C\) there have joint analytic logarithms. Their exact flow is \(\mathcal F_w=(e^{-w\log P}Z,e^{w\log C}V)\), and the plus-log map is \(\Psi_d=\mathcal F_{\log(t-d)/(2\pi i)}\), with its reciprocal. A branch change gives the full \(B\)-period, so the norm is positive one.

At the old cap, the family uses the actual \(XY=t-s\) node or the chosen selected fan with the same \(q=t-s\); these charts and \(s\) are submersions. At infinity \(b_0(0,0)=16/27\), so the original point/O modules and full period words extend. The other nodes remain distinct and simple. Uniformly contracting fundamental annuli, primitive infinity representatives, selected cones modulo the two full periods, the protected cap, and the remaining closed source pieces form a finite compact Hausdorff preimage of a closed parameter disc under the displayed reciprocal collars. The local submersions agree. This is the required smooth proper family.

The full K116 source/line/cap maps and F35/O45P.6 common-blowup/ruling/Gysin/van Kampen maps carry the K10 reference sphere to the prescribed fan and cap comparison. A horizontal lift from these charts has complete flow by compactness. Radial contraction of the parameter loop supplies an isotopy of the new return to the identity; the exact endpoint square transfers it to the original return, with its isotopically trivial physical scalar.

For an admitted fixed scalar outside the common small disc, \(\lambda_\tau=((1-\tau)+\tau\varepsilon)\lambda_0\) stays contracting since the entire multiplier is linear in \(\lambda\), and its argument is unchanged. The same full arrows give the proper cylinder and inverse transport with the original endpoints. Thus the result holds for the original admitted scalar.

It follows that \([\Phi]=0\in\Theta_7\) for precisely the twenty-four stated meridians and their reciprocals with the full prescribed data. The review assigns no result to other source-boundary generators or to a shorter loop with a different endpoint.

## 8. Credit, presentation, and residual limits

The reference-sphere and fan transport remain attributed to their exact identified inputs. The implicit inverse, Cartier maps, primitive period removal, integral contraction, full Laurent/Cauchy solve and proper-family transport are displayed in the receiving proof. No exhaustive novelty or priority claim is made, and no absent historical script is reported as executed.

The proposed edits clarify fixed \(C_*\), replace the opening preparation-history prose by a current proof roadmap, and replace the stale assertion that this complete proof still awaits global audit. Historical notices and attempts remain in records. The row can be marked proved/high-confidence at its full stated scope.

No remaining mathematical gate was identified. Residual limits are the explicit established reference-sphere/fan dependency, same-family review provenance, and bounded source-credit claim. Layout and global packaging remain with the root reviewer and are not marked complete here.
