"""Record the authorized hourly research check and the verified master75 QA."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,shutil
ROOT=Path(__file__).resolve().parents[1]
def sha(path):
 with path.open('rb') as source:return hashlib.file_digest(source,'sha256').hexdigest()
now=datetime.now(timezone.utc).isoformat()
qa=json.loads((ROOT/'records/master75_audit.json').read_text())
assert qa['status']=='PASS'
assert sha(ROOT/'S6_06_BLIND_paper.pdf')==qa['pdf_sha256']
assert qa['overfull_above2pt']==0 and not qa['findings']
part5={name:sha(ROOT/name) for name in ('notes/part5.tex','notes/part5_blind.md')}
assert part5['notes/part5.tex']=='f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert part5['notes/part5_blind.md']=='ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
typesetting={
 'checkpoint':24,'utc':now,'pages':qa['pages'],'master_build':75,
 'pdf_sha256':qa['pdf_sha256'],'pdf_bytes':qa['pdf_bytes'],
 'before_over_2pt':0,'overfull_over_2pt':0,'max_overfull_pt':qa['max_overfull_pt'],
 'rendered_pages':qa['rendered_pages'],'contact_sheets':qa['contact_sheets'],
 'visual_inspection':qa['visual_inspection'],'all_page_boundaries':'PASS',
 'missing_or_undefined_references':0,'retained_prior_audit':'records/master74_audit.json',
 'standalone_reviews':'K98 all nine standalone pages and every integrated page directly reviewed; prior K95–97 complete reviews retained.',
 'qa':'records/master75_audit.json'
}
(ROOT/'records/typesetting_checkpoint24.json').write_text(json.dumps(typesetting,indent=2)+'\n')
common=json.loads((ROOT/'records/checks_audit_e6_common_period_fan.json').read_text())
assert common['status']=='PASS'
assert sha(ROOT/common['certificate'])==common['certificate_sha256']
progress={
 'checked_utc':now,'decision':'CONTINUE',
 'reason':'The main Part3.4 calculation advanced through the complete higher-cap selected-cusp proof K98, an independently verified common fan with all three actual parent maps for the order-three collision, and the full selected-infinity source/root/Cartier/ordinary-chain/selected-corner/cap-overlap maps. The active work remains on the unresolved returns.',
 'main_question_progress':[
  'P3K.98 is complete and integrated. For both cap progressions(6,1;3l+2),l>=0, and(2,3;3l),l>=1, both norm signs, every finite character/full annular reference and every selected fan, the ordered selected-cusp return is computed through the actual K71 comparison. The vertical physical pair is(-6-18j(j-1),0), with class-1-3j(j-1) modulo28 and exact parameter degree4.',
  'The order-three collision now has all three p=0,1,infinity period-end models, full point/theta/Cartier graphs, exact source binomials and the original canonical P factor. The alternative p=0 fan has19 explicit regular cones. The generic common comparison has510 regular cones,186 exact intersection polygons,108 recorded stellar steps,745 interior and40 boundary faces, all parent monomial and full unit maps, both actual source rows and exact primitive multiplicities/canonical orders. Its independent peer certificate passes8167 checks. The infinity native-height arrow R=pP is retained explicitly.',
  'The common fan has now been extended into the p=0 and infinity corner models with520 and524 regular four-dimensional cones, full parent semigroup maps and exact four-dimensional period faces. Its exact certificate passes9929 checks. The infinity source-node map extends throughout; p=0 source cuts and point-line graphs remain active.',
  'The selected-infinity ordinary O/T coarse mu4 quotient has a new explicit52-cone periodic resolution in its actual invariant lattice, obtained by14 recorded subdivisions. Every invariant-ring generator has a nonnegative integral monomial pullback, and all physical weights, base arrows, local canonical divisors and full period-unit lifts are retained. Independent peer review, original determinant-form comparison and whole attachment are pending.',
  'The common generic model retains its finite isotropy. The four-dimensional corner source/line refinements and their global determinant/normal attachment remain active; no local charged-face count has been promoted to a total return.',
  'The selected-infinity calculation now retains the exact two root-graph charts, the ordinary mu4 quotient, both O/T source graphs and their additive source reset, the genuine point-line factors, the four-step ordinary line chain, the six-chart selected T0 attachment and nine-factor graph corners. Its actual ordinary-to-original-cap map is restricted to the proved large-sigma domain and includes the whole A B^j reference cochain and every scalar/root/character factor. Its global compact boundary and characteristic calculation remain unfinished.'
 ],
 'other_open_item_progress':[
  'Master75 has813 pages and278 statement rows. Both LuaLaTeX passes and all813 page bounds pass, with no overflow above2pt; the one retained overflow is1.61101pt. Root directly reviewed all21 rendered pages, including every K98 page and transitions. All preceding mathematical and failed computational attempts remain preserved.',
  'Parts1,2, the requested irreducible/normal-crossing scope of Part4, and the immutable blind Part5 retain their proved states. The remaining main catalogue includes further marked source-moduli generators, singular-site sectors and endpoint scopes recorded in P3K.75.'
 ],
 'next_progress_check_due_utc':'2026-11-18T00:49:44+00:00',
 'checkpoint_due_utc':'2026-11-17T23:49:44+00:00',
 'publication':'Exactly one complete immutable checkpoint24 ZIP is scheduled; no individual proof files are uploaded.',
 'main_pdf':{'build':75,'pages':qa['pages'],'sha256':qa['pdf_sha256'],'status':'PASS'},
 'part5_sha256':part5,
 'generic_common_fan_peer':'records/checks_audit_e6_common_period_fan.json',
}
(ROOT/'records/progress_check_24_hours.json').write_text(json.dumps(progress,indent=2)+'\n')
old=ROOT/'records/checkpoint24_prior_progress';old.mkdir(exist_ok=True)
for name in ('S6_06_BLIND_report.md','S6_06_BLIND_results.csv'):
 dest=old/name
 if not dest.exists():shutil.copy2(ROOT/name,dest)
subprocess.run([sys.executable,str(ROOT/'code/update_report.py')],cwd=ROOT,check=True)
assert (ROOT/'S6_06_BLIND_report.md').read_text().startswith('INCOMPLETE\n')
print(json.dumps({'status':'PASS','utc':now,'decision':'CONTINUE','pages':qa['pages'],'pdf_sha256':qa['pdf_sha256']},indent=2))
