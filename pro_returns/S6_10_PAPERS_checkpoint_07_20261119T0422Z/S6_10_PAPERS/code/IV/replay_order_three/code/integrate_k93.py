"""Record the completed root review and integrate the exact infinity formula."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil
import fitz

ROOT = Path(__file__).resolve().parents[1]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
stem = 'part3_source_infinity_closed_formula'
source = ROOT / f'notes/{stem}_working.md'
tex = ROOT / f'notes/{stem}.tex'
pdf = ROOT / 'code/part3_fourfold/k93_standalone.pdf'
cert = ROOT / 'code/part3_fourfold/source_infinity_closed_formula.json'
c = json.loads(cert.read_text())
assert c['status'] == 'PASS' and c['checks'] == 2885
assert c['source_hashes'][str(source.relative_to(ROOT))] == sha(source)
doc = fitz.open(pdf)
assert len(doc) == 5
log = pdf.with_suffix('.log').read_text()
assert not re.search(r'Overfull|Missing character|undefined|LaTeX Error|Rerun to get|Label\(s\) may have changed', log)
outside = []
for i, page in enumerate(doc):
    for w in page.get_text('words'):
        if w[0] < -.5 or w[1] < -.5 or w[2] > page.rect.width+.5 or w[3] > page.rect.height+.5:
            outside.append([i+1, w[4], w[:4]])
assert not outside
qa = {
    'id': 'P3K.93', 'status': 'PASS', 'reviewer': 'root', 'utc': now,
    'page_count': 5, 'pages_directly_reviewed': [1,2,3,4,5],
    'pdf': str(pdf.relative_to(ROOT)), 'pdf_sha256': sha(pdf),
    'source': str(source.relative_to(ROOT)), 'source_sha256': sha(source),
    'tex': str(tex.relative_to(ROOT)), 'tex_sha256': sha(tex),
    'render_directory': 'records/render_k93_standalone',
    'compile_status': 'PASS',
    'compile_findings': 'No overfull boxes, missing glyphs, undefined references, or rerun warnings; every page boundary checked.',
    'visual_findings': [],
    'visual_review': 'Root directly viewed all five final page PNGs. Formula tags, the full prism matrices, induction identities, exact image table and certificate paragraph are legible, with no clipping or collisions. The lowercase calligraphic derivative-array glyph was consistently renamed D and missing word-number spaces corrected; all earlier bytes and renders are preserved.',
    'certificate': str(cert.relative_to(ROOT)), 'exact_checks': 2885,
    'master_modified': False,
}
(ROOT/'records/k93_standalone_visual_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
audit = {
    'id': 'P3K.93', 'status': 'PASS', 'reviewer': 'root', 'utc': now,
    'source_sha256': sha(source), 'tex_sha256': sha(tex),
    'reviewed_sections': ['Statement', 'IC.1', 'IC.2', 'IC.3', 'IC.4', 'IC.5', 'IC.6'],
    'findings': [
        'The literal identical-fan maps preserve x^2+xy+y^2; JPE carries the reflected algorithm and interchanges Q0,Q1 after their common first step.',
        'The combined winding matrix is -8Id, with the index-two reflection sign retained; the full symmetric prism solution has exactly the displayed two scalar parameters.',
        'The complete common first-target matrices and derivative entries follow from the three actual seeds and their typed meridian resets.',
        'Both generator identities preserve the full target matrices by uniqueness, and their integral class increments equal f(Sprime)-f(S). No division of a sphere class is used.',
        'The vertical and first-step seeds agree with f(1),f(3), completing induction through every finite Euclidean word and all identical-fan arrows.',
        'The exact parity/modulo-seven bound gives eight classes on each branch; all sixteen displayed unimodular fans have determinant one and realize the stated values.',
        'The only final notation change is the identity renaming of the combined derivative array from mathcal d to mathcal D; its defining sum and every entry remain unchanged.'
    ],
    'independent_audit': 'records/checks_audit_source_infinity_closed_formula.json',
    'exact_certificate': str(cert.relative_to(ROOT)),
    'scope': 'Actual fixed-scalar E7 infinity return in K92, all its marked fans and stated branches; no infinity characteristic pair is asserted.'
}
(ROOT/'records/root_audit_source_infinity_closed_formula.json').write_text(json.dumps(audit,indent=2)+'\n')
assembly_path = ROOT/'records/k93_proof_assembly.json'
assembly = json.loads(assembly_path.read_text())
assembly.update(status='Proved; complete mathematical and visual review PASS',qa='records/k93_standalone_visual_qa.json',root_audit='records/root_audit_source_infinity_closed_formula.json')
assembly_path.write_text(json.dumps(assembly,indent=2)+'\n')

archive = ROOT/'records/attempts/master71_before_k93'
archive.mkdir(exist_ok=False)
for name in ['notes/part3.tex','notes/part3_remaining_return_obligations.tex','code/update_report.py','code/part3/results_mapping.json','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_paper.aux','S6_06_BLIND_paper.toc']:
    p=ROOT/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
p=ROOT/'notes/part3.tex';s=p.read_text();include=r'\input{notes/'+stem+'.tex}'
assert include not in s;p.write_text(s+'\n'+include+'\n')

p=ROOT/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
marker='The outstanding work is the remaining marked source-moduli'
assert marker in s
addition=r'''P3K.93 evaluates that complete algorithm in closed form. Put
\((x,y)^t=P^{-1}(0,1)^t\) and \(S=x^2+xy+y^2\). Then
\[
 I_a(P)=1-a-3(a-1)(S-1)-\frac{2a+1}{4}(S-1)(S-3)
          \pmod {28}.
\]
The proof supplies the full paired prism equations, the common
first-step seed and both generator identities. Its complete images
are \(\{0,6,8,10,14,20,22,24\}\) for \(a=1\) and
\(\{5,7,9,13,19,21,23,27\}\) for \(a=2\), with an actual
unimodular fan witness for every entry.

'''
s=s.replace(marker,addition+marker,1)
s=s.replace('P3K.76--92 cited','P3K.76--93 cited')
s=s.replace('P3K.92 is a new complete proof.','P3K.92--93 are new complete proofs.')
s=s.replace('P3K.85--92. In particular','P3K.85--93. In particular')
p.write_text(s)

p=ROOT/'code/part3/results_mapping.json';m=json.loads(p.read_text())
m['post_recovery_completed_return_results'].append({
    'id':'P3K.93','status':'Proved','item_of_prompt':'3.4',
    'statement':'Closed all-fan fixed-scalar E7 infinity formula in S=x^2+xy+y^2, proved through the full paired prism matrices and actual fan moves; complete eight-element images on both branches with sixteen explicit unimodular witnesses.',
    'proof':str(source.relative_to(ROOT)),'latex_file':str(tex.relative_to(ROOT)),
    'source_sha256':sha(source),'include_sha256':sha(tex),
    'certificate':str(cert.relative_to(ROOT)),
    'visual_qa':'records/k93_standalone_visual_qa.json',
    'root_audit':'records/root_audit_source_infinity_closed_formula.json',
    'provenance':'New complete proof after verified checkpoint21.'
})
p.write_text(json.dumps(m,indent=2)+'\n')

p=ROOT/'code/update_report.py';s=p.read_text()
s=s.replace('P3K.5–P3K.92','P3K.5–P3K.93')
needle='Vertical values are 1-a; Q0 squared gives 10 and 7. '
assert s.count(needle)==2
more=('K93 proves the closed formula I_a=1-a-3(a-1)(S-1)-(2a+1)(S-1)(S-3)/4 modulo 28, '
      'where S=x^2+xy+y^2 and (x,y)=P^-1 e2. Its complete images are {0,6,8,10,14,20,22,24} '
      'and {5,7,9,13,19,21,23,27}, with sixteen actual fan witnesses and 2,885 exact certificate checks. ')
s=s.replace(needle,needle+more)
p.write_text(s)
record={'utc':now,'status':'K93_INTEGRATED_PENDING_MASTER_BUILD_AND_VISUAL_REVIEW',
        'source_sha256':sha(source),'tex_sha256':sha(tex),'standalone_pdf_sha256':sha(pdf),
        'prior_master_preserved':str(archive.relative_to(ROOT)),
        'part5_sha256':{name:sha(ROOT/name) for name in ['notes/part5.tex','notes/part5_blind.md']}}
(ROOT/'records/k93_master_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
