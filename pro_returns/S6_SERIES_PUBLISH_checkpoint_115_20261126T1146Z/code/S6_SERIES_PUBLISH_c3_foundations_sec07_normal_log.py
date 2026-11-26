from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec07'
PREFIX = 'S6_SERIES_PUBLISH_sec07_normal'
path=OUT/(PREFIX+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
    row['review_status']='Complete original and receiving statement/proof read and compared; exact Catanese source application checked; integration pending.'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
evidence='publish:c3:foundations:sec07:normal-support'
event=dict.fromkeys(event_fields,'')
event.update(statement_id='cdp:st:C.2.UN.5',date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome='Read the complete 181-line original block and complete 168-line receiving subsection, including every proof item. Preserved the isolated-sphere obstruction, normalized root-cover maps w^m=u and s=wz, connected central cover, free deck action, affine and product-isogeny maps, canonical character orders 2/3/4/6, all torus and bielliptic multiplicities and compact quotient construction. Replaced only the known torus-deformation/Albanese re-proof by the exact Catanese Theorem4.6 application. Opened arXiv:math/0111245v2 PDF, SHA2567f0c802148fad516463507da5ca8bf1b78d9cb4ef72550931948acea0c48a78b, p9 Definition3.1/Theorems3.2–3.3 and pp13–14 Theorem4.6/full proof; also read Proposition4.8 and proof pp14–15 and the corresponding attached TeX passages. Explicit map sends the proper family to A’s Kuranishi base and its noncentral parameters to torus points approaching0; the source’s period-integral Albanese map is the retained map. A first external web opener returned DisabledError; direct primary arXiv retrieval succeeded. Initial source helper lacked requests, was changed to urllib/pdftotext before successful retrieval. No independent proof/computation, required-check increment or final PDF reading is claimed.',event_id=evidence,phase='publication text and proof comparison',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group=evidence,date_utc=now,where='Normal irreducible supports; complete original/receiving proof comparison and exact opened primary source')
with (OUT/(PREFIX+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerow(event)
status=[]
for row in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done'
    basis='The complete receiving normal-support statement and proof were read against this defect class; every changed instance is logged and no remaining instance was found in this bounded subsection.'
    if row in ('D10','D16'):
        basis='Existing Paper II closure preserved; title and permanent tag remain and hidden statement apparatus stays hidden.'
    if row in ('D14','D24','restructuring'):
        state='open'
        basis='The complete normal-support text is prepared in its own subsection; admission, the following subsection boundary and full sec07 dependency order remain with the section integration. No movement credit from a new heading alone.'
    if row=='D23':
        basis='Source typography and references were read and repaired where needed; root owns the separate integrated typesetting and page-reading gates.'
    status.append(dict(unit='subsec:II:normal-irreducible-supports',row=row,status=state,basis=basis,fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_normal.tex'))
with (OUT/(PREFIX+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(status[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(status)
print('Normal-support proposal: 15 defect rows, one exposed reading event, 26 bounded status rows; all integration gates explicit.')
