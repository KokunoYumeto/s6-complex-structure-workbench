"""Apply reviewed exact TeX guards and append their literal defect records.

The guard owns the manual contextual review. This program verifies exact
transport and identities; it performs no mathematical or visual review.
"""
from pathlib import Path
import argparse, collections, csv, datetime, hashlib, io, json, re

ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('guard',type=Path)
    parser.add_argument('--receipt',type=Path,required=True)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    guard_path=args.guard.resolve(); g=json.loads(guard_path.read_text())
    paper=g['paper'];assert paper in {'I','II','III','IV','V'}
    source=ROOT/f'S6_SERIES_PUBLISH_{paper}.tex'
    before=source.read_bytes();assert sha(before)==g['source_before_sha256']
    original=before.decode();text=original;changes=[]
    for n,patch in enumerate(g['patches'],1):
        old,new=patch['old'],patch['new']
        assert old and old!=new
        assert text.count(old)==1,(n,patch['statement_id'],text.count(old))
        i=text.index(old)
        changes.append(dict(patch,offset=i,intermediate_source_line=text[:i].count('\n')+1))
        text=text[:i]+new+text[i+len(old):]
    inverse=text
    for c in reversed(changes):
        i=c['offset'];assert inverse[i:i+len(c['new'])]==c['new']
        inverse=inverse[:i]+c['old']+inverse[i+len(c['new']):]
    assert inverse==original
    identities={}
    for kind,pattern in [('labels',r'\\label\{([^}]+)\}'),('targets',r'\\hypertarget\{([^}]+)\}')]:
        b=re.findall(pattern,original);a=re.findall(pattern,text)
        added=g.get('added_'+kind,[])
        assert len(added)==len(set(added))
        assert not set(added)&set(b)
        assert collections.Counter(a)==collections.Counter(b)+collections.Counter(added)
        assert [x for x in a if x not in set(added)]==b
        identities[kind]=dict(before=len(b),after=len(a),added=added,original_sequence_preserved=True)
    # Explicitly protect all unedited statement/proof bytes via the complete
    # forward/inverse literal map. No interpretation of wording is automated.
    log=ROOT/f'S6_SERIES_PUBLISH_defects_{paper}.tsv';oldlog=log.read_bytes()
    reader=csv.DictReader(io.StringIO(oldlog.decode()),delimiter='\t');fields=reader.fieldnames;oldrows=list(reader)
    assert oldlog.endswith(b'\n')
    newrows=[]
    for i,c in enumerate(changes,len(oldrows)+1):
        cid=f'{paper}-{i:05d}';c['change_id']=cid
        row={field:'' for field in fields}
        row.update(change_id=cid,type=c['type'],statement_id=c['statement_id'],
                   old_location=f"source {g['source_before_sha256']} literal guard {i-len(oldrows)}",
                   old_page=c.get('old_page','pending source-bound mapping'),
                   new_location=c['statement_id'],new_page='pending final build',
                   old_text=c['old'],new_text=c['new'],reason=c['reason'],
                   review_status='applied; final page review pending')
        newrows.append(row)
    buf=io.StringIO();writer=csv.DictWriter(buf,fieldnames=fields,delimiter='\t');writer.writerows(newrows)
    newlog=oldlog+buf.getvalue().encode();assert newlog.startswith(oldlog)
    record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),paper=paper,
                guard={'path':str(guard_path.relative_to(ROOT)),'sha256':sha(guard_path.read_bytes())},
                source_before_sha256=sha(before),source_after_sha256=sha(text.encode()),
                defects_before_sha256=sha(oldlog),defects_after_sha256=sha(newlog),
                old_defect_rows=len(oldrows),new_defect_rows=len(newrows),
                exact_forward_and_inverse_maps_verified=True,old_log_byte_prefix_preserved=True,
                identities=identities,changes=changes,applied=args.apply,
                mathematical_events_added=0,visual_reading_credit=0)
    out=args.receipt.resolve();assert not out.exists();out.parent.mkdir(parents=True,exist_ok=True)
    if args.apply:
        assert source.read_bytes()==before and log.read_bytes()==oldlog
        source.write_text(text);log.write_bytes(newlog)
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['changes','identities']},indent=2))

if __name__=='__main__':main()
