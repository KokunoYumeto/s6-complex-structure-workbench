from pathlib import Path
import csv,datetime,difflib,hashlib,io,json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex';before=p.read_bytes();s=before.decode()
old=next(l for l in s.splitlines() if l.startswith('Binary-cubic exterior-product discriminant'))
assert old.endswith('} \\[3pt]') and not old.endswith('} \\\\[3pt]')
new=old[:-len('\\[3pt]')]+'\\\\[3pt]'
assert s.count(old)==1
after=s.replace(old,new,1).encode()
d=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=d.read_bytes()
reader=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');rows=list(reader)
row=dict(change_id='II-C2-BF-PROGRAM-ROW-REPAIR-01',type='D23',statement_id='cdp:st:A.5.5',
 old_location='Programs',old_page='',new_location='Programs',new_page='pending integrated PDF',
 old_text=old,new_text=new,reason='Correct root integration escape error: the proposed TeX row terminator was reduced to one backslash; restore the required two. Mathematical text and program paths unchanged.',
 review_status='Literal code-point inspection and exact row-terminator check')
assert row['change_id'] not in {x['change_id'] for x in rows}
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=reader.fieldnames,delimiter='\t',lineterminator='\n');w.writerow(row)
p.write_bytes(after)
with d.open('a') as f:f.write(out.getvalue())
assert new.endswith('} \\\\[3pt]') and p.read_text().count(new)==1
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(after),
 defect_before_sha256=sha(db),defect_after_sha256=sha(d.read_bytes()),appended_defect_row=row,
 source_diff=''.join(difflib.unified_diff(before.decode().splitlines(True),after.decode().splitlines(True),fromfile=p.name+'.before',tofile=p.name+'.after')),
 mathematical_events_added=0,required_row_status_changes=0,page_reading_credit=0)
rp=R/'records/S6_SERIES_PUBLISH_II_BF_program_row_repair.json';assert not rp.exists();rp.write_text(json.dumps(record,indent=2)+'\n')
note='\n\n### Paper II Programs row integration correction\n\nThe continuation reviewer detected a single-backslash row ending introduced by the root admission code in the new BF Programs entry. Literal inspection confirmed it. The two-backslash TeX row terminator is restored and the exact source diff and appended D23 row are recorded in `records/S6_SERIES_PUBLISH_II_BF_program_row_repair.json`. No mathematical assertion, program path, event or required-check status changed. The preparation record\'s claim about decoding the row terminator was inaccurate; the command escapes and the row ending require separate handling.\n'
for fn in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
 with (R/fn).open('a') as f:f.write(note)
print(json.dumps({k:v for k,v in record.items() if k.endswith('sha256')},indent=2))
