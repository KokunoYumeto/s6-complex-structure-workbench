"""Record the actual bounded CP30 delta and complete K108 export reviews.

This creates no new computational replay and does not resolve K75.
"""
from pathlib import Path
import csv
import hashlib
import json
from datetime import datetime, timezone

R = Path(__file__).resolve().parents[4]
W = R / 'work/S6_10_PAPERS'
N = R / 'sources/newer_night/checkpoint30'
now = datetime.now(timezone.utc).isoformat()
checker = 'GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
delta = json.loads((W / 'analysis/inventory_cp30_export_delta.json').read_text())
events_path = W / 'analysis/IV/current_check_events.json'
events = json.loads(events_path.read_text())
assert not any(e['event_id'] in {'IV-D-084', 'IV-D-085'} for e in events)

k106 = {
    'event_id': 'IV-D-084', 'type': 'D', 'labels': ['night:P3K.106'],
    'verdict': 'proved',
    'scope': 'Complete mathematical delta review of all twelve changed CP29-to-CP30 supporting TeX files; the earlier complete proof review IV-D-069 supplies the unchanged argument. This event does not assert a new complete rereading of the unchanged support text.',
    'derivation': 'Read every diff hunk in all twelve changed supporting files, including the original SI3 source lattice and integral quadratic polarization, original height and period exponents, all normal and cap clutches, vertical characteristic sums and full native prism resets. Changes render existing subscripts, widehat symbols, binomial coefficients, matrix entries and mathematical words correctly; the exact source maps, integer values and theorem scope are unchanged. Re-derived the rendered SI3 lattice inclusion diag(1,2), symmetric period matrix [[7r,2r],[2r,4r+2z]], its integral quadratic polynomial, and the unchanged h=J^2 K^-1, B=K J^-1 full coefficient arrows. Rechecked the rendered target-prism signs, native m,n extraction, Cox multiplier lift, the fixed cap seam Cwidehat_1^-1 Cwidehat_0, and vertical Euler polynomial. The incoming IC2 Hermitian sentence still uses an ambiguous opposite metric convention, and IF3 still omits the required Tate/native dictionary; both actual receiving repairs from IV-D-069 are retained explicitly. The physical initial pair (47,-4), vertical pair (47-2j^3+18j^2-52j,-4), native seed and all twenty-eight fan witnesses remain unchanged.',
    'checker': checker, 'recorded_at': now, 'source_checkpoint': 30,
    'source_main_sha256': sha(N / delta['exports']['P3K.106']['source_file']),
    'included_source_files': delta['exports']['P3K.106']['included_files'],
    'prior_complete_proof_event': 'IV-D-069',
    'computation_scope': 'No new replay assigned; earlier unchanged executions retain their exact historical current-event scope.',
    'artifacts': ['analysis/IV/CP30_current_reviews.json', 'analysis/IV/K106_cp30_all_changes.diff', 'analysis/inventory_cp30_export_delta.json']
}
k108 = {
    'event_id': 'IV-D-085', 'type': 'D', 'labels': ['night:P3K.108', 'iv:i3_all_reduced_caps'],
    'verdict': 'proved',
    'scope': 'Complete CP30 K108 statement and all 427 lines of its included proof read and rederived; exact construction-by-construction comparison with the already rederived nine-step receiving ICAP proof. One theorem and one full proof carry both labels.',
    'derivation': 'Re-derived the exact selected discriminant roots and v-to-s height map, original root source scaling, three A2 charts, formal m-division and proper graph ideal (tau,z^k), including the full z^k s ell Cartier coefficients. The selected-height ratio H=h_c/h_o has its deck-invariant logarithm zero at z=0; its full mth root gives B_c=H B_o and Ftilde_c=H^(1/m) Ftilde_o with their chronological norms. Kept the signed generator A^m=B^n, J=A^n, every finite character, all original Pi/Lambda/integer sector cochains and their exact inverse arrows. Re-derived the finite weighted norm inequality and the compact relative cap products with the prescribed common boundary flow. Multiplied C_(m,n) T_(m,n)=C_(2,+), retaining n^2=1 and both determinant signs; the physical Euler restriction (0,-1), orbit and conifold matrices retain the primitive kernel (1,-1). The receiving proof spells out the actual M6 E6-B (6,1) sphere-reference w arc and its source/Cartier transport. On each five-dimensional cap body the pulled-back line and tangent connections make x^3 and p1*x vanish separately, while the full line and derivative maps match their common collar transgressions; the disjoint selected Hopf completion retains its original physical orientation. This carries both integer pairs and every unchanged AFI native fan map, all twenty-eight witness paths and the actual source/point-theta reflection (Z,V)->(Z^-1,P^6 V)->(Q/Z,V). The resulting proof is exactly the earlier ICAP construction with no additional cap domain, scalar range or M2 conclusion. The explicit vertical cubic S_j=8-j(j^2-9j+26)/3 is displayed in the shared theorem, and the harmless F_c^{,n} typographic comma is removed.',
    'checker': checker, 'recorded_at': now, 'source_checkpoint': 30,
    'source_main_sha256': sha(N / 'notes/part3_e6_selected_i3_all_caps.tex'),
    'source_proof_sha256': sha(N / 'notes/part3_e6_selected_i3_all_caps_proof.tex'),
    'receiving_sha256': sha(W / 'papers/IV/i3_all_reduced_caps.tex'),
    'prior_complete_proof_event': 'IV-D-072',
    'computation_scope': 'No new execution is claimed. IV-C-016 retains its two unchanged 5083- and 973-check executions against their exact CP29 programs.',
    'artifacts': ['analysis/IV/CP30_current_reviews.json', 'papers/IV/i3_all_reduced_caps.tex', 'analysis/IV/ICAP_current_review.json']
}
k75 = {
    'record_kind': 'context reading; parent owns the formal scope event', 'labels': ['night:P3K.75'],
    'verdict': 'Open; changed current-obligations statement reviewed',
    'scope': 'Full CP30 current-obligations statement and its exact CP29-to-CP30 addition reviewed. This is a scope/intake review, not a proof closure of the remaining attachment problem and not a new review of the archived failed-route history.',
    'derivation': 'Read the complete current statement through its explicit final residual gap. K106 supplies the M6 selected-I3 quadratic initial, signed vertical and all-fan calculation; K108 carries that precise construction through the full reduced cap progression m=3l+2, both primitive norm signs, every admitted character and complete annular reference in each cap/reference common strict contraction range, with the actual marked reflection. K107 supplies the M2 unselected order-three all-good-cap construction and sixteen-class algorithm. The unresolved scope is precisely the selected-I3 M2 return and remaining cap/norm/fan sectors, additional marked singular-site sectors and remaining holomorphic endpoints. These new registrations do not close that residual problem. The reader proof will contain the actual completed deductions; the inherited failed-route chronology remains in the source archive.',
    'checker': checker, 'recorded_at': now, 'source_checkpoint': 30,
    'source_file_sha256': sha(N / 'notes/part3_remaining_return_obligations.tex'),
    'artifacts': ['analysis/IV/CP30_current_reviews.json']
}
events.extend([k106, k108])
events_path.write_text(json.dumps(events, indent=2) + '\n')
fields = ['event_id','type','labels','verdict','scope','derivation','checker','recorded_at','artifacts']
with (W/'analysis/IV/current_check_events.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
    writer.writeheader()
    for event in events:
        row = dict(event)
        for key in ['labels','artifacts']:
            row[key] = json.dumps(row.get(key, []), ensure_ascii=False)
        writer.writerow(row)
(W/'analysis/IV/CP30_current_reviews.json').write_text(json.dumps({
    'recorded_at': now, 'source_checkpoint': 30,
    'reviews': [k106,k108], 'K75_context_reading_only': k75,
    'K108_shared_proof': {'labels': ['night:P3K.108','iv:i3_all_reduced_caps'],
        'file': 'papers/IV/i3_all_reduced_caps.tex', 'sha256': k108['receiving_sha256']},
    'receiving_integration': 'pending complete rebuild and exact repair assertions'
}, indent=2)+'\n')
print(now, 'IV-D-084; IV-D-085 written; parent owns K75 scope event; no new computation event')
