# F2.39 — order-one deletion and marked maps, before target reading

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

The F2.39 receiving proof and producer remain unopened. Inputs are root's clean assertions and the statement-only packet analysis/continuation_V/F2_39_statement_input_packet.md. The corrected and used clutch convention is exactly s_1...s_k x^kappa=1, as in (F.G3). The earlier clean-message convention product=x^kappa was corrected before this derivation and is not used.

## 1. Actual order-one local cap and its boundary marking

At the specified actual-order-one site i, m_i=1, M_i=I, and v_i is integral. Formula (F.G2) gives w_i=v_i, and (F.G3) gives s_i=x^(v_i). This relation also has a direct geometric map. The order-one cap is the product T^6 times D^2. Retain the chosen affine lift g_i(x)=x+v_i of the identity torus map. Its marked boundary mapping torus is described by (x,1)~(x+v_i,0), in addition to the lattice quotient in x.

The map to the boundary of the product cap is

Phi_i([x,t])=(x+t v_i, exp(2 pi i t)).

It is well-defined at the seam because Phi_i(x,1)=Phi_i(x+v_i,0), and it is equivariant for every lattice translation. Its inverse is (y,exp(2 pi i t))->[y-t v_i,t]; changing the lift t by an integer gives precisely the mapping-torus identification, so this inverse is well-defined. It preserves all fibre lattice labels. The marked peripheral loop [x,t] maps to the slope (v_i,1). The second component bounds the cap disk; therefore its image in the filled cap is exactly x^(v_i), with the positive sign shown. No unmarked replacement of the meridian is used.

## 2. Exact suffix transport and the clutch change

Set A=s_1...s_(i-1), B=s_(i+1)...s_k, and M_B=M_(i+1)...M_k, with B=1 and M_B=I when i=k. Left conjugation gives

B x^a B^(-1)=x^(M_B a),
so x^a B=B x^(M_B^(-1)a).

The actual affine suffix has the form b(x)=M_B x+b_0. Its corresponding transport calculation is

b^(-1) T_v b(x)=M_B^(-1)(M_B x+b_0+v-b_0)
=x+M_B^(-1)v.

Thus even the affine suffix offsets are retained and cancel by their actual inverse; no linear transport is substituted for an unexplained affine one.

Substitute the local cap relation into the corrected clutch word:

A x^(v_i) B x^kappa
= A B x^(M_B^(-1)v_i) x^kappa
= A B x^(kappa+M_B^(-1)v_i)=1.

The reduced datum therefore has exactly kappa'=kappa+M_B^(-1)v_i. The sign is fixed both by the product-cap boundary map in Section1 and the original clutch relation; it is not selected by a numerical convention.

## 3. Actual marked group and gluing comparisons

The map from the old presentation to the reduced presentation sends every fibre generator x^a to itself, sends every remaining peripheral generator s_j to its corresponding generator, and sends s_i to x^(v_i). The old conjugation relation at i becomes commutation of fibre translations; the local power relation becomes its defining equality; the old clutch relation becomes the new relation by Section2. All other relations remain literally unchanged. Conversely, map the reduced fibre and peripheral generators to the same old generators. The new clutch relation is the old one after substituting s_i=x^(v_i). These two homomorphisms compose to the identity on every generator, using exactly the removed local relation. This is the explicit marked Tietze isomorphism.

For the geometric comparison, fill the i-th base puncture using the actual product cap and the boundary chart Phi_i above. This enlarges the base chart by that disk. It is the same quotient space as the original construction, with identity comparison on all unchanged pieces and Phi_i as its transition to the product-cap chart. Move the resulting integral translation loop along the specified ordered clutch corridor. In its parallel fibre coordinate the chart change is x->x+t v_i; at the terminal end, where the coordinate is the suffix frame b, it is x->x+t M_B^(-1)v_i by the displayed affine conjugation calculation. These coordinate changes agree on each overlap and preserve lattice translations. Their terminal clutch is therefore x^(kappa'), while all other boundary identifications are the same. This gives the reduced marked-gluing atlas and its inverse atlas maps explicitly. It does not assert that the nontrivial translation loop extends over a disk while fixing all old boundary markings; its contribution is recorded in kappa'.

Since M_i=I, the ordered product of the remaining linear matrices equals the original product. Thus M_0=(M_1...M_k)^(-1), the cusp lattice im(M_0-I), and the specified primitive cusp basis/marking are unchanged as actual matrices and labelled sublattices. The comparison has not applied a new conjugator to the cusp marking.

## 4. Number of order-one sites

The given nontrivial square-zero cusp has M_0=I+N with N^2=0 and N nonzero over characteristic zero. The binomial product, or induction multiplying I+qN by I+N, gives (I+N)^q=I+qN for every positive integer q. This never equals I, so M_0 has infinite order.

Every finite-site M_j has finite order. If only zero or one nonidentity finite matrix remains, their product and its inverse have finite order, contradicting the displayed formula for M_0. With k=2 no site can have actual order one. With k=3 at most one site can have actual order one. These conclusions use the actual-order-one implication M_i=I; they do not identify linear order with affine order in any other case.

## 5. Optional characteristic-polynomial rejection map

For a simultaneous integral conjugator C, the identity

lambda I-C M_j C^(-1)=C(lambda I-M_j)C^(-1)

holds as an identity over Z[lambda]. Taking the top exterior power gives the determinant factors det C, det(lambda I-M_j), and det C^(-1); their outside product is 1. Hence each characteristic polynomial is preserved. Different characteristic polynomials therefore rule out that proposed conjugacy by this exact determinant identity. Equality alone is only the necessary invariant used by the filter; no converse classification statement is inferred here.

## 6. Scope of the optional H1 comparison

The clean F2.35 statement specifies a complete homology algorithm but does not supply the actual cellular cone maps or its degree-one generators. This note therefore does not claim the requested specific cone-to-presentation H1 comparison. The marked group equivalence above is proved directly. The root review must retain its own exact cone realization/comparison receipt, or supply those clean chain data for a separate before-reading derivation. No missing map is supplied by a generic assertion that two groups have the same invariant factors.
