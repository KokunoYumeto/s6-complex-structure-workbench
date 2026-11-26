#!/usr/bin/env python3
"""Write the full LU comparison and source/execution scope, not an edit manifest."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_corrected_initial_receiving'
PREFIX='S6_SERIES_PUBLISH_III_02LU_'
receiver=LANE/(PREFIX+'receiving.tex')
assert sha256(receiver.read_bytes()).hexdigest()=='f5eb57e9c7042d6fc4c0f561491cdc90f5241fc6edbe893ad7c7b32462403ea3'
comparison=r'''# 02LU: complete original-to-receiver comparison

25 November 2026. Checker: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode;
the numerical reasoning-effort setting is not separately exposed.
Permanent theorem identity: maps:src:D.2.52 / 02LU.

## 1. Exposure and scope

The root's complete fresh derivation was frozen at 09:19:58 UTC,
before LU's original was released. Its 698 lines have SHA256
c9439d8819da0dbf1ba285687e37a5ddce780e2afafeafb1a9f61297f71b29e1.
The 135-line graph peer review has SHA256
b5412b51db7af05098be7d27fc7240d6a94c0007e7786a2cd1e33e2445d93abe.
That review was attributed scrutiny of the root's derivation, not a
second independent fresh proof. Neither file is changed here.

Individual LU release occurred at 09:21:18.362497 UTC. The complete
56-line statement and 92-line proof were then read, including all six
argument-bearing proof items. The proof is canonical lines 21351--21442,
SHA256 ea81e990ecc1e2776b67c0489febe497ca1c0faf8f70cf732c76816a35e6b5bc
without terminal LF. The separately authorized following gap is exactly
21443--21457, with nonblank auxiliary 21444--21455. It was wholly read
and is the separate deletion guard. The next theorem, beginning 21458,
was not opened. No LS or LT original, old packet or historical algorithm
was opened in this lane. The bounded LS selector statement in Section 5
is attributed to its authorized checker.

The final receiver has 653 lines and SHA256
f5eb57e9c7042d6fc4c0f561491cdc90f5241fc6edbe893ad7c7b32462403ea3.
It is one theorem and one proof. The entire receiver was read back,
including the complete exact diffs of its two small assembly repairs.
The original theorem and equation identities are unchanged: labels
maps:src:D.2.52 and maps:eq:D.CI1; targets tag-02LU and tag-01YN;
printed equation tag D.CI1. The theorem prints its small 02LU tag.

## 2. Every original statement clause

| Original locus or assertion | Result and receiving treatment |
| --- | --- |
| Twenty-one profiles; P=aG,Q=bG with a,b positive and d0 dividing ab | Unchanged. The period calculation proves integrality for every such pair, and the CRT table proves the complete residue scope. |
| Nonnegative whole-fibre weights of total ab/d0 at multiplicative or additional regular sites | Unchanged. Their base divisor and exact unit-valued line maps give the ordered product I. Positive sites use the prescribed Mumford filling; regular logs are additional weight-zero sites. |
| The actual corrected line of LS | Unchanged. Tensor maps, reciprocal inverses, difference-line ratio, forward-arrow direction and base units are written explicitly. LS's fresh local/global derivation is attributed; no LS original was needed. |
| Item (i): marked same-fan rank-one or triangular Mumford caps | Unchanged. The corrected period lattice is transported to the admitted marked cap input; no identification of different fans is inferred from monodromy. |
| Item (ii): every free finite-good additive log; all powers and five columns | Unchanged. The LI/LN sheet, norm and all-five-column maps apply to each literal affine input, without restricting orders or twists. |
| Item (iii): corrected original additive h=1 and unchanged zero-degree additive | Unchanged. The receiver proves the complete h=1 mapping cone, free local groups, primitive area row, both literal normals and their integral bounding chains. The unchanged case retains its admitted relative frame. |
| Item (iv): uncorrected-degree original multiplicative cap as in LN | The mathematical cap choice stands and now explicitly includes its uncorrected line and relative frame. A degree vector alone omits the meridian shear of a whole-fibre change; the exact forward/inverse shear is supplied. |
| Item (v): arbitrarily many regular logs and ordinary integer clutch | Unchanged, for any finite list and every permitted integer. Their power/ordinary relations remain in the full group and bar presentations. |
| Odd stars filled originally | Unchanged. The new non-narrow pair (2,2) has the literal IC8 degree vector and h=1. |
| Canonical corrections admit every positive height-integral pair | Proved in full. The only non-prime additive component orders are the odd-star order-four cases. Their literal permutation and correction are supplied, with coordinate inverses. |
| Newly non-narrow multiplicative positions use Mumford caps | Unchanged. The choice uses the prescribed fan and the actual integral period matrix. |
| Removal of narrowness-OR on initial sections | Unchanged. A new direct CRT calculation gives exactly 45 residue pairs; all lists appear in the proof. |
| No identification of corrected original multiplicative caps or unsupplied h>1 caps | The same mathematical input boundary is retained positively: those caps need their complete relative boundary maps. No additional cap is silently admitted. |
| Exact implementation path and same unbounded data with optional literal d | The algorithm is now stated mathematically; the archive path and implementation evidence move to this comparison/source note. The literal historical guard is narrower than a degree-only reading: original multiplicative inputs require d=0. This is a D26 scope clarification, with the exact map between degree-preserving frames; no mathematical theorem refutation is asserted. |
| Integral correction equation, no rational substitution | Unchanged. The proof gives the exact integer equation, invariant solution lattice and its coefficient inverse. |
| Computation of orbit lengths/h, complete kernel only at h=1 | Unchanged. The full cone maps prove the stated kernel, including every scalar-long correction. |
| Whole-fibre change at a zero-degree original cap outside unsupplied implementation scope | Unchanged in substance. The two frame maps and opposite meridian shears now identify precisely the missing datum. |

The new theorem includes the original proof's number 45 as a numerical
conclusion. This changes its placement, not its value or scope.

## 3. All six original proof items

| Item | Original content | Complete receiving proof and comparison |
| --- | --- | --- |
| 1 | Corrected line, integral period blocks, product I, same bar model | The tensor and difference-line arrows are conjugated explicitly, with reciprocal inverses and retained units. The rational L and L inverse act between transported period lattices; denominator divisibility proves integer T and T inverse. The ordered product follows from the base height term. LI's integral graph kernel, binomial cochains and literal last-boundary word are then applied at their proved general scope. |
| 2 | Marked Mumford maps; full nonsaturated kernels/component meridians; finite and regular Thom data | The receiver specifies the exact dependency inputs: periods, same fan, frames, affine power, all boundary torsion, all component discs and all five columns. It proves that each corrected tuple supplies those inputs. Uncorrected original multiplicative invariance forces p=0 or q=0, giving exactly LN's original-cap scope. |
| 3 | h=1 original additive H1, area kernel, normals and H4 orbit count; unchanged caps | The roof map and inverse, lifted retraction/cylinder homotopy, component automorphism paths and reciprocal line gauges produce the cone. Eta bounds the scalar-long torus; orbit sums and partial sums are inverse H2 maps. The q-cover/transfer calculation gives the primitive integral area row with a Bezout section. Both literal normal tori have explicit integral bounding chains. H1 reads gamma, H3 is free of rank 2rho−1, H4 has rank rho. |
| 4 | Complete pi1 relators and terminating HNF normal closure | The generator path/roof/sheet maps and their inverses prove the complete presentation. The added exact closure argument identifies additive translates with conjugates, and its inverse reads the fibre exponent. Cayley--Hamilton gives inverse stability; finite generation of the union proves termination. HNF changes generators only, preserving the unsaturated subgroup. The remaining power/product relators are still imposed. |
| 5 | Smith cokernel, D.CI1, free relative extension, torsion, Euler and all groups | Tracked Smith maps give quotient generators and bounding chains. A positive nonlogarithmic site proves the finite-first power-disc injection. The full component-disc boundary Gamma is assembled in the actual frames. Solving Mz=Pz-prime with injective P, then closing discs by recorded relation chains, gives an integral section and its inverse. D.CI1 is preserved exactly; the Euler sum and explicit duality/UCT residue maps give all seven groups. |
| 6 | Exactly 45 additional pairs, only odd-star (2,2), h=1 and all-parameter scope | The new raw-period/CRT calculation proves the count and every list, independently of the historical LS certificate. The explicit affine D5/D7 correction, permutation and inverse give IC8 and eta=-e4. The arbitrary-weight/logarithm conclusion then follows from the proved integer maps, not from finite executions. |

No original mathematical conclusion was refuted. The added proofs repair
missing morphisms, inverse maps and quantitative justification. In
particular the invariant-lattice termination statement is true; it is
not classified as a false assertion merely because its original proof
omitted the conjugate-to-exponent inverse.

## 4. Following auxiliary: every numerical and execution assertion

The historical main has 209 lines and its audit has 61; both were read
wholly. The retrieved audit JSON has 9,974,555 bytes. Its exact field
scope is 42 old overlap homology tables, 16 full OS45 examples, 212 full
new-residue executions and 45 full higher-weight/regular-log executions.

The audit source asserts full H2-matrix equality for the 42 old inputs.
Both branches call the same local_lift and graph_data operations and
the same cap routines in the same column order; the source-level
input identity is proved in Section 5. This verifies that assertion
at its 42-input scope. The JSON stores their group tables, not 42 pairs
of matrices. The new program reconstructs all 42 tables and prints
each selected finite affine power. No old stdout or old process exit
status was recovered from the two exact candidate stdout URLs.

For the 16 OS45 examples the old audit checks their formula and stores
full matrices; it does not import a separate LS matrix table. The new
program compares every stored H2 matrix by equality of integer column
lattices, and every H1 matrix after the explicit peripheral-coordinate
map. It also verifies H1=0, H2=H3=Z/b and the trivial vertical quotient.
The ordinary e=±1 relation kills gamma, so their fundamental groups
are trivial. This is the precise accepted meaning of comparison with
the sixteen separately proved LS examples. The phrase suggesting a
second independently stored full-matrix table is corrected in scope.

Every one of the independently derived 45 residue pairs occurs with
every multiplicative zero position and both listed additive patterns.
The 212 stored cases form a multiset: a forced-original odd star can
make two requested patterns the same marked input. The new checker
builds and compares that entire multiset; it does not describe 212
distinct configurations. Every one of the 45 extra records has the
larger P=a+d0, its stated regular positive weight, e=-1 and the recorded
order-two regular logarithm with gamma numerator one.

For all 273 full records the new checker recomputes the integral maps
from the raw defining periods and actual recorded divisors/powers.
All 1,151 local fibre, normal and H1 maps agree as integer lattices.
All H2 relation lattices agree in their common six-fibre plus graph
coordinates, so the ambient identity induces inverse quotient maps.
For H1 the coordinate map is

    P(x,tau_0,...,tau_(N-1))=(x,tau_0-tau_(N-1),...,tau_(N-2)-tau_(N-1)).

Its section S inserts a zero final coordinate, P S=id and
S P-id=-tau_(N-1) times the peripheral-sum vector. The relation lattices
agree under P. The complete homology groups, Euler numbers, relative
free ranks, conjugation and power relations, killed vectors and the
unsaturated normal closures all pass their exact comparisons.

The historical following paragraph is deleted by its own exact guard.
Its mathematical obligations are proved in the receiver; its source
and finite-execution assertions are preserved and qualified here.
No text from the following theorem is part of the replacement.

## 5. Two exact default-input identities and the literal guard

For the 42 overlap inputs P=d0 G is narrow everywhere. The bounded
LS selector check was supplied by its authorized checker: p=0 makes
c=e_(labels[p])-e_(labels[0])=0 and rhs=0; the already authorized LN
integer_solution starts at the zero Smith coordinate vector and returns
V times it. The selected divisor is literally zero, with no kernel term.
The LS source was not opened here. The source hashes and exact helper
locator are recorded in the post-exposure note.

For finite affine powers the two kernel wrappers call the identical
Smith decomposition on DomainMatrix.from_Matrix(A-I).convert_to(ZZ)
and return the same ordered V[:,rank:] without later basis operations.
The fresh integrality wrapper only copies the integer matrix. Its
V-inverse row reader and the historical second-Smith left inverse both
compose with F to I, so they agree on every norm column and candidate v
in im F. Their Hermite H and the vector order*H-inverse*coordinates(v)
are equal. The primitive/divisibility tests are exactly the same gcd
conditions. Both select the first accepted pair in
product(range(-3,4),repeat=2), with m equal to the same local order.
Thus the new overlap inputs implement the same deterministic marked
selector. This conclusion is not drawn from equal abstract groups.
The archive retains no old runtime-version or affine-vector fields for
these 42 records, so separate recovery of absent runtime metadata is
not claimed.

The old original-multiplicative guard rejects every nonzero literal d,
including d=k mu with unchanged multidegree. The new checker extracted
and executed only this AST conditional, on d=0 and on the all-one I8
whole-fibre vector. It observed acceptance and the exact ValueError,
respectively. No historical module or helper was imported or run.
This isolated fragment execution is explicitly part of the record.

For D=kF and F=div(q), the punctured map I_D multiplies by sigma_D,
while the extending map E_D multiplies by q^(-k)sigma_D. Their inverse
composites multiply by q^(-k) and q^k. On the boundary these are
tau -> tau-k delta and tau -> tau+k delta, fixing delta. The mathematical
uncorrected original cap and the routine's literal d=0 input therefore
have precise compatible scope. Equality of degree vectors alone is
never used to identify two caps under an unchanged meridian marking.

## 6. Presentation, checks and held state

The machine dependency header and implementation/archive narrative are
removed from the theorem/proof. One geometric proof retains the entire
mapping-cone, cover, bar, group, integral splitting and counting argument.
The only permanent printed equation tag remains D.CI1; all labels and
hypertargets are unchanged. The separate following-auxiliary replacement
is empty. No new permanent alias is introduced.

All new mathematical executions were read in full, including separate
actual stderr files. The exact run and source scopes are in the source
note and post-exposure derivation. The two new post-release mathematical
programs each ran once successfully; neither failed or was rerun.
The historical guard fragment is the only historical executable code
run in this lane. The frozen LN definition prefix is an attributed new
implementation, not a historical target; its main run was not executed.

Assembly v001 wrote the receiver once. Version v002 changed only the
component-map reference from D.2.20 to the admitted KT label D.2.19.
Version v003 replaced the multi-column split display by aligned,
restored three Bezout accents and removed a four-line closing recap.
All three sources, successful stdout and actual empty stderr are retained
and read. The receiver is held at the hash in Section 1.

The proposals distinguish root's pre-exposure targeted derivation,
the attributed peer reading, the new computations, the bounded archive
checks and this post-exposure reread. No independent-reproof credit is
claimed for this receiving work. No refuted event is proposed, because
the complete theorem and every numerical auxiliary stand with the
specified implementation/relative-marking clarification.

Exact guards, all defect rows and event proposals are staged locally.
Canonical application, required-progress movement, final page concordance,
whole-paper clean build and rendered-page review remain root's later
gates. No global table, frozen fresh file or canonical source was changed.
'''
source=r'''# 02LU: source, computation and exact reading scope

25 November 2026. GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode;
numerical reasoning effort is not separately exposed. This is a check
record for maps:src:D.2.52 / 02LU, with no admission or global mutation.

## 1. Mathematical inputs and exposure

The root's 698-line frozen fresh proof, the 135-line attributed graph
peer note, the clean LU statement and named clean LT statement were
wholly read before original exposure. The peer note records the exact
LS fresh support sections and the complete fresh cone/star computation
scope. The 698-line proof is unchanged at SHA256
c9439d8819da0dbf1ba285687e37a5ddce780e2afafeafb1a9f61297f71b29e1.
The clean LT intake contained its 112-line theorem and no original proof.

Admitted inputs are the marked component/period fixture and KT maps,
LI's full ordered integral bar construction, LK's same-fan noncyclic
cap maps, and LN's all-parameter full local/global maps. LN was admitted
at 09:08:51.122973 UTC. The LS vertical/period/IC8 support was attributed
fresh derivation at LU's freeze. No original LS or LT proof or algorithm
was used. The later bounded p=0 selector confirmation came from the
authorized LS checker and is explicitly attributed below.

LU's original statement, all six proof items, and the exact following
auxiliary were read after release 09:21:18.362497 UTC. The released proof
is canonical 21351--21442, SHA256
ea81e990ecc1e2776b67c0489febe497ca1c0faf8f70cf732c76816a35e6b5bc
without terminal LF. The following gap is exactly 21443--21457, SHA256
965b174a829a975402c49ae4f60c658d14733d57159b0cf0d4ba5a856a06ce53.
The next theorem at 21458 was not opened. No broad canonical search or
new unrelated-original exposure occurred in LU.

## 2. Historical project sources and retrievals

The exact version is repository commit
a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7. The common raw prefix is

https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/

The three exact retrieved paths below are relative to that prefix.

| Path | Result | SHA256 and reading scope |
| --- | --- | --- |
| code/III/manifolds_corrected_initial.py | HTTP 200; 11,211 bytes | 0b3e4521d88814db7b37cb4932d90b5f76fcc2e2290be1c1cac841e970b4ba9e; all 209 source lines read. |
| code/III/manifolds_corrected_initial_audit.py | HTTP 200; 3,488 bytes | 2d0a5cd030a6e224f1598fd3506ca11e34cabc3aa3a8a9335d73ba3dc5ba1675; all 61 source lines read. |
| code/III/manifolds_corrected_initial_audit.json | HTTP 200; 9,974,555 bytes | 9a2a42f64554113985559bf8cbf78c70ae47fcf15461ece7b456a9cbc68722a0; complete data parsed and independently checked, not a manual reading of every serialized line. |

The exact candidate paths code/III/manifolds_corrected_initial_audit.out
and records/manifolds_corrected_initial_audit.out returned HTTP 404.
No old stdout, stderr, process exit or runtime-version record is claimed.

The retained retrieval programs and actual separate streams are
code/S6_SERIES_PUBLISH_c7_lu_historical_fetch_v001.py/.out/.err,
v002 and v003 with the same prefix. Their one successful process runs
were respectively 09:22:38.180887--09:22:46.396420,
09:25:27.253142--09:25:34.077035, and
09:30:26.168896--09:30:42.560141 UTC. The HTTP-404 observations in v003
are retained successful retrieval observations, not hidden failed
mathematical runs. All sources, complete stdout and actual empty stderr
were read. Version v002 also extracted only the authorized auxiliary gap.

At root's explicit request, c7_lu_historical_preserve_v001 copied all
three project evidence bodies byte for byte into this receiving lane's
historical/ directory, with S6_SERIES_PUBLISH_ prefixed filenames.
It ran once successfully at 09:40:46.649965--09:40:46.738250 UTC;
all five stdout lines, source and actual empty stderr were read.
Both copy and original hashes were checked. These are project archive
evidence; no primary published book, paper, extraction or page image is
included in the checkpoint lane.

The historical modules were not imported or rerun. One original
multiplicative guard conditional was extracted by AST and executed in
isolation by the new comparison program; Section 4 records that scope.

## 3. New residue computation

Input: the admitted raw twenty-one-profile geometry
agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json,
SHA256 6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522.
The program derives component orders from actual logarithms, CRT maps
and inverses, complete additional pairs and literal component corrections.
It does not read the old LS count or target output.

code/S6_SERIES_PUBLISH_c7_lu_residue_pairs_v001.py has 155 lines, SHA256
85a6cd491200793a6c2f66a3137ea36a8fb3dde455b28483b8e5ee682a4c72b8.
Its one exit-zero run was 09:28:18.232145--09:28:18.282132 UTC.
All 70 stdout lines were read, including all 45 complete pair records;
stdout SHA256 e6eb7f73c9fc2d1a2fb990e574f1793e718128759d7a4eb3935856b248c423c4.
The separate .err exists and is empty. The saved
S6_SERIES_PUBLISH_III_02LU_additional_residue_pairs_v001.json has SHA256
2a4c557f68879b3a8b680f108de205c49156cdc3cfd741e41682cf497126372e.
Every field is computationally verified; a manual whole-JSON read is
not claimed. No earlier version failed and this run was not repeated.

## 4. New complete archive comparison

code/S6_SERIES_PUBLISH_c7_lu_archived_comparison_v001.py has 290 lines,
SHA256 e92fb2658612d908ed40e433d8bb78ffdb4aa2f91f4cbdc136195825fcf2ebdf.
Its one exit-zero run was 09:40:31.863671--09:42:17.456188 UTC.
All 321 stdout lines and the actual empty separate stderr were read;
stdout SHA256 915d5bda6ad26395ae07b04a8656773f4bb344f9716593c679634c6091c0eaae.
The whole source was read, with a truncated attempted latter-half
readback repeated successfully as bounded lines 146--220 and 221--290.
The saved S6_SERIES_PUBLISH_III_02LU_archived_comparison_v001.json has
SHA256 47720e48c94705f9c325cefe7839abdd37c2e07a8f83085561af7aa9009d0a4c.
No earlier version failed and this execution was not repeated.

It loads only the definitions before the execution boundary of the frozen
independent LN program, hash
9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26.
LN's main 64-case run is not executed. The h=1 cap map is supplied by
LU's new primitive row, fixed normals, gamma quotient and orbit count.
The whole 42 overlap tables and 273 full records are checked, with 1,151
local-map comparisons and all 212 expected new-residue executions as a
multiset. Every extra input, all group tables and both complete relation
lattices are checked under the explicit inverse quotient maps.

Only the exact AST if-statement rejecting nonzero d at an original
multiplicative site is compiled from the historical main. Testing literal
d=0 and the all-one I8 vector gives acceptance and the recorded ValueError.
No historical dependency or full historical function is executed.

The 42 default-input rule uses only already authorized bounded historical
definitions: weighted_profiles lines 1--79, hash
c61db918ba5e4552a9f81c7a4c14e980e5decc317f77496fbc17b214a77d781a,
and rankone_families lines 1--100, hash
f2c80dfca5aac28e17f090e9873bb9b1da52583584a086882a775081bd4458d0.
Their deterministic Smith kernel basis and first-success affine-vector
selection are proved equal to the fresh wrappers in the postnote; no
helper import/execution is used to establish this equality. A narrow
symbol search also returned the already known default_finite call at
weighted_profiles line 126; no surrounding code was read or used.

The authorized LS checker supplied the bounded literal p=0 selector
fact: rhs=0, zero Smith solution vector and hence d=0. Its source hash is
db309494e50559a43d52fec581c425c8c237a46702b3b5d81c642d199cd645c2.
The named integer_solution helper, already read during LN, is lines
27--34 in source hash
f581acf2eaef5e40001ad8b27d6f93be7b213e9b42831853213e6dc227c5d669.
This is attributed source evidence; the LS source was not opened here.

## 5. Writing/readback history and remaining publication gates

The initial 217-line post-exposure note had SHA256
6923c85e7b38d91afa535ea7f53825094a5c8bf916c11d2de662b62da6b40a70.
The retained c7_lu_postnote_inputs_v001 source adds the exact selector
proofs and the explicit H1 composite sign. Its one exit-zero run at
09:53:06.148942--09:53:06.149352 UTC produced the complete read diff,
stdout and actual empty stderr. The final 262-line note hash is
425acc1d1e86ed8e0be553ba3cb23531e08bb5dea4bb2f8be046277499aa1e19.

Assembly sources code/S6_SERIES_PUBLISH_c7_lu_assemble_v001.py,
v002.py and v003.py, their separate .out and .err files, are retained.
All three ran once successfully. Version v001 wrote the complete
657-line draft; v002 changed one citation from KU's D.2.20 to the
actually read KT heading D.2.19; v003 repaired the multiple-alignment
environment, three accents and a closing recap. Their full source and
complete outputs were read. All actual stderr files are empty.
There is no discarded failed assembly or failed mathematical attempt.

The final receiver has 653 lines and SHA256
f5eb57e9c7042d6fc4c0f561491cdc90f5241fc6edbe893ad7c7b32462403ea3.
Its whole mathematical text and each final changed line were read
against the entire released original and every following auxiliary.
The comparison/record writers are retained with their actual streams.
No optional mathematical rerun was needed after the exact input proof.

There is no new external primary theorem citation in the LU receiver.
Its literature is accessed through the already checked internal inputs;
this lane claims no new primary-page reading or new bibliography
verification. A staged bibliography file records that no new entry is
required. In particular no LS source reading is silently inherited as
this checker's own reading.

The full-paper pdfLaTeX build, global reference resolution, final page
concordance and rendered-page inspection are later publication gates.
No staged fragment compilation or rendered-PDF check is claimed here.
The exact guard writer checks only the released blocks, permanent
identities and structural balances; it does not replace those gates.
No canonical manuscript, global CHECK_EVENTS, required-progress row,
frozen fresh proof or prior admitted writer is mutated by this packet.
'''
bib='''% 02LU receiving packet: no new external bibliography entry is required.
% The receiver invokes the checked internal line, period, bar and cap results.
% No new primary-source verification or citation credit is claimed in this lane.
'''
print('START',datetime.now(timezone.utc).isoformat())
for suffix,text in [('comparison.md',comparison),('source_checks.md',source),('staged_bibliography.bib',bib)]:
    p=LANE/(PREFIX+suffix)
    assert not p.exists(),p
    p.write_text(text)
    print('WROTE',p.relative_to(ROOT),'LINES',len(text.splitlines()),'SHA256',sha256(p.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
