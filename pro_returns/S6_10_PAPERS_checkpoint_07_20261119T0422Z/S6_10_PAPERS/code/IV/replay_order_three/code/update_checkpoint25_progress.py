"""Record the required hourly decision and the actual new mathematical state."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


now = datetime.now(timezone.utc).isoformat()
qa = json.loads((ROOT/'records/master75_audit.json').read_text())
assert qa['status'] == 'PASS' and not qa['findings']
assert sha(ROOT/'S6_06_BLIND_paper.pdf') == qa['pdf_sha256']
assert qa['overfull_above2pt'] == 0
part5 = {n:sha(ROOT/n) for n in ('notes/part5.tex','notes/part5_blind.md')}
assert part5['notes/part5.tex'] == 'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert part5['notes/part5_blind.md'] == 'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
certificates = [
    'code/part3_root/e6_p_one_common_peer.json',
    'code/part3/e6_selected_infinity_factor_overlay.json',
    'code/part3_root/e6_selected_infinity_mu2_pair.json',
    'code/part3_root/e6_selected_infinity_mu2_fixed.json',
    'code/part3_root/e6_selected_infinity_mu2_residue_comparison.json',
    'code/part3/e6_generic_fixed_curve_normals.json',
    'code/part3/e6_order_three_fixed_surfaces.json',
    'code/part3_root/e6_order_three_surfaces_aux_peer.json',
    'code/part3_fourfold/e6_fixed_face_orbits.json',
    'code/part3/e6_order_three_lower_surfaces.json',
    'code/part3/e6_lower_surface_blowups_peer.json',
    'code/part3_fourfold/e6_selected_infinity_curve_clutch.json'
]
evidence = {}
for name in certificates:
    path = ROOT/name
    data = json.loads(path.read_text())
    assert data['status'].startswith('PASS'), name
    evidence[name] = {'sha256':sha(path),'status':data['status'],
                      'checks':data.get('checks',data.get('check_count'))}
typesetting = {
    'checkpoint':25,'utc':now,'pages':qa['pages'],'master_build':75,
    'pdf_sha256':qa['pdf_sha256'],'pdf_bytes':qa['pdf_bytes'],
    'before_over_2pt':0,'overfull_over_2pt':0,'max_overfull_pt':qa['max_overfull_pt'],
    'rendered_pages':qa['rendered_pages'],'contact_sheets':qa['contact_sheets'],
    'visual_inspection':'The delivered master75 PDF is byte-identical to its previously fully reviewed813-page build. '+qa['visual_inspection'],
    'all_page_boundaries':'PASS','missing_or_undefined_references':0,
    'retained_prior_audit':'records/master75_audit.json',
    'new_work_scope':'The new complete local proofs and global working ledgers are preserved as working notes and exact certificates; no new master76 PDF or completed global return is claimed.',
    'qa':'records/master75_audit.json'
}
(ROOT/'records/typesetting_checkpoint25.json').write_text(json.dumps(typesetting,indent=2)+'\n')
progress = {
    'checked_utc':now,'decision':'CONTINUE',
    'reason':'The main Part3.4 return computations advanced to complete compact fixed-component normal ledgers, independently checked surface characteristic calculations, actual source/exterior chain maps, and the selected-infinity common quotient and local characteristic comparison. The remaining work is still the actual global boundary/reference/cap transfer needed for the unresolved returns.',
    'table_progress':'The current working calculations now include the complete510-cone generic fan and520/558/524 corner extensions, exact compact order-three subtotal(-45,120) from276 curves,117 surfaces and20 points, and the four remaining p1 lower surfaces with explicit source/normal maps and nine proved source blowups on each. The selected-infinity interfaces have38 common three-cones,39 selected charts and238 smooth quotient charts, plus the exact mu2 local zero-correction comparison. Both global characteristic returns remain unfinished; the working proofs and independent certificates are included.',
    'main_question_progress':[
        'The p1 common Cayley extension is complete with558 smooth four-cones, all30 original parent morphisms, full point-line P^3 factor, original volume orders and38 directed period maps. Its independent root certificate passes14013 assertions, including7698 exact triangle-pair separation checks and every full-unit inverse map. Together with the520 and524 corner extensions this closes the three-end fan interface.',
        'The stronger request for every translated source cut in one locally finite periodic fan is disproved by its actual dense boundary orbit. The finite marked boundary source/Cartier graphs and actual total-line completion remain in use. The exact failed greedy source-cut attempt is retained, with the reason it did not terminate in the requested stronger class.',
        'The order-three normal ledger now has276 compact P1 curves with physical inner pair(-1895/18,-50/3),117 compact surfaces with pair(1121/18,596/3), and two ten-point corner blocks each(-1,-31). The surfaces consist of113 actual ruled surfaces and4 one-point infinity blowups, with all free integral intersection matrices and full end clutches retained. Root independently recomputed every normal intersection and p1 by auxiliary-circle localization, passing1644 assertions. Precisely these compact pieces sum to(-45,120), with expression-25/2; this is not a total return.',
        'The four p1 lower fixed surfaces have the literal source coordinate Z_*=P^j Z, source-cell I=i+j and period Q=P^3, and the exact invariant normal frames c^-j a,c^j b. Reading all48 actual lower parent maps reveals three ordinary blowups at each of the three source nodes: each surface is the ninefold blowup of the minimal I3 source. The normal rows remain pulled back, while the tangent p1 difference is-27 per surface. Checks independently verified these maps in412 assertions; the superseded minimal-source diagnostic is preserved. The source/exterior boundary map carries the complete v-factor chain to U_k V_k=s, retaining every P,u_s,Z,c factor, both h/B arrows and the full finite-root/reference word. The sDelta point-line transfer through the selected tube and finite cap remains the exact open gate. The retained half-integer diagnostic is unassigned and is not used to choose a correction.',
        'The selected-infinity grouped/alternating factor mismatch now has a proper common38-cone interface, its full39-chart selected extension and238-chart smooth mu4 quotient resolution in the actual invariant lattice. The original canonical character(-1,5,4,0), point/theta q^j and psi arrows, full source translation and all period-unit factors are retained. The prior52-chart ordinary-only template and every failed or superseded version remain preserved.',
        'The non-O/T mu2 pair has a complete proper coarse quotient resolution, all twelve Rees charts, full chord mixing, actual gamma inverse B closing and original marked-volume coefficients. Its two stabilizer P1 bases and four isolated physical fixed points are independently checked. Each isolated point contributes1/16 in the specified positive-hyperplane polynomial. The actual A1 source resolution changes the fixed-surface term by-1/16: the integral matrix[-2], nontrivial boundary order-two character, literal ell=chi*a line map and explicit outward vector fields give delta D^2=-1/2 and delta p1=-3. Their exact local sum is zero at all four nodes; this comparison passed independent review.',
        'The selected-infinity fixed-face ledger now matches all18 O/T surface patches and10 interface curves through the38-cone interface to the39 selected charts. Its238-chart compact interior consists of106 points and18 curves, with positive-hyperplane subtotal9/4 per local O/T template. Strict-source, exceptional-source, refinement and moving selected surfaces remain separate. The ten interface-curve normal clutches now extend over the actual P1 base with full native/selected units and have zero subtotal per O/T copy. The surface base-direction normal clutches and selected reference-cap transfer remain active; no global surface class or return is inferred from a local equation.'
    ],
    'other_open_item_progress':[
        'Master75 remains unchanged at813 pages and278 formal statement rows. Its exact PDF hash and full prior direct-render QA were rechecked; there is no overflow above2pt and the retained maximum is1.61101pt. All new local proofs, full source maps, matrices, programs, outputs, audit records and preserved attempts are included as working material.',
        'Parts1,2, the requested irreducible/normal-crossing scope of Part4, and immutable blind Part5 retain their established states. The other marked source-moduli, singular-site and endpoint scopes remain in the detailed P3K.75 register.',
        'Checkpoint24 was independently restored and saved in full with8748 verified files. Checkpoint25 reuses all86 verified closed content shards and a resumable frozen-file journal, preserving exact original bytes and all predecessor content.'
    ],
    'next_progress_check_due_utc':'2026-11-18T01:49:44+00:00',
    'checkpoint_due_utc':'2026-11-18T00:49:44+00:00',
    'publication':'Exactly one complete immutable hourly checkpoint25 ZIP; no individual proof files are uploaded.',
    'main_pdf':{'build':75,'pages':qa['pages'],'sha256':qa['pdf_sha256'],'status':'PASS_UNCHANGED'},
    'part5_sha256':part5,'current_evidence':evidence
}
(ROOT/'records/progress_check_25_hours.json').write_text(json.dumps(progress,indent=2)+'\n')
archive = ROOT/'records/checkpoint25_prior_progress'
archive.mkdir(exist_ok=True)
for name in ('S6_06_BLIND_report.md','S6_06_BLIND_results.csv'):
    destination = archive/name
    if not destination.exists():
        shutil.copy2(ROOT/name,destination)
subprocess.run([sys.executable,str(ROOT/'code/update_report.py')],cwd=ROOT,check=True)
assert (ROOT/'S6_06_BLIND_report.md').read_text().startswith('INCOMPLETE\n')
print(json.dumps({'status':'PASS','utc':now,'decision':'CONTINUE','pages':qa['pages'],
                  'evidence_records':len(evidence),'pdf_sha256':qa['pdf_sha256']},indent=2))
