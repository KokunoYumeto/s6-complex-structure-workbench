"""Record the twelfth-hour review and exact post-audit deliverable state."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import shutil
import fitz

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
report = root / 'S6_03_CDP_report.md'
prior = root / 'records/versions/report_before_review12_20261116.md'
assert not prior.exists()
shutil.copy2(report, prior)
rows = list(csv.DictReader((root/'S6_03_CDP_results.csv').open()))
ids = [row['id'] for row in rows]
ordered = '\n'.join(p.read_text() for p in (root/'build/ordered').glob('*.tex'))
numbered = re.findall(r'\\begin\{(?:statement|idstatement)\}\{([^}]+)\}', ordered)
assert len(ids) == len(set(ids)) == len(numbered) == 231
assert set(ids) == set(numbered)
pdf_path = root/'S6_03_CDP_paper.pdf'
pdf = fitz.open(pdf_path)
assert len(pdf) == 489
qa = json.loads((root/'build/visual_qa/manifest.json').read_text())
assert qa['pdf_pages'] == 489
inspected = [247,256,259,335,338,339,341,342,390,392,393]
assert set(inspected) <= set(qa['rendered_pages'])
pdf_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
record = f'''## Twelve-hour progress review — {stamp}

Decision: continue. This is the review for00:36UTC on16November2026,
twelve hours after the12:36UTC start. The work since checkpoint11
directly advances the remaining main clause: the unrestricted geometric
classification and occurrence of reducible zero-Euler torus fibres in C.2.

UN69--73, previously beyond checkpoint11's verified PDF cutoff, are now
fully compiled and audited. They give the nonminimal no-triple reduction,
the actual elliptic-parent surface comparison, the full periodic toric
log gluing classification, ordinary-blowup reconstruction of every full
reduced SNC no-triple fibre, and compact occurrence of the toric log data.

UN74 proves actual ordinary contraction of a ruled component through
the specified triple-point configuration, with every full multiplicity,
normal extension and Euler correction retained. UN75 gives the complete
finite modification-record generation and exact normal-cone Euler balance
for the full reduced Hopf-minimum branch. UN76 treats arbitrary weights
with constant canonical ratio and a triple point: the original open
positive-dimensional strata have Euler zero, so e(S) is the positive
number of original triple points. It also constructs compact occurrence
of the complete marked reduced log data and the full multiplicity cycle.

UN77 gives actual finite minimalization of every globally maximal-order
Hopf component, using exact last-point alternatives, ruled removals and
sigma-atlas cleanup. It retains self-incidence branches on other endpoint
components and retains the actual proper graphs and overlap maps. The
fixed-order bound applies to the retained reduced stages; auxiliary
common Atiyah blowups retain their actual larger orders and multiplicity
two. The old ruled component used to check a cleanup lemma is inspected
on a diagnostic resolution; that resolution is not inserted into the
modification record or the finite-level count.

UN77 has complete root, D and E written-source audits, all PASS. Root
independently reran code/A_maximal_hopf.py:4298 effective-divisor states,
4753 actual smooth/node transitions,41 receiving-normal-degree cases,
900 self-double contradictions,1275 positive-removal-level identities
and5832 finite block-potential comparisons passed. Output is retained
in build/root_UN77_code_rerun.out. The proof includes the exact
point-map induction excluding a positive coefficient-(1,1) edge and
the rational self-double contradiction from its two normal degrees.

UN78 extends the finite-record branch to arbitrary original singularities
and full multiplicities by embedded resolution, normalized cyclic roots,
the actual semistable lattice subdivisions, and explicit descent. The
finite action on the core is retained as a birational action; the record
is reversed before quotient and coarsening. Its original-support formula
is e(S)=e(S0)-Delta_K-R_N-Delta_pi, with each term computed from the actual
maps. Over a resolved r-fold stratum of incident weights m_i and gcd d,
the root-resolution Euler coefficient is N^(r-1)*d^2/product(m_i).

The new intrinsic part C.RK.18--22 removes resolution/root choices from
the branch test. Its finite covers of original normalized components
are glued by the actual local normal-line units, and the map from every
strict central root cover is w_j=s^(N/n_alpha)/g_j. The exact monic
equation and normality extend that map. Every exceptional root cover
comes from a projective exceptional surface and has projective
resolution. The original density |Omega|^2/|f|^(2c) has threshold
tau=min_i(k_i+1)/m_i, by the literal Jacobian change of variables and
the radial integral, including divergence at equality. The required
Hopf-cover ratios equal this intrinsic threshold.

UN78, including this intrinsic addition, has full root, A and E source
audits, all PASS. The root rerun in build/root_UN78_intrinsic_code_rerun.out
passes3330 simplex volumes,3330 cyclic fixed-point averages,216 lattice
triangles,49977 ray/Jacobian comparisons,100 chain Euler calculations,
1120 positive toric examples,6426 zero balances,30 intrinsic root-line
transition algebras and2040 threshold refinements. The pre-addition
source, the literal superseded delimiter and toroidal paragraphs, and
the pre-spacing source are retained under records/versions/UN78_*.

The final current build is build/root_build_0031.out: all four passes
returned zero, with zero TeX errors, zero overfull boxes, zero unresolved
references and zero missing glyphs. The earlier0028 build found one
32.09746pt overflow in C.WF.13. Its full source is retained in
records/versions/UN76_before_WF13_layout_repair_20261116.tex; splitting
the same six definitions over two lines repaired it. The0030 build
also passed;0031 incorporates the final diagnostic-resolution wording.
All earlier PDFs and logs remain under build/history/.

The PDF has231 numbered statements and489 pages. The CSV has exactly231
unique rows, and this script verifies the equality of its ID set with
the compiled statement ID set. PDF SHA256: {pdf_hash}.
Rendering is recorded in build/render_qa_0032.out and the current visual
manifest. Root actually inspected the current images for pages
{','.join(map(str,inspected))}; all are legible, with no overlap or clipping.
The first attempted image390 was recognized as a stale image from the
preceding render, was not counted, and was explicitly regenerated from
the current PDF and then inspected. All112 unused old PNGs were removed
from the current image directory only after byte-comparing them with
their retained copies in build/history/20261116T0027_pre78_visual_qa.
That directory retains the entire prior visual-QA tree. The current
manifest lists293 actually rendered current pages, not489 rendered pages.

The precise remaining gap is the unrestricted assembly and occurrence
of zero-Euler supports with higher-order Hopf components and arbitrary
triple configurations, followed by exact original singularity and weight
descent. UN77 supplies actual maximal-Hopf minimalization, but a remaining
unblown Hopf leaf has not been holomorphically pruned from an arbitrary
given neighbourhood. UN60/61 retain central torsor comparisons and
construct a compact family for their complete classes; their smooth
collar comparison is not silently upgraded to a holomorphic whole-germ
contraction. UN70's exact surface morphism is likewise not used as an
unproved ambient morphism.

The active attacks now examine actual Hopf-neighbourhood surgery with
higher jets retained, local-to-global logarithmic deformation maps,
propagation of a no-triple region through the aligned elliptic parent,
and primary degeneration-classification sources. These are work paths,
not asserted conditional theorems. The report remains INCOMPLETE.
The stopping condition has not been reached: the new statements close
substantial complete branches of the main question.

One checkpoint12 is due00:36UTC. It freezes the full current project and
research support, retains all historical bytes and exact archive recipes,
and reconstructs checkpoint11 to verify its exact byte hash. Earlier
checkpoints remain unchanged. The next review and one hourly checkpoint
are due01:36UTC; no intervening ZIP is to be created.
'''
text = report.read_text()
text = text.replace('C.2.UN.1–73; C.2.UN.74–76, C.2.UN.78 (source)',
                    'C.2.UN.1–78')
text = text.replace('The source-audited UN74 extends', 'UN74 extends')
old = ('UN78 extends the finite generation branch to arbitrary original singularities and multiplicities through an explicit resolution/root condition, transported birational group action, exact coarsening and a computed original-stratum Euler correction. ')
new = ('UN77 gives actual finite minimalization of every globally maximal-order Hopf component, retaining the full modification record and its inverse. '
       'UN78 extends the finite generation branch to arbitrary original singularities and multiplicities through an intrinsic normal-root-cover and integrability-threshold criterion, transported birational group action, exact coarsening and a computed original-stratum Euler correction. ')
assert text.count(old) == 1
report.write_text(text.replace(old,new)+'\n\n'+record)
(root/'records/root_review12.md').write_text(record)
with (root/'records/progress_reviews.md').open('a') as stream:
    stream.write('\n\n'+record)
print('Twelve-hour main-question review: CONTINUE.')
print('231 CSV rows biject compiled statements;489 PDF pages;11 current pages actually inspected.')
print('UN1--78 now compiled. Full report remains INCOMPLETE for unrestricted C.2.')
print('No archive created by this script.')
