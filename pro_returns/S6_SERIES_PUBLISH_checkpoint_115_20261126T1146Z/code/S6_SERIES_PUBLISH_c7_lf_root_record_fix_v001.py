"""Correct LF event typing and remove the prohibited redundant edit manifest.

Preserve the executed preparer and its actual output.  Prepare a separate
admission helper that treats deletion guards as containing no receiver block.
"""
from pathlib import Path
from hashlib import sha256
import csv
import io

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_three_primary_receiving'
events=LANE/'S6_SERIES_PUBLISH_III_02LF_CHECK_EVENTS.tsv'
raw=events.read_bytes()
assert sha256(raw).hexdigest()=='dd8ea645fff55f1259ce081b70e41f684ad43568dd808b24d6a530f385289e45'
reader=csv.DictReader(io.StringIO(raw.decode()),delimiter='\t')
fields=reader.fieldnames
rows=list(reader)
row=next(r for r in rows if r['event_id']=='publish:c7:III:02LF:targeted')
assert row['type']==row['source_event_type']=='targeted proof check'
row['type']=row['source_event_type']='used and rechecked in this run'
row['outcome']+=' Root corrected this event to post-exposure rereading of the completed replacement; the earlier attributed fresh event carries the targeted derivation credit.'
buf=io.StringIO(newline='')
w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n')
w.writeheader(); w.writerows(rows)
events.write_text(buf.getvalue(),newline='\n')
print('Final LF rereading event typed used and rechecked; other seven event types unchanged.')
print('EVENTS_SHA256',sha256(events.read_bytes()).hexdigest())

redundant=LANE/'S6_SERIES_PUBLISH_III_02LF_packet_manifest_v001.json'
assert sha256(redundant.read_bytes()).hexdigest()=='133be993a3669086ef22dd6db227ff452e722c695df89735d82d1df44e862a45'
redundant.unlink()
print('Removed',redundant.relative_to(ROOT),'under prompt Section0.5: redundant edit manifest. Authoritative defects/events/replacement guards and actual source/output history remain.')

base=ROOT/'code/S6_SERIES_PUBLISH_c7_admit.py'
helper=ROOT/'code/S6_SERIES_PUBLISH_c7_admit_with_deletions.py'
assert not helper.exists()
old=base.read_text()
before="'\\n\\n'.join(g['new_text'].rstrip('\\n') for g in guards)"
after="'\\n\\n'.join(g['new_text'].rstrip('\\n') for g in guards if g['new_text'])"
assert old.count(before)==1
new=old.replace(before,after,1)
assert new.replace(after,before,1)==old
helper.write_text(new,newline='\n')
print('Separate admission helper',helper.relative_to(ROOT),'SHA256',sha256(helper.read_bytes()).hexdigest())
print('The only helper change omits empty deletion blocks from receiver concatenation; all exact old strings, hashes, identities and chronology checks remain.')
