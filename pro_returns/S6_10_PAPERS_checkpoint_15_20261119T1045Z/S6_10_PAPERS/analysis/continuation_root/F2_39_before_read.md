# F2.39: complete receiving argument before its printed proof

The only target/input material read is `analysis/continuation_V/F2_39_statement_input_packet.md`, SHA256 dacc0b383a7d6b82f1b91571a4ee717f60238b1e55b55c393b91d9c3ebc1d02b, containing statements and definitions. F2.39's printed proof and original producing programs remain unread. Its named algorithmic theorems are used at exactly their stated scopes; their own renewed reviews remain separately recorded. This derivation establishes the actual interfaces and all additional assertions made by the receiving theorem.

## 1. Canonical representative and input-dependent stopping bound

Write a full ordered tuple as T=(M1,…,Mk,M0), including its actual cusp matrix, and let H be its maximum absolute entry. Since its matrices are integral and invertible, H≥1. There are D=36(k+1) scalar entries. The entire cube of integer arrays with entries in[−H,H] contains exactly(2H+1)^D elements: the explicit bijection sends a tuple to its ordered list of D entries, with inverse reshaping each consecutive36 entries into its six-by-six matrix.

In the height/lex branch of F2.37, enumerate that cube in increasing maximum entry height and then in the fixed row-major tuple order. Apply its exact admissibility filters and the F2.36 simultaneous integral-conjugacy decision to each candidate S. The input T itself lies in this cube and passes, so a conjugate is found before more than(2H+1)^D candidate arrays have been tested. Each individual decision terminates by the named input theorem. Its returned matrix P is verified by integer multiplication and detP=±1; choose the explicit convention S_i=P M_i P⁻¹ for all labelled entries. A witness returned in the inverse convention is replaced by its computed inverse, so the convention is a specified map.

The first accepted tuple is the least-height/lex member of the entire conjugacy orbit: every earlier orbit member has height≤H and already occurred in this enumeration. The result consequently does not depend on the height of the input chosen from that orbit. Two conjugate inputs have the same first orbit member. Conversely, two inputs with the same output S and witnesses P,Q are conjugate by Q⁻¹P, since Q⁻¹P M_i P⁻¹Q equals the second input's i-th matrix. This proves both the canonical equality test and the returned simultaneous witness on every labelled matrix.

F2.37's exceptional marked sectors are retained literally. A fixed identity finite slot is deleted and reinserted at the same position by the equivariant maps derived in `F2_37_auxiliary_before_read.md`; its returned conjugator is unchanged. That operation preserves height and lex comparison for the ordinary branch. The two-involution branch uses the separate F2.38 canonical convention, its56 exact classes and its returned witness. Equality of its representatives is its already proved complete orbit test, and it performs no longer exhaustive cube search. Thus the stated cube bound remains an upper bound for the fallback, without identifying the special convention with a lex minimum.

The finite-order list and free-lift filter are the exact F2.2/F2.37 inputs. They remove candidates from the finite cube; they never increase its number. All arithmetic entries and lattice equalities in those tests are exact. This supplies the announced bound for k=2 and k=3 without a universal entry cutoff.

## 2. Why no fixed global height cutoff can represent all classes

Use the stated F2.16 family and its exact named trace identity

tr(M1 M2³)=p(v)=−v⁴+v³−v²+2.

Trace is invariant under the actual simultaneous conjugation: the word is carried to P(M1M2³)P⁻¹. A tuple all of whose entries have absolute value≤H has |tr(M1M2³)|≤6⁴H⁴. Indeed each diagonal entry of this four-factor word is a sum of6³ products of four entries, and the trace sums6 diagonal entries.

For |v|≥2, p(v) is negative and |p(v)|≥|v|⁴−|v|³+|v|²−2≥|v|⁴/2. The explicit infinite admissible integer-parameter subset in F2.16 is unbounded in absolute value. For each fixed H it therefore supplies |v| sufficiently large that |p(v)|>6⁴H⁴. That conjugacy class has no representative in the height-H cube. This proves the absence of a fixed global cutoff by the actual invariant word and its matrix-entry bound. The fresh program recomputes p(v) from the clean five-dimensional X,Y definitions, then adds the invariant-line trace1, so no old trace-producing code is reused.

## 3. Exact transport of a fully marked gluing input

Keep each actual affine order m_i, integer numerator v_i, clutch vector kappa and primitive cusp marking P0 as additional data. For a simultaneous unimodular change Q set

M_i′=Q M_i Q⁻¹, v_i′=Q v_i, kappa′=Q kappa, P0′=Q P0.

The actual map of real tori is x modZ⁶↦Qx modZ⁶, with inverse Q⁻¹. It satisfies g_i′(Qx)=Q g_i(x), and on a finite cap the map[(s,x)]↦[(s,Qx)] is equivariant for the same order-m_i cyclic action. It restricts to the identical boundary mapping-torus transport. On the standard Kuhn cap the equality(P0′)⁻¹ Q P0=I identifies every chosen standard chart, lattice and fan cell; its boundary is exactly the torus map Q. Thus the specified cusp cap is carried with its marking. Clutch translations satisfy Q(x+kappa)=Qx+kappa′, so these maps glue to the actual marked-space map. An orientation carried with the datum is transported by this same map, with detQ retained; no replacement of that transport by an undeclared ambient orientation is made.

The power vectors satisfy

w_i′=(1/m_i)sum_j (M_i′)^j v_i′=Q w_i,

and the actual cusp lattice and invariant integral normal closure satisfy U′=QU and L′=QL. These are identities of integral sums, with no saturation operation. In the group presentation the map x^lambda↦x′^(Q lambda), s_i↦s_i′ preserves the conjugation, actual power and clutch relations, and has the inverse from Q⁻¹. It therefore supplies an explicit group isomorphism for the transported fully marked datum.

The homology computation is likewise on that supplied cap and on those actual boundary maps. No inference from peripheral matrices alone enters: F2.3 supplies the need for a filling specification, and P0 is retained in the algorithm's input and in its geometric transport above.

## 4. Full groups and every integral homology group by finite operations

Apply F2.31 to the actual data. It returns its finite presentation and the precise injected abelian kernel: for two points A/<e> with the cyclic quotient and lifted relation t^d=z; for three points the stated Euclidean/hyperbolic or spherical-triangle quotient and its exact transfer relation. These are exactly the actual m_i,w_i,kappa,U supplied above. Hence the finite operations compute the full group with its extension data, rather than only its abelianization. In the two-point simply connected test, the stated quotient order d and the Smith factors of A/<e> give the exact answer. The F2.7 triangle quotient excludes three genuine multiple points from that survivor condition.

For homology apply F2.35 with the specified primitive marking. It returns the full chain prefix through degree9, with all maps, affine translations and higher coherence retained, and no more than4003 generators in each degree. A finite free integer chain prefix computes every H_j for j≤8 by exact kernel and quotient maps. Explicitly, write a Smith reduction U_j D_j V_j=diag(d_1,…,d_r,0,…,0). The last columns of V_j are a basis K_j for kerD_j. In V_j⁻¹D_(j+1), the first r rows vanish, because multiplication by the nonzero d_i gives zero and Z is torsion-free. Its remaining rows B_j are the actual coordinates of the next boundary in K_j. Therefore H_j=coker B_j, and a second Smith reduction gives its free rank and every nontrivial torsion invariant factor. The degree9 term is precisely the needed incoming boundary for H8. No spectral-sequence extension is left to choose.

There is no bound imposed on m_i, on the entries of v_i or kappa, or on the lattice indices: each input is a finite list of integers, and the invoked algorithms terminate on that input. The group and chain algorithms operate on those integers directly. The cube bound in section1 is the finite bound for a supplied linear tuple, not a cutoff on the other marked data.

## 5. Exhaustiveness of the survivor parametrization and its smooth type

F2.30 is a necessary-and-sufficient classification for this same specified Kuhn cap and these affine translation clutchings. Apply both directions of its stated equivalence. Every datum with pi1=1 and H2=H3=0 is in its two-point order-five/order-four parameter enumeration, its terminating stable-lattice/primitive-extension list, its exact F.HC1/F.HC3 lattice tests, and its F.T12 affine-twist tests. Conversely every retained datum passes those tests and has the stated three vanishing conditions. No extra cutoff is introduced while applying this equivalence to the full group/homology interfaces of section4.

For every retained filling, use F2.30's full integral homology and oriented smooth-type conclusion, in its recorded orientation: H0=H8=Z, H4=Z⁴, all other groups vanish, and the oriented manifold is3HP²#(−HP²). Its stated period consequence is exactly the existing F3.11 input, whose scope concerns bounded cusp periods with the other points still punctured. The current theorem adds no good-reduction condition. The complete unrestricted linear classification, all marked topological computations and this exact survivor subset together prove every clause of F2.39.

## Verification and remaining dependency scopes

The fresh companion program verifies the trace polynomial and actual matrix-entry bound examples, constructs the marked cusp basis for the supplied rank-six example, and checks the full F.G10 integer relation-matrix transport under explicit unimodular changes. It does not claim to implement or rerun the entire named F2.36 conjugacy algorithm or the general F2.35 chain builder. Their algorithms are named mathematical inputs here and retain their own separate computation/proof receipts. Root's whole-current-proof credit is not set until the printed F2.39 proof has been compared and every retained additional route covered.
