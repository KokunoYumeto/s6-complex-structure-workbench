#!/usr/bin/env python3
"""Bind all remaining active compendium calls without guessing absent targets."""
from pathlib import Path
import datetime as dt,hashlib,json,re
from S6_SERIES_PUBLISH_II_D10_census import mask_records
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_compendium_reference_audit_01'
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
assert not O.exists();s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();masked=mask_records(s);lo=s.index(r'\begin{document}');rows=[]
for h in re.finditer(r'\\CompendiumRef\{([^{}]+)\}\{([^{}]+)\}',masked[lo:]):
 a=lo+h.start();b=max(s.rfind('\n\n',0,a),lo);e=s.find('\n\n',a);e=len(s) if e<0 else e
 rows.append(dict(index=len(rows)+1,paper=h[1],historical_label=h[2],line=s.count('\n',0,a)+1,offset=a,command=h[0],complete_paragraph=s[b:e],current_literal_label_count=s.count('\\label{'+h[2]+'}') if h[1]=='II' else None))
assert len(rows)==15 and sum(x['paper']=='II' for x in rows)==10
assert all(x['current_literal_label_count']==0 for x in rows if x['paper']=='II')
p=R.parent/'S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_II.tex';old=p.read_text();blocks=[];O.mkdir()
for label,name in [('cdp:st:A.2.3','A23'),('cdp:st:C.2.NC.1','NC1'),('cdp:st:E2','E2')]:
 a=old.index('\\label{'+label+'}');a=old.rfind(r'\begin{proposition}',0,a);b=old.index(r'\end{proof}',a)+len(r'\end{proof}');body=old[a:b];q=O/(name+'_complete_original.tex');q.write_text(body)
 blocks.append(dict(label=label,path=str(q.relative_to(R)),bytes=len(body.encode()),sha256=sha(body.encode()),complete_root_original_reading=True))
receipt=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),current_source_sha256=sha(s.encode()),active_calls=rows,II_old_complete_blocks=blocks,attached_II_compendium_sha256=sha(p.read_bytes()),exact_metadata_finding='All three same-paper labels are inventory dispositions without literal source labels or targets. The five Paper I calls use three historical targets also absent from the current I label metadata. No identity transport was admitted.',root_current_readings=['All15 complete active-call paragraphs','Complete P4.6 statement and proof: it proves e(F)=triple points under b2=0, and is not used as an identity replacement for the general nearby-fibre formula.','Complete E17 statement/proof and the complete following nonholomorphic-proof audit.'],pending=['A2.3: source-relative residue module J^-1 and the Granger-Schulze normal-crossing criterion; restore exact cited-result identity at its orphan introduction.','NC1: exact proper oriented-boundary construction and branch-permutation transport; primary A Campo scope must be checked.','E2: known LRS vanishing statement, every-component vector-bundle twist, and exact locations of the present E17 repair and graph construction.','PaperI03BS/03DK/03BO: only attached metadata examined; current I text/proofs remain closed.'],canonical_mutations=0,mathematical_events_added=0,required_rows_closed=0,global_classes_closed=0,final_page_credit=0)
(O/'audit.json').write_bytes(enc(receipt));print(json.dumps(dict(path=str((O/'audit.json').relative_to(R)),sha256=sha((O/'audit.json').read_bytes()),active_calls=15,unresolved=True),indent=2))
