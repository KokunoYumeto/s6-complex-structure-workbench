"""Preserve and correct the premature global source-zero attachment invocation."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
utc = datetime.now(timezone.utc).isoformat()
prior = root/'code/part3_root/attempts/source_zero_global_attachment_invocation'
prior.mkdir(parents=True, exist_ok=True)
note = root/'notes/part3_source_zero_spin_c_boundary_working.md'
old_note = note.read_text()
assert not (prior/note.name).exists()
shutil.copy2(note, prior/note.name)
old_intro = '''This is a derivation for the regularized complex fourfold of the current
source-zero construction. The source coordinate is the literal new variable
`v`, with the literal base coordinate `T`. Its passage to the old `u,t`
marking is the separate annular-clutch computation in
`part3_source_zero_relative_comparison_working.md`. No value of an old-source
return is assigned here.'''
new_intro = '''**Scope correction.** The characteristic substitutions, mapping-torus
cohomology and relative-product algebra below have passed root and peer
audits. The compact global complex coboundary invoked in the first version
has not been constructed: the collision-to-cap attachment through `v=0`
has a newly identified component-monodromy mismatch. That invocation is
withdrawn and preserved under
`code/part3_root/attempts/source_zero_global_attachment_invocation/`.

The source coordinate remains the literal new `v`, with base coordinate
`T`. The actual punctured family and its mapping-torus boundary exist;
the source-zero local collision quotient and the finite-cap chain pieces
also exist separately. On the E overlap, the executed collision atlas
fixes each label `j mod N`, while the finite cap has the signed cyclic
shift `j -> j+kn mod N`. The full affine origin must be implemented before
these pieces can define a global `W`. The source formula recorded in
SC2--3 is therefore a verified computational input whose application to
that proposed global `W` remains unmade. No new theorem or numerical
return is entered from this note.'''
assert old_note.count(old_intro) == 1
updated = old_note.replace(old_intro, new_intro)
old_start = '''## SC1. The compact coboundary and its actual oriented boundary

Let `W` denote the inverse image of a sufficiently small closed `v` disc in
the smooth complex fourfold constructed in Sections 19--22 of
`part3_source_zero_completion_working.md`, after the relative periodic
regular subdivision in `part3_source_zero_equivariant_resolution_audit.md`.
The protected I/W/E boundaries and the signed finite-cap chain charts give
the specified rescaled family on the punctured disc. Properness of that
map makes `W` compact. The circle boundary lies in the smooth submersion
locus, so its inverse image `M` is smooth and is the actual mapping torus
of the rescaled positive `v` loop. The regular subdivision changes only
the central fibre. In particular it leaves this boundary and its positive
parameter marking literally unchanged.'''
new_start = '''## SC1. The actual oriented mapping-torus boundary

Write `M` for the mapping torus of the actual rescaled positive `v` loop
on a small parameter circle. This uses only the punctured family. The
relative periodic regular subdivision concerns the local collision
piece and preserves its noncentral part. The missing central overlap
identified above prevents invoking a compact global complex fourfold at
this stage. The following boundary calculations concern `M` itself.'''
assert updated.count(old_start) == 1
updated = updated.replace(old_start, new_start)
updated = updated.replace(
    'The almost complex tangent bundle of `W` determines a\nspin-c structure with determinant class `z=c1(TW)`. Its determinant line\nrestricts to a trivial line on `M`, since `H2(M;Z)=0`; a trivialization\ntherefore induces one of those two spin structures.',
    'The verified spin-c formula uses a determinant class `z` whose\nrestriction to `M` vanishes. The computed group `H2(M;Z)=0` supplies\nexactly that boundary vanishing and permits a boundary trivialization,\nwhich induces one of the two spin structures.'
)
updated = updated.replace(
    'Write `j:H4(W,M;Z)->H4(W;Z)` for the natural map. The preceding vanishing',
    'In the verified coboundary formula, the map used for its products is\n`j:H4(W,M;Z)->H4(W;Z)`. The preceding boundary vanishing'
)
updated = updated.replace(
    'The definition applies to the\n`M` just computed.',
    'The boundary cohomology hypotheses are exactly those of\nthe `M` just computed. A global source-zero coboundary is the remaining\nconstruction obligation before applying this formula to its local data.'
)
updated = updated.replace(
    'The forward boundary identification of SC1 and P3F.24 give\n\n`[Phi]=mu_Z28(M)`.',
    'Independently of the unresolved filling, the forward mapping-torus\nidentification in SC1 and P3F.24 gives `[Phi]=mu_Z28(M)`.'
)
updated = updated.replace(
    'The four quantities `Q(z^2,z^2)`, `Q(z^2,c2)`, `Q(c2,c2)`, and\n`sigma(W)` must now be evaluated for the full glued regularized\nfourfold.',
    'First the actual global collision-to-cap attachment must be supplied.\nThe quantities requested by the verified formula are `Q(z^2,z^2)`,\n`Q(z^2,c2)`, `Q(c2,c2)`, and `sigma(W)` of a complete coboundary.\nThe current local pieces do not yet supply those global quantities.'
)
note.write_text(updated)

report_code = root/'code/update_report.py'
source = report_code.read_text()
old = ('The two rank-one residual contractions and signed finite-cap chain maps, '
       'including both logarithmic deck squares, are retained in the normal analytic quotient construction. '
       'The relative barycentric orbit separator and exact integral star-subdivision algorithm now prove '
       'an equivariant regular subdivision preserving the actual I,W,E boundaries. '
       'The finite cone-orbit export and oriented fixed-stratum boundary computation remain active.')
new = ('The two rank-one residual contractions give the local normal collision quotient, and the signed '
       'finite-cap chain maps retain both logarithmic deck squares. The relative barycentric orbit separator '
       'and exact integral star-subdivision algorithm preserve the actual I,W,E boundaries; the two '
       'executed regular fans have 9851 and41902 maximal-cone orbits. Their local fixed charts and '
       'interior/H normal-characteristic residues are computed. A new global attachment check found that '
       'the zero-origin collision E atlas has trivial chain-label monodromy, whereas the finite-cap atlas '
       'has the shift j->j+kn modulo N. The ordinary-origin q1 deck has the inverse shift and has not yet '
       'been implemented in the full collision-to-cap morphism. The previously invoked compact global '
       'complex filling is therefore unproved; its earlier invocation is preserved with a correction. '
       'The verified spin-c characteristic polynomial supplies the required global Chern pairings and '
       'signature only after a complete coboundary is available; no return is assigned from the local sums.')
assert source.count(old) == 2
source = source.replace(old, new)
ast.parse(source)
report_code.write_text(source)

record = {
    'utc': utc,
    'status': 'CORRECTION; global collision-to-cap attachment unproved',
    'preserved_note': str((prior/note.name).relative_to(root)),
    'preserved_sha256': hashlib.sha256(old_note.encode()).hexdigest(),
    'exact_gap': 'The zero-origin E fixed-component local system fixes j modulo N, while the finite cap monodromy shifts j by kn modulo N. The new ordinary coordinate eta has q1 deck v^(-nk), but the executed collision fan used the original V coordinate.',
    'verified_parts_retained': ['local full-unit collision quotient', 'rank-one properness on local sectors', 'relative periodic regularization', 'separate finite-cap chain quotient', 'the two exact local origin/deck squares', 'interior/H normal-characteristic residue computations', 'spin-c polynomial and mapping-torus boundary algebra'],
    'not_established': ['global central collision-to-cap atlas', 'compact complex source-zero coboundary', 'global characteristic values', 'rescaled or original source-zero return'],
    'next_exact_task': 'Derive the full affine source/Cartier overlap and its chain-label monodromy, or construct the real orbit bordism carrying that same deck.',
    'numbered_theorems_changed': [],
    'published_checkpoints_overwritten': False
}
(root/'records/source_zero_global_attachment_correction.json').write_text(json.dumps(record,indent=2)+'\n')
(prior/'correction.json').write_text(json.dumps(record,indent=2)+'\n')
print('Preserved the earlier invocation; corrected working note and live report to the exact attachment gap.')
