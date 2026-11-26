"""Seal batch05 exact editorial evidence; never mutate canonical files."""
from pathlib import Path
import collections,csv,datetime,hashlib,json,shutil

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_working'
FINAL=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_final_v1'
P='S6_SERIES_PUBLISH_II_A2_D09_D04_batch05'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda x:hashlib.sha256(x).hexdigest()
def dump(name,value):
    (WORK/(P+'_'+name+'.json')).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def hashes():
    return {n:sha((ROOT/n).read_bytes()) for n in ['S6_SERIES_PUBLISH_II.tex','CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_inventory.csv','S6_SERIES_PUBLISH_tags.tsv']}
assert not FINAL.exists(),'Immutable final path already exists.'
start=hashes();s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
guards=json.loads((WORK/(P+'_guards.json')).read_text())
inverse=json.loads((WORK/(P+'_inverse_guards.json')).read_text())
pres=json.loads((WORK/(P+'_preservation.json')).read_text())
verify=json.loads((WORK/(P+'_verification.json')).read_text())
c=s
for g in guards:
    assert c.count(g['old'])==1,g['id'];c=c.replace(g['old'],g['new'])
for g in inverse:
    assert c.count(g['old'])==1,g['id'];c=c.replace(g['old'],g['new'])
assert c==s
for r in pres:
    for suffix in ['before','after']:
        p=WORK/f"S6_SERIES_PUBLISH_II_A2_{r['tag']}_{suffix}.tex"
        assert sha(p.read_bytes())==r[suffix+'_sha256']
    assert s.count((WORK/f"S6_SERIES_PUBLISH_II_A2_{r['tag']}_before.tex").read_text())==1
assert sum(r['original_item_tokens'] for r in pres)==52
assert sum(r['original_bracket_displays'] for r in pres)==91
assert sum(r['additional_bracket_displays'] for r in pres)==6

successful=[];failed=[]
for name in ['S6_SERIES_PUBLISH_II_A2_batch05_program_retrieval.json','S6_SERIES_PUBLISH_II_A2_batch05_program_retrieval_extension.json']:
    p=WORK/name;j=json.loads(p.read_text())
    for row in j['files']:
        if row.get('http_status')==200:
            f=Path(row['temporary_path']);assert sha(f.read_bytes())==row['sha256']
            row.update(read_scope='Complete historical source or saved output text actually read.',line_count=len(f.read_text().splitlines()),executed=False)
            successful.append(row)
        else:failed.append(row)
    j.update(full_reading_recorded_utc=now,historical_executions_this_batch=0,
             download_disposition='All downloaded bodies remain outside current and are excluded from the packet.')
    p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
assert len(successful)==16 and len(failed)==1

support=[]
paths=list(WORK.glob('S6_SERIES_PUBLISH_II_A2_batch05_support_*.tex'))
paths += [WORK/'S6_SERIES_PUBLISH_II_A2_02WH_before.tex',
          WORK/'S6_SERIES_PUBLISH_II_A2_033O_before.tex',WORK/'S6_SERIES_PUBLISH_II_A2_033P_before.tex']
for p in sorted(paths):support.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,
    sha256=sha(p.read_bytes()),complete_contents_read=True,changed_by_this_packet=False,new_events=0))
reading=dict(created_utc=now,scope='Complete exposed editorial comparison; no independent derivation or new mathematical computation event.',
    owners=[dict(owner=r['owner'],tag=r['tag'],before_sha256=r['before_sha256'],after_sha256=r['after_sha256'],
                 complete_original_and_final_read=True,complete_following_material_read=True,
                 identical_final_mathematical_block=r['before_sha256']==r['after_sha256']) for r in pres],
    actual_final_reading='Final BF and YC complete blocks read together; final B8 complete31,226-byte block read untruncated. YF/YE/WI final blocks are the identical bytes of their fully read originals.',
    supporting_complete_reads=support,historical_sources_fully_read=7,historical_stdout_fully_read=7,historical_json_fully_read=2,
    historical_executions_this_batch=0,new_mathematical_programs=0,
    failed_retrievals=failed,failed_retrieval_disposition='necessity_examples.json returned404. The complete source writes stdout only; the .out exists and was read. No computation failed.',
    structural_overlap_disposition='Original033O/033P and following paragraphs fully read, then reserved to C. After root admission, P208 and complete final E5.3 read; this packet changes only the existing Programs row scope. No duplicate source guard or event.',
    all_original_statements_identical=True,all_original_proof_steps_retained=True,
    equation_references_preserved=True,two_B8_program_sentence_equation_references_moved_unchanged_to_Programs=True,
    canonical_mutations=0,proposed_events=6,proposed_evidence_groups=1)
dump('reading_receipt',reading)
events=[]
for r in pres:
    events.append(dict(statement_id=r['owner'],date='2026-11-22',date_utc=now,
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort not separately exposed; S6_SERIES_PUBLISH continuation2, checker ii_checks_a2',
        type='used and rechecked in this run',event_id=f"ce:S6_SERIES_PUBLISH_II_A2_ED05_{r['tag']}_reread_20261122",
        evidence_group=P+'_20261122',source_file=str((FINAL/(P+'_comparison.md')).relative_to(ROOT)),
        where=r['tag']+' / '+r['owner'],event_count=1,
        outcome=f"Read the complete original/final statement and proof ({r['original_item_tokens']} original item tokens), together with all following material. Every statement and every original proof step/formula remains; BF/B8/YC mathematical following passages move into their owning proofs with all exact maps retained. Historical program sources and outputs are fully mapped at their actual scope. Two B8 program-sentence equation references are preserved in Programs. All guards/inverses replay. Six used rereads share one group; no independent derivation, mathematical repair, new computation event, required-row closure or page-reading credit."))
dump('event_proposals',dict(created_utc=now,canonical_events_added=0,events=events))
with (WORK/(P+'_defects.tsv')).open() as f:defects=list(csv.DictReader(f,delimiter='\t'))
dump('final_replay',dict(created_utc=now,source_snapshot_sha256=verify['source_snapshot_sha256'],
    current_source_verified_sha256=sha(s.encode()),exact_guards=len(guards),exact_inverses=len(inverse),
    all_guards_unique_and_replay_exact=True,canonical_hashes_before=start,canonical_hashes_after=hashes(),canonical_mutations_by_agent=0))
FINAL.mkdir()
for p in sorted(WORK.iterdir()):
    if p.is_file():shutil.copyfile(p,FINAL/p.name)
files=[]
for p in sorted(FINAL.iterdir()):files.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
for name in ['code/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_extract.py','code/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_prepare.py','code/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_seal.py','agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_E5_program_scope_01.json']:
    p=ROOT/name;files.append(dict(path=name,bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
index=dict(created_utc=now,status='Immutable bounded proposal for root admission; no canonical writes.',
    source_snapshot_sha256=verify['source_snapshot_sha256'],current_source_verified_sha256=sha(s.encode()),owners=pres,files=files,
    guard_count=13,owner_guard_count=6,Programs_guard_count=7,new_program_rows=1,amended_program_rows=6,
    new_historical_program_links=6,existing_historical_scope_expansions=1,defect_rows=len(defects),
    defect_rows_by_class=dict(collections.Counter(r['type'] for r in defects)),events_proposed=6,evidence_groups_proposed=1,
    new_independent_check_credit=0,required_row_movement=0,canonical_mutations=0,
    pending_scope='Fixed census residual after batch04, this packet and C\'s separate admitted E5 removals:39 D09 paragraphs in37contexts. No new whole-source closure census. The unchanged Reid credit paragraph afterBF remains pending for its owner/structure pass; root owns D10/D16/D19/builds.')
p=FINAL/(P+'_index.json');p.write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(index=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p.read_bytes()),bound_files=len(files),source_sha256=sha(s.encode()),guards=len(guards),defects=len(defects),events=6),indent=2))
