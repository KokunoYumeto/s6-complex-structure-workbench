"""Required hourly decision, with the current exact mathematical evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def sha(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source,'sha256').hexdigest()


now=datetime.now(timezone.utc).isoformat()
pdf_sha=sha(ROOT/'S6_06_BLIND_paper.pdf')
qa=None
for build in (76,75):
    path=ROOT/f'records/master{build}_audit.json'
    if not path.exists():
        continue
    candidate=json.loads(path.read_text())
    if candidate.get('status')=='PASS' and candidate.get('pdf_sha256')==pdf_sha:
        qa=candidate
        qa_path=path
        master_build=build
        break
assert qa is not None, 'The delivered main PDF needs its matching completed audit.'
assert qa.get('overfull_above2pt',qa.get('overfull_over_2pt',0))==0
part5={n:sha(ROOT/n) for n in ('notes/part5.tex','notes/part5_blind.md')}
assert part5['notes/part5.tex']=='f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert part5['notes/part5_blind.md']=='ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
certificates=[
 'records/root_audit_e6_order_three_outer_transfer.json',
 'records/blind_audit_e6_order_three_outer_transfer.json',
 'code/part3_root/e6_order_three_fan_algebra.json',
 'code/part3/e6_order_three_native_product_peer.json',
 'records/checks_audit_e6_order_three_all_fans.json',
 'code/part3/e6_order_three_all_fans_peer.json',
 'records/k99_standalone_visual_qa.json',
 'records/k100_standalone_visual_qa.json',
 'records/blind_audit_e6_selected_infinity_strict_surfaces.json',
 'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.json',
 'code/part3/e6_selected_infinity_compact_stars_peer.json',
 'records/blind_audit_e6_selected_infinity_compact_stars.json',
 'code/part3_root/e6_selected_infinity_moving_cap.json',
 'code/part3/e6_selected_infinity_moving_cap_peer.json',
 'records/blind_audit_e6_selected_infinity_moving_cap.json',
 'records/fourfold_audit_e6_selected_infinity_moving_cap.json',
 'code/part3_root/e6_selected_infinity_full_pair_ledger.json'
]
evidence={}
for name in certificates:
    path=ROOT/name
    data=json.loads(path.read_text())
    status=data.get('status',data.get('result',''))
    assert str(status).startswith('PASS'),(name,status)
    evidence[name]={'sha256':sha(path),'status':status,
                    'checks':data.get('checks',data.get('check_count'))}

typesetting={'checkpoint':26,'utc':now,'master_build':master_build,
 'pages':qa['pages'],'pdf_sha256':pdf_sha,'pdf_bytes':(ROOT/'S6_06_BLIND_paper.pdf').stat().st_size,
 'overfull_over_2pt':0,'before_over_2pt':0,'max_overfull_pt':qa.get('max_overfull_pt'),
 'rendered_pages':qa['rendered_pages'],'contact_sheets':qa['contact_sheets'],
 'visual_inspection':qa.get('visual_inspection','Direct page review recorded in the matching master audit.'),
 'qa':str(qa_path.relative_to(ROOT)),
 'new_standalone_QA':['records/k99_standalone_visual_qa.json','records/k100_standalone_visual_qa.json'],
 'scope':'The exact delivered master PDF and the complete72-page K99 and7-page K100 exports have matching direct visual and log audits. Selected-infinity proofs remain explicitly scoped working calculations.'}
(ROOT/'records/typesetting_checkpoint26.json').write_text(json.dumps(typesetting,indent=2)+'\n')

progress={'checked_utc':now,'decision':'CONTINUE',
 'reason':'The main Part3.4 catalogue advanced to a complete order-three source return, its full integral native data and all-fan class formula with complete image, and complete selected-infinity compact and moving-cap characteristic terms. The exact remaining outer-family transfer and remaining source-generator/cap scopes are active mathematical work.',
 'table_progress':'For the original E6 (6,1;2), norm n=1 and the ordered unselected-I3 loop, the initial fan has physical Jin pair(-27,-12), index-4 and class24. Every selected lattice-basis fan is now covered by the proved formula A=-4+3(S-1)/2-27(S^2-1)/8, S=x^2+xy+y^2 for (x,y)=P^-1 e2, with exactly16 realised residues. The selected-infinity strict surfaces, both O/T compact-star copies and the moving Q0Q1 reference-cap contribution have full maps and independent checks; the outer return/free-pair transfer, selected-I3 loops and remaining cap/endpoint scopes are still active.',
 'main_question_progress':[
  'K99 closes the original norm-one order-three initial fan. All four lower p1 surfaces are ninefold source blowups; their collision/reference doubles have unchanged normal squares and tangent difference-27 each. The compact subtotal(-45,120) and four lower pairs(18,-27) give the actual inner pair(27,12). The full point/Cartier H, source parameter word(1,2)-(0,2)=(1,0), finite cap and literal K68 inverse clutch give the physical Jin pair(-27,-12), integral index-4 and class24. No scalar reference is subtracted twice. The full72-page export and its seven complete proof companions have direct QA.',
  'K100 supplies the full native ordinary products for every basis fan, with the original q-dependent coefficient inverses recovered through their actual height maps. The based ordinary disc products and physical prism contractions give I=W=0. The actual K23/K68 quaternion product fixes native(m,n)=(-3,-24), V=diag(27,0,0), delta=(-21,0,0), A=-4. Full collar-matched connection excision proves the same initial data for every vertical fan. Each directed ruling retains the actual common-link reset(m+2n,-n,A+n).',
  'The fan factorization and complete prism systems give c=27[pr(p+r)]^2, e=pr(p+r)(6-27S) and A=-4+3(S-1)/2-27(S^2-1)/8. Exact enumeration modulo112, together with actual primitive Bezout witnesses, proves that the image is exactly{0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26}. Root arithmetic passes233305 checks; the full independent peer passes9256, and the native-product peer passes474. The earlier naive inverse of a q-dependent scaling is preserved and corrected before promotion.',
  'The selected-infinity four strict source surfaces now have the full refined normal bundles I_(O+T)^(4-j)L^j and L^(-j-1), the exact A3 boundary-character map, normal-difference squares(-14,-16,-14,-8), and tangent p1=-24 each. Their U expression sums to5/2; the four isolated mu2 points add1/4. The A1 source normal and tangent comparisons retain their previously verified local cancellation.',
  'The two O/T compact-star copies each close by the actual p=1/v and native finite-base charts, giving296 charts. Each contains four exceptional surfaces with U sum-5/2, ten refinement surfaces with U sum-9/4, twelve p-curves with U sum3/4, and the earlier zero-sum ten interface curves. The explicit B:(C,j)->(opposite C,j+4), B^2 shift8 proves two source orbits. Every surface has its complete integral tangent intersection matrix and actual normal divisor; the independent native-base-circle calculation passes625 checks. The dual-divisor sign label was located and corrected, with its complete earlier version preserved and all squares unchanged.',
  'The moving Q0Q1 face is identified with the two actual ordinary blowups of P1 times the parameter disc. The full elementary-transform map S=rho*z1 gives the original two infinitely near blowups and both source branches. Its exact q-factor negative normal retains the Z^-1 source unit. Full point/theta and Miller arrows retain all exceptional orders and determinant phases. The actual D3 times S1 reference cap has primitive H1 restriction and injective H2 gluing; this proves c1(Ec)=0 without discarding the SU2 clutch. Two blowup Jacobians give p1=-6, and the projective-link polynomial cancels the unassigned c2, yielding the scoped moving U contribution-1/4 before any global sum. Independent geometric reviews and exact certificates cover these maps. The separate free pair and complete outer return remain under construction.'
 ],
 'other_open_item_progress':[
  'Parts1,2, the requested irreducible/normal-crossing scope of Part4, and immutable blind Part5 retain their established states. The remaining Part3.4 source-moduli, cap and endpoint scopes stay explicitly unfinished.',
  'The new order-three initial/all-fan results are norm-one original(6,1;2) statements. No higher-cap extension or selected-I3 result is inferred from their local equations or finite-group residues.',
  'Checkpoint25 was independently restored with8952 verified files and saved. Checkpoint26 reuses all87 closed verified shards, adds the complete new proof/code/log/attempt contents, and keeps exact predecessor bytes.'
 ],
 'next_progress_check_due_utc':'2026-11-18T02:49:44+00:00',
 'checkpoint_due_utc':'2026-11-18T01:49:44+00:00',
 'publication':'Exactly one complete immutable hourly checkpoint26 ZIP; no individual uploads.',
 'main_pdf':{'build':master_build,'pages':qa['pages'],'sha256':pdf_sha,'status':'PASS'},
 'part5_sha256':part5,'current_evidence':evidence}
(ROOT/'records/progress_check_26_hours.json').write_text(json.dumps(progress,indent=2)+'\n')
archive=ROOT/'records/checkpoint26_prior_progress'
archive.mkdir(exist_ok=True)
for name in ('S6_06_BLIND_report.md','S6_06_BLIND_results.csv'):
    target=archive/name
    if not target.exists():
        shutil.copy2(ROOT/name,target)
subprocess.run([sys.executable,str(ROOT/'code/update_report.py')],cwd=ROOT,check=True)
assert (ROOT/'S6_06_BLIND_report.md').read_text().startswith('INCOMPLETE\n')
print(json.dumps({'status':'PASS','utc':now,'decision':'CONTINUE','master_build':master_build,
 'pages':qa['pages'],'evidence_records':len(evidence),'pdf_sha256':pdf_sha},indent=2))
