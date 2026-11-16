"""Record the actual UN69--74 source, execution and rendered-page audits."""
from pathlib import Path
from datetime import datetime, timezone
import shutil

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
report = root / 'S6_03_CDP_report.md'
backup = root / 'records/versions/report_before_UN69_74_integration_20261115.md'
assert not backup.exists()
shutil.copy2(report, backup)
record = f'''# Integration and visual audit of UN69--74

Recorded {stamp}. The single next hourly checkpoint is due at
2026-11-16 00:36 UTC. This record creates no checkpoint.

UN69 has full root, D and E source audits. Its actual surface maps,
coefficient-one blowdown comparison, closed maximum plateau, transported
sphere of square minus two and strict-height ascent were all checked.
Root reran code/A_nonminimal_maxima.py: PASS, including 417 finite
incidence records, in build/root_UN69_code_rerun.out.

UN70 has full root, A and D source audits. The contractions are explicitly
surface morphisms until the separate ambient statements are applied.
The marked elliptic curve is preserved; the equivariant ruled reduction
retains every lifted section, and the trace argument splits the additive
torsor. The actual fixed-Jacobian elliptic map aligns all surviving
boundary components. Root execution passed 2584 fibre states, 210
discrepancy records and 90 square comparisons.

UN71 has full root, A and E source audits, including the primary
Gross--Siebert statements and their needed proofs. Root read Theorems
4.14, 5.2 and 5.4, Definition 4.3 and Remark 5.6 in arXiv:math/0309070,
and the exact units-to-residues directed-system comparison. The angular
lattice injection uses the nonzero actual residue period. The complete
translation-affine cover, every shear, central freeness, uniform
logarithmic bounds and barycentric compactness were checked. Root reran
code/D_toric_gluing.py successfully. The actual central log structure,
including both triple-point factors in its normal product line, is
retained; no uniqueness of every higher-order degeneration germ is
asserted.

UN72 has full root, D and E source audits. It classifies every full
reduced SNC fibre without triple points, with no minimality assumption,
by actual ordinary contractions and the recorded inverse blowups. The
rational-edge and higher-genus-edge procedures terminate by removing an
actual component. The higher-genus ascent uses UN70 to exclude an
elliptic exit. A'Campo and the proved all-elliptic theorem identify the
remaining core. The exact centre normal extensions and compact maps are
retained. Root reran code/A_no_triple_reconstruction.py: PASS for 2016
records, including 110 zero balances, and the symbolic coordinate and
Jacobian identities.

UN73 has full root, A and E source audits. Every marked central toric log
space in UN71 and its conjugate occur at the two ends of one compact
family over the projective line. Root checked the real rank-four period
determinant, finite-index angular lattice, the exact exponential maps at
both ends, the sign in the infinity frame and the base rescalings that
recover the prescribed constants. Root reran
code/D_compact_toric_gluing.py: PASS, 588 positivity and 936 finite
angular/base comparisons. E supplied an independent symbolic determinant
calculation, and A independently executed the determinant identity.

The first expanded build, build/root_build_2342.out, reported one TeX
error: an undefined N macro in UN71. The prior source is preserved in
records/versions/UN71_before_N_macro_repair_20261115.tex. Root replaced
that occurrence by the explicit mathbb N. The next build,
build/root_build_2347.out, contains 226 numbered statements and 466
pages through UN73. All four stages exited zero. The final log has zero
TeX errors, zero overfull boxes, zero unresolved references and zero
missing glyphs. The PDF and render outputs from preceding builds remain
recoverable in build/history.

Root actually inspected the rendered page images 105, 106, 261, 263,
278, 281, 349 and 351, in four two-image calls. The period determinant,
both endpoint frames, the no-triple theorem and reconstruction, the
maximum/sphere argument, the ruled splitting, the log residue comparison
and the quotient properness argument are legible, with no clipping or
overlap. An earlier eight-image call had truncated its output and was
not counted as visual inspection. The render log is
build/render_qa_2347.out and its manifest has 466 pages.

UN74 was then read in full by root and independently by E. Both audits
pass. The principal full fibre gives the necessary and sufficient
ordinary-contraction condition m_T=m_P. The Cartier pullback coefficient
and first normal term prove the parent is smooth at every centre point;
the simple restriction of each other component to the centre proves its
smoothness and transversality. The exact weighted chart is
p=xy, q=z, r=x and f=x^m y^m z^n. The actual normal extension, root line,
canonical-generator-shift comparison, derivative map in the reduced
case, local-maximum splitting and compact gluing all check. Root reran
code/A_ruled_crossing_contraction.py: PASS for 3811 weighted comparisons
and 3905 negative-degree splitting records, with exact Jacobian and
Euler identities. Output: build/root_UN74_code_rerun.out. UN74 is still
source-only relative to the verified 466-page PDF.

The unresolved C.2 clause remains the unrestricted geometric
classification of reducible zero-Euler supports, including arbitrary
triples, weights and non-SNC assembly. Active proofs concern exact
Kulikov modification records and weighted equivariant roots. The
high-canonical Hopf point-blowup reduction still lacks a complete
termination proof; it is not promoted to a numbered assertion.
'''
(root / 'records/root_integration_2354.md').write_text(record)
text = report.read_text()
text = text.replace('C.2.UN.1–68; C.2.UN.69, C.2.UN.70, C.2.UN.71 (source)',
                    'C.2.UN.1–73; C.2.UN.74 (source)')
needle = 'The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
replacement = ('UN69 handles nonminimal canonical maxima and every rational double curve without triple points. '
               'UN70 aligns every isolated torsion-normal elliptic boundary with its actual elliptic minimal model. '
               'UN71 classifies the positive canonical-flat central log spaces by their full periodic unimodular triangulation and torus gluing constants. '
               'UN72 gives the complete actual ordinary-blowup reconstruction for every full reduced SNC fibre without triple points, with its exact zero-Euler balance. '
               'UN73 realizes every UN71 central log space and its conjugate in one compact family over P1. '
               'The source-audited UN74 extends ordinary curve contraction through the specified triple-point configuration, retaining all multiplicities. '
               + needle)
assert text.count(needle) == 1
text = text.replace(needle, replacement)
report.write_text(text + '\n\n' + record)
print('Recorded UN69--74 audits; verified PDF cutoff UN73, 226 statements, 466 pages.')
print('Actually inspected pages: 105,106,261,263,278,281,349,351; no clipping or overlap.')
print('Preserved the previous report; next hourly checkpoint remains 00:36 UTC.')
