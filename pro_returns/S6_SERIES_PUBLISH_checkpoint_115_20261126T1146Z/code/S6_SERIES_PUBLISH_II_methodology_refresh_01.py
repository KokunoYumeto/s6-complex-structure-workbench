#!/usr/bin/env python3
"""Refresh only the eight numeric Methodology fields from the exact current ledger."""
from pathlib import Path
import datetime as dt,difflib,hashlib,importlib.util,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as title_fingerprint
from S6_SERIES_PUBLISH_II_D10_census import fingerprint as apparatus_fingerprint
R=Path(__file__).resolve().parents[1];sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
builder=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_frontmatter_v1/S6_SERIES_PUBLISH_II_C2_frontmatter_build_v2.py';assert sha(builder.read_bytes())=='72fcff48aea18b8cb0b4faa3f2e77044b3fea482a07bd6041f70869a33dad985'
spec=importlib.util.spec_from_file_location('C_front_counts',builder);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
snapshot={n:(R/n).read_bytes() for n in ['S6_SERIES_PUBLISH_II.tex','CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_inventory.csv','S6_SERIES_PUBLISH_tags.tsv']};count=mod.census(snapshot);s=snapshot['S6_SERIES_PUBLISH_II.tex'].decode();a=s.index(r'\subsection{Methodology}');b=s.index(r'\subsection{How the paper is organized}',a);old=s[a:b];new=old;changes=[];t=count['by_type']
fields=[(r'(?<=The records associate )[\d,]+(?= entries)',count['statement_linked_rows']),(r'[\d,]+(?= examinations of proof steps)',t['targeted proof check']),(r'[\d,]+(?= independent\nre-derivations)',t['independent re-proof']),(r'[\d,]+(?= computations or formal certificates)',t['computation or formal certificate']),(r'[\d,]+(?= readings of proofs and applications)',t['used and rechecked in this run']),(r'[\d,]+(?= uses of\nbackground results)',t['carried as background without fault found']),(r'[\d,]+(?= refutation\nrecords)',t['refuted, with the refined statement\'s id']),(r'(?<=These entries belong to )[\d,]+(?= recorded groups)',count['statement_linked_unique_evidence_groups'])]
for pat,value in fields:
 matches=list(re.finditer(pat,new));assert len(matches)==1,pat;m=matches[0];replacement=f'{value:,}'
 if m.group()!=replacement:changes.append(dict(pattern=pat,old=m.group(),new=replacement));new=new[:m.start()]+replacement+new[m.end():]
if not changes:
 print(json.dumps({'status':'already current','source_sha256':sha(snapshot['S6_SERIES_PUBLISH_II.tex']),'counts':count},indent=2));raise SystemExit(0)
result=s[:a]+new+s[b:];assert title_fingerprint(s)==title_fingerprint(result) and apparatus_fingerprint(s)==apparatus_fingerprint(result)
now=dt.datetime.now(dt.timezone.utc);stamp=now.strftime('%Y%m%dT%H%M%SZ');O=R/'records'/('S6_SERIES_PUBLISH_II_methodology_refresh_'+stamp);O.mkdir()
(O/'census.json').write_bytes(enc(count));(O/'exact_numeric_changes.json').write_bytes(enc(changes));(O/'source.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='Methodology before',tofile='Methodology current')))
for n,v in snapshot.items():assert (R/n).read_bytes()==v
manifest=dict(created_utc=now.isoformat(),source_before_sha256=sha(snapshot['S6_SERIES_PUBLISH_II.tex']),source_after_sha256=sha(result.encode()),numeric_fields_changed=len(changes),ledger_sha256=sha(snapshot['CHECK_EVENTS.tsv']),ledger_rows=count['series_ledger_rows'],II_associations=count['statement_linked_rows'],II_groups=count['statement_linked_unique_evidence_groups'],counts=count['by_type'],all_noncount_prose_unchanged=True,D10_and_D16_projections_unchanged=True,mathematical_events_added=0,required_rows_closed=0,global_class_credit=0,page_reading_credit=0,evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
(O/'manifest.json').write_bytes(enc(manifest));(R/'S6_SERIES_PUBLISH_II.tex').write_text(result)
note=f"\n\nMethodology census refreshed at {now.isoformat()}: {count['statement_linked_rows']} Paper II associations in {count['statement_linked_unique_evidence_groups']} recorded groups from the {count['series_ledger_rows']}-row ledger. Only {len(changes)} numeric fields change; exact counts, source diff and input hashes are in `{O.relative_to(R)}/manifest.json`. No check, class or page credit is added.\n"
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','numeric_fields_changed','ledger_rows','II_associations','II_groups']},indent=2))
