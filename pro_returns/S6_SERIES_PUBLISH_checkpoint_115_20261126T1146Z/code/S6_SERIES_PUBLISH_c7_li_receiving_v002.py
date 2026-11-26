"""Add only LI's small printed permanent tag and update its exact guard."""
from pathlib import Path
from hashlib import sha256
import csv
import io

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_all_parity_receiving'
target=LANE/'S6_SERIES_PUBLISH_III_02LI_receiving.tex'
old=target.read_bytes()
assert sha256(old).hexdigest()=='8be58c84d60c456c27112fbd8c1813884dcc9efd069e7911fb45b577917b2238'
before='\\label{maps:src:D.2.41}\n'
after=before+'\\textnormal{\\small tag 02LI.}\n'
text=old.decode()
assert text.count(before)==1
new=text.replace(before,after,1)
assert new.replace(after,before,1)==text
guards=LANE/'S6_SERIES_PUBLISH_III_02LI_replacements.tsv'
with guards.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t')
    fields=reader.fieldnames
    rows=list(reader)
assert len(rows)==2 and rows[0]['new_text'].count(before)==1
rows[0]['new_text']=rows[0]['new_text'].replace(before,after,1)
assert new.rstrip('\n')=='\n\n'.join(r['new_text'].rstrip('\n') for r in rows)
buf=io.StringIO(newline='')
writer=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n')
writer.writeheader();writer.writerows(rows)
target.write_text(new,newline='\n')
guards.write_text(buf.getvalue(),newline='\n')
digest=sha256(target.read_bytes()).hexdigest()
print('Printed tag only; all498 prior mathematical lines unchanged.')
print('Receiver',len(new.splitlines()),'lines SHA256',digest)
print('Replacement guards SHA256',sha256(guards.read_bytes()).hexdigest())
note=LANE/'S6_SERIES_PUBLISH_III_02LI_comparison.md'
with note.open('a',newline='\n') as stream:
    stream.write('\nThe retained v002 source adds only the small printed tag02LI, with an exact\n'
                 'inverse string check and updated statement guard. All498 prior mathematical\n'
                 'lines are unchanged; the final receiver has499 lines, SHA256\n'+digest+'.\n'
                 'The complete bounded receiver review by the fresh author found no lost\n'
                 'hypothesis or map at the498-line stage; its exact scope is\n'
                 'agents/continuation7_iii_all_parity/S6_SERIES_PUBLISH_III_02LI_receiving_bounded_review.md.\n')
