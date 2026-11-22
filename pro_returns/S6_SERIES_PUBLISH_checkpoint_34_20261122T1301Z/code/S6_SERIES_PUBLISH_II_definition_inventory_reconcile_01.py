from pathlib import Path
import csv,datetime as dt,hashlib,io,json

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def binding(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=sha(b),bytes=len(b))
p=R/'S6_SERIES_PUBLISH_inventory.csv';before=p.read_bytes()
reader=csv.DictReader(io.StringIO(before.decode(),newline=''));rows=list(reader);fields=reader.fieldnames
with (R/'S6_SERIES_PUBLISH_tags.tsv').open() as f:tags={r['tag']:r for r in csv.DictReader(f,delimiter='\t')}
with (R/'CHECK_EVENTS.tsv').open() as f:events=list(csv.DictReader(f,delimiter='\t'))
source=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();source_text=source.decode()
ledger=binding('CHECK_EVENTS.tsv');out='records/S6_SERIES_PUBLISH_II_definition_inventory_reconcile_01.json'
assert not (R/out).exists()
added=[];blocks=[]
for tag in ['P201','P202']:
 t=tags[tag];owner=t['current_owner']
 assert t['paper']=='II' and t['kind']=='definition'
 assert not any(r['tag']==tag or r['label']==owner for r in rows)
 assert not any(r['statement_id']==owner for r in events)
 loc=source_text.index('\\hypertarget{tag-'+tag+'}')
 start=source_text.rfind('\\begin{definition}',0,loc)
 end=source_text.index('\\end{definition}',loc)+len('\\end{definition}')
 block=source_text[start:end]
 assert '\\StatementRecord{'+owner+'}{proved}{'+tag+'}{}' in block
 blocks.append(dict(tag=tag,owner=owner,source_block_sha256=sha(block.encode()),source_block=block))
 r={k:'' for k in fields}
 r.update(paper='II',label=owner,source_run='S6_SERIES_PUBLISH',source_id=owner,kind='Definition',status=t['status'],
  main_or_supporting='supporting',source_main_or_supporting='supporting',source_paper='II',tag=tag,
  uses='' if tag=='P201' else 'fam:src:C.2.3',
  check_record=json.dumps(dict(canonical_check_events=[],current_ledger_sha256=ledger['sha256'])),
  notes='Existing numbered definition and permanent tag entered in the inventory after their omission was observed. Original creation receipt retained. No new theorem or check event.',
  check_summary='0 canonical event associations',confidence_line='Definition/convention record; no independent proof-check credit added.',
  placement_state='Existing frontmatter position retained.',writing_state='Existing source definition unchanged.',
  confidence_state='Original source-transport and supporting records retained.',completion_state='Final publication gate remains open.',
  format_check='Existing numbered definition and permanent tag '+tag+'.',layout_check='pending integrated PDF',
  remaining_risk='Final source graph, provenance and complete rendered-page review remain open.',assessment_source=out,
  literature_disposition='Existing hypotheses and marked conventions; no new literature assertion introduced.',
  current_source_sha256=sha(source),current_statement_owner=owner,
  publication_review_status='Root read both complete current definition blocks and original tag-creation receipt; inventory omission repaired.',
  current_number=t['number'],current_page=t['page'])
 added.append(r)
buff=io.StringIO(newline='');w=csv.DictWriter(buff,fieldnames=fields,lineterminator='\r\n');w.writerows(added)
append=buff.getvalue().encode();assert before.endswith(b'\n')
after=before+append
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 inventory_before_sha256=sha(before),inventory_after_sha256=sha(after),inventory_original_rows=len(rows),added_rows=added,
 source_sha256=sha(source),ledger=ledger,source_unchanged=True,ledger_unchanged=True,
 original_tag_creation=binding('records/S6_SERIES_PUBLISH_II_frontmatter_new_tags_receipt.json'),
 complete_definition_blocks_actually_read=blocks,old_inventory_byte_prefix_preserved=True,
 events_added=0,required_rows_completed=0,publication_page_credit=0,
 scope='Reconcile two existing Paper II numbered definitions with their existing permanent tags. No new mathematical statement, source change or evidence credit.')
(R/out).write_text(json.dumps(record,indent=2)+'\n')
p.write_bytes(after)
assert p.read_bytes()[:len(before)]==before
assert binding('CHECK_EVENTS.tsv')==ledger
assert (R/'S6_SERIES_PUBLISH_II.tex').read_bytes()==source
print(json.dumps(dict(record=binding(out),rows_added=2,inventory_sha256=sha(after))))
