#!/usr/bin/env python3
"""Apply one root-read complete-proof recap deletion and preserve prior bytes."""
from pathlib import Path
import argparse, csv, datetime, hashlib, io, json, os
R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--apply',action='store_true')
a=p.parse_args()
guard_path=O/'S6_SERIES_PUBLISH_I_candidate19_root_guards.json'
graw=guard_path.read_bytes()
assert sha(graw)=='c56a3f08d9f47d18b06c1e238d34467cb1a6991363bccbaf80e8cd68b21691a0'
doc=json.loads(graw);g=doc['guards'][0]
src=R/'S6_SERIES_PUBLISH_I.tex';oldraw=src.read_bytes();s=oldraw.decode()
assert sha(oldraw)==doc['source_sha256']=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
pdfraw=(R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf').read_bytes()
assert sha(pdfraw)==doc['pdf_sha256']=='e7a48c79d7bc5588f272b7d138f82fef8bbc504e86626f06a01c0bd86de32f7f'
ledger=R/'CHECK_EVENTS.tsv';ledgerraw=ledger.read_bytes()
assert sha(ledgerraw)=='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
log=R/'S6_SERIES_PUBLISH_defects_I.tsv';lograw=log.read_bytes()
assert sha(lograw)=='541ff9755885d8430a183befe6f9767509e7ab1ebc8aa0755d414cc842cd7030'
x=(R/g['original_full_block']).read_text();y=(R/g['proposed_full_block']).read_text()
assert sha(x.encode())==g['original_full_block_sha256']
assert sha(y.encode())==g['proposed_full_block_sha256']
old,new=g['old'],g['new']
assert old=='  This explicit comparison proves the assertion\nabout the compact-dual limit.' and new==''
assert not any(c in old for c in '\\${}')
assert s.count(x)==s.count(old)==1 and x.replace(old,new,1)==y
pos=s.index(old);after=s[:pos]+new+s[pos+len(old):]
assert after.count(y)==1 and after[:pos]+old+after[pos:]==s
assert s.replace(x,'COMPLETE_REVIEWED_BLOCK',1)==after.replace(y,'COMPLETE_REVIEWED_BLOCK',1)
reader=csv.DictReader(io.StringIO(lograw.decode(),newline=''),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==2217 and lograw.endswith(b'\r\n')
row={k:'' for k in fields}
row.update(change_id='I-02218',type=g['type'],statement_id=g['statement_id'],old_location='candidate19 source line '+str(s[:pos].count('\n')+1)+'; fam:src:F.3.2',old_page='66',new_location='fam:src:F.3.2',new_page='pending candidate20 build',old_text=old,new_text=new,reason=g['reason'],review_status='applied; root complete statement/proof rereading and exact deletion comparison; candidate20 changed-page reading pending',mapped_old_location='candidate19 Proposition10.9, page66',mapped_new_location='pending candidate20 build and reading',page_mapping_method='Exact candidate19 source/proof archive and actual whole-page66 reading; candidate19 source/PDF SHA bound by receipt')
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\r\n');w.writerow(row);newlog=lograw+buf.getvalue().encode()
assert list(csv.DictReader(io.StringIO(newlog.decode(),newline=''),delimiter='\t'))==rows+[row]
record={'paper':'I','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'applied' if a.apply else 'prepared only','before_source_sha256':sha(oldraw),'after_source_sha256':sha(after.encode()),'before_defect_log_sha256':sha(lograw),'after_defect_log_sha256':sha(newlog),'candidate19_pdf_sha256':sha(pdfraw),'check_ledger_sha256':sha(ledgerraw),'guard':{'path':str(guard_path.relative_to(R)),'sha256':sha(graw)},'changes':[{'change_id':'I-02218','guard_id':g['id'],'type':g['type'],'statement_id':g['statement_id'],'old':old,'new':new,'old_source_line':s[:pos].count('\n')+1,'candidate19_page':66,'reason':g['reason']}],'full_block_comparison':{'original':g['original_full_block'],'original_sha256':g['original_full_block_sha256'],'proposed':g['proposed_full_block'],'proposed_sha256':g['proposed_full_block_sha256']},'source_exact_forward_and_inverse_maps_verified':True,'all_source_outside_compared_block_byte_identical':True,'all_mathematical_segments_and_references_preserved':True,'prior_defect_log_bytes_preserved':len(lograw),'prior_defect_rows_preserved':len(rows),'total_defect_rows':len(rows)+1,'mathematical_events_added_by_operation':0,'pending':['Section4.3 actual rereading event append','Methodology count update','Candidate20 clean build and changed-image reading']}
name='S6_SERIES_PUBLISH_I_candidate19_recap_'+('apply_receipt' if a.apply else 'preparation')+'.json'
out=O/name;assert not out.exists()
if a.apply:
    assert src.read_bytes()==oldraw and log.read_bytes()==lograw and ledger.read_bytes()==ledgerraw
    for path,data in [(src,after.encode()),(log,newlog)]:
        staged=O/(path.name+'.recap.commit');assert not staged.exists();staged.write_bytes(data);os.replace(staged,path)
assert ledger.read_bytes()==ledgerraw
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'mode':record['mode'],'receipt':str(out.relative_to(R)),'receipt_sha256':sha(out.read_bytes()),'after_source_sha256':record['after_source_sha256'],'after_defect_log_sha256':record['after_defect_log_sha256'],'total_defect_rows':record['total_defect_rows']},indent=2))
