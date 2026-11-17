from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
qa_path = ROOT / 'records/qa_k68.json'
qa = json.loads(qa_path.read_text())
assert qa['compile'] == 'PASS' and qa['pages'] == 6
assert not qa['overflows_gt_2pt'] and not qa['boundary_issues']
assert not qa['missing_character'] and not qa['undefined_reference']
qa['visual_review'] = 'PASS: all six pages inspected individually at full size'
qa['visual_review_utc'] = now
qa_path.write_text(json.dumps(qa, indent=2) + '\n')
visual = {
    'utc': now, 'status': 'PASS', 'reviewer': 'fourfold', 'statement': 'P3K.68',
    'pages_reviewed': list(range(1, 7)), 'full_size_pages': list(range(1, 7)),
    'findings': [],
    'observations': [
        'All six standalone page images were inspected individually at full size.',
        'The anti-linear matrix, quaternionic extension, circle representation and inverse-clutch displays are legible and within the page bounds.',
        'No clipping, collisions, missing symbols or malformed equations were observed.',
        'The rendered page 2 uses the pre-master wording currently written; root changed this historical wording to previously written in the master source without changing the mathematical display.'
    ],
    'pdf': 'code/part3_fourfold/k68_standalone.pdf',
    'pdf_sha256': digest('code/part3_fourfold/k68_standalone.pdf'),
    'include': 'notes/part3_physical_line_corrigendum.tex',
    'include_sha256': digest('notes/part3_physical_line_corrigendum.tex'),
    'working_proof_sha256': digest('notes/part3_physical_line_corrigendum_working.md')
}
(ROOT / 'records/k68_standalone_visual_qa.json').write_text(json.dumps(visual, indent=2) + '\n')

peer = {
    'utc': now, 'reviewer': 'fourfold', 'statement': 'P3K.69', 'status': 'PASS',
    'proof': 'notes/part3_physical_return_consequences.tex',
    'proof_sha256': digest('notes/part3_physical_return_consequences.tex'),
    'exact_dictionary': {
        'physical_pair': '(k_M,ell_M)=-(k_U,ell_U)',
        'physical_class': 'A_M=-A_U',
        'reference_pair_U': '(-3H,-24chi)',
        'reference_pair_M': '(3H,24chi)',
        'native_pair': '(6chi,3H-6chi)',
        'central_generator': '+1; direct native Cox increments are retained'
    },
    'weighted_OS47': {
        'actual_page_degree': 4, 'H': 14, 'chi': 3,
        'pair_U': [-42,-72], 'pair_M': [42,72],
        'native_pair': [18,24], 'physical_class': 4,
        'fixed_edge_flop_class': 0,
        'source_reopened': 'notes/part3_os47.md, actual degree-four page and line computation',
        'located_input_correction': 'Earlier H10 chi1 wording was corrected to H14 chi3 before this final audit.'
    },
    'source_loop': {
        'pair_U': [6,0], 'pair_M': [-6,0],
        'native_tuple': [0,-6,-1], 'ordinary_tuple': [6,-6,-1],
        'first_flop_classes': [21,21,27],
        'vertical_formula': '-1-3*n*(n-1)',
        'vertical_residues': [5,7,9,13,19,21,23,27]
    },
    'K57_K58_K60': {
        'good_fixed_infinity': 0, 'reduced_fixed_infinity': -1,
        'sum': 'Z_T+Z_JT=a+2*k*A_scalar',
        'difference': 'Z_JT-Z_T=a',
        'pairs': '(k*A_scalar+14*e, a+k*A_scalar+14*e), e in {0,1}',
        'small_good': [[0,1],[14,15]],
        'small_reduced_p1_k1': [[2,4],[16,18]],
        'remaining_scope': 'The common order-two ambiguity is retained; no individual e is assigned.'
    },
    'scope': 'Propagation uses the exact K68 physical dual and inverse-clutch maps plus the previously proved direct local comparisons. No unproved all-fan product or division in Theta7 is used.'
}
(ROOT / 'records/fourfold_audit_physical_return_consequences.json').write_text(json.dumps(peer, indent=2) + '\n')

mapping_path = ROOT / 'code/part3_fourfold/results_mapping.json'
mapping = json.loads(mapping_path.read_text())
row = {
    'id': 'P3K.68', 'status': 'Proved',
    'proof_file': 'notes/part3_physical_line_corrigendum_working.md',
    'latex_file': 'notes/part3_physical_line_corrigendum.tex',
    'physical_dictionary': '(k_M,ell_M,A_M)=-(k_U,ell_U,A_U); actual sphere class A_M',
    'exact_transfer': 'lambda_M(F)=-Sigma(F^-1); lambda_U(F)=Sigma(F^-1)',
    'corrected_source_pair_M': [-6,0], 'retained_source_pair_U': [6,0],
    'corrected_source_native_tuple': [0,-6,-1],
    'source_class_mod28': 27,
    'retained_scope': 'Actual Cartier/Cox/cap maps, SU2 degree and Pontryagin number, native signed commutator and Cox increments, K65 zero-reference classes.',
    'correction_scope': 'Previous linear SP9/10 coefficient arrow is replaced by the explicit anti-linear map and actual physical line is the dual of the outward-meridian-one Thom line.',
    'certificate': 'code/part3_fourfold/euler_cube_peer_sign.json',
    'visual_qa': 'records/k68_standalone_visual_qa.json',
    'preserved_originals': 'records/k42_pre_antilinear_arrow/'
}
mapping['results'] = [r for r in mapping['results'] if r.get('id') != 'P3K.68'] + [row]
mapping_path.write_text(json.dumps(mapping, indent=2) + '\n')
print(json.dumps({'status':'PASS','visual_pages':6,'peer':'P3K.69','OS47_native_pair':[18,24],'mapping':'P3K.68'}, indent=2))
