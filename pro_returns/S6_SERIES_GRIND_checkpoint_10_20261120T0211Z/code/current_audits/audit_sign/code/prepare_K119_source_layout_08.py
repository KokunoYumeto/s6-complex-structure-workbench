"""Narrow K119 source/layout consolidation. No canonical or body mutations."""
import csv
import datetime
import hashlib
import json
import zipfile
from pathlib import Path
import fitz

H=Path(__file__).resolve().parents[1]; W=H.parent; BASE=W.parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
with (W/'S6_SERIES_GRIND_inventory.csv').open(newline='') as f:
    row=next(x for x in csv.DictReader(f) if x['label']=='night:P3K.119')
with (W/'CHECK_EVENTS.tsv').open(newline='') as f:
    events=[x for x in csv.DictReader(f,delimiter='\t') if x['statement_id']=='night:P3K.119']
historic=next(x for x in events if x['event_id']=='ce:632aa7451dcb7766e3fd')
archive=BASE/'upload/S6_SERIES_GRIND.zip'
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    archive_scope={'archive':str(archive),'entries':len(names),
       'renewed_credit_matches':[n for n in names if 'renewed_credit' in n],
       'nested_archives':[n for n in names if n.endswith(('.zip','.tar','.tgz','.gz'))]}
assert not archive_scope['renewed_credit_matches'] and not archive_scope['nested_archives']

lit=BASE/'S6_SERIES_GRIND_source/S6_GRIND_6_literature'
e=lit/'papers/arXiv_2609.38442_Engel_src/S6.tex'
ac=lit/'original/AC26_original_manuscript.pdf'
et=e.read_text().splitlines(); acpdf=fitz.open(ac)
opened=[]
for lo,hi,loc in [(289,425,'Section2, Lemma2.1, Corollary2.2, Definition2.3 and Proposition2.4 statement'),
                  (426,558,'Section2, Proposition2.4 proof and Propositions2.6-2.8'),
                  (1738,1761,'Remark8.5, full general elliptic-line quotient and logarithmic modification construction')]:
    opened.append({'source':'E26','file':str(e),'sha256':sha(e),'locator':loc,
                   'lines':[lo,hi],'actually_read':True,'text':'\n'.join(et[lo-1:hi])})
for n in [25,26,82,83]:
    opened.append({'source':'AC26 original PDF','file':str(ac),'sha256':sha(ac),
                   'locator':f'Printed and PDF page{n}','actually_read':True,'text':acpdf[n-1].get_text()})
(H/'K119_source_openings_08.json').write_text(json.dumps(opened,indent=2)+'\n')

updates={
'credited_to':
'The original marked OS45 source, point line and primitive sphere/filling data are those of S6_06_BLIND K10, K78, K116 and F35. E26 Section2 Definition2.3, Propositions2.4,2.7,2.8 and Remark8.5 provide the elliptic-line quotient, scalar contraction, periodic Mumford filling and logarithmic modification construction. AC26 original Section4 pp25-26 and Proposition9.24/Remarks9.25-9.26 pp82-83 provide the reference toroidal atlas and physical fixed-set calculation, applied through F35\'s exact lattice/fan transport. K119 retains the complete source/Cartier/integral/Lie/protected-cap/endpoint proof for its twenty-four marked ordinary-cap meridians and reciprocals. Historical row-specific bounded credit event ce:632aa7451dcb7766e3fd is retained at its recorded scope.',
'literature_searches':
'Retained event ce:632aa7451dcb7766e3fd records49 supplied primary texts and1813 source-term queries, including original AC26, E26 and DGKXv1/v2, and its bounded row-specific comparison. The named renewed_credit_comparison.md and renewed_credit_searches.json files are absent from the956-entry uploaded ZIP and extracted source; they were not claimed reopened or replayed. Fresh current openings: E26 attached source lines289-558 and1738-1761; original AC26 PDF pp25-26 and82-83. Current IV_literature_comparison_report.md covers F35 and other named rows, not a new K119 theorem-specific search. Complete provenance and exact excerpts: audit_sign/K119_source_openings_08.json and K119_source_layout_consolidation_08.json.',
'source_credit_verdict':
'Known construction and reference-fan inputs are explicitly credited through their actual application maps. The historical bounded K119 credit comparison is retained as a recorded check; no unavailable historical file is claimed inspected. No new global novelty, priority or literature-absence conclusion is made.',
'credit_transport':
'In E26 Remark8.5 take the actual OS45 elliptic surface, M=O([8G]-[O]) and t=t_G. Its lift covers t_G^(-1), exactly p->p-G. K116\'s fixed-C_* Hom coefficient is lambda*C_*(t-t_c)*f2^8*(f8 composed with t_(-G))/f8, with chronological Miller divisor identity and the original source/target Cartier modules. The actual moving-node periods are h:(Z,V)->(QZ,P^8V) and B:(Z,V)->(P^(-1)Z,CV), where Q=(t-s)kappa and C=lambda(t-t_c)beta retain every unit. At each of the six selected-cap points t_c=s, their valuation columns are(1,0),(0,1), the primitive selected Mumford case. At each of the eighteen unselected-cap points t_c differs from s, C is a unit at the moving node, so only the source Tate column has nonzero order there; the prescribed selected Mumford filling remains at its own t_c. These literal functions retain both cases. AC26\'s reference triangulation is carried to F35\'s T_+ convention by diag(1,-1) and the indicated lattice translation; the prescribed fan is then reached by F35\'s actual common blowups and both ruling contractions, not by equality of supports. K119\'s own full integral cochain, Lie off-diagonal solve and protected-cap map carry the complete reference. Its typed identity F1*EX*F0^(-1)=C*EY and the reciprocal physical scalar isotopy identify the original return with the proper-disc return. The proof and source application preserve the fixed Hom normalization, original height, prescribed reference and fan.',
'literature_disposition':
'Retain K119 with its complete proof and explicit known-input credit. The original24-point zero-return statement is the received S6 source result; the bounded historical source comparison and current input-specific readings carry precisely their stated scopes. DGKX standard-family comparisons remain historical source context and are not substituted for the OS45 cap/endpoint argument.',
'in_compendium_only_because':
'The complete original-reference ordinary-cap return requires the actual24-point source cover, full integral period/cochain and Lie maps, protected proper-disc family, prescribed fan and directed endpoint. Those arguments remain printed; general elliptic/Mumford construction inputs receive direct source credit.'
}
assessment={k:row[k] for k in ['confidence_state','confidence_line','independent_routes']}
assessment.update({
 'completion_state':'done',
 'format_check':'PASS: fixed-C_* statement, exact dependency uses and current code/scope paragraphs are integrated. Root accepted the whole-before-receiving reconstruction and complete comparison; the earlier format field\'s stale pending-prereading sentence is superseded by that exact accepted receipt.',
 'layout_check':'Fresh current build27 visual PASS on pages1278,1279,1280,1291,1295,1297,1304, exact PDF SHA367ba8d90cd717dec33980ca8cd85ac2f590d375b890e65eb81ebea8471b2f8c. Receipt audit_sign/K119_build27_visual_QA_08.json records every image hash. This is the stated seven-page sample, not an every-page inspection.',
 'remaining_risk':'No K119 row-specific mathematical/source/format/sampled-layout gate remains after accepting this exact consolidation. K116/K10 source/filling/sphere, K78 invariant-stalk and F35 prescribed-fan morphisms remain established inputs at their documented scopes. The historical49-source credit event is retained; its absent detailed files are not claimed reopened. No new global novelty assertion or additional model-family independence is inferred.'})
receipts=[W/'audit_corrections/K119_before_receiving_freeze_07.json',
          W/'audit_corrections/K119_receiving_receipt_07.json',
          W/'audit_corrections/K119_receiving_comparison_07.md',
          W/'audit_paper_i/iv_os45/K119_REVIEW.md',
          W/'audit_corrections/IV_literature_comparison_report.md',
          H/'K119_build27_visual_QA_08.json',H/'K119_source_openings_08.json']
out={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'label':'night:P3K.119','reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; same family',
 'scope':'Narrow source-credit/current-layout consolidation requested by root. Root has accepted the complete before-receiving derivation, all four receiving proofs and both139/88 programs. This branch does not award a new whole mathematical re-proof by joining those receipts.',
 'historical_archive_presence':archive_scope,'retained_historical_credit_event':historic,
 'current_source_review_scope':'Current IV primary report has direct F35 input credit, not a separate K119 literature theorem comparison. Fresh positive-source openings are itemized. The historical bounded K119 event is preserved rather than replaced by generic corpus metadata.',
 'evidence':[{'file':str(p),'sha256':sha(p)} for p in receipts],
 'guarded_source_updates':[{'field':k,'old_value':row.get(k,''),'new_value':v} for k,v in updates.items()],
 'assessment_before':{k:row.get(k,'') for k in assessment},'assessment_proposal':assessment,
 'integration_rule':'Root/canonical owner accepts and applies exact field guards. No shared inventory, body or canonical assessment was edited by this script.'}
(H/'K119_source_layout_consolidation_08.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# K119: final source-credit and current-layout consolidation','',out['scope'],'',
       '## Source provenance','',updates['credited_to'],'',updates['literature_searches'],'',
       '## Exact transport','',updates['credit_transport'],'',
       '## Disposition','',updates['source_credit_verdict'],'',updates['literature_disposition'],'',
       '## Current layout','',assessment['layout_check'],'',
       '## Final proposal','',
       'Recommend canonical completion `done` at the accepted whole-proof, computation, source-application and seven-page visual scopes. Preserve the exact prereading exposure qualification and all imported dependency limits. The absence of the historical detailed search files is disclosed; their explicit existing event retains its recorded bounded credit. No source or body edits were made by this branch.','']
(H/'K119_source_layout_consolidation_08.md').write_text('\n'.join(lines))
print(json.dumps({'proposal_sha256':sha(H/'K119_source_layout_consolidation_08.json'),
                  'opened_sources_sha256':sha(H/'K119_source_openings_08.json'),
                  'layout_sha256':sha(H/'K119_build27_visual_QA_08.json')},indent=2))
