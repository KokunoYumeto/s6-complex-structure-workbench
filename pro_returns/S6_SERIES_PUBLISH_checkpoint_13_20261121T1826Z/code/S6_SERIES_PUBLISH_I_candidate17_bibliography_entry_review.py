#!/usr/bin/env python3
"""Bind the actually completed ten-entry read to immutable prepared proposals."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
prep=OUT/'S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_preparation.json'
d=json.loads(prep.read_text())
for rel,h in d['protected_files_sha256'].items():assert sha((ROOT/rel).read_bytes())==h
assert len(d['rows'])==10 and len(d['guards'])==9
checks=[]
for r in d['rows']:
    assert sha((ROOT/r['original_path']).read_bytes())==r['original_entry_sha256']
    assert sha((ROOT/r['proposed_path']).read_bytes())==r['proposed_entry_sha256']
    checks.append({'key':r['key'],'original_entry_sha256':r['original_entry_sha256'],
                   'proposed_entry_sha256':r['proposed_entry_sha256'],
                   'complete_original_entry_read':True,'complete_proposed_entry_read':True,
                   'exact_field_changes_read':True,'field_changes':r['field_changes'],
                   'finding':'The proposed fields agree with the recorded primary metadata and established edition. Existing bibliography identifiers, authors, cited-edition notes and stated publication years remain.'})
receipt={'paper':'I','candidate':17,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'source_sha256':d['source_sha256'],'pdf_sha256':d['pdf_sha256'],
         'prepared_evidence_path':str(prep.relative_to(ROOT)),'prepared_evidence_sha256':sha(prep.read_bytes()),
         'review_scope':'All ten complete original and proposed bibliography entries, their exact field changes, seven primary DOI records, three bounded no-DOI dispositions, cited-edition records and the four title/pagination images were read. The previously saved preparation remains immutable.',
         'entries':checks,'all_ten_entries_reviewed':True,
         'raw_dollar_parser_qualification':'The raw whole-file dollar regex crosses bibliography entry boundaries. Its three mismatches are preserved in the preparation. Actual preservation is established by byte-identical entire body, exact outside-entry reconstruction and identical mathematical segments in every complete edited entry.',
         'source_modified':False,'log_modified':False,'mathematical_events_added':0,'additional_paper_I_page_credit':0,
         'root_approval':'pending'}
rp=OUT/'S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_review_receipt.json'
assert not rp.exists();rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
for r in d['rows']:r['complete_original_and_proposed_entries_reviewed']=True
d['preparation_snapshot']={'path':str(prep.relative_to(ROOT)),'sha256':sha(prep.read_bytes())}
d['entry_review_receipt']={'path':str(rp.relative_to(ROOT)),'sha256':sha(rp.read_bytes())}
d['status']='Nine exact full-entry proposals reviewed by preparing reader; canonical application pending root approval and infrastructure consolidation.'
fp=OUT/'S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_guards.json'
assert not fp.exists();fp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
mp=OUT/'S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_review.md'
assert not mp.exists();mp.write_text('# Paper I — candidate 17 bibliography entry review\n\n'
    'All ten complete original and proposed entries have been read. Nine exact proposals are ready for infrastructure consolidation and root approval: seven published DOI additions, one exact-edition URL addition, and two French accents in one journal title. The DOI entries for Nguyen and Shin also pin the established arXiv editions; Nguyen gains the publisher issue field. The theta note remains unchanged after viewing its seven-page pagination and trailing blank.\n\n'
    'The exact original/proposed entry files, primary-source evidence, raw Crossref metadata and hashes are bound by the reviewed guard JSON and review receipt. The body is byte-identical, every complete entry retains its mathematical segments, and the exact inverse reconstructs the frozen source. The preparation preserves the observed whole-file dollar-regex boundary limitation rather than claiming that check passed.\n\n'
    'Canonical source, defect log, check ledger, completed page readings, source dossier and prose guard JSON remain unchanged. No mathematical event or Paper I page-reading credit is added.\n')
for rel,h in d['protected_files_sha256'].items():assert sha((ROOT/rel).read_bytes())==h
print(json.dumps({'guards_path':str(fp.relative_to(ROOT)),'guards_sha256':sha(fp.read_bytes()),
                 'review_receipt_path':str(rp.relative_to(ROOT)),'review_receipt_sha256':sha(rp.read_bytes()),
                 'preparation_sha256':sha(prep.read_bytes()),'guard_count':9,'source_modified':False},indent=2))
