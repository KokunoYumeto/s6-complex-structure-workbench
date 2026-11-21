from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/653608133b22')
OUT = ROOT/'work/agents/i_provenance'
LIT = OUT/'literature'
NOW = datetime.now(timezone.utc).isoformat()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, obj): p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

# Append records of images already actually viewed/read; do not manufacture a
# new mathematical event or a new page-reading time.
p=LIT/'S6_SERIES_PUBLISH_I_Oda1978_locator_receipt.json'
r=json.loads(p.read_text())
extra=[(142,130,'Theorem15.1: quadratic-field lattice, totally positive unit, quotient surface and its two cycles; hypotheses and complete statement read.'),
       (143,131,'The paragraph after Theorem15.1 and the complement description: the complement of the two cycles is the product of the real line with the Clifford-torus mapping torus. Full following paragraph read.')]
for pdfpage, printed, scope in extra:
    img=LIT/f'S6_SERIES_PUBLISH_I_Oda1978_page-{pdfpage}.png'
    if not any(x['pdf_page_one_based']==pdfpage for x in r['pages']):
        r['pages'].append({'pdf_page_one_based':pdfpage,'retypeset_printed_page':printed,'image':str(img),'image_sha256':sha(img),'actually_viewed':True,'scope':scope,'receipt_appended_utc':NOW})
r['scope']='Exact rendered pages listed below were actually viewed/read; no full-book reading or new mathematical check is asserted.'
r['locator']='Section13, retypeset pp.116–118 (PDF pp.128–130); Section15, Theorem15.1 and following paragraph, retypeset pp.130–131 (PDF pp.142–143).'
r['mathematical_check_events']=0
save(p,r)

p=LIT/'S6_SERIES_PUBLISH_I_AC_Engel_Conrad_locator_receipt.json'
r=json.loads(p.read_text())
if not any(x.get('source')=='Engel arXiv2609.38442v1' and x.get('printed_page')==7 for x in r['pages']):
    img=LIT/'S6_SERIES_PUBLISH_I_Engel_p007.png'
    r['pages'].append({'source':'Engel arXiv2609.38442v1','pdf':str(ROOT/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf'),'pdf_sha256':'5f7bc46bd47e7fc4a03e5dcab36a1c375be94bbdf065bd792673cd572547ac48','printed_page':7,'pdf_page':7,'image':str(img),'image_sha256':sha(img),'actual_rendered_page_read':True,'scope':'Figure2, completion of Proposition2.8 proof, and Proposition2.9 with its proof. Proposition2.8 permits the periodic area-one-half triangular fan; its figure does not identify the receiving paper’s chosen labelled diagonal.','receipt_appended_utc':NOW})
r['Engel_scope_correction']='The height1/6 and (6P).O=2 occur in the proof of Lemma2.1, pp.3–4. Proposition2.7, p.6, supplies the cusp Tate quotient by holomorphic units. AC Remark3.12, p.19, supplies the Mordell–Weil generator and its Abel–Jacobi sign, not that height calculation. Two earlier coordination summaries misstated these locators; the current page receipts and receiving citations use these corrected scopes.'
save(p,r)

tree=json.loads((OUT/'programs/S6_SERIES_PUBLISH_I_boundary_program_tree_receipt.json').read_text())
prefix='pro_returns/S6_02_PUSH_final_20261115T2217Z/S6_02_PUSH/code/'
commit='83d76022bcd442278b760db9ff438afceed6c6ea'
selected=[x for x in tree['matches'] if x['path'].startswith(prefix)]
assert len(selected)==7

def get(item):
    url='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'+commit+'/'+item['path']
    req=urllib.request.Request(url, headers={'User-Agent':'S6-series-publication-source-audit'})
    with urllib.request.urlopen(req,timeout=45) as response:
        b=response.read(); status=response.status
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    name=item['path'].rsplit('/',1)[1]
    local=OUT/'programs'/('S6_SERIES_PUBLISH_I_primary_'+name)
    local.write_bytes(b)
    assert len(b)==item['size'] and blob==item['sha'], (name,len(b),blob)
    return {'filename':name,'commit':commit,'path':item['path'],'url':url,'http_status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':blob,'expected_git_blob_sha1':item['sha'],'matches_pinned_tree':True,'local':str(local),'retrieved_utc':datetime.now(timezone.utc).isoformat(),'scope':'Primary raw source authenticated; scope/code reading recorded separately. No execution or new mathematical check.'}

with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
    rows=list(pool.map(get,selected))
receipt={'created_utc':NOW,'commit':commit,'tree_receipt':str(OUT/'programs/S6_SERIES_PUBLISH_I_boundary_program_tree_receipt.json'),'tree_truncation_scope':'The recursive tree is truncated. Only the observed positive paths are asserted; no missing-path inference is made.','programs':rows,'mathematical_events_added':0}
save(OUT/'S6_SERIES_PUBLISH_I_boundary_program_receipt.json',receipt)
print(json.dumps({'programs':len(rows),'all_matches':all(x['matches_pinned_tree'] for x in rows),'receipt':str(OUT/'S6_SERIES_PUBLISH_I_boundary_program_receipt.json'),'Oda_page_count':5,'new_math_events':0}))
