from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

root=Path(__file__).resolve().parents[1]
folder=root/'agents/continuation6_iii_root'
tag='03BC';label='wb:h24:ret:framing-proposition'
prefix=f'S6_SERIES_PUBLISH_III_{tag}'
source=root/'S6_SERIES_PUBLISH_III.tex'
raw=source.read_bytes()
assert sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old='\n'.join(raw.decode().splitlines()[29306:29352])
new=(folder/(prefix+'_receiving.tex')).read_text().rstrip('\n')
assert raw.decode().count(old)==1
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
    assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new))

def write(name,fields,rows):
    stream=io.StringIO(newline='')
    w=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
    (folder/(prefix+name)).write_text(stream.getvalue(),newline='\n')

write('_replacements.tsv',['statement_id','old_text','new_text'],[{'statement_id':label,'old_text':old,'new_text':new}])
defect_fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
defects=[]
for suffix,typ,ot,nt,reason in [
 ('header','D10',r'\StatementRecord{wb:h24:ret:framing-proposition}{proved}{03BC}{\SeriesRef{wb:h24:ret:eq:sign}, \SeriesRef{wb:h24:ret:eq:full-frame}, \SeriesRef{wb:h24:ret:eq:D-homotopy}}','','Remove the machine record; preserve every label and tag.'),
 ('title','D16',r'\begin{proposition}\hypertarget{tag-03BC}{}',r'\begin{proposition}[Stable framing of the cusp torus]','Give the proposition a mathematical title.'),
 ('proof','D02',old,new,'Write the explicit stable bundle and inverse maps, constant-matrix paths, both ambient orientation components and the torus reflection. Remove the closing defensive contrast; the retained-angle theorem keeps its own unique order-two evaluation.')]:
    row=dict.fromkeys(defect_fields,'')
    row.update(change_id='c6-III-03BC-'+suffix,type=typ,statement_id=label,
               old_location='S6_SERIES_PUBLISH_III.tex:29307--29352',
               new_location=str((folder/(prefix+'_receiving.tex')).relative_to(root)),
               old_text=ot,new_text=nt,reason=reason,
               review_status='complete comparison; root admission and source/page application pending')
    defects.append(row)
write('_defects.tsv',defect_fields,defects)
with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
    fields=csv.DictReader(f,delimiter='\t').fieldnames
event=dict.fromkeys(fields,'');now=datetime.now(timezone.utc).isoformat()
event.update(statement_id=label,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, sixth continuation root',
             type='targeted proof check',event_id='publish:c6:III:03BC:targeted',
             phase='fresh derivation followed by exact original/receiving comparison',
             source_file=source.name,source_row='29307',source_event_type='targeted proof check',
             evidence_group='publish:c6:III:03BC:targeted',
             publish_input_file=str((folder/(prefix+'_CHECK_EVENTS.tsv')).relative_to(root)),publish_input_row='2',date_utc=now,
             where='; '.join(str((folder/(prefix+s)).relative_to(root)) for s in ('_fresh_derivation.md','_comparison.md','_replacements.tsv')),
             outcome='Derived the stable tangent comparison from its disclosed full-frame, normal-coordinate and admitted orientation inputs before reading the original proposition proof. Explicit normal-quotient inverse, rational SU(2) contraction, realification and positive constant paths verified; all 22 exact symbolic checks pass. Full original comparison retained its arbitrary sphere-orientation branch via F R_sigma and constant reflection. This completes an unstated orientation branch of the fresh argument; the original proof was correct. No refutation; no credit for the separately associated later proof or already admitted dependencies. One titled proposition and one proof prepared, all original identifiers retained.')
write('_CHECK_EVENTS.tsv',fields,[event])
out=f'Prepared exact 03BC guard, receiver, three defect rows and one targeted event at {now}.\n'
Path(__file__).with_suffix('.out').write_text(out,newline='\n')
print(out,end='')
