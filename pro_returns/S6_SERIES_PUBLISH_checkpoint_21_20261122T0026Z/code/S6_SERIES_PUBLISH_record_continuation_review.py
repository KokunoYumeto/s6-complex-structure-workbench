"""Append one already completed hourly review to the canonical ledger/report."""
from pathlib import Path
import datetime,hashlib,json,sys
R=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);assert n>=8
p=R/f'records/S6_SERIES_PUBLISH_progress_review_{n:02d}.json';d=json.loads(p.read_text())
insert=R/f'agents/continuation_infra/S6_SERIES_PUBLISH_progress_review_{n:02d}_insert.md'
text=insert.read_text();header=f'## Progress review {n:02d} —';assert header in text
sha=lambda b:hashlib.sha256(b).hexdigest()
before={};after={}
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 q=R/name;raw=q.read_bytes();assert header.encode() not in raw;before[name]=sha(raw)
 q.write_bytes(raw+text.encode());after[name]=sha(q.read_bytes())
out=R/f'records/S6_SERIES_PUBLISH_progress_review_{n:02d}_recording.json';assert not out.exists()
out.write_text(json.dumps(dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),review=n,before_sha256=before,after_sha256=after,insert_sha256=sha(insert.read_bytes()),mathematical_events_added=0,page_reading_credit_added_by_recording=0,mandatory_stop=d['mandatory_stop']),indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes()),newly_done=len(d['newly_done_rows']),mandatory_stop=d['mandatory_stop'])))
