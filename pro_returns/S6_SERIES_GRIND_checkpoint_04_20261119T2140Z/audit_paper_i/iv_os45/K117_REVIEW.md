# Paper IV, `night:P3K.117`: ordered selected-cusp continuation

**Assessment: the mathematical receiving gate is closed for the stated positive ordered loop, fixed physical scalar, original order-one cap, fixed initial coefficient (C_*), and full prescribed reference. Confidence: high.** No conclusion for a shorter original-(a) meridian is supplied by this row. The fourfold degree of the ordered loop is retained throughout.

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. This is a full targeted check after the statement-first derivations locked in `prereading_freeze.json`. The complete geometric argument was read before the new program `code/k117_afterreading_exact.py` was written. The new execution is not described as a prereading independent proof or as a different-family review.

## Input and exact review coverage

All five supporting proofs of K117 were read in full: original cp15 Paper IV lines 109960–113348, comprising SC45.1–4, C45.1–8, SCP45.1–4, CR45.1–7, and CP45.1–9. These repeated arguments have different historical producing-run scopes; their old named code was not available or newly executed here. The current result is supported by the displayed maps, the present review, and new code saved with this audit.

Used dependencies checked at their actual scope:

* The complete K116 source/topology continuation and its literal (a=b=1) K10 input were checked separately in `K116_REVIEW.md`. The actual source equation, source translation, point line, cap, and period matrices are transported. No catalogue nickname supplies an identification.
* F7's complete orbit-pair proof and F8's subsequent cut-and-reglue Hopf-lift proof were read. The K117 prose repeatedly names F8 for the fixed-pair classification; the correct direct locator is F7. Exact replacements are in `K117_patches.json`.
* F9's whole relative conifold-orbit argument was read, including the positive proper one-dimensional coordinate, its inverse flow, relative stable framing, and the retained meridian class of the principal-circle line.
* F55's entire local lifted-link proof was read, including the actual zero-total-link framing, the Stiefel/Whitehead map, and the nonzero Kummer test comparing the Gauniyal–Turchin and corrected Takase conventions.
* The specific F56 weighted-pencil and braid input was read at SC.1–2 (original lines 16360–16495): the actual boundary lift, the six base-ideal blowups, both quotient charts, and the full exceptional pencil.
* K68's complete PL.1–7 argument was read (27927–28412): the physical and meridian-one lines, anti-linear map over both caps, circle-first orientations, piece exchange, and inverse clutch. No rejected older physical sign is used.
* GF.9–17 (23935–24155), OP.5 (22535–22625), and OR.1–3 (84910–85075) were read for the exact normal cylinder, full unit maps, axis degrees, half-angle endpoints, and the actual inverse boundary extension. The common-blowup and identical-fan inputs were already checked with K116; the full K117 C45.8/CP45.8 specialization was then checked independently of any numerical fan table.

The mathematical result is not made dependent on the claim that every page of each cited classical paper was re-proved here. The exact classical results used have been reopened below.

## 1. Original source, ordered parameter and full point line

The source remains

\[
R=t^2+a,quad f=R^2+t,quad g=R^3+	frac32tR+	frac38,quad
y^2=x^3-3fx+2g,quad G=(R,sqrt3/2).
\]

For the selected root, (a=-u/3-u^4/9), (t_c=1/(2u)-u^2/3), (v^2=4u^3+3), (c=v/(2u)), and (3\xi=c^2). The inverse local parameter is the branch of (u^3-u^2c^2+3/4=0), followed by (v=2uc); its (u)-derivative at (u_0^3=-3/4) is nonzero. The exact factorization of (a-a_0) gives nonzero leading term (-v^4/(216u_0^2)). Hence a positive ordered loop makes four positive original-parameter turns.

The actual shift (x=X+\xi), (t=q+t_c) gives

\[
y^2=X^2(X+c^2)+qH(q,X,c),qquad H(0,0,c)=-2u^4.
\]

The complete (H), including every original-height coefficient, is verified by direct substitution in the new code. Its central value is (3u_0/2\ne0), so the inverse source chart is the implicit solution for (q). This is also the total-source submersion through the cusp; the Tate collar is allowed to shrink.

The other critical point has (X=c^2R_1(c)), (q=c^6J_1(c)), with limiting values (-2/3,-4/(27H_0)). The exact central Jacobian is \(\begin{pmatrix}0&H_0\\-2&0\end{pmatrix}\). Thus the critical-value difference winds six times and the ordered two-point braid is (\sigma^{12}). The right Hurwitz convention sends six full twists to conjugation by ((g_1g_2)^{-6}). The actual boundary double cover has angle (\vartheta=2\widetilde\vartheta), so ((g_1g_2)^6=T_\partial); the weighted chart supplies its inverse-direction collar map. The full extending logarithm of (H/H_0) is carried by boundary velocity and contributes no additional turn.

On the normalization, (X=S^2-c^2), (y=S(S^2-c^2)), (S_G=-\sqrt3/(2u)), and (Z=(S-c)/(S+c)). Translation by (-G) is

\[
T(S)=\frac{S_GS-c^2}{S_G-S},qquad
T^{-1}(S')=\frac{S_GS'+c^2}{S_G+S'},qquad Z(TS)=P^{-1}Z(S).
\]

Chronological tangent quotients, not merely an assigned divisor, give (f_m=(S-S_G)^m/(S-S_m)) for (m=2,4,8). The new code derives each quotient from the actual tangent slope and verifies the exact cancellation

\[
f_2(S)\frac{T(S)-S_G}{S-S_G}=-2S_G.
\]

It follows that the original (B_{8,1}) sends (W=(S-S_8)v_M) to ((-2S_G)^8W=(81/u^8)W). Here (S-S_8) cancels the genuine point and (O) Cartier modules at their zero and pole. The point/tensor comparison is retained as

\[
V_{\rm pt}=W/(c-S_8),qquad
V_{\rm tensor}=W/(c-S_G)^8,qquad
V_{\rm tensor}=\frac{c-S_8}{(c-S_G)^8}V_{\rm pt}.
\]

Both denominators are nonzero analytic base units at the central parameter. The original-height multiplier is (\kappa(0,v)=2u^{10}/v^6), with winding (-6), and (\beta(0,v)=81C_*/u^8) has winding zero. The family is the fixed-(C_*) continuation of K116. An independently prescribed varying lift has the previously recorded exact scalar transport; it is not silently covered by fixing a single initial value.

The full theta inversion gives ((Z,V_{\rm pt})\mapsto(Z^{-1},P^8V_{\rm pt})). Composing with the actual target source period gives ((Q/Z,V_{\rm pt})). The point/tensor ratio is even in the ordered parameter. Both (P) representatives are units, which rules out an unrecorded (Q^h) factor for (h\ne0) by valuation. The exterior and cap were constructed over (v^2); the full ordered loop therefore closes by their literal original identity.

## 2. Actual trace, normal data and both cap evaluations

The fixed curve of a vertical fan has native charts (q=ZAB=Z'A'B'), (Z'=Z^{-1}), (A'=ZA), (B'=ZB), and physical weights ((-1,+1)). Strict contraction excludes an additional unit-circle stabilizer arising from a nonzero suspension deck.

The sphere antecedent comes from K116 before taking the quotient. Conjugating the negative normal summand gives (\mathcal O(1)\oplus\mathcal O(-1)), whose SU(2) clutch has the stated disc. A smooth radial parametrization can be taken as ((\sin(\pi r/2)e^{i\phi},\cos(\pi r/2))), as in F7. Thus the Hopf boundary is the indicated product. Alexander duality, the primitive linked (S^3), Gysin, Mayer–Vietoris and van Kampen give a simply connected homology five-sphere. Kervaire–Milnor and Haefliger identify the orbit pair with ((S^5,S^2)), with exactly this attachment and line. The later surgery uses the other (D^3\times S^2) filling.

The extending logarithm of the actual source translation and line lift supplies the F9 isotopy. Its derivative (db'/db>0), its inverse, the strict norm closing, and the short real circle arc fix the branch order. The fractional Möbius shear fixes both (S=\pm c); its derivative tends uniformly to the identity. Hence it can be removed through the actual orientation-preserving source germ isotopy.

The projected trace is literally

\[
f(S,c)=(S^2-c^2,S(S^2-c^2),c).
\]

Its derivative-minor ideal is ((S,c^2)), and its only distinct double pair is (S=c,-c). The height (\operatorname{Re}(S\bar c)/\sqrt{|S|^2+|c|^2}) separates those two points with the prescribed sign. Positive radial monotonicity of (\|f\|^2) provides the actual inner four-ball. The oriented stereographic boundary is exactly F55's lifted link, not just a link with the same unframed source equation. Its verified data are Smale integer (-2) and Haefliger integer (+1).

The full original source form is (-2(H+qH_q)^{-1}dX\wedge dy\wedge dc). The conormal and its two original-height products use the same unit:

\[
n_f=(3S^2-c^2)dX-2Sdy+2c(S^2-c^2)dc,quad
dq=-\frac{x_-x_+}{H}n_f,quad
d(AB)=-\frac{x_+^2}{H}n_f,quad
d(A'B')=-\frac{x_-^2}{H}n_f.
\]

The residue arrow (\mathcal O(-D_+-D_-)\to K_N) sends (x_-x_+\) to (dS\wedge dc) and extends at infinity. The determinant-one spinor has frames ((1/x_-,x_+)), determinant trivialization (Z=x_-/x_+), and the full anti-linear Cox arrow

\[
(a,b)\longmapsto\frac1{\sqrt{|x_-|^2+|x_+|^2}}
\begin{pmatrix}x_+&-\bar x_-\\x_-&\bar x_+\end{pmatrix}\overline{(a,b)}.
\]

The common (-1/H) has an extending logarithm/square root. A residual weight-preserving phase fixes the adjoint point; its full (S^1)-parameter winding extends over the outer (D^3\times S^1) because the boundary restriction on (H^1) is an isomorphism. This supplies actual line isomorphisms, not just equal Chern classes.

The outer cap uses (\mathcal B_c(P)=A_cPA_c^*/\operatorname{tr}(A_cPA_c^*)), (A_c=\begin{pmatrix}1&-c\\1&c\end{pmatrix}), with inverse formed from (A_c^{-1}), and holds the normal Cox quaternion fixed. The full differential has (x_+^2dZ=2c,dS-2S,dc). In particular the determinant winding one is retained. It is not replaced by the separate Tate winding (-6).

The closed trace base is (S^4=\partial(D^3\times D^2)). The first-column map ((S,c)\mapsto(x_+,x_-)) has complex determinant (-2) and real determinant (4), so its boundary degree is one. In the stated first-column orientation the SU(2) cubic has integral (24\pi^2). The cap boundary sign therefore gives (c_2=-1), (p_1(\operatorname{ad}E)=4). The meridian-one line on its sphere bundle has individual pair ((1,4)).

For the inner framed link, the two exact Seifert relations give (3\sigma+e^2=-4), (e^2-\sigma=8), hence (\sigma=-3,e^2=5). Its constant negative-normal cap is dual to the actual meridian-one line and contributes ((5,-4)). The quotient bordism boundary is (-P_f\sqcup-N_e\sqcup-B), so the positive-family (U)-pair is ((-6,0)). Jin's reversed parameter gives (U=(6,0)); the globally extending Hermitian duality gives the physical pair (M=(-6,0)).

The last sphere sign comes from the displayed pieces: (X=-\partial(D_y^3\times D_q^4)), with (u_M=q) and reversed (y)-ball orientation. Reordering first-to-second gluing replaces (F) by (F^{-1}). Thus (\lambda_M(F)=-\Sigma_{F^{-1}}), whereas (\lambda_U(F)=\Sigma_{F^{-1}}). For the disc-supported relative class the inverse clutch is the orientation inverse, so the physical class is (A_M=-1\pmod{28}). The native pair in this held product is ((\mu,\nu)=(0,-6)).

## 3. Every vertical fan and the unrestricted terminating algorithm

The exact character/period substitution is

\[
V_j=Z^{-j}V,quad H_j=hB^j,quad
Q_j=\kappa qg^j,quad
\alpha_j=\alpha\eta^j\kappa^{-j}g^{-j^2},quad
\eta_j=\eta g^{-j}.
\]

Its inverse, source-flow fields, Cartier multiplication by (Z^j), cap extension, and full logarithmic real coefficient frame are explicitly present. The primitive deck square gives (U_j\cong U_0\otimes\mathcal T^{6j}). CP45.5 additionally computes the integral (H_2) basis and all its pairings, and checks the potentially nonextending (q)-angle by a literal section disc whose coefficient extends across (q=0). The Čech integral cochain, partition-of-unity logarithms and extending boundary gauge then construct the required full relative line arrow with inverse.

The actual source coframe shear is unipotent triangular. Its source curvature-square trace vanishes; the remaining base block involves two angles and one collar variable. This gives zero relative Pontryagin transgression. The source-circle homotopy to a map constant near surgery supplies a relative level cobordism fixed on the outside; it transports the zero pairing from the actual source three-level times circle. Consequently (\ell_{M,j}=0).

The new code multiplies the complete exterior forms in the declared outward order and obtains

\[
3\int_0^1\beta_j\wedge(F_{{\rm ext},j}+s,d\beta_j)^2ds
=18j^2d\alpha_q\wedge du\wedge db\wedge d\gamma\wedge d\theta.
\]

The outward collar runs from (s=1) to (0). The interior cube difference is affine in (j), since (\Xi^2=0). The full height-one theta reflection, with both product caps retained, sends (T_0) to (T_1), fixing the remaining affine coefficient. Thus

\[
(k_M,\ell_M)_j=(-6-18j(j-1),0),qquad A_{M,j}=-1-3j(j-1).
\]

The ordinary product is compared through its full inverse height map (h_s^{-1}), with every coefficient evaluated at the recovered original (q). Compactness gives a common inverse disc. The explicit quaternion cylinder, its full zero-winding unit factors and higher normal jets carry the native product to the ordinary one by (L^6). OP.5 and OR.2 fix this connecting sign: the closed Hopf-oriented left degree is (-6); extension of the inverse gauge has endpoint degree (+6). This gives the printed complete vertical ordinary seed.

The identical-fan maps are the identity on absolute semigroups, with periods reindexed by the displayed integer matrix. Each (Q_0,Q_1) step has actual dense-character/Cox maps, common blowup, two ruling projections, target full coefficients (A'_{ik}=\prod A_{hl}^{(Q^{-1})_{ih}Q_{lk}}), and unchanged source/point/cap overlap. The weight parity closes both Spin factors. The native common-link map and carried complex reset give (V'_{22}=a), (\delta'_2=2a-b), (s'=s+(b-a)/2).

A homogeneous symmetric prism difference annihilates its two-plane, hence is the displayed rank-one outer product; the retained edge value kills it. The derivative difference has the corresponding one-dimensional kernel. This proves the full rationally written target solution is unique. Existence and integrality come from the actual target family and integer invariants, before reduction modulo 28. Euclidean subtraction strictly reduces (p+r), terminating at a vertical seed. This supplies the unbounded all-fan proof; no finite test is substituted for it.

## 4. Fresh execution, source evidence and remaining limits

`code/k117_afterreading_exact.py` passes **288 named checks**, including **217 fresh nine-variable Gaussian solves** and **868 forward/inverse full-atom exponent comparisons**, using Python 3.12.14 and SymPy 1.14.0. Its complete output, every path and full matrix are in `output/k117_afterreading_exact.json`; stdout is retained. The earlier statement-only execution has 50 named source checks plus 1001 fan cases/7343 steps and remains a separate chronology. One structural equality failure was repaired by checking the exact zero difference; one unfactored symbolic expansion was stopped and replaced by the previously verified exact Miller cancellation. Both attempts are retained under `output/attempts`.

Six primary PDFs were freshly downloaded from their publisher/arXiv/academic source, with exact hashes in `primary_sources/acquisition.json`. The bounded openings are:

| Primary source | Reopened precise scope | Use |
| --- | --- | --- |
| Gauniyal–Turchin, published 2026 | pp.1469–1471 orientation rules; pp.1492–1493, equations (4.1)–(4.3), Theorem4.1 and spherical qualification | The exact double-link push, Whitehead coefficient and local link formula |
| Némethi–Pintér, CMH90 (2015) | Theorem1.2.2 p.515; §2.4 pp.519–521; Propositions4.2.2–4.2.3 p.523 and the latter proof; Proposition6.1.1 and full proof pp.526–528; Theorem9.1.6 p.534 | Crosscap count, realification sign and boundary convention; exact normal-extension map |
| Takase, arXiv math/0506356v1 | Corrected Theorem2.3 and Corollary2.6 p.3; Proposition4.1 conclusion/proof and Remark4.2 pp.7–8 | Corrected Seifert sign and explicit nonzero Kummer comparison |
| Sakai, arXiv1405.1947v2 | Proposition6.8 and complete proof p.19 | Independent embedded-projection normalization (\mathcal H=-\Omega/12=-\sigma/8) |
| Haefliger, Ann.Math.83 (1966) | Theorem1.2 and proof pp.404–405, Corollary6.6 p.422; Theorem5.17 p.421 reopened online | Exact (n=2,q=3) unknotting/isotopy input and Kummer comparison |
| Kervaire–Milnor, Ann.Math.77 (1963) | p.504 table visually opened; p.505 Smale comparison reopened in source text | (\Theta_5=0) and identification with diffeomorphism classes |

The Haefliger file SHA256 is exactly the previously recorded `63748267f5a47062ccf29cdb2ea8aecd5249e8e144568d59e1d4a18a5dfdae93`. The source row does not credit these known classical conclusions to the continuation. The family-specific calculation uses their stated hypotheses through the concrete maps above. The present source search establishes those citations and their exact normalization; it is not an exhaustive claim of priority for the entire OS45 family.

There is no remaining mathematical continuation gate for this exact K117 scope. Trust in the cited classical theorems, ordinary smooth extension/relative flow arguments, and the exact arithmetic runtime remains explicit. The record is not formal proof-assistant verification. Layout and global bibliography/intake formatting are owned by root and are not marked complete by this file. Suggested text repairs are limited to the correct F7 locator, explicit fixed-(C_*) scope, a smooth representative of the displayed SU(2) contraction, and removal of the obsolete in-proof awaiting-review sentence while retaining its history in the audit records.
