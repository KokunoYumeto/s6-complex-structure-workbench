"""Retain late-discovered in-scope carrier proofs and their exact inventory.

The mathematical readings are separately recorded below; this script only
performs the auditable source-to-print operation and does not certify a proof
from a hash or a successful compilation.
"""
from pathlib import Path
import csv, hashlib, json, re
from paper_ii_transform import namespace, common_cleanup

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables'
S = ROOT / 'sources'
W = D / 'work/root'
reader = {'model': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro',
          'date': '2026-11-17', 'reader': '/root'}
metric_source = S / 'overleaf_working_edition/supporting_materials/workbench/research/cusp_sphere_fixed_metric.tex'
retained_source = S / 'workbench/higher_rung_24d_continuation.tex'
metric = metric_source.read_text()
whole = retained_source.read_text()
retained = ''.join(whole.splitlines(keepends=True)[4377:5111])
assert retained.startswith(r'\subsubsection{The retained-angle')
assert r'\label{h24:ret:q2-detected-quotient}' in retained

# The principal theorem is already printed once as MAPS B.3.1. Retain this
# longer proof, all three support statements, and the additional corollary.
main = re.search(r'\\begin\{theorem\}\s*\\label\{h24:ret:main\}.*?\\end\{theorem\}', retained, re.S)
assert main
removed_main = main[0]
retained = retained[:main.start()] + (
    r'\paragraph{The statement proved.} We give the complete expanded proof of '
    r'\cref{maps:src:B.3.1}, including the full differential, the relative '
    r'smoothing and the spin bordism calculation.' + '\n'
) + retained[main.end():]
retained = retained.replace(r'\subsubsection{The retained-angle cusp quotient and its nonzero top-cell class}',
    r'\subsection{Expanded proof of the retained-angle cusp class}')
old = retained[retained.index(r'\paragraph{The exact object.}'):retained.index(r'\paragraph{Original coordinates')]
retained = retained.replace(old, r'''\paragraph{The exact object.}
We use the fixed based smooth identification of the family member $X$ with
$S^6$, its cusp filling, and the complete original toric coordinates of
\cref{mapsI:src:A.1.2}. The native quotient and compact extension are
\cref{wb:cusp-cone-native-descent,wb:cusp-cone-S12-route}.
The local parameter $t$ in the following formulas is the cusp parameter
$q$ of the family convention; $B_0=J$ in the radial metric notation.
All original period terms and native lattices are retained. The
calculation is independent of the angle-forgetting map to $S^3$.

''')
retained = retained.replace(r'\cite{h24:retbib:ConeRoutes}',
                             r'\cref{wb:cusp-cone-native-descent}')
retained = retained.replace(r'\cite[Lemma 4.2(iii)]{h24:retbib:Canonical}',
                             r'\cref{mapsI:src:A.1.2}')
retained = retained.replace(r'\ref{h24:ret:main}', r'\ref{maps:src:B.3.1}')
retained = retained.replace(r'\eqref{h24:ret:eq:main-class}', r'\cref{maps:src:B.3.1}')
retained = retained.replace(r'\begin{proof}[Proof of the theorem]',
                             r'\begin{proof}[Expanded proof of \cref{maps:src:B.3.1}]')
retained = retained.replace('For the intrinsic Lie framing on\n',
    r'The intrinsic Lie-torus calculation is the known computation in \cite[Example~3.8, p.~6]{DebrayGunningham2018Root}; we retain its direct derivation. For the intrinsic Lie framing on'+'\n')
for oldkey, newkey in {
    'h24:retbib:Milnor1965': 'CuspNullMilnor1965',
    'h24:retbib:Hatcher': 'Hatcher2002',
    'h24:retbib:Pontryagin1950': 'Pontryagin1950Root',
    'h24:retbib:Pontryagin1955': 'Pontryagin1955Root',
    'h24:retbib:Johnson': 'Johnson1980Root',
    'h24:retbib:DebrayGunningham': 'DebrayGunningham2018Root',
}.items():
    retained = retained.replace(oldkey, newkey)
retained = retained.replace(r'\begin{lemma}' + '\n',
    r'\begin{lemma}\label{h24:ret:chart-lemma}' + '\n', 1)
retained = retained.replace(r'\begin{lemma}[The exact orientation sign]',
    r'\begin{lemma}[The exact orientation sign]\label{h24:ret:orientation-lemma}', 1)
retained = retained.replace(r'\begin{proposition}' + '\n',
    r'\begin{proposition}\label{h24:ret:framing-proposition}' + '\n', 1)
retained = re.sub(r'^% Staged proof only.*\n|^% Uses the already proved.*\n', '', retained, flags=re.M)

# Namespace only the local labels; explicitly shared labels remain shared.
def namespaced(s):
    s = namespace(s, 'wb')
    for prefix in ['maps:', 'mapsI:', 'wb:']:
        s = s.replace('{wb:' + prefix, '{' + prefix)
        s = s.replace(',wb:' + prefix, ',' + prefix)
    return common_cleanup(s)

metric_print = namespaced(metric)
retained_print = namespaced(retained)
(D / 'editorial/III_late_carriers.tex').write_text(metric_print + '\n' + retained_print)

metric_ids = ['sphere-metric-uniform-collapse', 'sphere-metric-fixed-realization',
              'sphere-metric-scaling-trichotomy', 'sphere-metric-unit-volume',
              'sphere-metric-tangent-scope']
retained_ids = ['h24:ret:chart-lemma', 'h24:ret:orientation-lemma',
                'h24:ret:framing-proposition', 'h24:ret:q2-detected-quotient']
audit = {
 'reader': reader,
 'source_ranges_fully_read': [str(metric_source.relative_to(ROOT)) + ':1–917',
                            str(retained_source.relative_to(ROOT)) + ':4378–5111'],
 'metric_source_sha256': hashlib.sha256(metric.encode()).hexdigest(),
 'retained_source_range_sha256': hashlib.sha256(''.join(whole.splitlines(keepends=True)[4377:5111]).encode()).hexdigest(),
 'metric_derivation': [
  'Uniform continuity on the compact cone-coordinate product gives simultaneous Hausdorff collapse to the smash base point in every compatible fixed metric.',
  'The cone metrics have uniformly bounded positive cross-section tensors and radial Lipschitz coordinate. Their completion has exactly the prescribed vertex; annular interpolation produces fixed compact length metrics.',
  'The collapsed-closed-subspace distance is min(d(x,y),d(x,W)+d(y,W)); the slice first fundamental forms give the exact T/r and ell/r native flat metrics.',
  'The matrix bound sys(Y_T Z²)>=T−C and circle length ell_T give exact Euclidean exhausting slice balls. The full ambient charts have dimensions4 per A factor and3 per B/C factor.',
  'For beta=lambda*r tending to infinity, both the fat wedge and outward chart boundary recede to infinity. Period systoles exclude lifted-deck shortcuts, and uniform tensor bounds on all bounded charts give the stated pointed GH and regular-stratum smooth limits.',
  'For beta→0, finite positive L, or infinity, the marked slice lattices respectively collapse, approach LJZ² in each two-dimensional factor, or have diverging systole. No finite-beta ambient/intrinsic equivalence is inferred.',
  'Unit-volume length factors follow from det(Y_T)^2 and ell_T^4; the limit is the square4-torus.',
  'Products of cones give the iterated-join links. The explicit collar map identifies C with M/boundary(M) as based spaces. Integral Kunneth, Poincare–Lefschetz and the boundary exact sequence give all local-homology ranks in degrees2–5 and8–12, with zeros6–7.',
  'The final moving-sphere metrics are separately assigned quotient metrics. Their midpoint distances diverge, so they cannot be restrictions of a fixed compact ambient metric. The native quotient-systole hypothesis is explicitly retained.'
 ],
 'retained_angle_derivation': [
  'The source range is the exact F24 range singled out by survey_20261112/FINDINGS.md. Its principal statement is already MAPS B3.1; this integration retains the more detailed full argument without printing that statement again.',
  'Using A=ell*B0+R and the original period action, each regular-fibre representative has a unique quotient coordinate u0. The holomorphic unit change and its explicit inverse place the entire native two-torus in one contractible coordinate chart.',
  'Differentiating before restriction gives du=A0 inverse(dv−p0 dell): all dA terms vanish because v−ell p0 is exactly zero on the chosen torus. The normal differential table and determinant−det(A0)|q0|² are independently rederived.',
  'The literal target-coordinate frame differs by a positive constant diagonal matrix. The original bounded period terms are removed only by an explicit homotopy of normal frames, with invertibility throughout.',
  'The entire frame is D(a,b)G0; the two periodic SU2 homotopies contract D in SU3. Comparison with the stable sphere frame is constant up to homotopy on the containing ball.',
  'The two Lie-circle spin structures are nonbounding. The quadratic form x+xy+y has Arf1; the handle argument preserves Arf under spin bordism. The explicit Hopf-frame contraction and product Pontryagin–Thom identify eta².',
  'The based relative smoothing fixes a closed neighborhood of the full inverse image and the source base point, with a positive compact-complement separation bound. Freudenthal in degree n+2 for n>=4 identifies the exact unstable class.',
  'Postcomposition induces a surjective group homomorphism to Z/2, giving exactly the quotient by its kernel and nonvanishing of every odd multiple; no splitting or exact total order is claimed.'
 ],
 'outcome': 'Complete receiving proofs independently read and rederived; no defect found in their stated scope. New retained-angle external citations require their separately recorded original-source gate before final publication.',
 'known_main_statement_route': {'source_label': 'h24:ret:main', 'printed_label': 'maps:src:B.3.1',
                              'removed_repeated_statement': removed_main,
                              'all_additional_proof_text_retained': True},
 'excluded_shared_file_ranges': 'Higher-rung ranges outside4378–5111 are not imported here. They include excluded quaternionic/octonionic/spectral material; the explicitly in-scope F24 proof is retained in full.'
}
(W / 'late_carrier_full_reading.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')

path = D / 'S6_09_PAPERS_inventory.csv'
with path.open(newline='') as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
existing = {(r['source_run'],r['source_id']):r for r in rows}
newrows=[]
all_late_rows=[]
def statement(s, label):
    p=s.index(r'\label{' + label + '}')
    ms=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary)\}',s[:p]))
    m=ms[-1];end=s.index(r'\end{' + m[1] + '}',p)+len(r'\end{' + m[1] + '}')
    return s[m.start():end],m[1]
for sid in metric_ids+retained_ids:
    src=metric_source if sid in metric_ids else retained_source
    content=metric_print if sid in metric_ids else retained_print
    lab='wb:'+sid
    st,env=statement(content,lab)
    r={k:'' for k in fields}
    r.update(source_run='working_edition',source_id=sid,source_file=str(src.relative_to(ROOT)),
       paper='III',printed_label=lab,kind=env.title(),statement_as_printed=st,
       wording_vs_source='Complete original statement and proof retained. Local notation and cross-references normalized; no mathematical strengthening. Unlabelled support statements receive stable labels.',
       recorded_checks=('The source status is not treated as a proof check. Survey C1-6–C1-12 identifies the sphere-carrier programme; actual earlier scope is preserved in the carrier review ledger.' if sid in metric_ids else 'Survey F24 identifies readers C1-3 and H-15 and the exact4378–5107 source range. The present independent full reading is separately recorded; no extra historical check is inferred.'),
       your_check=json.dumps({'reader':reader,'record':'work/root/late_carrier_full_reading.json','scope':'Every source line of the complete receiving proof, all metric/topological or differential/framing steps rederived'},ensure_ascii=False),
       check_outcome=('Passed complete receiving proof; metric and topology inputs are proved in the same paper.' if sid in metric_ids else 'Passed complete receiving proof; final operative original-source closure recorded separately.'),
       found_in_AC26='Exact bounded comparison pending in carrier matrix; original complex construction credited.',
       found_in_E26='Exact bounded comparison pending in carrier matrix; no general novelty claim.',
       found_in_DGKX_v1='Exact bounded comparison pending in carrier matrix; both DGKX versions kept distinct.',
       found_elsewhere='Classical metric-quotient and local-homology methods, or framed/spin bordism methods, are credited at use; precise original citations are checked separately.',
       credited_to='Attached working-edition explicit carrier calculation; classical inputs credited by their operative statements.',
       notes='Late completeness discrepancy found through unresolved source references. Full source retained rather than deleting the reference; work/root/late_carrier_full_reading.json.')
    all_late_rows.append(r)
    if (r['source_run'],sid) not in existing:
        rows.append(r);newrows.append(r)
for r in json.loads((D/'work/cdp_audit/carrier_prerequisite_inventory_2.json').read_text()):
    all_late_rows.append(r)
    if (r['source_run'],r['source_id']) not in existing:
        rows.append(r);newrows.append(r)
assert len(fields)==17
assert len({(r['source_run'],r['source_id']) for r in rows})==len(rows)
with path.open('w',newline='') as f:
    wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(rows)
(W/'late_carrier_inventory_additions.json').write_text(json.dumps(all_late_rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'added':len(newrows),'inventory_rows':len(rows),'metric_results':5,'retained_angle_support_results':4,'native_prerequisites':2}))
