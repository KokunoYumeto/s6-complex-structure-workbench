# Fresh recovery comparisons: AZ, B4, FJ, BB

Checker: ii_check_a_recovery_blind. Written on 2026-11-21 after the actual derivation freezes and proof releases. These are new recovery checks, not recreated historical B04/B05 receipts. No B reconstruction or prior proposed block was opened.

## Order, source scope, and actual readings

The original Paper II source is bound by SHA256 74497bfe327fae25c9cdcb17334b3bf42a9793a9df7c0a4404d97568f2f760f0. Each original statement packet, cited-input supplement, additional safe input and new computation is individually hashed in its frozen derivation.

AZ, B4 and FJ froze at 20:16:19 UTC; BB froze at 20:19:04 UTC. The exact freeze and release receipts are indexed in the adjacent clean_group01_freezes.json and clean_group01_releases.json. The first combined attempt to display all four released proofs and C_jets.py was context-truncated without visible contents. No reading credit is assigned to that failed display. At 20:21–20:22 UTC I actually read all of AZ, all six B4 items, all seven FJ items, all four BB items, and all of the old C_jets.py in separate bounded outputs. The complete original and proposed pairs were then reread at 20:26–20:28 UTC; B4 and FJ were read in full again after the final small corrections below. The separate rereading JSON binds the final exact block hashes.

Primary source reads for the citation additions were completed at 20:23 UTC: the Cambridge journal PDF of Campana–Demailly–Peternell, Compositio Mathematica 156 (2020), 679–696, DOI 10.1112/S0010437X19007802, Proposition 7.3, pp.693–695 (retrievals turn301284358view0 and turn761065722view0); and Mumford, Publications Mathématiques de l'IHÉS 9 (1961), 5–22, §1 p.6 (turn301284358view1, lines 46–74). The primary web retrievals supplied complete text at these loci. No new local PDF-byte checksum or screenshot inspection is claimed.

## 01AZ: every printed step and receiving application

The printed proof has one enumerated item. Its first arrow is the same canonical inclusion derived before release: in a local equation F, b tensor [F] maps to b dF. The input A.2.2 places the Jacobian ideal in the conductor, so every coefficient b F_xj belongs to O_S. A change F'=uF changes both the frame and the differential by u. Tensoring with A and the finite projection formula identify its domain with eta_*eta*(N* tensor A), and left exactness on global sections gives the exact asserted subspace of H0(S,V tensor A).

The printed trivialization step uses the full reduced fibre, not only its reduced support inside a multiple fibre. The proposed proof explicitly uses F=t composed with f and the frame [F] of I_S/I_S². This is precisely the full-fibre assumption in the statement. After the chosen trivialization of eta*A, the source becomes H0 of the compact normalization's structure sheaf. Every connected component contributes its constant function. The original source never required the normalization to be connected, and the proposed proof preserves that scope.

The statement's compatibility with the quotient vanishing is proved through the same exact map V tensor A to Q tensor A: the constructed subspace lies in its kernel K tensor A. Thus the quotient condition places no additional constraint on these kernel sections. The original A.4.1 input is a proposition, and its given group values match this map. The published application uses exactly A=L_t|S, with eta*A trivial; the opened CDP journal text explicitly records the all-trivial possibility on p.693 and its normalization pullback on p.694. The local equation reference (A.3) is transported to the existing label cdp:eq:A.3, with identical formula and maps.

No mathematical disagreement remains. The edits identify the ambient group, bind the published citation, and write out the quotient map. No computational program is needed for this sheaf-map argument.

## 01B4: genus bound, conductor duality, and embedded delta-one germs

Printed item 1 agrees with the independently derived evaluation and adjunction proof. On the base disc f_*K_Y is a torsion-free rank-one module and hence a line. Its generator has divisor aS; the full fibre mS trivializes O_Y(mS), giving omega_S=O_Y((a+1)S)|S and hence a torsion dualizing line. The Cartier exact sequence and the equality of the two rational Chern characters give chi(O_S)=0. A nonzero section of a torsion line has a nonzero constant tensor power, so it trivializes the line. Thus e=h0(omega_S) is zero or one, and h1(O_S)=1+e. The new proof expands the facts originally delegated to the inherited literal references (A.CD.1) and (A.CD.2).

Printed item 2 uses conductor duality, while the preproof derivation used a different route through Hom(I_D,omega_S). I compared both through exact maps. The preproof inclusion is multiplication in the total quotient sheaf:
Hom(I_D,O_S) → eta_*O_T.
Indeed I_D contains the conductor c, a multiplier q satisfies qc⊂O_S, qc is a B-ideal and therefore lies in c, and the determinant trick on the faithful finite B-module c makes q integral over normal B. Tensoring omega_S and Serre duality yield h2(I_D)≤1. The long cohomology sequence then gives h1(O_D)≤(1+e)+(h2(I_D)-e)≤2.

The printed intermediate equality A.J.31 is itself preserved and proved, rather than discarded in favour of this alternative argument. Put B=eta_*O_T and Q=B/O_S. Normality in dimension two makes B maximal Cohen–Macaulay as an O_S-module. Since S is Gorenstein, applying Hom(-,omega_S) to 0→O_S→B→Q→0 gives
Ext^1_sheaf(Q,omega_S)=omega_S/c omega_S=omega_S|Gamma
and all other sheaf Ext groups zero. Here Hom(B,omega_S)=c omega_S is the multiplication inclusion. Local-to-global Ext and compact Serre duality consequently identify (H0 Q)* with H1(Gamma,omega_S|Gamma). Constants on S and T agree, so H0 Q injects into H1 O_S. This proves the exact numerical equality and bound in A.J.31. Restriction to D is a sheaf quotient whose kernel has no H2, giving the surjective H1 map. The two printed cases e=1 and e=0 then give the same genus bound by the displayed curve Riemann–Roch equality. This proof also explains every map used in the printed item.

Printed item 3 is the same normalization sequence and arithmetic genus identity p_a=g+delta. For positive g the total delta is at most one, and the constants on r local branches give r−1≤delta.

Printed item 4 has the explicit node map C{u,v}/uv → pairs of series with equal constant term, u↦(t,0), v↦(0,s). Both subrings have colength one, proving equality and the node classification.

Printed item 5 has the explicit cusp map (u,v)↦(t²,t³). An order-one function would have a convergent analytic inverse and would make the local ring normal. Its absence places the ring inside C+t²C{t}; equal colength one then proves equality. The frozen derivation gave the additional constructive t² and t³ argument. Every exponent k≥2 has the explicit expression 2(k/2) for even k, or 3+2((k−3)/2) for odd k. Hence the convergent even/odd decomposition proves the claimed isomorphism.

Printed item 6 proves the actual embedding in Y. The surjection on cotangent spaces supplies a defining function with nonzero differential. Taking it as an ambient coordinate cuts a smooth surface; the remaining reduced height-one curve ideal in its factorial regular analytic ring is principal. The pair is a regular sequence. Applying the supplied A.5.5 statement to precisely the same Y,S,D yields the smooth elliptic and constant-type conclusions. No ambient Picard condition has been introduced.

The original B4 proof contains no false intermediate assertion found by this comparison. The conductor-duality explanation and the literal cross-reference repairs preserve all three labelled equations and all claims.

## 01FJ: all seven steps and exact notation transport

Use the following exact map between the frozen derivation and the printed normal-bundle notation:

| Frozen derivation | Printed proof | Reason |
|---|---|---|
| E=N* | N* | Identity of the conormal bundle |
| M⊂E | Q_printed* | The Hessian factor annihilates the radical R |
| Q_new=E/M | R_printed* | Dual of 0→R→N→Q_printed→0 |
| L | B=O_Y(S)|D | Same equation line |
| Delta_new=4ac−b² | 4 Delta_printed | Multiplication by the nonzero scalar 4 |
| triple branches (u,0),(0,u),(u,u) | (0,u),(u,0),(u,u) | Transposition of the first two normalization components |

Printed item 1 agrees with the degree identity deg N=2g−2, deg B=0, and the saturated radical. The degree inequalities in the derivation are the negatives of the corresponding normal-line degrees under the dual maps in the table.

Printed item 2 is the intrinsic radical cubic. In adapted coordinates changes of the third jet contribute a Hessian factor with a radical argument and hence vanish. A base retraction change differentiates the identity H(R,R)=0. This remains valid where the quadratic coefficient vanishes, because the saturated radical is a line bundle there. The nonzero cubic section has degree −3 deg R, giving the same cusp inequality.

Printed item 3 is the tacnode critical quartic. The substitution x↦x+u y² sends b↦b+2au and c↦c+bu+au². The cleared numerator is invariant and holomorphic even at a=0. In the frozen derivation this was the tensor section 4ac−b² of M² Q_new⁴ L². Under the table this is four times the printed section of B² Q_printed^-2 R^-4. Terms arising from retractions contain the radical cubic or a radical Hessian argument. On the open set a≠0 the critical-value construction gives the line transitions; the polynomial expression extends the same section across the zeros. The degree calculation is therefore the identical global argument.

Printed item 4 computes the ordinary-triple discriminant by the squared three pairwise wedges. Each wedge transforms by det(g), yielding weight six; scalar equation multiplication has weight four. The new preproof method uses this factor construction directly. The postrelease transport program proves its equality to the exact coefficient polynomial returned by the old C_jets.py, with a certified separate-degree-four interpolation grid.

Printed item 5 follows when g=1 because each nonnegative divisor degree becomes zero. The quadratic/cubic or quadratic/quartic sections are nowhere zero, and parameter-preserving holomorphic splitting followed by a local unit root gives the same cusp/tacnode forms. For the triple point, after ordering the tangent lines and straightening two branches, the third is y=x u(x,z) with u a unit. The biholomorphism (x,y,z)↦(x,y/u(x,z),z) gives xy(x−y). Thus the singular set is locally just D and the type is constant.

Printed item 6 gives the normalization covers and normal degrees. The maps (u,z)↦(u³,u²,z), (u,z)↦(±u²,u,z), and the three branch inclusions are finite birational maps from smooth sources onto the respective local normal forms. Their inverse-image curves therefore glue to the asserted degree-one, degree-two and degree-three unramified covers. The leading powers u² and u³ identify P² with R and P³ with Q; on the tacnode branch y=u identifies the normal with the pullback of R. On the ordering cover for the triple point, the third tangent line projects isomorphically to the first two. Their degrees are equal and their sum is deg N=0. Descent along the finite cover multiplies degrees by its positive degree, proving degree zero on every original component.

Printed item 7 agrees with the three complete fractional-module calculations in the frozen derivation. The proposed proof writes out the exact image rings and the generators. The cusp image is C{z}+u²B with Jacobian images u³,u⁴; A=u³h and uA in that ring force A∈u²B. The tacnode image consists of pairs differing by u²B; inverse expression (f+g)/2+x(f−g)/(2u²) proves surjectivity. Its multiplier constraints are a+b∈u²B and a−b∈uB, giving opposite simple-pole residues. The triple image has equal constants and third linear coefficient the sum of the first two; the listed degree-k monomials provide all higher coefficients independently. The two derivative vectors force every double-pole coefficient to vanish and leave residues (a,a,−a). Coordinate changes transport the ideals by their invertible Jacobian matrices, and equation units act by a scalar unit modulo the equation.

### Independent computational methods, with timing

The old C_jets.py was first read only after the FJ freeze and release. Its exact SHA256 is 3499553de2b9fb30351c0a4a3444f75ea9359abcb5fd0ab0ee5f4e23fdd5f53b. The pinned retrieval receipt is in records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01. Its entire scope is this target.

| Old routine | Fresh preproof computation | Exact transport and postrelease supplement |
|---|---|---|
| SymPy expand of ac−b²/4 after square completion | Integer evaluation on 54 points with separate degree bounds (2,2,1,2) | Multiply the old identity by 4; same a,b,c,u |
| SymPy discriminant of A x³+B x²+C x+D and diagonal scaling | 256-value multiaffine wedge transformation for all GL2 matrices, then three squared factors | Factor coefficient map A=ace, B=acf+ade+bce, C=adf+bcf+bde, D=bdf; the exact old coefficient discriminant equals the squared wedge product on a 5^6 grid, with each degree ≤4 |
| SymPy linsolve of tacnode constraints | Explicit rational combinations recovering each constant coefficient | Postrelease Hermitian identity norm(a1+a2)²+norm(a1−a2)²=2(norm(a1)²+norm(a2)²), certified on a degree-two grid; positivity gives the zero kernel |
| SymPy linsolve of triple constraints | Exact branch ring and coordinate coefficient maps | Postrelease squared norm of (−a1,a3,a2,−a3) is norm(a1)²+norm(a2)²+2 norm(a3)²; branch permutation is (1 2) |
| Cusp valuation scan on [-6,8] | Constructive entire convergent-series module C{z}+u²B, two coefficient extractions | The explicit map h↦u³h handles all pole orders and all z-coefficients; no finite scan is used to establish the universal statement |

The preproof program curve_jets.py ran 20:15:44 UTC and is bound in the FJ freeze. The postrelease transport program and the old program both ran successfully at 20:23:58 UTC, with outputs and hashes in clean_group01_program_runs.json. The postrelease program adds no prereading event. The coefficient factor map, degree bounds, and norm identities prove exact agreement with the old routines by different algorithms.

During comparative rereading I caught and corrected a sentence in my own proposed text that could have extended the degree-two regularity bound to the cusp. The final sentence explicitly applies that preliminary bound only to the tacnode and triple point. For the cusp, u³h and u⁴h being regular permit order three initially, and the additional ring coefficients then remove orders three and two. This was a correction to a new proposal before submission, not an error attributed to the original target.

## 01BB: arbitrary resolution, minimal conductor, and Euler characteristic

Printed item 1 agrees with the finite degree-one map C→D supplied by the unibranch cusp chart. The source C is the section and hence isomorphic to the positive-genus base. The newly checked B4 proposition applies to exactly this Y,S,D; the general two-torus has trivial canonical line and b2(Y)=0 gives H2(Y,Q)=0. It proves D smooth elliptic with constant cusp type. Thus C→D and the inverse-image normalization curve C_T→D are isomorphisms.

Printed item 2 writes the minimal-resolution passage in compressed notation. The target did not assume its original pi minimal, and it did not explicitly assume its original V effective. The frozen derivation resolves both points by the maps
pi=mu sigma, p=p' sigma, C'=sigma(C).
Every sigma-exceptional curve is pi-exceptional and vertical. The graph image gives the descended p' as a finite birational bijection onto normal Z'. The section maps isomorphically to C'. The minimal resolution mu is unchanged over the smooth cusp neighbourhood of C_T, so (C')²=deg N_C_T/T=0. The exact A.5.3 statement then gives an effective canonical conductor 2C'+V' on Z', with the same nonexceptional conductor valuations and only vertical exceptional components. This supplies effectiveness only at the place where it is proved. It also gives the stated canonical line identity and rational Chern-class equality. The cusp charts make V' disjoint from C'.

Printed item 3 excludes ruling blowups. The frozen proof and proposed proof contract to the same geometrically ruled Z0 through rho. The section square is C0²=n≥0, where n counts its blowup centres, and the effective vertical pushforward V0 is a sum of fibres. Intersecting the pushed canonical equality with the elliptic section gives n+V0.C0=0, hence both vanish. The exceptional divisor E_rho+V' is then numerically trivial; the total-transform basis of point-blowup exceptional divisors has diagonal form -I, so it is zero. Since E_rho is positive on every exceptional prime and V' is effective, rho is an isomorphism. The original local formula for the exceptional conductor coefficient, multiplicity at the centre minus one, is retained and follows from K_X=beta*K_X0+E. The original positive-intersection exclusion of a (-1)-curve meeting the section is justified explicitly by V' disjoint from C': such a curve is not a component of V', so its intersection is at least -1+2.

The remaining resolution map mu cannot contract a square-zero bundle fibre. For this analytic form, the proposed proof gives the exact local-function transport of Mumford's §1 p.6 argument: pull back a holomorphic function through the normal point, write G+sum m_iE_i, use principal-divisor intersections, weight by positive m_i, and apply the row-sum quadratic identity. Properness supplies a strict row and normality supplies connectedness. This proves negative definiteness for this actual analytic resolution. A bundle fibre has square zero, so none is exceptional. The finite bimeromorphic map mu to normal T is then an isomorphism. The conclusion is about T; the initial resolution Z may still contain its original extra blowups. The exact factorization records that distinction by morphisms.

Printed item 4 agrees with the Euler computation. Finite duality identifies the conductor on smooth T with the invertible ideal of the divisor 2C_T. The normalization is an isomorphism off C_T and restricts to the isomorphism C_T→D, hence is a proper bijection and a homeomorphism on underlying compact spaces. Additivity gives the original e(S)=e(T)−e(C_T)+e(D)=0, and the full nonreduced fibre has the same underlying space. The new prefreeze cell program computes the elliptic and sphere Euler factors and the formal product cell count, and proves the weighted matrix identity by coefficient dictionaries. It does not assume a product bundle to infer Betti numbers.

No false original mathematical assertion was found after interpreting its minimal-resolution notation by these maps. The printed identification of a curve on Z with its image on T and the reuse of pi,C,V after the factorization were insufficiently explicit; the proposed proof keeps all three surfaces and maps separate and retains all original hypotheses and conclusions.

## Editorial scope and verification

All 25 register types were considered in each complete block. The local edits address inherited literal references and tags, missing exact publication locators, program bookkeeping, process vocabulary, repeated scope prose, accents, and ambiguous map notation. D10 is already handled by root's tag-only StatementRecord rendering; its four arguments and all theorem metadata remain untouched. No duplicate theorem, orphan paragraph, front-matter claim, unrelated structure change, numerical-evidence theorem, or new parameter choice occurs in these four blocks.

The 14 guards are literal, sequential, uniquely matching replacements. Their full original and proposed blocks are separate files. All ordered label and hypertarget lists agree exactly. Root retains integration ownership. The program-table provenance item for the removed C_jets.py mention is supplied by the pinned source receipt and the old/new method table here; adding the end-table row, if it is absent, belongs to root's source integration.

No canonical events have been appended. The proposed events describe the four actual proof checks, four full paired rereadings, and the two target-specific computational records. They are proposals pending root's review.


Final complete proposed blocks, including the numbered equation environments, were reread in full before this record at 2026-11-21T20:30:39.237631+00:00. The final paired-read hashes are in the companion rereading JSON.
