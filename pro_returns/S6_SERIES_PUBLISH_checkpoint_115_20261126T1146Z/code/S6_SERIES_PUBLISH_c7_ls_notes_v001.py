"""Complete the local LS comparison and execution-scope notes.

The receiver and all frozen fresh evidence remain unchanged.  The earlier
post-exposure note is retained before its completion paragraph is added.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

W = Path(__file__).resolve().parents[1]
lane = W / 'agents/continuation7_iii_vertical_correction_receiving'
prefix = 'S6_SERIES_PUBLISH_III_02LS'
receiver = lane / f'{prefix}_receiving.tex'
fresh = W / 'agents/continuation7_iii_vertical_correction' / f'{prefix}_fresh_derivation.md'
assert sha256(receiver.read_bytes()).hexdigest() == '51e26023340cbb59099c02bacdd2db510caba3262c0d5b1a5fa079b16d9e10b2'
assert sha256(fresh.read_bytes()).hexdigest() == 'ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d'
post = lane / f'{prefix}_post_exposure_auxiliaries.md'
old = post.read_bytes()
backup = lane / f'{prefix}_post_exposure_auxiliaries_draft_v001.md'
assert not backup.exists()
backup.write_bytes(old)
text = old.decode()
before = ('additional blind-proof credit. This note is being completed together\n'
          'with its full output readback and receiving proof.')
after = ('additional blind-proof credit. Its complete mathematical content,\n'
         'the full direct lossless output and the receiving proof have been\n'
         'read. Root admission and canonical application remain pending.')
assert text.count(before) == 1
text = text.replace(before, after, 1)
text += r'''

## 9. Exact retained executions and completed reading scope

Every basename in the following table has the prefix
`code/S6_SERIES_PUBLISH_c7_ls_`. For every executed `.py` the actual
`.out` and `.err` were retained separately. All listed `.err` files
exist and have zero bytes; an HTTP404 was caught and printed to stdout,
so empty stderr does not turn that failed retrieval into a success.

| Basename | Source lines | Actual stdout scope | Execution UTC on 2026-11-25 |
|---|---:|---|---|
| historical_retrieve_v001 | 31 | 5 lines; three primary historical sources | 09:39:43--09:40:02 |
| historical_retrieve_v002 | 35 | 6 lines; two JSON files, literal audit-JSON404 and required common helper | 09:46:03--09:46:27 |
| historical_retain_v001 | 44 | 33 lines; byte-for-byte preservation and exact hashes | 09:47:26 |
| historical_inspect_v001 | 36 | 182 lines; exact bounded helper bodies and output fields | 09:51:26 |
| historical_retrieve_v003 | 29 | 4 lines; two strictly needed generic helper sources | 09:53:02--09:53:18 |
| historical_extract_v002 | 29 | 80 lines; bounded generic Smith, graph and central-word definitions | 09:53:56 |
| post_local_v001 | 150 | 627 lines, 179234 bytes; all local/global and original field checks | 09:57:41.986972--09:57:42.879077 |
| post_relations_v001 | 161 | 37 lines, 379906 bytes; all sixteen exact presentation maps and inverses | 09:59:52.710459--10:00:08.379970 |
| post_obstructions_v001 | 43 | 138 lines, 151082 bytes; all135 literal historical obstruction values and zero selectors | 10:02:35.379910--10:02:35.781838 |
| post_readback_v001 | 107 | 2038 lines, 485611 bytes; direct lossless reading form | 10:02:42.550553--10:02:43.190896 |
| post_readback_v002 | 58 | 2044 lines, 441117 bytes; optional reversible record-delta form | completed10:04:32.078365 |
| receiver_v001 | 751 | 4 lines; initial768-line receiver and identity checks | completed10:17:47.042871 |
| receiver_edit_v001 | 48 | full two-hunk diff and exact old/new hashes | completed10:30:54.106631 |

All these actual sources have been read in full. All retrieval,
retention, inspection, extraction, assembler and editor stdout files
have been read in full. The post-local, relation and obstruction
stdout streams were read through the complete direct lossless v001:
all2038 displayed lines, all742 matrix definitions, all481 vector
definitions, every structured record and every scalar field. This
reading completed before10:25:54 UTC. The complete v001 source proves
and checks the inverse expansion to every original output byte,
including line order, metadata and duplicated values. It additionally
reconstructs both historical pretty-printed JSON files and the new
relation JSON byte-identically. This is the precise lossless reading
scope; repeated original JSON bytes were not each manually displayed.

The optional v002 source was also read in full. It retains the same
literal matrix/vector definitions and replaces773 structured records
by exact earlier-record plus absolute-path changes, preserving object
key order and list lengths. Its successful run checks that expansion
recovers every byte of v001. Only its beginning and end were separately
displayed; no second whole manual reading of v002 is claimed. All its
mathematical entries are covered by the whole v001 reading and the
proved inverse. Root chose v001 as the canonical reading form.

One read-only attempt to display v001 lines1536--1560 encountered an
exec-server transport-disconnected diagnostic. It wrote no file and
ran no mathematical computation; the same range was then displayed
successfully. Earlier output-budget truncations likewise received no
whole-reading credit until their complete bounded ranges were read.
No unknown execution bytes have been reconstructed.

The two receiver edits have a retained exact diff at
`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v001.diff`. They specify the
least-positive-denominator solution of (B-I)z_G=g and the literal sign
f_T(x)=wedge^2(T) sum_{i<j}x_i x_j e_ij-z_T(x). The earlier receiver is
preserved as `S6_SERIES_PUBLISH_III_02LS_receiving_draft_v001.tex`.
The 772-line current receiver has SHA256
51e26023340cbb59099c02bacdd2db510caba3262c0d5b1a5fa079b16d9e10b2.
Its initial whole reread plus the exact two-hunk reread covers every
final line. No frozen fresh file was changed.

The three mathematical validator source hashes are, respectively:

* post_local_v001.py:
  5480af5629ea9f1d7858603b49a3e14ef05601371206bba78a8a2d14c31b4040.
* post_relations_v001.py:
  6cd3101269a4211cd007c2e0dd135aad168921ac3453d03508bb1c28085b229e.
* post_obstructions_v001.py:
  7128d1726be9e3ce96681dea9b224c15f0562cf12cafd6a262e31f2452a36057.

Their actual stdout hashes are, in the same order:
a3f9a1259cffe2113415c1cd6b44d87cf1bfe2596677899c70646f2d30d038cb;
40c87f5efd5abc46a609627d40838c1cd7da94c66ac647e532dfd2750a1d5dd7;
44c0783f0cbfae8de8fc9f529a05185dcca47b90fb175c95d781fa96aa99eb43.
The direct readback source and stdout hashes are
634dd5ed418e2699645a30ab09a90eed6daaa2c07f9ef86b48ddaa581c577beb
and38eeaf8832ab34f54a5f2895b068cdf5fc3cdc77e05f3f32a90b747c1d442531.

The receiver proves every stated conclusion. The exact old/new
component and presentation maps prove that neither the D.VC10 vector
difference nor the70/59 relation count refutes the original theorem.
There is no D25 or D27 mathematical refutation event in this packet.
The local repair proposals record the explicit convention/marking maps,
the complete relative and computational proof scope, and the movement
of the following audit paragraph inside the single proof. Publication
unit work, including ordinary equation numbering, navigation headers,
program-citation form and final PDF checks, remains separately open.
'''
post.write_text(text, newline='\n')
diff = ''.join(difflib.unified_diff(old.decode().splitlines(True), text.splitlines(True),
                                  fromfile=backup.name, tofile=post.name))
diffpath = W / 'code/S6_SERIES_PUBLISH_c7_ls_notes_v001.diff'
assert not diffpath.exists()
diffpath.write_text(diff, newline='\n')

comparison = r'''# 02LS whole-original comparison and receiving proof

Checker: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning
effort is not separately exposed. Permanent statement identity:
`maps:src:D.2.50`, printed tag02LS.

## 1. Outcome and exposure chronology

Every clause of the theorem stands. For all21 defining rational
elliptic surfaces and all signed integers a,b, an integral vertical
correction exists precisely when d0 divides ab. Every such correction
gives the actual line isomorphism J_D=f*O(ab/d0), and the complete
ambiguity consists of the invariant component orbit sums. For positive
a,b and every nonnegative whole-fibre weight distribution of that
total, the specified punctured periods are integral and have the
claimed ordered product. All sixteen specified OS45/default fillings
are simply connected and have H2=H3=Z/b and the other stated groups.

The complete fresh derivation froze at2026-11-25 09:29:21 UTC with
SHA256 ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d.
Root fully reviewed it before the individual release at
2026-11-25T09:37:04.929071+00:00. The fresh proof, every fresh program
version and every original fresh output remain unchanged.

The fresh work used the clean47-line LS statement, admitted inputs at
their disclosed scopes, and root's attributed local/global vertical
argument. The lane independently wrote the full six-coordinate fibre
and primitive graph-kernel computation for the16 examples. It did not
use the natural-row coprimality shortcut: here gcd(a,b)=2. The admitted
LI bar construction is an input, and root's local proof is attributed;
neither receives a second independent-proof count from this lane.

After release, the complete47-line statement, all232 original proof
lines20762--20993 and the entire following audit paragraph in the
authorized20994--21005 gap were read. The14 original items are all
settled below. The post-exposure additive-pair, historical-selector and
presentation-comparison work receives used-and-rechecked credit only.
This lane opened no LT or LU original or historical target algorithm.
Root's separate later LU exposure is not this lane's exposure.

The stable receiving file is
`S6_SERIES_PUBLISH_III_02LS_receiving.tex`, 772 lines,34453 bytes,
SHA256 51e26023340cbb59099c02bacdd2db510caba3262c0d5b1a5fa079b16d9e10b2.
It contains one theorem and one proof. The mathematical content has
been fully reread; root admission and canonical application are pending.

## 2. Every statement clause

| Original clause | Complete disposition and receiving locus |
|---|---|
| All21 rational elliptic surfaces, MW=ZG and height1/d0 | The admitted KT defining fixture and all21 marked component-order lists are used. Receiver item4 gives the explicit table and the order formula from U(B-I)V. All82 literal(B,g) entries have an integral preimage of order*g. |
| Arbitrary signed a,b | Items1--4 prove the integral local equation, its full solution lattice and the signed residue criterion. Zero multiples are handled by d=0 and the constant generic-fibre function. No positivity is used for this part. |
| J_D a base pullback iff d0 divides ab | Items2--4 construct the generic-fibre rational function, prove ker C=Z mu with mu0=1, obtain the exact whole-fibre divisor, and prove both divisibility directions. |
| Exact base line D.VC1 for every correction | Item2 derives d_q-d_0=contr(P,Q), cancels every mixed height correction and obtains degree ab/d0. The rational function, canonical vertical sections and degree-zero base rational function define the isomorphism; reciprocal factors give its inverse. |
| Full ambiguity is invariant component orbit sums | Item1 proves C(S-I)(d-d')=0 forces (S-I)(d-d')=0 and gives the literal orbit basis and representative-coordinate inverse. Whole fibres are included. |
| Positive a,b and all nonnegative weights of the prescribed total | Item5 gives the tensor/arrow conjugation, all multiplier units, logarithmic L and L inverse, integral T and T inverse, and product I+(sum w-ab/d0)E_delta,gamma. The denominator proof is unbounded in a,b. |
| Scope of punctured family versus original caps | The actual map is given on the punctured line and its period lattice. The theorem makes no original-cap identification. The later16 examples use only the explicitly constructed Mumford caps. |
| OS45/default pairs(2,4),(4,2), four I1 zero positions, e=±1, no extra affine translations | Items6--10 retain D.VC9 and D.VC10, specify the cap origins through the punctured map, retain the ordinary meridian mu_o+e gamma and give every boundary map and inverse. The2×4×2 parameter set is exactly the16 computed fillings. |
| pi1=1 | Item12 uses the actual semidirect-product presentation, the integral right inverse of the six toric vanishing vectors onto the nongamma fibre Z3, the singular origin discs and gamma^e=1. |
| H2=H3=Z/b and all other groups D.VC7 | Items11--13 give the23×59 integral matrix, full Smith maps and quotient inverse, the complete relative six-disc map and its inverse, chi=2, the Bockstein/linking map and integral duality. |
| Smooth diffeomorphism classes not inferred from these groups | The receiver proves exactly the homological and marked construction claims. No smooth-classification statement is introduced. |

The two families of sixteen have explicit different parameter sets:
the16 additional height-one initial rows range over OS45,46,50,55 and
their stated collision profiles; the16 completed examples use only
OS45/default with four zero positions and two clutch signs. Both sets
are written in the receiver and fully checked in the retained output.

## 3. Every original proof item and every added auxiliary

### Item1: integral multidegree and permutation conventions

The degree column is e_p-e_0+Cd, with mu-transpose degree zero.
The original pushforward convention T and the receiving pullback S
satisfy T=S inverse. Their two equations are related by the literal
unimodular left map -S inverse and inverse map -S. Thus both equations
have the same integral solution set. Receiver item1 makes the action
on component indices and the pullback formula explicit. No rational
solution or saturation replaces the integer equation.

### Item2: complete ambiguity

The original finite-norm argument is valid: if (S-I)x=k mu and S has
finite order h, applying its norm gives0=h k mu. The chosen receiver
uses the equally integral pairing with mu, which gives k=0. The full
orbit-sum basis and inverse extraction of a common coefficient prove
the lattice statement in both directions. The norm verification stays
in post-exposure checks; it is not counted as another fresh proof.

### Item3: actual global line, including degenerate section pairs

The generic divisor P-O-(P-Q)+(-Q) is principal. Its function is the
line through P and -Q divided by the vertical line through P-Q.
The P=Q specialization is x-x(P); P=-Q uses the tangent at P divided
by the vertical line at2P; at P=0 or Q=0 use1. These choices include
all degeneracies in the target scope. Multiplication by the canonical
vertical sections produces a rational section of J_D. Zero component
degrees put its divisor in Z mu at each fibre, and mu0=1 makes the
whole-fibre coefficient integral. Reciprocal functions and sections
give the exact inverse line map. Restriction to O proves injectivity
of base pullback. The original global sufficiency assertion stands.

### Item4: telescope, base degree and narrow translation

The h arrows telescope by evaluation of adjacent line and dual-line
factors, retaining all canonical sections. If hQ is narrow, its actual
translation fixes each component divisor, so T_(hQ)D=D. This gives
exactly D.VC5, including its inverse. Applying the admitted narrow
case and restricting to O also verifies the original degree argument.
The chosen main degree proof is the direct height-cancellation argument
in receiver item2; the telescope is retained in item5 for the actual
period map rather than as a second main degree proof.

### Items5--6: h-fold contraction and D.VC8

Off the singular fibres, I_D(p,v)=(p,v sigma_D(p)) and its reciprocal
inverse conjugate the arrow by the full section ratio. The arrow covers
-Q. A unit ratio constant on each compact elliptic fibre is a base
unit, retained with q^w. The h-fold iterate has long deck generator
h gamma and weights hw. The period inclusion S_h=diag(1,1,1,h) has
inverse on its image obtained by dividing its last coordinate by h;
T_i S_h=S_h T_(i,h) is D.VC8. It is not claimed to be a unimodular map
of one fixed lattice or a cover of a completed cap.

The receiver additionally supplies L,L inverse,T_i,T_i inverse on the
actual transported periods. A least-denominator solution z_G of
(B-I)z_G=g has denominator equal to the component order, dividing d0.
Thus d0|ab makes the central coefficient integral. At multiplicative
sites z_G=(kappa/nu)v with u^tJv=1 supplies this least denominator;
fixed-vector freedom leaves the scalar r_i z_G unchanged. The actual
positive roof retains the constant scalar and all units; its normalized
integral and strictly increasing inverse fix the circle coordinate.
The original assertions are valid at precisely this punctured scope.

### Item7: all cyclic local pairs

The moment map on the degree-zero cycle lattice is sum i*h_i mod n.
The receiver supplies its integral inverse by successive differences,
including n=1 and the two parallel edges at n=2. The orbit moment for
a q-invariant degree is (n/gcd(n,q)) sum j*m_j mod n. Therefore the
criterion is n|pq. An explicit invariant multidegree and Laplacian
inverse construct d for every soluble pair. All signed integers reduce
to these actual component residues. This proves the original finite
local assertion by maps, not only by a Smith-factor list.

### Item8: all additive local pairs and literal star markings

This auxiliary covers every p,q in each component group, beyond the
fresh proof's global necessity route. It is now proved directly using
d_q-d_0=contr(p,q) and the discriminant pairing. The generator pairings
are1/2,2/3,3/2,4/3,5/4,7/4 for III,IV,III*,IV*,I1*,I3* respectively.
Their numerators are units modulo the component order. Prime orders
force p=0 or q=0, where d=0 works. The only further odd-star pair is
(2,2): in the near-leaf ordering d=e_1 gives invariant degree
-e_0-e_1+e_2. The component-group action and unique graph automorphism
give the actual permutations. The exact new-to-old orders are
(0,1,4,5,2,3) for I1* and(0,1,4,5,6,7,2,3) for I3*, with their
inverse permutations. Thus the original local criterion D.VC6 stands.

The new150-line local validator computes the full integer transformations
and inverse matrices for all227 local pairs. The43-line supplement
reproduces every one of the135 insoluble historical obstruction values
using the disclosed generic Smith convention. All historical particular
solutions, multidegrees and full kernels are checked. These are
post-exposure checks; the historical target program was not executed.

### Item9: all21 profiles and all5696 residues

The defining profile data give unit section classes and component-order
least common multiple d0. In fact the nontrivial orders in each profile
are pairwise coprime; receiver item4 prints them. The raw(B,g) Smith
calculation gives the exact component order and an integer preimage of
that order times g for all82 sites. Consequently the local criteria are
equivalent to d0|ab for all signed multiples. The new check enumerates
all5696 residue pairs, comparing every historical global field and the
16 additional positive height-one initial pairs. No finite parameter
sampling substitutes for the unbounded residue proof.

### Item10: the I4 example, extra initial pairs and scope of caps

At p=q=2, C(-e_0)+(e_2-e_0)=(1,-1,1,-1). The two orbit sums
e_0+e_2 and e_1+e_3 give the whole ambiguity, with inverse coefficient
reading. The extra profiles are exactly OS45,46,50,55 with the listed
variants; their16 height-one rows are explicitly printed in the
receiver. Corrected original-cap degrees may be nonprimitive and
permuted. This proof makes no additional original-cap identification.
The original scope statement is respected, and the all-Mumford
examples are proved from their actual toric charts instead.

### Item11: D.VC9 and D.VC10, with the full frame transport

All five elliptic matrices and cocycles in D.VC9 agree literally with
the defining raw fixture. The original D.VC10 uses the raw positive
component +kappa=3. The fresh Tate valuation uses the negative component.
The exact involution is j->-j mod8, with F inverse=F, FCF=C and
F shift(q) F=shift(-q). It transports the coefficient and degree columns.

Subtracting the fresh physical d from the reflected original d gives

    E_(2,4)=(-1,0,-1,-1,-1,0,-1,-1),
    E_(4,2)=(-1,0,-1,0,-1,0,-1,0).

These are invariant under shifts4 and2 respectively. Thus D.VC10 is
valid in its raw convention. The original pronoun after that table is
made explicit: its multidegree column, not an arbitrarily chosen
coefficient column, is invariant. The punctured tensor map I_E and
its reciprocal transport the arrow and every unit. Along O,
sigma_E=q^(-1)u(q), so the angular displacement is
-t+arg u(q)/(2pi) and the meridian shear is -delta, with inverse +delta.
The receiver defines each cap origin through the proved punctured map
and transports the affine gluing accordingly. It proves the fillings
for the actual original D.VC10 choices. It does not identify two spaces
obtained by changing D while keeping an untransported boundary origin.
Neither the vector difference nor the shear is a theorem refutation.

### Item12: every local Mumford kernel and the common exterior

The two pairs have gcd(a,b)=2. At every weight-zero site the primitive
rank-one off-diagonal block is factored using gcd(nu,a*kappa), with
explicit Bezout matrices C_S,C_L and inverses. These act by character
monomials and period multiplier products on the actual charts. Flat
line gauges and the pole-translation isotopy have reciprocal/additive
inverses. The resulting nodal ruled core has the displayed integral
specialization and sections. At the selected I1 site C_+ and its inverse
give I+E12+E34 in the prescribed short lattice; its XYZ=q charts and
conductor complex give the primitive two-column fibre kernel, all four
degree-two quotient coordinates and an integral section. Actual fixed
circles sweeping the origin discs give the fixed-normal bounding chains.

Thus the old local-kernel transfer is valid for these exact periods.
The receiver proves the necessary maps here, retaining all units and
affine markings. The common exterior uses the admitted LI bar formula,
with the full six-coordinate fibre presentation so that its Z/2
coinvariant is retained. No natural-row quotient shortcut is used.

### Item13: full fundamental group and exact historical range

The historical program's range is exactly two(a,b) pairs, four selected
I1 sites and e=±1. The new computation supplies the six primitive
vanishing vectors and an integer right inverse onto the nongamma
fibre Z3 for every geometric choice. In the actual semidirect product,
their normal closure kills that entire abelian normal fibre subgroup.
The singular peripheral words bound the stated origin discs and the
ordinary relation is gamma^e. Thus the original pi1 conclusion stands
for all16, with the full nonabelian presentation accounted for.

Every field of the two historical JSON files has been compared,
including the H1 matrices, local cap labels, section residues, zero
position, clutch sign, corrections, kernels and homology metadata.
No historical target program execution is claimed.

### Item14: 70 relations, relative rank, Euler characteristic and duality

The old23×70 matrix is valid. The fresh23×59 matrix is related to it
by the actual Nielsen base-word map and its inverse. The graph map Q
is integral unimodular; the central fibre correction gives

    M=[[I6,C_o E_o K_old],[0,Q]],
    M inverse=[[I6,-C_o E_o K_old Q inverse],[0,Q inverse]].

The new validator retains integer relation maps C,D satisfying
B_new C=M B_old and B_old D=M inverse B_new. These make the quotient
maps induced by M and M inverse well-defined and inverse. C,D are not
asserted to be inverse on free modules of different ranks. Six zero
ordinary fibre columns and five redundant positive-cap columns account
for the difference11. Every one of the16 old matrices and its literal
Smith factors1^22,b is reconstructed; the new factors agree through
these actual maps rather than a group-order inference.

The old finite-first exterior H1=Z5 and its five whole-fibre classes
are confirmed from the literal9×25 integer matrix. The receiver proves
the full relative result by the map

    (t_o,t_0,...,t_4)->(e*t_o,-t_o+t_0,...,-t_o+t_4),
    t_o=y_gamma/e, t_i=y_i+y_gamma/e.

The two peripheral sign changes identify this with the exact matrix
printed by the fresh program. This is an integral inverse, proving the
relative kernel is zero. The four rank-one caps contribute Euler0,
the selected primitive triangular cap contributes2, and all other
pieces contribute0. The retained H2 generator and quotient map,
Bockstein into H3, linking inverse, integral duality and Euler equation
give every group in D.VC7. No original conclusion changes.

### Following audit paragraph

All its assertions are settled:227 local pairs,5696 residue pairs,
82 actual component orders and16 additional initial rows. The exact
historical audit source was retrieved and read. Its source-written
JSON path returned404; the actual failure is retained and no missing
output is invented. The new local and literal-obstruction validators
check the entire claimed finite scope, while the symbolic and geometric
proofs establish the parameter-unbounded conclusions. The paragraph is
moved inside the single receiving proof, with no unnumbered tail.

## 4. Exact mathematical morphisms retained in the receiver

The following are all genuine inverse statements at their stated scope:

* -S inverse and -S between the two component equations; orbit sums and
  representative coefficients between the invariant lattice and Z^rho.
* The explicit cycle-Laplacian inverse modulo its whole-fibre constant.
* Group-law functions, canonical vertical sections and reciprocal maps
  on J_D, including the zero/tangent/vertical degeneracies.
* I_D and I_D inverse, L and L inverse on the transported period lattice,
  T_i and T_i inverse, and S_h inverse on its finite-index image.
* Raw-to-Tate reflection F=F inverse, actual divisor tensor map I_E,
  its reciprocal, and the -delta/+delta peripheral shear.
* C_S,C_L,C_+ and their matrix/character inverses on the actual cap charts;
  fibre specialization with the displayed integral sections and kernels.
* The bar prism/polygon section and its projection/subtraction inverse;
  signed central lifts and inverse maps, including the ordinary word.
* The ordinary boundary map(x,tau) and inverse, retaining v=-e gamma.
* Tracked Smith quotient[z]->(Uz)_23 mod b and inverse[U inverse e_23].
* Nielsen word maps, Q/Q inverse and M/M inverse; the two relation
  inclusions prove the quotient maps are inverse.
* The relative six-disc map and its explicit integer inverse for both
  signs e, followed by the Bockstein/linking torsion identification.

The 70/59 free relation modules have different ranks; the exact inverse
assertion is for their presented quotients through M, as proved by the
two displayed relation inclusions. The logarithmic h-cover inverse is
on its image, and no cover of a completed cap is claimed. These scope
statements follow from the maps themselves.

## 5. Historical retrieval and independent validation

The pinned repository commit is
`a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7`. The exact raw base URL is
https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/ .
Every fetched original is preserved byte-for-byte in this receiving
lane, with the S6_SERIES_PUBLISH prefix. The three target source hashes
are:

* code/III/root_vertical_corrections.py,160 lines,7168 bytes:
  db309494e50559a43d52fec581c425c8c237a46702b3b5d81c642d199cd645c2.
* code/III/fourfolds_corrected_Mumford_examples.py,60 lines,3055 bytes:
  47c545dae8046314ab98ef8d319bae491e4c82f0394f37a1392e23c294fdb205.
* code/V/replay_chains/code/fourfolds_vertical_correction_audit.py,
  82 lines,4713 bytes:
  c6169b7ed538904a2e905ecdc8b10cfc4494a761e37c14556c6d2c7123d3b207.

The available root_vertical_corrections.json has8959 lines,134080 bytes,
SHA ae403a67929573c84040ab5c2c9402be11ad25c3a3d11003e789392db7cff7af.
The available fourfolds_corrected_Mumford_examples.json has45186 lines,
546851 bytes, SHA e8e6dc85bb65f8c3d3b13e19ee4f2dfe3b0ec53e7dacef2fcc7031ff443c4af4.
Their exact record paths are in the retained retrieval streams. The
source-written audit JSON request returned404. No historical stdout or
absent audit output is claimed. Historical programs were inspected,
not executed; there was no broad import of their autorun bodies.

Strictly needed helper files are preserved but only the exact named
definitions and line intervals listed in post-exposure Section8 were
read. Two bounded extract files preserve those definitions. The small
rankone helper metadata spill is disclosed there; it concerns already
admitted finite examples, was unused, and exposed no LT/LU history.

The three new validators preserve the actual source, separate stdout
and stderr, and the full exact matrices. The complete direct lossless
reader preserves742 matrices and481 vectors and reconstructs every
627+37+138 stdout line, every scalar and ordering field, both historical
JSON outputs and the new relation JSON byte-identically. All2038 lines
of that canonical reading form were read. This is lossless reading of
the full mathematical content; it does not claim manual display of
every repeated pretty-printed JSON byte. The optional second reader
has a proved byte-for-byte inverse to the first, with its own successful
actual streams; no second whole manual reading is claimed.

The complete execution table, exact timestamps, all limitations, the
transient read-only transport diagnostic and final receiver edits are
in post-exposure Section9. No unknown source or stream was reconstructed.

## 6. Primary source and admitted-input scopes

The source is Matthias Schuett and Tetsuji Shioda, Elliptic surfaces,
arXiv:0907.0298v3,9 July2010, https://arxiv.org/pdf/0907.0298v3 .
The exact retained PDF is outside W, with SHA256
eeac47d53b52e96a1d2457a131dcce474332dd6b226e4dcd944575e995aa44b1.
Root visually read all of printed25,32--34,50--52: affine component
graphs, component groups and section translation, narrow subgroup,
height formula and the negative inverse-Cartan correction. This lane
read root's whole exact primary-scope note; it does not claim a new
visual reading of those pages in this LS continuation. The notes do
not transfer unused statements from those pages into the proof.

The fresh input section records the whole admitted KT and LI reads,
the exact bounded KM/KQ/KO and admitted LJ cap-map passages, the raw
fixture, and the whole190-line newly written LN symbolic product source
and all89 output lines. The last computation is attributed and was not
rerun here. The clean LT statement and root's LU fresh cone notes were
read only for the separately disclosed support question; they are not
unproved premises for the16 all-Mumford spaces. Their originals and
historical target bodies remained closed in this lane.

## 7. Repairs, permanent identities, and remaining publication scope

No theorem clause or original numerical group assignment is refuted.
The D.VC10 coordinate difference and the70/59 relation difference each
have explicit inverse comparisons. No D25 or D27 event is proposed.
The local defect proposals record the permutation/marking clarification,
the explicit finite and relative proof replacing off-text dependencies,
and the removal of the orphan audit paragraph. These are bounded
repairs, not a new claim about other statements or a whole-paper pass.

All permanent labels, hypertargets and display tags are retained:
maps:src:D.2.50/tag02LS and D.VC1/026E, D.VC2/026G, D.VC3/026H,
D.VC4/026I, D.VC5/026J, D.VC6/026K, D.VC7/026L, D.VC8/026M,
D.VC9/026N, D.VC10/026F. The exact statement and proof-plus-following-
audit guards are separate. The receiving proof uses ordinary enumerate
and includes the computational auxiliary before its sole endproof.

Automatic equation numbering and other D19 publication work, navigation
headers and D10 apparatus, consolidated program-citation form and other
unit-level prose cleanup remain open. This packet does not claim a
whole-PDF read, successful full build, final page-number check or
publication-unit closure. Root alone applies canonical changes and
records admission. All local events share evidence group
publish:c7:III:02LS; their scopes do not multiply independent proof credit.
'''
comparison_path = lane / f'{prefix}_comparison.md'
assert not comparison_path.exists()
comparison_path.write_text(comparison, newline='\n')
assert sha256(receiver.read_bytes()).hexdigest() == '51e26023340cbb59099c02bacdd2db510caba3262c0d5b1a5fa079b16d9e10b2'
assert sha256(fresh.read_bytes()).hexdigest() == 'ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d'
print('COMPLETE', datetime.now(timezone.utc).isoformat())
for path in (backup, post, comparison_path, diffpath):
    data = path.read_bytes()
    print('FILE', path.relative_to(W), 'LINES', len(data.splitlines()),
          'BYTES', len(data), 'SHA256', sha256(data).hexdigest())
print('SCOPE local comparison notes only; stable receiver and frozen fresh unchanged; no canonical or global mutation.')
