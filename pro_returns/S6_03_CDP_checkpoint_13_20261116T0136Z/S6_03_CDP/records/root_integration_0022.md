# Root audits of the weighted and finite-modification branches

Recorded 2026-11-16T00:22:14.627472+00:00. These are source and execution audits; the current
verified PDF still has 226 statements and 466 pages through UN73.
The next single hourly checkpoint and progress review are due00:36UTC.

UN74 has full root, D and E source audits, all PASS, and the independent
root execution recorded in root_integration_2354.md.

UN75 has full root, A and E source audits, all PASS. Root read the entire
corrected source and independently executed code/D_kulikov_records.py.
Its output is build/root_UN75_code_rerun.out: 3855 canonical/full-weight
comparisons, 1330 finite-level potentials, 28 complete records with269
removals, 651 curve/triple maps and 2025 zero-Euler comparisons passed.
The symbolic Jacobians, overlap cancellation, type-I/type-II defects
and three-axis normal-cone fibre were checked exactly.

The root source audit specifically required and received the proper
composite-graph argument for a compact Hopf-birational divisor. A generic
complete exceptional rational fibre maps nonconstantly back to the old
component, or a compact projective point fibre has the whole component
as its closed birational image. The contradiction uses the actual global
component, not the birational type of a local analytic patch. The source
also now refines its charts to relatively compact subanalytic pieces;
the finite Euler subdivisions and their inverse images have the required
finite triangulations. Arbitrary open-cover Euler numbers are not used.

The primary Kulikov1981 four-page proof was read in full, including its
two-open-set definition, Theorem1prime, Sections8--10 finite-level game,
and all appendix corrections. Root read Kulikov1977's exact restored
overlaps in4.10.8--9, local atlas in4.11--4.14.5, selection step4.16.2
and endpoint argument4.17. These actual graph and overlap maps give the
global bimeromorphic endpoint comparison. The theorem retains this
finite atlas; it asserts no global ordinary-blowup factorization.

UN76 has full root, A and D source audits, all PASS. The promoted file
is sections/part_C2_weighted_flat_toric.tex; the complete draft remains
recoverable beside it. Root checked every formula C.WF.1--28: normalized
root lattices, height-one rays, unit-invariant toroidal subdivision,
global component labels, the exact central finite monomial cocycle,
the residue character and both original-stratum Euler comparisons.
The compact construction was checked through the actual real lattice
change, finite action equations, simultaneous shifts of B and a0,
real-linear period iteration, strict determinant, both exponential
frames, reflected infinity fan, torus inversion, and the finite POINT
inertia gauge. The last gauge fixes the root coordinate and identifies
the original coarse invariant ring, proving smoothness of the quotient.

The weighted generator normalization was explicitly corrected during
the audit. Minimum canonical order zero is valid for a full reduced
fibre, but was not inferred for weighted fibres. Instead primitivity
of the direct-image generator gives0<lambda<=1; the exact residue
character makes lambda half-integral. Thus lambda is1 or1/2, and all
weights are even in the latter case. The old open component strata
have finite unramified toric covers; for a double stratum a boundary
curve dominating it has the full C-star complement. Each positive-
dimensional original stratum has Euler zero. Therefore e(S) equals
the positive number of ORIGINAL triple points. This is a proved
exclusion from the zero-Euler problem for the entire weighted class.

Root reran code/E_weighted_flat_toric.py independently. Its exact
certificates passed648 old rays,1851 height-one points,1923 cones,
1974 valuations,3084 invariant character cosets,3172 primitive-generator
comparisons,420 inertia-averaging jets,42 finite-action iterations and
the symbolic determinant and endpoint identities. The saved root output
is build/root_UN76_code_rerun.out. The compact occurrence preserves
the marked reduced log support and every full multiplicity. The proof
does not identify arbitrary higher thickening or whole-germ jets with
the new compact family's jets. Exact original germ recovery instead
uses the original normalization, coarsening and quotient diagram.

UN78 has full root and E source audits, both PASS at this record.
Root checked the actual embedded resolution, labelled toric root
subdivision, canonical interpolation and minimum, conjugated finite
BIRATIONAL action, and the inverse-record-before-quotient comparison.
The source retains the actual endpoint family. It does not invoke an
equivariant Kulikov modification or quotient a central birational
action before regularizing it. The condition is attached to the given
resolution/root record: every strict Hopf root component has the
minimum ratio (k_i+1)/m_i.

Root independently verified the simplex determinant and cyclic sheet
count, then executed code/D_rooted_kulikov.py. PASS:3330 simplex volumes,
3330 Burnside averages,216 Pick triangles,49977 canonical ray comparisons,
100 double-chain Euler values,1120 toric root examples and6426 zero
balances, including the symbolic original/root/core reconstruction.
Output: build/root_UN78_code_rerun.out. Over an original r-fold stratum
the actual root-resolution fibre Euler is N^(r-1)*d^2/product(m_i),
where d is the incident-weight gcd. Together with the exact ordinary
resolution and normal-cone defects this gives the stated original-
support zero criterion. Root caught the plain-text left delimiter in
C.RK.10; D corrected it before compilation, with the earlier draft
retained in the work record. The toroidal gluing and global SNC label
precisions have also been incorporated.

The reserved UN77 is still being written and is not counted here as
proved. Its current target is actual minimalization of globally maximal
Hopf components through finite ruled-removal blocks and the explicit
sigma-atlas cleanup. No holomorphic pruning of an arbitrary Hopf-leaf
neighbourhood has been established. Root reread UN60 and the passage
at C.PT.11 in UN61: their necessity comparison for an arbitrary original
family uses smooth collars; the compact converse constructs a family
from its complete central torsors. They are not silently used to
contract an arbitrary original smoothing germ.

Additional searches used the exact Nishiguchi1983 and Ueno1983 titles,
non-Kahler torus degenerations, Hopf components and Kulikov modifications,
and Hopf-surface neighbourhoods in threefolds. The old Nishiguchi
Proc.Japan Acad. DOI still failed to open. The Hokkaido proceedings
source was opened, but its Ueno citation is not a substitute for the
unretrieved article. A primary IMRN2024 result on Hopf transforms was
located; its full publisher page failed to fetch, so its indexed
description is not used to justify a neighbourhood theorem here.
No priority claim is made.

The sole unfinished prompt clause remains the unrestricted geometric
classification of all reducible zero-Euler supports. The new results
settle exact additional branches and original-support comparisons;
they do not close the high-Hopf, arbitrary-triple assembly problem.
