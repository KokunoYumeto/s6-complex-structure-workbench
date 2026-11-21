# Paper II first-four checks: computational-method and exact-map addendum

This addendum concerns only 01F8 (C.3.2), 01F9 (C.3.3), 01FA (C.3.4) and 01G8 (D.2.1). Their substantive derivations were frozen before their respective target proofs were released. The old program was opened only after those derivations, complete proof comparisons and new computations. Only its target-relevant lines81–95 and102–159 were displayed and archived; unrelated routines were not displayed. This addendum creates no event and makes no claim that a representation change alone supplies a different mathematical method.

## 01F8: secondary Kodaira example

Write zeta=(1+i sqrt(3))/2. The prereading construction uses holomorphic affine maps of C²:

- a(Z,W)=(Z+1,W+Z+conjugate(zeta));
- b(Z,W)=(Z+zeta,W+conjugate(zeta)Z+conjugate(zeta));
- c(Z,W)=(Z,W+i sqrt(3)); d(Z,W)=(Z,W+1);
- T(Z,W)=(zeta Z,W+1/6).

The frozen argument proves a faithful lattice normal form, freeness, proper discontinuity, compactness, the primary elliptic-bundle cover, the free sixfold quotient, the abelianization, Euler characteristic and canonical character. These geometric arguments are in the prereading derivation; a successful matrix assertion does not replace them.

### Exact transport to the printed group and deck action

For the printed real Heisenberg group with product
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+(xy'-yx')/2), define

Phi(x,y,z,t)=(Z,W),
Z=x+zeta y,
W=t+i sqrt(3)z+(x²+xy+y²)/2-i sqrt(3)(x+y)/2.

Its inverse is

y=2 Im(Z)/sqrt(3), x=Re(Z)-y/2,
z=Im(W)/sqrt(3)+(x+y)/2,
t=Re(W)-(x²+xy+y²)/2.

The new program checks both inverse compositions and the real Jacobian determinant -3/2. It checks exact equivariance for left multiplication by a,b,c, the unit t-translation d, and (sigma,t+1/6), where sigma(x,y,z)=(-y,x+y,z-y/2). Their images are exactly the five affine transformations above. Thus the lattice presentation, central generator, finite deck action and abelianization are transported by an explicit real diffeomorphism.

No holomorphic identification by Phi is asserted or used. The printed fibre coframe has a different real-coordinate expression from the affine construction. The affine maps are independently holomorphic with determinant character zeta; the printed coframe's integrability and character are independently checked by the exact differential pullbacks below. Both routes establish the same stated existence and numerical conclusions without requiring an unproved complex-analytic identification.

| Printed computational step | Verified old target routine | New check and actual difference in method |
|---|---|---|
| Horizontal order6 and det(A-I)=1 | SymPy2×2 matrix power, determinant and Smith form at lines82–86 | Prereading3×3 homogeneous affine identities T a T^-1=b, T b T^-1=a^-1 b and T^6=d, plus a4×5 integer presentation Smith form. Postreading3×3 sigma matrix power and the2×2 determinant directly recheck the printed values. The latter direct calculations overlap the old method and are not represented as an independent route by themselves. |
| sigma^6=identity on the central coordinate | Six successive simultaneous symbolic substitutions at lines87–93 | One3×3 linear transformation on (x,y,z), raised to its sixth power, and the independently frozen affine lift T^6=d. Phi gives the exact relation between the lifts, including the central half-linear term. |
| Preservation of the integral Heisenberg lattice | One expanded polynomial difference xy+y(y-1)/2 at lines94–95 | New symbolic group-law identity and both forward and inverse lattice differences: xy+y(y-1)/2 and uv+u(u-1)/2. Products of consecutive integers prove both differences integral. The forward expansion checks the same polynomial as the old code; the inverse and group-law identities make the transport explicit. |
| Integrable complex coframe and canonical character | Not computed in the displayed old target routine | New Jacobian pullbacks give sigma*alpha=zeta alpha and sigma*beta=beta. Direct differentiation gives d alpha=0 and d beta=-dx wedge dy, of type(1,1); alpha wedge d beta=0. A division-free Berkowitz determinant is exactly2 sqrt(3), proving the coframe has no exceptional zero locus. The printed canonical form and its order6 character follow; compactness of the cover makes a trivialization ratio constant. |
| Abelianization H1=Z | Smith form of A-I, after central commutator and deck presentation in the printed proof | The prereading presentation uses columns(a,b,c,T,d), relations c=0,a-b=0,a=0,6T-d=0; its Smith factors are1,1,1,1 with one free generator. Phi identifies a,b,c,T,d with the printed generators. Eliminating c and d reduces this presentation to the printed coinvariant computation, so the two integer calculations have an explicit presentation map. |
| H²=0 and canonical order exactly6 | Geometric deductions in the printed proof, not a separate old routine | The prereading free finite quotient of an elliptic bundle has Euler0. With b1=1, oriented four-dimensional Poincare duality gives b2=0; UCT gives H²=0 because H1=Z is torsion-free. The character argument above proves exact canonical order6. These deductions were written before release and then checked against the complete printed argument. |

## 01F9: secondary Hopf example

The frozen argument starts from the double cover SU2→SO3 and the rotation group of an icosahedron, identified with A5. It proves that the full preimage is perfect: its commutator subgroup surjects onto the perfect quotient A5, while the central kernel is contained in the commutator subgroup because [i,j]=-1. Hence every element is in that subgroup. The prereading program checks A5's derived subgroup by even permutations of five letters, and the central commutator by explicit2×2 matrices. This is the separate group-theoretic route supporting the different-method requirement.

### Exact quaternion, matrix and rotation maps

For q=a+bi+cj+dk, use

rho(q)=[[a+ib,c+id],[-c+id,a-ib]].

The new transport program verifies rho(pq)=rho(p)rho(q) symbolically, rho(q)*rho(q)=norm(q)² I and det rho(q)=norm(q)². Its explicit inverse reads

a=(M11+M22)/2, b=(M11-M22)/(2i),
c=(M12-M21)/2, d=(M12+M21)/(2i).

Thus the printed120 unit quaternions and the newly computed120 faithful SU2 matrices are exactly related. Quaternion conjugation on imaginary coordinates gives the displayed3×3 rotation formula in the transport program. Its image has60 elements and kernel exactly{1,-1}. Every image rotation preserves the icosahedron obtained by swapping the last two coordinates of the prereading vertex set. This coordinate permutation is recorded explicitly. Conjugating rotations by that permutation identifies the two icosahedron rotation groups; because the vertex set is centrally symmetric, the same conjugation is induced by the determinant-one matrix equal to minus that permutation. No unrecorded identification of orientations is used.

A concrete graph of60 rotation/permutation pairs, generated by two displayed elements of orders2 and3 whose product has order5, is checked for consistency and bijectivity. The permutation generators are (12)(34) and (135) in one-based notation. Right multiplication by both generators closes the graph; it therefore gives an actual group isomorphism from the60 rotations to A5. The prereading A5 commutator calculation and the central commutator consequently apply to the printed group through explicit maps.

| Printed computational step | Verified old target routine | New check and actual difference in method |
|---|---|---|
| Construction of120 elements and norm1 | Tuple enumeration with exact Fraction pairs representing Q(sqrt(5)) | The source set is independently enumerated in SymPy's exact algebraic field and mapped injectively by rho. Cardinality120 and norm1 are checked. This is the same mathematical finite set and enumeration, now connected by the explicit map; representation choice alone is not claimed as a distinct proof. |
| All14,400 products belong to the set | Direct quaternion product formula over Fraction pairs, building a120×120 table | New2×2 matrix multiplication over QQ(i,sqrt(5)), with exact determinant-one and inverse checks. rho's symbolic multiplicativity proves that each matrix result tests the corresponding printed quaternion product. This is a recomputation in another algebraic representation, supplementing the prereading geometric-group construction. |
| Perfectness | All quaternion commutators, then subgroup closure in the multiplication table | The new matrix recomputation finds120 distinct single commutators. Separately, the prereading proof uses the perfect A5 quotient and central commutator, as described above. The postreading rotation/permutation graph explicitly transports that separate argument to the printed120-element group. |
| Free action on C² minus0 | Printed SU2 eigenvalue argument | The frozen proof uses determinant1 and unitarity: an eigenvalue1 forces the other to be1, and a unitary matrix is diagonalizable, hence identity. With scalar q=1/2, norm excludes a fixed point for every nonzero scalar exponent. The source uses2^Z; the exact exponent map n→-n identifies the two scalar subgroups. |
| Compact quotient and H1=Z,H²=0 | Printed product/radial quotient and perfectness deductions | The frozen radial decomposition gives(S³/P)×S¹. The first factor has finite perfect fundamental group and vanishing H1; oriented three-dimensional duality and UCT give H²=0, and Kunneth gives the stated Hopf quotient groups. The finite primary Hopf cover and noncyclic fundamental group supply the secondary designation. These geometric steps were checked in full, not inferred from code success. |

## 01FA and01G8: targeted checks at the repaired smooth scope

01FA's frozen proof uses Cartier intersection on a smooth ambient threefold, pulls the canonical section to a compact Kähler resolution, and pairs its nonzero effective divisor with a Kähler form. The b2=0 hypothesis makes the pulled-back first Chern class zero in real cohomology, contradicting positivity. The original statement lacked explicit smoothness. Root accepted and applied the smooth-hypothesis guard after auditing every coded receiving use. The event proposal is a targeted proof check of that repaired smooth statement, not a proof of the broader potentially singular reading.

01G8's frozen proof uses the connected-fibre Leray injection H1(base,Q)→H1(Y,Q) to prove genus0 directly; the identity torus monodromy has four-dimensional coinvariants, and D.1.2's count gives r=s+3. Thus a reducible fibre exists; the repaired01FA applies to its components. The source rewrite retains its exact mathematical sequences while providing the rational-cohomology base-genus argument explicitly. The new four-dimensional identity-matrix rank and integer substitution support that argument. Neither this check nor01FA is claimed as an independent re-proof merely because it was written before release; the proposed category remains targeted proof check.

## Evidence and event scope

The companion JSON binds the old source/routine extracts, all new programs and outputs, the original freeze/release receipts, the complete four-proof comparison, the smooth-scope receiver audit, the applied source guards and the JSON-only event proposals. The postreading recomputations and transports are identified as postreading. The event proposal contains one candidate event per distinct owning statement, not one event per routine, representation or calculation. Root review and canonical acceptance remain separate. No canonical source, ledger or defect log is changed by this addendum.
